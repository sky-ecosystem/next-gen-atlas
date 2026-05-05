---
id: 19fbd6f2-f303-4ad2-a56c-b3761bfc3b13
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.1.4.1
name: Initialize Interface For Address
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.4.1 - Initialize Interface For Address [Core]

The operator must initialize the interface for the `address of the underlying asset` retrieved from the `aToken` contract (the contract that represents the deposited assets in Aave). The `IERC20` interface allows interaction with ERC-20 tokens, including performing actions like transferring, approving, and checking balances.

` {
IERC20    underlying = IERC20(IATokenWithPool(aToken).UNDERLYING_ASSET_ADDRESS());`
