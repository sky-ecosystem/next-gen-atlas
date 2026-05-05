---
id: fd4f7715-ce73-4906-a9ed-cfdcc905cccb
docNo: A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.4
name: Send Remaining USDC
type: Core
depth: 18
childType: sections_and_primary_docs
---

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.4 - Send Remaining USDC [Core]

The operator must send the remaining USDC amount (if applicable). If there is any `usdcAmount` left after the loop, they must send the remaining amount in a single transfer, ensuring the entire amount is transferred, even if it didn't divide evenly by the `burnLimit`.

`if (usdcAmount > 0) {
    _initiateCCTPTransfer(usdcAmount, destinationDomain, mintRecipient);
}`
