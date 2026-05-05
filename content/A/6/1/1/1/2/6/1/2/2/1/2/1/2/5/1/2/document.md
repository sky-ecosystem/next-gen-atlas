---
id: 27da6bef-8e24-4aa5-86fc-9b47f1a896e0
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.2
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.2 - Check RateLimits [Core]

The operator must ensure the bridging transaction complies with `RateLimits`. The `LIMIT_USDC_TO_CCTP` parameter enforces a rate limit on total USDC transferred via CCTP. The `LIMIT_USDC_TO_DOMAIN` parameter enforces a rate limit on USDC transferred to a specific `destinationDomain`.

`rateLimited(LIMIT_USDC_TO_CCTP, usdcAmount)
        rateLimited(
            RateLimitHelpers.makeDomainKey(LIMIT_USDC_TO_DOMAIN, destinationDomain),
            usdcAmount
        )`
