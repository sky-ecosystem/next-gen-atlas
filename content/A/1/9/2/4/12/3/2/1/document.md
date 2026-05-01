---
id: fb60b182-3ac9-4593-b9c7-8e1eaaeaa099
docNo: A.1.9.2.4.12.3.2.1
name: Spell Validators Must Check Deployed Spell License
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.2.1 - Spell Validators Must Check Deployed Spell License [Core]

The correct license for the Spell contract is GNU AGPLv3. Validators should confirm that this license is used, which can be verified in one of two ways under the "Contract" tab on Etherscan:

1. In the `Other Settings` field under the contract’s metadata. The license should be displayed as `GNU AGPLv3`.
2. In the Spell Code in the commented line of code in the `DssSpell` contract. The line should contain: `SPDX-License-Identifier: AGPL-3.0-or-later`.

While the Spell should use the correct license to pass validation, this is not considered a strict requirement.
