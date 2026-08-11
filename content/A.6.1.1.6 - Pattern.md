# A.6.1.1.6 - Pattern [Core]  <!-- UUID: dc083d10-74bc-43b6-ab2f-c91efce76e84 -->

The documents herein specify all of the logic for Pattern, including Pattern's strategy and how it uses the Sky Primitives to operationalize this strategy.

## A.6.1.1.6.1 - Introduction [Core]  <!-- UUID: b137d591-a3a2-482a-a18e-d4ff447964cf -->

Pattern is an Agent providing on-chain liquidity to on-chain and off-chain credit opportunities. Pattern will support new Halo projects focused on both traditional credit and decentralized lending.

## A.6.1.1.6.2 - Sky Primitives [Core]  <!-- UUID: 42740824-41c4-49f1-9b59-177aa36ecc9d -->

The documents herein implement the Sky Primitives for Pattern. See [A.2.2 - Sky Primitives](fcde2604-a138-4c1b-9d9a-14895835c907).

### A.6.1.1.6.2.1 - Genesis Primitives [Core]  <!-- UUID: 6f66d930-9023-420e-b696-4cb59bc11066 -->

The documents herein implement the Genesis Primitives for Pattern. See [A.2.2.5 - Genesis Primitives](3d5e3668-8333-4908-adcc-5784cfe7f6b5).

#### A.6.1.1.6.2.1.1 - Agent Creation Primitive [Core]  <!-- UUID: b6a417d7-f308-4544-a4d7-eabd4d971556 -->

The documents herein contain all data and specifications for Pattern's Instance of the Agent Creation Primitive. See [A.2.2.5.1 - Agent Creation Primitive](82b95f6d-4883-4f08-ac3a-9d8189013fbe).

##### A.6.1.1.6.2.1.1.1 - Primitive Hub Document [Core]  <!-- UUID: a5f738ba-82b4-4a9a-a434-393f7a1da00d -->

The documents herein organize all base information relevant to Pattern's usage of the Agent Creation Primitive.

###### A.6.1.1.6.2.1.1.1.1 - Global Activation Status [Core]  <!-- UUID: ca2897ab-b88e-46bd-9703-955d007f186a -->

`Completed`

###### A.6.1.1.6.2.1.1.1.2 - Active Instances Directory [Core]  <!-- UUID: ecc0bff3-aa5f-4d3f-9804-35646eaedc4a -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.1.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: cfdd7b8f-b40d-4249-9a1f-1e79af084d6d -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.1.1.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 73b79367-bc9c-4df4-a50b-968d5fce2ea0 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.6.2.1.1.3.1 - Single Instance Configuration Document](0587ddd2-1a45-439c-ab47-400ef6f1fc14).

###### A.6.1.1.6.2.1.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: ec6be13b-0544-471e-88f8-77c567e9c8d0 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.6.2.1.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 511e162f-148d-4869-8f6f-d7bfd32f9247 -->

The document herein contains the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.1.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 79863165-2324-4824-8a58-bf4ee9b3bd0c -->

The subtrees for archived Invocations and Instances of the Agent Creation Primitive are stored here.

###### A.6.1.1.6.2.1.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 42f975c1-b9c5-41d6-8f5c-83979b4518e0 -->

The subtrees for failed Invocations of the Agent Creation Primitive are stored here.

###### A.6.1.1.6.2.1.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: a087ab7b-998c-4bbc-a10a-5e1281569e28 -->

The subtrees for Instances of the Agent Creation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.1.1.2 - Active Instances [Core]  <!-- UUID: 8fa0177e-3454-4d44-94e2-ca20873e98d2 -->

The Instances of the Agent Creation Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: b57af67d-e709-41a7-986b-afdd90fd18d1 -->

The Instances of the Agent Creation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.6.2.1.1.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 0587ddd2-1a45-439c-ab47-400ef6f1fc14 -->

The documents herein contain the Instance Configuration Document for the Single Agent Creation Primitive Instance.

###### A.6.1.1.6.2.1.1.3.1.1 - Parameters [Core]  <!-- UUID: 68bc9006-f5bd-4f8e-9608-28a138b0d29c -->

The documents herein define the parameters of the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.6.2.1.1.3.1.1.1 - Name [Core]  <!-- UUID: 3d765fcc-06a8-47ba-b510-60b3e306cb04 -->

The name of the Agent is Pattern.

###### A.6.1.1.6.2.1.1.3.1.1.2 - SubProxy Account [Core]  <!-- UUID: 9703d0ef-84c9-445b-a2b4-bfe9d24363f0 -->

The address of Pattern's SubProxy Account on the Ethereum Mainnet is `0xbC8959Ae2d4E9B385Fe620BEF48C2FD7f4A84736`.

###### A.6.1.1.6.2.1.1.3.1.1.3 - StarGuard Contract [Core]  <!-- UUID: 16b680a4-27f8-457a-acb5-f6c6e8d29d4d -->

The address of Pattern's StarGuard contract on the Ethereum Mainnet is `0x2fb18b28fB39Ec3b26C3B5AF5222e2ca3B8B2269`.

###### A.6.1.1.6.2.1.1.3.1.1.3.1 - StarGuard Max Delay [Core]  <!-- UUID: 5a466516-e901-4490-8d7c-22a31c82902c -->

The Pattern StarGuard `maxDelay` is seven (7) days.

###### A.6.1.1.6.2.1.1.3.1.1.4 - Genesis Account [Core]  <!-- UUID: f2c22b75-0ad5-4a7c-be15-d7f0a2d0af89 -->

The address of Pattern's Genesis Account will be specified in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.1.1.3.1.1.5 - Development Company [Core]  <!-- UUID: 07037190-1bad-41df-9fa3-012c8cd18bdf -->

Pattern Dev Co. is the development company that provides services to Pattern.

###### A.6.1.1.6.2.1.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: e1ea6ef1-5a19-4c09-bbf4-ba67cbc832c8 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.6.2.1.1.3.1.3 - Data Repository [Core]  <!-- UUID: 69ab5e3e-0505-485d-8b3e-225681b7565c -->

The documents herein contain data relevant to the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.6.2.1.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 23b86592-2145-4b96-b74f-7ce8e976b47d -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.1.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 79928bec-a87b-427b-9221-2bc19f92fc8d -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.1.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 63ba43df-c030-47a1-9563-75ee436969d9 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.6.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 38aff44f-e8ef-4734-8e11-fb7894d024a5 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.6.2.1.2 - Prime Transformation Primitive [Core]  <!-- UUID: ddd10617-caa7-4d4c-b088-cee2f888cef9 -->

The documents herein contain all data and specifications for Pattern's instance of the Prime Transformation Primitive. See [A.2.2.5.2 - Prime Transformation Primitive](81411106-fd6d-4f9c-b3ae-7af7b5e62482).

##### A.6.1.1.6.2.1.2.1 - Primitive Hub Document [Core]  <!-- UUID: 73321a03-f62c-4aaf-84de-ee79bfd55662 -->

The documents herein organize all base information relevant to Pattern's usage of the Prime Transformation Primitive.

###### A.6.1.1.6.2.1.2.1.1 - Global Activation Status [Core]  <!-- UUID: 4f8cc1c3-7aa4-4d55-a3c7-c3b90365f52a -->

`Completed`

###### A.6.1.1.6.2.1.2.1.2 - Active Instances Directory [Core]  <!-- UUID: afe290aa-60a5-4e27-869e-b25fc1ed7a9d -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.1.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 85dd2116-5311-4379-b89d-1216a59883e7 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.1.2.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 42771b54-c551-42e2-89ca-b592ccd41eaa -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.6.2.1.2.3.1 - Single Instance Configuration Document](2fcbd692-29c5-4788-8f4e-83b415eca7cd).

###### A.6.1.1.6.2.1.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 99a274fe-7da8-4b22-bdf6-8b8645f7c617 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.6.2.1.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 3ed71aa1-06fc-4e9d-a8ab-2746506a9562 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.1.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e2da8527-9f1e-46d8-beae-9580c3703fcf -->

The subtrees for archived Invocations and Instances of the Prime Transformation Primitive are stored here.

###### A.6.1.1.6.2.1.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 2783e2db-322c-4866-9b58-ce7e20c43d24 -->

The subtrees for failed Invocations of the Prime Transformation Primitive are stored here.

###### A.6.1.1.6.2.1.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 7df624c0-7e91-43de-bd55-eaf0b6b54ddf -->

The subtrees for Instances of the Prime Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.1.2.2 - Active Instances [Core]  <!-- UUID: 879bb696-688c-4c77-acde-3936b2c48e7f -->

The Instances of the Prime Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.1.2.3 - Completed Instances [Core]  <!-- UUID: 09d97b62-fc72-4695-a780-34899e670f9e -->

The Instances of the Prime Transformation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.6.2.1.2.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 2fcbd692-29c5-4788-8f4e-83b415eca7cd -->

The documents herein contain the Instance Configuration Document for the Single Prime Transformation Primitive Instance.

###### A.6.1.1.6.2.1.2.3.1.1 - Parameters [Core]  <!-- UUID: 39a9fe33-c0ed-4001-8e00-4877e651f820 -->

The documents herein define the parameters of the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.6.2.1.2.3.1.1.1 - Agent Type [Core]  <!-- UUID: cc457437-4f65-45d6-9c1a-b3e96806de60 -->

Pattern is a Prime Agent.

###### A.6.1.1.6.2.1.2.3.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 1b7f692d-75a1-4946-9edc-18287204df0f -->

The documents herein define the custom parameters of the Single Instance of the Prime Transformation Primitive, if any.

###### A.6.1.1.6.2.1.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: b6ac0688-a46a-4a93-9465-7f1481e757f9 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.6.2.1.2.3.1.3 - Data Repository [Core]  <!-- UUID: e88a0572-4a34-43f2-87df-397f568c1a6a -->

The documents herein contain data relevant to the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.6.2.1.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: f1d6c189-e998-4bfc-b7a0-322dffdf818e -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.1.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: f2188696-f28a-41ca-b1d9-7dba408089e7 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.1.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: f68d7dad-91a6-41df-8a4f-f0a51d1edcaa -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.6.2.1.2.4 - In Progress Invocations [Core]  <!-- UUID: 92101482-3d95-4596-8caa-331a7b32362f -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.6.2.1.3 - Executor Transformation Primitive [Core]  <!-- UUID: dbba1a29-c226-4da3-8609-36aea2ecf564 -->

The documents herein contain all data and specifications for Pattern's instance of the Executor Transformation Primitive. See [A.2.2.5.3 - Executor Transformation Primitive](2f249be5-8edb-41e4-b429-734e1ba2cbc7).

##### A.6.1.1.6.2.1.3.1 - Primitive Hub Document [Core]  <!-- UUID: 4053d47c-8495-470c-8363-763f6c9ea5e8 -->

The documents herein organize all base information relevant to Pattern's usage of the Executor Transformation Primitive.

###### A.6.1.1.6.2.1.3.1.1 - Global Activation Status [Core]  <!-- UUID: 9ceac949-3ea5-4c4e-9d14-a14c6af2e28b -->

`Inactive`

###### A.6.1.1.6.2.1.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 0136e45f-2150-4eee-ac7f-024c55df76e9 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.1.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 96d03759-39c1-47f1-b4df-3fb6f17c53d6 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.1.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: fe4c3186-e657-4503-866c-1c5951d36865 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.6.2.1.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 9b578e58-0b39-4c8f-85cf-d620e7b26aaa -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.1.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ec65edb3-27bc-4417-899e-7bf79a15bb89 -->

The subtrees for archived Invocations and Instances of the Executor Transformation Primitive are stored here.

###### A.6.1.1.6.2.1.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: da208691-821a-449f-91c8-12feebfa309e -->

The subtrees for failed Invocations of the Executor Transformation Primitive are stored here.

###### A.6.1.1.6.2.1.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 29a6a43c-10a4-4b9d-ac2d-ba8392d32848 -->

The subtrees for Instances of the Executor Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.1.3.2 - Active Instances [Core]  <!-- UUID: b663556e-0602-4afa-a333-c4bddb7cf763 -->

The Instances of the Executor Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.1.3.3 - Completed Instances [Core]  <!-- UUID: e6c0d4a8-24ef-4e0f-a0f3-439dd4cdf326 -->

The Instances of the Executor Transformation Primitive with `Completed` Status are contained herein.

##### A.6.1.1.6.2.1.3.4 - In Progress Invocations [Core]  <!-- UUID: f4b8bb12-b5ba-4bef-ae6d-0985bb9c0a90 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.6.2.1.4 - Agent Token Primitive [Core]  <!-- UUID: b16a82ab-c18b-474d-91f5-97dba7e73bf9 -->

The documents herein contain all data and specifications for Pattern's Instance of the Agent Token Primitive. See [A.2.2.5.4 - Agent Token Primitive](2047c361-db28-4952-a70c-83d07b562064).

##### A.6.1.1.6.2.1.4.1 - Primitive Hub Document [Core]  <!-- UUID: 9d78656b-5f03-4644-b6bb-c37ed7bdfe58 -->

The documents herein organize all base information relevant to Pattern's usage of the Agent Token Primitive.

###### A.6.1.1.6.2.1.4.1.1 - Global Activation Status [Core]  <!-- UUID: 548f4e01-9e6b-4031-af13-4db16657fe3c -->

`Active`

###### A.6.1.1.6.2.1.4.1.2 - Active Instances Directory [Core]  <!-- UUID: 840388d9-fee4-4ed5-ba4d-f66c86756a59 -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.1.4.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 2e06bfa4-06ab-4d99-98de-1aad9e96ae07 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.6.2.1.4.2.1 - Single Instance Configuration Document](0667a9c2-6fe1-456e-bd0a-3cf367fac480).

###### A.6.1.1.6.2.1.4.1.3 - Completed Instances Directory [Core]  <!-- UUID: e1fada1e-777d-4591-8c33-17fcd67a7e12 -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.1.4.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: e51a3ed3-3ddc-4148-af56-e5b9a43b20cb -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent's token, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.6.2.1.4.1.5 - Hub Data Repository [Core]  <!-- UUID: 9957f9c5-7770-4bb8-a883-2e2adbc57578 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.1.4.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: d2dd644c-787d-411b-8838-cb64863e08c0 -->

The subtrees for archived Invocations and Instances of the Agent Token Primitive are stored here.

###### A.6.1.1.6.2.1.4.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: b832b536-0c59-461d-b347-8f829b51a21d -->

The subtrees for failed Invocations of the Agent Token Primitive are stored here.

###### A.6.1.1.6.2.1.4.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 17139c9f-911a-412d-b8d9-b233212969fe -->

The subtrees for Instances of the Agent Token Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.1.4.2 - Active Instances [Core]  <!-- UUID: 2e096f4a-35ad-4a3a-a21a-2319bd5e45d7 -->

The Instances of the Agent Token Primitive with `Active` Status are stored herein.

###### A.6.1.1.6.2.1.4.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 0667a9c2-6fe1-456e-bd0a-3cf367fac480 -->

The documents herein contain the Instance Configuration Document for the Single Agent Token Primitive Instance.

###### A.6.1.1.6.2.1.4.2.1.1 - Parameters [Core]  <!-- UUID: c562edbd-5dd4-44c7-a6c4-ab8a2169df55 -->

The documents herein define the parameters of the Single Instance of the Agent Token Primitive.

###### A.6.1.1.6.2.1.4.2.1.1.1 - Token Name [Core]  <!-- UUID: 49243902-54b4-49e4-8bed-caa61cca4fa1 -->

The name of Pattern's token is Pattern.

###### A.6.1.1.6.2.1.4.2.1.1.2 - Token Symbol [Core]  <!-- UUID: b840db04-00cb-4f16-9f43-f967963807a4 -->

The symbol of Pattern's token is PATTERN.

###### A.6.1.1.6.2.1.4.2.1.1.3 - Genesis Supply [Core]  <!-- UUID: f699e4e0-6c47-41b2-ab52-9e0169fa7ffe -->

