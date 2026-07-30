---
id: e7f4ee84-ede7-464a-adbe-f20a22280dda
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.6
name: Clear Dust Approval
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.6 - Clear Dust Approval [Core]

The operator must reset the `router` allowance for `tokenIn` back to zero to clear any dust approval left after the swap.

`// Clear approvals of dust
        ERC20Lib.approve(context.proxy, params.tokenIn, address(params.router), 0);`
