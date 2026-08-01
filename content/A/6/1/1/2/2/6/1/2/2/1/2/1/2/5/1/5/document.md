---
id: 74415da6-e8d4-4da7-887d-ce27e5ecc307
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.5
name: Submit Deposit Request
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.5 - Submit Deposit Request [Core]

The operator must submit the deposit request by calling `requestDeposit` on the ERC-7540 vault, transferring the `amount` of the asset from the `proxy` into the vault. The `proxy` is set as both the controller and owner of the request, so the resulting shares can later be claimed to the `proxy`.

`        // Submit deposit request by transferring assets
        proxy.doCall(
            token,
            abi.encodeCall(IERC7540(token).requestDeposit, (amount, address(proxy), address(proxy)))
        );
    }`
