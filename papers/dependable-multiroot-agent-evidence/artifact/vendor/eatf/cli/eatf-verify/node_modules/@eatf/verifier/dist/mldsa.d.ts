/**
 * v0.1: ML-DSA-65 (NIST FIPS 204) signature verification.
 *
 * Web Crypto does not yet expose ML-DSA. We use `@noble/post-quantum`
 * which ships pure-TS implementations of Kyber and Dilithium / ML-DSA.
 * `@noble/post-quantum`'s `ml_dsa65` matches the parameter set the
 * EATF Java reference uses (`PqcSignatureServiceImpl`).
 *
 * v0.1-alpha caveat: the dependency is imported lazily so that bundlers
 * that strip unused exports do not pull the WASM/JS body unless the
 * caller actually verifies a PQC-signed package.
 */
/**
 * Verify an ML-DSA-65 signature over the canonical byte sequence.
 * Returns boolean; throws only on input shape errors.
 */
export declare function verifyMlDsa65(publicKeyPem: string, signature: Uint8Array, signedData: Uint8Array): Promise<boolean>;
//# sourceMappingURL=mldsa.d.ts.map