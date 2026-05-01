---
id: c4eb149e-8d0b-4e5b-93c6-49c67b2221a3
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.2.6.3
name: Decode For Underlying Assets
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.6.3 - Decode For Underlying Assets [Core]

The operator must decode the raw bytes data returned from the `doCall()` function into `uint256` value, representing the amount of underlying assets that were successfully withdrawn from the Aave pool (`amountWithdrawn`).

       ` // Withdraw underlying from Aave pool, decode resulting amount withdrawn.
// Assumes proxy has adequate aTokens.
amountWithdrawn = abi.decode(
proxy.doCall(
address(pool),
abi.encodeCall(
pool.withdraw,
(IATokenWithPool(aToken).UNDERLYING_ASSET_ADDRESS(), amount, address(proxy))
)
),
(uint256)
);`
