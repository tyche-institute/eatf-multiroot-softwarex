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
export declare function importRsaPublicKey(pem: string): Promise<CryptoKey>;
export declare function verifyRsa(key: CryptoKey, signature: Uint8Array, signedData: Uint8Array): Promise<boolean>;
/**
 * Java reference compatibility path.
 *
 * The backend signs DigestInfo(SHA-256, hash.sha256) with NONEwithRSA.
 * Some Web Crypto implementations expect the SHA-256 AlgorithmIdentifier to
 * include NULL parameters and reject the backend's BouncyCastle encoding. This
 * helper performs the public RSA operation directly, strips PKCS#1 v1.5
 * padding, and compares the trailing 32-byte digest.
 */
export declare function verifyRsaDigestInfo(publicKeyPem: string, signature: Uint8Array, expectedDigest: Uint8Array): boolean;
/**
 * Helper: decode a Base64-encoded signature (standard alphabet with
 * padding, as emitted by the Java reference) into raw bytes.
 */
export declare function decodeBase64(b64: string): Uint8Array;
//# sourceMappingURL=rsa.d.ts.map