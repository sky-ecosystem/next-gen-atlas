---
id: c513c254-32a7-4870-98f2-1b9f0d43b263
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.5
name: Quote The Transfer
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.5 - Quote The Transfer [Core]

The operator must call `quoteOFT` to determine the `amountReceivedLD` on the destination chain and set `sendParams.minAmountLD` to that value, then call `quoteSend` to obtain the native `MessagingFee` required to deliver the message.

`        // Query the min amount received on the destination chain and set it.
        ( ,, OFTReceipt memory receipt ) = ILayerZero(oftAddress).quoteOFT(sendParams);
        sendParams.minAmountLD = receipt.amountReceivedLD;

        MessagingFee memory fee = ILayerZero(oftAddress).quoteSend(sendParams, false);`
