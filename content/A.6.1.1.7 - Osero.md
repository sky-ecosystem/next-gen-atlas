# A.6.1.1.7 - Osero [Core]  <!-- UUID: eba0dcc7-e135-496f-b866-342deeb91dc4 -->

The documents herein specify all of the logic for Osero, including Osero's strategy and how it uses the Sky Primitives to operationalize this strategy.

## A.6.1.1.7.1 - Introduction [Core]  <!-- UUID: 963a72da-503f-4150-922e-94155924be8d -->

Osero is an Agent focused on building credit infrastructure for onchain and traditional finance, with a focus on USD₮ liquidity. In addition to allocating capital to scale Sky's collateral portfolio, Osero serves as a platform enabling stablecoin distribution hubs—including exchanges, wallets, and neobanks—to access institutional grade lending infrastructure underpinning USDS through a suite of products.

## A.6.1.1.7.2 - Sky Primitives [Core]  <!-- UUID: 0d6f6016-eaf1-47e2-b8e7-98bf5e4f1dc0 -->

The documents herein implement the Sky Primitives for Osero. See [A.2.2.1.5 - Primitives](947a5b27-d2dc-41e4-b6fd-696e35e2929d).

### A.6.1.1.7.2.1 - Genesis Primitives [Core]  <!-- UUID: 7594cfaf-c101-4379-976e-aba279add723 -->

The documents herein implement the Genesis Primitives for Osero. See [A.2.2.5 - Genesis Primitives](3d5e3668-8333-4908-adcc-5784cfe7f6b5).

#### A.6.1.1.7.2.1.1 - Agent Creation Primitive [Core]  <!-- UUID: 1049c46a-0222-4101-ad86-b8c75c73ffd6 -->

The documents herein contain all data and specifications for Osero's Instance of the Agent Creation Primitive. See [A.2.2.5.1 - Agent Creation Primitive](82b95f6d-4883-4f08-ac3a-9d8189013fbe).

##### A.6.1.1.7.2.1.1.1 - Primitive Hub Document [Core]  <!-- UUID: e8203aca-ee78-41c6-ad35-8f7324d9a277 -->

The documents herein organize all base information relevant to Osero's usage of the Agent Creation Primitive.

###### A.6.1.1.7.2.1.1.1.1 - Global Activation Status [Core]  <!-- UUID: 7e7f3004-1886-4783-8360-561ef927ff35 -->

`Completed`

###### A.6.1.1.7.2.1.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 77c294b2-2d74-4a90-8c43-982abcc64afb -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.1.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: ef331af9-dfd3-4b0c-abd2-75ce104bf1ca -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.1.1.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 211ee879-956d-4e04-aa8a-2599c9872e86 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.1.1.3.1 - Single Instance Configuration Document](a4cd3e49-84c9-44e6-86f2-6a1b34162d50).

###### A.6.1.1.7.2.1.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 383eb03a-1eba-4266-880f-58571f78b719 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.7.2.1.1.1.5 - Hub Data Repository [Core]  <!-- UUID: bdf94e77-b137-4a01-aefb-314b92d49b24 -->

The document herein contains the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.1.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 6a2b403a-772e-47a0-8873-47749729512f -->

The subtrees for archived Invocations and Instances of the Agent Creation Primitive are stored here.

###### A.6.1.1.7.2.1.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 038042c1-bec7-43e5-9a76-81a4a836aa7d -->

The subtrees for failed Invocations of the Agent Creation Primitive are stored here.

###### A.6.1.1.7.2.1.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 31c1d31a-91fb-4487-b65d-8e682044276f -->

The subtrees for Instances of the Agent Creation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.1.1.2 - Active Instances [Core]  <!-- UUID: 99e0c315-2f2a-4d61-b653-70b75c03be0d -->

The Instances of the Agent Creation Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.1.1.3 - Completed Instances [Core]  <!-- UUID: 6ff08b90-e51c-4ab7-abee-ab864131cced -->

The Instances of the Agent Creation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.7.2.1.1.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: a4cd3e49-84c9-44e6-86f2-6a1b34162d50 -->

The documents herein contain the Instance Configuration Document for the Single Agent Creation Primitive Instance.

###### A.6.1.1.7.2.1.1.3.1.1 - Parameters [Core]  <!-- UUID: c5df1f14-67f1-4be4-b4c2-be6ddf68e9cd -->

The documents herein define the parameters of the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.7.2.1.1.3.1.1.1 - Name [Core]  <!-- UUID: e225427b-cf79-4922-a423-b12a23a659c3 -->

The name of the Agent is Osero.

###### A.6.1.1.7.2.1.1.3.1.1.2 - SubProxy Account [Core]  <!-- UUID: bb7586a5-8e85-4d8c-aedc-2b0f76fb826f -->

The address of Osero's SubProxy Account on the Ethereum Mainnet is `0x24fdcd3bFA5C2553e05B2f9AD0365EBC296278D3`.

###### A.6.1.1.7.2.1.1.3.1.1.3 - StarGuard Contract [Core]  <!-- UUID: d3499ce6-c517-49f7-a07e-b321c390470d -->

The address of Osero's StarGuard contract on the Ethereum Mainnet is `0xBfA2D1dA838E55A74c61699e164cDFF8cF0cF0e2`.

###### A.6.1.1.7.2.1.1.3.1.1.3.1 - StarGuard Max Delay [Core]  <!-- UUID: 96060edd-a089-499c-9e96-b90a89bc2c0c -->

The Osero StarGuard `maxDelay` is seven (7) days.

###### A.6.1.1.7.2.1.1.3.1.1.4 - Genesis Account [Core]  <!-- UUID: a5674a63-9d57-4fd9-9b66-ec653f49afab -->

The address of Osero's Genesis Account will be specified in a future iteration of the Osero Artifact.

###### A.6.1.1.7.2.1.1.3.1.1.5 - Foundation [Core]  <!-- UUID: 62d84951-7f77-423e-b5df-960faf6b2fd0 -->

The Osero Foundation is the Prime Foundation associated with Osero. Its mandate is to support the development, growth, and adoption of Osero.

###### A.6.1.1.7.2.1.1.3.1.1.6 - Development Company [Core]  <!-- UUID: 0eb2722b-c3e2-4c9a-83c1-986b0b0587cb -->

Stablewatch is a development company that provides services to the Osero Foundation.

###### A.6.1.1.7.2.1.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: cf57e4ff-d96b-486d-a37e-93c711308d4c -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.7.2.1.1.3.1.3 - Data Repository [Core]  <!-- UUID: 61c2470d-9699-48c1-8d0b-93bf452fe8b8 -->

The documents herein contain data relevant to the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.7.2.1.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: d58b413f-6fce-4b0d-80a8-aba5d74117b0 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.1.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 0d4f2b2d-305b-4a23-9764-64fdf5a7bcc8 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.1.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: dc435918-f881-4d35-af7d-1640979cc9cd -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.7.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: ff4e7a8d-3832-40a3-b2b0-fec3831ed689 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.7.2.1.2 - Prime Transformation Primitive [Core]  <!-- UUID: ff1ff3b0-3505-475a-9b04-92e0fbb16978 -->

The documents herein contain all data and specifications for Osero's instance of the Prime Transformation Primitive. See [A.2.2.5.2 - Prime Transformation Primitive](81411106-fd6d-4f9c-b3ae-7af7b5e62482).

##### A.6.1.1.7.2.1.2.1 - Primitive Hub Document [Core]  <!-- UUID: ccbf1b06-7d52-4355-8780-2618c68f1bfe -->

The documents herein organize all base information relevant to Osero's usage of the Prime Transformation Primitive.

###### A.6.1.1.7.2.1.2.1.1 - Global Activation Status [Core]  <!-- UUID: f8278414-f667-4d1d-a2bd-8ada95c5311a -->

`Completed`

###### A.6.1.1.7.2.1.2.1.2 - Active Instances Directory [Core]  <!-- UUID: ea4d3442-8d1a-4948-b199-d4d3831a58ce -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.1.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 8a699a06-4d30-4815-a2c5-a77c6effe229 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.1.2.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 337fa7c7-9727-4257-a4cb-6205afc2b687 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.1.2.3.1 - Single Instance Configuration Document](9bfd222e-7d6f-4ad3-a248-bf87900f4993).

###### A.6.1.1.7.2.1.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 0fcf82ab-6ae3-41c7-b8e4-424dd5f3850d -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.7.2.1.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 7cc6435b-939d-4695-882b-2e2cde5dd9b5 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.1.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 378a3dc3-181d-48f1-bd16-6ab43905bbf7 -->

The subtrees for archived Invocations and Instances of the Prime Transformation Primitive are stored here.

###### A.6.1.1.7.2.1.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: f0c60a20-750b-4f1f-a17e-871d4f1c76c4 -->

The subtrees for failed Invocations of the Prime Transformation Primitive are stored here.

###### A.6.1.1.7.2.1.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 5ca98f18-9440-4717-a940-2c663121dbc7 -->

The subtrees for Instances of the Prime Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.1.2.2 - Active Instances [Core]  <!-- UUID: adb5289b-af36-42b8-8ca4-6bd4cfbc7ac7 -->

The Instances of the Prime Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.1.2.3 - Completed Instances [Core]  <!-- UUID: ab6b47e6-8f17-4caa-a2f4-4f1a87f95545 -->

The Instances of the Prime Transformation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.7.2.1.2.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 9bfd222e-7d6f-4ad3-a248-bf87900f4993 -->

The documents herein contain the Instance Configuration Document for the Single Prime Transformation Primitive Instance.

###### A.6.1.1.7.2.1.2.3.1.1 - Parameters [Core]  <!-- UUID: 38a57bee-dfc8-462c-888c-3a2963e3539d -->

The documents herein define the parameters of the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.7.2.1.2.3.1.1.1 - Agent Type [Core]  <!-- UUID: 69d7e31c-36a7-4500-9e78-25167e2f38ab -->

Osero is a Prime Agent.

###### A.6.1.1.7.2.1.2.3.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 967efec7-0378-4491-94b1-918ea79de538 -->

The documents herein define the custom parameters of the Single Instance of the Prime Transformation Primitive, if any.

###### A.6.1.1.7.2.1.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 70018dbb-8b14-41d5-aef0-529e6104ea36 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.7.2.1.2.3.1.3 - Data Repository [Core]  <!-- UUID: fa03dbed-b41c-41db-8adb-826c991d64b8 -->

The documents herein contain data relevant to the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.7.2.1.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 36e23c65-220f-43b9-ab14-6f0fe4a25524 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.1.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: d5c113e8-b4d2-40c4-80d8-5797f8833cd3 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.1.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 1b8cb6c6-0906-4c56-935f-ad8e43bb9a11 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.7.2.1.2.4 - In Progress Invocations [Core]  <!-- UUID: 33beb09c-af1f-4d75-8307-d4546192acf8 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.7.2.1.3 - Executor Transformation Primitive [Core]  <!-- UUID: 0e769f4f-510c-49a4-aaa8-03a822ed75f3 -->

The documents herein contain all data and specifications for Osero's instance of the Executor Transformation Primitive. See [A.2.2.5.3 - Executor Transformation Primitive](2f249be5-8edb-41e4-b429-734e1ba2cbc7).

##### A.6.1.1.7.2.1.3.1 - Primitive Hub Document [Core]  <!-- UUID: d46b399b-0432-4350-9e3c-d5cf3487764f -->

The documents herein organize all base information relevant to Osero's usage of the Executor Transformation Primitive.

###### A.6.1.1.7.2.1.3.1.1 - Global Activation Status [Core]  <!-- UUID: 24501122-1780-4f2c-b23c-d9608e8d3475 -->

`Inactive`

###### A.6.1.1.7.2.1.3.1.2 - Active Instances Directory [Core]  <!-- UUID: b967e4a6-4911-4dd5-a8e4-b54047a589c0 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.1.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 9744681d-c677-4153-8d70-32fd72a7554c -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.1.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 1344eb03-7880-49c9-bed0-c2a954c93069 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.7.2.1.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 061f9187-78ca-4966-a1dc-e53b7f11faa1 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.1.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ffd96894-fd24-4644-b9ed-ab03ba5b72ce -->

The subtrees for archived Invocations and Instances of the Executor Transformation Primitive are stored here.

###### A.6.1.1.7.2.1.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 800dbefc-e953-40fa-b84a-6b199c9f46ee -->

The subtrees for failed Invocations of the Executor Transformation Primitive are stored here.

###### A.6.1.1.7.2.1.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 866b3ee2-2a07-4bfa-81cc-d5a664bb78d0 -->

The subtrees for Instances of the Executor Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.1.3.2 - Active Instances [Core]  <!-- UUID: 00ccdc84-b88e-4e2c-ac6a-2e5b6e882c62 -->

The Instances of the Executor Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.1.3.3 - Completed Instances [Core]  <!-- UUID: f3fb394f-c38b-41f8-a215-db199329bfee -->

The Instances of the Executor Transformation Primitive with `Completed` Status are contained herein.

##### A.6.1.1.7.2.1.3.4 - In Progress Invocations [Core]  <!-- UUID: a5cbb162-5a2b-44db-857b-1af33c13b1e6 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.7.2.1.4 - Agent Token Primitive [Core]  <!-- UUID: b9ef6634-cc3a-487f-8588-a1f2d3b8346c -->

