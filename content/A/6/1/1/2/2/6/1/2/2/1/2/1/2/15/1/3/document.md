---
id: ffa66264-41fa-4425-9c01-155810c5b25d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.3
name: Check Domain Configuration
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.3 - Check Domain Configuration [Core]

The operator must ensure a `mintRecipient` has been configured for the target `destinationDomain`. If `mintRecipient` is zero the transfer reverts, as the destination domain has not been configured.

`        bytes32 mintRecipient = mintRecipients[destinationDomain];
        require(mintRecipient != 0, "CCTPLib/domain-not-configured");`
