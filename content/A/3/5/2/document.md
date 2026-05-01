---
id: ddb90fee-2851-4bf0-b924-f1d73e30ce7a
docNo: A.3.5.2
name: Smart Burn Engine Parameters
type: Section
depth: 4
childType: sections_and_primary_docs
---

##### A.3.5.2 - Smart Burn Engine Parameters [Section]

The current Smart Burn Engine parameters are:

- kicker.khump: -200 million USDS (Threshold of Surplus Buffer for Splitter to activate)
- kicker.kbump: 6,000 USDS
- splitter.hop: 13,787 seconds
- 100% of Splitter allocation is set to accumulate SKY
- 0% of Splitter allocation is set to reward SKY stakers
- burn (the percentage of the kicker.kbump to be moved to the underlying flapper): 100% (WAD * 1)
- LSEV2-SKY-A USDS rewardsDuration: 13,787 seconds

The rewardsDuration for the LSEV2-SKY-A USDS rewards contract must be set such that it is equal to the splitter.hop parameter.
