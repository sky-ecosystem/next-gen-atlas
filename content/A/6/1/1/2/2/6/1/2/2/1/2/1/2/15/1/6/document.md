---
id: 2a7cbcdc-de92-4c4e-ac2b-4277af33d578
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.6
name: Transfer Remaining Amount
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.6 - Transfer Remaining Amount [Core]

The operator must transfer the remaining amount, which is at or below the `burnLimit`, by calling `depositForBurn` on `cctp` through the `proxy` with `destinationCaller` set to zero, `maxFee` of zero, and a `minFinalityThreshold` of 2000, then emit `CCTPTransferInitiated` to the blockchain logs.

`        if (usdcAmount > 0) {
            _initiateCCTPTransfer(usdcAmount, destinationDomain, mintRecipient);
        }
    }`
