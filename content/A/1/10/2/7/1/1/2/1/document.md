---
id: f7e962d7-3f73-4b0e-97f2-1990a74ca224
docNo: A.1.10.2.7.1.1.2.1
name: General Requirements
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.10.2.7.1.1.2.1 - General Requirements [Core]

The following requirements apply to all deployment and initialization scripts:

- Libraries must not contain hardcoded addresses. All addresses and configuration values must be passed as parameters.
- All library functions must be tested. Test coverage must target 100%. Exceptions to this requirement must have reasonable justification.

Deployment verification, including confirmation of address correctness and on-chain state, is not within the scope of an audit of deployment and initialization scripts and must be performed as a separate deployment verification review.
