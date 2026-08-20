# A.3 - The Stability Scope [Scope]  <!-- UUID: d56538fc-2220-491a-a4d2-7ad6e461d707 -->

The Stability Scope governs the management of the USDS Stablecoin. The USDS Stablecoin must be a permissionless and useful currency available to anyone. Its stability and risk must be managed to generate as much value for Sky and public good as possible.

## A.3.1 - Core Stability Parameters [Article]  <!-- UUID: 80f168a3-4a01-40dd-bb57-851f48d58912 -->

This Article defines methodologies and processes for optimizing and aligning the Core Stability Parameters, which are designed to stabilize the USDS Stablecoin.

### A.3.1.1 - Role Of Core Executor Agents [Section]  <!-- UUID: 4162b64d-fff8-4200-9b6c-86284ff06d08 -->

This Section defines the role of the Core Executor Agents in managing the Core Stability Parameters.

#### A.3.1.1.1 - Setting Base Rate [Core]  <!-- UUID: 9ced57db-dfcd-4ca3-ba29-b4803c91bb7c -->

The Core Executor Agents, in consultation with the Core Council Risk Advisor, must set the Base Rate to ensure (1) a sufficient level of Cash Stablecoins and (2) price stability of USDS and other Stablecoins produced by the Sky Ecosystem. The subdocuments herein define the process that the Core Executor Agents should follow in setting the Base Rate.

##### A.3.1.1.1.1 - Adjustment Process [Core]  <!-- UUID: e152c03d-5891-4962-867d-a0c42fa7539f -->

The Core Executor Agents should modify the Base Rate on a daily basis, as necessary, in consultation with the Core Council Risk Advisor. In doing so, the Core Executor Agents should consider the factors specified in the documents herein.

###### A.3.1.1.1.1.1 - Level Of Actively Stabilizing Collateral In Lite PSM [Core]  <!-- UUID: 839bfb33-5ac5-4e10-9521-65e43dd04464 -->

PSM ASC is defined as the level of Actively Stabilizing Collateral (see [A.3.3.2.2.1 - Actively Stabilizing Collateral](62495dee-8d2a-45d4-87c4-01150e3db3c8)) in the Lite PSM (see [A.3.3.2.7.1.1 - Lite Peg Stability Module](39473e1a-63f8-433b-a850-08f53b2dcf02)) as a percentage of the Sky Collateral Portfolio (see [A.3.3.1.1 - Minimum Actively Stabilizing Collateral](de00cd5a-91ab-4c04-8ce1-8aa3b7f3c82b)). The Core Executor Agents should consider the level of PSM ASC using the following non-binding guidelines:

- If PSM ASC is above 30%, consider decreasing the Base Rate by approximately 2%;
- If PSM ASC is between 28% and 30%, consider decreasing the Base Rate by approximately 1%;
- If PSM ASC is between 26% and 28%, consider decreasing the Base Rate by approximately 0.3%;
- If PSM ASC is between 24% and 26%, consider maintaining the Base Rate at approximately its current level;
- If PSM ASC is between 22% and 24%, consider increasing the Base Rate by approximately 0.3%;
- If PSM ASC is between 20% and 22%, consider increasing the Base Rate by approximately 1%; and
- If PSM ASC is below 20%, consider increasing the Base Rate by approximately 2%.

###### A.3.1.1.1.1.2 - External Rate Environment [Core]  <!-- UUID: 0a4f2260-5f9a-4f78-a944-20500b153fec -->

The Core Executor Agents should consider the external interest-rate environment, including the interest rates offered by competitors and funding rates in decentralized finance and traditional finance markets.

###### A.3.1.1.1.1.2.1 - Tools Development [Core]  <!-- UUID: 4feb630b-d694-42d9-9b69-a6da09affa2c -->

The Core Executor Agents must develop automated tools to monitor the external interest-rate environment to improve the rate-setting process.

###### A.3.1.1.1.1.3 - Other Factors [Core]  <!-- UUID: a985bebe-4fe6-44e9-8025-78c4f099ef57 -->

The Core Executor Agents should consider other factors such as supporting long-term market stability, user stability, system sustainability, and growth. In addition, the Core Executor Agents should consider constraints on Primes, including their cost of capital and reaction time, to avoid creating unnecessary volatility in rates.

#### A.3.1.1.2 - Setting Other Core Stability Parameters [Core]  <!-- UUID: 7c65e6aa-3218-4636-bfee-545988aca7df -->

When setting the Base Rate, the Core Executor Agents must also set all other Core Stability Parameters so that they maintain their specified relationship to the Base Rate. See [A.3.1.2 - Parameters](86c75c9c-3803-48c1-a897-88d2be7aeb0e). The only exception is the Dai Savings Rate, which must be gradually reduced to 0% as specified in [A.3.1.2.4.1 - Dai Savings Rate Modification](238d8932-633d-44df-a7ed-0ec5a423cc53).

#### A.3.1.1.3 - Implementation Of Rate Changes [Core]  <!-- UUID: 21a34a01-87a8-4753-be83-ea452b5d388d -->

The smart contracts that implement all of the Core Stability Parameters must be configured to allow the Core Executor Agents to modify the Core Stability Parameters using the Stability Parameter Bounded External Access Module. See [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).

### A.3.1.2 - Parameters [Section]  <!-- UUID: 86c75c9c-3803-48c1-a897-88d2be7aeb0e -->

This Section defines the Core Stability Parameters.

#### A.3.1.2.1 - Base Rate [Core]  <!-- UUID: 228f9955-6bba-4252-a101-5529e7a300b9 -->

The Base Rate is the key interest rate in the system. It defines all other rates by various spreads. It is expressed as an annual percentage yield.

##### A.3.1.2.1.0.3.1 - Spreads - Element Annotation [Annotation]  <!-- UUID: e7be875c-fa61-42af-8986-ec22aceab0e8 -->

The element refers to the differences added or subtracted from the Base Rate to determine other specific rates.

#### A.3.1.2.2 - Sky Savings Rate [Core]  <!-- UUID: 2674cccb-d779-4868-b83f-8cb86648c88a -->

The Sky Savings Rate ("SSR") is the rate USDS holders can earn on their USDS in the Sky Savings Rate smart contracts.

##### A.3.1.2.2.1 - Relationship To Base Rate [Core]  <!-- UUID: d16483ff-b83e-490f-a620-1b58cc679c7f -->

The Sky Savings Rate is equal to the Base Rate minus the sum of (1) the Distribution Reward Fee (see [A.2.2.9.1.2.1.2 - Distribution Reward Rate](57384c49-e499-4c69-b22c-8e1f1dd34759)) and (2) the Sky Spread (see [A.3.1.2.6 - Sky Spread](e1b694de-1ee3-4502-a9c9-52eea9539804)).

##### A.3.1.2.2.2 - Sky Savings Rate Modification [Core]  <!-- UUID: 1c8bb297-52a6-4774-a76d-e457ae5f5862 -->

The Sky Savings Rate can be modified through either Executive Votes or the Stability Parameter Bounded External Access Module. See [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).

###### A.3.1.2.2.2.1 - Sky Savings Rate Stability Parameter Bounded External Access Module Parameters [Core]  <!-- UUID: e3a7ca35-0569-4867-bc64-e732622bda21 -->

The Stability Parameter Bounded External Access Module parameters for the Sky Savings Rate are:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

##### A.3.1.2.2.3 - Sky Savings Rate Current Value [Core]  <!-- UUID: aff1868f-66aa-4252-851f-9343567a52eb -->

The current value of the Sky Savings Rate can be obtained by calling the `ssr()` function on the sUSDS contract located on the Ethereum Mainnet at `0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD`.

The `ssr()` function returns a per-second compounding rate in RAY precision (10^27). The equivalent annualized rate, compounded over a 365-day year (31,536,000 seconds), is given by the formula:

`annualized rate = (ssr() / 1E27)^31536000 - 1`

The result is a decimal rate (e.g., 0.0365 represents 3.65% per year).

#### A.3.1.2.3 - Agent Rate [Core]  <!-- UUID: 012c953b-c522-4ea3-939b-3282af4e1d7e -->

The Agent Rate is the rate that Prime Agents earn on USDS, Dai, and sUSDS balances. Except as specified in [A.3.1.2.3.4 - Spark](e15caed7-276c-4489-95dc-9ba628566bf4), the Agent Rate applies only to such balances held in the Prime Agent's SubProxy.

##### A.3.1.2.3.1 - Relationship To Base Rate [Core]  <!-- UUID: 4e49c66c-3361-48bb-9a18-a0217278488e -->

The Agent Rate is equal to the Base Rate minus the Sky Spread (see [A.3.1.2.6 - Sky Spread](e1b694de-1ee3-4502-a9c9-52eea9539804)), and thus is equal to the Sky Savings Rate plus the Distribution Reward Fee (see [A.2.2.9.1.2.1.2 - Distribution Reward Rate](57384c49-e499-4c69-b22c-8e1f1dd34759)).

##### A.3.1.2.3.2 - Treatment Of USDS and Dai Balances [Core]  <!-- UUID: 3fbca67b-f75d-48f8-9459-3cba592f835b -->

Prime Agents receive the full Agent Rate on USDS and Dai balances held in their SubProxy through the Monthly Settlement Cycle, as specified in [A.3.1.2.3.6 - Settlement](eed3d922-7bb8-4cee-97a4-47e902a1c937).

##### A.3.1.2.3.3 - Treatment Of sUSDS Balances [Core]  <!-- UUID: b1cc2cb1-aff6-4b7a-bb32-bdf56fc7fd2f -->

Prime Agents earn the Agent Rate on sUSDS balances held in their SubProxy. Because sUSDS balances already earn the Sky Savings Rate, only the remaining 0.20% — the Distribution Reward Rate (see [A.2.2.9.1.2.1.2 - Distribution Reward Rate](57384c49-e499-4c69-b22c-8e1f1dd34759)) — is paid through the Monthly Settlement Cycle, as specified in [A.3.1.2.3.6 - Settlement](eed3d922-7bb8-4cee-97a4-47e902a1c937), bringing the total up to the Agent Rate.

##### A.3.1.2.3.4 - Spark [Core]  <!-- UUID: e15caed7-276c-4489-95dc-9ba628566bf4 -->

Spark is entitled to an Agent Rate equal to the Base Rate on USDS and sUSDS balances held in Peg Stability Modules. See [A.3.3.2.1.1 - Peg Stability Module](0082c12d-f1a7-46ff-a4aa-5fe42ece1a4d). The Agent Rate earned by Spark is still subject to the limitations set forth in [A.3.1.2.3.5 - Limitations For Prime Agents Receiving Subsidized Rate](7f6c1ab6-7674-41b0-9522-7e7e5a1cab3d).

##### A.3.1.2.3.5 - Limitations For Prime Agents Receiving Subsidized Rate [Core]  <!-- UUID: 7f6c1ab6-7674-41b0-9522-7e7e5a1cab3d -->

If a Prime Agent is borrowing funds from Sky at a Subsidized Rate, as defined in [A.3.1.2.5.2 - Subsidized Rate](ceceb90b-57d1-43db-9e52-133532c373fd), then the Agent Rate earned by that Prime Agent shall be limited. Specifically, if the standard Agent Rate would exceed the Prime Agent’s Subsidized Rate, the Prime Agent will earn the Subsidized Rate on those balances. The difference between what would have been the standard Agent Rate earnings and the earnings at the Subsidized Rate is effectively retained by Sky. This adjustment is processed as part of the Monthly Settlement Cycle, as specified in [A.3.1.2.3.6 - Settlement](eed3d922-7bb8-4cee-97a4-47e902a1c937). If the standard Agent Rate is less than or equal to the Subsidized Rate, the standard Agent Rate applies.

##### A.3.1.2.3.6 - Settlement [Core]  <!-- UUID: eed3d922-7bb8-4cee-97a4-47e902a1c937 -->

To the extent Prime Agents are entitled to payments for the Agent Rate, those payments are made through the Monthly Settlement Cycle. See [A.2.4 - Sky Core Monthly Settlement Cycle](6f8d5065-d6ff-4add-9a28-eadeffa7ed1a).

##### A.3.1.2.3.7 - No Double Counting [Core]  <!-- UUID: 2a02d413-2d1c-4f88-906f-0636547348e1 -->

A Prime Agent's total reward on a USDS, Dai, or sUSDS balance shall not exceed the Agent Rate, which for the Spark balances specified in [A.3.1.2.3.4 - Spark](e15caed7-276c-4489-95dc-9ba628566bf4) is the Base Rate. The Agent Rate is therefore never paid on top of an existing base reward: an sUSDS balance earning the Sky Savings Rate is topped up to the Agent Rate as specified in [A.3.1.2.3.3 - Treatment Of sUSDS Balances](b1cc2cb1-aff6-4b7a-bb32-bdf56fc7fd2f), not paid the full Agent Rate in addition; and a balance receiving Integration Boost or USDS Token Rewards does not earn the Agent Rate.

#### A.3.1.2.4 - Dai Savings Rate [Core]  <!-- UUID: d220731b-35db-4803-8a74-1c470a5ad693 -->

The Dai Savings Rate ("DSR") is the rate Dai holders can earn on their Dai in the Dai Savings Rate smart contracts.

##### A.3.1.2.4.1 - Dai Savings Rate Modification [Core]  <!-- UUID: 238d8932-633d-44df-a7ed-0ec5a423cc53 -->

The Dai Savings Rate can be modified through either Executive Votes or the Stability Parameter Bounded External Access Module. See [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).

The Dai Savings Rate must gradually be reduced to 0% over time.

###### A.3.1.2.4.1.1 - Dai Savings Rate Stability Parameter Bounded External Access Module Parameters [Core]  <!-- UUID: 335dd92b-cbd8-4d98-8d23-1dd57d98487d -->

The Stability Parameter Bounded External Access Module parameters for the Dai Savings Rate are:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

#### A.3.1.2.5 - Agent Credit Line Borrow Rate [Core]  <!-- UUID: 6b2b7302-e63b-457e-afeb-daab5ca7a7de -->

The Agent Credit Line Borrow Rate is the annual percentage yield that Agents must pay to Sky Core to receive USDS liquidity into their respective vaults.

##### A.3.1.2.5.1 - Relationship To Base Rate [Core]  <!-- UUID: 4659cbf0-78c2-469b-8432-883e5c931dd1 -->

The Agent Credit Line Borrow Rate is equal to the Base Rate unless variable pricing has been activated pursuant to [A.1.10.2.3.2.2.1.4.2.1 - Use Of Prime Spell Security Registry In Prime Agent Credit Rating System](4c165fcc-59e5-45c8-866d-c5c68192e591). Upon activation, the Agent Credit Line Borrow Rate will vary by Prime Agent according to its Credit Rating.

##### A.3.1.2.5.2 - Subsidized Rate [Core]  <!-- UUID: ceceb90b-57d1-43db-9e52-133532c373fd -->

Prime Agents may temporarily be able to borrow specified amounts from Sky Core at a Subsidized Rate below the Base Rate under the terms of an Ecosystem Accord entered into between Sky and the Prime Agent.

##### A.3.1.2.5.3 - Use Of Funds [Core]  <!-- UUID: b914352c-f270-46e8-991a-468a4b01dc49 -->

Funds borrowed by Agents from Sky at the Agent Credit Line Borrow Rate must be deposited into the Agent’s Allocation Vault and used to invest in Allocation System Instances. See [A.2.2.10.1 - Allocation System Primitive](9db14ab7-bb4b-4751-8084-843bd4359f2a). These funds may not be transferred to the Agent’s SubProxy account or otherwise outside of the Agent’s designated accounts for its Allocation System Primitive.

##### A.3.1.2.5.4 - Accrued Interest [Core]  <!-- UUID: 9835ebab-59cc-4a2b-b030-3b07b4e9203d -->

Interest accrues on borrowed funds and is reflected in the Allocation Vault balance. Prime Agents must regularly transfer interest payments to the Allocation Vault to pay down accrued interest, ensuring the Allocation Vault balance returns to the principal amount only. Any accrued but unpaid interest reduces the Prime Agent's available Total Risk Capital. See [A.3.2.1.2.1 - Total Risk Capital Definition](6f6b25d6-f73c-4733-ba37-12a0a411433c).

##### A.3.1.2.5.5 - Prime Agent Credit Rating System [Core]  <!-- UUID: 926fb13d-efdd-4a83-a3dc-db1448a106f5 -->

After the development of a Prime Agent Credit Rating System, the Agent Credit Line Borrow Rate will vary based on the Credit Rating of each Prime Agent. The Credit Rating for a Prime Agent will take into account factors including the Encumbrance Ratio and the Prime Spell Security Incident Registry.

#### A.3.1.2.6 - Sky Spread [Core]  <!-- UUID: e1b694de-1ee3-4502-a9c9-52eea9539804 -->

The Sky Spread is a margin Sky retains for facilitating the ecosystem’s financing. Together with the Distribution Reward Fee, it constitutes the difference between the Base Rate and the Sky Savings Rate. The Sky Spread is 0%.

#### A.3.1.2.7 - Rate Conventions [Core]  <!-- UUID: 154c3b5d-7a87-4dae-85f3-7d26deab9a31 -->

Unless otherwise specified, all rates defined in the Atlas are expressed as annual percentage yields.

A spread between two rates defined in the Atlas is the arithmetic difference between their annual percentage yields. Where the Atlas specifies one rate as another rate plus or minus a spread, that spread is added to or subtracted from the annual percentage yield directly, without conversion.

### A.3.1.0.3.1 - Methodologies - Element Annotation [Annotation]  <!-- UUID: 2f658a82-a8d2-4bd1-be5c-906e4733400d -->

The element "methodologies" refers to the systematic approaches or frameworks used to achieve the specific objective of optimizing and aligning the Core Stability Parameters.

### A.3.1.0.3.2 - Optimizing And Aligning - Element Annotation [Annotation]  <!-- UUID: fa290d52-16ee-49c7-b05c-0b53f3781d39 -->

The element "optimizing" refers to the process of making the Core Stability Parameters as effective as possible in achieving their goal of stabilizing the USDS Stablecoin. The element "aligning" refers to ensuring that these parameters are consistent and work in harmony with the objectives of Sky and with each other to prevent conflicts or discrepancies that could undermine stability.

### A.3.1.0.3.3 - Processes - Element Annotation [Annotation]  <!-- UUID: a740b3eb-9500-4134-b216-6dd97d4363b8 -->

The element "processes" refers to the step-by-step procedures or sequences of actions carried out to implement the methodologies referenced in the Target Document.

### A.3.1.0.3.4 - Stabilize - Element Annotation [Annotation]  <!-- UUID: f90156d0-6dd2-4a0d-9981-b3079368fbc0 -->

The element "stabilize" refers to the objective of maintaining USDS’s value within a narrow range, preventing significant fluctuations that could lead to volatility. USDS should be worth $1 USD to fulfill its promise of being a Stablecoin.

## A.3.2 - Risk Capital [Article]  <!-- UUID: 55999acf-75fe-4adf-8584-9746ef50d3e4 -->

Prime Agents who invest capital from Sky’s Collateral Portfolio using the Allocation System Primitive must hold Risk Capital to protect Sky from potential losses on these investments. This Article sets forth the framework governing Risk Capital.

### A.3.2.1 - Conceptual Framework [Section]  <!-- UUID: ee3a912d-c340-41ee-b33e-45e72f215d49 -->

This Section defines the conceptual framework for Risk Capital.

#### A.3.2.1.1 - Required Risk Capital [Core]  <!-- UUID: b6597fb4-d347-44f4-8780-b9a4116c1a36 -->

The documents herein define the conceptual framework for determining the Aggregate Required Risk Capital (RRC) that Prime Agents are required to hold to protect Sky from risks on their investments.

##### A.3.2.1.1.1 - Capital Ratio Requirement [Core]  <!-- UUID: 3828778e-0197-4ce9-a836-6770d04f2ea9 -->

The Capital Ratio Requirement (CRR) with respect to one or more Instances is the Required Risk Capital with respect to such Instances divided by the amount of capital from Sky’s Collateral Portfolio invested in such Instances.

Risk Capital requirements in the Risk Framework may be specified either as an amount of RRC or as a CRR. If a CRR is specified, then the RRC is equal to the amount of capital from Sky’s Collateral Portfolio invested in the relevant Instances times the CRR.

For example, if a certain Instance has a CRR of 5% and 100,000,000 USDS is invested in the Instance, then the RRC is 5,000,000 USDS.

CRR may be specified in aggregate (Aggregate CRR), for a particular Instance (Instance CRR), or for a particular type of risk with respect to an Instance (Instance Financial CRR, Instance Smart Contract CRR, or Instance Administrative CRR).

##### A.3.2.1.1.2 - Aggregate RRC [Core]  <!-- UUID: 6aed5cc1-9671-4b73-88a9-fdd86ac93ece -->

The Aggregate RRC that a Prime Agent must maintain is equal to the sum of the Instance Total RRC for each Active Instance of the Allocation System Primitive that the Prime Agent has deployed.

##### A.3.2.1.1.3 - Instance Total RRC [Core]  <!-- UUID: 5fe6b54c-cc68-4f8a-8d1e-5044af941afe -->

The Instance Total RRC for an Instance is equal to the sum of the Instance Financial RRC, Instance Smart Contract RRC, and Instance Administrative RRC for that Instance. See [A.3.2.1.1.4 - Instance Financial RRC](ba1d5c0e-399f-47a6-b5d4-b3f5477d5787), [A.3.2.1.1.5 - Instance Smart Contract RRC](4b4ea578-28b4-481c-9abd-d34c5a4f383c), and [A.3.2.1.1.6 - Instance Administrative RRC](c2b60f0d-6555-463c-9ad3-2a9746be77c5).

###### A.3.2.1.1.3.1 - Incorporation Of Additional Types Of RRC [Core]  <!-- UUID: 4ce93e4b-e842-475b-bf85-d814e7e9d19c -->

Additional types of RRC reflecting other risk factors, including legal risk and oracle risk, will be incorporated in future iterations of the Risk Framework.

###### A.3.2.1.1.3.2 - Inability To Calculate Types Of RRC [Core]  <!-- UUID: 268af0e9-be3d-458e-9ccd-5a560abc7540 -->

If Instance Financial RRC, Instance Smart Contract RRC, or Instance Administrative RRC for an Instance cannot be calculated then the Instance Total CRR is 100%.

##### A.3.2.1.1.4 - Instance Financial RRC [Core]  <!-- UUID: ba1d5c0e-399f-47a6-b5d4-b3f5477d5787 -->

The documents herein define the conceptual framework for determining the Instance Financial RRC required to protect Sky from financial risk arising from an Instance of the Allocation System Primitive.

###### A.3.2.1.1.4.1 - Introduction [Core]  <!-- UUID: 622580fb-1153-4ef7-8196-4e643f2178b7 -->

The conceptual framework for financial risk is designed to ensure that Prime Agents hold sufficient capital to cover potential losses on their investments in case of an extreme market event. The Financial Risk Framework is based on the Basel Accords developed by the Committee on Bank Supervision, including Basel II, Basel III, and Basel IV. These frameworks are then adapted to reflect the differences between traditional finance and decentralized finance.

###### A.3.2.1.1.4.2 - Financial Risk Categories [Core]  <!-- UUID: 3d1f35bf-4342-45cd-b151-090b241c7ba1 -->

Financial risk can be divided into three categories, as specified in the documents herein. These categories of risk are interrelated, so Instance Financial RRC is not directly associated with these risk categories. Instead, risk models are developed for different asset classes, as specified in [A.3.2.1.1.4.3 - Financial Risk Models](2af9fa64-ab25-4017-920c-f1c07dff4c06). The development of each of these risk models is informed by considerations regarding how each of the financial risk categories impacts the specific asset.

###### A.3.2.1.1.4.2.1 - Credit Risk [Core]  <!-- UUID: ca07880e-7bc4-4f18-a59a-2b5a8cd4374e -->

Credit risk is the risk that a loan or other debt instrument will not be repaid according to agreed terms.

###### A.3.2.1.1.4.2.2 - Market Risk [Core]  <!-- UUID: e0dc140f-8172-497d-8576-ce24a7464e89 -->

Market risk is the risk that a financial asset will decline in value due to market conditions or changes in investor perceptions of the asset.

###### A.3.2.1.1.4.2.3 - Liquidity Risk [Core]  <!-- UUID: 547571b1-83ae-4977-8f39-b136e6d52b9c -->

Liquidity risk is the risk that an asset cannot be sold quickly enough, or in sufficient quantity, at its fair market value without causing a significant price impact.

###### A.3.2.1.1.4.3 - Financial Risk Models [Core]  <!-- UUID: 2af9fa64-ab25-4017-920c-f1c07dff4c06 -->

The conceptual framework for financial risk is implemented through asset class specific risk models. The documents herein define the asset classes that risk models exist or are being developed for, including the high level approach and examples of relevant assets.

###### A.3.2.1.1.4.3.1 - Fully Implemented Risk Models [Core]  <!-- UUID: 419a1d00-fbae-4d26-bd47-8f57677d8001 -->

The documents herein define fully implemented asset-class-specific risk models.

###### A.3.2.1.1.4.3.1.1 - Lending Markets [Core]  <!-- UUID: b2c5ee5d-81f6-4066-94b5-e9d1b781cbc9 -->

The model for lending markets focuses on Credit Risk by incorporating asset volatility and liquidity factors. This model can be applied to lending markets such as SparkLend, Aave, Morpho, Fluid, and Maple. The implementation of the model for lending markets is specified in [A.3.2.2.1.1.1.1 - Lending Markets](d4e9c9e0-eeab-4399-99a0-5f72ff0d0e43).

###### A.3.2.1.1.4.3.1.2 - Real World Assets [Core]  <!-- UUID: 72076b08-d4f4-4cbf-af6d-379363cade39 -->

The model for Real World Assets is based on the direct application of existing frameworks to evaluate the risk of tokenized Real World Assets. The implementation of the model for Real World Assets is specified in [A.3.2.2.1.1.1.5 - Real World Assets](79c20bfd-f724-482e-8aae-52c962b8268a).

###### A.3.2.1.1.4.3.2 - Pending Risk Models [Core]  <!-- UUID: 81ca88bf-3f6a-4d10-a3e2-d47cf6636d7d -->

The documents herein define pending asset-class-specific risk models.

###### A.3.2.1.1.4.3.2.1 - Perpetual Positions [Core]  <!-- UUID: 8e518098-6a0b-4a31-b726-0739000a51ed -->

The model for perpetual positions uses a modified Credit Risk model to evaluate the risk of tokenized delta-neutral positions, such as Ethena and Resolv. The implementation of the model for perpetual positions is specified in [A.3.2.2.1.1.1.2 - Perpetual Positions](69fac7fa-6168-4b74-99cc-28b557826556).

###### A.3.2.1.1.4.3.2.2 - Direct Exposures [Core]  <!-- UUID: 38580dc9-dc5b-4842-88a2-7ab6eb3fcb14 -->

The model for direct exposures combines Market Risk and Liquidity Risk to evaluate the risk of direct asset holdings of volatile cryptoassets, such as ETH, stETH, and WBTC. The implementation of the model for direct exposures is specified in [A.3.2.2.1.1.1.3 - Direct Exposures](69d0776b-786c-408b-b76a-860ea60b6b9a).

###### A.3.2.1.1.4.3.2.3 - Bond-Like Instruments [Core]  <!-- UUID: 1d4cd705-2892-4b59-82e8-609c4649652d -->

The model for bond-like instruments uses a modified Credit Risk model to evaluate the risk of cryptoassets with duration risk, such as Pendle’s PT-tokens. The implementation of the model for bond-like instruments is specified in [A.3.2.2.1.1.1.4 - Bond-Like Instruments](da1a154c-6db8-4012-91a7-31ea4e73e95d).

###### A.3.2.1.1.4.3.2.4 - Cash Stablecoins [Core]  <!-- UUID: 0658e6cd-d785-498a-94c4-71cfbc319c24 -->

The model for Cash Stablecoins is based on identifying stablecoins, such as USDC and USDT, that do not present significant Market Risk, Credit Risk, or Liquidity Risk. The implementation of the model for Cash Stablecoins is specified in [A.3.2.2.1.1.1.6 - Cash Stablecoins](3c0a9e8b-4a0b-4059-87a4-155deaee0486).

##### A.3.2.1.1.5 - Instance Smart Contract RRC [Core]  <!-- UUID: 4b4ea578-28b4-481c-9abd-d34c5a4f383c -->

The documents herein define the conceptual framework for determining the Instance Smart Contract RRC required to protect Sky from smart contract risk arising from an Instance of the Allocation System Primitive.

###### A.3.2.1.1.5.1 - Definition [Core]  <!-- UUID: 8536fbd1-674d-4982-bd50-0bacf0986ce2 -->

Smart Contract Risk refers to the risk that an investment through the Allocation System will experience a loss of funds due to a bug or technical exploit. This risk may arise from the protocol invested in or other aspects of the investment such as bridging requirements.

###### A.3.2.1.1.5.2 - Risk Rating [Core]  <!-- UUID: 3cdbe77b-5df8-4ebb-9604-65db818abe69 -->

The determination of Smart Contract Risk should initially be based on an evaluation of the risk that the investment could experience losses due to a bug or technical exploit. This determination should take into account factors such as (1) the technical complexity of the code base (e.g. cyclomatic complexity, decision points, number of external calls, lines of code), (2) the number, quality, and recency of audits, and (3) the "Lindiness" of the relevant smart contracts.

###### A.3.2.1.1.5.3 - Required Risk Capital [Core]  <!-- UUID: eee90ace-5ee9-4efe-be26-6d3597d8b4a1 -->

The risk of a technical exploit in one protocol is unlikely to be correlated with the risk of a technical exploit in an unrelated protocol. Therefore, the risks from small exposures to even relatively risky protocols are likely to be diversified away. In contrast, very large exposures to even relatively safe protocols can create a risk to a Prime Agent and potentially to Sky itself if there is a technical exploit, especially if multiple Prime Agents have the same exposure. To account for this, the calculation of Instance Smart Contract RRC should take into account the risk rating, the level of exposure of the Prime, and the level of exposure of the Sky Ecosystem.

###### A.3.2.1.1.5.4 - Implementation [Core]  <!-- UUID: 3df9da84-f435-4d8d-a432-daa92d12a12c -->

The implementation of the calculation of Instance Smart Contract RRC is specified in [A.3.2.2.1.2 - Instance Smart Contract RRC Implementation](e6cfa64f-68c0-4dac-8cec-a5f9bfcb9080).

##### A.3.2.1.1.6 - Instance Administrative RRC [Core]  <!-- UUID: c2b60f0d-6555-463c-9ad3-2a9746be77c5 -->

The documents herein define the conceptual framework for determining the Instance Administrative RRC required to protect Sky from administrative risk arising from an Instance of the Allocation System Primitive.

###### A.3.2.1.1.6.1 - Definition [Core]  <!-- UUID: 0482b0c5-d78b-4e4a-b6c6-c858368d0b2c -->

Administrative Risk refers to the risk that an investment through the Allocation System will experience a loss of funds due to abuse of privileged access to a protocol. This risk may arise from a multisig or another actor that has the ability to modify the protocol or access funds without going through a governance process.

###### A.3.2.1.1.6.2 - Risk Rating [Core]  <!-- UUID: 3fe89645-48a9-430d-9ff1-925c361bb56f -->

The determination of Administrative Risk should initially be based on an evaluation of the risk that an investment could experience losses due to an abuse of privileged access. This determination should take into account factors such as (1) the level of privileged access that exists, (2) the security delay that such access is subject to, and (3) the "Lindiness" of the system.

###### A.3.2.1.1.6.3 - Required Risk Capital [Core]  <!-- UUID: bcb97e92-b578-4195-9ea5-a9e6bf2e201b -->

The risk of an abuse of privileged access in one protocol is unlikely to be correlated with the risk of an abuse of privileged access in an unrelated protocol. Therefore, the risks from small exposures to even relatively risky protocols are likely to be diversified away. In contrast, very large exposures to even relatively safe protocols can create a risk to a Prime Agent and potentially to Sky itself if there is an abuse of privileged access, especially if multiple Prime Agents have the same exposure. To account for this, the calculation of Instance Administrative RRC should take into account the risk rating, the level of exposure of the Prime, and the level of exposure of the Sky Ecosystem.

###### A.3.2.1.1.6.4 - Implementation [Core]  <!-- UUID: ee71508b-9c89-4765-83a5-6e50832549bb -->

The implementation of the calculation of Instance Administrative RRC is specified in [A.3.2.2.1.3 - Instance Administrative RRC Calculation](277d6712-25ff-4566-a42b-38d7e860ae76).

#### A.3.2.1.2 - Total Risk Capital [Core]  <!-- UUID: be7589f5-32c0-42d2-8d10-38bceb1de28b -->

The documents herein define the conceptual framework for types of capital that contribute to a Prime Agent’s Total Risk Capital (TRC). Prime Agents must maintain at all times a level of TRC that exceeds their Aggregate RRC or be subject to penalties.

##### A.3.2.1.2.1 - Total Risk Capital Definition [Core]  <!-- UUID: 6f6b25d6-f73c-4733-ba37-12a0a411433c -->

Total Risk Capital is capital that is currently eligible, available, and verifiably under the Prime’s control. For capital to be included in a Prime Agent's TRC, it must be currently deployable towards covering its Required Risk Capital obligations. Consequently, in-flight capital (e.g., assets being bridged) does not contribute towards a Prime’s TRC. Similarly, commitments for future capital, such as Ecosystem Accords for renting Prime-External Junior Risk Capital (PEJRC) or Tokenized External Junior Risk Capital (TEJRC) that have been agreed upon by counterparties but are not yet formally codified within the Atlas, cannot contribute towards a Prime’s TRC until such formalization is complete.

##### A.3.2.1.2.2 - Types Of Risk Capital [Core]  <!-- UUID: 24db6047-c829-4d31-ac0e-f81f908186ad -->

TRC comprises two categories based on loss absorption seniority: Junior Risk Capital (JRC) and Senior Risk Capital (SRC), further divided by source.

###### A.3.2.1.2.2.1 - Junior Risk Capital [Core]  <!-- UUID: 92e51a94-ef70-4a86-9946-36077ebad1e9 -->

Junior Risk Capital (JRC) is the first capital to absorb losses on investments under the Allocation System. Junior Risk Capital must experience 100% losses before any losses are absorbed by Senior Risk Capital.

###### A.3.2.1.2.2.1.1 - Junior Risk Capital Types [Core]  <!-- UUID: 57b0b226-ae2c-4d47-871d-57e6d3bb1a9f -->

The documents herein define the types of Junior Risk Capital.

###### A.3.2.1.2.2.1.1.1 - Internal Junior Risk Capital (IJRC) [Core]  <!-- UUID: 8728abee-0dc5-449b-b4c2-78698da16f10 -->

Internal Junior Risk Capital is capital owned by the Prime Agent itself. It serves as the foundation for the Prime’s risk capacity: the amount of IJRC directly dictates the maximum External JRC the Prime can source (governed by the External Per Internal ratio) and provides the primary capacity for enabling Senior Risk Capital (via the Senior Per Junior ratio), while also bearing the initial impact of any losses (the Tip JRC mechanism). IJRC must be eligible assets held in the Prime Agent’s designated treasury account (e.g., SubProxy), controlled by the Prime’s root governance.

See [A.3.2.1.2.3.1.1 - External Per Internal Ratio](ff374833-920c-40f6-ae6c-a71d33d99b82), [A.3.2.1.2.3.1.2 - Senior Per Junior Ratio](fbc9a273-d217-4d52-8b3e-b496580f27a2), and [A.3.2.1.2.2.1.2 - JRC Loss Allocation Rules](c201122a-75d2-44fa-b221-4e7c09bf42f2).

###### A.3.2.1.2.2.1.1.1.1 - Types Of Eligible Assets For IJRC [Core]  <!-- UUID: a2df2b73-c1c5-40d6-b87e-43ba24f54870 -->

The documents herein define the types of assets that qualify as Internal Junior Risk Capital.

These types will be specified in a future iteration of the Risk Framework.

###### A.3.2.1.2.2.1.1.2 - Prime-External Junior Risk Capital (PEJRC) [Core]  <!-- UUID: 00f61aa6-7bb4-4c7f-9492-2e2b2b4e78b2 -->

PEJRC is JRC rented from another Prime Agent via the [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce). The capital remains in the lender's treasury but counts towards the borrower's JRC amount. PEJRC is represented by a registered Ecosystem Accord signifying that a specified amount of the lending Agent's JRC (held within the lender's treasury) is designated to count towards the borrowing Agent's JRC requirement for the duration and terms specified in the Accord.

###### A.3.2.1.2.2.1.1.3 - Tokenized External Junior Risk Capital (TEJRC) [Core]  <!-- UUID: 6dd3c9c2-414b-4f06-bbc7-944f67e1cd89 -->

Tokenized External Junior Risk Capital is capital provided by external capital providers depositing sUSDS into the Tokenized External Junior Risk Capital smart contract, from which Primes can encumber funds. The details of this contract will be specified in a future iteration of the Atlas.

###### A.3.2.1.2.2.1.2 - JRC Loss Allocation Rules [Core]  <!-- UUID: c201122a-75d2-44fa-b221-4e7c09bf42f2 -->

This document defines the conceptual framework for distributing losses within the JRC layer.

###### A.3.2.1.2.2.1.2.1 - Initial Loss Absorption By "Tip JRC" [Core]  <!-- UUID: 6c33bcf5-c29d-48ca-9ee5-e37dcdeb0630 -->

The Tip JRC mechanism dictates that losses from a distinct risk event are first absorbed entirely by the Prime Agent's Internal Junior Risk Capital (IJRC), up to a specific threshold amount. This threshold amount is calculated as a percentage of Total JRC and is specified in [A.3.2.2.2.1 - JRC Loss Allocation Parameters](b718459e-57e0-414f-9c99-fbc82685cc0f).

Only losses exceeding this threshold amount trigger absorption by other Junior Risk Capital components - specifically, the remaining IJRC and External Junior Risk Capital. This initial absorption solely by IJRC ensures that Prime Agents are highly incentivized to prevent losses and avoids the need to resolve disputes regarding the allocation of small losses to EJRC providers.

###### A.3.2.1.2.2.1.2.2 - Post-Tip JRC Loss Allocation [Core]  <!-- UUID: 64cc7061-1bdf-4f1d-8300-fafb3743578b -->

If a loss event exceeds the Tip JRC amount, the remaining loss is allocated pro-rata across the rest of the JRC capital. This includes the remaining Internal Junior Risk Capital (Total IJRC minus the Tip amount) and all External Junior Risk Capital (Prime External Junior Risk Capital plus Tokenized External Junior Risk Capital).

###### A.3.2.1.2.2.1.2.3 - Per-Event Basis [Core]  <!-- UUID: ca685840-ab9a-4fa8-8f08-794536b94490 -->

The JRC loss allocation rules are applied independently based on the total losses attributed to each distinct risk event. The concept of "per-event basis" is crucial; the classification of a distinct risk event (classifying losses as one large event versus multiple smaller ones) can dictate whether the Tip JRC threshold is breached.

