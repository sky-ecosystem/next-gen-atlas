---
id: d8c986af-3586-4b01-b03e-eb75cb39bb28
docNo: A.6.1.1.1.2.6.1.2.2.1.2.2.1.1.2
name: Associate Mint Recipient With Domain
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.2.1.1.2 - Associate Mint Recipient With Domain [Core]

The operator must associate the `mintRecipient` with the `destinationDomain`, meaning that whenever tokens are minted on this domain, they will go to this recipient.

`{
        mintRecipients[destinationDomain] = mintRecipient;`
