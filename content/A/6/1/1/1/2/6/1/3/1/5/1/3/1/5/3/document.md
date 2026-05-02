---
id: 1c4f95da-5479-4c47-bc8b-4e7875cf8139
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.1.5.3
name: Decode Vault Shares
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.5.3 - Decode Vault Shares [Core]

The operator must decode the raw bytes data returned from the `doCall()` function into `uint256` value, representing the number of vault `shares` minted from the deposit.

`        // Deposit asset into the token, proxy receives token shares, decode the resulting shares
        shares = abi.decode(
            proxy.doCall(
                [Instance_Morpho_Fluid_Vault_Address_Placeholder],,
                abi.encodeCall(IERC4626([Instance_Fluid_USDS_Vault_Address_Placeholder]).deposit, (amount, address(proxy)))
            ),
            (uint256)
        );
    }`
