---
id: 02f75eaa-e4cf-462f-ae8d-6222c78bb066
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.4
name: Approve Vault Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.4 - Approve Vault Spend [Core]

The operator must approve the `token` to spend `amount` of the underlying `asset` on behalf of the Grove ALM Proxy. The approval is executed through `proxy.doCall` and reverts unless the token's `approve` returns empty or `true`. This assumes the `proxy` already holds sufficient underlying asset.

`        ERC20Lib.approve(proxy, address(asset), token, amount);`
