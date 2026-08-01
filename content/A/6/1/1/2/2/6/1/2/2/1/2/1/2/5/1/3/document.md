---
id: b60a2f0c-397f-4814-bf94-a3b3e671507b
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.3
name: Get Vault Asset
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.3 - Get Vault Asset [Core]

The operator must retrieve the underlying `asset` of the ERC-7540 vault by calling `asset` on the `token`. This is the ERC20 asset that will be deposited into the vault.

`        // Note that whitelist is done by rate limits
        IERC20 asset = IERC20(IERC7540(token).asset());`