The documents herein contain all data and specifications for Osero's Instance of the Agent Token Primitive. See [A.2.2.5.4 - Agent Token Primitive](2047c361-db28-4952-a70c-83d07b562064).

##### A.6.1.1.7.2.1.4.1 - Primitive Hub Document [Core]  <!-- UUID: 1885d903-2eff-43cf-9ed4-c7bd586c0af0 -->

The documents herein organize all base information relevant to Osero's usage of the Agent Token Primitive.

###### A.6.1.1.7.2.1.4.1.1 - Global Activation Status [Core]  <!-- UUID: b1f02877-3e82-4c5d-b99c-b422e5cad652 -->

`Active`

###### A.6.1.1.7.2.1.4.1.2 - Active Instances Directory [Core]  <!-- UUID: 0e0755ba-fbc4-417b-bb74-8c8c81aa20af -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.1.4.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 38b3be19-4fb6-4af7-9d6a-f46cd006d7b8 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.1.4.2.1 - Single Instance Configuration Document](80dc8fe6-5c4e-44aa-b9fb-89350ac4e5bf).

###### A.6.1.1.7.2.1.4.1.3 - Completed Instances Directory [Core]  <!-- UUID: 481bb1cf-1a60-4ceb-9502-ffdd1a19b50e -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.1.4.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 4163c78f-f018-47cd-8efc-f407119283c2 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent's token, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.7.2.1.4.1.5 - Hub Data Repository [Core]  <!-- UUID: 54bd28cb-95e9-432a-8107-751ef59b9fc4 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.1.4.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 090c9945-ad81-47e3-925a-3c364c38a6df -->

The subtrees for archived Invocations and Instances of the Agent Token Primitive are stored here.

###### A.6.1.1.7.2.1.4.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: f3ecfdce-f3d1-44b0-900b-5d1aca5e3edc -->

The subtrees for failed Invocations of the Agent Token Primitive are stored here.

###### A.6.1.1.7.2.1.4.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 72dbc2a7-c097-4385-94d5-8f71833b1360 -->

The subtrees for Instances of the Agent Token Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.1.4.2 - Active Instances [Core]  <!-- UUID: ca56cc56-4afb-46a8-b754-5956e73075f1 -->

The Instances of the Agent Token Primitive with `Active` Status are stored herein.

###### A.6.1.1.7.2.1.4.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 80dc8fe6-5c4e-44aa-b9fb-89350ac4e5bf -->

The documents herein contain the Instance Configuration Document for the Single Agent Token Primitive Instance.

###### A.6.1.1.7.2.1.4.2.1.1 - Parameters [Core]  <!-- UUID: 44fa192b-1ac1-4ef3-923e-8529a433c83f -->

The documents herein define the parameters of the Single Instance of the Agent Token Primitive.

###### A.6.1.1.7.2.1.4.2.1.1.1 - Token Name [Core]  <!-- UUID: ccd245e9-50d4-4083-9f9c-c77a204f9ecc -->

The name of Osero's token is Osero.

###### A.6.1.1.7.2.1.4.2.1.1.2 - Token Symbol [Core]  <!-- UUID: 841b8960-e62f-4602-b213-9474157b0684 -->

The symbol of Osero's token is OSERO.

###### A.6.1.1.7.2.1.4.2.1.1.3 - Genesis Supply [Core]  <!-- UUID: a1b32961-6aa2-4385-b515-b1bc334960df -->

The Genesis Supply of OSERO is 1 billion.

###### A.6.1.1.7.2.1.4.2.1.1.4 - Token Address [Core]  <!-- UUID: bd33da7e-609b-4866-89f7-637987cff659 -->

The address of OSERO will be specified in a future iteration of the Osero Artifact.

###### A.6.1.1.7.2.1.4.2.1.1.5 - Token Admin [Core]  <!-- UUID: 1863bfd0-8b9f-4c76-8748-c9262f6245a9 -->

The token Admin will be specified in a future iteration of the Osero Artifact.

###### A.6.1.1.7.2.1.4.2.1.1.6 - Token Emissions [Core]  <!-- UUID: 8ce3d244-b7d4-4cc4-b35e-5deaccc9c52f -->

Token emissions beyond the Genesis Supply are permanently disabled; this cannot be reverted by Osero Governance. Sky Governance retains the ability to revert where Osero is in violation of Risk Capital requirements and emissions are required by the Risk Framework. See [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.6.1.1.7.2.1.4.2.1.1.7 - Custom Instance Parameters [Core]  <!-- UUID: bac7bdc2-4060-4ae7-8273-4420d96c53dd -->

The documents herein define the custom parameters of the Single Instance of the Agent Token Primitive, if any.

###### A.6.1.1.7.2.1.4.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 5179fc59-1ed8-45be-9516-58c59083d6c1 -->

The documents herein define the operational processes for minting and initial distribution of the tokens from the Genesis Supply.

- These processes will be defined in a future iteration of the Osero Artifact.

###### A.6.1.1.7.2.1.4.2.1.3 - Data Repository [Core]  <!-- UUID: b4574752-f657-4d44-8be0-0387a26b2f0a -->

The documents herein contain data relevant to the Single Instance of the Agent Token Primitive.

###### A.6.1.1.7.2.1.4.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 1d7df1bf-116c-451f-ad56-3fb899db577b -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.1.4.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: a56b88fe-398f-4384-ac87-4cd45c0290cf -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.1.4.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: cc30ee14-2850-45fa-bdf0-84d4789b7d3d -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.7.2.1.4.3 - Completed Instances [Core]  <!-- UUID: dc44ad54-7a03-43b0-8a1b-232353c163c3 -->

The Instances of the Agent Token Primitive with `Completed` Status are contained herein.

##### A.6.1.1.7.2.1.4.4 - In Progress Invocations [Core]  <!-- UUID: cdd39473-4eaf-4a3b-9d6a-2cd0ac46859b -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent's token, no further Instances of the Primitive can be Invoked.

### A.6.1.1.7.2.2 - Operational Primitives [Core]  <!-- UUID: 6b98a6ae-9f12-4503-9096-9e548d68451d -->

The documents herein implement the Operational Primitives for Osero. See [A.2.2.6 - Operational Primitives](0192ec95-9207-480e-8c51-88d2a1da95ad).

#### A.6.1.1.7.2.2.1 - Executor Accord Primitive [Core]  <!-- UUID: 77a105f5-98e7-41b8-acac-47a4d5473c81 -->

The documents herein contain all data and specifications for Osero's Instances of the Executor Accord Primitive. See [A.2.2.6.1 - Executor Accord Primitive](88017877-3ec1-4c43-a035-6bebdf11d9bb).

##### A.6.1.1.7.2.2.1.1 - Primitive Hub Document [Core]  <!-- UUID: 6adf71d4-03f8-43ed-83ad-3011dfebe17d -->

The documents herein organize all base information relevant to Osero's usage of the Executor Accord Primitive.

###### A.6.1.1.7.2.2.1.1.1 - Global Activation Status [Core]  <!-- UUID: 64d43bdf-ecd5-41bf-8023-64bf78ad70d4 -->

`Active`

###### A.6.1.1.7.2.2.1.1.2 - Active Instances Directory [Core]  <!-- UUID: a1260e19-86fc-4ebe-a53a-501e4baf9752 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.2.1.1.2.1 - Ozone Instance Configuration Document Location [Core]  <!-- UUID: c0aff461-b4c5-4392-bf92-3db9ebe7a476 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.2.1.2.1 - Ozone Instance Configuration Document](c41fe115-5145-438e-bcaf-9924996b4fcd).

###### A.6.1.1.7.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: a3222e92-22ee-49a6-a7ae-20e7bd2a6ca5 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: c5af5be5-2612-4e3b-aad4-f06603235bd7 -->

This document contains a Directory of all prospective Instances of the Executor Accord Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.2.1.1.2 - Active Instances Directory](a1260e19-86fc-4ebe-a53a-501e4baf9752), whereas failed Invocations are Archived in [A.6.1.1.7.2.2.1.1.5 - Hub Data Repository](10c951e0-3200-4359-a76e-c1ff9ccb9105).

###### A.6.1.1.7.2.2.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 10c951e0-3200-4359-a76e-c1ff9ccb9105 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.2.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 5621fd19-1f72-47d1-823e-762399ef7eae -->

The subtrees for archived Invocations and Instances of the Executor Accord Primitive are stored here.

###### A.6.1.1.7.2.2.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 593f7150-b5b6-48c6-8e39-30d084ac31ee -->

The subtrees for failed Invocations of the Executor Accord Primitive are stored here.

###### A.6.1.1.7.2.2.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: b2f1f9df-2812-4aa7-a066-dfb67ebdb288 -->

The subtrees for Instances of the Executor Accord Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.2.1.2 - Active Instances [Core]  <!-- UUID: d5f4610a-9cd1-4a6e-96de-5ea617463152 -->

The Instances of the Executor Accord Primitive with `Active` Status are stored herein.

###### A.6.1.1.7.2.2.1.2.1 - Ozone Instance Configuration Document [Core]  <!-- UUID: c41fe115-5145-438e-bcaf-9924996b4fcd -->

The documents herein contain the Instance Configuration Document for the Ozone Executor Accord Primitive Instance.

###### A.6.1.1.7.2.2.1.2.1.1 - Parameters [Core]  <!-- UUID: f5dfa719-a44c-4a4f-bf28-9204a976dfcb -->

The documents herein define the parameters of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.7.2.2.1.2.1.1.1 - Operational Executor Agent [Core]  <!-- UUID: 1ab18042-345c-40b2-9ed3-06cfdb3b7d4b -->

The Operational Facilitator and Operational GovOps for Ozone are specified in [A.6.1.2.2 - Operational Executor Agent Ozone](565660dd-7850-4c3a-8dba-554542bf103a)

###### A.6.1.1.7.2.2.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 3b306de0-b8d7-4eda-b23b-0173c24e742e -->

The documents herein define the custom parameters of the Ozone Instance of the Executor Accord Primitive, if any.

###### A.6.1.1.7.2.2.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 68badec0-cfad-49de-b15a-51f12e90275a -->

The documents herein define the process for the ongoing management of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.7.2.2.1.2.1.3 - Data Repository [Core]  <!-- UUID: af743a8c-0d39-41ac-9898-0cdfac8e2c56 -->

The documents herein contain data relevant to the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.7.2.2.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 23aab69c-d555-46d7-88ab-cb06303dc9af -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.2.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: d283179e-7527-4522-8935-5fe4d2442ed5 -->

The materials associated with Operational GovOps review during the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.2.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 83075590-9293-4ae7-bdb0-701fd0689570 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.7.2.2.1.3 - Completed Instances [Core]  <!-- UUID: a1204555-a3db-4b2d-a965-5a8300d66b3e -->

The Instances of the Executor Accord Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.2.1.4 - In Progress Invocations [Core]  <!-- UUID: aa2527c7-a809-4552-8557-3d093bd80e53 -->

The in progress Invocations of the Executor Accord Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.2.1.2 - Active Instances](d5f4610a-9cd1-4a6e-96de-5ea617463152).

#### A.6.1.1.7.2.2.2 - Root Edit Primitive [Core]  <!-- UUID: 6c61b3d8-6cc8-4250-8173-eee8396a4ef4 -->

The documents herein contain all data and specifications for Osero's Instance of the Root Edit Primitive. See [A.2.2.6.2 - Root Edit Primitive](78488c6b-d77f-4344-b954-476e415a2c7d).

##### A.6.1.1.7.2.2.2.1 - Primitive Hub Document [Core]  <!-- UUID: 30a4ea54-3083-4a3b-add0-0d3c41f5fcd2 -->

The documents herein organize all base information relevant to Osero's usage of the Root Edit Primitive.

###### A.6.1.1.7.2.2.2.1.1 - Global Activation Status [Core]  <!-- UUID: c2d33537-86aa-4953-9549-f8a298280ef2 -->

`Active`

###### A.6.1.1.7.2.2.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 3a35c81d-b624-4f61-9fad-6bb18aaf196b -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.2.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 2bc5a631-5c2d-4d88-82ff-64883968bc22 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.2.2.2.1 - Single Instance Configuration Document](db6cb28a-c001-404d-b630-6ea755499ed3).

###### A.6.1.1.7.2.2.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 4050328d-f2b9-4a46-baf7-563489ea7ebc -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.2.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 4bbc8ebb-94be-4625-8dd6-67961a03574e -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.7.2.2.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 151cb222-ad08-45c5-a884-55efd3d050d2 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.2.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 5dabf55e-66a0-4662-a3cd-5f522593f254 -->

The subtrees for archived Invocations and Instances of the Root Edit Primitive are stored here.

###### A.6.1.1.7.2.2.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: c0cd8734-a01b-4e2b-b42c-622880a5e120 -->

The subtrees for failed Invocations of the Root Edit Primitive are stored here.

###### A.6.1.1.7.2.2.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 024712ec-d260-4464-86f2-10cad410a114 -->

