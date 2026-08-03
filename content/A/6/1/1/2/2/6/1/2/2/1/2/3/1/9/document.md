---
id: 5f279a4e-5c7f-4b59-aef0-2dffe4666b67
docNo: A.6.1.1.2.2.6.1.2.2.1.2.3.1.9
name: Set The Merkl Distributor
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.9 - Set The Merkl Distributor [Core]

The document herein defines the process to set the `merklDistributor` address used by the `ForeignController` contract to claim Merkl rewards. Only the `DEFAULT_ADMIN_ROLE` is allowed to call `setMerklDistributor`, which updates the `merklDistributor` state variable and emits the `MerklDistributorSet` event.

`function setMerklDistributor(address merklDistributor_) external onlyRole(DEFAULT_ADMIN_ROLE)`
