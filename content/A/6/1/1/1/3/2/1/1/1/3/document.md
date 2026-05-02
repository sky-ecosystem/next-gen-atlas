---
id: 9006fd8d-bd13-48fc-bf2f-04f47579b3b0
docNo: A.6.1.1.1.3.2.1.1.1.3
name: Interest Rate Model Definition
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.2.1.1.1.3 - Interest Rate Model Definition [Core]

The Interest Rate Model ("IRM") is defined by four main parameters:

1. Base Rate - the starting rate at 0% utilization,
2. Variable Slope 1 - the rate at optimal utilization,
3. Variable Slope 2 - the rate at 100% utilization,
4. Utilization - the utilization itself.

The Base Rate, Slope 1, and Slope 2 parameters are further defined in: [A.6.1.1.1.3.2.1.1.1.13 - Base Rate Definition](9372deb9-5115-4010-bf72-34023b846525); [A.6.1.1.1.3.2.1.1.1.15 - Slope 1 Definition](c16b2b24-d663-4877-8bb3-cbd32e977360); and [A.6.1.1.1.3.2.1.1.1.17 - Slope 2 Definition](56bc7808-5ef8-42af-ba17-708b995194cc).

All markets except Dai use this IRM. The IRM for Dai is independent of utilization and is defined as a spread over the Sky Savings Rate set forth in [A.3.1.2.2 - Sky Savings Rate](2674cccb-d779-4868-b83f-8cb86648c88a). The spread is determined by the Stability Facilitators, in consultation with the Core Council Risk Advisor.
