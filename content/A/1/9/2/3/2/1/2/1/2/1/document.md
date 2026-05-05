---
id: 3d031b7c-1b1f-4f84-8668-1cdf43cb2ab2
docNo: A.1.9.2.3.2.1.2.1.2.1
name: Requirements For Forum Post
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.1.9.2.3.2.1.2.1.2.1 - Requirements For Forum Post [Core]

The Forum post must include the following:

- The addresses of the deployed contracts
- A link to the audit reports, ideally externally verifiable sources, such as the Chain Security website link to an audit report.
- Confirmation that the deployed code matches the commit hash that was sent for audit.
- Constructor arguments are as expected in the Init script
- (optional) Authority is given to the protocol owner: `MCD_PAUSE_PROXY` in the case of SKY and denied from the deployer address.
- Include instructions to be added to the Executive Sheet, such as adding the module to the chainlog, defining parameters for the module (provided by the Risk Advisor), further authorization that needs to be done to different module elements.
