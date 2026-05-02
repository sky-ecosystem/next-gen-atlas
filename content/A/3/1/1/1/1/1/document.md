---
id: 839bfb33-5ac5-4e10-9521-65e43dd04464
docNo: A.3.1.1.1.1.1
name: Level Of Actively Stabilizing Collateral In Lite PSM
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.3.1.1.1.1.1 - Level Of Actively Stabilizing Collateral In Lite PSM [Core]

PSM ASC is defined as the level of Actively Stabilizing Collateral (see [A.3.3.2.2.1 - Actively Stabilizing Collateral](62495dee-8d2a-45d4-87c4-01150e3db3c8)) in the Lite PSM (see [A.3.3.2.7.1.1 - Lite Peg Stability Module](39473e1a-63f8-433b-a850-08f53b2dcf02)) as a percentage of the Sky Collateral Portfolio (see [A.3.3.1.1 - Minimum Actively Stabilizing Collateral](de00cd5a-91ab-4c04-8ce1-8aa3b7f3c82b)). The Core Executor Agents should consider the level of PSM ASC using the following non-binding guidelines:

- If PSM ASC is above 30%, consider decreasing the Base Rate by approximately 2%;
- If PSM ASC is between 28% and 30%, consider decreasing the Base Rate by approximately 1%;
- If PSM ASC is between 26% and 28%, consider decreasing the Base Rate by approximately 0.3%;
- If PSM ASC is between 24% and 26%, consider maintaining the Base Rate at approximately its current level;
- If PSM ASC is between 22% and 24%, consider increasing the Base Rate by approximately 0.3%;
- If PSM ASC is between 20% and 22%, consider increasing the Base Rate by approximately 1%; and
- If PSM ASC is below 20%, consider increasing the Base Rate by approximately 2%.
