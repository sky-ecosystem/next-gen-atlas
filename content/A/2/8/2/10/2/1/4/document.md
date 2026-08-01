---
id: 31e070cf-2474-4815-a7da-350feaa97cc7
docNo: A.2.8.2.10.2.1.4
name: Payment Frequency And Mechanism
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.2.8.2.10.2.1.4 - Payment Frequency And Mechanism [Core]

Compensation under this Accord is settled monthly via the Monthly Settlement Cycle (MSC). Each monthly settlement is calculated as:

$$ 
\text{Monthly Settlement} = \sum \left[ \frac{\text{USDS\_Deposited (sub-period)} \times 0.20 \times \text{Base\_Rate (sub-period)}}{365} \times \text{Sub-Period\_Days} \right] 
$$

where sub-periods are defined by any change to the USDS deposited in the Chronicle Point Reward Instance or the Base Rate during the settlement month, per the accrual method in [A.2.8.2.10.2.1.3 - Accrual Method](4bed0292-a720-4306-b528-5d583fd4ead5).
