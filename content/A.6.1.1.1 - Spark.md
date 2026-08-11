# A.6.1.1.1 - Spark [Core]  <!-- UUID: dee2f5a4-279a-488c-9a9d-9583e3216fbf -->

The documents herein specify all of the logic for Spark, including Spark’s strategy and how it uses the Sky Primitives to operationalize this strategy.

## A.6.1.1.1.1 - Introduction [Core]  <!-- UUID: fee4e7c1-bc69-496e-8e1b-a1f7a76daa70 -->

Spark is an Agent focused on building on USDS in the Ethereum and adjacent DeFi ecosystem. This includes driving adoption of USDS and deploying collateral backing USDS at attractive risk-adjusted returns. Spark does this through the Spark Liquidity Layer, SparkLend, and Spark Savings.

- The Spark Liquidity Layer directly provides USDS, sUSDS, and USDC liquidity across networks and DeFi markets.
- SparkLend is a lending market focused on USDS borrowing, sourcing liquidity directly from Sky to provide the best borrow rates for USDS.
- Spark Savings enables stablecoin holders to earn the best risk-adjusted rate in DeFi, at large scale, with minimal liquidity constraints.

## A.6.1.1.1.2 - Sky Primitives [Core]  <!-- UUID: 1bc21199-26d0-4cdd-8d66-454ac62204b9 -->

The documents herein implement the Sky Primitives for Spark. See [A.2.2 - Sky Primitives](fcde2604-a138-4c1b-9d9a-14895835c907).

### A.6.1.1.1.2.1 - Genesis Primitives [Core]  <!-- UUID: cccaa367-6157-4640-ba62-3fccd987d07c -->

The documents herein implement the Genesis Primitives for Spark. See [A.2.2.5 - Genesis Primitives](3d5e3668-8333-4908-adcc-5784cfe7f6b5).

#### A.6.1.1.1.2.1.1 - Agent Creation Primitive [Core]  <!-- UUID: 5f670f2b-16e4-4a3d-84bc-9a302e32b671 -->

The documents herein contain all data and specifications for Spark’s Instance of the Agent Creation Primitive. See [A.2.2.5.1 - Agent Creation Primitive](82b95f6d-4883-4f08-ac3a-9d8189013fbe).

##### A.6.1.1.1.2.1.1.1 - Primitive Hub Document [Core]  <!-- UUID: 30cd682c-0688-4b2f-a72e-7cded8feb180 -->

The documents herein organize all base information relevant to Spark’s usage of the Agent Creation Primitive.

###### A.6.1.1.1.2.1.1.1.1 - Global Activation Status [Core]  <!-- UUID: 5763b3c1-1605-4171-8928-4545ccb67cad -->

`Completed`

###### A.6.1.1.1.2.1.1.1.2 - Active Instances Directory [Core]  <!-- UUID: c9b60d7e-7009-4614-8975-aa481a8ef1de -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.1.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 4620942e-d34c-4383-b3f4-6faab0eaad27 -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.1.1.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: d1fbe16e-f2a5-4e3a-9352-fa6f8a69b445 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.1.1.3.1 - Single Instance Configuration Document](8f26332f-df39-4ff5-bec4-ec34a6bcc0c3).

###### A.6.1.1.1.2.1.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 5c48cc46-b6f9-4204-a16f-b3043903135e -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.1.2.1.1.1.5 - Hub Data Repository [Core]  <!-- UUID: d50b68ce-a255-4fd9-ba02-7a7b46b7f0ce -->

The document herein contains the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.1.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 912254f8-e19d-447f-9f6d-59ff488b8fbc -->

The subtrees for archived Invocations and Instances of the Agent Creation Primitive are stored here.

###### A.6.1.1.1.2.1.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 67bf2190-7ec8-4146-bd23-a714c964e0d9 -->

The subtrees for failed Invocations of the Agent Creation Primitive are stored here.

###### A.6.1.1.1.2.1.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: a0212282-b803-44f8-acdf-58529306a95c -->

The subtrees for Instances of the Agent Creation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.1.1.2 - Active Instances [Core]  <!-- UUID: 6879edeb-735e-43ef-ab35-e8fc3fc0e5aa -->

The Instances of the Agent Creation Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 5eff8c9f-8499-41ff-9aed-2e31d9f5f139 -->

The Instances of the Agent Creation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.1.2.1.1.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 8f26332f-df39-4ff5-bec4-ec34a6bcc0c3 -->

The documents herein contain the Instance Configuration Document for the Single Agent Creation Primitive Instance.

###### A.6.1.1.1.2.1.1.3.1.1 - Parameters [Core]  <!-- UUID: 78bd0c0c-bdf0-4f75-86f2-47cbfa2e3dfc -->

The documents herein define the parameters of the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.1.2.1.1.3.1.1.1 - Name [Core]  <!-- UUID: 6bb5016e-2252-4317-a5a5-6affc59b5209 -->

The name of the Agent is Spark.

###### A.6.1.1.1.2.1.1.3.1.1.2 - SubProxy Account [Core]  <!-- UUID: 378950e0-85c9-4f12-94cd-fb36cde59ba9 -->

The address of Spark’s SubProxy Account on the Ethereum Mainnet is `0x3300f198988e4C9C63F75dF86De36421f06af8c4`.

###### A.6.1.1.1.2.1.1.3.1.1.3 - Genesis Account [Core]  <!-- UUID: e160e2e9-a1f2-4beb-af44-b7bc86ab163f -->

The address of Spark’s Genesis Account will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.1.1.3.1.1.4 - Foundation [Core]  <!-- UUID: 166669dd-467a-4d82-b7e5-5ea18cae5b61 -->

The Spark Foundation is the Prime Foundation associated with Spark. Its mandate is to support the development, growth, and adoption of Spark.

###### A.6.1.1.1.2.1.1.3.1.1.5 - Development Company [Core]  <!-- UUID: dd82336a-db68-4e58-a624-22d6de00be4c -->

Phoenix Labs is a development company that provides services to the Spark Foundation. Phoenix Labs is a "Nested Contributor", i.e., a core contributor to both Spark and Sky.

###### A.6.1.1.1.2.1.1.3.1.1.6 - Custom Instance Parameters [Core]  <!-- UUID: 4bc28587-5f7f-4297-840d-ec2109f2e6be -->

The documents herein define the custom parameters of the Single Instance of the Agent Creation Primitive, if any.

###### A.6.1.1.1.2.1.1.3.1.1.6.1 - Spark Assets Foundation [Core]  <!-- UUID: 4d70e4a7-6f65-421c-b22a-ac5a6eae8170 -->

Spark Assets Foundation is an entity, the purpose of which is to support the Spark Liquidity Layer through real world engagements and allocations. Spark Assets Foundation will deploy assets which are held in the ALM Contracts.

###### A.6.1.1.1.2.1.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: b660c45c-7837-4cc8-b91a-6911c74e9342 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.1.2.1.1.3.1.3 - Data Repository [Core]  <!-- UUID: f1490752-03fe-4e21-ae1f-68a1ec44dbcc -->

The documents herein contain data relevant to the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.1.2.1.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: d48938da-ffb4-4470-b6ea-c22d25f3cced -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.1.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: e52ba148-0e92-4155-9df7-b35797ee4078 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.1.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 84c5a139-3778-4542-8631-c13283a2cc1c -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.1.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 1974618c-b054-41c3-a6aa-860ea7875d02 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.1.2.1.2 - Prime Transformation Primitive [Core]  <!-- UUID: 0037156e-3b1d-4baa-8a4a-a62936daeb3e -->

The documents herein contain all data and specifications for Spark’s Instance of the Prime Transformation Primitive. See [A.2.2.5.2 - Prime Transformation Primitive](81411106-fd6d-4f9c-b3ae-7af7b5e62482).

##### A.6.1.1.1.2.1.2.1 - Primitive Hub Document [Core]  <!-- UUID: 6dd6571c-f210-4e9e-850a-206275d2074e -->

The documents herein organize all base information relevant to Spark’s usage of the Prime Transformation Primitive.

###### A.6.1.1.1.2.1.2.1.1 - Global Activation Status [Core]  <!-- UUID: 192b3c63-90d9-430c-8046-d60b96d20903 -->

`Completed`

###### A.6.1.1.1.2.1.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 3bab6c0a-31a2-41d6-9bc8-560e3ff7ca95 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.1.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: c30a1946-aaf2-4523-b0c5-e5c8847e9ea9 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.1.2.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 2a9efb32-b644-4f2e-aea4-e92c8a53f8ab -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.1.2.3.1 - Single Instance Configuration Document](925c39a5-51a5-4d75-bac2-bae3af5f3861).

###### A.6.1.1.1.2.1.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 87a1cc55-f46d-4933-b53d-aff285fe5fec -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.1.2.1.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 2bf9316e-8ef2-45e4-b6a1-66db55a22bc6 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.1.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 50b95590-6c73-44ac-a09d-d7bac5995f7d -->

The subtrees for archived Invocations and Instances of the Prime Transformation Primitive are stored here.

###### A.6.1.1.1.2.1.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 50a8cdc0-f406-436a-84f6-2d554531da76 -->

The subtrees for failed Invocations of the Prime Transformation Primitive are stored here.

###### A.6.1.1.1.2.1.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 5c1785b4-152d-453a-91bb-f4d88e9eb1c8 -->

The subtrees for Instances of the Prime Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.1.2.2 - Active Instances [Core]  <!-- UUID: 48617d95-a95d-4ded-857d-479306443de5 -->

The Instances of the Prime Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.1.2.3 - Completed Instances [Core]  <!-- UUID: cf387ed3-7d5a-4e7b-9d2d-54c1f856f39c -->

The Instances of the Prime Transformation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.1.2.1.2.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 925c39a5-51a5-4d75-bac2-bae3af5f3861 -->

The documents herein contain the Instance Configuration Document for the Single Prime Transformation Primitive Instance.

###### A.6.1.1.1.2.1.2.3.1.1 - Parameters [Core]  <!-- UUID: d141615a-ab1a-4b5a-a483-aad1fcadc0e2 -->

The documents herein define the parameters of the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.1.2.1.2.3.1.1.1 - Agent Type [Core]  <!-- UUID: 053995ec-4b58-4c4b-a3c1-029d65cd7b00 -->

Spark is a Prime Agent.

###### A.6.1.1.1.2.1.2.3.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: e0a0c589-4952-4ccf-8af9-d0bd56abbe6a -->

The documents herein define the custom parameters of the Single Instance of the Prime Transformation Primitive, if any.

###### A.6.1.1.1.2.1.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: dcba1b43-498c-4947-9142-a2e8804a62e2 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.1.2.1.2.3.1.3 - Data Repository [Core]  <!-- UUID: 48223101-7247-4ddc-88d0-d502552708a0 -->

The documents herein contain data relevant to the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.1.2.1.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: b8c4fa46-ae4e-4caf-b5eb-09a3b0a45b80 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.1.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: dd32b7e4-8905-4ce8-b5a1-4478ef4f9028 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.1.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 7d7d5045-d2f5-4668-ad1f-d943f941238a -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.1.2.1.2.4 - In Progress Invocations [Core]  <!-- UUID: 4c591869-ad1c-4007-9159-78705b24e43a -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.1.2.1.3 - Executor Transformation Primitive [Core]  <!-- UUID: cf323ace-ea1f-4272-b4b6-152dd36eea9e -->

The documents herein contain all data and specifications for Spark’s Instance of the Executor Transformation Primitive. See [A.2.2.5.3 - Executor Transformation Primitive](2f249be5-8edb-41e4-b429-734e1ba2cbc7).

##### A.6.1.1.1.2.1.3.1 - Primitive Hub Document [Core]  <!-- UUID: 4130ff50-bc52-4c82-b461-df14bc9aece2 -->

The documents herein organize all base information relevant to Spark’s usage of the Executor Transformation Primitive.

###### A.6.1.1.1.2.1.3.1.1 - Global Activation Status [Core]  <!-- UUID: fead0e9f-9f57-4bf8-9a17-c91655748023 -->

`Inactive`

###### A.6.1.1.1.2.1.3.1.2 - Active Instances Directory [Core]  <!-- UUID: d05a0506-d0d7-4160-abc9-3d140624f637 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.1.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: c6a88406-677b-4135-af1f-a82f08196b92 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.1.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 99eee71b-341b-4446-bffd-3b3f81a0887a -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.1.2.1.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 7aa32207-e371-4e7a-8510-e52a6e04457a -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.1.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 0a661998-4951-4edf-9bcd-c9f06edca281 -->

The subtrees for archived Invocations and Instances of the Executor Transformation Primitive are stored here.

###### A.6.1.1.1.2.1.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 2d9ca145-3e86-4214-94f4-e7343b3aae9d -->

The subtrees for failed Invocations of the Executor Transformation Primitive are stored here.

###### A.6.1.1.1.2.1.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: a8b09d72-8d9b-4f07-9e1a-7a3542f3989e -->

The subtrees for Instances of the Executor Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.1.3.2 - Active Instances [Core]  <!-- UUID: 25082eb4-526e-4132-b8cb-f1b035b979bc -->

The Instances of the Executor Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.1.3.3 - Completed Instances [Core]  <!-- UUID: c0754ba7-c179-40b1-b4c5-f5cc54052004 -->

The Instances of the Executor Transformation Primitive with `Completed` Status are contained herein.

##### A.6.1.1.1.2.1.3.4 - In Progress Invocations [Core]  <!-- UUID: ea1e82bb-a5e5-48a4-bbf5-520da8282f78 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.1.2.1.4 - Agent Token Primitive [Core]  <!-- UUID: 676bc853-5516-41e6-911e-9e4dde93157c -->

The documents herein contain all data and specifications for Spark’s Instance of the Agent Token Primitive. See [A.2.2.5.4 - Agent Token Primitive](2047c361-db28-4952-a70c-83d07b562064).

##### A.6.1.1.1.2.1.4.1 - Primitive Hub Document [Core]  <!-- UUID: 4476d153-381e-4120-8230-68d1bd60ec6d -->

The documents herein organize all base information relevant to Spark’s usage of the Agent Token Primitive.

###### A.6.1.1.1.2.1.4.1.1 - Global Activation Status [Core]  <!-- UUID: dfbc2220-3077-4f33-9bf1-f53e78b08c26 -->

`Active`

###### A.6.1.1.1.2.1.4.1.2 - Active Instances Directory [Core]  <!-- UUID: 50fb42cb-2f3b-43ef-ad1a-51e5022aeacf -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.1.4.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 650e12f5-5126-476b-ad46-d686a6d2b22a -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.1.4.2.1 - Single Instance Configuration Document](b2b8b39e-e4d2-496c-b7ea-745ba9202197).

###### A.6.1.1.1.2.1.4.1.3 - Completed Instances Directory [Core]  <!-- UUID: 8c135060-f236-4b4e-bb85-85d07c41330b -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.1.4.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 90400c3d-7111-4e27-afaf-ed85b7d857f4 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.1.2.1.4.1.5 - Hub Data Repository [Core]  <!-- UUID: 294d8064-3368-48df-a1ad-d03a33afe123 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.1.4.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 79c042f5-1086-4526-a27f-45421672a17e -->

The subtrees for archived Invocations and Instances of the Agent Token Primitive are stored here.

###### A.6.1.1.1.2.1.4.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: db932cf1-db58-40fe-8a12-0114c76cb901 -->

The subtrees for failed Invocations of the Agent Token Primitive are stored here.

###### A.6.1.1.1.2.1.4.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: aaefe5c5-bd0c-4807-a25a-4d79be68943f -->

The subtrees for Instances of the Agent Token Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.1.4.2 - Active Instances [Core]  <!-- UUID: 1daf6d99-415f-4d4d-9de9-9a7300d591f5 -->

The Instances of the Agent Token Primitive with `Active` Status are stored herein.

###### A.6.1.1.1.2.1.4.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: b2b8b39e-e4d2-496c-b7ea-745ba9202197 -->

The documents herein contain the Instance Configuration Document for the Single Agent Token Primitive Instance.

###### A.6.1.1.1.2.1.4.2.1.1 - Parameters [Core]  <!-- UUID: 2e59431e-a058-4495-8c3b-a3619761754b -->

The documents herein define the parameters of the Single Instance of the Agent Token Primitive.

###### A.6.1.1.1.2.1.4.2.1.1.1 - Token Name [Core]  <!-- UUID: 23f952e8-47a7-4992-8066-18f200d4dddc -->

The name of Spark’s token is Spark.

###### A.6.1.1.1.2.1.4.2.1.1.2 - Token Symbol [Core]  <!-- UUID: f3dc9c8a-fc65-4856-82bc-13ecd956e7c8 -->

The symbol of Spark’s token is SPK.

###### A.6.1.1.1.2.1.4.2.1.1.3 - Genesis Supply [Core]  <!-- UUID: d238a8ef-985b-470f-b88d-0c3f1a449693 -->

The Genesis Supply of SPK is 10 billion.

###### A.6.1.1.1.2.1.4.2.1.1.4 - Token Address [Core]  <!-- UUID: 6ade0500-77d0-4d54-9bc3-0f6bad64f35f -->

The address of SPK on the Ethereum Mainnet is `0xc20059e0317DE91738d13af027DfC4a50781b066`. The address of SPK on Base is `0x24327d9138F9f3fc77BEcB10d9BDc2ABb324EE50`.

###### A.6.1.1.1.2.1.4.2.1.1.5 - Token Admin [Core]  <!-- UUID: b6153010-c6f7-41f0-b569-b2687b206ca2 -->

The token Admin is Spark’s SubProxy Account on the Ethereum Mainnet at `0x3300f198988e4C9C63F75dF86De36421f06af8c4`.

###### A.6.1.1.1.2.1.4.2.1.1.6 - Token Emissions [Core]  <!-- UUID: 6ff424a3-cb63-4eba-9966-771179ffa3ce -->

Token emissions beyond the Genesis Supply are permanently disabled; this cannot be reverted by Spark Governance. Sky Governance retains the ability to revert where Spark is in violation of Risk Capital requirements and emissions are required by the Risk Framework. See [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.6.1.1.1.2.1.4.2.1.1.7 - Custom Instance Parameters [Core]  <!-- UUID: 2debc8e3-b25a-41c6-aeb5-5f3b18dbc485 -->

The documents herein define the custom parameters of the Single Instance of the Agent Token Primitive, if any.

###### A.6.1.1.1.2.1.4.2.1.1.7.1 - Staking [Core]  <!-- UUID: 1bdf366d-1955-4ddb-8fb7-794ddcf1dc1e -->

SPK token holders can stake their tokens. The rewards for staking will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.1.4.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 978226ce-4c97-4a57-b4e0-d05b3e575c2d -->

The documents herein define the operational processes for minting and initial distribution of the tokens from the Genesis Supply.

###### A.6.1.1.1.2.1.4.2.1.2.1 - Minting Of Tokens To SPK Company Ltd [Core]  <!-- UUID: 8b3b46b1-e16a-4d1a-b4d0-52b4cc01ca4f -->

The Genesis Supply was minted to an account owned by SPK Company Ltd. The address of the account on the Ethereum Mainnet is `0x6FE588FDCC6A34207485cc6e47673F59cCEDF92B`.

###### A.6.1.1.1.2.1.4.2.1.2.2 - Transfer Of Tokens To Sky [Core]  <!-- UUID: 56e08ecf-3a37-45e3-9dce-c75271fcff6b -->

SPK Company Ltd transferred 6.5 billion SPK tokens from the SPK Company Ltd account to the Sky Pause Proxy. The SPK Company Ltd account is specified in [A.6.1.1.1.2.1.4.2.1.2.1 - Minting Of Tokens To SPK Company Ltd](8b3b46b1-e16a-4d1a-b4d0-52b4cc01ca4f).

###### A.6.1.1.1.2.1.4.2.1.2.3 - Transfer Of Tokens To Spark SubProxy Account [Core]  <!-- UUID: 34c854ac-2a38-4e44-9d49-ad5d1c1c1605 -->

SPK Company Ltd transferred 918,760,451 SPK tokens from the SPK Company Ltd account to the Spark SubProxy Account. The SPK Company Ltd account is specified in [A.6.1.1.1.2.1.4.2.1.2.1 - Minting Of Tokens To SPK Company Ltd](8b3b46b1-e16a-4d1a-b4d0-52b4cc01ca4f).

The Spark SubProxy Account is specified in [A.6.1.1.1.2.1.1.3.1.1.2 - SubProxy Account](378950e0-85c9-4f12-94cd-fb36cde59ba9).

###### A.6.1.1.1.2.1.4.2.1.2.4 - Transfer Of Tokens For Token Launch [Core]  <!-- UUID: 950458c9-dfa7-4c1f-a30a-05d7468fa1c6 -->

The SPK Company Ltd account will transfer SPK tokens in connection with the token launch. The SPK Company Ltd account is specified in [A.6.1.1.1.2.1.4.2.1.2.1 - Minting Of Tokens To SPK Company Ltd](8b3b46b1-e16a-4d1a-b4d0-52b4cc01ca4f).

The amount and nature of these distributions will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.1.4.2.1.2.5 - Transfer Of Tokens To Spark Foundation [Core]  <!-- UUID: e68b9cb2-81b0-414d-bea0-f05dbd6ed5a7 -->

The SPK Company Ltd account will transfer all of the SPK tokens held by it, other than the tokens specified in [A.6.1.1.1.2.1.4.2.1.2.4 - Transfer Of Tokens For Token Launch](950458c9-dfa7-4c1f-a30a-05d7468fa1c6), to the Spark Foundation. The SPK Company Ltd account is specified in [A.6.1.1.1.2.1.4.2.1.2.1 - Minting Of Tokens To SPK Company Ltd](8b3b46b1-e16a-4d1a-b4d0-52b4cc01ca4f).

The address of the Spark Foundation on the Ethereum Mainnet is `0x92e4629a4510AF5819d7D1601464C233599fF5ec`.

###### A.6.1.1.1.2.1.4.2.1.3 - Data Repository [Core]  <!-- UUID: a0504bd2-0147-406a-bfa3-ba5dcf518f84 -->

The documents herein contain data relevant to the Single Instance of the Agent Token Primitive.

###### A.6.1.1.1.2.1.4.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 5313f73b-6327-4bdd-8187-eba5f99620f9 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.1.4.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 75619f28-0a62-49cb-9afa-9e9e34f37ef5 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.1.4.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: ed197cc5-6ec7-4905-8b23-502940e1dd27 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.1.2.1.4.3 - Completed Instances [Core]  <!-- UUID: 6e713ffe-caf0-48dd-94e2-f1c9b1162aaa -->

The Instances of the Agent Token Primitive with `Completed` Status are contained herein.

##### A.6.1.1.1.2.1.4.4 - In Progress Invocations [Core]  <!-- UUID: bf55643f-a3db-4d19-9b83-d2da73acd0a5 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

### A.6.1.1.1.2.2 - Operational Primitives [Core]  <!-- UUID: 47f0c7ef-1b0a-4431-a9de-bc698fe51a46 -->

The documents herein implement the Operational Primitives for Spark. See [A.2.2.6 - Operational Primitives](0192ec95-9207-480e-8c51-88d2a1da95ad).

#### A.6.1.1.1.2.2.1 - Executor Accord Primitive [Core]  <!-- UUID: beff3df7-ff44-46f9-84ab-30cae1a03a06 -->

The documents herein contain all data and specifications for Spark’s Instances of the Executor Accord Primitive. See [A.2.2.6.1 - Executor Accord Primitive](88017877-3ec1-4c43-a035-6bebdf11d9bb).

##### A.6.1.1.1.2.2.1.1 - Primitive Hub Document [Core]  <!-- UUID: 7a6b27e0-4239-4481-9035-b16bf89e6a1d -->

The documents herein organize all base information relevant to Spark’s usage of the Executor Accord Primitive.

###### A.6.1.1.1.2.2.1.1.1 - Global Activation Status [Core]  <!-- UUID: 14ed5074-bac5-4328-9980-cd02d8ea4844 -->

`Active`

###### A.6.1.1.1.2.2.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 21e12538-4068-4bfe-978b-ebab93ccbfe7 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.2.1.1.2.1 - Amatsu Instance Configuration Document Location [Core]  <!-- UUID: bae55a03-dd1f-40c1-8675-3d2b8349a264 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.2.1.2.1 - Amatsu Instance Configuration Document](79147a0f-b07e-4137-a23c-a7ffbbf8b532).

###### A.6.1.1.1.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: beff536d-7bf2-42b1-87f3-d3163d0599c1 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 9d112903-70a7-4e8d-b1a9-c264c1273414 -->

This document contains a Directory of all prospective Instances of the Executor Accord Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.2.1.1.2 - Active Instances Directory](21e12538-4068-4bfe-978b-ebab93ccbfe7), whereas failed Invocations are Archived in [A.6.1.1.1.2.2.1.1.5 - Hub Data Repository](0bb8ba87-72eb-4219-b039-fa0ce29ae396).

###### A.6.1.1.1.2.2.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 0bb8ba87-72eb-4219-b039-fa0ce29ae396 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.2.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: d1ba7168-7093-4b73-828d-a92f9cdb1bb4 -->

The subtrees for archived Invocations and Instances of the Executor Accord Primitive are stored here.

###### A.6.1.1.1.2.2.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: f4b2c045-75a0-454a-8e5a-f92ac1895df4 -->

The subtrees for failed Invocations of the Executor Accord Primitive are stored here.

###### A.6.1.1.1.2.2.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 5fe424d1-c2f7-42a0-8925-53f2b22b8ca2 -->

The subtrees for Instances of the Executor Accord Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.2.1.2 - Active Instances [Core]  <!-- UUID: a092c9ca-35c7-4618-a85e-e3d12b6c8f3a -->

The Instances of the Executor Accord Primitive with `Active` Status are stored herein.

###### A.6.1.1.1.2.2.1.2.1 - Amatsu Instance Configuration Document [Core]  <!-- UUID: 79147a0f-b07e-4137-a23c-a7ffbbf8b532 -->

The documents herein contain the Instance Configuration Document for the Amatsu Executor Accord Primitive Instance.

###### A.6.1.1.1.2.2.1.2.1.1 - Parameters [Core]  <!-- UUID: ee6c93b6-2f9c-41c0-8a4e-9c83f2d726ef -->

The documents herein define the parameters of the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.1.2.2.1.2.1.1.1 - Operational Executor Agent [Core]  <!-- UUID: 7deff9e4-fa77-4f35-aac6-c73b3d014091 -->

The Operational Facilitator and Operational GovOps for Amatsu are specified in [A.6.1.2.1 - Operational Executor Agent Amatsu](c57df14a-fde0-43f3-89ed-c2e4981d6bd5).

###### A.6.1.1.1.2.2.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: df6dc78f-3340-4659-a1d8-60df78f6325e -->

The documents herein define the custom parameters of the Amatsu Instance of the Executor Accord Primitive, if any.

###### A.6.1.1.1.2.2.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 686bfbe0-9cce-46f5-ae47-ec69eb0fe561 -->

The documents herein define the process for the ongoing management of the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.1.2.2.1.2.1.3 - Data Repository [Core]  <!-- UUID: c1ee03df-67b9-4afc-ad4c-b681260412d9 -->

The documents herein contain data relevant to the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.1.2.2.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 1f60a729-4f0e-4310-8742-2f26395cd7de -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.2.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: ff21545c-e0d4-4057-8098-146a8c386f52 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.2.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 7ae391f1-e544-4ff5-b6d9-23fa95c75489 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.1.2.2.1.3 - Completed Instances [Core]  <!-- UUID: bf932245-fe5e-40cf-a79c-896f3220f3ec -->

The Instances of the Executor Accord Primitive with `Completed` Status are stored herein.

##### A.6.1.1.1.2.2.1.4 - In Progress Invocations [Core]  <!-- UUID: 30014177-2d03-44f5-ab3d-37c88cfd68e8 -->

The in progress Invocations of the Executor Accord Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.2.1.2 - Active Instances](a092c9ca-35c7-4618-a85e-e3d12b6c8f3a).

#### A.6.1.1.1.2.2.2 - Root Edit Primitive [Core]  <!-- UUID: f60887de-a4eb-4e4b-8aa6-e22cf724772a -->

The documents herein contain all data and specifications for Spark’s Instance of the Root Edit Primitive. See [A.2.2.6.2 - Root Edit Primitive](78488c6b-d77f-4344-b954-476e415a2c7d).

##### A.6.1.1.1.2.2.2.1 - Primitive Hub Document [Core]  <!-- UUID: c47922e8-4dca-49d9-ad95-79ca8ec04731 -->

The documents herein organize all base information relevant to Spark’s usage of the Root Edit Primitive.

###### A.6.1.1.1.2.2.2.1.1 - Global Activation Status [Core]  <!-- UUID: 9376926c-21db-43d6-ab51-382e99142367 -->

`Active`

###### A.6.1.1.1.2.2.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 8d46f816-d641-43bd-87a0-91892b8794b8 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.2.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 10cfec9a-f357-40cf-9653-05e1e53c693a -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.2.2.2.1 - Single Instance Configuration Document](2b2e324c-9ee1-4b25-b3b5-95ad85d6afeb).

###### A.6.1.1.1.2.2.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 08ee19bb-c8b6-4b13-9a5b-88d610a130a3 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.2.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 8fdc9d44-a0b0-488c-b244-8a84bd02a835 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.1.2.2.2.1.5 - Hub Data Repository [Core]  <!-- UUID: b6f05764-eb33-4263-ba7d-c849ea87d478 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.2.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 25f11e43-3772-4acb-8be8-4d66490e5587 -->

The subtrees for archived Invocations and Instances of the Root Edit Primitive are stored here.

###### A.6.1.1.1.2.2.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 40fdf4da-fd1a-434a-9d8a-5741ea76f864 -->

The subtrees for failed Invocations of the Root Edit Primitive are stored here.

###### A.6.1.1.1.2.2.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 6d59ed03-55af-4fff-a5f2-933e1f49115c -->

The subtrees for Instances of the Root Edit Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.2.2.2 - Active Instances [Core]  <!-- UUID: 75dc70de-f209-4c76-87b8-7a49bf989b3a -->

The Instances of the Root Edit Primitive with `Active` Status are stored herein.

###### A.6.1.1.1.2.2.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 2b2e324c-9ee1-4b25-b3b5-95ad85d6afeb -->

The documents herein contain the Instance Configuration Document for the Single Root Edit Primitive Instance.

###### A.6.1.1.1.2.2.2.2.1.1 - Parameters [Core]  <!-- UUID: 2708e477-b1ae-40f7-a206-9c736cb40491 -->

The parameters of the Root Edit Primitive are fully specified by the Operational Process Definition in [A.6.1.1.1.2.2.2.2.1.2 - Operational Process Definition](a9c97e28-6ac7-4e04-aac1-9d5dd617c6e0).

###### A.6.1.1.1.2.2.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: a9c97e28-6ac7-4e04-aac1-9d5dd617c6e0 -->

The documents herein define the process for using the Root Edit Primitive to update the Spark Agent Artifact. Information on Spark governance that is unrelated to the use of the Root Edit Primitive is located at [A.6.1.1.1.3.1 - Governance Information Unrelated To Root Edit Primitive](3dffc0f5-edbc-48e9-bf13-7d752a64de5a).

###### A.6.1.1.1.2.2.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 5c499f3a-d38e-4211-8394-4dc7d05cd383 -->

The documents herein define the process for using the Root Edit Primitive to update the Spark Agent Artifact in routine or normal conditions (i.e., non-emergency situations).

###### A.6.1.1.1.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission [Core]  <!-- UUID: c9f7cc6e-0548-4599-9f9d-bfa1d2bb7577 -->

The Root Edit process begins with a SPK token holder submitting a proposal through the Powerhouse system containing a draft Artifact Edit Proposal. A SPK token holder must hold at least 1% of the total token supply to submit a proposal. The proposal must also be posted on the Sky Forum under the "Spark Prime" category. The proposal must include an upfront review of opportunities and associated risks, outlining expected benefits, potential risks, and corresponding mitigation strategies for consideration by the community.

###### A.6.1.1.1.2.2.2.2.1.2.1.1.1 - Root Edit Proposal Submission Requirements Exception For Nested Contributors [Core]  <!-- UUID: cc4e9d94-1cba-45c0-938e-9260f9d8e458 -->

Nested Contributors are always authorized to submit Artifact Edit Proposals and do not have to fulfill the token-holding requirements defined in [A.6.1.1.1.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](c9f7cc6e-0548-4599-9f9d-bfa1d2bb7577). However, all other procedural requirements within the Root Edit process continue to apply.

To see the Agent’s Nested Contributors, see [A.6.1.1.1.2.1.1.3.1.1.5 - Development Company](dd82336a-db68-4e58-a624-22d6de00be4c).

###### A.6.1.1.1.2.2.2.2.1.2.1.1.2 - Short-Term Transitionary Measures [Core]  <!-- UUID: 3a6675c3-2bd6-49b0-8d2c-e9d4fe847a62 -->

Until the Powerhouse system supports submitting Artifact Edit Proposals, SPK token holders may submit Artifact Edit Proposals by posting them to the Sky Forum under the "Spark Prime" category. The title of the post must include the text "Spark Artifact Edit Proposal". The post must include cryptographic proof that the author controls an account holding the required percentage of the total SPK token supply specified in [A.6.1.1.1.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](c9f7cc6e-0548-4599-9f9d-bfa1d2bb7577).

###### A.6.1.1.1.2.2.2.2.1.2.1.2 - Root Edit Expert Advisor Review [Core]  <!-- UUID: 67fec75c-8289-4535-90bf-414417608254 -->

All Spark Root Edit proposals must be reviewed by the Spark Risk Council. The mandate, scope, and review process of the SRC are specified in [A.6.1.1.1.3.1.4 - Spark Risk Council](cf019fb3-d792-4867-abf7-cfe4d0b73e5d).

###### A.6.1.1.1.2.2.2.2.1.2.1.3 - Root Edit Proposal Review By Operational Facilitator [Core]  <!-- UUID: 32bad904-ba90-4abb-9115-0b304a792521 -->

Within seven (7) days of the proposal being submitted, the Operational Facilitator must review the Root Edit Proposal for alignment. The Operational Facilitator also checks if the author of the proposal complies with the requirements in [A.6.1.1.1.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](c9f7cc6e-0548-4599-9f9d-bfa1d2bb7577).

If the proposal is aligned, and the author is entitled to submit it, the Operational Facilitator must respond to the Forum post to announce their finding. In their Forum post, the Operational Facilitator must also confirm that the proposal is feasible for Operational GovOps to operationalize.

If the proposal is misaligned, or the author is not entitled to submit it, the Operational Facilitator must respond to the Forum post to announce their finding and provide the reasoning for it.

###### A.6.1.1.1.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote [Core]  <!-- UUID: b60cfc4e-4cc5-4040-9610-f2113980831b -->

Where their review of the proposal results in a finding of alignment with the Sky Core Atlas and Spark Artifact, and where the proposal passes review by the SRC (defined as "Passed SRC Review" in [A.6.1.1.1.3.1.4.3.1 - SRC Risk Review](968b4807-8032-42a3-b09d-f787cdb4ef87).), the Operational Facilitator next triggers a Snapshot poll to allow token holders to vote on the proposal. Token holders may vote directly or through Delegates. See [A.6.1.1.1.3.1.3 - Delegation Framework](afa6a37e-e7f1-4efb-bca7-f02bbbf5cf26). The poll is open for three (3) days. A poll must have more than 50% of votes cast, excluding abstentions, in favor to be approved.

Spark’s governance runs in a weekly cycle that begins every Monday. Upon receiving all approvals, the proposal is automatically included in the next cycle. The cut-off time is Friday 8:00 am UTC to ensure the Operational Facilitator has sufficient time to prepare the needed polls for the following Monday. After the cut-off time, it is at the discretion of the Operational Facilitator whether the proposal can be included in the immediate next cycle, or the following cycle.

###### A.6.1.1.1.2.2.2.2.1.2.1.5 - Root Edit Artifact Update [Core]  <!-- UUID: a9cecbeb-6f07-46fa-b5ad-68dd8ae4b0f0 -->

At the conclusion of the poll, if the proposal is approved, the Operational Facilitator submits the edit to Powerhouse to formally update the Agent Artifact. Regardless of the outcome, the Operational Facilitator updates the Powerhouse System to include the result of the vote, including any pertinent documents.

###### A.6.1.1.1.2.2.2.2.1.2.1.5.1 - Short Term Transitionary Measures [Core]  <!-- UUID: 6a9b3956-c4f0-4f59-bc7d-2028a642fc19 -->

Until the Powerhouse system supports updating Agent Artifacts, the Operational Facilitator works with the Core Facilitator to update the Atlas GitHub repository located at [https://github.com/sky-ecosystem/next-gen-atlas/pulls](https://github.com/sky-ecosystem/next-gen-atlas/pulls) to reflect proposals approved by Prime Governance.

###### A.6.1.1.1.2.2.2.2.1.2.1.6 - Artifact Edit Restrictions [Core]  <!-- UUID: 535cd1c9-1d4d-42e3-bb44-6c128690dd2d -->

The Spark Artifact cannot be edited in any way that violates the Sky Core Atlas or its specifications of the Sky Primitives, or in any way that is otherwise misaligned. The Operational Facilitator must enforce this rule through their review of Artifact Edit Proposals.

###### A.6.1.1.1.2.2.2.2.1.2.1.6.1 - Time-Limited Root Edit Restrictions On Removal Of Nested Contributors [Core]  <!-- UUID: cc60f445-1ed9-479e-9b44-00de9884a7b5 -->

For a period of three years after June 4, 2025, any Artifact Edit that would have the effect of removing a Nested Contributor must be approved by a vote of SKY holders in addition to a vote of SPK holders to be effective.

###### A.6.1.1.1.2.2.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 2ae0d2a3-5c06-4ecf-ab1d-abd797477642 -->

The documents herein define the process for using the Root Edit Primitive to update the Spark Agent Artifact in non-routine conditions.

###### A.6.1.1.1.2.2.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 7e4dd939-49ec-4cbc-80f5-eb1c71a80a50 -->

The documents herein define the process for using the Root Edit Primitive to update the Spark Agent Artifact in urgent or emergency situations.

###### A.6.1.1.1.2.2.2.2.1.2.3.1 - Root Edit Voting Process in Urgent and Emergency Situations [Core]  <!-- UUID: 0310ac15-5915-4174-8270-29b3119ce39b -->

In an Urgent or Emergency Situation, as defined by the Sky Core Atlas in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225), the Operational Facilitator may allow a Root Edit to occur more quickly than the timeline specified above. Where feasible, the Operational Facilitator should announce the decision to deploy the emergency Root Edit protocol and provide their reasoning via a public Sky Forum post (under the "Spark Prime" category), unless doing so would endanger Spark or its users.

###### A.6.1.1.1.2.2.2.2.1.2.4 - Short-Term Transitionary Measures [Core]  <!-- UUID: 6ecef2b2-42c7-4bea-80f0-1cb1cd4e735d -->

The parameters specified in [A.6.1.1.1.2.6.1 - Allocation System Primitive](cd70b9f1-1a59-407c-9945-05e52bf5a3b6) and [A.6.1.1.1.3.2.1 - SparkLend](d9ff0cd2-8999-4d3d-9670-2c7b49c1fe51) will be controlled by Sky Core Governance until Sky determines that the SPK token is decentralized enough to allow for meaningful governance by tokenholders. At such time, which is currently estimated for September 17, 2025, control will transition to Spark Governance. This transitionary measure ensures better decentralization of the SPK token before Spark Governance takes full control of the named parameters under the Root Edit Primitive.

###### A.6.1.1.1.2.2.2.2.1.3 - Data Repository [Core]  <!-- UUID: 67a53565-e1f0-4555-8223-fd6a4ba90814 -->

The documents herein contain data relevant to the Single Instance of the Root Edit Primitive.

###### A.6.1.1.1.2.2.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: f36d73f1-3ea3-4293-8902-15f7e8510a82 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.2.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 42aca05d-0f81-4e6a-a5df-4a0bd627bd94 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.2.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 8d76138a-8705-4a4f-bae0-b4dcedce56e7 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.1.2.2.2.3 - Completed Instances [Core]  <!-- UUID: 69483c09-487b-448e-aeda-06fbaa7eec4f -->

The Instances of the Root Edit Primitive with `Completed` Status are contained herein.

##### A.6.1.1.1.2.2.2.4 - In Progress Invocations [Core]  <!-- UUID: 0285add0-af7b-4026-a79b-0f6db72d8348 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.1.2.2.3 - Light Agent Primitive [Core]  <!-- UUID: 2ebe2537-74e6-476c-81a3-88a1abb76a6b -->

The documents herein contain all data and specifications for Spark’s Instances of the Light Agent Primitive. See [A.2.2.6.3 - Light Agent Primitive](44028423-2cd1-40cb-89ac-3f762b602b90).

##### A.6.1.1.1.2.2.3.1 - Primitive Hub Document [Core]  <!-- UUID: 35ba196a-9dee-45f2-8d9f-2aa48a4d2816 -->

The documents herein organize all base information relevant to Spark’s usage of the Light Agent Primitive.

###### A.6.1.1.1.2.2.3.1.1 - Global Activation Status [Core]  <!-- UUID: b050468a-8e2c-4143-b0a1-6cb170875143 -->

`Inactive`

###### A.6.1.1.1.2.2.3.1.2 - Active Instances Directory [Core]  <!-- UUID: c6c64d06-3533-491c-920c-5b58ee328a48 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.2.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 38fe6523-224d-4adf-9048-157879ca89a0 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.2.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 1fed54f6-a68b-4d70-a790-e3da5a1fb6f7 -->

This document contains a Directory of all prospective Instances of the Light Agent Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.2.3.1.2 - Active Instances Directory](c6c64d06-3533-491c-920c-5b58ee328a48), whereas failed Invocations are Archived in [A.6.1.1.1.2.2.3.1.5 - Hub Data Repository](aafad299-5a5d-48af-9e0f-519f2aee0f79).

###### A.6.1.1.1.2.2.3.1.5 - Hub Data Repository [Core]  <!-- UUID: aafad299-5a5d-48af-9e0f-519f2aee0f79 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.2.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 22c57270-fa9b-4bee-ab75-da8170e73eb4 -->

The subtrees for archived Invocations and Instances of the Light Agent Primitive are stored here.

###### A.6.1.1.1.2.2.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: d42821f2-4d0c-4b84-aace-e9f7c5c9d4b0 -->

The subtrees for failed Invocations of the Light Agent Primitive are stored here.

###### A.6.1.1.1.2.2.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: be668bea-0d71-46d7-98a5-455241823088 -->

The subtrees for Instances of the Light Agent Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.2.3.2 - Active Instances [Core]  <!-- UUID: 4c45583a-b948-4a1c-bd85-0adae4179761 -->

The Instances of the Light Agent Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.2.3.3 - Completed Instances [Core]  <!-- UUID: e001058f-bd04-45d0-b13a-53a8f3c66525 -->

The Instances of the Light Agent Primitive with `Completed` Status are contained herein.

##### A.6.1.1.1.2.2.3.4 - In Progress Invocations [Core]  <!-- UUID: ac5409c5-58d7-4e8a-b41a-49c7455cb42c -->

The in progress Invocations of the Light Agent Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.2.3.2 - Active Instances](4c45583a-b948-4a1c-bd85-0adae4179761).

### A.6.1.1.1.2.3 - Ecosystem Upkeep Primitives [Core]  <!-- UUID: 4547691b-3607-4b30-b7f1-4d04bfe3c912 -->

The documents herein implement the Ecosystem Upkeep Primitives for Spark. See [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

#### A.6.1.1.1.2.3.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: cc285753-1f2a-4a05-a9a9-e52da1168790 -->

The documents herein contain all data and specifications for Spark’s Instance of the Ecosystem Upkeep Fee Primitive. See [A.2.2.7.1 - Ecosystem Upkeep Fee Primitive](a21616f4-1611-4e0b-87b2-efbdff9f6f28).

##### A.6.1.1.1.2.3.1.1 - Primitive Hub Document [Core]  <!-- UUID: 4a0fea8a-d2e3-4ebd-8c3b-a5e27c74dac0 -->

The documents herein organize all base information relevant to Spark’s usage of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.1.2.3.1.1.1 - Global Activation Status [Core]  <!-- UUID: 66017146-97af-401a-92ae-9c1665e17492 -->

`Active`

###### A.6.1.1.1.2.3.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 93ce0ff1-a4c3-48e7-b147-cd27283fe307 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.3.1.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 44ef4e9c-5308-4cba-bf2a-e44951c67256 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.3.1.2.1 - Single Instance Configuration Document](0eff0bd2-25e6-4f13-8164-f4b41c9afe07).

###### A.6.1.1.1.2.3.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 49f65762-a90f-4096-aed2-ac913e3449ac -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.3.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 548b47ca-dc50-465c-b7ec-09805cc52af2 -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.1.2.3.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 48dd15d4-4cd4-4fb0-abe4-bccda146f08d -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.3.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ac8e9902-f252-4b84-bdd3-f5d255639e88 -->

The subtrees for archived Invocations and Instances of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.1.2.3.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: b9e2baa0-22cd-49f9-a3ed-65971ddb39ac -->

The subtrees for failed Invocations of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.1.2.3.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: b2aecba9-fdc6-41e9-ab42-3367effd17d9 -->

The subtrees for Instances of the Ecosystem Upkeep Fee Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.3.1.2 - Active Instances [Core]  <!-- UUID: 602f7677-417b-435a-96bd-eba64963c9e1 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Active` Status are stored herein.

###### A.6.1.1.1.2.3.1.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 0eff0bd2-25e6-4f13-8164-f4b41c9afe07 -->

The documents herein contain the Instance Configuration Document for the Single Ecosystem Upkeep Fee Primitive Instance.

###### A.6.1.1.1.2.3.1.2.1.1 - Parameters [Core]  <!-- UUID: eb1a5166-e3e1-4809-aa0b-77c985bd48c1 -->

The documents herein define the parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.1.2.3.1.2.1.1.1 - Terms [Core]  <!-- UUID: 0e1280e0-9781-4356-81f0-4540e06b380a -->

Spark will pay 0.50% of its market capitalization per year in USDS.

###### A.6.1.1.1.2.3.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 42b0e1c9-7b51-4cb7-865e-19911e4b8835 -->

The documents herein define the custom parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive, if any.

###### A.6.1.1.1.2.3.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: c8194db1-d94b-4bfc-8fc6-075f255a0fd9 -->

The documents herein define the process for the ongoing management of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.1.2.3.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 77c46d45-8fd7-4125-ae0a-ed6466e965d4 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.1.2.3.1.2.1.2.1.1 - Process Definition For Upkeep Fee Payment [Core]  <!-- UUID: 35af6171-70b6-4ccd-81ed-95b5548e8406 -->

The process to pay 0.50% of Spark’s market capitalization per year in USDS will be specified in future iterations of the Spark Artifact.

###### A.6.1.1.1.2.3.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: f6ea2cb2-ce88-4dda-aed1-8d2f4f0c9a97 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.1.2.3.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 14080c77-753f-4daa-ad7c-1b1ca203cb9a -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.1.2.3.1.2.1.3 - Data Repository [Core]  <!-- UUID: 928ae046-ac8d-47ff-a8c7-3b9abe2b9879 -->

The documents herein contain data relevant to the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.1.2.3.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: e6f23920-b611-41f2-8d80-97b0e79b7ca1 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.3.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: b8f8acf8-fbdc-47aa-9ff4-2e2fcee33815 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.3.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: aec8ac86-35d4-4ff7-a8c8-61a8056063b3 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.1.2.3.1.3 - Completed Instances [Core]  <!-- UUID: 9c60c0c9-19df-4cb1-afa8-2897932dafe5 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Completed` Status are stored herein.

##### A.6.1.1.1.2.3.1.4 - In Progress Invocations [Core]  <!-- UUID: f7b2e25f-fc99-4266-af87-f04239a97b1b -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.1.2.3.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: b39e05c8-cfcc-4671-b142-b691437cb98e -->

The documents herein contain all data and specifications for Spark’s Instance of the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

##### A.6.1.1.1.2.3.2.1 - Primitive Hub Document [Core]  <!-- UUID: 4b400b96-b0a3-4b7d-81b9-b22d4f12f16f -->

The documents herein organize all base information relevant to Spark’s usage of the Upkeep Rebate Primitive.

###### A.6.1.1.1.2.3.2.1.1 - Global Activation Status [Core]  <!-- UUID: d87daf19-7400-4a78-b7e8-4a5cb86f49d2 -->

`Active`

###### A.6.1.1.1.2.3.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 5f604d2e-2934-4347-b97a-3ab213e0b413 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.3.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 6cc8b26a-5b3c-49d6-9358-cbdbe9cb85cf -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.3.2.2.1 - Single Instance Configuration Document](64a12cf8-b7dc-4fd3-895b-bef979339bd1).

###### A.6.1.1.1.2.3.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 32779877-5fcb-49ff-b4c4-8246d8234a41 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.3.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: f13ef252-e2b3-4966-a554-279cae4f41ee -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.1.2.3.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 7dabf38f-5d1d-481b-bd96-eb3b2dcf8e8c -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.3.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 66af8a51-58a2-4a98-a510-4862bfb81cf6 -->

The subtrees for archived Invocations and Instances of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.1.2.3.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 0c53aaf7-ef3f-432a-bcac-c7c8c0e434b9 -->

The subtrees for failed Invocations of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.1.2.3.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: e1cf5c38-9e90-43c4-b133-faea5daf0ee5 -->

The subtrees for Instances of the Upkeep Rebate Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.3.2.2 - Active Instances [Core]  <!-- UUID: 507755d9-c459-475d-8099-63c0417f9335 -->

The Instances of the Upkeep Rebate Primitive with `Active` Status are stored herein.

###### A.6.1.1.1.2.3.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 64a12cf8-b7dc-4fd3-895b-bef979339bd1 -->

The documents herein contain the Instance Configuration Document for the Single Upkeep Rebate Primitive Instance.

###### A.6.1.1.1.2.3.2.2.1.1 - Parameters [Core]  <!-- UUID: c67462b5-3423-4323-b94b-f9e5270eda28 -->

Every Prime Agent is entitled to the Upkeep Rebate Primitive for tokens of other Prime Agents that they hold. Because this right automatically applies, there are no parameters.

###### A.6.1.1.1.2.3.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: bb605dda-ce85-46f2-8055-6d07d68b7214 -->

The documents herein define the process for the ongoing management of the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.1.2.3.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: b0882539-16b9-405f-9e7c-c98bdca1d8e7 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.1.2.3.2.2.1.2.1.1 - Spark Holds Tokens Of Other Agents In Its SubProxy Account [Core]  <!-- UUID: 9f9ad799-8c8d-43ad-a99e-24786f46dd40 -->

Spark keeps all tokens of other Agents it holds in its SubProxy account.

###### A.6.1.1.1.2.3.2.2.1.2.1.2 - Spark Deducts Rebate From Ecosystem Upkeep Fees [Core]  <!-- UUID: d14e7fce-217d-49bc-b0c3-c5305c17ea28 -->

When paying Ecosystem Upkeep fees, Spark deducts the rebate from the fees it pays.

###### A.6.1.1.1.2.3.2.2.1.2.1.3 - Operational GovOps Reviews Rebate [Core]  <!-- UUID: 93503e51-089a-4c63-a353-7c12574ea5b9 -->

Operational GovOps reviews Spark’s calculation of the rebate before executing a return of surplus to token holders. In the event of any issues, Operational GovOps cannot execute the distribution. If Operational GovOps does not execute the distribution, Operational GovOps must post an explanation on the Sky Forum under the "Spark Prime" category and work with Spark to resolve the disagreement. If Operational GovOps and Spark cannot resolve the disagreement, it must be escalated to Core GovOps.

###### A.6.1.1.1.2.3.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: a131e0d2-1946-4da2-b3a3-cfaace9d3978 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.1.2.3.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 03646635-39d9-4efb-9628-1f567cd2da99 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.1.2.3.2.2.1.3 - Data Repository [Core]  <!-- UUID: c0f8debb-8b20-428e-bdaa-8341c00fb0ee -->

The documents herein contain data relevant to the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.1.2.3.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 5bd30523-e635-41e2-9929-d458b0bc29db -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.3.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: be8f07a7-247f-466d-a68f-fd26fd84df9b -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.3.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 7997ed4f-6484-4aab-9b46-55b4db6e4e23 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.1.2.3.2.3 - Completed Instances [Core]  <!-- UUID: 29ea3609-b1d4-4488-9fa0-15e26dfd4c26 -->

The Instances of the Upkeep Rebate Primitive with `Completed` Status are contained herein.

##### A.6.1.1.1.2.3.2.4 - In Progress Invocations [Core]  <!-- UUID: 2008b69e-a0de-4274-b459-e2f613425a4b -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

### A.6.1.1.1.2.4 - SkyLink Primitives [Core]  <!-- UUID: bdb0c16b-8077-49c1-b925-bbc93884b04a -->

The documents herein implement the SkyLink Primitives for Spark. See [A.2.2.8 - SkyLink Primitives](7b5d8965-a64c-4c44-b742-607f51f69d8f).

#### A.6.1.1.1.2.4.1 - Token SkyLink Primitive [Core]  <!-- UUID: 148ada53-0815-49bc-a454-57bdf08a556e -->

The documents herein contain all data and specifications for Spark’s instances of the Token SkyLink Primitive. See [A.2.2.8.1 - Token SkyLink Primitive](4504d2d4-ee45-4a07-8c5b-9baf20b12e76).

##### A.6.1.1.1.2.4.1.1 - Primitive Hub Document [Core]  <!-- UUID: 88de14eb-6470-4980-add9-992726d6e006 -->

The documents herein organize all base information relevant to Spark’s usage of the Token SkyLink Primitive.

###### A.6.1.1.1.2.4.1.1.1 - Global Activation Status [Core]  <!-- UUID: e8b72d23-67b6-490e-9a3a-80953958e5b2 -->

`Active`

###### A.6.1.1.1.2.4.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 144380dc-5a6c-48e1-9004-12e0ca96ed10 -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.4.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 6be69464-0e1c-4f5f-9282-040f0a7b259b -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.4.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 25dbed2d-67a4-43c5-8877-189832337e68 -->

This document contains a Directory of all prospective Instances of the Token SkyLink Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.4.1.1.2 - Active Instances Directory](144380dc-5a6c-48e1-9004-12e0ca96ed10), whereas failed Invocations are Archived in [A.6.1.1.1.2.4.1.1.5 - Hub Data Repository](f2c09f57-213c-4157-b336-949924d2aa26).

###### A.6.1.1.1.2.4.1.1.5 - Hub Data Repository [Core]  <!-- UUID: f2c09f57-213c-4157-b336-949924d2aa26 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.4.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 8c6fc006-026d-48eb-8dfa-a06d3f6a3a92 -->

The subtrees for archived Invocations and Instances of the Token SkyLink Primitive are stored here.

###### A.6.1.1.1.2.4.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: d4257fc6-98a9-439b-a424-0d309efed41a -->

The subtrees for failed Invocations of the Token SkyLink Primitive are stored here.

###### A.6.1.1.1.2.4.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 7fc67d63-28aa-43c3-8a1d-36921f581df6 -->

The subtrees for Instances of the Token SkyLink Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.4.1.2 - Active Instances [Core]  <!-- UUID: 02016186-2953-489d-ae5d-aca30085c2b9 -->

The Instances of the Token SkyLink Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.4.1.3 - Completed Instances [Core]  <!-- UUID: dd1f8a40-8037-4cb6-961c-bb2448cbfc90 -->

The Instances of the Token SkyLink Primitive with `Completed` Status are stored herein.

##### A.6.1.1.1.2.4.1.4 - In Progress Invocations [Core]  <!-- UUID: 873c56da-485b-47cc-b926-08d62a471805 -->

The in progress Invocations of the Token SkyLink Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.4.1.2 - Active Instances](02016186-2953-489d-ae5d-aca30085c2b9).

### A.6.1.1.1.2.5 - Demand Side Stablecoin Primitives [Core]  <!-- UUID: 56116244-c569-4cb0-8399-eaae1ab36e97 -->

The documents herein implement the Demand Side Stablecoin Primitives for Spark. See [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d).

#### A.6.1.1.1.2.5.1 - Distribution Reward Primitive [Core]  <!-- UUID: 87916659-3b1e-4e65-8080-d6e1baab74e4 -->

The documents herein contain all data and specifications for Spark’s instances of the Distribution Reward Primitive. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

##### A.6.1.1.1.2.5.1.1 - Primitive Hub Document [Core]  <!-- UUID: 8dece7e0-529f-4522-9742-d883cc0939a7 -->

The documents herein organize all base information relevant to Spark’s usage of the Distribution Reward Primitive.

###### A.6.1.1.1.2.5.1.1.1 - Global Activation Status [Core]  <!-- UUID: b7f5818c-2c5c-4fda-aff0-58321cfbab35 -->

`Active`

###### A.6.1.1.1.2.5.1.1.2 - Active Instances Directory [Core]  <!-- UUID: fd278ccf-3054-4437-a052-ccb0291c3025 -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.5.1.1.2.1 - SparkLend Instance Configuration Document Location [Core]  <!-- UUID: 9537232d-674a-4821-b0ce-8ea5ce79b91e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.5.1.2.1 - SparkLend Instance Configuration Document](fd4059de-4a35-4147-a6ff-f7ecc88ceae6).

###### A.6.1.1.1.2.5.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7b60bfe0-3dbb-4a19-9c6c-88f0fdb9479b -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.5.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 798b67c4-749e-4d70-be25-7f7b9ff88268 -->

This document contains a Directory of all prospective Instances of the Distribution Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.5.1.1.2 - Active Instances Directory](fd278ccf-3054-4437-a052-ccb0291c3025), whereas failed Invocations are Archived in [A.6.1.1.1.2.5.1.1.5 - Hub Data Repository](fad965ad-63a7-4814-97db-bc1809dee69c).

###### A.6.1.1.1.2.5.1.1.5 - Hub Data Repository [Core]  <!-- UUID: fad965ad-63a7-4814-97db-bc1809dee69c -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.5.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 470664fd-8220-4745-8e5c-0fec350cc21f -->

The subtrees for archived Invocations and Instances of the Distribution Reward Primitive are stored here.

###### A.6.1.1.1.2.5.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 46ccaf77-f048-47fe-adfd-ef66fb0e2a93 -->

The subtrees for failed Invocations of the Distribution Reward Primitive are stored here.

###### A.6.1.1.1.2.5.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: d8edb5d5-2a21-46e0-a894-1cd452999763 -->

The subtrees for Instances of the Distribution Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.5.1.2 - Active Instances [Core]  <!-- UUID: 53a54bee-41b6-4135-9fa0-cf7876955a28 -->

The Instances of the Distribution Reward Primitive with `Active` Status are stored herein.

###### A.6.1.1.1.2.5.1.2.1 - SparkLend Instance Configuration Document [Core]  <!-- UUID: fd4059de-4a35-4147-a6ff-f7ecc88ceae6 -->

The documents herein contain the Instance Configuration Document for the SparkLend Distribution Reward Primitive Instance.

###### A.6.1.1.1.2.5.1.2.1.1 - Parameters [Core]  <!-- UUID: d737b3b2-f574-41e9-8ebc-3b828174f6fc -->

The documents herein define the parameters of the SparkLend Instance of the Distribution Reward Primitive.

###### A.6.1.1.1.2.5.1.2.1.1.1 - Reward Code [Core]  <!-- UUID: 1e5d71a8-5e79-40da-8b86-c07b3f341344 -->

`128`.

###### A.6.1.1.1.2.5.1.2.1.1.2 - Tracking Methodology [Core]  <!-- UUID: 101bce08-907e-442b-b6b3-754d3ad1455b -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.1.2.5.1.2.1.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 6c15d6b4-24b9-49e3-b7eb-c955c4a8d7cd -->

The documents herein define the custom parameters of the SparkLend Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.1.2.5.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 8dd6242a-e7ca-4cb9-bfd0-c0393886485f -->

The documents herein define the process for the ongoing management of the SparkLend Instance of the Distribution Reward Primitive.

###### A.6.1.1.1.2.5.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: a419b055-7d92-41b9-89f4-8f1fe082b814 -->

This document defines the protocol for routine ongoing management of the SparkLend Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Spark Artifact, a version of the full process definition customized to Spark will be included herein.

###### A.6.1.1.1.2.5.1.2.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: 620944c3-caa2-4c8c-823f-8ec08417221c -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.1.2.5.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 56404af1-c2ec-4bd5-876d-aa5db178ff40 -->

The documents herein define the protocol for non-routine ongoing management of the SparkLend Instance of this Distribution Reward Primitive.

###### A.6.1.1.1.2.5.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 221f522d-789e-418c-9d47-1d3c1bfcd803 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the SparkLend Instance of this Distribution Reward Primitive.

###### A.6.1.1.1.2.5.1.2.1.3 - Data Repository [Core]  <!-- UUID: cfe05f3a-5017-442a-998d-8b71ba3f6845 -->

The documents herein contain data relevant to the SparkLend Instance of the Distribution Reward Primitive.

###### A.6.1.1.1.2.5.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 09138ffc-9484-4a3a-b12a-d2fb2fc8f6ac -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.5.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: aaf76715-a3f3-4dc1-82d4-b10d7975f10b -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.5.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 41bffca2-7594-437c-84df-50827e8c001b -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.5.1.2.1.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 971d047b-4e7b-4545-9090-6d509e572aa0 -->

The Distribution Reward payments for the SparkLend Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.1.2.5.1.2.1.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 055fe10c-2d08-49a1-90c5-e124e2e0b4f9 -->

The Distribution Reward Payments are:

##### A.6.1.1.1.2.5.1.3 - Completed Instances [Core]  <!-- UUID: 6552c0fe-f9f7-4828-893b-cf278ce5161f -->

The Instances of the Distribution Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.1.2.5.1.4 - In Progress Invocations [Core]  <!-- UUID: 701a2dc3-bcfe-494e-8a4c-af18cfbffc54 -->

The in progress Invocations of the Distribution Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.5.1.2 - Active Instances](53a54bee-41b6-4135-9fa0-cf7876955a28).

#### A.6.1.1.1.2.5.2 - Integration Boost Primitive [Core]  <!-- UUID: e9f5a7e8-2260-484f-a725-871782a9bc01 -->

The documents herein contain all data and specifications for Spark’s Instances of the Integration Boost Primitive. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

##### A.6.1.1.1.2.5.2.1 - Primitive Hub Document [Core]  <!-- UUID: 8afae5a1-8734-4b98-bfd6-1dbe7842f146 -->

The documents herein organize all base information relevant to Spark’s usage of the Integration Boost Primitive.

###### A.6.1.1.1.2.5.2.1.1 - Global Activation Status [Core]  <!-- UUID: 305ab02d-23c0-45e7-9cc3-04122a339662 -->

`Active`

###### A.6.1.1.1.2.5.2.1.2 - Active Instances Directory [Core]  <!-- UUID: bb23a141-5119-4473-be3a-8f3c2a6f181a -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.5.2.1.2.1 - Aave Instance Configuration Document Location [Core]  <!-- UUID: c175e30d-5470-46b0-ad5f-433c3e934d1f -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.5.2.2.1 - Aave Instance Configuration Document](c88763c9-f2af-4d4e-81d5-6ea0dfdd05c5).

###### A.6.1.1.1.2.5.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 3c1fa1ea-752d-4438-aa3c-00634dcdb45a -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.5.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 786859ec-1f50-4343-8bed-82ef86781356 -->

This document contains a Directory of all prospective Instances of the Integration Boost Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.5.2.1.2 - Active Instances Directory](bb23a141-5119-4473-be3a-8f3c2a6f181a),; whereas failed Invocations are Archived in [A.6.1.1.1.2.5.2.1.5 - Hub Data Repository](469f9e75-4ac6-49d4-90d5-b6f3869d1fe8).

###### A.6.1.1.1.2.5.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 469f9e75-4ac6-49d4-90d5-b6f3869d1fe8 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.5.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 1a8018fb-c663-4e4b-9f4a-f08e1101ffe7 -->

The subtrees for archived Invocations and Instances of the Integration Boost Primitive are stored here.

###### A.6.1.1.1.2.5.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: a741a948-18c5-443c-a10e-d66f5f586363 -->

The subtrees for failed Invocations of the Integration Boost Primitive are stored here.

###### A.6.1.1.1.2.5.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: c5ec7cb4-18ed-4551-a1ea-dba32dfc2b80 -->

The subtrees for Instances of the Integration Boost Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.5.2.2 - Active Instances [Core]  <!-- UUID: 97e3a3e5-fa1c-4a33-8bb2-ae706201d1df -->

The Instances of the Integration Boost Primitive with `Active` Status are stored herein.

###### A.6.1.1.1.2.5.2.2.1 - Aave Instance Configuration Document [Core]  <!-- UUID: c88763c9-f2af-4d4e-81d5-6ea0dfdd05c5 -->

The documents herein contain the Instance Configuration Document for the Aave Integration Boost Primitive Instance.

###### A.6.1.1.1.2.5.2.2.1.1 - Parameters [Core]  <!-- UUID: a20ae261-ace1-4a64-b884-46d39d5a0c70 -->

The documents herein define the parameters of the Aave Instance of the Integration Boost Primitive.

###### A.6.1.1.1.2.5.2.2.1.1.1 - Integration Partner Name [Core]  <!-- UUID: 9508a55a-b9a9-492c-a6c8-c4374865ff24 -->

The partner for the Aave Integration Boost is Aave.

###### A.6.1.1.1.2.5.2.2.1.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: 5b5f88ff-8125-4103-8d00-2fd71052dabd -->

The reward address for the Aave Integration Boost is `0xac140648435d03f784879cd789130F22Ef588Fcd` on the Ethereum Mainnet.

###### A.6.1.1.1.2.5.2.2.1.1.3 - Integration Partner Chain [Core]  <!-- UUID: 7b41a7ac-e52d-4b5f-abbd-e7d5a9998195 -->

The Aave Integration Boost is on the Ethereum Mainnet.

###### A.6.1.1.1.2.5.2.2.1.1.4 - Integration Boost Cadence [Core]  <!-- UUID: a0d627a7-4284-4f2b-a919-5c2bae45a583 -->

The payment cadence for the Aave Integration Boost is weekly.

###### A.6.1.1.1.2.5.2.2.1.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: 6bbd42bc-d487-454a-82f6-9631a0830017 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/incentivized-pools/](https://info-sky.blockanalitica.com/api/v1/incentivized-pools/).

###### A.6.1.1.1.2.5.2.2.1.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: 0a654b1c-9dfe-4ddb-ab79-c3912d2a24bc -->

The Data Submission Responsible Actor is the Core Council Risk Advisor.

###### A.6.1.1.1.2.5.2.2.1.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: 41925f82-cd71-4abe-92ea-6ab5f660a23b -->

The Integration Boost is calculated based on per block values for USDS in Aave and the Sky Savings Rate.

###### A.6.1.1.1.2.5.2.2.1.1.8 - Custom Instance Parameters [Core]  <!-- UUID: c8b1fc3d-c3fa-4fac-8e2a-9b0cdd65dd35 -->

The documents herein define the custom parameters of the Aave Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.1.2.5.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 4cb1e983-4eb7-44de-b165-db352e6638c6 -->

The documents herein define the process for the ongoing management of the Aave Instance of the Integration Boost Primitive.

###### A.6.1.1.1.2.5.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 57fa2a62-f7d5-4926-b07a-50689a519942 -->

This document defines the protocol for routine ongoing management of the Aave Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.2.2.4 - Instance Ongoing Management Protocol](805381e5-89e7-4fb9-bda7-a97e84b531ba), subject to the qualifications specified in [A.2.2.9.2.2.1.3.2.1 - Near Term Process](4ab621b4-ef8e-4b01-a6aa-9296601033c5).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Spark Artifact, a version of the full process definition customized to Spark will be included herein.

###### A.6.1.1.1.2.5.2.2.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: c93f2fb8-89a5-4f17-8446-ed994a684b5a -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.1.2.5.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: b0601983-b6ad-44fb-abda-907a3fe53048 -->

The documents herein define the protocol for non-routine ongoing management of the Aave Instance of this Integration Boost Primitive.

###### A.6.1.1.1.2.5.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 66a730fa-47a9-4e2f-bc32-6f2c2de43b2f -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Aave Instance of this Integration Boost Primitive.

###### A.6.1.1.1.2.5.2.2.1.3 - Data Repository [Core]  <!-- UUID: 00e05f96-a641-4d12-b907-22be1f04d569 -->

The documents herein contain data relevant to the Aave Instance of the Integration Boost Primitive.

###### A.6.1.1.1.2.5.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 5a5c988e-6d19-4e82-9b27-ae0c0c02dd53 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.5.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 0628d063-99e1-4b59-a734-d2b07bee828f -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.5.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 6e4e9afb-cf23-4098-ae0b-1afcdc03e6c4 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.1.2.5.2.2.1.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: c3ca980e-56a7-42fc-a3f2-76516fb42088 -->

The Integration Boost payments for the Aave Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.1.2.5.2.2.1.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: 839e995c-cc05-40a7-ba31-a72bce152328 -->

The Integration Boost Payments are:

##### A.6.1.1.1.2.5.2.3 - Completed Instances [Core]  <!-- UUID: d492e503-1776-4956-a1ca-dbf604818400 -->

The Instances of the Integration Boost Primitive with `Completed` Status are contained herein.

##### A.6.1.1.1.2.5.2.4 - In Progress Invocations [Core]  <!-- UUID: f1427e80-b5a8-488b-b140-1685063efe39 -->

The in progress Invocations of the Integration Boost Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.5.2.2 - Active Instances](97e3a3e5-fa1c-4a33-8bb2-ae706201d1df).

#### A.6.1.1.1.2.5.3 - Pioneer Chain Primitive [Core]  <!-- UUID: 949247f8-c643-4f52-b0f1-cbf3c731da89 -->

The documents herein contain all data and specifications for Spark’s Instances of the Pioneer Chain Primitive. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).

##### A.6.1.1.1.2.5.3.1 - Primitive Hub Document [Core]  <!-- UUID: 0e476c6e-9dda-4366-9be6-d877df7356e3 -->

The documents herein organize all base information relevant to Spark’s usage of the Pioneer Chain Primitive.

###### A.6.1.1.1.2.5.3.1.1 - Global Activation Status [Core]  <!-- UUID: 697097a7-2c53-4e65-9543-4fa26c1f9e67 -->

`Inactive`

###### A.6.1.1.1.2.5.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 637d1fb7-4fe0-455b-b8c4-2a309fd01226 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.5.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: ed49aa25-b5e4-4a44-a897-c93d6764b099 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.5.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 4fed57e7-8850-4577-8138-c83065c337af -->

This document contains a Directory of all prospective Instances of the Pioneer Chain Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.5.3.1.2 - Active Instances Directory](637d1fb7-4fe0-455b-b8c4-2a309fd01226), whereas failed Invocations are Archived in [A.6.1.1.1.2.5.3.1.5 - Hub Data Repository](f941ecfc-13f1-40d6-b344-3e1d8d3f2321).

###### A.6.1.1.1.2.5.3.1.5 - Hub Data Repository [Core]  <!-- UUID: f941ecfc-13f1-40d6-b344-3e1d8d3f2321 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.5.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e49228b0-520d-4297-8a02-015238563397 -->

The subtrees for archived Invocations and Instances of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.1.2.5.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: bb2ed81d-87e3-4e90-8b83-b0e8b5596ccb -->

The subtrees for failed Invocations of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.1.2.5.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: f08e97af-9f90-4d0f-81b3-3d3bb23f8cbf -->

The subtrees for Instances of the Pioneer Chain Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.5.3.2 - Active Instances [Core]  <!-- UUID: 6dea3eb2-2f2d-4172-9026-6fd8f0226b1f -->

The Instances of the Pioneer Chain Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.5.3.3 - Completed Instances [Core]  <!-- UUID: 1bd7fe5c-0279-4184-b82e-e58d8f2c850e -->

The Instances of the Pioneer Chain Primitive with `Completed` Status are stored herein.

##### A.6.1.1.1.2.5.3.4 - In Progress Invocations [Core]  <!-- UUID: 3065c418-cfc5-4963-96ab-36cddfd66bea -->

The in progress Invocations of the Pioneer Chain Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.5.3.2 - Active Instances](6dea3eb2-2f2d-4172-9026-6fd8f0226b1f).

### A.6.1.1.1.2.6 - Supply Side Stablecoin Primitives [Core]  <!-- UUID: 683e3f9a-df0d-4bdb-adb4-f86dbc6530c6 -->

The documents herein implement the Supply Side Stablecoin Primitives for Spark. See [A.2.2.10 - Supply Side Stablecoin Primitives](d1142876-33c2-4e21-9339-d8711525d46f).

#### A.6.1.1.1.2.6.1 - Allocation System Primitive [Core]  <!-- UUID: cd70b9f1-1a59-407c-9945-05e52bf5a3b6 -->

The documents herein contain all data and specifications for Spark’s Allocation System Primitive Instances. Spark implements the Allocation System Primitive using the Spark Liquidity Layer. Developed prior to the introduction of the Sky Primitives, the Spark Liquidity Layer serves as the prototype for all Prime Agents’ Allocation Systems.

##### A.6.1.1.1.2.6.1.1 - Primitive Hub Document [Core]  <!-- UUID: 845ef31b-7b6e-4407-87ad-a5a4c8bce049 -->

The documents herein organize all base information relevant to Spark’s usage of the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.1.1 - Global Activation Status [Core]  <!-- UUID: f7a32d78-dabc-406e-a822-0a337a03b3e2 -->

`Active`

###### A.6.1.1.1.2.6.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 20e0bc23-8a73-4ea3-b626-56f6286aded9 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: e52dc682-bdab-4c3e-ae43-81666ff518e6 -->

The documents herein contain a Directory of all Instances on the Ethereum Mainnet of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.1.1.2.1.1 - SparkLend [Core]  <!-- UUID: c4a1d0ca-0794-4ad0-9920-7f8a837b6bfa -->

The Ethereum Mainnet Instances Directory of the SparkLend Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.1.1 - Ethereum Mainnet - SparkLend USDS Instance Configuration Document Location [Core]  <!-- UUID: fcb18db8-8a6a-4dfb-bfc9-f4b6e5f5a53a -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.1.1 - Ethereum Mainnet - SparkLend USDS Instance Configuration Document](4940f6ee-28e8-47a8-a7df-f2b30bd7dcc2).

###### A.6.1.1.1.2.6.1.1.2.1.1.2 - Ethereum Mainnet - SparkLend USDC Instance Configuration Document Location [Core]  <!-- UUID: c4d4ae3a-f133-41e2-a5e6-1ed61b8d273a -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.1.2 - Ethereum Mainnet - SparkLend USDC Instance Configuration Document](7cd0ec35-9449-48ce-a764-454ed33e72de).

###### A.6.1.1.1.2.6.1.1.2.1.1.3 - Ethereum Mainnet - SparkLend Dai Instance Configuration Document Location [Core]  <!-- UUID: b274ae84-b301-4935-b5d5-c3832d61f1b6 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.1.3 - Ethereum Mainnet - SparkLend Dai Instance Configuration Document](7e8135d5-7b45-48a7-bf9a-881f0bbf115c).

###### A.6.1.1.1.2.6.1.1.2.1.1.4 - Ethereum Mainnet - SparkLend USDT Instance Configuration Document Location [Core]  <!-- UUID: 2e0c5808-290a-4a39-ad87-ee4f7a7e457b -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.1.4 - Ethereum Mainnet - SparkLend USDT Instance Configuration Document](dbd8d0fc-d055-415c-a7ef-4796c5e33a87).

###### A.6.1.1.1.2.6.1.1.2.1.1.5 - Ethereum Mainnet - SparkLend pyUSD Instance Configuration Document Location [Core]  <!-- UUID: a98d046d-1cac-4987-a750-9b94137f7c91 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.1.5 - Ethereum Mainnet - SparkLend pyUSD Instance Configuration Document](84a0c43e-b64b-4018-bb2c-3d5c5a635c03).

###### A.6.1.1.1.2.6.1.1.2.1.1.6 - Ethereum Mainnet - SparkLend ETH Instance Configuration Document Location [Core]  <!-- UUID: baa53679-f8ba-4e8c-99dd-668638dd94b7 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.1.6 - Ethereum Mainnet - SparkLend ETH Instance Configuration Document](1eb4affe-3116-4d17-a3c1-0a06b6ac618b).

###### A.6.1.1.1.2.6.1.1.2.1.2 - Aave [Core]  <!-- UUID: b9745e5e-26bf-4abe-bff1-f3fdcfa93aca -->

The Ethereum Mainnet Instances Directory of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.2.1 - Ethereum Mainnet - Aave Prime USDS Instance Configuration Document Location [Core]  <!-- UUID: a1e31eab-caa2-4e20-8f55-49a23c5ce6e8 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.2.1 - Ethereum Mainnet - Aave Prime USDS Instance Configuration Document](bf8743ff-bd2e-4fb4-9b2f-2989f0361697).

###### A.6.1.1.1.2.6.1.1.2.1.2.2 - Ethereum Mainnet - Aave Core USDC Instance Configuration Document Location [Core]  <!-- UUID: 7b690555-9610-4a34-ba8f-90527894526a -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.2.2 - Ethereum Mainnet - Aave Core USDC Instance Configuration Document](bba861d8-9307-4e7f-ac54-f636232baff1).

###### A.6.1.1.1.2.6.1.1.2.1.2.3 - Ethereum Mainnet - Aave Core USDS Instance Configuration Document Location [Core]  <!-- UUID: fa291f5f-45bf-4798-b19f-90d5ab3ad593 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.2.3 - Ethereum Mainnet - Aave Core USDS Instance Configuration Document](1191f33a-dc78-4c2f-bc5e-e85802471c60).

###### A.6.1.1.1.2.6.1.1.2.1.2.4 - Ethereum Mainnet - Aave Core USDT Instance Configuration Document Location [Core]  <!-- UUID: 628a294b-ece9-4446-81db-e25c56ed02e4 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.2.4 - Ethereum Mainnet - Aave Core USDT Instance Configuration Document](c8bcfd26-cab2-43f6-9c35-ad13571fcf1e).

###### A.6.1.1.1.2.6.1.1.2.1.2.5 - Ethereum Mainnet - Aave USDe Instance Configuration Document Location [Core]  <!-- UUID: afea3002-f7b8-442e-a4f0-90bfd6c676f3 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.2.5 - Ethereum Mainnet - Aave USDe Instance Configuration Document](8bd798af-96fc-4fc4-9fb7-5b351740a962).

###### A.6.1.1.1.2.6.1.1.2.1.3 - Maple [Core]  <!-- UUID: 907ddd8e-0c22-4232-92d1-00144443c4fc -->

The Ethereum Mainnet Instances Directory of the Maple Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.3.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document Location [Core]  <!-- UUID: 12e43339-6c32-47ab-a2ec-43bb38f4f737 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.3.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document](06a83573-f319-4a56-a2bd-4389086dd2bf).

###### A.6.1.1.1.2.6.1.1.2.1.3.2 - Ethereum Mainnet - Maple USDT Instance Configuration Document Location [Core]  <!-- UUID: 46c72ef7-97f6-42c0-9d87-f28cff62bc97 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.3.2 - Ethereum Mainnet - Maple USDT Instance Configuration Document](5302863d-f777-461e-8238-2178fc9899c4).

###### A.6.1.1.1.2.6.1.1.2.1.4 - Ethena [Core]  <!-- UUID: 83f266b4-9b3b-44a2-a547-faa8c29a8833 -->

The Ethereum Mainnet Instances Directory of the Ethena Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.4.1 - Ethereum Mainnet - Ethena USDe Instance Configuration Document Location [Core]  <!-- UUID: b2bc23a2-2870-47ce-b32a-7b360b902782 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.4.1 - Ethereum Mainnet - Ethena USDe Instance Configuration Document](6be3e516-5374-41a0-8566-1c50656af772).

###### A.6.1.1.1.2.6.1.1.2.1.4.2 - Ethereum Mainnet - Ethena sUSDe Instance Configuration Document Location [Core]  <!-- UUID: 822350a5-27e8-4cb9-80c5-9fca9e84cb49 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.4.2 - Ethereum Mainnet - Ethena sUSDe Instance Configuration Document](1903250a-4499-4ce4-bdcb-5835102a6553).

###### A.6.1.1.1.2.6.1.1.2.1.5 - Fluid [Core]  <!-- UUID: c5e6035f-2712-4e64-a913-124b779605a4 -->

The Ethereum Mainnet Instances Directory of the Fluid Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.5.1 - Ethereum Mainnet - Fluid sUSDS ERC4626 Vault Instance Configuration Document Location [Core]  <!-- UUID: 2121074b-2a51-4330-952a-c05b628947cf -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.5.1 - Ethereum Mainnet - Fluid sUSDS ERC4626 Vault Instance Configuration Document](8da18a0c-2d5a-4895-ac53-804578b00a5b).

###### A.6.1.1.1.2.6.1.1.2.1.6 - Superstate [Core]  <!-- UUID: e502e83d-467d-4b58-a4bd-292a3985c7ff -->

The Ethereum Mainnet Instances Directory of the Superstate Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.6.1 - Ethereum Mainnet - Superstate USTB Instance Configuration Document Location [Core]  <!-- UUID: aed21e59-19b9-4b11-ac3f-55bb5a387772 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.6.1 - Ethereum Mainnet - Superstate USTB Instance Configuration Document](4ad2419c-7966-42de-bc2a-d8ca8ce61b90).

###### A.6.1.1.1.2.6.1.1.2.1.7 - Curve [Core]  <!-- UUID: d9cf6d6b-74a3-4bb6-b931-bfa3b5b8f70e -->

The Ethereum Mainnet Instances Directory of the Curve Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.7.1 - Ethereum Mainnet - Curve sUSDS/USDT Pool Instance Configuration Document Location [Core]  <!-- UUID: af6a87f7-9b67-4f30-a345-f0c46f97c039 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.7.1 - Ethereum Mainnet - Curve sUSDS/USDT Pool Instance Configuration Document](4e840dad-944c-4c45-9c5e-277dcb1830a8).

###### A.6.1.1.1.2.6.1.1.2.1.7.2 - Ethereum Mainnet - Curve USDC/USDT Pool Instance Configuration Document Location [Core]  <!-- UUID: dbbac28b-8627-462f-9326-f50bfdb50867 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.7.2 - Ethereum Mainnet - Curve USDC/USDT Pool Instance Configuration Document](30d359a0-287b-4b3b-93fd-4e70bf0b19a7).

###### A.6.1.1.1.2.6.1.1.2.1.7.3 - Ethereum Mainnet - Curve pyUSD/USDC Pool Instance Configuration Document Location [Core]  <!-- UUID: 7fe97dfc-8126-4c33-bc3d-74b7e1a1a88f -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.7.3 - Ethereum Mainnet - Curve pyUSD/USDC Pool Instance Configuration Document](e1fdaf49-0b32-4644-b021-9cae6e270c7a).

###### A.6.1.1.1.2.6.1.1.2.1.7.4 - Ethereum Mainnet - Curve pyUSD/USDS Pool Instance Configuration Document Location [Core]  <!-- UUID: 881d31bd-e24b-45f7-9f8a-fa18b8effc8d -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.7.4 - Ethereum Mainnet - Curve pyUSD/USDS Pool Instance Configuration Document](7635eff1-1fa0-4356-8953-2564a7f0693c).

###### A.6.1.1.1.2.6.1.1.2.1.7.5 - Ethereum Mainnet - Curve weETH/WETH-ng for Swaps Instance Configuration Document Location [Core]  <!-- UUID: 4ebb4393-9573-4e5f-9323-11770ba18191 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.7.5 - Ethereum Mainnet - Curve weETH/WETH-ng for Swaps Instance Configuration Document](cfc335a4-efcf-4f53-9609-1c9784cbb784).

###### A.6.1.1.1.2.6.1.1.2.1.7.6 - Ethereum Mainnet - Curve rlUSD/USDC for Swaps Instance Configuration Document Location [Core]  <!-- UUID: 5d2836d7-f633-4405-93b6-53d1c5734310 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.7.6 - Ethereum Mainnet - Curve rlUSD/USDC for Swaps Instance Configuration Document](3833eb97-f358-4019-9265-e4a45455ee0e).

###### A.6.1.1.1.2.6.1.1.2.1.8 - Morpho [Core]  <!-- UUID: 350d7312-0a09-43cd-bd31-265fda5a14a1 -->

The Ethereum Mainnet Instances Directory of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.8.1 - Ethereum Mainnet - Morpho Dai Instance Configuration Document Location [Core]  <!-- UUID: 3e92042e-1756-4c8f-a31d-6052176e87e5 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.8.1 - Ethereum Mainnet - Morpho Dai Instance Configuration Document](626dd4bf-108b-48bd-a1e1-c26d290c3a72).

###### A.6.1.1.1.2.6.1.1.2.1.8.2 - Ethereum Mainnet - Morpho USDS Instance Configuration Document Location [Core]  <!-- UUID: 79a60537-e5b6-4701-bde6-a98b33bca461 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.8.2 - Ethereum Mainnet - Morpho USDS Instance Configuration Document](138be894-8a4a-4e8c-9fdd-0f8183935d24).

###### A.6.1.1.1.2.6.1.1.2.1.8.3 - Ethereum Mainnet - Morpho USDC Instance Configuration Document Location [Core]  <!-- UUID: 3adb6bf9-e0f8-4583-996b-152bcdc1d51d -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.8.3 - Ethereum Mainnet - Morpho USDC Instance Configuration Document](f3063596-4f85-4a51-b52c-58221d043d3e).

###### A.6.1.1.1.2.6.1.1.2.1.8.4 - Ethereum Mainnet - Spark Blue Chip USDT Vault Instance Configuration Document Location [Core]  <!-- UUID: 35af6197-60c3-402d-a8dd-dafa8e30a24d -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.8.4 - Ethereum Mainnet - Spark Blue Chip USDT Vault Instance Configuration Document](2019122c-c16d-4132-ae08-8416c3f83b23).

###### A.6.1.1.1.2.6.1.1.2.1.9 - Spark Savings V2 [Core]  <!-- UUID: e59ca947-aa8d-4ab7-84b1-78422348a2d5 -->

The Ethereum Mainnet Instances Directory of the Spark Savings v2 with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.9.1 - Ethereum Mainnet - Spark Savings v2 ETH Instance Configuration Document Location [Core]  <!-- UUID: 2358e292-c9d1-4c23-9ef2-bb4a48304968 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.9.1 - Ethereum Mainnet - Spark Savings v2 ETH Instance Configuration Document](831b4fd8-06c6-4734-bb3a-93678082d8cc).

###### A.6.1.1.1.2.6.1.1.2.1.9.2 - Ethereum Mainnet - Spark Savings v2 USDC Instance Configuration Document Location [Core]  <!-- UUID: de15c2bf-cb03-45cc-9ee2-4acd1695ebc2 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.9.2 - Ethereum Mainnet - Spark Savings v2 USDC Instance Configuration Document](eeb34a6e-e377-4115-92f9-d299f6d2a5d9).

###### A.6.1.1.1.2.6.1.1.2.1.9.3 - Ethereum Mainnet - Spark Savings v2 USDT Instance Configuration Document Location [Core]  <!-- UUID: 113bbaa4-ac97-4ba7-9f31-20b8102b7a1a -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.9.3 - Ethereum Mainnet - Spark Savings v2 USDT Instance Configuration Document](0cc91e92-4523-4d3b-87a5-bb9a695d696c).

###### A.6.1.1.1.2.6.1.1.2.1.9.4 - Ethereum Mainnet - Spark Savings v2 PYUSD Instance Configuration Document Location [Core]  <!-- UUID: 3dabe1bb-244d-4546-993a-449b988d9199 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.9.4 - Ethereum Mainnet - Spark Savings v2 spPYUSD Instance Configuration Document](0b280652-ea99-4a53-8c9e-fb23b200d446).

###### A.6.1.1.1.2.6.1.1.2.1.10 - Arkis [Core]  <!-- UUID: 8e76f6f2-fb70-4ed0-a78d-7be94244819b -->

The Ethereum Instances Directory of the Arkis Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.10.1 - Ethereum Mainnet - Arkis Instance Configuration Document Location [Core]  <!-- UUID: a25915c0-0fc4-48f7-845b-92f446dbbba3 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.10.1 - Ethereum Mainnet - Arkis Instance Configuration Document](4bb58af1-fc25-442f-83a9-dd40989a7d37).

###### A.6.1.1.1.2.6.1.1.2.1.11 - Uniswap v4 [Core]  <!-- UUID: 4ef25928-26c1-4864-9670-88c5d676b8e4 -->

The Ethereum Mainnet Instances Directory of the Uniswap v4 with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.11.1 - Ethereum Mainnet - Uniswap v4 PYUSD/USDS Pool Instance Configuration Document Location [Core]  <!-- UUID: 5e1d4f42-84aa-4907-ad6f-eb62b26d28e3 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.11.1 - Ethereum Mainnet - Uniswap v4 PYUSD/USDS Pool Instance Configuration Document](c5d16727-69f7-454a-a3da-85c46dd9eed2).

###### A.6.1.1.1.2.6.1.1.2.1.11.2 - Ethereum Mainnet - Uniswap v4 USDT/USDS Pool Instance Configuration Document Location [Core]  <!-- UUID: 55e7dee1-dab9-4bc6-b8db-9aa8191597a1 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.11.2 - Ethereum Mainnet - Uniswap v4 USDT/USDS Pool Instance Configuration Document](3c4cfb29-1579-4abe-a17b-5b5574972b73).

###### A.6.1.1.1.2.6.1.1.2.1.11.3 - Ethereum Mainnet - Uniswap v4 USDG/USDS Pool Instance Configuration Document Location [Core]  <!-- UUID: 51abdb44-efb5-4b7d-b384-ee37fcd45ecd -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.11.3 - Ethereum Mainnet - Uniswap v4 USDG/USDS Pool Instance Configuration Document](8c92f153-c1bc-4c6a-afb3-97769f839a71).

###### A.6.1.1.1.2.6.1.1.2.1.11.4 - Ethereum Mainnet - Uniswap v4 rlUSD/USDS Pool Instance Configuration Document Location [Core]  <!-- UUID: 28d60d16-100f-42af-a3cf-4e1def7a2a35 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.11.4 - Ethereum Mainnet - Uniswap v4 rlUSD/USDS Pool Instance Configuration Document](102ef022-a660-4942-8bf2-bb061a7a8f8a).

###### A.6.1.1.1.2.6.1.1.2.1.12 - Paxos [Core]  <!-- UUID: c6e67244-8bdc-487a-b5bf-61025f623d22 -->

The Ethereum Mainnet Instances Directory of Paxos with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.12.1 - Ethereum Mainnet - USDC To PYUSD Via Paxos Instance Configuration Document Location [Core]  <!-- UUID: 65702dc0-78d3-4d0e-84bc-0d642fb42e73 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.12.1 - Ethereum Mainnet - USDC To PYUSD Via Paxos Instance Configuration Document](efc57615-b3ac-4122-8fd3-6a8d68ce71a1).

###### A.6.1.1.1.2.6.1.1.2.1.12.2 - Ethereum Mainnet - PYUSD To USDC Via Paxos Instance Configuration Document Location [Core]  <!-- UUID: 0a76cc35-3c37-421f-b123-e325cb581189 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.12.2 - Ethereum Mainnet - PYUSD To USDC Via Paxos Instance Configuration Document](28544284-0ee1-49da-a27f-b13dba9b5842).

###### A.6.1.1.1.2.6.1.1.2.1.12.3 - Ethereum Mainnet - PYUSD To USDG Via Paxos Instance Configuration Document Location [Core]  <!-- UUID: 5fdf2214-5345-4ca2-9fd6-b71981a438d9 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.12.3 - Ethereum Mainnet - PYUSD To USDG Via Paxos Instance Configuration Document](f6b739d1-c637-48f8-abf7-8c8f173bb392).

###### A.6.1.1.1.2.6.1.1.2.1.12.4 - Ethereum Mainnet - USDG To PYUSD Via Paxos Instance Configuration Document Location [Core]  <!-- UUID: 60055026-14c1-41ab-99ba-be28acbb4c1c -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.12.4 - Ethereum Mainnet - USDG To PYUSD Via Paxos Instance Configuration Document](bef47e5b-5568-4df4-9294-2eb108a006c6).

###### A.6.1.1.1.2.6.1.1.2.1.13 - Anchorage [Core]  <!-- UUID: 3e5b044d-1aeb-4664-bfb3-16fa613e0df7 -->

The Ethereum Mainnet Instances Directory of Anchorage with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.13.1 - Ethereum Mainnet - Anchorage USAT Instance Configuration Document Location [Core]  <!-- UUID: 0793bcc1-4b69-437d-bbf3-38e1ac6d29b6 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.13.1 - Ethereum Mainnet - Anchorage USAT Instance Configuration Document](8048e396-7bb4-4541-a68f-6dd7ec0a6015).

###### A.6.1.1.1.2.6.1.1.2.1.13.2 - Ethereum Mainnet - Anchorage USDT Instance Configuration Document Location [Core]  <!-- UUID: 905c5726-8d51-4bf3-80c7-2b4f48bf66cd -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.13.2 - Ethereum Mainnet - Anchorage USDT Instance Configuration Document](4eee15e5-46e2-4438-8299-6c85c46bb85b).

###### A.6.1.1.1.2.6.1.1.2.1.13.3 - Ethereum Mainnet - Anchorage USDC Instance Configuration Document Location [Core]  <!-- UUID: e93291ac-f9aa-41de-9d39-7d6ef95e54b0 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.13.3 - Ethereum Mainnet - Anchorage USDC Instance Configuration Document](efa4ea69-60de-4499-8ef0-86551373fa34).

###### A.6.1.1.1.2.6.1.1.2.1.14 - Binance [Core]  <!-- UUID: 7148129f-9198-42f6-af1d-b1c203d6c60a -->

The Ethereum Mainnet Instances Directory of Binance with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.1.14.1 - Ethereum Mainnet - Binance Transfer USDC to Binance (receive USDT) Instance Configuration Document Location [Core]  <!-- UUID: fddc6d87-9d31-4234-995d-08fac2f23ef9 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.14.1 - Ethereum Mainnet - Transfer USDC to Binance (receive USDT) Instance Configuration Document](ea00f585-11f4-4984-879e-22a6a0689a67).

###### A.6.1.1.1.2.6.1.1.2.1.14.2 - Ethereum Mainnet - Binance Transfer USDT to Binance (receive USDC) Instance Configuration Document Location [Core]  <!-- UUID: 9b9d6744-b3b4-4cc8-9649-ae60a8db20a6 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.1.14.2 - Ethereum Mainnet - Transfer USDT to Binance (receive USDC) Instance Configuration Document](47a2b1c2-104c-4bb4-bb10-574cab86daf5).

###### A.6.1.1.1.2.6.1.1.2.2 - Base [Core]  <!-- UUID: 305a6351-bb16-4e4d-8912-7ef1c3ff26bb -->

The documents herein contain a Directory of all Instances on Base of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.1.1.2.2.1 - Morpho [Core]  <!-- UUID: 368907a1-0c9f-43b9-98dc-8132ef38b450 -->

The Base Instances Directory of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.2.1.1 - Base - Morpho Blue USDC ERC4626 Vault Instance Configuration Document Location [Core]  <!-- UUID: dbd3aa7c-2a3d-4a2e-be5d-5d25a5d9dd8e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.2.1.1 - Base - Morpho Blue USDC ERC4626 Vault Instance Configuration Document](97c54a67-ff3d-40c3-a702-f632f2b81f2d).

###### A.6.1.1.1.2.6.1.1.2.2.2 - Fluid [Core]  <!-- UUID: aaabd71c-637f-4680-841f-6a00db261095 -->

The Base Instances Directory of the Fluid Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.2.2.1 - Base - Fluid sUSDS ERC4626 Vault Instance Configuration Document Location [Core]  <!-- UUID: cb87926d-f011-47ff-a0ab-81a057016ed6 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.2.2.1 - Base Mainnet - Fluid sUSDS ERC4626 Vault Instance Configuration Document](b955e881-1ad7-479f-9858-efebe8e23bdc).

###### A.6.1.1.1.2.6.1.1.2.2.3 - Aave [Core]  <!-- UUID: 51cc6fa3-1e1a-4f07-bbad-c54ba6645e71 -->

The Base Instances Directory of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.2.3.1 - Base - Aave USDC Instance Configuration Document Location [Core]  <!-- UUID: a61290d6-caae-4cb2-a2bc-8fc99ec2d7e6 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.2.3.1 - Base - Aave USDC Instance Configuration Document](adfe1844-38ae-4eac-9060-f79978751765).

###### A.6.1.1.1.2.6.1.1.2.3 - Arbitrum [Core]  <!-- UUID: 9e3cf2d4-99b5-4b25-a552-1eb8becef4ae -->

The documents herein contain a Directory of all Instances on Arbitrum of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.1.1.2.3.1 - Fluid [Core]  <!-- UUID: 78bfa934-14f8-45eb-aec1-945d4e262dd7 -->

The Arbitrum Instances Directory of the Fluid Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.3.1.1 - Arbitrum - Fluid sUSDS ERC4626 Vault Instance Configuration Document Location [Core]  <!-- UUID: e49ce8a1-1e28-4fcf-a991-589d604fb12e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.3.1.1 - Arbitrum - Fluid sUSDS ERC4626 Vault Instance Configuration Document](e6a55c76-91f7-4503-9349-b082c762ec76).

###### A.6.1.1.1.2.6.1.1.2.3.2 - Aave [Core]  <!-- UUID: 7e0e5a2d-0dd8-4184-9eea-c8ef4284cbcb -->

The Arbitrum Instances Directory of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.2.3.2.1 - Arbitrum - Aave USDC Instance Configuration Document Location [Core]  <!-- UUID: 6a9a6b83-5337-4f61-b01c-757809bd90b9 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.3.2.1 - Arbitrum - Aave USDC Instance Configuration Document](e11091aa-e569-4ca9-9151-dc5e1a8e1062).

###### A.6.1.1.1.2.6.1.1.2.4 - Avalanche [Core]  <!-- UUID: 4f0c9316-383c-464f-8266-d6c7a6f5ef08 -->

The documents herein contain a Directory of all Instances on Avalanche of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.1.1.2.4.1 - Aave [Core]  <!-- UUID: 830b9c54-37df-41f1-9ae1-e114bc47636c -->

The Avalanche Instances Directory of the Aave Protocol with `Completed` Status are stored herein

###### A.6.1.1.1.2.6.1.1.2.4.1.1 - Avalanche - Aave v3 USDC Vault Instance Configuration Document Location [Core]  <!-- UUID: 85bc9184-abf0-4767-ae07-cda159c63f6f -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.4.1.1 - Avalanche - Aave v3 USDC Vault Instance Configuration Document](ae06054a-1ed8-410b-983d-1789b49f1f19).

###### A.6.1.1.1.2.6.1.1.2.4.2 - Spark Savings V2 [Core]  <!-- UUID: 805d95ac-c6fa-4326-bade-380c3635306c -->

The Avalanche Instances Directory of the Spark Savings v2 Protocol with `Active` Status are stored herein

###### A.6.1.1.1.2.6.1.1.2.4.2.1 - Avalanche - Spark Savings v2 USDC Instance Configuration Document Location [Core]  <!-- UUID: 82ccfe21-2172-41cc-b845-231ed61b101d -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.4.2.1 - Avalanche - Spark Savings v2 USDC Instance Configuration Document](afa35a43-18e2-4084-b36c-eb584f4749ac)

###### A.6.1.1.1.2.6.1.1.2.5 - Robinhood Chain [Core]  <!-- UUID: f3ced164-396f-4014-ae27-e2ce7303a3b4 -->

The documents herein contain a Directory of all Instances on Robinhood Chain of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.1.1.2.5.1 - Spark Savings V2 [Core]  <!-- UUID: d0cbb95a-5115-4a9a-a67e-cc00172beef5 -->

The Robinhood Chain Instances Directory of the Spark Savings v2 Protocol with `Active` Status are stored herein

###### A.6.1.1.1.2.6.1.1.2.5.1.1 - Robinhood Chain - Spark Savings v2 USDG Instance Configuration Document Location [Core]  <!-- UUID: 8c634d61-3959-473d-8dea-f1a015e7650a -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.5.1.1 - Robinhood Chain - Spark Savings v2 USDG Instance Configuration Document](87c1f6a7-8af8-4350-b43e-f63bc3287a1f)

###### A.6.1.1.1.2.6.1.1.2.6 - X Layer [Core]  <!-- UUID: 5d3e7362-9f38-49a1-8150-28c5f81228eb -->

The documents herein contain a Directory of all Instances on X Layer of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.1.1.2.6.1 - Spark Savings V2 [Core]  <!-- UUID: 70c70fa9-9cb4-4bcf-a62f-b815a90981c3 -->

The X Layer Instances Directory of the Spark Savings v2 Protocol with `Active` Status are stored herein

###### A.6.1.1.1.2.6.1.1.2.6.1.1 - X Layer - Spark Savings v2 USDT Instance Configuration Document Location [Core]  <!-- UUID: 9c5abebd-6cfe-407c-9cda-5a397dd54ee8 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.3.6.1.1 - X Layer - Spark Savings v2 USDT Instance Configuration Document](8c303f01-617d-40aa-9f4f-181af2c6e040)

###### A.6.1.1.1.2.6.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 1df4d054-4443-4c64-b34b-c9fce456276b -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.6.1.1.3.1 - Blackrock [Core]  <!-- UUID: e4ec840c-dee5-4afe-9f41-c9061c70a0d9 -->

The Ethereum Mainnet Instances Directory of the Blackrock Protocol with `Completed` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.3.1.1 - Ethereum Mainnet - Blackrock USDC Instance Configuration Document Location [Core]  <!-- UUID: 6d30c514-ea40-45ca-93cd-0771830b3617 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.4.1.1 - Ethereum Mainnet - Blackrock USDC Instance Configuration Document](7a52fb87-96bf-4135-9a61-f2dc068af12c).

###### A.6.1.1.1.2.6.1.1.3.2 - Centrifuge [Core]  <!-- UUID: 5e56bd40-1e89-4549-adaa-54776089fe13 -->

The Ethereum Mainnet Instances Directory of the Centrifuge Protocol with `Completed` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.3.2.1 - Ethereum Mainnet - Centrifuge USDC Instance Configuration Document Location [Core]  <!-- UUID: 495b8996-fd2c-46ba-8e46-945b22eff733 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.4.2.1 - Ethereum Mainnet - Centrifuge USDC Instance Configuration Document](289555ee-996e-43a7-b05f-a0b06d1238f5).

###### A.6.1.1.1.2.6.1.1.3.3 - Ethereum Mainnet [Core]  <!-- UUID: 04b9c9b0-0a49-4149-9a29-92d8192ae5c2 -->

The documents herein contain a Directory of all Instances on the Ethereum Mainnet of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.6.1.1.3.3.1 - Morpho [Core]  <!-- UUID: 023da344-8767-4175-bb06-953747c383a7 -->

The Ethereum Mainnet Instances Directory of the Morpho Protocol with `Completed` Status are stored herein.

###### A.6.1.1.1.2.6.1.1.3.3.1.1 - Ethereum Mainnet - Morpho USDT Instance Configuration Document Location [Core]  <!-- UUID: 5b70027d-bea1-4899-946f-6a2094a8ca55 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.1.2.6.1.4.3.1.1 - Ethereum Mainnet - Morpho USDT Instance Configuration Document](a2f66f86-ddea-4260-820a-cde66a861413).

###### A.6.1.1.1.2.6.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 73a22cb8-06cd-4324-b0fe-f37bf538f7a9 -->

This document contains a Directory of all prospective Instances of the Allocation System Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.6.1.1.2 - Active Instances Directory](20e0bc23-8a73-4ea3-b626-56f6286aded9), whereas failed Invocations are Archived in [A.6.1.1.1.2.6.1.1.5 - Hub Data Repository](143d1560-f068-4f83-9b50-c5e80fc9ec21).

###### A.6.1.1.1.2.6.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 143d1560-f068-4f83-9b50-c5e80fc9ec21 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.6.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e0c8e24c-9b21-4281-8ea7-dfbb2bbdeb15 -->

The subtrees for archived Invocations and Instances of the Allocation System Primitive are stored here.

###### A.6.1.1.1.2.6.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 63b469da-4eb4-48b9-8b91-83edcc819dd9 -->

The subtrees for failed Invocations of the Allocation System Primitive are stored here.

###### A.6.1.1.1.2.6.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 6506b603-5723-4b1c-b82c-25ed31ac429a -->

The subtrees for Instances of the Allocation System Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.6.1.2 - Multi-Instance Coordinator Document [Core]  <!-- UUID: e4ba3491-5b24-49b0-91f1-c9ad9438b190 -->

The documents herein provide general specifications of the Spark Liquidity Layer and define Spark’s overarching strategy and operational framework for managing across all Instances.

###### A.6.1.1.1.2.6.1.2.1 - General Specifications [Core]  <!-- UUID: 137b4d21-d68c-4cdd-9f7f-58b9a28bb048 -->

The documents herein contain general specifications for the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.2.1.1 - Spark Liquidity Layer Architecture [Core]  <!-- UUID: e9d83462-27f2-4bc0-a63a-596dd7c517b4 -->

The documents herein describe the high-level design of the Spark Liquidity Layer, including its key smart contracts and their functionality.

###### A.6.1.1.1.2.6.1.2.1.1.1 - Spark Liquidity Layer Addresses [Core]  <!-- UUID: f3885398-6641-437b-a413-276ac48e624a -->

The subdocuments herein provide the addresses of the Spark Liquidity Layer’s constituent contracts.

###### A.6.1.1.1.2.6.1.2.1.1.1.1 - Allocator Contract Addresses [Core]  <!-- UUID: fd4ca647-2eb2-403c-975b-4da0601bffba -->

The documents herein contain global key addresses for the Allocator Contracts.

###### A.6.1.1.1.2.6.1.2.1.1.1.1.1 - Allocator Buffer Contract [Core]  <!-- UUID: 86a5b9c5-8d49-4538-9995-c8c1200f5942 -->

The address of the ALLOCATOR_BUFFER contract is: `0xc395D150e71378B47A1b8E9de0c1a83b75a08324`

###### A.6.1.1.1.2.6.1.2.1.1.1.1.2 - Allocator Oracle Contract [Core]  <!-- UUID: fcad0844-97d7-429b-b4bf-8ba4c657a0fc -->

The address of the ALLOCATOR_ORACLE contract is: `0xc7B91C401C02B73CBdF424dFaaa60950d5040dB7`

###### A.6.1.1.1.2.6.1.2.1.1.1.1.3 - Allocator Registry Contract [Core]  <!-- UUID: 6936b2a0-5933-4550-88eb-ee87c9227d8e -->

The address of the ALLOCATOR_REGISTRY contract is: `0xCdCFA95343DA7821fdD01dc4d0AeDA958051bB3B`

###### A.6.1.1.1.2.6.1.2.1.1.1.1.4 - Allocator Roles Contract [Core]  <!-- UUID: b64d1f0a-3c6d-48af-bb79-0504e4e58a88 -->

The address of the ALLOCATOR_ROLES contract is: `0x9A865A710399cea85dbD9144b7a09C889e94E803`

###### A.6.1.1.1.2.6.1.2.1.1.1.1.5 - Allocator Vault (Spark-A) Contract [Core]  <!-- UUID: a9b28dbc-1993-43ba-9b24-dcca91f08f14 -->

The address of the ALLOCATOR_VAULT (ALLOCATOR-SPARK-A) contract is: `0x691a6c29e9e96dd897718305427Ad5D534db16BA`

###### A.6.1.1.1.2.6.1.2.1.1.1.2 - ALM Contracts [Core]  <!-- UUID: 7db865de-8519-464b-8752-f39ecaf54fd2 -->

The documents herein contain addresses for the ALM Contracts for the Spark Liquidity Layer on each blockchain.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: 834b9f4a-a39f-4b1f-95d9-d841fabfa7a2 -->

The documents herein contain the ALM Contract Addresses for the Spark Liquidity Layer on the Ethereum Mainnet.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1.1 - ALM Controller (MainnetController) Contract Address [Core]  <!-- UUID: 3546c2d3-7b7c-4446-aa16-ff357c1a7a0f -->

The address of the ALM_CONTROLLER (MainnetController) contract is: `0x577Fa18a498e1775939b668B0224A5e5a1e56fc3`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1.2 - ALM Controller (MainnetController) Contract Version [Core]  <!-- UUID: d7b0b6a0-0bac-4169-a006-4a375cba4baa -->

The ALM_CONTROLLER (MainnetController) contract version is: 1.10

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1.3 - ALM Freezer Multisig (Mainnet) Address [Core]  <!-- UUID: 8d6c5c86-4b70-4115-b712-65106416aa77 -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.1.2.6.1.2.1.2.2.3.1 - Address](51777bdd-df5f-4a6e-93f5-8163d981f595).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1.4 - ALM Relayer Multisig (Mainnet) Address [Core]  <!-- UUID: f8958f39-6893-471a-bfd0-f72cb0aa0e4c -->

The address of the Multisigs that has the Relayer Role are specified in [A.6.1.1.1.2.6.1.2.1.2.2.1.1 - Address](67bf2799-8d57-44be-82e4-827912ff30df) and [A.6.1.1.1.2.6.1.2.1.2.2.2.1 - Address](567e4905-2b05-493e-95ac-8a4d20afed2b).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1.5 - ALM Proxy (Mainnet) Contract [Core]  <!-- UUID: a29a6751-4809-446c-a659-0dd93ca40379 -->

The address of the ALM_PROXY contract is: `0x1601843c5E9bC251A3272907010AFa41Fa18347E`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1.6 - ALM Rate Limits (Mainnet) Contract Address [Core]  <!-- UUID: 3d7c06c5-18ab-4c30-82f1-4de153e2bc76 -->

The address of the ALM_RATE_LIMITS contract is: `0x7A5FD5cf045e010e62147F065cEAe59e5344b188`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1.7 - ALM Proxy Freezable (Mainnet) Contract Address [Core]  <!-- UUID: a937f2e1-5f17-4c60-b007-fef5a7f00f5b -->

The address of the ALM_PROXY_FREEZABLE contract is: `0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.1.8 - ALM Proxy Freezable (Mainnet) Contract Version [Core]  <!-- UUID: 5879057d-df2d-4f23-8927-9c6e5160edd2 -->

The version of the ALM_PROXY_FREEZABLE contract is: 1.1

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2 - Base [Core]  <!-- UUID: 339e27da-297e-458f-8420-546e085a51dd -->

The documents herein list the ALM Contract Addresses for the Spark Liquidity Layer on Base.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2.1 - ALM Controller (ForeignController Base) Contract Address [Core]  <!-- UUID: eaa1d582-a814-49ef-a3ec-3fbffa414a3a -->

The address of the ALM_CONTROLLER (ForeignController) contract is: `0xC0bcbb2554D4694fe7b34bB68b9DdfbB55D896BC`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2.2 - ALM Controller (ForeignController Base) Contract Version Address [Core]  <!-- UUID: 2f264586-051d-4944-9c15-c271a2a8a0b5 -->

The ALM_CONTROLLER (ForeignController) contract version is: 1.8

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2.3 - ALM Freezer Multisig (Base) Address [Core]  <!-- UUID: 5147079e-3ff5-44c5-8039-5b1d3895ceec -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.1.2.6.1.2.1.2.2.3.1 - Address](51777bdd-df5f-4a6e-93f5-8163d981f595).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2.4 - ALM Relayer Multisig (Base) Address [Core]  <!-- UUID: 0d92d953-ce09-4f3a-a788-2f1dc7b190ed -->

The address of the Multisigs that has the Relayer Role are specified in [A.6.1.1.1.2.6.1.2.1.2.2.1.1 - Address](67bf2799-8d57-44be-82e4-827912ff30df) and [A.6.1.1.1.2.6.1.2.1.2.2.2.1 - Address](567e4905-2b05-493e-95ac-8a4d20afed2b).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2.5 - ALM Proxy (Base) Contract [Core]  <!-- UUID: 425339ce-8e44-430b-ab8c-6c69f0b757e9 -->

The address of the ALM_PROXY contract is: `0x2917956eFF0B5eaF030abDB4EF4296DF775009cA`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2.6 - ALM Rate Limits (Base) Contract [Core]  <!-- UUID: 576b33fc-ee31-40a4-8a04-2b6c0e618a58 -->

The address of the ALM_RATE_LIMITS contract is: `0x983eC82E45C61a42FDDA7B3c43B8C767004c8A74`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2.7 - ALM Proxy Freezable (Base) Contract Address [Core]  <!-- UUID: ab85b80b-096b-438d-ad9a-c4ece54274a8 -->

The address of the ALM_PROXY_FREEZABLE contract is: `0xCBA0C0a2a0B6Bb11233ec4EA85C5bFfea33e724d`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.2.8 - ALM Proxy Freezable (Base) Contract Version [Core]  <!-- UUID: 68dd49b4-4d08-4a4d-a0b2-a294526ca30c -->

The version of the ALM_PROXY_FREEZABLE contract is: 1.1

###### A.6.1.1.1.2.6.1.2.1.1.1.2.3 - Arbitrum [Core]  <!-- UUID: de02348b-d300-4b85-b7f9-5546106c5191 -->

This document contains the ALM Contract Addresses for the Spark Liquidity Layer on Arbitrum.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.3.1 - ALM Controller (ForeignController Arbitrum) Contract Address [Core]  <!-- UUID: 60979099-707d-497d-ad65-4fd6dd6c7cb0 -->

The address of the ALM_CONTROLLER (ForeignController) contract is:
TBC

###### A.6.1.1.1.2.6.1.2.1.1.1.2.3.2 - ALM Controller (ForeignController Arbitrum) Contract Version [Core]  <!-- UUID: ea182fbb-586b-4df2-ac03-ea8291702649 -->

The ALM_CONTROLLER (ForeignController) contract version is: 1.8

###### A.6.1.1.1.2.6.1.2.1.1.1.2.3.3 - ALM Freezer Multisig (Arbitrum) Address [Core]  <!-- UUID: 294230e0-d7f9-43c5-9f38-d19074b61d47 -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.1.2.6.1.2.1.2.2.3.1 - Address](51777bdd-df5f-4a6e-93f5-8163d981f595).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.3.4 - ALM Relayer Multisig (Arbitrum) Address [Core]  <!-- UUID: d9bbc9dc-a8e9-413c-83ee-b6d1d3a2c2ec -->

The address of the Multisigs that has the Relayer Role are specified in [A.6.1.1.1.2.6.1.2.1.2.2.1.1 - Address](67bf2799-8d57-44be-82e4-827912ff30df) and [A.6.1.1.1.2.6.1.2.1.2.2.2.1 - Address](567e4905-2b05-493e-95ac-8a4d20afed2b).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.3.5 - ALM Proxy (Arbitrum) Contract [Core]  <!-- UUID: c671b407-fcb2-48eb-8217-2ec156b581ad -->

The address of the ALM_PROXY contract is: `0x92afd6F2385a90e44da3a8B60fe36f6cBe1D8709`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.3.6 - ALM Rate Limits (Arbitrum) Contract [Core]  <!-- UUID: 83f8da05-267e-4dd7-beaa-7561c9b8c5c1 -->

The address of the ALM_RATE_LIMITS contract is: `0x19D08879851FB54C2dCc4bb32b5a1EA5E9Ad6838`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.4 - Unichain [Core]  <!-- UUID: 6cd31b91-4309-49ae-8d23-2486129f3b20 -->

This document contains the ALM Contract Addresses for the Spark Liquidity Layer on Unichain.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.4.1 - ALM Controller (ForeignController Unichain) Contract Address [Core]  <!-- UUID: bcc685eb-d28c-4306-8b78-5639b1d31f6b -->

The address of the ALM_CONTROLLER (ForeignController) contract is: TBC

###### A.6.1.1.1.2.6.1.2.1.1.1.2.4.2 - ALM Controller (ForeignController Unichain) Contract Version [Core]  <!-- UUID: 17ff233f-2ada-4856-be5f-f3ba2616c1b7 -->

The ALM_CONTROLLER (ForeignController) contract version is: 1.8

###### A.6.1.1.1.2.6.1.2.1.1.1.2.4.3 - ALM Freezer Multisig (Unichain) Address [Core]  <!-- UUID: 23bb04f0-d312-4230-930d-27782b73b04f -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.1.2.6.1.2.1.2.2.3.1 - Address](51777bdd-df5f-4a6e-93f5-8163d981f595).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.4.4 - ALM Relayer Multisig (Unichain) Address [Core]  <!-- UUID: 351fc37c-0567-4fbc-bae0-975427192f29 -->

The address of the Multisigs that has the Relayer Role are specified in [A.6.1.1.1.2.6.1.2.1.2.2.1.1 - Address](67bf2799-8d57-44be-82e4-827912ff30df) and [A.6.1.1.1.2.6.1.2.1.2.2.2.1 - Address](567e4905-2b05-493e-95ac-8a4d20afed2b).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.4.5 - ALM Proxy (Unichain) Contract [Core]  <!-- UUID: 6affe08d-0c1c-4cbf-a100-4a04c58220bb -->

The address of the ALM_PROXY contract is: `0x345E368fcCd62266B3f5F37C9a131FD1c39f5869`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.4.6 - ALM Rate Limits (Unichain) Contract [Core]  <!-- UUID: 422a99bd-357f-4c48-882b-2608e0526282 -->

The address of the ALM_RATE_LIMITS contract is: `0x5A1a44D2192Dd1e21efB9caA50E32D0716b35535`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.5 - Optimism [Core]  <!-- UUID: 2c97bd03-ef58-411f-b2cc-1db6d8396d95 -->

This document contains the ALM Contract Addresses for the Spark Liquidity Layer on Optimism.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.5.1 - ALM Controller (ForeignController Optimism) Contract Address [Core]  <!-- UUID: 1eaa9220-d5e2-44f2-83eb-232add8f04ff -->

The address of the ALM_CONTROLLER (ForeignController) contract is: TBC

###### A.6.1.1.1.2.6.1.2.1.1.1.2.5.2 - ALM Controller (ForeignController Optimism) Contract Version [Core]  <!-- UUID: 715c19b6-63bc-4eae-b8a4-0327e9a10c71 -->

The ALM_CONTROLLER (ForeignController) contract version is: 1.8

###### A.6.1.1.1.2.6.1.2.1.1.1.2.5.3 - ALM Freezer Multisig (Optimism) Address [Core]  <!-- UUID: a4cb2345-64a9-4e1f-b084-c25f6df7082a -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.1.2.6.1.2.1.2.2.3.1 - Address](51777bdd-df5f-4a6e-93f5-8163d981f595).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.5.4 - ALM Relayer Multisig (Optimism) Address [Core]  <!-- UUID: 1ce78bd7-1a4f-4389-b4dc-f2f7ab9e2b33 -->

The address of the Multisigs that has the Relayer Role are specified in [A.6.1.1.1.2.6.1.2.1.2.2.1.1 - Address](67bf2799-8d57-44be-82e4-827912ff30df) and [A.6.1.1.1.2.6.1.2.1.2.2.2.1 - Address](567e4905-2b05-493e-95ac-8a4d20afed2b).

###### A.6.1.1.1.2.6.1.2.1.1.1.2.5.5 - ALM Proxy (Optimism) Contract [Core]  <!-- UUID: f1895dfc-a18c-4009-bfd3-1c16c9a62092 -->

The address of the ALM_PROXY contract is: `0x876664f0c9Ff24D1aa355Ce9f1680AE1A5bf36fB`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.5.6 - ALM Rate Limits (Optimism) Contract [Core]  <!-- UUID: 71eaf0a6-1d32-4b8c-b55f-c56c9af11634 -->

The address of the ALM_RATE_LIMITS contract is: `0x6B34A6B84444dC3Fc692821D5d077a1e4927342d`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6 - Avalanche [Core]  <!-- UUID: 4299d551-8954-4290-acb8-e97b501f8f08 -->

This document contains the ALM Contract Addresses for the Spark Liquidity Layer on Avalanche.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.1 - ALM Controller (ForeignController Avalanche) Contract Address [Core]  <!-- UUID: 2a9bf1bb-81f7-40d2-a26d-2cc7e729913f -->

The address of the ALM_CONTROLLER (ForeignController) contract address is: `0x4E64b576F72c237690F27727376186639447f096`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.2 - ALM Controller (ForeignController Avalanche) Contract Version [Core]  <!-- UUID: 0bf9305e-df4e-4f12-9051-a4974fd7272c -->

The ALM_CONTROLLER (ForeignController) contract version is: 1.8

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.3 - ALM Freezer Multisig (Avalanche) Address [Core]  <!-- UUID: abe7f425-65fd-4a3a-b70c-55a8f30e708d -->

The address of the Multisig that has the Freezer Role is specified in TBD.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.4 - ALM Relayer Multisig (Avalanche) Address [Core]  <!-- UUID: 229a9ce0-30bd-4069-a8a9-2ff911185b66 -->

The address of the Multisigs that has the Relayer Role will be specified in a future iteration of the artifact.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.5 - ALM Proxy (Avalanche) Contract [Core]  <!-- UUID: 179f186a-079b-4663-b06c-b21f9dec85ca -->

The address of the ALM_PROXY contract is: `TBD`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.6 - ALM Rate Limits (Avalanche) Contract [Core]  <!-- UUID: 43462d47-89bf-4166-88de-8601eb6ac7ad -->

The address of the ALM_RATE_LIMITS contract is: `TBD`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.7 - ALM Proxy Freezable (Avalanche) Contract Address [Core]  <!-- UUID: 4eb4959c-a91b-4a00-a605-138ac53b0786 -->

The address of the ALM_PROXY_FREEZABLE contract is: `0x45d91340B3B7B96985A72b5c678F7D9e8D664b62`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.8 - ALM Proxy Freezable (Avalanche) Contract Version [Core]  <!-- UUID: 7594b5c7-8ba4-4b81-a737-acb76858d762 -->

The version of the ALM_PROXY_FREEZABLE contract is: 1.1

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.9 - Governance Bridge Protection [Core]  <!-- UUID: dfffb528-049b-4f11-98cd-25c908d3385a -->

The documents herein contain the protection-related parameters of the Avalanche governance bridge.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.9.1 - Timelock Delay [Core]  <!-- UUID: 2af50d93-00ba-4546-b827-0759ab8dd4a2 -->

Governance actions delivered to the Avalanche deployment via the governance bridge are subject to a timelock delay of three (3) days between scheduling and execution.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.9.2 - Guardian Multisig Address [Core]  <!-- UUID: e47f8b7c-48e8-4d5e-bceb-75e2b0b0517d -->

`0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC` (Spark Operations Multisig)

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.9.3 - Guardian Multisig Required Number Of Signers [Core]  <!-- UUID: 25c35ce7-ded6-48d1-8eb8-4b2098152c28 -->

The Guardian Multisig has five (5) or more signers.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.9.4 - Guardian Multisig Quorum [Core]  <!-- UUID: 7e6ebd94-6864-4f96-bf29-77d9491788f1 -->

The Guardian Multisig quorum is half of the signer set, rounded up.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.6.9.5 - Guardian Powers [Core]  <!-- UUID: 022bbefc-9a31-4ac0-a14a-5f87ba9739e1 -->

The guardian mechanism power is strictly limited to cancelling pending actions during the timelock period. It does not have admin control over the Avalanche deployment at any time.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.7 - Robinhood Chain [Core]  <!-- UUID: 7be9f6a4-293e-439b-b7f7-ad4677981780 -->

This document contains the ALM Contract Addresses for the Spark Liquidity Layer on Robinhood Chain.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.7.1 - ALM Controller (ForeignController Robinhood Chain) Contract Address [Core]  <!-- UUID: 48b6b65d-6a28-4d33-a026-8dd6e646c610 -->

The address of the ALM_CONTROLLER (ForeignController) contract address is: `0xcf8d58A6eeF2a1cae2Ce69bC463b1178FB76bA1E`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.7.2 - ALM Controller (ForeignController Robinhood Chain) Contract Version [Core]  <!-- UUID: 13fcfb0e-3628-4dd1-9823-cdc99b478d97 -->

The ALM_CONTROLLER (ForeignController) contract version is: 1.10.0

###### A.6.1.1.1.2.6.1.2.1.1.1.2.7.3 - ALM Freezer Multisig (Robinhood Chain) Address [Core]  <!-- UUID: ad9553ca-eada-45d2-a968-aed9bb0e555e -->

The address of the Multisig that has the Freezer Role is: `0x2d5Aa449FB8C5646C81BC3C1D2034c2d37F17099`.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.7.4 - ALM Relayer Multisig (Robinhood Chain) Address [Core]  <!-- UUID: 88d4702c-da76-4fe8-a748-65f558953276 -->

The address of the Multisig that has the Relayer Role is: `0x0ca8f938Aba2214eA11eb451e795A8ef7B720C18`.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.7.5 - ALM Proxy (Robinhood Chain) Contract [Core]  <!-- UUID: d19eab7d-e0b8-4be2-b672-40d7773c6119 -->

The address of the ALM_PROXY contract is: `0xfD2fD4B046136B540A56C11c75ac679AE7d1dB24`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.7.6 - ALM Rate Limits (Robinhood Chain) Contract [Core]  <!-- UUID: 6a90553a-6798-43da-aeb6-98e1fffc7fc6 -->

The address of the ALM_RATE_LIMITS contract is: `0x5c1fDE9d4C7f1BF4bc5dEAA2a7752e56232c68a0`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.8 - X Layer [Core]  <!-- UUID: 9c35c0e5-d7b9-4538-a87b-3290897e35e4 -->

This document contains the ALM Contract Addresses for the Spark Liquidity Layer on X Layer.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.8.1 - ALM Controller (ForeignController X Layer) Contract Address [Core]  <!-- UUID: 63430cf9-0f5d-4a22-9879-6b9ecb8b9ee9 -->

The address of the ALM_CONTROLLER (ForeignController) contract address is: `0xf9187C99Ee842beABE8e2e346d958315BFc9331f`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.8.2 - ALM Controller (ForeignController X Layer) Contract Version [Core]  <!-- UUID: 65892a16-5e68-4a90-a2e5-89139aaa6823 -->

The ALM_CONTROLLER (ForeignController) contract version is: 1.10.0

###### A.6.1.1.1.2.6.1.2.1.1.1.2.8.3 - ALM Freezer Multisig (X Layer) Address [Core]  <!-- UUID: ed5c698b-cca9-43b8-965f-1dacd3ec46b3 -->

The address of the Multisig that has the Freezer Role is: `0x8a25A24EDE9482C4Fc0738F99611BE58F1c839AB`.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.8.4 - ALM Relayer Multisig (X Layer) Address [Core]  <!-- UUID: 7248a5ae-a45e-46a1-9cee-a8cb0b391ff8 -->

The address of the Multisig that has the Relayer Role is: `0x90D8c80C028B4C09C0d8dcAab9bbB057F0513431`.

###### A.6.1.1.1.2.6.1.2.1.1.1.2.8.5 - ALM Proxy (X Layer) Contract [Core]  <!-- UUID: eac738f2-1b92-4ea2-a3e7-79fd528ae587 -->

The address of the ALM_PROXY contract is: `0x83A914C361bB729EB6BEBC8C7bA993667A0E6Df8`

###### A.6.1.1.1.2.6.1.2.1.1.1.2.8.6 - ALM Rate Limits (X Layer) Contract [Core]  <!-- UUID: bd7ba684-2c40-4290-b263-0de4fd1f9aad -->

The address of the ALM_RATE_LIMITS contract is: `0x7F7E2286983994c4403Cf2B86758cE0e7bA666a8`

###### A.6.1.1.1.2.6.1.2.1.1.2 - Off-Chain Operational Parameters [Core]  <!-- UUID: 257dcfcb-9bb8-4989-a063-69ae4f01f224 -->

The documents herein list the off-chain operational parameters for the Spark Liquidity Layer on each blockchain. These operational parameters are protocol settings managed outside of smart contracts (off-chain), used by operators and off-chain systems to guide the functioning of the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.2.1.1.2.1 - Off-chain Operational Parameters For Ethereum Mainnet [Core]  <!-- UUID: 82d5f557-3a13-4426-a10f-afbbc763df22 -->

The document herein lists the current off-chain operational parameters for the Spark Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.1.2.6.1.2.1.1.2.1.1 - Minimum Operation Size Ethereum Mainnet [Core]  <!-- UUID: fc5d7d30-b863-4be9-8ce2-66f88ce51d74 -->

The minimum transaction size for operations on Ethereum Mainnet is (`MAINNET_MIN_OPERATION_SIZE`):

- 500,000

###### A.6.1.1.1.2.6.1.2.1.1.2.1.2 - Debt Ceiling Buffer Ethereum Mainnet [Core]  <!-- UUID: faa7bb3a-7e8c-4f00-b80f-fb10862d943c -->

The buffer amount below the maximum debt ceiling is (`DEBT_CEILING_BUFFER`):

- 10,000

###### A.6.1.1.1.2.6.1.2.1.1.2.2 - Off-chain Operational Parameters For Base [Core]  <!-- UUID: 0aa39269-9d5c-48af-a1de-6b1d5f5058b5 -->

The document herein lists the current off-chain operational parameters for the Spark Liquidity Layer on Base.

###### A.6.1.1.1.2.6.1.2.1.1.2.2.1 - Minimum Operation Size Base [Core]  <!-- UUID: c97c059e-23e4-4cf4-830f-e67020bb73d7 -->

The minimum transaction size for operations on Base is (`BASE_MIN_OPERATION_SIZE`):

- 100,000

###### A.6.1.1.1.2.6.1.2.1.1.2.2.2 - Minimum Maintained Balance Of USDC On Base [Core]  <!-- UUID: 73d73cb8-3692-4dcf-9446-e25243715bcf -->

The minimum balance of USDC that must be maintained in a Base account within the Spark Liquidity Layer is (`USDC_MIN_BALANCE_BASE`):

- 800,000

###### A.6.1.1.1.2.6.1.2.1.1.2.2.3 - Ideal Balance Of USDC On Base [Core]  <!-- UUID: e7641f75-dfd5-4f65-8294-052475389ac2 -->

The ideal balance of USDC that should be maintained in a Base account within the Spark Liquidity Layer is (`USDC_OPTIMAL_BALANCE_BASE`):

- 800,000

###### A.6.1.1.1.2.6.1.2.1.1.2.2.4 - Maximum Balance Of USDC On Base [Core]  <!-- UUID: 96791401-16fb-498f-9f00-34ff820c325a -->

The maximum balance of USDC that should be maintained in a Base account within the Spark Liquidity Layer is (`USDC_MAX_BALANCE_BASE`):

- 800,000

###### A.6.1.1.1.2.6.1.2.1.1.2.3 - Off-chain Operational Parameters For Arbitrum Parameters [Core]  <!-- UUID: 0f305c45-a2a2-4007-ae0e-9d829a09aba7 -->

The documents herein list the current off-chain operational parameters for the Spark Liquidity Layer on Arbitrum.

###### A.6.1.1.1.2.6.1.2.1.1.2.3.1 - Minimum Operation Size Arbitrum [Core]  <!-- UUID: 57117d7b-c4ad-4848-beda-894eab3cdbda -->

The minimum transaction size for operations on Arbitrum is (`ARBITRUM_MIN_OPERATION_SIZE`):

- 100,000

###### A.6.1.1.1.2.6.1.2.1.1.2.3.2 - Minimum Maintained Balance Of USDC On Arbitrum [Core]  <!-- UUID: d6bcfcf6-851d-48b4-9a29-4f85be428475 -->

The minimum balance of USDC that must be maintained in an Arbitrum account within the Spark Liquidity Layer is (`USDC_MIN_BALANCE_ARBITRUM`):

- This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.1.2.3.3 - Ideal Balance Of USDC On Arbitrum [Core]  <!-- UUID: 8f1288a8-bf03-4190-a44b-b63aa31428c1 -->

The ideal balance of USDC that should be maintained in an Arbitrum account within the Spark Liquidity Layer is (`USDC_OPTIMAL_BALANCE_ARBITRUM`):

- This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.1.2.3.4 - Maximum Balance Of USDC On Arbitrum [Core]  <!-- UUID: b8c1a6c1-c1a4-404c-ad41-5e1ed4dd672c -->

The maximum balance of USDC that should be maintained in an Arbitrum account within the Spark Liquidity Layer is (`USDC_MAX_BALANCE_ARBITRUM`):

- This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.1.3 - RateLimits [Core]  <!-- UUID: cdf6df73-045a-4bcb-a456-03441aa4530e -->

The documents herein list the `Ratelimits` for the Spark Liquidity Layer on each blockchain.

###### A.6.1.1.1.2.6.1.2.1.1.3.1 - Ethereum Mainnet [Core]  <!-- UUID: 91227e5c-65e5-4858-bfb2-41ab65c3bc87 -->

The documents herein list the current `RateLimits` for the Spark Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.1.2.6.1.2.1.1.3.1.1 - USDS Mint Maximum [Core]  <!-- UUID: ae234813-233e-4231-926b-5d0a8c09c684 -->

The maximum amount of USDS that can be minted within the Spark Liquidity Layer (`LIMIT_USDS_MINT`) is specified in the document herein.

- `maxAmount`: 1,000,000,000 USDS
- `slope`: 1,000,000,000 USDS per day

###### A.6.1.1.1.2.6.1.2.1.1.3.1.2 - USDS Burn Maximum [Core]  <!-- UUID: 85d01cb5-2bbf-4df9-998c-63131d83d9db -->

The maximum amount of USDS that can be burned within the Spark Liquidity Layer (`LIMIT_USDS_BURN`) is specified in the document herein.

- `maxAmount`: 0
- `slope`: 0

###### A.6.1.1.1.2.6.1.2.1.1.3.1.3 - USDS For USDC Swap Maximum [Core]  <!-- UUID: cd6ad021-80f4-432d-b00f-1d26e7984297 -->

The maximum amount of USDS that can be swapped for USDC by the Spark Liquidity Layer in the Mainnet PSM (`LIMIT_USDS_TO_USDC`) is specified in the document herein.

- `maxAmount`: 1,000,000,000 USDC
- `slope`: 1,000,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.1.4 - USDC Mainnet ALM Proxy Maximum [Core]  <!-- UUID: 9024c8ce-40a6-4eb7-90c7-62dee7d5e408 -->

The maximum amount of USDC that can be sent to the Ethereum Mainnet ALM Proxy (`LIMIT_USDC_TO_DOMAIN`, hashed with Ethereum domain) is specified in the document herein.

- `maxAmount`: 4,000,000 USDC
- `slope`: 2,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.1.4.1 - Maximum USDC Bridged To Ethereum Mainnet Via Circle CCTP [Core]  <!-- UUID: 77d2f2c3-c1a6-4d63-ac8f-dd1b8dedaab8 -->

The maximum amount of USDC that can be bridged to Ethereum Mainnet ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_ETH`) is specified in the document herein.

- `maxAmount`: 200,000,000 USDC
- `slope`: 500,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.2 - Base [Core]  <!-- UUID: e2055ff1-f601-4923-b186-57513a2cf682 -->

The documents herein list the current `RateLimits` for the Spark Liquidity Layer on Base.

###### A.6.1.1.1.2.6.1.2.1.1.3.2.1 - Base USDC Deposit Maximum [Core]  <!-- UUID: 6cd396d6-8f98-4ca8-a61d-8b49def2a793 -->

The maximum amount of USDC that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDC`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.2.2 - Base USDC Withdrawal Maximum [Core]  <!-- UUID: 3cd83281-90cf-4c29-a3a5-6dc83099750b -->

The maximum amount of USDC that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDC`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.2.3 - Base USDS Deposit Maximum [Core]  <!-- UUID: 38d0e2c3-3702-4906-b230-66a152dd998d -->

The maximum amount of USDS that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.2.4 - Base USDS Withdrawal Maximum [Core]  <!-- UUID: 2cac91fb-e1e2-443d-ad12-ee45211eba1d -->

The maximum amount of USDS that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: 0

###### A.6.1.1.1.2.6.1.2.1.1.3.2.5 - Base sUSDS Deposit Maximum [Core]  <!-- UUID: f9e926e1-e127-42ec-883d-d11baecb0fd6 -->

The maximum amount of sUSDS that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_SUSDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.2.6 - Base sUSDS Withdrawal Maximum [Core]  <!-- UUID: 521cc062-0b43-4d93-91c3-fdc29e4792f1 -->

The maximum amount of sUSDS that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_SUSDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: 0

###### A.6.1.1.1.2.6.1.2.1.1.3.2.7 - USDC Base ALM Proxy Maximum [Core]  <!-- UUID: 59bc4c89-3edf-4a1b-a288-151cd5cfc624 -->

The maximum amount of USDC that can be sent to the Base ALM Proxy (`LIMIT_USDC_TO_DOMAIN`, hashed with Base domain) is specified in the document herein.

- `maxAmount`: 4,000,000 USDC
- `slope`: 2,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.2.7.1 - Maximum USDC Bridged From Ethereum Mainnet To Base Via Circle CCTP [Core]  <!-- UUID: 2a8a7903-983a-4dc5-9f77-0b90ab66f9ae -->

The maximum amount of USDC that can be bridged to Base ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_BASE`) is specified in the document herein.

- `maxAmount`: 200,000,000 USDC
- `slope`: 500,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.3 - Arbitrum [Core]  <!-- UUID: 626bcaea-4de3-4262-9098-82c454c4fb9c -->

The documents herein list the current `RateLimits` for the Spark Liquidity Layer on Arbitrum.

###### A.6.1.1.1.2.6.1.2.1.1.3.3.1 - Arbitrum USDC Deposit Maximum [Core]  <!-- UUID: ffbc3f81-fd95-4a38-9f95-6c834d01212a -->

The maximum amount of USDC that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDC`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.1.3.3.2 - Arbitrum USDC Withdrawal Maximum [Core]  <!-- UUID: f7e5dc3b-b26c-4a44-9e0b-0b385ad22704 -->

The maximum amount of USDC that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDC`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.1.3.3.3 - Arbitrum USDS Deposit Maximum [Core]  <!-- UUID: ddf6a5b7-5c41-4c80-8ad9-0222ef558fb4 -->

The maximum amount of USDS that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDS`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.1.3.3.4 - Arbitrum USDS Withdrawal Maximum [Core]  <!-- UUID: f5a14451-b476-46ea-91e8-009f6230ac3e -->

The maximum amount of USDS that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDS`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.1.3.3.5 - Arbitrum sUSDS Deposit Maximum [Core]  <!-- UUID: 8be6ab2f-9b82-4727-be24-e2d6ac5c4c5f -->

The maximum amount of sUSDS that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_SUSDS`) is specified in the document herein.

- `maxAmount`: 10,000,000 USDS worth of sUSDS
- `slope`: 5,000,000 USDS worth of sUSDS per day

###### A.6.1.1.1.2.6.1.2.1.1.3.3.6 - Arbitrum sUSDS Withdrawal Maximum [Core]  <!-- UUID: 127e7438-d797-4b3e-a464-230f8253f0d2 -->

The maximum amount of sUSDS that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_SUSDS`) is specified in the document herein.

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.3.7 - USDT Arbitrum ALM Proxy Maximum [Core]  <!-- UUID: 5621e3c9-4537-4e9d-9a10-bfa4f68cc755 -->

The maximum amount of USDT that can be sent to the Arbitrum ALM Proxy (`LIMIT_USDT_TO_DOMAIN`, hashed with Arbitrum domain) is specified in the document herein.

- `maxAmount` (USDT): 5,000,000
- `slope` (USDT/ day): 50,000,000

###### A.6.1.1.1.2.6.1.2.1.1.3.4 - Unichain [Core]  <!-- UUID: 40eb29f0-9d83-4c83-ae68-ea46b9f1bcac -->

The documents herein list the current `RateLimits` for the Spark Liquidity Layer on Unichain.

###### A.6.1.1.1.2.6.1.2.1.1.3.4.1 - Unichain USDC Deposit Maximum [Core]  <!-- UUID: c02294b9-1938-40b5-af8c-57b82c7b1f51 -->

The maximum amount of USDC that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDC`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.4.2 - Unichain USDC Withdrawal Maximum [Core]  <!-- UUID: cb146c46-207d-4a52-be6d-9a4623f2d921 -->

The maximum amount of USDC that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDC`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.4.3 - Unichain USDS Deposit Maximum [Core]  <!-- UUID: f998ce83-747f-4c60-95ba-26f1f2facdb8 -->

The maximum amount of USDS that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.4.4 - Unichain USDS Withdrawal Maximum [Core]  <!-- UUID: 3a6e6efd-314a-4f21-b238-0ffa148fb8e3 -->

The maximum amount of USDS that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.4.5 - Unichain sUSDS Deposit Maximum [Core]  <!-- UUID: 1741e5ba-e45a-4960-b193-f8bee9d595c9 -->

The maximum amount of sUSDS that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_SUSDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.4.6 - Unichain sUSDS Withdrawal Maximum [Core]  <!-- UUID: 16004284-de05-4ee4-a9db-762de1270de9 -->

The maximum amount of sUSDS that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_SUSDS`) is specified in the document herein.

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.5 - Optimism [Core]  <!-- UUID: 13bda6de-0abf-4b64-9379-4653c8f4875e -->

The documents herein list the current `RateLimits` for the Spark Liquidity Layer on Optimism.

###### A.6.1.1.1.2.6.1.2.1.1.3.5.1 - Optimism USDC Deposit Maximum [Core]  <!-- UUID: 3f08e295-8edc-489a-8d46-9b4b7ca83d01 -->

The maximum amount of USDC that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDC`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.5.2 - Optimism USDC Withdrawal Maximum [Core]  <!-- UUID: 90c809f2-3f2c-4a76-beb8-06140822e2cd -->

The maximum amount of USDC that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDC`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.5.3 - Optimism USDS Deposit Maximum [Core]  <!-- UUID: f162baa7-9400-4368-adf8-5793415de5b3 -->

The maximum amount of USDS that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.5.4 - Optimism USDS Withdrawal Maximum [Core]  <!-- UUID: f04f600b-3cc0-4c10-8540-1dce56d130e2 -->

The maximum amount of USDS that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.5.5 - Optimism sUSDS Deposit Maximum [Core]  <!-- UUID: ae241843-1492-42b4-8a66-687701ba4dc0 -->

The maximum amount of sUSDS that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_SUSDS`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.5.6 - Optimism sUSDS Withdrawal Maximum [Core]  <!-- UUID: a9d4793d-da6a-440e-9435-993070700b60 -->

The maximum amount of sUSDS that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_SUSDS`) is specified in the document herein.

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.6 - Avalanche [Core]  <!-- UUID: bf7f9935-ef38-4d33-a871-d4273cb341e0 -->

The documents herein list the current `RateLimits` for the Spark Liquidity Layer on Avalanche.

###### A.6.1.1.1.2.6.1.2.1.1.3.6.1 - Avalanche USDC Deposit Maximum [Core]  <!-- UUID: 3d180927-6af0-462e-b507-ecd3b76aead9 -->

The maximum amount of USDC that can be deposited into the PSM (`LIMIT_PSM_DEPOSIT_USDC`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.6.2 - Avalanche USDC Withdrawal Maximum [Core]  <!-- UUID: 8b9fa488-8005-488a-8537-11a8bdcb205b -->

The maximum amount of USDC that can be withdrawn from the PSM (`LIMIT_PSM_WITHDRAW_USDC`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.2.1.1.3.6.3 - USDC Avalanche ALM Proxy Maximum [Core]  <!-- UUID: 59673606-e50f-4c75-86e1-6bbc968321f0 -->

The maximum amount of USDC that can be sent to the Avalanche ALM Proxy (`LIMIT_USDC_TO_DOMAIN`, hashed with Avalanche domain) is specified in the document herein.

- `maxAmount`: 100,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.6.3.1 - Maximum USDC Bridged From Ethereum Mainnet To Avalanche Via Circle CCTP [Core]  <!-- UUID: 0de9f0f1-ccef-4f17-b699-7dedb79673b9 -->

The maximum amount of USDC that can be bridged to Avalanche ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_AVALANCHE`) is specified in the document herein.

- `maxAmount`: 100,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.2.1.1.3.7 - Robinhood Chain [Core]  <!-- UUID: 0e4713f0-0f3c-42c8-8c28-9643febf8f5f -->

The documents herein list the current `RateLimits` for the Spark Liquidity Layer on Robinhood Chain.

###### A.6.1.1.1.2.6.1.2.1.1.3.7.1 - USDG Robinhood Chain Transfer Maximum [Core]  <!-- UUID: 101066cd-5863-4391-af66-210fec7c8ab8 -->

The maximum amount of USDG that can be transferred from the Robinhood Chain ALM Proxy is specified in the document herein.

- `maxAmount` (USDG): 50,000,000
- `slope` (USDG/ day): 250,000,000
- Recipient: `0x17C0F5345d1144fdF670D14719077be3842E5087`

###### A.6.1.1.1.2.6.1.2.1.1.3.7.2 - USDG Robinhood Chain ALM Proxy Maximum [Core]  <!-- UUID: bb47f741-e64b-440c-822c-3937fe94e87e -->

The maximum amount of USDG that can be sent to the Robinhood Chain ALM Proxy is specified in the document herein.

- `maxAmount` (USDG): 50,000,000
- `slope` (USDG/ day): 250,000,000
- Recipient: `0xf752cF318dfF2C01575c98741AA52e7a34d873Fd`

###### A.6.1.1.1.2.6.1.2.1.1.3.8 - X Layer [Core]  <!-- UUID: 76127cf5-4b2e-4c2f-8d8a-352759e5a149 -->

The documents herein list the current `RateLimits` for the Spark Liquidity Layer on X Layer.

###### A.6.1.1.1.2.6.1.2.1.1.3.8.1 - USDT X Layer ALM Proxy Maximum [Core]  <!-- UUID: 390b47c3-9183-4a79-93d1-ed8bab578bb3 -->

The maximum amount of USDT that can be sent to the X Layer ALM Proxy is specified in the document herein.

- `maxAmount` (USDT): 5,000,000
- `slope` (USDT/ day): 100,000,000

###### A.6.1.1.1.2.6.1.2.1.2 - Governance Processes [Core]  <!-- UUID: 9e74aa40-898f-4389-ba3d-8590c12f075d -->

The documents herein describe the specific governance processes for the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.2.1.2.1 - Invoking New Instances [Core]  <!-- UUID: da88ec3d-3ce8-4f28-bb8e-bbdd3deb2b14 -->

The governance process to invoke a new Instance of the Allocation System Primitive follows the Root Edit process see [A.6.1.1.1.2.2.2.2.1.2 - Operational Process Definition](a9c97e28-6ac7-4e04-aac1-9d5dd617c6e0).

###### A.6.1.1.1.2.6.1.2.1.2.2 - Multisigs [Core]  <!-- UUID: 631973de-6f13-440b-8f66-478dfdda4d60 -->

The documents herein define multisigs that have privileged access to manage the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.2.1.2.2.1 - Prime Relayer Multisig [Core]  <!-- UUID: d4628bb9-978c-4e4a-884c-7e0b3b7e1daf -->

The Prime Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.1.2.6.1.2.2.1.1.2 - Relayer Role](cc2f7956-90ce-4025-9642-bfe403dc3ccc) and is controlled by Phoenix Labs.

###### A.6.1.1.1.2.6.1.2.1.2.2.1.1 - Address [Core]  <!-- UUID: 67bf2799-8d57-44be-82e4-827912ff30df -->

The address of the Prime Relayer Multisig on the Ethereum Mainnet, Base, and Arbitrum is `0x8a25A24EDE9482C4Fc0738F99611BE58F1c839AB`.

###### A.6.1.1.1.2.6.1.2.1.2.2.1.2 - Required Number Of Signers [Core]  <!-- UUID: 8deac2a8-c728-4d0c-9f05-6fcf3965bdc9 -->

The Prime Relayer Multisig currently has a 1/2 signing requirement.

###### A.6.1.1.1.2.6.1.2.1.2.2.1.3 - Signers [Core]  <!-- UUID: bad3c652-ddda-4161-9ec8-5cef7a74b3f4 -->

The signers of the Prime Relayer Multisig are two (2) addresses controlled by Ecosystem Actor Phoenix Labs.

###### A.6.1.1.1.2.6.1.2.1.2.2.1.4 - Usage Standards [Core]  <!-- UUID: d800ab5e-4efa-45db-8d31-435f090a9678 -->

The signers of the Prime Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.2.2.1.5 - Modification [Core]  <!-- UUID: 19d05632-97ef-4717-a47d-c0de16631fac -->

Ecosystem Actor Phoenix Labs can change the signers of the Prime Relayer Multisig at any time, so long as there are at least two (2) signers and at least a majority of signers are required to execute transactions.

###### A.6.1.1.1.2.6.1.2.1.2.2.2 - Core Operator Relayer Multisig [Core]  <!-- UUID: 8286092a-69f2-46af-a989-c694a1756753 -->

The Core Operator Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.1.2.6.1.2.2.1.1.2 - Relayer Role](cc2f7956-90ce-4025-9642-bfe403dc3ccc) and is jointly controlled by Operational GovOps Soter Labs and the Spark Assets Foundation in accordance with [A.6.1.1.1.2.1.1.3.1.1.6.1 - Spark Assets Foundation](4d70e4a7-6f65-421c-b22a-ac5a6eae8170).

###### A.6.1.1.1.2.6.1.2.1.2.2.2.1 - Address [Core]  <!-- UUID: 567e4905-2b05-493e-95ac-8a4d20afed2b -->

The address of the Core Operator Relayer Multisig on the Ethereum Mainnet, Base, and Arbitrum is `0x8Cc0Cb0cfB6B7e548cfd395B833c05C346534795`.

###### A.6.1.1.1.2.6.1.2.1.2.2.2.2 - Required Number Of Signers [Core]  <!-- UUID: d397fcef-85da-4c07-b675-14ec66d4cff9 -->

The Core Operator Relayer Multisig currently has a 2/5 signing requirement.

###### A.6.1.1.1.2.6.1.2.1.2.2.2.3 - Signers [Core]  <!-- UUID: 1563f1ee-0097-4bb3-a03a-01162d00788b -->

The Core Operator Relayer Multisig comprises the following signers:

- Operational GovOps Soter Labs: 2 signers
- Spark Assets Foundation (SAF): 2 signers
- Phoenix Labs (PL): 1 signer

Phoenix Labs' signer may create and propose transactions; execution requires meeting the 2/5 threshold.

###### A.6.1.1.1.2.6.1.2.1.2.2.2.4 - Usage Standards [Core]  <!-- UUID: 846f23a1-eca3-4d55-8ed7-2c14c618d722 -->

The signers of the Core Operator Relayer Multisig must use the multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.1.2.2.2.5 - Modification [Core]  <!-- UUID: 31c59017-769f-4a5b-88f7-8bef200dcc71 -->

Operational GovOps Soter Labs can change the signers of the Core Operator Relayer Multisig at any time, so long as there are at least three (3) signers and at least two-thirds of signers are required to execute transactions.

###### A.6.1.1.1.2.6.1.2.1.2.2.3 - Freezer Multisig [Core]  <!-- UUID: c805c872-05df-4157-a869-dff28535bf81 -->

The Freezer Multisig has the `FREEZER_ROLE` as defined in [A.6.1.1.1.2.6.1.2.2.1.1.4 - Freezer Role](02a614ea-1d6b-4197-b39b-49de676092cb) and is controlled by Phoenix Labs and VoteWizard.

###### A.6.1.1.1.2.6.1.2.1.2.2.3.1 - Address [Core]  <!-- UUID: 51777bdd-df5f-4a6e-93f5-8163d981f595 -->

The address of the Freezer Multisig on the Ethereum Mainnet, Base, and Arbitrum is `0x90D8c80C028B4C09C0d8dcAab9bbB057F0513431`.

###### A.6.1.1.1.2.6.1.2.1.2.2.3.2 - Required Number Of Signers [Core]  <!-- UUID: cf7acab9-9363-402b-b636-395f6bb5f6f7 -->

The Freezer Multisig currently has a 2/4 signing requirement.

###### A.6.1.1.1.2.6.1.2.1.2.2.3.3 - Signers [Core]  <!-- UUID: f76b5952-9060-4fe6-b64e-5533ef205919 -->

The Freezer Multisig has the following signers:

- Phoenix Labs (PL): 3 signers
- VoteWizard: 1 signer

###### A.6.1.1.1.2.6.1.2.1.2.2.3.4 - Usage Standards [Core]  <!-- UUID: 4c33239e-59c9-4d5b-8872-bf7176d205dc -->

The signers of the Freezer Multisig should exercise their authority to freeze the Spark Liquidity Layer in the event that Spark is not complying with rules regarding Risk Capital or Asset Liability Management, or in the event of another emergency. The signers should consult with Operational GovOps Soter Labs before exercising such authority, unless such consultation would cause a delay that could result in a loss of user funds or harm to Sky or Spark. Operational GovOps Soter Labs may also ask the signers to exercise the Freezer Multisig in an emergency. The signers will work with Operational GovOps Soter Labs and, if necessary, other Ecosystem Actors, in good faith in determining whether to exercise their authority based on such request.

Each action executed by the Freezer Multisig, including any function calls and their parameters, must be reported to the Sky community within a reasonable time frame through a post on the Sky Forum.

###### A.6.1.1.1.2.6.1.2.1.2.2.3.5 - Modification [Core]  <!-- UUID: 658b3a32-0416-4380-b960-f86f3a2f3cfa -->

Modification of the signers of the Freezer Multisig must be approved through a Governance Poll; no Executive Vote is required.

The only exceptions to this are if: 1) a signer self-reports a loss of access to their private key due to any reason; or 2) a signer explicitly expresses their wish to be removed as a signer. In both cases, the signer is required to communicate the loss of access to their private key, or the wish to be removed as a signer, in the form of a public Sky Forum post. The specific signer should be replaced as soon as possible, which does not require a Governance Poll.

Any changes to the multisig signers that do not fall within the two exceptions listed above, or that have not been ratified by Sky Governance, should be questioned immediately and treated as malicious. Where malicious activity is suspected, the Core Facilitator must prepare an expedited Executive Vote so that Sky Governance can vote on removing external security access from the multisig.

###### A.6.1.1.1.2.6.1.2.1.2.3 - Token Claim Authorization [Core]  <!-- UUID: ea73f176-0b94-4e93-b1ee-ca498ac5a6c6 -->

Phoenix Labs is authorized to propose the inclusion of transfers of accrued treasury and collector revenues from the Active Instances to the Spark ALM Proxy in a Spark Spell. Additionally, for non-USD-denominated reserve assets, or USD-denominated reserve assets that are not supported by the Spark Liquidity Layer, the reserves can be transferred to the Spark Operations Multisig at address (`0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC`) to be liquidated for USDS, with the proceeds of sale transferred to the Spark SubDAO Proxy. This request must be posted to the Sky Forum under the Spark Prime category. The Operational Executor Agent must formally approve the inclusion of the transfer in a Spark Spell, with no token holder vote needed.

###### A.6.1.1.1.2.6.1.2.1.3 - Total Risk Capital (TRC) Management [Core]  <!-- UUID: ff7add39-b942-4df0-a710-75f70a05b49d -->

The documents herein** **specify requirements related to Spark’s Total Risk Capital (TRC) management.

###### A.6.1.1.1.2.6.1.2.1.3.1 - Spark’s Operation Of Spark Liquidity Layer And Agreement Regarding Encumbrance Ratio [Core]  <!-- UUID: 23f7ed09-99ca-45aa-8e12-dffcf55170af -->

Spark will continue to operate the Spark Liquidity Layer and agrees to stay at or below a 90% Encumbrance Ratio. See [A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9).

###### A.6.1.1.1.2.6.1.2.1.3.2 - Spark’s Total Risk Capital (TRC) Management Processes [Core]  <!-- UUID: ed9602b1-c7fe-4e2b-b4c4-37a1fd21fafd -->

As operators of the Spark Liquidity Layer, Spark automatically inherits, and is subject to, the base class of operational requirements related to Total Risk Capital management defined in [A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capital (TRC) Management](3af8a3a2-25e5-44b3-87a4-7df1f2712685). Modifications to the base operational logic automatically propagate to the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.2 - Spark Liquidity Layer Operational Processes [Core]  <!-- UUID: f6c90935-4266-4987-9060-d1f1675ff24b -->

The documents herein describe common operational procedures for the Spark Liquidity Layer applicable across multiple Instances.

###### A.6.1.1.1.2.6.1.2.2.1 - Routine Protocol [Core]  <!-- UUID: 7f69f60f-a0eb-429e-a8a7-228b42b456a2 -->

The documents herein define the protocol for routine ongoing management of the Spark Liquidity Layer and its active Instances.

###### A.6.1.1.1.2.6.1.2.2.1.1 - Role Hierarchy And Permissions [Core]  <!-- UUID: e72290a8-e1af-494b-931d-778f5d697d4d -->

The documents herein defines roles (Admin, Relayer, Freezer) and their responsibilities/permissions for managing the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.2.2.1.1.1 - Default Admin Role [Core]  <!-- UUID: da2e149b-e70c-4373-94da-6da6c4c26048 -->

The admin role (`DEFAULT_ADMIN_ROLE`) is the role that can grant and revoke any role, including itself and all other roles defined in the contract. The admin role is also used for general admin functions in all contracts. This role is fully controlled by Sky Governance via the Spark Proxy.

`constructor(address admin) {
        _grantRole(DEFAULT_ADMIN_ROLE, admin);`

###### A.6.1.1.1.2.6.1.2.2.1.1.2 - Relayer Role [Core]  <!-- UUID: cc2f7956-90ce-4025-9642-bfe403dc3ccc -->

The `RELAYER_ROLE` is the address for the Spark Liquidity Layer ALM Planner off-chain system that calls functions on `Controller` contracts to perform actions on behalf of the `ALMProxy` contract. The Relayer Role may be granted to an address by any address holding the `DEFAULT_ADMIN_ROLE`. The Relayer Role may be removed from an address by any address holding the `DEFAULT_ADMIN_ROLE` or the `FREEZER_ROLE`.

###### A.6.1.1.1.2.6.1.2.2.1.1.3 - ALM Controller Role [Core]  <!-- UUID: 846e460d-db29-4ad0-82f7-5174fcb9b195 -->

The `ALM_CONTROLLER_ROLE` is the address of the role that can call the `call` functions on the `ALMProxy` contract and update `RateLimits` contract. It includes the `MainnetController` and `ForeignController` contracts. ALM Controller contracts are accessed and modified via the Relayer Role.

###### A.6.1.1.1.2.6.1.2.2.1.1.4 - Freezer Role [Core]  <!-- UUID: 02a614ea-1d6b-4197-b39b-49de676092cb -->

The `FREEZER_ROLE` is the address of the emergency role that can remove a compromised Relayer.

###### A.6.1.1.1.2.6.1.2.2.1.2 - Controller Functions [Core]  <!-- UUID: 92e30e64-76dd-493d-be14-2088892e11b1 -->

The documents herein describe the purpose and operational use of key functions within Spark Liquidity Layer `MainnetController` and `ForeignController` contracts: USDS management (mint/burn USDS), Asset Transfer Management (direct transfers, protocol deposits/withdrawals), Cross-chain Operations (CCTP bridging).

###### A.6.1.1.1.2.6.1.2.2.1.2.1 - Mainnet Controller Contract Functions [Core]  <!-- UUID: 9d9c441e-b5c9-4d5a-a776-b89d6b85f568 -->

The documents herein define the functions controlled by the Controller contract for Spark Liquidity Layer operations on Ethereum Mainnet.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.1 - Admin Functions [Core]  <!-- UUID: 1c6ea8a1-71a7-4d56-ba74-68de7ed59f2b -->

The documents herein define the operations performed by the `DEFAULT_ADMIN_ROLE` within the `MainnetController` contract.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.1.1 - Set The Mint Recipient [Core]  <!-- UUID: 6e08ac53-a63b-4c23-8a52-7644f25cb8cf -->

The documents herein define the process to set the `mintRecipient` for a specific `destinationDomain`. This is used in cross-chain transfers to specify the address that will receive minted tokens on the target chain.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.1.1.1 - Admin Role [Core]  <!-- UUID: a6f085f5-4670-443e-ad83-b538527b8c24 -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMintRecipient`.

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.1.1.2 - Associate Mint Recipient With Domain [Core]  <!-- UUID: 0d7bbcaf-477f-4b07-bb8b-fca7cf316f57 -->

The operator must associate the `mintRecipient` with the `destinationDomain` such that any tokens minted on this domain will go to this recipient.

`{
        mintRecipients[destinationDomain] = mintRecipient;`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.1.1.3 - Emit Event To Logs [Core]  <!-- UUID: 6ced376c-a922-4626-82ea-ab6001a17257 -->

The operator must emit the event to the blockchain logs.

`        emit MintRecipientSet(destinationDomain, mintRecipient);
    }`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2 - Relayer Functions [Core]  <!-- UUID: 3d1d2f04-1f4d-4af8-9dcb-2e8dfd3aa704 -->

The documents herein define the operations performed by the `RELAYER_ROLE` within the `MainnetController` contract.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1 - Core Vault Functions [Core]  <!-- UUID: 55532d77-304b-4844-ba7f-781c014e99fa -->

The documents herein define the operations that are performed to maintain the desired level of liquidity and debt balance of the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1 - Mint USDS [Core]  <!-- UUID: 8e62cfdb-189c-4ea1-88e0-a1eaf5c55716 -->

The documents herein define the steps for an operator to `mint` USDS from the Sky Allocation Vault to the Spark ALM Proxy.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.1 - Relayer Role [Core]  <!-- UUID: a0424398-100e-4c6e-9691-f59efbda6fcd -->

The operator must ensure they are working as a `Relayer`. Only the `RELAYER` role is allowed to `mintUSDS`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function mintUSDS(uint256 usdsAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.2 - Check RateLimits [Core]  <!-- UUID: 4414c19c-3194-4481-8db1-42b6dd718c5a -->

The operator must ensure the `RateLimits` allow for minting the required amount.

` rateLimited(LIMIT_USDS_MINT, usdsAmount)`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.3 - Mint USDS To Buffer [Core]  <!-- UUID: 3d84f6a0-5bcf-4140-913b-072a97663b07 -->

The operator must call the `MainnetController` contract to `mint` USDS into the Buffer.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.3.1 - Encode Mint Function Call [Core]  <!-- UUID: c7b2c565-d1b5-4239-9139-89762423443d -->

The operator must encode the `mint` function call, using `abi.encodeCall` with the address `vault` from which USDS will be `drawn`, and the `amount` of USDS to `mint`.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.3.2 - Send Encoded Call [Core]  <!-- UUID: a171748b-6070-4b76-bda0-2268e2e1938d -->

The operator must send the encoded call using `proxy.doCall()` to the `draw` function of the vault contract.

`    {
        // Mint USDS into the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.draw, (usdsAmount))
        );`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.4 - Transfer USDS To ALM Proxy [Core]  <!-- UUID: a35cb461-3087-4093-8a06-ed7c69a11385 -->

The operator must call the `MainnetController` contract to `transfer` USDS from the Buffer to the ALM Proxy.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.4.1 - Encode Transfer Function [Core]  <!-- UUID: b46d9837-cca9-4d36-8363-a32379d28f93 -->

The operator must encode the `transfer` function call, using `abi.encodeCall` with the `buffer` address USDS will be transferred from, the `proxy` address that will receive USDS (i.e. ALM Proxy), and the `amount` of USDS to `transfer`.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.1.4.2 - Send Encoded Call [Core]  <!-- UUID: 39ed68c1-6341-44a3-a8ee-4ae982acf341 -->

The operator must send the encoded call using `proxy.doCall()` to the `transferFrom` function of the USDS contract.

`        // Transfer USDS from the buffer to the proxy
        proxy.doCall(
            address(usds),
            abi.encodeCall(usds.transferFrom, (buffer, address(proxy), usdsAmount))
        );
    }`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS [Core]  <!-- UUID: fc8b57fd-c0c8-422d-b0a9-e124b3cac439 -->

The documents herein define the steps for an operator to return and then `burn` Spark’s USDS debt in the Sky Allocation Vault.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.1 - Relayer Role [Core]  <!-- UUID: bcb7d73b-3f6d-4b79-8c8f-6cbbb438dcf3 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `burnUSDS`. They must also ensure the contract `isActive` i.e. can process the request.

`function burnUSDS(uint256 usdsAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.2 - Check RateLimits [Core]  <!-- UUID: efbe3b04-022f-4181-b7c9-402728536931 -->

The operator must ensure the `RateLimits` allow for minting the required amount.

`cancelRateLimit(LIMIT_USDS_MINT, usdsAmount)`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.3 - Transfer USDS To Buffer [Core]  <!-- UUID: 33dfd992-2e15-4af6-9331-d15f62f55045 -->

The operator must call the `MainnetController` to `transfer` USDS from the ALM Proxy to the Buffer.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.3.1 - Encode Transfer Function Call [Core]  <!-- UUID: 14dd94bf-536e-444a-8d92-e5bb186b3a9f -->

The operator must encode the `transfer` function call, using `abi.encodeCall` with the `buffer` address USDS will be transferred to, and the `amount` of USDS to `transfer`.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.3.2 - Send Encoded Call [Core]  <!-- UUID: a0dff4ff-a21f-40a4-b774-c0483ac9c90d -->

The operator must send the encoded call using `proxy.doCall()` to the `transfer` function of the USDS contract.

`     {
        // Transfer USDS from the proxy to the buffer
        proxy.doCall(
            address(usds),
            abi.encodeCall(usds.transfer, (buffer, usdsAmount))
        );`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.4 - Burn USDS [Core]  <!-- UUID: 807a0401-2c4d-46f3-b7c7-aba18e0bd8c1 -->

The operator must call the `MainnetController` contract to `burn` USDS.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.4.1 - Encode Wipe Function Call [Core]  <!-- UUID: 6d28bbc7-7124-4eb3-a594-8684214b5ecb -->

The operator must encode the `wipe` function call, using `abi.encodeCall` with the address `vault` from which USDS will be `burned`, and the `amount` of USDS to `burn`.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2.4.2 - Send Encoded Call [Core]  <!-- UUID: 5db8d9fd-015e-414e-a35e-450fea7f9e8b -->

The operator must send the encoded call using `proxy.doCall()` to the `wipe` function of the vault contract.

`// Burn USDS from the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.wipe, (usdsAmount))
        );
    }`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.2 - ERC-4626 Functions [Core]  <!-- UUID: e386a0df-9e0b-4ffd-9879-49131f795b0b -->

The documents herein define the general Spark Liquidity Layer operational procedures for interacting with ERC4626-compliant tokenized vaults. ERC4626 is a standard interface for vaults representing shares of an underlying ERC20 token. Spark Liquidity Layer can integrate with various ERC4626 vaults (e.g., Fluid Finance).

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.1 - General Deposit to ERC-4626 Tokens Procedure [Core]  <!-- UUID: 862f4064-47e5-4f76-908d-64edfcfe0ddd -->

This document defines the steps for an operator to deposit assets from the ALM Proxy to the ERC-4626 vault to receive yield-bearing shares.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a deposit.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient underlying asset, and the deposit amount is within instance-specific `RateLimits` (defined in the relevant Instance Configuration Document).
- The Spark Liquidity Layer Operator approves the target ERC4626 vault (identified by its `token` address in the Instance Configuration Document) to spend the underlying `asset` from the ALM Proxy.
- The Spark Liquidity Layer Operator calls the `deposit(uint256 amount, address receiver)` function on the target ERC4626 vault, specifying the `amount` of underlying asset and the ALM `proxy` as the receiver of vault shares.
- The number of shares received is recorded.
- For detailed call structures, instance-specific parameters (vault address, asset address, rate limits), and operational examples, refer to the specific ERC4626 Instance Configuration Document (ICD) (e.g., [A.6.1.1.1.2.6.1.3.1.5.1.3 - Instance-specific Operational Processes](3bc424bf-079e-4b6b-8749-58c942c7d57b) or other relevant ERC4626 ICDs).

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.2 - General Withdraw from ERC-4626 Tokens Procedure [Core]  <!-- UUID: e797d1cc-9161-4b7a-8c16-db20a026d001 -->

This document defines the steps for an operator to withdraw a yield-earning balance from the ERC-4626 vault to the ALM Proxy.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a withdrawal.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient shares of the ERC4626 vault token, and the withdrawal amount is within instance-specific `RateLimits` (defined in the relevant ICD).
- The Spark Liquidity Layer Operator calls the `withdraw(uint256 assets, address receiver, address owner)` function on the target ERC4626 vault, specifying the `amount` of underlying assets to withdraw, with the ALM `proxy` as both `receiver` (of assets) and `owner` (of shares being burned).
- The number of shares burned is recorded.
- For detailed call structures, instance-specific parameters, and operational examples, refer to the specific ERC4626 Instance Configuration Document.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.3 - General Redeem from ERC-4626 Tokens Procedure [Core]  <!-- UUID: ed774ab7-c761-444b-963d-7407bf91e243 -->

This document defines the steps for an operator to redeem yield-bearing shares from the ERC-4626 vault, receiving the corresponding amount of underlying assets into the ALM Proxy.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a redemption of shares.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient shares of the ERC4626 vault token.
- The Spark Liquidity Layer Operator calls the `redeem(uint256 shares, address receiver, address owner)` function on the target ERC4626 vault, specifying the number of `shares` to redeem, with the ALM `proxy` as both `receiver` (of assets) and `owner` (of shares being redeemed).
- The amount of underlying assets received is recorded, and relevant `RateLimits` (for withdrawal) are updated.
- For detailed call structures, instance-specific parameters, and operational examples, refer to the specific ERC4626 Instance Configuration Document.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.3 - Aave Functions [Core]  <!-- UUID: 9922dcf0-4562-445b-9a46-712f677cce64 -->

The documents herein describe the general Spark Liquidity Layer operational procedures for depositing to and withdrawing from Aave lending pools.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.1 - General Deposit to Aave ATokens Procedure [Core]  <!-- UUID: 316008c1-0c1f-487a-a5bf-1966e86fb946 -->

This document defines the steps for an operator to deposit to Aave lending pools.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a deposit to an Aave instance.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient underlying asset, and the deposit amount is within instance-specific `RateLimits` (defined in the relevant Aave ICD).
- The Spark Liquidity Layer Operator identifies the `underlying` asset address and Aave `pool` address from the specific Aave ICD.
- The Spark Liquidity Layer Operator approves the Aave `pool` to spend the `underlying` asset from the ALM Proxy.
- The Spark Liquidity Layer Operator calls the `supply(address asset, uint256 amount, address onBehalfOf, uint16 referralCode)` function on the Aave `pool`, providing the `underlying` asset address, `amount`, ALM `proxy` address (as `onBehalfOf`), and referral code (typically 0).
- The ALM Proxy receives `aTokens` representing the deposited assets.
- For detailed call structures, instance-specific parameters (aToken address, underlying asset address, pool address, rate limits), and operational examples, refer to the specific Aave Instance Configuration Document (ICD) (e.g., [A.6.1.1.1.2.6.1.3.1.2.1.3 - Instance-specific Operational Processes](7895798c-50e2-4fa6-b4e9-5b9f259f822d) or other relevant Aave ICDs).

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2 - General Withdraw from Aave ATokens Procedure [Core]  <!-- UUID: 6e75a2bd-70b7-4081-bb9f-39cf6b321066 -->

This document defines the steps for an operator to withdraw from Aave lending pools.

- The Spark Liquidity Layer Operator, acting as `RELAYER`, initiates a withdrawal from an Aave instance.
- Pre-conditions are checked: Spark Liquidity Layer contract `isActive`, ALM Proxy has sufficient `aTokens` for the instance, and the withdrawal amount is within instance-specific `RateLimits` (defined in the relevant Aave ICD).
- The Spark Liquidity Layer Operator identifies the `underlying` asset address and Aave `pool` address from the specific Aave ICD.
- The Spark Liquidity Layer Operator calls the `withdraw(address asset, uint256 amount, address to)` function on the Aave `pool`, providing the `underlying` asset address, `amount` to withdraw, and the ALM `proxy` address (as `to`).
- The amount of underlying assets withdrawn is recorded, and relevant `RateLimits` are updated.
- For detailed call structures, instance-specific parameters, and operational examples, refer to the specific Aave ICD.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4 - PSM Functions [Core]  <!-- UUID: 70785812-c0aa-4efc-8790-093e6c23ef52 -->

The documents herein define the swap operations performed by the Spark Liquidity Layer in the PSM.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1 - Swap USDS to USDC [Core]  <!-- UUID: f6b656c2-dc00-4c07-9452-34b01ef2e1ea -->

The documents herein define a series of operations for an operator to `swap` USDS to USDC through the PSM.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.1 - Relayer Role [Core]  <!-- UUID: a84b5647-13f5-4a47-92fa-a1de76059c31 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapUSDSToUSDC`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function swapUSDSToUSDC(uint256 usdcAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.2 - Check RateLimits [Core]  <!-- UUID: a1dddb9b-93cf-4064-816e-928f761a1239 -->

The operator must ensure that `RateLimits` allows for swapping the required USDS amount to USDC.

`rateLimited(LIMIT_USDS_TO_USDC, usdcAmount)`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.3 - Convert To 18 Token Format [Core]  <!-- UUID: 6eebacbd-ab75-4ecc-ac3b-5ff882dd4037 -->

The operator must convert USDC amounts to an 18 token decimal format using `psmTo18ConversionFactor`.

`{
        uint256 usdsAmount = usdcAmount * psmTo18ConversionFactor;`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.4 - Check ALM Proxy [Core]  <!-- UUID: 01af3b1c-a370-4ede-8f8c-c915a5885591 -->

The operator must ensure that the ALM Proxy has enough USDS balance to `swap` for the required USDC amount.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.5 - Approve Contract Spend [Core]  <!-- UUID: f3f447b4-22c4-4e49-a128-1672c38a2fb9 -->

The operator must approve the `daiUsds` contract to spend the `usdsAmount` on behalf of the `proxy`. `daiUsds` is a contract that facilitates a 1:1 swap between USDS and DAI.

`proxy.doCall(
            address(usds),
            abi.encodeCall(usds.approve, (address(daiUsds), usdsAmount))
        );`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.6 - Swap USDS To DAI [Core]  <!-- UUID: da1d0829-5676-4713-988f-13eea2a6924f -->

The operator must swap USDS to DAI. USDS is swapped to DAI in a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`proxy.doCall(
    address(daiUsds),
    abi.encodeCall(daiUsds.usdsToDai, (address(proxy), usdsAmount))
);`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.7 - Approve PSM Spend [Core]  <!-- UUID: e5b56658-1fe0-4d3f-b911-8e66b9d16a6e -->

The operator must approve the PSM to spend the newly acquired DAI. The approval is needed for the PSM to be able to `swap` DAI for USDC.

`proxy.doCall(
    address(dai),
    abi.encodeCall(dai.approve, (address(psm), usdsAmount))
);`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.1.8 - Swap DAI To USDC [Core]  <!-- UUID: 58bd2f3d-0d7e-41e9-a3f1-43e8deedaea9 -->

The operator must swap DAI to USDC. DAI is swapped to USDC in the PSM at a 1:1 ratio with no fee, using the `buyGemNoFee` function and return USDC to the `proxy`.

`        proxy.doCall(
            address(psm),
            abi.encodeCall(psm.buyGemNoFee, (address(proxy), usdcAmount))
        );
    }`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2 - Swap USDC to USDS [Core]  <!-- UUID: 8b7c4526-ea6a-488d-925a-884704a7bc80 -->

The documents herein define a series of operations for an operator to `swap` USDC to USDS through the PSM.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.1 - Relayer Role [Core]  <!-- UUID: bceb6404-8060-4bb7-86f5-8a5c98f6ebea -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapUSDCToUSDS`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function swapUSDCToUSDS(uint256 usdcAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.2 - Check RateLimits [Core]  <!-- UUID: 084174bc-eaa4-4474-80ca-8a7ab0d21c6e -->

The operator must ensure that `RateLimits` allows for swapping the required USDC amount to USDS.

`cancelRateLimit(LIMIT_USDS_TO_USDC, usdcAmount)`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.3 - Check ALM Proxy [Core]  <!-- UUID: a373fb80-cb38-4564-a386-454604ba5221 -->

The operator must ensure ALM Proxy has enough USDC balance to `swap` for the required USDS amount.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.4 - Approve Contract Spend [Core]  <!-- UUID: b1d47385-8512-475a-8860-9ae927677785 -->

The operator must approve the PSM to spend USDC. The approval is needed for the PSM to be able to execute a `swap` of USDC.

`proxy.doCall(
    address(usdc),
    abi.encodeCall(usdc.approve, (address(psm), usdcAmount))
);`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.5 - Calculate Swap Limit [Core]  <!-- UUID: f16d98d9-dbba-44ab-8764-445693b81ff5 -->

The operator must calculate the `swap` `limit` per transaction. The maximum amount of USDC that can be swapped to DAI in one transaction is calculated based on the DAI balance held by the PSM. `psmTo18ConversionFactor` converts DAI’s 18 token decimals to USDC’s 6 token decimals.

`uint256 limit = dai.balanceOf(address(psm)) / psmTo18ConversionFactor;`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.6 - Swap USDC To DAI Directly If Possible [Core]  <!-- UUID: 6a6ddd58-9215-4dae-9d34-8bd4622720bd -->

The operator must perform a `direct swap` feasibility check and `swap` USDC to DAI, if possible. If the `usdcAmount` is less than or equal to the `limit`, a direct swap should be performed. `_swapUSDCToDAI` is called to execute the swap from `USDC` to `DAI`.

`if (usdcAmount <= limit) {
    _swapUSDCToDAI(usdcAmount);
}`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.7 - Swap USDC To DAI Iteratively If Needed [Core]  <!-- UUID: 38e66872-ee2e-49f4-ada4-a1dec515f6d9 -->

If `direct swap` is not possible, the operator must perform an `iterative swap` of USDC to DAI with DAI `refilling`.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.8 - Split Into Multiple Swaps If Limit Exceeded [Core]  <!-- UUID: 99e4d243-b61f-48b6-b127-b5d1855a849c -->

If the `usdcAmount` exceeds the limit, the operator must split the swap into multiple smaller swaps as follows.

1. The operator must refill the PSM with DAI by calling `psm.fill()`.
2. The operator must recalculate the limit to see how much USDC can be swapped after the refill.
3. The operator must swap the maximum possible USDC amount that doesn't exceed the limit.
4. The operator must update `remainingUsdcToSwap` by subtracting the amount just swapped.
5. The operator must repeat the process until the full `usdcAmount` is swapped.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.9 - Split Into Multiple Swaps If Limit Exceeded [Core]  <!-- UUID: 5b50fe5d-22a9-4ea4-a9e1-de7feba453a3 -->

If the PSM can't be filled, the transaction reverts with `DssLitePsm/nothing-to-fill`.

`else {
    uint256 remainingUsdcToSwap = usdcAmount;

    while (remainingUsdcToSwap > 0) {
        psm.fill();

        limit = dai.balanceOf(address(psm)) / psmTo18ConversionFactor;

        uint256 swapAmount = remainingUsdcToSwap < limit ? remainingUsdcToSwap : limit;

        _swapUSDCToDAI(swapAmount);

        remainingUsdcToSwap -= swapAmount;
    }
}`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.10 - Convert USDC Amount To DAI Amount [Core]  <!-- UUID: 12b79490-4a18-466b-91fc-45f1a966b78a -->

The operator must convert the USDC amount to the DAI amount, accounting for the token decimal difference.

`{
        uint256 daiAmount = usdcAmount * psmTo18ConversionFactor;`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.11 - Approve Contract Spend [Core]  <!-- UUID: 3cf7c26f-7c3b-4d32-8610-b935d57721a6 -->

The operator must approve the `daiUsds` contract to spend the `daiAmount` on behalf of the `proxy`.

`proxy.doCall(
    address(dai),
    abi.encodeCall(dai.approve, (address(daiUsds), daiAmount))
);`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2.12 - Swap DAI to USDS [Core]  <!-- UUID: 25fac618-a634-4762-983d-c3451e690f5f -->

The operator must swap DAI to USDS. DAI is swapped to USDS at a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`proxy.doCall(
            address(daiUsds),
            abi.encodeCall(daiUsds.daiToUsds, (address(proxy), daiAmount))
        );
    }`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5 - Bridging Functions [Core]  <!-- UUID: 36748aac-f4af-4c2d-ae4b-0416bc84b680 -->

The documents herein define the operations performed by an operator to bridge liquidity between Ethereum Mainnet and the destination blockchains for the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1 - Bridge USDC Using Circle Cross-Chain Transfer Protocol [Core]  <!-- UUID: 956f0941-5121-4dce-99d8-2fd1af00ffa6 -->

The documents herein define the process to bridge USDC using the Circle Cross-Chain Transfer Protocol.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.1 - Relayer Role [Core]  <!-- UUID: eb5d0ce2-ae57-4a99-b020-02e611667fbe -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferUSDCToCCTP`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function transferUSDCToCCTP(uint256 usdcAmount, uint32 destinationDomain)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.2 - Check RateLimits [Core]  <!-- UUID: 27da6bef-8e24-4aa5-86fc-9b47f1a896e0 -->

The operator must ensure the bridging transaction complies with `RateLimits`. The `LIMIT_USDC_TO_CCTP` parameter enforces a rate limit on total USDC transferred via CCTP. The `LIMIT_USDC_TO_DOMAIN` parameter enforces a rate limit on USDC transferred to a specific `destinationDomain`.

`rateLimited(LIMIT_USDC_TO_CCTP, usdcAmount)
        rateLimited(
            RateLimitHelpers.makeDomainKey(LIMIT_USDC_TO_DOMAIN, destinationDomain),
            usdcAmount
        )`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.3 - Verify Mint Recipient [Core]  <!-- UUID: 469d9616-010c-4648-8fc4-66eeff7398c3 -->

** **The operator must verify the `mint` recipient. They must check that a mint recipient (mapping from domain IDs to recipient addresses) is configured for the `destinationDomain`. If no recipient is configured, the transaction will revert with an error message.

`bytes32 mintRecipient = mintRecipients[destinationDomain];
require(mintRecipient != 0, "MainnetController/domain-not-configured");`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.4 - Check ALM Proxy [Core]  <!-- UUID: 757267df-e76d-4d58-86e3-218d4e6f9efd -->

The operator must ensure the ALM Proxy has enough USDC to cover the amount instructed in the transfer.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.5 - Approve Contract Spend [Core]  <!-- UUID: f7ef5ebb-e30e-4941-918c-63706690b7e0 -->

The operator must approve the CCTP to spend USDC on behalf of the `proxy`. This action is necessary for the CCTP contract to initiate the cross-chain transfer.

`proxy.doCall(
    address(usdc),
    abi.encodeCall(usdc.approve, (address(cctp), usdcAmount))
);`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6 - Initiate USDC Transfer Through CCTP [Core]  <!-- UUID: ea3d54cc-49af-47e6-a11c-b9055f72db75 -->

The operator must initiate the USDC transfer through CCTP.

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.1 - Check CCTP Transfer Limit [Core]  <!-- UUID: b25fcca3-374b-408d-9715-bb514ee209b1 -->

The operator must check the `transfer limit`. They must retrieve the maximum amount of USDC that can be transferred in a single CCTP message. This limit is fetched from the `localMinter` contract associated with CCTP.

`uint256 burnLimit = cctp.localMinter().burnLimitsPerMessage(address(usdc));`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.2 - Initiate Single Transaction If Possible [Core]  <!-- UUID: 22cb4839-7520-435f-b99b-086446d6a64a -->

If a single transaction is possible within the per-message limit, the operator must initiate the CCTP transfer for the entire USDC amount.

` {
    _initiateCCTPTransfer(usdcAmount, destinationDomain, mintRecipient);
}`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.3 - Initiate Smaller Transactions If Needed [Core]  <!-- UUID: 6423437d-d062-4a4f-ac03-7f056938d3c6 -->

If `usdcAmount` exceeds the per-message limit, the transfer must be split into multiple smaller batches executing the following loop until the remaining amount is less than or equal to the limit.

1. The operator must transfer the maximum allowed (`burnLimit`) using `_initiateCCTPTransfer`.
2. The operator must reduce the remaining `usdcAmount` by the `burnLimit`.

`while (usdcAmount > burnLimit) {
    _initiateCCTPTransfer(burnLimit, destinationDomain, mintRecipient);
    usdcAmount -= burnLimit;
}`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1.6.4 - Send Remaining USDC [Core]  <!-- UUID: fd4f7715-ce73-4906-a9ed-cfdcc905cccb -->

The operator must send the remaining USDC amount (if applicable). If there is any `usdcAmount` left after the loop, they must send the remaining amount in a single transfer, ensuring the entire amount is transferred, even if it didn't divide evenly by the `burnLimit`.

`if (usdcAmount > 0) {
    _initiateCCTPTransfer(usdcAmount, destinationDomain, mintRecipient);
}`

###### A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.2 - Bridge USDS / sUSDS Using OP Token Bridge [Core]  <!-- UUID: 46502b5d-e272-4aca-a979-6dce6f9230d8 -->

This document defines the process for an operator to bridge USDS or sUSDS using the OP Token Bridge. This process will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.2.1.2.2 - Foreign Controller Contract Functions [Core]  <!-- UUID: fc5b3ff6-6458-4e5a-8372-5fada3f51572 -->

The documents herein define the functions controlled by the Controller contract for Spark Liquidity Layer cross-chain operations on a destination blockchain.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.1 - Admin Functions [Core]  <!-- UUID: f8e60eae-5df8-45dc-88d9-52168583686d -->

The documents herein define the operations performed by the `DEFAULT_ADMIN_ROLE` within the `ForeignController` contract.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.1.1 - Set The Mint Recipient [Core]  <!-- UUID: 0388bcfb-e181-45f0-9ef6-ee3d7b5daf34 -->

The documents herein define the process for an operator to set a `mintRecipient` for a specific `destinationDomain`. This is used in cross-chain transfers to specify the address that will receive minted tokens on the target chain.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.1.1.1 - Admin Role [Core]  <!-- UUID: 80c322c2-586d-46be-9421-acdb69cbc622 -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMintRecipient`.

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.1.2.6.1.2.2.1.2.2.1.1.2 - Associate Mint Recipient With Domain [Core]  <!-- UUID: d8c986af-3586-4b01-b03e-eb75cb39bb28 -->

The operator must associate the `mintRecipient` with the `destinationDomain`, meaning that whenever tokens are minted on this domain, they will go to this recipient.

`{
        mintRecipients[destinationDomain] = mintRecipient;`

###### A.6.1.1.1.2.6.1.2.2.1.2.2.1.1.3 - Emit Event To Logs [Core]  <!-- UUID: 1bf12913-0a08-4c83-9b05-7fa576ff8cd6 -->

The operator must emit the event to the blockchain logs.

`        emit MintRecipientSet(destinationDomain, mintRecipient);
    }`

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2 - Relayer Functions [Core]  <!-- UUID: 7c384ca5-6a23-4539-801a-de35adebc1b7 -->

The documents herein define the operations performed by the `RELAYER_ROLE` within the `ForeignController` contract.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.1 - ERC-4626 Functions [Core]  <!-- UUID: f9225946-9172-4013-bd04-5e032a998e05 -->

The documents herein define the operations that are performed to deposit and withdraw liquidity from yield-bearing Integrator vaults.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.1.1 - Deposit to ERC-4626 Vault [Core]  <!-- UUID: 8ffb4820-ae4a-408e-a328-1b1a39d6b374 -->

This document defines the steps to deposit assets from the ALM Proxy to the ERC-4626 vault to receive yield-bearing shares.

The process for depositing to ERC-4626 Tokens on destination blockchain through the `ForeignController` contract is the same as the one for depositing to ERC-4626 Tokens on Ethereum Mainnet through the `MainnetController` contract; see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.1 - General Deposit to ERC-4626 Tokens Procedure](862f4064-47e5-4f76-908d-64edfcfe0ddd).

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.1.2 - Withdraw ERC-4626 Tokens [Core]  <!-- UUID: c2bbf44a-496c-4cf6-b0f6-25f77e66465b -->

This document defines the steps to withdraw a yield-earning balance from the ERC-4626 vault to the ALM Proxy.

The process for withdrawing ERC-4626 Tokens on destination blockchain through the `ForeignController` contract is the same as the one for withdrawing ERC-4626 Tokens on Ethereum Mainnet through the `MainnetController` contract, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.2 - General Withdraw from ERC-4626 Tokens Procedure](e797d1cc-9161-4b7a-8c16-db20a026d001).

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.1.3 - Redeem ERC-4626 Tokens [Core]  <!-- UUID: ab5eb90f-1007-4560-a0ea-1c25d433c602 -->

This document defines the steps for an operator to redeem yield-bearing shares from the ERC-4626 vault, receiving the corresponding amount of underlying assets into the ALM Proxy.

The process for redeeming ERC-4626 Tokens on destination blockchain through the `ForeignController` contract is the same as the one for redeeming ERC-4626 Tokens on Ethereum Mainnet through the `MainnetController` contract, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.3 - General Redeem from ERC-4626 Tokens Procedure](ed774ab7-c761-444b-963d-7407bf91e243).

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.2 - Aave Functions [Core]  <!-- UUID: 652877a2-0d8f-42cf-afef-8721fc988046 -->

The documents herein define the operations that are performed to deposit and withdraw liquidity from yield-bearing Aave deployments.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.2.1 - Deposit to Aave ATokens [Core]  <!-- UUID: 4b3ec104-dc60-4cb0-8e90-5b96c495c974 -->

This document defines the steps to deposit assets from the ALM Proxy to the Aave pool to receive yield-bearing ATokens.

The process for depositing to Aave ATokens on destination blockchain through the `ForeignController` contract is the same as the one for depositing to Aave ATokens on Ethereum Mainnet through the `MainnetController` contract, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.1 - General Deposit to Aave ATokens Procedure](316008c1-0c1f-487a-a5bf-1966e86fb946).

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.2.2 - Withdraw Aave ATokens [Core]  <!-- UUID: 5b090e5a-a2e7-4548-a1b4-53be86db6516 -->

This document defines the steps to withdraw a yield-earning balance from the Aave AToken vaults to the ALM Proxy.

The process for withdrawing Aave ATokens on destination blockchain through the `ForeignController` contract is the same as the one for withdrawing Aave ATokens on Ethereum Mainnet through the `MainnetController` contract, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2 - General Withdraw from Aave ATokens Procedure](6e75a2bd-70b7-4081-bb9f-39cf6b321066).

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.2.3 - Withdraw Aave ATokens [Core]  <!-- UUID: 35cf8ecc-ce16-4498-81f5-d96073ec5724 -->

This document defines the steps to withdraw a yield-earning balance from the Aave AToken vaults to the ALM Proxy.

The process for withdrawing Aave ATokens on destination blockchain through the `ForeignController` contract is the same as the one for withdrawing Aave ATokens on Ethereum Mainnet through the `MainnetController` contract, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2 - General Withdraw from Aave ATokens Procedure](6e75a2bd-70b7-4081-bb9f-39cf6b321066).

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.3 - PSM Functions [Core]  <!-- UUID: 6c18d284-b720-49b4-ac11-904d512fc841 -->

The documents herein define the swap operations that are performed by the Spark Liquidity Layer in the Spark Base PSM.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.3.1 - Deposit Asset Into The PSM [Core]  <!-- UUID: 0328a7f5-d4fd-40a6-a521-4f443687993e -->

The documents herein define a series of operations for an operator to `deposit` an asset into the PSM.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.3.2 - Withdraw The Maximum Amount Of Asset From The PSM [Core]  <!-- UUID: c102ced7-782f-403d-99a8-82d10a089fc7 -->

The documents herein define a series of operations for an operator to `withdraw` an asset from the PSM.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.4 - Bridging Functions [Core]  <!-- UUID: 4621745d-65b3-44e0-9261-004430118551 -->

The documents herein define the operations that are performed to bridge liquidity between the destination blockchain and Ethereum Mainnet for the Spark Liquidity Layer.

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.4.1 - Bridge USDC Using Circle Cross-Chain Transfer Protocol [Core]  <!-- UUID: b871295a-f74a-4bf3-aca7-2bdba2b0292a -->

This document defines the process to bridge USDC using the Circle Cross-Chain Transfer Protocol. The process for bridging USDC using CCTP through the `ForeignController` contract is the same as the one for bridging USDC using CCTP through the `MainnetController` contract; see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1 - Bridge USDC Using Circle Cross-Chain Transfer Protocol](956f0941-5121-4dce-99d8-2fd1af00ffa6).

###### A.6.1.1.1.2.6.1.2.2.1.2.2.2.4.2 - Bridge USDS / sUSDS using OP Token Bridge [Core]  <!-- UUID: 5fe16ede-05e3-48eb-b43a-e4ea84d86e25 -->

The documents herein define the process to bridge USDS / sUSDS using the OP Token Bridge. This process will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.2.1.3 - Rate Limit Management [Core]  <!-- UUID: 554a654f-930a-419e-a8a4-f49dd5599ee8 -->

The documents herein define the protocol for querying, setting, and adjusting `RateLimits` for Instances using their `RateLimitID`s. The ratelimits must be maintained in line with Spark’s strategy, market conditions, and security considerations.

###### A.6.1.1.1.2.6.1.2.2.1.3.1 - RateLimits Query [Core]  <!-- UUID: 89577062-a38b-4cf7-a1ae-33c0bcff1cca -->

The following code sets out instructions for the operator to query the current `RateLimits` for a specific key:

`Function getRateLimitData(bytes32 key) external override view returns (RateLimitData memory) {
        return _data[key];
    }

    function getCurrentRateLimit(bytes32 key) public override view returns (uint256) {
        RateLimitData memory d = _data[key];

        // Unlimited rate limit case
        if (d.maxAmount == type(uint256).max) {
            return type(uint256).max;
        }

        return _min(
            d.slope * (block.timestamp - d.lastUpdated) + d.lastAmount,
            d.maxAmount
        );
    }`

###### A.6.1.1.1.2.6.1.2.2.1.3.2 - Set RateLimit [Core]  <!-- UUID: 24e955c5-4555-41f5-b4f3-e9bcf6baf0e9 -->

The following code sets out instructions for the operator to set the `RateLimit` for a specific key:

`function setRateLimitData(
        bytes32 key,
        uint256 maxAmount,
        uint256 slope,
        uint256 lastAmount,
        uint256 lastUpdated
    )
        public override onlyRole(DEFAULT_ADMIN_ROLE)
    {
        require(lastAmount  <= maxAmount,       "RateLimits/invalid-lastAmount");
        require(lastUpdated <= block.timestamp, "RateLimits/invalid-lastUpdated");

        _data[key] = RateLimitData({
            maxAmount:   maxAmount,
            slope:       slope,
            lastAmount:  lastAmount,
            lastUpdated: lastUpdated
        });

        emit RateLimitDataSet(key, maxAmount, slope, lastAmount, lastUpdated);
    }

    function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope) external override {
        setRateLimitData(key, maxAmount, slope, maxAmount, block.timestamp);
    }`

###### A.6.1.1.1.2.6.1.2.2.1.3.3 - Set Unlimited RateLimit [Core]  <!-- UUID: 241dde83-2f9b-486d-be55-19895291c183 -->

The following code sets out instructions for the operator to set an unlimited `RateLimit` for a specific key:

`function setUnlimitedRateLimitData(bytes32 key) external override {
        setRateLimitData(key, type(uint256).max, 0, type(uint256).max, block.timestamp);`

###### A.6.1.1.1.2.6.1.2.2.1.3.4 - Set Trigger For RateLimit Decrease [Core]  <!-- UUID: c58e3657-404b-40f7-b83e-26063d908155 -->

The following code sets out instructions for the operator to trigger a decrease of a `RateLimit` for a specific key:

`function triggerRateLimitDecrease(bytes32 key, uint256 amountToDecrease)
        external override onlyRole(CONTROLLER) returns (uint256 newLimit)
    {
        RateLimitData storage d = _data[key];
        uint256 maxAmount = d.maxAmount;

        require(maxAmount > 0, "RateLimits/zero-maxAmount");
        if (maxAmount == type(uint256).max) return type(uint256).max;  // Special case unlimited

        uint256 currentRateLimit = getCurrentRateLimit(key);

        require(amountToDecrease <= currentRateLimit, "RateLimits/rate-limit-exceeded");

        d.lastAmount = newLimit = currentRateLimit - amountToDecrease;
        d.lastUpdated = block.timestamp;

        emit RateLimitDecreaseTriggered(key, amountToDecrease, currentRateLimit, newLimit);
    }`

###### A.6.1.1.1.2.6.1.2.2.1.3.5 - Set Trigger For RateLimit Increase [Core]  <!-- UUID: 873c7ba8-1bff-451f-8987-0c21a62c6993 -->

The following code sets out instructions for the operator to trigger an increase of a `RateLimit` for a specific key:

`function triggerRateLimitIncrease(bytes32 key, uint256 amountToIncrease)
        external override onlyRole(CONTROLLER) returns (uint256 newLimit)
    {
        RateLimitData storage d = _data[key];
        uint256 maxAmount = d.maxAmount;

        require(maxAmount > 0, "RateLimits/zero-maxAmount");
        if (maxAmount == type(uint256).max) return type(uint256).max;  // Special case unlimited

        uint256 currentRateLimit = getCurrentRateLimit(key);

        d.lastAmount = newLimit = _min(currentRateLimit + amountToIncrease, maxAmount);
        d.lastUpdated = block.timestamp;

        emit RateLimitIncreaseTriggered(key, amountToIncrease, currentRateLimit, newLimit);`

###### A.6.1.1.1.2.6.1.2.2.1.4 - Instance Lifecycle Management [Core]  <!-- UUID: edbc0297-0640-4833-9e15-b0e4bce960b8 -->

The documents herein define processes for invoking (onboarding) new Spark Liquidity Layer Instances and offboarding existing ones. This process will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.2.1.5 - Upgrading Controller [Core]  <!-- UUID: 438042de-d556-4ea6-9434-cb4c070481d0 -->

The documents herein define the process for deploying new Controller contracts. This process will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 00cebdd9-db63-4ddb-95e0-93b4dc456be7 -->

The documents herein define the process for non-routine ongoing management of the Spark Liquidity Layer and its active Instances.

###### A.6.1.1.1.2.6.1.2.2.3 - Emergency Protocol [Core]  <!-- UUID: 0b96f0e0-e490-4b4c-a65f-5625f9352aaa -->

The documents herein define all the possible actions that can be taken in case of an emergency within Spark Liquidity Layer operations.

###### A.6.1.1.1.2.6.1.2.2.3.1 - Remove Compromised Relayer As Freezer [Core]  <!-- UUID: 7bd4a4cc-315b-4365-a793-923cd4aaacff -->

In the event of a compromised Relayer, the `FREEZER_ROLE` can call the function to `removeRelayer` from the Controller contract. This function takes an address, and then the Freezer can remove the compromised Relayer, thereby preventing it from doing any harm to the system. The backstop relayer can then take over. This function should only be used if the keys to the relayer multisig have been leaked or compromised, and the relayer is now in the hands of an external bad actor.

`mainnetController.removeRelayer(compromisedRelayer)`

###### A.6.1.1.1.2.6.1.2.2.3.2 - Redeem All L2 Positions [Core]  <!-- UUID: 962b1da7-0f80-4abc-a7a9-ef229b0f1c13 -->

The documents herein list the actions that should be performed by an operator if there is a need to recover the liquidity from L2 Protocols and centralize it in the L2 Spark ALM Proxy.

###### A.6.1.1.1.2.6.1.2.2.3.2.1 - ERC-4626 Withdrawal Action [Core]  <!-- UUID: aad3683d-38d4-4e94-b2bf-88b408c2290e -->

In order to withdraw all ERC-4626 balances, the operator must execute the following action:

`foreignController.redeemERC4626(address(token), token.balanceOf(address(proxy)))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.2.2.1.2 - Withdraw ERC-4626 Tokens](c2bbf44a-496c-4cf6-b0f6-25f77e66465b) and [A.6.1.1.1.2.6.1.2.2.1.2.2.2.1.3 - Redeem ERC-4626 Tokens](ab5eb90f-1007-4560-a0ea-1c25d433c602).

###### A.6.1.1.1.2.6.1.2.2.3.2.2 - ERC-4626 Withdrawal Action [Core]  <!-- UUID: 29bb82e9-a308-448f-ace1-e8b0397a0995 -->

[A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.3 - General Redeem from ERC-4626 Tokens Procedure](ed774ab7-c761-444b-963d-7407bf91e243)

###### A.6.1.1.1.2.6.1.2.2.3.2.3 - Aave AToken Withdrawal Action [Core]  <!-- UUID: 2560adbb-4a5c-4c95-86cb-04647bb33836 -->

In order to withdraw all AToken balances, the operator must execute the following action:

`foreignController.withdrawAave(aToken, aToken.balanceOf(address(proxy)))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.2.2.2.2 - Withdraw Aave ATokens](5b090e5a-a2e7-4548-a1b4-53be86db6516).

###### A.6.1.1.1.2.6.1.2.2.3.2.4 - Aave AToken Withdrawal Action [Core]  <!-- UUID: c1f708eb-7373-448d-a54c-b178d0fd909a -->

In order to withdraw all AToken balances, the operator must execute the following action:

`foreignController.withdrawAave(aToken, aToken.balanceOf(address(proxy))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2 - General Withdraw from Aave ATokens Procedure](6e75a2bd-70b7-4081-bb9f-39cf6b321066).

###### A.6.1.1.1.2.6.1.2.2.3.2.5 - All PSM Assets Withdrawal Action [Core]  <!-- UUID: 3bd03154-f7f0-408e-b3bf-654aaaf7e8cf -->

In order to withdraw all Assets from the PSM, the operator must execute the following action:

`foreignController.withdrawPSM(address(usdc), type(uint256).max)
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.2.2.3.2 - Withdraw The Maximum Amount Of Asset From The PSM](c102ced7-782f-403d-99a8-82d10a089fc7).

###### A.6.1.1.1.2.6.1.2.2.3.3 - Bridge Liquidity From L2 ALM Proxy To Mainnet [Core]  <!-- UUID: c4ed7a34-4c1c-43ec-8eb2-7285c9a46184 -->

The documents herein define the actions that should be performed by an operator if there is a need to bring all liquidity from the Spark ALM Proxy on the destination domain to the Spark ALM Proxy on Ethereum Mainnet.

###### A.6.1.1.1.2.6.1.2.2.3.3.1 - USDC Bridging Action [Core]  <!-- UUID: 3c47986f-3a20-4593-b4c1-cd5f8a0837c8 -->

In order to bridge USDC, the operator must execute the following action:

`foreignController.transferUSDCToCCTP(usdc.balanceOf(address(proxy)), 0);
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.5.1 - Bridge USDC Using Circle Cross-Chain Transfer Protocol](956f0941-5121-4dce-99d8-2fd1af00ffa6).

###### A.6.1.1.1.2.6.1.2.2.3.3.2 - USDS and sUSDS Bridging Action [Core]  <!-- UUID: 188124a1-32fe-4ed3-90bb-1774cbcf18c5 -->

The function to bridge USDS and sUSDS is currently actioned by an Executive Vote by Sky Governance. This process will be managed by the operator of the Spark Liquidity Layer in the future.

###### A.6.1.1.1.2.6.1.2.2.3.4 - Redeem All Mainnet Positions [Core]  <!-- UUID: 77067d73-922a-45e1-9f74-2b6947108d3b -->

The documents herein define the actions that should be performed by an operator if there is a need to recover the liquidity from Mainnet Protocols and centralize it in the Mainnet Spark ALM Proxy.

###### A.6.1.1.1.2.6.1.2.2.3.4.1 - ERC-4626 Withdrawal Action [Core]  <!-- UUID: f92ddc3f-672a-4f52-931f-5263a9f709b9 -->

In order to withdraw all ERC-4626 balances, the operator must execute the following action:

`mainnetController.redeemERC4626(address(token), token.balanceOf(address(proxy)))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.2 - General Withdraw from ERC-4626 Tokens Procedure](e797d1cc-9161-4b7a-8c16-db20a026d001) and [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.3 - General Redeem from ERC-4626 Tokens Procedure](ed774ab7-c761-444b-963d-7407bf91e243).

###### A.6.1.1.1.2.6.1.2.2.3.4.2 - ERC-4626 Withdrawal Action [Core]  <!-- UUID: eb2056e5-2987-45fc-bb7d-453f09a3d5b7 -->

[A.6.1.1.1.2.6.1.2.2.1.2.1.2.2.3 - General Redeem from ERC-4626 Tokens Procedure](ed774ab7-c761-444b-963d-7407bf91e243)

###### A.6.1.1.1.2.6.1.2.2.3.4.3 - Aave AToken Withdrawal Action [Core]  <!-- UUID: 09de757a-e742-4061-a1d4-7e5d70e9c0df -->

In order to withdraw all Aave AToken balances, the operator must execute the following action:

`mainnetController.withdrawAave(aToken, aToken.balanceOf(address(proxy))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3.2 - General Withdraw from Aave ATokens Procedure](6e75a2bd-70b7-4081-bb9f-39cf6b321066).

###### A.6.1.1.1.2.6.1.2.2.3.5 - USDC to USDS Swap Action [Core]  <!-- UUID: 62bf500a-56be-4766-8390-c6c1aaa4aeb9 -->

This document defines the action that should be performed by an operator if there is a need to centralize all recovered liquidity in USDS.

`mainnetController.swapUSDCToUSDS(usdc.balanceOf(address(proxy))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.4.2 - Swap USDC to USDS](8b7c4526-ea6a-488d-925a-884704a7bc80).

###### A.6.1.1.1.2.6.1.2.2.3.6 - USDS Burn Action [Core]  <!-- UUID: dadf134c-5faa-4dfb-b31b-62f0bacc9519 -->

This document defines the action that should be performed if there is a need to repay and then burn Spark’s USDS debt.

`mainnetController.burnUSDS(usds.balanceOf(address(proxy))
`
More detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS](fc8b57fd-c0c8-422d-b0a9-e124b3cac439).

###### A.6.1.1.1.2.6.1.2.3 - Allocation Strategy [Core]  <!-- UUID: 138f0270-4aa7-41c4-9a00-c4c661d2d426 -->

In the future, additional logic will be added herein regarding the strategy by which capital is allocated between different Instances of the Spark Liquidity Layer.

##### A.6.1.1.1.2.6.1.3 - Active Instances [Core]  <!-- UUID: f7c9fdda-3d42-4b9d-852d-610d7ae4f6c0 -->

The Instances of the Spark Liquidity Layer with `Active` Status are stored herein. The `RRC Framework Full Implementation` status defines whether the Instance Financial RRC is calculated based on a fully implemented risk model (see [A.3.2.1.1.4.3.1 - Fully Implemented Risk Models](419a1d00-fbae-4d26-bd47-8f57677d8001)) or a pending risk model (see [A.3.2.1.1.4.3.2 - Pending Risk Models](81ca88bf-3f6a-4d10-a3e2-d47cf6636d7d)). If the Instance Financial RRC is calculated based on a fully implemented risk model the status is `Covered`. If the Instance Financial RRC is calculated based on a pending risk model the status is `Pending`.

###### A.6.1.1.1.2.6.1.3.1 - Ethereum Mainnet Instances [Core]  <!-- UUID: cce62366-93d3-4856-9dcb-d700695a8a96 -->

The Ethereum Mainnet Instances of the Spark Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.1.2.6.1.3.1.1 - SparkLend [Core]  <!-- UUID: 1fdebcff-990a-40ac-8db6-8ef993edd57a -->

The Ethereum Mainnet Instances of the SparkLend Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.1.1 - Ethereum Mainnet - SparkLend USDS Instance Configuration Document [Core]  <!-- UUID: 4940f6ee-28e8-47a8-a7df-f2b30bd7dcc2 -->

The documents herein contain the Instance Configuration Document for the SparkLend USDS Instance.

###### A.6.1.1.1.2.6.1.3.1.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 56203f5d-8205-48ac-a278-66218fda9c2e -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.1.1.2 - Parameters [Core]  <!-- UUID: e79d6215-c40b-45c1-9660-eda89b17325e -->

The documents herein define the parameters of the SparkLend USDS Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 813cf6b5-ee1b-4767-a05b-4cf03c0bd37f -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.1.1.2.1.1 - Network [Core]  <!-- UUID: 8a6a8cf9-289d-42e1-842c-dcb722b6225c -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 403b96e6-977f-4eaf-91e3-d9c6a9cb9b2f -->

SparkLend Protocol

###### A.6.1.1.1.2.6.1.3.1.1.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: ab86175c-e81a-41b0-98cb-e35971d08363 -->

USDS

###### A.6.1.1.1.2.6.1.3.1.1.1.2.1.4 - Token [Core]  <!-- UUID: 65988a53-f492-49b6-b693-6e98f82b2c29 -->

spUSDS

###### A.6.1.1.1.2.6.1.3.1.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 02bf0b42-0993-431f-af52-3b1f7e0c3675 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.1.1.2.2.1 - Token Address [Core]  <!-- UUID: a8171359-d11e-4014-bd9b-ef19712e556d -->

`0xC02aB1A5eaA8d1B114EF786D9bde108cD4364359`

###### A.6.1.1.1.2.6.1.3.1.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: aeb1bcc7-1214-4544-b686-687d1bb2fa70 -->

`0xdC035D45d973E3EC169d2276DDab16f1e407384F`

###### A.6.1.1.1.2.6.1.3.1.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 66b08d31-c12e-401b-8270-6e1aeb445140 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 85106bf0-7367-4355-acf1-5fb22199d135 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 4fae5f20-61df-4df3-8018-2be0a287de79 -->

The inflow rate limits are:

- `maxAmount`: 200,000,000 USDS
- `slope`: 400,000,000 USDS per day

###### A.6.1.1.1.2.6.1.3.1.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: e2216e6c-7075-464e-9df6-98b02d8ee4a0 -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 26826191-9e5c-4337-b274-43d064d7a63a -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 1cc294ee-5bea-41c8-ac48-deb47aa95ec6 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.1.2 - Ethereum Mainnet - SparkLend USDC Instance Configuration Document [Core]  <!-- UUID: 7cd0ec35-9449-48ce-a764-454ed33e72de -->

The documents herein contain the Instance Configuration Document for the SparkLend USDC Instance.

###### A.6.1.1.1.2.6.1.3.1.1.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 404340ff-76f9-44fd-9c05-7a4f36780e71 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.1.2.2 - Parameters [Core]  <!-- UUID: 62cae553-442b-4a02-a550-b11c318fa124 -->

The documents herein define the parameters of the SparkLend USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.1.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 639e838f-8153-446d-8e1b-80d16c7c7495 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.1.2.2.1.1 - Network [Core]  <!-- UUID: f81f92a6-e867-4713-8d75-bb65407f8c4a -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.1.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 33ff048b-1c73-449a-af30-ebb5261d5bf1 -->

SparkLend Protocol

###### A.6.1.1.1.2.6.1.3.1.1.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: bc4fbbb2-eacc-40bb-8197-da8f3ae38db9 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.1.2.2.1.4 - Token [Core]  <!-- UUID: aee5e636-70e0-4fd9-b52a-814a7bac123c -->

spUSDC

###### A.6.1.1.1.2.6.1.3.1.1.2.2.2 - Contract Addresses [Core]  <!-- UUID: e5440caf-87d0-4e09-a5f9-1736f2c6e55f -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.1.2.2.2.1 - Token Address [Core]  <!-- UUID: de211b16-8d7a-4560-9cb9-52a98941fb43 -->

`0x377C3bd93f2a2984E1E7bE6A5C22c525eD4A4815`

###### A.6.1.1.1.2.6.1.3.1.1.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: c78afa3b-9e4b-4c25-a85f-28492d7729aa -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.1.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 6b9ef39f-99f9-4dad-b687-f397f5f36b64 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.1.2.2.4 - Rate Limits [Core]  <!-- UUID: 969d566b-46b5-41ad-8317-0bc4b8981c6a -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.1.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 4e05fefc-c013-4f04-8173-7f96cdb90d1e -->

The inflow rate limits are:

- `maxAmount`: 100,000,000 USDC
- `slope`: 200,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.1.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: ff880422-b0e0-401d-8d01-e541f7643ffc -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.1.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: e3ffdba1-d90d-4c9e-a0b7-3ba14293ec41 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.1.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 0e700537-6981-4b70-bca5-08937cf30f73 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.1.3 - Ethereum Mainnet - SparkLend Dai Instance Configuration Document [Core]  <!-- UUID: 7e8135d5-7b45-48a7-bf9a-881f0bbf115c -->

The documents herein contain the Instance Configuration Document for the SparkLend Dai Instance.

###### A.6.1.1.1.2.6.1.3.1.1.3.1 - RRC Framework Full Implementation [Core]  <!-- UUID: a0131763-e837-4a90-a3e7-710c5a2068d9 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.1.3.2 - Parameters [Core]  <!-- UUID: 92a92ef9-daa9-4285-814a-697a36d55997 -->

The documents herein define the parameters of the SparkLend Dai Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.1.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 3c64b11d-c123-48de-ba91-97e9c2f461e7 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.1.3.2.1.1 - Network [Core]  <!-- UUID: 2c800a97-c0a8-4ddd-8e03-b149b779bd9a -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.1.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 9a89ca9d-4351-4ff7-9a3a-99728545846f -->

SparkLend Protocol

###### A.6.1.1.1.2.6.1.3.1.1.3.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: bffaf20b-5502-42c8-9c15-25bec3816430 -->

Dai

###### A.6.1.1.1.2.6.1.3.1.1.3.2.1.4 - Token [Core]  <!-- UUID: 85b21780-1fcf-4a91-a5f8-4d0d301e5de5 -->

spDai

###### A.6.1.1.1.2.6.1.3.1.1.3.2.2 - Contract Addresses [Core]  <!-- UUID: 2d82fc81-ed61-4097-a122-5ab0a0c34e3c -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.1.3.2.2.1 - Token Address [Core]  <!-- UUID: edbdeb06-4b87-4dd6-960a-cba704f7bf94 -->

`0x4DEDf26112B3Ec8eC46e7E31EA5e123490B05B8B`

###### A.6.1.1.1.2.6.1.3.1.1.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 388c73f9-17cc-4518-9af9-4bc619963172 -->

`0x6B175474E89094C44Da98b954EedeAC495271d0F`

###### A.6.1.1.1.2.6.1.3.1.1.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: f8225872-d517-40f1-a931-241b5d0cc07b -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.1.3.2.4 - Rate Limits [Core]  <!-- UUID: ec3317a7-e330-45a8-a797-9c8f4bf3b606 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.1.3.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 381c40f3-008e-4541-81c7-6192a186def7 -->

The inflow rate limits are:

- `maxAmount`: 100,000,000 DAI
- `slope`: 50,000,000 DAI per day

###### A.6.1.1.1.2.6.1.3.1.1.3.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 101cf682-0eda-4e40-81e0-601e3d2895aa -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.1.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 69f08826-c669-4407-84b4-bade022c2357 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.1.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 9427c9de-cc7b-4ea0-ad1f-d1ceb6d7e866 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.1.4 - Ethereum Mainnet - SparkLend USDT Instance Configuration Document [Core]  <!-- UUID: dbd8d0fc-d055-415c-a7ef-4796c5e33a87 -->

The documents herein contain the Instance Configuration Document for the SparkLend USDT Instance.

###### A.6.1.1.1.2.6.1.3.1.1.4.1 - RRC Framework Full Implementation [Core]  <!-- UUID: cf25dc95-3f66-47aa-854e-25e54e56f855 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.1.4.2 - Parameters [Core]  <!-- UUID: 7dbcc194-323c-41ff-b5ef-31fc104fb2e2 -->

The documents herein define the parameters of the SparkLend USDT Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.1.4.2.1 - Instance Identifiers [Core]  <!-- UUID: c1116956-306b-4b51-afcd-bf0e895ea738 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.1.4.2.1.1 - Network [Core]  <!-- UUID: adfe7e8c-3626-4168-a422-59bb008df5f5 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.1.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 3514f1da-184b-4c4a-bb28-7e5bf98136d3 -->

SparkLend Protocol

###### A.6.1.1.1.2.6.1.3.1.1.4.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: fe96e727-c44b-4c2d-93bf-bdff1ae10373 -->

USDT

###### A.6.1.1.1.2.6.1.3.1.1.4.2.1.4 - Token [Core]  <!-- UUID: 86c2b46c-afa4-456a-a261-fc20c9840441 -->

spUSDT

###### A.6.1.1.1.2.6.1.3.1.1.4.2.2 - Contract Addresses [Core]  <!-- UUID: a657da06-c319-4b61-9e2c-f09e383672f9 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.1.4.2.2.1 - Token Address [Core]  <!-- UUID: 85a280c2-a45d-4e67-ab6e-7cdcf5746106 -->

`0xe7dF13b8e3d6740fe17CBE928C7334243d86c92f`

###### A.6.1.1.1.2.6.1.3.1.1.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: a7f5e722-e39c-4f9c-be0d-c43484cc18ae -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.1.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: 2857a038-a0c7-41e5-b547-8a067a854155 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.1.4.2.4 - Rate Limits [Core]  <!-- UUID: 3662bfb6-2730-40f3-bdb2-7944e5f591ad -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.1.4.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 4a4f3cb4-fc31-4901-b684-c26234dca7bb -->

The inflow rate limits are:

- `maxAmount`: 500,000,000 USDT
- `slope`: 2,000,000,000 USDT per day

###### A.6.1.1.1.2.6.1.3.1.1.4.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: dadcd267-a47c-4bc0-9216-98369b470b72 -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.1.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 126b8574-c161-4c0e-b7a6-a5ceb032a395 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.1.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 9c6b2c92-ede8-43a8-8a17-25617429e4f0 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.1.5 - Ethereum Mainnet - SparkLend pyUSD Instance Configuration Document [Core]  <!-- UUID: 84a0c43e-b64b-4018-bb2c-3d5c5a635c03 -->

The documents herein contain the Instance Configuration Document for the SparkLend pyUSD Instance.

###### A.6.1.1.1.2.6.1.3.1.1.5.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 26b618a9-205b-4eca-9592-1491108ece2e -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.1.5.2 - Parameters [Core]  <!-- UUID: 2ce01191-6e84-46b2-ac07-0c368829b638 -->

The documents herein define the parameters of the SparkLend pyUSD Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.1.5.2.1 - Instance Identifiers [Core]  <!-- UUID: 1645641e-bf06-4d30-b7e4-71f79feb46ab -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.1.5.2.1.1 - Network [Core]  <!-- UUID: 9562ff84-c0b8-4a19-b6be-7e0f40b7613d -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.1.5.2.1.2 - Target Protocol [Core]  <!-- UUID: 40994499-298a-4f7b-af05-e22688b729f5 -->

SparkLend Protocol

###### A.6.1.1.1.2.6.1.3.1.1.5.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: f4c28b2b-3c0a-4356-b7d7-3132833a7d67 -->

pyUSD

###### A.6.1.1.1.2.6.1.3.1.1.5.2.1.4 - Token [Core]  <!-- UUID: 8e4fe4a2-bc78-4d01-bd3d-668bbb247353 -->

sppyUSD

###### A.6.1.1.1.2.6.1.3.1.1.5.2.2 - Contract Addresses [Core]  <!-- UUID: 4dfb8749-96b0-42f7-80fb-0683f915aeb0 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.1.5.2.2.1 - Token Address [Core]  <!-- UUID: 9730bb57-1bab-44c2-bdfb-805b992d53d0 -->

`0x779224df1c756b4EDD899854F32a53E8c2B2ce5d`

###### A.6.1.1.1.2.6.1.3.1.1.5.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: af95c4ee-4010-436b-8717-c747f5a46d96 -->

`0x6c3ea9036406852006290770BEdFcAbA0e23A0e8`

###### A.6.1.1.1.2.6.1.3.1.1.5.2.3 - Rate Limit IDs [Core]  <!-- UUID: 9c845059-1b83-4b6c-b823-1e686fc7593e -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.1.5.2.4 - Rate Limits [Core]  <!-- UUID: abaee24f-40a5-4584-8525-7363e7a7eb46 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.1.5.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: be156d9d-6c3b-4694-b598-0beb95ee57e9 -->

The inflow rate limits are:

- `maxAmount`: 100,000,000 pyUSD
- `slope`: 100,000,000 pyUSD per day

###### A.6.1.1.1.2.6.1.3.1.1.5.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 42fbe675-1c41-432c-93cc-67fe79e2718d -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.1.5.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 74c6841c-6608-4673-9baa-ffea94f9f699 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.1.5.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 82a7b2ed-f831-45b5-a888-35ace26aa267 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.1.6 - Ethereum Mainnet - SparkLend ETH Instance Configuration Document [Core]  <!-- UUID: 1eb4affe-3116-4d17-a3c1-0a06b6ac618b -->

The documents herein contain the Instance Configuration Document for the SparkLend ETH Instance.

###### A.6.1.1.1.2.6.1.3.1.1.6.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 230d8210-e3a2-41d7-8fcc-957f44d9f296 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.1.6.2 - Parameters [Core]  <!-- UUID: a128bf36-a93a-4fc0-aee3-36ff07d542bd -->

The documents herein define the parameters of the SparkLend ETH Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.1.6.2.1 - Instance Identifiers [Core]  <!-- UUID: ec1c764c-f37d-4090-9504-ba4a1f9e74e2 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.1.6.2.1.1 - Network [Core]  <!-- UUID: faa97600-1a42-4d8e-a020-398eef686d5c -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.1.6.2.1.2 - Target Protocol [Core]  <!-- UUID: 8aa492e2-95b4-4806-92b8-626da4d66f96 -->

SparkLend Protocol

###### A.6.1.1.1.2.6.1.3.1.1.6.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: c1c7c252-219c-4cfe-a9c0-998e0520afce -->

wETH

###### A.6.1.1.1.2.6.1.3.1.1.6.2.1.4 - Token [Core]  <!-- UUID: 8356bb07-85ee-41a0-a1a7-4071c37dd5a7 -->

spwETH

###### A.6.1.1.1.2.6.1.3.1.1.6.2.2 - Contract Addresses [Core]  <!-- UUID: 65dd7b46-41e4-4f5e-8f32-ccecf58bf5c2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.1.6.2.2.1 - Token Address [Core]  <!-- UUID: fa19fb59-fb98-4082-826b-649ce7cdc037 -->

`0x59cD1C87501baa753d0B5B5Ab5D8416A45cD71DB`

###### A.6.1.1.1.2.6.1.3.1.1.6.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 3267c66e-aefa-48ec-8f76-62e50eddd1b4 -->

`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`

###### A.6.1.1.1.2.6.1.3.1.1.6.2.3 - Rate Limit IDs [Core]  <!-- UUID: 70bf8d47-0bb2-4650-8830-1d5856eef740 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.1.6.2.3.1 - Inflow Rate Limit ID [Core]  <!-- UUID: 22d5d878-bed1-4918-b9e3-fc3b00c56204 -->

The inflow RateLimitID is: `0xfd90d9b1f97fedb7eab52e6be9ba5c54b48164e3bef7f0fade829e807354da77`

###### A.6.1.1.1.2.6.1.3.1.1.6.2.3.2 - Outflow Rate Limit ID [Core]  <!-- UUID: 27e77ee3-b59b-4c8b-a729-741627952fb3 -->

The outflow RateLimitID is: `0x2373d5805bbf5d42574ae53a80e39a0bb90f497f312ccf0b96de71fc6f980909`

###### A.6.1.1.1.2.6.1.3.1.1.6.2.4 - Rate Limits [Core]  <!-- UUID: 3ef61462-8f74-4b84-ac42-8b847714b9e8 -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.1.6.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: c8320b60-3cf3-4047-aad1-e12cc6ca46f8 -->

The inflow rate limits are:

- `maxAmount`: 50,000 ETH
- `slope`: 250,000 ETH per day

###### A.6.1.1.1.2.6.1.3.1.1.6.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 68716e71-a257-4f6c-b227-fba7abc8ec31 -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.1.6.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: ab2d6946-b18e-4199-a27c-61f44dd1fe7a -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.1.6.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 1f909758-9b95-4e50-ba97-4688157d02a5 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.2 - Aave [Core]  <!-- UUID: 85b11a45-1718-4ed3-9c64-1471d0887e63 -->

The Ethereum Mainnet Instances of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.2.1 - Ethereum Mainnet - Aave Prime USDS Instance Configuration Document [Core]  <!-- UUID: bf8743ff-bd2e-4fb4-9b2f-2989f0361697 -->

The documents herein contain the Instance Configuration Document for the Aave Prime USDS Instance.

###### A.6.1.1.1.2.6.1.3.1.2.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: a11b86fd-7f8b-413f-9e38-99041fa877a2 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.2.1.2 - Parameters [Core]  <!-- UUID: 4ff0a9da-8ac6-4b83-882c-8df9602ab191 -->

The documents herein define the parameters of the Aave Prime USDS Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 8f7cadc9-b03e-46ac-a8ea-611777540ef6 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.2.1.2.1.1 - Network [Core]  <!-- UUID: e10e7d15-186e-4f26-9746-cf26d0546a19 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 1eb3724b-92f7-463a-81a4-6ef14a518383 -->

Aave Prime

###### A.6.1.1.1.2.6.1.3.1.2.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 27e2624c-a0c4-449c-9a04-c08225c1155b -->

USDS

###### A.6.1.1.1.2.6.1.3.1.2.1.2.1.4 - Token [Core]  <!-- UUID: 81123b01-7547-4ad2-a82c-7ee496445525 -->

aEthLidoUSDS

###### A.6.1.1.1.2.6.1.3.1.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: afd62e51-3af1-40d6-8918-72c3b7fb95ab -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.2.1.2.2.1 - Token Address [Core]  <!-- UUID: 5c10f62b-25cc-4daf-877c-36f9291d585d -->

`0x09AA30b182488f769a9824F15E6Ce58591Da4781`

###### A.6.1.1.1.2.6.1.3.1.2.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 6a4979e7-46f8-49ce-acbe-fa8b28d2693a -->

`0xdC035D45d973E3EC169d2276DDab16f1e407384F`

###### A.6.1.1.1.2.6.1.3.1.2.1.2.2.3 - Pool [Core]  <!-- UUID: c358ae91-bc20-4c39-9a31-7f867fab56e4 -->

This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.2.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 7e6afc3c-5c09-4ca4-9c2c-05aa9ed85e67 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.2.1.2.4 - Rate Limits [Core]  <!-- UUID: 46a1c28f-f4e4-4c45-9a89-1d88b50bf57b -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.2.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 4ed25455-3128-4395-9b58-cf24e275498c -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.1.2.6.1.3.1.2.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 6dc14672-e655-49fd-a351-45537408c74b -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 25a46c53-dca4-43ef-876a-64b5cea91fb6 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 7895798c-50e2-4fa6-b4e9-5b9f259f822d -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes. For the general operational procedures applicable to all Aave-type instances. See [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3 - Aave Functions](9922dcf0-4562-445b-9a46-712f677cce64) and [A.6.1.1.1.2.6.1.2.2.3.2.3 - Aave AToken Withdrawal Action](2560adbb-4a5c-4c95-86cb-04647bb33836).

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1 - Process Definition For Depositing [Core]  <!-- UUID: fa2520ac-4779-4aeb-abe4-2c1b89e7ca51 -->

The documents herein define the steps to deposit assets from the ALM Proxy to the Aave pool to receive yield-bearing ATokens.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.1 - Relayer Role [Core]  <!-- UUID: 25fd8f89-cb76-464e-b659-e2e1885ac4c5 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `depositAave`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function depositAave(address aToken, uint256 amount)
external
onlyRole(RELAYER)
isActive`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.2 - Check ALM Proxy [Core]  <!-- UUID: d3977382-1434-4958-8910-b0f61a5aecc7 -->

The operator must ensure ALM Proxy holds enough of the underlying asset to cover the instructed `deposit` amount.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.3 - Check RateLimits [Core]  <!-- UUID: bda7b89b-9065-4fa0-b7c1-903ef0b9a41b -->

The operator must ensure the `deposit` amount is allowed within the `RateLimits`.

        `rateLimited(
RateLimitHelpers.makeAssetKey(LIMIT_AAVE_DEPOSIT, aToken),
amount
)`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.4 - Initialize ERC-20 Token Interface [Core]  <!-- UUID: 87922fd8-ff01-40d4-b6cc-c72f4a1b322e -->

The operator must initialize the `underlying` variable as an ERC-20 token interface.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.4.1 - Initialize Interface For Address [Core]  <!-- UUID: 19fbd6f2-f303-4ad2-a56c-b3761bfc3b13 -->

The operator must initialize the interface for the `address of the underlying asset` retrieved from the `aToken` contract (the contract that represents the deposited assets in Aave). The `IERC20` interface allows interaction with ERC-20 tokens, including performing actions like transferring, approving, and checking balances.

` {
IERC20    underlying = IERC20(IATokenWithPool(aToken).UNDERLYING_ASSET_ADDRESS());`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.5 - Initialize Pool Variable [Core]  <!-- UUID: 7ab77ba4-3513-4661-b08c-41b24f73cb59 -->

The operator must initialize the `pool` variable as an interface for the Aave pool.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.5.1 - Retrieve Aave Address [Core]  <!-- UUID: 5b405222-e981-44b7-853b-09d1976fdbbb -->

The operator must retrieve the Aave pool contract address associated with the given `aToken`. This address represents the Aave lending pool where the assets are deposited. `IAavePool` interface allows interaction with the Aave pool's functions (like `supply`).

`    IAavePool pool       = IAavePool(IATokenWithPool(aToken).POOL());`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.6 - Call Approve Function [Core]  <!-- UUID: 989427e7-7ced-49a9-88b1-df3c461b15b6 -->

The operator must call the `approve` function to update the allowance of the `underlying` asset contract.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.6.1 - Encode Function Call [Core]  <!-- UUID: b4c5ecdf-c38f-47fa-93ff-d914ea520c19 -->

The operator must encode the `approve` function call, using `abi.encodeCall` allowing the Aave `pool` address to spend up to `amount` of the `underlying` token from the ALM Proxy’s balance.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.6.2 - Send Encoded Call [Core]  <!-- UUID: 79ba7e11-2adf-45fa-a73f-4c20ba1efc27 -->

The operator must send the encoded call using `proxy.doCall()` specifying the `address` of the `asset` contract they want to deposit into.

       `// Approve underlying to Aave pool from the proxy (assumes the proxy has enough underlying).
proxy.doCall(
address(underlying),
abi.encodeCall(underlying.approve, (address(pool), amount))
);`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.7 - Call Deposit Function [Core]  <!-- UUID: ce52a39f-a0dc-4df4-8a34-1f4be4b3443a -->

The operator must call the `deposit` function to transfer the `underlying` asset to the Aave lending pool and receive the `aTokens`.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.7.1 - Encode Function Call [Core]  <!-- UUID: 7d5b7673-1d17-4d64-9777-9d584d99ada6 -->

The operator must encode the `deposit` function call, using `abi.encodeCall` with the address of the `underlying` token, the `amount` of the underlying asset to `deposit` and the `address(proxy)` that will receive the resulting `aTokens` (i.e. ALM Proxy).

###### A.6.1.1.1.2.6.1.3.1.2.1.3.1.7.2 - Send Encoded Call [Core]  <!-- UUID: 58ca518e-9ff1-4008-9616-18f135a33772 -->

The operator must send the encoded call using `proxy.doCall()` to the `supply` function on Aave (`pool`).

        `// Deposit underlying into Aave pool, proxy receives aTokens
proxy.doCall(
address(pool),
abi.encodeCall(pool.supply, (address(underlying), amount, address(proxy), 0))
);
}`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2 - Process Definition For Withdrawing [Core]  <!-- UUID: 35e32620-a28c-4101-a881-2b7c2b9e42f2 -->

The documents herein define the steps for an operator to withdraw a yield-earning balance from the Aave AToken vaults to the ALM Proxy.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.1 - Relayer Role [Core]  <!-- UUID: 9daa0cad-61ef-43e3-9e78-aaddde2e5c35 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `withdrawAave` tokens. Also, they ensure the contract `isActive` i.e. can process the request.

`function withdrawAave(address aToken, uint256 amount)
external
onlyRole(RELAYER)
isActive`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.2 - Check ALM Proxy [Core]  <!-- UUID: 4a206a15-75a3-44b5-a95d-faad248ded5e -->

The operator must ensure the ALM Proxy holds sufficient `aTokens` to cover the instructed `withdraw` amount.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.3 - Check RateLimits [Core]  <!-- UUID: e5e9c15f-dd74-44c3-b6fc-e9855a66bcba -->

The operator must ensure the `withdraw` amount is allowed within the `RateLimits`.

`// Check withdrawal limits.
rateLimited(
RateLimitHelpers.makeAssetKey(LIMIT_AAVE_WITHDRAW, aToken),
amount
)`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.4 - Initialize Pool Variable [Core]  <!-- UUID: 8c529eb7-aaaa-4c25-9040-6513d5ca02a5 -->

The operator must initialize the `pool` variable as an interface for the Aave pool.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.5 - Retrieve Aave Address [Core]  <!-- UUID: 9349014e-68e7-4832-bbab-d0d9fa34607b -->

The operator must retrieve the Aave pool contract address associated with the given `aToken`. This address represents the Aave lending pool from which the assets are withdrawn.

    `IAavePool pool       = IAavePool(IATokenWithPool(aToken).POOL());`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.6 - Call Withdraw Function [Core]  <!-- UUID: 5fb6e805-a394-4cfd-a788-bdb9bb4ff1c9 -->

The operator must call the `withdraw` function to withdraw a required amount of `underlying` asset from Aave `pool` address and receive the corresponding `aTokens`.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.6.1 - Encode Function Call [Core]  <!-- UUID: d0168bc6-231f-44b8-87f6-b1cad0d742cc -->

The operator must encode the `withdraw` function using `abi.encodeCall` with the `underlying asset address` from the `aToken` contract, specifying which token is being withdrawn, the `amount` of the underlying asset to `withdraw`, and the `address(proxy)` of the recipient of the withdrawn assets (i.e. ALM Proxy).

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.6.2 - Send Encoded Call [Core]  <!-- UUID: 664e5cea-9efb-4db8-96b1-3afee35d4860 -->

The operator must send the encoded call using `proxy.doCall()` to the `withdraw` function of the Aave `pool` contract.

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.6.3 - Decode For Underlying Assets [Core]  <!-- UUID: c4eb149e-8d0b-4e5b-93c6-49c67b2221a3 -->

The operator must decode the raw bytes data returned from the `doCall()` function into `uint256` value, representing the amount of underlying assets that were successfully withdrawn from the Aave pool (`amountWithdrawn`).

       ` // Withdraw underlying from Aave pool, decode resulting amount withdrawn.
// Assumes proxy has adequate aTokens.
amountWithdrawn = abi.decode(
proxy.doCall(
address(pool),
abi.encodeCall(
pool.withdraw,
(IATokenWithPool(aToken).UNDERLYING_ASSET_ADDRESS(), amount, address(proxy))
)
),
(uint256)
);`

###### A.6.1.1.1.2.6.1.3.1.2.1.3.2.7 - Decrease RateLimit [Core]  <!-- UUID: 835ceecc-82b0-4c00-8ba3-86d5a8cd782e -->

The operator must decrease the `RateLimit` based on the assets redeemed.

`rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(LIMIT_AAVE_WITHDRAW, aToken),
            amountWithdrawn
        );
    }`

###### A.6.1.1.1.2.6.1.3.1.2.2 - Ethereum Mainnet - Aave Core USDC Instance Configuration Document [Core]  <!-- UUID: bba861d8-9307-4e7f-ac54-f636232baff1 -->

The documents herein contain the Instance Configuration Document for the Aave Core USDC Instance.

###### A.6.1.1.1.2.6.1.3.1.2.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 8c579e3f-9096-4825-911b-db2864752443 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.2.2.2 - Parameters [Core]  <!-- UUID: e267a558-6217-4016-b86e-0bfe96a4b2f1 -->

The documents herein define the parameters of the Aave Core USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.2.2.2.1 - Instance Identifiers [Core]  <!-- UUID: eb139f3f-92ca-47f1-950c-bd226382a5e5 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.2.2.2.1.1 - Network [Core]  <!-- UUID: 74de563a-acff-48ae-abf5-088d1eb75b1d -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.2.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 74942ea3-011d-47fa-8020-709ec4b008df -->

Aave Core

###### A.6.1.1.1.2.6.1.3.1.2.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: e339e615-59df-4714-9d05-9fa9864abd00 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.2.2.2.1.4 - Token [Core]  <!-- UUID: 25ce1351-b3f8-45d1-9a50-ac199f099c33 -->

aEthUSDC

###### A.6.1.1.1.2.6.1.3.1.2.2.2.2 - Contract Addresses [Core]  <!-- UUID: 4e9d183a-5b07-46a1-8591-f43fd13c32a0 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.2.2.2.2.1 - Token Address [Core]  <!-- UUID: 2f0e8c66-aabb-48c0-a9ed-d9a7d0652737 -->

`0x98C23E9d8f34FEFb1B7BD6a91B7FF122F4e16F5c`

###### A.6.1.1.1.2.6.1.3.1.2.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: a11796f1-e89e-4dfc-b53e-0ab6527cc025 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.2.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: b3b677e8-a154-4c5a-9e88-5222716a806d -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.2.2.2.4 - Rate Limits [Core]  <!-- UUID: 4b08586e-4e28-404d-90c4-29a44fc29cb5 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.2.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 6b65dffb-15a2-4c2c-83a2-ef5325b1f8cc -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 25,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.2.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 89b3f4e4-c845-4a6c-bdce-a383bf11a947 -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.2.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 9ff8418d-457e-4ce3-83c4-18c5ae3b35d7 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.2.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 5b51c049-870b-407e-bce9-2d383c8eb961 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.2.3 - Ethereum Mainnet - Aave Core USDS Instance Configuration Document [Core]  <!-- UUID: 1191f33a-dc78-4c2f-bc5e-e85802471c60 -->

The documents herein contain the Instance Configuration Document for the Aave Core USDS Instance.

###### A.6.1.1.1.2.6.1.3.1.2.3.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 92f8531a-927d-43b4-aaea-7da957606df2 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.2.3.2 - Parameters [Core]  <!-- UUID: c2823616-9db0-47f8-a25e-4bc5fa9bad77 -->

The documents herein define the parameters of the Aave Core USDS Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.2.3.2.1 - Instance Identifiers [Core]  <!-- UUID: f2255528-1c74-49f6-a745-d5e6ab6e1ffd -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.2.3.2.1.1 - Network [Core]  <!-- UUID: 854b6f90-e44a-401c-9786-397f102e9206 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.2.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 247554ce-878e-4e52-9cc4-38dc6d9a280c -->

Aave Core

###### A.6.1.1.1.2.6.1.3.1.2.3.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: c2d4fcec-44fb-45ca-94d0-529b559797c8 -->

USDS

###### A.6.1.1.1.2.6.1.3.1.2.3.2.1.4 - Token [Core]  <!-- UUID: 527bb529-4641-47f9-94de-b9cdf54f8db2 -->

aEthUSDS

###### A.6.1.1.1.2.6.1.3.1.2.3.2.2 - Contract Addresses [Core]  <!-- UUID: 29dbed1a-ba1b-4424-b74e-b3a4842dbfca -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.2.3.2.2.1 - Token Address [Core]  <!-- UUID: b1c3fe3e-922f-4261-ab62-f0103b5a1cdd -->

`0x32a6268f9Ba3642Dda7892aDd74f1D34469A4259`

###### A.6.1.1.1.2.6.1.3.1.2.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: f366a310-9e3a-4b4f-9437-4fa3bbf72d65 -->

`0xdC035D45d973E3EC169d2276DDab16f1e407384F`

###### A.6.1.1.1.2.6.1.3.1.2.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: e444d574-2b11-4187-a45f-9a80d75aae10 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.2.3.2.4 - Rate Limits [Core]  <!-- UUID: 71151ae6-4224-426c-a8fa-5ba03cf64b5a -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.2.3.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 27876101-2e16-4a33-811d-c662df211b2c -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 25,000,000 USDS per day

###### A.6.1.1.1.2.6.1.3.1.2.3.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: c02c329a-9e38-472b-ae0f-b2974694982e -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.2.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 07ce54dc-92dd-4f7e-a9ef-53760b999de7 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.2.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: c0533414-3031-43a7-9e9f-99160976b9b1 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.2.4 - Ethereum Mainnet - Aave Core USDT Instance Configuration Document [Core]  <!-- UUID: c8bcfd26-cab2-43f6-9c35-ad13571fcf1e -->

The documents herein contain the Instance Configuration Document for the Aave Core USDT Instance.

###### A.6.1.1.1.2.6.1.3.1.2.4.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 33dd70f8-51c4-487b-9e08-f2204349aaf3 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.2.4.2 - Parameters [Core]  <!-- UUID: 2eabaaa2-b4a0-4a76-a872-20b1fa49949d -->

The documents herein define the parameters of the Aave Core USDT Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.2.4.2.1 - Instance Identifiers [Core]  <!-- UUID: 25929517-be4b-4a41-bbc8-41f19a24885f -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.2.4.2.1.1 - Network [Core]  <!-- UUID: e041990b-f947-4c53-9bf7-5b12c7c45a37 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.2.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 7e47cc90-7bb8-465f-b528-266b6b967d05 -->

Aave Core

###### A.6.1.1.1.2.6.1.3.1.2.4.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 08e907a6-86fb-4e34-a795-01439955467c -->

USDT

###### A.6.1.1.1.2.6.1.3.1.2.4.2.1.4 - Token [Core]  <!-- UUID: 36025c5c-99be-43f8-8f52-fe90fac62efb -->

aEthUSDT

###### A.6.1.1.1.2.6.1.3.1.2.4.2.2 - Contract Addresses [Core]  <!-- UUID: 3264c038-e7ac-4127-81a7-bb74ffdfc3c9 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.2.4.2.2.1 - Token Address [Core]  <!-- UUID: 6f712e66-f262-4db6-b846-282865e16156 -->

`0x23878914EFE38d27C4D67Ab83ed1b93A74D4086a`

###### A.6.1.1.1.2.6.1.3.1.2.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 1f74c7a5-f038-4bc6-824b-6005ff313297 -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.2.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: b4612996-b947-467b-a982-9791daf37a1f -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.2.4.2.4 - Rate Limits [Core]  <!-- UUID: 2b7b02e3-b63a-445f-86bb-098627ae20ed -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.2.4.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 42c4a115-4fed-4d24-a260-d86dc2a71bea -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 0

###### A.6.1.1.1.2.6.1.3.1.2.4.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: c52a5acc-ef73-4e13-ab15-8c1c1daf12a6 -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: 0

###### A.6.1.1.1.2.6.1.3.1.2.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 8587305b-0af4-49e0-b156-e270d64e69da -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.2.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 70a5413e-80da-43b6-8e40-32865d9a28f9 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.2.5 - Ethereum Mainnet - Aave USDe Instance Configuration Document [Core]  <!-- UUID: 8bd798af-96fc-4fc4-9fb7-5b351740a962 -->

The documents herein contain the Instance Configuration Document for the Aave USDe Instance.

###### A.6.1.1.1.2.6.1.3.1.2.5.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 29315031-1577-49d5-b40f-f818c945a047 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.2.5.2 - Parameters [Core]  <!-- UUID: bbfe8d2f-b82a-471e-a9d5-78892abc3465 -->

The documents herein define the parameters of the Aave Core USDe Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.2.5.2.1 - Instance Identifiers [Core]  <!-- UUID: 670dce17-03d2-4815-94b5-c58406b8b40d -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.2.5.2.1.1 - Network [Core]  <!-- UUID: 12dde8d6-ff41-4c34-bf15-fe5c28e0f3c3 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.2.5.2.1.2 - Target Protocol [Core]  <!-- UUID: b5fc5332-162f-45ca-b7a4-c6669f42134e -->

Aave Core

###### A.6.1.1.1.2.6.1.3.1.2.5.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 4015efa4-bed3-476a-bfc8-dec3d2909604 -->

USDe

###### A.6.1.1.1.2.6.1.3.1.2.5.2.1.4 - Token [Core]  <!-- UUID: a40aaf6a-b29f-413b-987d-bdf3a8bbf9c3 -->

aEthUSDe

###### A.6.1.1.1.2.6.1.3.1.2.5.2.2 - Contract Addresses [Core]  <!-- UUID: 54fac347-de59-4a8f-a9cf-bd7fe0ccdcfb -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.2.5.2.2.1 - Token Address [Core]  <!-- UUID: 6f8813ff-3f2c-4eb1-be25-10b6b428781d -->

`0x4F5923Fc5FD4a93352581b38B7cD26943012DECF`

###### A.6.1.1.1.2.6.1.3.1.2.5.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: a0682e7a-b111-4283-80c9-e806dd1bd225 -->

`0x4c9EDD5852cd905f086C759E8383e09bff1E68B3`

###### A.6.1.1.1.2.6.1.3.1.2.5.2.3 - Rate Limit IDs [Core]  <!-- UUID: 4fbb1a36-0889-4258-a7e9-0f1ab7d2b00e -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.2.5.2.4 - Rate Limits [Core]  <!-- UUID: c8b82f71-acd7-4ccc-8067-ceab3bb46f53 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.2.5.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: ce159b4f-4e1a-48e9-9a73-b16c5fe19288 -->

The inflow rate limits are:

- `maxAmount`: 250,000,000 USDe
- `slope`: 100,000,000 USDe per day

###### A.6.1.1.1.2.6.1.3.1.2.5.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: a773878d-3f7c-492c-9486-139788f5b50f -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.2.5.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 0d912386-ce60-4018-bc95-6403b2316fce -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.2.5.3 - Instance-specific Operational Processes [Core]  <!-- UUID: fdb9edc5-6934-4a5a-8806-d835a6729de0 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.3 - Maple [Core]  <!-- UUID: 0d069124-5ef8-4152-96d8-30980e522df9 -->

The Ethereum Mainnet Instances of the Maple Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.3.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document [Core]  <!-- UUID: 06a83573-f319-4a56-a2bd-4389086dd2bf -->

The documents herein contain the Instance Configuration Document for the Maple USDC Instance.

###### A.6.1.1.1.2.6.1.3.1.3.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 7cc5a238-418d-4301-bf78-de8f5fa5669c -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.3.1.2 - Parameters [Core]  <!-- UUID: 305d6ee1-997d-47bd-94ed-4c28fc8a6e1c -->

The documents herein define the parameters of the Maple USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.3.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 5005b27d-46a7-45a6-a8b7-68496fb343e5 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.3.1.2.1.1 - Network [Core]  <!-- UUID: 0577f89a-0ecf-4f99-a43b-880885b0fb84 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.3.1.2.1.2 - Target Protocol [Core]  <!-- UUID: a2c71d09-8578-4854-98ae-8d122343dbed -->

Maple

###### A.6.1.1.1.2.6.1.3.1.3.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 6431d5f7-1e50-4537-902f-0d772ee3f08e -->

USDC

###### A.6.1.1.1.2.6.1.3.1.3.1.2.1.4 - Token [Core]  <!-- UUID: 5f4e0d3c-f3b4-4e1e-b3ea-59c3883df0c8 -->

syrupUSDC

###### A.6.1.1.1.2.6.1.3.1.3.1.2.2 - Contract Addresses [Core]  <!-- UUID: 0802482b-d11d-43d7-992a-8fde39fdcf2c -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.3.1.2.2.1 - Token Address [Core]  <!-- UUID: 953bd87a-5781-42f1-b989-f9ab267bc707 -->

`0x80ac24aA929eaF5013f6436cdA2a7ba190f5Cc0b`

###### A.6.1.1.1.2.6.1.3.1.3.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: acb94b04-e58a-4948-9a85-aaf6887d8f65 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.3.1.2.2.3 - Pool [Core]  <!-- UUID: 80ab522b-2f60-4d3a-bcd7-63f728f180f9 -->

`0x80ac24aA929eaF5013f6436cdA2a7ba190f5Cc0b`

###### A.6.1.1.1.2.6.1.3.1.3.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 8fd1f7ba-7c0b-4414-be6d-a45a1e263966 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.3.1.2.4 - Rate Limits [Core]  <!-- UUID: d3641a4d-6104-4dc9-90ff-d4c7d1766917 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.3.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: b5d5ba32-342f-4d98-a51e-4d43ff458b48 -->

The inflow rate limits are:

- `maxAmount`: 100,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.3.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: ce4681b7-b94f-4acb-a2de-49b92b70245b -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.3.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: c7791404-4478-4bf8-8292-7bd3ff676e01 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.3.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: a0a08a60-a588-4586-b237-51273e259d8a -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.3.2 - Ethereum Mainnet - Maple USDT Instance Configuration Document [Core]  <!-- UUID: 5302863d-f777-461e-8238-2178fc9899c4 -->

The documents herein contain the Instance Configuration Document for the Maple USDT Instance.

###### A.6.1.1.1.2.6.1.3.1.3.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 1ed4dd56-1e0a-4c73-ba31-3fd6894c91bf -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.3.2.2 - Parameters [Core]  <!-- UUID: 46c4446e-ce4f-4ab8-85fd-c1868636ff2b -->

The documents herein define the parameters of the Maple USDT Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.3.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 33273ac7-e169-48f6-a89b-eb3173050bfe -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.3.2.2.1.1 - Network [Core]  <!-- UUID: e05459c2-ea54-4b1a-a68f-f87c0291d713 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.3.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 0d38db2a-1471-4f69-b0a6-37cabf5e7f4f -->

Maple

###### A.6.1.1.1.2.6.1.3.1.3.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: c2e6edf2-d064-4079-bb51-403d6963db0b -->

USDT

###### A.6.1.1.1.2.6.1.3.1.3.2.2.1.4 - Token [Core]  <!-- UUID: 39086a4b-4656-4884-894f-895c88bef238 -->

syrupUSDT

###### A.6.1.1.1.2.6.1.3.1.3.2.2.2 - Contract Addresses [Core]  <!-- UUID: 3147106a-6918-449e-bb1b-70a52ac1af26 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.3.2.2.2.1 - Token Address [Core]  <!-- UUID: 348f78f4-07a2-4e72-8d2a-4a62a2e44bed -->

`0x356B8d89c1e1239Cbbb9dE4815c39A1474d5BA7D`

###### A.6.1.1.1.2.6.1.3.1.3.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: ffaf2d1b-8942-489f-8408-ab0e5718d3c5 -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.3.2.2.2.3 - Pool [Core]  <!-- UUID: 3b9ecc4e-0cc5-491b-aebc-bf08d2e8c6f9 -->

`0x356B8d89c1e1239Cbbb9dE4815c39A1474d5BA7D`

###### A.6.1.1.1.2.6.1.3.1.3.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: efc9f35a-40e1-4847-8a48-06eda4d17d85 -->

- `deposit`: `0x207bb548ee62bbfd7b6906087f0de38e6c19d5be908e83166c0f089ccc2d97eb`
- `withdraw`: `0xe701ee8a9573df3a49595c8d32a8df7809120a0541dd386e9bf54c148d969707`
- `redeem`: `0x0562da8d8466582e6dc86134ab2ec5656cb4e3d5b57650f6bb1a0f3683bea329`

###### A.6.1.1.1.2.6.1.3.1.3.2.2.4 - Rate Limits [Core]  <!-- UUID: dfab21ad-13a4-48dd-8398-0c3d7dbc8996 -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.3.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 9bf306d1-bc24-4214-9799-53a00ab04ab5 -->

The inflow rate limits are:

- `maxAmount`: 50,000,000 USDT
- `slope`: 100,000,000 USDT per day

###### A.6.1.1.1.2.6.1.3.1.3.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: fc23d5a1-6e97-4e3e-bead-9a41955441c6 -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.3.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: a9ece9ee-2c12-462e-928e-d1a69b5f83a3 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.3.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 3cd39fda-4e26-4f1b-ac32-93d3825a660b -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.3.2.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 717e595c-d7ff-406e-802b-cb4351858f00 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.1.3.2.4.1 - Request Redemption Parameters [Core]  <!-- UUID: 34e632af-1fd9-4dbe-be28-633837cdfe67 -->

- `maxAmount`: Unlimited
- `slope`: 500,000,000 USDT per day

###### A.6.1.1.1.2.6.1.3.1.4 - Ethena [Core]  <!-- UUID: b23e9a6b-e78a-486f-9f6e-07cfdb437bee -->

The Ethereum Mainnet Instances of the Ethena Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.4.1 - Ethereum Mainnet - Ethena USDe Instance Configuration Document [Core]  <!-- UUID: 6be3e516-5374-41a0-8566-1c50656af772 -->

The documents herein contain the Instance Configuration Document for the Ethena USDe Instance.

###### A.6.1.1.1.2.6.1.3.1.4.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: c5c8cd59-5d39-462c-b27d-79a7f65630b7 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.4.1.2 - Parameters [Core]  <!-- UUID: 5218de11-dc55-4933-aea7-46916969a60d -->

The documents herein define the parameters of the Ethena USDe Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.4.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 62efc9a3-79e0-46dc-b67c-83add146ed55 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.4.1.2.1.1 - Network [Core]  <!-- UUID: 67144d2b-382d-4817-b9a8-5b3483da164d -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.4.1.2.1.2 - Target Protocol [Core]  <!-- UUID: acb1b896-a531-498d-9e77-057b0c30d15b -->

Ethena Protocol

###### A.6.1.1.1.2.6.1.3.1.4.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 355a1d6b-6138-4e23-84dc-244b8f1ba26c -->

USDC

###### A.6.1.1.1.2.6.1.3.1.4.1.2.1.4 - Token [Core]  <!-- UUID: aa5fd0d5-4e71-46e1-95ee-609337769f10 -->

USDe

###### A.6.1.1.1.2.6.1.3.1.4.1.2.2 - Contract Addresses [Core]  <!-- UUID: ea69bedc-c388-4925-af83-9fa5496d0d36 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.4.1.2.2.1 - Token Address [Core]  <!-- UUID: deb2d957-2230-48d8-befb-8a9f44454c14 -->

`0x4c9EDD5852cd905f086C759E8383e09bff1E68B3`

###### A.6.1.1.1.2.6.1.3.1.4.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: e72457e9-cfd1-4a67-a694-4b487d38d3c0 -->

This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.4.1.2.2.3 - EthenaMinter [Core]  <!-- UUID: e9625e37-993c-4690-b3e3-cf6a29fb8c96 -->

`0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3`

###### A.6.1.1.1.2.6.1.3.1.4.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: cc7955d0-0214-48cf-bc2b-7fc0692ef755 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.4.1.2.4 - Rate Limits [Core]  <!-- UUID: 54992e68-12d5-4036-9a7c-36403a2e17f8 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.4.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: c45e65d9-9577-4414-b163-5f55c4335d3c -->

The inflow rate limits are:

- `maxAmount`: 250,000,000 USDC
- `slope`: 100,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.4.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: fecaf504-50ea-4f75-bd4d-b5f26c724bc2 -->

The outflow rate limits are:

- `maxAmount`: 500,000,000 USDe
- `slope`: 200,000,000 USDe per day

###### A.6.1.1.1.2.6.1.3.1.4.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: c4f10363-7872-4d71-a8c4-4d5314c78f33 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.4.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 6a009815-fba1-452c-af33-7ac5454211f1 -->

The documents herein defines the operations performed to manage the Ethena Instance, including rate limiting, role-based access control, and cooldown functionality.

###### A.6.1.1.1.2.6.1.3.1.4.1.3.1 - Delegated Signers [Core]  <!-- UUID: e6722e78-c1f5-4704-8bf9-2b3ab7c1b811 -->

The documents herein contain the addresses authorized as `delegatedSigners` in the `ethenaMinter` contract. `delegatedSigners` are set up and removed in the `MainnetController` contract by the `Relayer` role.

###### A.6.1.1.1.2.6.1.3.1.4.1.3.1.1 - Addresses Of Delegated Signers [Core]  <!-- UUID: 7fcbd408-2aef-427f-b88d-d301350bd41b -->

`delegatedSigner` addresses

- These addesses will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.4.1.3.2 - Set A Delegated Signer In The EthenaMinter Contract [Core]  <!-- UUID: 4413579c-6ca5-4ff5-9dd5-ff669606eeb7 -->

The documents herein define the process for an operator to set a delegated signer to the EthenaMinter contract.

###### A.6.1.1.1.2.6.1.3.1.4.1.3.2.1 - Relayer Role [Core]  <!-- UUID: bb5f7a55-8c79-4678-a281-8264eb5de225 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `setDelegatedSigner`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function setDelegatedSigner(address delegatedSigner)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.2.2 - Encode Function [Core]  <!-- UUID: 77e7f0e6-016f-4d66-b7cf-39efa5b4f0b2 -->

The operator must use `proxy.doCall()` to forward the call to the `ethenaMinter` contract and call `setDelegatedSigner` function to set the address that will be authorized as a `delegatedSigner`. To call on `ethenaMinter` contract, the function must be encoded using `abi.encodeCall`.

`{
    proxy.doCall(
        address(ethenaMinter),
        abi.encodeCall(ethenaMinter.setDelegatedSigner, (address(delegatedSigner)))
    );
}`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.3 - Remove A Delegated Signer In The Ethena Minter Contract [Core]  <!-- UUID: 40d3f261-a7f3-4cd9-b92b-3a79872eb339 -->

The documents herein define the process for an operator to remove a delegated signer from the Ethena Minter contract.

###### A.6.1.1.1.2.6.1.3.1.4.1.3.3.1 - Relayer Role [Core]  <!-- UUID: 157361f8-7758-4e6b-a04d-a592d40b3b41 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `removeDelegatedSigner`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function removeDelegatedSigner(address delegatedSigner)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.3.2 - Encode Function [Core]  <!-- UUID: 71d2f286-960f-4264-86db-b48154f38366 -->

The operator must use `proxy.doCall()` to forward the call to the `ethenaMinter` contract and call `removeDelegatedSigner` function to remove the authorization for the `address` to act as a `delegatedSigner`. To call on `ethenaMinter` contract, the function must be encoded using `abi.encodeCall`.

`{
    proxy.doCall(
        address(ethenaMinter),
        abi.encodeCall(ethenaMinter.removeDelegatedSigner, (address(delegatedSigner)))
    );
}`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.4 - Approve Minting of USDe By Ethena Minter Contract [Core]  <!-- UUID: 43775285-0a42-44d8-bc3f-acc80f97a8f3 -->

The documents herein define the process for an operator to approve the minting of USDe by the EthenaMinter contract.

###### A.6.1.1.1.2.6.1.3.1.4.1.3.4.1 - Relayer Role [Core]  <!-- UUID: 41214aef-fb81-42d5-ade2-f7263b8fffb0 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeMint`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function prepareUSDeMint(uint256 usdcAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.4.2 - Enforce Rate Limit [Core]  <!-- UUID: 62adede2-12c9-4388-b078-dbb3ef41e875 -->

The operator must enforce a rate limit on how much USDC can be approved for minting USDe.

`rateLimited(LIMIT_USDE_MINT, usdcAmount)`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.4.3 - Encode Function [Core]  <!-- UUID: 097fc13f-6cdd-4cde-ac00-3db8aa94f3a5 -->

The operator must use `proxy.doCall()` to send an approval call to the `usdc` contract, allowing the `ethenaMinter` contract to spend up to the specified `amount` of USDC. They must encode the function using `abi.encodeCall`.

` {
    proxy.doCall(
        address(usdc),
        abi.encodeCall(usdc.approve, (address(ethenaMinter), usdcAmount))
    );
}`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.5 - Approve Burning of USDe By EthenaMinter Contract [Core]  <!-- UUID: 9df0fbc9-4d5f-4ddb-a184-d5a069cde43c -->

The documents herein define the process for an operator to approve the burning of USDe by the EthenaMinter contract.

###### A.6.1.1.1.2.6.1.3.1.4.1.3.5.1 - Relayer Role [Core]  <!-- UUID: 083618d3-6102-4a1a-bc7a-dfa854d49197 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeBurn`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function prepareUSDeBurn(uint256 usdeAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.5.2 - Enforce Rate Limit [Core]  <!-- UUID: b31a63bd-3163-4d8d-8fe1-c664a989a709 -->

The operator must enforce a rate limit on how much USDe can be approved for burning.

`rateLimited(LIMIT_USDE_BURN, usdeAmount)`

###### A.6.1.1.1.2.6.1.3.1.4.1.3.5.3 - Encode Function [Core]  <!-- UUID: 4f454648-637e-442a-9f0f-314958d15915 -->

The operator must use `proxy.doCall()` to send an approval call to the `usde` contract, allowing the `ethenaMinter` contract to spend up to the specified `amount` of USDe. They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(usde),
        abi.encodeCall(usde.approve, (address(ethenaMinter), usdeAmount))
    );
}`

###### A.6.1.1.1.2.6.1.3.1.4.2 - Ethereum Mainnet - Ethena sUSDe Instance Configuration Document [Core]  <!-- UUID: 1903250a-4499-4ce4-bdcb-5835102a6553 -->

The documents herein contain the Instance Configuration Document for the Ethena sUSDe Instance.

###### A.6.1.1.1.2.6.1.3.1.4.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: df6d3b8e-4ded-4918-b657-3f812783aad5 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.4.2.2 - Parameters [Core]  <!-- UUID: 47518c8c-fe69-45cc-b268-858c39c4462a -->

The documents herein define the parameters of the Ethena sUSDe Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.4.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 3499d700-688c-4586-9ab1-7033b092b150 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.4.2.2.1.1 - Network [Core]  <!-- UUID: 54017580-366b-4358-b9ff-b6a05fe1c51e -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.4.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 1112e047-b8b6-4fe9-bf10-f90a6111b4ea -->

Ethena Protocol

###### A.6.1.1.1.2.6.1.3.1.4.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: a147254d-5aa8-4473-81be-778e3b8eb7c4 -->

USDe

###### A.6.1.1.1.2.6.1.3.1.4.2.2.1.4 - Token [Core]  <!-- UUID: 5642013a-bd4d-49f2-8b25-c70287159da5 -->

sUSDe

###### A.6.1.1.1.2.6.1.3.1.4.2.2.2 - Contract Addresses [Core]  <!-- UUID: 3f06cfb3-327d-4578-8a5c-9f93817441c4 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.4.2.2.2.1 - Token Address [Core]  <!-- UUID: da72f25e-649c-45b6-bac1-54e7c4f714a5 -->

`0x9D39A5DE30e57443BfF2A8307A4256c8797A3497`

###### A.6.1.1.1.2.6.1.3.1.4.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 36beeacb-b9c7-4dac-aa1a-db6a69f3af24 -->

`0x4c9EDD5852cd905f086C759E8383e09bff1E68B3`

###### A.6.1.1.1.2.6.1.3.1.4.2.2.2.3 - EthenaMinter [Core]  <!-- UUID: 534a5d66-47ec-4db3-b6d9-ffc21f22cc53 -->

`0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3`

###### A.6.1.1.1.2.6.1.3.1.4.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 6364f050-3634-4baa-8032-cd5d964f2c80 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.4.2.2.4 - Rate Limits [Core]  <!-- UUID: 3370ffb9-c14a-46ee-9b08-b54ce3296ae8 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.4.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 9acb1a46-3e4a-470f-b8b8-61edc40c3a04 -->

The inflow rate limits are:

- `maxAmount`: 250,000,000 USDe
- `slope`: 100,000,000 USDe per day

###### A.6.1.1.1.2.6.1.3.1.4.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: a58592c6-f4f0-4874-bee1-ef11fb91c544 -->

The outflow rate limits are:

- `maxAmount`: unlimited
- `slope`: unlimited

###### A.6.1.1.1.2.6.1.3.1.4.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 5be31657-391b-4385-9893-125157bd771f -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.4.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 3c72575c-ce4e-4379-ba45-080f335851a1 -->

For operational processes defining the operations performed to manage the Ethena Instance, including rate limiting, role-based access control, and minting of USDe functionality see [A.6.1.1.1.2.6.1.3.1.4.1.3 - Instance-specific Operational Processes](6a009815-fba1-452c-af33-7ac5454211f1). For detailed logic specific for this instance see [A.6.1.1.1.2.6.1.3.1.4.2.3.1 - Initiate A sUSDe Cooldown Period](cf235e02-23fb-48e6-b39e-b4fd09dc7911), [A.6.1.1.1.2.6.1.3.1.4.2.3.2 - Cool Down sUSDe Shares](24171b90-4967-4c15-ac77-789d42b0fc80), [A.6.1.1.1.2.6.1.3.1.4.2.3.3 - Unstake sUSDe And Return It To ALM Proxy](57337963-ea1f-4d12-bea4-127896d35855) and [A.6.1.1.1.2.6.1.3.1.4.2.3.4 - Emergency Procedure To Withdraw Ethena Balances](037dc4f2-0b55-42a9-851c-8769b60b7122).

###### A.6.1.1.1.2.6.1.3.1.4.2.3.1 - Initiate A sUSDe Cooldown Period [Core]  <!-- UUID: cf235e02-23fb-48e6-b39e-b4fd09dc7911 -->

The documents herein define the process for an operator to initiate a sUSDe Cooldown period.

###### A.6.1.1.1.2.6.1.3.1.4.2.3.1.1 - Relayer Role [Core]  <!-- UUID: 463dba18-1e74-49bd-b06f-7df0b0cedae7 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownAssetsSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function cooldownAssetsSUSDe(uint256 usdeAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.4.2.3.1.2 - Enforce Rate Limit [Core]  <!-- UUID: 11d78bab-58b4-4ee0-8d73-124e1f9a8972 -->

The operator must enforce a rate limit on how much sUSDe can be cooled down.

`rateLimited(LIMIT_SUSDE_COOLDOWN, usdeAmount)`

###### A.6.1.1.1.2.6.1.3.1.4.2.3.1.3 - Encode Function [Core]  <!-- UUID: 938f26c5-6028-420d-86bf-f41f5d7aeb7e -->

The operator must use `proxy.doCall()` to make a call to the `susde` contract, invoking the `cooldownAssets` function with the specified amount of sUSDe. They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(susde),
        abi.encodeCall(susde.cooldownAssets, (usdeAmount))
    );
}`

###### A.6.1.1.1.2.6.1.3.1.4.2.3.2 - Cool Down sUSDe Shares [Core]  <!-- UUID: 24171b90-4967-4c15-ac77-789d42b0fc80 -->

The documents herein define the process for an operator to cool down sUSDe shares.

###### A.6.1.1.1.2.6.1.3.1.4.2.3.2.1 - Relayer Role [Core]  <!-- UUID: eacdbe29-1c6b-43b4-93a6-5e4eb9aa0fa7 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownSharesSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function cooldownSharesSUSDe(uint256 susdeAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.4.2.3.2.2 - Encode Function [Core]  <!-- UUID: 8ab94554-c56e-4c2c-aa04-7be2d887beb3 -->

The operator must use `proxy.doCall()` to make a call to the `susde` contract, initiating the `cooldown` on the specified amount of sUSDe shares. They must encode the function using `abi.encodeCall`.

###### A.6.1.1.1.2.6.1.3.1.4.2.3.2.2.1 - Decode For Underlying Shares [Core]  <!-- UUID: e2e16365-4a11-4df4-ab33-332fd9a14fac -->

The operator must decode the result returned by the `cooldownShares` function into a `uint256` value, representing the amount of shares that were actually cooled down (`cooldownAmount`).

`{
    cooldownAmount = abi.decode(
        proxy.doCall(
            address(susde),
            abi.encodeCall(susde.cooldownShares, (susdeAmount))
        ),
        (uint256)
    );`

###### A.6.1.1.1.2.6.1.3.1.4.2.3.2.3 - Decrease RateLimit [Core]  <!-- UUID: 386c0363-ce6c-49bd-a440-fc1ab4fb733d -->

The operator must decrease the `RateLimit`, effectively reducing the available `cooldown` limit, based on the `cooldownAmount`.

`rateLimits.triggerRateLimitDecrease(LIMIT_SUSDE_COOLDOWN, cooldownAmount);
}`

###### A.6.1.1.1.2.6.1.3.1.4.2.3.3 - Unstake sUSDe And Return It To ALM Proxy [Core]  <!-- UUID: 57337963-ea1f-4d12-bea4-127896d35855 -->

The documents herein define the process for an operator to unstake sUSDe and return it to the ALM Proxy.

###### A.6.1.1.1.2.6.1.3.1.4.2.3.3.1 - Relayer Role [Core]  <!-- UUID: 9984b00e-ecc2-4328-9e86-c0c2e913f79a -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `unstakeSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function unstakeSUSDe()
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.4.2.3.3.2 - Encode Function [Core]  <!-- UUID: 24486f09-3df1-4620-bd0f-8368b1e3ed7c -->

The operator must use `proxy.doCall()` to make a call to the `susde` contract to invoke the `unstake` function, which unstakes sUSDe and sends the resulting tokens back to the `proxy` address (i.e. ALM Proxy). They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(susde),
        abi.encodeCall(susde.unstake, (address(proxy)))
    );
}`

###### A.6.1.1.1.2.6.1.3.1.4.2.3.4 - Emergency Procedure To Withdraw Ethena Balances [Core]  <!-- UUID: 037dc4f2-0b55-42a9-851c-8769b60b7122 -->

In order to withdraw all Ethena balances, the operator must execute the following actions:

###### A.6.1.1.1.2.6.1.3.1.4.2.3.4.1 - sUSDe Cooldown Action [Core]  <!-- UUID: 98ced6ee-3fa9-49b5-9212-6826a17adc27 -->

The operator must start the cooldown for sUSDe using the following action:

`mainnetController.cooldownSharesSUSDe(susde.balanceOf(address(proxy))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.3.1.4.2.3.2 - Cool Down sUSDe Shares](24171b90-4967-4c15-ac77-789d42b0fc80).

###### A.6.1.1.1.2.6.1.3.1.4.2.3.4.2 - sUSDe Unstake Action [Core]  <!-- UUID: cef1fead-17d3-40ce-9d2f-ea592e51541d -->

The operator must unstake sUSDe using the following action:

`mainnetController.unstakeSUSDe()
`
For more detailed instructions on the code to execute this, see [A.6.1.1.1.2.6.1.3.1.4.2.3.3 - Unstake sUSDe And Return It To ALM Proxy](57337963-ea1f-4d12-bea4-127896d35855).

###### A.6.1.1.1.2.6.1.3.1.5 - Fluid [Core]  <!-- UUID: be04dae7-88d7-42e0-9162-88428080d43b -->

The Ethereum Mainnet Instances of the Fluid Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.5.1 - Ethereum Mainnet - Fluid sUSDS ERC4626 Vault Instance Configuration Document [Core]  <!-- UUID: 8da18a0c-2d5a-4895-ac53-804578b00a5b -->

The documents herein contain the Instance Configuration Document for the Fluid sUSDS ERC4626 Instance.

###### A.6.1.1.1.2.6.1.3.1.5.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: a6215f0e-e4bd-4dc7-9afa-edbb9c09042c -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.5.1.2 - Parameters [Core]  <!-- UUID: 1c806523-7ef2-4f4c-8b6e-c609478d9112 -->

The documents herein define the parameters of the Fluid sUSDS ERC4626 Vault Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.5.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 24967b50-8941-452a-b3f7-47034da4aa00 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.5.1.2.1.1 - Network [Core]  <!-- UUID: 5c50d8a2-bd79-47a8-b4bb-9f8b482c45d7 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.5.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 20caee73-7720-4acf-852f-c656922583cf -->

Fluid Finance (ERC4626 Vault)

###### A.6.1.1.1.2.6.1.3.1.5.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: bf5832db-c854-4439-9207-b9d4cdddd8c8 -->

sUSDS

###### A.6.1.1.1.2.6.1.3.1.5.1.2.1.4 - Token [Core]  <!-- UUID: 02c8c973-3f1e-45bc-bbf0-a099e1db33ce -->

fsUSDS

###### A.6.1.1.1.2.6.1.3.1.5.1.2.2 - Contract Addresses [Core]  <!-- UUID: 0b34a94d-22f6-4aa0-b62b-5c0415cb6460 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.5.1.2.2.1 - Token Address [Core]  <!-- UUID: 1f34b538-6081-4be9-9d69-3ae4bc75200f -->

`0x2BBE31d63E6813E3AC858C04dae43FB2a72B0D11`

###### A.6.1.1.1.2.6.1.3.1.5.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: dbe01ca1-3431-402b-a742-48ceb6d710d8 -->

`0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD`

###### A.6.1.1.1.2.6.1.3.1.5.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: d3fe0ad8-786f-47dc-8193-f34d99a01d9f -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.5.1.2.4 - Rate Limits [Core]  <!-- UUID: 426f42fa-c85c-48de-8859-205d2fa98c3e -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.5.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: f9c88aaf-90d0-404e-b870-182846f58bf6 -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 5,000,000 sUSDS per day

###### A.6.1.1.1.2.6.1.3.1.5.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 67155bd0-093a-49ff-9b96-eb6a8aa22c68 -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: 5,000,000 fsUSDS per day

###### A.6.1.1.1.2.6.1.3.1.5.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 1591a545-a8c6-4a41-aeea-f92d4fa30510 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.5.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 3bc424bf-079e-4b6b-8749-58c942c7d57b -->

The Instance follows the general ERC4626 procedures see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2 - ERC-4626 Functions](e386a0df-9e0b-4ffd-9879-49131f795b0b) and for emergency procedures see [A.6.1.1.1.2.6.1.2.2.3.4.1 - ERC-4626 Withdrawal Action](f92ddc3f-672a-4f52-931f-5263a9f709b9). For detailed example of the Spark Liquidity Layer interaction logic for depositing to, withdrawing from, and redeeming from this ERC4626 vault instance see [A.6.1.1.1.2.6.1.3.1.5.1.3.1 - Deposit ERC-4626 Tokens](e2ad525b-3f3f-4402-9e4d-3ae125b35b76) and [A.6.1.1.1.2.6.1.3.1.5.1.3.2 - Withdraw ERC-4626 Tokens](caa295f4-92f4-4ca9-9083-2a1b94c70d5f).

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1 - Deposit ERC-4626 Tokens [Core]  <!-- UUID: e2ad525b-3f3f-4402-9e4d-3ae125b35b76 -->

The documents herein define the steps for an operator to deposit assets from the ALM Proxy to the ERC-4626 vault (e.g., `[Instance_Fluid_USDS_Vault_Address_Placeholder]`) to receive yield-bearing shares.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.1 - Relayer Role [Core]  <!-- UUID: 9ba1c843-7332-4602-a675-172d5312054d -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `depositERC4626` tokens. Also, they must ensure the contract `isActive` i.e. can process the request.

`function depositERC4626(address token, uint256 amount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.2 - Check ALM Proxy [Core]  <!-- UUID: 089a461f-0ee1-4234-a3ae-f2496c79148c -->

The operator must ensure the ALM Proxy holds enough of the underlying asset (e.g., `[Instance_USDS_Address_Placeholder]`) to cover the instructed `deposit` amount.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.3 - Check RateLimits [Core]  <!-- UUID: eea8794f-8067-4f97-b03a-ae654d0793a8 -->

The operator must ensure the `deposit` amount is allowed within the `RateLimits` for this instance (e.g., using `[Instance_RateLimitID_Deposit_Placeholder]` for `token [Instance_Fluid_USDS_Vault_Address_Placeholder]`).

`        rateLimited(
            RateLimitHelpers.makeAssetKey([Instance_RateLimitID_Deposit_Placeholder], [Instance_Fluid_USDS_Vault_Address_Placeholder]),,
            amount
        )
        returns (uint256 shares)
    {
        // Note that whitelist is done by rate limits
        IERC20 asset = IERC20(IERC4626([Instance_Fluid_USDS_Vault_Address_Placeholder]).asset());`

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.4 - Update Allowance of Asset Contract [Core]  <!-- UUID: 1e7bad6c-fce7-4832-8281-63a89de7fe47 -->

The operator must call the `approve` ERC-4626 function to update the allowance of the `asset` contract.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.4.1 - Encode Function Call [Core]  <!-- UUID: a2430308-7a82-457e-b505-ea9889bf90d5 -->

The operator must encode the function call to the ERC-4626 `approve` method, using `abi.encodeCall` to allow the `token` address (`[Instance_Fluid_USDS_Vault_Address_Placeholder`]) spend up to `amount` of a token from ALM Proxy’s balance.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.4.2 - Send Encoded Call [Core]  <!-- UUID: 07418471-50d1-4c6b-92a1-c883121f2622 -->

The operator must send the encoded call using `proxy.doCall()` specifying the `address` of the `asset` contract (`[Instance_USDS_Address_Placeholder]`) they want to deposit into.

`        // Approve asset to token from the proxy (assumes the proxy has enough of the asset).
        proxy.doCall(
            address(asset),
            abi.encodeCall(asset.approve, ([Instance_Fluid_USDS_Vault_Address_Placeholder], amount))
        );`

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.5 - Deposit Assets [Core]  <!-- UUID: 78ff9c9a-a75e-4b94-a376-c8bc43e1d360 -->

The operator must call the `deposit` ERC-4626 function to transfer the underlying `asset` to ERC-4626 token and receive vault `shares`.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.5.1 - Encode Function Call [Core]  <!-- UUID: 6eb71a3a-09b6-430d-9677-af0c3f9667f1 -->

The operator must encode the function call to ERC-4626 `deposit` method, using `abi.encodeCall` with the address of the ERC-4626 `token` vault (`[Instance_Fluid_USDS_Vault_Address_Placeholder]`), the `amount` of the underlying asset to `deposit` and the `address(proxy)` that will receive the resulting shares (i.e. ALM Proxy).

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.5.2 - Send Encoded Call [Core]  <!-- UUID: 6fd50750-0bee-4895-8ef4-ced22d81ce66 -->

The operator must send the encoded call using `proxy.doCall()` to the `deposit` function on the ERC-4626 vault contract (`token`).

###### A.6.1.1.1.2.6.1.3.1.5.1.3.1.5.3 - Decode Vault Shares [Core]  <!-- UUID: 1c4f95da-5479-4c47-bc8b-4e7875cf8139 -->

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

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2 - Withdraw ERC-4626 Tokens [Core]  <!-- UUID: caa295f4-92f4-4ca9-9083-2a1b94c70d5f -->

The documents herein define the steps for an operator to withdraw a yield-earning balance from the ERC-4626 vault (e.g., `[Instance_Fluid_USDS_Vault_Address_Placeholder]`) to the ALM Proxy.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.1 - Relayer Role [Core]  <!-- UUID: 3ad29e6a-90fb-4739-aacf-434e467c070e -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `withdrawERC4626` tokens. Also, they must ensure the contract `isActive` i.e. can process the request.

`function withdrawERC4626(address token, uint256 amount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.2 - Check ALM Proxy [Core]  <!-- UUID: 61a5f740-e2a6-432d-a3fc-728bff5312e5 -->

The operator must ensure that the ALM Proxy holds sufficient shares of the ERC-4626 vault token (`[Instance_Fluid_USDS_Vault_Address_Placeholder]`) to cover the instructed `withdraw` amount.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.3 - Check RateLimits [Core]  <!-- UUID: 5b77e7bb-5f31-48eb-9cdd-8fb799986788 -->

The operator must ensure the `withdraw` amount is allowed within the `RateLimits `for this instance (e.g. using `[Instance_RateLimitID_Withdraw_Placeholder]` for `token` `[Instance_Fluid_USDS_Vault_Address_Placeholder]`).

`// Check withdrawal limits.
        rateLimited(
            RateLimitHelpers.makeAssetKey([Instance_RateLimitID_Withdraw_Placeholder], [Instance_Fluid_USDS_Vault_Address_Placeholder]),
            amount
        )
        returns (uint256 shares)`

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.4 - Receive Vault Shares [Core]  <!-- UUID: 91ec656f-417c-4357-b8ab-9c7a2404bc13 -->

The operator must call the `withdraw` ERC-4626 function to withdraw a required amount of underlying assets from an ERC-4626 vault and receive the corresponding vault shares.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.4.1 - Encode Function Call [Core]  <!-- UUID: e8053d8a-c24c-4acc-a928-c57fdbe11810 -->

The operator must encode the function call to the ERC-4626 `withdraw` method, using `abi.encodeCall` with the address of the ERC-4626 `token` vault (`[Instance_Fluid_USDS_Vault_Address_Placeholder]`), the `amount` of the underlying asset to `withdraw` and the `address(proxy)` of the recipient of the withdrawn assets and the sender of the shares (i.e. ALM Proxy).

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.4.2 - Send Encoded Call [Core]  <!-- UUID: d1889137-80a3-4e21-a5ea-522d23830574 -->

The operator must send the encoded call using `proxy.doCall()` to the `withdraw` function on the ERC-4626 vault contract (`token`).

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.4.3 - Decode Token Shares [Core]  <!-- UUID: ca253911-1755-481f-ae63-1d4027d1a690 -->

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

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.5 - Redeem Vault Shares For Assets [Core]  <!-- UUID: d0acf55e-d5da-499a-b815-65a1bba8ed57 -->

The operator must call the `redeem` ERC-4626 function to redeem a specific number of vault shares for the underlying asset.

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.5.1 - Encode Function Call [Core]  <!-- UUID: 13e8ea29-273a-45ce-9a61-10256fb7caf0 -->

The operator must encode the function call to the ERC-4626 `redeem` method, using `abi.encodeCall` with the address of the ERC-4626 `token` vault(`[Instance_Morpho_USDS_Vault_Address_Placeholder]`), the `shares` to `redeem` and the `address(proxy)` of the receiver of redeemed assets and the owner of shares being received (i.e. ALM Proxy).

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.5.2 - Send Encoded Call [Core]  <!-- UUID: 4992974d-f666-4b23-8623-4eedc3a96e91 -->

The operator must send the encoded call using `proxy.doCall()` to the `redeem` function on the ERC-4626 vault contract (`token`).

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.5.3 - Decode For Underlying Assets [Core]  <!-- UUID: 83c04cbf-fbd9-4bd0-9791-4fb7b02b091d -->

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

###### A.6.1.1.1.2.6.1.3.1.5.1.3.2.6 - Decrease RateLimit [Core]  <!-- UUID: 50c85778-c824-496b-ae01-7f8868ad341f -->

The operator must decrease the `RateLimit` based on the assets redeemed.

`rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey([Instance_RateLimitID_Withdraw_Placeholder], [Instance_Fluid_USDS_Vault_Address_Placeholder]),
            assets
        );
    }`

###### A.6.1.1.1.2.6.1.3.1.6 - Superstate [Core]  <!-- UUID: 79d6bfdf-c542-4a60-a5f0-a17042d98d35 -->

The Ethereum Mainnet Instances of the Superstate Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.6.1 - Ethereum Mainnet - Superstate USTB Instance Configuration Document [Core]  <!-- UUID: 4ad2419c-7966-42de-bc2a-d8ca8ce61b90 -->

The documents herein contain the Instance Configuration Document for the Superstate USTB Instance.

###### A.6.1.1.1.2.6.1.3.1.6.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 0ecae4db-37e8-4505-b8e1-4211816bf9ed -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.6.1.2 - Parameters [Core]  <!-- UUID: a5f05d4d-431b-45cc-a474-6070dc65ca83 -->

The documents herein define the parameters of the Superstate USTB Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.6.1.2.1 - Instance Identifiers [Core]  <!-- UUID: cc925cb9-823f-426b-aaa2-0a82f646b03e -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.6.1.2.1.1 - Network [Core]  <!-- UUID: 83773f20-1656-4a6c-ab60-a773e9f9e4c7 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.6.1.2.1.2 - Target Protocol [Core]  <!-- UUID: a46217e1-c887-444c-b04d-fa9b412476b9 -->

Superstate

###### A.6.1.1.1.2.6.1.3.1.6.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 965e886d-7b27-41f3-ba61-d5e3f7f1b556 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.6.1.2.1.4 - Token [Core]  <!-- UUID: e4b489eb-3c85-4585-8cd2-e6a7e9143a16 -->

USTB

###### A.6.1.1.1.2.6.1.3.1.6.1.2.2 - Contract Addresses [Core]  <!-- UUID: 20f898ec-d6f0-4608-9590-754161548dcf -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.6.1.2.2.1 - Token Address [Core]  <!-- UUID: 818944d2-c16f-4bd8-af85-09c3a31eccd3 -->

`0x43415eB6ff9DB7E26A15b704e7A3eDCe97d31C4e`

###### A.6.1.1.1.2.6.1.3.1.6.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: b4e63a9d-65e7-4c61-826e-fe9733b3f00f -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.6.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 8e52e9d6-6cb0-44e9-9068-21257c1cde34 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow is:

- `USTB_DEPOSIT`: `0x43415eB6ff9DB7E26A15b704e7A3eDCe97d31C4e`
- `USTB_REDEEM`: `0x43415eB6ff9DB7E26A15b704e7A3eDCe97d31C4e`
- `USTB_REDEEM` (instant liquidity): `0x4c21B7577C8FE8b0B0669165ee7C8f67fa1454Cf`

###### A.6.1.1.1.2.6.1.3.1.6.1.2.4 - Rate Limits [Core]  <!-- UUID: 69e164bc-ef0c-4d74-a17d-e56bf498b7e0 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.6.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 04975455-99e4-447b-8629-0a6088174e69 -->

The inflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.6.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 8639aa8f-3902-4f81-9c1e-a56b4c57f03d -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.6.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: b2e85192-58da-4702-8a5f-f5d2011b008b -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.6.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 5cb29bf7-30f4-43ef-aca8-020d26f66fcb -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.7 - Curve [Core]  <!-- UUID: 614f24ff-943e-40b2-853b-6c8a0a97ca3d -->

The Ethereum Mainnet Instances of the Curve Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.7.1 - Ethereum Mainnet - Curve sUSDS/USDT Pool Instance Configuration Document [Core]  <!-- UUID: 4e840dad-944c-4c45-9c5e-277dcb1830a8 -->

The documents herein contain the Instance Configuration Document for the Curve sUSDS/USDT Pool Instance.

###### A.6.1.1.1.2.6.1.3.1.7.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: bcaaaa86-4799-44cc-ab84-0faf3610ae66 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.7.1.2 - Parameters [Core]  <!-- UUID: b26af91d-675e-4b3f-8f70-e8db5b93c5c0 -->

The documents herein define the parameters of the Curve sUSDS/USDT Pool Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.7.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 1e14eb69-7e41-4113-9ff6-41863539e16b -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.7.1.2.1.1 - Network [Core]  <!-- UUID: 2e3df36f-4370-4613-8ba5-4c25ad502553 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.7.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 470b6ae4-1392-4fff-8f31-2b9c306870d8 -->

Curve

###### A.6.1.1.1.2.6.1.3.1.7.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 72b80d4d-ae2c-4980-87f4-79f734e0544f -->

USDT

###### A.6.1.1.1.2.6.1.3.1.7.1.2.1.4 - Token [Core]  <!-- UUID: 29723ddf-4114-493d-ad46-901725a1bc14 -->

sUSDSUSDT

###### A.6.1.1.1.2.6.1.3.1.7.1.2.2 - Contract Addresses [Core]  <!-- UUID: 7acb9f43-9b9f-4cbd-909c-7e58f6357e5b -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.7.1.2.2.1 - Token Address [Core]  <!-- UUID: 8ce212dc-4f34-41a5-8621-01edd0ab2ea4 -->

`0x00836Fe54625BE242BcFA286207795405ca4fD10`

###### A.6.1.1.1.2.6.1.3.1.7.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 6a780894-8075-4bed-88a9-42b0c3086a37 -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.7.1.2.2.3 - Underlying Asset Address [Core]  <!-- UUID: 2957563b-3948-40b3-a247-15c6ddd41b03 -->

`0xa3931d71877C0E7a3148CB7Eb4463524FEc27fbD`

###### A.6.1.1.1.2.6.1.3.1.7.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: e8833ae1-fdee-4e35-9e83-586c0289c6fd -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.7.1.2.4 - Rate Limits [Core]  <!-- UUID: 408f0d03-44cb-4e6f-b330-5782be816567 -->

The current `maxAmount,` `slope` and slippage for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.7.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 186761a1-5152-40f5-85f3-1e8868d8c6df -->

The inflow rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 20,000,000 per day
- Max slippage: 0.15%

###### A.6.1.1.1.2.6.1.3.1.7.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: f3f5e19c-f85b-484f-b0fb-4ee96e54a616 -->

The outflow rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 20,000,000 per day
- Max slippage: 0.15%

###### A.6.1.1.1.2.6.1.3.1.7.1.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 6f9628a6-7574-4f63-a28f-797bd581e907 -->

The swap rate limits are:

- `maxAmount`: 10,000,000
- `slope`: 200,000,000 per day
- Max slippage: 0.25%

###### A.6.1.1.1.2.6.1.3.1.7.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 8d74f809-b54e-490f-aa7b-c1cb0aea5b7f -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.7.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 60c4efad-67aa-411e-90d1-d5d0a427814a -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.7.2 - Ethereum Mainnet - Curve USDC/USDT Pool Instance Configuration Document [Core]  <!-- UUID: 30d359a0-287b-4b3b-93fd-4e70bf0b19a7 -->

The documents herein contain the Instance Configuration Document for the Curve USDC/USDT Pool Instance.

###### A.6.1.1.1.2.6.1.3.1.7.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: db6624bf-b38d-4516-96d3-04302bdc1dd3 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.7.2.2 - Parameters [Core]  <!-- UUID: e011af54-a277-4ecd-bd73-680ae96a7a51 -->

The documents herein define the parameters of the Curve USDC/USDT Pool Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.7.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 83513371-150d-46c3-82ae-671cc965d39e -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.7.2.2.1.1 - Network [Core]  <!-- UUID: 54e1de2e-1301-4763-98d0-ef2aee8d3221 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.7.2.2.1.2 - Target Protocol [Core]  <!-- UUID: cc6acf48-9b55-4edf-a115-c463c0a78a9d -->

Curve

###### A.6.1.1.1.2.6.1.3.1.7.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: b2bf10d6-adcc-4df4-99cc-9e3abeaeca1c -->

N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.2.2.1.4 - Token [Core]  <!-- UUID: 0dc97998-edff-4d53-8251-18301991dd56 -->

crv2pool

###### A.6.1.1.1.2.6.1.3.1.7.2.2.2 - Contract Addresses [Core]  <!-- UUID: 5b8c7810-5e84-44ba-b245-f3fa8f683b84 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.7.2.2.2.1 - Token Address [Core]  <!-- UUID: a6a50db9-901d-44c4-84d9-cbd581637394 -->

`0x4f493B7dE8aAC7d55F71853688b1F7C8F0243C85`

###### A.6.1.1.1.2.6.1.3.1.7.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 43f3e5cd-12de-4bae-bcf0-ec4348a7e7e5 -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.7.2.2.2.3 - Underlying Asset Address [Core]  <!-- UUID: 5e58a4bf-c0a0-4351-a069-b39b420edb5f -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.7.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 25c72eb6-9a21-4592-b6f1-cede0644b607 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.7.2.2.4 - Rate Limits [Core]  <!-- UUID: f2389063-4d57-4f28-844c-d63c991c5568 -->

The current `maxAmount,` `slope` and slippage for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.7.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 10ce5b4c-068d-44a8-bd34-a4afdb52ac9e -->

The inflow rate limits are:

- `maxAmount`: N/A - swap only
- `slope`: N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 997cbc11-99ee-4d26-87a8-a8a01e0a0537 -->

The outflow rate limits are:

- `maxAmount`: N/A - swap only
- `slope`: N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.2.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 8b143018-298a-4878-9516-9b71049f1d0b -->

The swap rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 20,000,000 per day
- Max slippage: 0.05%

###### A.6.1.1.1.2.6.1.3.1.7.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 6a51a0d9-5b6d-4f68-8740-57033b74d1bc -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.7.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: d6bc0a40-0ed7-4366-902d-22eea7538c02 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.7.3 - Ethereum Mainnet - Curve pyUSD/USDC Pool Instance Configuration Document [Core]  <!-- UUID: e1fdaf49-0b32-4644-b021-9cae6e270c7a -->

The documents herein contain the Instance Configuration Document for the Curve pyUSD/USDC Pool Instance.

###### A.6.1.1.1.2.6.1.3.1.7.3.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 8f864934-c750-443f-b7f5-780d1e5cb47f -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.7.3.2 - Parameters [Core]  <!-- UUID: 2d44ce84-fb22-4435-93f2-ea5a62ccc130 -->

The documents herein define the parameters of the Curve pyUSD/USDC Pool Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.7.3.2.1 - Instance Identifiers [Core]  <!-- UUID: b7328b28-d8cb-4a5d-9ef9-e9fe0d633d9d -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.7.3.2.1.1 - Network [Core]  <!-- UUID: aba55fe1-bd3e-499c-a480-3ea7b860f4d5 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.7.3.2.1.2 - Target Protocol [Core]  <!-- UUID: a0794c17-0668-4bae-a5b1-141c61db12ef -->

Curve

###### A.6.1.1.1.2.6.1.3.1.7.3.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: af3418ca-ed5f-4bee-b4ef-9cdd187cc4a1 -->

N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.3.2.1.4 - Token [Core]  <!-- UUID: dd247f16-4d46-4780-9c19-2b1dec0e547b -->

PYUSDUSDC

###### A.6.1.1.1.2.6.1.3.1.7.3.2.2 - Contract Addresses [Core]  <!-- UUID: 2b15153d-8cd1-4096-b764-e56a1f38d9b7 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.7.3.2.2.1 - Token Address [Core]  <!-- UUID: 51de16a9-1184-45e9-a21f-1329d57ef3d7 -->

`0x383E6b4437b59fff47B619CBA855CA29342A8559`

###### A.6.1.1.1.2.6.1.3.1.7.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: c3d92c36-70ae-46f3-b887-64bb8419072c -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.7.3.2.4 - Rate Limits [Core]  <!-- UUID: 18e7ddf1-71e2-40fd-b74d-8ad6312b9a38 -->

The current `maxAmount`, `slope` and slippage for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.7.3.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 893256f7-00f6-42e7-92cd-218af9beac76 -->

The inflow rate limits are:

- `maxAmount`: 0

###### A.6.1.1.1.2.6.1.3.1.7.3.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: dfcceae6-65f0-44e2-9d47-9ad2324d983d -->

The outflow rate limits are:

- `maxAmount`: 0

###### A.6.1.1.1.2.6.1.3.1.7.3.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 2b4a19db-137d-404d-b475-3008eda3c82d -->

The swap rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 100,000,000 per day
- Max slippage: 0.1%

###### A.6.1.1.1.2.6.1.3.1.7.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 215cc709-a3e0-4cd5-98e1-ccb4430fc85d -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.7.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: cd57ed73-dc55-4543-a910-81a9ee4bc1e3 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.7.4 - Ethereum Mainnet - Curve pyUSD/USDS Pool Instance Configuration Document [Core]  <!-- UUID: 7635eff1-1fa0-4356-8953-2564a7f0693c -->

The documents herein contain the Instance Configuration Document for the Curve pyUSD/USDS Pool Instance.

###### A.6.1.1.1.2.6.1.3.1.7.4.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 464835ae-a3ce-44a7-84c8-11ab2d5138d8 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.7.4.2 - Parameters [Core]  <!-- UUID: fdb613e0-4d7f-46a7-95c3-b84ea9dafa6a -->

The documents herein define the parameters of the Curve pyUSD/USDS Pool Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.7.4.2.1 - Instance Identifiers [Core]  <!-- UUID: d3aa95cf-88e9-432b-90cf-0b4d1da094b5 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.7.4.2.1.1 - Network [Core]  <!-- UUID: 4f3d5b84-1235-4932-8295-8df0e122e4c0 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.7.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 953adabd-347a-4d0c-aaa2-da618ee04151 -->

Curve

###### A.6.1.1.1.2.6.1.3.1.7.4.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: c76d3c17-0be6-4d59-a73f-2952385164f1 -->

USDS and PYUSD

###### A.6.1.1.1.2.6.1.3.1.7.4.2.1.4 - Token [Core]  <!-- UUID: 2b34a305-2239-4b83-b829-dd1e7e8554ad -->

PYUSDUSDS

###### A.6.1.1.1.2.6.1.3.1.7.4.2.2 - Contract Addresses [Core]  <!-- UUID: d386076c-607f-49fd-bd9c-07f4583cc1c9 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.7.4.2.2.1 - Token Address [Core]  <!-- UUID: aee3fc62-2c9a-4283-b447-149dc5f4a741 -->

`0xA632D59b9B804a956BfaA9b48Af3A1b74808FC1f`

###### A.6.1.1.1.2.6.1.3.1.7.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: b86c4730-0a55-4a86-8c08-b01619e55e28 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.7.4.2.4 - Rate Limits [Core]  <!-- UUID: 82a8a51a-1650-438b-bdf4-3dc1b41132f3 -->

The current `maxAmount`, `slope` and slippage for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.7.4.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 00d72073-ebb7-49d6-8ece-e5c506c7cf0c -->

The inflow rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 50,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.7.4.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 5547c29e-0dcd-40c0-9811-f88f4a906825 -->

The outflow rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 100,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.7.4.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 664c8068-a848-42aa-b50a-3000f3081507 -->

The swap rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 50,000,000 per day
- Max slippage: 0.2%

###### A.6.1.1.1.2.6.1.3.1.7.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 4999136f-41f3-49a1-93db-2d72b14c2f17 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.7.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 99474f36-6c37-4627-acdb-0372fdf216ef -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.7.5 - Ethereum Mainnet - Curve weETH/WETH-ng for Swaps Instance Configuration Document [Core]  <!-- UUID: cfc335a4-efcf-4f53-9609-1c9784cbb784 -->

The documents herein contain the Instance Configuration Document for the Curve weETH/WETH-ng for Swaps Instance.

###### A.6.1.1.1.2.6.1.3.1.7.5.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 1020417c-dc56-4808-b867-178ca4ca8681 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.7.5.2 - Parameters [Core]  <!-- UUID: a1dc6fa3-bec8-41ca-bb5a-e60275c03dcf -->

The documents herein define the parameters of the Curve weETH/WETH-ng for Swaps Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.7.5.2.1 - Instance Identifiers [Core]  <!-- UUID: b7f9fa20-dddb-4733-b0e1-9029e79a8aba -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.7.5.2.1.1 - Network [Core]  <!-- UUID: 853b65c3-4b43-436d-9350-cf7ffbed559e -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.7.5.2.1.2 - Target Protocol [Core]  <!-- UUID: 2b599f55-2177-4aad-b9be-a2cda8608900 -->

Curve

###### A.6.1.1.1.2.6.1.3.1.7.5.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: c7a2911c-faf7-40f4-9a90-c43e75bc2396 -->

N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.5.2.1.4 - Token [Core]  <!-- UUID: 25de66b2-d391-44ab-b88c-9e558679640c -->

crv2pool

###### A.6.1.1.1.2.6.1.3.1.7.5.2.2 - Contract Addresses [Core]  <!-- UUID: dfbfa2ba-6fd5-4e56-9366-992e64d86ac1 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.7.5.2.2.1 - Token Address [Core]  <!-- UUID: 92a9fec3-7b4d-4388-bd05-7d18790bc584 -->

`0xDB74dfDD3BB46bE8Ce6C33dC9D82777BCFc3dEd5`

###### A.6.1.1.1.2.6.1.3.1.7.5.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: c740d6f1-cda5-46d5-b7a7-6d2358c3770f -->

`0xCd5fE23C85820F7B72D0926FC9b05b43E359b7ee`

###### A.6.1.1.1.2.6.1.3.1.7.5.2.2.3 - Underlying Asset Address [Core]  <!-- UUID: ad094f82-5619-4558-abd1-e793131e9ec0 -->

`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`

###### A.6.1.1.1.2.6.1.3.1.7.5.2.2.4 - Pool Address [Core]  <!-- UUID: 96a50ef4-938b-475e-8244-40d376e95e6e -->

`0xDB74dfDD3BB46bE8Ce6C33dC9D82777BCFc3dEd5`

###### A.6.1.1.1.2.6.1.3.1.7.5.2.3 - Rate Limit IDs [Core]  <!-- UUID: 7fabde01-b8a5-4226-85d4-b25f55d93b12 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.7.5.2.4 - Rate Limits [Core]  <!-- UUID: dac0cadf-a966-40d3-b739-09a0baceea30 -->

The current `maxAmount`, `slope` and slippage for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.7.5.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 8734b53f-0220-43df-acdc-3c8cb25f323a -->

The inflow rate limits are:

- maxAmount: N/A - swap only
- slope: N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.5.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 8280f97f-d69c-4fc3-a9d4-42407159a5ea -->

The outflow rate limits are:

- maxAmount: N/A - swap only
- slope: N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.5.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: b24f80d1-80cc-46c0-895c-d9bdc49e2e8b -->

The swap rate limits are:

- `maxAmount`: 1,000
- `slope`: 50,000 per day
- `Max slippage`: 0.25%

###### A.6.1.1.1.2.6.1.3.1.7.5.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: a8106b30-ef8c-4ce5-a25a-80755ab624d0 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.7.5.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 28a4bce9-e6d9-4840-8b0b-ed7d9f454dd1 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.7.6 - Ethereum Mainnet - Curve rlUSD/USDC for Swaps Instance Configuration Document [Core]  <!-- UUID: 3833eb97-f358-4019-9265-e4a45455ee0e -->

The documents herein contain the Instance Configuration Document for the Curve rlUSD/USDC for Swaps Instance.

###### A.6.1.1.1.2.6.1.3.1.7.6.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 104bab54-9b08-4232-a748-a5dac8330d6b -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.7.6.2 - Parameters [Core]  <!-- UUID: 57e0e7b0-dd77-4634-810c-53d4e371a3dc -->

The documents herein define the parameters of the Curve rlUSD/USDC for Swaps Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.7.6.2.1 - Instance Identifiers [Core]  <!-- UUID: a844fb4a-0f83-4e7d-8e62-3d33ca1873c2 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.7.6.2.1.1 - Network [Core]  <!-- UUID: d9ea8446-5c91-4888-80d6-a1ecb003d37e -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.7.6.2.1.2 - Target Protocol [Core]  <!-- UUID: 1a09a104-d2fc-415d-82f9-27c31c69cb94 -->

Curve

###### A.6.1.1.1.2.6.1.3.1.7.6.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: d1ae143b-f524-4222-9e03-033716426bff -->

N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.6.2.1.4 - Token [Core]  <!-- UUID: 3a7994c0-8eb9-4c82-a545-226472d39b18 -->

crv2pool

###### A.6.1.1.1.2.6.1.3.1.7.6.2.2 - Contract Addresses [Core]  <!-- UUID: 71b6a35e-0211-435e-9e3e-1f81240171af -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.7.6.2.2.1 - Token Address [Core]  <!-- UUID: 2b44c968-2850-4be0-9bd3-23f24e8ee36b -->

`0xD001aE433f254283FeCE51d4ACcE8c53263aa186`

###### A.6.1.1.1.2.6.1.3.1.7.6.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 0d43a4c4-daf7-44a9-97a4-c90b512fa1ba -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.1.2.6.1.3.1.7.6.2.2.3 - Underlying Asset Address [Core]  <!-- UUID: cb6dbf5b-3a78-41d7-88f6-9ff598b94cb9 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.7.6.2.2.4 - Pool Address [Core]  <!-- UUID: e23f1842-85c4-4931-ad85-b1d653b79308 -->

`0xD001aE433f254283FeCE51d4ACcE8c53263aa186`

###### A.6.1.1.1.2.6.1.3.1.7.6.2.3 - Rate Limit IDs [Core]  <!-- UUID: d319be68-9f32-47be-a74c-cf9c79821027 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.7.6.2.4 - Rate Limits [Core]  <!-- UUID: 7de1e41d-c8b5-4ec6-931b-ae3ee2f3f4a3 -->

The current `maxAmount`, `slope` and slippage for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.7.6.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: e8419a65-2e14-4f59-af28-a224cb00e5c4 -->

The inflow rate limits are:

- maxAmount: N/A - swap only
- slope: N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.6.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 0fc9d196-84f9-453e-af4a-4d8efefd2d3e -->

The outflow rate limits are:

- maxAmount: N/A - swap only
- slope: N/A - swap only

###### A.6.1.1.1.2.6.1.3.1.7.6.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: ff055884-4518-41ae-a320-dd7293147a37 -->

The swap rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 25,000,000 per day
- `Max slippage`: 0.1%

###### A.6.1.1.1.2.6.1.3.1.7.6.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: c73a4929-43af-451b-875d-f9e7c8c54a2a -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.7.6.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 28144d70-2c9d-4415-ab38-b440bc27b58a -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.8 - Morpho [Core]  <!-- UUID: 8efd627c-7439-4ea9-aabc-ecdffb5cb2ec -->

The Ethereum Mainnet Instances of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.8.1 - Ethereum Mainnet - Morpho Dai Instance Configuration Document [Core]  <!-- UUID: 626dd4bf-108b-48bd-a1e1-c26d290c3a72 -->

The documents herein contain the Instance Configuration Document for the Morpho Dai Instance.

###### A.6.1.1.1.2.6.1.3.1.8.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: a96c3d29-51b2-45b8-9820-56ec9edeffd3 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.8.1.2 - Parameters [Core]  <!-- UUID: b0ae7680-7179-4fd6-93f0-56c03d6f91eb -->

The documents herein define the parameters of the Morpho Dai Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.8.1.2.1 - Instance Identifiers [Core]  <!-- UUID: d378528c-192a-4b4b-b4ad-0fd39cf6d9a0 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.8.1.2.1.1 - Network [Core]  <!-- UUID: acfbf398-dfe6-415a-8355-36aaf57b4322 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.8.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 4de6d799-4ebf-4876-af77-c9cbfee16bac -->

Morpho

###### A.6.1.1.1.2.6.1.3.1.8.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 5bde4982-cdea-482b-972a-372352c883a1 -->

Dai

###### A.6.1.1.1.2.6.1.3.1.8.1.2.1.4 - Token [Core]  <!-- UUID: a1eca238-d0bc-4372-899e-3cd3c42908cc -->

spDAI

###### A.6.1.1.1.2.6.1.3.1.8.1.2.2 - Contract Addresses [Core]  <!-- UUID: 1de795f6-94fe-4a9b-8952-f11375f2c330 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.8.1.2.2.1 - Token Address [Core]  <!-- UUID: 1614a57a-15d9-4081-862b-d1b1d80f59f4 -->

`0x73e65DBD630f90604062f6E02fAb9138e713edD9`

###### A.6.1.1.1.2.6.1.3.1.8.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: faf749a9-9737-49c8-8783-e09034ab190d -->

`0x6B175474E89094C44Da98b954EedeAC495271d0F`

###### A.6.1.1.1.2.6.1.3.1.8.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 191e781d-17da-459c-9366-88d0efc8a4d8 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.8.1.2.4 - Rate Limits [Core]  <!-- UUID: 9a6b7691-5bdf-497d-a8d3-0421624c23c1 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.8.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 27c105d3-a93c-45b9-b951-050e60a50c51 -->

The inflow rate limits are:

- `maxAmount`: 200,000,000 DAI
- `slope`: 100,000,000 DAI per day

###### A.6.1.1.1.2.6.1.3.1.8.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 5cbdb15a-3a5b-4ea3-9fc2-4098f512712c -->

The outflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.8.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: d39f115f-51e6-466a-a329-8761d4ae50c0 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.8.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: e76bc120-89fd-438f-b338-7951f4660a7e -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.8.2 - Ethereum Mainnet - Morpho USDS Instance Configuration Document [Core]  <!-- UUID: 138be894-8a4a-4e8c-9fdd-0f8183935d24 -->

The documents herein contain the Instance Configuration Document for the Morpho USDS Instance.

###### A.6.1.1.1.2.6.1.3.1.8.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 0fd39503-617a-4850-8a11-2b0f2f7b5ae7 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.8.2.2 - Parameters [Core]  <!-- UUID: f1b8abcc-2254-4826-9a82-f03f78d4f846 -->

The documents herein define the parameters of the Morpho USDS Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.8.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 1676db92-f89e-4701-b4ea-dc14475b603c -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.8.2.2.1.1 - Network [Core]  <!-- UUID: 146f0253-a524-4d2d-b047-68df518ea163 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.8.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 0e95f0b2-4d41-4676-8dcb-f5faeb2768ef -->

Morpho

###### A.6.1.1.1.2.6.1.3.1.8.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 0a270b1d-8ce7-487c-b571-1f7f114eb19e -->

USDS

###### A.6.1.1.1.2.6.1.3.1.8.2.2.1.4 - Token [Core]  <!-- UUID: 55807963-1266-4eb3-ba61-f1073dbcc685 -->

sparkUSDS

###### A.6.1.1.1.2.6.1.3.1.8.2.2.2 - Contract Addresses [Core]  <!-- UUID: 5bdcf2a4-85a3-45df-b525-3de5fce91391 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.8.2.2.2.1 - Token Address [Core]  <!-- UUID: 972aa481-5c2c-44e0-956e-f649e86f6cc2 -->

`0xe41a0583334f0dc4E023Acd0bFef3667F6FE0597`

###### A.6.1.1.1.2.6.1.3.1.8.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 64e52154-360d-49e5-882c-6ef389b7a2df -->

`0xdC035D45d973E3EC169d2276DDab16f1e407384F`

###### A.6.1.1.1.2.6.1.3.1.8.2.2.2.3 - Allocator Role Address [Core]  <!-- UUID: e40cb4f0-7ff1-4c64-a936-5e33189952a5 -->

`0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178`

###### A.6.1.1.1.2.6.1.3.1.8.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 73b8b172-1562-4729-9d21-832bf1efdd19 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.8.2.2.4 - Rate Limits [Core]  <!-- UUID: aa89df3f-655e-4e91-952b-41db6b7e5671 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.8.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 6fb6752a-a468-4f67-92a3-f86038be581d -->

The inflow rate limits are:

- `maxAmount`: 200,000,000 USDS
- `slope`: 100,000,000 USDS per day

###### A.6.1.1.1.2.6.1.3.1.8.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 6f8914eb-62e1-4946-901a-ae70839845fc -->

The outflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.8.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 731b87e1-bf2e-4214-9574-16074809b771 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.8.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 86e8dd23-9895-453f-a56a-460eaff0c0a2 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.8.2.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: e560d14b-b1f1-4351-9214-62a3d6d7fd53 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.1.8.2.4.1 - Contract Addresses [Core]  <!-- UUID: bfdae446-8562-4c34-8bf8-9f6d7d612d2e -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.8.2.4.1.1 - Curator Role Address [Core]  <!-- UUID: ca1eb012-2401-4e24-9e9e-a76f869e422d -->

`0x0f963A8A8c01042B69054e787E5763ABbB0646A3`

###### A.6.1.1.1.2.6.1.3.1.8.2.4.1.2 - Guardian Role Address [Core]  <!-- UUID: 86831263-5a01-4259-80e6-7829f062a1e6 -->

`0xf5748bBeFa17505b2F7222B23ae11584932C908B`

###### A.6.1.1.1.2.6.1.3.1.8.2.4.2 - Timelock [Core]  <!-- UUID: bf0333e1-219a-4dc2-89d9-0ac64907c3d2 -->

Timelock: 240 hours (10 days)

###### A.6.1.1.1.2.6.1.3.1.8.3 - Ethereum Mainnet - Morpho USDC Instance Configuration Document [Core]  <!-- UUID: f3063596-4f85-4a51-b52c-58221d043d3e -->

The documents herein contain the Instance Configuration Document for the Morpho USDC Instance.

###### A.6.1.1.1.2.6.1.3.1.8.3.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 6e492a2b-7105-4c7f-a659-2fa62dc3617f -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.8.3.2 - Parameters [Core]  <!-- UUID: 925286bb-f987-4d35-8c74-23279a2c018f -->

The documents herein define the parameters of the Morpho USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.8.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 46c99f91-4d4f-424f-a431-439103ad83f4 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.8.3.2.1.1 - Network [Core]  <!-- UUID: f02eb3b3-62df-4086-8e85-be37f7b80d85 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.8.3.2.1.2 - Target Protocol [Core]  <!-- UUID: ed302176-488b-43e5-ac32-51c77badf0fe -->

Morpho

###### A.6.1.1.1.2.6.1.3.1.8.3.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: c1dd3047-57f6-4410-9c13-febcceae5971 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.8.3.2.1.4 - Token [Core]  <!-- UUID: f056c54a-476a-419c-8baf-2d5c5b70797f -->

sparkUSDCbc

###### A.6.1.1.1.2.6.1.3.1.8.3.2.2 - Contract Addresses [Core]  <!-- UUID: 73277621-b349-47cf-af66-a5444f8f1c58 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.8.3.2.2.1 - Token Address [Core]  <!-- UUID: 711b3b1f-ecf8-42d4-8112-00d032cb4293 -->

`0x56A76b428244a50513ec81e225a293d128fd581D`

###### A.6.1.1.1.2.6.1.3.1.8.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: cfad62db-289a-4840-a31b-1ec231c8a1da -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.8.3.2.2.3 - Allocator Role Address [Core]  <!-- UUID: b63d90f5-1c8a-41e0-8ada-5db9986ec4a2 -->

`0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178`

###### A.6.1.1.1.2.6.1.3.1.8.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: 5b0ead44-7dce-4af5-b750-422c8f97c4ce -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.8.3.2.4 - Rate Limits [Core]  <!-- UUID: d24c412e-6ba8-4b1b-a3c6-ccb48b268e2f -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.8.3.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 024d6105-55ae-4a54-b5be-c5e17987fb0f -->

The inflow rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 25,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.8.3.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 7385df6a-1431-41ef-8f05-bc4e78d48ed3 -->

The outflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.8.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 564ac34b-aa6c-46ec-9fd4-9f7caed7c31b -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.8.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: d778fa59-35a2-4b5a-9e22-2880e99746a4 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.8.3.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: d30c7467-bdc4-42b7-a0fd-332828e5acd7 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.1.8.3.4.1 - Contract Addresses [Core]  <!-- UUID: a672e8f2-886e-4d1f-a217-364e638408d9 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.8.3.4.1.1 - Curator Role Address [Core]  <!-- UUID: ac41be8b-f6c9-4df2-9fac-c543c77e0166 -->

`0x0f963A8A8c01042B69054e787E5763ABbB0646A3`

###### A.6.1.1.1.2.6.1.3.1.8.3.4.1.2 - Guardian Role Address [Core]  <!-- UUID: b7d0b9a8-4dba-4fba-8aab-b5afd645a6d0 -->

`0xf5748bBeFa17505b2F7222B23ae11584932C908B`

###### A.6.1.1.1.2.6.1.3.1.8.3.4.2 - Timelock [Core]  <!-- UUID: d2692d99-d52c-4586-8dbe-b23d8f835f29 -->

Timelock: 240 hours (10 days)

###### A.6.1.1.1.2.6.1.3.1.8.4 - Ethereum Mainnet - Spark Blue Chip USDT Vault Instance Configuration Document [Core]  <!-- UUID: 2019122c-c16d-4132-ae08-8416c3f83b23 -->

The documents herein contain the Instance Configuration Document for the Spark Blue Chip USDT Vault Instance.

###### A.6.1.1.1.2.6.1.3.1.8.4.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 045b5df6-b987-41a4-8375-cb3184f1544c -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.8.4.2 - Parameters [Core]  <!-- UUID: 0d0b492a-ad25-43a0-8a45-3ac1021cd491 -->

The documents herein define the parameters of the Spark Blue Chip USDT Vault Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.8.4.2.1 - Instance Identifiers [Core]  <!-- UUID: e93f8500-aa6e-40e1-8ad9-848454571620 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.8.4.2.1.1 - Network [Core]  <!-- UUID: 80f7fecc-cfbf-4f86-878e-23298f9d8f44 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.8.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 0f19955b-0c74-4c25-8522-8487888d016e -->

Morpho

###### A.6.1.1.1.2.6.1.3.1.8.4.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 0f988a3f-3275-4785-a4b2-5a8b68636058 -->

USDT

###### A.6.1.1.1.2.6.1.3.1.8.4.2.1.4 - Token [Core]  <!-- UUID: 7afd18bc-eb99-4aa1-8096-863c3e8b5d68 -->

sparkUSDT

###### A.6.1.1.1.2.6.1.3.1.8.4.2.2 - Contract Addresses [Core]  <!-- UUID: 3b1e6448-26b6-4db8-b33d-15ee6ef2edfa -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.8.4.2.2.1 - Token Address [Core]  <!-- UUID: 0830d4af-65df-489c-9402-99696215f667 -->

`0xb0c424116172B55CbB6dD3136F5989F7959e5B91`

###### A.6.1.1.1.2.6.1.3.1.8.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 65ac69fd-913a-44cd-bb38-c93ef3726dbe -->

`0xdac17f958d2ee523a2206206994597c13d831ec7`

###### A.6.1.1.1.2.6.1.3.1.8.4.2.2.3 - Allocator Role Address [Core]  <!-- UUID: 3d9e1745-e0c1-4b75-8c3e-04a87019d8db -->

`0xe5c6318456a7Cb6f74f93B4eee4616dB5fcef699`

###### A.6.1.1.1.2.6.1.3.1.8.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: 0e2d991d-9225-48f8-a9a3-dacf6c182181 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.8.4.2.4 - Rate Limits [Core]  <!-- UUID: 46f33c44-c9b3-4241-a5ad-84f4f7765280 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.8.4.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 9f2b2176-e725-4f93-bcda-62b466f502e8 -->

The inflow rate limits are:

- `maxAmount`: 100,000,000 USDT
- `slope`: 1,000,000,000 USDT per day

###### A.6.1.1.1.2.6.1.3.1.8.4.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 779c6c99-f620-4bd0-b261-7d36b6d503b7 -->

The outflow rate limits are:

- `maxAmount`: unlimited
- `slope`: unlimited

###### A.6.1.1.1.2.6.1.3.1.8.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 4b630d7d-09ee-4039-8850-71a2d287fe3e -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.8.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: b213d173-e3b9-41a0-9ae2-ba5a2526aa42 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.8.4.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: e0e9f22c-2c9c-43f8-87be-fb4bbb14804a -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.1.8.4.4.1 - Contract Addresses [Core]  <!-- UUID: e88e8a71-3860-4a30-9446-dc3fe19fbd17 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.8.4.4.1.1 - Curator Role Address [Core]  <!-- UUID: f9605664-b8e2-4efb-b4ef-c60d5d85ec8a -->

`0x0f963A8A8c01042B69054e787E5763ABbB0646A3`

###### A.6.1.1.1.2.6.1.3.1.8.4.4.1.2 - Guardian Role Address [Core]  <!-- UUID: 9eeee40f-fb34-4ca0-922a-ad54fb4d30c1 -->

`0xf5748bBeFa17505b2F7222B23ae11584932C908B`

###### A.6.1.1.1.2.6.1.3.1.8.4.4.2 - Timelock [Core]  <!-- UUID: f44940e3-fda2-444c-a2ae-bd91d00b411c -->

Timelock: 240 hours (10 days)

###### A.6.1.1.1.2.6.1.3.1.9 - Spark Savings V2 [Core]  <!-- UUID: 47f2b461-1d82-4ee8-8cd2-39c95184c51b -->

The Ethereum Mainnet Instances of the Spark Savings v2 with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.9.1 - Ethereum Mainnet - Spark Savings v2 ETH Instance Configuration Document [Core]  <!-- UUID: 831b4fd8-06c6-4734-bb3a-93678082d8cc -->

The documents herein contain the Instance Configuration Document for the Spark Savings v2 ETH Instance.

###### A.6.1.1.1.2.6.1.3.1.9.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 917d6e87-5dd3-4190-9ec6-909460d88b03 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.9.1.2 - Parameters [Core]  <!-- UUID: e55eba15-5b8d-4a2d-bf5a-704dfceb6457 -->

The documents herein define the parameters of the Spark Savings v2 ETH Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.9.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 95bbd1c5-f7c9-4f77-883c-a593fd930656 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.9.1.2.1.1 - Network [Core]  <!-- UUID: 448d472c-0d5f-4a24-a4f0-6ee855f384ac -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.9.1.2.1.2 - Target Protocol [Core]  <!-- UUID: ad53ae31-1644-4680-bcf3-ca894600199e -->

Spark Savings Protocol

###### A.6.1.1.1.2.6.1.3.1.9.1.2.1.3 - Asset Supplied By Users [Core]  <!-- UUID: 8d9ff794-c545-4179-8bb4-214943250467 -->

wETH

###### A.6.1.1.1.2.6.1.3.1.9.1.2.1.4 - Token [Core]  <!-- UUID: 964ef35e-bde9-4fa3-b07b-f423f35d2f80 -->

spETH

###### A.6.1.1.1.2.6.1.3.1.9.1.2.2 - Contract Addresses [Core]  <!-- UUID: a59789f1-bcad-42a3-98ba-bb9c0aa92b0d -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.9.1.2.2.1 - Token Address [Core]  <!-- UUID: 93f2939e-b2d2-4c2e-b74d-8af8b9fbf12e -->

`0xfE6eb3b609a7C8352A241f7F3A21CEA4e9209B8f`

###### A.6.1.1.1.2.6.1.3.1.9.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: cb300f77-edf2-45eb-8f2a-14d1455a7d1d -->

`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`

###### A.6.1.1.1.2.6.1.3.1.9.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 0471c82b-6517-4f35-afe2-eebe6a02d052 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.9.1.2.4 - Rate Limits [Core]  <!-- UUID: 318fa90a-2fd9-42cc-af6a-086063caebc6 -->

The specific `maxAmount` and `slope` for this conduit's inflow/outflow are not defined for this Instance.

###### A.6.1.1.1.2.6.1.3.1.9.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 87c19bc8-2029-498e-887b-f5c9ec095107 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.9.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: c22fc43d-2947-4919-a266-9e5809a93736 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.9.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 06f87be7-087d-480c-8cd8-4baa4ab4b170 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.1.9.1.4.1 - Contract Addresses [Core]  <!-- UUID: 7fde7297-118e-4485-b4bd-c844773e0233 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.9.1.4.1.1 - Spark Vault v2 Implementation [Core]  <!-- UUID: 868225a7-68c0-4046-9ee9-9461963664a8 -->

`0x1b992302652A92611DCd5090D1Cb388C6377f455`

###### A.6.1.1.1.2.6.1.3.1.9.1.4.1.2 - Default admin [Core]  <!-- UUID: 3b166ec3-5185-4b14-8737-7febd99ec3e8 -->

`0x3300f198988e4C9C63F75dF86De36421f06af8c4`

###### A.6.1.1.1.2.6.1.3.1.9.1.4.1.3 - Setter [Core]  <!-- UUID: a2802a44-0979-4af6-bbdf-ffb01f46120d -->

`0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC`

###### A.6.1.1.1.2.6.1.3.1.9.1.4.1.4 - Taker [Core]  <!-- UUID: e58963e6-b6a5-4ecd-a681-117ec7eaa2ae -->

`0x1601843c5E9bC251A3272907010AFa41Fa18347E`

###### A.6.1.1.1.2.6.1.3.1.9.1.4.2 - Risk Parameters Current Configuration [Core]  <!-- UUID: cafa5499-a804-479b-8af9-5a07cd4735af -->

The subdocuments herein define the current configuration of the risk parameters.

###### A.6.1.1.1.2.6.1.3.1.9.1.4.2.1 - Spark Savings ETH Risk Parameters [Core]  <!-- UUID: 94ab6b40-66aa-4a42-8df9-b9fb633ba306 -->

The Risk parameters are:

- Supply cap: 500,000 WETH
- Max yield: 5%
- Current yield (at launch): 0%

###### A.6.1.1.1.2.6.1.3.1.9.1.4.2.2 - Rate Limits [Core]  <!-- UUID: e4e8eee4-c449-4adc-aae7-d7fa31f311e0 -->

The current `maxAmount` for this conduit's take and transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.9.1.4.2.3 - Take Rate Limits [Core]  <!-- UUID: d516e83f-017b-45ac-88bc-67c4a8eb3e57 -->

The take rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.9.1.4.2.4 - TransferAssets Rate Limits [Core]  <!-- UUID: 85e39357-e537-4175-be32-a6753f27d5f2 -->

The transferAssets rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.9.2 - Ethereum Mainnet - Spark Savings v2 USDC Instance Configuration Document [Core]  <!-- UUID: eeb34a6e-e377-4115-92f9-d299f6d2a5d9 -->

The documents herein contain the Instance Configuration Document for the Spark Savings v2 USDC Instance.

###### A.6.1.1.1.2.6.1.3.1.9.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 6852af1c-6e3c-4599-9f76-3b1587ec7c53 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.9.2.2 - Parameters [Core]  <!-- UUID: 14fe988d-d2a9-4c95-b0d3-63fe58ab40d5 -->

The documents herein define the parameters of the Spark Savings v2 ETH Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.9.2.2.1 - Instance Identifiers [Core]  <!-- UUID: a4a68c40-17d3-4a60-ac15-c2bfe0fa7a3e -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.9.2.2.1.1 - Network [Core]  <!-- UUID: 53035cdc-866c-4901-9744-74a92b537f75 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.9.2.2.1.2 - Target Protocol [Core]  <!-- UUID: e7fd4b6e-94a8-4078-ab32-4a4c719d033c -->

Spark Savings Protocol

###### A.6.1.1.1.2.6.1.3.1.9.2.2.1.3 - Asset Supplied By Users [Core]  <!-- UUID: b67d52f5-8242-402a-8f22-b13ecd3874f6 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.9.2.2.1.4 - Token [Core]  <!-- UUID: 6131b29c-52b3-492a-8197-0af376bb60bb -->

spUSDC

###### A.6.1.1.1.2.6.1.3.1.9.2.2.2 - Contract Addresses [Core]  <!-- UUID: d75699b9-f1d0-4da7-ba6b-23f244047072 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.9.2.2.2.1 - Token Address [Core]  <!-- UUID: 60e2171d-0b25-405c-9ca5-627e8049b8b1 -->

`0x28B3a8fb53B741A8Fd78c0fb9A6B2393d896a43d`

###### A.6.1.1.1.2.6.1.3.1.9.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 4065d210-a9ee-4d96-83f0-c4ff4ac09a07 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.9.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: fa5d229a-040c-447f-bd53-24ef6c5e735c -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.9.2.2.4 - Rate Limits [Core]  <!-- UUID: d6d28ef9-cafd-434c-a106-8dfae2ff8908 -->

The specific `maxAmount` and `slope` for this conduit's inflow/outflow are not defined for this Instance.

###### A.6.1.1.1.2.6.1.3.1.9.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: c4b21848-5450-4e0a-adac-dd97b4bd562b -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.9.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 5a7fa3ce-f71c-4c57-85f3-c3450881bd56 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.9.2.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 7ea9a810-7278-46c9-9adb-ad4d48c393f0 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.1.9.2.4.1 - Contract Addresses [Core]  <!-- UUID: fbff1bf2-67ae-48e4-9724-4126b24b5b24 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.9.2.4.1.1 - Spark Vault v2 Implementation [Core]  <!-- UUID: b7396d52-e3b6-4d56-a95f-9f4c8309d954 -->

`0x1b992302652A92611DCd5090D1Cb388C6377f455`

###### A.6.1.1.1.2.6.1.3.1.9.2.4.1.2 - Default admin [Core]  <!-- UUID: 5d658c45-cd8f-4598-b535-648a3a621526 -->

`0x3300f198988e4C9C63F75dF86De36421f06af8c4`

###### A.6.1.1.1.2.6.1.3.1.9.2.4.1.3 - Setter [Core]  <!-- UUID: ca64abf7-8cd3-4368-8c83-bca52968008d -->

`0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC`

###### A.6.1.1.1.2.6.1.3.1.9.2.4.1.4 - Taker [Core]  <!-- UUID: 35c9a6ce-92f8-4a3a-a95a-0e2513360afd -->

`0x1601843c5E9bC251A3272907010AFa41Fa18347E`

###### A.6.1.1.1.2.6.1.3.1.9.2.4.2 - Risk Parameters Current Configuration [Core]  <!-- UUID: 135300b0-5b11-4d6f-8b26-9aef99f5fb39 -->

The subdocuments herein define the current configuration of the risk parameters.

###### A.6.1.1.1.2.6.1.3.1.9.2.4.2.1 - Spark Savings USDC Risk Parameters [Core]  <!-- UUID: 2470f2c9-e160-40d8-8d9e-69b09bd8ee39 -->

The Risk parameters are:

- Supply cap: 2,000,000,000 USDC
- Max yield: 10%
- Current yield (at launch): 0%

###### A.6.1.1.1.2.6.1.3.1.9.2.4.2.2 - Rate Limits [Core]  <!-- UUID: 9ea0e72b-2fc7-4291-b589-3414cdb7baac -->

The current `maxAmount` for this conduit's take and transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.9.2.4.2.3 - Take Rate Limits [Core]  <!-- UUID: 4b64fc4a-b6ef-49d9-b212-8894526b680d -->

The take rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.9.2.4.2.4 - TransferAssets Rate Limits [Core]  <!-- UUID: a3af1ab3-c7a5-4f27-90db-0c01ac73f39e -->

The transferAssets rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.9.3 - Ethereum Mainnet - Spark Savings v2 USDT Instance Configuration Document [Core]  <!-- UUID: 0cc91e92-4523-4d3b-87a5-bb9a695d696c -->

The documents herein contain the Instance Configuration Document for the Spark Savings v2 USDT Instance.

###### A.6.1.1.1.2.6.1.3.1.9.3.1 - RRC Framework Full Implementation [Core]  <!-- UUID: ff0f290d-12eb-4c72-ae60-a5097c6dd671 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.9.3.2 - Parameters [Core]  <!-- UUID: f3eae5f3-db85-4f92-9fca-46c13af64d99 -->

The documents herein define the parameters of the Spark Savings v2 USDT Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.9.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 90db3809-ee39-43de-9a3a-07c9c3be77cc -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.9.3.2.1.1 - Network [Core]  <!-- UUID: 5f4150e0-c263-49b9-802f-acbc93f9e5d7 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.9.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 83932398-c228-4d62-b3b0-0b0a96c82fe9 -->

Spark Savings Protocol

###### A.6.1.1.1.2.6.1.3.1.9.3.2.1.3 - Asset Supplied By Users [Core]  <!-- UUID: 10229012-9591-4ac2-a82f-744ffb2a38d0 -->

USDT

###### A.6.1.1.1.2.6.1.3.1.9.3.2.1.4 - Token [Core]  <!-- UUID: 9bf00b29-a6e5-4850-9247-a46b9ee47f2b -->

spUSDT

###### A.6.1.1.1.2.6.1.3.1.9.3.2.2 - Contract Addresses [Core]  <!-- UUID: f8105d2e-11cc-4f40-a2c2-0c919ae89422 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.9.3.2.2.1 - Token Address [Core]  <!-- UUID: 224538f9-fde7-43f3-aa9b-1c3cf6036663 -->

`0xe2e7a17dFf93280dec073C995595155283e3C372`

###### A.6.1.1.1.2.6.1.3.1.9.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 2959cf7c-9026-45d9-83d4-2ef755613d33 -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.9.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: d031b87f-ee09-4019-a7d8-1dcc6c698622 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.9.3.2.4 - Rate Limits [Core]  <!-- UUID: ab480592-3e9b-4bdb-9e8d-80e4370a964e -->

The specific `maxAmount` and `slope` for this conduit's inflow/outflow are not defined for this Instance.

###### A.6.1.1.1.2.6.1.3.1.9.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 5059455b-0fc8-4ab7-b9c2-78cfd9ab253f -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.9.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 0ae91e4f-3189-4aba-858f-eff906496b9b -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.9.3.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 248a7063-2c28-4077-99af-d2db125d6c02 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.1.9.3.4.1 - Contract Addresses [Core]  <!-- UUID: 1978c0cd-a433-4232-ab94-438ba1fbd511 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.9.3.4.1.1 - Spark Vault v2 Implementation [Core]  <!-- UUID: 730c2ba9-d2d3-438c-881b-a36d7c698c2e -->

`0x1b992302652A92611DCd5090D1Cb388C6377f455`

###### A.6.1.1.1.2.6.1.3.1.9.3.4.1.2 - Default admin [Core]  <!-- UUID: a84b734e-7bcf-4a29-8173-bf2388756074 -->

`0x3300f198988e4C9C63F75dF86De36421f06af8c4`

###### A.6.1.1.1.2.6.1.3.1.9.3.4.1.3 - Setter [Core]  <!-- UUID: dfda6276-2747-4135-996a-d516eb734855 -->

`0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC`

###### A.6.1.1.1.2.6.1.3.1.9.3.4.1.4 - Taker [Core]  <!-- UUID: 5fdbbda4-844e-4280-bacd-0cad16dbf3de -->

`0x1601843c5E9bC251A3272907010AFa41Fa18347E`

###### A.6.1.1.1.2.6.1.3.1.9.3.4.2 - Risk Parameters Current Configuration [Core]  <!-- UUID: 64c424db-af06-4910-b9f4-df2560236a99 -->

The subdocuments herein define the current configuration of the risk parameters.

###### A.6.1.1.1.2.6.1.3.1.9.3.4.2.1 - Spark Savings USDT Risk Parameters [Core]  <!-- UUID: 473796c1-c41f-4924-80f6-468f966fa064 -->

The Risk parameters are:

- Supply cap: 4,000,000,000 USDT
- Max yield: 10%
- Current yield (at launch): 0%

###### A.6.1.1.1.2.6.1.3.1.9.3.4.2.2 - Rate Limits [Core]  <!-- UUID: 3802d641-27cf-4ec1-bba4-6a09a84071af -->

The current `maxAmount` for this conduit's take and transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.9.3.4.2.3 - Take Rate Limits [Core]  <!-- UUID: fc186f71-dce3-46d8-bf50-fcccdfad5e5d -->

The take rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.9.3.4.2.4 - TransferAssets Rate Limits [Core]  <!-- UUID: 9c92bc84-cfdf-4356-8fc4-4df33937ec89 -->

The transferAssets rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.9.4 - Ethereum Mainnet - Spark Savings v2 spPYUSD Instance Configuration Document [Core]  <!-- UUID: 0b280652-ea99-4a53-8c9e-fb23b200d446 -->

The documents herein contain the Instance Configuration Document for the Spark Savings v2 spPYUSD Instance.

###### A.6.1.1.1.2.6.1.3.1.9.4.1 - RRC Framework Full Implementation [Core]  <!-- UUID: bc708dab-227b-4512-9c0d-d6205b5db840 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.1.9.4.2 - Parameters [Core]  <!-- UUID: 93f2f53e-1907-4828-b1a6-dbd0838e17ff -->

The documents herein define the parameters of the Spark Savings v2 spPYUSD Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.9.4.2.1 - Instance Identifiers [Core]  <!-- UUID: d8f4f071-4dd2-4b24-b3fb-da99dc7e05c8 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.1.2.6.1.3.1.9.4.2.1.1 - Network [Core]  <!-- UUID: 5df33a54-f040-4784-b3de-1eef0a6aa58a -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.9.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 4030df21-d528-4d68-a08a-861344b8db1c -->

Spark Savings Protocol

###### A.6.1.1.1.2.6.1.3.1.9.4.2.1.3 - Asset Supplied By Users [Core]  <!-- UUID: 40afdb41-a6e3-4e33-b01c-c145aa234170 -->

PYUSD

###### A.6.1.1.1.2.6.1.3.1.9.4.2.1.4 - Token [Core]  <!-- UUID: bf8871b0-7a57-470c-8ac5-82f104220289 -->

spPYUSD

###### A.6.1.1.1.2.6.1.3.1.9.4.2.2 - Contract Addresses [Core]  <!-- UUID: edc37448-90df-45c7-a0d8-f7aef9ff85a6 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.9.4.2.2.1 - Token Address [Core]  <!-- UUID: 32e9ffdc-e437-46cb-a2fc-272fb3e826a7 -->

`0x80128DbB9f07b93DDE62A6daeadb69ED14a7D354`

###### A.6.1.1.1.2.6.1.3.1.9.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: e3bf5dca-f865-45b0-87dd-1bb67b9b52af -->

`0x6c3ea9036406852006290770bedfcaba0e23a0e8`

###### A.6.1.1.1.2.6.1.3.1.9.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: 2f06d1e8-bcc6-4ac2-92af-3006f1abaa02 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.9.4.2.4 - Rate Limits [Core]  <!-- UUID: 8d9562b5-4277-4c63-96a2-923a36afb192 -->

The specific `maxAmount` and `slope` for this conduit's inflow/outflow are not defined for this Instance.

###### A.6.1.1.1.2.6.1.3.1.9.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 02970ea9-7538-4d59-b6fe-28220cfb61e2 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.9.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 14ccaa13-1c17-4161-bf53-005dcc75bfd9 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.9.4.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: f1f811e3-5489-45ca-a293-495eff825381 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.1.9.4.4.1 - Contract Addresses [Core]  <!-- UUID: cd1a9cac-7b69-45af-85ac-bbf39e0b7f12 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.9.4.4.1.1 - Spark Vault v2 Implementation [Core]  <!-- UUID: 3ebbf669-af67-4b15-880e-4a5b5c74dce1 -->

`0x1b992302652A92611DCd5090D1Cb388C6377f455`

###### A.6.1.1.1.2.6.1.3.1.9.4.4.1.2 - Default admin [Core]  <!-- UUID: f13af98a-f12f-48b6-8827-ba942ccacbcf -->

`0x3300f198988e4C9C63F75dF86De36421f06af8c4`

###### A.6.1.1.1.2.6.1.3.1.9.4.4.1.3 - Setter [Core]  <!-- UUID: 2ece6e1d-b07a-4df5-9aa6-616756f64815 -->

`0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178`

###### A.6.1.1.1.2.6.1.3.1.9.4.4.1.4 - Taker [Core]  <!-- UUID: 32dc1afe-59e0-472d-8f09-c2a923adb6bb -->

`0x1601843c5E9bC251A3272907010AFa41Fa18347E`

###### A.6.1.1.1.2.6.1.3.1.9.4.4.2 - Risk Parameters Current Configuration [Core]  <!-- UUID: 5d4ed5ae-8141-43da-a20a-42238170e1a3 -->

The subdocuments herein define the current configuration of the risk parameters.

###### A.6.1.1.1.2.6.1.3.1.9.4.4.2.1 - Spark Savings spPYUSD Risk Parameters [Core]  <!-- UUID: 48e7ec46-a69b-41cc-ab24-eb9c05324a07 -->

The Risk parameters are:

- Supply cap: 250,000,000 PYUSD
- Max yield: 10%
- Current yield (at launch): 0%

###### A.6.1.1.1.2.6.1.3.1.9.4.4.2.2 - Rate Limits [Core]  <!-- UUID: 8a75c7ba-4d34-4e0e-8f6e-25e765fcbe36 -->

The current `maxAmount` for this conduit's take and transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.9.4.4.2.3 - Take Rate Limits [Core]  <!-- UUID: 6343b9eb-fa3e-4ca6-8f98-90c08d400c0f -->

The take rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.9.4.4.2.4 - TransferAssets Rate Limits [Core]  <!-- UUID: f291a712-4c0c-4ef4-8d2f-0b558fb9cbbe -->

The transferAssets rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.10 - Arkis [Core]  <!-- UUID: 61ad54f3-9faa-4a9a-9cee-e685fb8fc4cf -->

The Ethereum Mainnet Instances of the Arkis Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.10.1 - Ethereum Mainnet - Arkis Instance Configuration Document [Core]  <!-- UUID: 4bb58af1-fc25-442f-83a9-dd40989a7d37 -->

The documents herein contain the Instance Configuration Document for the Arkis Instance.

###### A.6.1.1.1.2.6.1.3.1.10.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 4ec36447-71fa-4a0f-865a-1353740b663d -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.10.1.2 - Parameters [Core]  <!-- UUID: e1921ad5-ff6f-4ffe-9e69-1d1796567296 -->

The documents herein define the parameters of the Arkis Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.10.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 4aafd731-9770-4f4c-925a-7f54fcca8327 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.1.2.6.1.3.1.10.1.2.1.1 - Network [Core]  <!-- UUID: cc527da6-8dce-4165-a1ea-22075da1b3e2 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.10.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 092f9755-377e-4d34-9abc-7b7293cf5f64 -->

Arkis

###### A.6.1.1.1.2.6.1.3.1.10.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 521360e7-dccc-4066-a69c-ea2a2c6a2306 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.10.1.2.1.4 - Token [Core]  <!-- UUID: d148fb40-413f-4ef7-a852-e26f613c8cd0 -->

spUSDC

###### A.6.1.1.1.2.6.1.3.1.10.1.2.2 - Contract Addresses [Core]  <!-- UUID: 39ee8922-db8a-47d7-a4ac-f183e1314975 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.10.1.2.2.1 - Token Address [Core]  <!-- UUID: befde66f-e9f7-4f70-b107-ded60431052f -->

`0x377C3bd93f2a2984E1E7bE6A5C22c525eD4A4815`

###### A.6.1.1.1.2.6.1.3.1.10.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: fa448799-af8f-494d-9db8-5361ea02b576 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.10.1.2.2.3 - Pool Address [Core]  <!-- UUID: 8efbce12-9417-4ab7-9e55-6194ee592bd4 -->

The pool address will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.10.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 541b2c98-6c5d-4e8d-9aef-30d3b15bd6bc -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.10.1.2.4 - Rate Limits [Core]  <!-- UUID: fde9903c-91a1-40f8-bc4a-a6511bb346aa -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.10.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: ce2b927e-3338-4101-a538-ca1a02ae917c -->

The inflow rate limits are:

- `maxAmount`: 5,000,000 USDC
- `slope`: 5,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.10.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 61f4c11f-73d0-49f2-ba54-abf214c60881 -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.10.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 389d1003-434b-4acb-a0db-7a587a5ee006 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.10.1.2.5.1 - Maximum Exposure [Core]  <!-- UUID: baf1fbad-0ef7-424e-832f-bd0c47377144 -->

The Maximum Exposure for this Instance is $50 million.

###### A.6.1.1.1.2.6.1.3.1.10.1.2.5.2 - Instance Capital Ratio Requirement [Core]  <!-- UUID: c9cc845b-9971-4ee5-a5ec-e3d2771d85e2 -->

The Instance Capital Ratio Requirement for this Instance is 50%.

###### A.6.1.1.1.2.6.1.3.1.10.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 0a1caa15-48bb-4047-bf18-76f65ba20410 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.11 - Uniswap v4 [Core]  <!-- UUID: 6c5c956c-608f-40aa-9911-d1c04df4f99e -->

The Ethereum Mainnet Instances of the Uniswap v4 Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.11.1 - Ethereum Mainnet - Uniswap v4 PYUSD/USDS Pool Instance Configuration Document [Core]  <!-- UUID: c5d16727-69f7-454a-a3da-85c46dd9eed2 -->

The documents herein contain the Instance Configuration Document for the Uniswap v4 PYUSD/USDS Pool Instance.

###### A.6.1.1.1.2.6.1.3.1.11.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: bd5042f9-cd5d-4574-b868-d0b9ad247a3a -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.11.1.2 - Parameters [Core]  <!-- UUID: 4139b0ae-87f7-4b3f-aa48-78ee8efc1047 -->

The documents herein define the parameters of the Uniswap v4 PYUSD/USDS Pool Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.11.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 7efb34f5-5007-4ab4-93e7-e00e616df5b3 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.11.1.2.1.1 - Network [Core]  <!-- UUID: 94de254f-7f5e-4e40-a683-26935e3503ed -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.11.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 61fb4454-3c58-4757-b796-cc9890685e71 -->

Uniswap v4

###### A.6.1.1.1.2.6.1.3.1.11.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 967a9605-4d90-46a7-a4bd-1ebcd7192b70 -->

USDS and PYUSD

###### A.6.1.1.1.2.6.1.3.1.11.1.2.1.4 - Token [Core]  <!-- UUID: 4d4123a0-312b-4351-aecc-28e56b1de290 -->

PYUSDUSDS

###### A.6.1.1.1.2.6.1.3.1.11.1.2.2 - Contract Addresses [Core]  <!-- UUID: fda1c342-7d97-4674-a383-d32544990ae9 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.11.1.2.2.1 - Token Address [Core]  <!-- UUID: df34137f-2994-48fb-ba1d-1c533b1fc305 -->

`0xa632d59b9b804a956bfaa9b48af3a1b74808fc1f`

###### A.6.1.1.1.2.6.1.3.1.11.1.2.2.2 - Pool ID [Core]  <!-- UUID: 1ec43acc-0aba-4e5e-96f9-cb6c4143c7f3 -->

`0xe63e32b2ae40601662f760d6bf5d771057324fbd97784fe1d3717069f7b75d45`

###### A.6.1.1.1.2.6.1.3.1.11.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 7b94ebfe-42c9-4319-80ff-d57258f5773c -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.11.1.2.4 - Rate Limits [Core]  <!-- UUID: 689f87d9-e66b-4eab-b984-9ad21ed4bb59 -->

The current `maxAmount,` `slope`, slippage, ticks, and fee for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.11.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 02ca893e-879e-47fa-a2f1-ca783ccf2106 -->

The inflow rate limits are:

- `maxAmount`: 10,000,000
- `slope`: 100,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 7b1bcd5c-8af6-46bd-8fb0-cbac22bae80a -->

The outflow rate limits are:

- `maxAmount`: 50,000,000
- `slope`: 200,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.1.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 1a2ba197-1389-4cdd-8e55-ca950ecacdca -->

The swap rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 50,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.1.2.4.4 - Maximum Slippage [Core]  <!-- UUID: 0318bf34-70a0-42a0-9019-e5a48de96ec6 -->

Max slippage: 0.1%

###### A.6.1.1.1.2.6.1.3.1.11.1.2.4.5 - Tick Range and Width [Core]  <!-- UUID: 9e8e50cc-eb69-43f4-b0d6-dd2f0c4fc01a -->

- Min lower tick limit: 276,314 (-0.1%)
- Max upper tick limit: 276,334 (+0.1%)
- Max tick width: 10 ticks

###### A.6.1.1.1.2.6.1.3.1.11.1.2.4.6 - Swap Fee [Core]  <!-- UUID: 3c776b0d-7ab4-4949-993e-ce290341654d -->

0.0005%

###### A.6.1.1.1.2.6.1.3.1.11.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 809b7844-1e15-4e43-bc33-b0af6074a725 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.11.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: c8bfb680-b56f-4cd2-835c-4fdec23be484 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.11.2 - Ethereum Mainnet - Uniswap v4 USDT/USDS Pool Instance Configuration Document [Core]  <!-- UUID: 3c4cfb29-1579-4abe-a17b-5b5574972b73 -->

The documents herein contain the Instance Configuration Document for the Uniswap v4 USDT/USDS Pool Instance.

###### A.6.1.1.1.2.6.1.3.1.11.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 686428f2-87e7-4592-8656-60ab5bee3168 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.11.2.2 - Parameters [Core]  <!-- UUID: d46584b0-4ec1-4450-b915-79969d7c3c74 -->

The documents herein define the parameters of the Uniswap v4 USDT/USDS Pool Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.11.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 0845627e-c64a-4e04-8be2-4f5bac7114d2 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.11.2.2.1.1 - Network [Core]  <!-- UUID: 6d1a7aa5-3aab-461b-a0ab-aa68137ffd0d -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.11.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 1fdf2ecf-e70e-4294-91de-1596f991ca2a -->

Uniswap v4

###### A.6.1.1.1.2.6.1.3.1.11.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 13b49366-aaee-4f35-b2cd-e2317bc4b92c -->

USDS and USDT

###### A.6.1.1.1.2.6.1.3.1.11.2.2.1.4 - Token [Core]  <!-- UUID: a877ea22-2aae-451e-b0d6-912fdaca1796 -->

USDTUSDS

###### A.6.1.1.1.2.6.1.3.1.11.2.2.2 - Contract Addresses [Core]  <!-- UUID: 164e3bb8-8a61-41b7-9d34-797db864ac87 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.11.2.2.2.1 - Token Address [Core]  <!-- UUID: c864e1c5-a653-433b-85e5-3bd1037fc7a1 -->

`0x00836Fe54625BE242BcFA286207795405ca4fD10`

###### A.6.1.1.1.2.6.1.3.1.11.2.2.2.2 - Pool ID [Core]  <!-- UUID: 6e231bfb-e04f-44e0-9023-7ab98c9b7568 -->

`0x3b1b1f2e775a6db1664f8e7d59ad568605ea2406312c11aef03146c0cf89d5b9`

###### A.6.1.1.1.2.6.1.3.1.11.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 77850de8-afe7-47e2-aedd-e44de6922c6f -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.11.2.2.4 - Rate Limits [Core]  <!-- UUID: 91ad3746-e58c-43b3-a53d-0430b5e20a4c -->

The current `maxAmount,` `slope`, slippage, ticks, and fee for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.11.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: a6105d1a-16d8-4920-808c-780891e2112d -->

The inflow rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 50,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 2a7d1855-feb9-4a16-b726-144f52c89dd3 -->

The outflow rate limits are:

- `maxAmount`: 50,000,000
- `slope`: 200,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.2.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 18355afe-c656-47a5-8867-206263d8cb09 -->

The swap rate limits are:

- `maxAmount`: 25,000,000
- `slope`: 250,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.2.2.4.4 - Maximum Slippage [Core]  <!-- UUID: fa48928b-af8a-4455-88ac-43a68631e329 -->

Max slippage: 0.2%

###### A.6.1.1.1.2.6.1.3.1.11.2.2.4.5 - Tick Range and Width [Core]  <!-- UUID: e72be948-a47e-4303-b9b2-d1acb07cecd4 -->

- Min lower tick limit: 276,304 (-0.2%)
- Max upper tick limit: 276,344 (+0.2%)
- Max tick width: 10 ticks

###### A.6.1.1.1.2.6.1.3.1.11.2.2.4.6 - Swap Fee [Core]  <!-- UUID: 9f92e7b7-83e6-4b0c-9f3d-6ec66a259c98 -->

0.0005%

###### A.6.1.1.1.2.6.1.3.1.11.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: bc14c22c-f7a7-4de9-afe9-4b121d05ee7a -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.11.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: afd2544b-24de-439b-8d8f-44d5cd82a8bd -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.11.3 - Ethereum Mainnet - Uniswap v4 USDG/USDS Pool Instance Configuration Document [Core]  <!-- UUID: 8c92f153-c1bc-4c6a-afb3-97769f839a71 -->

The documents herein contain the Instance Configuration Document for the Uniswap v4 USDG/USDS Pool Instance.

###### A.6.1.1.1.2.6.1.3.1.11.3.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 67bfc5a6-1fc5-4fa5-9f8c-a6509aad3470 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.11.3.2 - Parameters [Core]  <!-- UUID: 07d562e8-9e1a-41d8-9229-02b4e5a448e1 -->

The documents herein define the parameters of the Uniswap v4 USDG/USDS Pool Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.11.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 9af638aa-20a6-4476-b445-ef5b5d08bbd3 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.11.3.2.1.1 - Network [Core]  <!-- UUID: c3041fec-8f96-4206-8324-44a61f241812 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.11.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 2ded93bf-aee1-47df-9794-ab590b0327ad -->

Uniswap v4

###### A.6.1.1.1.2.6.1.3.1.11.3.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 97f7c2f4-856e-4514-a0ce-9e472fdb54c9 -->

USDS and USDG

###### A.6.1.1.1.2.6.1.3.1.11.3.2.1.4 - Token [Core]  <!-- UUID: 8dc76e4f-cdf9-4d05-ba7d-de9b5e45eb08 -->

USDGUSDS

###### A.6.1.1.1.2.6.1.3.1.11.3.2.2 - Contract Addresses [Core]  <!-- UUID: 1165703a-4bd0-4eee-aae9-a5859c4b6706 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.11.3.2.2.1 - Pool ID [Core]  <!-- UUID: 1a03015e-99ee-4fce-a123-a0dad38877d7 -->

`0x28adc7179a8a83c3379955d59563c0fec33eadfa83946b447af289190ff5fcff`

###### A.6.1.1.1.2.6.1.3.1.11.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: 06755c72-aef3-458d-a76b-b96c964e3f85 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.11.3.2.4 - Rate Limits [Core]  <!-- UUID: 415920c5-b4d8-476f-b550-62ebfd4d821c -->

The current `maxAmount,` `slope`, slippage, ticks, and fee for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.11.3.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: e4247d3b-7534-41b4-9144-0b0f4df0b53a -->

The inflow rate limits are:

- `maxAmount`: 10,000,000
- `slope`: 100,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.3.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: fedd5aff-5da6-4fbc-a117-c742d8706971 -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.11.3.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 794cfe55-5989-42c3-8656-8ec5c2f0d280 -->

The swap rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 200,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.3.2.4.4 - Maximum Slippage [Core]  <!-- UUID: 24e2eff9-42f8-4c46-b1e8-e05e16556ea0 -->

Max slippage: 0.1%

###### A.6.1.1.1.2.6.1.3.1.11.3.2.4.5 - Tick Range and Width [Core]  <!-- UUID: e6a7bb80-e477-4d6a-bc94-7d55058305d7 -->

- Min lower tick limit: -276,334 (-0.1%)
- Max upper tick limit: -276,314 (+0.1%)

###### A.6.1.1.1.2.6.1.3.1.11.3.2.4.6 - Swap Fee [Core]  <!-- UUID: 2caf9fd4-e135-4135-88d3-52e96def487b -->

0.0005%

###### A.6.1.1.1.2.6.1.3.1.11.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 84fdf5d4-d5f9-4728-ba6a-e45c970f2da3 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.11.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 04ffe8ae-940c-4439-86b1-9b73a9042035 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.11.4 - Ethereum Mainnet - Uniswap v4 rlUSD/USDS Pool Instance Configuration Document [Core]  <!-- UUID: 102ef022-a660-4942-8bf2-bb061a7a8f8a -->

The documents herein contain the Instance Configuration Document for the Uniswap v4 rlUSD/USDS Pool Instance.

###### A.6.1.1.1.2.6.1.3.1.11.4.1 - RRC Framework Full Implementation [Core]  <!-- UUID: a0b35835-4018-4fff-97e6-6f25a1879c48 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.11.4.2 - Parameters [Core]  <!-- UUID: 92466f64-08ea-44bf-b319-6f43e8bd7021 -->

The documents herein define the parameters of the Uniswap v4 rlUSD/USDS Pool Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.11.4.2.1 - Instance Identifiers [Core]  <!-- UUID: 8c320d89-ffd5-4a4b-817d-33f871cc62ff -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.11.4.2.1.1 - Network [Core]  <!-- UUID: 66a8ab26-7e7c-461d-aa2d-7580cec5fc94 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.11.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 302c0d80-4636-4188-ae78-b554abf42851 -->

Uniswap v4

###### A.6.1.1.1.2.6.1.3.1.11.4.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 41220e27-c21c-4826-b342-77022775926a -->

USDS and rlUSD

###### A.6.1.1.1.2.6.1.3.1.11.4.2.1.4 - Token [Core]  <!-- UUID: 5e723718-ac24-4c68-bb95-111dccea5693 -->

rlUSDUSDS

###### A.6.1.1.1.2.6.1.3.1.11.4.2.2 - Contract Addresses [Core]  <!-- UUID: 68d566b7-52b2-40c5-98db-2df6a7dc85b2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.11.4.2.2.1 - Pool ID [Core]  <!-- UUID: 9488fd1d-dc31-4c27-8c00-8711d403511d -->

`0x9035721b23481db3888fd201b9c2b26dbc3af60258bca65e669f2ed98dc8eb4f`

###### A.6.1.1.1.2.6.1.3.1.11.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: a469565c-8521-4e00-822c-9539530fa320 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.11.4.2.4 - Rate Limits [Core]  <!-- UUID: 448c87f5-4bc3-41c5-995d-353717d0fbd3 -->

The current `maxAmount,` `slope`, slippage, ticks, and fee for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.11.4.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 5d1628f1-7b31-4ae7-9aa9-8ee7c2ae8114 -->

The inflow rate limits are:

- `maxAmount`: 10,000,000
- `slope`: 50,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.4.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 4ae75785-5950-4483-a943-aa921e8a4cc0 -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.1.11.4.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: a339eb67-4bea-4fcb-aeca-6fcaba0d7ebb -->

The swap rate limits are:

- `maxAmount`: 5,000,000
- `slope`: 100,000,000 per day

###### A.6.1.1.1.2.6.1.3.1.11.4.2.4.4 - Maximum Slippage [Core]  <!-- UUID: a3c6f486-cfb5-4ba4-b671-cdf75b0bbeee -->

Max slippage: 0.1%

###### A.6.1.1.1.2.6.1.3.1.11.4.2.4.5 - Tick Range and Width [Core]  <!-- UUID: 6d4c2995-12a5-41db-a730-fb798ad75897 -->

- Min lower tick limit: -10 (-0.1%)
- Max upper tick limit: 10 (+0.1%)

###### A.6.1.1.1.2.6.1.3.1.11.4.2.4.6 - Swap Fee [Core]  <!-- UUID: cfacb9b5-e2e2-4a4e-8be9-b68ec7ce4dfa -->

0.0005%

###### A.6.1.1.1.2.6.1.3.1.11.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 4f4c6eaf-e4da-4fea-9086-4d714fffeaed -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.11.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 1fdc549c-eefb-4dd7-bb44-cb79612605e2 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.12 - Paxos [Core]  <!-- UUID: e01f0c20-5d3d-4ca4-ac9e-0a1e51780b19 -->

The Ethereum Mainnet Instances of the Paxos Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.12.1 - Ethereum Mainnet - USDC To PYUSD Via Paxos Instance Configuration Document [Core]  <!-- UUID: efc57615-b3ac-4122-8fd3-6a8d68ce71a1 -->

The documents herein contain the Instance Configuration Document for the USDC To PYUSD Via Paxos Instance.

###### A.6.1.1.1.2.6.1.3.1.12.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: c9d05c8a-7e78-45f6-8422-64793b739434 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.12.1.2 - Parameters [Core]  <!-- UUID: 99c9d288-1fd2-4608-b38e-085d40c12ce1 -->

The documents herein define the parameters of the USDC To PYUSD Via Paxos Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.12.1.2.1 - Instance Identifiers [Core]  <!-- UUID: f8220beb-0c4c-420f-b7d5-9dc7f86ca84b -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.12.1.2.1.1 - Network [Core]  <!-- UUID: b4acd29e-a541-4cd4-9df0-520ea85633ad -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.12.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 32c4f476-cbe3-4871-a63b-5501a17e3a0d -->

Paxos

###### A.6.1.1.1.2.6.1.3.1.12.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 9fe5aafe-b11c-4d00-9e4c-87d7a1903beb -->

USDC

###### A.6.1.1.1.2.6.1.3.1.12.1.2.1.4 - Token to Receive [Core]  <!-- UUID: eb7e08a0-9fc6-48f8-97c4-eeace222f34c -->

PYUSD

###### A.6.1.1.1.2.6.1.3.1.12.1.2.2 - Contract Addresses [Core]  <!-- UUID: 48ec53db-6ca2-4cdb-90bd-3860116bc551 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.12.1.2.2.1 - Token Address [Core]  <!-- UUID: 78ba019c-013f-4352-8208-a273d15fa1e2 -->

`0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`

###### A.6.1.1.1.2.6.1.3.1.12.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 78c62b61-6ccc-42d0-9232-6e66c8d8a26f -->

`0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`

###### A.6.1.1.1.2.6.1.3.1.12.1.2.2.3 - Paxos Deposit Address [Core]  <!-- UUID: c631c210-451e-4149-b375-c9e5105df0d5 -->

`0xFb1F749024b4544c425f5CAf6641959da31EdF37`

###### A.6.1.1.1.2.6.1.3.1.12.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 3b67cada-07bb-4e5c-b0ab-84ddbe515d19 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.12.1.2.4 - Rate Limits [Core]  <!-- UUID: bd104480-24d4-4fb1-a8f0-13e5c04a2c18 -->

The current TransferAsset rate limits for this conduit's transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.12.1.2.4.1 - TransferAssets Rate Limits [Core]  <!-- UUID: 66f2a388-119c-4908-9ff7-f38190e9566d -->

The transferAssets rate limits are:

- `maxAmount`: 5,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.12.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 51453e8e-19c2-45e1-95e3-88ce99e9c80f -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.12.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 9acd91e4-2705-42d9-a72a-b6e3cd0f6855 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.12.2 - Ethereum Mainnet - PYUSD To USDC Via Paxos Instance Configuration Document [Core]  <!-- UUID: 28544284-0ee1-49da-a27f-b13dba9b5842 -->

The documents herein contain the Instance Configuration Document for the PYUSD To USDC Via Paxos Instance.

###### A.6.1.1.1.2.6.1.3.1.12.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 253039f6-e11e-4356-9ee2-bcc87603e23c -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.12.2.2 - Parameters [Core]  <!-- UUID: e156bb45-006d-4341-b9a0-d8dd39be06fd -->

The documents herein define the parameters of the PYUSD To USDC Via Paxos Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.12.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 435d5c6e-32ed-43ea-8419-9d20cf998aed -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.12.2.2.1.1 - Network [Core]  <!-- UUID: 1b33f32e-7133-478c-a053-bb3aa3d4ec91 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.12.2.2.1.2 - Target Protocol [Core]  <!-- UUID: f07a80ae-654b-484e-8ccf-d2abd235a1a5 -->

Paxos

###### A.6.1.1.1.2.6.1.3.1.12.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 06daf347-26de-45c6-844b-9894c09d16cc -->

PYUSD

###### A.6.1.1.1.2.6.1.3.1.12.2.2.1.4 - Token to Receive [Core]  <!-- UUID: 933af4c1-32da-4b82-a1db-138e838b3377 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.12.2.2.2 - Contract Addresses [Core]  <!-- UUID: 7cfef7de-2859-48fb-9436-46017ecefc9a -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.12.2.2.2.1 - Token Address [Core]  <!-- UUID: c95f4d5b-a056-40ef-bf18-c5753c6f7182 -->

`0x6c3ea9036406852006290770bedfcaba0e23a0e8`

###### A.6.1.1.1.2.6.1.3.1.12.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 29802d42-1ddd-4c89-9e01-167abc1e5df7 -->

`0x6c3ea9036406852006290770bedfcaba0e23a0e8`

###### A.6.1.1.1.2.6.1.3.1.12.2.2.2.3 - Paxos Deposit Address [Core]  <!-- UUID: 4377a68b-2bc0-4c7b-96e6-e7d5c6527bd9 -->

`0x2f7BE67e11A4D621E36f1A8371b0a5Fe16dE6B20`

###### A.6.1.1.1.2.6.1.3.1.12.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: cd38213e-84bf-4a72-8f14-9c803c721e19 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.12.2.2.4 - Rate Limits [Core]  <!-- UUID: ad179de7-3167-476d-ae82-36fb715ec68f -->

The current TransferAsset rate limits for this conduit's transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.12.2.2.4.1 - TransferAssets Rate Limits [Core]  <!-- UUID: 1f64320b-feca-4059-95d3-f73950382031 -->

The transferAssets rate limits are:

- `maxAmount`: 5,000,000 PYUSD
- `slope`: 200,000,000 PYUSD per day

###### A.6.1.1.1.2.6.1.3.1.12.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 880763c4-9474-41e4-bd59-2afb8796ab8b -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.12.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: ae19bb92-fec6-4939-83ed-43154b8db004 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.12.3 - Ethereum Mainnet - PYUSD To USDG Via Paxos Instance Configuration Document [Core]  <!-- UUID: f6b739d1-c637-48f8-abf7-8c8f173bb392 -->

The documents herein contain the Instance Configuration Document for the PYUSD To USDG Via Paxos Instance.

###### A.6.1.1.1.2.6.1.3.1.12.3.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 4010a8e3-6ef1-4ad1-ad18-46c8e6de8e6a -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.12.3.2 - Parameters [Core]  <!-- UUID: d60d90db-4847-4c3a-b0c1-337cb0364350 -->

The documents herein define the parameters of the PYUSD To USDG Via Paxos Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.12.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 539c956e-f77b-48cc-9ebf-e875178bf97a -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.12.3.2.1.1 - Network [Core]  <!-- UUID: 9ba2f854-f17a-4f66-8bd6-75da9633b032 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.12.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 94488493-0093-4f6d-979a-45194be5465c -->

Paxos

###### A.6.1.1.1.2.6.1.3.1.12.3.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: f4d4b3b4-e720-4047-8b52-e08dd377ece0 -->

PYUSD

###### A.6.1.1.1.2.6.1.3.1.12.3.2.1.4 - Token to Receive [Core]  <!-- UUID: bd9ef5f1-01ec-476e-82f0-00790a80c63b -->

USDG

###### A.6.1.1.1.2.6.1.3.1.12.3.2.2 - Contract Addresses [Core]  <!-- UUID: 7faea6c2-408d-42c4-8be0-bdd712211562 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.12.3.2.2.1 - Token Address [Core]  <!-- UUID: 51c7e0ae-a2b2-4e0b-a9bf-6b7c6acb58e3 -->

`0x6c3ea9036406852006290770bedfcaba0e23a0e8`

###### A.6.1.1.1.2.6.1.3.1.12.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 9951f14e-9d5e-489a-8479-de33afd6c1c4 -->

`0x6c3ea9036406852006290770bedfcaba0e23a0e8`

###### A.6.1.1.1.2.6.1.3.1.12.3.2.2.3 - Paxos Deposit Address [Core]  <!-- UUID: d30c73f2-c1dc-4ae1-91a0-f8f1061d80d1 -->

`0x227B1912C2fFE1353EA3A603F1C05F030Cc262Ff`

###### A.6.1.1.1.2.6.1.3.1.12.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: c0f6ad05-ec97-4464-9627-82b14035bc17 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.12.3.2.4 - Rate Limits [Core]  <!-- UUID: 0d22ec04-8742-49d5-a285-3668ce6d4947 -->

The current TransferAsset rate limits for this conduit's transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.12.3.2.4.1 - TransferAssets Rate Limits [Core]  <!-- UUID: eb39ef45-405a-46d5-acac-c0ecc47b7ea2 -->

The transferAssets rate limits are:

- `maxAmount`: 5,000,000 PYUSD
- `slope`: 50,000,000 PYUSD per day

###### A.6.1.1.1.2.6.1.3.1.12.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 58faa1d1-96fb-44cd-8902-81a48cf7d2a8 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.12.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: f9be22e8-f6dd-4b99-9821-17cc1f251be9 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.12.4 - Ethereum Mainnet - USDG To PYUSD Via Paxos Instance Configuration Document [Core]  <!-- UUID: bef47e5b-5568-4df4-9294-2eb108a006c6 -->

The documents herein contain the Instance Configuration Document for the USDG To PYUSD Via Paxos Instance.

###### A.6.1.1.1.2.6.1.3.1.12.4.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 1154efd4-1d7f-4cf2-8d6a-09bdde842827 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.12.4.2 - Parameters [Core]  <!-- UUID: bc5c8128-8fbf-428c-a90a-34afb7cf2107 -->

The documents herein define the parameters of the USDG To PYUSD Via Paxos Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.12.4.2.1 - Instance Identifiers [Core]  <!-- UUID: 5268a2a0-1dc1-442c-a3ee-64eb6c91fdbb -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.12.4.2.1.1 - Network [Core]  <!-- UUID: 0df49dfc-3125-4b9c-8b5e-95d8036cb1f7 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.12.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 47d5f804-35a8-4016-b816-1066c75c1914 -->

Paxos

###### A.6.1.1.1.2.6.1.3.1.12.4.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 61bc115a-5433-44d3-b86b-e5991fe2f077 -->

USDG

###### A.6.1.1.1.2.6.1.3.1.12.4.2.1.4 - Token to Receive [Core]  <!-- UUID: 4aa26757-47fd-4cc3-845e-d0d1b8487182 -->

PYUSD

###### A.6.1.1.1.2.6.1.3.1.12.4.2.2 - Contract Addresses [Core]  <!-- UUID: f16deb9b-1cba-4178-9fea-b228862c9cc4 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.12.4.2.2.1 - Token Address [Core]  <!-- UUID: b3f52d1f-e089-4f99-b597-71e310cee76f -->

`0xe343167631d89B6Ffc58B88d6b7fB0228795491D`

###### A.6.1.1.1.2.6.1.3.1.12.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: cb6e5759-1db7-4287-afec-612348ee545b -->

`0xe343167631d89B6Ffc58B88d6b7fB0228795491D`

###### A.6.1.1.1.2.6.1.3.1.12.4.2.2.3 - Paxos Deposit Address [Core]  <!-- UUID: 61d68d4e-dc31-4f29-9d69-7d2839b79b59 -->

`0x035b322D0e79de7c8733CdDA5a7EF8b51a6cfcfa`

###### A.6.1.1.1.2.6.1.3.1.12.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: 18f1f756-3755-4875-8c2f-a93be31bb8fa -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.12.4.2.4 - Rate Limits [Core]  <!-- UUID: ffbfbbf7-8de6-47b8-aa8d-052e8273f33e -->

The current TransferAsset rate limits for this conduit's transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.12.4.2.4.1 - TransferAssets Rate Limits [Core]  <!-- UUID: 22e01de3-379b-4724-9ff6-136937c002d2 -->

The transferAssets rate limits are:

- `maxAmount`: 5,000,000 USDG
- `slope`: 100,000,000 USDG per day

###### A.6.1.1.1.2.6.1.3.1.12.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: c8887b5e-fb8f-4364-bc4d-715a5393fbb3 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.12.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 56e556cc-0401-4cbd-9bda-8fea5d921f6d -->

###### A.6.1.1.1.2.6.1.3.1.13 - Anchorage [Core]  <!-- UUID: 1565129f-7249-4f5b-babb-7f81d33eff13 -->

The Ethereum Mainnet Instances of the Anchorage Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.13.1 - Ethereum Mainnet - Anchorage USAT Instance Configuration Document [Core]  <!-- UUID: 8048e396-7bb4-4541-a68f-6dd7ec0a6015 -->

The documents herein contain the Instance Configuration Document for the Anchorage USAT Instance.

###### A.6.1.1.1.2.6.1.3.1.13.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: eff5d00f-b831-417f-8cb9-a9edfaccbbcd -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.13.1.2 - Parameters [Core]  <!-- UUID: 78067cd5-bd11-47eb-bdf7-947038912cfa -->

The documents herein define the parameters of the Anchorage USAT Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.13.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 65214651-962d-442b-99f1-dd1157a77c86 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.13.1.2.1.1 - Network [Core]  <!-- UUID: 83f14764-63d8-4908-ac4e-ac7a46f37cac -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.13.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 882a4a15-b9e8-4ebe-b800-410cddc87ab1 -->

Anchorage

###### A.6.1.1.1.2.6.1.3.1.13.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: db820c09-0b14-45ea-8367-d7a301718fb9 -->

USAT

###### A.6.1.1.1.2.6.1.3.1.13.1.2.1.4 - Token [Core]  <!-- UUID: ac45e6ad-5076-4fed-8805-d48593e41778 -->

USAT

###### A.6.1.1.1.2.6.1.3.1.13.1.2.2 - Contract Addresses [Core]  <!-- UUID: b9b80a90-766b-424b-b56d-334cacee4dd2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.13.1.2.2.1 - Token Address [Core]  <!-- UUID: cca5bcb2-eb4a-429a-b10c-a55c7c6bb683 -->

`0x07041776f5007aca2a54844f50503a18a72a8b68`

###### A.6.1.1.1.2.6.1.3.1.13.1.2.2.2 - Destination Address [Core]  <!-- UUID: 5396d5c2-6f79-4ab2-8978-61dc6209a00c -->

`0x49506C3Aa028693458d6eE816b2EC28522946872`

###### A.6.1.1.1.2.6.1.3.1.13.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: a7508ca1-0132-4a94-9efd-2288a30c3220 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.13.1.2.4 - Rate Limits [Core]  <!-- UUID: 132f9c53-0f2d-4e0a-9adb-649eadf9d95f -->

The current `maxAmount` and `slope` for this conduit’s transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.13.1.2.4.1 - transferAsset Rate Limits [Core]  <!-- UUID: 4093b98b-2421-4642-982b-8c08b2f5ef20 -->

- `maxAmount`: 50,000,000 USAT
- `slope`: 250,000,000 USAT per day

###### A.6.1.1.1.2.6.1.3.1.13.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 069aa415-4d37-4567-b7da-bda62e4d0423 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.13.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 98759dcc-8bb4-459a-b020-d46a02b038ec -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.13.2 - Ethereum Mainnet - Anchorage USDT Instance Configuration Document [Core]  <!-- UUID: 4eee15e5-46e2-4438-8299-6c85c46bb85b -->

The documents herein contain the Instance Configuration Document for the Anchorage USDT Instance.

###### A.6.1.1.1.2.6.1.3.1.13.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 54ce1edc-9556-4103-bb4d-0b45efcdbb43 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.13.2.2 - Parameters [Core]  <!-- UUID: 7b07774c-4cda-4866-bc4e-7e469a685f5e -->

The documents herein define the parameters of the Anchorage USDT Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.13.2.2.1 - Instance Identifiers [Core]  <!-- UUID: afa6a7e4-fbeb-4138-9220-91c023203ce5 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.13.2.2.1.1 - Network [Core]  <!-- UUID: e0febf90-ab83-4b7f-9bea-dc037c1b96c0 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.13.2.2.1.2 - Target Protocol [Core]  <!-- UUID: b8aed139-8a1a-467f-acf4-877d42516e87 -->

Anchorage

###### A.6.1.1.1.2.6.1.3.1.13.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: f993b46b-291c-45a1-a369-27c37e7bfddd -->

USDT

###### A.6.1.1.1.2.6.1.3.1.13.2.2.1.4 - Token [Core]  <!-- UUID: 00f2dded-9e35-4af8-9ac4-c706737540ac -->

USDT

###### A.6.1.1.1.2.6.1.3.1.13.2.2.2 - Contract Addresses [Core]  <!-- UUID: 30bc6650-5589-443b-ae3a-1b86d463e05b -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.13.2.2.2.1 - Token Address [Core]  <!-- UUID: c9ef9947-ee35-416c-bb6d-30d1fea15d3f -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.13.2.2.2.2 - Destination Address [Core]  <!-- UUID: f5b05cdd-1aef-4b02-beda-99a2e3a69015 -->

`0x49506C3Aa028693458d6eE816b2EC28522946872`

###### A.6.1.1.1.2.6.1.3.1.13.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 435ca83e-fbd7-4ace-866d-8ffc9388118c -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.13.2.2.4 - Rate Limits [Core]  <!-- UUID: b494026e-d3bc-4122-bac3-98ea1d7436b0 -->

The current `maxAmount` and `slope` for this conduit’s transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.13.2.2.4.1 - transferAsset Rate Limits [Core]  <!-- UUID: 5a56203b-5c1b-42e8-9acb-8ab78eb4dc06 -->

- `maxAmount`: 50,000,000 USDT
- `slope`: 250,000,000 USDT per day

###### A.6.1.1.1.2.6.1.3.1.13.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 1ec11acd-b8fe-4310-b1ba-6e57c9c27fd3 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.13.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 1c69d51a-f202-4e17-99cd-dd29a046e2a5 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.13.3 - Ethereum Mainnet - Anchorage USDC Instance Configuration Document [Core]  <!-- UUID: efa4ea69-60de-4499-8ef0-86551373fa34 -->

The documents herein contain the Instance Configuration Document for the Anchorage USDC Instance.

###### A.6.1.1.1.2.6.1.3.1.13.3.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 7cdbb389-360d-417d-bdc4-f142d7eb9dd7 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.13.3.2 - Parameters [Core]  <!-- UUID: 70521c48-b900-4f25-bf9a-dc3a7804bafe -->

The documents herein define the parameters of the Anchorage USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.13.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 1bd43af8-3739-4ce2-ac3a-65b10194ae80 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.13.3.2.1.1 - Network [Core]  <!-- UUID: b6feeb2a-fdd2-4c1d-8899-b8ca219b9c01 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.13.3.2.1.2 - Target Protocol [Core]  <!-- UUID: ccbc9e4a-a9c9-4d7d-a4be-b48ec63ca05a -->

Anchorage

###### A.6.1.1.1.2.6.1.3.1.13.3.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: fd33f615-8c47-44f4-9403-a7611f09dd59 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.13.3.2.1.4 - Token [Core]  <!-- UUID: b501fbcd-f2de-411a-858f-c57fdccb7509 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.13.3.2.2 - Contract Addresses [Core]  <!-- UUID: a9d85159-7e84-4551-a60a-44ba56f2d9e2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.13.3.2.2.1 - Token Address [Core]  <!-- UUID: a04dc56a-2dbe-4e0f-8825-c35f2728823a -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.13.3.2.2.2 - Destination Address [Core]  <!-- UUID: a90ea568-70ea-4413-bf34-158f2644f8b8 -->

`0x49506C3Aa028693458d6eE816b2EC28522946872`

###### A.6.1.1.1.2.6.1.3.1.13.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: 501f003f-6082-4d87-9155-9569d1a12d69 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.13.3.2.4 - Rate Limits [Core]  <!-- UUID: 88ae938c-2370-4a27-b6de-609fc3dd6808 -->

The current `maxAmount` and `slope` for this conduit’s transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.13.3.2.4.1 - transferAsset Rate Limits [Core]  <!-- UUID: 9d3f2437-5dcd-4a38-8507-a2def33c7756 -->

- `maxAmount`: 50,000,000 USDC
- `slope`: 250,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.13.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 54e82f98-4059-4364-b0a4-08f34cc3a716 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.13.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: d0245971-a244-41a9-9033-5d2c93e4f632 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.14 - Binance [Core]  <!-- UUID: be4602ea-5289-4bc9-9f93-0ddd172e814a -->

The Ethereum Mainnet Instances of Binance with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.1.14.1 - Ethereum Mainnet - Transfer USDC to Binance (receive USDT) Instance Configuration Document [Core]  <!-- UUID: ea00f585-11f4-4984-879e-22a6a0689a67 -->

The documents herein contain the Instance Configuration Document for the Transfer USDC to Binance (receive USDT) Instance.

###### A.6.1.1.1.2.6.1.3.1.14.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: ea758765-790e-4617-ae20-19938264fbae -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.14.1.2 - Parameters [Core]  <!-- UUID: 331a1641-9427-4cb8-b19b-8ca24d60aa7e -->

The documents herein define the parameters of the Transfer USDC to Binance (receive USDT) of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.14.1.2.1 - Instance Identifiers [Core]  <!-- UUID: f37802a1-2650-4665-a132-0d39b2dbd819 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.14.1.2.1.1 - Network [Core]  <!-- UUID: 68cf23b2-4e15-47b5-8e72-2440ce9fe2ac -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.14.1.2.1.2 - Target Protocol [Core]  <!-- UUID: ac44296b-332c-4287-a5c0-71cd43f5d355 -->

Binance

###### A.6.1.1.1.2.6.1.3.1.14.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 50cc20da-6c4e-48a3-8162-a9aed32118fd -->

USDC

###### A.6.1.1.1.2.6.1.3.1.14.1.2.1.4 - Token to Receive [Core]  <!-- UUID: d4f85ab9-1d10-4034-b450-6379ef502342 -->

USDT

###### A.6.1.1.1.2.6.1.3.1.14.1.2.2 - Contract Addresses [Core]  <!-- UUID: e86c98bc-5cee-400f-8992-0a98a741a218 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.14.1.2.2.1 - Token Address [Core]  <!-- UUID: 5f45db3f-1837-46ec-9206-119345438721 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.14.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 6f6e6011-2ea9-42c3-8a91-61ee468b3070 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.3.1.14.1.2.2.3 - Binance Deposit Address [Core]  <!-- UUID: ec3d3c63-f0ac-4d85-a05b-4af82744340d -->

TBD

###### A.6.1.1.1.2.6.1.3.1.14.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 1b4e3734-5a4d-4205-a217-9a1a54fe4c57 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.14.1.2.4 - Rate Limits [Core]  <!-- UUID: c8cd2bb5-cd8c-43f3-af6f-e1458e12164b -->

The current TransferAsset rate limits for this conduit's transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.14.1.2.4.1 - TransferAssets Rate Limits [Core]  <!-- UUID: 7792d17d-6660-4b16-b85e-a9cea4b6edda -->

The transferAssets rate limits are:

- `maxAmount`: 5,000,000 USDC
- `slope`: 100,000,000 USDC per day
- `maxSlippage`: 0.2%
- `rechargeRate`: 50,000 USDC per day

###### A.6.1.1.1.2.6.1.3.1.14.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 7f1605a9-6421-4a8f-aed7-a2eab870d0a8 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.14.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 7080c0eb-1508-4534-9649-c8927dcd597e -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.1.14.2 - Ethereum Mainnet - Transfer USDT to Binance (receive USDC) Instance Configuration Document [Core]  <!-- UUID: 47a2b1c2-104c-4bb4-bb10-574cab86daf5 -->

The documents herein contain the Instance Configuration Document for the Transfer USDT to Binance (receive USDC) Instance.

###### A.6.1.1.1.2.6.1.3.1.14.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: af93001f-8368-4a09-a30c-32207f74208e -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.1.14.2.2 - Parameters [Core]  <!-- UUID: b6d7baee-c09a-47f1-aa73-a384b16caf6c -->

The documents herein define the parameters of the Transfer USDT to Binance (receive USDC) of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.1.14.2.2.1 - Instance Identifiers [Core]  <!-- UUID: ad247457-154b-4f10-ab18-4fdb8045849d -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.1.14.2.2.1.1 - Network [Core]  <!-- UUID: f775e16f-9608-4e03-bda7-b5fe427c3c88 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.3.1.14.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 0c5c931c-9c63-48b2-bd7b-7b87ec52ee60 -->

Binance

###### A.6.1.1.1.2.6.1.3.1.14.2.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 25695b01-071c-4055-8026-42fa168c4456 -->

USDT

###### A.6.1.1.1.2.6.1.3.1.14.2.2.1.4 - Token to Receive [Core]  <!-- UUID: 1fd6bf76-3293-488f-8ac8-1e7d76cebf01 -->

USDC

###### A.6.1.1.1.2.6.1.3.1.14.2.2.2 - Contract Addresses [Core]  <!-- UUID: 8b7ca367-710b-422f-900f-fd32e84dc802 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.1.14.2.2.2.1 - Token Address [Core]  <!-- UUID: abfb7450-ee85-43b1-8de6-59214ba865ef -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.14.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: b23aa2c6-87c2-42ec-9fb4-436fd1514570 -->

`0xdAC17F958D2ee523a2206206994597C13D831ec7`

###### A.6.1.1.1.2.6.1.3.1.14.2.2.2.3 - Binance Deposit Address [Core]  <!-- UUID: d22ee5e9-4601-4ff1-b0c0-b2641f871b2b -->

TBD

###### A.6.1.1.1.2.6.1.3.1.14.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: e66e804c-d81c-4157-b949-1045bb99ef7f -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.1.14.2.2.4 - Rate Limits [Core]  <!-- UUID: 0db8118c-50a2-442c-86ea-083b85df9688 -->

The current TransferAsset rate limits for this conduit's transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.1.14.2.2.4.1 - TransferAssets Rate Limits [Core]  <!-- UUID: ce06a6b4-faa7-4406-ba40-bc2821bc6b88 -->

The transferAssets rate limits are:

- `maxAmount`: 5,000,000 USDT
- `slope`: 100,000,000 USDT per day
- `maxSlippage`: 0.2%
- `rechargeRate`: 50,000 USDT per day

###### A.6.1.1.1.2.6.1.3.1.14.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 5b85cf5f-3c93-42c8-9733-00335214f4a3 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.1.14.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 54e39388-b13f-4b7b-8027-ec937f7f29a7 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.2 - Base [Core]  <!-- UUID: 9ddbfaed-ebb8-4dd4-9f08-d12cad450a00 -->

The Base Instances of the Spark Liquidity Layer with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.2.1 - Morpho [Core]  <!-- UUID: a5351a25-419c-437f-92c0-ff6f07c8677a -->

The Base Instances of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.2.1.1 - Base - Morpho Blue USDC ERC4626 Vault Instance Configuration Document [Core]  <!-- UUID: 97c54a67-ff3d-40c3-a702-f632f2b81f2d -->

The documents herein contain the Instance Configuration Document for the Morpho Blue USDC ERC4626 Vault Instance.

###### A.6.1.1.1.2.6.1.3.2.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 2bd39387-8ce1-4e3d-9c3b-5bbfb241f935 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.2.1.1.2 - Parameters [Core]  <!-- UUID: c0b80ed0-dda1-4efd-9899-d35ecf5b2ab4 -->

The documents herein define the parameters of the Morpho Blue USDC ERC4626 Vault Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.2.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 49ab64df-ac5c-4595-82dc-0e984a8c97d9 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.1.2.6.1.3.2.1.1.2.1.1 - Network [Core]  <!-- UUID: 421aae3a-2ade-4dd3-accb-829a92b8fdf5 -->

Base

###### A.6.1.1.1.2.6.1.3.2.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 8af68bad-a084-482d-bb17-746d2dc48a77 -->

Morpho Blue (ERC4626 Vault)

###### A.6.1.1.1.2.6.1.3.2.1.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: e40597fd-a25d-4865-a486-d1b6fd3141e7 -->

USDC

###### A.6.1.1.1.2.6.1.3.2.1.1.2.1.4 - Token [Core]  <!-- UUID: 6ed4c7e8-a0b2-4b61-aa55-9d5d43ba61b4 -->

sparkUSDC

###### A.6.1.1.1.2.6.1.3.2.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: b29004e1-3967-4f92-93e5-152d6f96bac7 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.2.1.1.2.2.1 - Token Address (ERC4626 Vault) [Core]  <!-- UUID: 89fc9a0a-0407-463e-8f45-2b2ca6e1d832 -->

`0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A`

###### A.6.1.1.1.2.6.1.3.2.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 2efab1a6-9c66-4b61-af68-2740efd8d475 -->

`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`

###### A.6.1.1.1.2.6.1.3.2.1.1.2.2.3 - Allocator Role Address [Core]  <!-- UUID: 64f057b6-40cc-4ef9-b1c5-36c7430b543f -->

`0xCBA0C0a2a0B6Bb11233ec4EA85C5bFfea33e724d`

###### A.6.1.1.1.2.6.1.3.2.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: c8ac360b-6c77-458f-a481-78b4554dd682 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.2.1.1.2.4 - Rate Limits [Core]  <!-- UUID: dbd9a2e2-74c7-47e5-abe4-d0940cb16f8e -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.2.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 97aa974e-5b7d-43fb-be88-947454d69a53 -->

The inflow rate limits are:

- `maxAmount`: 100,000,00 USDC
- `slope`: 50,000,00 USDC per day

###### A.6.1.1.1.2.6.1.3.2.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 63e50c95-64fd-4266-86c0-096681fa54e6 -->

The outflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.2.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 1249bc92-d66d-4ffc-bc42-a0184cbef5cb -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.2.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 9b849363-5380-406f-888a-d533f6ec69de -->

The Instance follows the general ERC4626 procedures see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2 - ERC-4626 Functions](e386a0df-9e0b-4ffd-9879-49131f795b0b) and for emergency procedures see [A.6.1.1.1.2.6.1.2.2.3.4.1 - ERC-4626 Withdrawal Action](f92ddc3f-672a-4f52-931f-5263a9f709b9). For detailed example of the Spark Liquidity Layer interaction logic for depositing to, withdrawing from, and redeeming from this ERC4626 vault instance see [A.6.1.1.1.2.6.1.3.1.5.1.3.1 - Deposit ERC-4626 Tokens](e2ad525b-3f3f-4402-9e4d-3ae125b35b76) and [A.6.1.1.1.2.6.1.3.1.5.1.3.2 - Withdraw ERC-4626 Tokens](caa295f4-92f4-4ca9-9083-2a1b94c70d5f).

###### A.6.1.1.1.2.6.1.3.2.1.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 71568640-f127-441d-bdbe-5761d685e505 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.2.1.1.4.1 - Market Exposure [Core]  <!-- UUID: ab15055e-99ff-4699-82f9-6f1b9a6b4f58 -->

The documents herein contains exposure details for this Instance

###### A.6.1.1.1.2.6.1.3.2.1.1.4.1.1 - ETH/USDC 86% LLTV Pool [Core]  <!-- UUID: f826bb79-9903-49f0-a421-ff3e5a6b4efb -->

- Pool ID: 0x8793cf302b8ffd655ab97bd1c695dbd967807e8367a65cb2f4edaf1380ba1bda
- Supply cap: 1,000,000,000

###### A.6.1.1.1.2.6.1.3.2.1.1.4.1.2 - cbETH/USDC 86% LLTV Pool [Core]  <!-- UUID: e9a7720b-27a4-4ec2-8c2c-ce46625369fd -->

- Pool ID: 0x1c21c59df9db44bf6f645d854ee710a8ca17b479451447e9f56758aee10a2fad
- Supply cap: 50,000,000

###### A.6.1.1.1.2.6.1.3.2.1.1.4.2 - Contract Addresses [Core]  <!-- UUID: 38936f4a-42da-4d27-a7ef-65ae9b104a7a -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.2.1.1.4.2.1 - Curator Role Address [Core]  <!-- UUID: 921d59d4-baaf-45a8-b6ff-93aa879e0e41 -->

`0x0f963A8A8c01042B69054e787E5763ABbB0646A3`

###### A.6.1.1.1.2.6.1.3.2.1.1.4.2.2 - Guardian Role Address [Core]  <!-- UUID: edee318a-59b1-4ff1-9790-8d4606f2f7bd -->

`0xf5748bBeFa17505b2F7222B23ae11584932C908B`

###### A.6.1.1.1.2.6.1.3.2.1.1.4.3 - Timelock [Core]  <!-- UUID: 63f24280-1724-4d2c-a0b8-aa8a2381afb8 -->

Timelock: 240 hours (10 days)

###### A.6.1.1.1.2.6.1.3.2.2 - Fluid [Core]  <!-- UUID: 6be8271c-9f42-4eef-a05e-96e73e5d18b4 -->

The Base Instances of the Fluid Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.2.2.1 - Base Mainnet - Fluid sUSDS ERC4626 Vault Instance Configuration Document [Core]  <!-- UUID: b955e881-1ad7-479f-9858-efebe8e23bdc -->

The documents herein contain the Instance Configuration Document for the Fluid sUSDS ERC4626 Instance.

###### A.6.1.1.1.2.6.1.3.2.2.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 79edb8fa-6801-43c0-9190-4dbb5e9865c8 -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.2.2.1.2 - Parameters [Core]  <!-- UUID: c090d021-d1a9-41c9-afcf-4edaa97150c0 -->

The documents herein define the parameters of the Fluid sUSDS ERC4626 Vault Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.2.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: f8aeef37-1251-4871-b5c7-5d1e80d8f15c -->

The documents herein define the Instance identifiers.

###### A.6.1.1.1.2.6.1.3.2.2.1.2.1.1 - Network [Core]  <!-- UUID: f09051d1-3526-49cc-b09d-576a3705f4f8 -->

Base

###### A.6.1.1.1.2.6.1.3.2.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 84fd28d3-1624-4a94-bff2-9c69cbaa2904 -->

Fluid Finance (ERC4626 Vault)

###### A.6.1.1.1.2.6.1.3.2.2.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: cb25347b-93dc-42cb-a691-1c130ec9c6a1 -->

sUSDS

###### A.6.1.1.1.2.6.1.3.2.2.1.2.1.4 - Token [Core]  <!-- UUID: d638194b-7668-4ccd-bef0-1110c38fe6a3 -->

fsUSDS

###### A.6.1.1.1.2.6.1.3.2.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: 18ae718a-6a68-41df-a5a0-b8f27d2b7665 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.2.2.1.2.2.1 - Token Address (ERC4626 Vault) [Core]  <!-- UUID: 5ce2cf40-bc6f-48fe-894b-aca0c6a8ecec -->

`0xf62e339f21d8018940f188F6987Bcdf02A849619`

###### A.6.1.1.1.2.6.1.3.2.2.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 8b66880c-e943-46b2-8411-a1c84dc0a5f6 -->

`0x5875eEE11Cf8398102FdAd704C9E96607675467a`

###### A.6.1.1.1.2.6.1.3.2.2.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 4a6342b9-8f9f-48ae-82a2-8c1293bb8004 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.2.2.1.2.4 - Rate Limits [Core]  <!-- UUID: 4f689c17-28f3-4217-984d-b71eb7b97b7a -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.2.2.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 29114e51-9590-4585-b494-b78417f35910 -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 5,000,000 USDS per day

###### A.6.1.1.1.2.6.1.3.2.2.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: f8a431bd-2d0b-4d60-886c-6e3dac42989e -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: 5,000,000 fsUSDS per day

###### A.6.1.1.1.2.6.1.3.2.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 00f6c298-eb05-4c7a-b83c-5bc80a283104 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.2.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 7c196eb9-92b0-4c43-bd8a-d78a8743a589 -->

The Instance follows the general ERC4626 procedures see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2 - ERC-4626 Functions](e386a0df-9e0b-4ffd-9879-49131f795b0b) and for emergency procedures see [A.6.1.1.1.2.6.1.2.2.3.4.1 - ERC-4626 Withdrawal Action](f92ddc3f-672a-4f52-931f-5263a9f709b9). For detailed example of the Spark Liquidity Layer interaction logic for depositing to, withdrawing from, and redeeming from this ERC4626 vault instance see [A.6.1.1.1.2.6.1.3.1.5.1.3.1 - Deposit ERC-4626 Tokens](e2ad525b-3f3f-4402-9e4d-3ae125b35b76) and [A.6.1.1.1.2.6.1.3.1.5.1.3.2 - Withdraw ERC-4626 Tokens](caa295f4-92f4-4ca9-9083-2a1b94c70d5f).

###### A.6.1.1.1.2.6.1.3.2.3 - Aave [Core]  <!-- UUID: a74ec7ed-eb8a-4144-ae32-fa90f751538c -->

The Base Instances of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.2.3.1 - Base - Aave USDC Instance Configuration Document [Core]  <!-- UUID: adfe1844-38ae-4eac-9060-f79978751765 -->

The documents herein contain the Instance Configuration Document for the Aave USDC Instance.

###### A.6.1.1.1.2.6.1.3.2.3.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 5339627f-27f5-4c01-8d99-0b0bb0866f33 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.2.3.1.2 - Parameters [Core]  <!-- UUID: 7b66655a-be93-49fa-b9d2-0ea76622930b -->

The documents herein define the parameters of the Aave USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.2.3.1.2.1 - Instance Identifiers [Core]  <!-- UUID: a2fae303-cde7-4e71-99ec-29fff49abb82 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.1.2.6.1.3.2.3.1.2.1.1 - Network [Core]  <!-- UUID: 25f23eac-7761-4b9e-9d10-19235d65d201 -->

Base

###### A.6.1.1.1.2.6.1.3.2.3.1.2.1.2 - Target Protocol [Core]  <!-- UUID: a33b4fb5-ee2b-49fc-bc99-4278f3ef281a -->

Aave

###### A.6.1.1.1.2.6.1.3.2.3.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 444562db-82e3-4e85-b1a0-eea3b5ed2162 -->

USDC

###### A.6.1.1.1.2.6.1.3.2.3.1.2.1.4 - Token [Core]  <!-- UUID: a066bf00-a88d-486d-b288-76dcf6e74c15 -->

aBasUSDC

###### A.6.1.1.1.2.6.1.3.2.3.1.2.2 - Contract Addresses [Core]  <!-- UUID: 4d455770-96aa-4ecd-93a0-00b54494ea9c -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.2.3.1.2.2.1 - Token Address [Core]  <!-- UUID: 92d1ebed-51c8-4877-898e-e21c0cc85e6d -->

`0x4e65fE4DbA92790696d040ac24Aa414708F5c0AB`

###### A.6.1.1.1.2.6.1.3.2.3.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: ce769e22-56cc-4ab1-91a7-ae8d12c2f9fd -->

`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`

###### A.6.1.1.1.2.6.1.3.2.3.1.2.2.3 - Pool [Core]  <!-- UUID: 510aabe8-5660-4b5d-b647-cd4ff022a620 -->

This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.2.3.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: bdb8e938-6930-4307-8d26-1e6e0e29f5d5 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.2.3.1.2.4 - Rate Limits [Core]  <!-- UUID: 9942de86-4cb3-4d55-a24c-7cf7cc42ea6d -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.2.3.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 3ef9417d-39af-46ba-b26d-4fbe11ef153b -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 25,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.2.3.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 89e0b1fb-f660-4cf2-8977-ccb872854ced -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.2.3.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 93b85c6b-8dff-420e-9f5a-c8c10390ef86 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.2.3.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: bac5a103-a0fa-4d3b-8cd0-b9dfe024d4a9 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes. For the general operational procedures applicable to all Aave-type instances. See [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3 - Aave Functions](9922dcf0-4562-445b-9a46-712f677cce64) and [A.6.1.1.1.2.6.1.2.2.3.2.3 - Aave AToken Withdrawal Action](2560adbb-4a5c-4c95-86cb-04647bb33836). For detailed example of the Spark Liquidity Layer interaction logic for depositing to and withdrawing from Aave see [A.6.1.1.1.2.6.1.3.1.2.1.3.1 - Process Definition For Depositing](fa2520ac-4779-4aeb-abe4-2c1b89e7ca51) and [A.6.1.1.1.2.6.1.3.1.2.1.3.2 - Process Definition For Withdrawing](35e32620-a28c-4101-a881-2b7c2b9e42f2).

###### A.6.1.1.1.2.6.1.3.3 - Arbitrum [Core]  <!-- UUID: 52565140-229d-42b4-9284-905b858dee6c -->

The Arbitrum Instances of the Spark Liquidity Layer with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.3.1 - Fluid [Core]  <!-- UUID: ede14170-01c6-4706-b17d-fb494b734a93 -->

The Arbitrum Instances of the Fluid Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.3.1.1 - Arbitrum - Fluid sUSDS ERC4626 Vault Instance Configuration Document [Core]  <!-- UUID: e6a55c76-91f7-4503-9349-b082c762ec76 -->

The documents herein contain the Instance Configuration Document for the Fluid sUSDS ERC4626 Instance.

###### A.6.1.1.1.2.6.1.3.3.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 910fe6e2-aeee-4d8a-8c98-dab4f9869a5c -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.3.1.1.2 - Parameters [Core]  <!-- UUID: 8ae596a4-1e54-430d-83ab-65e14c1b59a7 -->

The documents herein define the parameters of the Fluid sUSDS ERC4626 Vault Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.3.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: a3a5d44d-9ce3-40d0-af7d-dab76efd5d1e -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.3.1.1.2.1.1 - Network [Core]  <!-- UUID: b840b879-fcbe-4d18-ac3e-146693c67268 -->

Arbitrum

###### A.6.1.1.1.2.6.1.3.3.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: ed8dfb3b-d69b-4238-a685-0ee37d4c047b -->

Fluid Finance (ERC4626 Vault)

###### A.6.1.1.1.2.6.1.3.3.1.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: d6a11516-1a75-4d97-a7de-402595d68dbc -->

sUSDS

###### A.6.1.1.1.2.6.1.3.3.1.1.2.1.4 - Token [Core]  <!-- UUID: f9882004-d6bf-4c5d-b85a-d9230e52a1a8 -->

fsUSDS

###### A.6.1.1.1.2.6.1.3.3.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 30cb7c3c-1133-4899-9850-d92a72e86446 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.3.1.1.2.2.1 - Token Address (ERC4626 Vault) [Core]  <!-- UUID: d9b0d43b-3d65-453d-8099-f49e7959e6a4 -->

`0x3459fcc94390C3372c0F7B4cD3F8795F0E5aFE96`

###### A.6.1.1.1.2.6.1.3.3.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 656e1bad-91a3-4360-9804-a04ac194b1c7 -->

`0xdDb46999F8891663a8F2828d25298f70416d7610`

###### A.6.1.1.1.2.6.1.3.3.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: f6ab4108-a374-4fa6-81b2-61ca5078691f -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.3.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 74318ab4-90e3-4dd0-a21f-138a856b0c76 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.3.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 6c0b965a-f912-454e-9214-1fb23974ad2c -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 5,000,000 USDS per day

###### A.6.1.1.1.2.6.1.3.3.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 4abd5303-6a27-42fa-8128-4c6e65f089ee -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: 5,000,000 fsUSDS per day

###### A.6.1.1.1.2.6.1.3.3.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: ac2eb45f-a059-4dcc-9af4-baa1bbd60e3c -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.3.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 9eb37215-612f-45cd-a975-00683437326c -->

The Instance follows the general ERC4626 procedures see [A.6.1.1.1.2.6.1.2.2.1.2.1.2.2 - ERC-4626 Functions](e386a0df-9e0b-4ffd-9879-49131f795b0b) and for emergency procedures see [A.6.1.1.1.2.6.1.2.2.3.4.1 - ERC-4626 Withdrawal Action](f92ddc3f-672a-4f52-931f-5263a9f709b9). For detailed example of the Spark Liquidity Layer interaction logic for depositing to, withdrawing from, and redeeming from this ERC4626 vault instance see [A.6.1.1.1.2.6.1.3.1.5.1.3.1 - Deposit ERC-4626 Tokens](e2ad525b-3f3f-4402-9e4d-3ae125b35b76) and [A.6.1.1.1.2.6.1.3.1.5.1.3.2 - Withdraw ERC-4626 Tokens](caa295f4-92f4-4ca9-9083-2a1b94c70d5f).

###### A.6.1.1.1.2.6.1.3.3.2 - Aave [Core]  <!-- UUID: 014fccbf-4720-43f5-8dff-e58518c06f8c -->

The Arbitrum Instances of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.3.2.1 - Arbitrum - Aave USDC Instance Configuration Document [Core]  <!-- UUID: e11091aa-e569-4ca9-9151-dc5e1a8e1062 -->

The documents herein contain the Instance Configuration Document for the Aave USDC Instance.

###### A.6.1.1.1.2.6.1.3.3.2.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 25631831-853b-489f-b41a-2647ada595d6 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.3.2.1.2 - Parameters [Core]  <!-- UUID: 3aadca43-40a6-4647-81c6-912edc9ccd94 -->

The documents herein define the parameters of the Aave USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.3.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 2583e4c8-26d6-496f-99d6-30e0ece95dfa -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.3.2.1.2.1.1 - Network [Core]  <!-- UUID: f1e00fd6-c833-409f-9386-54787628d17b -->

Arbitrum

###### A.6.1.1.1.2.6.1.3.3.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 598df96f-6205-4149-a359-97bba4acae1c -->

Aave

###### A.6.1.1.1.2.6.1.3.3.2.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 698f28fd-3186-42b0-a0cb-0ef6a4cf71e3 -->

USDC

###### A.6.1.1.1.2.6.1.3.3.2.1.2.1.4 - Token [Core]  <!-- UUID: e836034b-a658-45ff-bcbd-bc2ee3bc24e7 -->

aArbUSDCn

###### A.6.1.1.1.2.6.1.3.3.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: 14933ea3-8469-4538-a37a-4963723a2fd3 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.3.2.1.2.2.1 - Token Address [Core]  <!-- UUID: 8768aad5-79b2-4e6d-a92b-6e1c654681a7 -->

`0x724dc807b04555b71ed48a6896b6F41593b8C637`

###### A.6.1.1.1.2.6.1.3.3.2.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 3fe18ab3-8f90-494e-8c8b-0b4218dd77f6 -->

`0xaf88d065e77c8cC2239327C5EDb3A432268e5831`

###### A.6.1.1.1.2.6.1.3.3.2.1.2.2.3 - Pool [Core]  <!-- UUID: aaf8a23e-ca02-4a8a-a75e-9431119b25bb -->

This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.3.2.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: b89d0921-1a1f-4b1e-a074-4027c7ab19ea -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.3.2.1.2.4 - Rate Limits [Core]  <!-- UUID: 2f22951b-c30c-47f9-a102-25a854c9a002 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.3.2.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: be3d1475-4efe-4eee-99eb-3f9941b858fa -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.1.2.6.1.3.3.2.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 254af84a-fe4c-471f-bc8c-dde31c728141 -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: Unlimited

###### A.6.1.1.1.2.6.1.3.3.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 4a10347b-02ab-47f4-8a13-b2b526fde198 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.3.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: d30527ea-821f-4c63-9f2a-3f13ff8064f7 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes. For the general operational procedures applicable to all Aave-type instances. See [A.6.1.1.1.2.6.1.2.2.1.2.1.2.3 - Aave Functions](9922dcf0-4562-445b-9a46-712f677cce64) and [A.6.1.1.1.2.6.1.2.2.3.2.3 - Aave AToken Withdrawal Action](2560adbb-4a5c-4c95-86cb-04647bb33836). For detailed example of the Spark Liquidity Layer interaction logic for depositing to and withdrawing from Aave see [A.6.1.1.1.2.6.1.3.1.2.1.3.1 - Process Definition For Depositing](fa2520ac-4779-4aeb-abe4-2c1b89e7ca51) and [A.6.1.1.1.2.6.1.3.1.2.1.3.2 - Process Definition For Withdrawing](35e32620-a28c-4101-a881-2b7c2b9e42f2).

###### A.6.1.1.1.2.6.1.3.3.3 - Spark Savings V2 [Core]  <!-- UUID: 417952e8-a21d-40e8-9a42-4a79f4fb0b62 -->

The Arbitrum Instances of the Spark Savings v2 with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.3.3.1 - Arbitrum - Spark Savings v2 USDT Instance Configuration Document [Core]  <!-- UUID: 1185b8bc-532d-4f34-93f3-1906bce1e119 -->

The documents herein contain the Instance Configuration Document for the Spark Savings v2 USDT Instance on Arbitrum.

###### A.6.1.1.1.2.6.1.3.3.3.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: bb1848fe-9e77-4b88-8d72-81720d43a8d4 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.3.3.1.2 - Parameters [Core]  <!-- UUID: c513d81f-468c-443d-a347-e4ac1f1e13a9 -->

The documents herein define the parameters of the Spark Savings v2 USDT Instance on Arbitrum of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.3.3.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 36ed03cc-4d66-44e6-9a61-ec91a74c2df4 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.3.3.1.2.1.1 - Network [Core]  <!-- UUID: 5fc5b168-7bf1-4d0f-b670-ffc371f4a2b4 -->

Arbitrum

###### A.6.1.1.1.2.6.1.3.3.3.1.2.1.2 - Target Protocol [Core]  <!-- UUID: cd865020-3ae2-4536-9611-3c6f615ba276 -->

Spark Savings Protocol

###### A.6.1.1.1.2.6.1.3.3.3.1.2.1.3 - Asset Supplied By Users [Core]  <!-- UUID: 64058ff5-bd62-4857-a800-7dfe14778b47 -->

USDT

###### A.6.1.1.1.2.6.1.3.3.3.1.2.1.4 - Token [Core]  <!-- UUID: 4cf98a3c-0682-43dd-9285-7870c73c1e97 -->

spUSDT

###### A.6.1.1.1.2.6.1.3.3.3.1.2.2 - Contract Addresses [Core]  <!-- UUID: 1fe8e6dd-f492-402e-b1d6-5573f5794724 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.3.3.1.2.2.1 - Token Address [Core]  <!-- UUID: a455756e-8476-443b-9d98-afee0bee28e5 -->

TBD

###### A.6.1.1.1.2.6.1.3.3.3.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 580ecc7a-ce02-4c7c-bd90-7f5bba059670 -->

`0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9`

###### A.6.1.1.1.2.6.1.3.3.3.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 6c53c9b0-8956-4c25-a6c5-ed7c254c276e -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.3.3.1.2.4 - Rate Limits [Core]  <!-- UUID: bfb9bfe1-e90b-4955-aa23-9892c2c85f2d -->

The specific `maxAmount` and `slope` for this conduit's inflow/outflow are not defined for this Instance.

###### A.6.1.1.1.2.6.1.3.3.3.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: e56ed430-1635-46b3-80d2-835443bc4988 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.3.3.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 07a4d26b-f250-4f37-b1b1-0974ed8138b6 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.3.3.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: c9140abd-2dd0-4055-918d-72302b90b4f5 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.3.3.1.4.1 - Contract Addresses [Core]  <!-- UUID: 55c38842-e297-4273-8d35-941d6c3beb71 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.3.3.1.4.1.1 - Spark Vault v2 Implementation [Core]  <!-- UUID: bfa35719-77b3-4fbf-b8a3-329238b66c86 -->

TBD

###### A.6.1.1.1.2.6.1.3.3.3.1.4.1.2 - Default admin [Core]  <!-- UUID: 079a23a2-8b55-4cfa-859e-0c3d5bbe9f80 -->

`0x65d946e533748A998B1f0E430803e39A6388f7a1`

###### A.6.1.1.1.2.6.1.3.3.3.1.4.1.3 - Setter [Core]  <!-- UUID: 60113aaa-8464-4417-9344-8594b5a2d23f -->

TBD

###### A.6.1.1.1.2.6.1.3.3.3.1.4.1.4 - Taker [Core]  <!-- UUID: 19011642-44ea-44d6-b5fa-74483f22692a -->

`0x92afd6F2385a90e44da3a8B60fe36f6cBe1D8709` (ALM_PROXY)

###### A.6.1.1.1.2.6.1.3.3.3.1.4.2 - Risk Parameters Current Configuration [Core]  <!-- UUID: eda78c7f-9e42-447f-ae44-fbe2ce987036 -->

The subdocuments herein define the current configuration of the risk parameters.

###### A.6.1.1.1.2.6.1.3.3.3.1.4.2.1 - Spark Savings USDT Risk Parameters [Core]  <!-- UUID: 36a496db-20c1-4d34-810e-518c4f99a755 -->

The Risk parameters are:

- Supply cap: 250,000,000 USDT
- Max yield: 6%
- Current yield (at launch): 0%

###### A.6.1.1.1.2.6.1.3.3.3.1.4.2.2 - Rate Limits [Core]  <!-- UUID: e9b62d67-cb5d-4bcb-9f5d-90688a85f123 -->

The current `maxAmount` for this conduit's take, transferAssets, and bridge operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.3.3.1.4.2.3 - Take Rate Limits [Core]  <!-- UUID: 430776a5-cc59-4904-a2c7-65bd5ee8e4ca -->

The take rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.3.3.1.4.2.4 - TransferAssets Rate Limits [Core]  <!-- UUID: 9496a85f-d220-4827-b7f4-b8b21c90b131 -->

The transferAssets rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.3.3.1.4.2.5 - Bridge to Ethereum Rate Limits [Core]  <!-- UUID: 26c7a10c-dc71-4ccd-a3d3-706549b2e4aa -->

The bridge-to-Ethereum rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.4 - Avalanche [Core]  <!-- UUID: c7b4d92f-9fdf-4f86-9ec5-84d7ac5373ac -->

The Avalanche Instances of the Spark Liquidity Layer with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.4.1 - Aave [Core]  <!-- UUID: 0a406127-5dc8-4d96-bc2e-4ba017d610bc -->

The Avalanche Instances of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.4.1.1 - Avalanche - Aave v3 USDC Vault Instance Configuration Document [Core]  <!-- UUID: ae06054a-1ed8-410b-983d-1789b49f1f19 -->

The documents herein contain the Instance Configuration Document for the Avalanche Aave v3 USDC Instance.

###### A.6.1.1.1.2.6.1.3.4.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 787a0db5-15a1-4220-97df-040647747a2f -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.4.1.1.2 - Parameters [Core]  <!-- UUID: bf0b9e14-f89d-45d8-83f7-09fd7fa596d4 -->

The documents herein define the parameters of the Avalanche Aave v3 USDC Vault Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.4.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 6567b399-126a-4b42-8716-8d899809990e -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.4.1.1.2.1.1 - Network [Core]  <!-- UUID: 8abad2b7-1efd-4e48-b2fc-009dd299d4b4 -->

Avalanche

###### A.6.1.1.1.2.6.1.3.4.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 1cb748ac-2e03-4d8e-89f2-17b8c935a37a -->

Aave

###### A.6.1.1.1.2.6.1.3.4.1.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 56593e5a-8e0b-42af-b8bd-a041e9a4999e -->

USDC

###### A.6.1.1.1.2.6.1.3.4.1.1.2.1.4 - Token [Core]  <!-- UUID: f3579a1a-b94e-48ea-96ec-f44b2d706278 -->

aAvaxUSDC

###### A.6.1.1.1.2.6.1.3.4.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: f0cd090b-7754-4436-8760-1491421fbee1 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.4.1.1.2.2.1 - Token Address [Core]  <!-- UUID: ea787215-4911-47e3-a9dc-e6b3f16f6e47 -->

`0x625E7708f30cA75bfd92586e17077590C60eb4cD`

###### A.6.1.1.1.2.6.1.3.4.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 494409b0-468f-4abb-b634-9f26d02f2bbe -->

`0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E`

###### A.6.1.1.1.2.6.1.3.4.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 6c79b029-bc6b-42b4-8689-c13c8105cad9 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.4.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 8e6dc8bd-4276-400a-9525-1c4e057727cf -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.4.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: ae6e143b-db94-46c3-b42f-96d73a0e2c0a -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 0

###### A.6.1.1.1.2.6.1.3.4.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: e3c0527d-368e-4c8c-bf7f-47ffb010f54c -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: 0

###### A.6.1.1.1.2.6.1.3.4.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 6f06f814-58ff-4978-b8e8-67848cae9290 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.4.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 8364da67-b040-4b71-9ef9-57c83f43cede -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes. For the general operational procedures applicable to all Aave-type instances. See Aave Functions and Aave AToken Withdrawal Action. For detailed example of the Spark Liquidity Layer interaction logic for depositing to and withdrawing from Aave see Process Definition For Depositing and Process Definition For Withdrawing.

###### A.6.1.1.1.2.6.1.3.4.2 - Spark Savings V2 [Core]  <!-- UUID: 3224ce80-1f48-48d9-b0d3-058aebb4723c -->

The Avalanche Instances of the Spark Savings v2 with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.4.2.1 - Avalanche - Spark Savings v2 USDC Instance Configuration Document [Core]  <!-- UUID: afa35a43-18e2-4084-b36c-eb584f4749ac -->

The documents herein contain the Instance Configuration Document for the Spark Savings v2 USDC Instance.

###### A.6.1.1.1.2.6.1.3.4.2.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 6cdcf295-4999-4c30-8f72-1a840a40c10e -->

**`Covered`**

###### A.6.1.1.1.2.6.1.3.4.2.1.2 - Parameters [Core]  <!-- UUID: 30cde382-587d-4cf2-b6a5-44918086131a -->

The documents herein define the parameters of the Spark Savings v2 USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.4.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 6487fdd4-c5a7-458e-8117-6cb0645674f7 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.4.2.1.2.1.1 - Network [Core]  <!-- UUID: ea9193c5-209b-464a-bfb5-5de47965f8c5 -->

Avalanche

###### A.6.1.1.1.2.6.1.3.4.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: dbee4fe8-546f-4e9f-bd11-a27c5309b148 -->

Spark Savings Protocol

###### A.6.1.1.1.2.6.1.3.4.2.1.2.1.3 - Asset Supplied By Users [Core]  <!-- UUID: fc1b9adf-616f-413b-9aa8-1977f30cdaea -->

USDC

###### A.6.1.1.1.2.6.1.3.4.2.1.2.1.4 - Token [Core]  <!-- UUID: eda065b2-4338-42b1-aafb-bd297ccc8645 -->

spUSDC

###### A.6.1.1.1.2.6.1.3.4.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: e251ec36-6483-48f0-a78a-1d392c9f0c81 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.4.2.1.2.2.1 - Token Address [Core]  <!-- UUID: 32e9d09c-1f8c-44b8-a281-f51a68351d41 -->

`0x28B3a8fb53B741A8Fd78c0fb9A6B2393d896a43d`

###### A.6.1.1.1.2.6.1.3.4.2.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: f6168c84-306f-4f20-afd6-fd24e84d405e -->

`0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E`

###### A.6.1.1.1.2.6.1.3.4.2.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: fb1032d9-61da-4bde-83b5-1410a53342d5 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.4.2.1.2.4 - Rate Limits [Core]  <!-- UUID: bc158ad0-debd-4f56-af7e-d0655772f693 -->

The specific `maxAmount` and `slope` for this conduit's inflow/outflow are not defined for this Instance.

###### A.6.1.1.1.2.6.1.3.4.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 382b30d4-e315-4622-b084-8b2ede0f37cd -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.4.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 5bba533c-caff-47b4-8236-06421a44533e -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.4.2.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 4df29394-5d9c-41ab-be95-886ea4b6f488 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.4.2.1.4.1 - Contract Addresses [Core]  <!-- UUID: e6135b1d-16f8-4c3f-97fb-c811eae22ce2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.4.2.1.4.1.1 - Spark Vault v2 Implementation [Core]  <!-- UUID: ae89c0a6-c7a9-4c53-81b9-6cf980747ace -->

`0xC2C0582D1cCe30449cF561C7b9C4D6d527547F12`

###### A.6.1.1.1.2.6.1.3.4.2.1.4.1.2 - Default admin [Core]  <!-- UUID: 13349fb3-57ed-4ab8-b1e3-18be5874c43c -->

`0x7566DEbC906C17338524A414343fA61BcA26A843`

###### A.6.1.1.1.2.6.1.3.4.2.1.4.1.3 - Setter [Core]  <!-- UUID: 5e5e0b85-842f-46fa-8124-6e272dd95351 -->

`0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC`

###### A.6.1.1.1.2.6.1.3.4.2.1.4.1.4 - Taker [Core]  <!-- UUID: a0b65455-b90d-43a1-bedd-5eb9f9c1378f -->

`0xecE6B0E8a54c2f44e066fBb9234e7157B15b7FeC`

###### A.6.1.1.1.2.6.1.3.4.2.1.4.2 - Risk Parameters Current Configuration [Core]  <!-- UUID: 668577c4-a21f-417f-aad0-95dddfc78fe2 -->

The subdocuments herein define the current configuration of the risk parameters.

###### A.6.1.1.1.2.6.1.3.4.2.1.4.2.1 - Spark Savings USDC Risk Parameters [Core]  <!-- UUID: 3d6a3fd3-4f36-45eb-9399-4eedfdc1c30d -->

The Risk parameters are:

- Supply cap: 500,000,000 USDC
- Max yield: 10%
- Current yield (at launch): 0%

###### A.6.1.1.1.2.6.1.3.4.2.1.4.2.2 - Rate Limits [Core]  <!-- UUID: 2b911731-5f03-41b0-afbd-41af37e8646f -->

The current `maxAmount` for this conduit's take and transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.4.2.1.4.2.3 - Take Rate Limits [Core]  <!-- UUID: 8507429b-f999-4990-825b-550ac91de996 -->

The take rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.4.2.1.4.2.4 - TransferAssets Rate Limits [Core]  <!-- UUID: 4c7311c4-a8fa-4bba-88f7-09abe67a8709 -->

The transferAssets rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.5 - Robinhood Chain [Core]  <!-- UUID: 21c64d57-704c-4be8-9fea-a144f2f6d823 -->

The Robinhood Chain Instances of the Spark Liquidity Layer with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.5.1 - Spark Savings V2 [Core]  <!-- UUID: 63906399-80ad-4bed-a21a-3256086445f6 -->

The Robinhood Chain Instances of the Spark Savings v2 with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.5.1.1 - Robinhood Chain - Spark Savings v2 USDG Instance Configuration Document [Core]  <!-- UUID: 87c1f6a7-8af8-4350-b43e-f63bc3287a1f -->

The documents herein contain the Instance Configuration Document for the Spark Savings v2 USDG Instance.

###### A.6.1.1.1.2.6.1.3.5.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 75a59e7d-89ec-4d3b-b3ac-d7bb1ef4e1f9 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.5.1.1.2 - Parameters [Core]  <!-- UUID: f0686fca-47c3-4e1b-8b2e-0a0f200fee27 -->

The documents herein define the parameters of the Spark Savings v2 USDG Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.5.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 2db3fcc3-168f-45f2-a485-1d564221cedb -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.5.1.1.2.1.1 - Network [Core]  <!-- UUID: 1f0c540b-58b4-4de0-8f98-7f78720545e6 -->

Robinhood Chain

###### A.6.1.1.1.2.6.1.3.5.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 47003e73-2ae3-480e-94a7-f02fc846bed0 -->

Spark Savings Protocol

###### A.6.1.1.1.2.6.1.3.5.1.1.2.1.3 - Asset Supplied By Users [Core]  <!-- UUID: 9b73a2bc-07d4-46ac-a2d1-bbfd17da0f65 -->

USDG

###### A.6.1.1.1.2.6.1.3.5.1.1.2.1.4 - Token [Core]  <!-- UUID: 2367709b-69c6-4802-83a0-359412ad5e90 -->

spUSDG

###### A.6.1.1.1.2.6.1.3.5.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: fc72fd66-d27c-4b4a-a9da-9fc1922f8712 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.5.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 0221abcc-dba6-4217-960d-a1283fc203e1 -->

`0xde770c84FE66E063336b31737cFE9790f18c4087`

###### A.6.1.1.1.2.6.1.3.5.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 4d74a337-b95b-4d8e-8443-57934eaf1b3d -->

`0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168`

###### A.6.1.1.1.2.6.1.3.5.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 474f18dd-93ea-47a4-a381-355a30495198 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.5.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 46fab347-8af2-4e79-ba3f-401f27d6155f -->

The specific `maxAmount` and `slope` for this conduit's inflow/outflow are not defined for this Instance.

###### A.6.1.1.1.2.6.1.3.5.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 76edace7-cc8b-4538-b4ea-5adde1867a6f -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.5.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: f649a78f-31e1-44a9-bcfe-186548c8a80d -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.5.1.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 7ed6859a-9622-488d-a876-136537246a8d -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.5.1.1.4.1 - Contract Addresses [Core]  <!-- UUID: 1dd81328-273d-4d86-b9c0-1bc652525c5a -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.5.1.1.4.1.1 - Spark Vault v2 Implementation [Core]  <!-- UUID: e9d71724-1d9c-40ae-9c55-7424484588c8 -->

`0x797c58C9779D46a437D8f57908D6d56371A55F02`

###### A.6.1.1.1.2.6.1.3.5.1.1.4.1.2 - Default admin [Core]  <!-- UUID: 9f747b40-077a-4d10-894b-ea006629b58f -->

`0x826AEaeee9233fA8Ba199518dd8621A5962b1D02`

###### A.6.1.1.1.2.6.1.3.5.1.1.4.1.3 - Setter [Core]  <!-- UUID: 2c8113d6-0239-4e90-8098-168d59b4a92a -->

`0xAEa9f5dE56e6C20383a1fcC2C3629Dca0A92cE41`

###### A.6.1.1.1.2.6.1.3.5.1.1.4.1.4 - Taker [Core]  <!-- UUID: bfcceb27-6f94-402c-ab56-fe2f5c1a5f58 -->

`0xfD2fD4B046136B540A56C11c75ac679AE7d1dB24`

###### A.6.1.1.1.2.6.1.3.5.1.1.4.2 - Risk Parameters Current Configuration [Core]  <!-- UUID: 2301ce34-abd5-44d2-9ef4-5bf2f296988e -->

The subdocuments herein define the current configuration of the risk parameters.

###### A.6.1.1.1.2.6.1.3.5.1.1.4.2.1 - Spark Savings USDG Risk Parameters [Core]  <!-- UUID: b5ac41a3-6ea8-453b-9a21-703f14d6a03b -->

The Risk parameters are:

- Supply cap: 500,000,000 USDG
- Max yield: 6%
- Current yield (at launch): 3.2%

###### A.6.1.1.1.2.6.1.3.5.1.1.4.2.2 - Rate Limits [Core]  <!-- UUID: f052e1ed-e2ff-4eaa-8cc4-8ecaabe0bcb4 -->

The current `maxAmount` for this conduit's take and transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.5.1.1.4.2.3 - Take Rate Limits [Core]  <!-- UUID: 6c10e42f-bd39-4359-9f7c-08ac9db45bbd -->

The take rate limits are:

- `maxAmount`: `TBD` (not specified in the proposal)

###### A.6.1.1.1.2.6.1.3.5.1.1.4.2.4 - TransferAssets Rate Limits [Core]  <!-- UUID: b58e2248-8251-4000-8867-9ba32d48f422 -->

The transferAssets rate limits are:

- `maxAmount`: `TBD`

###### A.6.1.1.1.2.6.1.3.6 - X Layer [Core]  <!-- UUID: 3a7ab5cb-578f-45c5-9af2-709d0994fc59 -->

The X Layer Instances of the Spark Liquidity Layer with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.6.1 - Spark Savings V2 [Core]  <!-- UUID: fc553aab-ee15-46b7-b7c8-1cd0c2d66a3e -->

The X Layer Instances of the Spark Savings v2 with `Active` Status are stored herein.

###### A.6.1.1.1.2.6.1.3.6.1.1 - X Layer - Spark Savings v2 USDT Instance Configuration Document [Core]  <!-- UUID: 8c303f01-617d-40aa-9f4f-181af2c6e040 -->

The documents herein contain the Instance Configuration Document for the Spark Savings v2 USDT Instance.

###### A.6.1.1.1.2.6.1.3.6.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 84621d14-e163-4901-a587-db71bd41c29b -->

**`Pending`**

###### A.6.1.1.1.2.6.1.3.6.1.1.2 - Parameters [Core]  <!-- UUID: 00682222-1a8c-4d61-afeb-3dec35a407ff -->

The documents herein define the parameters of the Spark Savings v2 USDT Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.3.6.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: af707a9d-4924-4d8f-8e1a-1d705ccf8037 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.3.6.1.1.2.1.1 - Network [Core]  <!-- UUID: efd71d98-be59-4b53-a6f4-95c0fa472676 -->

X Layer

###### A.6.1.1.1.2.6.1.3.6.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 1a39c007-d43e-428d-b632-d7f5e8363d4e -->

Spark Savings Protocol

###### A.6.1.1.1.2.6.1.3.6.1.1.2.1.3 - Asset Supplied By Users [Core]  <!-- UUID: db33e357-9873-4df4-85f1-cf3641056a4d -->

USDT

###### A.6.1.1.1.2.6.1.3.6.1.1.2.1.4 - Token [Core]  <!-- UUID: 11e3876c-60b9-4ade-99a5-cf3826aefb85 -->

spUSDT

###### A.6.1.1.1.2.6.1.3.6.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: ff87da05-63a5-4679-bbe8-a0742425f076 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.6.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 0e5728ab-c6c0-4522-9171-4bb471cd236f -->

`0xc358c90D32375721Cb3924320Fdc2F8B694347Ca`

###### A.6.1.1.1.2.6.1.3.6.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 423b3d2d-2e9e-482f-ba35-7e4999724ad5 -->

`0x779Ded0c9e1022225f8E0630b35a9b54bE713736`

###### A.6.1.1.1.2.6.1.3.6.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 33cba822-a02a-4217-abcd-95df7d27e617 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.3.6.1.1.2.4 - Rate Limits [Core]  <!-- UUID: eeb497f8-b2eb-407a-99a2-d13c1331639f -->

The specific `maxAmount` and `slope` for this conduit's inflow/outflow are not defined for this Instance.

###### A.6.1.1.1.2.6.1.3.6.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 9a6e598f-d847-4b98-a77b-56e439faee70 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.3.6.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 417f67dd-91e6-4dc9-beb9-0e5f8ee71b45 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.3.6.1.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 8c180763-df32-4b22-bce4-409d8c7e2e30 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.3.6.1.1.4.1 - Contract Addresses [Core]  <!-- UUID: dee8f3c2-fa48-42ef-abbc-65fe730cb2d8 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.3.6.1.1.4.1.1 - Spark Vault v2 Implementation [Core]  <!-- UUID: 9e0a1b83-768f-40f3-9431-3eae4bb41dcf -->

`0xdCe929A335C75a1676EF5957A4D7a3b928C48820`

###### A.6.1.1.1.2.6.1.3.6.1.1.4.1.2 - Default admin [Core]  <!-- UUID: 647925dc-3546-4752-ab35-ada93692540b -->

`0xCF5af6F53ceC74B791cb4182aC778ca9CD323510`

###### A.6.1.1.1.2.6.1.3.6.1.1.4.1.3 - Setter [Core]  <!-- UUID: 7cfdb652-c322-42d6-921d-3fc53149a2bf -->

`0x9449ed367C60ea757544fd990B57e1C2D0Ec3A94`

###### A.6.1.1.1.2.6.1.3.6.1.1.4.1.4 - Taker [Core]  <!-- UUID: 6ad784d7-78bb-40fa-be70-32c9d6a721a9 -->

`0x83A914C361bB729EB6BEBC8C7bA993667A0E6Df8`

###### A.6.1.1.1.2.6.1.3.6.1.1.4.2 - Risk Parameters Current Configuration [Core]  <!-- UUID: 52f29085-dacf-4d83-bfdc-57e7b9d3e44f -->

The subdocuments herein define the current configuration of the risk parameters.

###### A.6.1.1.1.2.6.1.3.6.1.1.4.2.1 - Spark Savings USDT Risk Parameters [Core]  <!-- UUID: ca2ed587-e956-4672-a5f1-5fc0f0ea666d -->

The Risk parameters are:

- Supply cap: 750,000,000 USDT
- Max yield: 6%
- Current yield (at launch): 0%

###### A.6.1.1.1.2.6.1.3.6.1.1.4.2.2 - Rate Limits [Core]  <!-- UUID: 36204d14-11b1-439d-91b0-1dfc2a381a0d -->

The current `maxAmount` for this conduit's take and transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.3.6.1.1.4.2.3 - Take Rate Limits [Core]  <!-- UUID: e33c5054-f982-49a4-ae18-6e7394a3ea1a -->

The take rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.1.2.6.1.3.6.1.1.4.2.4 - TransferAssets Rate Limits [Core]  <!-- UUID: 6fd02c5f-ce6d-4e0c-8f4f-69e45dd3aa37 -->

The transferAssets rate limits are:

- `maxAmount`: Unlimited

##### A.6.1.1.1.2.6.1.4 - Completed Instances [Core]  <!-- UUID: ed8c3394-ee05-496c-8dd6-4d5275d2ed1f -->

The Instances of the Spark Liquidity Layer with `Completed` Status are stored herein.

###### A.6.1.1.1.2.6.1.4.1 - Blackrock [Core]  <!-- UUID: ce83f39e-5efb-4a88-b27f-989083213239 -->

The Ethereum Mainnet Instances of the Blackrock Protocol with `Completed` Status are stored herein.

###### A.6.1.1.1.2.6.1.4.1.1 - Ethereum Mainnet - Blackrock USDC Instance Configuration Document [Core]  <!-- UUID: 7a52fb87-96bf-4135-9a61-f2dc068af12c -->

The documents herein contain the Instance Configuration Document for the Blackrock USDC Instance.

###### A.6.1.1.1.2.6.1.4.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 704fd922-1700-4c0e-b182-e3ffe8741274 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.4.1.1.2 - Parameters [Core]  <!-- UUID: 9f44d3eb-b1d4-490e-bab2-8f39b73dc6ad -->

The documents herein define the parameters of the Blackrock USDC Instance of the Allocation System Primitive

###### A.6.1.1.1.2.6.1.4.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: fcee0621-3878-461c-8900-a55e62c90aeb -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.4.1.1.2.1.1 - Network [Core]  <!-- UUID: c667269d-b366-4a14-9861-e506d107a767 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.4.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 10169c03-bbd8-40c2-990c-44ee2f5d436f -->

Blackrock

###### A.6.1.1.1.2.6.1.4.1.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 3215e3d7-850e-400a-adac-b57223c354c6 -->

USDC

###### A.6.1.1.1.2.6.1.4.1.1.2.1.4 - Token [Core]  <!-- UUID: 892b7916-3ca3-4fd1-a8d2-732646ad7353 -->

BUIDL-I

###### A.6.1.1.1.2.6.1.4.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 1dd65da0-57e4-4cb4-bf6c-7885b0616ae2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.4.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 43930781-984c-4ba4-91e1-5e564fe448ad -->

`0x6a9DA2D710BB9B700acde7Cb81F10F1fF8C89041`

###### A.6.1.1.1.2.6.1.4.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 284c77f5-ea1b-4569-a4f4-9241cf338f9b -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.4.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 43f9fa01-68a2-4c8f-b1f4-fe775927562e -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow is:

- `BUIDLI_DEPOSIT`: `0xD1917664bE3FdAea377f6E8D5BF043ab5C3b1312`
- `BUIDL_REDEEM` (Circle redeem): `0x31D3F59Ad4aAC0eeE2247c65EBE8Bf6E9E470a53`
- `BUIDLI_REDEEM` (Offchain redeem): `0x8780Dd016171B91E4Df47075dA0a947959C34200`

###### A.6.1.1.1.2.6.1.4.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 3a9acb95-b227-4473-aa26-95b7f25cfd8a -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.4.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 4ec7ede8-416b-486e-ba56-160b02189a7b -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.4.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 1fc9d6f3-3996-4245-a096-53dad4a624ea -->

The outflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.4.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: dd3dffeb-7157-46dc-bf65-f5c8d5bf9fc8 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.4.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: ddd37d10-75dd-4de4-a88b-b92745fd53bc -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.4.2 - Centrifuge [Core]  <!-- UUID: 8fb735f7-7d36-4b35-9e9a-19b645674517 -->

The Ethereum Mainnet Instances of the Centrifuge Protocol with `Completed` Status are stored herein.

###### A.6.1.1.1.2.6.1.4.2.1 - Ethereum Mainnet - Centrifuge USDC Instance Configuration Document [Core]  <!-- UUID: 289555ee-996e-43a7-b05f-a0b06d1238f5 -->

The documents herein contain the Instance Configuration Document for the Centrifuge USDC Instance.

###### A.6.1.1.1.2.6.1.4.2.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: c9a19386-f124-49bc-aca1-6860293395f3 -->

**`Pending`**

###### A.6.1.1.1.2.6.1.4.2.1.2 - Parameters [Core]  <!-- UUID: 35533e6c-2d70-4cba-8192-95a150f93e9c -->

The documents herein define the parameters of the Centrifuge USDC Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.4.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 1ba05a79-f768-45e8-ae14-bb04495e6f6c -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.4.2.1.2.1.1 - Network [Core]  <!-- UUID: c10013b3-c688-4a97-8a5c-44c56d9ef481 -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.4.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 1c386cce-adee-4f5a-aa88-7c84f0709a70 -->

Centrifuge

###### A.6.1.1.1.2.6.1.4.2.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 8eb1c7a9-18a7-46bf-841d-2db3476bf8ea -->

USDC

###### A.6.1.1.1.2.6.1.4.2.1.2.1.4 - Token [Core]  <!-- UUID: aaa19944-a11f-43e3-8ddf-25e8ab357d97 -->

JTRSY

###### A.6.1.1.1.2.6.1.4.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: 538be44e-fe35-4f33-83de-613713f0b674 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.4.2.1.2.2.1 - Token Address [Core]  <!-- UUID: 75405fc4-d493-410d-b036-dc7f67242ca3 -->

`0x8c213ee79581Ff4984583C6a801e5263418C4b86`

###### A.6.1.1.1.2.6.1.4.2.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 8e1a1625-29e0-46d0-ac50-d43b40c4c79d -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.1.2.6.1.4.2.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 3cd3c96e-b459-468f-a7be-f5c52c38666e -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.4.2.1.2.4 - Rate Limits [Core]  <!-- UUID: e5519b29-8100-4490-965b-a616729865e1 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.4.2.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 81ab5665-f9b9-4363-9d05-0d7bf371394a -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.4.2.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 997c0581-022d-4fdd-8fde-cb43d58c8940 -->

The outflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Spark Artifact.
- `slope`: This parameter will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.4.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 5ab63d35-c3d1-4ea6-924c-2d56bcd68295 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.4.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: d14420a3-4b36-4eac-bb1b-04f5598fe347 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.4.3 - Ethereum Mainnet Instances [Core]  <!-- UUID: 4a98960f-dd05-4f2b-9e7c-66a489ee499a -->

The Ethereum Mainnet Instances of the Spark Liquidity Layer with `Completed` Status are stored herein and are organized by target protocol.

###### A.6.1.1.1.2.6.1.4.3.1 - Morpho [Core]  <!-- UUID: 1581c7c2-ee47-45ed-a7ba-b254ab7a6975 -->

The Ethereum Mainnet Instances of the Morpho Protocol with `Completed` Status are stored herein.

###### A.6.1.1.1.2.6.1.4.3.1.1 - Ethereum Mainnet - Morpho USDT Instance Configuration Document [Core]  <!-- UUID: a2f66f86-ddea-4260-820a-cde66a861413 -->

The documents herein contain the Instance Configuration Document for the Morpho USDT Instance.

###### A.6.1.1.1.2.6.1.4.3.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 0679d377-0d6f-4511-a8a9-2c1fe7b5d78f -->

**`Pending`**

###### A.6.1.1.1.2.6.1.4.3.1.1.2 - Parameters [Core]  <!-- UUID: 3c749393-8134-4483-ad35-c6820768421f -->

The documents herein define the parameters of the Morpho USDT Instance of the Allocation System Primitive.

###### A.6.1.1.1.2.6.1.4.3.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 077e23e8-fc30-4dc9-8c61-c08f7fe10864 -->

The documents herein define the Instance identifiers

###### A.6.1.1.1.2.6.1.4.3.1.1.2.1.1 - Network [Core]  <!-- UUID: bea790d6-8b58-45fb-a974-2813284831ee -->

Ethereum Mainnet

###### A.6.1.1.1.2.6.1.4.3.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: a700da65-026f-4cf7-a1fb-a30cedc10189 -->

Morpho

###### A.6.1.1.1.2.6.1.4.3.1.1.2.1.3 - Asset Supplied By Spark Liquidity Layer [Core]  <!-- UUID: 9ecacc4a-fe57-427b-a652-92409b64aef6 -->

USDT

###### A.6.1.1.1.2.6.1.4.3.1.1.2.1.4 - Token [Core]  <!-- UUID: 46ea2f39-26c6-4ac4-9ee7-baf921d8e86e -->

sparkUSDT

###### A.6.1.1.1.2.6.1.4.3.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 1eb8cc31-5d23-4aaa-b99e-b57654c9dbc4 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.4.3.1.1.2.2.1 - Token Address [Core]  <!-- UUID: c4629de2-eb51-4661-a4bc-6b955e267f5f -->

`0xc7CDcFDEfC64631ED6799C95e3b110cd42F2bD22`

###### A.6.1.1.1.2.6.1.4.3.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: a3ed9893-931b-4d4e-9cf9-35373d1ed005 -->

`0xdac17f958d2ee523a2206206994597c13d831ec7`

###### A.6.1.1.1.2.6.1.4.3.1.1.2.2.3 - Allocator Role Address [Core]  <!-- UUID: 30cdfa34-7b8d-4280-bda2-ec53940a8093 -->

`0xe5c6318456a7Cb6f74f93B4eee4616dB5fcef699`

###### A.6.1.1.1.2.6.1.4.3.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: bde22f96-915b-4073-840f-ac0408aa8407 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.2.6.1.4.3.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 7eaf8614-3343-4a6b-a637-8a92a7115bbb -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.1.2.6.1.4.3.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 0c654529-b8b7-4071-bc72-5eee02d295c9 -->

The inflow rate limits are:

- `maxAmount`: 0
- `slope`: 0

###### A.6.1.1.1.2.6.1.4.3.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 6dab7518-caa3-4339-a573-718675fe19ee -->

The outflow rate limits are:

- `maxAmount`: 0
- `slope`: 0

###### A.6.1.1.1.2.6.1.4.3.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 3bb2d3ac-cdcc-4f25-a03c-71d2d0902582 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.1.2.6.1.4.3.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 32759a33-f619-4a41-a4fd-fbcdb642a82a -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer processes.

###### A.6.1.1.1.2.6.1.4.3.1.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 06914650-b873-4c39-8389-5c615c64edf7 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Spark Liquidity Layer parameters.

###### A.6.1.1.1.2.6.1.4.3.1.1.4.1 - Market Exposure [Core]  <!-- UUID: bcf45274-0125-4856-a405-ed2726fad468 -->

The documents herein contain exposure details for this Instance

###### A.6.1.1.1.2.6.1.4.3.1.1.4.1.1 - sUSDS/USDT 96.5% LLTV Pool [Core]  <!-- UUID: 2187c7a6-d9d2-46c7-a794-5779939c708f -->

- Pool ID: 0x3274643db77a064abd3bc851de77556a4ad2e2f502f4f0c80845fa8f909ecf0b
- Absolute cap: Unlimited
- Relative cap: 100%

###### A.6.1.1.1.2.6.1.4.3.1.1.4.1.2 - wstETH/USDT 86% LLTV Pool [Core]  <!-- UUID: 28068a47-d95a-4edb-a7cd-15a9fa769d01 -->

- Pool ID: 0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2
- Absolute cap: 250 million
- Relative cap: 100%

###### A.6.1.1.1.2.6.1.4.3.1.1.4.1.3 - WBTC/USDT 86% LLTV Pool [Core]  <!-- UUID: c2b81ec6-62d4-4a8e-8195-411051e74708 -->

- Pool ID: 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99
- Absolute cap: 100 million
- Relative cap: 100%

###### A.6.1.1.1.2.6.1.4.3.1.1.4.1.4 - cbBTC/USDT 86% LLTV Pool [Core]  <!-- UUID: b89ff2c9-be7e-4634-bddd-8ebbf5eb6769 -->

- Pool ID: 0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca
- Absolute cap: 250 million
- Relative cap: 100%

###### A.6.1.1.1.2.6.1.4.3.1.1.4.2 - Contract Addresses [Core]  <!-- UUID: c481d26c-a4b1-4c76-9031-478bd64a8aca -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.1.2.6.1.4.3.1.1.4.2.1 - Curator Role Address [Core]  <!-- UUID: e71e777b-b5a8-41bb-8434-97650500467a -->

`0x0f963A8A8c01042B69054e787E5763ABbB0646A3`

###### A.6.1.1.1.2.6.1.4.3.1.1.4.2.2 - Guardian Role Address [Core]  <!-- UUID: 6e105430-ea5c-4368-b76f-725c0208afdc -->

`0xf5748bBeFa17505b2F7222B23ae11584932C908B`

###### A.6.1.1.1.2.6.1.4.3.1.1.4.3 - Timelock [Core]  <!-- UUID: 62c056de-3136-4faa-bb86-3b348e2e874c -->

Timelock: 240 hours (10 days)

##### A.6.1.1.1.2.6.1.5 - In Progress Invocations [Core]  <!-- UUID: 5b1ce161-fc9e-4c90-ac14-75cfbba6a213 -->

The in progress Invocations of the Allocation System Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.6.1.3 - Active Instances](f7c9fdda-3d42-4b9d-852d-610d7ae4f6c0).

##### A.6.1.1.1.2.6.1.6 - Data Repository [Core]  <!-- UUID: 0ffbf052-9a57-430a-a140-40666dc2548b -->

The documents herein contain data relevant to the Spark Liquidity Layer.

#### A.6.1.1.1.2.6.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: bef153ea-bce0-4f87-aea1-be1ed219b0c1 -->

The documents herein contain all data and specifications for Spark’s Instances of the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.6.1.1.1.2.6.2.1 - Primitive Hub Document [Core]  <!-- UUID: 760db109-8209-4993-aa0f-a472cd09342f -->

The documents herein organize all base information relevant to Spark’s usage of the Risk Capital Rental Primitive.

###### A.6.1.1.1.2.6.2.1.1 - Global Activation Status [Core]  <!-- UUID: f677430e-d241-4697-afb7-3375ab33f901 -->

`Inactive`

###### A.6.1.1.1.2.6.2.1.2 - Active Instances Directory [Core]  <!-- UUID: cdd934f4-7607-4447-873a-2b08618d50b5 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 064dec5f-e008-450a-80b9-098dd49a06bc -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.6.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 0e18ffbc-b51b-4a25-a60a-b4b8ba61580b -->

This document contains a Directory of all prospective Instances of the Risk Capital Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.6.2.1.2 - Active Instances Directory](cdd934f4-7607-4447-873a-2b08618d50b5), whereas failed Invocations are Archived in [A.6.1.1.1.2.6.2.1.5 - Hub Data Repository](073af9bf-c7df-41ab-93cc-798f972134a3).

###### A.6.1.1.1.2.6.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 073af9bf-c7df-41ab-93cc-798f972134a3 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.6.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 93185aa4-1770-4649-b9b8-a570a3f6b2e8 -->

The subtrees for archived Invocations and Instances of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.1.2.6.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: b9d396f1-e40c-4ec7-9855-852ae94e51ca -->

The subtrees for failed Invocations of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.1.2.6.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 505bd7a0-19e8-4b67-acb0-cf007114dd6c -->

The subtrees for Instances of the Risk Capital Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.6.2.2 - Active Instances [Core]  <!-- UUID: a9dfa35d-e51d-43ee-aa07-90c96a6acb86 -->

The Instances of the Risk Capital Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.6.2.3 - Completed Instances [Core]  <!-- UUID: 6fab7906-d1dd-4291-9044-10eecd2c65d0 -->

The Instances of the Risk Capital Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.1.2.6.2.4 - In Progress Invocations [Core]  <!-- UUID: 17e60d50-f521-4634-a732-ecface0953ca -->

The in progress Invocations of the Risk Capital Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.6.2.2 - Active Instances](a9dfa35d-e51d-43ee-aa07-90c96a6acb86).

#### A.6.1.1.1.2.6.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: 9f627e5c-f56e-42a3-abf9-1bce25e7d1ba -->

The documents herein contain all data and specifications for Spark’s Instances of the Asset Liability Management Rental Primitive. See [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

##### A.6.1.1.1.2.6.3.1 - Primitive Hub Document [Core]  <!-- UUID: 45974478-1591-4d54-9aae-e68a9b6f8793 -->

The documents herein organize all base information relevant to Spark’s usage of the Asset Liability Management Rental Primitive.

###### A.6.1.1.1.2.6.3.1.1 - Global Activation Status [Core]  <!-- UUID: 8eece156-6d42-4cf3-88ec-0080b82be855 -->

`Inactive`

###### A.6.1.1.1.2.6.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 22456b6d-8106-48dd-ab8f-b6c5feec643a -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.6.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 197dc003-e809-49dd-85f3-8286f304e70f -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.6.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 5e84e500-7b2b-42ae-b23e-34fad4d9aa57 -->

This document contains a Directory of all prospective Instances of the Asset Liability Management Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.6.3.1.2 - Active Instances Directory](22456b6d-8106-48dd-ab8f-b6c5feec643a), whereas failed Invocations are Archived in [A.6.1.1.1.2.6.3.1.5 - Hub Data Repository](ea4f687a-7c81-41bd-918a-7f4d56120f43).

###### A.6.1.1.1.2.6.3.1.5 - Hub Data Repository [Core]  <!-- UUID: ea4f687a-7c81-41bd-918a-7f4d56120f43 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.6.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e1c20a8c-f154-4680-95d4-5776281fd1d2 -->

The subtrees for archived Invocations and Instances of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.1.2.6.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: d4c34da2-6c80-461a-a156-7ca0ad76ef0c -->

The subtrees for failed Invocations of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.1.2.6.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 06cc0973-28bf-48de-a5af-4438ea8a76fa -->

The subtrees for Instances of the Asset Liability Management Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.6.3.2 - Active Instances [Core]  <!-- UUID: cdb5065b-0a14-4cf8-a0ac-d6b547ee0994 -->

The Instances of the Asset Liability Management Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.6.3.3 - Completed Instances [Core]  <!-- UUID: 25ce8d32-f425-4769-9de3-60c5517f1ab1 -->

The Instances of the Asset Liability Management Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.1.2.6.3.4 - In Progress Invocations [Core]  <!-- UUID: 203386d2-3c59-4edd-aece-4d8034a2a08f -->

The in progress Invocations of the Asset Liability Management Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.6.3.2 - Active Instances](cdb5065b-0a14-4cf8-a0ac-d6b547ee0994).

### A.6.1.1.1.2.7 - Core Governance Primitives [Core]  <!-- UUID: a0865261-677f-4cbf-a409-df6ac29d6e29 -->

The documents herein implement the Core Governance Primitives for Spark. See [A.2.2.11 - Core Governance Primitives](6fa54611-c744-4b9d-897d-b2a20e9cae5d).

#### A.6.1.1.1.2.7.1 - Core Governance Reward Primitive [Core]  <!-- UUID: 5d111751-fac3-495e-8829-ce849c28aac8 -->

The documents herein contain all data and specifications for Spark’s Instances of the Core Governance Reward Primitive. See [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a).

##### A.6.1.1.1.2.7.1.1 - Primitive Hub Document [Core]  <!-- UUID: 88a9d7aa-be82-4f4b-bb86-7eb9748c64ee -->

The documents herein organize all base information relevant to Spark’s usage of the Core Governance Reward Primitive.

###### A.6.1.1.1.2.7.1.1.1 - Global Activation Status [Core]  <!-- UUID: 85326b8b-a790-4b68-be43-2fff907bbf75 -->

`Inactive`

###### A.6.1.1.1.2.7.1.1.2 - Active Instances Directory [Core]  <!-- UUID: f4c484c7-e2e6-4d7c-ab60-6154e6c44fcd -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Active`.

###### A.6.1.1.1.2.7.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 46fcc70f-f3a8-4a6d-ba36-985b0adfda11 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.1.2.7.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 777f68a6-2248-44e5-9386-e6d4105498a4 -->

This document contains a Directory of all prospective Instances of the Core Governance Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.1.2.7.1.1.2 - Active Instances Directory](f4c484c7-e2e6-4d7c-ab60-6154e6c44fcd), whereas failed Invocations are Archived in [A.6.1.1.1.2.7.1.1.5 - Hub Data Repository](b8e04127-ab44-4b58-b122-d85532138b13).

###### A.6.1.1.1.2.7.1.1.5 - Hub Data Repository [Core]  <!-- UUID: b8e04127-ab44-4b58-b122-d85532138b13 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.1.2.7.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: c214c982-d058-4cc5-b8f9-024d5ca5dea7 -->

The subtrees for archived Invocations and Instances of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.1.2.7.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: e9d454c5-88b2-491e-bba0-206f2ca987a9 -->

The subtrees for failed Invocations of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.1.2.7.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 7f3c7c95-5759-4fd7-891b-60841b98df86 -->

The subtrees for Instances of the Core Governance Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.1.2.7.1.2 - Active Instances [Core]  <!-- UUID: 1f638b59-eff7-4d69-870c-487f2728b188 -->

The Instances of the Core Governance Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.1.2.7.1.3 - Completed Instances [Core]  <!-- UUID: ffe6fa8d-4fb7-4cb3-8dda-328387613987 -->

The Instances of the Core Governance Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.1.2.7.1.4 - In Progress Invocations [Core]  <!-- UUID: 7aae676b-55ba-4001-9a03-e9112f9bd94c -->

The in progress Invocations of the Core Governance Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.1.2.7.1.2 - Active Instances](1f638b59-eff7-4d69-870c-487f2728b188).

## A.6.1.1.1.3 - Omni Documents [Core]  <!-- UUID: f5ba2aec-ac1b-4da9-adc9-e1d370620e72 -->

The documents herein define Spark’s strategic intent and operational processes relating to infrastructure inherited from Sky Core, activities unrelated to Sky Primitives, or activities spanning multiple Sky Primitives.

### A.6.1.1.1.3.1 - Governance Information Unrelated To Root Edit Primitive [Core]  <!-- UUID: 3dffc0f5-edbc-48e9-bf13-7d752a64de5a -->

The documents herein specify Spark governance information that is unrelated to the use of the Root Edit Primitive. The governance process for updating the Spark Artifact is specified in the Root Edit Primitive above at [A.6.1.1.1.2.2.2 - Root Edit Primitive](f60887de-a4eb-4e4b-8aa6-e22cf724772a).

#### A.6.1.1.1.3.1.1 - Sky Forum [Core]  <!-- UUID: 978879a2-3f8b-4f3e-a938-07e8a5b4b4de -->

Spark uses the Sky Forum for governance-related discussion. Posts should use the "Spark Prime" category.

#### A.6.1.1.1.3.1.2 - Discord [Core]  <!-- UUID: e7118615-bbaa-4a3d-b395-407244cc0969 -->

Spark also uses Discord for more immediate communication. The Spark Discord is located at [https://t.co/v6zG0MZtak](https://t.co/v6zG0MZtak).

#### A.6.1.1.1.3.1.3 - Delegation Framework [Core]  <!-- UUID: afa6a37e-e7f1-4efb-bca7-f02bbbf5cf26 -->

The documents herein specify Spark’s governance delegation system, defining the rights and duties of Delegates and Delegators, as well as the processes for onboarding and offboarding Delegates.

##### A.6.1.1.1.3.1.3.1 - Delegate Definition [Core]  <!-- UUID: f667b5fa-0e31-4e59-9cfe-85c31c9f0b84 -->

A "Delegate" is a recognized actor empowered to exercise governance voting power on behalf of one or more SPK holders ("Delegators"). Delegates act as trusted representatives and are expected to vote in the long-term best interest of the Spark ecosystem.

##### A.6.1.1.1.3.1.3.2 - How Delegation Works [Core]  <!-- UUID: 7fcbb9da-7559-4a18-ab68-f0840a3fe921 -->

SPK holders may assign ("delegate") the full voting power of their wallet to an Active Delegate at any time (see [A.6.1.1.1.3.1.3.8 - Registry of Delegates](f49a1e26-f774-4fbd-b7f8-156639e077f2)). The key features of delegation are specified in the subdocuments herein.

###### A.6.1.1.1.3.1.3.2.1 - Interfaces [Core]  <!-- UUID: e5ad866a-9d53-472e-bff5-077d06e8171f -->

Delegation can be executed through (i) the Spark App or (ii) directly on Spark’s Snapshot page.

###### A.6.1.1.1.3.1.3.2.2 - Snapshot Voting-Power Lock [Core]  <!-- UUID: 99c40e7d-2033-4ca2-bf8d-a2f4a8556b0d -->

A snapshot records voting power at each proposal snapshot-block height. Voting power (including delegations) cannot be altered for the duration of a specific active proposal. Changes in voting power are reflected in future votes.

###### A.6.1.1.1.3.1.3.2.3 - Undelegation & Re-delegation [Core]  <!-- UUID: 375d4774-24f8-4f19-9b00-1a9043891b70 -->

Delegators may revoke or move their delegation whenever no proposal is live. All changes take effect at the next snapshot-block.

###### A.6.1.1.1.3.1.3.2.4 - Restrictions [Core]  <!-- UUID: 64fd2894-944b-41a3-bfaa-435035bfd257 -->

SPK holders may only assign their voting power to Active Delegates. This also means Delegators cannot delegate to another wallet they themselves control, unless it is an Active Delegate wallet.

##### A.6.1.1.1.3.1.3.3 - Delegate Responsibilities [Core]  <!-- UUID: f230ba4e-eb5a-444e-b07a-13a0292338bd -->

The responsibilities for Delegates are defined in the subdocuments herein.

###### A.6.1.1.1.3.1.3.3.1 - Monitor Governance Channels [Core]  <!-- UUID: 3a662279-94d2-469e-b4c8-256b998a1b35 -->

The Delegate must track the Sky Forum ("Spark Prime" category), Discord, and any other official communication venues for new proposals and discussions.

###### A.6.1.1.1.3.1.3.3.2 - Review Proposals Thoroughly [Core]  <!-- UUID: e494b7ff-22ae-40cf-8ce5-c285dd6a63ea -->

The Delegate must evaluate technical, economic, and risk implications before voting.

###### A.6.1.1.1.3.1.3.3.3 - Vote on Every Proposal [Core]  <!-- UUID: 46e9d0bb-e251-4f07-8327-804456f2e68a -->

The Delegate must cast a vote (For / Against) on 100% of governance proposals within the designated voting window (see [A.6.1.1.1.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote](b60cfc4e-4cc5-4040-9610-f2113980831b)).

###### A.6.1.1.1.3.1.3.3.4 - Abstain Only for Disclosed Conflicts [Core]  <!-- UUID: 16eb44b8-0a93-4138-a11a-99e654727b90 -->

The "Abstain" option may be used solely in cases where the Delegate has a documented conflict of interest for the specific proposal.

###### A.6.1.1.1.3.1.3.3.4.1 - Disclosure Of Conflicts [Core]  <!-- UUID: cfdf3c2d-6ede-49f0-8f2c-0cd91a5602bc -->

Conflicts must be disclosed to both the Spark Foundation before the voting window (see [A.6.1.1.1.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote](b60cfc4e-4cc5-4040-9610-f2113980831b)) for the proposal begins.

###### A.6.1.1.1.3.1.3.3.4.2 - Abstaining For Non-Disclosed Conflicts [Core]  <!-- UUID: 4d8ad5e6-937e-4916-ad8b-8d7e74a93542 -->

Abstaining for any reason other than a disclosed conflict is treated as non-performance under [A.6.1.1.1.3.1.3.5 - Delegate Offboarding](b49d9086-cb8a-43f7-a024-0d3320eae317).

###### A.6.1.1.1.3.1.3.3.5 - Report Rationale [Core]  <!-- UUID: 683bd4a6-b07a-4ed0-85dc-2f6d0f13bc6e -->

The Delegate must post a concise rationale for each vote on the proposal thread.

###### A.6.1.1.1.3.1.3.3.6 - Maintain Independence [Core]  <!-- UUID: 6b2f76c8-3486-45f9-a79a-feae8b9117c0 -->

The Delegate must disclose conflicts of interest and abstain where impartiality is compromised (see [A.6.1.1.1.3.1.3.3.4.1 - Disclosure Of Conflicts](cfdf3c2d-6ede-49f0-8f2c-0cd91a5602bc)). Failure to meet these obligations is grounds for offboarding (see [A.6.1.1.1.3.1.3.5 - Delegate Offboarding](b49d9086-cb8a-43f7-a024-0d3320eae317)).

##### A.6.1.1.1.3.1.3.4 - Delegate Onboarding [Core]  <!-- UUID: fcf62ce5-910a-4357-a3d5-959b3be37021 -->

The Delegate onboarding process is specified in the subdocuments herein.

###### A.6.1.1.1.3.1.3.4.1 - Delegate Onboarding Process [Core]  <!-- UUID: d08b9b32-bce9-45f4-b8db-9301556ac8db -->

The Spark Foundation manages Delegate onboarding. The Spark Foundation may onboard a Delegate at its discretion. Minimum onboarding requirements are (1) identity and contact information, (2) Delegate wallet address, and (3) a signed acceptance of [A.6.1.1.1.3.1.3.3 - Delegate Responsibilities](f230ba4e-eb5a-444e-b07a-13a0292338bd). The Spark Foundation conducts identity verification, conflict-of-interest collection, and sanctions and undue-risk checks as it deems necessary. Upon acceptance, the Foundation notifies the Operational Facilitator, who updates [A.6.1.1.1.3.1.3.8 - Registry of Delegates](f49a1e26-f774-4fbd-b7f8-156639e077f2) and posts a notice on the Sky Forum.

###### A.6.1.1.1.3.1.3.4.2 - Application Requirements [Core]  <!-- UUID: 1bc894fc-f8d1-450b-9829-15a4a5b707c3 -->

Prospective Delegates must submit (i) identity & contact info, (ii) delegate wallet address, and (iii) a signed statement accepting the responsibilities in [A.6.1.1.1.3.1.3.3 - Delegate Responsibilities](f230ba4e-eb5a-444e-b07a-13a0292338bd). These requirements are further specified in the subdocuments herein.

###### A.6.1.1.1.3.1.3.4.2.1 - Requirement To Verify Identity [Core]  <!-- UUID: 2d7744d1-80ca-41b8-af6b-79d7ae3e89bd -->

Every prospective Delegate must complete an initial, confidential identity verification process with the Spark Foundation, subject to additional KYC verification as necessary in the future. Delegates may remain anonymous or pseudonymous to the public.

###### A.6.1.1.1.3.1.3.4.2.2 - Conflict-of-Interest Disclosure [Core]  <!-- UUID: d27d5d53-9ebc-45af-a755-f83e03dccdf7 -->

At onboarding, prospective Delegates must provide any known conflicts of interest to the Spark Foundation. Disclosures must be updated as new conflicts arise.

###### A.6.1.1.1.3.1.3.4.2.3 - Eligibility [Core]  <!-- UUID: 912f59c2-7aea-4ce6-b3ee-137102fc80b7 -->

Individuals or entities listed on any international sanctions list are ineligible to serve as Delegates. In addition, a prospective Delegate may be deemed ineligible if, in the Spark Foundation’s sole discretion, their participation would be unlawful or would pose undue risk to Spark.

###### A.6.1.1.1.3.1.3.4.2.4 - Ongoing Compliance [Core]  <!-- UUID: 88f9aebd-8182-41be-ab0f-1003188bfad9 -->

Delegates must promptly update the Spark Foundation on any material change in their legal status. Failure to do so results in automatic suspension until rectified.

###### A.6.1.1.1.3.1.3.4.2.5 - Grounds for Disqualification [Core]  <!-- UUID: 1b98f386-689d-4935-a994-46c598415c23 -->

Submission of fraudulent information, criminal indictment for financial crime, or repeated governance negligence (see [A.6.1.1.1.3.1.3.5.2 - Non-Performance Removal](ca90a844-23e2-4741-aa76-97dd1092370d)) triggers an SRC-initiated Delegate Removal vote.

###### A.6.1.1.1.3.1.3.4.2.6 - Application Does Not Guarantee Acceptance [Core]  <!-- UUID: 6dd2ed9e-7b1a-4b03-901f-51d29c19e8a4 -->

Submission of a Delegate Application does not guarantee acceptance. Acceptance is at the Spark Foundation's sole discretion. The Spark Foundation may approve or deny any application at any time, for any reason or no stated reason including legal, sanctions, risk, operational, or capacity considerations even if the applicant satisfies the minimum requirements in [A.6.1.1.1.3.1.3.4.2 - Application Requirements](1bc894fc-f8d1-450b-9829-15a4a5b707c3). The Spark Foundation is not required to provide individualized rationale. Decisions are final unless otherwise provided in this Artifact.

###### A.6.1.1.1.3.1.3.4.3 - Minimum Term [Core]  <!-- UUID: c612d4e4-96c4-4ccf-a830-7f742338cfd9 -->

Effective upon approval of this proposal, Delegates are appointed by the Spark Foundation to fixed six (6) month terms aligned to calendar half-years (January 1–June 30; July 1–December 31). To continue beyond a term, a Delegate must be re-approved by the Spark Foundation prior to term end; absent re-approval, the Delegate is automatically offboarded at term end pursuant to [A.6.1.1.1.3.1.3.5.5 - Term-End Automatic Offboarding](02deeacc-5305-4a08-a5aa-2aabeb5591be).

Transition. Delegates serving prior to approval are automatically rolled over into this structure and deemed approved through June 30, 2026. For the avoidance of doubt, there will be no re-approval on January 1, 2026; the first re-approval checkpoint is July 1, 2026 for all such Delegates.

###### A.6.1.1.1.3.1.3.4.4 - Delegate Record [Core]  <!-- UUID: 708a614c-115e-470c-b076-52834422ebc9 -->

Accepted Delegates are appended to [A.6.1.1.1.3.1.3.8 - Registry of Delegates](f49a1e26-f774-4fbd-b7f8-156639e077f2).

##### A.6.1.1.1.3.1.3.5 - Delegate Offboarding [Core]  <!-- UUID: b49d9086-cb8a-43f7-a024-0d3320eae317 -->

The delegation offboarding process is specified in the subdocuments herein.

###### A.6.1.1.1.3.1.3.5.1 - Voluntary Offboarding [Core]  <!-- UUID: 8606cdec-f7c2-44af-befb-c702d2ed4735 -->

A Delegate can voluntarily offboard by submitting a resignation message in the Spark Prime category of Sky Forum with a signed message from their Delegate wallet as proof. The offboarding takes effect immediately after all active proposals conclude.

###### A.6.1.1.1.3.1.3.5.2 - Non-Performance Removal [Core]  <!-- UUID: ca90a844-23e2-4741-aa76-97dd1092370d -->

A Delegate is automatically offboarded if they:

- Fail to vote on ≥ 3 proposals in a row; or
- Maintain a voting percentage less than 85%.

###### A.6.1.1.1.3.1.3.5.3 - Emergency Removal [Core]  <!-- UUID: b016a208-3fce-4429-aea8-381fe6d4fb28 -->

The Spark Risk Council can immediately offboard a delegate if they:

- Breach disclosure / conflict-of-interest duties;
- Engage in malicious or negligent conduct; or
- Fail to provide acceptable KYC or updated KYC when requested.

###### A.6.1.1.1.3.1.3.5.4 - Updating of Status [Core]  <!-- UUID: a80aee08-2be5-419f-999c-44749fcf6a18 -->

Upon offboarding, the Delegate’s status in [A.6.1.1.1.3.1.3.8 - Registry of Delegates](f49a1e26-f774-4fbd-b7f8-156639e077f2) is updated to Inactive. SPK delegators must manually revoke their delegations and redelegate if they wish to continue participating in Spark governance.

###### A.6.1.1.1.3.1.3.5.5 - Term-End Automatic Offboarding [Core]  <!-- UUID: 02deeacc-5305-4a08-a5aa-2aabeb5591be -->

At the end of a Delegate's six (6) month term (see [A.6.1.1.1.3.1.3.4.3 - Minimum Term](c612d4e4-96c4-4ccf-a830-7f742338cfd9)), if the Spark Foundation has not recorded a re-approval, the Delegate is automatically offboarded effective 00:00 UTC on the day after term end. The Operational Facilitator updates the Registry and posts a notice on the Sky Forum.

##### A.6.1.1.1.3.1.3.6 - Incentives & Compensation [Core]  <!-- UUID: 5e38acbd-f010-4bd1-af6c-acdd17b3e9e9 -->

Delegates are compensated for their service as follows:

1. Compensation Amount. Active Delegates receive USD 4,000 per calendar month.
2. Administration. The Spark Foundation administers compensation from its approved operating budget.
3. Timing & Proration. The compensation structure goes into effect by December 1st 2025, with first payment being made January 2026. Payment is made monthly in arrears and prorated for partial months of service.
4. Eligibility & Clawback. Payment requires the Delegate to be in good standing and to have met responsibilities in [A.6.1.1.1.3.1.3.3 - Delegate Responsibilities](f230ba4e-eb5a-444e-b07a-13a0292338bd) during the covered period; the Spark Foundation may withhold or claw back amounts for non-performance or breach.
5. No Waiver of Oversight. Compensation does not limit or waive any onboarding, renewal, or offboarding requirements.

##### A.6.1.1.1.3.1.3.7 - Security Requirements & Compromise Procedure [Core]  <!-- UUID: 8ab7950c-c347-41a1-bf53-ef4d77000af5 -->

The security requirements and procedure for a compromised key are specified in the subdocuments herein.

###### A.6.1.1.1.3.1.3.7.1 - Operational Security [Core]  <!-- UUID: b5d668cd-5f19-4660-8846-8293126c5a57 -->

Delegates must:

- Sign votes from a hardware wallet or an equivalent secure device.
- Use unique signing keys that are never reused for personal transactions.
- Enable Multi-Factor Authentication on any platform accounts used for governance communication.

###### A.6.1.1.1.3.1.3.7.2 - Compromised Key Response [Core]  <!-- UUID: 05dbbbcc-7702-4d17-a222-9c93356be7cd -->

If a Delegate suspects key compromise, the following steps must be taken:

- The Delegate must notify the SRC as soon as the breach is discovered.
- SRC flags the Delegate in Registry of Delegates as "Suspended - Security Review" and notifies the governance community on the Sky Forum. All voting power to the suspended address is annulled.
- The Delegate may submit a new verified address; upon SRC approval, suspensions are lifted and delegations migrate at the next snapshot-block.

###### A.6.1.1.1.3.1.3.7.3 - Non-Compliance [Core]  <!-- UUID: e66be018-f2f2-4294-9357-be8ee6484e6c -->

Failure to execute the steps in [A.6.1.1.1.3.1.3.7.2 - Compromised Key Response](05dbbbcc-7702-4d17-a222-9c93356be7cd) within 48 hours constitutes grounds for emergency removal.

##### A.6.1.1.1.3.1.3.8 - Registry of Delegates [Core]  <!-- UUID: f49a1e26-f774-4fbd-b7f8-156639e077f2 -->

The subdocuments herein list each active Delegate’s name, wallet address, effective date, and status. Entries are maintained via an Active Data document updated by the Operational Facilitator.

###### A.6.1.1.1.3.1.3.8.1 - Template Information For Each Delegate [Core]  <!-- UUID: 6067e262-d4c3-40ee-af02-f3c69bf19b2f -->

The list of Delegates must follow this template for each recorded Delegate:

[Insert Delegate Handle]

- Delegate Name: [Insert Handle]
- Delegate Wallet Address:
- Effective Date:
- Status: Active/Inactive/Suspended

###### A.6.1.1.1.3.1.3.8.2 - Updating List of Delegates [Active Data Controller]  <!-- UUID: 7802904e-51fd-4308-ae9f-5f4595eca3e5 -->

The list of Delegates is defined as Active Data in [A.6.1.1.1.3.1.3.8.2.0.6.1 - List of Delegates](daa90217-00f4-4579-bc6d-cacb6afc70dc).

The Active Data is updated as follows:

- Responsible Party: Operational Facilitator.
- Trigger: Receipt of onboarding, renewal/re-approval, term-end automatic offboarding, or discretionary offboarding notice from the Spark Foundation.
- Update Process: Direct Edit.
- Publication: The Operational Facilitator posts a notice on the Sky Forum.

###### A.6.1.1.1.3.1.3.8.2.0.6.1 - List of Delegates [Active Data]  <!-- UUID: daa90217-00f4-4579-bc6d-cacb6afc70dc -->

The information for each Delegate is listed below:

- Remi
    - Delegate Name: Remi
    - Delegate Wallet Address: `0xDC5D4228a42880F5bbd577A184035503Bd55799a`
    - Effective Date: 2025-08-21
    - Current Term: 2026-07-01 to 2026-12-31
    - Status: Active
- NeoNode
    - Delegate Name: NeoNode
    - Delegate Wallet Address: `0x71faa03C0cEbCbB53236763B6b118aD906d9F6d3`
    - Effective Date: 2025-08-21
    - Current Term: 2026-07-01 to 2026-12-31
    - Status: Active
- TheMoon
    - Delegate Name: TheMoon
    - Delegate Wallet Address: `0xF80A26ee68Bdf0224c18F85876b20858ee5206A9`
    - Effective Date: 2026-01-14
    - Current Term: 2026-07-01 to 2026-12-31
    - Status: Active

##### A.6.1.1.1.3.1.3.9 - Subject to Change [Core]  <!-- UUID: 57f6f628-dfc3-4819-8265-c85a38c0fc9f -->

Spark reserves the right to vary or amend these terms at its discretion, subject to established Spark Artifact governance procedures related to Artifact edits.

#### A.6.1.1.1.3.1.4 - Spark Risk Council [Core]  <!-- UUID: cf019fb3-d792-4867-abf7-cfe4d0b73e5d -->

The documents herein define the Spark Risk Council (SRC). The SRC safeguards the integrity and security of the Spark Ecosystem by conducting pre-vote risk reviews and, where necessary, preventing proposals from proceeding to a vote in order to protect Spark.

##### A.6.1.1.1.3.1.4.1 - Purpose And Mandate [Core]  <!-- UUID: b2a23ffe-34db-4793-87fd-a9fec45a5a35 -->

The SRC identifies, assesses, and mitigates technical, economic, and governance-process risks posed by proposals subject to Spark Governance. The SRC’s mandate is to inform the community of potential risks inherent in proposals and, where necessary, prevent proposals from proceeding that are malicious or likely to expose Spark to substantial, unreasonable risk.

##### A.6.1.1.1.3.1.4.2 - Scope Of Review [Core]  <!-- UUID: b269ffa9-8abc-4b02-ba54-ecfde4d30549 -->

The SRC reviews proposals for (i) security vulnerabilities and operational attack surface, (ii) market and treasury risks, (iii) economic risk, and (iv) misalignment with the Sky Core Atlas or the Spark Artifact. The SRC’s authority is limited to reviewing proposals within this scope.

##### A.6.1.1.1.3.1.4.3 - SRC Risk Review Process [Core]  <!-- UUID: c586a7cc-a4d0-4c9b-9578-cbfe1f99a20e -->

The subdocuments herein clarify the process of the SRC independent risk review in terms of new Root Edit proposals. See [A.6.1.1.1.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](c9f7cc6e-0548-4599-9f9d-bfa1d2bb7577).

###### A.6.1.1.1.3.1.4.3.1 - SRC Risk Review [Core]  <!-- UUID: 968b4807-8032-42a3-b09d-f787cdb4ef87 -->

Within seven (7) days (based on the start of the weekly cycle) of a new Atlas Root Edit proposal, the SRC must conduct an independent risk review and post (i) a conclusion ("Passed SRC Review," or "Failed SRC Review") and (ii) a stand-alone risk analysis to the relevant forum thread. Details for each of these deliverables are set out in the subdocuments herein.

###### A.6.1.1.1.3.1.4.3.1.1 - SRC Risk Review Conclusion [Core]  <!-- UUID: e468575b-bb18-475c-aa82-7f7e9e80a576 -->

The SRC conclusion must reflect the majority opinion of SRC members. However, individual SRC members are free to post dissenting or concurring opinions at their discretion. See [A.6.1.1.1.3.1.4.9.1 - Concurring Or Dissenting Opinions](fef5a280-76c8-402b-bbeb-7c6ca4fab0d5).

###### A.6.1.1.1.3.1.4.3.1.2 - SRC Risk Analysis [Core]  <!-- UUID: 6c82172a-bd7d-4aa7-8ff9-771cf166707b -->

The SRC risk analysis must summarize key findings, assumptions, mitigations, and any monitoring plan.

###### A.6.1.1.1.3.1.4.3.2 - SRC Risk Review Extension [Core]  <!-- UUID: b67605fd-a381-4299-aac9-4e6ef1d54386 -->

The SRC can formally request, at the Operational Facilitator’s discretion, an extension of the deadline of seven (7) days by posting a public justification for an extension in the Sky Forum.

###### A.6.1.1.1.3.1.4.3.3 - Failure To Review [Core]  <!-- UUID: f55b35ba-1013-4a86-a874-feda7d750e45 -->

If no SRC conclusion or request for extension is posted within seven (7) days of submission, the Operational Facilitator will move the proposal to the Snapshot voting phase, provided the proposal is aligned with the Sky Core Atlas and the Spark Artifact.

##### A.6.1.1.1.3.1.4.4 - “Failed SRC Review” Authority and Procedure [Core]  <!-- UUID: ac9d89b5-7a07-4b95-8597-6644bc4029ab -->

The subdocuments herein set out the threshold, process and implications of a "Failed SRC Review" determination by the SRC.

###### A.6.1.1.1.3.1.4.4.1 - Standard [Core]  <!-- UUID: 85633365-939a-44c4-8a55-aa17fa4a7809 -->

A determination of "Failed SRC Review" may be exercised when a proposal is determined to be:

- malicious or exploitative;
- procedurally non-compliant with the Sky Core Atlas or Spark Artifact;
- likely to expose Spark to substantial, unreasonable risk; or
- in need of revisions in order for the SRC to evaluate the proposal.

###### A.6.1.1.1.3.1.4.4.2 - Threshold [Core]  <!-- UUID: 0d0a0212-4439-4fb3-a8b2-77e53a1d60db -->

A determination of "Failed SRC Review" must reflect the majority opinion of SRC members.

###### A.6.1.1.1.3.1.4.4.3 - Failed SRC Review Notice [Core]  <!-- UUID: 8be65dbb-1cba-453b-a2cf-d37e8a1f0b42 -->

A "Failed SRC Review" notice must be posted on the Sky Forum in the relevant thread prior to the Snapshot voting window opening (or, if already posted, prior to closure).

###### A.6.1.1.1.3.1.4.4.4 - Operational Facilitator Designation [Core]  <!-- UUID: bca3632c-eb40-4256-a430-51252f00f0e0 -->

The Operational Facilitator marks the proposal "Failed SRC Review."

###### A.6.1.1.1.3.1.4.4.5 - Effect [Core]  <!-- UUID: 1a81ade4-dc44-4272-adda-b2c3bbfc8554 -->

The proposal does not proceed to Snapshot (or is withdrawn).

##### A.6.1.1.1.3.1.4.5 - Composition, Tenure, And Due Diligence [Core]  <!-- UUID: e8b3fdc4-8e46-47b8-b2d3-3775b4436d21 -->

The subdocuments herein set out key details about the SRC, including their composition and appointment.

###### A.6.1.1.1.3.1.4.5.1 - Expertise [Core]  <!-- UUID: bb276783-cf71-46a8-84f5-f85e99a25c97 -->

SRC members shall be domain experts across security, risk/economics, and operations.

###### A.6.1.1.1.3.1.4.5.2 - Seat Count [Core]  <!-- UUID: f9b6eb2f-ae02-4870-9470-be8065f7d90f -->

The SRC will have a seat count of three (3).

###### A.6.1.1.1.3.1.4.5.3 - Bootstrapping Phase [Core]  <!-- UUID: 83e078f3-b7a3-443c-b3fe-694b6806a999 -->

During the bootstrapping phase, initial members are appointed directly by the Operational Facilitator in consultation with the Spark Foundation through a public announcement on the Sky Forum. The Operational Facilitator shall either reappoint current SRC members to their seats or appoint new members in consultation with and with the consent of the Spark Foundation on an as-needed basis to allow the Operational Facilitator and the Spark Foundation flexibility during the initial governance procedures.

Additional procedures on future elections governing the appointment of SRC members voted upon by the community will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.1.3.1.4.5.4 - Coordinator [Core]  <!-- UUID: 5350be2f-636a-47a5-aad3-071275bcc473 -->

The Nested Contributor Phoenix Labs has a seat on the SRC as a non-voting coordinating member. The role of the coordinator is to facilitate the work of the SRC being done in a timely manner.

###### A.6.1.1.1.3.1.4.5.5 - Due Diligence [Core]  <!-- UUID: b97dbb58-676c-434f-8973-2080102660c2 -->

Members may be required to complete a confidential due diligence process, if the Spark Foundation deems it necessary.

##### A.6.1.1.1.3.1.4.6 - Compensation [Core]  <!-- UUID: 3dddde86-989d-44ea-a2f4-7a1c26f9c844 -->

SRC members will receive compensation for performing their role on terms approved by the Spark Foundation.

##### A.6.1.1.1.3.1.4.7 - Council Meetings [Core]  <!-- UUID: 3c6ed2b0-8ae1-4e3f-8f64-04ce2ae64e57 -->

The subdocuments herein set out details about SRC meetings, including cadence and external participation.

###### A.6.1.1.1.3.1.4.7.1 - Cadence [Core]  <!-- UUID: ea7b0884-c4f8-4272-af38-cdda387bb65f -->

The SRC shall hold a monthly internal governance meeting.

###### A.6.1.1.1.3.1.4.7.2 - Participants [Core]  <!-- UUID: 440d1f15-915b-45b8-9bec-1ca5e32ea036 -->

In addition to SRC members, representatives of the Spark Foundation, Nested Contributor Phoenix Labs, and the Operational Facilitator are each permitted to attend in a coordinating and facilitating capacity.

##### A.6.1.1.1.3.1.4.8 - Mid-Term Appointments And Member Changes [Core]  <!-- UUID: c139606c-f594-4dba-9afe-a32e2a2c64a1 -->

The subdocuments herein set out the process for mid-term appointments and other out-of-schedule replacement rules.

###### A.6.1.1.1.3.1.4.8.1 - Vacancies Mid-Term (Out-Of-Schedule Replacement Appointment) [Core]  <!-- UUID: 123b69dc-c3ef-4143-b66a-485a2d526b1c -->

If a seat becomes vacant (resignation, removal, ineligibility, or failure to complete due diligence), the Operational Facilitator shall make an out-of-schedule replacement appointment. This process is defined in the subdocuments herein.

###### A.6.1.1.1.3.1.4.8.1.1 - Notice [Core]  <!-- UUID: b7390f2a-9d24-4f1a-ac04-0db841a1bcd5 -->

Within seven (7) days of the vacancy, the Operational Facilitator publishes a vacancy notice and forum thread on the Sky Forum describing the circumstances of the vacancy.

###### A.6.1.1.1.3.1.4.8.1.2 - Appointment [Core]  <!-- UUID: aa27264b-865b-47bd-8de5-0731c772dae1 -->

The Operational Facilitator shall appoint a replacement member of the SRC to fill the vacant seat in consultation with the Spark Foundation and publish a new post in the relevant forum thread in order to announce the appointment.

###### A.6.1.1.1.3.1.4.8.1.3 - Term [Core]  <!-- UUID: c7e40d3d-5485-426c-944a-16291fb36674 -->

The appointee is seated upon due diligence completion to the Spark Foundation’s satisfaction and update to the SRC Membership Registry and serves the remainder of the current term.

###### A.6.1.1.1.3.1.4.8.1.4 - Seating And Continuity [Core]  <!-- UUID: 27bb6f28-1021-4c68-b435-36f32ce72bfa -->

Incumbent SRC members remain in office until successors are seated to ensure continuity of SRC operations. Newly appointed members are seated upon completion of due diligence to the Spark Foundation’s satisfaction and publication to the SRC Membership Registry.

##### A.6.1.1.1.3.1.4.9 - Process Requirements [Core]  <!-- UUID: c1304ded-6912-472a-b836-cd7092262434 -->

The subdocuments herein set out key deliverables for the SRC as well as rules around conflicts of interest.

###### A.6.1.1.1.3.1.4.9.1 - Concurring Or Dissenting Opinions [Core]  <!-- UUID: fef5a280-76c8-402b-bbeb-7c6ca4fab0d5 -->

In addition to the determinative independent risk review posted by the SRC for each proposal, individual SRC members may post concurring or dissenting opinions in the Sky Forum at their discretion.

###### A.6.1.1.1.3.1.4.9.2 - Conflicts Of Interest [Core]  <!-- UUID: 20d7297d-b100-438d-a535-6b9968b2bb43 -->

SRC members must disclose conflicts of interest to Spark Foundation and recuse themselves where impartiality is compromised.

##### A.6.1.1.1.3.1.4.10 - Non-Performance [Core]  <!-- UUID: 4a07187f-9fc2-4a70-ae4b-919a4f52467d -->

Repeated failure to meet review timelines; failure to document decisions; blocking valid proposals due to malicious intent or evident poor due diligence; or any other failure to uphold the duties of the SRC set forth in the Spark Artifact may trigger removal and replacement of SRC members at the discretion of the Spark Foundation.

##### A.6.1.1.1.3.1.4.11 - SRC Membership Registry Process [Core]  <!-- UUID: dc208bb2-ffb4-4a2a-b561-d563bc52eb14 -->

The subdocuments herein contain the registry of SRC members, including name or alias, domain expertise, verified governance address, start date, term status, and standing (Active / Recused / Removed). The registry is maintained via an Active Data document updated by the Operational Facilitator per the subdocuments herein.

###### A.6.1.1.1.3.1.4.11.1 - Updating SRC Membership Registry [Active Data Controller]  <!-- UUID: 066783d5-c191-4db7-a38a-5370a75944ee -->

The SRC Membership Registry is defined as Active Data in [A.6.1.1.1.3.1.4.11.1.0.6.1 - SRC Membership Registry List](d9c6ed16-5b0d-4a6f-bb43-387398090afc).

The Active Data is updated as follows:

- The Responsible Party is the Operational Facilitator.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.1.3.1.4.11.1.0.6.1 - SRC Membership Registry List [Active Data]  <!-- UUID: d9c6ed16-5b0d-4a6f-bb43-387398090afc -->

The information for each member of the SRC is listed below:

| Name or Alias        | Domain Expertise | Verified Governance Address | Start Date  | Term Status  | Standing |
|----------------------|------------------|-----------------------------|-------------|--------------|----------|
| Blockworks Advisory  | Risk             | N/A                         | 2025-10-03  | Active Term  | Active   |
| L2 Beat              | Risk             | N/A                         | 2025-10-03  | Active Term  | Active   |
| Aragon               | Risk             | N/A                         | 2025-10-03  | Active Term  | Active   |

#### A.6.1.1.1.3.1.5 - Sky Ecosystem Emergency Response [Core]  <!-- UUID: 0483b49d-b074-4a98-bb4b-bc5d222dabf1 -->

The documents herein specify Spark’s emergency response protocol in situations that impact the entire Sky Ecosystem. This protocol will be specified in a future iteration of the Spark Artifact.

#### A.6.1.1.1.3.1.6 - Agent-Specific Emergency Response [Core]  <!-- UUID: 2d540356-97e0-431b-a03b-c3ec360e139b -->

The documents herein specify Spark’s emergency response protocol in situations solely impacting Spark versus the broader Sky Ecosystem. This protocol will be specified in a future iteration of the Spark Artifact.

### A.6.1.1.1.3.2 - Management Of Infrastructure Inherited From Sky Core [Core]  <!-- UUID: fd2f8da1-616b-4c4f-9d6e-bdd14131eca4 -->

The documents herein specify Spark's strategy and operational processes for managing infrastructure inherited from Sky Core.

#### A.6.1.1.1.3.2.1 - SparkLend [Core]  <!-- UUID: d9ff0cd2-8999-4d3d-9670-2c7b49c1fe51 -->

The documents herein define the parameters and operational processes related to SparkLend. Control of SparkLend is being transitioned to Spark.

##### A.6.1.1.1.3.2.1.1 - Parameters [Core]  <!-- UUID: a15a6203-23b1-4921-8bdb-fe0ef6013bf6 -->

The parameters of SparkLend are specified in the subdocuments herein.

###### A.6.1.1.1.3.2.1.1.1 - SparkLend Risk Parameters Definitions [Core]  <!-- UUID: 667abf8c-64a3-4029-b218-e7a6e7000bbd -->

The subdocuments herein provide definitions of the SparkLend risk parameters.

###### A.6.1.1.1.3.2.1.1.1.1 - Borrow Rate Definition [Core]  <!-- UUID: b93bf576-6972-48b6-8847-5988b094e325 -->

The borrow rate is the annualized percentage yield for borrowing the asset, which is determined based on the market’s Interest Rate Model and actual utilization in the market.

###### A.6.1.1.1.3.2.1.1.1.2 - Supply Rate Definition [Core]  <!-- UUID: 5c4963af-872c-45b9-ac39-fda5ac4f43a1 -->

The supply rate is the annualized percentage yield for supplying the asset, which is determined based on borrow rate as:
supply rate = market utilization * borrow rate * (1-reserve factor)

###### A.6.1.1.1.3.2.1.1.1.3 - Interest Rate Model Definition [Core]  <!-- UUID: 9006fd8d-bd13-48fc-bf2f-04f47579b3b0 -->

The Interest Rate Model ("IRM") is defined by four main parameters:

1. Base Rate - the starting rate at 0% utilization,
2. Variable Slope 1 - the rate at optimal utilization,
3. Variable Slope 2 - the rate at 100% utilization,
4. Utilization - the utilization itself.

The Base Rate, Slope 1, and Slope 2 parameters are further defined in: [A.6.1.1.1.3.2.1.1.1.13 - Base Rate Definition](9372deb9-5115-4010-bf72-34023b846525); [A.6.1.1.1.3.2.1.1.1.15 - Slope 1 Definition](c16b2b24-d663-4877-8bb3-cbd32e977360); and [A.6.1.1.1.3.2.1.1.1.17 - Slope 2 Definition](56bc7808-5ef8-42af-ba17-708b995194cc).

All markets except Dai use this IRM. The IRM for Dai is independent of utilization and is defined as a spread over the Sky Savings Rate set forth in [A.3.1.2.2 - Sky Savings Rate](2674cccb-d779-4868-b83f-8cb86648c88a). The spread is determined by the Core Facilitator, in consultation with the Core Council Risk Advisor.

###### A.6.1.1.1.3.2.1.1.1.4 - LTV Definition [Core]  <!-- UUID: 586478a3-51cb-4a2e-8bb1-b96e6520fdcc -->

The LTV is the maximum percentage of the value of collateral that borrowers can borrow against their collateral.

###### A.6.1.1.1.3.2.1.1.1.5 - Liquidation Threshold Definition [Core]  <!-- UUID: 2dd2045c-6a33-4229-b6c8-e531d6ecd27a -->

The liquidation threshold is the maximum debt a borrower can owe as a percentage of their collateral before their position is considered under-collateralized and thus at risk of being liquidated.

###### A.6.1.1.1.3.2.1.1.1.6 - High Efficiency Mode Category Definition [Core]  <!-- UUID: 49159478-90c9-4200-ab33-277a70b924d6 -->

The High Efficiency Mode Category groups assets that are highly correlated with each other into buckets, for example Stablecoins or various forms of ETH. Borrowing against an asset to acquire another asset in the same category can support higher LTVs and liquidation thresholds as determined by the protocol.

###### A.6.1.1.1.3.2.1.1.1.7 - Liquidation Bonus Definition [Core]  <!-- UUID: 173ff961-bf1f-4c6c-992c-4a67b269e544 -->

The liquidation bonus is the bonus for liquidating an unhealthy loan, or equivalently the penalty for having an unhealthy loan liquidated. The party paying off the unhealthy loan is entitled to collateral with an equivalent value as the debt paid off plus the liquidation bonus.

###### A.6.1.1.1.3.2.1.1.1.8 - Reserve Factor Definition [Core]  <!-- UUID: a68d2ffe-e541-4754-b11e-6cafe7b4ae5c -->

The reserve factor is the percentage of interest payments paid to the protocol.

###### A.6.1.1.1.3.2.1.1.1.9 - Supply Cap Definition [Core]  <!-- UUID: e222b8da-abda-42f5-8106-20c6f2881dc7 -->

The supply cap is the maximum amount of the asset that can be supplied.

###### A.6.1.1.1.3.2.1.1.1.10 - Borrow Cap Definition [Core]  <!-- UUID: a2d6a99e-c63a-4f30-87f3-a3d66b1eda92 -->

The borrow cap is the maximum amount of the asset that can be borrowed.

###### A.6.1.1.1.3.2.1.1.1.11 - Optimal Utilization Definition [Core]  <!-- UUID: a6677e8a-7ef1-460b-a5cd-5411319bf2c0 -->

The optimal utilization represents the desired target utilization of the borrowing capacity for the asset. It is an input used to determine the interest rate of borrowing. When the actual utilization is above the optimal utilization, borrowing rates will be higher; and when the actual utilization is below the optimal utilization, borrowing rates will be lower.

###### A.6.1.1.1.3.2.1.1.1.12 - Isolated Debt Ceiling Definition [Core]  <!-- UUID: ccb5b20f-8fe0-487c-9d61-d038c87e04f0 -->

The isolated debt ceiling represents the maximum amount that can be borrowed against designated isolated assets, as determined by the Core Facilitator in consultation with the Core Council Risk Advisor. Only Stablecoins may be borrowed against isolated assets.

###### A.6.1.1.1.3.2.1.1.1.13 - Base Rate Definition [Core]  <!-- UUID: 9372deb9-5115-4010-bf72-34023b846525 -->

The base rate is an input used to determine the interest rate of borrowing. The base rate is adjusted based on actual borrowing utilization relative to optimal borrowing utilization to arrive at the actual borrowing rate.

###### A.6.1.1.1.3.2.1.1.1.14 - Reserve State Definition [Core]  <!-- UUID: d6b75f49-ca6b-49ef-923f-1a8d452abaf2 -->

The reserve state represents the state of the market for a particular collateral type. The reserve state may be:

- Active - all activities may occur
- Frozen - all activities may occur except for supplying and borrowing
- Paused - no activities may occur

###### A.6.1.1.1.3.2.1.1.1.15 - Slope 1 Definition [Core]  <!-- UUID: c16b2b24-d663-4877-8bb3-cbd32e977360 -->

Slope 1 is the interest rate at optimal utilization in the Interest Rate Model.

###### A.6.1.1.1.3.2.1.1.1.16 - Slope 1 Spread Definition [Core]  <!-- UUID: a868bb67-36e5-44e5-b852-62f23c1c8ec4 -->

The Slope 1 Spread is the difference between the WETH interest rate at optimal utilization in the Interest Rate Model and the staking yield on stETH. The Slope 1 Spread Parameter is only defined for WETH.

###### A.6.1.1.1.3.2.1.1.1.17 - Slope 2 Definition [Core]  <!-- UUID: 56bc7808-5ef8-42af-ba17-708b995194cc -->

Slope 2 is the interest rate at 100% utilization in the Interest Rate Model.

###### A.6.1.1.1.3.2.1.1.1.18 - Collateral-Enabled Definition [Core]  <!-- UUID: f0f7d864-7f68-4727-8c20-9d261dfd63eb -->

If Collateral is Enabled, then the asset may be used as collateral.

###### A.6.1.1.1.3.2.1.1.1.19 - Borrowing-Enabled Definition [Core]  <!-- UUID: 2ec70ad1-f979-4a4a-bce2-cd070e9e283f -->

If Borrowing is Enabled, then the asset may be borrowed.

###### A.6.1.1.1.3.2.1.1.1.20 - Isolated Collateral-Enabled Definition [Core]  <!-- UUID: 7dfd4e6f-7b62-42a5-9ff1-7326bdc979bb -->

If Isolated Collateral is Enabled, only Stablecoins can be borrowed when using the asset as collateral.

###### A.6.1.1.1.3.2.1.1.1.21 - Isolation Mode Definition [Core]  <!-- UUID: 6e0c4a4d-c6b0-4c41-b6ac-747a90707fdb -->

When a user is in Isolation Mode, only assets with Isolated Borrow enabled can be borrowed.

###### A.6.1.1.1.3.2.1.1.1.21.0.3.1 - Isolated Borrow - Element Annotation [Annotation]  <!-- UUID: eb779cd6-adeb-490e-b67d-d0854b7a844c -->

"Isolated Borrow" specifies whether an asset can be borrowed when a user is in Isolation Mode on the SparkLend platform.

###### A.6.1.1.1.3.2.1.1.1.22 - Siloed Borrowing-Enabled Definition [Core]  <!-- UUID: f6764325-46d2-4fe4-872e-6e89a1914a5d -->

If Siloed Borrowing is Enabled, then when borrowing the asset, no other asset may be borrowed.

###### A.6.1.1.1.3.2.1.1.1.23 - Flash Loan Enabled Definition [Core]  <!-- UUID: 17d352ee-a54b-43e5-92ee-224a1193c7ee -->

If the Flash Loan Enabled parameter is activated, then the asset may be borrowed using a flash loan.

###### A.6.1.1.1.3.2.1.1.1.24 - Total Flash Loan Fee Definition [Core]  <!-- UUID: 250bb1bd-128b-48d2-aa56-53006dab795e -->

The Total Flash Loan Fee incorporates a fee paid to the protocol and a fee paid to liquidity providers. This total fee is calculated as a percentage of the flash loan amount. Of the Total Flash Loan Fee, the Protocol Flash Loan Fee is paid to the protocol, with the remainder paid to liquidity providers.

The Total Flash Loan Fee is set on a protocol level, regardless of what assets are being borrowed.

###### A.6.1.1.1.3.2.1.1.1.25 - Protocol Flash Loan Fee Definition [Core]  <!-- UUID: 638d0e6b-8d6a-48e9-9bf9-e8ee201e0e97 -->

The Protocol Flash Loan Fee is the fee for a flash loan paid to the protocol as a percentage of the flash loan amount.

The Protocol Flash Loan Fee is set on a protocol level, regardless of what assets are being borrowed.

###### A.6.1.1.1.3.2.1.1.2 - SparkLend Risk Parameters Current Configuration [Core]  <!-- UUID: cb959917-c29c-4d2f-b151-ded03618357c -->

The subdocuments herein define the current configuration of the SparkLend risk parameters.

###### A.6.1.1.1.3.2.1.1.2.1 - SparkLend Ethereum Risk Parameters [Core]  <!-- UUID: b370fb72-57f8-4cf1-aab9-597d08afe403 -->

The subdocuments herein define the current configuration of the SparkLend Ethereum risk parameters.

###### A.6.1.1.1.3.2.1.1.2.1.1 - GNO Risk Parameters [Core]  <!-- UUID: acd9d2a2-ff4f-44fc-a544-f4cc02262a5b -->

The current GNO risk parameters are:

- LTV: 0%
- Liquidation Threshold: 25%
- E-mode Category: N/A
- Liquidation Bonus: 10%
- Reserve Factor: 0%
- Supply Cap: N/A
- Borrow Cap: N/A
- Optimal Utilization: 100%
- Isolated Debt Ceiling: $5,000,000
- Base Rate: 1%
- Slope 1: 0%
- Slope 2: 0%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: Yes
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.1.2 - Dai Risk Parameters [Core]  <!-- UUID: 7d8ed55b-4aca-483b-af6d-24badb49d042 -->

The current Dai risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0.01%
- E-mode Category: N/A
- Liquidation Bonus: 4.5%
- Reserve Factor: 10%
- Supply Cap: N/A
- Borrow Cap: N/A
- Optimal Utilization: 80%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: SSR + 1.25%
- Slope 2: 15%
- Reserve State: Active
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: Yes
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

The Dai Borrow Rate is set through the Interest Rate Model as a spread over the Sky Savings Rate. The spread is set directly by the Core Facilitator in consultation with the Core Council Risk Advisor.

###### A.6.1.1.1.3.2.1.1.2.1.3 - USDS Risk Parameters [Core]  <!-- UUID: d9a146b8-f101-4cd6-916c-85142bb8deec -->

The current USDS risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0%
- E-mode Category: N/A
- Liquidation Bonus: 0%
- Reserve Factor: 10%
- Supply Cap: Unlimited
- Borrow Cap: Unlimited
- Optimal Utilization: 80%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: SSR + 1.25%
- Slope 2: 15%
- Reserve State: Active
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: Yes
- Siloed Borrowing: No
- Flash Loan Enabled: Yes.

The USDS Borrow Rate is set through the Interest Rate Model as a spread over the Sky Savings Rate. The spread is set directly by the Core Facilitator in consultation with the Core Council Risk Advisor.

###### A.6.1.1.1.3.2.1.1.2.1.4 - WETH Risk Parameters [Core]  <!-- UUID: b1a1fb8a-29d7-4bbd-8204-25c74263c25d -->

The current WETH risk parameters are:

- LTV: 85%
- Liquidation Threshold: 86%
- E-mode Category: ETH
- Liquidation Bonus: 5%
- Reserve Factor: 5%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 90%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: N/A
- Slope 1 Spread: -0.10%
- Slope 2: 75%
- Reserve State: Active
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

The Slope 1 parameter for WETH is calculated based on the following formula:

slope 1 = stETH yield + slope 1 spread - base rate

###### A.6.1.1.1.3.2.1.1.2.1.5 - USDT Risk Parameters [Core]  <!-- UUID: 4999a374-380b-4694-a67c-0fa471b4cf43 -->

The current USDT risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0%
- E-mode Category: USD
- Liquidation Bonus: 0%
- Reserve Factor: 1%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 95%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: SSR value + 0.5%
- Slope 2: 15%
- Reserve State: Active
- Collateral: No
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.1.6 - WBTC Risk Parameters [Core]  <!-- UUID: c3c3830f-4829-48fc-aced-30dcdd2a5ba7 -->

The current WBTC risk parameters are:

- LTV: 0%
- Liquidation Threshold: 35%
- E-mode Category: N/A
- Liquidation Bonus: 7%
- Reserve Factor: 20%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 60%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 2%
- Slope 2: 300%
- Reserve State: Active
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.1.7 - sDai Risk Parameters [Core]  <!-- UUID: 61c21da3-22ff-4dba-8736-4a9a8556a32b -->

The current sDai risk parameters are:

- LTV: 79%
- Liquidation Threshold: 80%
- E-mode Category: USD
- Liquidation Bonus: 5%
- Reserve Factor: 10%
- Supply Cap: Set by cap automator
- Borrow Cap: N/A
- Optimal Utilization: 100%
- Isolated Debt Ceiling: N/A
- Base Rate: 1%
- Slope 1: 0%
- Slope 2: 0%
- Reserve State: Active
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.1.8 - wstETH Risk Parameters [Core]  <!-- UUID: 5d721ab3-be87-4989-b4a2-b32ff38b912f -->

The current wstETH risk parameters are:

- LTV: 83%
- Liquidation Threshold: 84%
- E-mode Category: ETH
- Liquidation Bonus: 7%
- Reserve Factor: 30%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 70%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 2%
- Slope 2: 200%
- Reserve State: Active
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.1.9 - USDC Risk Parameters [Core]  <!-- UUID: d8242d1a-18f2-4000-a98b-0521486b0708 -->

The current USDC risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0%
- E-mode Category: USD
- Liquidation Bonus: 0%
- Reserve Factor: 1%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 98%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: SSR value + 1.00%
- Slope 2: 15%
- Reserve State: Active
- Collateral: No
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.1.10 - weETH Risk Parameters [Core]  <!-- UUID: 6ed18918-a695-44a6-82e7-547a3fbcafd3 -->

The current weETH risk parameters are:

- LTV: 79%
- Liquidation Threshold: 80%
- E-mode Category: N/A
- Liquidation Bonus: 10%
- Reserve Factor: 15%
- Supply Cap: Set by cap automator
- Borrow Cap: N/A
- Optimal Utilization: 45%
- Isolated Debt Ceiling: $200,000,000
- Base Rate: 5%
- Slope 1: 15%
- Slope 2: 300%
- Reserve State: Active
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: Yes
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.1.11 - rETH Risk Parameters [Core]  <!-- UUID: 9ef0bc64-db94-4d78-ac8b-cef71d28fedc -->

The current rETH risk parameters are:

- LTV: 0%
- Liquidation Threshold: 70%
- E-mode Category: ETH
- Liquidation Bonus: 7%
- Reserve Factor: 15%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 45%
- Isolated Debt Ceiling: N/A
- Base Rate: 0.25%
- Slope 1: 7%
- Slope 2: 300%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.1.12 - LBTC Risk Parameters [Core]  <!-- UUID: 37ff9748-6f72-4adf-af97-0f90cb7154b4 -->

The current LBTC risk parameters are:

- LTV: 74%
- Liquidation Threshold: 75%
- E-mode Category: 0
- Liquidation Bonus: 8%
- Reserve Factor: 15%
- Supply Cap: Set by cap automator
- Borrow Cap: 0
- Optimal Utilization: 45%
- Isolated Debt Ceiling: N/A
- Base Rate: 5%
- Slope 1: 15%
- Slope 2: 300%
- Reserve State: Active
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.1.13 - tBTC Risk Parameters [Core]  <!-- UUID: 17e2cc64-6172-48f8-a4f1-a2a7bc5edbbb -->

The current tBTC risk parameters are:

- LTV: 0%
- Liquidation Threshold: 70%
- E-mode Category: 0
- Liquidation Bonus: 8%
- Reserve Factor: 99%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 80%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 1%
- Slope 2: 300%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.1.14 - ezETH Risk Parameters [Core]  <!-- UUID: 51f3555b-57a3-4275-b462-a4ba85f3b8fe -->

The current ezETH risk parameters are:

- LTV: 0%
- Liquidation Threshold: 70%
- E-mode Category: 0
- Liquidation Bonus: 10%
- Reserve Factor: 15%
- Supply Cap: Set by cap automator
- Borrow Cap: 0
- Optimal Utilization: 45%
- Isolated Debt Ceiling: N/A
- Base Rate: 5%
- Slope 1: 15%
- Slope 2: 300%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.1.15 - rsETH Risk Parameters [Core]  <!-- UUID: 1da6ef90-fca2-4f72-9b8d-13a3786a3c1c -->

The current rsETH risk parameters are:

- LTV: 0%
- Liquidation Threshold: 70%
- E-mode Category: 0
- Liquidation Bonus: 10%
- Reserve Factor: 15%
- Supply Cap: Set by cap automator
- Borrow Cap: 0
- Optimal Utilization: 45%
- Isolated Debt Ceiling: N/A
- Base Rate: 5%
- Slope 1: 15%
- Slope 2: 300%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.1.16 - cbBTC Risk Parameters [Core]  <!-- UUID: 63038ac2-7666-40bb-ad9f-dba7c1a546b8 -->

The current cbBTC risk parameters are:

- LTV: 81%
- Liquidation Threshold: 82%
- E-mode Category: 0
- Liquidation Bonus: 8%
- Reserve Factor: 20%
- Supply Cap: 500 cbBTC
- Borrow Cap: 50 cbBTC
- Optimal Utilization: 80%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 1%
- Slope 2: 300%
- Reserve State: Active
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No

###### A.6.1.1.1.3.2.1.1.2.1.17 - sUSDS Risk Parameters [Core]  <!-- UUID: 1d7f757a-aabb-463d-9d3d-3f34f1c0656a -->

The current sUSDS risk parameters are:

- LTV: 79%
- Liquidation Threshold: 80%
- E-mode Category: USD
- Liquidation Bonus: 5%
- Reserve Factor: 10%
- Supply Cap: 50,000,000 sUSDS
- Borrow Cap: 0 sUSDS
- Optimal Utilization: 80%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 2%
- Slope 2: 300%
- Reserve State: Active
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No

###### A.6.1.1.1.3.2.1.1.2.1.18 - pyUSD Risk Parameters [Core]  <!-- UUID: 5e05e5d8-8477-460f-a197-4b49bfa8652f -->

The current pyUSD risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0%
- E-mode Category: USD
- Liquidation Bonus: 10%
- Reserve Factor: 10%
- Supply Cap: Set by cap automator
- Borrow Cap: Set by cap automator
- Optimal Utilization: 95%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: SSR + 1.5%
- Slope 2: 15%
- Reserve State: Active
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No

###### A.6.1.1.1.3.2.1.1.2.1.19 - Total Flash Loan Fee Current Value [Core]  <!-- UUID: fdd544f0-fa59-42f5-afb8-290cd812eb35 -->

The Total Flash Loan Fee is 0.00%.

###### A.6.1.1.1.3.2.1.1.2.1.20 - Protocol Flash Loan Fee Current Value [Core]  <!-- UUID: 086d81f6-e8e2-4693-996f-6ccb62ee362b -->

The Protocol Flash Loan Fee is 0.00%.

###### A.6.1.1.1.3.2.1.1.2.2 - SparkLend Gnosis Risk Parameters [Core]  <!-- UUID: 1ecdd683-0f6f-4bca-8f43-c2a458224404 -->

The subdocuments herein define the current configuration of the SparkLend Gnosis risk parameters.

###### A.6.1.1.1.3.2.1.1.2.2.1 - GNO Risk Parameters [Core]  <!-- UUID: aacc4fa0-3fd8-44f4-af79-7ec3d4128328 -->

The current GNO risk parameters are:

- LTV: 40%
- Liquidation Threshold: 50%
- E-mode Category: N/A
- Liquidation Bonus: 12%
- Reserve Factor: 50%
- Supply Cap: 100,000 GNO
- Borrow Cap: N/A
- Optimal Utilization: 80%
- Isolated Debt Ceiling: $1,000,000
- Base Rate: 0%
- Slope 1: 0%
- Slope 2: 0%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: Yes
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.2.2 - WETH Risk Parameters [Core]  <!-- UUID: dc3b3c32-f891-49fa-bdb4-8944d14e3d56 -->

The current WETH risk parameters are:

- LTV: 70%
- Liquidation Threshold: 75%
- E-mode Category: ETH
- Liquidation Bonus: 5%
- Reserve Factor: 50%
- Supply Cap: 5,000 ETH
- Borrow Cap: 3,000 ETH
- Optimal Utilization: 80%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 2.5%
- Slope 2: 120%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.2.3 - USDT Risk Parameters [Core]  <!-- UUID: f5a396c7-dc2c-4d67-adff-89c5a8c62652 -->

The current USDT risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0%
- E-mode Category: USD
- Liquidation Bonus: 0%
- Reserve Factor: 10%
- Supply Cap: 10,000,000 USDT
- Borrow Cap: 8,000,000 USDT
- Optimal Utilization: 95%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 9%
- Slope 2: 15%
- Reserve State: Frozen
- Collateral: No
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: Yes
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.2.4 - sDai Risk Parameters [Core]  <!-- UUID: 2c982dbd-dee3-45ce-9e45-48d7ebc33acb -->

The current sDai risk parameters are:

- LTV: 70%
- Liquidation Threshold: 75%
- E-mode Category: USD
- Liquidation Bonus: 6%
- Reserve Factor: 50%
- Supply Cap: 40,000,000 sDai
- Borrow Cap: N/A
- Optimal Utilization: 80%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 0%
- Slope 2: 0%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: No
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.2.5 - wstETH Risk Parameters [Core]  <!-- UUID: a07d0682-9249-4a4f-b2a3-c0dfb163c683 -->

The current wstETH risk parameters are:

- LTV: 65%
- Liquidation Threshold: 72.5%
- E-mode Category: ETH
- Liquidation Bonus: 8%
- Reserve Factor: 50%
- Supply Cap: 15,000 wstETH
- Borrow Cap: 100 wstETH
- Optimal Utilization: 45%
- Isolated Debt Ceiling: N/A
- Base Rate: 1%
- Slope 1: 3%
- Slope 2: 100%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.2.6 - USDC Risk Parameters [Core]  <!-- UUID: f54fff22-1cad-4ccd-80ae-f05f0345c384 -->

The current USDC risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0%
- E-mode Category: USD
- Liquidation Bonus: 0%
- Reserve Factor: 10%
- Supply Cap: 10,000,000 USDC
- Borrow Cap: 1,000,000 USDC
- Optimal Utilization: 80%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 9%
- Slope 2: 50%
- Reserve State: Frozen
- Collateral: No
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: Yes
- Siloed Borrowing: No
- Flash Loan Enabled: Yes

###### A.6.1.1.1.3.2.1.1.2.2.7 - USDC.e Risk Parameters [Core]  <!-- UUID: b54fc943-6d64-4c67-9aa2-150665be6493 -->

The current USDC.e risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0%
- E-mode Category: USD
- Liquidation Bonus: 0%
- Reserve Factor: 50%
- Supply Cap: 10,000,000 USDC.e
- Borrow Cap: 8,000,000 USDC.e
- Optimal Utilization: 95%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 9%
- Slope 2: 15%
- Reserve State: Frozen
- Collateral: No
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: Yes
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.2.8 - WXDAI Risk Parameters [Core]  <!-- UUID: 57bae006-ff07-4da7-adc3-ea3649ce7e38 -->

The current WXDAI risk parameters are:

- LTV: 0%
- Liquidation Threshold: 75%
- E-mode Category: USD
- Liquidation Bonus: 5%
- Reserve Factor: 50%
- Supply Cap: 20,000,000 WXDAI
- Borrow Cap: 16,000,000 WXDAI
- Optimal Utilization: 95%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 9%
- Slope 2: 15%
- Reserve State: Frozen
- Collateral: Yes
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: Yes
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.2.2.9 - EURe Risk Parameters [Core]  <!-- UUID: 1a8186bd-c557-4a6d-80e3-a8140a215e06 -->

The current EURe risk parameters are:

- LTV: 0%
- Liquidation Threshold: 0%
- E-mode Category: N/A
- Liquidation Bonus: 0%
- Reserve Factor: 50%
- Supply Cap: 5,000,000 EURe
- Borrow Cap: 4,000,000 EURe
- Optimal Utilization: 95%
- Isolated Debt Ceiling: N/A
- Base Rate: 0%
- Slope 1: 5%
- Slope 2: 15%
- Reserve State: Frozen
- Collateral: No
- Borrowing: Yes
- Isolated Collateral: No
- Isolated Borrowing: No
- Siloed Borrowing: No
- Flash Loan Enabled: No

###### A.6.1.1.1.3.2.1.1.3 - SparkLend Risk Parameters Cap Automators [Core]  <!-- UUID: 6ffdb8ee-b083-40f5-b51b-1c91e954b68b -->

Cap Automators allow the Supply Cap defined in [A.6.1.1.1.3.2.1.1.1.9 - Supply Cap Definition](e222b8da-abda-42f5-8106-20c6f2881dc7) and the Borrow Cap defined in [A.6.1.1.1.3.2.1.1.1.10 - Borrow Cap Definition](a2d6a99e-c63a-4f30-87f3-a3d66b1eda92) to be dynamically adjusted.

The cap automator is defined in terms of three parameters:

1. `gap` - the target available exposure
2. `ttl` - the cooldown period for cap increases
3. `max` - the absolute maximum exposure

Authorized parties can update a covered Supply Cap or Borrow Cap so the available exposure is equal to the target, as long as the resulting exposure does not exceed the specified maximum limit and the cooldown period has elapsed in the case of increases to the Supply Cap or Borrow Cap.

###### A.6.1.1.1.3.2.1.1.3.1 - SparkLend Risk Parameters Cap Automator Parameter Definitions [Core]  <!-- UUID: e6bc54e6-91df-4095-a032-0e1128c2cab7 -->

The subdocuments herein define the parameters of the Cap Automators.

###### A.6.1.1.1.3.2.1.1.3.1.1 - SparkLend Risk Parameters Cap Automator Target Available Exposure Definition [Core]  <!-- UUID: 6d069b25-fb76-4fa6-93f2-7b9ff6aeaa4c -->

The `gap` parameter is the target gap between the supply usage and the Supply Cap, in the case of the Supply Cap, or between the borrow usage and the Borrow Cap, in the case of the Borrow Cap.

###### A.6.1.1.1.3.2.1.1.3.1.2 - SparkLend Risk Parameters Cap Automator Cooldown Period Definition [Core]  <!-- UUID: 7807007b-c076-4c7a-bd90-10cd23d41189 -->

The `ttl` parameters is the minimum time requirement before it is possible to increase the Supply Cap or Borrow Cap, expressed in seconds.

###### A.6.1.1.1.3.2.1.1.3.1.3 - SparkLend Risk Parameters Cap Automator Absolute Maximum Exposure Definition [Core]  <!-- UUID: 35323a90-f863-4fad-b6ca-9968a163a76d -->

The `max` parameter is the maximum the Supply Cap or Borrow Cap can be increased to.

###### A.6.1.1.1.3.2.1.1.3.2 - SparkLend Cap Automator Current Configuration [Core]  <!-- UUID: 44689f16-06e9-479b-9285-0bc897edca31 -->

The subdocuments herein define the current configuration of the cap automators for each covered market.

###### A.6.1.1.1.3.2.1.1.3.2.1 - SparkLend Cap Automator WETH Parameters [Core]  <!-- UUID: 89304383-83e5-48fe-aa1a-a34a5ded82e5 -->

The current WETH cap automator parameters are:

- Supply cap
    - `gap`: 100,000 WETH
    - `ttl`: 4 hours
    - `max`: Unlimited
- Borrow cap
    - `gap`: 10,000 WETH
    - `ttl`: 4 hours
    - `max`: Unlimited

###### A.6.1.1.1.3.2.1.1.3.2.2 - SparkLend Cap Automator wstETH Parameters [Core]  <!-- UUID: 93b851d7-9825-4022-a583-51a4bbdf4f9c -->

The current wstETH cap automator parameters are:

- Supply cap
    - `gap`: 50,000 wstETH
    - `ttl`: 4 hours
    - `max`: Unlimited
- Borrow cap
    - `gap`: 10,000 wstETH
    - `ttl`: 12 hours
    - `max`: 1 wstETH

###### A.6.1.1.1.3.2.1.1.3.2.3 - SparkLend Cap Automator rETH Parameters [Core]  <!-- UUID: 4bec80b2-33d2-48a9-83e6-26bb2a00e303 -->

The current rETH cap automator parameters are:

- Supply cap
    - `gap`: 10,000 rETH
    - `ttl`: 12 hours
    - `max`: 80,000 rETH
- Borrow cap
    - `gap`: 100 rETH
    - `ttl`: 12 hours
    - `max`: 1 rETH

###### A.6.1.1.1.3.2.1.1.3.2.4 - SparkLend Cap Automator WBTC Parameters [Core]  <!-- UUID: b67fb946-b21d-4173-b57b-e5505128f003 -->

The current WBTC cap automator parameters are:

- Supply cap
    - `gap`: 500 WBTC
    - `ttl`: 4 hours
    - `max`: 50,000 WBTC
- Borrow cap
    - `gap`: 100 WBTC
    - `ttl`: 4 hours
    - `max`: 50,000 WBTC

###### A.6.1.1.1.3.2.1.1.3.2.5 - SparkLend Cap Automator sDai Parameters [Core]  <!-- UUID: 21bdfe50-0996-494d-8413-1d41966fb4f6 -->

The current sDai cap automator parameters are:

- Supply cap
    - `gap`: 50 million sDai
    - `ttl`: 12 hours
    - `max`: 1 billion sDai
- Borrow cap: n/a - not a borrowable asset
    - `gap`: n/a
    - `ttl`: n/a
    - `max`: 0 sDAI

###### A.6.1.1.1.3.2.1.1.3.2.6 - SparkLend Cap Automator USDC Parameters [Core]  <!-- UUID: 07f1853e-ec34-44ae-b137-708a81cd3195 -->

The current USDC cap automator parameters are:

- Supply cap
    - `gap`: 150 million USDC
    - `ttl`: 12 hours
    - `max`: 0 (no cap)
- Borrow cap
    - `gap`: 50 million USDC
    - `ttl`: 12 hours
    - `max`: 0 (no cap)

###### A.6.1.1.1.3.2.1.1.3.2.7 - SparkLend Cap Automator USDT Parameters [Core]  <!-- UUID: 7edd58f1-df79-4346-803b-4d01883e3f09 -->

The current USDT cap automator parameters are:

- Supply cap
    - `gap`: 1 billion USDT
    - `ttl`: 12 hours
    - `max`: 0 (no cap)
- Borrow cap
    - `gap`: 200 million USDT
    - `ttl`: 12 hours
    - `max`: 0 (no cap)

###### A.6.1.1.1.3.2.1.1.3.2.8 - SparkLend Cap Automator cbBTC Parameters [Core]  <!-- UUID: e2b2d7b0-56f9-408e-a49c-cfd211a20748 -->

The current cbBTC cap automator parameters are:

- Supply cap
    - `gap`: 500 cbBTC
    - `ttl`: 4 hours
    - `max`: 50,000 cbBTC
- Borrow cap
    - `gap`: 100 cbBTC
    - `ttl`: 4 hours
    - `max`: 50,000 cbBTC

###### A.6.1.1.1.3.2.1.1.3.2.9 - SparkLend Cap Automator sUSDS Parameters [Core]  <!-- UUID: 061ca4e3-08a7-4262-aa22-9a79b988cf89 -->

The current sUSDS cap automator parameters are:

- Supply cap
    - `gap`: 50 millions sUSDS
    - `ttl`: 12 hours
    - `max`: 500 million sUSDS
- Borrow cap
    - `gap`: N/A
    - `ttl`: N/A
    - `max`: N/A

###### A.6.1.1.1.3.2.1.1.3.2.10 - SparkLend Cap Automator weETH Parameters [Core]  <!-- UUID: cc049d6b-327f-4c85-aab0-97c976405e39 -->

The current weETH cap automator parameters are:

- Supply cap
    - `gap`: 10,000 weETH
    - `ttl`: 12 hours
    - `max`: 500,000 weETH
- Borrow cap
    - `gap`: N/A
    - `ttl`: N/A
    - `max`: N/A

###### A.6.1.1.1.3.2.1.1.3.2.11 - SparkLend Cap Automator LBTC Parameters [Core]  <!-- UUID: b0837675-5d32-43ee-84f9-076fe644c61e -->

The current LBTC cap automator parameters are:

- Supply cap
    - `gap`: 500 LBTC
    - `ttl`: 12 hours
    - `max`: 10,000 LBTC
- Borrow cap
    - `gap`: N/A
    - `ttl`: N/A
    - `max`: N/A

###### A.6.1.1.1.3.2.1.1.3.2.12 - SparkLend Cap Automator tBTC Parameters [Core]  <!-- UUID: 33ee5bdf-e28d-4c9f-98a2-3e7b28bd9b50 -->

The current tBTC cap automator parameters are:

- Supply cap
    - `gap`: 125 tBTC
    - `ttl`: 12 hours
    - `max`: 1,000 tBTC
- Borrow cap
    - `gap`: 25 tBTC
    - `ttl`: 12 hours
    - `max`: 900 tBTC

###### A.6.1.1.1.3.2.1.1.3.2.13 - SparkLend Cap Automator ezETH Parameters [Core]  <!-- UUID: 10f81b39-59d8-4f8c-837b-6f8eb00804b8 -->

The current ezETH cap automator parameters are:

- Supply cap
    - `gap`: 5,000 ezETH
    - `ttl`: 12 hours
    - `max`: 40,000 ezETH
- Borrow cap
    - `gap`: N/A
    - `ttl`: N/A
    - `max`: N/A

###### A.6.1.1.1.3.2.1.1.3.2.14 - SparkLend Cap Automator rsETH Parameters [Core]  <!-- UUID: e8012cc7-5e8c-47e7-af44-d7e61bd16b3e -->

The current rsETH cap automator parameters are:

- Supply cap
    - `gap`: 5,000 rsETH
    - `ttl`: 12 hours
    - `max`: 40,000 rsETH
- Borrow cap
    - `gap`: N/A
    - `ttl`: N/A
    - `max`: N/A

###### A.6.1.1.1.3.2.1.1.3.2.15 - SparkLend Cap Automator pyUSD Parameters [Core]  <!-- UUID: c06b8247-1397-4887-b1e6-0ea370d25dc9 -->

The current pyUSD cap automator parameters are:

- Supply cap
    - `gap`: 50 million pyUSD
    - `ttl`: 12 hours
    - `max`: 0 (no cap)
- Borrow cap
    - `gap`: 25 million pyUSD
    - `ttl`: 12 hours
    - `max`: 0 (no cap)

###### A.6.1.1.1.3.2.1.1.3.3 - SparkLend Cap Automator Authorized Parties [Core]  <!-- UUID: e58645fb-0085-4ea2-aba5-c4b5968038b8 -->

The SparkLend Cap Automator can be triggered by any of the authorized parties below:

- `0x9Ad87668d49ab69EEa0AF091de970EF52b0D5178` (ALM Proxy Freezable)

###### A.6.1.1.1.3.2.1.1.3.4 - SparkLend Cap Automator Version [Core]  <!-- UUID: 2b17cf11-f0e3-4118-bbac-6a8458b4f70a -->

The SparkLend Cap Automator Version is: 1.1

###### A.6.1.1.1.3.2.1.1.4 - SparkLend Risk Parameters Kill Switch [Core]  <!-- UUID: 38329b4f-7666-4f68-ba66-74ebb2e60e13 -->

The kill switch disables all borrowing across SparkLend markets in the event of a depeg on key collateral assets.

The kill switch is defined in terms of a threshold for specified pegged assets. If the ratio of the price of a specified asset to its peg is equal to or less than the threshold, then any user can trigger the kill switch to disable borrowing across all SparkLend markets.

After the kill switch is triggered, markets can be reactivated by Sky Governance after resetting the kill switch. Resetting the kill switch is subject to the Governance Security Delay specified in [A.1.10.3 - Governance Security Delay Requirements](c5f0e955-0441-42e0-a6fc-eab875bba568).

###### A.6.1.1.1.3.2.1.1.4.1 - SparkLend Risk Parameters Kill Switch Current Configuration [Core]  <!-- UUID: d9e7ca3f-53f9-46aa-9e2c-c09f9d6392e1 -->

The kill switch currently covers the following assets with the specified thresholds:

- wstETH/ETH - 0.95
- LBTC/BTC - 0.95
- weETH/ETH - 0.95
- rETH/ETH - 0.95
- cbBTC/BTC - 0.95
- WBTC/BTC - 0.95 - Oracle: ChainLink WBTC/BTC (0xfdFD9C85aD200c506Cf9e21F1FD8dd01932FBB23)

##### A.6.1.1.1.3.2.1.2 - Operational Process Definition [Core]  <!-- UUID: e547484b-1388-4cc2-a03f-971b96c341bd -->

The documents herein define the process for the ongoing management of SparkLend. Future iterations of the Artifact will specify operational processes owned by Spark.

###### A.6.1.1.1.3.2.1.2.1 - SparkLend Risk Parameters Modification [Core]  <!-- UUID: 6029a425-ad81-46c5-866d-94e2ff663873 -->

The modification of SparkLend parameters is temporarily controlled by Sky Core, but will be transitioned to Spark in the future. Currently, the Core Council Risk Advisor, in consultation with Phoenix Labs, may recommend changes to any of the parameters specified in the subdocuments of [A.6.1.1.1.3.2.1.1.1 - SparkLend Risk Parameters Definitions](667abf8c-64a3-4029-b218-e7a6e7000bbd) or [A.6.1.1.1.3.2.1.1.3.1 - SparkLend Risk Parameters Cap Automator Parameter Definitions](e6bc54e6-91df-4095-a032-0e1128c2cab7).

As a general rule, the modification of said parameters is pursuant to the Operational Weekly Cycle and can be effected directly via an Executive Vote, without requiring a Governance Poll.

###### A.6.1.1.1.3.2.1.2.2 - Collateral Onboarding/Offboarding [Core]  <!-- UUID: 1a1f4bef-d19d-42ff-8ac4-746498df9fbc -->

The onboarding/offboarding of SparkLend collateral is temporarily controlled by Sky Core, but will be transitioned to Spark in the future. Currently, it is implemented by the Core Facilitator, in consultation with the Core Council Risk Advisor and Phoenix Labs, through the Operational Weekly Cycle.

###### A.6.1.1.1.3.2.1.2.3 - Spark Protocol-Aave Revenue Share [Core]  <!-- UUID: a9529f7f-c2fa-4d56-a2b1-0a75e78fd135 -->

Spark Protocol must pay out 10% of the income it generates from operating the borrowing and lending functionality of the protocol that is based on the Aave codebase. The documents herein define the Spark Protocol-Aave Revenue Share and its associated operational processes.

###### A.6.1.1.1.3.2.1.2.3.1 - Sky Core Governance Responsibility For Virtual Revenue Share Prior to Launch of SPK [Core]  <!-- UUID: f84a1cb6-7f77-4bd0-904f-8bf7b368d2d6 -->

Before the launch of Agent tokens, Sky Governance is temporarily responsible for paying out a "virtual revenue share" on behalf of Spark Protocol. It is calculated by taking the total amount of Dai borrowed from Spark Protocol, and then assuming a "virtual income" equivalent to 1% of this supply, and calculating a revenue share of 10% on that basis. The calculations and payments must be done manually by the Support Facilitators at the end of each quarter.

As an example: if, before the launch of Agent tokens, 200 million Dai is borrowed on Spark Protocol, then the virtual income is 1% of 200 million Dai, which gives 2 million Dai; and of that 2 million Dai the virtual revenue share is 200,000 Dai.

This 200,000 Dai must be paid out in incremental payments each quarter directly by Sky Governance from the Sky Surplus Buffer to a smart contract under the control of Aave Governance. If, before the launch of Agent tokens, less than 100 million Dai is borrowed from Spark Protocol by the Sky Protocol, accrual towards the virtual revenue share payments are paused (unpaid virtual revenue share that already accrued is still paid out at the end of the quarter), and the counting down of the revenue share duration is paused. The virtual revenue share payments and the counting down of the remaining revenue share duration is resumed when at least 100 million Dai is again borrowed from Spark Protocol by the Sky Protocol.

Once SPK tokens launch, the virtual revenue share system will be discontinued, and the standard rules of the Spark Protocol Aave Revenue Share Ecosystem Agreement shall take effect. See [A.6.1.1.1.3.2.1.2.3.2 - Standard Agreement Post SPK Launch](bb867551-5231-4a5b-ac37-09d545bf70ce).

###### A.6.1.1.1.3.2.1.2.3.2 - Standard Agreement Post SPK Launch [Core]  <!-- UUID: bb867551-5231-4a5b-ac37-09d545bf70ce -->

Post SPK launch, the following revenue-share operational process takes effect. The revenue share payment must be calculated manually at the end of each quarter by the Spark and manually paid as Dai to a smart contract under the control of Aave Governance from Spark. The payments must occur for the revenue share duration of two (2) years, starting from September 25th, 2023.

If at any point in time after the launch of Agent tokens, Spark Protocol is generating less than 1 million Dai per year in income for Spark Agent, accrual towards the revenue share payments are paused (unpaid revenue share that already accrued is still paid out at the end of the quarter), and the counting down of the revenue share duration is paused. The revenue share payments and the counting down of the remaining revenue share duration is resumed when Spark Protocol is generating more than 1 million Dai per year in income again.

##### A.6.1.1.1.3.2.1.3 - Data Repository [Core]  <!-- UUID: 2301085e-3492-422b-8b75-c6dd6564ef29 -->

The documents herein contain data relevant to SparkLend.

#### A.6.1.1.1.3.2.2 - Spark Pre-launch Token Rewards [Core]  <!-- UUID: b4172fc3-9566-4512-b058-75040e47e3bf -->

The subdocuments herein define the parameters and operational processes related to Spark’s pre-launch token rewards program. These rewards will be paid exclusively out of the SPK tokens held by the Spark Foundation.

##### A.6.1.1.1.3.2.2.1 - Parameters [Core]  <!-- UUID: 666671f0-ce3b-4b3f-bf72-d163afa42f4e -->

The parameters of the Spark Pre-launch Token Rewards are specified in the subdocuments herein.

###### A.6.1.1.1.3.2.2.1.1 - Conditions For The Pre-launch Token Rewards [Core]  <!-- UUID: 93dddb43-1d2e-4ea8-ab18-eb0518a193ba -->

Spark has a pre-launch token rewards program based on the usage of its lending platform. Users of the platform will receive an airdrop of SPK tokens, depending on how much and how long they have used the platform during the pre-launch token reward period. These rewards are only for users on Ethereum Mainnet.

There are two seasons of the Spark pre-launch token rewards: Season 1 and Season 2.

Season 1 of pre-launch token rewards was active from August 20 2023 and lasted for nine months, ending on May 20 2024. 130,434,783 SPK tokens were allocated in this period.

In Season 2 14,478,261 SPK will be rewarded per month to SparkLend users who qualify for the airdrop.

Season 2 is an additional pre-farming period, which runs until the Spark Agent launches as part of Sky Endgame launch season.

The monthly SPK rewards are allocated as follows:

- 80 % is allocated to users borrowing DAI and/or USDS
- 20 % is allocated to users supplying ETH

The proposed full anti-cheat SPK Airdrop for SparkLend is calculated using the following formula:

`Airdrop = 80% * (DAI Borrows + USDS Borrows - sDAI Supplies * sDAI Liquidation Threshold - sUSDS Supplies * sUSDS Liquidation Threshold) + 20% * (ETH Supplies - ETH Borrows / ETH Liquidation Threshold)`

All supplies and borrows are denominated in USD based on the on-chain oracle price at that block to determine the conversion.

##### A.6.1.1.1.3.2.2.2 - Operational Process Definition [Core]  <!-- UUID: ba833546-a8aa-4390-9c87-0204abd53e4b -->

The documents herein define the process for the ongoing management of the Spark Pre-launch Token Rewards.

###### A.6.1.1.1.3.2.2.2.1 - Special Pre-launch Token Reward Programs [Core]  <!-- UUID: 9906332c-bc2d-4864-97d4-589f206d6482 -->

Spark can activate a new SPK token pre-launch token reward airdrop program to capture other growth opportunities.

The program can last until the moment SPK launches, or a shorter duration. When activated, the exact details of the special pre-launch token reward airdrop program must be specified in [A.6.1.1.1.3.2.2.2.1.1.0.6.1 - Special Pre-launch Token Reward Program Details](51316a6c-fd6a-4507-b99d-731e80fc9f76).

The SPK tokens for the future Spark Airdrop are allocated between all borrowers based on a formula announced by Spark and specified in the above cited document. The rate of SPK tokens being earned is 7,239,130 SPK per month, distributed on a per block basis proportional to the formula specified in the above cited document.

###### A.6.1.1.1.3.2.2.2.1.1 - Special Pre-launch Token Reward Program Details [Active Data Controller]  <!-- UUID: 1e4ea33d-2d0d-4cfc-8ac2-febce5baf883 -->

The special pre-launch token reward airdrop program is defined as Active Data in [A.6.1.1.1.3.2.2.2.1.1.0.6.1 - Special Pre-launch Token Reward Program Details](51316a6c-fd6a-4507-b99d-731e80fc9f76).

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.1.3.2.2.2.1.1.0.6.1 - Special Pre-launch Token Reward Program Details [Active Data]  <!-- UUID: 51316a6c-fd6a-4507-b99d-731e80fc9f76 -->

Active pre-launch token reward programs established by [A.6.1.1.1.3.2.2.2.1 - Special Pre-launch Token Reward Programs](9906332c-bc2d-4864-97d4-589f206d6482) are:

Aave V3 Main Market sUSDS (7,239,130 SPK per month, ending with SPK token launch):

sUSDS supplies on Aave V3 Main Market are eligible to earn 7,239,130 SPK tokens per month. The SPK rewards program will start on the block during which the sUSDS market is onboarded onto the Aave V3 Main Market and lasts until the issuance of the SPK token, based on the following formula:

`sUSDS Supplies - Sum_i(Stablecoin_i Borrow Amount (in USD) / Stablecoin_i Liquidation Threshold)`

##### A.6.1.1.1.3.2.2.3 - Data Repository [Core]  <!-- UUID: 4ffe4c6e-0dc0-4cb5-9365-8e5a62f0caa5 -->

The documents herein contain data relevant to the Spark Pre-launch Token Rewards.

### A.6.1.1.1.3.3 - Ecosystem Accords [Core]  <!-- UUID: 599fad77-5117-44b2-83c6-3028b2a8a160 -->

Spark has formally agreed to the Ecosystem Accords herein.

#### A.6.1.1.1.3.3.1 - Ecosystem Accord 1 [Core]  <!-- UUID: 7e68a753-88bc-4711-b709-3b5be9e286ad -->

Spark engaged in terms of agreement with the Grove Agent in Ecosystem Accord 1, located in [A.2.8.2.1 - Ecosystem Accord 1: Grove And Spark Agents](9ca40096-937e-431e-af50-9ecd50c0d0a8).

##### A.6.1.1.1.3.3.1.1 - Right of First Refusal Activity [Core]  <!-- UUID: 3b3961e9-9763-499e-bb75-0ea6a9af16b9 -->

The subdocuments herein record the Right of First Refusal activity engaged in by Spark.

###### A.6.1.1.1.3.3.1.1.1 - Right of First Refusal Forgoing [Core]  <!-- UUID: c8fbcc0c-37c2-4ecc-84a6-a0e4607f9753 -->

Spark forwent exercising its Right of First Refusal in order to enable Grove to deploy in Aave Core RLUSD.

#### A.6.1.1.1.3.3.2 - Ecosystem Accord 2 [Core]  <!-- UUID: d8c5d4f5-5b32-4897-8174-90de0b3d9d84 -->

Spark engaged in terms of agreement with Sky, Moonbow and Grove in Ecosystem Accord 2, located in [A.2.8.2.2 - Prime Program](aa3b8e65-0ded-48c2-9c40-812debf99f32).

### A.6.1.1.1.3.4 - SubDAO Proxy Management [Core]  <!-- UUID: 2ad53f55-44cb-44fd-9e68-6c7ed128e360 -->

The documents herein specify Spark's strategy and operational processes for managing assets held in the Spark SubDAO Proxy, and obligations relating to these assets.

#### A.6.1.1.1.3.4.1 - Operational Process Definition [Core]  <!-- UUID: bfdc08d5-42f5-4d49-9390-b6ad210c5c40 -->

The documents herein define the process for updating Spark's SubDAO Proxy management policies.

##### A.6.1.1.1.3.4.1.1 - Spark SubDAO Proxy Policy Changes [Core]  <!-- UUID: 90240e75-6e5f-4a54-8999-ee430cfcf20d -->

Changes to Spark SubDAO Proxy management policies are implemented using the Root Edit Primitive.

##### A.6.1.1.1.3.4.1.2 - Preapproved Subdao Proxy Activities [Core]  <!-- UUID: 8a421648-d732-44c1-8666-bbbb9b7bfff2 -->

Dispositions of Spark SubDAO Proxy assets that have already been approved by governance and added to the Spark artifact, including periodic payments and disposal of non-core assets, can continue as planned until a superseding policy change is adopted via the Spark SubDAO Proxy Policy Changes process.

#### A.6.1.1.1.3.4.2 - Policies and Parameters [Core]  <!-- UUID: 262ff1c9-9634-45a4-9f18-ed222352ddb4 -->

The documents herein define the currently active policies for managing the Spark SubDAO Proxy, alongside relevant parameters for implementing the policies.

##### A.6.1.1.1.3.4.2.1 - Encumbrance Ratio [Core]  <!-- UUID: 9995ba51-1de7-4b32-8b76-a71462dc4c5b -->

The documents herein define Spark's policy for managing the Encumbrance Ratio.

###### A.6.1.1.1.3.4.2.1.1 - Definition [Core]  <!-- UUID: f426cc6e-336a-43bf-825d-1f0c08d1795e -->

The Encumbrance Ratio is defined as the ratio of Spark's Required Risk Capital (RRC) to Total Risk Capital (TRC), as these terms are defined in the Sky Atlas Stability Scope ([A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9)). Spark will seek to maintain a Encumbrance Ratio not greater than the Target Risk Tolerance Ratio specified in [A.6.1.1.1.3.4.2.1.3 - Parameters](d65a06a6-1426-4af2-978c-cd4f7bac79b7).

###### A.6.1.1.1.3.4.2.1.2 - Operational Process [Core]  <!-- UUID: 7bc96051-ce11-4e29-aa30-b535183aeaa7 -->

Spark governance and contributors must take immediate action to reduce the Encumbrance Ratio when it exceeds the Target Encumbrance Ratio level. These actions may fall into two categories, risk capital actions or allocation system actions.

Risk capital actions are actions Spark takes to increase Total Risk Capital, including increasing Internal Junior Risk Capital, sourcing External Junior Risk Capital from other Prime Agents or tokenized sources, or sourcing External Senior Risk Capital from Sky or tokenized sources.

Allocation system actions involve adjusting the capital allocations within the Spark instance of the Allocation System to reduce Required Risk Capital, such as unwinding or disposing of assets requiring higher levels of risk capital as a percent of exposure.

The operational processes implemented at Spark will meet or exceed the requirements specified in the Sky Atlas at [A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capital (TRC) Management](3af8a3a2-25e5-44b3-87a4-7df1f2712685).

###### A.6.1.1.1.3.4.2.1.3 - Parameters [Core]  <!-- UUID: d65a06a6-1426-4af2-978c-cd4f7bac79b7 -->

The current Target Encumbrance Ratio is 90%.

This parameter will be maintained in parallel with the value specified in the Spark Artifact Allocation System Primitive section at [A.6.1.1.1.2.6.1.2.1.3.1 - Spark’s Operation Of Spark Liquidity Layer And Agreement Regarding Encumbrance Ratio](23f7ed09-99ca-45aa-8e12-dffcf55170af); any change to one section of the Spark Artifact will require a corresponding change in the other section.

##### A.6.1.1.1.3.4.2.2 - Target SubDAO Proxy Value [Core]  <!-- UUID: 2e676b28-14e8-4536-ab70-c49b896da8b8 -->

The documents herein define Spark’s policy for maintaining a SubDAO Proxy balance sufficient to cover anticipated risk exposures and operational expenses.

###### A.6.1.1.1.3.4.2.2.1 - Definitions [Core]  <!-- UUID: fd1df613-3038-4f60-9156-ecd4335addb0 -->

The subdocuments herein provide definitions of target SubDAO Proxy value and relevant parameters.

###### A.6.1.1.1.3.4.2.2.1.1 - Target SubDAO Proxy Value Definition [Core]  <!-- UUID: 3baabdcc-d715-419d-97b7-28936d4b0f95 -->

Target SubDAO Proxy Value is the minimum target value of the Spark DAO SubDAO Proxy, below which Spark will not undertake any non-critical and non-strategic dispositions of SubDAO Proxy assets such as SPK token purchases.

###### A.6.1.1.1.3.4.2.2.1.2 - RRC Lookback Period Definition [Core]  <!-- UUID: 6e832698-c71b-441c-9132-4df8d0357351 -->

The Target SubDAO Proxy Value evaluation method ([A.6.1.1.1.3.4.2.2.2 - Evaluation Method](99d4b8da-fa5c-49ce-b93c-70d07334d7aa)) considers the higher of current Required Risk Capital (RRC) or highest RRC incurred within a trailing period. RRC Lookback Period defines the amount of time to review for the trailing period when evaluating the RRC component of Target SubDAO Proxy Value.

###### A.6.1.1.1.3.4.2.2.1.3 - Spark Product Backstop Definition [Core]  <!-- UUID: ac10196b-18b2-4bc4-8627-0cacac8a3524 -->

The Spark Product Backstop is a fixed value of USDS, updated from time to time by Spark governance via the Spark SubDAO Proxy Policy Changes process ([A.6.1.1.1.3.4.1.1 - Spark SubDAO Proxy Policy Changes](90240e75-6e5f-4a54-8999-ee430cfcf20d)), meant to cover the anticipated risk exposures to Spark products that are not covered under Sky’s Required Risk Capital framework.

###### A.6.1.1.1.3.4.2.2.1.4 - Target Runway Definition [Core]  <!-- UUID: 0bd4cd1e-1a37-4209-8ac4-45c17facafd3 -->

Target Runway defines the amount of operational expenses Spark holds in reserve as part of the Target SubDAO Proxy Value. The operational expenses component of Target SubDAO Proxy Value counts the higher of past month’s operating expenses multiplied by Target Runway (in months), or total operating expenses incurred in trailing period equal to Target Runway.

###### A.6.1.1.1.3.4.2.2.1.5 - Operating Expense Definition [Core]  <!-- UUID: 3ffad8de-515c-45e0-ac75-223d075cb9f8 -->

Operating Expense is defined as the sum of governance-approved transfers to the Spark Foundation within a given period.

###### A.6.1.1.1.3.4.2.2.2 - Evaluation Method [Core]  <!-- UUID: 99d4b8da-fa5c-49ce-b93c-70d07334d7aa -->

Target SubDAO Proxy Value is computed as the greater of Required Risk Capital (RRC) plus Spark Product Backstop, or Operational Expense Reserve.

RRC is calculated as the higher of current RRC or highest RRC incurred within the RRC Lookback Period, divided by Risk Tolerance Ratio ([A.6.1.1.1.3.4.2.1 - Encumbrance Ratio](9995ba51-1de7-4b32-8b76-a71462dc4c5b)).

Spark Product Backstop is set manually by Spark governance per [A.6.1.1.1.3.4.2.2.1.3 - Spark Product Backstop Definition](ac10196b-18b2-4bc4-8627-0cacac8a3524).

Operational expense reserve is calculated as the higher of past month’s operating expenses multiplied by Target Runway (in months), or total operating expenses incurred in trailing period equal to Target Runway.

###### A.6.1.1.1.3.4.2.2.3 - Parameters [Core]  <!-- UUID: 7410ed94-db95-437a-a4d2-9120036ec7bd -->

The current Target SubDAO Proxy Value parameters are:

- RRC Lookback Period: 3 months
- Spark Product Backstop: 1 million USDS
- Target Runway: 12 months

##### A.6.1.1.1.3.4.2.3 - Excess SubDAO Proxy Funds Disposition Policy [Core]  <!-- UUID: 6a4870fa-73f1-4d49-b7ee-d531fb59a971 -->

The documents herein define Spark’s policy for disposition of excess SubDAO Proxy funds above the target SubDAO Proxy value.

###### A.6.1.1.1.3.4.2.3.1 - Definitions [Core]  <!-- UUID: 0da9928f-ae14-4869-b36b-761930422502 -->

The subdocuments herein provide definitions for relevant parameters and values.

###### A.6.1.1.1.3.4.2.3.1.1 - Current SubDAO Proxy Value [Core]  <!-- UUID: 9705a4be-e92f-4195-8e85-1cfe19ec1a0d -->

The Current SubDAO Proxy Value is defined as the sum of all USDS tokens held in the Spark SubDAO on Ethereum at 0x3300f198988e4C9C63F75dF86De36421f06af8c4. Note that the operational process of excess SubDAO Proxy funds disposition as defined in [A.6.1.1.1.3.4.2.3.2 - Operational Process](dfa483c7-5adb-480e-9f82-c97cf4d0f74e) uses the most up-to-date onchain value for the Current SubDAO Proxy Value, and this does not need to be updated in the Spark Artifact as it is expected to fluctuate frequently based on monthly settlements and other operational processes.

###### A.6.1.1.1.3.4.2.3.1.2 - Standard Buyback Rate [Core]  <!-- UUID: 796dc640-03a7-4608-b676-a235a68174b1 -->

The Standard Buyback Rate defines the percentage of excess SubDAO Proxy value that is used for buybacks during each monthly cycle, up to the Enhanced Buyback Threshold.

###### A.6.1.1.1.3.4.2.3.1.3 - Enhanced Buyback Rate [Core]  <!-- UUID: 0efbdfe8-3ccd-4e6a-8195-a52e7f63c1d9 -->

The Enhanced Buyback Rate defines the percentage of SubDAO Proxy value in excess of the Enhanced Buyback Threshold that is used for buybacks during each monthly cycle.

###### A.6.1.1.1.3.4.2.3.1.4 - Enhanced Buyback Threshold [Core]  <!-- UUID: e150176c-1da5-4adb-ba5d-f344d0be03ae -->

The Enhanced Buyback Threshold defines the threshold over which the Enhanced Buyback Rate is applied to calculate buyback amounts. This variable is specified as a percentage of the Target SubDAO Proxy Value; for example, a 200% Enhanced Buyback Threshold means that the Enhanced Buyback Rate will apply to any subDAO proxy value over 2x the Target SubDAO Proxy Value.

###### A.6.1.1.1.3.4.2.3.1.5 - Buyback Executor [Core]  <!-- UUID: d6be588d-e76e-4413-8a3e-c1b59e5bd106 -->

The Buyback Executor is the entity responsible for receiving excess SubDAO Proxy funds in USDS, purchasing SPK, and returning the SPK to the Spark SubDAO Proxy. Initially, this role will be performed by the Spark Operations Multisig.

###### A.6.1.1.1.3.4.2.3.2 - Operational Process [Core]  <!-- UUID: dfa483c7-5adb-480e-9f82-c97cf4d0f74e -->

Each month, immediately following Spark’s monthly settlement with Sky, the Current SubDAO Proxy Value with be calculated based on the definition in [A.6.1.1.1.3.4.2.3.1.1 - Current SubDAO Proxy Value](9705a4be-e92f-4195-8e85-1cfe19ec1a0d), and the Target SubDAO Proxy Value based on the evaluation method in [A.6.1.1.1.3.4.2.2.2 - Evaluation Method](99d4b8da-fa5c-49ce-b93c-70d07334d7aa). If the Current SubDAO Proxy Value is greater than the Target SubDAO Proxy Value, this excess SubDAO Proxy Value is multiplied by the Standard Buyback Rate parameter up to the Enhanced Buyback Threshold, and then by the Enhanced Buyback Rate for any amount in excess of the Enhanced Buyback Threshold. The buyback amount for the month is set as the sum of the two values of the standard and enhanced buybacks.

The next available Spark proxy Spell will include a transfer of this calculated buyback amount to the designated Buyback Executor. After using the transferred funds to purchase SPK, the Buyback Executor will transfer all accrued SPK to the Spark SubDAO Proxy.

###### A.6.1.1.1.3.4.2.3.3 - Parameters [Core]  <!-- UUID: b52a4011-5346-4de7-9522-90ae66b81600 -->

The current buyback policy parameters are:

- Standard Buyback rate: 25%
- Enhanced Buyback rate: 100%
- Enhanced Buyback threshold: 200%
- Buyback executor: 0x2E1b01adABB8D4981863394bEa23a1263CBaeDfC
- Buyback recipient: 0x3300f198988e4C9C63F75dF86De36421f06af8c4

##### A.6.1.1.1.3.4.2.4 - SPK Contributor Vesting [Core]  <!-- UUID: 3b2d9368-7dd5-424a-b9da-b6218ffb5c55 -->

The documents herein define Spark’s policy for managing the SPK contributor vesting.

###### A.6.1.1.1.3.4.2.4.1 - Definition [Core]  <!-- UUID: 318b9af4-5b49-41f1-b134-dd2133eafca8 -->

The SPK contributor vesting is a 4-year linear vesting schedule that compensates Spark contributors.

###### A.6.1.1.1.3.4.2.4.2 - Parameters [Core]  <!-- UUID: 0921d2d9-0270-40ab-bfad-726d3bcd345d -->

The current SPK contributor vesting parameters are:

- DssVest
    - Recipient address(es): `0xEFF097C5CC7F63e9537188FE381D1360158c1511`
    - Start date: 17 June 2025
    - Cliff date: 17 June 2026
    - End date: 16 June 2029
    - Vesting method: Linear per block with cliff
    - Claim auth: Permissionless
- SubDAO Proxy actions
    - Approve SPK
        - Address: `0x6Bad07722818Ceff1deAcc33280DbbFdA4939A09`
        - Amount: 1.2 billion SPK (12% of total supply)

### A.6.1.1.1.3.5 - Spark Savings Configuration [Core]  <!-- UUID: 9b4ce799-3baa-42e8-a742-7e8deb377dfc -->

The documents herein specify Spark's strategy and operational processes for managing parameters and liquidity for the Spark Savings protocol.

#### A.6.1.1.1.3.5.1 - Operational Process Definition [Core]  <!-- UUID: 99f4c04b-e531-498a-aeaa-016c7811bf7a -->

The documents herein define the process for updating Spark Savings Configuration policies and parameters.

##### A.6.1.1.1.3.5.1.1 - Spark Savings Configuration Changes [Core]  <!-- UUID: d6405fa7-d02f-4c31-b191-ad1a2485cca3 -->

Changes to Spark Savings Configuration policies and parameters are implemented using the Root Edit Primitive.

#### A.6.1.1.1.3.5.2 - Onchain Parameters [Core]  <!-- UUID: 32a8f019-86e2-47a0-a55d-c481ade62051 -->

The documents herein define the onchain parameters that are implemented within Spark Savings.

##### A.6.1.1.1.3.5.2.1 - Spark Savings Parameters Definitions [Core]  <!-- UUID: 81198aca-06bd-44fa-90b0-16f8c2c4dd19 -->

The subdocuments herein provide definitions for Spark Savings onchain parameters.

###### A.6.1.1.1.3.5.2.1.1 - Default Admin Role [Core]  <!-- UUID: a4d74779-a7d4-4f89-a1b0-8296227f9a9b -->

The default admin role controls upgrades to Spark Savings vault contracts, and has overall admin control over the vault. This role will be assigned to Spark governance to ensure maximum possible security and decentralization.

###### A.6.1.1.1.3.5.2.1.2 - Setter Role [Core]  <!-- UUID: 811c9931-3a70-4c64-a8fb-d1f162a46d62 -->

The setter role controls the current rewards rate for a Spark Savings vault, within the upper and lower bounds defined by the max yield and min yield onchain parameters.

###### A.6.1.1.1.3.5.2.1.3 - Taker Role [Core]  <!-- UUID: a7fd125d-4017-48ba-a366-96253c6f3a16 -->

The taker role has permission to withdraw a Spark Savings vault's underlying asset from the vault to the Spark Liquidity Layer ALM Proxy contract.

###### A.6.1.1.1.3.5.2.1.4 - Take Rate Limit [Core]  <!-- UUID: e5dbc65a-45b9-41d5-ae13-56c3b3416b13 -->

The take rate limit defines the maximum amount and pace of withdrawals from a Spark Savings vault permitted by the taker role.

###### A.6.1.1.1.3.5.2.1.5 - Min Yield [Core]  <!-- UUID: 739b7c5d-d1b5-48e6-a945-26db2a803854 -->

The min yield parameter is the lowest Spark Savings vault rewards rate that can be implemented by the setter role. Typically this value will be 0.

###### A.6.1.1.1.3.5.2.1.6 - Max Yield [Core]  <!-- UUID: ffc7bf31-df84-4c71-9da2-b4ebea95ae01 -->

The max yield parameter is the highest Spark Savings vault rewards rate that can be implemented by the setter role.

###### A.6.1.1.1.3.5.2.1.7 - Supply Cap [Core]  <!-- UUID: 77918273-af7f-4c7e-80af-3f3d9d2097ec -->

The supply cap defines the maximum amount of underlying asset that can be deposited to a Spark Savings vault by users.

##### A.6.1.1.1.3.5.2.2 - Spark Savings Parameters Current Configuration [Core]  <!-- UUID: 5cfe1941-3231-495c-a4c9-50745ec0a5a9 -->

The subdocuments herein provide the current configuration of Spark Savings onchain parameters.

###### A.6.1.1.1.3.5.2.2.1 - Spark Savings USDC on Ethereum [Core]  <!-- UUID: e541391b-f470-480f-adea-5453f3f7da7a -->

The current parameters for Spark Savings USDC on Ethereum are:

- Default admin role: 0x3300f198988e4C9C63F75dF86De36421f06af8c4
- Setter role: 0xe5c6318456a7Cb6f74f93B4eee4616dB5fcef699
- Taker role: 0x1601843c5E9bC251A3272907010AFa41Fa18347E
- Take rate limit: unlimited
- Min yield: 0%
- Max yield: 10%
- Supply cap: 2 billion

###### A.6.1.1.1.3.5.2.2.2 - Spark Savings USDT on Ethereum [Core]  <!-- UUID: 39a398d7-600e-472a-ac85-c789866fddfc -->

The current parameters for Spark Savings USDT on Ethereum are:

- Default admin role: 0x3300f198988e4C9C63F75dF86De36421f06af8c4
- Setter role: 0xe5c6318456a7Cb6f74f93B4eee4616dB5fcef699
- Taker role: 0x1601843c5E9bC251A3272907010AFa41Fa18347E
- Take rate limit: unlimited
- Min yield: 0%
- Max yield: 10%
- Supply cap: 4 billion

###### A.6.1.1.1.3.5.2.2.3 - Spark Savings ETH on Ethereum [Core]  <!-- UUID: 02c0847b-5608-4c12-a1f6-df889538722f -->

The current parameters for Spark Savings ETH on Ethereum are:

- Default admin role: 0x3300f198988e4C9C63F75dF86De36421f06af8c4
- Setter role: 0xe5c6318456a7Cb6f74f93B4eee4616dB5fcef699
- Taker role: 0x1601843c5E9bC251A3272907010AFa41Fa18347E
- Take rate limit: unlimited
- Min yield: 0%
- Max yield: 5%
- Supply cap: 500,000

###### A.6.1.1.1.3.5.2.2.4 - Spark Savings USDC on Avalanche [Core]  <!-- UUID: fc108236-9f07-45fb-9ff1-4c806975e049 -->

The current parameters for Spark Savings USDC on Avalanche are:

- Default admin role: 0x7566DEbC906C17338524A414343fA61BcA26A843
- Setter role: 0x93c81ADc7F98FdBC8C7a15eCBeD312c8F6adbcB3
- Taker role: 0xecE6B0E8a54c2f44e066fBb9234e7157B15b7FeC
- Take rate limit: unlimited
- Min yield: 0%
- Max yield: 10%
- Supply cap: 500 million

###### A.6.1.1.1.3.5.2.2.5 - Spark Savings PYUSD on Ethereum [Core]  <!-- UUID: 18920d7a-1566-4296-8823-33ace94f0ddc -->

The current parameters for Spark Savings PYUSD on Ethereum are:

- Default admin role: 0x3300f198988e4C9C63F75dF86De36421f06af8c4
- Setter role: 0xe5c6318456a7Cb6f74f93B4eee4616dB5fcef699
- Taker role: 0x1601843c5E9bC251A3272907010AFa41Fa18347E
- Take rate limit: unlimited
- Min yield: 0%
- Max yield: 10%
- Supply cap: 250 million

###### A.6.1.1.1.3.5.2.2.6 - Spark Savings USDG on Robinhood Chain [Core]  <!-- UUID: 398944f7-59c3-495c-900b-939358b76e68 -->

The current parameters for Spark Savings USDG on Robinhood Chain are:

- Default admin role: 0x826AEaeee9233fA8Ba199518dd8621A5962b1D02
- Setter role: 0x59C85fe4385403e93877e48e5521f2F02B150359
- Taker role: 0xfD2fD4B046136B540A56C11c75ac679AE7d1dB24
- Take rate limit: unlimited
- Min yield: 0%
- Max yield: 6%
- Supply cap: 500 million
###### A.6.1.1.1.3.5.2.2.7 - Spark Savings USDT on Arbitrum [Core]  <!-- UUID: 5a2b0ec2-5358-4464-b6cb-0d39642a437d -->

The current parameters for Spark Savings USDT on Arbitrum are:

- Default admin role: 0x65d946e533748A998B1f0E430803e39A6388f7a1
- Setter role: 0x4eE67c8Db1BAa6ddE99d936C7D313B5d31e8fa38
- Taker role: 0x92afd6F2385a90e44da3a8B60fe36f6cBe1D8709
- Take rate limit: unlimited
- Min yield: 0%
- Max yield: 6%
- Supply cap: 250 million

###### A.6.1.1.1.3.5.2.2.8 - Spark Savings USDT on X Layer [Core]  <!-- UUID: c6eb9203-a5af-4f9b-baaf-b70c4449d4a4 -->

The current parameters for Spark Savings USDT on X Layer are:

- Default admin role: 0xCF5af6F53ceC74B791cb4182aC778ca9CD323510
- Setter role: 0x9449ed367C60ea757544fd990B57e1C2D0Ec3A94
- Taker role: 0x83A914C361bB729EB6BEBC8C7bA993667A0E6Df8
- Take rate limit: unlimited
- Min yield: 0%
- Max yield: 6%
- Supply cap: 750 million
#### A.6.1.1.1.3.5.3 - Policies and Operational Parameters [Core]  <!-- UUID: c8fcae7c-01ea-48cf-9b8c-4de7d3c86d78 -->

The documents herein define the currently active policies for Spark Savings Configuration, alongside relevant operational parameters for implementing the policies.

##### A.6.1.1.1.3.5.3.1 - Target Liquidity [Core]  <!-- UUID: 6f328a96-1275-46f7-a034-b40dcb69f708 -->

The documents herein define Spark's policy for managing the liquidity buffers available for user withdrawals from Spark Savings vaults.

###### A.6.1.1.1.3.5.3.1.1 - Definition [Core]  <!-- UUID: 0289444b-b7fe-4003-b737-4e07230a4d9b -->

Target Liquidity is the amount of deposited assets that should remain within each Spark Savings vault contract to support instant withdrawals. This value may be defined as a percent of total vault deposits, a fixed quantity of tokens, or a combination of both types of evaluation.

###### A.6.1.1.1.3.5.3.1.2 - Operational Process [Core]  <!-- UUID: 33a7389c-c8a3-46ab-96a4-17d6b9ee2b4f -->

The Spark Prime Relayer Multisig will execute transactions to ensure liquidity within Spark Savings vaults is aligned with the Target Liquidity configurations specified in Target Liquidity Current Configuration, up to the total amount of user deposits in a given Spark Savings vault. This will be implemented via control of the taker role in the vault and transferAsset rate limit from Spark Liquidity Layer ALM Proxy to the vault.

In normal conditions, this will be automated via the ALM Planner software. If the Prime Relayer Multisig fails to maintain Spark Savings vault liquidity in alignment with the Target Liquidity configurations, the Core Operator Relayer Multisig is empowered to effectuate transactions to achieve this.

###### A.6.1.1.1.3.5.3.1.2.1 - Savings Liquidity Intents [Core]  <!-- UUID: cae48a72-fa6d-439e-88fd-1dc37f499101 -->

Spark Savings will enable users to withdraw amounts exceeding the standard Target Liquidity buffer via Savings Liquidity Intents. Users may submit signed withdrawal intents indicating their intent to redeem Spark Savings vault tokens in amounts exceeding the standard Target Liquidity buffer. Subject to available liquidity within the Spark Liquidity Layer and underlying asset allocations, the Spark Liquidity Layer planner may automatically trigger transactions through the Spark Prime Relayer infrastructure to fulfill such intents. Fulfillment of withdrawal intents is not guaranteed. Withdrawal intents may be replaced or cancelled by submitting a superseding signed intent with the same nonce. Intents that have passed their deadline timestamp may not be executed.

###### A.6.1.1.1.3.5.3.1.3 - Target Liquidity Current Configuration [Core]  <!-- UUID: 98bf1329-ccd7-4a7e-bfaf-d30b5c29574c -->

The subdocuments herein specify the current values for Target Liquidity for each instance of Spark Savings.

###### A.6.1.1.1.3.5.3.1.3.1 - Spark Savings USDC on Ethereum [Core]  <!-- UUID: 3b92fb2c-9944-4fa8-9300-5a53c16189dd -->

The current Target Liquidity for Spark Savings USDC on Ethereum is the greater of 10% of total deposits or 1 million USDC, up to a maximum amount of 10 million USDC.

###### A.6.1.1.1.3.5.3.1.3.2 - Spark Savings USDT on Ethereum [Core]  <!-- UUID: 5e8fdea7-ce4a-4185-9d18-995ff823eb94 -->

The current Target Liquidity for Spark Savings USDT on Ethereum is the greater of 10% of total deposits or 1 million USDT, up to a maximum amount of 10 million USDT.

###### A.6.1.1.1.3.5.3.1.3.3 - Spark Savings ETH on Ethereum [Core]  <!-- UUID: 944ebd8c-0562-4397-8a5a-6ebcea8167e7 -->

The current Target Liquidity for Spark Savings ETH on Ethereum is the greater of 10% of total deposits or 250 ETH, up to a maximum amount of 2,500 ETH.

###### A.6.1.1.1.3.5.3.1.3.4 - Spark Savings USDC on Avalanche [Core]  <!-- UUID: 3a7b2e58-01ac-4b0c-a53e-6cce6f563168 -->

The current Target Liquidity for Spark Savings USDC on Avalanche is the greater of 10% of total deposits or 1 million USDC, up to a maximum amount of 10 million USDC.

###### A.6.1.1.1.3.5.3.1.3.5 - Spark Savings PYUSD on Ethereum [Core]  <!-- UUID: 5af03853-e89b-418a-a457-e8ecf34fc06e -->

The current Target Liquidity for Spark Savings PYUSD on Ethereum is the greater of 10% of total deposits or 1 million PYUSD, up to a maximum amount of 10 million PYUSD.

###### A.6.1.1.1.3.5.3.1.3.6 - Spark Savings USDG on Robinhood Chain [Core]  <!-- UUID: 2fad3cf6-eddc-4924-a461-17e1faebf38c -->

The current Target Liquidity for Spark Savings USDG on Robinhood Chain is the greater of 10% of total deposits or 1 million USDG, up to a maximum amount of 10 million USDG.

###### A.6.1.1.1.3.5.3.1.3.7 - Spark Savings USDT on Arbitrum [Core]  <!-- UUID: 77d38961-5052-4558-a9a4-b21c3651fb58 -->

The current Target Liquidity for Spark Savings USDT on Arbitrum is the greater of 10% of total deposits or 1 million USDT, up to a maximum amount of 10 million USDT.

###### A.6.1.1.1.3.5.3.1.3.8 - Spark Savings USDT on X Layer [Core]  <!-- UUID: 43b26b98-6186-49c9-b91b-8197050c61f1 -->

The current Target Liquidity for Spark Savings USDT on X Layer is the greater of 10% of total deposits or 1 million USDT, up to a maximum amount of 10 million USDT.

##### A.6.1.1.1.3.5.3.2 - Rewards Rate [Core]  <!-- UUID: 22d359a5-3f83-409f-8396-595ac1ea0060 -->

The documents herein define Spark's policy for managing the rewards rate for Spark Savings vaults.

###### A.6.1.1.1.3.5.3.2.1 - Definition [Core]  <!-- UUID: 3a143911-80c9-4eb0-9aa3-5b3d3a8ca843 -->

The Spark Savings Rewards Rate specifies the yield paid out to depositors on their supplied capital, expressed as an annual percentage rate. The Rewards Rate configuration for each vault may be set as a fixed value, or via reference to external benchmarks such as the Sky Savings Rate, Secured Overnight Funding Rate, SparkLend market supply rates, or other relevant measures.

###### A.6.1.1.1.3.5.3.2.2 - Operational Process [Core]  <!-- UUID: 6c7a4964-485f-4edf-a05f-61fa65c9871c -->

The Rewards Rate for each Spark Savings vault will be maintained in alignment with the configuration specified in Rewards Rate Current Configuration via the setter role for each vault. When the currently implemented Rewards Rate diverges from the target value, the setter is responsible for promptly updating the rate onchain.

###### A.6.1.1.1.3.5.3.2.3 - Rewards Rate Current Configuration [Core]  <!-- UUID: 89192471-7e48-43d8-b86e-fa4e70edcf8a -->

The subdocuments herein specify the current configuration for determining Rewards Rate for each instance of Spark Savings.

###### A.6.1.1.1.3.5.3.2.3.1 - Spark Savings USDC on Ethereum [Core]  <!-- UUID: 8cba4337-8305-4b75-9fa2-79cee08a9739 -->

The Rewards Rate for Spark Savings USDC on Ethereum will be maintained to be equal to the Sky Savings Rate.

###### A.6.1.1.1.3.5.3.2.3.2 - Spark Savings USDT on Ethereum [Core]  <!-- UUID: 087dc001-1a44-4096-acd1-feeb109f7ec0 -->

The Rewards Rate for Spark Savings USDT on Ethereum is set via the vault’s setter role in accordance with [A.6.1.1.1.3.5.3.2.2 - Rewards Rate Operational Process](6c7a4964-485f-4edf-a05f-61fa65c9871c), within the Min Yield and Max Yield bounds specified in [A.6.1.1.1.3.5.2.2.2 - Onchain Parameters](39a398d7-600e-472a-ac85-c789866fddfc). Within those bounds, the rate may be set as a fixed value or by reference to an external benchmark, as provided in [A.6.1.1.1.3.5.3.2.1 - Rewards Rate Definition](3a143911-80c9-4eb0-9aa3-5b3d3a8ca843).
###### A.6.1.1.1.3.5.3.2.3.3 - Spark Savings ETH on Ethereum [Core]  <!-- UUID: a2a900aa-a3d6-42d6-b491-cd1fb9701fce -->

The Rewards Rate for Spark Savings ETH on Ethereum will be maintained to be equal to the supply-weighted average yield of ETH-denominated assets held in the Spark Liquidity Layer, multiplied by one minus the percentage of spETH backing held in the spETH vault contract for instant redemptions, plus the Spark Savings ETH Spread.

The Spark Savings ETH Spread will be defined as part of the ALM Planner configuration process, and will be set within a range of -0.5% to 2%.

###### A.6.1.1.1.3.5.3.2.3.4 - Spark Savings USDC on Avalanche [Core]  <!-- UUID: afac32a3-7f73-4b24-8857-061eb5c6c264 -->

The Rewards Rate for Spark Savings USDC on Avalanche will be maintained to be equal to the Sky Savings Rate.

###### A.6.1.1.1.3.5.3.2.3.5 - Spark Savings PYUSD on Ethereum [Core]  <!-- UUID: c54b370a-df10-4621-82a2-7fc4e5caf728 -->

The Rewards Rate for Spark Savings PYUSD on Ethereum will be maintained to be equal to the Sky Savings Rate.

###### A.6.1.1.1.3.5.3.2.3.6 - Spark Savings USDG on Robinhood Chain [Core]  <!-- UUID: ad064b08-8866-4c14-ad34-1275101032a5 -->

The Rewards Rate for Spark Savings USDG on Robinhood Chain is set via the vault’s setter role in accordance with [A.6.1.1.1.3.5.3.2.2 - Rewards Rate Operational Process](6c7a4964-485f-4edf-a05f-61fa65c9871c), within the Min Yield and Max Yield bounds specified in [A.6.1.1.1.3.5.2.2.6 - Onchain Parameters](398944f7-59c3-495c-900b-939358b76e68). Within those bounds, the rate may be set as a fixed value or by reference to an external benchmark, as provided in [A.6.1.1.1.3.5.3.2.1 - Rewards Rate Definition](3a143911-80c9-4eb0-9aa3-5b3d3a8ca843).

###### A.6.1.1.1.3.5.3.2.3.7 - Spark Savings USDT on Arbitrum [Core]  <!-- UUID: 2df1f51c-308f-4b29-90a7-7c01c35e891c -->

The Rewards Rate for Spark Savings USDT on Arbitrum is set via the vault’s setter role in accordance with [A.6.1.1.1.3.5.3.2.2 - Rewards Rate Operational Process](6c7a4964-485f-4edf-a05f-61fa65c9871c), within the Min Yield and Max Yield bounds specified in [A.6.1.1.1.3.5.2.2.7 - Onchain Parameters](5a2b0ec2-5358-4464-b6cb-0d39642a437d). Within those bounds, the rate may be set as a fixed value or by reference to an external benchmark, as provided in [A.6.1.1.1.3.5.3.2.1 - Rewards Rate Definition](3a143911-80c9-4eb0-9aa3-5b3d3a8ca843).

###### A.6.1.1.1.3.5.3.2.3.8 - Spark Savings USDT on X Layer [Core]  <!-- UUID: 40f91471-6b4c-4058-8917-d3b6d2a87f38 -->

The Rewards Rate for Spark Savings USDT on X Layer is set via the vault’s setter role in accordance with [A.6.1.1.1.3.5.3.2.2 - Rewards Rate Operational Process](6c7a4964-485f-4edf-a05f-61fa65c9871c), within the Min Yield and Max Yield bounds specified in [A.6.1.1.1.3.5.2.2.8 - Onchain Parameters](c6eb9203-a5af-4f9b-baaf-b70c4449d4a4). Within those bounds, the rate may be set as a fixed value or by reference to an external benchmark, as provided in [A.6.1.1.1.3.5.3.2.1 - Rewards Rate Definition](3a143911-80c9-4eb0-9aa3-5b3d3a8ca843).

### A.6.1.1.1.3.6 - Strategic Investments [Core]  <!-- UUID: a05cc5db-64e5-4279-84ed-e93d4aa67c38 -->

The documents herein specify Spark's operational processes for undertaking and managing strategic investments, alongside details of existing strategic investments.

#### A.6.1.1.1.3.6.1 - Operational Process Definition [Core]  <!-- UUID: b706d2e5-6f78-4c02-b3da-1ecc9d0a2397 -->

The documents herein define the process for updating Strategic Investment policies and procedures, and for actions related to proposed or current strategic investments.

##### A.6.1.1.1.3.6.1.1 - Strategic Investment Policy Updates [Core]  <!-- UUID: 4216b5c8-9038-4620-a4a9-17062e59863e -->

Changes to Strategic Investment policies and procedures are implemented using the Root Edit Primitive.

##### A.6.1.1.1.3.6.1.2 - Strategic Investment Approvals and Significant Decisions [Core]  <!-- UUID: 66baa7af-73c7-493e-8fbb-66da8a2e8caf -->

Approval of new Strategic Investments, as well as significant changes to existing strategic investments including assignment of rights, sales or disposal of interests, are subject to Spark governance approval and implemented via the Root Edit Primitive.

##### A.6.1.1.1.3.6.1.3 - Delegation of Authority [Core]  <!-- UUID: daf295c4-78eb-463c-a7db-3a012deec873 -->

Certain rights and responsibilities related to strategic investments, including shareholder voting rights, conversion rights, and informational rights, may be held and exercised by Spark Foundation and/or Spark Asset Foundation. Additionally, legal ownership of and title to equity, tokens, or other interests in Spark's Strategic Investments may be held by Spark Foundation or Spark Asset Foundation. Details of delegated authority and rights management, where applicable, should be specified for each individual strategic investment.

#### A.6.1.1.1.3.6.2 - Current Strategic Investments [Core]  <!-- UUID: 0eb2eb16-7306-4410-a596-8c2ff371598a -->

The documents herein provide details on each Strategic Investment undertaken by Spark.

##### A.6.1.1.1.3.6.2.1 - Arkis [Core]  <!-- UUID: a4e71b17-18ca-4911-b9a6-3be65f919591 -->

Arkis is a protocol and technology infrastructure layer facilitating prime brokerage services across both defi protocols and assets, as well as centralized exchanges and custodial services.

###### A.6.1.1.1.3.6.2.1.1 - Investment Terms [Core]  <!-- UUID: 88040e43-50b4-4594-8b22-b2512259e8df -->

Spark's strategic investment will be undertaken with the following terms:

- Investing entity: Spark Foundation
- Investment amount: $4 million paid in USDS
- Recipient: PRM LBS LTD, at address 0xD5FF8bdeF23fc3C8Ff6815C6B4051F9809C877a5
- Arkis post-money valuation: $45 million
- Deal structure:
    - Simple Agreement for Future Equity (SAFE) substantially mirroring the Ycombinator SAFE format
    - Token warrant providing for token ownership share equal to at least 50% of Spark's share of equity ownership at the time of token launch
    - Side letter providing for most favored nation rights, pro rata rights, information rights, major investor rights, and right to elect one director
- Fee reduction: Spark will benefit from reduced fees for use of Arkis protocol for 5 years with Spark Foundation holding the option to extend by 2 additional years, assessed as a 50% reduction vs the lowest rate of fees paid by any other user

###### A.6.1.1.1.3.6.2.1.2 - Delegation of Authority [Core]  <!-- UUID: 483d37f0-0143-44cc-b470-63bbe7913f6d -->

Spark Foundation, as legal owner of the interest in PRM LBS LTD, is empowered to exercise all rights and responsibilities related to the investment for the benefit of the Spark ecosystem, and according to generally accepted business practices as well as the Spark Foundation's own professional judgement.

### A.6.1.1.1.3.7 - Arkis Infrastructure [Core]  <!-- UUID: 9a2d76b9-95c7-4e11-b3b8-ed74f2188e4f -->

The documents herein specify Spark’s strategy and operational processes for allocating capital via Arkis Infrastructure, powered by the Arkis protocol prime brokerage infrastructure.

#### A.6.1.1.1.3.7.1 - Operational Process Definition [Core]  <!-- UUID: cb7c2b0f-15e7-48b3-80fc-f2dc46341468 -->

The documents herein define the process for updating Arkis Infrastructure policies and procedures.

##### A.6.1.1.1.3.7.1.1 - Arkis Infrastructure Policy Changes [Core]  <!-- UUID: a9061ad0-9dbd-4188-94eb-3f1f6783f271 -->

Changes to Arkis Infrastructure policies are implemented using the Root Edit Primitive.

##### A.6.1.1.1.3.7.1.2 - Arkis Infrastructure Policy Change Execution [Core]  <!-- UUID: 3d254422-962c-405c-9c5c-dc72ff37bfec -->

Approved changes to Arkis Infrastructure policies are executed by either Spark Governance (for onchain updates under Spark governance admin control), or via the Arkis team (for offchain components including the Arkis Margin engine or CEX subaccount management). Policy changes must be executed promptly after Root Edit Primitive approval. If policy changes are not executed as required, Spark must remove all funding allocated through the Arkis protocol infrastructure as soon as reasonably practicable.

#### A.6.1.1.1.3.7.2 - Policies and Mandate [Core]  <!-- UUID: d126ed27-57ef-4bf0-ae49-aabbaec47ad4 -->

The documents herein define the currently active policies and mandate for allocation via Arkis Infrastructure.

##### A.6.1.1.1.3.7.2.1 - Counterparty Requirements [Core]  <!-- UUID: 15349ede-15d1-4cee-80d9-fd0b5e5f9f3a -->

Borrowers funded via Arkis Infrastructure must be duly registered by competent authorities in their primary jurisdiction, and must not be subject to sanctions by the US, UK, EU, or UN. Responsibility for verifying KYC/KYB and meeting related compliance requirements is handled by Arkis during the borrower onboarding process.

Borrowers must not be insolvent at the time of loan origination or renewal. Borrowers will self-certify their solvency as part of loan agreements. If a borrower becomes insolvent or enters administration while having an active loan, the entire loan amount becomes due and payable and Arkis may immediately liquidate collateral to recover the loan balance.

##### A.6.1.1.1.3.7.2.2 - Marginable Assets [Core]  <!-- UUID: ef6decfd-b7ce-49a0-85aa-0885921c21f3 -->

The documents herein define the assets or positions that are accepted as margin collateral within instances of the Arkis protocol funded by Spark.

###### A.6.1.1.1.3.7.2.2.1 - Marginable Assets Parameters Definitions [Core]  <!-- UUID: a8a8220e-0380-411a-af53-8ba421bcdba4 -->

The subdocuments herein define the specific risk parameters or limits applicable to each accepted margin collateral asset.

###### A.6.1.1.1.3.7.2.2.1.1 - Collateral Haircut [Core]  <!-- UUID: 131e55ba-86f0-4249-93d1-6d7d40906ab0 -->

The minimum discount applied to net exposure to an asset while calculating position health and stress tested portfolio value, expressed as a negative percentage for accounts net long an asset, or a positive percentage for accounts net short an asset. Spark and Arkis have discretion to implement more conservative collateral haircuts than those listed in the artifact on a case by case basis.

###### A.6.1.1.1.3.7.2.2.1.2 - Exposure Limit [Core]  <!-- UUID: 62b3310b-678a-4159-8a79-6d6433d0e8ab -->

The maximum aggregate gross exposure to a given asset permitted within Spark funded instances of the Arkis protocol. When calculating gross exposure, we use the higher of the sum of long exposure across all positions or short exposure across all positions, without offsetting long and short exposure within each position.

###### A.6.1.1.1.3.7.2.2.1.3 - Staked, Wrapped, and Approved Versions [Core]  <!-- UUID: d24ea4df-6922-48f1-8b14-f62710c89575 -->

The acceptable staked or wrapped versions of a given marginable asset, including non-native bridged versions of an asset. Alternatively, definitions of what specific tokens or assets within a specified asset class are approved to be used as a marginable asset.

###### A.6.1.1.1.3.7.2.2.2 - Marginable Assets Current Configuration [Core]  <!-- UUID: 0dfe744f-7918-403b-85e3-520341769e71 -->

The subdocuments herein define the assets currently accepted as margin collateral within Spark funded instances of the Arkis protocol.

###### A.6.1.1.1.3.7.2.2.2.1 - Bitcoin (BTC) [Core]  <!-- UUID: 60525756-fcea-4439-af53-e9c6eb1ef898 -->

- Collateral Haircut: +20% / -20%
- Exposure Limit: None (native BTC, cbBTC, WBTC), $100 million (LBTC)
- Staked and Wrapped Versions: Lombard LBTC, Coinbase cbBTC, Bitgo/BitGlobal WBTC

###### A.6.1.1.1.3.7.2.2.2.2 - Ether (ETH) [Core]  <!-- UUID: c015634f-20ec-4a86-a056-b0d9b8e46601 -->

- Collateral Haircut: +20% / -20%
- Exposure Limit: None (ETH/WETH, stETH), $250 million (weETH, native staking)
- Staked and Wrapped Versions: WETH, Lido stETH/wstETH, Etherfi weETH, native staking with approved provider

###### A.6.1.1.1.3.7.2.2.2.3 - Ripple (XRP) [Core]  <!-- UUID: 4d25dda5-14c0-46cb-8a93-447445d3a154 -->

- Collateral Haircut: +20% / -20%
- Exposure Limit: $50 million
- Staked and Wrapped Versions: None

###### A.6.1.1.1.3.7.2.2.2.4 - Solana (SOL) [Core]  <!-- UUID: 4e3841e8-b90e-476d-b0ab-da3786b15978 -->

- Collateral Haircut: +20% / -20%
- Exposure Limit: $100 million
- Staked and Wrapped Versions: JitoSOL, Binance BNSOL, Bybit BBSOL, OKX OKSOL, native staking with approved provider

###### A.6.1.1.1.3.7.2.2.2.5 - Dogecoin (DOGE) [Core]  <!-- UUID: 53bb9ea7-b86d-419d-836c-4b4edd21b297 -->

- Collateral Haircut: +25% / -25%
- Exposure Limit: $25 million
- Staked and Wrapped Versions: None

###### A.6.1.1.1.3.7.2.2.2.6 - Cardano (ADA) [Core]  <!-- UUID: 66b2fe30-3bf2-4488-a8e2-b26f39a2fad9 -->

- Collateral Haircut: +25% / -25%
- Exposure Limit: $25 million
- Staked and Wrapped Versions: None

###### A.6.1.1.1.3.7.2.2.2.7 - Hyperliquid (HYPE) [Core]  <!-- UUID: 6828399d-ea70-4044-a26d-b5c726e573b7 -->

- Collateral Haircut: +25% / -25%
- Exposure Limit: $50 million
- Staked and Wrapped Versions: kHYPE, stHYPE, native staking with approved provider

###### A.6.1.1.1.3.7.2.2.2.8 - Zcash (ZEC) [Core]  <!-- UUID: 3847ad1c-a5cb-446d-af95-ad918b2798bf -->

- Collateral Haircut: +30% / -30%
- Exposure Limit: $20 million
- Staked and Wrapped Versions: None

###### A.6.1.1.1.3.7.2.2.2.9 - Avalanche (AVAX) [Core]  <!-- UUID: 32d1cdc6-9d76-45b0-83a4-8ee228628987 -->

- Collateral Haircut: +30% / -30%
- Exposure Limit: $20 million
- Staked and Wrapped Versions: Benqi sAVAX, native staking with approved provider

###### A.6.1.1.1.3.7.2.2.2.10 - Sui (SUI) [Core]  <!-- UUID: b27f52fc-dee9-448e-bdf7-62453b559bd3 -->

- Collateral Haircut: +30% / -30%
- Exposure Limit: $20 million
- Staked and Wrapped Versions: native staking with approved provider

###### A.6.1.1.1.3.7.2.2.2.11 - Near (NEAR) [Core]  <!-- UUID: a33a0224-1005-4875-b202-0935f48f9c82 -->

- Collateral Haircut: +30% / -30%
- Exposure Limit: $20 million
- Staked and Wrapped Versions: native staking with approved provider

###### A.6.1.1.1.3.7.2.2.2.12 - Ethena (USDe) [Core]  <!-- UUID: 862b3d39-6298-40ae-b1d7-909e24e87e07 -->

- Collateral Haircut: -10%
- Exposure Limit: $500 million
- Staked and Wrapped Versions: sUSDe

###### A.6.1.1.1.3.7.2.2.2.13 - Tether (USDT) [Core]  <!-- UUID: 224b6c35-7ec4-4dfb-8ec1-8efe4d88b942 -->

- Collateral Haircut: 0%
- Exposure Limit: None
- Staked and Wrapped Versions: Spark Savings USDT (spUSDT)

###### A.6.1.1.1.3.7.2.2.2.14 - Circle (USDC) [Core]  <!-- UUID: 839c1db9-48d7-45cf-b049-13e3edd0290d -->

- Collateral Haircut: 0%
- Exposure Limit: None
- Staked and Wrapped Versions: Spark Savings USDC v2 (spUSDC) and v1 (sUSDC)

###### A.6.1.1.1.3.7.2.2.2.15 - Fully Reserved USD Stablecoins [Core]  <!-- UUID: 2782410b-2ba0-49d2-91e5-1de2a0e89ab8 -->

- Collateral Haircut: -5%
- Exposure Limit: not more than 20% of the circulating supply of any given stablecoin
- Approved Versions: Paypal PYUSD, Paxos USDG, Ripple RLUSD, Ethena USDtb

###### A.6.1.1.1.3.7.2.2.2.16 - Fully Reserved Major Non-USD Stablecoins [Core]  <!-- UUID: 79eb2c89-6107-4b56-a8fe-7f3582d4bd24 -->

- Collateral Haircut: +10% / -10%
- Exposure Limit: not more than 20% of the circulating supply of any given stablecoin
- Approved Versions: Circle EURC, Société Générale EURCV, Monerium EURe

###### A.6.1.1.1.3.7.2.2.2.17 - Gold (XAU) [Core]  <!-- UUID: 406351ec-ca29-4980-8475-61090bb37e98 -->

- Collateral Haircut: +10% / -10%
- Exposure Limit: $500 million (XAUT, PAXG), $50 million (XAUM)
- Approved Versions: Tether XAUT, Paxos PAXG, Matrixdock XAUM

###### A.6.1.1.1.3.7.2.2.2.18 - Silver (XAG) [Core]  <!-- UUID: 0a907606-7766-41b7-afc2-04da1bc80cdf -->

- Collateral Haircut: +15% / -15%
- Exposure Limit: $250 million
- Approved Versions: No spot assets supported (only derivatives)

###### A.6.1.1.1.3.7.2.2.2.19 - Oil [Core]  <!-- UUID: f4da836b-1f60-42a0-b0fc-7f7c6189ea45 -->

- Collateral Haircut: +15% / -15%
- Exposure Limit: $250 million
- Approved Versions: No spot assets supported (only derivatives). Contracts must reference Brent Crude or West Texas Intermediate (WTI).

###### A.6.1.1.1.3.7.2.2.3 - Pendle PTs [Core]  <!-- UUID: d65ab4f5-a2cf-4817-95e7-f19c8b1a972f -->

Pendle PTs expiring within 120 days linked to approved assets may be accepted as margin collateral. Exposure to Pendle PTs shall not exceed 10 times the total liquidity within the Pendle AMM for the given PT.

###### A.6.1.1.1.3.7.2.2.4 - Perpetual and Calendar Futures [Core]  <!-- UUID: 904fd5ef-ac80-4171-8c29-27cc812a70bd -->

Perpetual futures and calendar futures expiring within 120 days that reference an approved asset as underlying may be included in margin calculations.

###### A.6.1.1.1.3.7.2.2.5 - Decentralized Exchange Protocols [Core]  <!-- UUID: 5ac93594-d197-4fac-b5ca-6bc9b7f10bed -->

Approved onchain spot decentralized exchange protocols may be included within position margin calculations, under the following conditions: (1) all assets to which a pool has exposure are approved as marginable assets, and (2) the protocol is either Curve-ng stableswap, Uniswap v2, Uniswap v3, Uniswap v4 vanilla (no hooks), or Uniswap v4 using hook(s) that have been onboarded via direct integration within the Spark Liquidity Layer. If one or more of these conditions is not met in full, the pool is treated as an unapproved asset/product.

###### A.6.1.1.1.3.7.2.2.6 - Unapproved Assets and Products [Core]  <!-- UUID: 5163ebb9-a425-4df6-aba9-b483e8a482c1 -->

Exposure to unapproved assets and/or futures products is not permitted, and incurs a collateral haircut rating of +100% / -100%. Long and short exposure to unapproved products will not be counted as offsetting each other. Frequent or significant exposure to unapproved assets or products may result in recall of the loan amount or liquidation of outstanding positions.

##### A.6.1.1.1.3.7.2.3 - Approved Venues [Core]  <!-- UUID: c0a9aae3-661b-4124-9da7-1a85e01e4358 -->

The documents herein define the venues where Arkis Infrastructure users are permitted to trade and hold positions.

###### A.6.1.1.1.3.7.2.3.1 - Approved Venues Parameters Definitions [Core]  <!-- UUID: 06fcb0dd-3f54-420c-b518-34790d7a20ab -->

The subdocuments herein define the specific risk parameters or limits applicable to each approved venue.

###### A.6.1.1.1.3.7.2.3.1.1 - Exposure Limit [Core]  <!-- UUID: 5fbe9a91-0142-4d47-b89c-b46c911b313e -->

The exposure limit is the maximum amount of account value, defined in USD based on current value of assets and positions, inclusive of spot assets, collateral for derivatives positions, and both settled and unrealized PNL within derivatives positions.

###### A.6.1.1.1.3.7.2.3.2 - Approved Venues Current Configuration [Core]  <!-- UUID: 0b290136-8726-49b5-92d4-fa3ac320af19 -->

The subdocuments herein define the currently approved venues where positions and assets may be held in Spark funded instances of the Arkis Protocol.

###### A.6.1.1.1.3.7.2.3.2.1 - Onchain [Core]  <!-- UUID: 5f029ce0-cb6e-4364-9cce-8dc7ad8fffbd -->

Users are permitted to hold assets and positions within their onchain Arkis margin account.

- Exposure Limit: None

###### A.6.1.1.1.3.7.2.3.2.2 - Binance [Core]  <!-- UUID: e9f0543a-ce6e-46b3-bdb7-c0fd60239c29 -->

Users are permitted to hold assets and positions within Binance, in a subaccount controlled under the Arkis master account.

- Exposure Limit: $100 million

###### A.6.1.1.1.3.7.2.3.2.3 - OKX [Core]  <!-- UUID: 35f40a50-fca5-4140-ab93-81e58c181b95 -->

Users are permitted to hold assets and positions within OKX, in a subaccount controlled under the Arkis master account.

- Exposure Limit: $100 million

###### A.6.1.1.1.3.7.2.3.2.4 - Bybit [Core]  <!-- UUID: ccb02230-7ade-4935-800d-8e038d104bcd -->

Users are permitted to hold assets and positions within Bybit, in a subaccount controlled under the Arkis master account.

- Exposure Limit: $100 million

###### A.6.1.1.1.3.7.2.3.2.5 - Bitget [Core]  <!-- UUID: 790805e0-4798-4388-afd3-cfc977fa4fee -->

Users are permitted to hold assets and positions within Bitget, in a subaccount controlled under the Arkis master account.

- Exposure Limit: $25 million

###### A.6.1.1.1.3.7.2.3.2.6 - Hyperliquid (Hypercore) [Core]  <!-- UUID: ce034c3a-89af-444b-bfad-bcf2e64e8b19 -->

Users are permitted to hold assets and positions Hyperliquid perpetuals exchange (Hypercore), in a subaccount controlled under the Arkis master account.

- Exposure Limit: $50 million

###### A.6.1.1.1.3.7.2.3.2.7 - Anchorage [Core]  <!-- UUID: f4bd5948-0d52-4fc9-9fa5-530b7768484c -->

Users are permitted to hold assets and positions within Anchorage, in a subaccount controlled under the Arkis master account, or via collateral management account where Arkis holds a secured interest.

- Exposure Limit: $100 million

###### A.6.1.1.1.3.7.2.3.2.8 - Bitgo [Core]  <!-- UUID: 982d2ada-1f8f-422e-94d2-1027e9b0903c -->

Users are permitted to hold assets and positions within Bitgo, in a subaccount controlled under the Arkis master account, or via collateral management account where Arkis holds a secured interest.

- Exposure Limit: $100 million

###### A.6.1.1.1.3.7.2.3.2.9 - Ceffu [Core]  <!-- UUID: 8d8d15cb-f24a-4960-89c9-5d7a2b1c04bd -->

Users are permitted to hold assets and positions within Ceffu, in a subaccount controlled under the Arkis master account as implemented through Arkis infrastructure arrangements, or via collateral management account where Arkis holds a secured interest.

- Exposure Limit: $100 million

###### A.6.1.1.1.3.7.2.3.2.10 - Copper [Core]  <!-- UUID: 1da59154-e4af-4fa8-b235-1004869e68e5 -->

Users are permitted to hold assets and positions within Copper, in a subaccount controlled under the Arkis master account as implemented through Arkis infrastructure arrangements, or via collateral management account where Arkis holds a secured interest.

- Exposure Limit: $100 million

###### A.6.1.1.1.3.7.2.3.2.11 - Lighter [Core]  <!-- UUID: 827b0862-4598-4296-882c-98da321f8920 -->

Users are permitted to hold assets and positions within Lighter, in a subaccount controlled under the Arkis master account.

- Exposure Limit: $25 million

###### A.6.1.1.1.3.7.2.3.2.12 - Aster [Core]  <!-- UUID: bacfdbb6-46b7-4f86-82c4-fc32f8ed36b7 -->

Users are permitted to hold assets and positions within Aster, in a subaccount controlled under the Arkis master account.

- Exposure Limit: $25 million

##### A.6.1.1.1.3.7.2.4 - Loan Terms [Core]  <!-- UUID: b3fed3ac-7b42-4dfd-b35e-c229598781f7 -->

The documents herein specify the policies and parameters for setting loan agreement terms.

###### A.6.1.1.1.3.7.2.4.1 - Loan Term Definitions [Core]  <!-- UUID: c62a0868-5713-4fec-b6b5-aea342bf149c -->

The subdocuments herein define parameters used to specify loan terms.

###### A.6.1.1.1.3.7.2.4.1.1 - Duration [Core]  <!-- UUID: 5e4d2a15-2ac1-4a59-b2e1-412c5b721c0c -->

The length of time that a loan is issued under specific terms. At the conclusion of the loan duration, the loan may either be payable in full, be rolled over upon mutual agreement with equivalent or different loan terms, or be set up as an “evergreen” loan where the loan is automatically extended at the current terms until recalled.

###### A.6.1.1.1.3.7.2.4.1.2 - Borrow Rate [Core]  <!-- UUID: ab65feec-36fd-4138-bf00-df715fb896e5 -->

The minimum borrow rate that accrues on the outstanding loan balance, expressed as an annual percentage. Actual borrow rate charged may be structured in various ways including fixed rate, fixed spread vs a benchmark, performance fee or profit sharing based, or combination of the above. However, loans may not be issued with borrow cost structures below the values specified in this Loan Terms section.

###### A.6.1.1.1.3.7.2.4.2 - Loan Terms Current Configuration [Core]  <!-- UUID: 5f14d3d4-7def-4cbc-b6d8-3775c8262568 -->

The subdocuments herein specify the currently active parameters for loan terms that fall within Spark’s operational mandate.

###### A.6.1.1.1.3.7.2.4.2.1 - Duration [Core]  <!-- UUID: fa2dceca-3851-4844-8013-a399ddcba9b3 -->

Loans may be issued for the following durations:

- Revolving / evergreen / demand
- Fixed term up to 1 month

###### A.6.1.1.1.3.7.2.4.2.2 - Borrow Rate [Core]  <!-- UUID: 2bdfe55f-7788-480a-800c-09845c9dcd6b -->

The minimum borrow rate for loans via the Arkis infrastructure must be the greater of the following at the time of issuance or renewal:

- Sky Savings Rate + 0.3%
- SOFR

##### A.6.1.1.1.3.7.2.5 - Recall and Acceleration [Core]  <!-- UUID: d234e0ca-af2f-4cab-8f84-6e5a39650b05 -->

The documents herein provide details of how and when loans should be recalled, accelerated, or liquidated in order to mitigate risk.

###### A.6.1.1.1.3.7.2.5.1 - Borrower Insolvency [Core]  <!-- UUID: 8f7c70ad-b083-46fa-9550-3f2ae263c293 -->

If a borrower becomes insolvent or enters administration, any outstanding debts facilitated via the Arkis protocol become due and payable immediately. If the borrower does not repay the debt promptly, collateral may be liquidated to protect the interests of the lender.

###### A.6.1.1.1.3.7.2.5.2 - Unapproved Products [Core]  <!-- UUID: a51aef25-bf7e-4467-9678-0b1ea59fb47e -->

If a borrower trades unapproved assets or products, this will be discounted or penalized via the margin calculation as noted in section [A.6.1.1.1.3.7.2.2.5 - Unapproved Assets and Products](5163ebb9-a425-4df6-aba9-b483e8a482c1). Repeated or serious instances of holding unapproved positions may result in the position being liquidated to protect the interests of the lender.

###### A.6.1.1.1.3.7.2.5.3 - Borrow Rate Shortfall [Core]  <!-- UUID: a81f2f5d-796f-49e0-ac34-dbc5650ee2fe -->

If the borrow rate charged on a loan falls below the borrow rate threshold specified in [A.6.1.1.1.3.7.2.4.2.2 - Borrow Rate](2bdfe55f-7788-480a-800c-09845c9dcd6b), either due to variation in the borrow rate itself (e.g., via profit sharing mechanisms) or because the benchmark rate(s) have increased, Spark must recall the debt or adjust the borrow rate at the earliest opportunity.

###### A.6.1.1.1.3.7.2.5.4 - Parameter Updates in Non Emergency Situations [Core]  <!-- UUID: 50fa8061-8133-4765-a17c-4941634a6ff5 -->

Spark may update approved assets and products, risk parameters, and other details of the Arkis Infrastructure product or allocation strategy into the Arkis protocol via governance. If a previously issued loan no longer conforms with Spark’s current operational mandate due to a non-emergency parameter update, Spark will recall the loan at the earliest possible opportunity, while respecting the agreed loan duration.

###### A.6.1.1.1.3.7.2.5.5 - Emergency Parameter Updates [Core]  <!-- UUID: 4d3f3e27-a0b6-430a-b9b4-ccf48bc49cbb -->

If market conditions or other factors create an immediate and severe risk of capital impairment, Spark and Arkis are empowered to implement immediate changes to risk parameters and configuration to mitigate risk. Actions taken may include preventing new loans or draws on existing loans, adjusting risk parameters of existing positions including increasing margin requirements or haircuts, demanding immediate repayment, up to and including liquidating high risk positions.

##### A.6.1.1.1.3.7.2.6 - Delegation of Rights and Responsibilities [Core]  <!-- UUID: 404a62a2-6918-44e3-9809-1fec0b7ca2a1 -->

Spark Asset Foundation is the legal owner of funds allocated via the Spark Liquidity Layer and is the entity responsible for the Arkis onboarding and capital allocation relationship. Spark Asset Foundation will be empowered to exercise all rights and responsibilities with respect to the Arkis Infrastructure capital allocation activities via the Arkis protocol, for the benefit of the Spark ecosystem and according to generally accepted business practices and Spark Asset Foundation’s professional judgement.

##### A.6.1.1.1.3.7.2.7 - Account Management [Core]  <!-- UUID: d55a80b7-f3e9-43b2-831c-0f41bbbb7b68 -->

The documents herein define the requirements for controlling and managing offchain accounts and permissions related to Arkis Infrastructure.

###### A.6.1.1.1.3.7.2.7.1 - Critical Actions [Core]  <!-- UUID: 8b7e62e7-95f3-40a9-bc3e-22b6645e59cf -->

Critical actions are actions that could conceivably result in the loss of funds if they were executed maliciously or without authorization. The critical actions include:

- Adding a withdrawal address to the whitelist
- Adding or removing a signer from the account approvals policy
- Changing the approval quorum
- Transferring funds to an address under control of an external entity other than Spark Asset Foundation, Spark Foundation, or the Spark Liquidity Layer

###### A.6.1.1.1.3.7.2.7.2 - Address Whitelist [Core]  <!-- UUID: 2f4882cd-ddbf-4419-b69d-b5d6075d702c -->

Accounts shall only whitelist addresses for withdrawals to either an approved collateral agent (which will transfer received funds to borrowers as part of loan origination) or to the Spark Liquidity Layer.

###### A.6.1.1.1.3.7.2.7.3 - Quorum and Signers [Core]  <!-- UUID: 4c8b20c3-e723-4304-904f-7d7f8de5fc8b -->

Accounts must require a quorum of at least 3 signers for Critical Actions. It must not be possible for quorum to be met with signers from a single entity (no single entity will have enough signers to meet the quorum alone, and each critical action will therefore require approval from signers from at least 2 independent entities).

Signers may be sourced from any of the following entities: Spark Asset Foundation (including legal council), Phoenix Labs, Spark Operational Facilitator.

###### A.6.1.1.1.3.7.2.7.4 - Transfers [Core]  <!-- UUID: cffebd02-baee-4b4c-809d-35d4b90246e6 -->

Funds may only be transferred to a collateral agent after confirmation that all necessary steps proceeding loan origination have been completed, including execution of final MLA and provision of configuration file for the loan to the custodian and/or collateral agent.

Funds may be transferred to the designated address for Spark Liquidity Layer at any time without restriction.

### A.6.1.1.1.3.8 - Offchain Collateralized Lending [Core]  <!-- UUID: 7905b0d3-4269-4ba5-a3e2-fdb327b087f4 -->

The documents herein specify Spark’s strategy and operational processes for allocating capital via offchain lending arrangements with collateral secured in qualified custodians.

#### A.6.1.1.1.3.8.1 - Operational Process Definition [Core]  <!-- UUID: 8142b2db-e601-4222-a411-5a5caeb4009b -->

The documents herein define the process for updating Offchain Collateralized Lending policies and procedures.

##### A.6.1.1.1.3.8.1.1 - Offchain Collateralized Lending Policy Changes [Core]  <!-- UUID: c9ef7b0f-ed76-42d5-baa8-6afcd288fd58 -->

Changes to Offchain Collateralized Lending policies are implemented using the Root Edit Primitive.

##### A.6.1.1.1.3.8.1.2 - Offchain Collateralized Lending Policy Change Execution [Core]  <!-- UUID: c91355f0-4a54-4dd9-a13d-f40f8c515994 -->

Approved changes to Offchain Collateralized Lending policies are executed by either Spark Governance (for onchain updates under Spark governance admin control), or via the Spark Asset Foundation account held at relevant custodian(s) and related admin panel(s) (for offchain components). Policy changes must be executed promptly after Root Edit Primitive approval. If policy changes are not executed as required, Spark must remove all funding allocated through the Offchain Collateralized Lending infrastructure as soon as reasonably practicable.

#### A.6.1.1.1.3.8.2 - Policies and Mandate [Core]  <!-- UUID: b3ebb481-d63f-45d7-9c9b-93a3a7be1f6d -->

The documents herein define the currently active policies and mandate for allocation via Offchain Collateralized Lending arrangements.

##### A.6.1.1.1.3.8.2.1 - Counterparty Requirements [Core]  <!-- UUID: 5a57a6c6-f88d-439a-9e8b-f11068438bf6 -->

Borrowers funded via Offchain Collateralized Lending must be duly registered by competent authorities in their primary jurisdiction, and must not be subject to sanctions by the US, UK, EU, or UN. Responsibility for verifying KYC/KYB and meeting related compliance requirements is handled by venues (custodians and/or collateral agents) during the borrower onboarding process.

Borrowers must not be insolvent at the time of loan origination or renewal. Borrowers will self-certify their solvency as part of loan agreements. If a borrower becomes insolvent or enters administration while having an active loan, the entire loan amount becomes due and payable and the collateral agent or custodian may immediately liquidate collateral to recover the loan balance.

##### A.6.1.1.1.3.8.2.2 - Marginable Assets [Core]  <!-- UUID: 137b6e3a-b6c7-4660-b135-8aff765a57a0 -->

The documents herein define the assets or positions that are accepted as margin collateral within Offchain Collateralized Lending arrangements funded by Spark.

###### A.6.1.1.1.3.8.2.2.1 - Marginable Assets Parameters Definitions [Core]  <!-- UUID: a8b82143-da87-47bb-8c68-5ce367ed629c -->

The subdocuments herein define the specific risk parameters or limits applicable to each accepted margin collateral asset.

###### A.6.1.1.1.3.8.2.2.1.1 - Initial LTV [Core]  <!-- UUID: 5c35ebd7-da09-4f2e-b709-e081f654609e -->

The maximum ratio of loan amount to collateral value permitted when a new loan is issued. Additionally, when a margin call is triggered, the borrower must return the position to an LTV ratio equal or less than the Initial LTV. Borrowers may only withdraw collateral from their position if their position LTV remains below the Initial LTV threshold after the withdrawal.

###### A.6.1.1.1.3.8.2.2.1.2 - Maintenance LTV [Core]  <!-- UUID: 7f7e0f99-83d7-45b4-b9ba-4ce80bdfe666 -->

The maximum ratio of loan amount to collateral value above which a margin call is triggered. When triggered, the borrower is notified by the collateral agent to meet the margin call by reducing the position LTV to equal or less than the Initial LTV within the Cure Period.

###### A.6.1.1.1.3.8.2.2.1.3 - Liquidation LTV [Core]  <!-- UUID: 5fdde1df-a2b7-4310-9d63-98392e1fdfcd -->

The maximum ratio of loan amount to collateral value above which a position may be liquidated immediately, regardless of whether there is an outstanding margin call in effect.

###### A.6.1.1.1.3.8.2.2.1.4 - Exposure Limit [Core]  <!-- UUID: ee8d2d3f-b5cf-4391-8081-81de0a5936c7 -->

The maximum aggregate exposure to a given asset permitted within Spark funded Offchain Collateralized Lending arrangements. Exposure is calculated based on total loan amounts secured by collateral backages.

###### A.6.1.1.1.3.8.2.2.1.5 - Staked and Wrapped Versions [Core]  <!-- UUID: 634e54de-0818-4307-aeb9-c9aae2d0a774 -->

The acceptable staked or wrapped versions of a given marginable asset, including non native bridged versions of an asset.

###### A.6.1.1.1.3.8.2.2.2 - Marginable Assets Current Configuration [Core]  <!-- UUID: 34d75d61-1df2-4921-890b-cb4ed68abe25 -->

The subdocuments herein define the assets currently accepted as margin collateral within Spark funded Offchain Collateralized Lending arrangements.

###### A.6.1.1.1.3.8.2.2.2.1 - Bitcoin (BTC) [Core]  <!-- UUID: 8fd4dc40-59b1-47ae-ba5c-4782b9550245 -->

- Initial LTV: 80%
- Maintenance LTV: 85%
- Liquidation LTV: 90%
- Exposure limit: Unlimited
- Staked and wrapped versions: Coinbase cbBTC, Lombard LBTC, Bitgo/Bitglobal WBTC

###### A.6.1.1.1.3.8.2.2.2.2 - Ether (ETH) [Core]  <!-- UUID: f6d82898-b431-43d5-8c0b-3b8e4aa9e236 -->

- Initial LTV: 70%
- Maintenance LTV: 85%
- Liquidation LTV: 90%
- Exposure limit: Unlimited
- Staked and wrapped versions: WETH, Lido stETH, Etherfi weETH, Alluvial lsETH, native staking with approved providers

###### A.6.1.1.1.3.8.2.2.2.3 - Ripple (XRP) [Core]  <!-- UUID: ff7bf52c-e89d-4b2e-a55b-8c1b704a48f5 -->

- Initial LTV: 60%
- Maintenance LTV: 70%
- Liquidation LTV: 80%
- Exposure limit: $25 million
- Staked and wrapped versions: None

###### A.6.1.1.1.3.8.2.2.2.4 - Solana (SOL) [Core]  <!-- UUID: b84f4195-c79d-477f-9361-3a9687ff5934 -->

- Initial LTV: 70%
- Maintenance LTV: 80%
- Liquidation LTV: 85%
- Exposure limit: $100 million
- Staked and wrapped versions: JitoSOL, native staking with approved providers

###### A.6.1.1.1.3.8.2.2.2.5 - Hyperliquid (HYPE) [Core]  <!-- UUID: e5d67f78-23cd-423c-80e4-2f9a4908a17c -->

- Initial LTV: 60%
- Maintenance LTV: 70%
- Liquidation LTV: 80%
- Exposure limit: $25 million
- Staked and wrapped versions: Kinetiq kHYPE, native staking with approved providers

###### A.6.1.1.1.3.8.2.2.2.6 - Gold (AU) [Core]  <!-- UUID: 8db0e30b-c85c-4a92-8afd-84af4bfdfe92 -->

- Initial LTV: 80%
- Maintenance LTV: 85%
- Liquidation LTV: 90%
- Exposure limit: $500 million (of which, not more than $50 million from XAUM)
- Staked and wrapped versions: Tether XAUT, Paxos PAXG, Matrixdock XAUM

##### A.6.1.1.1.3.8.2.3 - Approved Venues [Core]  <!-- UUID: b03b3354-1290-41d6-89fe-d841c3a79d3c -->

The documents herein define the venues where liquidity and collateral related to Offchain Collateralized Lending arrangements may be held.

###### A.6.1.1.1.3.8.2.3.1 - Approved Venues Parameters Definitions [Core]  <!-- UUID: 22fe93af-9188-4308-95ba-ac9917196290 -->

The subdocuments herein define the specific risk parameters or limits applicable to each approved venue.

###### A.6.1.1.1.3.8.2.3.1.1 - Exposure Limit [Core]  <!-- UUID: eeba9879-a5b3-4a85-b9ad-6df6c970f8d3 -->

The exposure limit is the maximum amount of account value, defined in USD based on current value of assets and positions, inclusive of collateral, idle liquidity pending loan issuance, and repaid loan proceeds pending withdrawal or reinvestment, that may be held within each approved venue or under management of each collateral agent.

###### A.6.1.1.1.3.8.2.3.1.2 - Collateral Agent [Core]  <!-- UUID: 7552fd04-f619-4b13-ad86-50b00f6cdfc8 -->

The collateral agent performs certain critical loan servicing functions on behalf of Spark Asset Foundation as lender, including issuing margin calls, performing liquidations, returning loan proceeds to the lender and excess collateral or liquidation proceeds to borrowers. This service may be provided by an affiliate of the venue/custodian, or by a third party. One venue may have multiple approved collateral agents, each with their own maximum exposure limit.

###### A.6.1.1.1.3.8.2.3.2 - Approved Venues Current Configuration [Core]  <!-- UUID: 817e1360-ac36-4282-9604-1ab625755450 -->

The subdocuments herein define the currently approved venues where liquidity and collateral assets may be held for Spark’s Offchain Collateralized Lending activity.

###### A.6.1.1.1.3.8.2.3.2.1 - Anchorage [Core]  <!-- UUID: fd82a25b-ef66-4fa4-b849-f2e34c9a575e -->

Offchain Collateralized Lending may be facilitated via Anchorage, which is approved to hold collateral as well as lending liquidity related to such loans.

- Venue exposure Limit: $1 billion
- Collateral Agent(s):
    - Anchorage Innovations: $1 billion

##### A.6.1.1.1.3.8.2.4 - Loan Terms [Core]  <!-- UUID: f80317f5-cf93-4610-b35a-2e60c94011d0 -->

The documents herein specify the policies and parameters for setting loan agreement terms.

###### A.6.1.1.1.3.8.2.4.1 - Loan Terms Definitions [Core]  <!-- UUID: b28fabb2-4e1e-4140-92cf-b6190d5e0031 -->

The subdocuments herein define parameters used to specify loan terms.

###### A.6.1.1.1.3.8.2.4.1.1 - Duration [Core]  <!-- UUID: d8c712e4-b71d-4e0a-812e-e86bb01af27f -->

The length of time that a loan is issued under specific terms. At the conclusion of the loan duration, the loan may either be payable in full, be rolled over upon mutual agreement with equivalent or different loan terms, or be set up as an "evergreen" loan where the loan is automatically extended at the current terms until recalled.

###### A.6.1.1.1.3.8.2.4.1.2 - Borrow Rate [Core]  <!-- UUID: 0ea26c9e-3dc5-43c0-8cc7-d9075afce8f3 -->

The minimum borrow rate that accrues on the outstanding loan balance, expressed as an annual percentage. Actual borrow rate charged may be structured in various ways including fixed rate, fixed spread vs a benchmark, performance fee or profit sharing based, or combination of the above. However, loans may not be issued with borrow cost structures below the values specified in this Loan Terms section.

###### A.6.1.1.1.3.8.2.4.1.3 - Margin Call Cure Period [Core]  <!-- UUID: 0d3f2142-7069-41c6-8b79-e4972a3e4bdc -->

The maximum permitted amount of time for a borrower to meet a margin call before being liquidated.

###### A.6.1.1.1.3.8.2.4.2 - Loan Terms Current Configuration [Core]  <!-- UUID: df6eb53c-1cad-4fcc-97b8-d5bd3ca55ee8 -->

The subdocuments herein specify the currently active parameters for loan terms that fall within Spark’s operational mandate.

###### A.6.1.1.1.3.8.2.4.2.1 - Duration [Core]  <!-- UUID: bc92d589-b079-41f8-a3fa-37300aef91b1 -->

Loans may be issued for the following durations:

- Revolving / evergreen / payable on demand
- Fixed rate, fixed term for up to 6 months

###### A.6.1.1.1.3.8.2.4.2.2 - Borrow Rate [Core]  <!-- UUID: 67c9fae6-6911-4341-b94b-c03e9305c266 -->

The minimum borrow rate for loans via Offchain Collateralized Lending arrangements must be the greater of the following at the time of issuance or renewal:

- Sky Savings Rate + 0.3%
- SOFR + 0%

###### A.6.1.1.1.3.8.2.4.2.3 - Margin Call Cure Period [Core]  <!-- UUID: aedd10ee-5db1-4d38-b720-c451608c19e1 -->

The maximum permitted margin call cure period is 24 hours from the time the Maintenance LTV is breached.

##### A.6.1.1.1.3.8.2.5 - Recall and Acceleration [Core]  <!-- UUID: 19eeb757-6167-4aff-87f4-5f97331ab7e6 -->

The documents herein provide details of how and when loans should be recalled, accelerated, or liquidated in order to mitigate risk.

###### A.6.1.1.1.3.8.2.5.1 - Borrower Insolvency [Core]  <!-- UUID: 86e1af9b-26e8-4170-a4a9-5b7285d861c2 -->

If a borrower becomes insolvent or enters administration, any outstanding debts facilitated via Offchain Collateralized Lending arrangements become due and payable immediately. If the borrower does not repay the debt promptly, collateral may be liquidated to protect the interests of the lender.

###### A.6.1.1.1.3.8.2.5.2 - Cross Default [Core]  <!-- UUID: a080d478-dcc8-4830-be67-136f810422d0 -->

If a borrower defaults on or is liquidated in one Offchain Collateralized Loan funded by Spark, Spark may accelerate any other outstanding loans from the same borrower.

###### A.6.1.1.1.3.8.2.5.3 - Borrow Rate Shortfall [Core]  <!-- UUID: 7953c6c6-337b-4d28-889c-e96fc44ab65d -->

If the borrow rate charged on a loan falls below the borrow rate threshold specified in [A.6.1.1.1.3.8.2.4.2.2 - Borrow Rate](67c9fae6-6911-4341-b94b-c03e9305c266), Spark must recall the debt or adjust the borrow rate at the earliest opportunity.

###### A.6.1.1.1.3.8.2.5.4 - Parameter Updates in Non Emergency Situations [Core]  <!-- UUID: 936fa08a-3148-4c18-9aa2-420780ac884a -->

Spark may update approved assets, risk parameters, and other details of the Offchain Collateralized Lending program via governance. If a previously issued loan no longer conforms with Spark’s current operational mandate due to a non-emergency parameter update, Spark will recall the loan at the earliest possible opportunity, while respecting the agreed loan duration.

###### A.6.1.1.1.3.8.2.5.5 - Emergency Parameter Updates [Core]  <!-- UUID: 72ceaca8-788a-446b-90ac-c41ca65460c3 -->

If market conditions or other factors create an immediate and severe risk of capital impairment, Spark is empowered to implement immediate changes to risk parameters and configuration to mitigate risk. Actions taken may include preventing new loans or draws on existing loans, adjusting configurable parameters, or requesting accelerated repayment and return of capital.

##### A.6.1.1.1.3.8.2.6 - Delegation of Rights and Responsibilities [Core]  <!-- UUID: 4a181787-661e-4c97-9eec-0eaaa4d632c5 -->

Spark Asset Foundation is the legal owner of funds allocated via the Spark Liquidity Layer and onboarded entity for custodians and collateral agents. Spark Asset Foundation will be empowered to exercise all rights and responsibilities with respect to the Offchain Collateralized Lending allocation activities and account management, for the benefit of the Spark ecosystem and according to generally accepted business practices and Spark Asset Foundation’s professional judgement. Spark Asset Foundation may delegate certain operational functions to Phoenix Labs at its discretion, including risk underwriting, sourcing prospective borrowers, and deal negotiation.

##### A.6.1.1.1.3.8.2.7 - Account Management [Core]  <!-- UUID: d6284e0b-441e-478b-b465-9053cd13ffaa -->

The documents herein define the requirements for controlling and managing offchain custody accounts used within Offchain Collateralized Lending arrangements.

###### A.6.1.1.1.3.8.2.7.1 - Critical Actions [Core]  <!-- UUID: b501dc78-2452-40d9-acd7-7a89eef70e25 -->

Critical actions are actions that could conceivably result in the loss of funds if they were executed maliciously or without authorization. The critical actions include:

- Adding a withdrawal address to the whitelist
- Adding or removing a signer from the account approvals policy
- Changing the approval quorum
- Transferring funds to an address outside of the preexisting withdrawal address whitelist

###### A.6.1.1.1.3.8.2.7.2 - Address Whitelist [Core]  <!-- UUID: 8787ecfc-d1f5-45fa-a261-c0ff12a20538 -->

Accounts shall only whitelist addresses for withdrawals to either an approved collateral agent for the relevant custodian, to borrower addresses in connection with offchain collateralized lending agreements, or to the Spark Liquidity Layer.

###### A.6.1.1.1.3.8.2.7.3 - Quorum and Signers [Core]  <!-- UUID: 8f3822f2-8403-444f-9db7-2a9fa2da552f -->

Accounts must require a quorum of at least 3 signers for Critical Actions. It must not be possible for quorum to be met with signers from a single entity (no single entity will have enough signers to meet the quorum alone, and each critical action will therefore require approval from signers from at least 2 independent entities).

Signers may be sourced from any of the following entities: Spark Asset Foundation (including legal council), Phoenix Labs, Spark Operational Executor Agent.

###### A.6.1.1.1.3.8.2.7.4 - Transfers [Core]  <!-- UUID: 28517c27-b028-4b7a-9fea-6a70ae706468 -->

Funds may be transferred to a collateral agent or whitelisted address only after Spark Asset Foundation confirmation that all required steps prior to loan disbursement have been completed.

Funds may be transferred to the designated address(es) provided by the custodian or collateral manager for the payment of custody or collateral management service fees as permitted by governance-approved arrangements and upon receipt of a valid invoice.

Funds may be transferred to the designated address for Spark Liquidity Layer at any time without restriction.

### A.6.1.1.1.3.9 - Risk Curation Framework [Core]  <!-- UUID: 78018ebc-c69d-44f6-b602-190edca11483 -->

The documents herein specify Spark’s framework for delegating and executing certain on-chain activities through approved curator roles.

#### A.6.1.1.1.3.9.1 - Operational Process Definition [Core]  <!-- UUID: d0c6aaa3-2d24-41f9-ac1b-51f56feff62f -->

The documents herein define the process for updating Risk Curation Framework policies and procedures.

##### A.6.1.1.1.3.9.1.1 - Risk Curation Framework Changes [Core]  <!-- UUID: ca226501-8073-4830-b5e9-01fa960f17fe -->

Changes to Risk Curation Framework policies are implemented using the Root Edit Primitive.

#### A.6.1.1.1.3.9.2 - Purpose [Core]  <!-- UUID: 86925539-2db1-4a2e-930a-2ee6bc833ccd -->

The Risk Curation Framework defines the conditions under which Spark governance may authorize external contributors to execute approved changes onchain, while preserving governance oversight, timelock protections, and cancellation authorities.

#### A.6.1.1.1.3.9.3 - Curator Roles [Core]  <!-- UUID: 6c3b277c-4acd-4692-939e-203855cff43e -->

The documents herein define the meaning and scope of Curator roles within the Spark ecosystem.

##### A.6.1.1.1.3.9.3.1 - Definition [Core]  <!-- UUID: 3a796888-a39b-47c4-9cb9-6716d3e1c0db -->

A Curator is a specific admin role defined within the Morpho smart contract system.

##### A.6.1.1.1.3.9.3.2 - Scope of Authority [Core]  <!-- UUID: e4fb1a94-cfd8-40d3-ac79-966dd9f8db24 -->

Curators may only execute actions that have been explicitly approved by Spark governance via polling.

##### A.6.1.1.1.3.9.3.3 - Reporting of Curator Actions [Core]  <!-- UUID: 6f64ac9e-daf1-4339-8046-3894e57f4383 -->

All actions taken under a Curator role must be reported by the Curator in the Spark-Prime subsection of the Sky forum within 24 hours of submission. The report should include a transaction hash of the action, the UTC time at which the timelock period for the action elapses, a description of the action being implemented, and a link to the poll which provided governance approval for the action.

#### A.6.1.1.1.3.9.4 - Governance Approval Process [Core]  <!-- UUID: e3ddbd39-ee57-4b17-b66e-8bc823a03098 -->

The documents herein describe the requirements for all Curator actions to be approved by governance.

##### A.6.1.1.1.3.9.4.1 - Polling Requirement [Core]  <!-- UUID: 218f889f-6a5d-46a8-b8a3-cb0a075825c2 -->

All curator-executed changes must be approved in advance by Spark governance through a polling process.

##### A.6.1.1.1.3.9.4.2 - Execution Authority [Core]  <!-- UUID: 48e6eeb9-86c0-4bfa-8be0-e9917d163118 -->

Following successful governance approval, the Curator is authorized to execute the approved change or changes by submitting the corresponding onchain transaction or transactions.

#### A.6.1.1.1.3.9.5 - Timelock Controls [Core]  <!-- UUID: a4f6132e-787f-445a-9290-bd810b9eb93f -->

The documents herein define the requirements for Timelock mechanisms to be used in conjunction with Curator roles.

##### A.6.1.1.1.3.9.5.1 - Timelock Requirement [Core]  <!-- UUID: 9cb30c4c-ecbb-4874-a931-b900b868b888 -->

All admin or privileged controls managed by curator roles must be subject to a minimum timelock delay of three (3) days between scheduling and execution.

##### A.6.1.1.1.3.9.5.2 - Visibility [Core]  <!-- UUID: 4f45b29e-9f94-48d3-940c-1cd6b1f06f4b -->

Pending changes subject to the timelock must be publicly visible onchain for the duration of the delay period.

#### A.6.1.1.1.3.9.6 - Cancellation Authorities [Core]  <!-- UUID: 86153ff2-e3f2-44af-b19b-678cbbac27f5 -->

The documents herein define the cancellation mechanisms and authorities for pending actions within the Timelock period.

##### A.6.1.1.1.3.9.6.1 - Authorized Cancellers [Core]  <!-- UUID: f87333c8-ec5e-4483-83a9-791e1f9f9634 -->

Pending changes within the timelock must be able to be cancelled by any of the following: the Spark subdao proxy, or a designated guardian role.

##### A.6.1.1.1.3.9.6.2 - Cancellation Reasons [Core]  <!-- UUID: 0e572cad-bdf2-437f-b272-0cd634424b19 -->

Pending changes may be cancelled for the following reasons: misalignment or conflict with the Sky Atlas or Spark Artifact; excessive or unacceptable risk, as identified by the Sky Core Council or Spark Risk Council; emergency situations, as defined in the Sky Atlas in [A.1.9 - Emergency Response System](1d940c6d-02ce-4c17-8057-cef13c1cc7ad); or cancellation requested by the Curator.

##### A.6.1.1.1.3.9.6.3 - Guardian Role [Core]  <!-- UUID: 900c4a0d-ed93-41ad-b914-f84d50d6940e -->

A Guardian is a specific admin role defined within the Morpho smart contract system, also referred to as a Sentinel in some cases.

###### A.6.1.1.1.3.9.6.3.1 - Guardian Independence [Core]  <!-- UUID: ea50c8da-008e-4f0f-b2df-ac666d5faf13 -->

The Guardian must be independent from the Curator for each specific smart contract instance, meaning there must be no overlap between approvers, signers, contributors, role owners, or entities between the two roles. Compromise or misalignment of the Curator role should not in itself create risk of the Guardian role also becoming compromised.

###### A.6.1.1.1.3.9.6.3.2 - Guardian Reporting [Core]  <!-- UUID: ac45b63b-3394-49d6-aab7-ff67b1d4fd0c -->

All actions taken under a Guardian role must be reported by the Guardian in the Spark-Prime subsection of the Sky forum within 24 hours of submission. The report should include a transaction hash of the action, a description of the action, general reasoning for the action, and justification for the action being within the governance-approved mandate.

#### A.6.1.1.1.3.9.7 - Delegated Risk Curation Instances [Core]  <!-- UUID: b3b590f9-0d3e-4c4a-a9e5-5b114d3c0ae4 -->

Spark governance approves the following instances of delegated risk curation authority. Each instance is governed independently and subject to the Risk Curation Framework.

##### A.6.1.1.1.3.9.7.1 - Instance Parameter Definitions [Core]  <!-- UUID: 3d1e7988-f513-4632-a653-69d420379998 -->

The subdocuments herein describe the parameters which must be defined and maintained for each instance of delegated risk curation authority.

###### A.6.1.1.1.3.9.7.1.1 - Instance Name [Core]  <!-- UUID: e6fadf50-32a8-4c12-9b01-2ac1b9f8c1fb -->

The name of the product, vault, or protocol where authority is delegated.

###### A.6.1.1.1.3.9.7.1.2 - Contract Address [Core]  <!-- UUID: 6b237359-81f4-4089-a1cb-9674cc029fcd -->

The specific onchain contract address and the ownership or admin role over which curator authority is delegated.

###### A.6.1.1.1.3.9.7.1.3 - Curator [Core]  <!-- UUID: 35326711-9bda-4880-a716-bbb0eb6a3762 -->

The entity or entities serving in the curator role, including how the role is controlled at the smart contract level, such as a multisig address and approval threshold or an alternative control mechanism.

###### A.6.1.1.1.3.9.7.1.4 - Scope of Curator Authority [Core]  <!-- UUID: 0d5c17a2-a4a3-4f81-af4c-49839bc7b36f -->

The specific execution actions the curator is permitted to take, subject to prior Spark governance approval via polling.

###### A.6.1.1.1.3.9.7.1.5 - Guardian [Core]  <!-- UUID: 817391bd-3748-479c-846e-f8d3e3ec56f4 -->

The entity or entities serving in the guardian role, including how the role is controlled at the smart contract level and how cancellation authority is exercised.

##### A.6.1.1.1.3.9.7.2 - Approved Instances [Core]  <!-- UUID: 5f30c335-8f12-4cc7-becd-f542a7546463 -->

The documents herein enumerate the current approved instances of delegated risk curation authority.

###### A.6.1.1.1.3.9.7.2.1 - Spark USDS Morpho Vault - Ethereum Mainnet [Core]  <!-- UUID: 3e8ed24b-da4a-4c3f-9a74-c3dd6a557abf -->

The Spark USDS Morpho Vault on Ethereum Mainnet is an approved instance with the following details:

- Instance Name: Spark USDS Morpho Vault (Ethereum Mainnet)
- Contract Address: `0xe41a0583334f0dc4E023Acd0bFef3667F6FE0597`
- Curator: Soter Labs, implemented via a Gnosis Safe multisig at `0x0f963A8A8c01042B69054e787E5763ABbB0646A3`, requiring a 3 of 5 signer approval threshold
- Scope of Curator Authority: Execution of risk parameter changes and operational actions approved by Spark governance polls
- Guardian: Spark Foundation, implemented via a Gnosis Safe multisig at `0xf5748bBeFa17505b2F7222B23ae11584932C908B`, requiring a 3 of 5 signer approval threshold

###### A.6.1.1.1.3.9.7.2.2 - Spark Blue Chip USDC Morpho Vault - Ethereum Mainnet [Core]  <!-- UUID: 603cf96e-5819-4e3d-942e-5290dd000847 -->

The Spark Blue Chip USDC Morpho Vault on Ethereum mainnet is an approved instance with the following details:

- Instance Name: Spark Blue Chip USDC Morpho Vault (Ethereum Mainnet)
- Contract Address: `0x56A76b428244a50513ec81e225a293d128fd581D`
- Curator: Soter Labs, implemented via a Gnosis Safe multisig at `0x0f963A8A8c01042B69054e787E5763ABbB0646A3`, requiring a 3 of 5 signer approval threshold
- Scope of Curator Authority: Execution of risk parameter changes and operational actions approved by Spark governance polls
- Guardian: Spark Foundation, implemented via a Gnosis Safe multisig at `0xf5748bBeFa17505b2F7222B23ae11584932C908B`, requiring a 3 of 5 signer approval threshold

###### A.6.1.1.1.3.9.7.2.3 - Spark Blue Chip USDT Morpho Vault - Ethereum Mainnet [Core]  <!-- UUID: 5ef1e78f-e1d2-4b09-b00c-618e36ccb2d8 -->

The Spark Blue Chip USDT Morpho Vault on Ethereum mainnet is an approved instance with the following details:

- Instance Name: Spark Blue Chip USDT Morpho Vault (Ethereum Mainnet)
- Contract Address: `0xc7CDcFDEfC64631ED6799C95e3b110cd42F2bD22`
- Curator: Soter Labs, implemented via a Gnosis Safe multisig at `0x0f963A8A8c01042B69054e787E5763ABbB0646A3`, requiring a 3 of 5 signer approval threshold
- Scope of Curator Authority: Execution of risk parameter changes and operational actions approved by Spark governance polls
- Guardian: Spark Foundation, implemented via a Gnosis Safe multisig at `0xf5748bBeFa17505b2F7222B23ae11584932C908B`, requiring a 3 of 5 signer approval threshold

###### A.6.1.1.1.3.9.7.2.4 - Spark USDC Morpho Vault - Base [Core]  <!-- UUID: 85722a93-ec30-4e7f-883c-adde12b0ac6b -->

The Spark USDC Morpho Vault on Base is an approved instance with the following details:

- Instance Name: Spark USDC Morpho Vault (Base)
- Contract Address: `0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A`
- Curator: Soter Labs, implemented via a Gnosis Safe multisig at `0x0f963A8A8c01042B69054e787E5763ABbB0646A3`, requiring a 3 of 5 signer approval threshold
- Scope of Curator Authority: Execution of risk parameter changes and operational actions approved by Spark governance polls
- Guardian: Spark Foundation, implemented via a Gnosis Safe multisig at `0xf5748bBeFa17505b2F7222B23ae11584932C908B`, requiring a 3 of 5 signer approval threshold

### A.6.1.1.1.3.10 - Confidential Strategic Integrations and Deployments [Core]  <!-- UUID: 5902deeb-0c4d-4df6-89bb-22212b81e96a -->

The provisions herein establish Spark’s framework for confidential strategic integrations and pre-launch deployment activities conducted subject to applicable confidentiality obligations.

#### A.6.1.1.1.3.10.1 - Purpose [Core]  <!-- UUID: 80b870fa-c09a-4fbf-89f5-5de110761cd9 -->

The Confidential Strategic Integrations and Deployments framework defines the conditions under which Designated Contributors may enter into confidential strategic arrangements and perform pre-launch operational readiness activities, including deployment and configuration of protocol infrastructure, while confidentiality obligations remain in effect. The framework does not authorize deployment or allocation of Spark protocol funds except as expressly approved through Spark governance processes.

#### A.6.1.1.1.3.10.2 - Designated Contributors [Core]  <!-- UUID: 41241e46-3b2a-464c-8f4f-30a8f80a2103 -->

The following entities are authorized to perform actions on behalf of Spark under the Confidential Strategic Integrations and Deployments Framework: Spark Foundation may perform actions under this Confidential Strategic Integrations and Deployments framework, directly or through contractors or service providers authorized to act on its behalf.

#### A.6.1.1.1.3.10.3 - Permitted Actions [Core]  <!-- UUID: 56281438-63f9-46d4-a382-39a790a3bba1 -->

Designated Contributors are permitted to take any actions reasonably necessary to facilitate the deployment, configuration, testing, maintenance, and operational readiness of a Confidential Strategic Integration and Deployment. Such actions may include deployment and configuration of smart contracts, establishment of multisigs or administrative control systems, deployment and configuration of Spark Savings or Morpho vault infrastructure, operation of relayer or frontend infrastructure, and related implementation activities.

Confidential Strategic Integrations and Deployments may remain undisclosed while applicable confidentiality obligations remain in effect, provided that the governance acceptance and disclosure requirements set forth in this section are satisfied.

For the avoidance of doubt, this authorization does not permit deployment or allocation of Spark treasury assets, Spark Liquidity Layer assets, governance-controlled capital, or other protocol-owned funds, except as otherwise expressly authorized through Spark governance processes. Nothing herein prohibits the movement or allocation of assets voluntarily deposited by users into a Confidential Strategic Partnership and Deployment through preconfigured product functionality established prior to public launch, provided that such functionality remains subject to the limitations and governance acceptance requirements set forth in this section.

#### A.6.1.1.1.3.10.4 - Incentives and Rewards Obligations [Core]  <!-- UUID: a4cd23dc-5c71-4a3a-8d95-ad09c658e0de -->

The yield accrued on Spark Savings vaults deployed under the Confidential Strategic Integrations and Deployments framework may constitute obligations incurred pursuant to this framework, subject to the limitations set forth herein. The onchain parameters and offchain configuration of Spark Savings vaults created under the Confidential Strategic Integrations and Deployments framework will be set such that the total aggregate rewards that may accrue per month will not exceed USD 5 million in value, and the total aggregate rewards outstanding for all Confidential Strategic Integration and Deployment vaults still awaiting Governance Acceptance shall not exceed USD 5 million in value.

#### A.6.1.1.1.3.10.5 - Disclaimers [Core]  <!-- UUID: 60c1b634-399b-423a-b4de-ef63b75791d9 -->

Protocol deployments and products launched under the Confidential Strategic Integrations and Deployments framework are not covered by Spark or Sky insurance, and users bear all risk associated with the deployments and products, including but not limited to hacks, operational or key management failures, illiquidity, insolvency, or failure of a collateral asset. Spark protocol coverage will only be conveyed if Spark governance explicitly votes to extend coverage to a specific deployment or products after public launch and full disclosure of the deployment or product details.

#### A.6.1.1.1.3.10.6 - Governance Acceptance [Core]  <!-- UUID: 6436eedd-35a6-4c89-a518-b2a4bb1d6e1c -->

Any products or protocol elements created under the Confidential Strategic Integrations and Deployments framework must be publicly disclosed and receive explicit acceptance by Spark governance within 6 months of the earlier of: (i) the deployments no longer being subject to confidentiality requirements, or (ii) the deployments having their first interaction with end users (excluding Designated Contributors). Confidential Strategic Integration and Deployment elements that are not approved within this period must be wound down in an orderly fashion.

#### A.6.1.1.1.3.10.7 - Private Ecosystem Review [Core]  <!-- UUID: 52b28880-10d4-4aff-b694-f5278adb3fbb -->

Prior to activation of a Confidential Strategic Integration and Deployment for end user interactions or deposits, Designated Contributors shall confidentially disclose all relevant deployment details to the Spark Risk Council, and to applicable Sky ecosystem governance reviewers designated for confidential ecosystem reviews. Such reviewers may object to a deployment where they identify concerns within the scope of their review authority. If an objection is raised, Designated Contributors shall not activate the deployment for end user interactions or deposits until the identified concerns have been resolved, any required approvals have been obtained, or the deployment has otherwise been cancelled and wound down in an orderly fashion.
