---
id: c6d58a58-9d15-45d1-a886-5c405f2350ee
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.4
name: Claim Shares
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.4 - Claim Shares [Core]

The operator must claim the `shares` from the vault to the `proxy` by calling `mint` on the ERC-7540 vault. The `proxy` receives the minted shares.

`        // Claim shares from the vault to the proxy
        proxy.doCall(
            token,
            abi.encodeCall(IERC4626(token).mint, (shares, address(proxy)))
        );
    }`
