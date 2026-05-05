---
id: 58ca518e-9ff1-4008-9616-18f135a33772
docNo: A.6.1.1.1.2.6.1.3.1.2.1.3.1.7.2
name: Send Encoded Call
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.7.2 - Send Encoded Call [Core]

The operator must send the encoded call using `proxy.doCall()` to the `supply` function on Aave (`pool`).

        `// Deposit underlying into Aave pool, proxy receives aTokens
proxy.doCall(
address(pool),
abi.encodeCall(pool.supply, (address(underlying), amount, address(proxy), 0))
);
}`
