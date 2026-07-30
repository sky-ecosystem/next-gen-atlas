---
id: 8c1cd838-4032-4f43-a5cf-cf35f6fef967
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.3
name: Withdraw Underlying
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.3 - Withdraw Underlying [Core]

The operator must `withdraw` the underlying asset from the Aave `pool` to the `proxy`, assuming the `proxy` holds adequate `aToken`, and decode the returned `amountWithdrawn`.

`        // Withdraw underlying from Aave pool, decode resulting amount withdrawn.
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
