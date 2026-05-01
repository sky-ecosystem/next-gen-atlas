---
id: 0257a420-e92e-4942-b794-a559f299365f
docNo: A.3.7.1.1.2.3
name: Stability Fee
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.3.7.1.1.2.3 - Stability Fee [Core]

The Stability Fee parameter is an annual percentage fee charged on the Dai generated on Vaults. It is expressed as an annual percentage yield but it is charged on a per-block basis in Dai. The Dai from this fee is minted, added to the Dai debt for the vault, and then transferred into the Surplus Buffer which is under the control of Sky Governance. Each vault type has its own Stability Fee that can be adjusted independently.

The Stability Fees can be modified through either Executive Votes or the Stability Parameter Bounded External Access Module. See [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).

The Stability Fees must be gradually increased over time to incentivize users to migrate to SparkLend and other borrowing platforms offered by Prime Agents.