The Genesis Supply of PATTERN is 10 billion.

###### A.6.1.1.6.2.1.4.2.1.1.4 - Token Address [Core]  <!-- UUID: 1108297e-9d69-4468-859e-2d26a42c27af -->

The address of PATTERN will be specified in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.1.4.2.1.1.5 - Token Admin [Core]  <!-- UUID: 82d9f120-27e1-4b0c-a575-d26b537df45e -->

The token Admin will be specified in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.1.4.2.1.1.6 - Token Emissions [Core]  <!-- UUID: ddb9f10e-8452-482a-b102-656dc8b23eea -->

Token emissions beyond the Genesis Supply are permanently disabled; this cannot be reverted by Pattern Governance. Sky Governance retains the ability to revert where Pattern is in violation of Risk Capital requirements and emissions are required by the Risk Framework. See [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.6.1.1.6.2.1.4.2.1.1.7 - Custom Instance Parameters [Core]  <!-- UUID: 488f6950-fecd-4f82-ab43-62c4fab0f9ae -->

The documents herein define the custom parameters of the Single Instance of the Agent Token Primitive, if any.

###### A.6.1.1.6.2.1.4.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 7f6bce4b-af7e-4810-aea8-890ee4b5f6ad -->

The documents herein define the operational processes for minting and initial distribution of the tokens from the Genesis Supply.

- These processes will be defined in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.1.4.2.1.3 - Data Repository [Core]  <!-- UUID: 16fc704d-3db3-4701-b3e3-cddadd99f125 -->

The documents herein contain data relevant to the Single Instance of the Agent Token Primitive.

###### A.6.1.1.6.2.1.4.2.1.3.1 - Initial Planning [Core]  <!-- UUID: c900576f-7e31-40cc-8c2d-994b6b06bb5a -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.1.4.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 34f38616-01ff-4516-8ede-b553d2305fb8 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.1.4.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: bc407d25-c3f5-412e-bf72-4cab3189f9e4 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.6.2.1.4.3 - Completed Instances [Core]  <!-- UUID: abfc5286-88ee-4cb1-9610-ef45082019d6 -->

The Instances of the Agent Token Primitive with `Completed` Status are contained herein.

##### A.6.1.1.6.2.1.4.4 - In Progress Invocations [Core]  <!-- UUID: 2c50493d-aa00-4aaa-95a7-fd43a5625500 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent's token, no further Instances of the Primitive can be Invoked.

### A.6.1.1.6.2.2 - Operational Primitives [Core]  <!-- UUID: 74b5123e-1557-4323-851b-96ada6249e50 -->

The documents herein implement the Operational Primitives for Pattern. See [A.2.2.6 - Operational Primitives](0192ec95-9207-480e-8c51-88d2a1da95ad).

#### A.6.1.1.6.2.2.1 - Executor Accord Primitive [Core]  <!-- UUID: 5675fbe0-03fc-4571-9bf6-0eed37f06b8c -->

The documents herein contain all data and specifications for Pattern's Instances of the Executor Accord Primitive. See [A.2.2.6.1 - Executor Accord Primitive](88017877-3ec1-4c43-a035-6bebdf11d9bb).

##### A.6.1.1.6.2.2.1.1 - Primitive Hub Document [Core]  <!-- UUID: 4604fb19-254c-455e-93c6-e2aba0b7261d -->

The documents herein organize all base information relevant to Pattern's usage of the Executor Accord Primitive.

###### A.6.1.1.6.2.2.1.1.1 - Global Activation Status [Core]  <!-- UUID: 3d671fa2-ff8c-4a09-aac6-579b23e43d9a -->

`Active`

###### A.6.1.1.6.2.2.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 8466094a-9e2a-4dad-bac9-88e0bb8987aa -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.2.1.1.2.1 - Ozone Instance Configuration Document Location [Core]  <!-- UUID: d00595bb-b9c6-4663-8055-18332fa01647 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.6.2.2.1.2.1 - Ozone Instance Configuration Document](960445d5-4b1c-406e-b05a-470e0cca6e71).

###### A.6.1.1.6.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 061c10bc-d108-4610-abc3-fb017304d711 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 2d253ba6-4610-4478-b844-d5288368e94a -->

This document contains a Directory of all prospective Instances of the Executor Accord Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.2.1.1.2 - Active Instances Directory](8466094a-9e2a-4dad-bac9-88e0bb8987aa), whereas failed Invocations are Archived in [A.6.1.1.6.2.2.1.1.5 - Hub Data Repository](f5ddf7f3-add9-4599-ae6e-108d56abcb5b).

###### A.6.1.1.6.2.2.1.1.5 - Hub Data Repository [Core]  <!-- UUID: f5ddf7f3-add9-4599-ae6e-108d56abcb5b -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.2.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 087712fc-59c2-4a4a-90fa-a5644451d476 -->

The subtrees for archived Invocations and Instances of the Executor Accord Primitive are stored here.

###### A.6.1.1.6.2.2.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9bbb61da-85ae-4926-868e-69fe3935284e -->

The subtrees for failed Invocations of the Executor Accord Primitive are stored here.

###### A.6.1.1.6.2.2.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 2f4c6bfd-ef22-481e-996f-8d443c446aad -->

The subtrees for Instances of the Executor Accord Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.2.1.2 - Active Instances [Core]  <!-- UUID: b50f2b43-50b8-43e4-bb4b-393434d8d935 -->

The Instances of the Executor Accord Primitive with `Active` Status are stored herein.

###### A.6.1.1.6.2.2.1.2.1 - Ozone Instance Configuration Document [Core]  <!-- UUID: 960445d5-4b1c-406e-b05a-470e0cca6e71 -->

The documents herein contain the Instance Configuration Document for the Ozone Executor Accord Primitive Instance.

###### A.6.1.1.6.2.2.1.2.1.1 - Parameters [Core]  <!-- UUID: 8cee1084-ac2b-4608-bbfd-adbc021b290b -->

The documents herein define the parameters of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.6.2.2.1.2.1.1.1 - Operational Executor Agent [Core]  <!-- UUID: 9eb31932-9fe5-49fb-9f7c-4d44db589295 -->

The Operational Facilitator and Operational GovOps for Ozone are specified in [A.6.1.2.2 - Operational Executor Agent Ozone](565660dd-7850-4c3a-8dba-554542bf103a).

###### A.6.1.1.6.2.2.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 62d6ce9b-d6b3-4ccf-9739-7fa4aee3c5fa -->

The documents herein define the custom parameters of the Ozone Instance of the Executor Accord Primitive, if any.

###### A.6.1.1.6.2.2.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 5f9cf743-c9f6-4a7b-a543-45cc5b950d13 -->

The documents herein define the process for the ongoing management of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.6.2.2.1.2.1.3 - Data Repository [Core]  <!-- UUID: aa2c1044-4832-4e97-a2c9-36f4b872bd88 -->

The documents herein contain data relevant to the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.6.2.2.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 5ac885aa-64f6-4400-82b9-d11a33470b28 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.2.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: b3a60a21-7f43-403f-9cfa-aa8bd29f0140 -->

The materials associated with Operational GovOps review during the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.2.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: eb0aaebd-16e4-4955-b7c9-c1a778b4cf9e -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.6.2.2.1.3 - Completed Instances [Core]  <!-- UUID: 20a2abf2-ca4d-407e-8c23-2950271ffa19 -->

The Instances of the Executor Accord Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.2.1.4 - In Progress Invocations [Core]  <!-- UUID: 475e7d64-fa87-480a-bb50-adf16acd4af8 -->

The in progress Invocations of the Executor Accord Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.2.1.2 - Active Instances](b50f2b43-50b8-43e4-bb4b-393434d8d935).

#### A.6.1.1.6.2.2.2 - Root Edit Primitive [Core]  <!-- UUID: e30f2e01-78c1-4286-a80a-0df31923303f -->

The documents herein contain all data and specifications for Pattern's Instance of the Root Edit Primitive. See [A.2.2.6.2 - Root Edit Primitive](78488c6b-d77f-4344-b954-476e415a2c7d).

##### A.6.1.1.6.2.2.2.1 - Primitive Hub Document [Core]  <!-- UUID: f987a5d2-2fe4-450e-a57b-32c44ba2eb99 -->

The documents herein organize all base information relevant to Pattern's usage of the Root Edit Primitive.

###### A.6.1.1.6.2.2.2.1.1 - Global Activation Status [Core]  <!-- UUID: 0f9cb02c-8c9b-459a-b326-86a81cfcca9c -->

`Active`

###### A.6.1.1.6.2.2.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 8653a85e-f6dc-44b9-8192-5f998c9f5369 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.2.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: e36d3e60-d222-4ae4-a02f-6994bd6b252c -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.6.2.2.2.2.1 - Single Instance Configuration Document](a53a7f47-1c80-4ab8-bf86-d32dc0e21ccc).

###### A.6.1.1.6.2.2.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 8fa24145-e0d4-4d70-ae7c-b830ad966e8f -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.2.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 47690711-4a0d-4f50-9aa8-47c3cada5afc -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.6.2.2.2.1.5 - Hub Data Repository [Core]  <!-- UUID: fe138146-b5f3-4790-a027-366281bee9d4 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.2.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: f6241c15-1f4e-44a1-9e32-9b0593ff09c9 -->

The subtrees for archived Invocations and Instances of the Root Edit Primitive are stored here.

###### A.6.1.1.6.2.2.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: ec7cb8c6-c1a9-470c-8f3a-4a8bae47f28c -->

The subtrees for failed Invocations of the Root Edit Primitive are stored here.

###### A.6.1.1.6.2.2.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 6443e0c7-2ec7-431f-a4d7-a93453e742ef -->

The subtrees for Instances of the Root Edit Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.2.2.2 - Active Instances [Core]  <!-- UUID: 4bfaf43d-8cde-4359-9581-cff3c9363337 -->

The Instances of the Root Edit Primitive with `Active` Status are stored herein.

###### A.6.1.1.6.2.2.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: a53a7f47-1c80-4ab8-bf86-d32dc0e21ccc -->

The documents herein contain the Instance Configuration Document for the Single Root Edit Primitive Instance.

###### A.6.1.1.6.2.2.2.2.1.1 - Parameters [Core]  <!-- UUID: cdf80bb3-4e22-4e51-b0fd-4325c331b7e2 -->

The parameters of the Root Edit Primitive are fully specified by the Operational Process Definition in [A.6.1.1.6.2.2.2.2.1.2 - Operational Process Definition](0a6525e3-429d-4955-8dac-9fc61f6643f8).

###### A.6.1.1.6.2.2.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 0a6525e3-429d-4955-8dac-9fc61f6643f8 -->

The documents herein define the process for using the Root Edit Primitive to update the Pattern Agent Artifact. Information on Pattern governance that is unrelated to the use of the Root Edit Primitive is located at [A.6.1.1.6.3.1 - Governance Information Unrelated To Root Edit Primitive](df8e7155-ba1f-4606-8a4a-0619c06da12b).

###### A.6.1.1.6.2.2.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 531cdc0a-091f-4c06-9d4e-e2421853a4c6 -->

The documents herein define the process for using the Root Edit Primitive to update the Pattern Agent Artifact in routine or normal conditions (i.e., non-emergency situations).

###### A.6.1.1.6.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission [Core]  <!-- UUID: a6261165-8c88-432f-a3c1-79465599d706 -->

The Root Edit process begins with a PATTERN token holder submitting a proposal through the Powerhouse system containing a draft Artifact Edit Proposal. A PATTERN token holder must hold at least 1% of the circulating token supply to submit a proposal. The proposal must also be posted on the Sky Forum under the "Pattern Prime" category.

###### A.6.1.1.6.2.2.2.2.1.2.1.1.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: 351f7eac-691a-4bcb-868e-5ca56787d53a -->

Until the Powerhouse system supports submitting Artifact Edit Proposals, PATTERN token holders may submit Artifact Edit Proposals by posting them to the Sky Forum under the "Pattern Prime" category. The title of the post must include the text "Pattern Artifact Edit Proposal". The post must include cryptographic proof that the author controls an account holding the required percentage of the total PATTERN token supply specified in [A.6.1.1.6.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](a6261165-8c88-432f-a3c1-79465599d706).

###### A.6.1.1.6.2.2.2.2.1.2.1.2 - Root Edit Expert Advisor Review [Core]  <!-- UUID: 17be5231-4b3e-44ab-92ea-c7e259e633e1 -->

A future iteration of the Pattern Artifact will specify guidelines for obtaining specialized review of proposals requiring advanced technical or financial analysis.

###### A.6.1.1.6.2.2.2.2.1.2.1.3 - Root Edit Proposal Review By Operational Facilitator [Core]  <!-- UUID: af30f942-9746-4576-ab61-df3dd9697fbe -->

Within seven (7) days of the proposal being submitted, the Operational Facilitator must review the Root Edit Proposal for alignment.

If the proposal is aligned, the Operational Facilitator must respond to the Forum post to announce their finding. In this Forum post, the Operational Facilitator must also confirm that the proposal is feasible for Operational GovOps to operationalize.

If the proposal is misaligned, the Operational Facilitator must respond to the Forum post to announce their finding and provide the reasoning for it.

###### A.6.1.1.6.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote [Core]  <!-- UUID: 8704e66e-872f-4bca-b63c-8361aa694496 -->

Where their review of the proposal results in a finding of alignment with the Sky Core Atlas and Pattern Artifact, the Operational Facilitator next triggers a Snapshot poll to allow token holders to vote on the proposal. The poll is open for three (3) days. A poll must have at least 10% of the circulating token supply participating and must have 50% of votes in favor to be approved.

###### A.6.1.1.6.2.2.2.2.1.2.1.5 - Root Edit Artifact Update [Core]  <!-- UUID: d2543813-8897-48a1-968d-1cfd3a2d3068 -->

At the conclusion of the poll, if the proposal is approved, the Operational Facilitator submits the edit to Powerhouse to formally update the Agent Artifact. Regardless of the outcome, the Operational Facilitator updates the Powerhouse System to include the result of the vote, including any pertinent documents.

###### A.6.1.1.6.2.2.2.2.1.2.1.5.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: 058a9110-5c05-4b0d-9602-1d0429ab6fbb -->

Until the Powerhouse system supports updating Agent Artifacts, the Operational Facilitator works with the Core Facilitator to update the Atlas GitHub repository located at [https://github.com/sky-ecosystem/next-gen-atlas/pulls](https://github.com/sky-ecosystem/next-gen-atlas/pulls) to reflect proposals approved by Prime Governance.

###### A.6.1.1.6.2.2.2.2.1.2.1.6 - Artifact Edit Restrictions [Core]  <!-- UUID: 4137d6f6-d330-4953-99e7-b17f2fb8ac55 -->

The Pattern Artifact cannot be edited in any way that violates the Sky Core Atlas or its specifications of the Sky Primitives, or in any way that is otherwise misaligned. The Operational Facilitator must enforce this rule through their review of Artifact Edit Proposals.

###### A.6.1.1.6.2.2.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 3474027e-8a10-4972-b929-90f9c2894c70 -->

The documents herein define the process for using the Root Edit Primitive to update the Pattern Agent Artifact in non-routine conditions.

###### A.6.1.1.6.2.2.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: fbd6606d-dfe5-4816-bb90-f555c13323b1 -->

The documents herein define the process for using the Root Edit Primitive to update the Pattern Agent Artifact in emergency situations.

###### A.6.1.1.6.2.2.2.2.1.2.3.1 - Root Edit Voting Process In Emergency Situations [Core]  <!-- UUID: 7d31d593-75bb-41ef-86f4-a10ecf83e19f -->

In an Emergency Situation, as defined by the Sky Core Atlas in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225), the Operational Facilitator may allow a Root Edit to occur more quickly than the timeline specified above. Where feasible, the Operational Facilitator should announce the decision to deploy the emergency Root Edit protocol and provide their reasoning via a public Sky Forum post (under the "Pattern Prime" category), unless doing so would endanger Pattern or its users.

