export type OvertReceipt = Record<string, unknown>;
export type OvertValidation = {
    receipt: OvertReceipt | null;
    error: string | null;
};
export declare function parseAndValidateOvertReceipt(entries: Record<string, Uint8Array>, metadata: Record<string, unknown>, expectedHashHex: string): OvertValidation;
//# sourceMappingURL=overt.d.ts.map