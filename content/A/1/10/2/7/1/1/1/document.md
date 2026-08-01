---
id: 7bd3f4a0-899a-4954-a00e-48b6fbce922c
docNo: A.1.10.2.7.1.1.1
name: Deployment And Initialization Script Structure
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.10.2.7.1.1.1 - Deployment And Initialization Script Structure [Core]

Deployment logic and initialization logic must be structured as follows:

- Deployment logic must be extracted into a Solidity library that accepts constructor arguments and deploys the contract.
- Initialization logic must be extracted into a Solidity library that performs post-deployment configuration, including granting roles and setting state.
- The deployment script must orchestrate the deployment by calling the deployment and initialization libraries.

Deployment and initialization logic must be combined into a single library unless there is reasonable justification for separation.
