/**
 * v0.1 — RFC 3161 timestamp parsing + verification.
 *
 * <p>This module parses a base64-encoded TimeStampToken via {@code pkijs}
 * and performs four independent checks:
 *
 * <ol>
 *   <li><b>tsaPresent</b> — the token is non-empty and parses as
 *       {@code ContentInfo} with the CMS SignedData OID
 *       ({@code 1.2.840.113549.1.7.2}).</li>
 *   <li><b>messageImprintMatches</b> — the {@code TSTInfo.messageImprint
 *       .hashedMessage} octet string equals {@code SHA-256(expectedHashHex
 *       as ASCII)}. The EATF AEP profile (see {@code docs/specs/aep
 *       -profile-v1.md} §7) hashes the lower-case hex string of the
 *       canonical SHA-256, not the canonical bytes themselves; this is
 *       the deliberate compatibility point with Java's
 *       {@code RealTsaServiceImpl}.</li>
 *   <li><b>signatureVerified</b> — the embedded
 *       {@code SignerInfo.signature} validates against the embedded
 *       signing certificate's public key over the
 *       {@code signedAttributes} (CMS RFC 5652 §5.4). This is the
 *       "internally consistent" check: the entity holding the
 *       certificate did sign this messageImprint at this genTime.</li>
 *   <li><b>genTime</b> — the {@code TSTInfo.genTime} timestamp, returned
 *       as a JavaScript {@code Date} for downstream policy. Not a check
 *       in itself; the caller decides whether to enforce a window.</li>
 * </ol>
 *
 * <p>Trust-anchor chain validation is a <em>separate</em> step exposed
 * by {@link verifyTsaTrust} so an operator can opt in / out
 * independently of the internal-consistency checks.
 *
 * <p>v0.1-alpha shipped a regex-over-hex heuristic for
 * messageImprintMatches and left signatureVerified always {@code null}.
 * This module replaces both with deterministic ASN.1 parsing and a
 * real Web Crypto signature verify.
 */
import type { TsaTrustResult } from "./tsa-trust-list.js";
export type TsaCheck = {
    /** Token is non-empty and parses as RFC 3161 ContentInfo + SignedData. */
    tsaPresent: boolean;
    /** Imprint inside the token equals SHA-256 of the expected hash hex. */
    messageImprintMatches: boolean | null;
    /** SignerInfo signature verifies against the embedded cert's public key. */
    signatureVerified: boolean | null;
    /** Hash algorithm OID inside the imprint (typically 2.16.840.1.101.3.4.2.1 for SHA-256). */
    imprintAlgorithmOid: string | null;
    /** TSTInfo.genTime, as a JavaScript Date. */
    genTime: Date | null;
    /** Number of certificates embedded in the SignedData.certificates field. */
    embeddedCertCount: number;
    /** Subject DN of the embedded signing cert (informational). */
    signerSubject: string | null;
    /** Issuer DN of the embedded signing cert (informational). */
    signerIssuer: string | null;
    /** Total bytes of the DER-decoded token. */
    rawSizeBytes: number;
    /** Human-readable note when a step short-circuits. */
    note?: string;
};
export declare function inspectTsa(timestampBase64: string, expectedHashHex: string): Promise<TsaCheck>;
/**
 * Cross-check the embedded signing cert chain against a pinned trust
 * list. This is independent of {@link inspectTsa}; an operator may
 * choose to require it (production) or skip it (dev / no trust anchors
 * pinned yet).
 *
 * <p>v0.2 does a minimal validation: the embedded signer's issuer DN
 * must match the subject DN of at least one provided trust-list root.
 * Full RFC 5280 path validation (NotBefore / NotAfter / KeyUsage /
 * EKU / Basic Constraints / CRL / OCSP) is v0.3 territory.
 *
 * @param check the result of {@link inspectTsa}
 * @param trustList PEM-encoded root certificates. Empty → skipped.
 */
export declare function verifyTsaTrust(check: TsaCheck, trustList: string[]): Promise<TsaTrustResult>;
//# sourceMappingURL=tsa.d.ts.map