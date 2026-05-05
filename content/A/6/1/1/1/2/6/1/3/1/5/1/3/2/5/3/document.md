---
id: 83c04cbf-fbd9-4bd0-9791-4fb7b02b091d
docNo: A.6.1.1.1.2.6.1.3.1.5.1.3.2.5.3
name: Decode For Underlying Assets
type: Core
depth: 16
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.5.3 - Decode For Underlying Assets [Core]

The operator must decode the raw bytes data returned from the `doCall()` function into `uint256` value, representing the number of underlying `assets` received for the redeemed `shares`.

` function redeemERC4626(address token, uint256 shares)
        external onlyRole(RELAYER) isActive returns (uint256 assets)
    {
        // Redeem shares for assets from the token, decode the resulting assets.
        // Assumes proxy has adequate token shares.
        assets = abi.decode(
            proxy.doCall(
                [Instance_Fluid_USDS_Vault_Address_Placeholder],
                abi.encodeCall(IERC4626([Instance_Fluid_USDS_Vault_Address_Placeholder]).redeem, (shares, address(proxy), address(proxy)))
            ),
            (uint256)
        );`