###### A.6.1.1.6.2.2.2.2.1.3 - Data Repository [Core]  <!-- UUID: ffdbcc14-282a-47ae-81c6-7773b2cc09bf -->

The documents herein contain data relevant to the Single Instance of the Root Edit Primitive.

###### A.6.1.1.6.2.2.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: f4b2bc56-63d1-4b5b-8c84-8eccc1fa3218 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.2.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 10680aaa-0b55-4c66-b40d-9741bcd4dc6e -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.2.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 17aa4887-fc5d-4b66-8f3e-60a3490250a5 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.6.2.2.2.3 - Completed Instances [Core]  <!-- UUID: 261adee1-2841-4c6b-937e-c5c86cf6cbac -->

The Instances of the Root Edit Primitive with `Completed` Status are contained herein.

##### A.6.1.1.6.2.2.2.4 - In Progress Invocations [Core]  <!-- UUID: 2f12e03a-7561-4b7c-ae2f-baec03f1b18f -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.6.2.2.3 - Light Agent Primitive [Core]  <!-- UUID: ecf594f7-ccc6-45f0-8ed0-e7a0f0b5182d -->

The documents herein contain all data and specifications for Pattern's Instances of the Light Agent Primitive. See [A.2.2.6.3 - Light Agent Primitive](44028423-2cd1-40cb-89ac-3f762b602b90).

##### A.6.1.1.6.2.2.3.1 - Primitive Hub Document [Core]  <!-- UUID: 2abd678a-fea3-4968-87c5-a81302f3c387 -->

The documents herein organize all base information relevant to Pattern's usage of the Light Agent Primitive.

###### A.6.1.1.6.2.2.3.1.1 - Global Activation Status [Core]  <!-- UUID: c1a3ea5f-5cd9-46f3-9d0a-a7ad7648c3c4 -->

`Inactive`

###### A.6.1.1.6.2.2.3.1.2 - Active Instances Directory [Core]  <!-- UUID: d59c68f3-1755-457d-b16e-3ca9eda708bf -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.2.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 2c5faabf-cbe8-47f4-b710-d431ae46ac2d -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.2.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: d90aac90-120d-4ed3-83bc-cf2d2fd91250 -->

This document contains a Directory of all prospective Instances of the Light Agent Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.2.3.1.2 - Active Instances Directory](d59c68f3-1755-457d-b16e-3ca9eda708bf), whereas failed Invocations are Archived in [A.6.1.1.6.2.2.3.1.5 - Hub Data Repository](cdf9a214-d0a4-482d-8218-8bfe3f783524).

###### A.6.1.1.6.2.2.3.1.5 - Hub Data Repository [Core]  <!-- UUID: cdf9a214-d0a4-482d-8218-8bfe3f783524 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.2.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 6b266aa2-92ea-4072-af2a-b7bbf05366ed -->

The subtrees for archived Invocations and Instances of the Light Agent Primitive are stored here.

###### A.6.1.1.6.2.2.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 61056f64-f4ec-45bd-996c-677745cb4d18 -->

The subtrees for failed Invocations of the Light Agent Primitive are stored here.

###### A.6.1.1.6.2.2.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 06b30e73-6a92-4e83-acd0-f09a3dca5b37 -->

The subtrees for Instances of the Light Agent Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.2.3.2 - Active Instances [Core]  <!-- UUID: 1f384209-da9a-4792-a244-2effa8187f50 -->

The Instances of the Light Agent Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.2.3.3 - Completed Instances [Core]  <!-- UUID: 978cd88e-53a9-403b-9186-9462d572cee4 -->

The Instances of the Light Agent Primitive with `Completed` Status are contained herein.

##### A.6.1.1.6.2.2.3.4 - In Progress Invocations [Core]  <!-- UUID: b1642b58-8b1f-4a05-9ff2-6dccbcc217ee -->

The in progress Invocations of the Light Agent Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.2.3.2 - Active Instances](1f384209-da9a-4792-a244-2effa8187f50).

### A.6.1.1.6.2.3 - Ecosystem Upkeep Primitives [Core]  <!-- UUID: 49eaa780-25f5-4732-8a47-fc18e06f320c -->

