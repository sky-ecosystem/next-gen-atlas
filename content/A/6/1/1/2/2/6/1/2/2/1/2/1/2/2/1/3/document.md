---
id: e4132ae2-cdaa-4221-a69c-0b332e71337b
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.3
name: Get Vault Asset
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.3 - Get Vault Asset [Core]

The operator must resolve the underlying `asset` of the ERC-4626 vault by calling `asset` on the `token`. This is the ERC-20 asset that will be deposited from the Grove ALM Proxy.

`        IERC20 asset = IERC20(IERC4626(token).asset());`
