---
id: 1c1acaaa-8f4c-46b4-b336-429597968dc7
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.4
name: Claim Assets
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.4 - Claim Assets [Core]

The operator must claim the `assets` from the vault to the `proxy` by calling `withdraw` on the ERC-7540 vault. The `proxy` receives the withdrawn assets.

`        // Claim assets from the vault to the proxy
        proxy.doCall(
            token,
            abi.encodeCall(IERC7540(token).withdraw, (assets, address(proxy), address(proxy)))
        );
    }`
