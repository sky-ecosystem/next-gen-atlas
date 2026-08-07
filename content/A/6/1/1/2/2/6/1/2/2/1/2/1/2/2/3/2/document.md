---
id: 0d0eae8c-8b1f-4493-a574-53ad8d96322b
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.2
name: Redeem Shares
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.2 - Redeem Shares [Core]

The operator must call `redeem` on the `token` through the `proxy`, redeeming `shares` with the `proxy` as both the `receiver` of the underlying asset and the `owner` of the shares being redeemed. The amount of underlying `assets` received is decoded from the return data. This assumes the `proxy` holds adequate vault shares.

`        assets = abi.decode(
            proxy.doCall(
                token,
                abi.encodeCall(IERC4626(token).redeem, (shares, address(proxy), address(proxy)))
            ),
            (uint256)
        );`
