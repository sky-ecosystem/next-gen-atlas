---
id: 097fc13f-6cdd-4cde-ac00-3db8aa94f3a5
docNo: A.6.1.1.1.2.6.1.3.1.4.1.3.4.3
name: Encode Function
type: Core
depth: 15
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.4.1.3.4.3 - Encode Function [Core]

The operator must use `proxy.doCall()` to send an approval call to the `usdc` contract, allowing the `ethenaMinter` contract to spend up to the specified `amount` of USDC. They must encode the function using `abi.encodeCall`.

` {
    proxy.doCall(
        address(usdc),
        abi.encodeCall(usdc.approve, (address(ethenaMinter), usdcAmount))
    );
}`
