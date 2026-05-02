---
id: ca253911-1755-481f-ae63-1d4027d1a690
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.2.4.3
name: Decode Token Shares
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.4.3 - Decode Token Shares [Core]

The operator must decode the raw bytes data returned from the `doCall()` function into `uint256` value, representing the number of token `shares` burned in the withdrawal.

`    {
        // Withdraw asset from a token, decode resulting shares.
        // Assumes proxy has adequate token shares.
        shares = abi.decode(
            proxy.doCall(
                [Instance_Morpho_Fluid_Vault_Address_Placeholder],,
                abi.encodeCall(IERC4626(token).withdraw, (amount, address(proxy), address(proxy)))
            ),
            (uint256)
        );
    }`
