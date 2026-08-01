---
id: 58b13044-b093-4cd4-a006-0557360ece3e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.5
name: Deposit Asset
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.5 - Deposit Asset [Core]

The operator must call `deposit` on the `token` through the `proxy`, depositing `amount` of the underlying asset and directing the minted vault shares to the `proxy`. The number of `shares` received is decoded from the return data.

`        shares = abi.decode(
            proxy.doCall(
                token,
                abi.encodeCall(IERC4626(token).deposit, (amount, address(proxy)))
            ),
            (uint256)
        );`
