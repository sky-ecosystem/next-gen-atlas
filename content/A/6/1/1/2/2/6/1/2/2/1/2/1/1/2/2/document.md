---
id: 9e079e2a-6b46-4261-b3ce-cc001d676011
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.2
name: Associate LayerZero Recipient With Endpoint
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.2 - Associate LayerZero Recipient With Endpoint [Core]

The operator must associate the `layerZeroRecipient` with the `destinationEndpointId` such that any tokens bridged to this endpoint will go to this recipient.

`{
        layerZeroRecipients[destinationEndpointId] = layerZeroRecipient;`
