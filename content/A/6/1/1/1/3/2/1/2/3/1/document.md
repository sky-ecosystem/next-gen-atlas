---
id: f84a1cb6-7f77-4bd0-904f-8bf7b368d2d6
docNo: A.6.1.1.1.3.2.1.2.3.1
name: Sky Core Governance Responsibility For Virtual Revenue Share Prior to Launch of SPK
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.2.1.2.3.1 - Sky Core Governance Responsibility For Virtual Revenue Share Prior to Launch of SPK [Core]

Before the launch of Agent tokens, Sky Governance is temporarily responsible for paying out a "virtual revenue share" on behalf of Spark Protocol. It is calculated by taking the total amount of Dai borrowed from Spark Protocol, and then assuming a "virtual income" equivalent to 1% of this supply, and calculating a revenue share of 10% on that basis. The calculations and payments must be done manually by the Support Facilitators at the end of each quarter.

As an example: if, before the launch of Agent tokens, 200 million Dai is borrowed on Spark Protocol, then the virtual income is 1% of 200 million Dai, which gives 2 million Dai; and of that 2 million Dai the virtual revenue share is 200,000 Dai.

This 200,000 Dai must be paid out in incremental payments each quarter directly by Sky Governance from the Sky Surplus Buffer to a smart contract under the control of Aave Governance. If, before the launch of Agent tokens, less than 100 million Dai is borrowed from Spark Protocol by the Sky Protocol, accrual towards the virtual revenue share payments are paused (unpaid virtual revenue share that already accrued is still paid out at the end of the quarter), and the counting down of the revenue share duration is paused. The virtual revenue share payments and the counting down of the remaining revenue share duration is resumed when at least 100 million Dai is again borrowed from Spark Protocol by the Sky Protocol.

Once SPK tokens launch, the virtual revenue share system will be discontinued, and the standard rules of the Spark Protocol Aave Revenue Share Ecosystem Agreement shall take effect. See [A.6.1.1.1.3.2.1.2.3.2 - Standard Agreement Post SPK Launch](bb867551-5231-4a5b-ac37-09d545bf70ce).
