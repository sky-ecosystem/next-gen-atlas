---
id: 52fa11b0-7167-47c3-9678-e879dc981127
docNo: A.3.5.1.1.1
name: Current Value
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.3.5.1.1.1 - Current Value [Core]

The current value of the Surplus Buffer can be calculated using the Vat contract, Sky’s central accounting contract, located on the Ethereum Mainnet at `0x35D1b3F3D7966A1DFe207aa4514C12a259A0492B`. The current value of the Surplus Buffer is the difference between:

1. The assets of the Vow contract obtained by calling the `dai` function on the Vat contract with the address of the Vow contract, and
2. The liabilities of the Vow contract obtained by calling the `sin` function on the Vat contract with the address of the Vow contract.
