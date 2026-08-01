---
id: 3b4bb347-5f04-4fec-bb34-e0072a80c012
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.1
name: Admin Role
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.1 - Admin Role [Core]

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setLayerZeroRecipient`.

`function setLayerZeroRecipient(uint32 destinationEndpointId, bytes32 layerZeroRecipient)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`
