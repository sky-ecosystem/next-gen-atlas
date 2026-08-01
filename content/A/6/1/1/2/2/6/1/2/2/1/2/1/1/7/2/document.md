---
id: 33cee360-03fb-4c0a-a412-0d037a14640f
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.2
name: Validate The TWAP Seconds Ago
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.2 - Validate The TWAP Seconds Ago [Core]

The operator must load the `UniswapV3PoolParams` for the `pool` and ensure the supplied `twapSecondsAgo` is less than `uint32(type(int32).max)`, which caps the value at approximately 68 years; this bound is required due to the casting in `UniswapV3OracleLibrary.consult`. Otherwise the call reverts with `MainnetController/twap-seconds-ago-out-of-bounds`.

`{
        UniswapV3Lib.UniswapV3PoolParams storage params = uniswapV3PoolParams[pool];
        // Required due to casting in UniswapV3OracleLibrary.consult
        // Limits twapSecondsAgo to approximately 68 years
        require(twapSecondsAgo < uint32(type(int32).max), "MainnetController/twap-seconds-ago-out-of-bounds");`
