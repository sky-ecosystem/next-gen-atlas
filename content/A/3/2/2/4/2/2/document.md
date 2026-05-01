---
id: 38a99586-4a13-4ce3-8b2f-cee025e0c390
docNo: A.3.2.2.4.2.2
name: Deposit And Redemption Queues
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.3.2.2.4.2.2 - Deposit And Redemption Queues [Core]

The srUSDS contract utilizes distinct queues for managing conversions. Users can add USDS to the deposit queue for conversion into srUSDS; or add srUSDS to the redemption queue for conversion back into USDS at any point during the month.

Assets placed in either queue can be withdrawn by the user at any time before the Monthly Settlement Cycle begins.

At the Monthly Settlement Cycle, all assets remaining in the queues are processed: queued USDS is converted into srUSDS, and queued srUSDS is converted into USDS based on the prevailing Conversion Rate. See [A.3.2.2.4.2.3 - Conversion Rate](2220b1b5-f2f6-4325-9bb5-43cca84e184c).
