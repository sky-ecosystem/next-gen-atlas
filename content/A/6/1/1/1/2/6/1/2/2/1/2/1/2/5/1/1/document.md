---
id: eb5d0ce2-ae57-4a99-b020-02e611667fbe
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.1
name: Relayer Role
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.1 - Relayer Role [Core]

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferUSDCToCCTP`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function transferUSDCToCCTP(uint256 usdcAmount, uint32 destinationDomain)
        external
        onlyRole(RELAYER)
        isActive`
