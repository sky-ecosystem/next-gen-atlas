---
id: acda4904-4a23-47f3-84bb-211d53cc4463
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.3
name: Withdraw Asset
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.3 - Withdraw Asset [Core]

The operator must call `withdraw` on the `token` through the `proxy`, withdrawing `amount` of the underlying asset with the `proxy` as both the `receiver` of the asset and the `owner` of the shares being burned. The number of `shares` burned is decoded from the return data. This assumes the `proxy` holds adequate vault shares.

`        shares = abi.decode(
            proxy.doCall(
                token,
                abi.encodeCall(IERC4626(token).withdraw, (amount, address(proxy), address(proxy)))
            ),
            (uint256)
        );`
