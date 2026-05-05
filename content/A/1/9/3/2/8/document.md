---
id: 5247c795-7f9d-4d3f-a040-6bc9b070e2d4
docNo: A.1.9.3.2.8
name: Smart Burn Engine Breaker Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.8 - Smart Burn Engine Breaker Exception [Core]

The SPLITTER_MOM contract allows for the disabling of the Smart Burn Engine without the GSM Pause Delay.

This functionality is available so that Sky Governance can react to emergencies regarding the Smart Burn Engine.

Since the Splitter contract also allocates USDS from the Surplus Buffer to USDS Staking Rewards, the activation of SPLITTER_MOM also disables these rewards until the activation is reversed by Sky Governance.
