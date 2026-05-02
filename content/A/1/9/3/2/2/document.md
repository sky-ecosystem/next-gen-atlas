---
id: e604c477-e8e4-483f-a41e-c93dcff3acfd
docNo: A.1.9.3.2.2
name: Oracle Freeze Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.2 - Oracle Freeze Exception [Core]

The OSM_MOM contract manages the freezing of Sky’s oracles. The freeze functionality allows a successful governance proposal to immediately freeze the oracle price for any or all of the vault types in the Sky Protocol. Once frozen, the oracle price will remain at its current value.

The oracle cannot be unfrozen without waiting for the GSM Pause Delay as part of a regular governance proposal.

The risk opened up by this exceptional functionality is that the oracles may be frozen by an attacker in order to either:

- Prevent an expensive liquidation.
- Take advantage of a significant drop in collateral prices to mint unbacked USDS.
