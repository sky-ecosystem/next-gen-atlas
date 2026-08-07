---
id: 7bba47ea-4bad-4223-bdd5-29a852402a92
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.5
name: Split Transfer Over Burn Limit
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.5 - Split Transfer Over Burn Limit [Core]

The operator must, while the remaining amount exceeds the `burnLimit`, initiate a CCTP transfer of `burnLimit` USDC per message and reduce the remaining amount by `burnLimit` on each iteration. Each transfer calls `depositForBurn` on `cctp` through the `proxy` with `destinationCaller` set to zero, `maxFee` of zero, and a `minFinalityThreshold` of 2000, and emits `CCTPTransferInitiated`.

`        while (usdcAmount > burnLimit) {
            _initiateCCTPTransfer(burnLimit, destinationDomain, mintRecipient);
            usdcAmount -= burnLimit;
        }`
