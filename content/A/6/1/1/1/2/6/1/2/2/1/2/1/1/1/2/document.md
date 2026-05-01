---
id: 0d7bbcaf-477f-4b07-bb8b-fca7cf316f57
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.1.1.2
name: Associate Mint Recipient With Domain
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.1.1.2 - Associate Mint Recipient With Domain [Core]

The operator must associate the `mintRecipient` with the `destinationDomain` such that any tokens minted on this domain will go to this recipient.

`{
        mintRecipients[destinationDomain] = mintRecipient;`
