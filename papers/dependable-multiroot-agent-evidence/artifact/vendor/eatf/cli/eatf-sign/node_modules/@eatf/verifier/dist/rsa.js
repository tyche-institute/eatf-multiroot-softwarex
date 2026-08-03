/**
 * v0.1: RSA-4096 signature verification via Web Crypto.
 *
 * EATF signs with PKCS#1 v1.5 over SHA-256. The Java reference uses
 * `Signature.getInstance("SHA256withRSA", "BC")` which is the same
 * scheme. Web Crypto exposes it as `RSASSA-PKCS1-v1_5` with hash
 * SHA-256.
 *
 * Public key arrives as PEM. We strip the headers, base64-decode the
 * SubjectPublicKeyInfo (SPKI), and import.
 */
const PEM_HEADERS = [
    /-----BEGIN PUBLIC KEY-----/,
    /-----END PUBLIC KEY-----/,
];
function pemToDer(pem) {
    let body = pem;
    for (const re of PEM_HEADERS)
        body = body.replace(re, "");
    body = body.replace(/\s+/g, "");
    if (!body)
        throw new Error("Empty PEM body.");
    // atob is available in both browsers and Node 20+.
    const raw = atob(body);
    const out = new Uint8Array(raw.length);
    for (let i = 0; i < raw.length; i++)
        out[i] = raw.charCodeAt(i);
    return out;
}
export async function importRsaPublicKey(pem) {
    const der = pemToDer(pem);
    // crypto.subtle.importKey expects an ArrayBuffer; pass the underlying buffer.
    return crypto.subtle.importKey("spki", der.buffer, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["verify"]);
}
export async function verifyRsa(key, signature, signedData) {
    return crypto.subtle.verify("RSASSA-PKCS1-v1_5", key, (signature instanceof Uint8Array ? signature.buffer.slice(signature.byteOffset, signature.byteOffset + signature.byteLength) : signature), (signedData instanceof Uint8Array ? signedData.buffer.slice(signedData.byteOffset, signedData.byteOffset + signedData.byteLength) : signedData));
}
/**
 * Java reference compatibility path.
 *
 * The backend signs DigestInfo(SHA-256, hash.sha256) with NONEwithRSA.
 * Some Web Crypto implementations expect the SHA-256 AlgorithmIdentifier to
 * include NULL parameters and reject the backend's BouncyCastle encoding. This
 * helper performs the public RSA operation directly, strips PKCS#1 v1.5
 * padding, and compares the trailing 32-byte digest.
 */
export function verifyRsaDigestInfo(publicKeyPem, signature, expectedDigest) {
    if (expectedDigest.length !== 32 || signature.length === 0)
        return false;
    const { modulus, exponent } = parseRsaSpki(pemToDer(publicKeyPem));
    const modulusBytes = Math.ceil(bitLength(modulus) / 8);
    if (signature.length !== modulusBytes)
        return false;
    const recovered = modPow(bytesToBigInt(signature), exponent, modulus);
    const encoded = bigIntToBytes(recovered, modulusBytes);
    if (encoded.length < 11 || encoded[0] !== 0x00 || encoded[1] !== 0x01) {
        return false;
    }
    let sep = -1;
    for (let i = 2; i < encoded.length; i++) {
        if (encoded[i] === 0x00) {
            sep = i;
            break;
        }
        if (encoded[i] !== 0xff) {
            return false;
        }
    }
    if (sep < 0)
        return false;
    const digestInfo = encoded.slice(sep + 1);
    if (digestInfo.length < expectedDigest.length)
        return false;
    const recoveredDigest = digestInfo.slice(digestInfo.length - expectedDigest.length);
    return constantTimeEqual(recoveredDigest, expectedDigest);
}
/**
 * Helper: decode a Base64-encoded signature (standard alphabet with
 * padding, as emitted by the Java reference) into raw bytes.
 */
export function decodeBase64(b64) {
    const cleaned = b64.replace(/\s+/g, "");
    const raw = atob(cleaned);
    const out = new Uint8Array(raw.length);
    for (let i = 0; i < raw.length; i++)
        out[i] = raw.charCodeAt(i);
    return out;
}
function parseRsaSpki(spki) {
    const c = { bytes: spki, offset: 0 };
    readSequence(c);
    skipAny(c); // AlgorithmIdentifier
    const bitString = readBitString(c);
    const r = { bytes: bitString, offset: 0 };
    readSequence(r);
    const modulus = bytesToBigInt(readInteger(r));
    const exponent = bytesToBigInt(readInteger(r));
    if (modulus <= 0n || exponent <= 0n)
        throw new Error("Invalid RSA public key.");
    return { modulus, exponent };
}
function readSequence(c) {
    return readTagAndLength(c, 0x30);
}
function readInteger(c) {
    const len = readTagAndLength(c, 0x02);
    let out = c.bytes.slice(c.offset, c.offset + len);
    c.offset += len;
    while (out.length > 1 && out[0] === 0x00)
        out = out.slice(1);
    return out;
}
function readBitString(c) {
    const len = readTagAndLength(c, 0x03);
    if (len < 1)
        throw new Error("Invalid BIT STRING.");
    const unusedBits = c.bytes[c.offset];
    if (unusedBits !== 0)
        throw new Error("Unsupported BIT STRING padding.");
    const out = c.bytes.slice(c.offset + 1, c.offset + len);
    c.offset += len;
    return out;
}
function skipAny(c) {
    if (c.offset >= c.bytes.length)
        throw new Error("Unexpected end of DER.");
    c.offset++;
    const len = readLength(c);
    c.offset += len;
    if (c.offset > c.bytes.length)
        throw new Error("DER length exceeds input.");
}
function readTagAndLength(c, expectedTag) {
    if (c.bytes[c.offset++] !== expectedTag) {
        throw new Error("Unexpected DER tag.");
    }
    return readLength(c);
}
function readLength(c) {
    const first = c.bytes[c.offset++];
    if ((first & 0x80) === 0)
        return first;
    const count = first & 0x7f;
    if (count === 0 || count > 4)
        throw new Error("Unsupported DER length.");
    let len = 0;
    for (let i = 0; i < count; i++) {
        len = (len << 8) | c.bytes[c.offset++];
    }
    if (c.offset + len > c.bytes.length)
        throw new Error("DER length exceeds input.");
    return len;
}
function bytesToBigInt(bytes) {
    let out = 0n;
    for (const b of bytes)
        out = (out << 8n) | BigInt(b);
    return out;
}
function bigIntToBytes(value, length) {
    const out = new Uint8Array(length);
    let current = value;
    for (let i = length - 1; i >= 0; i--) {
        out[i] = Number(current & 0xffn);
        current >>= 8n;
    }
    return out;
}
function bitLength(value) {
    return value.toString(2).length;
}
function modPow(base, exponent, modulus) {
    if (modulus === 1n)
        return 0n;
    let result = 1n;
    let b = base % modulus;
    let e = exponent;
    while (e > 0n) {
        if ((e & 1n) === 1n)
            result = (result * b) % modulus;
        e >>= 1n;
        b = (b * b) % modulus;
    }
    return result;
}
function constantTimeEqual(a, b) {
    if (a.length !== b.length)
        return false;
    let diff = 0;
    for (let i = 0; i < a.length; i++)
        diff |= a[i] ^ b[i];
    return diff === 0;
}
//# sourceMappingURL=rsa.js.map