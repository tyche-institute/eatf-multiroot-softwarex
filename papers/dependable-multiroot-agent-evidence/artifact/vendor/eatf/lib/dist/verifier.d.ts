/**
 * v0.1: top-level verifier entry.
 *
 * Pipeline (mirrors the Java reference):
 *   1. Unzip the .aep package.
 *   2. Read required entries (response.txt, canonical.bin, hash.sha256,
 *      signature.sig, public_key.pem, metadata.json, timestamp.tsr).
 *   3. Recompute supported canonical forms and compare to canonical.bin.
 *   4. Hash canonical bytes with SHA-256; compare to hash.sha256.
 *   5. Verify RSA signature with public_key.pem.
 *   6. If PQC entries present, verify ML-DSA-65 signature.
 *   7. Structural-check the RFC 3161 timestamp.
 *
 * Each step appends to the report; a single failure short-circuits.
 */
import type { VerifyOptions, VerifyResult } from "./index.js";
export declare function verify(input: Uint8Array | ArrayBuffer | Blob, opts?: VerifyOptions): Promise<VerifyResult>;
//# sourceMappingURL=verifier.d.ts.map