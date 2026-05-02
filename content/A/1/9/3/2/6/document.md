---
id: d07e74b5-2faa-4d4d-9b4f-eb6ea72e8768
docNo: A.1.9.3.2.6
name: Dynamic Debt Ceiling Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.6 - Dynamic Debt Ceiling Exception [Core]

The MCD_IAM_AUTO_LINE contract manages the debt ceiling parameters for many of Sky’s vault types according to preset rules. Keepers can use the contract to attempt to maintain a Target Available Debt in a given vault type. The contract modifies the debt ceiling up or down to maintain a level of available debt.

This functionality is exceptional so that the Sky protocol can react to changes in debt demand more quickly than waiting for the GSM Pause Delay.

The risk opened up by this exceptional functionality is a theoretical griefing attack on the IAM that prevents debt from being accessible in affected vault types.
