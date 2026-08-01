---
id: 8a55fb60-99d2-4780-ab6c-9cf3df788872
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.3
name: Submit Redeem Request
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.3 - Submit Redeem Request [Core]

The operator must submit the redeem request by calling `requestRedeem` on the ERC-7540 vault, transferring the `shares` from the `proxy` into the vault. The `proxy` is set as both the controller and owner of the request, so the resulting assets can later be claimed to the `proxy`.

`        // Submit redeem request by transferring shares
        proxy.doCall(
            token,
            abi.encodeCall(IERC7540(token).requestRedeem, (shares, address(proxy), address(proxy)))
        );
    }`
