---
id: c639083a-417f-45c8-ba94-c0713d1539ac
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.1.2
name: Associate Mint Recipient With Domain
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.1.2 - Associate Mint Recipient With Domain [Core]

The operator must associate the `mintRecipient` with the `destinationDomain` such that any tokens minted on this domain will go to this recipient.

`{
        mintRecipients[destinationDomain] = mintRecipient;`
