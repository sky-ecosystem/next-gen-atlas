---
id: 07418471-50d1-4c6b-92a1-c883121f2622
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.1.4.2
name: Send Encoded Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.4.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` specifying the `address` of the `asset` contract (`[Instance_USDS_Address_Placeholder]`) they want to deposit into.

`        // Approve asset to token from the proxy (assumes the proxy has enough of the asset).
        proxy.doCall(
            address(asset),
            abi.encodeCall(asset.approve, ([Instance_Fluid_USDS_Vault_Address_Placeholder], amount))
        );`
