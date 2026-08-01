---
id: 6255c62f-5a22-4f7a-9ffe-e9d8353f83da
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.4
name: Approve Contract Spend
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.4 - Approve Contract Spend [Core]

The operator must approve the `cctp` contract to spend the `usdcAmount` on behalf of the `proxy`, then read the per-message `burnLimit` from the CCTP local minter to determine whether the transfer must be split across multiple messages.

`        ERC20Lib.approve(proxy, address(usdc), address(cctp), usdcAmount);
        uint256 burnLimit = cctp.localMinter().burnLimitsPerMessage(address(usdc));`
