/**
 * Offline TypeScript verifier for EATF .aep evidence packages.
 *
 * Runs in the browser via Web Crypto and in Node 20+ without any
 * backend round-trip. Implements the AEP wire-format profile.
 *
 * Public API:
 *
 *   import { verify } from "@eatf/verifier";
 *   const result = await verify(file);                   // Blob | Uint8Array
 *   if (result.valid) console.log("ok", result.report);
 *   else console.warn("fail", result.failureReason);
 *
 * The browser bundle at `@eatf/verifier/browser` re-exports the same
 * symbols with a Web-Crypto-only path (no Node polyfills).
 */
export { verify } from "./verifier.js";
export { sign } from "./signer.js";
export { DEFAULT_TSA_TRUST_LIST, } from "./tsa-trust-list.js";
export { inspectTsa, verifyTsaTrust } from "./tsa.js";
//# sourceMappingURL=index.js.map