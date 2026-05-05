---
id: 4a154956-88d7-4b90-a9b0-3a96871087a7
docNo: A.1.9.5.3.1.3.5
name: Plans Parameter Definition
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.5.3.1.3.5 - Plans Parameter Definition [Core]

The `plans` parameter is an array of scheduled Spells to be canceled. Each scheduled Spell to be canceled is represented as a `Plan` struct:

`/**
 * @notice A struct representing a plan.
 * @param usr The address of the scheduled spell.
 * @param tag The tag identifying the address.
 * @param fax The encoded call to be made in \`usr\`.
 * @param eta The expiration time.
 */
struct Plan {
    address usr;
    bytes32 tag;
    bytes fax;
    uint256 eta;
}`

The parameters of the `Plan` struct are defined in [A.1.9.5.3.1.3 - Protego Parameters](55195cdc-90c3-4133-a0e4-792444b60ed8).