The documents herein implement the Ecosystem Upkeep Primitives for Pattern. See [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

#### A.6.1.1.6.2.3.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: 0d6ea791-8496-4fe5-8430-b636482ed967 -->

The documents herein contain all data and specifications for Pattern's Instance of the Ecosystem Upkeep Fee Primitive. See [A.2.2.7.1 - Ecosystem Upkeep Fee Primitive](a21616f4-1611-4e0b-87b2-efbdff9f6f28).

##### A.6.1.1.6.2.3.1.1 - Primitive Hub Document [Core]  <!-- UUID: 494d6e55-e1c1-4d0f-a51d-8f87d2a95ad5 -->

The documents herein organize all base information relevant to Pattern's usage of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.6.2.3.1.1.1 - Global Activation Status [Core]  <!-- UUID: 280c32bc-e40e-4187-be61-0f2fd26ab167 -->

`Active`

###### A.6.1.1.6.2.3.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 09267410-31c0-42be-a8d2-dfb0768b72b0 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.3.1.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: b23ab610-19e1-44a7-b23a-2b44c2d18720 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.6.2.3.1.2.1 - Single Instance Configuration Document](d8b7f338-3318-462c-a65d-4e49a29398b2).

###### A.6.1.1.6.2.3.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: e7a3cf2c-258e-4709-8a0c-db71bccc487f -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.3.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: c58a4af2-fdf4-4b79-8720-5836734d028a -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.6.2.3.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 033c7842-34e2-4043-b7fa-238c52e21709 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.3.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: f33304eb-bd49-4f6b-ad0f-6bd869f51c81 -->

The subtrees for archived Invocations and Instances of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.6.2.3.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 15afa4dd-86cb-4080-8c57-7c0e9083871d -->

The subtrees for failed Invocations of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.6.2.3.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 21ab98ce-6e98-43e1-907b-f9851d19114e -->

The subtrees for Instances of the Ecosystem Upkeep Fee Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.3.1.2 - Active Instances [Core]  <!-- UUID: dc3af461-324a-44d3-8971-6ed3ed93d34b -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Active` Status are stored herein.

###### A.6.1.1.6.2.3.1.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: d8b7f338-3318-462c-a65d-4e49a29398b2 -->

The documents herein contain the Instance Configuration Document for the Single Ecosystem Upkeep Fee Primitive Instance.

###### A.6.1.1.6.2.3.1.2.1.1 - Parameters [Core]  <!-- UUID: 27bfc7f9-d9da-42bc-8fde-7c3aacb0b2c7 -->

The documents herein define the parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.6.2.3.1.2.1.1.1 - Terms [Core]  <!-- UUID: 14a3b7fc-37f3-4407-a59b-061df4b7fc73 -->

Pattern will pay 0.50% of its market capitalization per year in USDS.

###### A.6.1.1.6.2.3.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 5147797a-7219-4f30-ab4e-38b6306bcc3b -->

The documents herein define the custom parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive, if any.

###### A.6.1.1.6.2.3.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: a1718608-c793-4521-a2ae-df2a685f2070 -->

The documents herein define the process for the ongoing management of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.6.2.3.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 46b382ec-7179-44ce-b07c-f53a33b8bf23 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.6.2.3.1.2.1.2.1.1 - Process Definition For Upkeep Fee Payment [Core]  <!-- UUID: 8d0b0487-8d3d-4663-8096-04b32c52b073 -->

The process to pay 0.50% of Pattern's market capitalization per year in USDS will be specified in future iterations of the Pattern Artifact.

###### A.6.1.1.6.2.3.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 8508d44e-41ca-41ed-a491-3d5135ce490a -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.6.2.3.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 3564cdbb-e173-413c-b21d-1fa25259470e -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.6.2.3.1.2.1.3 - Data Repository [Core]  <!-- UUID: 899424bc-a0b7-4766-aa19-2b17e6b37991 -->

The documents herein contain data relevant to the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.6.2.3.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 87094d8d-a42a-4665-8215-615124a8e123 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.3.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 0b1d35c9-7ae9-4b23-a5c8-360c5af2d58c -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.3.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: cf3abeef-7836-457a-a659-e432d1eb7c20 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.6.2.3.1.3 - Completed Instances [Core]  <!-- UUID: 88e57951-b13f-4c14-8af1-c0b6f757df42 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.3.1.4 - In Progress Invocations [Core]  <!-- UUID: 7493f2d6-1910-43fd-b7db-40f435529fe3 -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.6.2.3.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: 33b2f3db-d757-472e-be6e-c03b376f4ec3 -->

The documents herein contain all data and specifications for Pattern's instances of the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

##### A.6.1.1.6.2.3.2.1 - Primitive Hub Document [Core]  <!-- UUID: c1ba86c9-f638-4ebe-9346-e22377841c2c -->

The documents herein organize all base information relevant to Pattern's usage of the Upkeep Rebate Primitive.

###### A.6.1.1.6.2.3.2.1.1 - Global Activation Status [Core]  <!-- UUID: 91965eb0-adbe-44fb-90eb-b4b898579c02 -->

`Active`

###### A.6.1.1.6.2.3.2.1.2 - Active Instances Directory [Core]  <!-- UUID: c3368a88-6bd8-4111-8e9a-e22d9afe1bfe -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.3.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 04802fe1-3d1b-4499-8006-22048d3e8b6c -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.6.2.3.2.2.1 - Single Instance Configuration Document](77bd8e6f-aad2-4830-8822-1abc3281bfa8).

###### A.6.1.1.6.2.3.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 85c523fe-a6be-4695-ac8c-1d584f285324 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.3.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 9da85689-3fae-4814-8e7e-3c817f1c09f8 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.6.2.3.2.1.5 - Hub Data Repository [Core]  <!-- UUID: d3c8ecd1-8a0f-4ffe-a181-3906b7daae8d -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.3.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: f58354db-e99a-426a-a5b6-0517e65d0cf3 -->

The subtrees for archived Invocations and Instances of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.6.2.3.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: b00aa59c-d001-4043-ac29-6f4ea207183e -->

The subtrees for failed Invocations of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.6.2.3.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 17d4ef14-d08a-4c23-b4b6-629adf08ef80 -->

The subtrees for Instances of the Upkeep Rebate Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.3.2.2 - Active Instances [Core]  <!-- UUID: 805a832a-10ef-49d8-b1de-9e5d28f29f95 -->

The Instances of the Upkeep Rebate Primitive with `Active` Status are stored herein.

###### A.6.1.1.6.2.3.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 77bd8e6f-aad2-4830-8822-1abc3281bfa8 -->

The documents herein contain the Instance Configuration Document for the Single Upkeep Rebate Primitive Instance.

###### A.6.1.1.6.2.3.2.2.1.1 - Parameters [Core]  <!-- UUID: 8ecbe4ce-28f0-48d0-844f-7d236c242264 -->

Every Prime Agent is entitled to the Upkeep Rebate Primitive for tokens of other Prime Agents that they hold. Because this right automatically applies, there are no parameters.

###### A.6.1.1.6.2.3.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 79728f8b-64c3-49d1-9477-990073c87c94 -->

The documents herein define the process for the ongoing management of the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.6.2.3.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 377b7042-5cee-4baf-a77f-39acd0f99854 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.6.2.3.2.2.1.2.1.1 - Pattern Holds Tokens Of Other Agents In Its SubProxy Account [Core]  <!-- UUID: 106faf37-f072-4cac-aa1d-50982c04acea -->

Pattern keeps all tokens of other Agents it holds in its SubProxy account.

###### A.6.1.1.6.2.3.2.2.1.2.1.2 - Pattern Deducts Rebate From Ecosystem Upkeep Fees [Core]  <!-- UUID: 5abf2834-3f70-4ca9-9bf8-14df17e1f1bd -->

When paying Ecosystem Upkeep fees, Pattern deducts the rebate from the fees it pays.

###### A.6.1.1.6.2.3.2.2.1.2.1.3 - Operational GovOps Reviews Rebate [Core]  <!-- UUID: 3e913724-ce5a-41a5-b9db-27ba25c35c06 -->

Operational GovOps reviews Pattern's calculation of the rebate before executing a return of surplus to token holders. In the event of any issues, Operational GovOps cannot execute the distribution. If Operational GovOps does not execute the distribution, Operational GovOps must post an explanation on the Sky Forum under the "Pattern Prime" category and work with Pattern to resolve the disagreement. If Operational GovOps and Pattern cannot resolve the disagreement, it must be escalated to Core GovOps.

###### A.6.1.1.6.2.3.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: e5897490-739e-4778-9eb3-15a57309bf7b -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.6.2.3.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: a506aba7-1c37-46eb-954c-bb99b83d59c6 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.6.2.3.2.2.1.3 - Data Repository [Core]  <!-- UUID: c1002f65-de06-45e0-ab0b-99d44279ffb3 -->

The documents herein contain data relevant to the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.6.2.3.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 136d9a42-5b8f-4e7c-835a-bbcdff8e3d9a -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.3.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: e432bb7e-0054-4306-a573-494655454d35 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.6.2.3.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 1e486b02-fcb5-4c95-b832-153f592b5f13 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.6.2.3.2.3 - Completed Instances [Core]  <!-- UUID: 3aa8f9e7-67ca-4411-9938-d3e7472f3cfe -->

The Instances of the Upkeep Rebate Primitive with `Completed` Status are contained herein.

##### A.6.1.1.6.2.3.2.4 - In Progress Invocations [Core]  <!-- UUID: 31495a53-3a81-466f-bb02-ac7ba4180851 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

### A.6.1.1.6.2.4 - SkyLink Primitives [Core]  <!-- UUID: fcc2d538-6b23-45bc-b153-53d2e25ab056 -->

The documents herein implement the SkyLink Primitives for Pattern. See [A.2.2.8 - SkyLink Primitives](7b5d8965-a64c-4c44-b742-607f51f69d8f).

#### A.6.1.1.6.2.4.1 - Token SkyLink Primitive [Core]  <!-- UUID: f2056d2f-e669-41a8-b402-184c8f12092c -->

The documents herein contain all data and specifications for Pattern's Instances of the Token SkyLink Primitive. See [A.2.2.8.1 - Token SkyLink Primitive](4504d2d4-ee45-4a07-8c5b-9baf20b12e76).

##### A.6.1.1.6.2.4.1.1 - Primitive Hub Document [Core]  <!-- UUID: 028c364c-6ac4-42b1-86a7-afb6b255d3f7 -->

The documents herein organize all base information relevant to Pattern's usage of the Token SkyLink Primitive.

###### A.6.1.1.6.2.4.1.1.1 - Global Activation Status [Core]  <!-- UUID: 6239f922-626f-4d62-aa0d-4404f3728578 -->

`Inactive`

###### A.6.1.1.6.2.4.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 584acc45-1d1c-4133-8c6a-e37ffeba25a7 -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.4.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 36da00c5-3634-43f9-882f-f8ccfb5220ae -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.4.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 7c196ec5-654e-4f5c-91ea-6e8fc3701edd -->

This document contains a Directory of all prospective Instances of the Token SkyLink Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.4.1.1.2 - Active Instances Directory](584acc45-1d1c-4133-8c6a-e37ffeba25a7), whereas failed Invocations are Archived in [A.6.1.1.6.2.4.1.1.5 - Hub Data Repository](598e9e9c-1e55-41df-916e-d7df282a60a1).

###### A.6.1.1.6.2.4.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 598e9e9c-1e55-41df-916e-d7df282a60a1 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.4.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 43ac33bd-cc48-4c9b-bad2-1b5502e8b66e -->

The subtrees for archived Invocations and Instances of the Token SkyLink Primitive are stored here.

###### A.6.1.1.6.2.4.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 55532dd8-2c51-449d-83e5-ff3fbed3db1b -->

The subtrees for failed Invocations of the Token SkyLink Primitive are stored here.

###### A.6.1.1.6.2.4.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 6b8ee6b3-5a83-4c1e-822d-bad42feed529 -->

The subtrees for Instances of the Token SkyLink Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.4.1.2 - Active Instances [Core]  <!-- UUID: 0767e0df-03e9-49ba-b47f-12502213732e -->

The Instances of the Token SkyLink Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.4.1.3 - Completed Instances [Core]  <!-- UUID: 19165634-385c-4bba-a279-685f6bd91492 -->

The Instances of the Token SkyLink Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.4.1.4 - In Progress Invocations [Core]  <!-- UUID: 688eb991-5d06-4f3a-b847-e258d96857ab -->

The in progress Invocations of the Token SkyLink Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.4.1.2 - Active Instances](0767e0df-03e9-49ba-b47f-12502213732e).

### A.6.1.1.6.2.5 - Demand Side Stablecoin Primitives [Core]  <!-- UUID: 0545c0f9-eab5-4b9e-93f9-cb59a8267312 -->

The documents herein implement the Demand Side Stablecoin Primitives for Pattern. See [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d).

#### A.6.1.1.6.2.5.1 - Distribution Reward Primitive [Core]  <!-- UUID: 6cfff1d4-93e9-41cb-9e40-6051a43975c1 -->

The documents herein contain all data and specifications for Pattern's instances of the Distribution Reward Primitive. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

##### A.6.1.1.6.2.5.1.1 - Primitive Hub Document [Core]  <!-- UUID: 076aeee9-3225-4b3e-8d2c-da278c0cb334 -->

The documents herein organize all base information relevant to Pattern's usage of the Distribution Reward Primitive.

###### A.6.1.1.6.2.5.1.1.1 - Global Activation Status [Core]  <!-- UUID: 0fb59894-f344-4fbf-8918-7a8cb271c3b8 -->

`Active`

###### A.6.1.1.6.2.5.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 082222ab-1802-4eb6-91ee-22986f27a43c -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.5.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: d2443507-e41f-401a-9953-feb3b683c66d -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.5.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 7c88dfbb-08eb-40ac-92e9-8b934a630d2d -->

This document contains a Directory of all prospective Instances of the Distribution Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.5.1.1.2 - Active Instances Directory](082222ab-1802-4eb6-91ee-22986f27a43c), whereas failed Invocations are Archived in [A.6.1.1.6.2.5.1.1.5 - Hub Data Repository](f10a7cf3-932b-4123-9a7d-c8813c50063f).

###### A.6.1.1.6.2.5.1.1.5 - Hub Data Repository [Core]  <!-- UUID: f10a7cf3-932b-4123-9a7d-c8813c50063f -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.5.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ee7ee835-4894-489b-a0cc-08b649e1ecf5 -->

The subtrees for archived Invocations and Instances of the Distribution Reward Primitive are stored here.

###### A.6.1.1.6.2.5.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: e8a949ae-d26b-4a59-a0e0-8657d99c0f59 -->

The subtrees for failed Invocations of the Distribution Reward Primitive are stored here.

###### A.6.1.1.6.2.5.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 6785c95f-4712-4760-8d56-29717402f654 -->

The subtrees for Instances of the Distribution Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.5.1.2 - Active Instances [Core]  <!-- UUID: c1b876c3-5328-4313-b957-e5b0c3eb7d42 -->

The Instances of the Distribution Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.5.1.3 - Completed Instances [Core]  <!-- UUID: 2759639a-3ed8-4f82-9cea-c9beeb927318 -->

The Instances of the Distribution Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.5.1.4 - In Progress Invocations [Core]  <!-- UUID: e3a7fb2e-9621-4066-a73d-96340caec41e -->

The in progress Invocations of the Distribution Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.5.1.2 - Active Instances](c1b876c3-5328-4313-b957-e5b0c3eb7d42).

#### A.6.1.1.6.2.5.2 - Integration Boost Primitive [Core]  <!-- UUID: 1fb482e6-cb6d-4311-9f2a-be481b65c9c2 -->

The documents herein contain all data and specifications for Pattern's Instances of the Integration Boost Primitive. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

##### A.6.1.1.6.2.5.2.1 - Primitive Hub Document [Core]  <!-- UUID: 64832811-c6d5-4269-8bae-f95a7f334cc4 -->

The documents herein organize all base information relevant to Pattern's usage of the Integration Boost Primitive.

###### A.6.1.1.6.2.5.2.1.1 - Global Activation Status [Core]  <!-- UUID: a8713d41-40eb-48f8-82ee-020948616d59 -->

`Active`

###### A.6.1.1.6.2.5.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 7c44f1ca-0d6a-481a-82e0-a9aab01badd9 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.5.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: e8117148-0c90-4960-baea-bd26800db9ef -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.5.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 571dbaf2-afaf-4e94-ae56-c9fd9f2a7462 -->

This document contains a Directory of all prospective Instances of the Integration Boost Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.5.2.1.2 - Active Instances Directory](7c44f1ca-0d6a-481a-82e0-a9aab01badd9), whereas failed Invocations are Archived in [A.6.1.1.6.2.5.2.1.5 - Hub Data Repository](b70f4e2b-678b-4b71-a3eb-3e8e62e09fe8).

###### A.6.1.1.6.2.5.2.1.5 - Hub Data Repository [Core]  <!-- UUID: b70f4e2b-678b-4b71-a3eb-3e8e62e09fe8 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.5.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: b0c2c079-6855-44ca-8e7e-dbfca4da7106 -->

The subtrees for archived Invocations and Instances of the Integration Boost Primitive are stored here.

###### A.6.1.1.6.2.5.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 7d6e06d9-f858-4c77-ab31-16878e06f2b6 -->

The subtrees for failed Invocations of the Integration Boost Primitive are stored here.

###### A.6.1.1.6.2.5.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: ce1a95be-d2cf-416e-89e0-e61c7a959e04 -->

The subtrees for Instances of the Integration Boost Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.5.2.2 - Active Instances [Core]  <!-- UUID: 15973e56-ba8b-41b9-b7b5-a08879226b1c -->

The Instances of the Integration Boost Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.5.2.3 - Completed Instances [Core]  <!-- UUID: 27f4e5af-96a6-490f-8f1c-5f745548a4af -->

The Instances of the Integration Boost Primitive with `Completed` Status are contained herein.

##### A.6.1.1.6.2.5.2.4 - In Progress Invocations [Core]  <!-- UUID: f4323304-2a2b-41e2-9be1-adb41d3f1f8e -->

The in progress Invocations of the Integration Boost Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.5.2.2 - Active Instances](15973e56-ba8b-41b9-b7b5-a08879226b1c).

#### A.6.1.1.6.2.5.3 - Pioneer Chain Primitive [Core]  <!-- UUID: a6c0ce30-cd60-49ca-875f-b96ffb72273a -->

The documents herein contain all data and specifications for Pattern's Instances of the Pioneer Chain Primitive. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).

##### A.6.1.1.6.2.5.3.1 - Primitive Hub Document [Core]  <!-- UUID: d3d4d0b2-e491-4fd5-9c2f-8f2545f0130b -->

The documents herein organize all base information relevant to Pattern's usage of the Pioneer Chain Primitive.

###### A.6.1.1.6.2.5.3.1.1 - Global Activation Status [Core]  <!-- UUID: 1271c05e-f761-49ae-b26f-650f643e6480 -->

`Inactive`

###### A.6.1.1.6.2.5.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 899d30b8-2bc5-4ec9-b888-285fca7e37c1 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.5.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 0f1efcda-3b38-4255-9c69-16e96d62db42 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.5.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 3102c70c-dca5-4211-a978-18319e17524b -->

This document contains a Directory of all prospective Instances of the Pioneer Chain Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.5.3.1.2 - Active Instances Directory](899d30b8-2bc5-4ec9-b888-285fca7e37c1), whereas failed Invocations are Archived in [A.6.1.1.6.2.5.3.1.5 - Hub Data Repository](53fc4aba-c522-4876-83e6-492c2ee95ca2).

###### A.6.1.1.6.2.5.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 53fc4aba-c522-4876-83e6-492c2ee95ca2 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.5.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 601ec019-c79f-4142-9ef1-9116c59153a8 -->

The subtrees for archived Invocations and Instances of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.6.2.5.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: cfd5b108-3fe8-4228-b983-b098a6a3cd08 -->

The subtrees for failed Invocations of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.6.2.5.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 076af992-fa03-4e82-80b7-80095ddc96bd -->

The subtrees for Instances of the Pioneer Chain Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.5.3.2 - Active Instances [Core]  <!-- UUID: 55104448-6e24-4557-bfb9-5cb4b217b636 -->

The Instances of the Pioneer Chain Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.5.3.3 - Completed Instances [Core]  <!-- UUID: f9ef6582-b22c-4065-bd1f-0f959e2aba53 -->

The Instances of the Pioneer Chain Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.5.3.4 - In Progress Invocations [Core]  <!-- UUID: 0f4adb4b-97d5-40b3-ab09-697eeb1e128c -->

The in progress Invocations of the Pioneer Chain Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.5.3.2 - Active Instances](55104448-6e24-4557-bfb9-5cb4b217b636).

### A.6.1.1.6.2.6 - Supply Side Stablecoin Primitives [Core]  <!-- UUID: 5994da99-c086-4877-8777-3be6e5e63562 -->

The documents herein implement the Supply Side Stablecoin Primitives for Pattern. See [A.2.2.10 - Supply Side Stablecoin Primitives](d1142876-33c2-4e21-9339-d8711525d46f).

#### A.6.1.1.6.2.6.1 - Allocation System Primitive [Core]  <!-- UUID: 62ce0e4a-e6fb-4617-8bb6-46e89a83d5bc -->

The documents herein contain all data and specifications for Pattern's Instances of the Allocation System Primitive. See [A.2.2.10.1 - Allocation System Primitive](9db14ab7-bb4b-4751-8084-843bd4359f2a).

##### A.6.1.1.6.2.6.1.1 - Primitive Hub Document [Core]  <!-- UUID: ac8bef79-4452-44b6-8947-2dff84da918e -->

The documents herein organize all base information relevant to Pattern's usage of the Allocation System Primitive.

###### A.6.1.1.6.2.6.1.1.1 - Global Activation Status [Core]  <!-- UUID: 7e0762bd-f890-481f-b26c-f737985054e6 -->

`Active`

###### A.6.1.1.6.2.6.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 9fa776cb-2485-4c4d-92f2-02789b1c914b -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.6.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: d2ae0f64-bb95-4c50-961e-52c82dd52586 -->

The documents herein contain a Directory of all Instances on Ethereum Mainnet of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.6.1.1.2.1.1 - Maple [Core]  <!-- UUID: 5572abc6-902d-4c4d-8eee-0823a3616c36 -->

The Ethereum Mainnet Instances Directory of the Maple Protocol with `Active` Status are stored herein.

###### A.6.1.1.6.2.6.1.1.2.1.1.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document Location [Core]  <!-- UUID: 5755702e-4107-4d81-a986-39b970dce859 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.6.2.6.1.3.1.1.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document](50d86fb7-cacd-4f9b-adf4-7056cfe8cd97).

###### A.6.1.1.6.2.6.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: d447c96a-dec9-4ce7-87fa-44291e6a4c32 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.6.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: c9a77c32-b63a-4d9a-8dd3-f09b05e20eda -->

This document contains a Directory of all prospective Instances of the Allocation System Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.6.1.1.2 - Active Instances Directory](9fa776cb-2485-4c4d-92f2-02789b1c914b), whereas failed Invocations are Archived in [A.6.1.1.6.2.6.1.1.5 - Hub Data Repository](8a6d2cf2-ca58-48a3-b5fc-0cf932257e9e).

###### A.6.1.1.6.2.6.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 8a6d2cf2-ca58-48a3-b5fc-0cf932257e9e -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.6.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 36721bb0-2049-4660-b8fe-20408586d8a9 -->

The subtrees for archived Invocations and Instances of the Allocation System Primitive are stored here.

###### A.6.1.1.6.2.6.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 30befb6f-af6f-451d-88e2-5df33fb8e7f4 -->

The subtrees for failed Invocations of the Allocation System Primitive are stored here.

###### A.6.1.1.6.2.6.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: d137860e-b7f0-4601-a6ce-c98dbfc1d90c -->

The subtrees for Instances of the Allocation System Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.6.1.2 - Multi-Instance Coordinator Document [Core]  <!-- UUID: d02fc174-54ea-4336-8f61-99f530ea533b -->

The documents herein provide general specifications of the Pattern Liquidity Layer and define Pattern's overarching strategy and operational framework for managing across all Instances.

###### A.6.1.1.6.2.6.1.2.1 - General Specifications [Core]  <!-- UUID: 45faacc7-d61e-4446-9900-d1aa2bb2280e -->

The documents herein contain general specifications for the Pattern Liquidity Layer.

###### A.6.1.1.6.2.6.1.2.1.1 - Pattern Liquidity Layer Architecture [Core]  <!-- UUID: 73d09dec-c8d4-425c-9d54-2ef73a82d6b9 -->

The documents herein describe the high-level design of the Pattern Liquidity Layer, including its key smart contracts and their functionality.

###### A.6.1.1.6.2.6.1.2.1.1.1 - Pattern Liquidity Layer Addresses [Core]  <!-- UUID: 440cb15b-0421-444a-aa3b-fc14a3f11026 -->

The subdocuments herein provide the addresses of the Pattern Liquidity Layer’s constituent contracts.

###### A.6.1.1.6.2.6.1.2.1.1.1.1 - Allocator Contract Addresses [Core]  <!-- UUID: b64940f7-ae82-49c7-84ae-0019aff1d7f7 -->

The documents herein contain global key addresses for the Allocator Contracts.

###### A.6.1.1.6.2.6.1.2.1.1.1.1.1 - Ethereum Mainnet [Core]  <!-- UUID: 54c9cfe2-b5d7-425b-a9ee-bf6901066437 -->

The documents herein contain the Allocator Contract Addresses on the Ethereum Mainnet.

###### A.6.1.1.6.2.6.1.2.1.1.1.1.1.1 - Allocator Buffer Contract [Core]  <!-- UUID: deb0a2c0-4a6c-403b-b9b4-79803de4fea8 -->

The address of the ALLOCATOR_BUFFER contract is: `0x823459b55D79F0421f24a4828237F7ecb8D7F1ef`.

###### A.6.1.1.6.2.6.1.2.1.1.1.1.1.2 - Allocator Oracle Contract [Core]  <!-- UUID: a808de67-ebcb-4b57-83be-eaf1c536bc9b -->

The address of the ALLOCATOR_ORACLE contract is: `0xc7B91C401C02B73CBdF424dFaaa60950d5040dB7`

###### A.6.1.1.6.2.6.1.2.1.1.1.1.1.3 - Allocator Registry Contract [Core]  <!-- UUID: 91f97de8-17f8-44e8-a0ec-e140d2ecab30 -->

The address of the ALLOCATOR_REGISTRY contract is: `0xCdCFA95343DA7821fdD01dc4d0AeDA958051bB3B`

###### A.6.1.1.6.2.6.1.2.1.1.1.1.1.4 - Allocator Roles Contract [Core]  <!-- UUID: e2c792e9-abf1-475f-a657-987bc2736a5e -->

The address of the ALLOCATOR_ROLES contract is: `0x9A865A710399cea85dbD9144b7a09C889e94E803`

###### A.6.1.1.6.2.6.1.2.1.1.1.1.1.5 - Allocator Vault Contract [Core]  <!-- UUID: 5ee30a61-2280-4744-8f8f-eb5c5fd56682 -->

The address of the ALLOCATOR_VAULT (ALLOCATOR-PATTERN-A) contract is: `0xbd34fc6AAa1d3F52B314CB9D78023dd23eAc3B0E`.

###### A.6.1.1.6.2.6.1.2.1.1.1.2 - ALM Contracts [Core]  <!-- UUID: e21f8717-c764-42c0-a544-d9991345515a -->

The documents herein contain addresses for the ALM Contracts for the Pattern Liquidity Layer.

###### A.6.1.1.6.2.6.1.2.1.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: 9cad03ef-0226-44b6-b424-c18669e71b00 -->

The documents herein contain the ALM Contract Addresses for the Pattern Liquidity Layer on the Ethereum Mainnet.

###### A.6.1.1.6.2.6.1.2.1.1.1.2.1.1 - ALM Controller Contract [Core]  <!-- UUID: 6d579a04-dc47-47a7-b504-8047782bb4e3 -->

The address of the ALM_CONTROLLER (MainnetController) contract is: `0x8739a869E41e828c83EA45575fBDf9FfcC0962b1`

###### A.6.1.1.6.2.6.1.2.1.1.1.2.1.2 - ALM Controller Contract Version [Core]  <!-- UUID: 2a2092ee-243a-43c8-8e1a-11264b0373db -->

The ALM_CONTROLLER contract version is: V.1.6.0

###### A.6.1.1.6.2.6.1.2.1.1.1.2.1.3 - ALM Freezer Multisig Address [Core]  <!-- UUID: 4a56a0a4-2046-4eb8-ab4f-1afb2ee91a66 -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.6.2.6.1.2.1.2.2.2 - Freezer Multisig](841e629e-c887-48ec-8219-e0b1c86145d6).

###### A.6.1.1.6.2.6.1.2.1.1.1.2.1.4 - ALM Relayer Multisig Address [Core]  <!-- UUID: d55d14f5-d749-4e5c-8931-1c931a4f8ef7 -->

The address of the Multisig that has the Relayer Role is specified in [A.6.1.1.6.2.6.1.2.1.2.2.1 - Relayer Multisig](42f3ceba-f9bc-48bb-aa89-dde3feb21479).

###### A.6.1.1.6.2.6.1.2.1.1.1.2.1.5 - ALM Proxy Contract [Core]  <!-- UUID: 65c5dd3b-9ef8-4ace-9dd8-491431b86242 -->

The address of the ALM_PROXY contract is: `0xbA43325E91C79E500486a23E953ab3d8C46f169F`

###### A.6.1.1.6.2.6.1.2.1.1.1.2.1.6 - ALM Rate Limits Contract [Core]  <!-- UUID: 5afd1a4a-8803-479c-82e1-21a9b94c047f -->

The address of the ALM_RATE_LIMITS contract is: `0xa77f69f90646A4c0e44cEe1D44Fab08bEb4EA204`

###### A.6.1.1.6.2.6.1.2.1.1.2 - Off-chain Operational Parameters [Core]  <!-- UUID: d92dedda-2021-4279-888e-f49fda05a32e -->

The documents herein list the off-chain operational parameters for the Pattern Liquidity Layer. These operational parameters are protocol settings managed outside of smart contracts (off-chain), used by operators and off-chain systems to guide the functioning of the Pattern Liquidity Layer.

###### A.6.1.1.6.2.6.1.2.1.1.2.1 - Off-chain Operational Parameters For Ethereum Mainnet [Core]  <!-- UUID: 83b318cc-a2de-4f00-a340-04699481af4e -->

The document herein lists the current off-chain operational parameters for the Pattern Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.6.2.6.1.2.1.1.2.1.1 - Minimum Operation Size Ethereum Mainnet [Core]  <!-- UUID: 0d3a94a6-7e10-426a-8542-585120e4a77d -->

The minimum transaction size for operations on Ethereum Mainnet is (`MAINNET_MIN_OPERATION_SIZE`):

- This parameter will be specified in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.6.1.2.1.1.2.1.2 - Debt Ceiling Buffer Ethereum Mainnet [Core]  <!-- UUID: e8c9203a-0241-4be1-9efa-b72e9ae7aa89 -->

The buffer amount below the maximum debt ceiling is (`DEBT_CEILING_BUFFER`):

- This parameter will be specified in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.6.1.2.1.1.3 - Rate Limits [Core]  <!-- UUID: cdda3be6-f632-44a7-aaae-b5ee01442bd6 -->

The documents herein list the Rate Limits for the Pattern Liquidity Layer on each blockchain.

###### A.6.1.1.6.2.6.1.2.1.1.3.1 - Ethereum Mainnet [Core]  <!-- UUID: 08ac5921-06ce-4b7d-9dfa-7a466ed9e7de -->

The documents herein list the current `RateLimits` for the Pattern Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.6.2.6.1.2.1.1.3.1.1 - Ethereum Mainnet USDS [Core]  <!-- UUID: bda93796-f235-4b48-a131-b84fdd5bc920 -->

The maximum mint, burn, and swap for USDS on Ethereum Mainnet are located herein.

###### A.6.1.1.6.2.6.1.2.1.1.3.1.1.1 - USDS Mint Maximum [Core]  <!-- UUID: c71c498c-1529-4bf1-9520-b0a580ce1ffb -->

The maximum amount of USDS that can be minted within the Pattern Liquidity Layer (`LIMIT_USDS_MINT`) is specified in the document herein.

- `maxAmount`: 100,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.6.2.6.1.2.1.1.3.1.1.2 - USDS Burn Maximum [Core]  <!-- UUID: 55c46a1a-5a5a-44b6-a184-c7dbe4a4f68d -->

The maximum amount of USDS that can be burned within the Pattern Liquidity Layer (`LIMIT_USDS_BURN`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Pattern Artifact.
- `slope`: This parameter will be specified in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.6.1.2.1.1.3.1.1.3 - USDS For USDC Swap Maximum [Core]  <!-- UUID: c73a58b7-0931-44ab-8599-eca4dc70194a -->

The maximum amount of USDS that can be swapped for USDC by the Pattern Liquidity Layer in the Mainnet PSM (`LIMIT_USDS_TO_USDC`) is specified in the document herein.

- `maxAmount`: 100,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.6.2.6.1.2.1.1.4 - On-chain Parameters [Core]  <!-- UUID: d3dc636f-e81d-4889-a84c-d7818ef48b6b -->

The documents herein list general on-chain parameters for the Pattern Liquidity Layer.

###### A.6.1.1.6.2.6.1.2.1.1.4.1 - Allocator Vault Parameters [Core]  <!-- UUID: e8c676bb-a818-47dc-bd1c-05199588ba4f -->

The Allocator Vault parameters for ALLOCATOR-PATTERN-A are defined in [A.3.7.1.2.1.6 - ALLOCATOR-PATTERN-A Parameters](322e7ccc-6dcb-4f83-96e5-d8f2fa87cd00).

###### A.6.1.1.6.2.6.1.2.1.1.4.2 - Whitelisting Of ALMProxy [Core]  <!-- UUID: a8094362-4ca8-4bf0-a1d8-bbed3c80d61c -->

The ALMProxy for Pattern must be whitelisted on the LitePSM. This will effectively allow Pattern to call `buyGemNoFee` and `sellGemNoFee` on the `MCD_LITE_PSM_USDC_A` contract.

###### A.6.1.1.6.2.6.1.2.1.2 - Governance Processes [Core]  <!-- UUID: 7c432de2-411e-497b-82b3-17c6853cb0b9 -->

The documents herein describe the specific governance processes for the Pattern Liquidity Layer.

###### A.6.1.1.6.2.6.1.2.1.2.1 - Invoking New Instances [Core]  <!-- UUID: 3d4aba3f-a9d8-41c6-a132-c292cabab25e -->

The governance process to invoke a new Instance of the Allocation System Primitive follows the Root Edit process see [A.6.1.1.6.2.2.2.2.1.2 - Operational Process Definition](0a6525e3-429d-4955-8dac-9fc61f6643f8).

###### A.6.1.1.6.2.6.1.2.1.2.2 - Multisigs [Core]  <!-- UUID: cf32471f-42ca-4299-a84c-ccf437ec6950 -->

The documents herein define multisigs that have privileged access to manage the Pattern Liquidity Layer.

###### A.6.1.1.6.2.6.1.2.1.2.2.1 - Relayer Multisig [Core]  <!-- UUID: 42f3ceba-f9bc-48bb-aa89-dde3feb21479 -->

The Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.6.2.6.1.2.2.1.1.2 - Relayer Role](905e342b-8dca-4fbc-8673-f6fabb6b29fd) and is controlled by Operational GovOps Soter Labs.

###### A.6.1.1.6.2.6.1.2.1.2.2.1.1 - Address [Core]  <!-- UUID: 77969281-5739-4eba-a856-6b89259b26e1 -->

The address of the Relayer Multisig on the Ethereum Mainnet is `0xd00665Df77E0b1294Ae2bdC3662F870092f6737B`.

###### A.6.1.1.6.2.6.1.2.1.2.2.1.2 - Required Number Of Signers [Core]  <!-- UUID: 15f7cf5c-7e06-4a26-8f2f-2adacf21ec32 -->

The Relayer Multisig currently has a 2/3 signing requirement.

###### A.6.1.1.6.2.6.1.2.1.2.2.1.3 - Signers [Core]  <!-- UUID: 5660ebf4-dc55-4f91-b5f7-d735195c62a3 -->

The signers of the Relayer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs.

###### A.6.1.1.6.2.6.1.2.1.2.2.1.4 - Usage Standards [Core]  <!-- UUID: 9fd84c4e-5160-4b87-857d-8dde97d08ff2 -->

The signers of the Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Pattern Artifact.

###### A.6.1.1.6.2.6.1.2.1.2.2.1.5 - Modification [Core]  <!-- UUID: 066ac9dc-3020-4d14-bafe-43e62bacdb90 -->

Operational GovOps Soter Labs can change the signers of the Relayer Multisig at any time, so long as there are at least three (3) signers and at least two-thirds of signers are required to execute transactions.

###### A.6.1.1.6.2.6.1.2.1.2.2.2 - Freezer Multisig [Core]  <!-- UUID: 841e629e-c887-48ec-8219-e0b1c86145d6 -->

The Freezer Multisig has the `FREEZER_ROLE` as defined in [A.6.1.1.6.2.6.1.2.2.1.1.4 - Freezer Role](62db1fa2-9958-4692-a2af-907feb5d2c72).

###### A.6.1.1.6.2.6.1.2.1.2.2.2.1 - Address [Core]  <!-- UUID: 008e670d-d877-475a-96f2-950aa0d6c072 -->

The address of the Freezer Multisig on the Ethereum Mainnet is `0xe728D67bca6cb18dE249325792b6379Eef4618bB`.

###### A.6.1.1.6.2.6.1.2.1.2.2.2.2 - Required Number Of Signers [Core]  <!-- UUID: f5140241-938a-4775-a873-8ddbb21d6758 -->

The Freezer Multisig currently has a 2/5 signing requirement.

###### A.6.1.1.6.2.6.1.2.1.2.2.2.3 - Signers [Core]  <!-- UUID: 4525e369-401f-4d39-869f-5b121444ff69 -->

The signers of the Freezer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs, one (1) address controlled by Operational Facilitator Redline Facilitation Group, and one (1) address controlled by Pattern.

###### A.6.1.1.6.2.6.1.2.1.2.2.2.4 - Usage Standards [Core]  <!-- UUID: db641bf1-41f3-4035-9d0c-9328f79c7b4a -->

The signers of the Freezer Multisig should exercise their authority to freeze the Pattern Liquidity Layer in the event that Pattern is not complying with rules regarding Risk Capital or Asset Liability Management, or in the event of another emergency.

Each action executed by the Freezer Multisig, including any function calls and their parameters, must be reported to the Sky community within a reasonable time frame through a post on the Sky Forum.

###### A.6.1.1.6.2.6.1.2.1.2.2.2.5 - Modification [Core]  <!-- UUID: 601869a5-973d-46da-b601-7fef88a9e07a -->

Modification of the signers of the Freezer Multisig must be approved through an Atlas Edit Proposal.

The only exceptions to this are if: 1) a signer self-reports a loss of access to their private key due to any reason; or 2) a signer explicitly expresses their wish to be removed as a signer. In both cases, the signer is required to communicate the loss of access to their private key, or the wish to be removed as a signer, in the form of a public Sky Forum post. The specific signer should be replaced as soon as possible.

Any changes to the Multisig signers that do not fall within the two exceptions listed above, or that have not been ratified by Sky Governance, should be questioned immediately and treated as malicious. Where malicious activity is suspected, the Core Facilitator must prepare an expedited Executive Vote so that Sky Governance can vote on removing external security access from the Multisig.

###### A.6.1.1.6.2.6.1.2.1.3 - Total Risk Capital (TRC) Management [Core]  <!-- UUID: d8fa58f9-8f77-43be-a2d4-6a5b55bc9b67 -->

The documents herein specify requirements related to Pattern's Total Risk Capital (TRC) management.

###### A.6.1.1.6.2.6.1.2.1.3.1 - Pattern Dev Co.'s Operation Of Pattern Liquidity Layer And Agreement Regarding Encumbrance Ratio [Core]  <!-- UUID: 4a799475-64ce-45e7-8ecd-d63af574dfca -->

Pattern Dev Co. will operate the Pattern Liquidity Layer and agrees to stay at or below a 90% Encumbrance Ratio. See [A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9).

###### A.6.1.1.6.2.6.1.2.1.3.2 - Pattern Dev Co.'s Total Risk Capital (TRC) Management Processes [Core]  <!-- UUID: 52c89daa-256c-4779-b644-71615bb092d7 -->

As operators of the Pattern Liquidity Layer, Pattern Dev Co. automatically inherits, and is subject to, the base class of operational requirements related to Total Risk Capital management defined in [A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capital (TRC) Management](3af8a3a2-25e5-44b3-87a4-7df1f2712685). Modifications to the base operational logic automatically propagate to the Pattern Artifact.

###### A.6.1.1.6.2.6.1.2.2 - Pattern Liquidity Layer Operational Processes [Core]  <!-- UUID: a7ce0d4c-c47d-4976-a40c-d8005d35cd5c -->

The documents herein describe common operational procedures for the Pattern Liquidity Layer applicable across multiple Instances.

###### A.6.1.1.6.2.6.1.2.2.1 - Routine Protocol [Core]  <!-- UUID: d15c12da-9ef3-4b47-bcaa-d5832ee57ddf -->

The documents herein define the protocol for routine ongoing management of the Pattern Liquidity Layer and its active Instances.

###### A.6.1.1.6.2.6.1.2.2.1.1 - Role Hierarchy And Permissions [Core]  <!-- UUID: a7d02d42-69b7-4b55-924f-8513163d23e8 -->

The documents herein define roles (Admin, Relayer, ALM Controller, and Freezer) and their responsibilities/permissions for managing the Pattern Liquidity Layer.

###### A.6.1.1.6.2.6.1.2.2.1.1.1 - Default Admin Role [Core]  <!-- UUID: 6434ee18-27d9-4dcc-9895-0bbf316b8144 -->

The admin role (DEFAULT_ADMIN_ROLE) is the role that can grant and revoke any role, including itself and all other roles defined in the contract. The admin role is also used for general admin functions in all contracts. This role is fully controlled by Sky Governance via the Pattern Proxy.

`constructor(address admin) {
_grantRole(DEFAULT_ADMIN_ROLE, admin);`

###### A.6.1.1.6.2.6.1.2.2.1.1.2 - Relayer Role [Core]  <!-- UUID: 905e342b-8dca-4fbc-8673-f6fabb6b29fd -->

The `RELAYER_ROLE` is the address for the Pattern Liquidity Layer ALM Planner off-chain system that calls functions on `Controller` contracts to perform actions on behalf of the `ALMProxy` contract. The Relayer Role may be granted to an address by any address holding the `DEFAULT_ADMIN_ROLE`. The Relayer Role may be removed from an address by any address holding the `DEFAULT_ADMIN_ROLE` or the `FREEZER_ROLE`.

###### A.6.1.1.6.2.6.1.2.2.1.1.3 - ALM Controller Role [Core]  <!-- UUID: 090b5728-5338-4ab7-83bf-15b213758616 -->

The `ALM_CONTROLLER_ROLE` is the address of the role that can call the `call` functions on the `ALMProxy` contract and update `RateLimits` contract. It includes the `MainnetController` and `ForeignController` contracts. ALM Controller contracts are accessed and modified via the Relayer Role.

###### A.6.1.1.6.2.6.1.2.2.1.1.4 - Freezer Role [Core]  <!-- UUID: 62db1fa2-9958-4692-a2af-907feb5d2c72 -->

The `FREEZER_ROLE` is the address of the emergency role that can remove a compromised Relayer.

###### A.6.1.1.6.2.6.1.2.2.1.2 - Controller Functions [Core]  <!-- UUID: a4dba2f1-0f11-4a04-9982-ba41674bcec9 -->

The documents herein describe the purpose and operational use of key functions within the Pattern Liquidity Layer `MainnetController` contracts: USDS management (mint/burn USDS), Asset Transfer Management (direct transfers, protocol deposits/withdrawals), Cross-chain Operations (CCTP bridging).

###### A.6.1.1.6.2.6.1.2.2.1.2.1 - Mainnet Controller Contract Functions [Core]  <!-- UUID: b48c9008-3166-4240-a54d-732463cd28b1 -->

The documents herein define the functions controlled by the Controller contract for Pattern Liquidity Layer operations on Ethereum Mainnet.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1 - Admin Functions [Core]  <!-- UUID: 886081b4-f379-4dba-bf28-038559138713 -->

The documents herein define the operations performed by the admin role (see [A.6.1.1.6.2.6.1.2.2.1.1.1 - Default Admin Role](6434ee18-27d9-4dcc-9895-0bbf316b8144)) within the `MainnetController` contract.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1.1 - Set Mint Recipient For Destination Domain [Core]  <!-- UUID: f849be24-c82e-4b13-9a34-027dcaf03fb2 -->

The documents herein define the steps for an admin to specify which address should receive newly minted tokens on a particular destination domain.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1.1.1 - Call setMintRecipient Function [Core]  <!-- UUID: 929818fb-10b0-4520-ba00-5bc2f46815ed -->

Only an operator with the admin role is able to set the mint recipient for a destination domain. To do so, they must call the `setMintRecipient` function on the Controller contract on mainnet providing the destination domain and the mint recipient address. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role the transaction will revert.
- The contract will set the selected mint recipient for the specified destination domain.
- The contract will emit a `MintRecipientSet` event to the blockchain logs.

The function call is as follows:

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1.2 - Set LayerZero Recipient [Core]  <!-- UUID: 8666edaa-5bd6-4c13-9d3b-5854e90583cb -->

The documents herein define the steps for an admin to specify which address should receive LayerZero messages on a particular destination endpoint.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1.2.1 - Call setLayerZeroRecipient Function [Core]  <!-- UUID: 0bc584c7-53da-47ee-9e7f-7514076e5fb0 -->

Only an operator with the admin role is able to set the LayerZero recipient for a destination endpoint. To do so, they must call the `setLayerZeroRecipient` function on the Controller contract on mainnet, providing the destination endpoint ID and the recipient address. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the selected LayerZero recipient for the specified destination endpoint.
- The contract will emit a `LayerZeroRecipientSet` event to the blockchain logs.

The function call is as follows:

`function setLayerZeroRecipient(uint32 destinationEndpointId, bytes32 layerZeroRecipient) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1.3 - Set Maximum Slippage [Core]  <!-- UUID: 829d2426-0bd7-44cb-b1c3-b9958706e1b6 -->

The documents herein define the steps for an admin to set the maximum allowed slippage for a specific pool.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.1.3.1 - Call setMaximumSlippage Function [Core]  <!-- UUID: 1d54c38f-02a3-4f15-b101-d23861967337 -->

Only an operator with the admin role is able to set the maximum slippage for a pool. To do so, they must call the `setMaxSlippage` function on the Controller contract on mainnet, providing the pool address and the maximum slippage value. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the maximum slippage for the specified pool.
- The contract will emit a `MaxSlippageSet` event to the blockchain logs.

The function call is as follows:

`function setMaxSlippage(address pool, uint256 maxSlippage) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2 - Relayer Functions [Core]  <!-- UUID: 6607a910-567f-4331-9edc-e8f5013f93fb -->

The documents herein define the operations performed by the relayer role (see [A.6.1.1.6.2.6.1.2.2.1.1.2 - Relayer Role](905e342b-8dca-4fbc-8673-f6fabb6b29fd)) within the `MainnetController` contract.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.1 - Relayer Vault Functions [Core]  <!-- UUID: ada3451f-65ff-4c36-9706-4ebad61564dc -->

The documents herein define the operations that are performed to maintain the desired level of liquidity and debt balance of the Pattern Liquidity Layer.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.1.1 - Mint USDS [Core]  <!-- UUID: 52901348-0e9a-4809-94c3-09ceeda40e91 -->

The documents herein define the steps for a relayer to mint USDS from the Sky Allocation Vault to the Pattern ALM Proxy.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.1.1.1 - Call mintUSDS Function [Core]  <!-- UUID: e58f4b54-eae5-4b7c-a6b5-68406b5b50b7 -->

Only an operator with the relayer role is able to mint USDS. To do so, they must call the `mintUSDS` function on the Controller contract on mainnet with the amount of USDS that is required for minting. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will ensure the `RateLimits` allow for minting the required amount. If the mint amount does not fall within the available Rate Limit the transaction will revert.
- The contract will reduce the Rate Limit by the amount of USDS minted in this transaction.
- The contract will mint the required USDS into the buffer contract.
- The contract will transfer the newly minted USDS from the buffer to the Proxy.

The function call is as follows:

`function mintUSDS(uint256 usdsAmount) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS [Core]  <!-- UUID: 886d04ba-23c3-45fb-ac5d-044288a621e1 -->

The documents herein define the steps for a relayer to return and then burn Pattern's USDS debt in the Sky Allocation Vault.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.1.2.1 - Call burnUSDS Function [Core]  <!-- UUID: b974ebda-d402-456a-8b4d-1ea805ac7be0 -->

Only an operator with the relayer role is able to repay vault debt and burn USDS. To do so, they must call the `burnUSDS` function of the Controller contract on mainnet with the amount of USDS that they wish to burn. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will increase the available Rate Limit for minting USDS by the amount of USDS being burned. This increase will be limited by the `maxAmount` parameter in the `Rate Limit` contract.
- The contract will transfer USDS from the proxy to the buffer.
- The contract will burn the USDS from the buffer and `wipe` an equivalent amount from the vault's debt.

The function call is as follows:

`function burnUSDS(uint256 usdsAmount) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.2 - ERC-20 Functions [Core]  <!-- UUID: dfc76ebc-2a7e-453f-8d9f-e2c380af3083 -->

The documents herein define the operations that are performed to transfer ERC-20 assets to specified destinations.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.2.1 - Transfer Asset [Core]  <!-- UUID: 32b22532-f92b-4544-b1a5-41acead7982e -->

The documents herein define the steps for a relayer to transfer ERC-20 tokens to a destination address.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.2.1.1 - Call transferAsset Function [Core]  <!-- UUID: 530a40e2-8322-44ff-b2ce-4ea0821a8b80 -->

Only an operator with the relayer role is able to transfer ERC-20 assets. To do so, they must call the `transferAsset` function on the Controller contract on mainnet, providing the ERC20 asset address, the destination address, and the amount to transfer. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will ensure the `RateLimits` allow for transferring the specified amount of the asset to the destination. If the transfer amount does not fall within the available Rate Limit, the transaction will revert.
- The contract will execute the ERC-20 `transfer` function, sending the specified amount of the asset to the destination address.

The function call is as follows:

`function transferAsset(address asset, address destination, uint256 amount) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3 - ERC-4626 Functions [Core]  <!-- UUID: c6dcf1ab-9861-4a41-9edc-ea79b705db2d -->

The documents herein define the general Pattern Liquidity Layer operational procedures for interacting with ERC-4626-compliant tokenized vaults. ERC-4626 is a standard interface for vaults representing shares of an underlying ERC-20 token. Pattern Liquidity Layer can integrate with various ERC-4626 vaults. For instance-specific parameters (such as vault addresses, asset addresses, and rate limits), refer to the relevant ERC-4626 Instance Configuration Document.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.1 - Deposit To ERC-4626 Vault [Core]  <!-- UUID: 2dd9a377-0fc7-483a-8942-9eb668b8e334 -->

The documents herein define the steps for a relayer to deposit assets from the ALM Proxy to an ERC-4626 vault to receive yield-bearing shares.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.1.1 - Call depositERC4626 Function [Core]  <!-- UUID: 04ac423a-ef3a-42a2-87de-745da9afded3 -->

Only an operator with the relayer role can deposit assets into an ERC-4626 vault. To do so, they must call the `depositERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to deposit. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for deposit; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the deposit amount is within the allowed rate limit for the specified vault.
- The contract will approve the vault to spend the underlying asset from the ALM Proxy. The approval and deposit are both performed from the ALM Proxy address.
- The contract will deposit the specified amount into the vault, and the ALM Proxy will receive the corresponding number of vault shares.

The function call is as follows:

`function depositERC4626(address token, uint256 amount) external returns (uint256 shares)`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.2 - Withdraw From ERC-4626 Vault [Core]  <!-- UUID: 788ff656-5797-41f3-ac17-38c88e690cc5 -->

The documents herein define the steps for a relayer to withdraw a specified amount of the underlying asset from an ERC-4626 vault to the ALM Proxy.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.2.1 - Call withdrawERC4626 Function [Core]  <!-- UUID: 40875283-48ec-48f0-8b61-e45d33f976ab -->

Only an operator with the relayer role can withdraw assets from an ERC-4626 vault. To do so, they must call the `withdrawERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to withdraw. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for withdrawal; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the withdrawal amount is within the allowed rate limit for the specified vault.
- The contract will withdraw the specified amount from the vault, burning the necessary number of vault shares held by the ALM Proxy as part of the withdrawal process.
- The withdrawn assets will be sent to the ALM Proxy.

The function call is as follows:

`function withdrawERC4626(address token, uint256 amount) external returns (uint256 shares)`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.3 - Redeem ERC-4626 Shares [Core]  <!-- UUID: 7582c5d2-205c-4ae0-8190-ae583a3db138 -->

The documents herein define the steps for a relayer to redeem vault shares for the underlying asset from an ERC-4626 vault, with the assets sent to the ALM Proxy.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.3.3.1 - Call redeemERC4626 Function [Core]  <!-- UUID: 037d3def-39bc-4aaf-9c3d-69fb86245f35 -->

Only an operator with the relayer role can redeem vault shares for the underlying asset. To do so, they must call the `redeemERC4626` function on the Controller contract on mainnet, providing the number of shares to redeem. The address is the ALM Proxy acting as both the owner of the shares being redeemed and the receiver of the resulting assets. The operation will only succeed if the ALM Proxy holds at least the number of shares specified for redemption; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will redeem the specified number of shares from the vault, sending the resulting assets to the ALM Proxy.
- After redemption, the contract will update the withdrawal rate limit based on the amount of assets received.

The function call is as follows:

`function redeemERC4626(address token, uint256 shares) external returns (uint256 assets)`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4 - ERC-7540 Functions [Core]  <!-- UUID: f11f72f7-5f70-43e0-ad48-1b3285211284 -->

The documents herein define the general Pattern Liquidity Layer operational procedures for interacting with ERC-7540-compliant tokenized vaults. ERC-7540 is a standard interface for vaults representing and managing multiple underlying assets within a single vault. Pattern Liquidity Layer can integrate with various ERC-7540 vaults. For instance-specific parameters (such as vault addresses, asset addresses, and rate limits), refer to the relevant ERC-7540 Instance Configuration Document.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.1 - Deposit To ERC-7540 Vault [Core]  <!-- UUID: 9cb65647-4f82-44a6-9b55-25384e7a6cf6 -->

The documents herein define the steps for a relayer to request and claim deposit of assets from the ALM Proxy to an ERC-7540 vault.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.1.1 - Call requestDepositERC7540 Function [Core]  <!-- UUID: 138b2674-60c1-4a5c-925a-e30956299119 -->

Only an operator with the relayer role can request a deposit into an ERC-7540 vault. To do so, they must call the `requestDepositERC7540` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to deposit. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for deposit; otherwise, the transaction will revert. The Rate Limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the deposit amount is within the allowed rate limit for the specified vault.
- The contract will approve the vault to spend the underlying asset from the ALM Proxy. The approval and deposit are both performed from the ALM Proxy address.
- The contract will submit a deposit request to the vault. Shares will not be received immediately; they must be claimed in a separate step after the vault processes the deposit.

The function call is as follows:

`function requestDepositERC7540(address token, uint256 amount) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.1.2 - Call claimDepositERC7540 Function [Core]  <!-- UUID: fccd0af9-6156-400e-bb4b-27a9d4fca711 -->

Only an operator with the relayer role can claim shares from an ERC-7540 vault after a deposit request. To do so, they must call the `claimDepositERC7540` function on the Controller contract on mainnet, providing the vault token address. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will determine the maximum number of shares that can be claimed by the ALM Proxy.
- The contract will claim the shares from the vault, and the ALM Proxy will receive the corresponding number of vault shares.

The function call is as follows:

`function claimDepositERC7540(address token) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.2 - Redeem From ERC-7540 Vault [Core]  <!-- UUID: b46a85df-ba8e-482a-bcde-b61f2b520190 -->

The documents herein define the steps for a relayer to request and redeem vault shares for the underlying asset from an ERC-7540 vault, with the assets sent to the ALM Proxy.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.2.1 - Call requestRedeemERC7540 Function [Core]  <!-- UUID: e637cc53-2243-483f-afa2-d3e92a3365fd -->

Only an operator with the relayer role can request the redemption of shares from an ERC-7540 vault. To do so, they must call the `requestRedeemERC7540` function on the Controller contract on mainnet, providing the vault token address and the number of shares to redeem. The rate limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the redemption amount is within the allowed rate limit for the specified vault.
- The contract will submit a redemption request to the vault. Assets will not be received immediately; they must be claimed in a separate step after the vault processes the redemption.

The function call is as follows:

`function requestRedeemERC7540(address token, uint256 shares) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.4.2.2 - Call claimRedeemERC7540 Function [Core]  <!-- UUID: 0c3a819b-f93f-4565-948f-7d9147cfe9d8 -->

Only an operator with the relayer role can claim assets from an ERC-7540 vault after a redemption request. To do so, they must call the `claimRedeemERC7540` function on the Controller contract on mainnet, providing the vault token address. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will determine the maximum amount of assets that can be claimed by the ALM Proxy.
- The contract will claim the assets from the vault, and the ALM Proxy will receive the corresponding amount of underlying assets.

The function call is as follows:

`function claimRedeemERC7540(address token) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.5 - Dai / USDS Functions [Core]  <!-- UUID: 918d2721-5fea-4b89-a134-56de5146aa5c -->

The documents herein define the swap operations between Dai and USDS.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.5.1 - Swap USDS to Dai [Core]  <!-- UUID: 3107138f-1944-40da-9e60-7b9fed97b984 -->

The documents herein define a series of operations for an operator to `swap` USDS to Dai.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.5.1.1 - Call swapUSDSToDAI Function [Core]  <!-- UUID: b28a88b4-bb7f-4f7b-a538-cb394ce6ce23 -->

Only an operator with the relayer role can swap USDS to Dai. To do so, they must call the `swapUSDSToDAI` function on the Controller contract on mainnet, providing the usdsAmount. The operation will only succeed if the Proxy holds enough USDS for the swap; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will approve the DaiUsds migrator to spend the specified USDS amount from the Proxy.
- The contract will swap USDS to Dai at a 1:1 ratio by calling the `usdsToDai` function on the migrator, sending the resulting DAI to the proxy.

The function call is as follows:

`function swapUSDSToDAI(uint256 usdsAmount) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.5.2 - Swap Dai to USDS [Core]  <!-- UUID: 76a9ada0-0697-4201-8b3b-621063b3554b -->

The documents herein define a series of operations for an operator to `swap` Dai to USDS.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.5.2.1 - Call swapDAIToUSDS Function [Core]  <!-- UUID: 06ba856a-91a7-43b5-b4d7-9f392df360d4 -->

Only an operator with the relayer role can swap Dai to USDS. To do so, they must call the `swapDAIToUSDS` function on the Controller contract on mainnet, providing the daiAmount. The operation will only succeed if the Proxy holds enough Dai for the swap; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will approve the DaiUsds migrator to spend the specified Dai amount from the Proxy.
- The contract will swap Dai to USDS at a 1:1 ratio by calling the `daiToUsds` function on the migrator, sending the resulting USDS to the proxy.

The function call is as follows:

`function swapDAIToUSDS(uint256 daiAmount) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.6 - PSM Functions [Core]  <!-- UUID: 4ee9a639-8b91-4bd9-8993-9efe3117524a -->

The documents herein define the swap operations performed by the Pattern Liquidity Layer in the PSM.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.6.1 - Swap USDS to USDC [Core]  <!-- UUID: ef9a88a1-cf2b-47a9-9664-685880558489 -->

The documents herein define a series of operations for an operator to `swap` USDS to USDC through the PSM.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.6.1.1 - Call swapUSDSToUSDC Function [Core]  <!-- UUID: b08f57de-599d-46e4-aabe-64b1db5a38ad -->

Only an operator with the relayer role can swap USDS to USDC via the PSM. To do so, they must call the `swapUSDSToUSDC` function on the Controller contract on mainnet, providing the usdcAmount (denominated in 1e6 precision to match PSM USDC handling). The operation will only succeed if the ALM Proxy holds at least the equivalent amount of USDS for the swap; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for swaps. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the swap amount is within the allowed rate limit (LIMIT_USDS_TO_USDC) for the PSM.
- The contract will convert the USDC amount to an 18-decimal format using psmTo18ConversionFactor.
- The contract will approve the daiUsds contract to spend the converted amount from the ALM Proxy.
- The contract will swap USDS to Dai at a 1:1 ratio via daiUsds, sending Dai to the proxy.
- The contract will approve the PSM to spend the Dai.
- The contract will swap Dai to USDC at a 1:1 ratio with no fee via psm.buyGemNoFee, sending USDC to the proxy.

The function call is as follows:

`function swapUSDSToUSDC(uint256 usdcAmount) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.6.2 - Swap USDC To USDS [Core]  <!-- UUID: 9d828ddb-7423-41cb-9adb-43d4cbfc9d38 -->

The documents herein define a series of operations for an operator to `swap` USDC to USDS through the PSM.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.6.2.1 - Call swapUSDCToUSDS Function [Core]  <!-- UUID: 355f4606-5346-41d5-8ea7-2c4490d761e1 -->

Only an operator with the relayer role can swap USDC to USDS via the PSM. To do so, they must call the `swapUSDCToUSDS` function on the Controller contract on mainnet, providing the usdcAmount (denominated in 1e6 precision to match PSM USDC handling). The operation will only succeed if the ALM Proxy holds at least the amount of USDC specified for the swap; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for swaps. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the swap amount is within the allowed rate limit (LIMIT_USDC_TO_USDS) for the PSM.
- The contract will approve the PSM to spend the USDC from the ALM Proxy.
- The contract will calculate the swap limit per transaction based on the Dai balance held by the PSM, converting with psmTo18ConversionFactor.
- If the usdcAmount is less than or equal to the limit, the contract will perform a direct swap of USDC to Dai.
- If the usdcAmount exceeds the limit, the contract will split the swap into multiple smaller swaps: refill the PSM with Dai via psm.fill, recalculate the limit, swap the maximum allowed amount, update the remaining amount, and repeat until complete (reverting with "DssLitePsm/nothing-to-fill" if PSM cannot be filled).
- The contract will convert the USDC amount to a Dai amount, accounting for token decimal differences.
- The contract will approve the daiUsds contract to spend the Dai amount from the ALM Proxy.
- The contract will swap Dai to USDS at a 1:1 ratio via daiUsds, sending USDS to the proxy.

The function call is as follows:

`function swapUSDCToUSDS(uint256 usdcAmount) external`

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.6.3 - Transfer Token Via LayerZero [Core]  <!-- UUID: 901bf629-cee3-4296-afd6-d1e7779d15bb -->

The documents herein define the steps for a relayer to `transfer` a token via LayerZero to a destination endpoint, with the assets sent according to the configured recipient.

###### A.6.1.1.6.2.6.1.2.2.1.2.1.2.6.3.1 - Call transferTokenLayerZero Function [Core]  <!-- UUID: 24c70856-ba73-4b1e-86db-1d7829220c49 -->

Only an operator with the relayer role can transfer tokens via LayerZero. To do so, they must call the `transferTokenLayerZero` function on the Controller contract on mainnet, providing the oftAddress, amount, and destinationEndpointId (payable for native fees). The operation will only succeed if the ALM Proxy holds sufficient tokens and fees; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the transfer amount is within the allowed rate limit (built from LIMIT_LAYERZERO_TRANSFER, oftAddress, and destinationEndpointId).
- If approval is required, the contract will approve the token for the oftAddress.
- The contract will build LayerZero send options and a SendParam struct with destination details, amount, and recipient from layerZeroRecipients.
- The contract will quote the OFT receipt to set the minimum amount received.
- The contract will quote the messaging fee and execute the send via proxy.doCallWithValue, passing the fee value.

The function call is as follows:

`function transferTokenLayerZero(address oftAddress, uint256 amount, uint32  destinationEndpointId) external payable`

###### A.6.1.1.6.2.6.1.2.2.1.3 - Rate Limit Management [Core]  <!-- UUID: 2b03d21b-d03a-4c0e-8d90-d5a2f5dd9140 -->

The documents herein define the protocol for querying, setting, and adjusting `RateLimits` for Instances using their `RateLimitID`s. The Rate Limits must be maintained in line with Pattern's strategy, market conditions, and security considerations.

###### A.6.1.1.6.2.6.1.2.2.1.3.1 - Get Rate Limit Data [Core]  <!-- UUID: f46cbe06-e7df-4a92-8972-cd21bf9be2c5 -->

Anyone can query the full rate limit data for a specific key. Calling this function will carry out the following actions:

- The contract will return the stored RateLimitData struct from the _data mapping for the key.

The function call is as follows:

`function getRateLimitData(bytes32 key) external override view returns (RateLimitData memory)`

###### A.6.1.1.6.2.6.1.2.2.1.3.2 - Set Rate Limit Data [Core]  <!-- UUID: 89b060bd-1026-46ec-ab32-d032edb58f83 -->

Only an operator with the admin role is able to set or update rate limit data for a specific key, including maxAmount, slope, and historical values. There are two overloads for flexibility. Calling these functions will carry out the following actions:

- The contract will require that lastAmount is less than or equal to maxAmount, reverting with "RateLimits/invalid-lastAmount" if not.
- The contract will require that lastUpdated is less than or equal to the current block timestamp, reverting with "RateLimits/invalid-lastUpdated" if not.
- The contract will store the provided data in the _data mapping as a RateLimitData struct.
- The contract will emit a RateLimitDataSet event with the key and provided values.

The function calls are as follows:

`function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope, uint256 lastAmount, uint256 lastUpdated) public override onlyRole(DEFAULT_ADMIN_ROLE)

function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope) external override`

###### A.6.1.1.6.2.6.1.2.2.1.3.3 - Set Unlimited Rate Limit Data [Core]  <!-- UUID: 7c4bdc16-13e0-47b4-8988-18e9720eb292 -->

Only an operator with the admin role is able to set unlimited rate limit data for a specific key by configuring it with maximum values. Calling this function will carry out the following actions:

- The contract will call setRateLimitData internally with type(uint256).max for maxAmount and lastAmount, 0 for slope, and the current block timestamp for lastUpdated.

The function call is as follows:

`function setUnlimitedRateLimitData(bytes32 key) external override`

###### A.6.1.1.6.2.6.1.2.2.1.3.4 - Get Current Rate Limit [Core]  <!-- UUID: b0afea3f-9ff2-4462-a771-522b1256a343 -->

Anyone can query the current rate limit value for a specific key, accounting for time-based slope accrual. Calling this function will carry out the following actions:

- The contract will retrieve the RateLimitData for the key from the _data mapping.
- If maxAmount is type(uint256).max (unlimited case), the contract will return type(uint256).max.
- Otherwise, the contract will calculate and return the minimum of (slope * time elapsed since lastUpdated + lastAmount) and maxAmount.

The function call is as follows:

`function getCurrentRateLimit(bytes32 key) public override view returns (uint256)`

###### A.6.1.1.6.2.6.1.2.2.1.3.5 - Trigger Rate Limit Decrease [Core]  <!-- UUID: 9f76a9bc-5451-4ff7-8dcd-153e4c47fe72 -->

Only an operator with the controller role can trigger a decrease in the rate limit for a specific key by a given amount. Calling this function will carry out the following actions:

- The contract will retrieve the RateLimitData storage for the key from the data mapping.
- The contract will require that maxAmount is greater than 0, reverting with "RateLimits/zero-maxAmount" if not.
- If maxAmount is type(uint256).max (unlimited case), the contract will return type(uint256).max without changes.
- The contract will calculate the currentRateLimit using getCurrentRateLimit.
- The contract will require that amountToDecrease is less than or equal to currentRateLimit, reverting with "RateLimits/rate-limit-exceeded" if not.
- The contract will update lastAmount to currentRateLimit minus amountToDecrease and set lastUpdated to the current block timestamp.
- The contract will emit a RateLimitDecreaseTriggered event with the key, amountToDecrease, currentRateLimit, and newLimit.
- The contract will return the newLimit.

The function call is as follows:

`function triggerRateLimitDecrease(bytes32 key, uint256 amountToDecrease) external override onlyRole(CONTROLLER) returns (uint256 newLimit)`

###### A.6.1.1.6.2.6.1.2.2.1.4 - Instance Lifecycle Management [Core]  <!-- UUID: 568f470e-adce-49ee-8cbe-756757814dc5 -->

The documents herein define processes for invoking (onboarding) new Pattern Liquidity Layer Instances and offboarding existing ones. This process will be specified in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.6.1.2.2.1.5 - Upgrading Controller [Core]  <!-- UUID: 2858c1d6-bc8d-4896-a5d7-8647a1010e46 -->

The documents herein define the process for deploying new Controller contracts. This process will be specified in a future iteration of the Pattern Artifact.

###### A.6.1.1.6.2.6.1.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: ae7cab85-07da-4c66-ab60-f7837dd268fd -->

The documents herein define the process for non-routine ongoing management of the Pattern Liquidity Layer and its active Instances.

###### A.6.1.1.6.2.6.1.2.2.3 - Emergency Protocol [Core]  <!-- UUID: 9eb7f00e-dfdb-48da-92cd-ac6793496290 -->

The documents herein define all the possible actions that can be taken in case of an emergency within Pattern Liquidity Layer operations.

###### A.6.1.1.6.2.6.1.2.2.3.1 - Remove Compromised Relayer As Freezer [Core]  <!-- UUID: a7054e75-b492-4e49-bae6-41c786153fb2 -->

In the event of a compromised Relayer, the `FREEZER_ROLE` can call the function to `removeRelayer` from the Controller contract. Only an operator with the freezer role can remove a relayer. To do so, they must call the `removeRelayer` function on the Controller contract on mainnet, providing the compromised relayer's address. Calling this function will carry out the following actions:

- The contract will confirm the caller holds the freezer role. If the caller does not have the freezer role, the transaction will revert.
- The contract will revoke the relayer role from the specified address.
- The contract will emit a `RelayerRemoved(relayer)` event.

The function call is as follows:

`function removeRelayer(address relayer) external`

###### A.6.1.1.6.2.6.1.2.2.3.2 - Redeem All Mainnet Positions [Core]  <!-- UUID: d1885385-a7d8-4d1c-b345-a843a5001052 -->

The documents herein define the actions that should be performed by an operator if there is a need to recover the liquidity from Mainnet Protocols and centralize it in the Mainnet Pattern ALM Proxy.

###### A.6.1.1.6.2.6.1.2.2.3.2.1 - ERC-4626 Withdrawal Action [Core]  <!-- UUID: 872a4857-504e-4795-9cbd-2a6f159c1ea0 -->

In order to withdraw all ERC-4626 balances, the operator must call the `redeemERC4626` function.

The function call is as follows:

`function redeemERC4626(address(token), token.balanceOf(address(proxy)))`

For more detailed instructions on the code to execute this, see [A.6.1.1.6.2.6.1.2.2.1.2.1.2.3 - ERC-4626 Functions](c6dcf1ab-9861-4a41-9edc-ea79b705db2d).

###### A.6.1.1.6.2.6.1.2.2.3.3 - USDC To USDS Swap Action [Core]  <!-- UUID: c30c1496-0eff-4199-9c18-eb72fb486aac -->

This document defines the action that should be performed by an operator if there is a need to centralize all recovered liquidity in USDS. The operator must call the `swapUSDCToUSDS` function.

The function call is as follows:

`function swapUSDCToUSDS(usdc.balanceOf(address(proxy))`

For more detailed instructions on the code to execute this see [A.6.1.1.6.2.6.1.2.2.1.2.1.2.6.2 - Swap USDC To USDS](9d828ddb-7423-41cb-9adb-43d4cbfc9d38).

###### A.6.1.1.6.2.6.1.2.2.3.4 - USDS Burn Action [Core]  <!-- UUID: 451ccaa5-640c-423d-b816-de953edbf115 -->

This document defines the action that should be performed if there is a need to repay and then burn Pattern's USDS debt. The operator must call the `burnUSDS` function.

The function call is as follows:

`function burnUSDS(usds.balanceOf(address(proxy))`

More detailed instructions on the code to execute this, see [A.6.1.1.6.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS](886d04ba-23c3-45fb-ac5d-044288a621e1).

###### A.6.1.1.6.2.6.1.2.3 - Allocation Strategy [Core]  <!-- UUID: e4bc88c1-a8b6-428a-aafd-2b03e7cb85ae -->

In the future, additional logic will be added herein regarding the strategy by which capital is allocated between different Instances of the Pattern Liquidity Layer.

##### A.6.1.1.6.2.6.1.3 - Active Instances [Core]  <!-- UUID: 5050f24e-45b1-4032-adf7-319235cdb6b9 -->

The Instances of the Pattern Liquidity Layer with `Active` Status are stored herein. The `RRC Framework Full Implementation Coverage` status defines whether the Instance Financial RRC is calculated based on a fully implemented risk model (see [A.3.2.1.1.4.3.1 - Fully Implemented Risk Models](419a1d00-fbae-4d26-bd47-8f57677d8001)) or a pending risk model (see [A.3.2.1.1.4.3.2 - Pending Risk Models](81ca88bf-3f6a-4d10-a3e2-d47cf6636d7d)). If the Instance Financial RRC is calculated based on a fully implemented risk model the status is `Covered`. If the Instance Financial RRC is calculated based on a pending risk model the status is `Pending`.

###### A.6.1.1.6.2.6.1.3.1 - Ethereum Mainnet Instances [Core]  <!-- UUID: 5eb721ed-289b-42f8-bed4-1e62debcc31c -->

The Ethereum Mainnet Instances of the Pattern Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.6.2.6.1.3.1.1 - Maple [Core]  <!-- UUID: ffd9916b-8088-47bb-854f-2fd3f31b67eb -->

The Ethereum Mainnet Instances of the Maple Protocol with `Active` Status are stored herein.

###### A.6.1.1.6.2.6.1.3.1.1.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document [Core]  <!-- UUID: 50d86fb7-cacd-4f9b-adf4-7056cfe8cd97 -->

The documents herein contain the Instance Configuration Document for the Maple USDC Instance.

###### A.6.1.1.6.2.6.1.3.1.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 1b922f8d-dc0e-4788-bb42-a01319b3e272 -->

**`Covered`**

###### A.6.1.1.6.2.6.1.3.1.1.1.2 - Parameters [Core]  <!-- UUID: 91e09aad-6287-44a1-a113-07adb46045d8 -->

The documents herein define the parameters of the Maple USDC Instance of the Allocation System Primitive.

###### A.6.1.1.6.2.6.1.3.1.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 3bb453cb-4ae2-466f-9008-b50079d27767 -->

The documents herein define the Instance identifiers

###### A.6.1.1.6.2.6.1.3.1.1.1.2.1.1 - Network [Core]  <!-- UUID: b20300e4-a1e9-4461-a62f-7d28dd3ba411 -->

Ethereum Mainnet

###### A.6.1.1.6.2.6.1.3.1.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 68c3772f-bb79-4518-94b4-f62a5f9976cd -->

Maple

###### A.6.1.1.6.2.6.1.3.1.1.1.2.1.3 - Asset Supplied By Pattern Liquidity Layer [Core]  <!-- UUID: 3374585c-f518-4f40-ae7e-ef6adf934d30 -->

USDC

###### A.6.1.1.6.2.6.1.3.1.1.1.2.1.4 - Token [Core]  <!-- UUID: 91b6aca1-10f0-4353-b392-33c28777ced3 -->

syrupUSDC

###### A.6.1.1.6.2.6.1.3.1.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 29098a46-4273-4375-8ae1-4c2f869c12bc -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.6.2.6.1.3.1.1.1.2.2.1 - Token Address [Core]  <!-- UUID: f62da26d-7c08-4c6c-8ed2-732bd756fa18 -->

`0x80ac24aA929eaF5013f6436cdA2a7ba190f5Cc0b`

###### A.6.1.1.6.2.6.1.3.1.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 2b47ae9c-85f4-41ac-97f9-63737a95aab3 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.6.2.6.1.3.1.1.1.2.3 - RateLimitIDs [Core]  <!-- UUID: b909a2b6-4fea-42f1-a883-6c4be70abd3c -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are specified in the documents herein.

###### A.6.1.1.6.2.6.1.3.1.1.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 36faf4e4-dbef-488e-b1f3-a145c2058289 -->

The inflow RateLimitID is: `0x99a69e57b2f387f999d6adff6eb2e707b59fdb54f06ca6211b4f20956e9bfe10`

###### A.6.1.1.6.2.6.1.3.1.1.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 8b64e6db-f656-47cc-939d-34d92e10048e -->

The outflow RateLimitID is: `0x64e6fd9d694640eebeeefc7b5abe32ef09bbabaa3d4e60221461d05a9577dc57`

###### A.6.1.1.6.2.6.1.3.1.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 93912f1a-3f33-4584-9d4c-dd0a57571c4e -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the documents herein.

###### A.6.1.1.6.2.6.1.3.1.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: baf5e2d2-8d4f-4248-90ff-c3bb21972b62 -->

The deposit rate limits are:

- `maxAmount`: 100,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.6.2.6.1.3.1.1.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 49a40f8d-e564-4cb3-bd6d-44d51bcba9c2 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.6.2.6.1.3.1.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: eb78d31a-7540-4851-815a-8d1200050dee -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.6.2.6.1.3.1.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: d19f3ee9-95d8-42fc-971d-1fe20aeea6ba -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Pattern Liquidity Layer processes.

###### A.6.1.1.6.2.6.1.3.1.1.1.3.1 - Redeem Maple Shares [Core]  <!-- UUID: e1bc16e0-7239-49fe-bc15-c51867bb1b5a -->

The documents herein define the steps for a relayer to redeem vault shares from Maple.

###### A.6.1.1.6.2.6.1.3.1.1.1.3.1.1 - Call RequestMapleRedemption Function [Core]  <!-- UUID: d080330d-912e-4c6d-9c81-714ce4b544a1 -->

Only an operator with the relayer role can request the redemption of shares from Maple. To do so, they must call the `requestMapleRedemption` function on the Controller contract on mainnet, providing the Maple token address and the number of shares to request. All Maple redemption operations are performed on behalf of the ALM Proxy and the destination address is always set to the proxy by the contract. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the redemption amount is within the allowed rate limit for the specified vault and decrease the rate limit for the redemption amount.
- The contract will submit a redemption request to the vault. Assets will not be received immediately; they must be claimed in a separate step after the vault processes the redemption.

The function call is as follows:

`function requestMapleRedemption(address mapleToken, uint256 shares) external`

###### A.6.1.1.6.2.6.1.3.1.1.1.3.1.2 - Call CancelMapleRedemption Function [Core]  <!-- UUID: 85d7a1f5-3361-49cf-b087-b027183cb640 -->

Only an operator with the relayer role can cancel a previously requested redemption of shares from Maple. To do so, they must call the `cancelMapleRedemption` function on the Controller contract on mainnet, providing the Maple token address and the number of shares to cancel. All Maple cancellations of redemption operations are performed on behalf of the ALM Proxy. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will check that a rate limit exists for the asset. If no rate limit exists the transaction will revert.
- The contract will submit a cancellation request to the vault, removing the specified number of shares from the pending redemption.

The function call is as follows:

`function cancelMapleRedemption(address mapleToken, uint256 shares) external`

##### A.6.1.1.6.2.6.1.4 - Completed Instances [Core]  <!-- UUID: f7a6d433-9be9-4140-89b4-eacf579522e4 -->

The Instances of the Allocation System Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.6.1.5 - In Progress Invocations [Core]  <!-- UUID: 1899ca65-7192-4881-b75d-21712af70e3c -->

The in progress Invocations of the Allocation System Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.6.1.3 - Active Instances](5050f24e-45b1-4032-adf7-319235cdb6b9).

#### A.6.1.1.6.2.6.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: 5345e5c5-d791-48ab-835c-413af9665327 -->

The documents herein contain all data and specifications for Pattern's Instances of the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.6.1.1.6.2.6.2.1 - Primitive Hub Document [Core]  <!-- UUID: f4572c7d-15e0-44e6-842e-80b93f4a3357 -->

The documents herein organize all base information relevant to Pattern's usage of the Risk Capital Rental Primitive.

###### A.6.1.1.6.2.6.2.1.1 - Global Activation Status [Core]  <!-- UUID: a865a886-0961-46d5-9ba9-079c49971538 -->

`Inactive`

###### A.6.1.1.6.2.6.2.1.2 - Active Instances Directory [Core]  <!-- UUID: edf76ec6-4b5b-4d06-be3a-21a97096754a -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.6.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: b73aa2a6-aa69-4bf1-91aa-cad8c95f1cce -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.6.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: b6ff1423-0299-4688-bfa4-f900fd940698 -->

This document contains a Directory of all prospective Instances of the Risk Capital Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.6.2.1.2 - Active Instances Directory](edf76ec6-4b5b-4d06-be3a-21a97096754a), whereas failed Invocations are Archived in [A.6.1.1.6.2.6.2.1.5 - Hub Data Repository](ea2a247c-3564-4bdb-a1a7-2a2559e51f03).

###### A.6.1.1.6.2.6.2.1.5 - Hub Data Repository [Core]  <!-- UUID: ea2a247c-3564-4bdb-a1a7-2a2559e51f03 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.6.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: c47c1559-736e-43af-b8d3-55d0a7b60e8c -->

The subtrees for archived Invocations and Instances of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.6.2.6.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9edcdbb1-02ab-48aa-bd6d-b363bb34559a -->

The subtrees for failed Invocations of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.6.2.6.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 8f7140b0-0f4c-46a7-9ce0-4dac030e12f6 -->

The subtrees for Instances of the Risk Capital Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.6.2.2 - Active Instances [Core]  <!-- UUID: 8bc496da-9dbc-49ea-9539-bc0c68eae4e1 -->

The Instances of the Risk Capital Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.6.2.3 - Completed Instances [Core]  <!-- UUID: 39aefad1-cd44-4526-86ed-3f2e1b76d658 -->

The Instances of the Risk Capital Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.6.2.4 - In Progress Invocations [Core]  <!-- UUID: f443ef76-7111-479f-ba69-1f0d5e1342fe -->

The in progress Invocations of the Risk Capital Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.6.2.2 - Active Instances](8bc496da-9dbc-49ea-9539-bc0c68eae4e1).

#### A.6.1.1.6.2.6.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: 6e435727-a8e1-492e-a004-31526d042d39 -->

The documents herein contain all data and specifications for Pattern's Instances of the Asset Liability Management Rental Primitive. See [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

##### A.6.1.1.6.2.6.3.1 - Primitive Hub Document [Core]  <!-- UUID: b971db81-6c85-4e95-9fb1-4556cd05e988 -->

The documents herein organize all base information relevant to Pattern's usage of the Asset Liability Management Rental Primitive.

###### A.6.1.1.6.2.6.3.1.1 - Global Activation Status [Core]  <!-- UUID: d00700e6-033b-4cd8-a986-7129adae5859 -->

`Inactive`

###### A.6.1.1.6.2.6.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 5095bf55-801b-43b9-9346-addbd20d6380 -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.6.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: a633ddea-66b1-4391-874f-ffdd2034380b -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.6.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: c1ac8c62-bd2f-4108-a297-6e0bea3e5244 -->

This document contains a Directory of all prospective Instances of the Asset Liability Management Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.6.3.1.2 - Active Instances Directory](5095bf55-801b-43b9-9346-addbd20d6380), whereas failed Invocations are Archived in [A.6.1.1.6.2.6.3.1.5 - Hub Data Repository](d7ec5f26-18a6-4453-bb73-fc40cfb6f8d1).

###### A.6.1.1.6.2.6.3.1.5 - Hub Data Repository [Core]  <!-- UUID: d7ec5f26-18a6-4453-bb73-fc40cfb6f8d1 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.6.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ce88b10b-8ff5-470b-bbc4-14ad92752989 -->

The subtrees for archived Invocations and Instances of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.6.2.6.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: a14c1182-eaec-4c43-adc6-4b3f6809adb9 -->

The subtrees for failed Invocations of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.6.2.6.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: be53be24-2aab-4b26-815d-23b776016bb9 -->

The subtrees for Instances of the Asset Liability Management Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.6.3.2 - Active Instances [Core]  <!-- UUID: 64838888-348c-4209-925a-f5bb3be8c5e8 -->

The Instances of the Asset Liability Management Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.6.3.3 - Completed Instances [Core]  <!-- UUID: 8c9e34d9-05c5-4885-af09-83de803f9417 -->

The Instances of the Asset Liability Management Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.6.3.4 - In Progress Invocations [Core]  <!-- UUID: ae5f669d-b19f-4ddb-ad13-9e9012a1bef3 -->

The in progress Invocations of the Asset Liability Management Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.6.3.2 - Active Instances](64838888-348c-4209-925a-f5bb3be8c5e8).

### A.6.1.1.6.2.7 - Core Governance Primitives [Core]  <!-- UUID: 99858314-0f00-4b3b-b249-a0b236f52f0a -->

The documents herein implement the Core Governance Primitives for Pattern. See [A.2.2.11 - Core Governance Primitives](6fa54611-c744-4b9d-897d-b2a20e9cae5d).

#### A.6.1.1.6.2.7.1 - Core Governance Reward Primitive [Core]  <!-- UUID: a63ed032-155a-42c3-9791-571a01d5f2fb -->

The documents herein contain all data and specifications for Pattern's Instances of the Core Governance Reward Primitive. See [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a).

##### A.6.1.1.6.2.7.1.1 - Primitive Hub Document [Core]  <!-- UUID: 4ca55a86-e89b-43d7-8291-297c3ecf5586 -->

The documents herein organize all base information relevant to Pattern's usage of the Core Governance Reward Primitive.

###### A.6.1.1.6.2.7.1.1.1 - Global Activation Status [Core]  <!-- UUID: cf6ee47e-4796-44a7-9689-5ac2189be470 -->

`Inactive`

###### A.6.1.1.6.2.7.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 757d7404-e9c0-4320-9db0-841a5b703d12 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Active`.

###### A.6.1.1.6.2.7.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 9bef7242-a809-4cf3-a2db-787974915c1e -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.6.2.7.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 374de01d-c42b-4322-89cf-aa613a136a3f -->

This document contains a Directory of all prospective Instances of the Core Governance Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.6.2.7.1.1.2 - Active Instances Directory](757d7404-e9c0-4320-9db0-841a5b703d12), whereas failed Invocations are Archived in [A.6.1.1.6.2.7.1.1.5 - Hub Data Repository](3bcc019b-a28c-4532-9b1a-0b563eaa7cc2).

###### A.6.1.1.6.2.7.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 3bcc019b-a28c-4532-9b1a-0b563eaa7cc2 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.6.2.7.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 91e8f0e7-55f0-4fcb-a46a-97086e69696b -->

The subtrees for archived Invocations and Instances of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.6.2.7.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: dc26dbaf-0c48-4b40-90bf-46543efc6050 -->

The subtrees for failed Invocations of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.6.2.7.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 5a6d6aae-19ed-4474-b8f4-de09a5dc8344 -->

The subtrees for Instances of the Core Governance Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.6.2.7.1.2 - Active Instances [Core]  <!-- UUID: c7489972-e440-4693-b8e4-0e0c2ead4850 -->

The Instances of the Core Governance Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.6.2.7.1.3 - Completed Instances [Core]  <!-- UUID: fe4128c5-e0a0-4e25-8b47-5ee583e00e33 -->

The Instances of the Core Governance Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.6.2.7.1.4 - In Progress Invocations [Core]  <!-- UUID: 4da34ab2-143e-4a89-8b40-e4c1bafa7951 -->

The in progress Invocations of the Core Governance Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.6.2.7.1.2 - Active Instances](c7489972-e440-4693-b8e4-0e0c2ead4850).