The subtrees for Instances of the Root Edit Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.2.2.2 - Active Instances [Core]  <!-- UUID: c5c7c09a-2b33-465e-bc01-dc90415872d5 -->

The Instances of the Root Edit Primitive with `Active` Status are stored herein.

###### A.6.1.1.7.2.2.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: db6cb28a-c001-404d-b630-6ea755499ed3 -->

The documents herein contain the Instance Configuration Document for the Single Root Edit Primitive Instance.

###### A.6.1.1.7.2.2.2.2.1.1 - Parameters [Core]  <!-- UUID: dfaa57ba-36fa-45be-9f89-0bf77fbcff59 -->

The parameters of the Root Edit Primitive are fully specified by the Operational Process Definition in [A.6.1.1.7.2.2.2.2.1.2 - Operational Process Definition](cfd923fb-0a53-4dd2-bb4f-5e840bda69c6).

###### A.6.1.1.7.2.2.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: cfd923fb-0a53-4dd2-bb4f-5e840bda69c6 -->

The documents herein define the process for using the Root Edit Primitive to update the Osero Agent Artifact. Information on Osero governance that is unrelated to the use of the Root Edit Primitive is located at [A.6.1.1.7.3.1 - Governance Information Unrelated To Root Edit Primitive](a472d201-3dfd-4939-9789-5cedce9ea37a).

###### A.6.1.1.7.2.2.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: ff28b8ca-2279-4ec4-96d9-e0b4d2340c64 -->

The documents herein define the process for using the Root Edit Primitive to update the Osero Agent Artifact in routine or normal conditions (i.e., non-emergency situations).

###### A.6.1.1.7.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission [Core]  <!-- UUID: 70c91853-b74b-4c6b-befb-8446f00c9691 -->

The Root Edit process begins with an OSERO token holder submitting a proposal through the Powerhouse system containing a draft Artifact Edit Proposal. An OSERO token holder must hold at least 1% of the circulating token supply to submit a proposal. The proposal must also be posted on the Sky Forum under the "Osero Prime" category.

###### A.6.1.1.7.2.2.2.2.1.2.1.1.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: caafe932-8fa7-4ee6-ba0b-dd49bcef1ee1 -->

Until the Powerhouse system supports submitting Artifact Edit Proposals, OSERO token holders may submit Artifact Edit Proposals by posting them to the Sky Forum under the "Osero Prime" category. The title of the post must include the text "Osero Artifact Edit Proposal". The post must include cryptographic proof that the author controls an account holding the required percentage of the total OSERO token supply specified in [A.6.1.1.7.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](70c91853-b74b-4c6b-befb-8446f00c9691).

###### A.6.1.1.7.2.2.2.2.1.2.1.2 - Root Edit Expert Advisor Review [Core]  <!-- UUID: baaa8a79-a8a9-4a90-b350-83e845b52895 -->

A future iteration of the Osero Artifact will specify guidelines for obtaining specialized review of proposals requiring advanced technical or financial analysis.

###### A.6.1.1.7.2.2.2.2.1.2.1.3 - Root Edit Proposal Review By Operational Facilitator [Core]  <!-- UUID: 8f6ab3a5-f915-4faf-8d3b-4cc48cd03824 -->

Within seven (7) days of the proposal being submitted, the Operational Facilitator must review the Root Edit Proposal for alignment.

If the proposal is aligned, the Operational Facilitator must respond to the Forum post to announce their finding. In this Forum post, the Operational Facilitator must also confirm that the proposal is feasible for Operational GovOps to operationalize.

If the proposal is misaligned, the Operational Facilitator must respond to the Forum post to announce their finding and provide the reasoning for it.

###### A.6.1.1.7.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote [Core]  <!-- UUID: a015eb36-9095-4112-9fe6-a75dd8a6040a -->

Where their review of the proposal results in a finding of alignment with the Sky Core Atlas and Osero Artifact, the Operational Facilitator next triggers a Snapshot poll to allow token holders to vote on the proposal. The poll is open for three (3) days. A poll must have at least 10% of the circulating token supply participating and must have 50% of votes in favor to be approved.

###### A.6.1.1.7.2.2.2.2.1.2.1.5 - Root Edit Artifact Update [Core]  <!-- UUID: 4328ddab-d71b-47bf-8ff7-d6f0a2e37c2f -->

At the conclusion of the poll, if the proposal is approved, the Operational Facilitator submits the edit to Powerhouse to formally update the Agent Artifact. Regardless of the outcome, the Operational Facilitator updates the Powerhouse System to include the result of the vote, including any pertinent documents.

###### A.6.1.1.7.2.2.2.2.1.2.1.5.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: 6de8c6b8-2e65-4a0b-940f-c509eb0661cd -->

Until the Powerhouse system supports updating Agent Artifacts, the Operational Facilitator works with the Core Facilitator to update the Atlas GitHub repository located at [https://github.com/sky-ecosystem/next-gen-atlas/pulls](https://github.com/sky-ecosystem/next-gen-atlas/pulls) to reflect proposals approved by Prime Governance.

###### A.6.1.1.7.2.2.2.2.1.2.1.6 - Artifact Edit Restrictions [Core]  <!-- UUID: ad3c8df7-2df3-4bb3-8192-f97ba459de7b -->

The Osero Artifact cannot be edited in any way that violates the Sky Core Atlas or its specifications of the Sky Primitives, or in any way that is otherwise misaligned. The Operational Facilitator must enforce this rule through their review of Artifact Edit Proposals.

###### A.6.1.1.7.2.2.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 08bc46ae-a50a-499a-99be-6f3449f13bc1 -->

The documents herein define the process for using the Root Edit Primitive to update the Osero Agent Artifact in non-routine conditions.

###### A.6.1.1.7.2.2.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: dd51cdeb-242b-4d26-8841-754079074e41 -->

The documents herein define the process for using the Root Edit Primitive to update the Osero Agent Artifact in emergency situations.

###### A.6.1.1.7.2.2.2.2.1.2.3.1 - Root Edit Voting Process In Emergency Situations [Core]  <!-- UUID: 8d2ba042-109c-4819-89c3-023e8f1c3de2 -->

In an Emergency Situation, as defined by the Sky Core Atlas in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225), the Operational Facilitator may allow a Root Edit to occur more quickly than the timeline specified above. Where feasible, the Operational Facilitator should announce the decision to deploy the emergency Root Edit protocol and provide their reasoning via a public Sky Forum post (under the "Osero Prime" category), unless doing so would endanger Osero or its users.

###### A.6.1.1.7.2.2.2.2.1.3 - Data Repository [Core]  <!-- UUID: 08286cf1-8c6f-4cd2-9898-92e4147c60e8 -->

The documents herein contain data relevant to the Single Instance of the Root Edit Primitive.

###### A.6.1.1.7.2.2.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 9dbfdcc1-4908-489a-8887-a36628d0e2d6 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.2.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 7cfd996c-2a02-412b-8d65-0efbc88a6cdf -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.2.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: ade379d8-2b49-49d8-8425-8060c5bba942 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.7.2.2.2.3 - Completed Instances [Core]  <!-- UUID: e8c23769-6920-4fba-aebf-3051851be0fc -->

The Instances of the Root Edit Primitive with `Completed` Status are contained herein.

##### A.6.1.1.7.2.2.2.4 - In Progress Invocations [Core]  <!-- UUID: 9f9665de-c252-4376-91aa-103482f41152 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.7.2.2.3 - Light Agent Primitive [Core]  <!-- UUID: 5b3ff28a-27e7-414c-87c7-b2d4f239ac2a -->

The documents herein contain all data and specifications for Osero's Instances of the Light Agent Primitive. See [A.2.2.6.3 - Light Agent Primitive](44028423-2cd1-40cb-89ac-3f762b602b90).

##### A.6.1.1.7.2.2.3.1 - Primitive Hub Document [Core]  <!-- UUID: 40fd0acb-dd7c-4b72-a842-9024d1250f3e -->

The documents herein organize all base information relevant to Osero's usage of the Light Agent Primitive.

###### A.6.1.1.7.2.2.3.1.1 - Global Activation Status [Core]  <!-- UUID: 963ebcfe-f66b-4598-90fb-c8d61eb87520 -->

`Inactive`

###### A.6.1.1.7.2.2.3.1.2 - Active Instances Directory [Core]  <!-- UUID: e04cf30c-cb79-4b5c-902a-c75e6387dadb -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.2.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: db97fdbc-5163-4b23-a6ed-e05ac62167ea -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.2.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 0bb0c992-f0b6-463b-abff-e50d8e3689ca -->

This document contains a Directory of all prospective Instances of the Light Agent Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.2.3.1.2 - Active Instances Directory](e04cf30c-cb79-4b5c-902a-c75e6387dadb), whereas failed Invocations are Archived in [A.6.1.1.7.2.2.3.1.5 - Hub Data Repository](29a0cd95-500c-45ce-b5a5-66ea10493545).

###### A.6.1.1.7.2.2.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 29a0cd95-500c-45ce-b5a5-66ea10493545 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.2.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 89a1c42e-611a-4239-8330-0a9003955634 -->

The subtrees for archived Invocations and Instances of the Light Agent Primitive are stored here.

###### A.6.1.1.7.2.2.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 71e93307-834d-485b-a576-cdd0490af3f5 -->

The subtrees for failed Invocations of the Light Agent Primitive are stored here.

###### A.6.1.1.7.2.2.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: cece35ac-24aa-44e6-87fe-d9f2e0d1e68c -->

The subtrees for Instances of the Light Agent Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.2.3.2 - Active Instances [Core]  <!-- UUID: a2e69b89-5ac1-43bf-8841-ecfe17ad8d84 -->

The Instances of the Light Agent Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.2.3.3 - Completed Instances [Core]  <!-- UUID: 7f7e5c17-b539-4fff-8620-6630ef8c1285 -->

The Instances of the Light Agent Primitive with `Completed` Status are contained herein.

##### A.6.1.1.7.2.2.3.4 - In Progress Invocations [Core]  <!-- UUID: 328eff05-96c8-46e8-9e15-95add9638abb -->

The in progress Invocations of the Light Agent Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.2.3.2 - Active Instances](a2e69b89-5ac1-43bf-8841-ecfe17ad8d84).

### A.6.1.1.7.2.3 - Ecosystem Upkeep Primitives [Core]  <!-- UUID: 539eca6a-be95-47ee-bd9d-22a031abbd86 -->

