/**
 * Offline TypeScript signer for EATF .aep evidence packages.
 *
 * Mirrors the verifier in src/verifier.ts in reverse: given a payload,
 * an RSA keypair, OVERT receipt parameters, and an RFC 3161 timestamp
 * token, produces a v0.1-conformant .aep that the verifier in this
 * package will accept.
 *
 * Wire format documented in docs/aep-profile.md.
 *
 * Network policy: this module performs NO network I/O. The RFC 3161
 * timestamp token must be supplied by the caller — either fetched
 * out-of-band (via the eatf-sign CLI's --tsa-url flag) or copied from
 * an existing valid .aep package.
 *
 * Not yet implemented in this signer: ML-DSA-65 post-quantum signing.
 * Verifier already supports verifying packages that carry it
 * (entries signature_pqc.sig + pqc_public_key.pem); a future release
 * will extend this signer to emit them.
 */
export type SignerInput = {
    /** The payload bytes being attested (e.g. an LLM response). */
    payload: Uint8Array | string;
    /** PEM-encoded RSA private key for the issuer. */
    privateKeyPem: string;
    /** PEM-encoded RSA public key for the issuer (will be embedded as public_key.pem). */
    publicKeyPem: string;
    /**
     * Base metadata for the package. The signer fills in `created_at`
     * (if absent) and validates that the caller-supplied metadata is
     * consistent with the OVERT receipt it generates.
     */
    metadata: Record<string, unknown>;
    /**
     * OVERT scope identifier, e.g. "foundational:aep-response" or
     * "agentic-extended:mcp-tools-call".
     */
    overtScope: string;
    /** Free-form subject block placed into receipt.subject. */
    overtSubject?: Record<string, unknown>;
    /** Free-form event block placed into receipt.event (excluding timestamp). */
    overtEvent?: Record<string, unknown>;
    /**
     * Policy block placed into receipt.policy. The signer copies
     * policy_id/version/coverage/decision from metadata when not
     * explicitly supplied here.
     */
    overtPolicy?: Record<string, unknown>;
    /** Raw bytes of an RFC 3161 TimeStampResp covering this signature's canonical bytes (or any older valid token; verifier accepts both). */
    timestampTsr: Uint8Array;
    /** Optional issuer identifier ("EATF.eu" by default). */
    iap?: string;
};
export type SignerOutput = {
    /** The .aep package as a single Uint8Array. */
    aep: Uint8Array;
    /** SHA-256 hex of canonical.bin, useful for logging. */
    canonicalHashHex: string;
    /** Names of every ZIP entry written. */
    entries: string[];
};
/**
 * Sign a payload into a v0.1-conformant .aep package.
 *
 * Uses the "Java response-only" canonical form: canonical.bin equals
 * the payload bytes verbatim. This form is what the existing test
 * vectors (valid-overt-profile, mcp-tools-call-valid, ...) use.
 */
export declare function sign(input: SignerInput): Promise<SignerOutput>;
//# sourceMappingURL=signer.d.ts.map