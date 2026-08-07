---
id: 79029ed0-7c9d-443e-b928-b528d0a66d00
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.4
name: Approve Contract Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.4 - Approve Contract Spend [Core]

The operator must approve the ERC-7540 vault (`token`) to spend the `amount` of the underlying `asset` on behalf of the `proxy`. This assumes the `proxy` holds enough of the asset.

`        // Approve asset to vault from the proxy (assumes the proxy has enough of the asset).
        ERC20Lib.approve(proxy, address(asset), token, amount);`