The documents herein implement the Ecosystem Upkeep Primitives for Osero. See [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

#### A.6.1.1.7.2.3.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: e30013e8-4d99-40fa-9708-ede560312786 -->

The documents herein contain all data and specifications for Osero's Instance of the Ecosystem Upkeep Fee Primitive. See [A.2.2.7.1 - Ecosystem Upkeep Fee Primitive](a21616f4-1611-4e0b-87b2-efbdff9f6f28).

##### A.6.1.1.7.2.3.1.1 - Primitive Hub Document [Core]  <!-- UUID: 1a65a542-00ef-4bb6-85ec-67c7b3127f43 -->

The documents herein organize all base information relevant to Osero's usage of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.7.2.3.1.1.1 - Global Activation Status [Core]  <!-- UUID: b2ddd73c-530b-4dcc-b821-371a4bb49eda -->

`Active`

###### A.6.1.1.7.2.3.1.1.2 - Active Instances Directory [Core]  <!-- UUID: a254f828-3f7c-4810-b084-13ded96a3727 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.3.1.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 31065251-c40d-4298-9d8a-d9b4ef0d23f7 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.3.1.2.1 - Single Instance Configuration Document](8cd599cd-d6f1-4ef4-86cd-94aaf842d62e).

###### A.6.1.1.7.2.3.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: bade3eef-dde0-4103-814c-17b428fb7a68 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.3.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 7efb6642-5543-4a7a-9d4a-3dcf4b9f8a50 -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.7.2.3.1.1.5 - Hub Data Repository [Core]  <!-- UUID: a978e8ea-067b-45f7-915a-2189a47fb035 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.3.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 1fe40ee6-efd4-4cdb-a5ab-cbb8ccef8bad -->

The subtrees for archived Invocations and Instances of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.7.2.3.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: f92f755a-d487-4871-b126-a92c049bfdcb -->

The subtrees for failed Invocations of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.7.2.3.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: bc7d3904-3cf6-4b38-9d33-46b734891bfb -->

The subtrees for Instances of the Ecosystem Upkeep Fee Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.3.1.2 - Active Instances [Core]  <!-- UUID: cd0de0c7-7970-49b0-b05a-def3e1bcab9a -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Active` Status are stored herein.

###### A.6.1.1.7.2.3.1.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 8cd599cd-d6f1-4ef4-86cd-94aaf842d62e -->

The documents herein contain the Instance Configuration Document for the Single Ecosystem Upkeep Fee Primitive Instance.

###### A.6.1.1.7.2.3.1.2.1.1 - Parameters [Core]  <!-- UUID: 0b3112c5-3632-4e98-971c-8737f657ec80 -->

The documents herein define the parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.7.2.3.1.2.1.1.1 - Terms [Core]  <!-- UUID: 0545120b-a962-479c-a35d-9e208e6fff17 -->

Osero will pay 0.50% of its market capitalization per year in USDS.

###### A.6.1.1.7.2.3.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 65782992-194b-4f7a-af35-23dc1db7287f -->

The documents herein define the custom parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive, if any.

###### A.6.1.1.7.2.3.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: bea02c9f-ea6a-4d22-ab23-04f5ca6a37d0 -->

The documents herein define the process for the ongoing management of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.7.2.3.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 9a0c543e-1846-4baf-9245-7a218bd45d3f -->

This document defines the protocol for routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.7.2.3.1.2.1.2.1.1 - Process Definition For Upkeep Fee Payment [Core]  <!-- UUID: 82841628-ddd7-4ccc-90c3-a45bf961d678 -->

The process to pay 0.50% of Osero's market capitalization per year in USDS will be specified in future iterations of the Osero Artifact.

###### A.6.1.1.7.2.3.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 2b131681-dfba-4f69-b185-d512fbdf8a26 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.7.2.3.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: ac8f7954-3348-4cb7-bdea-76b1dd4a294f -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.7.2.3.1.2.1.3 - Data Repository [Core]  <!-- UUID: 5909f14c-6248-4a31-b8b5-c699e1f51897 -->

The documents herein contain data relevant to the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.7.2.3.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 1d31b5fd-d55c-4d8e-b554-d2d9f1e95a05 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.3.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 9e648afc-d5c5-4f2e-8026-71fede7b270b -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.3.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: e5150ceb-77a8-468c-b202-19fefcb1f95d -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.7.2.3.1.3 - Completed Instances [Core]  <!-- UUID: bdcaed32-e33f-4426-b059-93dfe4fc1956 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.3.1.4 - In Progress Invocations [Core]  <!-- UUID: 6ef3b9a9-b6a7-45ef-aaf4-3788389d7bf3 -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.7.2.3.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: 8389ea55-0cd8-4471-b940-50b9882f0924 -->

The documents herein contain all data and specifications for Osero's instance of the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

##### A.6.1.1.7.2.3.2.1 - Primitive Hub Document [Core]  <!-- UUID: 9693a23e-9116-43d3-87ae-5036fa0fb4d1 -->

The documents herein organize all base information relevant to Osero's usage of the Upkeep Rebate Primitive.

###### A.6.1.1.7.2.3.2.1.1 - Global Activation Status [Core]  <!-- UUID: bbec58f6-cf9f-4bb9-a760-3cde09c6c153 -->

`Active`

###### A.6.1.1.7.2.3.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 17114b33-3010-4053-aa42-bcf3bf3ae73b -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.3.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 7c31bd54-47e2-4b66-8a6a-bca28cb4c5f9 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.3.2.2.1 - Single Instance Configuration Document](6e734cc1-a07e-42d7-afac-31ffa3cfd5dc).

###### A.6.1.1.7.2.3.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7882085c-54c7-468d-9693-7c03ab8c847f -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.3.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 6f4901f6-2170-481c-8fd9-7d7c9ef2ab6d -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.7.2.3.2.1.5 - Hub Data Repository [Core]  <!-- UUID: d1a41004-f2c2-4a95-9872-ba3f09778366 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.3.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 02c01711-c3ca-4fdd-b8a1-660ee2c1cf23 -->

The subtrees for archived Invocations and Instances of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.7.2.3.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9f0f82e8-a49b-4ed4-ac3a-27c427a327f5 -->

The subtrees for failed Invocations of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.7.2.3.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: b548b647-8c48-41cc-8d60-ad34075226bf -->

The subtrees for Instances of the Upkeep Rebate Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.3.2.2 - Active Instances [Core]  <!-- UUID: 288c1b34-5986-4a83-abc1-56efa6af6500 -->

The Instances of the Upkeep Rebate Primitive with `Active` Status are stored herein.

###### A.6.1.1.7.2.3.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 6e734cc1-a07e-42d7-afac-31ffa3cfd5dc -->

The documents herein contain the Instance Configuration Document for the Single Upkeep Rebate Primitive Instance.

###### A.6.1.1.7.2.3.2.2.1.1 - Parameters [Core]  <!-- UUID: 1c3dc285-97c5-4732-b763-2525038de133 -->

Every Prime Agent is entitled to the Upkeep Rebate Primitive for tokens of other Prime Agents that they hold. Because this right automatically applies, there are no parameters.

###### A.6.1.1.7.2.3.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 2330f1de-6a7c-469e-9a2a-8706c6930d25 -->

The documents herein define the process for the ongoing management of the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.7.2.3.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 5126a10e-9036-42fc-a0f7-236df746295c -->

This document defines the protocol for routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.7.2.3.2.2.1.2.1.1 - Osero Holds Tokens Of Other Agents In Its SubProxy Account [Core]  <!-- UUID: a0347944-1dea-473f-acfe-a66f582d27a9 -->

Osero keeps all tokens of other Agents it holds in its SubProxy account.

###### A.6.1.1.7.2.3.2.2.1.2.1.2 - Osero Deducts Rebate From Ecosystem Upkeep Fees [Core]  <!-- UUID: eac62395-4c6c-40d5-bc37-e2acf3301072 -->

When paying Ecosystem Upkeep fees, Osero deducts the rebate from the fees it pays.

###### A.6.1.1.7.2.3.2.2.1.2.1.3 - Operational GovOps Reviews Rebate [Core]  <!-- UUID: e7058972-4fa4-4a85-967b-965afede3a23 -->

Operational GovOps reviews Osero's calculation of the rebate before executing a return of surplus to token holders. In the event of any issues, Operational GovOps cannot execute the distribution. If Operational GovOps does not execute the distribution, Operational GovOps must post an explanation on the Sky Forum under the "Osero Prime" category and work with Osero to resolve the disagreement. If Operational GovOps and Osero cannot resolve the disagreement, it must be escalated to Core GovOps.

###### A.6.1.1.7.2.3.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 7a5f2fbb-e524-4ca0-95bd-2f7c76fd3c3f -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.7.2.3.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 1192301e-a2ff-4016-b650-90e1436af97d -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.7.2.3.2.2.1.3 - Data Repository [Core]  <!-- UUID: 3a02223c-f21e-4fee-8bc8-36a4cf36366a -->

The documents herein contain data relevant to the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.7.2.3.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: e6be574b-1a20-4fbb-8ee9-43d649be4c0d -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.3.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 86a4e532-848d-4363-a87d-944176a3707f -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.7.2.3.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 54f739a5-7170-4bed-aa9b-67e6b4591786 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.7.2.3.2.3 - Completed Instances [Core]  <!-- UUID: 6187f71c-8d4f-4a95-9aff-a87395f3f6b1 -->

The Instances of the Upkeep Rebate Primitive with `Completed` Status are contained herein.

##### A.6.1.1.7.2.3.2.4 - In Progress Invocations [Core]  <!-- UUID: 5ceee64b-59df-42e1-9da4-71b9f91dcb1c -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

### A.6.1.1.7.2.4 - SkyLink Primitives [Core]  <!-- UUID: 58d0ebb7-7b3d-46bb-9976-de6a7fa76e2d -->

The documents herein implement the SkyLink Primitives for Osero. See [A.2.2.8 - SkyLink Primitives](7b5d8965-a64c-4c44-b742-607f51f69d8f).

#### A.6.1.1.7.2.4.1 - Token SkyLink Primitive [Core]  <!-- UUID: f599a2d4-2527-4747-abe8-3418ca46d0de -->

The documents herein contain all data and specifications for Osero's Instances of the Token SkyLink Primitive. See [A.2.2.8.1 - Token SkyLink Primitive](4504d2d4-ee45-4a07-8c5b-9baf20b12e76).

##### A.6.1.1.7.2.4.1.1 - Primitive Hub Document [Core]  <!-- UUID: 3244d08e-fcb7-4685-afda-41d6b82460da -->

The documents herein organize all base information relevant to Osero's usage of the Token SkyLink Primitive.

###### A.6.1.1.7.2.4.1.1.1 - Global Activation Status [Core]  <!-- UUID: 1bce4eaa-2b7e-466c-8e2c-abf9680af8ac -->

`Inactive`

###### A.6.1.1.7.2.4.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 5697d516-fc74-40a8-a2c7-7f00c534f3a6 -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.4.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 4df0c5d3-3273-47da-b144-de84b87600dc -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.4.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 7ae00ad7-11bd-428a-99c9-a787ba7d6c97 -->

This document contains a Directory of all prospective Instances of the Token SkyLink Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.4.1.1.2 - Active Instances Directory](5697d516-fc74-40a8-a2c7-7f00c534f3a6), whereas failed Invocations are Archived in [A.6.1.1.7.2.4.1.1.5 - Hub Data Repository](dff4750a-bf17-475d-8741-049e00083d5f).

###### A.6.1.1.7.2.4.1.1.5 - Hub Data Repository [Core]  <!-- UUID: dff4750a-bf17-475d-8741-049e00083d5f -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.4.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 690d210b-0a09-448e-a691-448551f029c8 -->

The subtrees for archived Invocations and Instances of the Token SkyLink Primitive are stored here.

###### A.6.1.1.7.2.4.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 71081f64-8e4b-46e1-9c58-b45cdceeb362 -->

The subtrees for failed Invocations of the Token SkyLink Primitive are stored here.

###### A.6.1.1.7.2.4.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: da4c1103-d221-4f8a-a51a-2c5601aa70cf -->

The subtrees for Instances of the Token SkyLink Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.4.1.2 - Active Instances [Core]  <!-- UUID: 9e0bbf6f-a71c-4db1-80a2-b3a5991a072b -->

The Instances of the Token SkyLink Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.4.1.3 - Completed Instances [Core]  <!-- UUID: 1488c64d-f8a7-4f11-8e81-b0096e50ed97 -->

The Instances of the Token SkyLink Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.4.1.4 - In Progress Invocations [Core]  <!-- UUID: 5883e7cb-4e0a-4ed0-a0c9-6e3ce7564a9d -->

The in progress Invocations of the Token SkyLink Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.4.1.2 - Active Instances](9e0bbf6f-a71c-4db1-80a2-b3a5991a072b).

### A.6.1.1.7.2.5 - Demand Side Stablecoin Primitives [Core]  <!-- UUID: a0f8bc2e-4ac4-4335-8fd1-37132c875baf -->

The documents herein implement the Demand Side Stablecoin Primitives for Osero. See [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d).

#### A.6.1.1.7.2.5.1 - Distribution Reward Primitive [Core]  <!-- UUID: 10fdd41c-61e5-42fa-96b9-97f268f46902 -->

The documents herein contain all data and specifications for Osero's instances of the Distribution Reward Primitive. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

##### A.6.1.1.7.2.5.1.1 - Primitive Hub Document [Core]  <!-- UUID: f3db2774-0ec3-4efd-9da8-0fa6d0fe609b -->

The documents herein organize all base information relevant to Osero's usage of the Distribution Reward Primitive.

###### A.6.1.1.7.2.5.1.1.1 - Global Activation Status [Core]  <!-- UUID: d4cef458-3331-464c-9352-f36704aaecff -->

`Active`

###### A.6.1.1.7.2.5.1.1.2 - Active Instances Directory [Core]  <!-- UUID: ef465153-3408-49f2-8b39-761c445e7a8a -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.5.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: d495c6cf-095e-4257-b54a-59139110bd3e -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.5.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: ab0d6db3-879d-4bc3-b099-89810a10877c -->

This document contains a Directory of all prospective Instances of the Distribution Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.5.1.1.2 - Active Instances Directory](ef465153-3408-49f2-8b39-761c445e7a8a), whereas failed Invocations are Archived in [A.6.1.1.7.2.5.1.1.5 - Hub Data Repository](aad36c3f-431d-4a1d-942b-a583805618c1).

###### A.6.1.1.7.2.5.1.1.5 - Hub Data Repository [Core]  <!-- UUID: aad36c3f-431d-4a1d-942b-a583805618c1 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.5.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 18514778-d22b-43bc-ad19-ebb7403e02a5 -->

The subtrees for archived Invocations and Instances of the Distribution Reward Primitive are stored here.

###### A.6.1.1.7.2.5.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: fdfc3679-50ad-4c3e-bcae-e69df4c6d6b2 -->

The subtrees for failed Invocations of the Distribution Reward Primitive are stored here.

###### A.6.1.1.7.2.5.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: ecb8493a-5c44-4619-8f5a-e36327c797e8 -->

The subtrees for Instances of the Distribution Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.5.1.2 - Active Instances [Core]  <!-- UUID: 464695e4-744c-48fd-a023-565096dc9144 -->

The Instances of the Distribution Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.5.1.3 - Completed Instances [Core]  <!-- UUID: 4e7b84d1-356c-437a-9aa2-3a569c0c29ab -->

The Instances of the Distribution Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.5.1.4 - In Progress Invocations [Core]  <!-- UUID: ef23d204-14e2-4576-bca3-8bceca7b1c63 -->

The in progress Invocations of the Distribution Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.5.1.2 - Active Instances](464695e4-744c-48fd-a023-565096dc9144).

#### A.6.1.1.7.2.5.2 - Integration Boost Primitive [Core]  <!-- UUID: 937c895e-2569-46d3-8de0-8ed716e11b09 -->

The documents herein contain all data and specifications for Osero's Instances of the Integration Boost Primitive. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

##### A.6.1.1.7.2.5.2.1 - Primitive Hub Document [Core]  <!-- UUID: 60d8973d-b5e0-4dc3-ae21-edfda998bc42 -->

The documents herein organize all base information relevant to Osero's usage of the Integration Boost Primitive.

###### A.6.1.1.7.2.5.2.1.1 - Global Activation Status [Core]  <!-- UUID: bafcd161-a5d8-4498-8502-cf71deffd0ee -->

`Active`

###### A.6.1.1.7.2.5.2.1.2 - Active Instances Directory [Core]  <!-- UUID: cdbc02f2-7ec8-4ae4-b027-8938f0824864 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.5.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: c915735d-8347-433e-bc47-6f94a41e8689 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.5.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: bd14164c-8c4f-4d7d-99f4-da281221288a -->

This document contains a Directory of all prospective Instances of the Integration Boost Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.5.2.1.2 - Active Instances Directory](cdbc02f2-7ec8-4ae4-b027-8938f0824864), whereas failed Invocations are Archived in [A.6.1.1.7.2.5.2.1.5 - Hub Data Repository](ed0542a2-e910-4caa-9d1a-e96381aed48d).

###### A.6.1.1.7.2.5.2.1.5 - Hub Data Repository [Core]  <!-- UUID: ed0542a2-e910-4caa-9d1a-e96381aed48d -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.5.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 0af68d0c-c6fc-43cd-aed5-5b889110d25a -->

The subtrees for archived Invocations and Instances of the Integration Boost Primitive are stored here.

###### A.6.1.1.7.2.5.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9ad5e114-dd9f-4caf-a255-d830011c784d -->

The subtrees for failed Invocations of the Integration Boost Primitive are stored here.

###### A.6.1.1.7.2.5.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 101f1885-e1ba-49f8-93f8-2c7d45288d2c -->

The subtrees for Instances of the Integration Boost Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.5.2.2 - Active Instances [Core]  <!-- UUID: 2628525c-6956-49dd-9a48-e3de403a0597 -->

The Instances of the Integration Boost Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.5.2.3 - Completed Instances [Core]  <!-- UUID: 0d520de1-d730-427f-95bd-2ed92b80512d -->

The Instances of the Integration Boost Primitive with `Completed` Status are contained herein.

##### A.6.1.1.7.2.5.2.4 - In Progress Invocations [Core]  <!-- UUID: b86632f7-9311-4313-956f-dd502be7480c -->

The in progress Invocations of the Integration Boost Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.5.2.2 - Active Instances](2628525c-6956-49dd-9a48-e3de403a0597).

#### A.6.1.1.7.2.5.3 - Pioneer Chain Primitive [Core]  <!-- UUID: ad535f1f-c7f0-4cd8-aca0-5a447dc2622b -->

The documents herein contain all data and specifications for Osero's Instances of the Pioneer Chain Primitive. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).

##### A.6.1.1.7.2.5.3.1 - Primitive Hub Document [Core]  <!-- UUID: 92023efc-2ee6-4f98-9750-574f90e21184 -->

The documents herein organize all base information relevant to Osero's usage of the Pioneer Chain Primitive.

###### A.6.1.1.7.2.5.3.1.1 - Global Activation Status [Core]  <!-- UUID: e33acbf0-cf13-4e74-acb0-23319b551d42 -->

`Active`

###### A.6.1.1.7.2.5.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 04a6899a-8b0c-4b3d-873a-69325cc5bf50 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.5.3.1.2.1 - Plasma Instance Configuration Document Location [Core]  <!-- UUID: 04ba9c33-02e3-44e1-a003-9b9ca96bcdb2 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.5.3.2.1 - Plasma Instance Configuration Document](eb40fb85-194c-4bae-a0c4-24c66df4735e).

###### A.6.1.1.7.2.5.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 0e7ab6cf-3e07-4f0d-9294-802072d07a4e -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.5.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: ce54fef7-9758-4c98-8e3f-bed68ff82f73 -->

This document contains a Directory of all prospective Instances of the Pioneer Chain Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.5.3.1.2 - Active Instances Directory](04a6899a-8b0c-4b3d-873a-69325cc5bf50), whereas failed Invocations are Archived in [A.6.1.1.7.2.5.3.1.5 - Hub Data Repository](5cd1f6cd-7349-429d-9f3d-42aaca039b69).

###### A.6.1.1.7.2.5.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 5cd1f6cd-7349-429d-9f3d-42aaca039b69 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.5.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 2c6db399-c525-49bd-b020-4761a50ce837 -->

The subtrees for archived Invocations and Instances of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.7.2.5.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: c31b6835-60e8-445d-94f6-924b1d81d5ed -->

The subtrees for failed Invocations of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.7.2.5.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 7415359b-8d19-4607-9054-30258781eb51 -->

The subtrees for Instances of the Pioneer Chain Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.5.3.2 - Active Instances [Core]  <!-- UUID: 1cf22b6c-83d7-4ddf-8b4c-13059f4ec555 -->

The Instances of the Pioneer Chain Primitive with `Active` Status are stored herein.

###### A.6.1.1.7.2.5.3.2.1 - Plasma Instance Configuration Document [Core]  <!-- UUID: eb40fb85-194c-4bae-a0c4-24c66df4735e -->

The documents herein contain the Instance Configuration Document for the Plasma Instance of the Pioneer Chain Primitive.

###### A.6.1.1.7.2.5.3.2.1.1 - Parameters [Core]  <!-- UUID: 3f22028a-59e5-470c-b5bf-80226706d085 -->

The documents herein define the parameters of the Plasma Instance of the Pioneer Chain Primitive.

###### A.6.1.1.7.2.5.3.2.1.1.1 - Instance Identifiers [Core]  <!-- UUID: 96f5ca50-30db-43ca-aa03-ba7b88835db5 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.7.2.5.3.2.1.1.1.1 - Network [Core]  <!-- UUID: 774ad565-8ee2-4abc-87d6-390ee470b18b -->

Plasma

###### A.6.1.1.7.2.5.3.2.1.1.2 - Pioneer Incentive Pool [Core]  <!-- UUID: 3e96125b-ce79-4639-86a7-d22db2ee801e -->

The documents herein contain the terms that govern this Instance's Pioneer Incentive Pool and its address.

###### A.6.1.1.7.2.5.3.2.1.1.2.1 - Address [Core]  <!-- UUID: dd6dfbb0-c7fc-45be-ad2c-aeca560eb644 -->

The address of Osero's Pioneer Incentive Pool is Osero's SubProxy Account on the Ethereum Mainnet: `0x24fdcd3bFA5C2553e05B2f9AD0365EBC296278D3`.

###### A.6.1.1.7.2.5.3.2.1.1.2.2 - Terms [Core]  <!-- UUID: 60702f4c-cbfe-416f-aab9-f8097fbca47a -->

The Pioneer Incentive Pool for this Instance is governed by the terms specified in [A.2.2.9.3.1.4 - Pioneer Incentive Pool](04edac33-19d5-4a87-a8ab-945a0cd57771).

###### A.6.1.1.7.2.5.3.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 5127e898-68b8-4ae5-8a7f-92202a9d2553 -->

The documents herein define the process for the ongoing management of the Plasma Instance of the Pioneer Chain Primitive.

###### A.6.1.1.7.2.5.3.2.1.3 - Data Repository [Core]  <!-- UUID: 652f040b-29ed-4578-a502-e8fe037bb436 -->

The documents herein contain data relevant to the Plasma Instance of the Pioneer Chain Primitive.

##### A.6.1.1.7.2.5.3.3 - Completed Instances [Core]  <!-- UUID: 472618e9-29c6-406e-928d-d79dff4b9722 -->

The Instances of the Pioneer Chain Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.5.3.4 - In Progress Invocations [Core]  <!-- UUID: 990419d2-5061-4d9a-97b7-00a7b9e7a86c -->

The in progress Invocations of the Pioneer Chain Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.5.3.2 - Active Instances](1cf22b6c-83d7-4ddf-8b4c-13059f4ec555).

### A.6.1.1.7.2.6 - Supply Side Stablecoin Primitives [Core]  <!-- UUID: f37cc62c-9e14-40b2-9cb7-b78add3111b4 -->

The documents herein implement the Supply Side Stablecoin Primitives for Osero. See [A.2.2.10 - Supply Side Stablecoin Primitives](d1142876-33c2-4e21-9339-d8711525d46f).

#### A.6.1.1.7.2.6.1 - Allocation System Primitive [Core]  <!-- UUID: d3d385ed-e53b-4b3f-be9f-4cbeee3420b4 -->

The documents herein contain all data and specifications for Osero's Allocation System Primitive Instances. See [A.2.2.10.1 - Allocation System Primitive](9db14ab7-bb4b-4751-8084-843bd4359f2a).

##### A.6.1.1.7.2.6.1.1 - Primitive Hub Document [Core]  <!-- UUID: 8a97ce72-1505-4301-a647-e3b28c839bf8 -->

The documents herein organize all base information relevant to Osero's usage of the Allocation System Primitive.

###### A.6.1.1.7.2.6.1.1.1 - Global Activation Status [Core]  <!-- UUID: 8b0c94e2-0489-463b-bb9b-d1571d7240e6 -->

`Active`

###### A.6.1.1.7.2.6.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 57de5036-2c56-4cb6-b1dd-8e2dc1b214f6 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.6.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: 4c7bab4f-b60d-46f6-a5cc-0071218d5ddf -->

The documents herein contain a Directory of all Instances on the Ethereum Mainnet of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.6.1.1.2.1.1 - SparkLend [Core]  <!-- UUID: 5d2cd0cf-2e73-490b-9d9c-a662e15688cb -->

The Ethereum Mainnet Instances of the SparkLend Protocol with `Active` Status are stored herein.

###### A.6.1.1.7.2.6.1.1.2.1.1.1 - Ethereum Mainnet - SparkLend USDS Instance Configuration Document Location [Core]  <!-- UUID: 39dca6a6-fd8c-44fd-bd51-510d0cc9a122 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.7.2.6.1.3.1.1.1 - Ethereum Mainnet - SparkLend USDS Instance Configuration Document](80b9a7d4-e110-45ec-955b-ebd6d0c8aa39).

###### A.6.1.1.7.2.6.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 4c12626b-272a-4886-b7af-c6968b021fc2 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.6.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 759c5f6a-7c13-466f-9130-0801575b0145 -->

This document contains a Directory of all prospective Instances of the Allocation System Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.6.1.1.2 - Active Instances Directory](57de5036-2c56-4cb6-b1dd-8e2dc1b214f6), whereas failed Invocations are Archived in [A.6.1.1.7.2.6.1.1.5 - Hub Data Repository](7936954e-cfc9-4491-9432-842450e86af3).

###### A.6.1.1.7.2.6.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 7936954e-cfc9-4491-9432-842450e86af3 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.6.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 3db6fb6f-37fd-4872-a427-38d811af0192 -->

The subtrees for archived Invocations and Instances of the Allocation System Primitive are stored here.

###### A.6.1.1.7.2.6.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 1651e4eb-66a7-4f72-b7ad-27b34786bc02 -->

The subtrees for failed Invocations of the Allocation System Primitive are stored here.

###### A.6.1.1.7.2.6.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 4109cac5-0f83-4274-8061-fb55d4ef1df7 -->

The subtrees for Instances of the Allocation System Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.6.1.2 - Multi-Instance Coordinator Document [Core]  <!-- UUID: f9501c81-b5cd-4c07-b781-539974d39f1d -->

The documents herein provide general specifications of the Osero Liquidity Layer and define Osero's overarching strategy and operational framework for managing across all Instances.

###### A.6.1.1.7.2.6.1.2.1 - General Specifications [Core]  <!-- UUID: 38996719-e2ff-491b-89b4-c63fcbaf5353 -->

The documents herein contain general specifications for the Osero Liquidity Layer.

###### A.6.1.1.7.2.6.1.2.1.1 - Osero Liquidity Layer Architecture [Core]  <!-- UUID: e8f3afd5-d1a8-4379-826c-2c3bcc365947 -->

The documents herein describe the high-level design of the Osero Liquidity Layer, including its key smart contracts and their functionality.

###### A.6.1.1.7.2.6.1.2.1.1.1 - Osero Liquidity Layer Addresses [Core]  <!-- UUID: 4148f5dc-ec79-4e4e-96ea-debf17e8bc28 -->

The subdocuments herein provide the addresses of the Osero Liquidity Layer's constituent contracts.

###### A.6.1.1.7.2.6.1.2.1.1.1.1 - Allocator Contract Addresses [Core]  <!-- UUID: 22f84daa-f402-433d-8bd2-4a03b5776e20 -->

The documents herein contain global key addresses for the Allocator Contracts.

###### A.6.1.1.7.2.6.1.2.1.1.1.1.1 - Ethereum Mainnet [Core]  <!-- UUID: 451328dd-17f0-4efd-8515-377ce6a138b6 -->

The documents herein contain the Allocator Contract Addresses on the Ethereum Mainnet.

###### A.6.1.1.7.2.6.1.2.1.1.1.1.1.1 - Allocator Buffer Contract [Core]  <!-- UUID: 7f40e7d1-ed33-4b31-8641-d721f1dc2f01 -->

The address of the ALLOCATOR_BUFFER contract is: `0xD0BB61b34771146e31055f20f329cDf97429F889`.

###### A.6.1.1.7.2.6.1.2.1.1.1.1.1.2 - Allocator Vault Contract [Core]  <!-- UUID: 0562eb6d-3770-4c3c-851b-7a6f9f5b2aa0 -->

The address of the ALLOCATOR_VAULT (ALLOCATOR-PRYSM-A) contract is: `0x146181Aa9B362EaEC2eC3aDd7429a06D53B43d1a`.

###### A.6.1.1.7.2.6.1.2.1.1.1.1.1.3 - Allocator Oracle Contract [Core]  <!-- UUID: eafb8f6f-3b1d-4783-af72-ef7ded7ac9b3 -->

The address of the ALLOCATOR_ORACLE contract is: `0xc7B91C401C02B73CBdF424dFaaa60950d5040dB7`.

###### A.6.1.1.7.2.6.1.2.1.1.1.1.1.4 - Allocator Registry Contract [Core]  <!-- UUID: e1babaf7-acb6-4977-b340-6402d605b488 -->

The address of the ALLOCATOR_REGISTRY contract is: `0xCdCFA95343DA7821fdD01dc4d0AeDA958051bB3B`.

###### A.6.1.1.7.2.6.1.2.1.1.1.1.1.5 - Allocator Roles Contract [Core]  <!-- UUID: f612bab0-2401-4166-9443-f1a9d2966dbe -->

The address of the ALLOCATOR_ROLES contract is: `0x9A865A710399cea85dbD9144b7a09C889e94E803`.

###### A.6.1.1.7.2.6.1.2.1.1.1.2 - Diamond PAU Contracts [Core]  <!-- UUID: 00360509-2608-4e2b-9551-769df2931173 -->

The documents herein define the addresses of the Diamond Parallelized Allocation Unit (Diamond PAU) contracts deployed for the Osero Liquidity Layer. The Diamond PAU is a modular implementation of the Allocation System in which the Controller dispatches operations to shared Facet contracts, with integration configurations held in a shared Beacon contract. The Beacon and the Facet contracts are shared across Diamond PAU implementations and are specified in [A.2.2.10.1.1.1.2.3 - Liquidity Layer Shared Contracts](a2677d19-1f2c-4361-bedc-34cb2e7eaab5).

###### A.6.1.1.7.2.6.1.2.1.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: f7cfed3f-e724-4aa8-b5e1-3900c84293c7 -->

The documents herein define the addresses of the Diamond PAU contracts on Ethereum Mainnet.

###### A.6.1.1.7.2.6.1.2.1.1.1.2.1.1 - ALM Proxy Contract [Core]  <!-- UUID: 6869558b-7215-4bec-a93e-475c0963262b -->

The address of the ALM Proxy contract is: `0x6d370e359e9cbd0Fd35Bb38fAF705D84238CB884`. The ALM Proxy custodies the Instance's funds and routes calls to external contracts as directed by the Controller contract.

###### A.6.1.1.7.2.6.1.2.1.1.1.2.1.2 - Controller Contract [Core]  <!-- UUID: 8e1d584f-6368-493d-a6c5-c5068250b63a -->

The address of the Controller contract is: `0x24169Afb34fAe4D4356BC54Bd80319131e35ca38`. The Controller is the entry point for all allocator operations; it synchronizes integration configurations from the shared Beacon contract specified in [A.2.2.10.1.1.1.2.3.1 - Beacon](5b0627e8-102b-42ea-8d9b-38463591faf9) and dispatches calls to the appropriate Facet contract specified in [A.2.2.10.1.1.1.2.3.2 - Facets](b7c73a0c-456d-4e75-93ac-8eec185ece31).

###### A.6.1.1.7.2.6.1.2.1.1.1.2.1.3 - AccessControls Contract [Core]  <!-- UUID: 6694670e-d13c-4466-afde-2830820ac000 -->

The address of the AccessControls contract is: `0x791D2a017532CfAD881c446e6bF93BbC3c0778b2`. The AccessControls contract manages the roles and permissions of the Diamond PAU, as specified in [A.2.2.10.1.1.1.2.2 - Liquidity Layer Role Definitions](2ae4b91a-6900-41e8-9718-32805b956550).

###### A.6.1.1.7.2.6.1.2.1.1.1.2.1.4 - ALM Rate Limits Contract [Core]  <!-- UUID: a6111874-7c68-4476-b282-20631378174a -->

The address of the ALM Rate Limits contract is: `0xE9a78f34fe497e2186f81B8c014cd93B308BC62a`. The ALM Rate Limits contract enforces the rate limits on operations performed through the Controller contract.

###### A.6.1.1.7.2.6.1.2.1.1.1.2.1.5 - AdministeredAgent Contract [Core]  <!-- UUID: 0eed3609-62a2-4c5b-ae5b-4f78212252ee -->

The address of the AdministeredAgent contract is: `0x1837505D104F7a6D8b7e19452610B0A3D652EF12`. The AdministeredAgent holds the Allocator Role as specified in [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) and mediates relayer access to the Controller: the Relayer Multisigs are registered as its Actors, as specified in [A.2.2.10.1.1.1.2.2.4 - Actor](636a39e4-5908-4fee-bae8-e0b11e0d9c55), and submit operations through it, while the Freezer Multisig is registered as a Revoker, as specified in [A.2.2.10.1.1.1.2.2.5 - Revoker](cc7cb4b7-981e-44f5-a0d5-62e5b47d112e), authorized to remove a compromised Actor.

###### A.6.1.1.7.2.6.1.2.1.1.2 - RateLimits [Core]  <!-- UUID: cec50748-c32f-4496-8e8d-d4a38dbb0e63 -->

The documents herein list the rate limits for the Osero Liquidity Layer Diamond PAU.

###### A.6.1.1.7.2.6.1.2.1.1.2.1 - Diamond PAU Rate Limits [Core]  <!-- UUID: 325731dc-5e89-4a8a-9d64-91b203febf48 -->

The documents herein list the Diamond PAU rate limits for the Osero Liquidity Layer.

###### A.6.1.1.7.2.6.1.2.1.1.2.1.1 - USDS Mint Maximum [Core]  <!-- UUID: c6456279-0dab-4517-aad9-46d9e8d4aede -->

The maximum amount of USDS that can be minted by the Osero Diamond PAU (`LIMIT_USDS_MINT`) is specified in the document herein.
- `maxAmount`: 5,000,000 USDS
- `slope`: 5,000,000 USDS per day

###### A.6.1.1.7.2.6.1.2.1.1.2.1.2 - USDS Burn Maximum [Core]  <!-- UUID: eafa2031-9560-4b23-aa7a-f4ee62097438 -->

The maximum amount of USDS that can be burned by the Osero Diamond PAU (`LIMIT_USDS_BURN`) is specified in the document herein.
- `maxAmount`: Unlimited

###### A.6.1.1.7.2.6.1.2.1.1.3 - On-chain Parameters [Core]  <!-- UUID: 5b8cc141-bd99-4b69-b4de-854b4c7f5002 -->

The documents herein list general on-chain parameters for the Osero Liquidity Layer.

###### A.6.1.1.7.2.6.1.2.1.1.3.1 - Allocator Vault Parameters [Core]  <!-- UUID: b42ff812-17ba-408f-8e0d-7f1746906e1a -->

The Allocator Vault parameters for ALLOCATOR-PRYSM-A are defined in [A.3.7.1.2.1.7 - ALLOCATOR-PRYSM-A Parameters](17630a67-b287-4f44-bc60-f2a4f5d16cfa).

###### A.6.1.1.7.2.6.1.2.1.1.3.2 - Whitelisting Of ALM Proxy [Core]  <!-- UUID: 817fabeb-fcd9-42f4-bcdb-863c67105ccf -->

The ALM Proxy for the Osero Diamond PAU will be whitelisted on the litePSM in an upcoming spell. This will allow it to call `buyGemNoFee` and `sellGemNoFee` on the `MCD_LITE_PSM_USDC_A` contract, enabling no-fee USDS and USDC swaps through the PSM.

###### A.6.1.1.7.2.6.1.2.1.2 - Governance Processes [Core]  <!-- UUID: d6410ff9-1cb6-4433-a455-15ba6d571b8f -->

The documents herein describe the specific governance processes for the Osero Liquidity Layer.

###### A.6.1.1.7.2.6.1.2.1.2.1 - Multisigs [Core]  <!-- UUID: 8b94b40a-a729-426c-8544-3e93175c5b9f -->

The documents herein define the multisigs that hold privileged access in the Osero Liquidity Layer.

###### A.6.1.1.7.2.6.1.2.1.2.1.1 - Osero Relayer Multisig [Core]  <!-- UUID: 1830fb80-a44b-4aaf-b72c-7c4997cb9486 -->

The Osero Relayer Multisig is registered as an Actor on the AdministeredAgent, which holds the Allocator Role as specified in [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a), and is controlled by Osero.

###### A.6.1.1.7.2.6.1.2.1.2.1.1.1 - Address [Core]  <!-- UUID: d39e8188-807c-4cf1-8952-e02e455e255b -->

The address of the Osero Relayer Multisig on Ethereum Mainnet is `0x29c5A20A49A0D522A3714af97C517a908946b6A8`.

###### A.6.1.1.7.2.6.1.2.1.2.1.1.2 - Required Number Of Signers [Core]  <!-- UUID: 9abbed49-3b16-4bb3-956c-7809958b1b9a -->

The Osero Relayer Multisig currently has a 2/3 signing requirement.

###### A.6.1.1.7.2.6.1.2.1.2.1.1.3 - Signers [Core]  <!-- UUID: 2ecfa2d0-b20c-41fa-99c9-8c865d665519 -->

The signers of the Osero Relayer Multisig are three (3) addresses controlled by Osero.

###### A.6.1.1.7.2.6.1.2.1.2.1.1.4 - Usage Standards [Core]  <!-- UUID: 4721045a-46d0-42b9-b763-9826b7c88735 -->

The signers of the Osero Relayer Multisig must use the Multisig to submit allocator operations through the AdministeredAgent in accordance with the instructions specified in the Osero Artifact.

###### A.6.1.1.7.2.6.1.2.1.2.1.1.5 - Modification [Core]  <!-- UUID: da68307c-23cb-48fa-b6cc-52a31f812dc5 -->

Osero can change the signers of the Osero Relayer Multisig at any time, so long as there are at least two (2) signers and at least a majority of signers are required to execute transactions.

###### A.6.1.1.7.2.6.1.2.1.2.1.2 - Core Operator Relayer Multisig [Core]  <!-- UUID: f48b14c7-6dd1-4d10-b546-a604be45758c -->

The Core Operator Relayer Multisig is registered as an Actor on the AdministeredAgent, which holds the Allocator Role as specified in [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a), and is controlled by Operational GovOps Soter Labs.

###### A.6.1.1.7.2.6.1.2.1.2.1.2.1 - Address [Core]  <!-- UUID: 92ed192c-7019-4864-b06d-c56fec8d3414 -->

The address of the Core Operator Relayer Multisig on Ethereum Mainnet is `0x3dE688267Cf099307aBdd85F64D8efe03D0b2b26`.

###### A.6.1.1.7.2.6.1.2.1.2.1.2.2 - Required Number Of Signers [Core]  <!-- UUID: 4d53e814-8131-4fb9-b9d3-17e27ed04f9e -->

The Core Operator Relayer Multisig currently has a 2/3 signing requirement.

###### A.6.1.1.7.2.6.1.2.1.2.1.2.3 - Signers [Core]  <!-- UUID: b35e8470-3b60-4093-a7d4-384f2a86f44d -->

The signers of the Core Operator Relayer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs.

###### A.6.1.1.7.2.6.1.2.1.2.1.2.4 - Usage Standards [Core]  <!-- UUID: 5c9542e5-bd8c-4c9d-a6d2-c2f8382f13d1 -->

The signers of the Core Operator Relayer Multisig must use the Multisig to submit allocator operations through the AdministeredAgent in accordance with the instructions specified in the Osero Artifact.

###### A.6.1.1.7.2.6.1.2.1.2.1.2.5 - Modification [Core]  <!-- UUID: 7c52496f-8863-44a1-8e62-119f755fc038 -->

Soter Labs can change the signers of the Core Operator Relayer Multisig at any time, so long as there are at least two (2) signers and at least a majority of signers are required to execute transactions.

###### A.6.1.1.7.2.6.1.2.1.2.1.3 - Freezer Multisig [Core]  <!-- UUID: 51460bc2-f5fb-4302-912a-ed3e6943aae0 -->

The Freezer Multisig is registered as a Revoker on the AdministeredAgent, as specified in [A.2.2.10.1.1.1.2.2.5 - Revoker](cc7cb4b7-981e-44f5-a0d5-62e5b47d112e).

###### A.6.1.1.7.2.6.1.2.1.2.1.3.1 - Address [Core]  <!-- UUID: 3b22b5f4-3cc4-4c47-9b84-a64fb4f3b159 -->

The address of the Freezer Multisig on Ethereum Mainnet is `0xF61F90907551a8A23f0f8EEE9658Fa53326de603`.

###### A.6.1.1.7.2.6.1.2.1.2.1.3.2 - Required Number Of Signers [Core]  <!-- UUID: 3639aaf9-48b9-4021-8ccc-76d956689c83 -->

The Freezer Multisig currently has a 2/5 signing requirement.

###### A.6.1.1.7.2.6.1.2.1.2.1.3.3 - Signers [Core]  <!-- UUID: 5476d3cf-1781-46df-95a2-ff86a7965c97 -->

The signers of the Freezer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs, one (1) address controlled by Operational Facilitator Redline Facilitation Group, and one (1) address controlled by Osero.

###### A.6.1.1.7.2.6.1.2.1.2.1.3.4 - Usage Standards [Core]  <!-- UUID: 0af92fed-3b01-40b2-95c7-a3726241906b -->

The signers of the Freezer Multisig should exercise their authority to remove a compromised or malicious Actor from the AdministeredAgent in the event of an emergency. Each action executed by the Freezer Multisig must be reported to the Sky community within a reasonable time frame.

###### A.6.1.1.7.2.6.1.2.1.2.1.3.5 - Modification [Core]  <!-- UUID: 72931c13-0cd1-44c9-80b7-eb9a83463758 -->

Modification of the signers of the Freezer Multisig must be approved through an Atlas Edit Proposal.

###### A.6.1.1.7.2.6.1.2.1.2.2 - Invoking New Instances [Core]  <!-- UUID: d00957a1-4de5-4234-ae4a-37fc96c975f8 -->

The governance process to invoke a new Instance of the Allocation System Primitive follows the Root Edit process, see [A.6.1.1.7.2.2.2.2.1.2 - Operational Process Definition](cfd923fb-0a53-4dd2-bb4f-5e840bda69c6).

###### A.6.1.1.7.2.6.1.2.1.3 - Total Risk Capital (TRC) Management [Core]  <!-- UUID: 80559817-dc95-4328-95ee-9ba7aefe9369 -->

The documents herein specify requirements related to Osero's Total Risk Capital (TRC) management.

###### A.6.1.1.7.2.6.1.2.1.3.1 - Stablewatch's Operation Of Osero Liquidity Layer And Agreement Regarding Encumbrance Ratio [Core]  <!-- UUID: f70c4c5e-1a8f-4fe1-b95d-3a44d4f47f4b -->

Stablewatch will operate the Osero Liquidity Layer and agrees to stay at or below a 90% Encumbrance Ratio. See [A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9).

###### A.6.1.1.7.2.6.1.2.1.3.2 - Stablewatch's Total Risk Capital (TRC) Management Processes [Core]  <!-- UUID: fc89f81a-cad3-42fe-afc1-880e2ecb73a3 -->

As operators of the Osero Liquidity Layer, Stablewatch automatically inherits, and is subject to, the base class of operational requirements related to Total Risk Capital management defined in [A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capital (TRC) Management](3af8a3a2-25e5-44b3-87a4-7df1f2712685). Modifications to the base operational logic automatically propagate to the Osero Artifact.

###### A.6.1.1.7.2.6.1.2.2 - Osero Liquidity Layer Operational Processes [Core]  <!-- UUID: 5c05c2d0-8189-41f7-b284-7c46286f2457 -->

The documents herein describe common operational procedures for the Osero Liquidity Layer applicable across multiple Instances.

###### A.6.1.1.7.2.6.1.2.2.1 - Routine Protocol [Core]  <!-- UUID: 5c7f2e24-c2e4-43fd-ad43-8ca0fb2d6dc9 -->

The documents herein define the protocol for routine ongoing management of the Osero Liquidity Layer and its active Instances.

###### A.6.1.1.7.2.6.1.2.2.1.1 - Role Hierarchies And Permissions [Core]  <!-- UUID: aae0e1ba-4ed0-4484-9187-3e53f3695ae8 -->

The roles and permissions of the Diamond PAU Instance are the Liquidity Layer roles defined in [A.2.2.10.1.1.1.2.2 - Liquidity Layer Role Definitions](2ae4b91a-6900-41e8-9718-32805b956550), managed by the AccessControls contract. For the Osero Liquidity Layer, the `DEFAULT_ADMIN_ROLE` is held by the Osero SubProxy, and the `CONTROLLER` role by the Controller contract. The `ALLOCATOR_ROLE` is held by the AdministeredAgent contract, as specified in [A.6.1.1.7.2.6.1.2.1.1.1.2.1.5 - AdministeredAgent Contract](0eed3609-62a2-4c5b-ae5b-4f78212252ee). The Osero Relayer Multisig ([A.6.1.1.7.2.6.1.2.1.2.1.1 - Osero Relayer Multisig](1830fb80-a44b-4aaf-b72c-7c4997cb9486)) and the Core Operator Relayer Multisig ([A.6.1.1.7.2.6.1.2.1.2.1.2 - Core Operator Relayer Multisig](f48b14c7-6dd1-4d10-b546-a604be45758c)) are registered as its Actors, as specified in [A.2.2.10.1.1.1.2.2.4 - Actor](636a39e4-5908-4fee-bae8-e0b11e0d9c55). The Freezer Multisig ([A.6.1.1.7.2.6.1.2.1.2.1.3 - Freezer Multisig](51460bc2-f5fb-4302-912a-ed3e6943aae0)) is registered as a Revoker, as specified in [A.2.2.10.1.1.1.2.2.5 - Revoker](cc7cb4b7-981e-44f5-a0d5-62e5b47d112e).

###### A.6.1.1.7.2.6.1.2.2.1.2 - Controller Functions [Core]  <!-- UUID: 14aa9d85-4878-49b9-9cd7-d6a014bdecea -->

The Diamond PAU Controller functions for the Osero Liquidity Layer are the shared Diamond PAU Controller functions specified in [A.2.2.10.1.1.1.2.5.2 - Diamond PAU Controller Functions](5e941add-bf8d-4623-95a1-69795e7f7034). The Facets used by the Osero Liquidity Layer are specified in the documents herein.

###### A.6.1.1.7.2.6.1.2.2.1.2.1 - USDS Facet [Core]  <!-- UUID: 9b35cae7-b629-4bf8-b2d1-472bedebae14 -->

The Osero Liquidity Layer uses the USDS Facet ([A.2.2.10.1.1.1.2.3.2.22 - USDS Facet](917e1162-3c06-4508-b0e9-02c5eefc1346)) to mint and burn USDS through the allocator vault.

###### A.6.1.1.7.2.6.1.2.2.1.2.2 - Aave v3 Facet [Core]  <!-- UUID: f983e134-c97d-4e90-94d6-4cad14d0702f -->

The Osero Liquidity Layer uses the Aave v3 Facet ([A.2.2.10.1.1.1.2.3.2.1 - Aave v3 Facet](c9ecd9c2-dd1b-426b-8e52-66a2b1892289)) to deposit into and withdraw from SparkLend USDS.

###### A.6.1.1.7.2.6.1.2.2.1.3 - Rate Limit Management [Core]  <!-- UUID: a0fca594-a7b9-45fa-9be1-a209d5341029 -->

The rate limits of the Osero Liquidity Layer are managed as specified in [A.2.2.10.1.1.1.2.5.3 - Rate Limit Management](6f5bc654-a053-4b1f-9ada-6aa13d0a2109). The Osero-specific rate limit values are specified under the [A.6.1.1.7.2.6.1.2.1.1 - Osero Liquidity Layer Architecture](e8f3afd5-d1a8-4379-826c-2c3bcc365947) and the [A.6.1.1.7.2.6.1.3.1.1.1 - Ethereum Mainnet - SparkLend USDS Instance Configuration Document](80b9a7d4-e110-45ec-955b-ebd6d0c8aa39).

###### A.6.1.1.7.2.6.1.2.2.1.4 - Instance Lifecycle Management [Core]  <!-- UUID: bbbb38cb-5a0d-4f5f-9361-33ebb954e4ca -->

The documents herein define processes for invoking (onboarding) new Osero Liquidity Layer Instances and offboarding existing ones. This process will be specified in a future iteration of the Osero Artifact.

###### A.6.1.1.7.2.6.1.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 28bcf2f0-31b8-466d-90f5-3579002840a0 -->

The documents herein define the process for non-routine ongoing management of the Osero Liquidity Layer and its active Instances.

###### A.6.1.1.7.2.6.1.2.2.3 - Emergency Protocol [Core]  <!-- UUID: b202047d-a1da-4cf6-b7d2-89d35c707cfb -->

The documents herein define the actions that can be taken in the event of an emergency within Osero Liquidity Layer operations.

###### A.6.1.1.7.2.6.1.2.2.3.1 - Remove Compromised Actor As Freezer [Core]  <!-- UUID: 39b320a8-240c-487d-9c72-25b8a2457a4b -->

In the event of a compromised or malicious Actor, the Freezer Multisig — registered as a Revoker on the AdministeredAgent, as specified in [A.2.2.10.1.1.1.2.2.5 - Revoker](cc7cb4b7-981e-44f5-a0d5-62e5b47d112e) — removes that Actor by calling `removeActor` on the AdministeredAgent contract. Removing the Actor prevents it from submitting further operations, while the Allocator Role itself remains with the AdministeredAgent. This action should only be taken if a Relayer Multisig's keys have been leaked or compromised and the Actor is in the control of an external bad actor.

###### A.6.1.1.7.2.6.1.2.2.3.2 - Withdraw All SparkLend Positions [Core]  <!-- UUID: 7ba1cc79-9a9f-460c-85b8-72181788397f -->

In the event that liquidity must be recovered from SparkLend and centralized in the Osero ALM Proxy, a Relayer Multisig, acting as an Actor, withdraws the Osero Liquidity Layer's full SparkLend USDS position through the Aave v3 Facet, as specified in [A.2.2.10.1.1.1.2.5.2.2.2 - Withdraw From Aave v3 Market](038eaa5c-d4c0-4a56-8d30-bc3a04508f0e). SparkLend withdrawals are unlimited so that the full position can be unwound.

###### A.6.1.1.7.2.6.1.2.2.3.3 - Burn USDS [Core]  <!-- UUID: 3040614f-1100-45e5-a0dc-9ab22c383e9d -->

Once liquidity has been recovered to the Osero ALM Proxy, the recovered USDS is repaid and burned through the USDS Facet, as specified in [A.2.2.10.1.1.1.2.5.2.1.2 - Burn USDS](f01e63b7-dde7-422a-89a1-6931839d49f5). USDS burning is unlimited so that the full outstanding amount can be burned.

##### A.6.1.1.7.2.6.1.3 - Active Instances [Core]  <!-- UUID: 6f8a8e14-13be-4893-9bb1-17c88e984426 -->

The Instances of the Allocation System Primitive with `Active` Status are stored herein.

###### A.6.1.1.7.2.6.1.3.1 - Ethereum Mainnet Instances [Core]  <!-- UUID: 3ebb2e50-311f-4dab-9ad9-faff0e59d3b6 -->

The Ethereum Mainnet Instances of the Osero Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.7.2.6.1.3.1.1 - SparkLend [Core]  <!-- UUID: a0487ced-39d2-487d-9415-55620a12ea3c -->

The Ethereum Mainnet Instances of the SparkLend Protocol with `Active` Status are stored herein.

###### A.6.1.1.7.2.6.1.3.1.1.1 - Ethereum Mainnet - SparkLend USDS Instance Configuration Document [Core]  <!-- UUID: 80b9a7d4-e110-45ec-955b-ebd6d0c8aa39 -->

The documents herein contain the Instance Configuration Document for the SparkLend USDS Instance.

###### A.6.1.1.7.2.6.1.3.1.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: a68dddff-9e7a-461f-b56c-85e0614ad78e -->

**`Covered`**

###### A.6.1.1.7.2.6.1.3.1.1.1.2 - Parameters [Core]  <!-- UUID: 71bf4607-f3cc-45e6-a79d-917af5bd95ef -->

The documents herein define the parameters of the SparkLend USDS Instance of the Allocation System Primitive.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 3f389fbe-9815-4728-bb34-e81aff55d8e7 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.1.1 - Network [Core]  <!-- UUID: a49f2d1a-b8d1-4066-b656-28168366025e -->

Ethereum Mainnet

###### A.6.1.1.7.2.6.1.3.1.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: ecc20a97-6e7f-4f12-8445-d3c1d687353b -->

SparkLend

###### A.6.1.1.7.2.6.1.3.1.1.1.2.1.3 - Asset Supplied By Osero Liquidity Layer [Core]  <!-- UUID: 3d5895e3-8da8-46b5-82c0-bdef81c3346d -->

USDS

###### A.6.1.1.7.2.6.1.3.1.1.1.2.1.4 - Token [Core]  <!-- UUID: 1a208cb9-a2c7-488f-af77-c97945169971 -->

spUSDS

###### A.6.1.1.7.2.6.1.3.1.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: bd92de02-23e3-4572-912b-3f233c5b25d2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 26708475-708e-450d-aa9b-9ef21b63af89 -->

`0xC02aB1A5eaA8d1B114EF786D9bde108cD4364359`

###### A.6.1.1.7.2.6.1.3.1.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 96540b0d-ff98-46a9-b379-f1a5e0b9db93 -->

`0xdC035D45d973E3EC169d2276DDab16f1e407384F`

###### A.6.1.1.7.2.6.1.3.1.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 7955432c-9f6e-428f-81ed-107a4f78981a -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 5a8c4661-e07f-4182-becc-ff724b7d16e9 -->

The inflow RateLimitID is: `0x5534da2f28b3dd200cb0042c0876cd6e2beca93d3232c366ec077018c82da73d`.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: b9360d7a-7cd4-4019-909d-bd729334cd5c -->

The outflow RateLimitID is: `0xf9ac1455c7ba8e0bacb7a3eca4a2cf412eda3cbc0f6aa1b071d73b37d49925d8`.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.4 - Rate Limits [Core]  <!-- UUID: d0d163d7-b9d3-4e7d-9371-0a8c48bf2d9f -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: e3b12e29-eb67-40be-8cac-85913eff958c -->

The deposit rate limits are:
- `maxAmount`: 5,000,000 USDS
- `slope`: 5,000,000 USDS per day

###### A.6.1.1.7.2.6.1.3.1.1.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: b021fcff-b1e3-456d-a1e6-f14604784100 -->

The withdrawal rate limits are:
- `maxAmount`: Unlimited

###### A.6.1.1.7.2.6.1.3.1.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 9781b3b4-bc78-49e6-9f4d-8da869ee113f -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.5.1 - Max Slippage [Core]  <!-- UUID: b650660f-a579-42ce-bc7e-6f6046d9a7b4 -->

The `maxSlippage` for this Instance is 0.01%.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.5.2 - Maximum Exposure [Core]  <!-- UUID: 7baff09a-9aae-4abc-9643-dcb20940fe4d -->

The Maximum Exposure for this Instance is 5,000,000 USDS.

###### A.6.1.1.7.2.6.1.3.1.1.1.2.5.3 - Capital Ratio Requirement [Core]  <!-- UUID: 771b1a44-5bb6-4c9b-92de-e45485c5a11f -->

The Capital Ratio Requirement for this Instance, as specified in [A.3.2.1.1.1 - Capital Ratio Requirement](3828778e-0197-4ce9-a836-6770d04f2ea9), is 25%.

###### A.6.1.1.7.2.6.1.3.1.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: ff10e260-7465-4dd0-a1c3-899a66f3bbcb -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Osero Liquidity Layer processes.

##### A.6.1.1.7.2.6.1.4 - Completed Instances [Core]  <!-- UUID: 1292a07b-637f-4b35-adc1-1a9bdeee9566 -->

The Instances of the Allocation System Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.6.1.5 - In Progress Invocations [Core]  <!-- UUID: 475822f8-5a16-48e3-8228-85785657b2ac -->

The in progress Invocations of the Allocation System Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.6.1.3 - Active Instances](6f8a8e14-13be-4893-9bb1-17c88e984426).

#### A.6.1.1.7.2.6.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: 8faea57c-348a-4d40-b241-868d5dbc8008 -->

The documents herein contain all data and specifications for Osero's Instances of the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.6.1.1.7.2.6.2.1 - Primitive Hub Document [Core]  <!-- UUID: 16f4cc5c-09ce-4ccd-be18-5a9a333e99d7 -->

The documents herein organize all base information relevant to Osero's usage of the Risk Capital Rental Primitive.

###### A.6.1.1.7.2.6.2.1.1 - Global Activation Status [Core]  <!-- UUID: a1047457-ad33-4d0c-8b60-fa67f3ab57e6 -->

`Inactive`

###### A.6.1.1.7.2.6.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 997d4b26-65c5-4ad3-bbde-3441df9491ff -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.6.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 51b0d96c-ca4c-4a89-8a95-41987d7b6ab7 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.6.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: f72ba911-8c52-402e-a462-e69c13098d34 -->

This document contains a Directory of all prospective Instances of the Risk Capital Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.6.2.1.2 - Active Instances Directory](997d4b26-65c5-4ad3-bbde-3441df9491ff), whereas failed Invocations are Archived in [A.6.1.1.7.2.6.2.1.5 - Hub Data Repository](2c163402-c55f-4995-8866-a0074ff01df6).

###### A.6.1.1.7.2.6.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 2c163402-c55f-4995-8866-a0074ff01df6 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.6.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: a86f03fe-0570-4031-b616-3c1a3f03a65d -->

The subtrees for archived Invocations and Instances of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.7.2.6.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 4cb29356-93cd-418b-af94-7690a20b3883 -->

The subtrees for failed Invocations of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.7.2.6.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 4eecf3be-1cc1-4981-95d3-e96bc553652b -->

The subtrees for Instances of the Risk Capital Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.6.2.2 - Active Instances [Core]  <!-- UUID: d48fecab-0528-4d96-b760-49ca8568be85 -->

The Instances of the Risk Capital Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.6.2.3 - Completed Instances [Core]  <!-- UUID: 32d1da62-94e0-4881-95cc-434c65aca77b -->

The Instances of the Risk Capital Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.6.2.4 - In Progress Invocations [Core]  <!-- UUID: d55dafa1-0e6c-4e2a-9cfe-bcac3ccaa6ac -->

The in progress Invocations of the Risk Capital Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.6.2.2 - Active Instances](d48fecab-0528-4d96-b760-49ca8568be85).

#### A.6.1.1.7.2.6.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: da849319-df3c-4b3b-a100-157828990761 -->

The documents herein contain all data and specifications for Osero's Instances of the Asset Liability Management Rental Primitive. See [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

##### A.6.1.1.7.2.6.3.1 - Primitive Hub Document [Core]  <!-- UUID: 612c1dde-b718-4d81-8a0c-ce9ed6c018f7 -->

The documents herein organize all base information relevant to Osero's usage of the Asset Liability Management Rental Primitive.

###### A.6.1.1.7.2.6.3.1.1 - Global Activation Status [Core]  <!-- UUID: 24c6a8ba-280e-468e-be34-6c497220850e -->

`Inactive`

###### A.6.1.1.7.2.6.3.1.2 - Active Instances Directory [Core]  <!-- UUID: f6266454-9845-44e8-a079-851ddd576e8f -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.6.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 9b68a034-5b97-49fd-9c05-8fdc0a6b8fcf -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.6.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: b78c2547-cfe5-414f-97f6-af9e763c6721 -->

This document contains a Directory of all prospective Instances of the Asset Liability Management Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.6.3.1.2 - Active Instances Directory](f6266454-9845-44e8-a079-851ddd576e8f), whereas failed Invocations are Archived in [A.6.1.1.7.2.6.3.1.5 - Hub Data Repository](50250f92-7f80-4685-b94d-f1ed639c9c98).

###### A.6.1.1.7.2.6.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 50250f92-7f80-4685-b94d-f1ed639c9c98 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.6.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ead9dc67-a5aa-49b1-a9fb-cbed7ede94e5 -->

The subtrees for archived Invocations and Instances of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.7.2.6.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: fa04da99-79a6-46de-b1bc-160d0ea4e700 -->

The subtrees for failed Invocations of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.7.2.6.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: dc49f561-dade-4b78-bffc-efbc533ab6b9 -->

The subtrees for Instances of the Asset Liability Management Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.6.3.2 - Active Instances [Core]  <!-- UUID: d5f275e5-98b9-4ef7-90dd-f81e786252df -->

The Instances of the Asset Liability Management Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.6.3.3 - Completed Instances [Core]  <!-- UUID: 22b7c4eb-a8e0-4e56-a4ca-590fe8eed182 -->

The Instances of the Asset Liability Management Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.6.3.4 - In Progress Invocations [Core]  <!-- UUID: 9dabbad7-776e-4801-89a3-669341dbb30d -->

The in progress Invocations of the Asset Liability Management Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.6.3.2 - Active Instances](d5f275e5-98b9-4ef7-90dd-f81e786252df).

### A.6.1.1.7.2.7 - Core Governance Primitives [Core]  <!-- UUID: 19c086d0-420a-4c29-b0ac-8d8dec444ce5 -->

The documents herein implement the Core Governance Primitives for Osero. See [A.2.2.11 - Core Governance Primitives](6fa54611-c744-4b9d-897d-b2a20e9cae5d).

#### A.6.1.1.7.2.7.1 - Core Governance Reward Primitive [Core]  <!-- UUID: d4e3b585-bb39-41d7-af60-3a65204e1917 -->

The documents herein contain all data and specifications for Osero's Instances of the Core Governance Reward Primitive. See [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a).

##### A.6.1.1.7.2.7.1.1 - Primitive Hub Document [Core]  <!-- UUID: 095b3dfe-4ea4-4ce3-8a7d-e9253269e096 -->

The documents herein organize all base information relevant to Osero's usage of the Core Governance Reward Primitive.

###### A.6.1.1.7.2.7.1.1.1 - Global Activation Status [Core]  <!-- UUID: eea5262e-a1ba-4394-8769-e5098dc7aff6 -->

`Inactive`

###### A.6.1.1.7.2.7.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 3269b582-af99-475b-b3e2-9d25a079c5ec -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Active`.

###### A.6.1.1.7.2.7.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: db2f0051-f5a0-4392-845d-1b44213299bc -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.7.2.7.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: a108020b-3cbf-493d-8407-5570c36b14e7 -->

This document contains a Directory of all prospective Instances of the Core Governance Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.7.2.7.1.1.2 - Active Instances Directory](3269b582-af99-475b-b3e2-9d25a079c5ec), whereas failed Invocations are Archived in [A.6.1.1.7.2.7.1.1.5 - Hub Data Repository](5b09155b-063c-41c0-b714-4a5d275d7b57).

