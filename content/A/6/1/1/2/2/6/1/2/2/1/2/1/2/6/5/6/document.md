---
id: 695ec457-b53f-4521-b238-e8dccd377c2e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.6
name: Transfer Shares Cross-Chain
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.6 - Transfer Shares Cross-Chain [Core]

The operator must initiate the cross-chain share transfer through the resolved `spoke`, forwarding `msg.value` to cover the messaging fee. The call passes the vault `poolId` and `scId`, the configured `recipient`, and the `amount` of shares.

`proxy.doCallWithValue{value: msg.value}(
            spoke,
            abi.encodeCall(
                ISpokeLike(spoke).crosschainTransferShares,
                (
                    destinationCentrifugeId,
                    ICentrifugeV3VaultLike(token).poolId(),
                    ICentrifugeV3VaultLike(token).scId(),
                    recipient,
                    amount,
                    0
                )
            ),
            msg.value
        );
    }`
