---
id: afbf5683-4b25-4286-9b9f-98e8a9cbc2e6
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.3
name: Check RateLimits
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.3 - Check RateLimits [Core]

The operator must ensure the `RateLimits` allow for transferring the required `amount` of shares. The rate limit is keyed on the `LIMIT_CENTRIFUGE_TRANSFER` identifier together with the `token` and `destinationCentrifugeId`, and is decreased by `amount`.

`rateLimited(
            keccak256(abi.encode(LIMIT_CENTRIFUGE_TRANSFER, token, destinationCentrifugeId)),
            amount
        );`