###### A.6.1.1.7.2.7.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 5b09155b-063c-41c0-b714-4a5d275d7b57 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.7.2.7.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 8039d41b-466d-42e0-aa67-27fb7a686a1f -->

The subtrees for archived Invocations and Instances of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.7.2.7.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 146d622f-f1e3-475c-8a59-b433143c9fbd -->

The subtrees for failed Invocations of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.7.2.7.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: e1922587-e2a8-4ec3-81a8-a325bbe73e18 -->

The subtrees for Instances of the Core Governance Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.7.2.7.1.2 - Active Instances [Core]  <!-- UUID: b4954eea-0108-4820-bdbf-402e74ea1407 -->

The Instances of the Core Governance Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.7.2.7.1.3 - Completed Instances [Core]  <!-- UUID: 06c9df0b-903a-4d24-8906-fb3f7ceec0d0 -->

The Instances of the Core Governance Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.7.2.7.1.4 - In Progress Invocations [Core]  <!-- UUID: 857ab3e5-af7a-4e23-9c1d-0621b8d626a8 -->

The in progress Invocations of the Core Governance Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.7.2.7.1.2 - Active Instances](b4954eea-0108-4820-bdbf-402e74ea1407).

## A.6.1.1.7.3 - Omni Documents [Core]  <!-- UUID: 5e85bc90-de8f-43ab-80ea-4d7657f315a4 -->

