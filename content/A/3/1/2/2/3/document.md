---
id: aff1868f-66aa-4252-851f-9343567a52eb
docNo: A.3.1.2.2.3
name: Sky Savings Rate Current Value
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.3.1.2.2.3 - Sky Savings Rate Current Value [Core]

The current value of the Sky Savings Rate can be obtained by calling the `ssr()` function on the sUSDS contract located on the Ethereum Mainnet at `0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD`.

The `ssr()` function returns a per-second compounding rate in RAY precision (10^27). The equivalent annualized rate, compounded over a 365-day year (31,536,000 seconds), is given by the formula:

`annualized rate = (ssr() / 1E27)^31536000 - 1`

The result is a decimal rate (e.g., 0.0365 represents 3.65% per year).
