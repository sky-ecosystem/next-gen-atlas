---
id: 764ec592-5ff7-462c-9617-759914e1077b
docNo: A.4.6.1.1.1.1.1
name: DssBlow2
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.4.6.1.1.1.1.1 - DssBlow2 [Core]

Dai or USDS tokens can be transferred to the DssBlow2 contract, MCD_BLOW2, at `0x81EFc7Dd25241acd8E5620F177E42F4857A02B79`. Calling the `blow` function on this contract will cause any Dai or USDS tokens held by it to be added to the Surplus Buffer. During this process, the ERC-20 tokens are burned and the tokens are instead reflected as an internal balance in the MCD_VAT contract.