The documents herein define Osero's strategic intent and operational processes relating to infrastructure inherited from Sky Core, activities unrelated to Sky Primitives, or activities spanning multiple Sky Primitives.

### A.6.1.1.7.3.1 - Governance Information Unrelated To Root Edit Primitive [Core]  <!-- UUID: a472d201-3dfd-4939-9789-5cedce9ea37a -->

The documents herein specify Osero governance information that is unrelated to the use of the Root Edit Primitive. The governance process for updating the Osero Artifact is specified in the Root Edit Primitive above at [A.6.1.1.7.2.2.2 - Root Edit Primitive](6c61b3d8-6cc8-4250-8173-eee8396a4ef4).

#### A.6.1.1.7.3.1.1 - Sky Forum [Core]  <!-- UUID: 05e36f80-32a1-4181-a98d-feabd2839e50 -->

Osero uses the Sky Forum for governance-related discussion. Posts should use the "Osero Prime" category.

#### A.6.1.1.7.3.1.2 - Sky Ecosystem Emergency Response [Core]  <!-- UUID: 007abab1-5cba-438d-8e91-9ad2b65a5521 -->

The documents herein specify Osero's emergency response protocol in situations that impact the entire Sky Ecosystem. This protocol will be specified in a future iteration of the Osero Artifact.

#### A.6.1.1.7.3.1.3 - Agent-Specific Emergency Response [Core]  <!-- UUID: 83b9de18-b26c-4b7a-a5d9-8cb39f6dec8c -->

The documents herein specify Osero's emergency response protocol in situations solely impacting Osero versus the broader Sky Ecosystem. This protocol will be specified in a future iteration of the Osero Artifact.

### A.6.1.1.7.3.2 - Ecosystem Accords [Core]  <!-- UUID: e5440d4f-c17a-4269-9e45-68f324046c84 -->

Osero has formally agreed to the Ecosystem Accords herein.

#### A.6.1.1.7.3.2.1 - Ecosystem Accord 6 [Core]  <!-- UUID: e80f76d8-ab4e-44be-a649-4bb742d8e149 -->

Osero engaged in terms of agreement with Sky in Ecosystem Accord 6, located in [A.2.8.2.6 - Ecosystem Accord 6: Sky And Osero](45125ff8-5435-4cbf-9b20-9f55a1dbc883).
