/**
 * v0.1: SHA-256 over the canonical byte sequence, via
 * Web Crypto SubtleCrypto (browser + Node 20+).
 */
export declare function sha256(data: Uint8Array): Promise<Uint8Array>;
export declare function toHex(bytes: Uint8Array): string;
export declare function fromHex(hex: string): Uint8Array;
//# sourceMappingURL=hash.d.ts.map