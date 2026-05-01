---
id: 54b41b8f-8104-47b9-a115-14a4a9716cf7
docNo: A.1.9.3.2.4
name: Liquidations Circuit Breaker Exception
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.3.2.4 - Liquidations Circuit Breaker Exception [Core]

The CLIPPER_MOM contract manages the circuit breaker for vault types using Liquidations 2.0. The circuit breaker functionality allows a successful governance proposal to impose Sky Governance’s choice of limitations on liquidations for any or all of the vault types in the Sky Protocol.

- Level 0 - Liquidations Enabled - The breaker is not tripped, new vaults can be liquidated and old liquidations can proceed.
- Level 1 - New Liquidations Disabled - No new liquidations can take place.
- Level 2 - New Liquidations and Resets Disabled - No new liquidations can take place. No existing auctions can be reset if they expire.
- Level 3 - All Liquidations Disabled - No new liquidations, no resets, no bidding in active auctions.

This functionality is exceptional because liquidations at non-market prices have the potential to be irreversibly damaging to both users and the Sky Protocol. The circuit breaker allows Sky Governance to attempt to limit the damage in the event of an issue affecting liquidations without waiting for the GSM Pause Delay.

Additionally, the contract allows for permissionless activation of the circuit breaker, if the price decrease in a collateral exceeds a preset percentage value between oracle price updates. The permissionless activation triggers the circuit breaker at Level 2 because both new auctions and resets reference the current oracle price.

When Level (0, 1, 2, 3) of liquidations circuit breaker is altered via Executive Vote, Sky Governance has the ability to set locked time, which is a specified duration which needs to pass before the liquidations circuit breaker can be triggered again via permissionless activation.

The risk opened up by this exceptional functionality is that liquidations may be halted by an attacker in order to either:

- Prevent an expensive liquidation.
- Take advantage of a significant drop in collateral prices to mint unbacked USDS.
