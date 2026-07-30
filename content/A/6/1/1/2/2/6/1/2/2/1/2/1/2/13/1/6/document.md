---
id: 46731c27-e45f-4ccf-8f1b-199141570bff
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.6
name: Execute Cross-Chain Transfer
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.6 - Execute Cross-Chain Transfer [Core]

The operator must call the `MainnetController` contract to execute the transfer. The `send` call is forwarded to the `oftAddress` through `proxy.doCallWithValue`, passing `fee.nativeFee` as the native value, with the Grove ALM Proxy set as the refund address.

`        proxy.doCallWithValue{value: fee.nativeFee}(
            oftAddress,
            abi.encodeCall(ILayerZero.send, (sendParams, fee, address(proxy))),
            fee.nativeFee
        );
    }`
