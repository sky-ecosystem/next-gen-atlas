---
id: 42d05753-9759-4054-93cb-27c2c7bd3245
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.2
name: Associate Recipient With Centrifuge ID
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.2 - Associate Recipient With Centrifuge ID [Core]

The operator must associate the `recipient` with the `centrifugeId` such that any tokens transferred to this Centrifuge chain will go to this recipient.

`        centrifugeRecipients[centrifugeId] = recipient;`
