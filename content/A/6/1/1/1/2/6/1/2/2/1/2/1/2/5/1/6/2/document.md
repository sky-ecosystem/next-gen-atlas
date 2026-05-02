---
id: 22cb4839-7520-435f-b99b-086446d6a64a
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.2
name: Initiate Single Transaction If Possible
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.2 - Initiate Single Transaction If Possible [Core]

If a single transaction is possible within the per-message limit, the operator must initiate the CCTP transfer for the entire USDC amount.

` {
    _initiateCCTPTransfer(usdcAmount, destinationDomain, mintRecipient);
}`
