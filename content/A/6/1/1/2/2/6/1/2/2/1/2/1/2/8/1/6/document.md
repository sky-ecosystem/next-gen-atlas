---
id: f4cccce9-ded8-4924-8398-81bd43b95e51
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.6
name: Approve Pool Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.6 - Approve Pool Spend [Core]

The operator must approve the `pool` to spend `amountIn` of the input token on behalf of the `proxy`.

`ERC20Lib.approve(params.proxy, curvePool.coins(params.inputIndex), params.pool, params.amountIn);`
