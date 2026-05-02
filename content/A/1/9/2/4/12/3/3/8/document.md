---
id: 353d7fab-461c-4141-b0b5-24a91357ee4d
docNo: A.1.9.2.4.12.3.3.8
name: Spell Validators Should Review Timestamps
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.8 - Spell Validators Should Review Timestamps [Core]

Validators should ensure that all timestamps in the Spell (e.g., ETAs, expirations, or delays like GSM Pause) are calculated correctly and use Unix timestamp format (seconds since epoch) to prevent execution issues, such as invalid timings or reverts. Use the `make time` command in Spells-mainnet to validate these.
