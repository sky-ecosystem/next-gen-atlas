---
id: 42ea8a7b-fb28-455e-8038-5fcf25250f17
docNo: A.3.5.2.4.4
name: Technical Limitations
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.3.5.2.4.4 - Technical Limitations [Core]

The SBE-BEAM enforces technical limitations, including the following, that apply independently of the bounding parameters set by Sky Governance. An attempt to use the SBE-BEAM in a manner that exceeds these limitations will revert.

The `hop` parameter cannot be set higher than five (5) years. This limitation prevents the Smart Burn Engine from being placed in a state in which its reward stream — the staking rewards funded by the non-burned portion of surplus and streamed out over the Splitter Interval — can no longer be revived through the SBE-BEAM.

The `burn` parameter cannot be set higher than 100%, the point at which the entire surplus is directed to SKY accumulation. A higher value would cause the Smart Burn Engine to halt.

The `kbump` parameter must be set to a whole multiple of `RAY` (10²⁷). A value that is not an exact multiple of `RAY` will revert, ensuring the Kicker Lot Size is always expressed in the protocol's standard fixed-point precision.
