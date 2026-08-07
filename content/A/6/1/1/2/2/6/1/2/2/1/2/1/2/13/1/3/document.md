---
id: 37850859-598b-4a40-9f29-5a2622683fad
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.3
name: Approve Token Transfer
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.3 - Approve Token Transfer [Core]

The operator must, when the OFT reports that `approvalRequired` is `true`, approve the `oftAddress` to spend the `amount` of the underlying `token` on behalf of the Grove ALM Proxy through `ERC20Lib.approve`. The approval is skipped for OFT implementations that do not require it.

`        // NOTE: Full integration testing of this logic is not possible without OFTs with
        //       approvalRequired == false. Add integration testing for this case before
        //       using in production.
        if (ILayerZero(oftAddress).approvalRequired()) {
            ERC20Lib.approve(proxy, ILayerZero(oftAddress).token(), oftAddress, amount);
        }`
