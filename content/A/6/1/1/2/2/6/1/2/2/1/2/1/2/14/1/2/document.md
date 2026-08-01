---
id: 6dc805cb-36ca-4c2c-af85-4657fcf82d2d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1.2
name: Toggle Operator
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1.2 - Toggle Operator [Core]

The operator must toggle the authorization of the `operator` on the Merkl Distributor. This calls `toggleOperator` on the `MERKL_DISTRIBUTOR` through the `proxy` to authorize or deauthorize the `operator` to claim Merkl rewards on the `proxy`'s behalf.

`
        MerklLib.toggleOperator(MerklLib.MerklToggleOperatorParams({
            proxy       : proxy,
            distributor : Ethereum.MERKL_DISTRIBUTOR,
            operator    : operator
        }));
    }`
