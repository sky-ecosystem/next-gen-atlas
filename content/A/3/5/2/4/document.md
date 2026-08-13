---
id: b57ac61b-f6b1-4025-bd44-569d0f2afe2f
docNo: A.3.5.2.4
name: Smart Burn Engine Bounded External Access Module
type: Core
depth: 5
childType: sections_and_primary_docs
---

###### A.3.5.2.4 - Smart Burn Engine Bounded External Access Module [Core]

The Smart Burn Engine Bounded External Access Module (SBE-BEAM) enables a designated, Governance-whitelisted Operator to adjust the Kicker Lot Size (`kbump`), the SKY Accumulation Percentage (`burn`), and the Splitter Interval (`hop`) parameters of the Smart Burn Engine, as specified in [A.3.5.2.2.1.2 - Kicker Lot Size Parameter](fc9cece1-84bf-4133-a2ef-ef2182a23a35), [A.3.5.2.1.1.2 - SKY Accumulation Percentage Parameter](e16d6215-c2f1-4140-affd-30e52a17fd43), and [A.3.5.2.1.1.1 - Splitter Interval Parameter](39a67e65-33f0-4f2c-917d-efff544cf5ab). Adjustments are governed by the SBE-BEAM smart contract logic and specific parameters set by Sky Governance.

The SBE-BEAM Operator can raise or lower these parameters within the bounds set by Sky Governance. Those bounds are one-sided guardrails on the rate of accumulation: the Kicker Lot Size cannot be set above `maxKbump`, the Splitter Interval cannot be set below `minHop`, and the combined throughput, expressed as the Kicker Lot Size divided by the Splitter Interval, cannot exceed `maxRate`. The rate of accumulation therefore cannot be raised beyond the maximum that Sky Governance has sanctioned, while no corresponding bound limits reductions to it. The SKY Accumulation Percentage (`burn`) is not subject to these bounds, which limit only the rate of accumulation, and the only technical constraint on it is the maximum specified in [A.3.5.2.4.4 - Technical Limitations](42ea8a7b-fb28-455e-8038-5fcf25250f17). The `tau` parameter separately requires a minimum interval between operations, applying to any operation regardless of whether it raises or lowers the parameters. The SBE-BEAM holds the following bounding parameters: (i) `maxKbump`, (ii) `minHop`, (iii) `maxRate`, and (iv) `tau`. The bases on which these parameters may be modified are specified in [A.3.5.2.3 - Modification](499570de-9fae-4009-be34-c3330266030a).
