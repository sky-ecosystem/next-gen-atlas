---
id: 52511026-55f4-4848-95a2-53db048d906c
docNo: A.3.2.2.1.3.1.3
name: Delay Factor
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.3.2.2.1.3.1.3 - Delay Factor [Core]

The Delay Adjustment Factor $\text{DF}$ is a factor indicating the extent to which the risk associated with backdoor access is mitigated by a security delay between the time that a change using backdoor access is approved and the time that such a change becomes effective. This delay gives users time to raise issues or withdraw funds in the event of malicious or undesirable use of backdoor access.

The Delay Factor is `1` if there is no security delay and `0` if the security delay is 48 hours or greater. For security delays between 0 hours and 48 hours, the Delay Factor is linearly reduced for each hour of security delay. So a security delay of 24 hours would result in a Delay Factor of `0.5`.
