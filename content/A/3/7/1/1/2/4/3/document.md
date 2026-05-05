---
id: a5ae79ad-9460-41a3-8dbf-65605f54b79b
docNo: A.3.7.1.1.2.4.3
name: Ceiling Increase Cooldown (ttl)
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.3.7.1.1.2.4.3 - Ceiling Increase Cooldown (ttl) [Core]

The Ceiling Increase Cooldown (`ttl`) parameter controls how frequently the Debt Ceiling can be increased by the DC-IAM. If a user attempts to use the DC-IAM to increase the Debt Ceiling of a vault type before this time expires, the transaction will fail to execute and the Debt Ceiling will remain unchanged. The `ttl` parameter in combination with the `gap` parameter enforces a maximum rate at which debt usage can increase over time using a given vault type. These parameters should be set such that the maximum increase over time can accommodate all reasonable usage of the vault type in question. The `ttl` parameter is defined in seconds.