## A.6.1.1.6.3 - Omni Documents [Core]  <!-- UUID: 42652f00-4299-41db-9124-10be8b030ee3 -->

The documents herein define Pattern's strategic intent and operational processes relating to infrastructure inherited from Sky Core, activities unrelated to Sky Primitives, or activities spanning multiple Sky Primitives.

### A.6.1.1.6.3.1 - Governance Information Unrelated To Root Edit Primitive [Core]  <!-- UUID: df8e7155-ba1f-4606-8a4a-0619c06da12b -->

The documents herein specify Pattern governance information that is unrelated to the use of the Root Edit Primitive. The governance process for updating the Pattern Artifact is specified in the Root Edit Primitive above at [A.6.1.1.6.2.2.2 - Root Edit Primitive](e30f2e01-78c1-4286-a80a-0df31923303f).

#### A.6.1.1.6.3.1.1 - Sky Forum [Core]  <!-- UUID: 1382be77-1dc3-40e0-811d-cce8052282ee -->

Pattern uses the Sky Forum for governance-related discussion. Posts should use the "Pattern Prime" category.

#### A.6.1.1.6.3.1.2 - Sky Ecosystem Emergency Response [Core]  <!-- UUID: 721cb164-5c20-425d-a479-43e426066909 -->

The documents herein specify Pattern's emergency response protocol in situations that impact the entire Sky Ecosystem. This protocol will be specified in a future iteration of the Pattern Artifact.

#### A.6.1.1.6.3.1.3 - Agent-Specific Emergency Response [Core]  <!-- UUID: 5c2318bb-f6ce-4804-83b1-cb5efa914a23 -->

The documents herein specify Pattern's emergency response protocol in situations solely impacting Pattern versus the broader Sky Ecosystem. This protocol will be specified in a future iteration of the Pattern Artifact.
