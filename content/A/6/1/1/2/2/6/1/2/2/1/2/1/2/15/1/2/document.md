---
id: ccec5230-f1df-4dde-be4b-9f9a948d379d
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.2 - Check RateLimits [Core]

The operator must ensure that `RateLimits` allows the transfer, both against the global `LIMIT_USDC_TO_CCTP` limit and the per-destination `LIMIT_USDC_TO_DOMAIN` limit for the target `destinationDomain`.

`        rateLimited(LIMIT_USDC_TO_CCTP, usdcAmount);
        rateLimited(makeDomainKey(LIMIT_USDC_TO_DOMAIN, destinationDomain), usdcAmount);`
