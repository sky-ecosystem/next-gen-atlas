---
id: 7f43aea7-9b81-48ef-b3ce-fdfae7e8a551
docNo: A.2.4.1.1
name: Operational Processes
type: Core
depth: 5
childType: sections_and_primary_docs
---

###### A.2.4.1.1 - Operational Processes [Core]

The Monthly Settlement Cycle (MSC) synchronizes several key operational processes across the ecosystem, including:

1. Sky Protocol’s net revenue from the previous month is calculated and allocated through the steps of the Treasury Management Function. See [A.2.3 - Treasury Management](6c0af059-5d33-4e2b-90f1-1606957b8f85).
2. The monthly Senior Risk Capital (SRC) origination process is settled: the clearing price is established, costs are deducted from winning Prime Agents’ accounts, and their accounts are credited with Originated SRC (OSRC) for the upcoming month. See [A.3.2.2.4.3.5 - Settlement Of Origination](fff0112a-58dd-4041-97f9-7baf113b4e70).
3. Queued conversions between USDS and srUSDS within the SRC system are processed. See [A.3.2.2.4.2.2 - Deposit And Redemption Queues](38a99586-4a13-4ce3-8b2f-cee025e0c390).
4. Pioneer Incentive Pools are funded with an amount equivalent to the Sky Savings Rate multiplied by the balance of Unrewarded USDS. See [A.2.2.8.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).
5. Smart Burn Engine parameters are updated at each Monthly Settlement Cycle based on the prior month's state. See [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121) and [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a).
6. Critical Core GovOps functions related to the operationalization of Sky Primitives are executed, including payment/reimbursement processing, compliance monitoring, and the calculation and application of retroactive penalties.