Breaching the threshold activates the pro-rata sharing mechanism for any losses exceeding the Tip JRC amount, distributing such excess losses between both the remaining Internal JRC (IJRC) and all External JRC (EJRC). Conversely, if the threshold is not breached for an event, the loss is contained entirely within the Tip layer and absorbed solely by IJRC.

The operational process for the determination of distinct risk events will be defined in a future iteration of the Atlas.

###### A.3.2.1.2.2.2 - Senior Risk Capital [Core]  <!-- UUID: 6bba2076-5d5b-43fd-82c6-df6a35f67355 -->

Senior Risk Capital (SRC) is protected from losses relative to Junior Risk Capital. Senior Risk Capital only begins to absorb losses after Junior Risk Capital has experienced 100% losses and absorbs 100% of losses thereafter.

Senior Risk Capital can be originated from Sky Core on a monthly basis as part of the Monthly Settlement Cycle; Prime Agents can also rent Senior Risk Capital from each other via the [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

###### A.3.2.1.2.2.2.1 - Senior Risk Capital Types [Core]  <!-- UUID: d2e9a92e-dd5d-4a26-8fc6-c5b47a2c06c2 -->

The documents herein define the types of Senior Risk Capital.

###### A.3.2.1.2.2.2.1.1 - Internal Senior Risk Capital [Core]  <!-- UUID: 09c20045-4b53-4370-98b8-a1199ccf7007 -->

Internal Senior Risk Capital (ISRC) is capital sourced from Aggregate Backstop Capital, as specified in [A.2.3.1.3 - Sourcing Of Internal Senior Risk Capital](ac7a6636-acbc-40c9-abc1-4543c0beb300).

###### A.3.2.1.2.2.2.1.2 - External Senior Risk Capital [Core]  <!-- UUID: 2adf8738-09b2-43e2-884c-c4ce6ff601ba -->

External Senior Risk Capital (ESRC) is capital provided from the srUSDS smart contract, which allow users to provide USDS to Sky Core to serve as senior risk capital in exchange for higher returns. The mechanics of this are specified in [A.3.2.2.4.2 - External Senior Risk Capital And srUSDS System](9fac0f6b-cb2d-4dc2-97d5-72c705303675).

##### A.3.2.1.2.3 - Total Risk Capital Sourcing Ratios [Core]  <!-- UUID: 9e99b084-f15a-4f60-b831-d6c0bd9aec04 -->

The documents herein define the required relationship and constraints between the different types of Total Risk Capital. These ensure that the Prime Agent maintains the appropriate level of Internal Junior Risk Capital relative to its External and Senior capital exposures, ensuring sufficient "skin in the game" with respect to its investments.

###### A.3.2.1.2.3.1 - Definition Of Ratios [Core]  <!-- UUID: e600afc0-6f8e-42a7-9413-9ef2f5cf0ebb -->

The documents herein define the Total Risk Capital sourcing ratios.

###### A.3.2.1.2.3.1.1 - External Per Internal Ratio [Core]  <!-- UUID: ff374833-920c-40f6-ae6c-a71d33d99b82 -->

The External Per Internal (EPI) ratio determines the maximum amount of External Junior Risk Capital (PEJRC and TEJRC combined) that a Prime Agent can source directly based on its held Internal Junior Risk Capital (IJRC). This acts as the primary constraint ensuring a baseline level of the Prime’s own capital backs its external JRC sourcing. The required External Per Internal ratio is specified in [A.3.2.2.2.2.1 - External Per Internal (EPI) Ratio Value](3ed32706-c072-42b5-b1e5-187bddf8dc37).

###### A.3.2.1.2.3.1.2 - Senior Per Junior Ratio [Core]  <!-- UUID: fbc9a273-d217-4d52-8b3e-b496580f27a2 -->

The Senior Per Junior (SPJ) ratio defines the effectiveness of each type of Junior Risk Capital (IJRC, PEJRC, TEJRC) in supporting Senior Risk Capital (SRC). Specifically, it quantifies how many units of SRC (whether Originated or Rented) can be activated or "enabled" per unit of a given JRC type.

A Prime Agent's overall "SPJ capacity" is calculated by summing the potential enablement contributed by each type of JRC it holds (IJRC, PEJRC or TEJRC), where each contribution equals the amount of that JRC type multiplied by its specific SPJ ratio.

Since SRC only absorbs losses after JRC is depleted, the SPJ enablement mechanism validates that sufficient JRC backing exists, allowing enabled SRC to be counted as part of the Prime Agent's total eligible Risk Capital. Therefore, a Prime Agent might hold a certain amount of OSRC or rented SRC, but only the portion that is successfully "enabled" by its JRC according to the SPJ ratios is accounted by the system as eligible capital contributing towards the Prime’s satisfaction of its Required Risk Capital. The required ratio of Senior Per Junior is specified in [A.3.2.2.2.2.2 - Senior Per Junior (SPJ) Ratio Values](8578e240-3fe8-41c0-8b2c-15ec9a7181ab).

###### A.3.2.1.2.3.1.2.1 - Alternative Use Of SPJ Capacity To Source External Junior Risk Capital [Core]  <!-- UUID: 03029174-91b4-4974-af1e-52438556a70b -->

A Prime Agent may optionally choose to deploy all or some portion of its calculated SPJ capacity not to enable Senior Risk Capital, but instead to source additional External Junior Risk Capital. This provides a secondary mechanism to increase the total JRC potentially beyond the amount initially constrained by the EPI ratio applied solely to IJRC.

Crucially, the EJRC tranche acquired through utilizing SPJ capacity is permanently accounted for as having an SPJ ratio of zero (0). It contributes to the JRC buffer but provides no capacity itself for enabling SRC in any subsequent calculations. This contrasts with EJRC sourced normally via the EPI ratio, which retains its standard SPJ capacity.

###### A.3.2.1.2.3.2 - Interaction Between Ratios And SPJ Capacity [Core]  <!-- UUID: e19dc42d-10d4-46d1-81e7-081f2f3e79f9 -->

The sourcing of External Junior Risk Capital and enablement of Senior Risk Capital involves a sequential application of the Risk Capital sourcing ratios in conjunction with the Prime Agent’s deployment of its SPJ capacity.

First, the EPI ratio sets the initial limit for sourcing standard, SPJ-bearing EJRC based solely on the Prime Agent’s IJRC.
Second, the total SPJ capacity is calculated from the Prime Agent’s resulting JRC pool (IJRC + any EPI-sourced EJRC).

Finally, this total calculated SPJ capacity can be allocated by the Prime Agent to enable SRC (standard use), and/or to source additional, non-SPJ-bearing EJRC using the mechanism described under [A.3.2.1.2.3.1.2.1 - Alternative Use Of SPJ Capacity To Source External Junior Risk Capital](03029174-91b4-4974-af1e-52438556a70b). Any specific portion of the total SPJ capacity allocated towards sourcing EJRC cannot simultaneously be allocated towards enabling SRC.

### A.3.2.2 - Implementation [Section]  <!-- UUID: e8ca3c08-3daf-4b36-bd5e-02b3eea0935a -->

This Section defines the current implementation of the Risk Capital framework.

#### A.3.2.2.1 - Required Risk Capital Calculation Implementation [Core]  <!-- UUID: d10b1c92-b839-45f1-995d-a23381fd6068 -->

The documents herein define the implementation of the Risk Framework for calculating required Total Instance RRC.

##### A.3.2.2.1.1 - Instance Financial RRC Implementation [Core]  <!-- UUID: aada206c-84bd-41e7-880d-1304889f4896 -->

The documents herein define the implementation of the Risk Framework for calculating Instance Financial RRC.

###### A.3.2.2.1.1.1 - Asset Class Specific Implementation [Core]  <!-- UUID: 8b6a6ecd-da74-4be5-bcb8-96215f473c08 -->

The documents herein define the calculation of Instance Financial RRC for specific asset classes.

###### A.3.2.2.1.1.1.1 - Lending Markets [Core]  <!-- UUID: d4e9c9e0-eeab-4399-99a0-5f72ff0d0e43 -->

The documents herein define the calculation of Instance Financial RRC for lending markets.

###### A.3.2.2.1.1.1.1.1 - Process For Calculating Instance Financial RRC [Core]  <!-- UUID: 0442fb55-5abb-4fa8-8f50-9a6f0bf6b86f -->

The documents herein define the process for calculating Instance Financial RRC for lending markets.

###### A.3.2.2.1.1.1.1.1.1 - Calculate Probability Of Default [Core]  <!-- UUID: 6766c25f-3e67-41e0-8b66-5af444c40572 -->

The first step is calculating the Probability Of Default $PD$. $PD$ is calculated using the following formula:

$$
\text{PD} = N(-d_1) + N(-d_2) \left( \frac{\sum_{i=1}^n \text{LT}_i V_0^i}{\sum_{j=1}^m D_0^j} \right)^{-2a}
$$

Here $N$ is the normal cumulative probability distribution function.

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.1.1.1.1.1.1 - Leverage Adjusted Drift To Risk Ratio [Core]  <!-- UUID: 0fcaf411-74e1-4b99-be50-40eb36bd6566 -->

The Leverage Adjusted Drift To Risk Ratio $a$ is calculated as follows:

$$
a = \frac{\sum_{i=1}^n w_U^i (r_c^i + r_s^i) - \sum_{j=1}^m w_D^j (r_d^j + r_s^j) + \rho_{UD} \sigma_U \sigma_D - \sigma_U^2}{\sigma_U^2 + \sigma_D^2 - 2 \rho_{UD} \sigma_U \sigma_D}
$$

###### A.3.2.2.1.1.1.1.1.1.2 - Distance To Default [Core]  <!-- UUID: b449741c-0144-406e-9d18-eabb050bcba0 -->

The Distance To Default $d_1$ is calculated using the following formula:

$$
d_1 = \frac{\ln\left( \frac{\sum_{i=1}^n \text{LT}_i V_0^i}{\sum_{j=1}^m D_0^j} \right) + \left( \sum_{i=1}^n w_U^i (r_c^i + r_s^i) - \sum_{j=1}^m w_D^j (r_d^j + r_s^j) + \rho_{UD} \sigma_U \sigma_D - \sigma_U^2 \right) T}{\sqrt{\sigma_U^2 + \sigma_D^2 - 2 \rho_{UD} \sigma_U \sigma_D} \sqrt{T}}
$$

###### A.3.2.2.1.1.1.1.1.1.3 - Downward Adjusted Distance To Default [Core]  <!-- UUID: 6eedb98a-0238-421a-9f8d-613859ddfcef -->

The Downward Adjusted Distance To Default $d_2$ is calculated using the following formula:

$$
d_2 = \frac{\ln\left( \frac{\sum_{i=1}^n \text{LT}_i V_0^i}{\sum_{j=1}^m D_0^j} \right) - \left( \sum_{i=1}^n w_U^i (r_c^i + r_s^i) - \sum_{j=1}^m w_D^j (r_d^j + r_s^j)+ \rho_{UD} \sigma_U \sigma_D - \sigma_U^2 \right) T}{\sqrt{\sigma_U^2 + \sigma_D^2 - 2 \rho_{UD} \sigma_U \sigma_D} \sqrt{T}}
$$

###### A.3.2.2.1.1.1.1.1.1.4 - Total Variance Of Underlying Asset Portfolio [Core]  <!-- UUID: d7f84a30-53f6-425c-afba-3ffc59e03e0f -->

The Total Variance Of Underlying Asset Portfolio $\sigma_U^2$ is calculated using the following formula:

$$
\sigma_U^2 = \sum_{i,k=1}^n w_U^i w_U^k \sigma_V^i \sigma_V^k \rho_{V,ik}
$$

###### A.3.2.2.1.1.1.1.1.1.5 - Total Variance Of Debt Portfolio [Core]  <!-- UUID: 1db43b96-d2eb-4563-87ad-d5046c21b66c -->

The Total Variance Of Debt Portfolio $\sigma_D^2$ is calculated using the following formula:

$$
\sigma_D^2 = \sum_{j,l=1}^m w_D^j w_D^l \sigma_D^j \sigma_D^l \rho_{D,jl}
$$

###### A.3.2.2.1.1.1.1.1.1.6 - Correlation Between Asset Portfolio And Debt Portfolio [Core]  <!-- UUID: ae1dbcb9-828d-40c0-8ad8-96b3072dad4e -->

The Correlation Between Asset Portfolio And Debt Portfolio $\rho_{UD}$ is calculated using the following formula:

$$
\rho_{UD} = \frac{\sum_{i=1}^n \sum_{j=1}^m w_U^i w_D^j \sigma_V^i \sigma_D^j \rho_{VD,ij}}{\sqrt{\sigma_U^2 \sigma_D^2}}
$$

###### A.3.2.2.1.1.1.1.1.1.7 - Weight Of Asset In Underlying Asset Portfolio [Core]  <!-- UUID: c614e705-59c8-40bd-aa15-c8d61c0ead4f -->

The weight of asset $i$ in the underlying asset portfolio $w_U^i$ is calculated using the following formula:

$$
w_U^i = \frac{\text{LT}_i V_0^i}{\sum_{k=1}^n \text{LT}_k V_0^k}
$$

###### A.3.2.2.1.1.1.1.1.1.8 - Weight Of Debt Instrument In Debt Portfolio [Core]  <!-- UUID: c5605290-8c64-4ed0-8fab-f2824488c4c9 -->

The weight of debt instrument $j$ in the debt portfolio $w_D^j$ is calculated using the following formula:

$$
w_D^j = \frac{D_0^j}{\sum_{l=1}^m D_0^l}
$$

###### A.3.2.2.1.1.1.1.1.1.9 - Return On Asset [Core]  <!-- UUID: 9f322c61-92d7-4ff5-aa9b-523e124c8748 -->

The Return On Asset $r_c^i$ of an asset $i$ is the yield earned for supplying the asset in the lending market.

###### A.3.2.2.1.1.1.1.1.1.10 - Asset Yield [Core]  <!-- UUID: e0fea8fd-3925-463b-ab0d-3ff9fee1298d -->

The Asset Yield $r_s^i$ of an asset $i$ is the income yield of the asset and would include any dividends or interest paid by the asset and/or asset issuer, including staking rewards for yield-bearing assets.

###### A.3.2.2.1.1.1.1.1.1.11 - Cost Of Debt [Core]  <!-- UUID: 5051029f-8e9c-4234-9951-c6a95fc0cddb -->

The Cost Of Debt $r_d^j$ of a debt instrument $j$ is the interest rate on the debt.

###### A.3.2.2.1.1.1.1.1.1.12 - Debt Yield [Core]  <!-- UUID: 022a0b3b-18db-4440-9868-be62ad2f6d47 -->

The Debt Yield $r_s^j$ of a debt instrument $j$ is the income yield on the debt asset. It includes any dividends or interest paid by the debt asset and/or debt asset issuer, including staking rewards for yield-bearing debt assets.

###### A.3.2.2.1.1.1.1.1.1.13 - Correlation Coefficient [Core]  <!-- UUID: 0663022c-c7bf-49db-800c-c186e9819455 -->

The correlation coefficient $\rho$ between two instruments is the correlation of block-weighted log returns of those assets over the last 365 days. In the documents herein, the correlation coefficient is followed by subscripts indicating the relevant instruments. For example, $\rho_{UD}$ is the correlation between the underlying asset portfolio $U$ and the debt portfolio $D$ as specified in [A.3.2.2.1.1.1.1.1.1.6 - Correlation Between Asset Portfolio And Debt Portfolio](ae1dbcb9-828d-40c0-8ad8-96b3072dad4e). The subscript may begin with $V$ or $D$ to indicate whether the relevant instruments are part of the asset portfolio or debt portfolio. For example, $\rho_{VD,ij}$ is the correlation coefficient between the asset $i$ and the debt instrument $j$.

###### A.3.2.2.1.1.1.1.1.1.14 - Liquidation Threshold [Core]  <!-- UUID: ce774017-be30-4482-8df7-361875cb771d -->

The Liquidation Threshold $LT_i$ is the value of the debt as a percentage of the collateral value at which the lender may liquidate the collateral to satisfy the debt.

###### A.3.2.2.1.1.1.1.1.1.15 - Asset Value [Core]  <!-- UUID: 63b212be-2bde-43b3-ba61-7ebf9c442137 -->

The Asset Value $V_0^i$ of an asset $i$ is the market value of that asset.

###### A.3.2.2.1.1.1.1.1.1.16 - Debt Value [Core]  <!-- UUID: 65032e2b-5da8-4fed-b893-20b18e13383b -->

The Debt Value $D_0^i$ of a debt instrument is the notional value of the debt.

###### A.3.2.2.1.1.1.1.1.1.17 - Time Horizon [Core]  <!-- UUID: 9dc1abf3-365b-4ed5-b4aa-fdbb9024e0e2 -->

The Time Horizon $T$ is the time horizon in years over which the Probability Of Default is being estimated. The value of the $T$ parameter is `1`.

###### A.3.2.2.1.1.1.1.1.2 - Calculate Loss Given Default [Core]  <!-- UUID: c9bd4928-d054-4e89-9a98-720c439b0db3 -->

The second step is calculating the Loss Given Default $LGD$. $LGD$ is calculated using the following formula:

$$
LGD = min(1 - \frac{(1 - LP) * (1 - S)}{LT}, 0)
$$

Here $min$ is the mathematical minimum function that returns the lower of the two specified parameters.

The parameters of this formula are specified in the subdocuments herein. All of these parameters should be specified as decimal numbers. For example, 3% should be specified as `0.03`.

###### A.3.2.2.1.1.1.1.1.2.1 - Liquidation Penalty [Core]  <!-- UUID: bce9331b-04ca-4c50-9783-098739fc72c8 -->

The Liquidation Penalty $LP$ is the contractually agreed upon liquidation penalty if the asset is liquidated to satisfy the debt.

###### A.3.2.2.1.1.1.1.1.2.2 - Slippage [Core]  <!-- UUID: f2612a0d-6bf8-470b-b5b6-884567e1317b -->

The Slippage $S$ is the estimated slippage for liquidating the entire position in one block. The estimated slippage should not exceed 25%.

###### A.3.2.2.1.1.1.1.1.2.3 - Liquidation Threshold [Core]  <!-- UUID: f1d3990a-f398-454f-82ed-272052d1ad08 -->

The Liquidation Threshold $LT$ is the value of the debt as a percentage of the collateral value at which the lender may liquidate the collateral to satisfy the debt.

###### A.3.2.2.1.1.1.1.1.3 - Calculate Asset Correlation Coefficient [Core]  <!-- UUID: bbf43294-09c2-413a-b0a4-745cb72d1cd8 -->

The third step is to calculate the Asset Correlation Coefficient $R$. $R$ is calculated as follows:

$$
R = a \times \left(1 - e^{-K \times PD}\right) + b \times \left(1 - \left(1 - e^{-K \times PD}\right)\right)
$$

Here $e$ is the base of the natural logarithm.

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.1.1.1.1.3.1 - Lower Bound [Core]  <!-- UUID: 68c5da4f-9c4e-4206-a582-99be9833481f -->

The Lower Bound $a$ is an estimate of the correlation between assets during "calm" periods. It is set of `0.13`.

###### A.3.2.2.1.1.1.1.1.3.2 - Upper Bound [Core]  <!-- UUID: 71136e6a-d0f5-443b-b834-40d39234e707 -->

The Upper Bound $b$ is an estimate of the correlation between assets during "stressful" market environments. It is set to `0.33`.

###### A.3.2.2.1.1.1.1.1.3.3 - Sensitivity Coefficient [Core]  <!-- UUID: 3b7924b2-1236-43cb-b0f0-ebe06f573b78 -->

The Sensitivity Factor `K` is a tuning parameter indicating how quickly the correlations transition between $a$ and $b$. It is set to `10`.

###### A.3.2.2.1.1.1.1.1.4 - Calculate Capital Requirement Without Buffers [Core]  <!-- UUID: 152bc5d8-7642-424c-b5fc-9242479f705e -->

The fourth step is to calculate the Capital Requirement Without Buffers $K$. $K$ is calculated as follows:

$$
K = \left[ LGD \times N\left( \frac{N^{-1}(PD) + \sqrt{R} \cdot N^{-1}(0.999)}{\sqrt{1-R}} \right) - PD \times LGD \right]
$$

Here $N$ is the cumulative normal probability distribution function and $N^{-1}$ is the inverse cumulative normal probability distribution function.

###### A.3.2.2.1.1.1.1.1.5 - Calculate Required Risk Capital [Core]  <!-- UUID: fc471b5a-6741-4f50-aa69-302a34479526 -->

The final step is to calculate the Instance Financial RRC $RRC$. $RRC$ is calculated as follows:

$$
\text{RRC} = K \times \frac{1}{CR} \times \text{EAD} \times \text{ECR}
$$

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.1.1.1.1.5.1 - Capital Ratio [Core]  <!-- UUID: 4a1d377d-eb0e-481a-a447-9ff3630b8787 -->

The Capital Ratio $CR$ is the capital ratio without additional buffers. It is set to `8.75%`.

###### A.3.2.2.1.1.1.1.1.5.2 - Exposure At Default [Core]  <!-- UUID: 49ed449e-6caf-4b70-9b9f-eef294f80c0e -->

The Exposure At Default $EAD$ is the total amount of funds from the Allocation System that have been deployed into the decentralized lending protocol.

###### A.3.2.2.1.1.1.1.1.5.3 - Effective Capital Ratio [Core]  <!-- UUID: 3b4c7006-0bb1-4885-9c57-e97abf3d59e9 -->

The Effective Capital Ratio $ECR$ is the capital ratio included additional capital buffers established by Sky Governance as part of the Risk Framework. There are currently no additional capital buffers so the $ECR$ is equal to the $CR$, which is `8.75%`.

###### A.3.2.2.1.1.1.1.2 - Covered Protocols [Core]  <!-- UUID: 881a9eee-1d05-4394-b0eb-cad2f9c1b181 -->

The calculation of Instance Financial RRC for lending markets is applicable to the following protocols:

- Aave v2
- Aave v3
- SparkLend
- Morpho
- Maple

The application by a Prime Agent of the Risk Framework for lending markets to any protocols not listed above must be approved by the Core Executor Agents. The Core Executor Agents shall consult with the Core Council Risk Advisor in making this determination. Any such approval must be posted to the Sky Forum under the category for the Prime Agent.

###### A.3.2.2.1.1.1.1.3 - Exceptions [Core]  <!-- UUID: 21cd7356-14c9-42f1-adc0-883655ad4795 -->

The documents herein define exceptions to the calculation of Instance Financial RRC for specific lending protocols.

###### A.3.2.2.1.1.1.1.3.1 - Maple [Core]  <!-- UUID: d3000c93-d5d5-4a9e-b8c7-484aa3d16633 -->

The Instance Financial CRR for Maple SyrupUSDC is 3%.

The maximum exposure a Prime Agent may have to Maple SyrupUSDC will be specified in a future iteration of the Atlas.

###### A.3.2.2.1.1.1.1.3.2 - Fluid [Core]  <!-- UUID: ef7403c9-8663-4759-b5aa-9496eca1f475 -->

The Instance Financial CRR for Fluid is 3% of the amount of funds supplied to Fluid that are borrowed.

###### A.3.2.2.1.1.1.1.3.3 - Ethena-Related Assets [Core]  <!-- UUID: e831249e-f81a-496a-b9b9-17229c2683dd -->

The portion of exposure to lending markets that is backed by Ethena-related assets is not subject to the standard Instance Financial RRC calculation. Instead, an alternative calculation method applies: the Instance Financial CRR for indirect Ethena exposure through lending markets should be applied for this portion. See [A.3.2.2.1.1.1.2.1 - Near-Term Treatment](92727d50-1ca0-48a9-93a0-0e504e845654). This portion of exposure is calculated based on the proportional debt amount backed by Ethena-related assets, weighted by the collateral amount times liquidation threshold.

###### A.3.2.2.1.1.1.1.3.4 - Aave And SparkLend [Core]  <!-- UUID: 5ac25db9-6567-4b83-88a2-59e295db6ed8 -->

Because Aave and SparkLend liquidate a maximum of 50% of a user’s position, the Slippage parameter for Aave and SparkLend should be the estimated slippage for liquidating half of the position in one block. See [A.3.2.2.1.1.1.1.1.2.2 - Slippage](f2612a0d-6bf8-470b-b5b6-884567e1317b).

###### A.3.2.2.1.1.1.1.3.5 - Kamino [Core]  <!-- UUID: 836668a9-235b-458d-80fa-91a9d08c84b4 -->

The CRR for Kamino is:

- 4.98% for USDG on JLP market
- 4.94% for USDC on JLP market
- 4.91% for USDT on JLP market
- 4.87% for PYUSD on JLP market
- 1.60% for USDG on Main market
- 1.58% for USDC on Main market
- 1.48% for EURC on Main market
- 0.91% for PYUSD on Main market
- 0.78% for USDT on Main market
- 0.77% for USDS on Main market
- 2.12% for USDC on Maple market
- 0.75% for USDS on Maple market

The maximum exposure a Prime Agent may have to Kamino may not exceed 25,000,000 USDS.

###### A.3.2.2.1.1.1.1.3.6 - Drift [Core]  <!-- UUID: 05036471-be13-42e6-b278-7ae128de708b -->

The CRR for Drift is:

- 3.51% for USDe on Main market
- 3.49% for USDC on Main market
- 2.67% for EURC on Main market
- 2.26% for sUSDe on Main market
- 2.24% for USDY on Main market
- 1.90% for USDT on Main market
- 1.84% for AUSD on Main market
- 1.82% for syrupUSDC on Main market
- 1.59% for PYUSD on Main market
- 1.55% for USDS on Main market
- 1.52% for USDC on JLP market

The maximum exposure a Prime Agent may have to Drift may not exceed 25,000,000 USDS.

###### A.3.2.2.1.1.1.1.3.7 - Anchorage [Core]  <!-- UUID: 3f49b256-b18d-4a2a-b5a9-f55318455a3c -->

Offchain lending through Anchorage Digital has a CRR of 3%. The maximum exposure is 500,000,000 USD. The terms of this offchain lending must conform to the following specifications:

- Collateral Asset: Native BTC
- Initial LTV: 80% (125% collateralization ratio)
- Margin Call LTV: 85% (117.6% collateralization ratio)
- Margin Call Period: 24 hours
- Liquidation LTV: 90% (111.1% collateralization ratio)
- Maturity Date: Approximately 6-month duration

###### A.3.2.2.1.1.1.1.3.8 - Morpho Vaults [Core]  <!-- UUID: 6cef23c7-aaae-493d-bd76-a2909c25970a -->

The documents herein define the Instance Financial CRR applied to specific Morpho vault allocations.

###### A.3.2.2.1.1.1.1.3.8.1 - Morpho Grove x Steakhouse High Yield USDC Vault [Core]  <!-- UUID: f3df0565-407c-43bb-9b3e-52bbc5223a26 -->

The CRRs for the following market allocations in the vault are:

- PT-USDe / USDC – LLTV: 91.5%
    - CRR = 4%
- PT-sUSDe / USDC – LLTV: 91.5%
    - CRR = 4%
- PT-cUSD0 / USDC – LLTV: 91.5%
    - CRR = 1%
- mF-One / USDC – LLTV: 91.5%
    - CRR = 100%

###### A.3.2.2.1.1.1.1.3.9 - Uniswap V3 [Core]  <!-- UUID: 200cd606-26e9-427e-b965-976e7140a976 -->

Allocation to the AUSD / USDC Uniswap v3 pool via FalconX on Monad has a CRR of 3%. Total combined FalconX allocations must not exceed 100,000,000 USDS.

###### A.3.2.2.1.1.1.1.3.10 - Galaxy Warehouse [Core]  <!-- UUID: edbd7845-ac1e-4a48-a725-89632e225849 -->

The Instance Financial CRR for Galaxy Warehouse is 2%. The maximum exposure is 500,000,000 USD.

###### A.3.2.2.1.1.1.1.4 - Unauthorized Exposures [Core]  <!-- UUID: 6a103b6f-53ef-4666-870c-92cfbff6d099 -->

An underlying asset of a lending market in which a Prime Agent has invested that was not included in the pro-forma Required Risk Capital estimate approved by the Core Council Risk Advisor, as specified in [A.2.2.10.1.1.2.3 - Instance Setup Deployments](3766cb8c-ab6c-41af-9465-b8dea76d0532), constitutes an Unauthorized Exposure. Because the risk of an Unauthorized Exposure has not been assessed, its Capital Ratio Requirement is 100%, applying at the exposure level the full-reservation principle specified in [A.3.2.1.1.3.2 - Inability To Calculate Types Of RRC](268af0e9-be3d-458e-9ccd-5a560abc7540). An Instance's Capital Ratio Requirement is the capital-weighted aggregate of its exposures' Capital Ratio Requirements, so an Instance with only a fraction of its capital in Unauthorized Exposures has a Capital Ratio Requirement below 100%.

###### A.3.2.2.1.1.1.1.5 - Reference Implementation [Core]  <!-- UUID: e96da090-34ff-4445-a1d3-22cc69be2e51 -->

A reference implementation of the calculation of Instance Financial RRC for lending markets is included herein.

`import math
from collections import defaultdict
import numpy as np
from scipy.stats import norm

# Constants
RISK_FREE_RATE = 0.04  # SOFR
TIME_HORIZON = 1       # 1 year

class FinancialRRCModel:
    def __init__(self):
        # For demo purposes, we hardcode a dummy correlation map
        self.token_correlation_map = {
            'TOKENA': {'TOKENB': 0.5},
            'TOKENB': {'TOKENA': 0.5},
        }

    def _calculate_effective_volatility(self, list_1, list_2):
        """
        Calculate the effective variance between two sets of positions.
        """
        effective_variance = 0.0
        for sym1, pos1 in list_1.items():
            for sym2, pos2 in list_2.items():
                if sym1 == sym2:
                    corr = 1.0
                else:
                    corr = self.token_correlation_map.get(sym1, {}).get(sym2,
                           self.token_correlation_map.get(sym2, {}).get(sym1, 0.0))
                effective_variance += (
                    pos1["share"]
                    * pos2["share"]
                    * pos1["volatility_30d"]
                    * pos2["volatility_30d"]
                    * corr
                )
        return effective_variance

    def _estimate_rrc_for_position(self, wallet_data):
        """
        Estimate the required-risk capital (RRC) for a given wallet_data dict.
        """
        # 1) compute effective volatilities
        var_coll = self._calculate_effective_volatility(
            wallet_data["collateral_positions"],
            wallet_data["collateral_positions"],
        )
        var_debt = self._calculate_effective_volatility(
            wallet_data["debt_positions"],
            wallet_data["debt_positions"],
        )
        vol_coll = math.sqrt(var_coll)
        vol_debt = math.sqrt(var_debt)

        # 2) correlation collateral↔debt
        cov_cd = self._calculate_effective_volatility(
            wallet_data["collateral_positions"],
            wallet_data["debt_positions"],
        )
        corr_cd = cov_cd / (vol_coll * vol_debt) if vol_coll * vol_debt > 0 else 0.0

        # 3) drift terms
        eff_coll_rate = sum(p["share"] * p["supply_apy_30d"]
                            for p in wallet_data["collateral_positions"].values())
        eff_borrow_rate = sum(p["share"] * p["borrow_apy_30d"]
                              for p in wallet_data["debt_positions"].values())
        eff_stake_rate = sum(p["share"] * p["staking_apy_30d"]
                             for p in wallet_data["collateral_positions"].values())

        drift_cd = (
            eff_coll_rate + eff_stake_rate - eff_borrow_rate
            + (var_debt - var_coll) / 2
        )

        vol_cd = math.sqrt(
            max(var_coll + var_debt - 2 * corr_cd * vol_coll * vol_debt, 0)
        )

        # 4) Black-Cox inputs
        a = (drift_cd - vol_cd**2 / 2) / (vol_cd**2) if vol_cd > 0 else 0.0
        L = wallet_data["collateral_usd_lt"]
        D = wallet_data["debt_usd"]
        log_term = math.log(L / D) if L > 0 and D > 0 else float("-inf")
        denom = vol_cd * math.sqrt(TIME_HORIZON) if vol_cd > 0 else 1e-10

        d1 = (log_term + (drift_cd - vol_cd**2/2) * TIME_HORIZON) / denom
        d2 = (log_term - (drift_cd - vol_cd**2/2) * TIME_HORIZON) / denom

        # 5) Probability of Default
        try:
            pd = (
                norm.cdf(-d1)
                + norm.cdf(-d2) * (L / D) ** (-2 * a)
            )
        except OverflowError:
            pd = 1.0
        pd = max(0.0, min(pd, 1.0))

        # 6) Loss Given Default
        recovery = sum(
            p["share"] * (1 - p["liquidation_penalty"]) * (1 - p["slippage"])
            / p["liquidation_threshold"]
            for p in wallet_data["collateral_positions"].values()
        )
        lgd = max(0.0, min(1 - recovery, 1.0))

        # 7) Exposure at Default
        ead = sum(
            debt["debt_usd"] * math.exp((RISK_FREE_RATE + debt["borrow_apy_30d"]) * TIME_HORIZON)
            for debt in wallet_data["debt_positions"].values()
        )

        # 8) Asset Correlation Coefficient
        a_acc, b_acc, c_acc = 0.13, 10, 0.33
        exp_term = math.exp(-b_acc * pd)
        acc = a_acc * (1 - exp_term)/(1-math.exp(-b_acc)) + c_acc*(1 - (1-exp_term)/(1-math.exp(-b_acc)))

        # 9) Credit risk weight
        default_threshold = (
            norm.ppf(max(pd, 1e-10)) + math.sqrt(acc) * norm.ppf(0.999)
        ) / math.sqrt(1 - acc)
        credit_risk = max(lgd * norm.cdf(default_threshold) - lgd * pd, 0)

        # 10) RRC
        rrc = credit_risk * ead
        return rrc

# -------- DEMO USAGE --------

if __name__ == "__main__":
    # 1) Build a dummy wallet_data structure
    wallet_data = {
        "collateral_positions": {
            "TOKENA": {
                "share": 0.6,
                "volatility_30d": 0.2,
                "supply_apy_30d": 0.05,
                "staking_apy_30d": 0.02,
                "liquidation_penalty": 0.1,
                "liquidation_threshold": 0.8,
                "slippage": 0.01,
            },
            "TOKENB": {
                "share": 0.4,
                "volatility_30d": 0.25,
                "supply_apy_30d": 0.04,
                "staking_apy_30d": 0.015,
                "liquidation_penalty": 0.12,
                "liquidation_threshold": 0.85,
                "slippage": 0.015,
            },
        },
        "debt_positions": {
            "TOKENA": {
                "share": 0.7,
                "volatility_30d": 0.2,
                "borrow_apy_30d": 0.06,
                "debt_usd":  100_000,
            },
            "TOKENB": {
                "share": 0.3,
                "volatility_30d": 0.25,
                "borrow_apy_30d": 0.07,
                "debt_usd":  50_000,
            },
        },
        "collateral_usd_lt": 200_000,
        "debt_usd": 150_000,
    }

    # 2) Instantiate and run
    model = FinancialRRCModel()
    rrc = model._estimate_rrc_for_position(wallet_data)
    print(f"Estimated Required Risk Capital (RRC): ${rrc:,.2f}")
`

###### A.3.2.2.1.1.1.2 - Perpetual Positions [Core]  <!-- UUID: 69fac7fa-6168-4b74-99cc-28b557826556 -->

The implementation of the model for perpetual positions will be specified in a future iteration of the Atlas. The near-term treatment of these assets are specified in the subdocuments herein.

###### A.3.2.2.1.1.1.2.1 - Near-Term Treatment [Core]  <!-- UUID: 92727d50-1ca0-48a9-93a0-0e504e845654 -->

In the near term pending development of the implementation of the model for perpetual positions, the Instance Financial CRRs specified in the documents herein will apply.

###### A.3.2.2.1.1.1.2.1.1 - Ethena [Core]  <!-- UUID: f999239e-8676-4772-b201-2e00920b2bfb -->

The near-term treatment for Ethena is specified in the documents herein.

###### A.3.2.2.1.1.1.2.1.1.1 - Ethena Capital Ratio Requirement [Core]  <!-- UUID: 7ce05a43-e3ec-4c54-a11e-30e56526cfdd -->

Ethena Exposures consist of Direct Ethena Exposures (see [A.3.2.2.1.1.1.2.1.1.1.1 - Direct Ethena Exposures](e0fa035c-e8f3-4cd2-8ca1-a6afbd1825eb)), Indirect Ethena Exposures (see [A.3.2.2.1.1.1.2.1.1.1.2 - Indirect Ethena Exposures](d549b42d-a62e-4a5c-98a8-0ddc72aa6a67)), and Pendle Ethena Exposures (see [A.3.2.2.1.1.1.2.1.1.1.3 - Pendle Ethena Exposures](4094c159-9132-454a-81be-361a461b5098)). The Instance Financial CRR for Ethena Exposures is specified in the documents herein.

###### A.3.2.2.1.1.1.2.1.1.1.1 - Direct Ethena Exposures [Core]  <!-- UUID: e0fa035c-e8f3-4cd2-8ca1-a6afbd1825eb -->

Direct Ethena Exposures are exposures from directly holding USDe and sUSDe. Direct Ethena Exposures have a 3% Instance Financial CRR.

###### A.3.2.2.1.1.1.2.1.1.1.2 - Indirect Ethena Exposures [Core]  <!-- UUID: d549b42d-a62e-4a5c-98a8-0ddc72aa6a67 -->

Indirect Ethena Exposures are exposures from lending against Ethena related assets through lending markets. Indirect Ethena Exposures have Instance Financial CRR as specified in the documents herein.

For Indirect Ethena Exposure through lending markets, only the portion of the exposure to the lending market that is backed by Ethena related assets is subject to the Instance Financial CRR specified in the documents herein. The Instance Financial CRR for the remaining portion of the exposure is calculated based on the nature of the assets backing the exposure.

###### A.3.2.2.1.1.1.2.1.1.1.2.1 - Lending Ethena Related Assets Against Ethena Related Collateral [Core]  <!-- UUID: cfa615fb-9927-4059-873a-7c824a517835 -->

For Ethena related assets lent against Ethena related collateral (e.g. lending USDe or sUSDe against PT-USDe or PT-sUSDe), the Instance Financial CRR is 3%.

###### A.3.2.2.1.1.1.2.1.1.1.2.2 - Lending Non-Ethena Related Assets Against Ethena Related Collateral [Core]  <!-- UUID: dadc95a6-c8ef-4abb-b9a5-d51bf2c0bf29 -->

For non-Ethena related assets lent against Ethena related collateral (e.g. lending USDC against PT-USDe or PT-sUSDe), the Instance Financial CRR is 4%.

###### A.3.2.2.1.1.1.2.1.1.1.3 - Pendle Ethena Exposures [Core]  <!-- UUID: 4094c159-9132-454a-81be-361a461b5098 -->

Pendle Ethena Exposures are exposures from directly holding PT-USDe or PT-sUSDe. The Instance Financial CRR for Pendle Ethena Exposures is specified in the documents herein.

###### A.3.2.2.1.1.1.2.1.1.1.3.1 - Maturity Greater Than Six Months [Core]  <!-- UUID: ee9246d9-7500-4cd6-a934-0d2312d9e2a6 -->

Pendle Ethena Exposures with more than six (6) months to maturity require 100% Instance Total CRR.

###### A.3.2.2.1.1.1.2.1.1.1.3.2 - Maturity Less Than Or Equal To Six Months [Core]  <!-- UUID: 6ed19cc0-5447-4df9-a9c1-45c8730f5f44 -->

Pendle Ethena Exposures with less than or equal to six (6) months to maturity have Instance Financial CRR calculated as follows:

`Instance Financial CRR = initialValue - ((currentTime - startTime) * decayRatePerSecond)`

The parameters of this formula are defined in the documents herein.

###### A.3.2.2.1.1.1.2.1.1.1.3.2.1 - Initial Value [Core]  <!-- UUID: 5d2d2430-2fd5-4418-a688-e8f091eb44b9 -->

The Initial Value `initialValue` is the Instance Financial CRR when the PT has exactly six (6) months to maturity. The `initialValue` is 10%.

###### A.3.2.2.1.1.1.2.1.1.1.3.2.2 - Current Time [Core]  <!-- UUID: 340be283-72fe-4b51-9d75-d7f3c28fdab2 -->

The Current Time `currentTime` is the timestamp of the current Ethereum block.

###### A.3.2.2.1.1.1.2.1.1.1.3.2.3 - Start Time [Core]  <!-- UUID: 461eef24-5b4d-44b2-8281-a8c86bc4bc40 -->

The Start Time `startTime` is the timestamp of the block exactly six (6) months before the expiration timestamp of the PT.

###### A.3.2.2.1.1.1.2.1.1.1.3.2.4 - Decay Rate Per Second [Core]  <!-- UUID: cda560ff-5b25-44e1-bad4-e6ccfefdf7eb -->

The Decay Rate Per Second `decayRatePerSecond` is calculated as follows:

`decayRatePerSecond = totalDecay / totalDuration`

The parameters of this formula are defined in the documents herein.

###### A.3.2.2.1.1.1.2.1.1.1.3.2.4.1 - Total Decay [Core]  <!-- UUID: c5530d25-b8ef-4ebe-9b38-7b2a29014ff3 -->

The Total Decay `totalDecay` is equal to the Initial Value minus the Final Value.

###### A.3.2.2.1.1.1.2.1.1.1.3.2.4.1.1 - Final Value [Core]  <!-- UUID: 900ecd08-64b7-4f37-8539-f4e822f11d98 -->

The Final Value is the Instance Financial CRR when the PT is at maturity. Since the PT is convertible into the underlying asset at this point it is equal to the Instance Financial CRR for Direct Ethena Exposures specified in [A.3.2.2.1.1.1.2.1.1.1.1 - Direct Ethena Exposures](e0fa035c-e8f3-4cd2-8ca1-a6afbd1825eb).

###### A.3.2.2.1.1.1.2.1.1.1.3.2.4.2 - Total Duration [Core]  <!-- UUID: 0e21a4c4-cd66-4ace-9dcd-6015fc9e4966 -->

The Total Duration `totalDuration` is equal to the Expiration Time minus the Start Time.

###### A.3.2.2.1.1.1.2.1.1.1.3.2.4.2.1 - Expiration Time [Core]  <!-- UUID: 537db44c-1b07-49bd-8b26-0174e3a2f34a -->

The Expiration Time is the expiration timestamp of the PT.

###### A.3.2.2.1.1.1.2.1.1.1.3.3 - Concentration Limit [Core]  <!-- UUID: 6f850537-5e8a-4e57-95c8-f57a099ed8f3 -->

Any investments made by Prime Agents in Pendle Ethena Exposures in excess of 20% of their total Allocation System Investments require 100% Instance Total CRR.

###### A.3.2.2.1.1.1.2.1.1.2 - Ethena Aggregate Exposure Limits [Core]  <!-- UUID: 31757562-7f99-4d4e-b4e6-a7b0028e5d4d -->

The documents herein define aggregate exposure limits applicable to Ethena.

###### A.3.2.2.1.1.1.2.1.1.2.1 - Ethena Aggregate Exposure [Core]  <!-- UUID: 642b6bee-9702-4339-bda3-3a35d025bbcc -->

Ethena Aggregate Exposure is the sum of Ethena Exposures (see [A.3.2.2.1.1.1.2.1.1.1 - Ethena Capital Ratio Requirement](7ce05a43-e3ec-4c54-a11e-30e56526cfdd)) across all Prime Agents in the Sky Ecosystem.

###### A.3.2.2.1.1.1.2.1.1.2.2 - Ethena Aggregate Exposure Limit [Core]  <!-- UUID: 176c8562-848c-4868-8490-8e64da24adcd -->

The Ethena Aggregate Exposure Limit is 1,300,000,000 USDS.

###### A.3.2.2.1.1.1.2.1.1.2.3 - Ethena Exposure Limit [Core]  <!-- UUID: 8e120edf-c87b-4d99-8f2a-65fb49bcc3b7 -->

The Ethena Exposure Limit for each Agent is:

- Spark - One half of the Ethena Aggregate Exposure Limit
- Grove - One half of the Ethena Aggregate Exposure Limit
- All other Prime Agents - Zero

###### A.3.2.2.1.1.1.2.1.1.2.4 - Prohibition On Investments That Would Cause Ethena Exposure Limit To Be Exceeded [Core]  <!-- UUID: 50854ba8-c788-4df5-9c70-b6f070a28bfd -->

No Prime Agent may make an investment in Ethena Exposures that would cause its Ethena Exposures to exceed its Ethena Exposure Limit.

###### A.3.2.2.1.1.1.2.1.1.2.5 - Sale Of Investments When Ethena Exposure Limit Is Exceeded [Core]  <!-- UUID: 81e64445-f74c-4d61-8322-b2d30d3582f1 -->

If a Prime Agent’s Ethena Exposures exceed its Ethena Exposure Limit, then the Core Council may direct the Agent to sell Ethena Exposures to reduce its Ethena Exposures below its Ethena Exposure Limit.

###### A.3.2.2.1.1.1.2.1.2 - Superstate [Core]  <!-- UUID: 465472b5-acc2-4a8e-9a42-543e16854e71 -->

The near-term treatment for Superstate is specified in the documents herein.

###### A.3.2.2.1.1.1.2.1.2.1 - Superstate Capital Ratio Requirement [Core]  <!-- UUID: ffca1065-7f92-4815-8a65-52bdbc82c558 -->

Superstate Exposures are exposures from holding USCC. Superstate Exposures have a 4.5% Instance Financial CRR.

###### A.3.2.2.1.1.1.2.1.2.2 - Superstate Aggregate Exposure Limits [Core]  <!-- UUID: f5348df6-6161-454d-a8d4-bd02d2acc354 -->

The documents herein define aggregate exposure limits applicable to Superstate Exposures.

###### A.3.2.2.1.1.1.2.1.2.2.1 - Superstate Aggregate Exposure [Core]  <!-- UUID: 6cf2221f-214c-4bc2-8de1-b0d6adb2a327 -->

Superstate Aggregate Exposure is the sum of Superstate Exposures (see [A.3.2.2.1.1.1.2.1.2.1 - Superstate Capital Ratio Requirement](ffca1065-7f92-4815-8a65-52bdbc82c558)) across all Prime Agents in the Sky Ecosystem.

###### A.3.2.2.1.1.1.2.1.2.2.2 - Superstate Aggregate Exposure Limit [Core]  <!-- UUID: ea606bf7-6dbf-41d2-a993-79b66c56b7c2 -->

The Superstate Aggregate Exposure Limit is 500,000,000 USDS.

###### A.3.2.2.1.1.1.2.1.2.2.3 - Prohibition On Investments That Would Cause Superstate Aggregate Exposure Limit To Be Exceeded [Core]  <!-- UUID: a75e7eea-7567-4f5c-aba4-6d41fb6732dd -->

No Prime Agent may make an investment in Superstate Exposures that would cause the Superstate Aggregate Exposure to exceed the Superstate Aggregate Exposure Limit.

###### A.3.2.2.1.1.1.2.1.2.2.4 - Sale Of Investments When Superstate Aggregate Exposure Limit Is Exceeded [Core]  <!-- UUID: ee3016e5-521a-4f86-a684-aa66bd102c8f -->

If the Superstate Aggregate Exposure exceeds the Superstate Aggregate Exposure Limit, then the Core Council may direct Prime Agents to sell Superstate Exposures to reduce the Superstate Aggregate Exposure below the Superstate Aggregate Exposure Limit.

###### A.3.2.2.1.1.1.2.1.2.3 - Superstate Deployment Limits [Core]  <!-- UUID: d0b3b345-23c1-4cb0-9d16-aa7b44ff7294 -->

The documents herein define the deployment limits applicable to Superstate Exposures.

###### A.3.2.2.1.1.1.2.1.2.3.1 - Superstate Initial Deployment Limit [Core]  <!-- UUID: 3fd57a2e-3e2a-41c1-a9f7-cfbe58799837 -->

The Initial Deployment is the first deployment of capital by a Prime Agent into Superstate Exposures. The Initial Deployment may not exceed 20,000,000 USDS.

###### A.3.2.2.1.1.1.2.1.2.3.2 - Superstate Subsequent Deployment Limits [Core]  <!-- UUID: e36d7537-95f8-4156-955f-bc74d37935d8 -->

Subsequent Deployments are deployments of capital by a Prime Agent into Superstate Exposures after its Initial Deployment (see [A.3.2.2.1.1.1.2.1.2.3.1 - Superstate Initial Deployment Limit](3fd57a2e-3e2a-41c1-a9f7-cfbe58799837)). Each Subsequent Deployment may not exceed 50,000,000 USDS and requires approval from the Core Council Risk Advisor on behalf of the Core Council.

###### A.3.2.2.1.1.1.3 - Direct Exposures [Core]  <!-- UUID: 69d0776b-786c-408b-b76a-860ea60b6b9a -->

The implementation of the model for direct exposures will be specified in a future iteration of the Atlas. The near-term treatment of these assets are specified in the subdocuments herein.

###### A.3.2.2.1.1.1.3.1 - Near-Term Treatment [Core]  <!-- UUID: f4d20c04-8a62-43b1-b806-7559e8182bfb -->

In the near term pending development of the implementation of the model for direct exposures, a 25% Instance Financial CRR will be applied to all direct exposures. In the near term, direct exposures will be considered to be any assets held idle in a wallet controlled by a Prime Agent.

###### A.3.2.2.1.1.1.4 - Bond-Like Instruments [Core]  <!-- UUID: da1a154c-6db8-4012-91a7-31ea4e73e95d -->

The implementation of the model for bond-like instruments will be specified in a future iteration of the Atlas. The near-term treatment of these assets are specified in the subdocuments herein.

###### A.3.2.2.1.1.1.4.1 - Near-Term Treatment [Core]  <!-- UUID: a479643e-fbd3-4c9b-aba0-40f4657a8011 -->

In the near term pending development of the implementation of the model for bond-like exposures, the following Instance Financial CRRs will apply:

- PT-USDS - 0% Instance Financial CRR
- All other bond-like exposures - 4% Instance Financial CRR

In the near term, only Pendle PT tokens will be eligible for investment under this provision.

###### A.3.2.2.1.1.1.5 - Real World Assets [Core]  <!-- UUID: 79c20bfd-f724-482e-8aae-52c962b8268a -->

The documents herein define the calculation of Instance Financial RRC for Real World Assets.

###### A.3.2.2.1.1.1.5.1 - Methodology [Core]  <!-- UUID: b95825a2-9293-434d-bc06-459fee6aecde -->

The documents herein define common methodologies that are applicable to the entirety of the process for calculating Instance Financial RRC for Real World Assets.

###### A.3.2.2.1.1.1.5.1.1 - Basis In Basel Framework [Core]  <!-- UUID: 95695429-cc27-403d-ad12-4ecf89203637 -->

The process for calculating Instance Financial RRC for Real World Assets is based on the Basel Framework developed by the Basel Committee on Bank Supervision. See [https://www.bis.org/basel_framework/index.htm](https://www.bis.org/basel_framework/index.htm).

###### A.3.2.2.1.1.1.5.1.2 - Citations To Basel Framework [Core]  <!-- UUID: 0c97534b-d4f4-4a42-854c-b39993c95f02 -->

Citations are made throughout the process for calculating Instance Financial RRC for Real World Assets to relevant provisions from the Basel Framework.

These citations follow the standard format of `[Prefix][Chapter Number].[Paragraph Number]`, where `Prefix` is a three letter prefix indicating the regulatory standard area or chapter family. For example, a citation to `CRE20.1` refers to Credit Risk Standards, Chapter 20 regarding "Standardised Approach: Individual Exposures", paragraph 1.

When reference is made to a range of documents, a hyphen may be used. For example, `CRE20.1-93` refers to Credit Risk Standards, Chapter 20 regarding "Standardised Approach: Individual Exposures", paragraphs 1 through 93.

Similarly, discrete sets of documents may be referenced using a comma. For example, `CRE40-41, 45` refers to Credit Risk Standards, Chapters 40 to 41 and 45.

###### A.3.2.2.1.1.1.5.1.3 - Banking Book [Core]  <!-- UUID: 96a9c07c-6a3e-4a03-87a9-d6c72ffac340 -->

In the process for calculating Instance Financial RRC for Real World Assets, all exposures are treated as if they were part of the banking book.

###### A.3.2.2.1.1.1.5.2 - Process For Calculating Instance Financial RRC [Core]  <!-- UUID: 58cc9f0b-0d88-4027-bae4-a33cb839e748 -->

The documents herein define the process for calculating Instance Financial RRC for Real World Assets.

###### A.3.2.2.1.1.1.5.2.1 - Identify Exposure Types [Core]  <!-- UUID: dbc4c20e-faa4-429d-8289-f38318d443f1 -->

The first step is identifying the Exposure Type that an exposure fits under. The Exposure Types are:

- On-Balance Sheet Items (see `CRE20.1-93`)
- Off-Balance Sheet Items (see `CRE20.94-101`)
- Securitization Tranches (see `CRE40-41, 45`)
- Derivatives or Securities Financing Transactions (see `CRE50-52`)
- Funds / Collective Investment Undertakings / Exchange Traded Funds (see `CRE60`)
- Commodities (see `MAR21.13`)
- Foreign Exchange (see `MAR21.14`)

###### A.3.2.2.1.1.1.5.2.2 - Calculate Exposure At Default Including Credit Risk Mitigation [Core]  <!-- UUID: db4ae988-b240-4506-b040-4712afc76fb2 -->

The second step is calculating the Exposure at Default including Credit Risk Mitigation as specified in the documents herein.

###### A.3.2.2.1.1.1.5.2.2.1 - Calculation Of Exposure At Default [Core]  <!-- UUID: ec8879e3-71b8-450d-985f-b1edf14f8b4d -->

Exposure At Default is calculated as specified in the documents herein.

###### A.3.2.2.1.1.1.5.2.2.1.1 - Exposure At Default Equal To Book Value [Core]  <!-- UUID: 9e047432-7a9f-4dc0-8172-4085c603d9ba -->

For the following Exposure Types, Exposure At Default is equal to book value:

- On-Balance Sheet Items
- Securitization Tranches
- Derivatives or Securities Financing Transactions
- Funds / Collective Investment Undertakings / Exchange Traded Funds
- Commodities
- Foreign Exchange

###### A.3.2.2.1.1.1.5.2.2.1.2 - Exposure At Default Equal To Book Value Multiplied By Credit Conversion Factor [Core]  <!-- UUID: 9868d6c9-17ec-44da-8898-b59a1ae579e0 -->

For the following Exposure Types, Exposure At Default is equal to book value multiplied by the Credit Conversion Factor (see `CRE51`):

- Off-Balance Sheet Items

###### A.3.2.2.1.1.1.5.2.2.2 - Adjustment For Credit Risk Mitigation [Core]  <!-- UUID: da454ffd-494a-4806-acb5-93653b1b8b11 -->

The Exposure At Default calculated in [A.3.2.2.1.1.1.5.2.2.1 - Calculation Of Exposure At Default](ec8879e3-71b8-450d-985f-b1edf14f8b4d) is then adjusted for Credit Risk Mitigation (see `CRE22`) to arrive at an adjusted Exposure At Default used for the remainder of the calculations.

###### A.3.2.2.1.1.1.5.2.3 - Determine Risk Weights [Core]  <!-- UUID: a1ff2a3d-7131-425c-80c5-a887a4259f12 -->

The third step is calculating the Risk Weights as specified in the documents herein.

###### A.3.2.2.1.1.1.5.2.3.1 - On-Balance Sheet Or Off-Balance Sheet Items [Core]  <!-- UUID: 0144ae72-c945-4f62-998c-e533a5f32858 -->

Credit Risk for On-Balance Sheet or Off-Balance Sheet Items is calculated based on the relevant provisions in the Basel Framework as follows:

| Exposure Type | Reference |
| --- | --- |
| Sovereigns | `CRE20.7-10` |
| Non-central government Public Sector Entities (PSEs) | `CRE20.11-12` |
| Multilateral Development Banks | `CRE20.13-15` |
| Banks | `CRE20.16-32` |
| Covered Bonds | `CRE20.33-39` |
| Securities, firms, and other financial institutions | `CRE20.40` |
| Corporates | `CRE20.41-52` |
| Subordinated debt, equity, and other capital instruments | `CRE20.53-62` |
| Retail exposure class | `CRE20.63-68` |
| Real Estate exposure class | `CRE20.69-91` |
| Direct credit substitutes | `CRE20.95` |
| Sale and repurchase agreements where the credit risk remains with the bank | `CRE20.95` |
| Lending of banks' securities or the posting of securities as collateral by banks | `CRE20.95` |
| Forward assets purchases | `CRE20.95` |
| Forward forward deposits | `CRE20.95` |
| Partly paid shares and securities | `CRE20.95` |
| Credit substitutes not included in any other category | `CRE20.95` |
| Note issuance facilities | `CRE20.96` |
| Revolving underwriting facilities | `CRE20.96` |
| Certain transactions-related contingent items (e.g. performance bonds, bid bonds, warranties, standby letters of credit) | `CRE20.97` |
| Commitments regardless of the maturity of the underlying facility | `CRE20.98` |
| Both issuing and confirming banks of short-term self-liquidating trade letters of credit arising from the movement of goods | `CRE20.99` |
| Commitments that are unconditionally cancellable at any time by the bank without prior notice | `CRE20.100` |

###### A.3.2.2.1.1.1.5.2.3.2 - Securitization Tranches [Core]  <!-- UUID: 5f70b7dd-4a76-4204-9bd6-9e6ce2864f82 -->

Risk Weights for Securitization Tranches (see `CRE40-41, 45`) are calculated as follows:

- If the Securitization Tranche is rated, then the Securitisation - External Ratings Based Approach should be applied (see `CRE42`).
- If the Securitization Tranche is not rated, then the Securitisation - Standard Approach should be applied (see `CRE41`).

###### A.3.2.2.1.1.1.5.2.3.3 - Derivatives Or Securities Financing Transactions [Core]  <!-- UUID: 3622ac1e-4ed9-41ba-ba91-0396e1b30b67 -->

Counterparty Credit Risk for Derivatives or Securities Financing Transactions is calculated based on the relevant provisions in the Basel Framework (see `CRE50-52`). In addition, if the instrument is an Over The Counter derivative, Credit Valuation Adjustment capital is applied as well (see `MAR50`).

###### A.3.2.2.1.1.1.5.2.3.4 - Funds / Collective Investment Undertakings / Exchange Traded Funds [Core]  <!-- UUID: 56ef98fa-582e-4c60-87f2-34400bad72fe -->

Risk Weights for Funds / Collective Investment Undertakings / Exchange Traded Funds (see `CRE60`) are calculated as follows:

- If look-through is feasible, apply the Look Through Approach (see `CRE60.2-5`)
- If look-through is not feasible but the mandate information is available, apply the Mandate Based Approach (see `CRE60.6-7`)
- If look-through is not feasible and the mandate information is not available, apply the fallback conservative approach (see `CRE60.8`)

###### A.3.2.2.1.1.1.5.2.3.5 - Commodities [Core]  <!-- UUID: 75db9d5b-c245-4574-8705-2cd5d4dde0b1 -->

Market Risk for Commodities is calculated based on the relevant provisions in the Basel Framework (see `MAR21.13`).

###### A.3.2.2.1.1.1.5.2.3.6 - Foreign Exchange [Core]  <!-- UUID: 11b18384-63d6-478c-bc14-9f1ec495c1cb -->

Market Risk for Foreign Exchange is calculated based on the relevant provisions in the Basel Framework (see `MAR21.14`).

###### A.3.2.2.1.1.1.5.2.4 - Aggregate Risk Weighted Assets [Core]  <!-- UUID: cb6e24c8-5e69-41ae-b600-4d9a7261f172 -->

The fourth step is calculating Aggregate Risk Weighted Assets ("RWA").

###### A.3.2.2.1.1.1.5.2.4.1 - Calculate Risk Weighted Assets [Core]  <!-- UUID: 34a37582-aa59-4c04-92d6-3cc758e9e92e -->

Credit RWA, Market RWA, Counterparty Credit Risk RWA, and Credit Valuation Adjustment RWA are calculated by multiplying the Exposure At Default (see [A.3.2.2.1.1.1.5.2.2 - Calculate Exposure At Default Including Credit Risk Mitigation](db4ae988-b240-4506-b040-4712afc76fb2)) by the applicable Risk Weights (see [A.3.2.2.1.1.1.5.2.3 - Determine Risk Weights](a1ff2a3d-7131-425c-80c5-a887a4259f12)).

###### A.3.2.2.1.1.1.5.2.4.2 - Calculate Aggregate Risk Weighted Assets [Core]  <!-- UUID: fabb3382-d2eb-4cba-9e54-3fd5b83ea47c -->

Aggregate RWA is calculated as the sum of (1) Credit RWA, (2) Market RWA, (3) Counterparty Credit RWA, and (4) Credit Valuation Adjustment RWA.

###### A.3.2.2.1.1.1.5.2.5 - Apply Leverage Adjustment [Core]  <!-- UUID: 6047795b-9a0e-4410-b794-76083388281e -->

The fifth step is to adjust the Aggregate RWA specified in [A.3.2.2.1.1.1.5.2.4 - Aggregate Risk Weighted Assets](cb6e24c8-5e69-41ae-b600-4d9a7261f172) for leverage (see `CRE99.128-133`)

###### A.3.2.2.1.1.1.5.2.6 - Determine Required Risk Capital [Core]  <!-- UUID: 70013695-3823-407a-9603-b38795ba9899 -->

The final step is to multiply the adjusted Aggregate RWA specified in [A.3.2.2.1.1.1.5.2.5 - Apply Leverage Adjustment](6047795b-9a0e-4410-b794-76083388281e) by an 8% capital ratio to arrive at Instance Financial RRC.

###### A.3.2.2.1.1.1.5.3 - Exceptions [Core]  <!-- UUID: 748f6364-f63b-4601-8f43-345ae3398224 -->

The documents herein define exceptions to the calculation of Instance Financial RRC for specific Real World Assets. These exceptions will be removed in a future iteration of the Atlas.

###### A.3.2.2.1.1.1.5.3.1 - Instance Financial CRRs For Specific Assets [Core]  <!-- UUID: 672d377f-067e-4742-a987-b2c6258f9c99 -->

The following Instance Financial CRRs apply to specific assets listed:

- BUIDL, JTRSY on Ethereum Mainnet, and USTB - 0% Instance Financial CRR
- JTRSY on Avalanche - 0.5% Instance Financial CRR
- JAAA on Ethereum Mainnet - 1.6% Instance Financial CRR
- JAAA on Avalanche - 1.6% Instance Financial CRR
- STAC on Ethereum Mainnet - 1.6% Instance Financial CRR
- GACLO-1 on Ethereum Mainnet - 0.85% Instance Financial CRR
- ACRDX on Plume - 9.99% Instance Financial CRR
- ACRDX on Ethereum Mainnet - 9.99% Instance Financial CRR

###### A.3.2.2.1.1.1.5.3.1.1 - Additional Restrictions On Investments In JTRSY And JAAA On Avalanche [Core]  <!-- UUID: 66506235-0e6c-4fa9-8e22-5eb4f19cb330 -->

Investments in JTRSY and JAAA on Avalanche are subject to the following additional restrictions:

- The initial deployment of capital into JTRSY and JAAA on Avalanche may not exceed 20 million USDS in total;
- Each additional deployment of capital into JTRSY or JAAA must be approved by the Core Council Risk Advisor;
- Until audits of Centrifuge v3 are approved by the Protocol Security Workstream Lead, the Prime must be below a 90% Encumbrance Ratio on a pro forma basis assuming that each additional deployment of capital into JTRSY and JAAA requires 100% Instance Total CRR; and
- Total investments in JTRSY and JAAA on Avalanche may not exceed 250 million USDS.

###### A.3.2.2.1.1.1.5.3.1.2 - Additional Restrictions On Investments In ACRDX On Plume And Ethereum Mainnet [Core]  <!-- UUID: 8cbfb295-019d-4ac6-af19-1a1fead233b0 -->

Total ACRDX exposure may not increase beyond 50.97 million USDS and should be reduced to zero over time.

###### A.3.2.2.1.1.1.5.3.2 - Restrictions On Investments On Plume [Core]  <!-- UUID: c5d70220-4797-4df9-8977-4998d4a57888 -->

Investments on Plume are subject to the following restrictions:

- Assets other than RWAs on Plume or being bridged to Plume require 100% Instance Total CRR; and
- Total investments on Plume may not exceed 125 million USDS.

###### A.3.2.2.1.1.1.6 - Cash Stablecoins [Core]  <!-- UUID: 3c0a9e8b-4a0b-4059-87a4-155deaee0486 -->

The implementation of the model for Cash Stablecoins will be specified in a future iteration of the Atlas. The near-term treatment of these assets are specified in the subdocuments herein.

###### A.3.2.2.1.1.1.6.1 - Near-Term Treatment [Core]  <!-- UUID: 8aee612b-fe36-4c6b-adee-2e0762579a40 -->

In the near term pending development of the implementation of the model for Cash Stablecoins, a 0% Instance Financial CRR will be applied to Cash Stablecoins. In the near term, only USDS, sUSDS, Dai, sDai, USDC, USDT, and pyUSD (either held directly or through decentralized exchanges such as Curve) will be eligible for investment under this provision.

##### A.3.2.2.1.2 - Instance Smart Contract RRC Implementation [Core]  <!-- UUID: e6cfa64f-68c0-4dac-8cec-a5f9bfcb9080 -->

The documents herein define the implementation of the Risk Framework for calculating Instance Smart Contract RRC.

###### A.3.2.2.1.2.1 - Defining Relevant Smart Contracts [Core]  <!-- UUID: 162cfc93-77bd-4878-a8be-370d8862d792 -->

The first step in calculating Instance Smart Contract RRC with respect to an Allocation System opportunity is to identify the set of relevant smart contracts for the opportunity.

###### A.3.2.2.1.2.1.1 - Identifying Exposure Contracts [Core]  <!-- UUID: 87a91c14-92b1-4d14-a90a-a02086a05066 -->

First, all relevant smart contracts must be identified. Relevant smart contracts are those that are critical for the project being invested in, including core business logic, vaults, token contracts, and proxy implementations.

###### A.3.2.2.1.2.1.1.1 - Reliance On External Sources [Core]  <!-- UUID: fa41a412-b81d-4eba-93a9-95fec2a842c5 -->

External sources such as third party data providers, security consultants, and project documentation may be used to help identify relevant smart contracts. However, the Prime Agent deploying funds from the Collateral Portfolio into the opportunity retains overall responsibility for the reasonableness of identifying the relevant smart contracts.

###### A.3.2.2.1.2.1.2 - Locating Verified Code [Core]  <!-- UUID: b4e430a3-e848-4ef1-9b3a-6da724060674 -->

Second, the source code for each relevant contract must be obtained. The source code should be obtained for the deployed version of the contract using an appropriate block explorer (e.g. Etherscan for Ethereum Mainnet or L2s). The source code should include any dependencies or inherited library contracts that are part of the live system.

###### A.3.2.2.1.2.2 - Smart Contract Risk Rating Calculation [Core]  <!-- UUID: 00fd9362-f606-49bc-a425-9c96008be238 -->

The second step in calculating the Instance Smart Contract RRC with respect to an Allocation System opportunity is to calculate the Smart Contract Risk Rating $SCRR$ for the covered smart contracts identified in [A.3.2.2.1.2.1 - Defining Relevant Smart Contracts](162cfc93-77bd-4878-a8be-370d8862d792). The $SCRR$ is calculated as follows:

$$
\text{SCRR} = min[\text{CAP}, (\text{SR} + \text{CCR}) \times \text{LAF} \times {AF}]
$$

Here $min$ is the mathematical minimum function that returns the lesser of the specified parameters.
The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.2.2.1 - Smart Contract Risk Rating Cap [Core]  <!-- UUID: b824c6ec-940b-4921-89f0-aca89b54e86a -->

The Smart Contract Risk Rating Cap $\text{CAP}$ is a temporary cap on the Smart Contract Risk Rating. The value of the $CAP$ is `30`.

###### A.3.2.2.1.2.2.2 - Starting Rate [Core]  <!-- UUID: 51fc7445-8602-451d-87af-64f35abd7833 -->

The Starting Rate $SR$ is an arbitrary starting risk rating for protocols. The value of the $SR$ is `25`.

###### A.3.2.2.1.2.2.3 - Code Complexity Rating [Core]  <!-- UUID: 295e4d3b-8c8a-4f74-879f-88060bb07803 -->

The Code Complexity Rate $CCR$ is a measure of the complexity of the code of the smart contracts used by the protocol. The $CCR$ is calculated as follows:

$$
CCR = \text{CCRMax} \times min(1, \frac{\text{RawCCR} + 1}{\text{CCRUpperBound} + 1})
$$

Here the $min$ function is the mathematical minimum function that returns the lesser of the specified parameters.

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.2.2.3.1 - Code Complexity Rating Maximum [Core]  <!-- UUID: d41b80e2-97fc-4227-bcda-51f4d5fac7a6 -->

The Code Complexity Rating Maximum $\text{CCRMax}$ is the maximum Code Complexity Rating for a protocol. The $\text{CCRMax}$ is set to `75`.

###### A.3.2.2.1.2.2.3.2 - Code Complexity Rating Upper Bound [Core]  <!-- UUID: 1632947d-b197-4478-9122-0c0e1acc8c7a -->

The Code Complexity Rating Upper Bound $\text{CCRUpperBound}$ is an arbitrary factor to normalize the Raw Code Complexity Rating. The $\text{CCRUpperBound}$ is set to `8,500`.

###### A.3.2.2.1.2.2.3.3 - Raw Code Complexity Rating [Core]  <!-- UUID: ce3f2e96-b643-4de7-bfb9-cb0aee678635 -->

The Raw Code Complexity Rating $\text{RawCCR}$ is an unnormalized measure of the complexity of the code of the smart contracts that implement the protocol. The $\text{RawCCR}$ is calculated as follows:

$$
\text{RawCCR}=(\text{TCC} \times \text{CCweight}) + (\text{TDP} \times \text{DPweight}) + (\text{TEC} \times \text{ECweight}) + (\text{ID} \times \text{IDweight}) + (\frac{\text{CS}}{\text{CSfactor}} \times \text{CSweight})
$$

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.2.2.3.3.1 - Total Cyclomatic Complexity [Core]  <!-- UUID: 935d13f6-c66c-4020-85e3-831525776629 -->

Cyclomatic complexity measures the number of independent execution paths through a unit of code. The total cyclomatic complexity score is the sum of the cyclomatic complexity of each of the covered smart contracts.

###### A.3.2.2.1.2.2.3.3.2 - Cyclomatic Complexity Weight [Core]  <!-- UUID: 9bd7b778-eeb2-4704-81cf-1135240924a0 -->

The Cyclomatic Complexity Weight $\text{CCweight}$ is a weighting factor indicating the relative importance of the Total Cyclomatic Complexity versus other factors. It is set to `1`.

###### A.3.2.2.1.2.2.3.3.3 - Total Decision Points [Core]  <!-- UUID: e62098b2-f2ef-4604-9041-c7e0c8356ed3 -->

Decision points measure the number of branching points where conditional logic is applied. The Total Decision Points are the total number of Decision Points in all functions in the covered smart contracts.

###### A.3.2.2.1.2.2.3.3.4 - Decision Points Weight [Core]  <!-- UUID: 3c4d6fc5-2c37-4094-9a06-681fded786bc -->

The Decision Points Weight $\text{DPweight}$ is a weighting factor indicating the relative importance of the Total Decision Points versus other factors. It is set to `0.5`.

###### A.3.2.2.1.2.2.3.3.5 - Total External Calls [Core]  <!-- UUID: 028431ff-5b02-4f42-9224-6b53ff8756c8 -->

Total External Calls is the count of all external calls (e.g. `call`, `delegatecall`) made in the covered smart contracts.

###### A.3.2.2.1.2.2.3.3.6 - External Calls Weight [Core]  <!-- UUID: 3088abe3-4206-431a-9408-9672cc45d61a -->

The External Calls Weight $\text{ECweight}$ is a weighting factor indicating the relative importance of the Total External Calls versus other factors. It is set to `1.5`.

###### A.3.2.2.1.2.2.3.3.7 - Inheritance Depth [Core]  <!-- UUID: bc711432-efd9-4724-8244-d9469fcd193e -->

Inheritance Depth is the maximum number of inheritance levels in any contract in the covered contracts.

###### A.3.2.2.1.2.2.3.3.8 - Inheritance Depth Weight [Core]  <!-- UUID: b519469f-3f2b-40dc-96b5-69f5e81d9fe6 -->

The Inheritance Depth Weight $\text{IDweight}$ is a weighting factor indicating the relative importance of the Inheritance Depth versus other factors. It is set to `5`.

###### A.3.2.2.1.2.2.3.3.9 - Code Size [Core]  <!-- UUID: 32c32e11-baf0-4bce-a865-5de19a3e5d09 -->

Code Size is the total number of lines of code in the covered contracts, excluding tests and documentation.

###### A.3.2.2.1.2.2.3.3.10 - Code Size Factor [Core]  <!-- UUID: a30c8bc7-2686-46ac-952e-9c1f71c96aa0 -->

The Code Size Factory is an arbitrary factor to normalize the Code Size relative to other parameters. It is set to `1,000`.

###### A.3.2.2.1.2.2.3.3.11 - Code Size Weight [Core]  <!-- UUID: 21656714-b6f6-4ba5-b99a-ea3ac6f2ff89 -->

The Code Size Weight $\text{CSweight}$ is a weighting factor indicating the relative importance of the Code Size versus other factors. It is set to `1`.

###### A.3.2.2.1.2.2.4 - Lindy Adjustment Factor [Core]  <!-- UUID: 227eff62-f2aa-4e49-91ad-1321261ed299 -->

The Lindy Adjustment Factor $\text{LAF}$ is a measure of the "Lindiness" of the smart contracts and is based on the idea that vulnerable smart contracts with large TVL for a significant period of time would have already been hacked. Therefore, protocols with a greater time integrated TVL are safer, all other things equal, than protocols with a lower time integrated TVL. The $\text{LAF}$ is calculated as follows:

$$
\text{LAF} = max(0, 1 - \frac{ln(1 + \lambda \times \text{AGEeff})}{ln(1 + \lambda \times \text{max})})
$$

Here $max$ is the mathematical maximum function that returns the greater of the specified parameters and $ln$ is the natural logarithm.

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.2.2.4.1 - Decay Factor [Core]  <!-- UUID: 7f109cc0-ee8d-48b6-8fbf-6e363004edfb -->

The Decay Factor $lambda$ is a tuning parameter that represents an estimate of how quickly the risk of a set of smart contracts decreases as its effective age increases. The value of $lambda$ is set to `0.1`.

###### A.3.2.2.1.2.2.4.2 - Maximum Age [Core]  <!-- UUID: 891eab12-0c47-4b87-b867-3cba6ca7db4e -->

The Maximum Age $\text{max}$ is the effective age, in months, at which the risk of a set of smart contracts has decayed to zero. The value of $\text{max}$ is set to `60`.

###### A.3.2.2.1.2.2.4.3 - Effective Age [Core]  <!-- UUID: a8db99b2-f072-4132-9ee2-c8ebcc2b3609 -->

The Effective Age $\text{AGEeff}$ is the age of the contracts adjusted for the TVL of the contracts. The $\text{AGEeff}$ is calculated as follows:

$$
\text{AGEeff}=\text{CA} \times ln(1 + \frac{\text{gmTVL}}{\text{TVLthreshold}})
$$

Here $ln$ is the natural logarithm.

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.2.2.4.3.1 - Contract Age [Core]  <!-- UUID: 8ee9538a-0655-4600-8436-1cc610bcdb1b -->

The contract age $\text{CA}$ is the average age, in months, of each of the relevant contracts. The age of each relevant contract should be measured based on the time elapsed between the date the contract was deployed and the date of calculation.

###### A.3.2.2.1.2.2.4.3.2 - Geometric Mean Total Value Locked [Core]  <!-- UUID: bec61312-6a70-4881-8a52-4a7fa75dbf07 -->

The Geometric Mean Total Value Locked $\text{gmTVL}$ is the geometric mean of the daily TVL over the contract age.

###### A.3.2.2.1.2.2.4.3.3 - Total Value Locked Threshold [Core]  <!-- UUID: c7939b23-39e1-4299-9beb-700857b8f90e -->

The Total Value Locked Threshold $\text{TVLthreshold}$ is a factor used to normalize the Geometric mean Total Value Locked. The $\text{TVLthreshold}$ is set to `100,000,000`.

###### A.3.2.2.1.2.2.5 - Audit Factor [Core]  <!-- UUID: 0016d78c-66e7-447f-9691-eaff8ea68d6d -->

The Audit Factor $AF$ is a measure of the extent to which the Base Risk is reduced by audits. The $AF$ is calculated as:

$$
AF = \Pi{[1 - \text{effAuditValue} \times \text{decayFactor}]}
$$

The audit from each audit firm with the highest product of Effective Audit Value and Delay factor should be included in this calculation.

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.2.2.5.1 - Effective Audit Value [Core]  <!-- UUID: ade75eba-ac08-465c-a8a1-4ccaf5b99109 -->

The Effective Audit Value $\text{effAuditValue}$ measures the effectiveness of a single audit in reducing the risk of a set of smart contracts and is a function of the percent of the code covered by the audit and the reputation of the audit firm. The $\text{effAuditValue}$ is calculated as:

$$
\text{effAuditValue} = \text{effectivenessCoefficient} \times \text{coverage}
$$

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.2.2.5.1.1 - Coverage [Core]  <!-- UUID: 096c574f-7194-4b4d-aa5b-e5da7c6c87f2 -->

The Coverage $\text{coverage}$ is a measure of the percent of a set of smart contracts that were covered in the scope of an audit. The $\text{coverage}$ is calculated as:

$$
\text{coverage} = \frac{\text{LinesOfCodeCovered}}{\text{TotalLinesOfCode}}
$$

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.2.2.5.1.1.1 - Lines Of Code Covered [Core]  <!-- UUID: 428022f5-039e-418b-831d-7f816afb2cf3 -->

The Lines Of Code Covered $\text{LinesOfCodeCovered}$ is the number of lines of code of the relevant contracts that were within the scope of the audit, excluding documentation and tests.

###### A.3.2.2.1.2.2.5.1.1.2 - Total Lines Of Code [Core]  <!-- UUID: baaf78d3-7182-459e-83a0-6494eb43f048 -->

The Total Lines Of Code $\text{TotalLinesOfCode}$ is the total number of lines of code of the relevant contracts, excluding documentation and tests.

###### A.3.2.2.1.2.2.5.1.2 - Effectiveness Coefficient [Core]  <!-- UUID: d281c572-ff98-43ba-a01d-e54657b50ab9 -->

The Effectiveness Coefficient $\text{effectivenessCoefficient}$ is a measure of the effectiveness of the particular audit firm and is estimated based on the tier of the audit firm.

###### A.3.2.2.1.2.2.5.1.2.1 - Audit Firm Tiers [Core]  <!-- UUID: 97eee131-b5d6-4246-8631-fb077616b671 -->

Audit firms are divided into two tiers: top-tier and mid-tier.

###### A.3.2.2.1.2.2.5.1.2.1.1 - Top-Tier Effectiveness Coefficient [Core]  <!-- UUID: b4a13cfc-1fef-47da-a350-6e81346203f4 -->

The Effectiveness Coefficient of a top-tier audit firm is set to `0.8`.

###### A.3.2.2.1.2.2.5.1.2.1.2 - Mid-Tier Effectiveness Coefficient [Core]  <!-- UUID: 18e07645-44c3-4175-8941-d7010233288a -->

The Effectiveness Coefficient of a mid-tier audit firm is set to `0.5`.

###### A.3.2.2.1.2.2.5.1.2.2 - Audit Firms By Tier [Core]  <!-- UUID: 5b542b65-2ef1-49e9-8995-122373f1b312 -->

The subdocuments herein categorize specific audit firms into the top-tier and mid-tier categories. Audits from firms other than the ones specified herein may not be included in the calculation of the Audit Adjustment Factor.

The Protocol Security Workstream Lead must review this categorization on a regular basis and update it as necessary.

###### A.3.2.2.1.2.2.5.1.2.2.1 - List Of Top-Tier Audit Firms [Core]  <!-- UUID: 6ada67c6-0cf1-4456-b280-57e8ae7edc13 -->

The top-tier audit firms are:

- ChainSecurity
- OpenZeppelin
- ConsenSys Diligence
- Trail Of Bits

###### A.3.2.2.1.2.2.5.1.2.2.2 - List Of Mid-Tier Audit Firms [Core]  <!-- UUID: dea3a182-4b89-4fda-9eed-232562e5f057 -->

The mid-tier audit firms are:

- Quantstamp
- SlowMist
- PeckShield
- Halborn
- Certora
- Hunter Security
- Omniscia
- Spearbit
- Electisec
- MixBytes
- Cyfrin
- SECBIT Labs
- Bramah Systems
- Zokyo
- Guardian Audits
- Zellic
- Code4rena
- Pashov
- ABDK
- Decurity
- OtterSec
- WatchPug
- Sigma Prime
- Cantina
- Oxorio
- Enigma Dark
- Runtime Verification
- Pessimistic
- Solidified
- StErMi
- Sherlock
- 0xMacro

###### A.3.2.2.1.2.2.5.2 - Decay Factor [Core]  <!-- UUID: 7ccfae3d-59ae-433e-adba-7822ae335755 -->

The Decay Factor $decayFactor$ is a parameter indicating how rapidly the effectiveness of audits in reducing risk decreases over time. The $decayFactor$ is calculated as follows:

$$
decayFactor =\begin{cases}1 & \text{if } auditAge \leq 2 \\\frac{10 - auditAge}{8} & \text{if } 2 < auditAge < 10 \\0 & \text{if } auditAge \geq 10\end{cases}
$$

The parameter of this formula is specified in the subdocument herein.

###### A.3.2.2.1.2.2.5.2.1 - Audit Age [Core]  <!-- UUID: 792084a1-d844-4774-b909-0cf0bc40df7c -->

The Audit Age $auditAge$ is the age, in years, of the audit. The age of the audit should be measured based on the time elapsed between the date the audit report was issued and the date of calculation.

###### A.3.2.2.1.2.3 - Smart Contract Risk Required Risk Capital Calculation [Core]  <!-- UUID: b2c8867b-0da0-4765-a927-9a530a0ccf24 -->

The third step in calculating the Instance Smart Contract RRC with respect to an Allocation System opportunity is to calculate the Instance Smart Contract RRC as a function of the Smart Contract Risk Rating.

###### A.3.2.2.1.2.3.1 - Calculation Of Instance Smart Contract CRR Based on Risk Category [Core]  <!-- UUID: 01f9d3be-2e3e-4bd0-9f34-1000165405c5 -->

The methodology used to calculate the Instance Smart Contract CRR as a percentage of the exposure depends on the Risk Rating $r$ of the protocol as specified in the documents herein.

###### A.3.2.2.1.2.3.1.1 - Low Risk Protocols [Core]  <!-- UUID: 80701bc2-5b75-4205-841e-7799c2be2c33 -->

Low risk protocols are ones with a Risk Rating between less than or equal to `25`. The methodology for low risk protocols is specified in the documents herein.

###### A.3.2.2.1.2.3.1.1.1 - Calculate F1 Parameter [Core]  <!-- UUID: 4f841792-cffb-4817-939a-454ce4f262f0 -->

For low risk protocols, the F1 parameter $f_{1}$ should first be calculated using the methodology specified in [A.3.2.2.1.2.3.3.2.2 - F1 Function](443bcf99-b015-44d3-99c9-42fd611710fe).

###### A.3.2.2.1.2.3.1.1.2 - Calculate Capital Ratio Requirement Using Piecewise Function With F1 Thresholds [Core]  <!-- UUID: e7be59bb-a72c-4ca8-afeb-da78f1afd44e -->

The Capital Ratio Requirement should then be calculated by inputting the F1 parameter calculated in [A.3.2.2.1.2.3.1.1.1 - Calculate F1 Parameter](4f841792-cffb-4817-939a-454ce4f262f0) into the Piecewise Function specified in [A.3.2.2.1.2.3.3.1 - Piecewise Function](7441253c-0030-4b8e-ac91-65046761aab6) using the F1 thresholds specified in [A.3.2.2.1.2.3.3.1.5.3 - Kink Threshold](c28b47a8-951b-4ca4-8501-bbd6d2279b74).

###### A.3.2.2.1.2.3.1.2 - Medium Risk Protocols [Core]  <!-- UUID: 8500fc58-7cd8-4573-b64d-bf7bd445745e -->

Medium risk protocols are ones with a Risk Rating greater than `25` but less than or equal to `50`. The methodology for medium risk protocols is specified in the documents herein.

###### A.3.2.2.1.2.3.1.2.1 - Calculate F1 Parameter [Core]  <!-- UUID: fb47383f-e7f9-412b-893d-86e4c7b83def -->

For medium risk protocols, the F1 parameter $f_{1}$ should first be calculated using the methodology specified in [A.3.2.2.1.2.3.3.2.2 - F1 Function](443bcf99-b015-44d3-99c9-42fd611710fe).

###### A.3.2.2.1.2.3.1.2.2 - Calculate F2 Parameter [Core]  <!-- UUID: 3f2622e3-dce6-44ef-9bc5-2853413abbe8 -->

The F2 parameter $f_{2}$ should then be calculated using the methodology specified in [A.3.2.2.1.2.3.3.2.3 - F2 Function](3286915a-7d81-4eb4-a238-bc7ded8e2634).

###### A.3.2.2.1.2.3.1.2.3 - Calculate Capital Ratio Requirement Using F1 Piecewise Function [Core]  <!-- UUID: 15290d29-ea87-4d07-a25e-84a6c34c6c87 -->

The Capital Ratio Requirement using the F1 Piecewise Function should then be calculated by inputting the F1 parameter calculated in [A.3.2.2.1.2.3.1.2.1 - Calculate F1 Parameter](fb47383f-e7f9-412b-893d-86e4c7b83def) into the Piecewise Function specified in [A.3.2.2.1.2.3.3.1 - Piecewise Function](7441253c-0030-4b8e-ac91-65046761aab6) using the F1 thresholds specified in [A.3.2.2.1.2.3.3.1.5.3 - Kink Threshold](c28b47a8-951b-4ca4-8501-bbd6d2279b74).

###### A.3.2.2.1.2.3.1.2.4 - Calculate Capital Ratio Requirement Using F2 Piecewise Function [Core]  <!-- UUID: ac7e97eb-a780-4986-8f4d-0f9c5a0831a4 -->

The Capital Ratio Requirement using the F2 Piecewise Function should then be calculated by inputting the F2 parameter calculated in [A.3.2.2.1.2.3.1.2.2 - Calculate F2 Parameter](3f2622e3-dce6-44ef-9bc5-2853413abbe8) into the Piecewise Function specified in [A.3.2.2.1.2.3.3.1 - Piecewise Function](7441253c-0030-4b8e-ac91-65046761aab6) using the F2 thresholds specified in [A.3.2.2.1.2.3.3.1.5.2 - Maximum Threshold](df77d6b1-b08a-45c9-8fc2-74268918b0b0).

###### A.3.2.2.1.2.3.1.2.5 - Calculate Blended Average Required Capital Percentage [Core]  <!-- UUID: 95ee7840-66b0-4db9-80f7-c1f641bf0f17 -->

The final Required Capital Percentage $x$ should be calculated as a weighted average of the F1 Required Capital Percentage and the F2 Required Capital Percentage as follows:

$$
x = b \times \alpha \times f_2 + (1 - \alpha) \times f_1
$$

The parameters of this formula are defined in the subdocuments herein.

###### A.3.2.2.1.2.3.1.2.5.1 - Constant Factor [Core]  <!-- UUID: 303c0d7f-42a7-4b9e-8afd-26e4d54e2f56 -->

The constant factor $b$ is set to `0.15`.

###### A.3.2.2.1.2.3.1.2.5.2 - Alpha [Core]  <!-- UUID: b753da3d-ce30-4a66-8da6-16f563cee120 -->

Alpha $\alpha$ is a weighting factor indicating how close the Risk Rating is to the threshold for a High Risk Protocol versus the threshold for a Low Risk Protocol. It is calculated as:

$$
\alpha = \dfrac{r - 25}{50 - 25}
$$

Here $r$ is the Risk Rating of the protocol.

###### A.3.2.2.1.2.3.1.2.5.3 - F1 Capital Ratio Requirement [Core]  <!-- UUID: 04abc79f-ad0f-49d9-91d4-1a94271e1979 -->

The F1 Capital Ratio Requirement $f_1$ is the figure calculated as the output of [A.3.2.2.1.2.3.1.2.3 - Calculate Capital Ratio Requirement Using F1 Piecewise Function](15290d29-ea87-4d07-a25e-84a6c34c6c87).

###### A.3.2.2.1.2.3.1.2.5.4 - F2 Capital Ratio Requirement [Core]  <!-- UUID: 44f6339f-988c-494b-9f0f-37460d11ac56 -->

The F2 Capital Ratio Requirement $f_2$ is the figure calculated as the output of [A.3.2.2.1.2.3.1.2.4 - Calculate Capital Ratio Requirement Using F2 Piecewise Function](ac7e97eb-a780-4986-8f4d-0f9c5a0831a4).

###### A.3.2.2.1.2.3.1.3 - High Risk Protocols [Core]  <!-- UUID: 5dc03a3c-aac9-4a32-bcf6-16077d21e4fd -->

High risk protocols are ones with a Risk Rating greater than `50` but less than or equal to `75`. The methodology for high risk protocols is specified in the documents herein.

###### A.3.2.2.1.2.3.1.3.1 - Calculate F2 Parameter [Core]  <!-- UUID: 234dea0c-e4db-49ea-8dff-30bd7652f6c2 -->

For high risk protocols, the F2 parameter $f_{2}$ should first be calculated using the methodology specified in [A.3.2.2.1.2.3.3.2.3 - F2 Function](3286915a-7d81-4eb4-a238-bc7ded8e2634).

###### A.3.2.2.1.2.3.1.3.2 - Calculate Capital Ratio Requirement Using Piecewise Function With F2 Thresholds [Core]  <!-- UUID: 456c0a8f-348a-477b-8550-eea23e9fd4a5 -->

The Capital Ratio Requirement should then be calculated by inputting the F2 parameter calculated in [A.3.2.2.1.2.3.1.3.1 - Calculate F2 Parameter](234dea0c-e4db-49ea-8dff-30bd7652f6c2) into the Piecewise Function specified in [A.3.2.2.1.2.3.3.1 - Piecewise Function](7441253c-0030-4b8e-ac91-65046761aab6) using the F2 thresholds specified in [A.3.2.2.1.2.3.3.1.5.2 - Maximum Threshold](df77d6b1-b08a-45c9-8fc2-74268918b0b0).

###### A.3.2.2.1.2.3.1.4 - Extreme Risk Protocols [Core]  <!-- UUID: 8c73b3c0-04e2-491d-bd52-367c3590e992 -->

Extreme risk protocols are ones with a Risk Rating greater than `75`. The methodology for extreme risk protocols is specified in the documents herein.

###### A.3.2.2.1.2.3.1.4.1 - Maximum Capital Ratio Requirement [Core]  <!-- UUID: a5a0fab2-d380-41eb-b7d0-ba534cefa0ae -->

For extreme risk protocols, the Capital Ratio Requirement is automatically set to 100%.

###### A.3.2.2.1.2.3.2 - Calculation Of Instance Smart Contract CRR Value [Core]  <!-- UUID: 6905f51d-374e-4bf7-b43c-059073d2d68c -->

The Instance Smart Contract CRR is equal to the product of (1) the Instance Smart Contract CRR calculated from [A.3.2.2.1.2.3.1 - Calculation Of Instance Smart Contract CRR Based on Risk Category](01f9d3be-2e3e-4bd0-9f34-1000165405c5) and (2) the exposure to the Allocation System opportunity.

###### A.3.2.2.1.2.3.3 - Inputs To Instance Smart Contract CRR Calculations [Core]  <!-- UUID: b634443b-ee03-4b53-a924-049fa971bfef -->

The documents herein define functions and parameters that are used in multiple parts of the methodology for calculating the Instance Smart Contract CRR based on the Smart Contract Risk Rating specified in [A.3.2.2.1.2.3.1 - Calculation Of Instance Smart Contract CRR Based on Risk Category](01f9d3be-2e3e-4bd0-9f34-1000165405c5).

###### A.3.2.2.1.2.3.3.1 - Piecewise Function [Core]  <!-- UUID: 7441253c-0030-4b8e-ac91-65046761aab6 -->

The Piecewise Function $CRR(x)$ calculates a percentage risk capital requirement based on an input $x$ and is defined as follows:

$$
\text{CRR}(x) =\begin{cases}a & \text{if } x \le x_{\text{start}}, \\[8pt]b \times \dfrac{x - x_{\text{start}}}{x_{\text{kink}} - x_{\text{start}}} & \text{if } x_{\text{start}} < x \le x_{\text{kink}}, \\[8pt]b \;+\; c \;\dfrac{x - x_{\text{kink}}}{x_{\text{max}} - x_{\text{kink}}}& \text{if } x_{\text{kink}} < x < x_{\text{max}}, \\[8pt]d& \text{if } x \ge x_{\text{max}}.\end{cases}
$$

###### A.3.2.2.1.2.3.3.1.1 - Low Risk Parameter [Core]  <!-- UUID: d6fda10f-7eff-4703-a2b4-29bbcd2241e1 -->

The low risk parameter $a$ is the output of the piecewise function when the input is at or below the starting threshold. The $a$ parameter is set to `0`.

###### A.3.2.2.1.2.3.3.1.2 - Medium Risk Parameter [Core]  <!-- UUID: 5efe5b7e-cd77-43ea-9499-549e0f46a5d1 -->

The medium risk parameter $b$ is the output of the piecewise function when the input is equal to the kink threshold. The $b$ parameter is set to `0.25`.

###### A.3.2.2.1.2.3.3.1.3 - High Risk Parameter [Core]  <!-- UUID: 2262dbd9-d59b-490f-9ff6-b28057bbb6ce -->

The high risk parameter $c$ is the incremental value above the $b$ parameter that the piecewise function will output when the input is equal to the maximum threshold. The $c$ parameter is set to `0.75`.

###### A.3.2.2.1.2.3.3.1.4 - Extreme Risk Parameter [Core]  <!-- UUID: a2ed34be-4bb3-44ae-b92c-4bf4384abc8b -->

The extreme risk parameter $d$ is the output of the piecewise function when the input is equal to or greater than the maximum threshold. The $d$ parameter is set to `1`.

###### A.3.2.2.1.2.3.3.1.5 - Thresholds [Core]  <!-- UUID: 0fc529dd-d4f7-43d3-a618-d41fd8a8c42f -->

The documents herein define the thresholds for the piecewise function.

###### A.3.2.2.1.2.3.3.1.5.1 - Starting Threshold [Core]  <!-- UUID: bbda61eb-828d-486a-8bba-df1f517ad0b5 -->

The Starting Threshold $x_{\text{start}}$ is calculated as follows:

$$
x_{\text{start}}(r) = i \times (r_i - r)
$$

Here $r$ is the Risk Rating.

The parameters of this formula are defined in [A.3.2.2.1.2.3.3.1.5.4 - Threshold Parameters](654528b9-d7c8-4cee-9261-d5a745ea231e).

###### A.3.2.2.1.2.3.3.1.5.2 - Maximum Threshold [Core]  <!-- UUID: df77d6b1-b08a-45c9-8fc2-74268918b0b0 -->

The Maximum Threshold $x_{\text{max}}$ is calculated as follows:

$$
x_{\text{max}}(r) = x_{\text{start}}(r) + i_{max}
$$

Here $r$ is the Risk Rating.

The parameters of this formula are defined in [A.3.2.2.1.2.3.3.1.5.4 - Threshold Parameters](654528b9-d7c8-4cee-9261-d5a745ea231e).

###### A.3.2.2.1.2.3.3.1.5.3 - Kink Threshold [Core]  <!-- UUID: c28b47a8-951b-4ca4-8501-bbd6d2279b74 -->

The Kink Threshold $x_{\text{kink}}$ is calculated as follows:

$$
x_{\text{kink}}(r) = x_{\text{start}}(r) \;+\; i_{kink} \times\bigl[\;x_{\text{max}}(r)\;-\;x_{\text{start}}(r)\bigr]
$$

Here $r$ is the Risk Rating.

The parameters of this formula are defined in [A.3.2.2.1.2.3.3.1.5.4 - Threshold Parameters](654528b9-d7c8-4cee-9261-d5a745ea231e).

###### A.3.2.2.1.2.3.3.1.5.4 - Threshold Parameters [Core]  <!-- UUID: 654528b9-d7c8-4cee-9261-d5a745ea231e -->

The documents herein define inputs that are used to calculate the Starting Threshold, Maximum Threshold, and Kink Threshold. These parameters differ depending on whether the piecewise function is invoked with F1 threshold parameters or F2 threshold parameters.

###### A.3.2.2.1.2.3.3.1.5.4.1 - F1 Threshold Parameters [Core]  <!-- UUID: f022c0b5-e19d-4fff-aa14-c34c686a7629 -->

The documents herein define the F1 threshold parameters.

###### A.3.2.2.1.2.3.3.1.5.4.1.1 - Rating Point Scaling Coefficient [Core]  <!-- UUID: c2c18ff3-1186-4dd9-84b4-ace189d6cda4 -->

The value of the Rating Point Scaling Coefficient $i$ is `0.01`.

###### A.3.2.2.1.2.3.3.1.5.4.1.2 - Reference Inflection Risk Rating [Core]  <!-- UUID: 26fc2a85-86c4-4b75-b561-357d1fcc6115 -->

The value of the Reference Inflection Risk Rating $r_i$ is `50`.

###### A.3.2.2.1.2.3.3.1.5.4.1.3 - Maximum Interval Width [Core]  <!-- UUID: 4f28bafe-6366-40ce-a3df-b796421af66c -->

The value of the Maximum Interval Width $i_{max}$ is `0.50`.

###### A.3.2.2.1.2.3.3.1.5.4.1.4 - Kink Location Fraction [Core]  <!-- UUID: 648567a4-b457-46a0-b9da-7a1586c0735e -->

The value of the Kink Location Fraction $i_{kink}$ is `0.75`.

###### A.3.2.2.1.2.3.3.1.5.4.2 - F2 Threshold Parameters [Core]  <!-- UUID: a7250cdc-5bf8-48c0-a79f-beb774de8196 -->

The documents herein define the F2 threshold parameters.

###### A.3.2.2.1.2.3.3.1.5.4.2.1 - Rating Point Scaling Coefficient [Core]  <!-- UUID: c7650bb7-11b0-4ab1-a163-09f948b740a1 -->

The value of the Rating Point Scaling Coefficient $i$ is `0.02`.

###### A.3.2.2.1.2.3.3.1.5.4.2.2 - Reference Inflection Risk Rating [Core]  <!-- UUID: 9cee8e99-7d32-4eaa-a559-c364c428f7e1 -->

The value of the Reference Inflection Risk Rating $r_i$ is `75`.

###### A.3.2.2.1.2.3.3.1.5.4.2.3 - Maximum Interval Width [Core]  <!-- UUID: e746474b-16ae-4472-b382-f431060a72ec -->

The value of the Maximum Interval Width $i_{max}$ is `0.50`.

###### A.3.2.2.1.2.3.3.1.5.4.2.4 - Kink Location Fraction [Core]  <!-- UUID: 0e04acfb-336b-499a-bbec-e332a82685fd -->

The value of the Kink Location Fraction $i_{kink}$ is `0.75`.

###### A.3.2.2.1.2.3.3.2 - F1 And F2 Functions [Core]  <!-- UUID: 3f150022-5449-42cf-b673-fd6ca037f624 -->

The documents herein define the F1 and F2 functions.

###### A.3.2.2.1.2.3.3.2.1 - Variable Definitions [Core]  <!-- UUID: 7f919121-af12-4adb-904a-8ee88a70e98a -->

The documents herein define variables used in the F1 and F2 functions.

###### A.3.2.2.1.2.3.3.2.1.1 - Internal Exposure [Core]  <!-- UUID: 23cebf79-75ee-49d5-8244-a3e67add3b89 -->

The Internal Exposure $e_{\text{int}}$ is the Agent’s allocation to the protocol.

###### A.3.2.2.1.2.3.3.2.1.2 - Total Exposure [Core]  <!-- UUID: ca513c78-e517-4d95-9d5e-d9485cbaee7a -->

The Total Exposure $e_{\text{tot}}$ is the Sky Ecosystem’s aggregate allocation to the protocol.

###### A.3.2.2.1.2.3.3.2.1.3 - Internal Liquid Surplus [Core]  <!-- UUID: 291fabbc-2121-4439-8129-f9eb9d9ec863 -->

The Internal Liquid Surplus $s_{\text{liq}}$ is equal to the Total Risk Capital of the Agent.

###### A.3.2.2.1.2.3.3.2.1.4 - Exposure Beyond Surplus [Core]  <!-- UUID: 6e3f511e-c4bc-479b-b34a-56c42863da2e -->

The Exposure Beyond Surplus $E_{\text{beyond}}$ is the difference between the Sky Ecosystem’s aggregate allocation to the protocol and aggregate internal liquid surplus of all Agents.

###### A.3.2.2.1.2.3.3.2.1.5 - Total Collateral [Core]  <!-- UUID: 567dd86e-9df5-4dd5-94a9-dcb2d3d4a1e9 -->

The Total Collateral $C_{\text{tot}}$ is the total USDS and Dai debt in the system.

###### A.3.2.2.1.2.3.3.2.2 - F1 Function [Core]  <!-- UUID: 443bcf99-b015-44d3-99c9-42fd611710fe -->

The F1 parameter $f_{1}$ is calculated as follows:

$$
f_{1} = \dfrac{E_{\text{beyond}}}{C_{\text{tot}}}
$$

The parameters of this function are defined in [A.3.2.2.1.2.3.3.2.1 - Variable Definitions](7f919121-af12-4adb-904a-8ee88a70e98a).

###### A.3.2.2.1.2.3.3.2.3 - F2 Function [Core]  <!-- UUID: 3286915a-7d81-4eb4-a238-bc7ded8e2634 -->

The F2 parameter $f_2$ is calculated as follows:

$$
f_{2} = \dfrac{e_{\text{int}} + a \,\bigl(e_{\text{tot}} - e_{\text{int}}\bigr)}{s_{\text{liq}}}
$$

Here $\alpha$ is equal to `0.1`.

The parameters of this function are defined in [A.3.2.2.1.2.3.3.2.1 - Variable Definitions](7f919121-af12-4adb-904a-8ee88a70e98a).

###### A.3.2.2.1.2.3.4 - Reference Implementation [Core]  <!-- UUID: 35ec7382-0613-4e74-b5ba-d86c647b1d73 -->

The document herein contains a reference implementation of the calculation of Instance Smart Contract RRC based on the Smart Contract Risk Rating.

`import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# Function Definition
# ------------------------------------------------------------------

def piecewise_coverage(x, x_start, x_kink, x_max):
    """
    Returns a coverage fraction in [0.0 ... 1.0] given x
    and piecewise linear thresholds:
      - 0% coverage if x < x_start
      - linear 0%→25% from x_start to x_kink
      - linear 25%→100% from x_kink to x_max
      - 100% if x > x_max
    """
    # Safely handle edge cases
    if x <= x_start:
        return 0.0
    if x >= x_max:
        return 1.0

    # If between x_start and x_kink -> map linearly from 0% to 25%
    if x_start < x <= x_kink:
        span = x_kink - x_start
        # fraction of the way through that segment
        frac = (x - x_start) / span
        # coverage goes 0 -> 0.25 (25%)
        return 0.25 * frac

    # If between x_kink and x_max -> map linearly from 25% to 100%
    else:  # x_kink < x < x_max
        span = x_max - x_kink
        frac = (x - x_kink) / span
        # coverage goes 0.25 -> 1.0
        return 0.25 + (0.75 * frac)

# ------------------------------------------------------------------
# Thresholds
# ------------------------------------------------------------------

def f1_thresholds_low_risk(rating):
    """
    Return (x_start, x_kink, x_max)
    in % terms, e.g. 5%, 23.75%, 30%, etc.
    """
    x_start = (50 - rating) * 0.01  # e.g. rating=0 -> 0.5 (50%)
    x_max   = x_start + 0.50       # always a 50% gap to max
    # kink is 75% of the way from start to max
    x_kink  = x_start + 0.75 * (x_max - x_start)
    return (x_start, x_kink, x_max)

def f2_thresholds_high_risk(rating):
    """
    Return (x_start, x_kink, x_max)
    in fraction form (0.50, 0.875, 1.00, etc).
    """
    # starting threshold = (75 - rating) * 2%:
    x_start = (75 - rating) * 0.02
    x_max = x_start + 0.50
    x_kink = x_start + 0.75 * (x_max - x_start)  # 75% of the way
    return (x_start, x_kink, x_max)

# ------------------------------------------------------------------
# RRC Calculation
# ------------------------------------------------------------------

def calculate_rrc_coverage(
    rating,
    exposure_internal,
    exposure_total,
    liquid_surplus_internal,
    total_exposure_beyond_surplus,
    total_collateral
):
    """
    Returns the coverage fraction (0 - 1) for a given rating & scenario.
    For the absolute coverage amount, multiply coverage_fraction
    by \`exposure_internal\`.
    """

    # 1) Compute the two driver ratios
    f1 = max(0.0, total_exposure_beyond_surplus / total_collateral) # Ensuring it is non-negative when surplus > exposure
    f2 = (exposure_internal + 0.1 * (exposure_total - exposure_internal)) / liquid_surplus_internal

    # 2) Determine which category the rating is in
    if rating <= 25:
        # TRR Category 1 (Low Risk)  => use only f1 piecewise
        x_start, x_kink, x_max = f1_thresholds_low_risk(rating)
        coverage_fraction = piecewise_coverage(f1, x_start, x_kink, x_max)

    elif rating <= 50:
        # TRR Category 2 (Medium Risk) => blend coverage from f1-curve and f2-curve
        # First get coverage from the "f1 low-risk"
        x_start_1, x_kink_1, x_max_1 = f1_thresholds_low_risk(25)
        cov_f1 = piecewise_coverage(f1, x_start_1, x_kink_1, x_max_1)

        # Then get coverage from the "f2 high-risk"
        x_start_2, x_kink_2, x_max_2 = f2_thresholds_high_risk(50)
        cov_f2 = piecewise_coverage(f2, x_start_2, x_kink_2, x_max_2)

        # Blend factor alpha
        alpha = (rating - 25) / (50 - 25)
        coverage_fraction = (1 - alpha) * cov_f1 + 0.15 * alpha * cov_f2

    elif rating <= 75:
        # TRR Category 3 (High Risk) => use only f2
        x_start, x_kink, x_max = f2_thresholds_high_risk(rating)
        coverage_fraction = piecewise_coverage(f2, x_start, x_kink, x_max)

    else:
        # TRR Category 4 (Extreme Risk) => special piecewise lumps.
        if rating > 75:
            return 1.0

    return coverage_fraction
`

###### A.3.2.2.1.2.4 - Exceptions [Core]  <!-- UUID: 3de7a183-3871-49e0-89b0-1363db621dc0 -->

The documents herein define exceptions to the calculation of Instance Smart Contract CRR for specific asset classes or protocols.

###### A.3.2.2.1.2.4.1 - BUIDL, JTRSY, USTB, And JAAA [Core]  <!-- UUID: 52c23a24-aedf-4a1e-abf3-23b819ec9fc5 -->

In the short term, investments in BUIDL, JTRSY, USTB, and JAAA have Instance Smart Contract CRR and Instance Administrative CRR of zero.

###### A.3.2.2.1.2.4.2 - Legal Recourse Assets [Core]  <!-- UUID: 717b33c3-708e-4acf-acb4-7be5d5039a2f -->

The exposure for investments in Legal Recourse Assets is calculated as specified in the documents herein.

###### A.3.2.2.1.2.4.2.1 - Definition [Core]  <!-- UUID: 48216554-13d2-460d-b7c5-539167946528 -->

Legal Recourse Assets ("LRAs") are Real World Assets where legal recourse can be used to recover the assets even if the smart contract is technically hacked or exploited.

###### A.3.2.2.1.2.4.2.2 - Exposure Calculation [Core]  <!-- UUID: 522e7dc2-9f9d-40f8-a24f-21a688099f15 -->

The exposure for investments in Legal Recourse Assets is calculated according to the following formula:

`Exposure = Equivalent Loss * Effective Age + Raw Exposure * (1 - Effective Age)`

The parameters of this formula are defined in the documents herein.

###### A.3.2.2.1.2.4.2.2.1 - Equivalent Loss [Core]  <!-- UUID: dbe94efe-061f-4821-9494-aea27a8c80bf -->

Equivalent Loss is an estimate of the loss that the holder of a Legal Recourse Asset would experience if they had to use legal recourse to recover the assets, based on a combination of expected time to recovery and litigation financing costs. It is calculated according to the following formula:

`Equivalent Loss = Raw Exposure * Expected Frozen Duration * Litigation Financing Costs`

The parameters of this formula are defined in the documents herein.

###### A.3.2.2.1.2.4.2.2.1.1 - Raw Exposure [Core]  <!-- UUID: 60833a59-f7f8-45db-92c0-a3bc71ea5375 -->

Raw Exposure is specified in [A.3.2.2.1.2.4.2.2.3 - Raw Exposure](87fe863b-801d-4415-a3d2-8b4fb977b6c2).

###### A.3.2.2.1.2.4.2.2.1.2 - Expected Frozen Duration [Core]  <!-- UUID: 1e07154c-2a3f-40ff-b96b-476558bc0002 -->

Expected Frozen Duration is the estimated time, in years or fractions thereof, that the Legal Recourse Asset would remain frozen after a hack or technical exploit before the holder would be able to recover the underlying assets through legal recourse. The value of the Expected Frozen Duration is 0.5.

###### A.3.2.2.1.2.4.2.2.1.3 - Litigation Financing Costs [Core]  <!-- UUID: 061ee579-9c4f-4f59-b5cf-401ff4c11f72 -->

Litigation Financing Costs are the annual costs of borrowing against the right to receive the future recovery of the assets underlying the Legal Recourse Asset through legal recourse. The value of the Litigation Financing Costs is 20%.

###### A.3.2.2.1.2.4.2.2.2 - Effective Age [Core]  <!-- UUID: c06bbc44-09c0-43f9-b443-39c2802a4a78 -->

The Effective Age is calculated as specified in [A.3.2.2.1.2.2.4.3 - Effective Age](a8db99b2-f072-4132-9ee2-c8ebcc2b3609) except that the Effective Age cannot exceed one (1) year.

###### A.3.2.2.1.2.4.2.2.3 - Raw Exposure [Core]  <!-- UUID: 87fe863b-801d-4415-a3d2-8b4fb977b6c2 -->

The Raw Exposure is the total exposure to the particular Allocation System opportunity.

###### A.3.2.2.1.2.4.3 - Ethena [Core]  <!-- UUID: 4d4f4c60-4941-41c8-8164-c1f35c4574c8 -->

In the short term, Direct Ethena Exposures (see [A.3.2.2.1.1.1.2.1.1.1.1 - Direct Ethena Exposures](e0fa035c-e8f3-4cd2-8ca1-a6afbd1825eb)) automatically have Instance Smart Contract CRR and Instance Administrative CRR of zero. In the long term, given the similarity of these assets to Real World Assets, adapted frameworks for Smart Contract Risk and Administrative Risk for these exposures must be developed. See [A.3.2.2.1.2.4.2 - Legal Recourse Assets](717b33c3-708e-4acf-acb4-7be5d5039a2f).

###### A.3.2.2.1.2.4.4 - Superstate [Core]  <!-- UUID: d129279e-73a5-4f55-9cc8-3950a05c3fc1 -->

In the short term, Superstate Exposures (see [A.3.2.2.1.1.1.2.1.2.1 - Superstate Capital Ratio Requirement](ffca1065-7f92-4815-8a65-52bdbc82c558)) automatically have Instance Smart Contract CRR and Instance Administrative CRR of zero. In the long term, given the similarity of these assets to Real World Assets, adapted frameworks for Smart Contract Risk and Administrative Risk for these exposures must be developed. See [A.3.2.2.1.2.4.2 - Legal Recourse Assets](717b33c3-708e-4acf-acb4-7be5d5039a2f).

###### A.3.2.2.1.2.4.5 - Fluid [Core]  <!-- UUID: 442c47ef-0fef-4d10-9b5c-12b163795cdd -->

The Smart Contract Risk Rating for Fluid is `25`.

##### A.3.2.2.1.3 - Instance Administrative RRC Calculation [Core]  <!-- UUID: 277d6712-25ff-4566-a42b-38d7e860ae76 -->

The documents herein define the implementation of the Risk Framework for calculating Instance Administrative RRC.

###### A.3.2.2.1.3.1 - Administrative Risk Rating Calculation [Core]  <!-- UUID: a9dfd122-2862-4759-aba7-482f86428ca7 -->

The first step in calculating the Instance Administrative RRC with respect to an Allocation System opportunity is to calculate the Administrative Risk Rating $\text{ARR}$ for the protocol being invested in. The $\text{ARR}$ is calculated as follows:

$$
\text{ARR} = min[\text{CAP}, \text{SR} \times \text{DF} \times \text{LAF}]
$$

Here $min$ is the mathematical minimum function that returns the lesser of the specified parameters.

The parameters of this formula are specified in the subdocuments herein.

###### A.3.2.2.1.3.1.1 - Administrative Risk Rating Cap [Core]  <!-- UUID: 7e359ea6-e846-4977-b3db-87fc1db64c0f -->

The Administrative Risk Rating Cap $\text{CAP}$ is a temporary cap on the Administrative Risk Rating. The value of the $\text{CAP}$ is `30`.

###### A.3.2.2.1.3.1.2 - Starting Rating [Core]  <!-- UUID: 368786cb-da80-4d48-a2e8-52d14fb6320c -->

The Starting Rate $\text{SR}$ is an initial risk rating for Administrative Risk before taking into account the Delay Factor and Lindy Adjustment Factor. It is a function of the type of backdoor access that exists to the protocol, as specified in the documents herein.

###### A.3.2.2.1.3.1.2.1 - No Backdoor [Core]  <!-- UUID: 0d40ea83-8eef-4bea-b1ca-5700fb4536bc -->

A protocol with no backdoor access allows no privileged access to the relevant smart contracts by a whitelisted set of users. The Starting Rate for a protocol with no backdoor access is `0`.

###### A.3.2.2.1.3.1.2.2 - Limited Backdoor [Core]  <!-- UUID: ef31a379-c7ea-43c6-9a68-0f6083fcfeaf -->

A protocol with limited backdoor access allows a set of privileged users to materially modify the terms of the smart contracts (e.g. freezing the transfer of funds) but does not allow root backdoor access as specified in [A.3.2.2.1.3.1.2.3 - Root Backdoor](7d203683-a16c-479c-8425-2fed3b4c2375). The Starting Rate for a protocol with limited backdoor access is `50`.

###### A.3.2.2.1.3.1.2.3 - Root Backdoor [Core]  <!-- UUID: 7d203683-a16c-479c-8425-2fed3b4c2375 -->

A protocol with root backdoor access allows a set of privileged users to make arbitrary changes to the terms of the smart contracts, including transferring user funds. The Starting Rate for a protocol with root backdoor access is `100`.

###### A.3.2.2.1.3.1.3 - Delay Factor [Core]  <!-- UUID: 52511026-55f4-4848-95a2-53db048d906c -->

The Delay Adjustment Factor $\text{DF}$ is a factor indicating the extent to which the risk associated with backdoor access is mitigated by a security delay between the time that a change using backdoor access is approved and the time that such a change becomes effective. This delay gives users time to raise issues or withdraw funds in the event of malicious or undesirable use of backdoor access.

The Delay Factor is `1` if there is no security delay and `0` if the security delay is 48 hours or greater. For security delays between 0 hours and 48 hours, the Delay Factor is linearly reduced for each hour of security delay. So a security delay of 24 hours would result in a Delay Factor of `0.5`.

###### A.3.2.2.1.3.1.4 - Lindy Adjustment Factor [Core]  <!-- UUID: 1d676660-675c-40a4-8319-23671c55491b -->

The Lindy Adjustment Factor $\text{LAF}$ is calculated using the same methodology specified in [A.3.2.2.1.2.2.4 - Lindy Adjustment Factor](227eff62-f2aa-4e49-91ad-1321261ed299).

###### A.3.2.2.1.3.2 - Instance Administrative RRC Calculation [Core]  <!-- UUID: d5546d38-3aba-4161-a991-1e74ef637fbc -->

The second step in calculating the Instance Administrative RRC with respect to an Allocation System opportunity is to calculate the Instance Administrative RRC as a function of the Administrative Risk Rating. This is done using the same methodology as specified in [A.3.2.2.1.2.3 - Smart Contract Risk Required Risk Capital Calculation](b2c8867b-0da0-4765-a927-9a530a0ccf24).

###### A.3.2.2.1.3.3 - Exceptions [Core]  <!-- UUID: 5ecb7c62-29bb-4135-a5c6-dbfb0999c996 -->

The documents herein define exceptions to the calculation of Instance Administrative CRR for specific asset classes or protocols.

###### A.3.2.2.1.3.3.1 - BUIDL, JTRSY, USTB, And JAAA [Core]  <!-- UUID: 095464ba-2301-4bb6-b342-e840bdd3c018 -->

The Administrative CRR for BUIDL, JTRSY, USTB, and JAAA is calculated as specified in [A.3.2.2.1.2.4.1 - BUIDL, JTRSY, USTB, And JAAA](52c23a24-aedf-4a1e-abf3-23b819ec9fc5).

###### A.3.2.2.1.3.3.2 - Legal Recourse Assets [Core]  <!-- UUID: e5cf1f62-b8e7-405d-9e3e-46e2e4cbcfd1 -->

The exposure for investments in Legal Recourse Assets is calculated as specified in [A.3.2.2.1.2.4.2 - Legal Recourse Assets](717b33c3-708e-4acf-acb4-7be5d5039a2f).

###### A.3.2.2.1.3.3.3 - Ethena [Core]  <!-- UUID: 2397551e-9704-435e-b815-0384429be224 -->

The Administrative CRR for Ethena is calculated as specified in [A.3.2.2.1.2.4.3 - Ethena](4d4f4c60-4941-41c8-8164-c1f35c4574c8).

###### A.3.2.2.1.3.3.4 - Superstate [Core]  <!-- UUID: 92c06f19-21a3-4aea-9503-db685b3fd7f9 -->

The Administrative CRR for Superstate is calculated as specified in [A.3.2.2.1.2.4.4 - Superstate](d129279e-73a5-4f55-9cc8-3950a05c3fc1).

###### A.3.2.2.1.3.3.5 - Fluid [Core]  <!-- UUID: 6bbbfa59-7988-4d34-bd75-05402d8ac6f8 -->

The Administrative Risk Rating for Fluid is `25`.

#### A.3.2.2.2 - Core Risk Capital Parameters [Core]  <!-- UUID: 15276567-bf61-4c27-8aa2-2f27da831a48 -->

The documents herein define the core risk capital parameters.

##### A.3.2.2.2.1 - JRC Loss Allocation Parameters [Core]  <!-- UUID: b718459e-57e0-414f-9c99-fbc82685cc0f -->

This document specifies the JRC loss allocation parameters.

###### A.3.2.2.2.1.1 - Tip Junior Risk Capital Percentage [Core]  <!-- UUID: 73f2410b-3579-4c68-ae36-e4a4713a6e4b -->

The Tip JRC amount is **10%** of the Prime Agent's Total Junior Risk Capital (IJRC + PEJRC + TEJRC).

For example, if a Prime Agent has $20 million of Internal Junior Risk Capital and $20 million of Prime External Junior Risk Capital, the Tip Junior Risk Capital would be $4 million.

##### A.3.2.2.2.2 - Risk Capital Composition Structural Ratios [Core]  <!-- UUID: c8b80b82-abe9-43d0-96bb-bfc82c83feb4 -->

This document specifies the values of the Risk Capital sourcing ratios defined in [A.3.2.1.2.3 - Total Risk Capital Sourcing Ratios](9e99b084-f15a-4f60-b831-d6c0bd9aec04).

###### A.3.2.2.2.2.1 - External Per Internal (EPI) Ratio Value [Core]  <!-- UUID: 3ed32706-c072-42b5-b1e5-187bddf8dc37 -->

The External Per Internal (EPI) ratio is **1.00**. For example, if a Prime Agent has $20 million of Internal Junior Risk Capital, the EPI ratio enables it to source $20 million of External Junior Risk Capital.

This EPI ratio governs the initial mechanism for sourcing EJRC (PEJRC + TEJRC) and is based purely on the Prime’s IJRC; Primes can source EJRC via this initial mechanism up to a maximum amount equal to their IJRC holdings. However, additional EJRC may potentially be acquired via the alternative use of SPJ capacity, as described in [A.3.2.1.2.3.1.2.1 - Alternative Use Of SPJ Capacity To Source External Junior Risk Capital](03029174-91b4-4974-af1e-52438556a70b).

###### A.3.2.2.2.2.2 - Senior Per Junior (SPJ) Ratio Values [Core]  <!-- UUID: 8578e240-3fe8-41c0-8b2c-15ec9a7181ab -->

The SPJ ratio varies by the JRC type used for enablement:

- Internal Junior Risk Capital SPJ: **1.00**,
- EPI-acquired Prime External Junior Risk Capital SPJ: **0.75**,
- EPI-acquired Tokenized External Junior Risk Capital SPJ: **0.50**,
- SPJ-acquired External Junior Risk Capital (PEJRC or TEJRC): **zero (0)**.

For example, if a Prime Agent has $20 million of Internal Junior Risk Capital, $10 million of Prime External Junior Risk Capital, and $10 million of Tokenized External Junior Risk Capital, then it would be able to count or "enable" $32.5 million of Senior Capital towards its required Risk Capital.

#### A.3.2.2.3 - Junior Risk Capital System Implementation [Core]  <!-- UUID: 2c7c0297-28d5-4954-be87-ffc24d70cef5 -->

The documents herein define operational requirements and protocols for the implementation of the Junior Risk Capital system in the Risk Framework.

##### A.3.2.2.3.1 - Prime External JRC Rental System Implementation [Core]  <!-- UUID: d47ffd80-c463-49b3-b4a9-60bb6d2b114e -->

The implementation of the PEJRC rental system is defined as a Sky Primitive, specifically, the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.3.2.2.3.2 - Tokenized External JRC System Implementation [Core]  <!-- UUID: 025c8a59-3c2e-4b33-a635-bb84b6ac6496 -->

This document will be further developed in a future iteration of the Atlas.

#### A.3.2.2.4 - Senior Risk Capital System Implementation [Core]  <!-- UUID: 6d2be0c6-37fe-42ba-a4a8-a18dd17b0bc1 -->

The documents herein define operational requirements and protocols for the implementation of the Senior Risk Capital system in the Risk Framework.

##### A.3.2.2.4.1 - Sourcing Of Internal Senior Risk Capital [Core]  <!-- UUID: 70888f64-f53f-488a-b138-b3b2ab2300b0 -->

ISRC is sourced from Aggregate Backstop Capital, as specified in [A.2.3.1.3 - Sourcing Of Internal Senior Risk Capital](ac7a6636-acbc-40c9-abc1-4543c0beb300).

##### A.3.2.2.4.2 - External Senior Risk Capital And srUSDS System [Core]  <!-- UUID: 9fac0f6b-cb2d-4dc2-97d5-72c705303675 -->

The documents herein define rules and infrastructure pertaining to the sourcing of External Senior Risk Capital (ESRC). ESRC is capital provided by external investors to be invested as Senior Risk Capital of Prime Agents.

###### A.3.2.2.4.2.1 - srUSDS Contract [Core]  <!-- UUID: 30e9de3a-d67f-4b89-a777-a9781aab9b1a -->

srUSDS is the tokenized form of External Senior Risk Capital. Users can deposit USDS into the srUSDS contract to provide External Senior Risk Capital to the SRC system, making it available for origination by Prime Agents. See [A.3.2.2.4.3 - Senior Risk Capital (SRC) Origination Process](b74e61f5-3793-406d-a0e5-f8f0e4d3ac2f). srUSDS holders can potentially earn higher yields in exchange for the risk that the External Senior Risk Capital will suffer losses.

###### A.3.2.2.4.2.2 - Deposit And Redemption Queues [Core]  <!-- UUID: 38a99586-4a13-4ce3-8b2f-cee025e0c390 -->

The srUSDS contract utilizes distinct queues for managing conversions. Users can add USDS to the deposit queue for conversion into srUSDS; or add srUSDS to the redemption queue for conversion back into USDS at any point during the month.

Assets placed in either queue can be withdrawn by the user at any time before the Monthly Settlement Cycle begins.

At the Monthly Settlement Cycle, all assets remaining in the queues are processed: queued USDS is converted into srUSDS, and queued srUSDS is converted into USDS based on the prevailing Conversion Rate. See [A.3.2.2.4.2.3 - Conversion Rate](2220b1b5-f2f6-4325-9bb5-43cca84e184c).

###### A.3.2.2.4.2.3 - Conversion Rate [Core]  <!-- UUID: 2220b1b5-f2f6-4325-9bb5-43cca84e184c -->

The conversion rate represents the amount of USDS redeemable per unit of srUSDS. This rate increases or decreases over time, reflecting the net return earned by the ESRC pool. The rate is updated at the conclusion of each Monthly Settlement Cycle based on the performance of the ESRC pool during the preceding month, according to the following standard compounding formula:

`New srUSDS Conversion Rate = Previous Conversion Rate * (1 + Monthly srUSDS Yield)`

The parameters of this formula are defined in the documents herein.

###### A.3.2.2.4.2.3.1 - Previous Conversion Rate [Core]  <!-- UUID: 7074ce0f-5a30-40cf-804f-7621233ac9db -->

`Previous Conversion Rate` is the conversion rate (USDS per srUSDS) that was in effect at the beginning of the concluded monthly cycle. The initial conversion rate between srUSDS and USDS is 1:1.

###### A.3.2.2.4.2.3.2 - Monthly srUSDS Yield [Core]  <!-- UUID: cb9bb5b1-50a7-49d8-8ff6-27269061f87e -->

`Monthly srUSDS Yield` represents the net percentage return earned solely by the ESRC pool during the concluded monthly cycle, distributable to srUSDS holders via the conversion rate adjustment. It directly reflects the risk-adjusted performance of the capital deployed and is calculated as:

`[(Total Interest Paid by Stars on ESRC Portion - Losses Allocated to ESRC) / ESRC Principal at start of month - Sky Spread] * (1 - ESRC Earnings Fee)`

The Sky Spread and ESRC Earnings Fee are specified in [A.3.2.2.4.2.3.3.1 - Sky Spread](c160f99c-c3d8-41e9-a3d1-cde514b7a2da) and [A.3.2.2.4.2.3.3.2 - ESRC Earnings Fee](559f6fb6-daf6-41b2-9882-53a91aaf132f), respectively.

###### A.3.2.2.4.2.3.3 - Sources Of Revenue To Sky [Core]  <!-- UUID: 2e3dcac8-d641-49b7-94e9-6947f0a413ca -->

Sky earns revenue from facilitating ESRC from two sources. These sources are included in the formula and defined in the subdocuments below.

###### A.3.2.2.4.2.3.3.1 - Sky Spread [Core]  <!-- UUID: c160f99c-c3d8-41e9-a3d1-cde514b7a2da -->

Sky takes a spread equal to the Sky Spread (see [A.3.1.2.6 - Sky Spread](e1b694de-1ee3-4502-a9c9-52eea9539804)) on all ESRC balances.

###### A.3.2.2.4.2.3.3.2 - ESRC Earnings Fee [Core]  <!-- UUID: 559f6fb6-daf6-41b2-9882-53a91aaf132f -->

Sky takes a 5% fee on the net interest earnings generated from the ESRC portion of originated SRC before these earnings are distributed to srUSDS holders via the conversion rate adjustment.

###### A.3.2.2.4.2.4 - srUSDS Distribution Reward [Core]  <!-- UUID: 626f0f67-1df9-41e8-a4a6-230aa1ccc824 -->

The srUSDS Distribution Reward incentivizes Prime Agents and Integrators to drive srUSDS usage, similar to the Distribution Reward paid on USDS balances. The srUSDS Distribution Reward Fee is the same as the Distribution Reward Fee on USDS. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6). The srUSDS Distribution Reward is paid to the Prime Agent that manages the relationship with the Integrator, and any sharing with the Integrator is subject to bilateral negotiation between the Prime Agent and the Integrator, as specified in [A.2.2.4.2 - Reward Recipient And Sharing](40395562-d447-4c85-b670-c08d2341bcd2).

##### A.3.2.2.4.3 - Senior Risk Capital (SRC) Origination Process [Core]  <!-- UUID: b74e61f5-3793-406d-a0e5-f8f0e4d3ac2f -->

This document defines the operational details of the recurring monthly process allowing Prime Agents to originate Senior Risk Capital (Originated Senior Risk Capital or OSRC) from the Total Senior Risk Capital (TSRC) pool. The process involves determining the available TSRC supply, a bidding phase, an allocation auction, and settlement aligned with the Monthly Settlement Cycle.

###### A.3.2.2.4.3.1 - Process Timing and Schedule [Core]  <!-- UUID: d06b1c1a-7613-4361-a155-f62f68ec30a1 -->

The SRC origination process operates monthly, synchronized with the Monthly Settlement Cycle. The bidding window occurs during the current month for SRC that is usable in the next month; the bidding window closes before settlement processing begins. Additional operational details, including timelines, will be specified in a future iteration of the Atlas.

###### A.3.2.2.4.3.2 - Available Total Senior Risk Capital Pool Determination [Core]  <!-- UUID: 48a3a23c-2e2f-48b8-bcca-6c99d1c2b6ca -->

Total Senior Risk Capital (TSRC) is the amount of Senior Risk Capital that is available each Monthly Settlement Cycle for Primes to originate and thus turn into Originated Senior Risk Capital (OSRC) through the monthly origination process. TSRC is the sum of designated Internal Senior Risk Capital (ISRC) (see [A.2.3.1.3 - Sourcing Of Internal Senior Risk Capital](ac7a6636-acbc-40c9-abc1-4543c0beb300)) and available External Senior Risk Capital (ESRC) from the srUSDS contract. Prior to each monthly bidding window, the TSRC is calculated and publicly announced. Additional operational details will be defined in a future iteration of the Atlas.

###### A.3.2.2.4.3.3 - Bidding Process [Core]  <!-- UUID: 33ef06d4-6ee3-4302-943d-1b932d8c88b4 -->

Participating Prime Agents submit bids via the Powerhouse interface during the defined bidding window. Each bid must specify: (1) The quantity of SRC the Prime seeks to originate, and (2) The maximum price the Prime is willing to pay (expressed in basis points above the Base Rate) for using the OSRC during the upcoming monthly period. Additional operational details will be specified in a future iteration of the Atlas.

###### A.3.2.2.4.3.4 - Allocation & Clearing Price Determination [Core]  <!-- UUID: 0234bb0c-4686-40bc-94e5-13cd8bcd0db7 -->

Bids are ranked descending by price. TSRC is allocated sequentially to the highest bids until the pool is exhausted or all bids are filled. The price of the lowest successful bid that receives an allocation (even partial) sets the uniform clearing price for the month. All winning bidders pay this clearing price per unit of OSRC allocated, regardless of their original bid price. Additional operational details will be specified in a future iteration of the Atlas.

###### A.3.2.2.4.3.5 - Settlement Of Origination [Core]  <!-- UUID: fff0112a-58dd-4041-97f9-7baf113b4e70 -->

During the Monthly Settlement Cycle following allocation, the cost (Allocated OSRC Quantity * Clearing Price) is deducted from each winning Prime Agent’s operational account. Concurrently, the allocated OSRC amount is credited to the Prime Agent’s Risk Capital account as OSRC for the upcoming monthly period.

###### A.3.2.2.4.3.6 - OSRC Duration and Renewal [Core]  <!-- UUID: b63d43f9-cea7-42ee-bfea-5098e55fa68f -->

OSRC is valid only for the single monthly period following the settlement cycle in which it was originated. Renewal requires successful participation in the next monthly origination process; there is no automatic rollover.

##### A.3.2.2.4.4 - Originated Senior Risk Capital (OSRC) Rental Implementation [Core]  <!-- UUID: 268b4b1f-9a19-42f8-b7c6-d8dc01e32517 -->

The operational process for inter-Prime Agent OSRC risk-capital rentals is defined herein. OSRC rentals are facilitated through the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

###### A.3.2.2.4.4.1 - Ecosystem Accord Requirements [Core]  <!-- UUID: 0664a5cc-22c9-4d9e-adcf-55ce8c1afc20 -->

Rental of Originated Senior Risk Capital (OSRC) requires a registered Ecosystem Accord specifying: Amount, Duration, and Price/Terms. As the system permits sub-renting (allowing a Prime to rent out OSRC it has previously rented), the Accord must explicitly state if the borrower is granted this permission. In regards to Duration, the Ecosystem Accord must specify the rental period, which cannot extend beyond the end of the current Monthly Settlement Cycle. Primes may agree on any Duration within this limit.

Standardized Ecosystem Accord templates will be provided in a future iteration of the Atlas.

###### A.3.2.2.4.4.2 - SRC Accounting & Enablement [Core]  <!-- UUID: dab711a4-e932-4e2e-bed5-3f459f89cde6 -->

A registered OSRC-rental Ecosystem Accord effectively transfers the claim on the specified amount of the lender’s OSRC to the borrower for the duration of the agreement. The borrowing Prime Agent must possess sufficient Junior Risk Capital (IJRC, PEJRC, TEJRC) and corresponding Senior Per Junior (SPJ) capacity to enable the rented OSRC, such that it counts towards their own Risk Capital requirements. Rented OSRC that is not successfully enabled by the borrower pursuant to the SPJ ratio does not contribute to their Risk Capital calculation.

##### A.3.2.2.4.5 - Short Term Transitionary Measures [Core]  <!-- UUID: d33ac81e-bab1-4969-b46d-e605da2afae3 -->

As an interim measure, prior to the implementation of the Senior Risk Capital System, Sky Core may provide Senior Risk Capital to Prime Agents under Ecosystem Accords between Sky Core and the respective Prime Agents. The terms of such Ecosystem Accords shall be documented under [A.2.8 - Ecosystem Accords](104c3543-ce94-4a2f-9968-57f1ee858085).

#### A.3.2.2.5 - Risk Capital Update Process [Core]  <!-- UUID: d92f0d3b-e6d5-47d4-b6f1-203ef9326ea6 -->

The documents herein define the process for updating Risk Capital requirements.

##### A.3.2.2.5.1 - Schedule For Updating Parameters [Core]  <!-- UUID: f969dee1-774b-4201-97ae-c9fb91960a18 -->

The documents herein define the requirements for updating inputs to the calculation of Risk Capital requirements.

###### A.3.2.2.5.1.1 - Real Time Updates [Core]  <!-- UUID: 23083399-43b0-4bc2-adf8-4e97a9ae494d -->

Inputs into Risk Capital calculations that are based on market or other external variables should be updated in real time or immediately after the underlying data is updated, if the underlying data is only updated periodically.

###### A.3.2.2.5.1.1.1 - Responsibility For Cost Of Real Time Updates [Core]  <!-- UUID: 4c76f9d0-f354-4fba-bf99-2be97b77d234 -->

Each Prime Agent is responsible, at its own expense, for providing the required data and developing and maintaining the data feeds that update the Atlas with its data. A Prime Agent may retain another party, including its Operational Executor Agent, to assist it in fulfilling these responsibilities on mutually agreed terms. However, the ultimate responsibility always remains with the Prime Agent.

###### A.3.2.2.5.1.1.1.1 - Near Term Real Time Updates By Core Council Risk Advisor [Core]  <!-- UUID: 31095e6f-6f05-4d0f-83f6-49ef92e1b6ec -->

In the near term, the Core Council Risk Advisor will provide real time data regarding major lending markets on Ethereum Mainnet and Ethereum L2s. The Core Council Risk Advisor will be compensated for this work as part of its existing relationship with Sky Core and Spark.

###### A.3.2.2.5.1.2 - Non-Real Time Updates [Core]  <!-- UUID: 7cdc17d9-6199-42bb-8ff9-f7ffce126d3a -->

In the near term, Prime Agents may update calculations that are based on market or other external variables less frequently than real time. If they do so, Operational GovOps must apply a buffer to each variable that is not updated in real time to account for the fact that the variable may change in a way that increases Required Risk Capital between update frequencies.

##### A.3.2.2.5.2 - Data Maintenance And Integrity [Core]  <!-- UUID: d105b84d-c1f6-4460-892c-0971942f8905 -->

The documents herein define processes to maintain and ensure the integrity of data that is used as an input to Risk Capital calculations.

###### A.3.2.2.5.2.1 - Responsibility For Data Updates [Core]  <!-- UUID: ecd07bcd-8a9f-4a3d-b7b0-393f6b5143f7 -->

Each Prime Agent is responsible for providing and updating the required data inputs to the Risk Capital calculations. A Prime Agent may retain another party, including its Operational Executor Agent, to assist it in fulfilling these responsibilities on mutually agreed terms. However, the ultimate responsibility always remains with the Prime Agent.

###### A.3.2.2.5.2.2 - Verification Of Data Updates [Core]  <!-- UUID: b80bdd00-c88b-4186-84de-b6c770b915e0 -->

If Operational GovOps does not perform the data updates, it must verify their accuracy.

###### A.3.2.2.5.2.3 - Penalties For Late Data Updates [Core]  <!-- UUID: b6dd98ee-5156-496c-95f3-a6ad0f2eff3b -->

In the near term, Operational GovOps must reduce exposure to any Asset Allocation Conduit if the Prime Agent responsible for that Conduit fails to provide the timely information necessary to calculate the required Risk Capital. In the future, a system of monetary penalties must be developed to compensate Sky for the risk posed by late data submission.

#### A.3.2.2.6 - Process For Adjusting Risk Capital [Core]  <!-- UUID: b24ee088-0096-47b0-9e27-4c9e9aeb2d9b -->

The documents herein define how changes to the calculation of Required Risk Capital or Total Risk Capital should be handled.

##### A.3.2.2.6.1 - Updates Due To Changed Market Parameters [Core]  <!-- UUID: 86134cd1-f754-4637-8796-f239ec00e434 -->

The documents herein define the process for handling changes to Required Risk Capital requirements due to changes in market or other external variables.

###### A.3.2.2.6.1.1 - Immediate Update To Required Risk Capital For Changes In Market Or External Variables [Core]  <!-- UUID: 0932bccb-4d3e-4be8-afbf-649227a60435 -->

To the extent that a market or external variable changes in a way that increases the Aggregate Required Risk Capital, the Prime Agent is immediately responsible for supplying additional Total Risk Capital, as necessary, and is subject to penalties for any period in which this Total Risk Capital is not provided. It is the responsibility of the Prime Agent to maintain sufficient capital so that they remain well capitalized in the face of changes to market conditions.

##### A.3.2.2.6.2 - Updates Due To Changed Methodology Or Governance Parameters [Core]  <!-- UUID: 088cba75-a83b-4f85-8923-d98c36ff8714 -->

The documents herein define the process for adjusting the calculation of Required Risk Capital or Total Risk Capital whenever Sky Governance modifies the underlying methodology/parameters governing Risk Capital calculations.

###### A.3.2.2.6.2.1 - Phased Update To Risk Capital For Changes In Methodology Or Governance Parameters [Core]  <!-- UUID: 0f4b2490-bb15-480d-b719-be2bfec69c85 -->

To the extent that a change to the implementation of the Risk Capital framework or a parameter set by Sky Governance changes the Required Risk Capital or Total Risk Capital, the change will phase in over time. The Prime Agent must provide 50% of the additional Total Risk Capital necessary to comply with the change within seven (7) calendar days of the change, and the remaining 50% on a pro rata basis over the following twenty one (21) calendar days.

###### A.3.2.2.6.2.2 - No Penalties For Changes In Methodology Or Governance Parameters In Near Term [Core]  <!-- UUID: e083b732-237d-461b-92a4-fe91ea636e3f -->

In the near term as the Risk Capital implementation continues to be developed, Prime Agents will not be subject to penalties for failing to supply the incremental capital required by changes to the Risk Capital implementation. However, Operational GovOps must reduce the exposure to Allocation Conduits managed by the Prime Agent to bring it back into compliance with capital requirements if the Prime Agent does not work in good faith to provide the additional capital on the timeline specified above.

#### A.3.2.2.7 - Monitoring And Penalty Mechanisms [Core]  <!-- UUID: 50035dc9-4cab-4141-a5d8-a8a4e6870a56 -->

The documents herein define monitoring and penalty mechanisms.

##### A.3.2.2.7.1 - Monitoring As Part Of Settlement Cycle [Core]  <!-- UUID: 3fa1e746-ea64-49f0-92e3-f914e8b92b16 -->

Core GovOps reviews the calculation of Risk Capital by each Prime Agent as part of the Settlement Cycle. In the event that it detects that Risk Capital requirements were violated, it applies the penalty mechanisms specified in [A.3.2.2.7.2 - Penalty Mechanisms](b8ee2d12-c94b-4d22-b55e-d2b6e6d94ad0).

##### A.3.2.2.7.2 - Penalty Mechanisms [Core]  <!-- UUID: b8ee2d12-c94b-4d22-b55e-d2b6e6d94ad0 -->

The documents herein specify the penalty mechanisms that exist to incentivize Prime Agents and Operational Agents to ensure that sufficient capital is always held against investments by Prime Agents and to protect Sky from risks due to insufficient capital.

###### A.3.2.2.7.2.1 - Penalty Mechanisms For Prime Agents [Core]  <!-- UUID: 58d81b6e-148e-464f-b6ff-1cbbdb173fde -->

The documents herein specify the penalty mechanisms for Prime Agents for breaches of the Risk Capital requirements.

###### A.3.2.2.7.2.1.1 - Financial Penalties For Breach Of Capital Requirements [Core]  <!-- UUID: 3327c009-1d96-46c2-8094-9ca2149427e0 -->

The documents herein define the financial penalties for breaches of Risk Capital requirements.

###### A.3.2.2.7.2.1.1.1 - Encumbrance Ratio [Core]  <!-- UUID: 5435f680-aaaa-461a-bcae-4056bb8964d9 -->

The Encumbrance Ratio for a Prime Agent is the ratio of its Aggregate Required Risk Capital to its Total Risk Capital.

###### A.3.2.2.7.2.1.1.2 - Severity Of Breaches [Core]  <!-- UUID: cf1bcb59-c72a-4b17-ae4b-e80beb881f57 -->

The financial penalties for breaches of Risk Capital requirements depend on whether the breaches are Low Severity or High Severity. The documents herein define Low Severity and High Severity Breaches. The financial penalties associated with High Severity Breaches and Low Severity Breaches are defined in [A.3.2.2.7.2.1.1.4 - Financial Penalties For Low Severity Breaches](f4bef3da-45a1-4575-9e38-78f2a1f95a3d) and [A.3.2.2.7.2.1.1.5 - Financial Penalties For High Severity Breaches](970c1ce7-dc45-4c02-bad4-80c9f2e32eab), respectively.

###### A.3.2.2.7.2.1.1.2.1 - Low Severity Breach Definition [Core]  <!-- UUID: 1981fd65-a9a5-4e5a-a9f8-aa8e85342d7c -->

A Low Severity Breach is one in which the Encumbrance Ratio is greater than or equal to 100% but less than 103%.

###### A.3.2.2.7.2.1.1.2.2 - High Severity Breach Definition [Core]  <!-- UUID: 363e2bb5-47e2-4eb8-950d-eafd0f1392c7 -->

A High Severity Breach is one in which the Encumbrance Ratio is greater than 103%.

###### A.3.2.2.7.2.1.1.3 - Length Of Breaches [Core]  <!-- UUID: 9e689143-99a7-4cae-a6fc-1b1c31da4ff6 -->

The length of a breach refers to the duration measured between its defined start and end points, which depend on the specific aspect of the breach being considered.

If a breach is initially a Low Severity Breach and subsequently becomes a High Severity Breach, then (1) the length of the Low Severity Breach is the duration from when it became a Low Severity Breach until it became a High Severity Breach; and (2) the length of the High Severity Breach is the duration from when it became a High Severity Breach until that high-severity period concludes (e.g., upon final resolution of the breach or a transition to a different severity level).

Likewise, if a breach is initially a High Severity Breach and subsequently becomes a Low Severity Breach, then (1) the length of the High Severity Breach is the duration from when it became a High Severity Breach until it became a Low Severity Breach; and (2) the length of the Low Severity Breach is the duration from when it became a Low Severity Breach until that low-severity period concludes (e.g., upon final resolution of the breach or a transition to a different severity level).

###### A.3.2.2.7.2.1.1.4 - Financial Penalties For Low Severity Breaches [Core]  <!-- UUID: f4bef3da-45a1-4575-9e38-78f2a1f95a3d -->

The documents herein define the financial penalties for Low Severity Breaches.

###### A.3.2.2.7.2.1.1.4.1 - Financial Penalties For First 30 Minutes [Core]  <!-- UUID: 32750a35-acf3-4248-a5f0-6787a7fc0cd7 -->

For the first 30 minutes of a Low Severity Breach, the financial penalty is equal to a 500% annual percentage yield on the difference between Aggregate Required Risk Capital and Total Risk Capital.

###### A.3.2.2.7.2.1.1.4.2 - Financial Penalties For Subsequent 30 Minutes [Core]  <!-- UUID: 4f7e6e09-b0ca-477f-af42-a42d08ae04b7 -->

For the next 30 minutes of a Low Severity Breach after the expiration of the duration specified in [A.3.2.2.7.2.1.1.4.1 - Financial Penalties For First 30 Minutes](32750a35-acf3-4248-a5f0-6787a7fc0cd7), the financial penalty is equal to a 1,000% annual percentage yield on the difference between Aggregate Required Risk Capital and Total Risk Capital.

###### A.3.2.2.7.2.1.1.4.3 - Financial Penalties After 60 Minutes [Core]  <!-- UUID: 9da86bfb-9df0-4ea7-8e39-56dfc5ef04d9 -->

After the first 60 minutes of a Low Severity Breach, the financial penalty is equal to a 1,500% annual percentage yield on the difference between Aggregate Required Risk Capital and Total Risk Capital.

###### A.3.2.2.7.2.1.1.5 - Financial Penalties For High Severity Breaches [Core]  <!-- UUID: 970c1ce7-dc45-4c02-bad4-80c9f2e32eab -->

The documents herein define the financial penalties for High Severity Breaches.

###### A.3.2.2.7.2.1.1.5.1 - Financial Penalties For First 15 Minutes [Core]  <!-- UUID: b9bfd816-925e-4403-a4c2-fda647a2c59a -->

For the first 15 minutes of a High Severity Breach, the financial penalty is equal to a 1,500% annual percentage yield on the difference between Aggregate Required Risk Capital and Total Risk Capital.

###### A.3.2.2.7.2.1.1.5.2 - Financial Penalties For Subsequent 15 Minutes [Core]  <!-- UUID: 7d3dc8ba-d12c-4583-91eb-9a6d29dffd8d -->

For the next 15 minutes of a High Severity Breach after the expiration of the duration specified in [A.3.2.2.7.2.1.1.5.1 - Financial Penalties For First 15 Minutes](b9bfd816-925e-4403-a4c2-fda647a2c59a), the financial penalty is equal to a 2,000% annual percentage yield on the difference between Aggregate Required Risk Capital and Total Risk Capital.

###### A.3.2.2.7.2.1.1.5.3 - Financial Penalties For Subsequent 30 Minutes [Core]  <!-- UUID: 8151947c-c6e7-4551-8cb9-1cfb6e82f6d0 -->

For the next 30 minutes of a High Severity Breach after the expiration of the duration specified in [A.3.2.2.7.2.1.1.5.2 - Financial Penalties For Subsequent 15 Minutes](7d3dc8ba-d12c-4583-91eb-9a6d29dffd8d), the financial penalty is equal to a 2,500% annual percentage yield on the difference between Aggregate Required Risk Capital and Total Risk Capital.

###### A.3.2.2.7.2.1.1.5.4 - Financial Penalties After 60 Minutes [Core]  <!-- UUID: 7f70143b-ddc4-4ad1-b5e1-410fa5ba96e5 -->

After the first 60 minutes of a High Severity Breach, the financial penalty is equal to a 3,000% annual percentage yield on the difference between Aggregate Required Risk Capital and Total Risk Capital.

###### A.3.2.2.7.2.1.1.6 - Collection Of Penalties [Core]  <!-- UUID: 92bc8eae-deaa-45f2-85f4-1c010d2b5daa -->

Penalties are calculated by the Core Executor Agents as part of the Monthly Settlement Cycle. See [A.2.4 - Sky Core Monthly Settlement Cycle](6f8d5065-d6ff-4add-9a28-eadeffa7ed1a). Once calculated, penalties are transferred from the Prime Agent’s SubProxy Account to Sky by Sky Governance.

###### A.3.2.2.7.2.1.1.6.1 - Alternative Enforcement Mechanisms [Core]  <!-- UUID: 8067694d-e7a2-46ed-8e35-50f0ecde79c7 -->

In the event that the Prime Agent’s Total Risk Capital is less than its Required Risk Capital at the time of the Monthly Settlement Cycle, or the collection of the penalty would cause the Prime Agent’s Total Risk Capital to fall below its Required Risk Capital, then Sky may exercise the alternative enforcement mechanism described below.

In this instance Sky, at its discretion, may issue additional tokens of the Prime Agent and sell them on the open market until it has collected proceeds equal to the calculated penalty. Any proceeds above the calculated penalty shall be refunded to the Prime Agent SubProxy account.

Alternatively, Sky may convert the penalty into a debt owed by the Prime Agent to Sky Core at terms mutually agreed between Sky Core and the Prime Agent.

###### A.3.2.2.7.2.1.1.7 - Short-Term Exemption [Core]  <!-- UUID: 829e886b-0d00-488a-bb27-27f12dae9b3b -->

While the Risk Framework undergoes refinement, penalties for any Prime Agent breaches of Required Risk Capital will be calculated by Core GovOps once the infrastructure is in place to do so. This calculation serves the purposes of system monitoring, data gathering, and framework calibration. However, throughout this interim phase, such calculated penalties will not be formally assessed against Prime Agents, and consequently, Prime Agents will not be required to make payment for these penalties. Notwithstanding this temporary exemption from penalty payment, Prime Agents are expected to maintain a Encumbrance Ratio of less than or equal to 90%. See [A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9).

###### A.3.2.2.7.2.1.2 - Additional Token Issuance For Breach Of Capital Requirements [Core]  <!-- UUID: 2e1a8489-5849-4030-9ed8-8b9a0b09d483 -->

In the event that financial penalties are not sufficient to address the shortfall because payment of the penalties would exacerbate an existing capital shortfall, Core GovOps may require the Prime Agent to issue additional tokens and sell them to the extent it deems necessary. Operational GovOps will assist Core GovOps in executing any such transaction. Future iterations of the Risk Capital framework will specify a more detailed methodology for required token issuance.

###### A.3.2.2.7.2.1.3 - Restrictions On Investments For Breach Of Capital Requirement [Core]  <!-- UUID: 291f2548-a473-42f2-b5be-8fad854d8df3 -->

Core GovOps may impose whatever restrictions it deems necessary on the usage of the Allocation System Primitive by the Prime Agent, including limiting the Prime Agent’s exposure to certain Instances (conduits) or prohibiting the Prime Agent from using certain Instances. These restrictions may extend for a period of time that Core GovOps deems fit.

###### A.3.2.2.7.2.1.4 - Conservatorship For Breach Of Capital Requirements [Core]  <!-- UUID: 5c3dd35a-0c67-44c2-b51b-d40bc865af85 -->

In the event that less extreme measures are not adequate to address the capital shortfall, Core GovOps may seek to put the Prime Agent into conservatorship, in which case the Sky Core Facilitator takes direct control of the Prime Agent to maximize value for Sky and other Prime Agent stakeholders. Seeking to put a Prime Agent into conservatorship requires immediate escalation to Sky Core Governance and requires an expedited Executive Vote as specified in [A.1.9.1.5.4.1 - Known And Uncontentious Remedies](3f5f79fa-698c-42db-a941-ead5a5d0aa48).

###### A.3.2.2.7.2.2 - Penalty Mechanisms For Operational Executor Agents [Core]  <!-- UUID: a56f0e2a-2e3e-45a5-8aac-c7708ff4e20d -->

The documents herein specify the penalty mechanisms for Operational Executor Agents for breaches of Risk Capital requirements.

###### A.3.2.2.7.2.2.1 - Financial Penalties For Operational Executor Agents [Core]  <!-- UUID: 134f7d3e-fee1-4d9d-aef8-1e5a9b390d21 -->

In the near term there are no penalties for Operational Executor Agents for failure of the Prime Agents they supervise to maintain appropriate levels of capital. In future iterations of the Risk Framework, Operational Executor Agents will be required to put up collateral and act as "insurers" of all activities by the Prime Agents they supervise with regard to the Sky Primitives. At that point Core GovOps will be able to seize this collateral in the event of failure to obtain compensation for breaches of the Risk Capital requirement by the Prime Agent.

###### A.3.2.2.7.2.2.2 - Termination Of Executor Accord [Core]  <!-- UUID: 782d49c6-e4db-4d4a-be29-3f005cd654c1 -->

In the event that Core GovOps determines that the Operational Executor Agent is not appropriately supervising the activities of the Prime Agent, Core GovOps may terminate the respective Executor Accord. This requires an immediate escalation to Sky Governance and requires an expedited Executive Vote as specified in [A.1.9.1.5.4.1 - Known And Uncontentious Remedies](3f5f79fa-698c-42db-a941-ead5a5d0aa48). Core GovOps must arrange for another Operational Executor Agent to stand in until the Prime Agent can Invoke the Executor Accord Primitive to enter into a new Executor Accord. The Prime Agent must suspend all operations until a new Executor Accord is voted on and formally integrated into the Agent’s Artifact.

###### A.3.2.2.7.2.3 - Escalation To Sky Governance [Core]  <!-- UUID: 7ff23236-91c4-4c5c-b462-d4427b03bfd4 -->

The documents herein specify measures for escalating situations directly to Sky Governance in the event that they cannot be resolved by Core GovOps.

###### A.3.2.2.7.2.3.1 - Triggers For Escalation [Core]  <!-- UUID: 36978109-324d-40da-be44-f05809c1544a -->

In the event of a disagreement regarding the penalties for a violation of Risk Capital requirements, either party may escalate the matter to Sky Governance. In addition, the extraordinary remedies of Prime Agent Conservatorship and Executor Accord Termination must always be escalated to a Sky Governance Executive Vote.

###### A.3.2.2.7.2.3.2 - Sky Governance Process [Core]  <!-- UUID: 1ccb4063-facc-42d6-a71e-21fe29e84519 -->

Once a matter has been escalated to Sky Governance, the Sky Core Facilitator may request any information they deem necessary from Core GovOps, Operational GovOps, and the Prime Agent. Sky Governance then acts through a Governance Poll to determine its resolution of the matter.

## A.3.3 - Asset Liability Management [Article]  <!-- UUID: 6478afd5-7c3f-4bed-a2b7-9f8ee402bb64 -->

The Asset Liability Management framework establishes universal rules for Prime Agents deploying Sky’s Collateral Portfolio to maintain the stability of the USDS peg through highly liquid assets. The Asset Liability Management framework governs collateral allocation across all Agents, via the Allocation System Primitive, and replaces Sky Core’s historical Asset Liability Management mechanisms which will be offboarded entirely or transitioned to Prime Agents.

### A.3.3.1 - Conceptual Framework [Section]  <!-- UUID: dbdb3a38-4438-44a0-af77-9518ada97301 -->

This section defines the conceptual framework for Asset Liability Management.

#### A.3.3.1.1 - Minimum Actively Stabilizing Collateral [Core]  <!-- UUID: de00cd5a-91ab-4c04-8ce1-8aa3b7f3c82b -->

The "Sky Collateral Portfolio" consists of all assets backing USDS, whether deployed by Prime Agents or Sky Core. The Asset Liability Management framework is based on ensuring that a certain percentage of Sky Collateral Portfolio is invested in Actively Stabilizing Collateral, highly liquid market making non-USDS assets that trade for close to 1 USD per USDS. In this way, if there is ever downward pressure on the price of USDS these assets can be used to buy USDS to maintain the peg.

#### A.3.3.1.2 - Minimum Demand Absorption Buffer [Core]  <!-- UUID: 00592be0-8d84-4d3f-8c36-1454b18c27ec -->

The Asset Liability Management also ensures that a certain percentage of the Sky Collateral Portfolio is invested in a Demand Absorption Buffer, highly liquid market making USDS assets that trade for close to 1 USD per USDS. In this way, if there is ever upward pressure on the price of USDS these assets can be used to sell USDS to maintain the peg.

#### A.3.3.1.3 - Application To Prime Agents [Core]  <!-- UUID: 810270db-2436-411b-94e4-afbc66492531 -->

Each Prime Agent investing a portion of the Sky Collateral Portfolio must maintain, with respect to its portion of same, the percentage of Actively Stabilizing Collateral and Demand Absorption Buffer specified in [A.3.3.2.2 - Minimum Actively Stabilizing Collateral](475fe222-9e4a-4e9d-9be6-a7a424ce02f8). By ensuring that every Prime Agent maintains these levels, Sky as a whole remains compliant with the required thresholds of Actively Stabilizing Collateral and Demand Absorption Buffer.

##### A.3.3.1.3.1 - Agent Collateral Portfolio [Core]  <!-- UUID: 64e1390f-68a1-43ec-87a8-8ae7b990f7ec -->

An Agent Collateral Portfolio is defined as the total amount of capital that the Prime Agent has deployed from Sky through the Allocation System Primitive, excluding any portion of that capital held in USDS. See [A.2.2.10.1 - Allocation System Primitive](9db14ab7-bb4b-4751-8084-843bd4359f2a).

##### A.3.3.1.3.2 - Actively Stabilizing Collateral [Core]  <!-- UUID: c825a54b-8696-452c-b963-cbe999f61bad -->

Actively Stabilizing Collateral is collateral that actively supports the peg of USDS by market-making and providing buy support at a price close to 1 USD per USDS. The implementation of the Asset Liability Management framework specifies the downside spread that is allowed for collateral to qualify as Actively Stabilizing Collateral. See [A.3.3.2 - Implementation](bf1a1991-1c2b-457c-b1ca-6147049e93c5).

##### A.3.3.1.3.3 - Demand Absorption Buffer [Core]  <!-- UUID: 1a4a64fc-240b-4671-a333-3b35dc1e1e2f -->

The Demand Absorption Buffer is USDS that actively supports the peg of USDS by market-making and providing sell support at a price close to 1 USD per USDS. The implementation of the Asset Liability Management framework specifies the upside spread that is allowed for USDS to qualify toward the Demand Absorption Buffer. See [A.3.3.2 - Implementation](bf1a1991-1c2b-457c-b1ca-6147049e93c5).

#### A.3.3.1.4 - Application To Sky Core [Core]  <!-- UUID: 6e050b66-0bc8-43f1-b32d-2220c9df466b -->

While its legacy ALM infrastructure is being transferred to Prime Agents, Sky Core manages the portion of the Sky Collateral Portfolio not deployed by Prime Agents ("Sky Core Collateral Portfolio"). During this transitional period, Sky Core allocates the Sky Core Collateral Portfolio to Actively Stabilizing Collateral as specified in [A.3.3.2.6 - Sky Core Asset Liability Management Rules](8135523a-dd5f-482d-b522-ec4227746eaf).

#### A.3.3.1.5 - Peg Defense Event [Core]  <!-- UUID: 60d8fa49-f7cc-4b2e-b54a-cdd19b1e0a09 -->

In addition to the requirement for Prime Agents to hold a certain percentage of their Collateral Portfolio in Actively Stabilizing Collateral and the Demand Absorption Buffer, Prime Agents have special responsibilities in extraordinary situations where the stability of the peg is threatened. The definition of these events and the obligations for Prime Agents are specified in the implementation of the framework. See [A.3.3.2 - Implementation](bf1a1991-1c2b-457c-b1ca-6147049e93c5).

#### A.3.3.1.6 - Asset Liability Management Rental [Core]  <!-- UUID: 1a7f0b6c-4ec2-4a5f-bb43-deab9305aab6 -->

To allow the Asset Liability Management obligation of Prime Agents to be satisfied in the most efficient way possible, Prime Agents may enter into Asset Liability Management Rentals between each other, as specified in the Asset Liability Management Rental Primitive. This allows one Prime Agent to hold a greater amount of Actively Stabilizing Collateral to offset another Prime Agent holding a lesser amount. Thus, the overall level of Actively Stabilizing Collateral is unaffected but the Actively Stabilizing Collateral can be held by a Prime Agent that is able to more efficiently hold it.

##### A.3.3.1.6.1 - All Asset Liability Management Obligations Are Rented Together [Core]  <!-- UUID: d2895e10-71cf-416e-8c9c-3f3a9ff80d10 -->

When Asset Liability Management obligations are rented, the associated obligations with regard to Actively Stabilizing Collateral, Demand Absorption Buffer, and Peg Defense Events are all transferred together.

### A.3.3.2 - Implementation [Section]  <!-- UUID: bf1a1991-1c2b-457c-b1ca-6147049e93c5 -->

This Section defines the current implementation of the Asset Liability Management framework.

#### A.3.3.2.1 - Definitions [Core]  <!-- UUID: d6c1d594-eb4a-4a81-b643-977c5c995d7a -->

The documents herein define terms used through the implementation of the Asset Liability Management framework.

##### A.3.3.2.1.1 - Peg Stability Module [Core]  <!-- UUID: 0082c12d-f1a7-46ff-a4aa-5fe42ece1a4d -->

A Peg Stability Module ("PSM") allows users to swap a given collateral type directly for Dai or USDS at a fixed rate, rather than borrowing Dai or USDS. The PSM contract was designed with Stablecoin collateral in mind, allowing users to swap other Stablecoins for Dai or USDS at a fixed rate to aid with keeping Dai or USDS pegged to one (1) USD.

A PSM operates similarly to a regular vault type with a zero Stability Fee and a liquidation ratio of 100% that can only be accessed through a user-facing smart contract containing the relevant swap functions. Unlike regular vaults, users of the PSM do not retain ownership of the asset and borrow Dai or USDS. Instead, PSM users swap the asset directly for Dai or USDS.

##### A.3.3.2.1.2 - Low Risk Real World Assets [Core]  <!-- UUID: 590c645c-8045-4053-9ab1-ea718b62f770 -->

Low Risk RWAs ("LRR") are safe, short-term treasury strategies of less than one (1) year duration.

##### A.3.3.2.1.3 - Cash Stablecoins [Core]  <!-- UUID: 066a4d9f-13ed-4ac3-a55a-df7bf3429649 -->

Cash Stablecoins are defined as USDC, USDT, and pyUSD.

#### A.3.3.2.2 - Minimum Actively Stabilizing Collateral [Core]  <!-- UUID: 475fe222-9e4a-4e9d-9be6-a7a424ce02f8 -->

Prime Agents must maintain at least 5% of their Collateral Portfolio in Actively Stabilizing Collateral.

##### A.3.3.2.2.1 - Actively Stabilizing Collateral [Core]  <!-- UUID: 62495dee-8d2a-45d4-87c4-01150e3db3c8 -->

Actively Stabilizing Collateral is the sum of (1) Resting Actively Stabilizing Collateral and (2) Latent Actively Stabilizing Collateral.

###### A.3.3.2.2.1.1 - Resting Actively Stabilizing Collateral [Core]  <!-- UUID: 0e17b35a-c830-4695-b63c-5ef58b249d3f -->

Resting Actively Stabilizing Collateral must provide buy support at a price of at least 0.999 USD per USDS (10bps downside spread). Resting Actively Stabilizing Collateral includes Cash Stablecoins in PSMs or decentralized exchanges (e.g., Curve), other stablecoins, crypto assets, or off-chain Real World Asset (RWA) loans to market makers, provided they meet the specified redemption price and transparency requirements.

###### A.3.3.2.2.1.1.1 - Resting Actively Stabilizing Collateral Calculations [Core]  <!-- UUID: 4e8cd2d1-4c74-49fd-b3fe-f8b6ccc1a79f -->

Resting Actively Stabilizing Collateral is currently calculated as the sum of:

1. USDC in the LitePSM;
2. USDC in the PSM3 on Base, Arbitrum, Unichain, Optimism;
3. Cash Stablecoins in Curve (paired with USDS);
4. USDC in GUNI 0.01%;
5. USDC in GUNI 0.05%; and
6. Cash Stablecoins in Uniswap (paired with USDS).

###### A.3.3.2.2.1.2 - Latent Actively Stabilizing Collateral [Core]  <!-- UUID: 300d45c5-96b4-47ad-9471-8122534d9bc4 -->

Latent Actively Stabilizing Collateral consists of Cash Stablecoins that do not qualify as Resting Actively Stabilizing Collateral but can be converted to Resting Actively Stabilizing Collateral. Latent Actively Stabilizing Collateral may include Cash Stablecoins deposited into lending protocols, Cash Stablecoins used to provide liquidity to decentralized exchanges, or liquid staking derivatives of cash stablecoins.

Assets must satisfy the following requirements to qualify as Latent Actively Stabilizing Collateral:

1. The assets must be verifiable onchain or through reputable APIs or oracles;
2. The assets must be able to be converted into Resting Actively Stabilizing Collateral within 15 minutes under normal market conditions; and
3. The process to convert the assets into Resting Actively Stabilizing Collateral must be fully automated and triggered automatically when ASC falls below specified levels.

###### A.3.3.2.2.1.2.1 - Latent Actively Stabilizing Collateral Calculations [Core]  <!-- UUID: 35ce6b38-9fc1-456e-93da-10ab1468a8bf -->

Latent Actively Stabilizing Collateral is currently calculated as the sum of:

1. Cash Stablecoins in Curve (not paired with USDS);
2. Cash Stablecoins in Uniswap (not paired with USDS);
3. Cash Stablecoins in SparkLend;
4. Cash Stablecoins in Aave;
5. Cash Stablecoins in Morpho; and
6. Cash Stablecoins in a Prime ALM Proxy.

The Core Executor Agents, in consultation with the Core Council Risk Advisor, may impose limitations on the size of exposures to these protocols or to specific pools within these protocols that qualify as Latent Actively Stabilizing Collateral in order to prevent excessive risk to Sky.

###### A.3.3.2.2.1.2.2 - Maximum Latent Actively Stabilizing Collateral [Core]  <!-- UUID: 5e300cdb-b221-4b6f-9c4a-11502133a1f9 -->

Latent Actively Stabilizing Collateral may not exceed 25% of Actively Stabilizing Collateral.

##### A.3.3.2.2.2 - Penalties For Failing To Satisfy Actively Stabilizing Collateral Requirement [Core]  <!-- UUID: 51de8003-cdf3-4f86-93a1-1cc3424f299e -->

In the near term there will be no penalties for Prime Agents for failing to maintain the Minimum Actively Stabilizing Collateral. Instead, failures to maintain the Minimum Actively Stabilizing Collateral will be detected and reported as specified in [A.3.3.2.2.2.1 - Reporting Of Failures To Satisfy Actively Stabilizing Collateral Requirement](b74ba49a-de9e-4c4c-866c-b04d9dd208f7).

###### A.3.3.2.2.2.1 - Reporting Of Failures To Satisfy Actively Stabilizing Collateral Requirement [Core]  <!-- UUID: b74ba49a-de9e-4c4c-866c-b04d9dd208f7 -->

In the near term, the Core Council Risk Advisor must develop a tool to automatically detect and report failures by Prime Agents to maintain the Minimum Actively Stabilizing Collateral. Each violation by a Prime Agent must be reported within 24 hours to the following parties:

- the Core Facilitator;
- Core GovOps;
- the Operational Facilitator for the Prime Agent;
- Operational GovOps for the Prime Agent; and
- the Prime Agent.

##### A.3.3.2.2.3 - Near Term Exemption For Keel [Core]  <!-- UUID: 864611dd-38cd-493e-b594-a85610a9c63e -->

In the near term, due to limitations in the infrastructure on Solana, Keel is exempt from the requirement to maintain the Minimum Actively Stabilizing Collateral. This exemption will be removed in a future iteration of the Asset Liability Management Framework.

##### A.3.3.2.2.4 - Near Term Actively Stabilizing Collateral Incentive [Core]  <!-- UUID: e5d2d3c1-701c-4420-91a3-d02bc4aa50eb -->

In the near term, Prime Agents are eligible for an Actively Stabilizing Collateral Incentive for fulfilling Actively Stabilizing Collateral requirements.

###### A.3.3.2.2.4.1 - Calculation [Core]  <!-- UUID: 693330d6-9072-4054-bd61-d788537e34e8 -->

The Actively Stabilizing Collateral Incentive is calculated on a per block basis as follows:

`Actively Stabilizing Collateral Incentive = Eligible Actively Stabilizing Collateral * (Base Rate - SOFR)`

The parameters of this formula are defined in [A.3.3.2.2.4.1.1 - Eligible Actively Stabilizing Collateral](e0b95f42-2021-44ab-a979-491a113ccbc1), and SOFR is specified in [A.3.3.2.2.4.1.3 - Secured Overnight Financing Rate](2edd1333-6ca6-4c10-9d71-80b85d4a4265).

###### A.3.3.2.2.4.1.1 - Eligible Actively Stabilizing Collateral [Core]  <!-- UUID: e0b95f42-2021-44ab-a979-491a113ccbc1 -->

The Eligible Actively Stabilizing Collateral is the lesser of (1) the Prime Agent’s Actively Stabilizing Collateral and (2) the Prime Agent’s Minimum Actively Stabilizing Collateral specified in [A.3.3.2.2 - Minimum Actively Stabilizing Collateral](475fe222-9e4a-4e9d-9be6-a7a424ce02f8).

###### A.3.3.2.2.4.1.2 - Base Rate [Core]  <!-- UUID: 0569aabe-179a-42ed-bb9e-24dd0a74408c -->

The Base Rate is specified in [A.3.1.2.1 - Base Rate](228f9955-6bba-4252-a101-5529e7a300b9).

###### A.3.3.2.2.4.1.3 - Secured Overnight Financing Rate [Core]  <!-- UUID: 2edd1333-6ca6-4c10-9d71-80b85d4a4265 -->

The Secured Overnight Financing Rate ("SOFR") is, as of any date of determination, the rate (expressed as an annual rate) measuring the cost of overnight borrowing collateralized by United States Treasury securities, as administered and published by the Federal Reserve Bank of New York (or any successor administrator, publication, or source). If such rate is not published on the relevant date, SOFR shall be the most recently published rate prior to that date.

###### A.3.3.2.2.4.2 - Payment [Core]  <!-- UUID: 4ae6189e-231c-4a7f-b3cb-843fe495c2a8 -->

The Actively Stabilizing Collateral Incentive is paid on a monthly basis as part of the Monthly Settlement Cycle.

#### A.3.3.2.3 - Minimum Demand Absorption Buffer [Core]  <!-- UUID: 1e129119-a2ce-4978-b235-c50f2a1c5e2e -->

Every Prime Agent must maintain a Demand Absorption Buffer equal to 25% of their required Actively Stabilizing Collateral.

##### A.3.3.2.3.1 - Demand Absorption Buffer [Core]  <!-- UUID: 104c90df-9236-41bc-a6ee-a6db3e8ef097 -->

To further stabilize USDS during periods of excess supply, Prime Agents must maintain a Demand Absorption Buffer (DAB), a subset of ASC consisting of USDS that is for sale for at most 1.001 USD per USDS. The Demand Absorption Buffer includes USDS or DAI in PSMs. The Demand Absorption Buffer can also be fulfilled by autonomous systems that generate USDS dynamically through the allocation as needed.

##### A.3.3.2.3.2 - Penalties For Failing To Satisfy Demand Absorption Buffer Requirement [Core]  <!-- UUID: eabe411c-6325-4732-8615-8fb9f2037945 -->

Penalties for failing to maintain the Minimum Demand Absorption Buffer will be specified in a future iteration of the Asset Liability Management framework.

#### A.3.3.2.4 - Peg Defense Event [Core]  <!-- UUID: a61c1baa-db78-4106-b61a-62c6920a1a12 -->

The documents herein specify the obligations of Prime Agents during a Peg Defense Event.

##### A.3.3.2.4.1 - Peg Defense Event Definition [Core]  <!-- UUID: cc9b27bc-7c4e-46fd-a57c-d857875079dd -->

A Peg Defense Event is a situation where the average price of USDS on DEXes that are connected via LayerZero falls below 0.999 USD per USDS.

###### A.3.3.2.4.1.1 - Peg Defense Event Alert Tool [Core]  <!-- UUID: f2c381b3-96db-4f04-9817-6b69cdca8622 -->

The Core Council Risk Advisor, in consultation with Core GovOps, will develop a tool that calculates the average price of USDS on DEXes that are connected via LayerZero in real time. This tool must be made available to all Prime Agents and functionality must be developed that notifies Sky and Prime Agents in real time when a Peg Defense Event has been triggered.

##### A.3.3.2.4.2 - Peg Defense Obligations [Core]  <!-- UUID: 816e01d2-76a7-45ea-a770-22e4d3bc1247 -->

In a Peg Defense Event, all Prime Agents must immediately begin to buy USDS at a rate of at least 6.25% of their Actively Stabilizing Collateral requirement every six (6) hours. The six (6) hour periods run consecutively from the onset of the Peg Defense Event, and the Actively Stabilizing Collateral requirement is measured as of the start of each period. Each Prime Agent is responsible for monitoring its Actively Stabilizing Collateral requirement and maintaining sufficient capacity to satisfy this obligation for the duration of the Peg Defense Event.

###### A.3.3.2.4.2.1 - Alternatives For Satisfying Peg Defense Obligations [Core]  <!-- UUID: 58c006ae-d7a7-4e23-929a-18b2bdfe62a5 -->

Peg Defense can be performed through a combination of (1) selling other types of collateral for USDS, or (2) by using USDS, or generating new USDS via the Allocation System, that is then used as collateral to borrow other types of assets (e.g. USDC or USDT on Aave) and buy USDS with it.

##### A.3.3.2.4.3 - Penalties For Failure To Satisfy Peg Defense Obligations [Core]  <!-- UUID: 438697e3-7c67-4fc4-b174-df4d2fee176f -->

Penalties for failing to fulfill the Peg Defense Obligations will be specified in a future iteration of the Asset Liability Management framework.

#### A.3.3.2.5 - Asset Liability Management Rental [Core]  <!-- UUID: debeb71c-2689-4033-b3ab-51cd4018fed3 -->

The implementation of Asset Liability Management Rentals is specified in [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

#### A.3.3.2.6 - Sky Core Asset Liability Management Rules [Core]  <!-- UUID: 8135523a-dd5f-482d-b522-ec4227746eaf -->

Pursuant to [A.3.3.1.4 - Application To Sky Core](6e050b66-0bc8-43f1-b32d-2220c9df466b), Sky Core manages the Sky Core Collateral Portfolio by allocating capital to the Lite PSM (see [A.3.3.2.7.1.1 - Lite Peg Stability Module](39473e1a-63f8-433b-a850-08f53b2dcf02)).

#### A.3.3.2.7 - Legacy Mechanisms [Core]  <!-- UUID: da716553-ad32-4292-b11d-74b66f0683b8 -->

The documents herein outline Sky Core’s legacy ALM mechanisms. Given the launch of Prime Agents, these legacy mechanisms will be either offboarded entirely or transitioned to Prime Agents.

##### A.3.3.2.7.1 - Peg Stability Module [Core]  <!-- UUID: 29de21b4-0603-435e-8149-170f0ae2866a -->

The documents herein outline the legacy Peg Stability Module which supported Dai and USDS peg stability under Sky Core management. Going forward, the PSM will be transitioned to Grove.

###### A.3.3.2.7.1.1 - Lite Peg Stability Module [Core]  <!-- UUID: 39473e1a-63f8-433b-a850-08f53b2dcf02 -->

Control of the Lite PSM is being transitioned to Grove. Until this transition is complete, the Lite PSM continues to be controlled by Sky Core, subject to the requirements specified in [A.3.3.2.6 - Sky Core Asset Liability Management Rules](8135523a-dd5f-482d-b522-ec4227746eaf). Post-transition, Grove will manage the Lite PSM as an ASC asset pursuant to the rules defined in this Article.

###### A.3.3.2.7.1.1.1 - Lite Peg Stability Module Parameter Definitions [Core]  <!-- UUID: 9196786a-18b6-4dea-b4e2-852090371dd7 -->

The subdocuments herein define the parameters of the Lite Peg Stability Module.

###### A.3.3.2.7.1.1.1.1 - Lite Peg Stability Module Toll / Fee In Definition [Core]  <!-- UUID: 12714156-5543-4443-b733-d213db62cecb -->

`tin` is a percentage fee applied when trading the collateral asset into the PSM in exchange for Dai**.**

###### A.3.3.2.7.1.1.1.2 - Lite Peg Stability Module Toll / Fee Out Definition [Core]  <!-- UUID: a39b4df8-c022-4bfb-9339-e4d3f38715ec -->

`tout` is the percentage fee applied when trading Dai into the PSM in exchange for the collateral asset.

###### A.3.3.2.7.1.1.1.3 - Lite Peg Stability Module Maximum Debt Ceiling Definition [Core]  <!-- UUID: c1805ee8-626e-4aec-9a88-21377579aa3d -->

DC-IAM `line` is the maximum amount of debt the LitePSM can accrue.

###### A.3.3.2.7.1.1.1.3.0.3.1 - Debt Ceiling - Element Annotation [Annotation]  <!-- UUID: 3b015982-458b-4412-8469-cbcdb4a0b481 -->

The element "Debt Ceiling" refers to the maximum amount that can be borrowed against assets in a vault. Although a PSM has a zero Stability Fee and a liquidation ratio of 100%, it is still a vault and swaps of a collateral asset for Dai represent issuance of Dai that is backed by that collateral asset. The Debt Ceiling serves to limit the exposure the PSM can incur to that collateral asset.

###### A.3.3.2.7.1.1.1.4 - Lite Peg Stability Module Target Available Debt Definition [Core]  <!-- UUID: 7d56c67d-d358-4641-aa27-ada5066c0579 -->

DC-IAM `gap` is the target gap between the debt usage and the Debt Ceiling.

###### A.3.3.2.7.1.1.1.5 - Lite Peg Stability Module Ceiling Increase Cooldown Definition [Core]  <!-- UUID: 51e64b05-ddb8-4ce3-9307-1f2f8dc51a5f -->

DC-IAM `ttl` is the minimum time requirement before it is possible to increase the debt ceiling, expressed in seconds.

###### A.3.3.2.7.1.1.1.5.0.3.1 - Debt Ceiling - Element Annotation [Annotation]  <!-- UUID: f1a64ee3-d89c-4c5e-9559-10bbf4977297 -->

The element "Debt Ceiling" refers to the maximum amount that can be borrowed against assets in a vault. Although a PSM has a zero Stability Fee and a liquidation ratio of 100%, it is still a vault and swaps of a collateral asset for Dai represent issuance of Dai that is backed by that collateral asset. The Debt Ceiling serves to limit the exposure the PSM can incur to that collateral asset.

###### A.3.3.2.7.1.1.1.6 - Lite Peg Stability Module Buffer Definition [Core]  <!-- UUID: 71776219-5425-4eaf-89fe-7dea283d5a7d -->

`buf` is a fixed-sized amount of pre-minted Dai which LitePSM is designed to maintain in most situations. Note, however, that when a user calls `buyGem`, the amount of Dai available can be temporarily larger than `buf`.

###### A.3.3.2.7.1.1.1.6.0.3.1 - BuyGem - Element Annotation [Annotation]  <!-- UUID: 41d9ae0a-c3a6-4a24-ae6a-b2ee841fb03d -->

`buyGem` is a function that can be called on the LitePSM smart contract to buy a collateral asset in exchange for Dai. "Gem" here is Daiwanese for the collateral token.

The Lite Peg Stability Module maintains a pool of pre-minted Dai and Stablecoins to minimize transaction costs in swapping. The `buf` parameter is the amount of pre-minted Dai the LitePSM is designed to maintain in most instances. However, when a user calls `buyGem` and buys the collateral asset in exchange for Dai, the amount of Dai can temporarily exceed the `buf` parameter.

###### A.3.3.2.7.1.1.1.7 - Lite Peg Stability Module Authorized Parties Definition [Core]  <!-- UUID: 12d3a162-9615-4bc0-ae09-57e0cd3af222 -->

Authorized Parties are actors who are authorized by Sky Governance to use the Lite Peg Stability Module without paying swap fees.

###### A.3.3.2.7.1.1.2 - Lite Peg Stability Module Parameter Values [Core]  <!-- UUID: 8694e11a-6acd-43f1-90fd-67eb7e7d98d6 -->

The current values of the Lite Peg Stability Module parameters are:

- `tin`: 0%
- `tout`: 0%
- DC-IAM `line`: 10,000,000,000 DAI
- DC-IAM `gap`: 800,000,000 DAI
- DC-IAM `ttl`: 43,200 seconds
- `buf`: 800,000,000 DAI
- Authorized Parties: None

###### A.3.3.2.7.1.1.3 - Lite Peg Stability Module Parameter Modification [Core]  <!-- UUID: bf561ea8-ab09-4ff5-a84d-2e92bcff997b -->

The Core Facilitator, in consultation with the Core Council Risk Advisor, may recommend changes to any of the parameters specified in the subdocuments of [A.3.3.2.7.1.1.1 - Lite Peg Stability Module Parameter Definitions](9196786a-18b6-4dea-b4e2-852090371dd7). These changes will be subject to an Executive Vote through the Operational Weekly Cycle.

##### A.3.3.2.7.2 - Real World Assets [Core]  <!-- UUID: bea66a32-4cf2-4de9-9a7e-3c94c293fc3c -->

The documents herein define legacy mechanisms related to Real World Assets.

###### A.3.3.2.7.2.1 - Andromeda [Core]  <!-- UUID: 1b153f9f-7c70-4ae1-b76c-ef12f87532c6 -->

Historically, Andromeda balanced Sky Core’s Cash Stablecoin liquidity by allocating excess into low-risk treasury strategies and replenishing shortages. Control of the Andromeda RWA Arranged Structure is currently being transitioned to Grove. Until the transition to Grove is complete, Andromeda continues to be controlled by Sky Core, subject to the requirements defined in [A.3.3.2.6 - Sky Core Asset Liability Management Rules](8135523a-dd5f-482d-b522-ec4227746eaf). Post-transition, Grove will manage Andromeda as a non-ASC asset within its Collateral Portfolio, subject to JRC requirements. Andromeda is not currently operational and its debt ceiling has been reduced to zero.

###### A.3.3.2.7.2.2 - Other RWA Offboarding [Core]  <!-- UUID: ca876157-5518-4bf3-9e87-7c4a07a13d36 -->

Other than Andromeda, all old RWA exposure that was added before Endgame must stay for as long as necessary, and optimized for yield if possible. When it is possible, the Core Facilitator should take action to wind down and offboard all such Legacy RWA. Governance actions related to optimizations, wind down and offboardings can be done directly in Executive Votes with no prior Governance Poll needed.

## A.3.4 - Real World Assets [Article]  <!-- UUID: edd96df7-4058-4a74-a6e5-827df31e5fdd -->

This Article governs the secure management of Real World Assets (RWA), which serve as collateral for the USDS Stablecoin. RWAs are enforced through legal recourse by Arranged Structures and present unique risks that this Article must address.

### A.3.4.1 - Arranged Structures [Section]  <!-- UUID: 1df6a6c4-4f2e-451b-af0d-5c9eccc8762d -->

Arranged Structures are special legal structures set up by Ecosystem Actors to secure Real World Assets to help stabilize the Sky Ecosystem. Each Arranged Structure has a Conduit system which is owned by an Agent and automatically connected to all Agents; the Conduit allows them to send and receive USDS or other assets.

### A.3.4.2 - Agent Owner For Arranged Structures [Section]  <!-- UUID: 2f1ab584-bb48-4588-a4ff-a4ff0e728c89 -->

Arranged Structures must have an Agent owner. The Agent owner assigns instructions to the Arranged Structure on behalf of Sky, and determines if and how other Agents can access the Conduit of the Arranged Structure.

### A.3.4.3 - Arrangers [Section]  <!-- UUID: 12c9e05d-b47f-456f-aff9-ddece22cec62 -->

This Section defines procedures related to Arrangers, Ecosystem Actors that assist in the design and operation of Arranged Structures. Every Arranged Structure must have a designated Arranger responsible for conducting ongoing reporting. All aspects of this relationship, including the Arranger's duties, must be defined in this Section.

#### A.3.4.3.1 - Introduction [Core]  <!-- UUID: 4b110433-bf28-4c9a-b709-e2deaac9212e -->

Arrangers are Ecosystem Actors who specialize in sourcing, negotiating, structuring, and reporting on Real World Assets, as well as maintaining and monitoring the underlying Arranged Structures used by the Sky Protocol. The Arrangers manage a restricted function on the Arranged Structure Conduit that allows them to send assets onwards to the predetermined blockchain account of the Arranged Structure.

Arrangers are generally prohibited from occupying any position where they could cause damage or loss to the Sky Ecoystem, notwithstanding delays or inconveniences.

After the Arranged Structures are established and assets are allocated, Arrangers must not have the capability to operate or influence the legal and operational structure’s asset operations in any manner that could cause significant harm or losses to the stability of USDS.

Arrangers are directly approved by SKY voters, and all LRA collateral exposure must be structured by an approved Arranger.

#### A.3.4.3.2 - Onboarding And Offboarding of Arrangers [Core]  <!-- UUID: 769c492c-2282-4466-8d24-0a530f724a0c -->

When they deem it necessary, the Core Facilitator may initiate a Governance Poll to onboard or offboard Arrangers. The list of current active Arrangers is maintained in [A.3.4.3.2.1 - List Of Active Arrangers](b8791aaa-84b7-4012-8a4f-053595ec232a).

##### A.3.4.3.2.1 - List Of Active Arrangers [Core]  <!-- UUID: b8791aaa-84b7-4012-8a4f-053595ec232a -->

List of current active Arrangers:

- No current active Arrangers.

#### A.3.4.3.3 - Reporting And Stress Test Requirements [Core]  <!-- UUID: a904881f-b235-4236-8439-deea105f06d0 -->

Arrangers must publish monthly reporting on each Arranged Structure they have arranged.

Every six (6) months, Arrangers are also required to publish a stress test analysis that demonstrates how the structures would perform under historical financial crisis scenarios and other hypothetical scenarios.

The Core Facilitator must periodically fund independent Ecosystem Actors to review and verify the quality and the results of the stress tests. Should an independent review produce an unfavorable result, the Core Facilitator must propose a Governance Poll for warning, temporarily deactivating, or permanently offboarding the Arranger and/or the Asset Managers connected to the discovered issue.

To be considered compliant, Arrangers’ monthly reports must satisfy the requirements of one of the following documents:

- [A.3.4.3.3.1 - Monthly Arranger Report Requirements](7b902bb1-68b4-477d-a575-29aaa02e9e7b)
- [A.3.4.3.3.2 - Access To Accounts](47eedd39-5bb9-492f-a4aa-9405bb5d196f)

##### A.3.4.3.3.1 - Monthly Arranger Report Requirements [Core]  <!-- UUID: 7b902bb1-68b4-477d-a575-29aaa02e9e7b -->

The following information must be included in the monthly Arranger report. Each item must be reported for at least the start and end date of the reporting period. If these dates fall on days when markets are closed, the first business day after the start date and the last business day before the end date may be used instead.

- Cash balance.
- Cash income over the reporting period. Any income over $20,000 in value should be broken out as its own line item, and an explanation provided for any non-recurring or non-ordinary expenses.
- Cash expenses over the reporting period. Any expense over $20,000 in value should be broken out as its own line item, and an explanation provided for any non-recurring or non-ordinary expenses.
- Market value of publicly traded equities, ETFs, and mutual funds.
- Market value (the closing price) of publicly traded debt securities. Debt securities that are investment grade and less than 12 months from maturity may alternatively be reported at cost basis + linearly recognizing scheduled interest income.
- A valuation for illiquid or privately traded assets. This should utilize a valuation from a reputable third party with relevant expertise or follow a well-defined methodology that is explained in detail in the report.
- CUSIPs, date of purchase, date of maturity, coupon, cost basis, and face value of all publicly traded debt securities in the portfolio for the last day of the reporting period.
- USDS inflows from the Sky Protocol during the reporting period.
- Total repayments on-chain to the Sky Protocol either to a vault or for surplus. If repayments are derived from multiple sources, they should be broken out into line items for each source.
- Vault debt to the Sky Protocol.
- Copies of original statements for all bank, brokerage, exchange, custodial, or other accounts. The Arranger may redact the names for non-Arranger service providers if and only if that is a requirement of confidentiality agreements with the non-Arranger service providers.

The Core Facilitator must publicly confirm on the Sky Forum that they have reviewed the original account documentation and verified that it supports the Arranger’s summary.

##### A.3.4.3.3.2 - Access To Accounts [Core]  <!-- UUID: 47eedd39-5bb9-492f-a4aa-9405bb5d196f -->

As an alternative to the requirements set out in [A.3.4.3.3.1 - Monthly Arranger Report Requirements](7b902bb1-68b4-477d-a575-29aaa02e9e7b), the Arranger can provide the following information through public read-only access to all accounts:

- All asset balances
- All transaction amounts (non-Arranger service provider names may be redacted)
- Hold-to-maturity yields (for assets with maturity) or current yield (for assets with no maturity)

In addition, Makerburn.com ([https://makerburn.com/#/](https://makerburn.com/#/)), Daistats.com ([https://daistats.com/#/](https://daistats.com/#/)), or another dashboard must be publicly available to summarize USDS inflows and outflows from the Sky vault.

### A.3.4.4 - Agent Owner Can Change Arrangers [Section]  <!-- UUID: cb2098b0-9970-4a5b-b835-eaa4f0e2ea6f -->

The Agent owner of the Arranged Structure can change the blockchain account of the Arranged Structure and change the Arranger.

### A.3.4.5 - Perpetual Yield Strategies [Section]  <!-- UUID: 87ec737c-7c0d-4d94-a760-a1ad9935179b -->

The subdocuments herein define perpetual yield strategies and exposure targets that can be implemented by the Core Facilitator.

#### A.3.4.5.1 - Implemented By Core Facilitator [Core]  <!-- UUID: a337def8-2baf-491b-9635-4beaa628b77f -->

The Core Facilitator can implement various perpetual yield strategies, including on-chain and off-chain mechanisms, that enable the Sky Protocol to take advantage of high risk-adjusted return on perpetual yield strategies in the crypto markets.

Exposure targets specified in this document override requirements defined by other Articles of the Stability Scope.

#### A.3.4.5.2 - Perpetual Exposure [Core]  <!-- UUID: 64841755-24d5-4464-850f-6b504b1c6022 -->

The subdocuments herein define Perpetual Exposure parameters and the associated governance processes.

##### A.3.4.5.2.1 - Perpetual Exposure Direct Accumulation [Core]  <!-- UUID: 6b70f984-1b30-40e8-9644-c49151b36caa -->

The Core Facilitator can trigger Executive Votes that instruct Arranged Structures to set up mechanisms that allow them to take direct exposure to Ethena sUSDe, or use legal rails to get direct exposure through custodians.

## A.3.5 - Surplus Buffer and Smart Burn Engine [Article]  <!-- UUID: 3eb6f099-2736-4f62-9cb8-096a8fcca757 -->

This Article defines key economic parameters relating to Sky Protocol Surplus, including the Surplus Buffer and Smart Burn Engine.

### A.3.5.1 - Surplus Buffer [Section]  <!-- UUID: 9782cdc5-c274-45c2-bf4a-690f22c6a294 -->

The Surplus Buffer is the difference between Sky’s assets and liabilities. Protocol revenue increases the Surplus Buffer and expenses decrease the Surplus Buffer.

#### A.3.5.1.1 - Current Implementation [Core]  <!-- UUID: b747f341-927a-4673-817d-5e895acc9eb8 -->

The current implementation of the Surplus Buffer is the Vow contract deployed on the Ethereum Mainnet at `0xA950524441892A31ebddF91d3cEEFa04Bf454466`.

##### A.3.5.1.1.1 - Current Value [Core]  <!-- UUID: 52fa11b0-7167-47c3-9678-e879dc981127 -->

The current value of the Surplus Buffer can be calculated using the Vat contract, Sky’s central accounting contract, located on the Ethereum Mainnet at `0x35D1b3F3D7966A1DFe207aa4514C12a259A0492B`. The current value of the Surplus Buffer is the difference between:

1. The assets of the Vow contract obtained by calling the `dai` function on the Vat contract with the address of the Vow contract, and
2. The liabilities of the Vow contract obtained by calling the `sin` function on the Vat contract with the address of the Vow contract.

### A.3.5.2 - Smart Burn Engine Parameters [Section]  <!-- UUID: ddb90fee-2851-4bf0-b924-f1d73e30ce7a -->

The current Smart Burn Engine parameters are:

- kicker.khump: -200 million USDS (Threshold of Surplus Buffer for Splitter to activate)
- kicker.kbump: 6,000 USDS
- splitter.hop: 3,748 seconds
- 55% of Splitter allocation is set to accumulate SKY
- 45% of Splitter allocation is set to reward SKY stakers
- burn (the percentage of the kicker.kbump to be moved to the underlying flapper): 55% (WAD * 1)
- LSEV2-SKY-A USDS rewardsDuration: 3,748 seconds

The rewardsDuration for the LSEV2-SKY-A USDS rewards contract must be set such that it is equal to the splitter.hop parameter.

#### A.3.5.2.1 - Splitter Module [Core]  <!-- UUID: 0103ec2d-56d5-4981-be23-73cc37aa57eb -->

The Splitter Module splits funds transferred to it from the Surplus Buffer between accumulating SKY and paying USDS rewards to SKY stakers.

##### A.3.5.2.1.1 - Splitter Module Parameters [Core]  <!-- UUID: d1f57081-28e7-4646-be12-2a4d43ff6752 -->

The parameters of the Splitter Module are defined in the documents herein.

###### A.3.5.2.1.1.1 - Splitter Interval Parameter [Core]  <!-- UUID: 39a67e65-33f0-4f2c-917d-efff544cf5ab -->

The `hop` parameter is the time interval between `kicker.kbump` funds being transferred from the Surplus Buffer to the Splitter. Together with the `kicker.kbump` parameter, it controls the rate at which funds are transferred from the Surplus Buffer to the Splitter.

###### A.3.5.2.1.1.1.1 - Splitter Interval Current Value [Core]  <!-- UUID: ab46f478-56a8-4ef0-86a3-d0010c60b6b1 -->

The current value of the `hop` parameter is specified in [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a).

###### A.3.5.2.1.1.2 - SKY Accumulation Percentage Parameter [Core]  <!-- UUID: e16d6215-c2f1-4140-affd-30e52a17fd43 -->

The `burn` parameter is the percentage of each transfer from the Surplus Buffer to the Splitter that is sent to the Flapper contract, which accumulates SKY. The remainder of each transfer is sent to the contract for USDS rewards for SKY stakers.

###### A.3.5.2.1.1.2.1 - SKY Accumulation Percentage Current Value [Core]  <!-- UUID: f6b14aab-a1af-40e2-9069-2f707cbe60f0 -->

The current value of the `burn` parameter is specified in [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a).

#### A.3.5.2.2 - Kicker Module [Core]  <!-- UUID: 92e9ad85-2bbd-4c19-bfd2-87bd8bb740c6 -->

The Kicker Module allows funds to be transferred from the Surplus Buffer to the Splitter as long as the Surplus Buffer is above a specified signed threshold. This allows funds to be transferred from the Surplus Buffer to the Splitter even when the Surplus Buffer is negative, as long as the Surplus Buffer is above the specified threshold.

##### A.3.5.2.2.1 - Kicker Module Parameters [Core]  <!-- UUID: 433c317d-0c92-4a3e-9734-0eb26a9a7606 -->

The parameters of the Kicker Module are defined in the documents herein.

###### A.3.5.2.2.1.1 - Kicker Threshold Parameter [Core]  <!-- UUID: ec7a5067-db8f-421b-ba85-074a5fa9845b -->

The `khump` parameter is the minimum value of the Surplus Buffer for funds to be transferred from the Surplus Buffer to the Splitter contract. It is a signed integer with `RAD` precision.

###### A.3.5.2.2.1.1.1 - Kicker Threshold Current Value [Core]  <!-- UUID: ce3affe8-9e1f-4825-82bd-40c320a1c220 -->

The current value of the `khump` parameter is specified in [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a).

###### A.3.5.2.2.1.2 - Kicker Lot Size Parameter [Core]  <!-- UUID: fc9cece1-84bf-4133-a2ef-ef2182a23a35 -->

The `kbump` parameter is the amount of funds transferred from the Surplus Buffer to the Splitter every `splitter.hop` interval when the Surplus Buffer is greater than `kbump`. Together with the `splitter.hop` parameter, it controls the rate at which funds are transferred from the Surplus Buffer to the Splitter.

###### A.3.5.2.2.1.2.1 - Kicker Lot Size Current Value [Core]  <!-- UUID: 443e0ae4-11d6-43f9-9988-f0e73926bf60 -->

The current value of the kbump parameter is specified in [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a).

##### A.3.5.2.2.2 - Deployment [Core]  <!-- UUID: 0803e6b5-5755-431c-9ef0-999115f6f897 -->

The activation of the Kicker Module will be executed in the October 30, 2025 Executive Vote. This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll.

#### A.3.5.2.3 - Modification [Core]  <!-- UUID: 499570de-9fae-4009-be34-c3330266030a -->

The Core Facilitator, in consultation with the Core Council Risk Advisor, can modify the `kbump` and `hop` parameters of the Smart Burn Engine. Such a modification can be enacted either by proposing it for inclusion in an Executive Vote pursuant to the Operational Weekly Cycle, without requiring a prior Governance Poll, or by executing it directly through the SBE-BEAM within its bounds, as specified in [A.3.5.2.4 - Smart Burn Engine Bounded External Access Module](b57ac61b-f6b1-4025-bd44-569d0f2afe2f). LSEV2-SKY-A-USDS rewardsDuration should always match the value of the `hop` parameter without requiring prior governance authorization.

The Core Facilitator must modify all parameters of the Smart Burn Engine as necessary to implement the allocation specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121). Such a modification can be enacted either by proposing it for inclusion in an Executive Vote pursuant to the Operational Weekly Cycle, without requiring a prior Governance Poll, or by executing it directly through the SBE-BEAM within its bounds.

Except as provided in the preceding paragraphs, modifications to the parameters of the Smart Burn Engine require a Governance Poll followed by an Executive Vote.

#### A.3.5.2.4 - Smart Burn Engine Bounded External Access Module [Core]  <!-- UUID: b57ac61b-f6b1-4025-bd44-569d0f2afe2f -->

The Smart Burn Engine Bounded External Access Module (SBE-BEAM) enables a designated, Governance-whitelisted Operator to adjust the Kicker Lot Size (`kbump`), the SKY Accumulation Percentage (`burn`), and the Splitter Interval (`hop`) parameters of the Smart Burn Engine, as specified in [A.3.5.2.2.1.2 - Kicker Lot Size Parameter](fc9cece1-84bf-4133-a2ef-ef2182a23a35), [A.3.5.2.1.1.2 - SKY Accumulation Percentage Parameter](e16d6215-c2f1-4140-affd-30e52a17fd43), and [A.3.5.2.1.1.1 - Splitter Interval Parameter](39a67e65-33f0-4f2c-917d-efff544cf5ab). Adjustments are governed by the SBE-BEAM smart contract logic and specific parameters set by Sky Governance.

The SBE-BEAM Operator can raise or lower these parameters within the bounds set by Sky Governance. Those bounds are one-sided guardrails on the rate of accumulation: the Kicker Lot Size cannot be set above `maxKbump`, the Splitter Interval cannot be set below `minHop`, and the combined throughput, expressed as the Kicker Lot Size divided by the Splitter Interval, cannot exceed `maxRate`. The rate of accumulation therefore cannot be raised beyond the maximum that Sky Governance has sanctioned, while no corresponding bound limits reductions to it. The SKY Accumulation Percentage (`burn`) is not subject to these bounds, which limit only the rate of accumulation, and the only technical constraint on it is the maximum specified in [A.3.5.2.4.4 - Technical Limitations](42ea8a7b-fb28-455e-8038-5fcf25250f17). The `tau` parameter separately requires a minimum interval between operations, applying to any operation regardless of whether it raises or lowers the parameters. The SBE-BEAM holds the following bounding parameters: (i) `maxKbump`, (ii) `minHop`, (iii) `maxRate`, and (iv) `tau`. The bases on which these parameters may be modified are specified in [A.3.5.2.3 - Modification](499570de-9fae-4009-be34-c3330266030a).

##### A.3.5.2.4.1 - Definitions [Core]  <!-- UUID: 3c9cac20-2f48-4bcb-a05b-05a192a54651 -->

The documents herein define the bounding parameters of the SBE-BEAM.

###### A.3.5.2.4.1.1 - Max Kbump Definition [Core]  <!-- UUID: 53370eb5-8fc7-4600-8f52-46615e03801e -->

The `maxKbump` parameter defines the maximum permitted value of the `kbump` parameter when set using the SBE-BEAM. The SBE-BEAM can set `kbump` to any value at or below `maxKbump`, whether that raises or lowers the current value, but cannot set `kbump` above `maxKbump`.

###### A.3.5.2.4.1.2 - Min Hop Definition [Core]  <!-- UUID: b1cbaeb4-4e7f-45f4-a033-e338c6855499 -->

The `minHop` parameter defines the minimum permitted value of the `hop` parameter when set using the SBE-BEAM. The SBE-BEAM can set `hop` to any value at or above `minHop`, whether that raises or lowers the current value, but cannot set `hop` below `minHop`.

###### A.3.5.2.4.1.3 - Max Rate Definition [Core]  <!-- UUID: f700ba6e-7aa4-4d47-addf-981c32f3c49d -->

The `maxRate` parameter defines the maximum combined throughput, expressed as `kbump` divided by `hop`, that can result from adjustments made using the SBE-BEAM. Because `hop` is denominated in seconds, this throughput is a quantity per second.

###### A.3.5.2.4.1.4 - Tau Definition [Core]  <!-- UUID: 6c389eb2-8f50-4b6b-ad77-deb27c9f9fb0 -->

The `tau` parameter defines the minimum time interval, in seconds, that must elapse between consecutive uses or operations of the SBE-BEAM.

A SBE-BEAM operation may adjust one or more parameters. Once a SBE-BEAM operation is executed, the `tau` duration must expire before any subsequent SBE-BEAM operation can be performed. This interval applies to every operation regardless of whether it raises or lowers the affected parameters.

##### A.3.5.2.4.2 - Parameters [Core]  <!-- UUID: 18e80e4a-ce0f-4dc4-87f1-d58252935860 -->

The bounding parameters set by Sky Governance for the SBE-BEAM are as follows:

- The value of the `maxKbump` parameter is 12,000 USDS.
- The value of the `minHop` parameter is 550 seconds.
- The value of the `maxRate` parameter is 350,000,000 USDS per year.
- The value of the `tau` parameter is 1,800 seconds.

##### A.3.5.2.4.3 - Parameter Adjustments [Core]  <!-- UUID: 335c6d95-56ac-46b8-a15a-7bfc748fb5e7 -->

All SBE-BEAM bounding parameters can be modified by Sky Governance, through the Operational Weekly Cycle or, if necessary, through out-of-schedule Executive Votes. Such changes are proposed by the Core Facilitator, on behalf of the Core Council and in consultation with the Core Council Risk Advisor.

##### A.3.5.2.4.4 - Technical Limitations [Core]  <!-- UUID: 42ea8a7b-fb28-455e-8038-5fcf25250f17 -->

The SBE-BEAM enforces technical limitations, including the following, that apply independently of the bounding parameters set by Sky Governance. An attempt to use the SBE-BEAM in a manner that exceeds these limitations will revert.

The `hop` parameter cannot be set higher than five (5) years. This limitation prevents the Smart Burn Engine from being placed in a state in which its reward stream — the staking rewards funded by the non-burned portion of surplus and streamed out over the Splitter Interval — can no longer be revived through the SBE-BEAM.

The `burn` parameter cannot be set higher than 100%, the point at which the entire surplus is directed to SKY accumulation. A higher value would cause the Smart Burn Engine to halt.

The `kbump` parameter must be set to a whole multiple of `RAY` (10²⁷). A value that is not an exact multiple of `RAY` will revert, ensuring the Kicker Lot Size is always expressed in the protocol's standard fixed-point precision.

##### A.3.5.2.4.5 - Operators [Core]  <!-- UUID: 2674da52-7a73-447f-811e-7dd40d23559f -->

The SBE-BEAM Operator is a Governance-whitelisted entity that can use the SBE-BEAM to alter the three Smart Burn Engine parameters within its control — the Kicker Lot Size (`kbump`), the SKY Accumulation Percentage (`burn`), and the Splitter Interval (`hop`). Changes to the `kbump` and `hop` parameters, and to their combined throughput, are limited by the `maxKbump`, `minHop`, and `maxRate` parameters, and every change is subject to the `tau` cadence. The `burn` parameter is not subject to the `maxKbump`, `minHop`, or `maxRate` bounds, which limit only the rate of accumulation, and the only technical constraint on it is the maximum specified in [A.3.5.2.4.4 - Technical Limitations](42ea8a7b-fb28-455e-8038-5fcf25250f17). The Operator can be changed by an Executive Vote.

###### A.3.5.2.4.5.1 - Operator Multisig [Core]  <!-- UUID: adf22311-1610-4da8-881e-29e00c590497 -->

The Operator Multisig is the Operator of the SBE-BEAM.

###### A.3.5.2.4.5.1.1 - Operator Multisig Address [Core]  <!-- UUID: 3bd78b59-47da-4c65-b07c-9d19936d40ac -->

The address of the Operator Multisig on the Ethereum Mainnet is `0x869294B42B80f99CF3Bdac0F44abddAd6cD41330`.

###### A.3.5.2.4.5.1.2 - Operator Multisig Required Number Of Signers [Core]  <!-- UUID: 7ac2cb75-152e-45dc-8303-62e4fbc1b4f3 -->

The Operator Multisig has a 4/6 signing requirement.

###### A.3.5.2.4.5.1.3 - Operator Multisig Signers [Core]  <!-- UUID: 91992754-8cef-4f78-9ac1-21e6abe6dc5d -->

The signers of the Operator Multisig are two (2) addresses controlled by the Core Facilitator, two (2) addresses controlled by Core GovOps, and two (2) addresses controlled by Operational GovOps Soter Labs.

###### A.3.5.2.4.5.1.4 - Operator Multisig Usage Standards [Core]  <!-- UUID: 573251d9-8d1a-417d-a113-74c327eb88c2 -->

The signers of the Operator Multisig must use the multisig to operate the SBE-BEAM in accordance with the instructions specified in [A.3.5.2.4.6 - Update Process](859e8e2f-61da-453f-91bb-f50f701149c8).

###### A.3.5.2.4.5.1.5 - Operator Multisig Modification [Core]  <!-- UUID: 5c65c1e4-b03a-4f5c-b665-6dc4abcec1be -->

The signers can change the signers of the Operator Multisig so long as:

- there are exactly six (6) signers;
- exactly four (4) signers are required to execute transactions; and
- two (2) signers are controlled by the Core Facilitator, two (2) signers are controlled by Core GovOps, and two (2) signers are controlled by Operational GovOps Soter Labs.

##### A.3.5.2.4.6 - Update Process [Core]  <!-- UUID: 859e8e2f-61da-453f-91bb-f50f701149c8 -->

The Smart Burn Engine parameters are managed by the SBE-BEAM Operator through the SBE-BEAM, as specified in the documents herein. The SBE-BEAM Operator's use of this authority must adhere to the requirements specified in [A.3.5.2.3 - Modification](499570de-9fae-4009-be34-c3330266030a).

###### A.3.5.2.4.6.1 - Recommendation By Core Council Risk Advisor [Core]  <!-- UUID: bda72e6a-195a-454d-8f18-a71b359c668f -->

A recommendation to modify the Smart Burn Engine parameters through the SBE-BEAM must be posted to the Sky Forum by the Core Council Risk Advisor. See [A.3.5.2.3 - Modification](499570de-9fae-4009-be34-c3330266030a).

###### A.3.5.2.4.6.2 - Agreement By Core Facilitator [Core]  <!-- UUID: e2feece4-ec13-4270-87c6-a783262de558 -->

Before a recommended change is executed, the Core Facilitator must post to the Sky Forum to indicate its agreement with the recommendation.

###### A.3.5.2.4.6.3 - Execution By Operator [Core]  <!-- UUID: 5a5b2774-4c67-4c24-b040-f844da58c91c -->

Once the Core Facilitator has agreed to a recommended change, the Operator prepares and executes the change through the SBE-BEAM. Preparation can include the creation of transaction simulations to verify inputs.

###### A.3.5.2.4.6.4 - Public Communication [Core]  <!-- UUID: af8ff5da-704a-4404-a882-8ba52c98e205 -->

Once a change has been executed through the SBE-BEAM, the Operator must publicly communicate the execution to the Sky Ecosystem. This communication may take the form of either (1) a post to the Sky Forum or (2) the inclusion of the execution in an informational dashboard that allows community members to see each change executed through the SBE-BEAM.

### A.3.5.3 - Sky Capital [Section]  <!-- UUID: f45ca50a-e1d3-4504-8e40-dd45b5fb3f83 -->

This Section defines the different types of Sky capital and rules related to that capital.

#### A.3.5.3.1 - Capital Types [Core]  <!-- UUID: d6973edf-ce53-4f77-b656-677002dfd6b4 -->

The documents herein define the different types of Sky capital.

##### A.3.5.3.1.1 - Aggregate Capital Buffer [Core]  <!-- UUID: cd36d152-1ba6-4958-9afd-d182e488e358 -->

The Aggregate Capital Buffer is the sum of (1) the Sky Surplus Buffer (see [A.3.5.1 - Surplus Buffer](9782cdc5-c274-45c2-bf4a-690f22c6a294)), (2) the Core Council Buffer (see [A.2.3.1.2.2.2.1 - Core Council Buffer](8b6781d7-f35c-4ffe-b8ed-299fa98e3da7)), (3) the Aligned Delegates Buffer (see [A.2.3.1.2.2.2.2 - Aligned Delegates Buffer](05fa5c41-26ca-4c25-94dd-834ef72c318a)), and (4) the capital held in the SubProxy of each Prime Agent. The Aggregate Capital Buffer provides a useful metric for assessing the capital level of the entire Sky Ecosystem on a consolidated basis.

##### A.3.5.3.1.2 - Aggregate Backstop Capital [Core]  <!-- UUID: 6dbead44-5ac4-4c5b-be3c-64eddd004e5c -->

Aggregate Backstop Capital is (1) the sum of the Genesis Capital held in the SubProxy of each Genesis Agent minus (2) the Allocated Genesis Capital. Aggregate Backstop Capital represents the "safety net" of excess capital backing USDS beyond standard collateral.

##### A.3.5.3.1.3 - Allocated Genesis Capital [Core]  <!-- UUID: c3b6546e-48f9-42ac-9a6c-524ed7ac91cb -->

Allocated Genesis Capital is the negative of the Surplus Buffer. Allocated Genesis Capital represents the funds Sky Core has deployed into the Genesis Agents to bootstrap innovation and Agent diversity.

#### A.3.5.3.2 - Capital Targets [Core]  <!-- UUID: 3b829981-2fe0-49dd-bfef-8a44edc9514d -->

The documents herein define capital targets for Sky and processes for achieving those targets over time.

##### A.3.5.3.2.1 - Target Aggregate Backstop Capital [Core]  <!-- UUID: f73dda95-0b1c-4bdc-b957-469253d27281 -->

The Target Aggregate Backstop Capital is one and one half percent (1.5%) of the total supply of USDS.

##### A.3.5.3.2.2 - Turbo-Fill Floor [Core]  <!-- UUID: db2aaf07-4ebb-4e5d-ae5e-575717d8fbcd -->

The current Turbo-Fill Floor for the Aggregate Backstop Capital is 150 million USDS. The Turbo-Fill Floor is the level below which an accelerated retention rate applies, as specified in [A.2.3.1.2.3 - Step 2: Aggregate Backstop Capital](2b28d464-e683-48ba-9a66-2fee05ea0a88).

##### A.3.5.3.2.3 - Capital Retention To Achieve Target Aggregate Backstop Capital [Core]  <!-- UUID: ae3b42cd-cdda-424a-b09a-87e2796538ba -->

When Aggregate Backstop Capital is below Target Aggregate Backstop Capital, a portion of Step 2 Capital is retained to grow Aggregate Backstop Capital, as specified in [A.2.3.1.2.3 - Step 2: Aggregate Backstop Capital](2b28d464-e683-48ba-9a66-2fee05ea0a88).

## A.3.6 - SKY Backstop [Article]  <!-- UUID: 4d8b0d82-97da-4041-b185-4b98c2779cbe -->

This Article governs the SKY Backstop. If the USDS Stablecoin becomes undercollateralized, the Sky Protocol will automatically generate and sell SKY to recapitalize the system. The period when the recapitalization mechanism is actively minting and selling SKY to close the shortfall is termed a "SKY Backstop Event."

### A.3.6.1 - Emission Rate [Section]  <!-- UUID: 463b58c0-79fa-4e50-85e6-20560f3da9a3 -->

An emissions rate for the SKY backstop function that prevents risk of sudden failure must be defined. This must be continuously assessed and improved to maximize stability of the system in worst case scenarios.

#### A.3.6.1.1 - Limitless [Core]  <!-- UUID: 193d8b40-bb67-4f22-b452-845e63481737 -->

The SKY Backstop is temporarily limitless.

### A.3.6.2 - Maximum Level Of Emission [Section]  <!-- UUID: 0e898ec0-e618-4deb-a7cb-f5ca47c00e71 -->

A maximum level of SKY emission per undercollateralization event must be defined. This must be continuously assessed and improved to maximize stability of the system in worst-case scenarios.

### A.3.6.3 - Override Mechanism [Section]  <!-- UUID: ed24e054-5c3f-4fc5-9992-d19462a47052 -->

The Protocol must include an override mechanism that allows Sky Governance to continue emitting SKY beyond the maximum level. This Section must specify research processes and principles to guide when and how the override mechanism can be safely used.

### A.3.6.4 - Halt Mechanism [Section]  <!-- UUID: 28f36566-e26e-4b51-bf68-f6ddd584c172 -->

The Protocol must contain a SKY backstop halt mechanism that immediately halts the backstop event in case of severe risk of total failure.

### A.3.6.5 - Mitigate Worst Case Scenario [Section]  <!-- UUID: 1008d9c7-98be-4fde-9473-5a5441160a20 -->

In case the backstop limit is reached and not overridden, or in case the backstop is halted during the event, the USDS target price receives a haircut to settle the remaining bad debt of the system. This Section must define elements and infrastructure to address this worst-case scenario, including research concerning ways to mitigate damage.

### A.3.6.6 - Relation To Genesis Capital Backstop [Section]  <!-- UUID: 5e795fa2-77d7-4f2a-8494-545d4bb2d955 -->

The SKY Backstop may not be invoked unless the Genesis Capital Backstop (see [A.3.7.1.6 - Genesis Capital Backstop](a9965d58-8cda-49fc-8a7f-f8cc2e0d6b98)) has been applied and USDS remains undercollateralized.

## A.3.7 - Measures For Endgame Transition [Article]  <!-- UUID: 94ed62af-6e69-4831-938a-69963e6c0a1f -->

This Article defines temporary measures for implementing the Stability Scope during the transition to the Endgame State.

### A.3.7.1 - Measures For Endgame Transition [Section]  <!-- UUID: 92b5164c-2a55-4947-bb8a-9b05ca5ed8c8 -->

This Section defines temporary measures to give effect to the Stability Scope during the Endgame transition.

#### A.3.7.1.1 - Native Vault Engine [Core]  <!-- UUID: 950c138e-c5f6-4ff9-92c0-35a3e1ef0ad3 -->

The Sky Core Vaults are gradually being deprecated over time to incentivize users to migrate to SparkLend and other borrowing platforms offered by Prime Agents (see [A.3.7.1.1.2.3 - Stability Fee](0257a420-e92e-4942-b794-a559f299365f)). During the transition period, the Core Vaults will have a limited set of collateral types and risk parameters that Core GovOps, in consultation with the Core Council Risk Advisor, must implement according to the following subdocuments.

##### A.3.7.1.1.1 - Vault Types [Core]  <!-- UUID: 64971463-0650-4462-b9c4-1eecb704fa1a -->

The collateral types of the Native Vault Engine and their parameters are defined in the subdocuments herein.

###### A.3.7.1.1.1.1 - ETH-A [Core]  <!-- UUID: f97321f8-c677-4a6c-aa87-8f9a93f8acd3 -->

Current ETH-A parameters are:

- Stability Fee: set by the SP-BEAM specified in A.3.9 - Measures For Endgame Transition - Stability Parameter Bounded External Access Module,
- Liquidation Ratio: 145%,
- DC-IAM `line`: 15,000,000,000 Dai,
- DC-IAM `gap`: 150,000,000 Dai,
- DC-IAM `ttl`: 21,600 seconds,
- `cut`: 99.00%,
- `step`: 90 seconds,
- `buf`: 110.00%,
- `cusp`: 45.00%,
- `tail`: 7,200 seconds,
- `chip`: 0.10%,
- `tip`: 250,
- `chop`: 13%,
- `hole`: 40,000,000 Dai,
- `dust`: 7,500 Dai

###### A.3.7.1.1.1.2 - ETH-B [Core]  <!-- UUID: 87fd7fd2-495f-452f-abed-4a887ba02c7c -->

Current ETH-B parameters are:

- Stability Fee: set by the SP-BEAM specified in A.3.9 - Measures For Endgame Transition - Stability Parameter Bounded External Access Module,
- Liquidation Ratio: 130%,
- DC-IAM `line`: 250,000,000 Dai,
- DC-IAM `gap`: 20,000,000 Dai,
- DC-IAM `ttl`: 21,600 seconds,
- `cut`: 99.00%,
- `step`: 60 seconds,
- `buf`: 110.00%,
- `cusp`: 45.00%,
- `tail`: 4,800 seconds,
- `chip`: 0.10%,
- `tip`: 250,
- `chop`: 13%,
- `hole`: 15,000,000 Dai,
- `dust`: 25,000 Dai

###### A.3.7.1.1.1.3 - ETH-C [Core]  <!-- UUID: 896ce563-a4f1-4a9d-ad23-fc5840ea2f28 -->

Current ETH-C parameters are:

- Stability Fee: set by the SP-BEAM specified in A.3.9 - Measures For Endgame Transition - Stability Parameter Bounded External Access Module,
- Liquidation Ratio: 170%,
- DC-IAM `line`: 2,000,000,000 Dai,
- DC-IAM `gap`: 100,000,000 Dai,
- DC-IAM `ttl`: 28,800 seconds,
- `cut`: 99.00%,
- `step`: 90 seconds,
- `buf`: 110.00%,
- `cusp`: 45.00%,
- `tail`: 7,200 seconds,
- `chip`: 0.10%,
- `tip`: 250,
- `chop`: 13%,
- `hole`: 35,000,000 Dai,
- `dust`: 3,500 Dai

###### A.3.7.1.1.1.4 - WSTETH-A [Core]  <!-- UUID: 1dbc84b7-a17e-40af-aef5-63a9b78e85b3 -->

Current WSTETH-A parameters are:

- Stability Fee: set by the SP-BEAM specified in A.3.9 - Measures For Endgame Transition - Stability Parameter Bounded External Access Module,
- Liquidation Ratio: 150%,
- DC-IAM `line`: 750,000,000 Dai,
- DC-IAM `gap`: 30,000,000 Dai,
- DC-IAM `ttl`: 43,200 seconds,
- `cut`: 99.00%,
- `step`: 90 seconds,
- `buf`: 110.00%,
- `cusp`: 45.00%,
- `tail`: 7,200 seconds,
- `chip`: 0.10%,
- `tip`: 250,
- `chop`: 13%,
- `hole`: 30,000,000 Dai,
- `dust`: 7,500 Dai

###### A.3.7.1.1.1.5 - WSTETH-B [Core]  <!-- UUID: cfb76935-bcd4-4973-967c-7625c1524e58 -->

Current WSTETH-B parameters are:

- Stability Fee: set by the SP-BEAM specified in A.3.9 - Measures For Endgame Transition - Stability Parameter Bounded External Access Module,
- Liquidation Ratio: 175%,
- DC-IAM `line`: 1,000,000,000 Dai,
- DC-IAM `gap`: 45,000,000 Dai,
- DC-IAM `ttl`: 43,200 seconds,
- `cut`: 99.00%,
- `step`: 90 seconds,
- `buf`: 110.00%,
- `cusp`: 45.00%,
- `tail`: 7,200 seconds,
- `chip`: 0.10%,
- `tip`: 250,
- `chop`: 13%,
- `hole`: 20,000,000 Dai,
- `dust`: 3,500 Dai

###### A.3.7.1.1.1.6 - WBTC-A [Core]  <!-- UUID: dba74f38-58f3-432a-b14b-bf5bc95ac5ed -->

Current WBTC-A parameters are:

- Stability Fee: set by the SP-BEAM specified in A.3.9 - Measures For Endgame Transition - Stability Parameter Bounded External Access Module,
- Liquidation Ratio: 150%,
- DC-IAM `line`: 0 Dai,
- DC-IAM `gap`: 4,000,000 Dai,
- DC-IAM `ttl`: 86,400 seconds,
- `cut`: 99.00%,
- `step`: 90 seconds,
- `buf`: 110.00%,
- `cusp`: 45.00%,
- `tail`: 7,200 seconds,
- `chip`: 0.10%,
- `tip`: 250,
- `chop`: 0%,
- `hole`: 10,000,000 Dai,
- `dust`: 7,500 Dai

###### A.3.7.1.1.1.7 - WBTC-B [Core]  <!-- UUID: 307ba340-c3d3-42c8-8121-e98c5de607d0 -->

Current WBTC-B parameters are:

- Stability Fee: set by the SP-BEAM specified in A.3.9 - Measures For Endgame Transition - Stability Parameter Bounded External Access Module,
- Liquidation Ratio: 150%,
- DC-IAM `line`: 0 Dai,
- DC-IAM `gap`: 2,000,000 Dai,
- DC-IAM `ttl`: 86,400 seconds,
- `cut`: 99.00%,
- `step`: 60 seconds,
- `buf`: 110.00%,
- `cusp`: 45.00%,
- `tail`: 4,800 seconds,
- `chip`: 0.10%,
- `tip`: 250,
- `chop`: 0%,
- `hole`: 5,000,000 Dai,
- `dust`: 25,000 Dai

###### A.3.7.1.1.1.8 - WBTC-C [Core]  <!-- UUID: 2f42fd1f-a79b-4208-ac07-bbfa9a447c18 -->

Current WBTC-C parameters are:

- Stability Fee: set by the SP-BEAM specified in A.3.9 - Measures For Endgame Transition - Stability Parameter Bounded External Access Module,
- Liquidation Ratio: 175%,
- DC-IAM `line`: 0 Dai,
- DC-IAM `gap`: 8,000,000 Dai,
- DC-IAM `ttl`: 86,400 seconds,
- `cut`: 99.00%,
- `step`: 90 seconds,
- `buf`: 110.00%,
- `cusp`: 45.00%,
- `tail`: 7,200 seconds,
- `chip`: 0.10%,
- `tip`: 250,
- `chop`: 0%,
- `hole`: 10,000,000 Dai,
- `dust`: 3,500 Dai

##### A.3.7.1.1.2 - Risk Parameter Definitions [Core]  <!-- UUID: 8eb26d06-d2b3-493f-a79f-e3509326ddc6 -->

The Native Vault Engine risk parameters are defined in the subdocuments herein.

###### A.3.7.1.1.2.1 - Liquidation Ratio [Core]  <!-- UUID: 9ce4d08e-aa5b-4cab-884e-7a53e937bdb8 -->

The Liquidation Ratio parameter limits the maximum amount of Dai debt that a vault user can draw from their vault given the value of their collateral locked in that vault. In practice, it expresses the minimum collateral in percentage terms that can support a given Dai debt. If the ratio of a Vault user's collateral to their debt drops below this value, their vault can be liquidated. Each vault type has its own Liquidation Ratio. The Liquidation Ratio for each vault type is expressed as a percentage value of the collateral that must be present in the vault to support its debt.

Changes to the Liquidation Ratio are subject to the Operational Weekly Cycle, requiring a Governance Poll followed by an Executive Vote.

###### A.3.7.1.1.2.2 - Debt Ceiling Limit [Core]  <!-- UUID: b490d4d0-8eb8-4dc6-9ef3-c85d357f1f4b -->

The Debt Ceiling Limit is numerically provided and acts as an upper limit. Core GovOps, in consultation with the Core Council Risk Advisor, can propose changes within this limit.

Debt Ceiling Limit = Unlimited is defined as large enough to avoid being reached in the near future.

The DC-IAM methodology contained in [A.3.7.1.1.2.4 - Debt Ceiling Instant Access Module (DC-IAM)](93c9f662-4e0d-477e-8fc9-e3726877e842) acts as a risk mitigation tool. It limits the rate at which exposure can increase in a short period of time in the event of an unexpected emergency.

###### A.3.7.1.1.2.3 - Stability Fee [Core]  <!-- UUID: 0257a420-e92e-4942-b794-a559f299365f -->

The Stability Fee parameter is an annual percentage fee charged on the Dai generated on Vaults. It is expressed as an annual percentage yield but it is charged on a per-block basis in Dai. The Dai from this fee is minted, added to the Dai debt for the vault, and then transferred into the Surplus Buffer which is under the control of Sky Governance. Each vault type has its own Stability Fee that can be adjusted independently.

The Stability Fees can be modified through either Executive Votes or the Stability Parameter Bounded External Access Module. See [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).

The Stability Fees must be gradually increased over time to incentivize users to migrate to SparkLend and other borrowing platforms offered by Prime Agents.

###### A.3.7.1.1.2.4 - Debt Ceiling Instant Access Module (DC-IAM) [Core]  <!-- UUID: 93c9f662-4e0d-477e-8fc9-e3726877e842 -->

The DC-IAM allows any user to adjust the Debt Ceiling of a supported vault type according to the rules defined in the DC-IAM smart contract logic and parameters set by the Core Facilitator. The DC-IAM holds three parameters that can be set by Sky Governance for each vault type, (i) Maximum Debt Ceiling (`line`), (ii) Target Available Debt (`gap`), and (iii) Ceiling Increase Cooldown (`ttl`).

###### A.3.7.1.1.2.4.1 - Maximum Debt Ceiling (line) [Core]  <!-- UUID: 6ba18f25-dae8-4fa5-929e-3c7071b70107 -->

The `line` parameter refers to the maximum value for the Debt Ceiling that the DC-IAM will allow in the given vault type. When using the DC-IAM to manage the Debt Ceiling of a vault type, the `line` parameter essentially replaces the Debt Ceiling parameter for that vault type. Rather than Sky Governance setting the Debt Ceiling directly, they will need to set the Maximum Debt Ceiling `line` in the DC-IAM. The `line` parameter is defined in Dai.

The Maximum Debt Ceiling is defined in [A.3.7.1.1.2.2 - Debt Ceiling Limit](b490d4d0-8eb8-4dc6-9ef3-c85d357f1f4b) and is currently unlimited.

###### A.3.7.1.1.2.4.2 - Target Available Debt (gap) [Core]  <!-- UUID: 07353080-4346-4ffd-bfc8-913cac78776a -->

The `gap` parameter controls how much of a gap the DC-IAM aims to maintain between the current debt usage and the Debt Ceiling of the vault type. The higher this value, the more risk there is from large collateral drops in very short amounts of time. The smaller this value, the more vault use is negatively affected. The `gap` parameter is defined in Dai.

###### A.3.7.1.1.2.4.3 - Ceiling Increase Cooldown (ttl) [Core]  <!-- UUID: a5ae79ad-9460-41a3-8dbf-65605f54b79b -->

The Ceiling Increase Cooldown (`ttl`) parameter controls how frequently the Debt Ceiling can be increased by the DC-IAM. If a user attempts to use the DC-IAM to increase the Debt Ceiling of a vault type before this time expires, the transaction will fail to execute and the Debt Ceiling will remain unchanged. The `ttl` parameter in combination with the `gap` parameter enforces a maximum rate at which debt usage can increase over time using a given vault type. These parameters should be set such that the maximum increase over time can accommodate all reasonable usage of the vault type in question. The `ttl` parameter is defined in seconds.

###### A.3.7.1.1.2.5 - Auction Parameters [Core]  <!-- UUID: 5774fd7c-ecd9-46ea-b33d-77ea9c6de4f3 -->

A clear justification and analysis must be provided to validate any proposed changes to the parameters specified in this document. Before these changes are added to an Executive Vote, Core GovOps, in consultation with the Core Council Risk Advisor, must obtain approval through a Governance Poll. However, in an emergency, Core GovOps, in consultation with the Core Council Risk Advisor, has the authority to bypass the Governance Poll and add the proposed parameters directly to an Executive Vote. The parameters contained herein must be regularly monitored and updated if needed.

###### A.3.7.1.1.2.5.1 - Auction Price Function (calc) [Core]  <!-- UUID: fc7341c8-5a58-4be4-be8c-201f858e3861 -->

The Auction Price Function is the mathematical function that determines how the collateral price changes over time during a collateral auction. Collateral auctions use a falling price auction, where the price starts high and decreases according to the function defined in this parameter.

The Exponential Stair Step function contains two key parameters, `cut` and `step`, defined in [A.3.7.1.1.2.5.1.1 - Auction Price Function (cut)](1ff3ceac-abd0-4195-9a60-a4aaf48c3d31) and [A.3.7.1.1.2.5.1.2 - Auction Price Function (step)](4b46633c-4d6c-4a9c-9be0-93d242ce9db9), respectively.

###### A.3.7.1.1.2.5.1.1 - Auction Price Function (cut) [Core]  <!-- UUID: 1ff3ceac-abd0-4195-9a60-a4aaf48c3d31 -->

The `cut` parameter controls the ‘depth’ of each step in the function. A smaller `cut` means a smoother line; a large one means more pronounced steps. The `cut` parameter is defined as a multiplicative factor. For example, 0.99 equated to a 1% price drop.

###### A.3.7.1.1.2.5.1.2 - Auction Price Function (step) [Core]  <!-- UUID: 4b46633c-4d6c-4a9c-9be0-93d242ce9db9 -->

The `step` parameter controls the length of time between price drops. A smaller step means a smoother line; a large one means more pronounced steps. The `step` parameter is defined in seconds.

###### A.3.7.1.1.2.5.2 - Auction Price Multiplier (buf) [Core]  <!-- UUID: 2bcdc1c9-6e43-4059-8a46-0a68c17f487d -->

The `buf` parameter is a multiplier that is applied to the starting price of a collateral auction. Each vault type has its own Auction Price Multiplier that can be adjusted by Sky Governance separately. This multiplier is intended to be greater than 1.0x because Liquidations 2.0 uses falling price auctions. This means that it is generally preferable for the auction price to begin above the market price and then fall to the correct value over some amount of time. The `buf` parameter is defined as a multiplicative factor.

###### A.3.7.1.1.2.5.3 - Max Auction Drawdown (cusp) [Core]  <!-- UUID: fc472dd5-3c2a-4335-ad2f-4988dbeb1c89 -->

The Max Auction Drawdown is the maximum percentage drop in collateral price during a collateral auction before the auction is reset. 'Collateral price' in this context refers to the collateral auction price rather than the collateral market price.

The Max Auction Drawdown parameter overlaps with the Max Auction Duration parameter in that an auction will need to be reset once either maximum is exceeded.

###### A.3.7.1.1.2.5.4 - Max Auction Duration (tail) [Core]  <!-- UUID: cd5a3cb9-e658-4bc5-8f82-b4dab52f32d9 -->

The Max Auction Duration parameter sets the maximum time that can elapse before an auction needs to reset for a particular vault type. Expressed in seconds, this parameter determines when an auction can no longer settle and must be reset.

The Max Auction Duration parameter overlaps with the Max Auction Drawdown parameter in that an auction will need to be reset once either maximum is exceeded.

###### A.3.7.1.1.2.5.5 - Proportional Kick Incentive (chip) [Core]  <!-- UUID: e92d5797-9d72-455b-95a3-7fca9bb68071 -->

The Proportional Kick Incentive parameter represents a reward in Dai paid to the keepers that trigger collateral liquidation auctions in the Sky Protocol. The Proportional Kick Incentive is set as a percentage and represents a portion of Dai based on the debt of the vault that is being liquidated. The Dai is rewarded for each liquidation auction at the point the auction is triggered. Each vault type has its own Proportional Kick Incentive that may be adjusted separately by Sky Governance.

###### A.3.7.1.1.2.5.6 - Flat Kick Incentive (tip) [Core]  <!-- UUID: e883adc9-b624-438b-8a4b-981ffe741478 -->

The Flat Kick Incentive parameter represents a reward in Dai paid to the keepers that trigger collateral liquidation auctions in the Sky Protocol. The Flat Kick Incentive is a fixed amount of Dai that is rewarded for each liquidation auction at the point the auction is triggered. Each vault type has its own Flat Kick Incentive that may be adjusted separately by Sky Governance.

###### A.3.7.1.1.2.5.7 - Liquidation Penalty (chop) [Core]  <!-- UUID: 7f2f2eba-1933-4974-8436-54372d3188b1 -->

The Liquidation Penalty parameter controls the fee vault owners must pay when their position is liquidated due to insufficient collateral. For a vault holder to receive any collateral back from the liquidations process, the debt and Liquidation Penalty must be covered by the collateral auction. Each vault type has its own Liquidation Penalty that can be adjusted by Sky Governance.

###### A.3.7.1.1.2.5.8 - Local Liquidation Limit (hole) [Core]  <!-- UUID: 5d10220e-0541-4537-82d2-d853fa65ec97 -->

The Local Liquidation Limit sets the maximum amount of Dai debt for which collateral auctions can be active at any one time within a particular vault type. When the total Dai value of auctions exceeds this maximum for a particular vault type, no more collateral can be auctioned using that vault type until others are completed. Each vault type has a separate Local Liquidation Limit.

###### A.3.7.1.1.2.6 - Debt Floor (dust) [Core]  <!-- UUID: d6e0c32d-aea2-4bc7-9ec3-97d54bdbd9a7 -->

The Debt Floor parameter controls the minimum amount of Dai that can be minted using a specific vault type for an individual vault. If a user tries to mint Dai and the amount of Dai minted would not put the vault's amount of Dai minted above its Debt Floor, the transaction will fail and no DAi will be minted. Likewise, if a user attempts to pay back debt such that their debt will equal less than the Debt Floor and greater than zero, the transaction will fail and no Dai will be paid back. Each vault type has its own Debt Floor that can be adjusted by Sky Governance.

##### A.3.7.1.1.3 - Collateral Offboarding [Core]  <!-- UUID: 05f29c65-4d92-43b3-aacb-3dd75b9f6794 -->

The processes for offboarding Native Vault Engine collateral are defined in the subdocuments herein.

###### A.3.7.1.1.3.1 - Offboarding Low Usage Collateral [Core]  <!-- UUID: 2c7a4db9-497e-4ed5-b91b-9543af3d58b3 -->

To protect the Protocol from unnecessary complexity, the Core Facilitator must offboard collateral types specified in [A.3.7.1.1.1 - Vault Types](64971463-0650-4462-b9c4-1eecb704fa1a) if they fall below a total debt of 20 million.

###### A.3.7.1.1.3.2 - Offboarding WBTC Collateral [Core]  <!-- UUID: f6762223-29f3-46c1-8fa4-a5c27636772d -->

WBTC-A, WBTC-B and WBTC-C are defined in [A.3.7.1.1.1 - Vault Types](64971463-0650-4462-b9c4-1eecb704fa1a) only for the purpose of Stability Fee consistency. These are otherwise not considered Native Vault Engine collateral and should be offboarded according to [A.3.7.1.1.3.3 - Offboarding Other Collateral](fe6595fc-173a-4d75-83ca-9f29dbbb63a3).

###### A.3.7.1.1.3.3 - Offboarding Other Collateral [Core]  <!-- UUID: fe6595fc-173a-4d75-83ca-9f29dbbb63a3 -->

All other collateral types should be offboarded when the Core Facilitator deems it appropriate and when new mechanisms are in place to take over the roles previously covered by the offboarded collateral.

###### A.3.7.1.1.3.4 - Collateral Offboarding Process [Core]  <!-- UUID: 9f87ff7a-d3a8-4999-ae20-b4c0773c732c -->

The Core Facilitator, in consultation with the Core Council Risk Advisor, must use the Operational Weekly Cycle to offboard Native Vault Engine collateral pursuant to [A.3.7.1.1.3 - Collateral Offboarding](05f29c65-4d92-43b3-aacb-3dd75b9f6794) and its subdocuments.

##### A.3.7.1.1.4 - Oracles [Core]  <!-- UUID: a38e05bf-0820-4916-a71c-cff4f54e45df -->

The Native Vault Engine collateral types of ETH, STETH, WBTC will specifically use the Chronicle v3 oracle solution, until at least January 1st 2026. The Native Vault Engine collateral types must be migrated to the new version of the Chronicle v3 oracle when it is feasible to do so.

Other oracle solutions, including diversified oracles, will only be considered until January 1st, 2026, and only if there are unresolvable security concerns with the Chronicle v3 oracles.

##### A.3.7.1.1.5 - Updates [Core]  <!-- UUID: 2107f160-751d-4fea-abc0-f0bef76a30d5 -->

If not otherwise specified, Core GovOps, in consultation with the Core Council Risk Advisor, has the ability to modify any of the parameters defined in [A.3.7.1.1.2 - Risk Parameter Definitions](8eb26d06-d2b3-493f-a79f-e3509326ddc6) for any of the Vault Types in [A.3.7.1.1.1 - Vault Types](64971463-0650-4462-b9c4-1eecb704fa1a). As a general rule, the modification of said parameters is pursuant to the Operational Weekly Cycle and can be effected directly via an Executive Vote, without requiring a Governance Poll. Exceptions to this general rule must be clearly stated in the relevant Atlas document.

#### A.3.7.1.2 - Prime Allocator Vaults [Core]  <!-- UUID: 1c09308d-b7cd-495c-b547-baf628a6e323 -->

The subdocuments herein govern the Allocator Vaults utilized by Prime Agents to access Sky Ecosystem liquidity. These documents define the specific risk parameters for each vault and the governance process for updating them.

##### A.3.7.1.2.1 - Prime Allocator Vault Risk Parameters [Core]  <!-- UUID: 305a31ea-ae42-478f-8a92-94d7e9d88067 -->

The subdocuments herein define the risk parameters for each active Allocator Vault.

###### A.3.7.1.2.1.1 - ALLOCATOR-SPARK-A Parameters [Core]  <!-- UUID: 47d69b3d-a650-4dcd-a8f7-0c4f6bf5e8d2 -->

The parameters for the Spark Allocator Vault are:

- `duty`: set by the SP-BEAM specified in [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).
- `line`: controlled by DC-IAM
- DC-IAM parameters:
    - `gap`: 1.5 billion USDS
    - `line`: 10 billion USDS
    - `ttl`: 12 hours

###### A.3.7.1.2.1.2 - ALLOCATOR-BLOOM-A Parameters [Core]  <!-- UUID: 53cba245-68c6-4af9-a280-b200dabebec7 -->

The parameters for the Grove Allocator Vault are:

- `duty`: set by the SP-BEAM specified in [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).
- `line`: controlled by DC-IAM
- DC-IAM parameters:
    - `gap`: 500 million USDS
    - `line`: 5 billion USDS
    - `ttl`: 24 hours

###### A.3.7.1.2.1.3 - ALLOCATOR-GROVE-A Parameters [Core]  <!-- UUID: 5ecdf33d-c8df-439c-98ac-892e62284797 -->

The parameters for the ALLOCATOR-GROVE-A Allocator Vault are:

- `duty`: set by the SP-BEAM specified in [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).
- `line`: controlled by DC-IAM
- DC-IAM parameters:
    - `gap`: 2 million USDS
    - `line`: 10 million USDS
    - `ttl`: 24 hours

###### A.3.7.1.2.1.4 - ALLOCATOR-NOVA-A Parameters [Core]  <!-- UUID: 08321783-f31a-4a80-8f0c-898afb4d8f9b -->

The parameters for the Keel Allocator Vault are:

- `duty`: set by the SP-BEAM specified in [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).
- `line`: 0 USDS

###### A.3.7.1.2.1.5 - ALLOCATOR-OBEX-A Parameters [Core]  <!-- UUID: 1ee3efd3-fe75-4766-bc6a-ec204f6a3bca -->

The parameters for the Obex Allocator Vault are:

- `duty`: set by the SP-BEAM specified in [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).
- `line`: controlled by DC-IAM
- DC-IAM parameters:
    - `gap`: 50 million USDS
    - `line`: 2.5 billion USDS
    - `ttl`: 24 hours

###### A.3.7.1.2.1.6 - ALLOCATOR-PATTERN-A Parameters [Core]  <!-- UUID: 322e7ccc-6dcb-4f83-96e5-d8f2fa87cd00 -->

The parameters for the Pattern Allocator Vault are:

- `duty`: set by the SP-BEAM specified in [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).
- `line`: controlled by DC-IAM
- DC-IAM parameters:
    - `gap`: 50 million USDS
    - `line`: 2.5 billion USDS
    - `ttl`: 24 hours

###### A.3.7.1.2.1.7 - ALLOCATOR-PRYSM-A Parameters [Core]  <!-- UUID: 17630a67-b287-4f44-bc60-f2a4f5d16cfa -->

The parameters for the Osero Allocator Vault are:

- `duty`: set by the SP-BEAM specified in [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).
- `line`: controlled by DC-IAM
- DC-IAM parameters:
    - `gap`: 2 million USDS
    - `line`: 10 million USDS
    - `ttl`: 24 hours

###### A.3.7.1.2.1.8 - ALLOCATOR-INTERVAL-A Parameters [Core]  <!-- UUID: cdbdd083-cb1c-4958-9cf0-18a088535c9d -->

The parameters for the Launch Agent 7 Allocator Vault are:

- `duty`: set by the SP-BEAM specified in [A.3.7.1.3 - Stability Parameter Bounded External Access Module](47b8b035-8abd-42e6-86b8-33f852fa953a).
- `line`: controlled by DC-IAM
- DC-IAM parameters:
    - `gap`: 10 million USDS
    - `line`: 10 million USDS
    - `ttl`: 24 hours

##### A.3.7.1.2.2 - Update Process [Core]  <!-- UUID: 41a1ae38-4f5c-468f-b6ba-47e16ecc5aec -->

Core GovOps, in consultation with the Core Council Risk Advisor, has the ability to modify any of the Prime Allocator Vault Risk Parameters listed under [A.3.7.1.2.1 - Prime Allocator Vault Risk Parameters](305a31ea-ae42-478f-8a92-94d7e9d88067). The modification of said parameters is pursuant to the Operational Weekly Cycle and can be effected directly via an Executive Vote, without requiring a prior Governance Poll.

#### A.3.7.1.3 - Stability Parameter Bounded External Access Module [Core]  <!-- UUID: 47b8b035-8abd-42e6-86b8-33f852fa953a -->

The Stability Parameter Bounded External Access Module (SP-BEAM) enables designated, Governance-whitelisted operators to adjust the Stability Fees of supported vault types, the Dai Savings Rate (DSR), and the Sky Savings Rate (SSR). Adjustments are governed by the SP-BEAM smart contract logic and specific parameters set by Sky Governance. SP-BEAM holds four parameters that can be set for each vault type or savings rate: (i) `min`, (ii) `max`, (iii) `step`, and (iv) `tau`.

##### A.3.7.1.3.1 - Definitions [Core]  <!-- UUID: b113ca06-9a25-4abf-81f1-53f419ffe2d2 -->

The documents herein define the parameters of the Stability Parameter Bounded External Access Module.

###### A.3.7.1.3.1.1 - Min Definition [Core]  <!-- UUID: 1896350c-5f87-4be5-b32f-f1114dc2c271 -->

The `min` parameter defines the minimum value for rates in basis points that can be set using the Stability Parameter Bounded External Access Module. Each rate parameter added to the SP-BEAM has a specific `min`.

###### A.3.7.1.3.1.2 - Max Definition [Core]  <!-- UUID: 67747090-8545-49b4-95e8-673af9836aa5 -->

The `max` parameter defines the maximum value for rates in basis points that can be set using the Stability Parameter Bounded External Access Module. Each rate parameter added to the SP-BEAM has a specific `max`.

###### A.3.7.1.3.1.2.1 - Max Technical Upper Limit [Core]  <!-- UUID: 4e2910c0-fd52-4e18-97e0-2fbd35569070 -->

Although the `max` parameter can be set higher, the SP-BEAM cannot be used to set a rate higher than 50% (5,000 basis points) due to technical limitations. Attempts to use the SP-BEAM in this manner will revert. To avoid confusion, `max` should not be set to a value higher than 50% (5,000 basis points).

###### A.3.7.1.3.1.3 - Step Definition [Core]  <!-- UUID: bcfac0d1-3d17-46e1-bf88-5a7937816d53 -->

The `step` parameter limits how much the rates can be increased or decreased in a single transaction in basis points, bound by the `tau` parameter. Each rate parameter added to the SP-BEAM has a specific `step`.

###### A.3.7.1.3.1.4 - Tau Definition [Core]  <!-- UUID: 8747effa-1080-4066-89da-4c25121a02ba -->

The `tau` parameter defines the minimum time interval, in seconds, that must elapse between consecutive uses or operations of the Stability Parameter Bounded External Access Module.

An SP-BEAM operation may adjust one or more parameters. Once an SP-BEAM operation is executed, the `tau` duration must expire before any subsequent SP-BEAM operation can be performed.

###### A.3.7.1.3.1.4.1 - Tau Current Value [Core]  <!-- UUID: dd9472e5-9796-4aff-a2b1-7a847e008c9b -->

The `tau` is currently set to 57,600 seconds (16 hours).

##### A.3.7.1.3.2 - Native Vault Parameters [Core]  <!-- UUID: 968d4388-a655-42ee-bab0-08e6583d1980 -->

The Stability Parameter Bounded External Access Module parameters for the Native Vaults are defined in the subdocuments herein. When new vaults are added to the protocol, they must also be added to the SP-BEAM. Unless specified otherwise within the relevant subdocument herein, the SP-BEAM parameters for any newly added Native Vault type shall default to match the parameters defined herein for the ETH-A vault type.

###### A.3.7.1.3.2.1 - ETH-A Parameters [Core]  <!-- UUID: c9cd99f2-9c40-4b06-94a1-630a26116bce -->

The Stability Parameter Bounded External Access Module parameters for the ETH-A Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.2.2 - ETH-B Parameters [Core]  <!-- UUID: 6f28d962-1e40-4753-ab39-865795b349f4 -->

The Stability Parameter Bounded External Access Module parameters for the ETH-B Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.2.3 - ETH-C Parameters [Core]  <!-- UUID: 748db209-f31e-444b-b134-55a8826a5d7a -->

The Stability Parameter Bounded External Access Module parameters for the ETH-C Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.2.4 - WSTETH-A Parameters [Core]  <!-- UUID: e134990f-7d06-46e3-a2c3-2277bb65e45c -->

The Stability Parameter Bounded External Access Module parameters for the WSTETH-A Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.2.5 - WSTETH-B Parameters [Core]  <!-- UUID: f27c3fa3-dcd6-4ba8-9d74-426807ac010c -->

The Stability Parameter Bounded External Access Module parameters for the WSTETH-B Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.2.6 - WBTC-A Parameters [Core]  <!-- UUID: e0ead8d6-7d1d-48f0-addb-702e21ef5a9e -->

The Stability Parameter Bounded External Access Module parameters for the WBTC-A Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.2.7 - WBTC-B Parameters [Core]  <!-- UUID: dba279e1-bb04-4574-a45b-87788be40a78 -->

The Stability Parameter Bounded External Access Module parameters for the WBTC-B Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.2.8 - WBTC-C Parameters [Core]  <!-- UUID: 74ccae87-580f-492b-b260-fa3ef6613979 -->

The Stability Parameter Bounded External Access Module parameters for the WBTC-C Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 200 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

##### A.3.7.1.3.3 - Allocator Vault Parameters [Core]  <!-- UUID: 6ab6bd12-93d3-419f-96e2-a7f79bfe1afa -->

The Stability Parameter Bounded External Access Module parameters for the Allocator Vaults are defined in the subdocuments herein. When new Allocator Vaults are added, they must also be added to the SP-BEAM. Unless specified otherwise within the relevant subdocument herein, the SP-BEAM parameters for any newly added Allocator Vault type shall default to match the parameters defined herein for the ALLOCATOR-SPARK-A vault type.

###### A.3.7.1.3.3.1 - ALLOCATOR-SPARK-A Parameters [Core]  <!-- UUID: 3f6791ef-1f90-45b2-96db-0c85aa2035a1 -->

The Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-SPARK-A Allocator Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.3.2 - ALLOCATOR-NOVA-A Parameters [Core]  <!-- UUID: 092b62b9-b9b8-4322-8b39-5c32ad420be3 -->

The Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-NOVA-A Allocator Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.3.3 - ALLOCATOR-BLOOM-A Parameters [Core]  <!-- UUID: 1cca9f9f-1a60-4de6-8ec2-694b87d3ee91 -->

The Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-BLOOM-A Allocator Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.3.4 - ALLOCATOR-GROVE-A Parameters [Core]  <!-- UUID: e71dbe73-9968-4f43-9656-4ebb86db6187 -->

The Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-GROVE-A Allocator Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.3.5 - ALLOCATOR-OBEX-A Parameters [Core]  <!-- UUID: d52799ce-589d-4ef8-9ee3-ef940866291a -->

The Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-OBEX-A Allocator Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.3.6 - ALLOCATOR-PATTERN-A Parameters [Core]  <!-- UUID: 505130f5-cf13-47e0-bcb6-e4810a36a46c -->

The Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-PATTERN-A Allocator Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.3.7 - ALLOCATOR-PRYSM-A Parameters [Core]  <!-- UUID: f09e5c6d-80cd-4d7d-b833-f64a96d23c15 -->

The Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-PRYSM-A Allocator Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

###### A.3.7.1.3.3.8 - ALLOCATOR-INTERVAL-A Parameters [Core]  <!-- UUID: 8766f5be-1a3b-4c74-ac5e-0e22aba94f9a -->

The Stability Parameter Bounded External Access Module parameters for the ALLOCATOR-INTERVAL-A Allocator Vault are as follows:

- `max` - 3,000 basis points,
- `min` - 0 basis points,
- `step` - 400 basis points,
- `tau` - Globally defined in [A.3.7.1.3.1.4.1 - Tau Current Value](dd9472e5-9796-4aff-a2b1-7a847e008c9b).

##### A.3.7.1.3.4 - Parameter Adjustments [Core]  <!-- UUID: 2d4aa875-b7ea-49c3-9506-479f0b5d157c -->

All Stability Parameter Bounded External Access Module parameters can be modified by the Core Executor Agents, in consultation with the Core Council Risk Advisor. This process will be conducted through the Operational Weekly Cycle or, if necessary, through out-of-schedule Executive Votes.

##### A.3.7.1.3.5 - Operators [Core]  <!-- UUID: 91f8b696-2c6b-4234-9126-2576a385882d -->

The Stability Parameter Bounded External Access Module (SP-BEAM) Operator is a whitelisted entity that can directly alter the current parameters of vault types or savings rates that have been added to the SP-BEAM. Changes to rates are limited by the `max`, `min`, `step`, and `tau` parameters. Operators can be added or removed by an Executive Vote.

###### A.3.7.1.3.5.1 - Operator Multisig [Core]  <!-- UUID: f0cc7297-8ab9-4255-9365-d9ba87764f13 -->

The Operator Multisig is the Operator of the Stability Parameter Bounded External Access Module and is controlled by Core GovOps.

###### A.3.7.1.3.5.1.1 - Operator Multisig Address [Core]  <!-- UUID: 793d4595-9f1f-4387-a3a6-b9c7b20266c3 -->

The address of the Operator Multisig on the Ethereum Mainnet is `0xe1c6f81D0c3CD570A77813b81AA064c5fff80309`.

###### A.3.7.1.3.5.1.2 - Operator Multisig Required Number Of Signers [Core]  <!-- UUID: 591ac4d7-5699-4a81-8b4a-d10c8d8c3457 -->

The Operator Multisig currently has a 2/3 signing requirement.

###### A.3.7.1.3.5.1.3 - Operator Multisig Signers [Core]  <!-- UUID: 154be1f7-3e96-417a-b125-f978c47e2301 -->

The signers of the Operator Multisig are three (3) addresses controlled by Core GovOps.

###### A.3.7.1.3.5.1.4 - Operator Multisig Usage Standards [Core]  <!-- UUID: 9e2f39aa-0568-46a3-ad5c-898eba6e50c0 -->

The signers of the Operator Multisig must use the multisig to operate the Stability Parameter Bounded External Access Module in accordance with the instructions specified in [A.3.7.1.3.6 - Update Process](823aa477-5400-40e5-881f-acb9cf724c21).

###### A.3.7.1.3.5.1.5 - Operator Multisig Modification [Core]  <!-- UUID: 24b8a5d0-b2b0-4bdf-94cf-f873d7468d48 -->

Core GovOps can change the signers of the Operator Multisig at any time, so long as there are at least three (3) signers and at least a majority of signers are required to execute transactions.

###### A.3.7.1.3.5.2 - Operator Update Process [Core]  <!-- UUID: ae2b5d27-b666-4796-8791-b59d151daf41 -->

Stability Parameter Bounded External Access Module Operators can be modified by the Core Facilitator, in consultation with the Core Council Risk Advisor. This process will be conducted through the Operational Weekly Cycle or, if necessary, through out-of-schedule Executive Votes.

##### A.3.7.1.3.6 - Update Process [Core]  <!-- UUID: 823aa477-5400-40e5-881f-acb9cf724c21 -->

The rates set by the Stability Parameter Bounded External Access Module (SP-BEAM) are managed by the SP-BEAM Operators. The SP-BEAM Operators' use of this authority must wholly adhere to instructions provided by the Core Council Risk Advisor.

###### A.3.7.1.3.6.1 - Request By Core Council Risk Advisor [Core]  <!-- UUID: 0f718693-f764-48e5-8b0c-ad36389ba3a0 -->

Any requests to change rates set by the SP-BEAM must be posted to the Sky Forum by the Core Council Risk Advisor that is recommending the change.

###### A.3.7.1.3.6.2 - Operator Execution [Core]  <!-- UUID: c49357ad-4961-497b-9449-662922cb70a7 -->

Once a rate change request has been posted to the Sky Forum by the Core Council Risk Advisor, the SP-BEAM Operators must prepare and execute the proposed changes in a timely manner. Preparation can include the creation of transaction simulations to verify inputs.

###### A.3.7.1.3.6.3 - Public Communication [Core]  <!-- UUID: 30a9cafe-92cc-4c9b-af94-c341915a1dfc -->

Once a change in rates set by the SP-BEAM has been executed, the execution must be publicly communicated to the Sky Ecosystem. This communication may take the form of either (1) a Forum post or (2) inclusion of the execution in an informational dashboard that allows community members to see each rate change executed by the SP-BEAM.

#### A.3.7.1.4 - Keepers [Core]  <!-- UUID: f2bba617-0bc5-4983-8885-4ab686ae4fc7 -->

Keepers are a critical component of the Sky Protocol infrastructure. They are automated systems responsible for controlling, monitoring, and supporting backend operations, thereby ensuring the stability, security, and overall integrity of the Sky Protocol and its users. Due to their importance, it is essential that keepers operate continuously and reliably. They must also maintain sufficient funding to cover gas costs required for their execution. The subdocuments herein specify the current keeper providers and, where applicable, their associated payment streams.

##### A.3.7.1.4.1 - Chainlink Automation [Core]  <!-- UUID: af29fc28-e4d4-4921-98e5-9468f06068ec -->

Chainlink Automation

Budget: 1,500 USDS per day
Stream Duration: 3 years (start date 29 May 2023).

##### A.3.7.1.4.2 - TechOps Services [Core]  <!-- UUID: cc7914f8-61bd-4cc6-933c-715ceff3ea19 -->

TechOps Services operates the `SKY` lane in the dss-cron Sequencer, handling keeper creation, setup, and regularly scheduled automatic execution with 24/7 support services for the Sky Protocol.

#### A.3.7.1.5 - Offboarding Process [Core]  <!-- UUID: 3da8a0fd-952c-4f80-b674-f60c9a293cb9 -->

The subdocuments herein define the process by which Sky vault users should be notified about collateral offboarding.

##### A.3.7.1.5.1 - Legacy Context [Core]  <!-- UUID: 6e08fc61-dc0d-4f18-8f4d-faa75f7dc59a -->

Periodically, collateral and vault types (ilks) are re-evaluated, which sometimes results in an offboarding of that collateral or vault type.

There have been several instances where users entered official Sky forums/chats to understand why they had been suddenly liquidated, despite historically comfortable collateralization ratios ([https://forum.skyeco.com/t/an-assessment-first-hand-experience-and-recommendations-from-the-aave-offboarding/11836](https://forum.skyeco.com/t/an-assessment-first-hand-experience-and-recommendations-from-the-aave-offboarding/11836)). This is, understandably, a poor user experience.

Even with liquidation penalties set to 0%, the forced unwinding of levered positions conceivably can result in user losses, as well as potentially taxable events.

This Section defines procedures concerning the dissemination of information about upcoming collateral offboarding on a best-effort basis. The objective is to minimize the number of users who are unaware of the offboarding prior to getting their positions liquidated.

###### A.3.7.1.5.1.1 - Legacy Context Specific Goals [Core]  <!-- UUID: dd7c5813-2026-4d1c-9bc8-33cf8fbee15a -->

Specific Goals:

1. Codify a series of good-faith communication efforts.
2. Provide an easy-to-follow process for Sky contributors to follow without significant burden.
3. Minimize the number of users unaware of a collateral offboarding.
4. Provide a method to bypass these requirements in the event a collateral is being offboarded due to serious security or solvency concerns.

##### A.3.7.1.5.2 - Technical Process [Core]  <!-- UUID: 305e2bd6-a594-4aec-8713-adbe7bc87120 -->

The subdocuments herein specify actions to be taken by specific actors within Sky when offboarding a vault type.

###### A.3.7.1.5.2.1 - Immediate Actions [Core]  <!-- UUID: 200a9e67-ed5d-4d60-b826-860a2a247dcc -->

Upon approval by Sky Governance to offboard a permissionless collateral type or vault type, the following actions are taken as soon as is practicable:

- Set debt ceiling to zero (0) Dai or USDS.
- Make an initial public announcement on all communication channels listed in [A.3.7.1.5.3.0.6.1 - Communication Channels And Media Assets Listing](9ac8a70b-8b6a-4825-a5e0-5e9019e50bc4).
- Make a second public announcement on all communication channels in the above cited document no later than 14 calendar days after the initial public announcement.
- Once the second public announcements have been made, set the liquidation penalty to 0%.

###### A.3.7.1.5.2.2 - Following Actions [Core]  <!-- UUID: e0891d48-c684-4372-96e8-988aba8cccee -->

Parameter changes designed to offboard users, such as changes to the liquidation ratio or stability fee, can only be implemented once 14 calendar days have passed following a second public announcement.

##### A.3.7.1.5.3 - Communication Channels And Media Assets [Active Data Controller]  <!-- UUID: 9d418790-3081-43b4-a6f6-1c49ff5b4be8 -->

The process for adding, removing, and modifying communication channels and media assets, and the order of announcement publication, are defined as Active Data in [A.3.7.1.5.3.0.6.1 - Communication Channels And Media Assets Listing](9ac8a70b-8b6a-4825-a5e0-5e9019e50bc4).

The Active Data is updated as follows:

- The Responsible Party is Core GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.3.7.1.5.3.0.6.1 - Communication Channels And Media Assets Listing [Active Data]  <!-- UUID: 9ac8a70b-8b6a-4825-a5e0-5e9019e50bc4 -->

The following channels should be used for initial and second public announcements of collateral offboarding. The order of announcement publication is as follows:

1. The author of the collateral offboarding notice shall post to the Sky Forum detailing the recommended offboarding. This forum thread is used to inform downstream announcements on other channels.
2. Core GovOps publishes the associated notices to:
    - All public Sky Calendars
    - The Sky Official Discord’s Announcement channel.
    - The official Sky subreddit.
3. Partner Relationship Leads from relevant Ecosystem Actors reach out to:
    - Affected collateral partners (e.g., Aave)
    - Affected frontend service providers (e.g., Oasis, DeFi Saver)

Additionally, outreach may be done to cover more channels not listed here. These may include other Ecosystem Actor or Facilitator owned Twitter accounts, communication channels, and platforms.

Unless otherwise noted in [A.3.7.1.5 - Offboarding Process](3da8a0fd-952c-4f80-b674-f60c9a293cb9) and its subdocuments, Core GovOps will take the lead in coordinating channels announcements.

##### A.3.7.1.5.4 - Expedited Offboarding [Core]  <!-- UUID: f9894690-fb43-431c-84ae-c6f5886745e9 -->

The subdocuments herein define an expedited offboarding process in the event a collateral type needs to be removed quickly due to security or solvency concerns.

###### A.3.7.1.5.4.1 - Requirements [Core]  <!-- UUID: 5f2109db-6680-478b-b72a-45f30065b626 -->

When a collateral type threatens the security or solvency of the Sky Protocol, an expedited offboarding is in order. Expedited offboardings override the timeline specified in [A.3.7.1.5.2 - Technical Process](305e2bd6-a594-4aec-8713-adbe7bc87120) and allow the immediate modification of all relevant parameters.

Expedited offboardings must proceed pursuant to the following requirements:

- The Offboarding Proposal must state that the offboarding should be expedited due to an emergency or urgent concern, as defined in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225)**.**
- The Offboarding Proposal must explicitly reference this Atlas document.

###### A.3.7.1.5.4.2 - Announcements [Core]  <!-- UUID: b83a3a8b-a5ab-4eed-abf0-31842ebbfa29 -->

The public announcements defined in [A.3.7.1.5.2 - Technical Process](305e2bd6-a594-4aec-8713-adbe7bc87120) must still be carried out. However, the timing of these announcements no longer constrains the modification of parameters. These announcements must also state that the offboarding is being expedited and explain the reasons for this accelerated process.

#### A.3.7.1.6 - Genesis Capital Backstop [Core]  <!-- UUID: a9965d58-8cda-49fc-8a7f-f8cc2e0d6b98 -->

If losses exceed a Prime Agent’s capital and cannot be absorbed by the Sky Surplus Buffer, the Sky Protocol must apply a pro‑rata haircut across each Genesis Agent’s Genesis Capital, implemented as a transfer of eligible assets from each Agent to the Sky Surplus Buffer. The haircut must be sized to cover the portion of the loss that exceeds what the Prime Agent’s capital and the Sky Surplus Buffer can absorb, up to a maximum of the Aggregate Backstop Capital (see [A.3.5.3.1.2 - Aggregate Backstop Capital](6dbead44-5ac4-4c5b-be3c-64eddd004e5c)).

##### A.3.7.1.6.1 - Implementation [Core]  <!-- UUID: 4381df75-0d4f-4f17-a263-f796cc33be27 -->

In the near term, transfers are made through Executive Votes and may be made through Emergency Spells (see [A.1.10.5 - Emergency Spells](b8266c11-3a84-4bbe-abe2-de9474f74ffd)) as part of the Emergency Response System (see [A.1.9.1 - Emergency Response](20dcf582-8862-48b3-9ca9-c3703871bd14)).

A solution must be developed to allow these transfers to be accomplished on an automated basis without waiting for the GSM Pause Delay (see [A.1.10.3 - Governance Security Delay Requirements](c5f0e955-0441-42e0-a6fc-eab875bba568)).

##### A.3.7.1.6.2 - Post Backstop Settlement [Core]  <!-- UUID: 1edfed11-0234-4d15-b52b-37d7493565cd -->

If, after the haircut, losses still exceed the combined capacity of the Prime Agent’s capital and Aggregate Backstop Capital (see [A.3.5.3.1.2 - Aggregate Backstop Capital](6dbead44-5ac4-4c5b-be3c-64eddd004e5c)), the SKY Backstop (see [A.3.6 - SKY Backstop](4d8b0d82-97da-4041-b185-4b98c2779cbe)) is activated. The SKY mint must be sized to cover the remaining loss. If losses still exceed what the SKY Backstop can absorb, Sky will adjust the USDS target price below $1 to the extent necessary to settle the remaining deficit; Sky will then distribute 24 billion SKY to USDS holders via an airdrop.

##### A.3.7.1.6.3 - Genesis Agent Capital Shortfalls [Core]  <!-- UUID: 81bacfed-5cc9-4980-bf71-1e5edcbdadba -->

Transfers of capital from Genesis Agents may cause capital shortfalls for Genesis Agents under the Risk Framework (see [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4)). Sky will work in good faith with such Agents to waive penalties for a reasonable period of time to allow the Agents to rebuild their capital.

##### A.3.7.1.6.4 - Relation To SKY Backstop [Core]  <!-- UUID: 3b7324cd-8246-4eed-9da9-56599dcac5b4 -->

The Genesis Capital Backstop must be applied before the SKY Backstop (see [A.3.6 - SKY Backstop](4d8b0d82-97da-4041-b185-4b98c2779cbe)).

##### A.3.7.1.6.5 - Genesis Agents [Core]  <!-- UUID: 8952aac5-24fb-4da1-ae10-49f86d30aecd -->

Genesis Agents are Agents that receive capital contributions from Sky, including, without limitation:

- Spark
- Grove
- Keel
- Skybase
- Obex
- Osero
- Core Council Executor Agent 1
- Amatsu
- Ozone

##### A.3.7.1.6.6 - Genesis Capital [Core]  <!-- UUID: 18f3de06-064b-4b08-a855-4720240e37f5 -->

The Genesis Capital of an Agent is the lesser of (1) the Eligible Genesis Capital of the Agent and (2) the total capital of the Agent. The Eligible Genesis Capital of an Agent is the amount of capital contributed by Sky to the Agent (see [A.3.7.1.6.6.1 - Amount Of Capital Contributed By Sky To Agents](0331556e-e7ae-48a2-a693-75468c416321)) minus the Phased-Out Genesis Capital of the Agent (see [A.3.7.1.6.6.2.3.0.6.1 - Current Phased-Out Genesis Capital](41bf89b5-dae5-47f3-bd6b-73b5598d9a0d)).

###### A.3.7.1.6.6.1 - Amount Of Capital Contributed By Sky To Agents [Core]  <!-- UUID: 0331556e-e7ae-48a2-a693-75468c416321 -->

The amount of capital contributed by Sky to Agents is:

- Spark - 25,000,000 USDS
- Grove - 25,000,000 USDS
- Obex - 21,000,000 USDS
- Skybase - 15,000,000 USDS
- Core Council Executor Agent 1 - 25,000,000 USDS
- Keel - 10,000,000 USDS
- Osero - 10,500,000 USDS
- Amatsu - 25,000,000 USDS
- Ozone - 25,000,000 USDS

###### A.3.7.1.6.6.2 - Genesis Capital Phase-Out [Core]  <!-- UUID: 9c06226e-b9ed-49e7-8d82-557b9414b294 -->

As the ecosystem matures and Aggregate Backstop Capital (see [A.3.5.3.1.2 - Aggregate Backstop Capital](6dbead44-5ac4-4c5b-be3c-64eddd004e5c)) reaches a sufficient level, Genesis Capital will phase out. The documents herein define the eligibility conditions and phase-out amounts.

Phase-out is effected by increasing an Agent's Phased-Out Genesis Capital (see [A.3.7.1.6.6.2.3 - Phased-Out Genesis Capital](8f813186-1317-41b1-86d1-47fce7f42af5)), which reduces the Agent's Eligible Genesis Capital and therefore its Genesis Capital, progressively reducing the Genesis Capital subject to the Genesis Capital Backstop (see [A.3.7.1.6 - Genesis Capital Backstop](a9965d58-8cda-49fc-8a7f-f8cc2e0d6b98)). Phase-out does not involve any repayment or transfer of capital from the Genesis Agents to Sky.

###### A.3.7.1.6.6.2.1 - Phase-Out Eligibility [Core]  <!-- UUID: 6038d06a-6a02-4f8f-9e7d-32f4f2d1f624 -->

The documents herein define the conditions under which Genesis Capital phase-out is active. Both Sky-level and Prime Agent-level conditions must be satisfied.

###### A.3.7.1.6.6.2.1.1 - Sky Phase-Out Eligibility Conditions [Core]  <!-- UUID: 5396bafc-8d6e-4006-bd8b-ee08ac35c729 -->

Genesis Capital phase-out is active when Aggregate Backstop Capital is at or above 125 million USDS. If Aggregate Backstop Capital falls below 125 million USDS at any point, phase-out pauses for all Genesis Agents until Aggregate Backstop Capital is once again at or above the threshold.

###### A.3.7.1.6.6.2.1.2 - Genesis Agent Phase-Out Eligibility Conditions [Core]  <!-- UUID: 392f7cb8-b2cf-4e2c-91e4-4b1eb6edf68f -->

A Genesis Agent becomes eligible for Genesis Capital phase-out when it has launched a liquid token with at least ten (10) million USDS in average daily trading volume over a thirty (30) day period.

###### A.3.7.1.6.6.2.2 - Phase-Out Amount [Core]  <!-- UUID: 32e3b6cf-c3f7-4756-a8af-31920fc81319 -->

For each eligible Genesis Agent whose eligibility conditions are satisfied, the phase-out amount per month (the Total Phase-Out Amount) is the sum of the Base Phase-Out Amount and the Additional Phase-Out Amount, as specified in the documents herein. Following each Monthly Settlement Cycle, the Current Phased-Out Genesis Capital (see [A.3.7.1.6.6.2.3.0.6.1 - Current Phased-Out Genesis Capital](41bf89b5-dae5-47f3-bd6b-73b5598d9a0d)) for each Agent must be increased by the Total Phase-Out Amount for that Agent, but must not exceed the amount of capital contributed by Sky to that Agent (see [A.3.7.1.6.6.1 - Amount Of Capital Contributed By Sky To Agents](0331556e-e7ae-48a2-a693-75468c416321)).

###### A.3.7.1.6.6.2.2.1 - Base Phase-Out Amount [Core]  <!-- UUID: 7584440d-182b-4d6d-bb8e-d85ee5a37291 -->

The Base Phase-Out Amount is one (1) million USDS per eligible Genesis Agent per month.

###### A.3.7.1.6.6.2.2.2 - Additional Phase-Out Amount [Core]  <!-- UUID: ed547147-bb36-42fa-9008-96af46f9640d -->

The Additional Phase-Out Amount per eligible Genesis Agent per month is the amount by which Aggregate Backstop Capital exceeds 125 million USDS, divided by 10.

###### A.3.7.1.6.6.2.3 - Phased-Out Genesis Capital [Active Data Controller]  <!-- UUID: 8f813186-1317-41b1-86d1-47fce7f42af5 -->

The Phased-Out Genesis Capital for each Genesis Agent is defined as Active Data in [A.3.7.1.6.6.2.3.0.6.1 - Current Phased-Out Genesis Capital](41bf89b5-dae5-47f3-bd6b-73b5598d9a0d).

The Active Data is updated as follows:

- The Responsible Party is the Core Council Risk Advisor.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.3.7.1.6.6.2.3.0.6.1 - Current Phased-Out Genesis Capital [Active Data]  <!-- UUID: 41bf89b5-dae5-47f3-bd6b-73b5598d9a0d -->

The current Phased-Out Genesis Capital for each Genesis Agent is:

- Spark - 0 USDS
- Grove - 0 USDS
- Obex - 0 USDS
- Skybase - 0 USDS
- Core Council Executor Agent 1 - 0 USDS
- Keel - 0 USDS
- Osero - 0 USDS
- Amatsu - 0 USDS
- Ozone - 0 USDS
