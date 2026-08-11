# A.6.1.1.3 - Keel [Core]  <!-- UUID: bc6aed17-2969-4d04-9af6-c7bf3e4497e6 -->

The documents herein specify all of the logic for Keel, including Keel’s strategy and how it uses the Sky Primitives to operationalize this strategy.

## A.6.1.1.3.1 - Introduction [Core]  <!-- UUID: 9cbee6c7-8bc4-4b0c-a3cd-0f7f4944114e -->

Keel is an Agent dedicated to expanding access to USDS, sUSDS, and other Sky benefits with an initial focus on the Solana ecosystem. Keel leverages strategic incentives and partnerships to foster adoption, deliver the Sky Savings Rate, and bring USDS liquidity to new markets. Keel also identifies and executes allocation opportunities to generate excess returns on assets in Sky’s collateral portfolio. Keel plans to develop a user-facing DeFi hub as well as other products that align naturally with Keel’s existing capabilities, including borrowing and lending solutions.

## A.6.1.1.3.2 - Sky Primitives [Core]  <!-- UUID: 0d415ab8-7a66-4d82-98a4-67696a120650 -->

The documents herein implement the Sky Primitives for Keel. See [A.2.2 - Sky Primitives](fcde2604-a138-4c1b-9d9a-14895835c907).

### A.6.1.1.3.2.1 - Genesis Primitives [Core]  <!-- UUID: 80c991f4-7714-4706-95ab-50b0edd2f181 -->

The documents herein implement the Genesis Primitives for Keel. See [A.2.2.5 - Genesis Primitives](3d5e3668-8333-4908-adcc-5784cfe7f6b5).

#### A.6.1.1.3.2.1.1 - Agent Creation Primitive [Core]  <!-- UUID: b439ba28-c334-4211-bdc7-bb3f62158e49 -->

The documents herein contain all data and specifications for Keel’s Instance of the Agent Creation Primitive. See [A.2.2.5.1 - Agent Creation Primitive](82b95f6d-4883-4f08-ac3a-9d8189013fbe).

##### A.6.1.1.3.2.1.1.1 - Primitive Hub Document [Core]  <!-- UUID: b001c1e5-89c6-4141-bc59-b4e7b86d5f47 -->

The documents herein organize all base information relevant to Keel’s usage of the Agent Creation Primitive.

###### A.6.1.1.3.2.1.1.1.1 - Global Activation Status [Core]  <!-- UUID: c6ee2c59-96cd-464c-9c38-7b177739ab25 -->

`Completed`

###### A.6.1.1.3.2.1.1.1.2 - Active Instances Directory [Core]  <!-- UUID: d25c9d88-d80f-4692-a8c4-23d5773c4db4 -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.1.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 4498f995-ee6c-47ee-9ab2-5c268b44cfd9 -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.1.1.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 91d4bf72-2fa7-4fdc-9e7b-f7960e1406a4 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.1.1.3.1 - Single Instance Configuration Document](66669635-acd1-4c2d-b75e-b9f05dfdf9bf).

###### A.6.1.1.3.2.1.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 5dc11d90-b6cb-4e32-8e37-ec7ce4afc470 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.3.2.1.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 6b3495db-ce51-4042-ab8b-6cf288bf7e21 -->

The document herein contains the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.1.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: d397b88b-ddde-4e66-b58b-c4168157a539 -->

The subtrees for archived Invocations and Instances of the Agent Creation Primitive are stored here.

###### A.6.1.1.3.2.1.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 77479534-34de-4154-be5c-7b6f9fab8bd9 -->

The subtrees for failed Invocations of the Agent Creation Primitive are stored here.

###### A.6.1.1.3.2.1.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: a8c87f52-ad5a-43ad-a9e8-7b087193d8d4 -->

The subtrees for Instances of the Agent Creation Primitive with Suspended Status are stored here.

##### A.6.1.1.3.2.1.1.2 - Active Instances [Core]  <!-- UUID: e67cd345-759d-4bd3-b264-a81971bf1921 -->

The Instances of the Agent Creation Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 0b9ec93a-58c8-48cf-b88f-ebbbc3a4333b -->

The Instances of the Agent Creation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.3.2.1.1.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 66669635-acd1-4c2d-b75e-b9f05dfdf9bf -->

The documents herein contain the Instance Configuration Document for the Single Agent Creation Primitive Instance.

###### A.6.1.1.3.2.1.1.3.1.1 - Parameters [Core]  <!-- UUID: baa172cb-2f8d-4606-b988-1280a665f53b -->

The documents herein define the parameters of the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.3.2.1.1.3.1.1.1 - Name [Core]  <!-- UUID: 678770b0-a7fd-4b38-beee-f985504bc5b0 -->

The name of the Agent is Keel.

###### A.6.1.1.3.2.1.1.3.1.1.2 - SubProxy Account [Core]  <!-- UUID: 2d5f052a-e32a-472c-884f-4fd8746e0459 -->

The address of Keel's SubProxy Account on the Ethereum Mainnet is `0x355CD90Ecb1b409Fdf8b64c4473C3B858dA2c310`.

###### A.6.1.1.3.2.1.1.3.1.1.3 - Genesis Account [Core]  <!-- UUID: 79ef290b-94c8-420b-9e05-dbfa4156c5b4 -->

The address of Keel’s Genesis Account will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.1.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: ad622a38-8b5f-4dca-991c-8d0fb79c965c -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.3.2.1.1.3.1.3 - Data Repository [Core]  <!-- UUID: 89b627cc-8223-4faa-bb56-370731f1ee9f -->

The documents herein contain data relevant to the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.3.2.1.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 9bacd440-487f-49f7-b0ca-fbd8367e9298 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.1.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: d8938b72-36af-4dce-91bc-4a8b67d20493 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.1.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: f79736e7-1c24-43fe-9645-605791e87942 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.3.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: e46ba795-34db-4fb0-ba67-3dc178a4b47e -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.3.2.1.2 - Prime Transformation Primitive [Core]  <!-- UUID: 564fff56-3cd6-4929-b6d6-f2ea53c7dd7f -->

The documents herein contain all data and specifications for Keel’s Instance of the Prime Transformation Primitive. See [A.2.2.5.2 - Prime Transformation Primitive](81411106-fd6d-4f9c-b3ae-7af7b5e62482).

##### A.6.1.1.3.2.1.2.1 - Primitive Hub Document [Core]  <!-- UUID: ddfade4a-7dba-49ad-8feb-c19dfb56e378 -->

The documents herein organize all base information relevant to Keel’s usage of the Prime Transformation Primitive.

###### A.6.1.1.3.2.1.2.1.1 - Global Activation Status [Core]  <!-- UUID: ce33e597-a6e9-45e6-800a-f83af4bfb8b6 -->

`Completed`

###### A.6.1.1.3.2.1.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 77c9f65c-b1f6-48fa-abd2-49bf900473d7 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.1.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 70d3ad1c-6625-4c99-87ce-c1044bd8d459 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.1.2.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 655dca13-6e80-4267-8555-303053aa6956 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.1.2.3.1 - Single Instance Configuration Document](c664d698-17af-4635-9e13-c0393f416b2d).

###### A.6.1.1.3.2.1.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 120e7afd-9bfd-4532-9ded-fca199e41517 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.3.2.1.2.1.5 - Hub Data Repository [Core]  <!-- UUID: bd76b4e7-543b-458f-bd8c-c6a8d687f28a -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.1.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 3036b076-251d-4434-b195-b1ed7923767c -->

The subtrees for archived Invocations and Instances of the Prime Transformation Primitive are stored here.

###### A.6.1.1.3.2.1.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 6c4e4296-f5ad-446b-a15f-51dc081f99be -->

The subtrees for failed Invocations of the Prime Transformation Primitive are stored here.

###### A.6.1.1.3.2.1.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: b270e04d-49ba-43a2-a2c6-dd2d9bd053bc -->

The subtrees for Instances of the Prime Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.1.2.2 - Active Instances [Core]  <!-- UUID: cd02e662-ac90-474e-93cd-4366cec2aa65 -->

The Instances of the Prime Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.1.2.3 - Completed Instances [Core]  <!-- UUID: 63bcf409-d7f5-4e5a-9e65-970df317653f -->

The Instances of the Prime Transformation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.3.2.1.2.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: c664d698-17af-4635-9e13-c0393f416b2d -->

The documents herein contain the Instance Configuration Document for the Single Prime Transformation Primitive Instance.

###### A.6.1.1.3.2.1.2.3.1.1 - Parameters [Core]  <!-- UUID: 83b76fe8-a186-4be4-8a8b-2929c9a99ac4 -->

The documents herein define the parameters of the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.3.2.1.2.3.1.1.1 - Agent Type [Core]  <!-- UUID: 84a5adbb-10cc-4bda-9e94-8facfdb114e6 -->

Keel is a Prime Agent.

###### A.6.1.1.3.2.1.2.3.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: ec58c072-add1-442f-abab-c5eefb8b19d5 -->

The documents herein define the custom parameters of the Single Instance of the Prime Transformation Primitive, if any.

###### A.6.1.1.3.2.1.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 8c8258a2-768f-4da1-b400-66ed0e25ac0a -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.3.2.1.2.3.1.3 - Data Repository [Core]  <!-- UUID: af920dd4-90f5-41fa-9547-049c35ed84e8 -->

The documents herein contain data relevant to the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.3.2.1.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 10d9a22e-22ff-4f1c-8ce9-4b907b3748f5 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.1.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 7ab8edc0-14e5-40e1-8bf6-80ef2eb86549 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.1.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 795f3788-68ae-48c0-8fe3-c33b9bb81dc7 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.3.2.1.2.4 - In Progress Invocations [Core]  <!-- UUID: 83b6ac05-69c2-43a5-b7f4-c24e02671c0d -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.3.2.1.3 - Executor Transformation Primitive [Core]  <!-- UUID: 56a1e9a7-9754-4354-952d-a6fb2605c7b4 -->

The documents herein contain all data and specifications for Keel’s Instance of the Executor Transformation Primitive. See [A.2.2.5.3 - Executor Transformation Primitive](2f249be5-8edb-41e4-b429-734e1ba2cbc7).

##### A.6.1.1.3.2.1.3.1 - Primitive Hub Document [Core]  <!-- UUID: 14e5e6ce-f8ba-4a83-a013-27c821cae118 -->

The documents herein organize all base information relevant to Keel’s usage of the Executor Transformation Primitive.

###### A.6.1.1.3.2.1.3.1.1 - Global Activation Status [Core]  <!-- UUID: 0608173d-703f-47a1-b66e-0fde1faee269 -->

`Inactive`

###### A.6.1.1.3.2.1.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 3a99c1c6-03a5-4136-8195-0fe20ac0a637 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.1.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 773eee8d-8581-4dec-a917-d7238f9d5480 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.1.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: f3844b2e-d070-493f-acbd-7bb582314ed3 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.3.2.1.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 4860f54a-803e-4cfb-a7cd-8af5a159af0e -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.1.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 4015cc5b-9843-44f6-805f-9938c47ea372 -->

The subtrees for archived Invocations and Instances of the Executor Transformation Primitive are stored here.

###### A.6.1.1.3.2.1.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: b8060ecb-32c7-4a12-a439-158e6fe636ab -->

The subtrees for failed Invocations of the Executor Transformation Primitive are stored here.

###### A.6.1.1.3.2.1.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 21078bf0-ff3a-42a7-9219-acd7ca8ad35e -->

The subtrees for Instances of the Executor Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.1.3.2 - Active Instances [Core]  <!-- UUID: 9611f413-a11b-4c5b-bdf5-4c861c52cb59 -->

The Instances of the Executor Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.1.3.3 - Completed Instances [Core]  <!-- UUID: 073a2259-36d6-473a-910a-0e0a8122254d -->

The Instances of the Executor Transformation Primitive with `Completed` Status are contained herein.

##### A.6.1.1.3.2.1.3.4 - In Progress Invocations [Core]  <!-- UUID: 8b270217-b3fb-4a6f-84f5-65e1073781cd -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.3.2.1.4 - Agent Token Primitive [Core]  <!-- UUID: 7c41668c-38c2-401b-8905-51d66b3574ff -->

The documents herein contain all data and specifications for Keel’s Instance of the Agent Token Primitive. See [A.2.2.5.4 - Agent Token Primitive](2047c361-db28-4952-a70c-83d07b562064).

##### A.6.1.1.3.2.1.4.1 - Primitive Hub Document [Core]  <!-- UUID: e3469208-9d4f-4862-a82f-16222cb7235e -->

The documents herein organize all base information relevant to Keel’s usage of the Agent Token Primitive.

###### A.6.1.1.3.2.1.4.1.1 - Global Activation Status [Core]  <!-- UUID: c3443c18-3cf1-4b02-8675-e1e404b06f37 -->

`Active`

###### A.6.1.1.3.2.1.4.1.2 - Active Instances Directory [Core]  <!-- UUID: 982226bb-b1d0-436f-ab86-9edd0880eb7c -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.1.4.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: b6ae5829-82aa-43a4-96e1-15ede7b76c07 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.1.4.2.1 - Single Instance Configuration Document](d212a592-0f0f-401b-b358-17cd453fcab2).

###### A.6.1.1.3.2.1.4.1.3 - Completed Instances Directory [Core]  <!-- UUID: fe0883fb-4758-44c9-8aa2-591e68f814b2 -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.1.4.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 53fa54ce-8d6a-4cc4-901b-80f87540e4a9 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.3.2.1.4.1.5 - Hub Data Repository [Core]  <!-- UUID: 1e00fec2-9ad0-48e7-aab2-e941e3cc1862 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.1.4.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 7cfb3a25-424d-415f-be14-b68a6c2e94a4 -->

The subtrees for archived Invocations and Instances of the Agent Token Primitive are stored here.

###### A.6.1.1.3.2.1.4.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 376ffc51-a5ee-43cc-b993-d045ee5588a1 -->

The subtrees for failed Invocations of the Agent Token Primitive are stored here.

###### A.6.1.1.3.2.1.4.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 0a97b894-190f-433a-ae34-76236acdd144 -->

The subtrees for Instances of the Agent Token Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.1.4.2 - Active Instances [Core]  <!-- UUID: 26f17849-a6a4-46c2-b128-d4eefa67db5b -->

The Instances of the Agent Token Primitive with `Active` Status are stored herein.

###### A.6.1.1.3.2.1.4.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: d212a592-0f0f-401b-b358-17cd453fcab2 -->

The documents herein contain the Instance Configuration Document for the Single Agent Token Primitive Instance.

###### A.6.1.1.3.2.1.4.2.1.1 - Parameters [Core]  <!-- UUID: a391467e-c3ad-4e80-b1ce-f6d041001cdc -->

The documents herein define the parameters of the Single Instance of the Agent Token Primitive.

###### A.6.1.1.3.2.1.4.2.1.1.1 - Token Name [Core]  <!-- UUID: 60029c9c-4fcd-4bbe-b918-9e7bcb5dfdbb -->

The name of Keel’s token is Keel.

###### A.6.1.1.3.2.1.4.2.1.1.2 - Token Symbol [Core]  <!-- UUID: 41c58fff-ec4b-4bd1-bcb7-7bec6c9141b5 -->

The symbol of Keel’s token is KEEL.

###### A.6.1.1.3.2.1.4.2.1.1.3 - Genesis Supply [Core]  <!-- UUID: ffb7392d-e4ab-40fd-a886-104140ef3a64 -->

The Genesis Supply of KEEL will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.1.4.2.1.1.4 - Token Address [Core]  <!-- UUID: c3a2a1c7-7e09-49f6-9789-8fb62412b9ad -->

The address of KEEL will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.1.4.2.1.1.5 - Token Admin [Core]  <!-- UUID: 603c0bd3-547b-46e5-b96c-ea9d48b06e48 -->

The token Admin will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.1.4.2.1.1.6 - Token Emissions [Core]  <!-- UUID: 1ba562b8-3d43-46f8-bc21-5021dc7b9fed -->

Token emissions beyond the Genesis Supply are permanently disabled; this cannot be reverted by Keel Governance. Sky Governance retains the ability to revert where Keel is in violation of Risk Capital requirements and emissions are required by the Risk Framework. See [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.6.1.1.3.2.1.4.2.1.1.7 - Custom Instance Parameters [Core]  <!-- UUID: cccb3c25-8862-412a-bad3-69b535cbfe5d -->

The documents herein define the custom parameters of the Single Instance of the Agent Token Primitive, if any.

###### A.6.1.1.3.2.1.4.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 1eaa59a7-4c50-4ace-ba78-956b8a4d9219 -->

The documents herein define the operational processes for minting and initial distribution of the tokens from the Genesis Supply.

- These processes will be defined in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.1.4.2.1.3 - Data Repository [Core]  <!-- UUID: 50d5319f-6c7f-4318-83a2-2bc2eb87a134 -->

The documents herein contain data relevant to the Single Instance of the Agent Token Primitive.

###### A.6.1.1.3.2.1.4.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 79139c7c-5234-4a41-a6f7-0112216a4a9c -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.1.4.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: b49a061d-1a47-4841-91d8-753e82488288 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.1.4.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: ae670617-6780-426c-b2ef-2037d12f4669 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.3.2.1.4.3 - Completed Instances [Core]  <!-- UUID: 9494bb11-ec12-4029-89bd-40228e6ea9de -->

The Instances of the Agent Token Primitive with `Completed` Status are contained herein.

##### A.6.1.1.3.2.1.4.4 - In Progress Invocations [Core]  <!-- UUID: 7a08825e-c44f-456e-9301-7f701e53d213 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

### A.6.1.1.3.2.2 - Operational Primitives [Core]  <!-- UUID: bbd36575-5a71-4b3e-aec2-564edb0f0303 -->

The documents herein implement the Operational Primitives for Keel. See [A.2.2.6 - Operational Primitives](0192ec95-9207-480e-8c51-88d2a1da95ad).

#### A.6.1.1.3.2.2.1 - Executor Accord Primitive [Core]  <!-- UUID: c75806c5-436f-4fd6-9367-e0bc9c5a3ee6 -->

The documents herein contain all data and specifications for Keel’s Instances of the Executor Accord Primitive. See [A.2.2.6.1 - Executor Accord Primitive](88017877-3ec1-4c43-a035-6bebdf11d9bb).

##### A.6.1.1.3.2.2.1.1 - Primitive Hub Document [Core]  <!-- UUID: 51000f60-cf06-4f87-8e86-45573952645e -->

The documents herein organize all base information relevant to Keel’s usage of the Executor Accord Primitive.

###### A.6.1.1.3.2.2.1.1.1 - Global Activation Status [Core]  <!-- UUID: 4fe13ac1-d80f-468d-87c9-fd766a9f5934 -->

`Active`

###### A.6.1.1.3.2.2.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 67640351-2db1-4252-a1cb-5c28aa02a56e -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.2.1.1.2.1 - Amatsu Instance Configuration Document Location [Core]  <!-- UUID: 680f4740-3ddb-49ee-a12b-0eaf44a6d04f -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.2.1.2.1 - Amatsu Instance Configuration Document](4e46f093-0dea-4d7f-9b61-52815cc65803).

###### A.6.1.1.3.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 16cd554f-daae-476c-8938-aacf1dba4be6 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 66568c73-c92f-4bac-8b7d-bd653782b39e -->

This document contains a Directory of all prospective Instances of the Executor Accord Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.2.1.2 - Active Instances](e1eb3283-ac9c-490e-bd36-850dd8bd71bd), whereas failed Invocations are Archived in [A.6.1.1.3.2.2.1.1.5 - Hub Data Repository](55586d0c-04d0-47dc-8ea1-3296a877f3e0).

###### A.6.1.1.3.2.2.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 55586d0c-04d0-47dc-8ea1-3296a877f3e0 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.2.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e79d1a63-abb5-4f3e-a41f-7c1c1bff68bc -->

The subtrees for archived Invocations and Instances of the Executor Accord Primitive are stored here.

###### A.6.1.1.3.2.2.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 92a64b7d-cef8-4b8f-a5fc-beca030d6fb5 -->

The subtrees for failed Invocations of the Executor Accord Primitive are stored here.

###### A.6.1.1.3.2.2.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: a370a8e3-5df9-4d17-9275-e16e9d7f35f8 -->

The subtrees for Instances of the Executor Accord Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.2.1.2 - Active Instances [Core]  <!-- UUID: e1eb3283-ac9c-490e-bd36-850dd8bd71bd -->

The Instances of the Executor Accord Primitive with `Active` Status are stored herein.

###### A.6.1.1.3.2.2.1.2.1 - Amatsu Instance Configuration Document [Core]  <!-- UUID: 4e46f093-0dea-4d7f-9b61-52815cc65803 -->

The documents herein contain the Instance Configuration Document for the Amatsu Executor Accord Primitive Instance.

###### A.6.1.1.3.2.2.1.2.1.1 - Parameters [Core]  <!-- UUID: 90a3d4c7-b094-4a1f-85f4-3165deef201f -->

The documents herein define the parameters of the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.3.2.2.1.2.1.1.1 - Operational Executor Agent [Core]  <!-- UUID: ceb1e104-908d-451c-bc18-b1df694b1caf -->

The Operational Facilitator and Operational GovOps for Amatsu are specified in [A.6.1.2.1 - Operational Executor Agent Amatsu](c57df14a-fde0-43f3-89ed-c2e4981d6bd5).

###### A.6.1.1.3.2.2.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 9b6b68f4-be11-4c3e-b426-909ac66a2467 -->

The documents herein define the custom parameters of the Amatsu Instance of the Executor Accord Primitive, if any.

###### A.6.1.1.3.2.2.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 9f515d3f-fef3-47ea-82c5-e553e2ef313e -->

The documents herein define the process for the ongoing management of the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.3.2.2.1.2.1.3 - Data Repository [Core]  <!-- UUID: 9ecf7a1f-9059-4d5b-a61e-8eb659064054 -->

The documents herein contain data relevant to the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.3.2.2.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 6f47f192-3277-4e40-89d9-73edee5f465c -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.2.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 969849ad-170b-4fad-972a-e37880e91b86 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.2.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 66ac9ca7-833a-457a-8d2b-e8c3fb968412 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.3.2.2.1.3 - Completed Instances [Core]  <!-- UUID: ecc18c15-e6f8-4a6f-9a6a-04fa32e3541c -->

The Instances of the Executor Accord Primitive with `Completed` Status are stored herein.

##### A.6.1.1.3.2.2.1.4 - In Progress Invocations [Core]  <!-- UUID: ef14c4d5-3862-49f7-be15-a1dac7581dc3 -->

The in progress Invocations of the Executor Accord Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.2.1.2 - Active Instances](e1eb3283-ac9c-490e-bd36-850dd8bd71bd).

#### A.6.1.1.3.2.2.2 - Root Edit Primitive [Core]  <!-- UUID: 3d02dcbc-6a31-4f63-b464-c8c3ecebb744 -->

The documents herein contain all data and specifications for Keel’s Instance of the Root Edit Primitive. See [A.2.2.6.2 - Root Edit Primitive](78488c6b-d77f-4344-b954-476e415a2c7d).

##### A.6.1.1.3.2.2.2.1 - Primitive Hub Document [Core]  <!-- UUID: d32ff849-fe1d-4a99-ac1d-18e58eeca32f -->

The documents herein organize all base information relevant to Keel’s usage of the Root Edit Primitive.

###### A.6.1.1.3.2.2.2.1.1 - Global Activation Status [Core]  <!-- UUID: 20f48216-ac88-48df-818f-45656c0f499c -->

`Active`

###### A.6.1.1.3.2.2.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 396dc450-748d-4047-9a8e-790dd6663f32 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.2.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 750a46d2-14ce-4509-8386-66703aebedca -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.2.2.2.1 - Single Instance Configuration Document](58822854-8549-427b-9548-48388ab3be4e).

###### A.6.1.1.3.2.2.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 268ed732-c908-4cdc-93b4-0682643a8b44 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.2.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 6e444033-afe3-4d6e-9a2f-29d9cc503135 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.3.2.2.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 23116311-532d-45f7-a8b1-874d959d26fa -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.2.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e8e41a2a-da41-4ddc-b2bd-15e7ce3f2b77 -->

The subtrees for archived Invocations and Instances of the Root Edit Primitive are stored here.

###### A.6.1.1.3.2.2.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 161f3a43-e825-4200-a798-e6364a718ad2 -->

The subtrees for failed Invocations of the Root Edit Primitive are stored here.

###### A.6.1.1.3.2.2.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: bcbe25d7-b9d4-41ab-b913-d90336dd6863 -->

The subtrees for Instances of the Root Edit Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.2.2.2 - Active Instances [Core]  <!-- UUID: 9ae94a26-915d-4a99-b469-c3cea7f3c6c8 -->

The Instances of the Root Edit Primitive with `Active` Status are stored herein.

###### A.6.1.1.3.2.2.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 58822854-8549-427b-9548-48388ab3be4e -->

The documents herein contain the Instance Configuration Document for the Single Root Edit Primitive Instance.

###### A.6.1.1.3.2.2.2.2.1.1 - Parameters [Core]  <!-- UUID: 008ab1e2-e2e6-488e-a9e8-1a66b8d55f85 -->

The parameters of the Root Edit Primitive are fully specified by the Operational Process Definition in [A.6.1.1.3.2.2.2.2.1.2 - Operational Process Definition](53987e91-b86c-42be-bb4b-20af084d622d).

###### A.6.1.1.3.2.2.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 53987e91-b86c-42be-bb4b-20af084d622d -->

The documents herein define the process for using the Root Edit Primitive to update the Keel Agent Artifact. Information on Keel governance that is unrelated to the use of the Root Edit Primitive is located at [A.6.1.1.3.3.1 - Governance Information Unrelated To Root Edit Primitive](1889a2a0-7378-487a-a278-aabe3177efff).

###### A.6.1.1.3.2.2.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: eaba3101-2ef6-441d-853e-909a920140fa -->

The documents herein define the process for using the Root Edit Primitive to update the Keel Agent Artifact in routine or normal conditions (i.e., non-emergency situations).

###### A.6.1.1.3.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission [Core]  <!-- UUID: 98f59541-8896-4e64-8e99-2b25e7791bf0 -->

The Root Edit process begins with a KEEL token holder submitting a proposal through the Powerhouse system containing a draft Artifact Edit Proposal. A KEEL token holder must hold at least 1% of the circulating token supply to submit a proposal. The proposal must also be posted on the Sky Forum under the "Keel Prime" category.

###### A.6.1.1.3.2.2.2.2.1.2.1.1.1 - Root Edit Proposal Submission Requirements Exception [Core]  <!-- UUID: b3c428c6-d73f-4ed3-a876-dcc130e23ab4 -->

For proposals that solely entail a buyback or a grant of KEEL tokens, the requirement that KEEL token holders must hold at least 1% of the circulating token supply to submit a proposal is waived. However, all other procedural requirements within the Root Edit process continue to apply.

###### A.6.1.1.3.2.2.2.2.1.2.1.1.2 - Short-Term Transitionary Measures [Core]  <!-- UUID: d4c3c15b-7cdc-4c57-9bf0-53bbfd95e52c -->

Until the Powerhouse system supports submitting Artifact Edit Proposals, KEEL token holders may submit Artifact Edit Proposals by posting them to the Sky Forum under the "Keel Prime" category. The title of the post must include the text "Keel Artifact Edit Proposal". The post must include cryptographic proof that the author controls an account holding the required percentage of the total KEEL token supply specified in [A.6.1.1.3.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](98f59541-8896-4e64-8e99-2b25e7791bf0).

###### A.6.1.1.3.2.2.2.2.1.2.1.2 - Root Edit Expert Advisor Review [Core]  <!-- UUID: b9858413-c2da-4e8f-9945-b03acb0b64f6 -->

A future iteration of the Keel Artifact will specify guidelines for obtaining specialized review of proposals requiring advanced technical or financial analysis.

###### A.6.1.1.3.2.2.2.2.1.2.1.3 - Root Edit Proposal Review By Operational Facilitator [Core]  <!-- UUID: 5caf90a5-60dc-4698-9ef7-70aba1c38efe -->

Within seven (7) days of the proposal being submitted, the Operational Facilitator must review the Root Edit Proposal for alignment.

If the proposal is aligned, the Operational Facilitator must respond to the Forum post to announce their finding. In this Forum post, the Operational Facilitator must also confirm that the proposal is feasible for Operational GovOps to operationalize.

If the proposal is misaligned, the Operational Facilitator must respond to the Forum post to announce their finding and provide the reasoning for it.

###### A.6.1.1.3.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote [Core]  <!-- UUID: 45218edd-29a1-44a3-af7b-7f048a7d04f6 -->

Where their review of the proposal results in a finding of alignment with the Sky Core Atlas and Keel Artifact, the Operational Facilitator next triggers a Snapshot poll to allow token holders to vote on the proposal. The poll is open for three (3) days. A poll must have at least 10% of the circulating token supply participating and must have more than 50% of votes cast, excluding abstentions, in favor to be approved.

###### A.6.1.1.3.2.2.2.2.1.2.1.5 - Root Edit Artifact Update [Core]  <!-- UUID: 293c49b9-48f4-433c-820f-4915696f742f -->

At the conclusion of the poll, if the proposal is approved, the Operational Facilitator submits the edit to Powerhouse to formally update the Agent Artifact. Regardless of the outcome, the Operational Facilitator updates the Powerhouse System to include the result of the vote, including any pertinent documents.

###### A.6.1.1.3.2.2.2.2.1.2.1.5.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: d76d266f-50b3-4100-b198-c9d403ad50fd -->

Until the Powerhouse system supports updating Agent Artifacts, the Operational Facilitator works with the Core Facilitator to update the Atlas GitHub repository located at [https://github.com/sky-ecosystem/next-gen-atlas/pulls](https://github.com/sky-ecosystem/next-gen-atlas/pulls) to reflect proposals approved by Prime Governance.

###### A.6.1.1.3.2.2.2.2.1.2.1.6 - Artifact Edit Restrictions [Core]  <!-- UUID: e86acb47-775f-4f02-8cef-26eac82dd358 -->

The Keel Artifact cannot be edited in any way that violates the Sky Core Atlas or its specifications of the Sky Primitives, or in any way that is otherwise misaligned. The Operational Facilitator must enforce this rule through their review of Artifact Edit Proposals.

###### A.6.1.1.3.2.2.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 58df0ed3-38f4-489b-8e3b-762731f598b2 -->

The documents herein define the process for using the Root Edit Primitive to update the Keel Agent Artifact in non-routine conditions.

###### A.6.1.1.3.2.2.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 28ae6634-9099-4971-8175-31a5bcd0bedb -->

The documents herein define the process for using the Root Edit Primitive to update the Keel Agent Artifact in urgent or emergency situations.

###### A.6.1.1.3.2.2.2.2.1.2.3.1 - Root Edit Voting Process in Urgent and Emergency Situations [Core]  <!-- UUID: a7d50d59-36a3-4301-a1c7-6ac5da584d06 -->

In an Urgent or Emergency Situation, as defined by the Sky Core Atlas in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225), the Operational Facilitator may allow a Root Edit to occur more quickly than the timeline specified above. Where feasible, the Operational Facilitator should announce the decision to deploy the emergency Root Edit protocol and provide their reasoning via a public Sky Forum post (under the "Keel Prime" category), unless doing so would endanger Keel or its users.

###### A.6.1.1.3.2.2.2.2.1.3 - Data Repository [Core]  <!-- UUID: 9f496f47-3f57-443c-ac5e-a44e08d4aa4c -->

The documents herein contain data relevant to the Single Instance of the Root Edit Primitive.

###### A.6.1.1.3.2.2.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 2e6ea01e-ec36-4150-a096-6ba0143dc800 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.2.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 360ae2a4-679c-4ee5-829a-6d01f0713602 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.2.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 79fe6be0-e7ce-4349-8c63-4579d2f17295 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.3.2.2.2.3 - Completed Instances [Core]  <!-- UUID: a5a2c272-8442-4caa-9423-5eb4e0c9a97d -->

The Instances of the Root Edit Primitive with `Completed` Status are contained herein.

##### A.6.1.1.3.2.2.2.4 - In Progress Invocations [Core]  <!-- UUID: d76c3889-78be-451a-9dbd-438b22ad4e63 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.3.2.2.3 - Light Agent Primitive [Core]  <!-- UUID: 1c45537d-f720-4462-8cc8-675d08618c2a -->

The documents herein contain all data and specifications for Keel’s Instances of the Light Agent Primitive. See [A.2.2.6.3 - Light Agent Primitive](44028423-2cd1-40cb-89ac-3f762b602b90).

##### A.6.1.1.3.2.2.3.1 - Primitive Hub Document [Core]  <!-- UUID: 34688a2f-3a17-404a-b985-8ff8479c13f8 -->

The documents herein organize all base information relevant to Keel’s usage of the Light Agent Primitive.

###### A.6.1.1.3.2.2.3.1.1 - Global Activation Status [Core]  <!-- UUID: 39b36112-08f2-470f-ba9d-d32c94f2d2f1 -->

`Inactive`

###### A.6.1.1.3.2.2.3.1.2 - Active Instances Directory [Core]  <!-- UUID: e196d802-de22-410a-963a-c9d8359e9644 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.2.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 00433aa2-6d23-4a5e-8e2e-06177e41d097 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.2.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 0f0a7685-546c-486c-bb70-3a6e70464428 -->

This document contains a Directory of all prospective Instances of the Light Agent Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.2.3.2 - Active Instances](7acfe8a6-80a2-4074-a6d0-fad968c95d1c), whereas failed Invocations are Archived in [A.6.1.1.3.2.2.3.1.5 - Hub Data Repository](e62355b7-d4e4-4c7f-b877-acdfa2d81f29).

###### A.6.1.1.3.2.2.3.1.5 - Hub Data Repository [Core]  <!-- UUID: e62355b7-d4e4-4c7f-b877-acdfa2d81f29 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.2.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: d966a7e3-5ba0-4f69-ba60-d62ed5f05883 -->

The subtrees for archived Invocations and Instances of the Light Agent Primitive are stored here.

###### A.6.1.1.3.2.2.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 5abb2a17-1eb4-4db4-8272-d4bb81bded88 -->

The subtrees for failed Invocations of the Light Agent Primitive are stored here.

###### A.6.1.1.3.2.2.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 81c7ec71-da63-465e-a0fb-56b8a9be44a8 -->

The subtrees for Instances of the Light Agent Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.2.3.2 - Active Instances [Core]  <!-- UUID: 7acfe8a6-80a2-4074-a6d0-fad968c95d1c -->

The Instances of the Light Agent Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.2.3.3 - Completed Instances [Core]  <!-- UUID: 1cf924ff-7eab-4d1d-8287-f8158925dc19 -->

The Instances of the Light Agent Primitive with `Completed` Status are contained herein.

##### A.6.1.1.3.2.2.3.4 - In Progress Invocations [Core]  <!-- UUID: a039d046-24d2-4857-a59a-081143d10d61 -->

The in progress Invocations of the Light Agent Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.2.3.2 - Active Instances](7acfe8a6-80a2-4074-a6d0-fad968c95d1c).

### A.6.1.1.3.2.3 - Ecosystem Upkeep Primitives [Core]  <!-- UUID: ae5cc5d4-a105-4f67-9e38-fd9b947c57a2 -->

The documents herein implement the Ecosystem Upkeep Primitives for Keel. See [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

#### A.6.1.1.3.2.3.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: 0300c5b6-3f31-411f-b64c-707a35a55205 -->

The documents herein contain all data and specifications for Keel’s Instance of the Ecosystem Upkeep Fee Primitive. See [A.2.2.7.1 - Ecosystem Upkeep Fee Primitive](a21616f4-1611-4e0b-87b2-efbdff9f6f28).

##### A.6.1.1.3.2.3.1.1 - Primitive Hub Document [Core]  <!-- UUID: 16c06503-ed5a-4dbc-aa30-9417ca0840ad -->

The documents herein organize all base information relevant to Keel’s usage of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.3.2.3.1.1.1 - Global Activation Status [Core]  <!-- UUID: 067c779a-34c6-4843-96b9-17f868f062de -->

`Active`

###### A.6.1.1.3.2.3.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 52fa55fc-0d16-4ace-a6f4-6bee82057a55 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.3.1.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 94da1bd6-eafb-46ed-831f-33a764ac5fda -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.3.1.2.1 - Single Instance Configuration Document](4037530e-66ee-4672-871f-601aef420e3f).

###### A.6.1.1.3.2.3.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 9b2d0fed-1be9-478a-8c07-ef80b891b8d4 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.3.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 689500ec-52c9-4b49-90df-7e75cbfb820b -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.3.2.3.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 97827d06-62bb-460d-838c-30a9140cf520 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.3.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 8e6b7896-76da-470d-b3b0-c3ca34e3cd96 -->

The subtrees for archived Invocations and Instances of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.3.2.3.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 6e4c12a1-1318-4d56-80c0-f82a658b0416 -->

The subtrees for failed Invocations of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.3.2.3.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 2787b09c-d682-4386-9cf7-12a84b7744dc -->

The subtrees for Instances of the Ecosystem Upkeep Fee Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.3.1.2 - Active Instances [Core]  <!-- UUID: c75d2427-3bfe-4e20-b33f-799f4af8e4b6 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Active` Status are stored herein.

###### A.6.1.1.3.2.3.1.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 4037530e-66ee-4672-871f-601aef420e3f -->

The documents herein contain the Instance Configuration Document for the Single Ecosystem Upkeep Fee Primitive Instance.

###### A.6.1.1.3.2.3.1.2.1.1 - Parameters [Core]  <!-- UUID: d7c2fe73-d620-4953-8f25-708a3cc53111 -->

The documents herein define the parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.3.2.3.1.2.1.1.1 - Terms [Core]  <!-- UUID: 3ef3d779-a66e-44f3-9192-6c3a5a5ca971 -->

Keel will pay 0.50% of its market capitalization per year in USDS.

###### A.6.1.1.3.2.3.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: f9ff9c94-1a3d-4bc6-b2a4-40f9af76b0ac -->

The documents herein define the custom parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive, if any.

###### A.6.1.1.3.2.3.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 0461ccfd-4791-459f-b79d-c1377c0eaea9 -->

The documents herein define the process for the ongoing management of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.3.2.3.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 770597e2-1c0d-4084-878f-045f7b90933a -->

This document defines the protocol for routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.3.2.3.1.2.1.2.1.1 - Process Definition For Upkeep Fee Payment [Core]  <!-- UUID: f8f8cbf6-75e0-4dbb-b617-f44bc8cc9d8d -->

The process to pay 0.50% of Keel’s market capitalization per year in USDS will be specified in future iterations of the Keel Artifact.

###### A.6.1.1.3.2.3.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 7080e7d9-2c7e-4cf8-ad5a-4e3bf65b6d10 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.3.2.3.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: de07d443-13f5-4d86-8eea-bb218ee2b8e7 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.3.2.3.1.2.1.3 - Data Repository [Core]  <!-- UUID: 1b71dd32-0f52-4f13-89ca-97d64932cd56 -->

The documents herein contain data relevant to the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.3.2.3.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: ea840f1f-dda7-42c5-80fe-f774657831e3 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.3.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 86e71f93-690a-478c-9c87-000c3572b4df -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.3.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 27bd4d7c-d6bb-43e8-96ef-7471798fa071 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.3.2.3.1.3 - Completed Instances [Core]  <!-- UUID: 5cbe0c56-1105-4ce8-a16a-499b409fbf6c -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Completed` Status are stored herein.

##### A.6.1.1.3.2.3.1.4 - In Progress Invocations [Core]  <!-- UUID: ff19abdc-12c9-45cf-aa80-04ed0a7d71d4 -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.3.2.3.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: 354f14b7-2263-45f6-8f27-9897b25d65df -->

The documents herein contain all data and specifications for Keel’s Instance of the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

##### A.6.1.1.3.2.3.2.1 - Primitive Hub Document [Core]  <!-- UUID: b8dba4a4-069a-466a-843c-61f676c3be7e -->

The documents herein organize all base information relevant to Keel’s usage of the Upkeep Rebate Primitive.

###### A.6.1.1.3.2.3.2.1.1 - Global Activation Status [Core]  <!-- UUID: f3c3f998-4abc-4c15-95bd-905a9dcf1897 -->

`Active`

###### A.6.1.1.3.2.3.2.1.2 - Active Instances Directory [Core]  <!-- UUID: a439f8d8-dab3-4e55-8f6c-a218c069d65a -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.3.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 55f5e89c-6629-49c4-8ada-6ab8befc0467 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.3.2.2.1 - Single Instance Configuration Document](b55f18e1-1a73-455f-8990-640273d8faa4).

###### A.6.1.1.3.2.3.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 3293ffde-7260-42ec-9685-b06a58e821d9 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.3.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: e2022311-1bd9-4ec4-9bd9-ee901f455ac4 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.3.2.3.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 4df83f84-5ebf-4495-b044-9c8d760a0236 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.3.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 16fc76ed-7b13-4fb7-9720-8d616c170f05 -->

The subtrees for archived Invocations and Instances of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.3.2.3.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 3ffb7952-1a5d-40fe-b0fe-289ca1e93bca -->

The subtrees for failed Invocations of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.3.2.3.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: f5f81875-29fd-4120-8210-32a545ab938e -->

The subtrees for Instances of the Upkeep Rebate Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.3.2.2 - Active Instances [Core]  <!-- UUID: 81a59fe8-9a9c-4cc9-ae8f-2d9d70f39196 -->

The Instances of the Upkeep Rebate Primitive with `Active` Status are stored herein.

###### A.6.1.1.3.2.3.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: b55f18e1-1a73-455f-8990-640273d8faa4 -->

The documents herein contain the Instance Configuration Document for the Single Upkeep Rebate Primitive Instance.

###### A.6.1.1.3.2.3.2.2.1.1 - Parameters [Core]  <!-- UUID: 0e875626-6f3b-49ae-a47f-2a7471a1da14 -->

Every Prime Agent is entitled to the Upkeep Rebate Primitive for tokens of other Prime Agents that they hold. Because this right automatically applies, there are no parameters.

###### A.6.1.1.3.2.3.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 120312e3-ee20-4dc4-bdc2-b3fdfda415e8 -->

The documents herein define the process for the ongoing management of the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.3.2.3.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: f9d8a156-1a7f-4c8a-bb1b-f19b8070aafc -->

This document defines the protocol for routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.3.2.3.2.2.1.2.1.1 - Keel Holds Tokens Of Other Agents In Its SubProxy Account [Core]  <!-- UUID: 06cd14d5-0f55-4ac0-8d9d-f9060e0fcc1b -->

Keel keeps all tokens of other Agents it holds in its SubProxy account.

###### A.6.1.1.3.2.3.2.2.1.2.1.2 - Keel Deducts Rebate From Ecosystem Upkeep Fees [Core]  <!-- UUID: 20ccbfff-9058-47e5-a2d5-893d5bf783b6 -->

When paying Ecosystem Upkeep fees, Keel deducts the rebate from the fees it pays.

###### A.6.1.1.3.2.3.2.2.1.2.1.3 - Operational GovOps Reviews Rebate [Core]  <!-- UUID: 77ad2a49-8fa6-499b-bd26-b9fdef57fded -->

Operational GovOps reviews Keel’s calculation of the rebate before executing a return of surplus to token holders. In the event of any issues, Operational GovOps cannot execute the distribution. If Operational GovOps does not execute the distribution, Operational GovOps must post an explanation on the Sky Forum under the "Keel Prime" category and work with Keel to resolve the disagreement. If Operational GovOps and Keel cannot resolve the disagreement, it must be escalated to Core GovOps

###### A.6.1.1.3.2.3.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 4fb94d9f-fc15-4823-bab7-fb35f1247bb7 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.3.2.3.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 86a386f4-db23-4c09-b165-a0ae6d3168c9 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.3.2.3.2.2.1.3 - Data Repository [Core]  <!-- UUID: 68cfcc8f-3c24-4d02-a25b-a4a93857d9ca -->

The documents herein contain data relevant to the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.3.2.3.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 725ad94b-e5d5-4aad-a205-5a4508c9fe79 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.3.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 0c0ef0b1-2d54-49f2-9ba6-c47fd5e56af1 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.3.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: ca265d73-1cc0-43d3-806f-dd03219c5dec -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.3.2.3.2.3 - Completed Instances [Core]  <!-- UUID: 92404db0-53f0-4042-8daa-2950f01807be -->

The Instances of the Upkeep Rebate Primitive with `Completed` Status are contained herein.

##### A.6.1.1.3.2.3.2.4 - In Progress Invocations [Core]  <!-- UUID: 21b6e826-f126-4234-9baa-3a1e8a822e99 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

### A.6.1.1.3.2.4 - SkyLink Primitives [Core]  <!-- UUID: c81714a3-e1c6-423a-bf54-6456fcb88112 -->

The documents herein implement the SkyLink Primitives for Keel. See [A.2.2.8 - SkyLink Primitives](7b5d8965-a64c-4c44-b742-607f51f69d8f).

#### A.6.1.1.3.2.4.1 - Token SkyLink Primitive [Core]  <!-- UUID: 016fd32e-a2db-45d0-8893-739bdacf1c2f -->

The documents herein contain all data and specifications for Keel’s Instances of the Token SkyLink Primitive. See [A.2.2.8.1 - Token SkyLink Primitive](4504d2d4-ee45-4a07-8c5b-9baf20b12e76).

##### A.6.1.1.3.2.4.1.1 - Primitive Hub Document [Core]  <!-- UUID: b9c869ff-73ed-4b30-bc1a-33c6875524aa -->

The documents herein organize all base information relevant to Keel’s usage of the Token SkyLink Primitive.

###### A.6.1.1.3.2.4.1.1.1 - Global Activation Status [Core]  <!-- UUID: 4dc84081-55f8-4ab0-aecf-f02c90bfb969 -->

`Active`

###### A.6.1.1.3.2.4.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 9e793e15-c1b3-41e9-a9ea-5cdd034aa27f -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.4.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 58fe24db-b9bd-48d3-bd6e-c4663788cf0d -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.4.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: e5f55c8d-f3f6-4f59-b49c-18b4085df50e -->

This document contains a Directory of all prospective Instances of the Token SkyLink Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.4.1.2 - Active Instances](38756877-b767-4a71-9f38-630a96b50f5a), whereas failed Invocations are Archived in [A.6.1.1.3.2.4.1.1.5 - Hub Data Repository](99d73511-9bec-4479-a451-8196ce3ea877).

###### A.6.1.1.3.2.4.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 99d73511-9bec-4479-a451-8196ce3ea877 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.4.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 9721d168-d3fd-429f-bc94-79fab9315753 -->

The subtrees for archived Invocations and Instances of the Token SkyLink Primitive are stored here.

###### A.6.1.1.3.2.4.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 6a3fa465-3dd8-4c94-bf6c-c7ff94ed5fd7 -->

The subtrees for failed Invocations of the Token SkyLink Primitive are stored here.

###### A.6.1.1.3.2.4.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: b8e84189-0ccd-4a83-b726-915bb519b11c -->

The subtrees for Instances of the Token SkyLink Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.4.1.2 - Active Instances [Core]  <!-- UUID: 38756877-b767-4a71-9f38-630a96b50f5a -->

The Instances of the Token SkyLink Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.4.1.3 - Completed Instances [Core]  <!-- UUID: 90dac12f-9fa3-45d2-b444-a644ca747d0a -->

The Instances of the Token SkyLink Primitive with `Completed` Status are stored herein.

##### A.6.1.1.3.2.4.1.4 - In Progress Invocations [Core]  <!-- UUID: b42701f2-b0d5-4901-a458-fe0042558c64 -->

The in progress Invocations of the Token SkyLink Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.4.1.2 - Active Instances](38756877-b767-4a71-9f38-630a96b50f5a).

### A.6.1.1.3.2.5 - Demand Side Stablecoin Primitives [Core]  <!-- UUID: e72378f0-3ee3-452b-8af3-a7ef31f619fe -->

The documents herein implement the Demand Side Stablecoin Primitives for Keel. See [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d).

#### A.6.1.1.3.2.5.1 - Distribution Reward Primitive [Core]  <!-- UUID: 9ec308ad-b010-4f2d-ac33-eb56f1236493 -->

The documents herein contain all data and specifications for Keel’s Instances of the Distribution Reward Primitive. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

##### A.6.1.1.3.2.5.1.1 - Primitive Hub Document [Core]  <!-- UUID: b6b85415-c331-41b9-847e-4c5173528ca8 -->

The documents herein organize all base information relevant to Keel’s usage of the Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.1.1 - Global Activation Status [Core]  <!-- UUID: 9e1fc932-ba41-43fb-a63f-c3011020669f -->

`Active`

###### A.6.1.1.3.2.5.1.1.2 - Active Instances Directory [Core]  <!-- UUID: cc24f926-2163-46e6-a480-8d6365911553 -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.5.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7e800a1b-d86b-43f7-a227-a7ba94d264ef -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.5.1.1.3.1 - Solana Bridge Instance Configuration Document Location [Core]  <!-- UUID: cf007f6d-17a1-40fd-be3e-663b815dc8fc -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.3.2.5.1.3.1 - Solana Bridge Instance Configuration Document](97421aa5-eebe-49e4-8da8-dd5cfe2f49c4).

###### A.6.1.1.3.2.5.1.1.3.2 - 1inch Instance Configuration Document Location [Core]  <!-- UUID: 60982fac-8d7e-4b13-b779-f257238dd4a5 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.3.2.5.1.3.2 - 1inch Instance Configuration Document](eca1c14e-b112-4905-92d2-9165075ea1d2).

###### A.6.1.1.3.2.5.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 63d5ec68-45da-4146-b672-6b7bae2e9c21 -->

This document contains a Directory of all prospective Instances of the Distribution Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.5.1.2 - Active Instances](4da74767-8e45-420c-9477-89b810654ab4), whereas failed Invocations are Archived in [A.6.1.1.3.2.5.1.1.5 - Hub Data Repository](4cc7dd10-6321-4c82-a504-a5021c79fe5f).

###### A.6.1.1.3.2.5.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 4cc7dd10-6321-4c82-a504-a5021c79fe5f -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.5.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 785e9f1a-fa79-416e-b71f-27604fc0f63d -->

The subtrees for archived Invocations and Instances of the Distribution Reward Primitive are stored here.

###### A.6.1.1.3.2.5.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: c3c58b55-7d46-4dfe-927b-e571311f61c7 -->

The subtrees for failed Invocations of the Distribution Reward Primitive are stored here.

###### A.6.1.1.3.2.5.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 72e1da1a-4b11-4920-b28a-2b1a8d070e79 -->

The subtrees for Instances of the Distribution Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.5.1.2 - Active Instances [Core]  <!-- UUID: 4da74767-8e45-420c-9477-89b810654ab4 -->

The Instances of the Distribution Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.5.1.3 - Completed Instances [Core]  <!-- UUID: 15a011c4-a0bb-4fd4-bf9d-ff8b5ebc74a6 -->

The Instances of the Distribution Reward Primitive with `Completed` Status are stored herein.

###### A.6.1.1.3.2.5.1.3.1 - Solana Bridge Instance Configuration Document [Core]  <!-- UUID: 97421aa5-eebe-49e4-8da8-dd5cfe2f49c4 -->

The documents herein contain the Instance Configuration Document for the Solana Bridge Distribution Reward Primitive Instance.

###### A.6.1.1.3.2.5.1.3.1.1 - Parameters [Core]  <!-- UUID: 70bdfca7-9103-47a8-91eb-47c5eb727933 -->

The documents herein define the parameters of the Solana Bridge Instance of the Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.1.1.1 - Reward Code [Core]  <!-- UUID: e5261fd0-16b6-4c94-a101-e311e858ba92 -->

`4001`.

###### A.6.1.1.3.2.5.1.3.1.1.2 - Tracking Methodology [Core]  <!-- UUID: 78ced90e-697d-408e-b301-e22740d650dc -->

Synthetic tagging of deposits and withdrawals from the LayerZero contract on Ethereum (`0x1e1D42781FC170EF9da004Fb735f56F0276d01B8`) minus the running balances already attributed to a Distribution Reward Instance.

###### A.6.1.1.3.2.5.1.3.1.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 0cea78ce-be5f-46f5-8a48-a5d313b60611 -->

The documents herein define the custom parameters of the Solana Bridge Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.3.2.5.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: d79a21fb-1b29-4d8b-ab0c-1b3e654970c9 -->

The documents herein define the process for the ongoing management of the Solana Bridge Instance of the Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.1.2.1 - Routine Protocol [Core]  <!-- UUID: 70a1df13-bfee-43ad-9e5f-cbf4db36868b -->

This document defines the protocol for routine ongoing management of the Solana Bridge Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Keel Artifact, a version of the full process definition customized to Keel will be included herein.

###### A.6.1.1.3.2.5.1.3.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: f08a63d5-4157-4be4-9046-59005bac03c2 -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.3.2.5.1.3.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: ece7350a-4588-4c4e-8bdc-d21f539582f5 -->

The documents herein define the protocol for non-routine ongoing management of the Solana Bridge Instance of this Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 4bb2e7f5-e9b8-4d0f-84c4-faef129b06a2 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Solana Bridge Instance of this Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.1.3 - Data Repository [Core]  <!-- UUID: 73afe8a4-db40-4310-ac84-be565a062d68 -->

The documents herein contain data relevant to the Solana Bridge Instance of the Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 764fdbd7-a8a6-4da5-bd3e-c6f5471afd91 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 634e03bc-fc80-4b2c-9182-0b3ae4386f0e -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: a2eeb79e-bb70-4f25-a106-18bacd69b5ab -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.1.3.1.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 394771d8-fa9c-4f5c-8b73-b8f996cb77c1 -->

The Distribution Reward payments for the Solana Bridge Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.6.1.1.3.2.5.1.3.1.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 1d0e0165-719b-4899-af1c-8a0366a058af -->

The Distribution Reward Payments are:

###### A.6.1.1.3.2.5.1.3.2 - 1inch Instance Configuration Document [Core]  <!-- UUID: eca1c14e-b112-4905-92d2-9165075ea1d2 -->

The documents herein contain the Instance Configuration Document for the 1inch Distribution Reward Primitive Instance.

###### A.6.1.1.3.2.5.1.3.2.1 - Parameters [Core]  <!-- UUID: 4fcd06bc-72fd-4cce-83fd-5b1a7dda3a4a -->

The documents herein define the parameters of the 1inch Instance of the Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.2.1.1 - Reward Code [Core]  <!-- UUID: adbef757-5f85-43ef-84d3-7ca3d5300d7a -->

`4011`.

###### A.6.1.1.3.2.5.1.3.2.1.2 - Tracking Methodology [Core]  <!-- UUID: 3642deee-6b05-45a8-ae8f-949997406709 -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.3.2.5.1.3.2.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 988cd4e4-908a-4b5d-aa3c-251666e32a6d -->

The documents herein define the custom parameters of the 1inch Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.3.2.5.1.3.2.2 - Operational Process Definition [Core]  <!-- UUID: 5634a0c6-dfa2-490d-b3b5-0735407e345a -->

The documents herein define the process for the ongoing management of the 1inch Instance of the Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.2.2.1 - Routine Protocol [Core]  <!-- UUID: 147799a6-7bc3-45c1-8e15-f9d6377d3b52 -->

This document defines the protocol for routine ongoing management of the 1inch Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Keel Artifact, a version of the full process definition customized to Keel will be included herein.

###### A.6.1.1.3.2.5.1.3.2.2.1.1 - Agent Customizations [Core]  <!-- UUID: d8159db3-8fd7-4706-aab8-eeba1a831da0 -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.3.2.5.1.3.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 72c61c6a-ef20-4e71-a3a2-5cbdfc8fc42f -->

The documents herein define the protocol for non-routine ongoing management of the 1inch Instance of this Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.2.2.3 - Emergency Protocol [Core]  <!-- UUID: f543af9e-d7db-4a0b-93f7-0108f789e7d0 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the 1inch Instance of this Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.2.3 - Data Repository [Core]  <!-- UUID: 343708ad-a3ea-4044-b56a-055d3ffc388e -->

The documents herein contain data relevant to the 1inch Instance of the Distribution Reward Primitive.

###### A.6.1.1.3.2.5.1.3.2.3.1 - Initial Planning [Core]  <!-- UUID: 90352ea8-67ed-4148-8594-bb66826b2ad9 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.1.3.2.3.2 - Operational GovOps Review [Core]  <!-- UUID: 1f8b494d-a550-4fb7-adff-8afe9301b006 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.1.3.2.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 4da0eb19-7721-4249-994e-91c86695b785 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.1.3.2.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 55f35766-6eb6-4f4d-be40-ce70af3bed55 -->

The Distribution Reward payments for the 1inch Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.6.1.1.3.2.5.1.3.2.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: f7274663-4447-4ed3-9fb5-30c72e23802b -->

The Distribution Reward Payments are:

##### A.6.1.1.3.2.5.1.4 - In Progress Invocations [Core]  <!-- UUID: 8aa73f62-1589-4f34-a14b-c95a4701eebc -->

The in progress Invocations of the Distribution Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.5.1.2 - Active Instances](4da74767-8e45-420c-9477-89b810654ab4).

#### A.6.1.1.3.2.5.2 - Integration Boost Primitive [Core]  <!-- UUID: 6319e8b0-577c-4d08-92af-8332fde7e553 -->

The documents herein contain all data and specifications for Keel’s Instances of the Integration Boost Primitive. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

##### A.6.1.1.3.2.5.2.1 - Primitive Hub Document [Core]  <!-- UUID: 18b58761-8afa-44e0-824d-32d4c85b429e -->

The documents herein organize all base information relevant to Keel’s usage of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.1.1 - Global Activation Status [Core]  <!-- UUID: 8a49aa6e-8451-4773-82b9-17c59d3a8931 -->

`Active`

###### A.6.1.1.3.2.5.2.1.2 - Active Instances Directory [Core]  <!-- UUID: bc7296ae-4bfb-4318-87fb-44869a7932c1 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.5.2.1.2.1 - Kamino Instance Configuration Document Location [Core]  <!-- UUID: 538f7325-dcab-49e9-a369-add9f5930586 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.5.2.2.1 - Kamino Instance Configuration Document](bff45812-80f3-4e46-9428-74a374bef2fc).

###### A.6.1.1.3.2.5.2.1.2.2 - Drift Instance Configuration Document Location [Core]  <!-- UUID: 40262564-35e3-4637-a384-9d38658fd981 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.5.2.2.2 - Drift Instance Configuration Document](25114297-6807-418a-a8e2-1e08daeb711d).

###### A.6.1.1.3.2.5.2.1.2.3 - Save Instance Configuration Document Location [Core]  <!-- UUID: 4c4d2ef7-9aa4-4eb9-8339-0aa0865ee5ee -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.5.2.2.3 - Save Instance Configuration Document](1cdf853f-2d68-4ced-b143-1f3f2f7bbe70).

###### A.6.1.1.3.2.5.2.1.2.4 - Lifinity Instance Configuration Document Location [Core]  <!-- UUID: cd0c2ad5-34ec-4a4e-8af3-55c656ccdfc9 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.5.2.2.4 - Lifinity Instance Configuration Document](fbaeaf7e-92a4-4dd3-b65c-5cac02f0e831).

###### A.6.1.1.3.2.5.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 18ae39d9-bf60-40de-ad6a-97d0b111e678 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.5.2.1.3.1 - MarginFi Instance Configuration Document Location [Core]  <!-- UUID: 402d52cd-aa0b-4982-9672-743726b197d2 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.5.2.3.1 - MarginFi Instance Configuration Document](86236277-2125-46f3-82a8-737956898288).

###### A.6.1.1.3.2.5.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 3d481afc-bf97-4354-9305-3c6948001f3b -->

This document contains a Directory of all prospective Instances of the Integration Boost Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.5.2.2 - Active Instances](a53d1d40-f944-4cf2-9941-8e6f0ec77a72), whereas failed Invocations are Archived in [A.6.1.1.3.2.5.2.1.5 - Hub Data Repository](a26de8b6-230f-402f-8de0-3a6439161ffb).

###### A.6.1.1.3.2.5.2.1.5 - Hub Data Repository [Core]  <!-- UUID: a26de8b6-230f-402f-8de0-3a6439161ffb -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.5.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: d7f4e888-fe3b-412f-9623-163470390a37 -->

The subtrees for archived Invocations and Instances of the Integration Boost Primitive are stored here.

###### A.6.1.1.3.2.5.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: a4295b57-9276-4a82-b8cb-11e8e122d558 -->

The subtrees for failed Invocations of the Integration Boost Primitive are stored here.

###### A.6.1.1.3.2.5.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: b48fc045-1754-4a89-83cf-6d76fbe056bb -->

The subtrees for Instances of the Integration Boost Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.5.2.2 - Active Instances [Core]  <!-- UUID: a53d1d40-f944-4cf2-9941-8e6f0ec77a72 -->

The Instances of the Integration Boost Primitive with `Active` Status are stored herein.

###### A.6.1.1.3.2.5.2.2.1 - Kamino Instance Configuration Document [Core]  <!-- UUID: bff45812-80f3-4e46-9428-74a374bef2fc -->

The documents herein contain the Instance Configuration Document for the Kamino Integration Boost Primitive Instance.

###### A.6.1.1.3.2.5.2.2.1.1 - Parameters [Core]  <!-- UUID: 6df9c015-0a57-48d2-9bdd-08fbf42b83c9 -->

The documents herein define the parameters of the Kamino Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.1.1.1 - Integration Partner Name [Core]  <!-- UUID: d86968f4-a54b-40e1-9e82-e513a7a69a58 -->

The partner for the Kamino Integration Boost is Kamino.

###### A.6.1.1.3.2.5.2.2.1.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: aa03c0ef-76b9-42b7-a8c0-c48b8392fab5 -->

The reward address for the Kamino Integration Boost is `AU4GkzA4G9rRX3hS8QCNTiVGAtt5MNUAfK5L5Q57BAC4` on Solana.

###### A.6.1.1.3.2.5.2.2.1.1.3 - Integration Partner Chain [Core]  <!-- UUID: bfca608d-73b2-429d-a51c-d8adb412fef7 -->

The Kamino Integration Boost is on Solana blockchain.

###### A.6.1.1.3.2.5.2.2.1.1.4 - Integration Boost Cadence [Core]  <!-- UUID: f90e64f7-84c9-41b5-b5eb-ed9e890ccd5f -->

The payment cadence for the Kamino Integration Boost is weekly.

###### A.6.1.1.3.2.5.2.2.1.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: 40834c20-539b-4295-8327-7f6b997f562f -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/solana-incentives/](https://info-sky.blockanalitica.com/api/v1/solana-incentives/).

###### A.6.1.1.3.2.5.2.2.1.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: 93b3b2a9-a105-4470-b827-96b56ae4e1d5 -->

The Data Submission Responsible Actor is the Core Council Risk Advisor.

###### A.6.1.1.3.2.5.2.2.1.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: ef715b84-a864-4e01-8615-0d7668c8155b -->

The Integration Boost is calculated based on per block values for USDS in Kamino and the Sky Savings Rate.

###### A.6.1.1.3.2.5.2.2.1.1.8 - Custom Instance Parameters [Core]  <!-- UUID: 8c2f1229-9472-4833-8e8b-9d686c5e1ec4 -->

The documents herein define the custom parameters of the Kamino Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.3.2.5.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: ba61357d-b348-4bf0-907a-389fed4db441 -->

The documents herein define the process for the ongoing management of the Kamino Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: ee4adbeb-b6eb-42cc-8aca-4c0dfa34b7b0 -->

This document defines the protocol for routine ongoing management of the Kamino Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.2.2.4 - Instance Ongoing Management Protocol](805381e5-89e7-4fb9-bda7-a97e84b531ba), subject to the qualifications specified in [A.2.2.9.2.2.1.3.2.1 - Near Term Process](4ab621b4-ef8e-4b01-a6aa-9296601033c5).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Keel Artifact, a version of the full process definition customized to Keel will be included herein.

###### A.6.1.1.3.2.5.2.2.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: 3872c2ee-5465-4ce1-8c34-3800e61fd674 -->

The Keel Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.3.2.5.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: c30f58b3-2431-428f-92ff-2519457e2c4d -->

The documents herein define the protocol for non-routine ongoing management of the Kamino Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: c7fc42f8-ba5f-4d71-9dec-af1a54fd1438 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Kamino Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.1.3 - Data Repository [Core]  <!-- UUID: bd0755f7-5787-4c4c-9d81-88e6b8573f6a -->

The documents herein contain data relevant to the Kamino Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 0886e43d-3f0e-4fbc-bb39-b21934477638 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: e00ea6ea-daab-4f81-a4c4-9e9c1a245495 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 0f24b8c3-c3ae-43e4-a649-9a7df4de6fde -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.1.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: f02b9ea5-ceae-42dd-8ca0-9565f7148efb -->

The Integration Boost payments for the Kamino Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.3.2.5.2.2.1.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: 0abca082-24c3-425d-a02f-631766a438d1 -->

The Integration Boost Payments are:

###### A.6.1.1.3.2.5.2.2.2 - Drift Instance Configuration Document [Core]  <!-- UUID: 25114297-6807-418a-a8e2-1e08daeb711d -->

The documents herein contain the Instance Configuration Document for the Drift Integration Boost Primitive Instance.

###### A.6.1.1.3.2.5.2.2.2.1 - Parameters [Core]  <!-- UUID: aa1660a7-2153-4c19-b541-21e0c99da42c -->

The documents herein define the parameters of the Drift Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.2.1.1 - Integration Partner Name [Core]  <!-- UUID: ce435a87-211f-45df-ac38-66c816796fe9 -->

The partner for the Drift Integration Boost is Drift.

###### A.6.1.1.3.2.5.2.2.2.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: 8eb58c56-1b4f-4deb-9a44-0578c876ec4a -->

The reward address for the Drift Integration Boost is `5hMjmxexWu954pX9gB9jkHxMqdjpxArQS2XdvkaevRax` on Solana.

###### A.6.1.1.3.2.5.2.2.2.1.3 - Integration Partner Chain [Core]  <!-- UUID: dcde5fe3-2b4d-463c-99c4-166a238b7cf2 -->

The Drift Integration Boost is on Solana blockchain.

###### A.6.1.1.3.2.5.2.2.2.1.4 - Integration Boost Cadence [Core]  <!-- UUID: 35b1e1da-1e21-4f29-97c9-c7e99377b750 -->

The payment cadence for the Drift Integration Boost is weekly.

###### A.6.1.1.3.2.5.2.2.2.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: 59d8afd5-abf0-4c59-be6e-cccbbe18da12 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/solana-incentives/](https://info-sky.blockanalitica.com/api/v1/solana-incentives/).

###### A.6.1.1.3.2.5.2.2.2.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: 2bf87576-4df5-4d01-ba0b-6f132782813d -->

The Data Submission Responsible Actor is the Core Council Risk Advisor.

###### A.6.1.1.3.2.5.2.2.2.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: 71951f16-8f4e-49db-b98c-9d1799a1b869 -->

The Integration Boost is calculated based on per block values for USDS in Drift and the Sky Savings Rate.

###### A.6.1.1.3.2.5.2.2.2.1.8 - Custom Instance Parameters [Core]  <!-- UUID: e53ba12e-957c-48f8-b508-7190d07b4778 -->

The documents herein define the custom parameters of the Drift Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.3.2.5.2.2.2.2 - Operational Process Definition [Core]  <!-- UUID: 313e0ae3-1981-4d0e-93d6-8a4719c3d8db -->

The documents herein define the process for the ongoing management of the Drift Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.2.2.1 - Routine Protocol [Core]  <!-- UUID: e329ad9b-8788-4261-82e3-891cf51ca6f2 -->

This document defines the protocol for routine ongoing management of the Drift Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.2.2.4 - Instance Ongoing Management Protocol](805381e5-89e7-4fb9-bda7-a97e84b531ba), subject to the qualifications specified in [A.2.2.9.2.2.1.3.2.1 - Near Term Process](4ab621b4-ef8e-4b01-a6aa-9296601033c5).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Keel Artifact, a version of the full process definition customized to Keel will be included herein.

###### A.6.1.1.3.2.5.2.2.2.2.1.1 - Agent Customizations [Core]  <!-- UUID: 072498cd-35c7-4e12-a2f7-3c6462257ed3 -->

The Keel Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.3.2.5.2.2.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 97aa301f-1b42-45fa-915a-3d3e0dcb55ee -->

The documents herein define the protocol for non-routine ongoing management of the Drift Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.2.2.3 - Emergency Protocol [Core]  <!-- UUID: e3d0dc30-cf9e-4101-8729-b0039cd03e1d -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Drift Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.2.3 - Data Repository [Core]  <!-- UUID: 1cbe8086-9c91-4e07-9310-79591f81430a -->

The documents herein contain data relevant to the Drift Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.2.3.1 - Initial Planning [Core]  <!-- UUID: cb8de39f-11d4-462d-80e4-12bd793697f1 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.2.3.2 - Operational GovOps Review [Core]  <!-- UUID: fdac7f0f-b7b3-45cd-be4f-51ba5755e097 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.2.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: fd38b098-1cee-4b81-9128-49f319a85624 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.2.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: de885def-4e9c-4116-9a16-899f0d45340f -->

The Integration Boost payments for the Drift Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.3.2.5.2.2.2.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: 1016d28e-fab4-4893-8e8f-846bed7e207d -->

The Integration Boost Payments are:

###### A.6.1.1.3.2.5.2.2.3 - Save Instance Configuration Document [Core]  <!-- UUID: 1cdf853f-2d68-4ced-b143-1f3f2f7bbe70 -->

The documents herein contain the Instance Configuration Document for the Save Integration Boost Primitive Instance.

###### A.6.1.1.3.2.5.2.2.3.1 - Parameters [Core]  <!-- UUID: 0666e496-d967-42f0-9ec6-465fce5cc6ea -->

The documents herein define the parameters of the Save Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.3.1.1 - Integration Partner Name [Core]  <!-- UUID: e247f4cc-b5fb-4202-a2c7-2eeb4b6476a9 -->

The partner for the Save Integration Boost is Save.

###### A.6.1.1.3.2.5.2.2.3.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: 9b3239d4-c331-45d2-ba53-2280ebaf7626 -->

The reward address for the Save Integration Boost is `5QbRL9MU5QakL5Fx2He9YaiUzB3TQpVAUBR2ARKN1NrM` on Solana.

###### A.6.1.1.3.2.5.2.2.3.1.3 - Integration Partner Chain [Core]  <!-- UUID: c31ef8da-0d27-42f8-a6e7-cdd72fb89e15 -->

The Save Integration Boost is on Solana blockchain.

###### A.6.1.1.3.2.5.2.2.3.1.4 - Integration Boost Cadence [Core]  <!-- UUID: 89cf27b7-ef63-4671-8a21-2a5c19064418 -->

The payment cadence for the Save Integration Boost is weekly.

###### A.6.1.1.3.2.5.2.2.3.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: e6dd6579-2a26-4e85-b1fd-7887a8a387e0 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/solana-incentives/](https://info-sky.blockanalitica.com/api/v1/solana-incentives/). The data for Save is available through the API endpoint under Solend, the previous name Save operated under.

###### A.6.1.1.3.2.5.2.2.3.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: 5cf367ae-6302-488e-89d9-8d05fd447725 -->

The Data Submission Responsible Actor is the Core Council Risk Advisor.

###### A.6.1.1.3.2.5.2.2.3.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: 9c58cd0d-d637-4c26-8cec-bb5c8f4fcdbd -->

The Integration Boost is calculated based on per block values for USDS in Save and the Sky Savings Rate.

###### A.6.1.1.3.2.5.2.2.3.1.8 - Custom Instance Parameters [Core]  <!-- UUID: c5c5aa96-d72b-4ae9-b48b-f4068f9f772c -->

The documents herein define the custom parameters of the Save Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.3.2.5.2.2.3.2 - Operational Process Definition [Core]  <!-- UUID: 1f098ea0-1d9e-4207-bbb1-217e14308d87 -->

The documents herein define the process for the ongoing management of the Save Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.3.2.1 - Routine Protocol [Core]  <!-- UUID: 0e669131-758f-4ab1-8835-4532cf22c29a -->

This document defines the protocol for routine ongoing management of the Save Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.2.2.4 - Instance Ongoing Management Protocol](805381e5-89e7-4fb9-bda7-a97e84b531ba), subject to the qualifications specified in [A.2.2.9.2.2.1.3.2.1 - Near Term Process](4ab621b4-ef8e-4b01-a6aa-9296601033c5).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Keel Artifact, a version of the full process definition customized to Keel will be included herein.

###### A.6.1.1.3.2.5.2.2.3.2.1.1 - Agent Customizations [Core]  <!-- UUID: e5ffb0b8-fd9d-4932-b8fa-1ebcc2cbb0d2 -->

The Keel Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.3.2.5.2.2.3.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 6e865551-6993-4193-9d2b-9aa3f7517e3e -->

The documents herein define the protocol for non-routine ongoing management of the Save Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.3.2.3 - Emergency Protocol [Core]  <!-- UUID: 071ccf78-e331-4457-a6ef-25bf3ca3f75a -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Save Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.3.3 - Data Repository [Core]  <!-- UUID: 6263e82f-b2f0-4d02-9e5e-d62bd615bce8 -->

The documents herein contain data relevant to the Save Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.3.3.1 - Initial Planning [Core]  <!-- UUID: d1d06d85-c679-4a6f-ab24-cd10e4de1361 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.3.3.2 - Operational GovOps Review [Core]  <!-- UUID: 0e3774ea-7b40-4188-a467-ba54faacfd59 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.3.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 7e0fc33a-f01c-4bd1-bfae-96bfda6a7986 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.3.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: 5c116971-2a07-4074-9a41-422e18f5eaec -->

The Integration Boost payments for the Save Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.3.2.5.2.2.3.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: 52237195-bbb7-4b4e-a13a-536f639bd0d0 -->

The Integration Boost Payments are:

###### A.6.1.1.3.2.5.2.2.4 - Lifinity Instance Configuration Document [Core]  <!-- UUID: fbaeaf7e-92a4-4dd3-b65c-5cac02f0e831 -->

The documents herein contain the Instance Configuration Document for the Lifinity Integration Boost Primitive Instance.

###### A.6.1.1.3.2.5.2.2.4.1 - Parameters [Core]  <!-- UUID: 02b34736-8bb3-4998-aad4-d059b6574313 -->

The documents herein define the parameters of the Lifinity Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.4.1.1 - Integration Partner Name [Core]  <!-- UUID: 877e9999-2210-4d33-ae34-6f443b8a1e79 -->

The partner for the Lifinity Integration Boost is Lifinity.

###### A.6.1.1.3.2.5.2.2.4.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: 3a3bc406-cd62-4b77-b905-938cca0a6be0 -->

The reward address for the Lifinity Integration Boost is `71hhezkHQ2dhmPySsHVCCkLggfWzPFEBdfEjbn4NCXMG` on Solana.

###### A.6.1.1.3.2.5.2.2.4.1.3 - Integration Partner Chain [Core]  <!-- UUID: 8cbc89e4-5287-4fb1-88b4-3c5c09d9d345 -->

The Lifinity Integration Boost is on Solana blockchain.

###### A.6.1.1.3.2.5.2.2.4.1.4 - Integration Boost Cadence [Core]  <!-- UUID: 16f59a39-f9d9-49d3-b7e6-7a77eb5c0a2c -->

The payment cadence for the Lifinity Integration Boost is weekly.

###### A.6.1.1.3.2.5.2.2.4.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: faf426ea-f52c-4262-ac80-6e3ef4dc4c08 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/solana-incentives/](https://info-sky.blockanalitica.com/api/v1/solana-incentives/).

###### A.6.1.1.3.2.5.2.2.4.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: 94bc2f19-0cbd-4afe-8c5d-d909092fb31d -->

The Data Submission Responsible Actor is the Core Council Risk Advisor..

###### A.6.1.1.3.2.5.2.2.4.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: 492bb423-8995-4e93-9bba-d063410bed8e -->

The Integration Boost is calculated based on per block values for USDS in Lifinity and the Sky Savings Rate.

###### A.6.1.1.3.2.5.2.2.4.1.8 - Custom Instance Parameters [Core]  <!-- UUID: 25a5f4b3-ef5e-455a-8f3d-27ed798ce5a2 -->

The documents herein define the custom parameters of the Lifinity Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.3.2.5.2.2.4.2 - Operational Process Definition [Core]  <!-- UUID: b066ba5b-d067-42c6-bfa5-ab84c696e020 -->

The documents herein define the process for the ongoing management of the Lifinity Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.4.2.1 - Routine Protocol [Core]  <!-- UUID: e7eb4307-efd2-4112-9bed-e9f5e85f565b -->

This document defines the protocol for routine ongoing management of the Lifinity Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.2.2.4 - Instance Ongoing Management Protocol](805381e5-89e7-4fb9-bda7-a97e84b531ba), subject to the qualifications specified in [A.2.2.9.2.2.1.3.2.1 - Near Term Process](4ab621b4-ef8e-4b01-a6aa-9296601033c5).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Keel Artifact, a version of the full process definition customized to Keel will be included herein.

###### A.6.1.1.3.2.5.2.2.4.2.1.1 - Agent Customizations [Core]  <!-- UUID: 917307b6-ec3f-4b5f-b517-3f561c2cfe9a -->

The Keel Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.3.2.5.2.2.4.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 6bbaef28-382b-4c2c-8a9a-020de7727c86 -->

The documents herein define the protocol for non-routine ongoing management of the Lifinity Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.4.2.3 - Emergency Protocol [Core]  <!-- UUID: 2685b9a3-e827-44b0-82e9-d7750396fecc -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Lifinity Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.4.3 - Data Repository [Core]  <!-- UUID: 24b453d1-6f31-4ab2-bdca-a5493229b62f -->

The documents herein contain data relevant to the Lifinity Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.2.4.3.1 - Initial Planning [Core]  <!-- UUID: 4de91f25-bb65-4bc4-94b2-e9d58fbf9733 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.4.3.2 - Operational GovOps Review [Core]  <!-- UUID: 2a2ac512-32ec-4ee1-85a5-5cae060bc2ca -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.4.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 780b5dbf-5b27-4d12-940d-2b2d324fcf2c -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.2.4.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: b2077965-9350-4699-be85-847934f1d7b0 -->

The Integration Boost payments for the Lifinity Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.3.2.5.2.2.4.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: 4c94d227-1244-4926-be0b-d6cf87cd91b3 -->

The Integration Boost Payments are:

##### A.6.1.1.3.2.5.2.3 - Completed Instances [Core]  <!-- UUID: cb3d56e6-8284-4292-9cfe-df8c23c04bf0 -->

The Instances of the Integration Boost Primitive with `Completed` Status are contained herein.

###### A.6.1.1.3.2.5.2.3.1 - MarginFi Instance Configuration Document [Core]  <!-- UUID: 86236277-2125-46f3-82a8-737956898288 -->

The documents herein contain the Instance Configuration Document for the MarginFi Integration Boost Primitive Instance.

###### A.6.1.1.3.2.5.2.3.1.1 - Parameters [Core]  <!-- UUID: 99f6f4f6-40c5-4b3d-bc80-8bf7361479a0 -->

The documents herein define the parameters of the MarginFi Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.3.1.1.1 - Integration Partner Name [Core]  <!-- UUID: 075a138e-889a-428a-bdd7-d1ccedecbfd7 -->

The partner for the MarginFi Integration Boost is MarginFi.

###### A.6.1.1.3.2.5.2.3.1.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: 951107cb-8087-4a47-8b6c-5c50793b8796 -->

The reward address for the MarginFi Integration Boost is `AZtUUe9GvTFq9kfseu9jxTioSgdSfjgmZfGQBmhVpTj1 `on Solana.

###### A.6.1.1.3.2.5.2.3.1.1.3 - Integration Partner Chain [Core]  <!-- UUID: 10f6ab13-0f78-4017-8ce2-b8443032b3be -->

The MarginFi Integration Boost is on Solana blockchain.

###### A.6.1.1.3.2.5.2.3.1.1.4 - Integration Boost Cadence [Core]  <!-- UUID: 17608de3-6224-4cc6-886d-ab5817178b6e -->

The payment cadence for the MarginFi Integration Boost is weekly.

###### A.6.1.1.3.2.5.2.3.1.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: 4164892e-41a3-4295-a35b-c0130859a378 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/solana-incentives/](https://info-sky.blockanalitica.com/api/v1/solana-incentives/).

###### A.6.1.1.3.2.5.2.3.1.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: f9e0a68d-89a4-4c57-8da5-4912be9688fd -->

The Data Submission Responsible Actor is the Core Council Risk Advisor.

###### A.6.1.1.3.2.5.2.3.1.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: 8bc6de1d-c9ee-43a5-9e1f-9307b4de9ee1 -->

The Integration Boost is calculated based on per block values for USDS in MarginFi and the Sky Savings Rate.

###### A.6.1.1.3.2.5.2.3.1.1.8 - Custom Instance Parameters [Core]  <!-- UUID: 3160b0a5-3822-49f9-b962-70b33baa0e2c -->

The documents herein define the custom parameters of the MarginFi Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.3.2.5.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 9ed9898f-a226-49f3-94d9-9279fa5eb143 -->

The documents herein define the process for the ongoing management of the MarginFi Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.3.1.2.1 - Routine Protocol [Core]  <!-- UUID: a367b919-e9bb-4a9e-9dbd-b3a0f520201b -->

This document defines the protocol for routine ongoing management of the MarginFi Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.2.2.4 - Instance Ongoing Management Protocol](805381e5-89e7-4fb9-bda7-a97e84b531ba), subject to the qualifications specified in [A.2.2.9.2.2.1.3.2.1 - Near Term Process](4ab621b4-ef8e-4b01-a6aa-9296601033c5).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Keel Artifact, a version of the full process definition customized to Keel will be included herein.

###### A.6.1.1.3.2.5.2.3.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: 9e8e1663-b7cf-4492-8e6d-b66f80b28ab4 -->

The Keel Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.3.2.5.2.3.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 9a62f3b7-bef9-4002-865a-9d59dd19fb23 -->

The documents herein define the protocol for non-routine ongoing management of the MarginFi Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.3.1.2.3 - Emergency Protocol [Core]  <!-- UUID: d4c759f6-c8cc-4bc3-84b3-76a1a1a9492e -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the MarginFi Instance of this Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.3.1.3 - Data Repository [Core]  <!-- UUID: a7f0ef1a-f643-4370-a2e6-d8d0c7db44d7 -->

The documents herein contain data relevant to the MarginFi Instance of the Integration Boost Primitive.

###### A.6.1.1.3.2.5.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 5d022265-732d-471f-960c-ad352469f71e -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: d7fe3f68-dc0b-4494-8563-44e2f8e684a3 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 3aaf2998-6729-4ccf-848d-5dbc8d8e68ae -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.3.2.5.2.3.1.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: 61c17003-e1b0-46a8-8b67-0b120a0cdd5b -->

The Integration Boost payments for the MarginFi Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.3.2.5.2.3.1.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: bc103251-76b5-4969-b17f-520474e01a14 -->

The Integration Boost Payments are:

##### A.6.1.1.3.2.5.2.4 - In Progress Invocations [Core]  <!-- UUID: 4d86b12e-7abe-4707-afa6-3694fdb09e32 -->

The in progress Invocations of the Integration Boost Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.5.2.2 - Active Instances](a53d1d40-f944-4cf2-9941-8e6f0ec77a72).

#### A.6.1.1.3.2.5.3 - Pioneer Chain Primitive [Core]  <!-- UUID: 8744a0ac-6d59-407d-a192-7ce4ce257420 -->

The documents herein contain all data and specifications for Keel’s Instances of the Pioneer Chain Primitive. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).

##### A.6.1.1.3.2.5.3.1 - Primitive Hub Document [Core]  <!-- UUID: 9502a517-1323-4f1a-9038-8314b4704ff1 -->

The documents herein organize all base information relevant to Keel’s usage of the Pioneer Chain Primitive.

###### A.6.1.1.3.2.5.3.1.1 - Global Activation Status [Core]  <!-- UUID: 5bf76475-f22b-4929-ac3c-7792a567fa49 -->

`Active`

###### A.6.1.1.3.2.5.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 0596e4e7-880f-42ce-96b8-00e8482837fb -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.5.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: e7dd62af-a742-4518-97a6-70b885ad67f6 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.5.3.1.3.1 - Solana Instance Configuration Document Location [Core]  <!-- UUID: adab4387-3553-4134-bd3c-1f3d07f98415 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.3.2.5.3.3.1 - Solana Instance Configuration Document](638b8dd4-6faa-47b8-9553-a8a4703b6545).

###### A.6.1.1.3.2.5.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 6b836e0a-37cd-4e54-9479-1cf54ee4088c -->

This document contains a Directory of all prospective Instances of the Pioneer Chain Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.5.3.2 - Active Instances](5d043c09-1d78-456d-b356-c72a13fe46c8), whereas failed Invocations are Archived in [A.6.1.1.3.2.5.3.1.5 - Hub Data Repository](e32e87d5-bbaf-4bde-9bbd-332e2465a44a).

###### A.6.1.1.3.2.5.3.1.5 - Hub Data Repository [Core]  <!-- UUID: e32e87d5-bbaf-4bde-9bbd-332e2465a44a -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.5.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 6bd42489-8672-49d0-923b-57c6ea782fe2 -->

The subtrees for archived Invocations and Instances of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.3.2.5.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 7cd4dd2e-693a-4879-ba88-158a95c6b428 -->

The subtrees for failed Invocations of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.3.2.5.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 4289b0d8-f587-4abf-8905-8c5df520c854 -->

The subtrees for Instances of the Pioneer Chain Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.5.3.2 - Active Instances [Core]  <!-- UUID: 5d043c09-1d78-456d-b356-c72a13fe46c8 -->

The Instances of the Pioneer Chain Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.5.3.3 - Completed Instances [Core]  <!-- UUID: 4ddfaa41-e902-4d6a-a915-6d999c502a34 -->

The Instances of the Pioneer Chain Primitive with `Completed` Status are stored herein.

###### A.6.1.1.3.2.5.3.3.1 - Solana Instance Configuration Document [Core]  <!-- UUID: 638b8dd4-6faa-47b8-9553-a8a4703b6545 -->

The documents herein contain the Instance Configuration Document for the Solana Instance of the Pioneer Chain Primitive.

###### A.6.1.1.3.2.5.3.3.1.1 - Parameters [Core]  <!-- UUID: c4a101cc-2c82-4fba-8811-bf84829eead1 -->

The documents herein define the parameters of the Solana Instance of the Pioneer Chain Primitive.

###### A.6.1.1.3.2.5.3.3.1.1.1 - Instance Identifiers [Core]  <!-- UUID: 86e50f38-bf79-43cb-854e-2421b6a3c812 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.5.3.3.1.1.1.1 - Network [Core]  <!-- UUID: 8c67dee5-c782-4cb9-bdcd-964eb662c28f -->

Solana

###### A.6.1.1.3.2.5.3.3.1.1.2 - Pioneer Incentive Pool [Core]  <!-- UUID: 1010660f-aa32-41bb-b85b-0986370b225f -->

The documents herein contain the terms that govern this Instance's Pioneer Incentive Pool and its address.

###### A.6.1.1.3.2.5.3.3.1.1.2.1 - Address [Core]  <!-- UUID: f2648962-8b3a-45a1-a455-206f704535bb -->

`8JmDPG5BFQ6gpUPJV9xBixYJLqTKCSNotkXksTmNsQfj`

###### A.6.1.1.3.2.5.3.3.1.1.2.2 - Terms [Core]  <!-- UUID: d8b93260-34fe-45b2-83a1-06e093813a7c -->

The Pioneer Incentive Pool for this Instance is governed by the terms specified in [A.2.2.9.3.1.4 - Pioneer Incentive Pool](04edac33-19d5-4a87-a8ab-945a0cd57771).

###### A.6.1.1.3.2.5.3.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 1f4a087f-1f3a-4e6e-89c6-58a162674757 -->

The documents herein define the process for the ongoing management of the Solana Instance of the Pioneer Chain Primitive.

###### A.6.1.1.3.2.5.3.3.1.3 - Data Repository [Core]  <!-- UUID: dcdd2415-6ad3-4a02-a0a4-10acda9d185f -->

The documents herein contain data relevant to the Solana Instance of the Pioneer Chain Primitive.

##### A.6.1.1.3.2.5.3.4 - In Progress Invocations [Core]  <!-- UUID: 079d3d3d-2549-4216-bc56-84af879ef929 -->

The in progress Invocations of the Pioneer Chain Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.5.3.2 - Active Instances](5d043c09-1d78-456d-b356-c72a13fe46c8).

### A.6.1.1.3.2.6 - Supply Side Stablecoin Primitives [Core]  <!-- UUID: 23e77e03-5726-4def-86a8-7ae41c7c9b51 -->

The documents herein implement the Supply Side Stablecoin Primitives for Keel. See [A.2.2.10 - Supply Side Stablecoin Primitives](d1142876-33c2-4e21-9339-d8711525d46f).

#### A.6.1.1.3.2.6.1 - Allocation System Primitive [Core]  <!-- UUID: 0f04cae2-326f-42f1-bc8a-74d01e6ad2af -->

The documents herein contain all data and specifications for Keel’s Allocation System Primitive Instances.

##### A.6.1.1.3.2.6.1.1 - Primitive Hub Document [Core]  <!-- UUID: 835a84a6-2167-4013-acce-281e164c5985 -->

The documents herein organize all base information relevant to Keel’s usage of the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.1.1 - Global Activation Status [Core]  <!-- UUID: 08c6ac06-313b-47bc-b0af-bc93192c6a95 -->

`Active`

###### A.6.1.1.3.2.6.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 134c14e9-28ed-4e18-b15a-26899644dc0b -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.6.1.1.2.1 - Solana [Core]  <!-- UUID: 421535cf-d79d-4e2f-92fa-020d53bd1aff -->

The documents herein contain a Directory of all Instances on Solana of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.6.1.1.2.1.1 - Kamino [Core]  <!-- UUID: 50b33f03-fdb8-4b5b-8b75-3768b17759a9 -->

The Solana Instances Directory of the Kamino Protocol with `Active` Status are stored herein.

###### A.6.1.1.3.2.6.1.1.2.1.1.1 - Solana - Kamino USDS Instance Configuration Document Location [Core]  <!-- UUID: 874acdaa-1c84-47a5-aa08-ec87718e3c0d -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.1.1 - Solana - Kamino USDS Instance Configuration Document](fa6f6aa7-410e-4515-8458-9f3efb30c942)

###### A.6.1.1.3.2.6.1.1.2.1.1.2 - Solana - Kamino USDC Instance Configuration Document Location [Core]  <!-- UUID: 202b96d7-36d0-4b5b-b885-dfe314464d3d -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.1.2 - Solana - Kamino USDC Instance Configuration Document](2510c2ba-c304-478f-84b1-a421e62de8b4)

###### A.6.1.1.3.2.6.1.1.2.1.1.3 - Solana - Kamino USDT Instance Configuration Document Location [Core]  <!-- UUID: 4e40376a-59b3-4c2d-ab2b-9320b4f72e4e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.1.3 - Solana - Kamino USDT Instance Configuration Document](4adbf528-4a16-496c-974f-ce612af69162).

###### A.6.1.1.3.2.6.1.1.2.1.1.4 - Solana - Kamino USDG Instance Configuration Document Location [Core]  <!-- UUID: 09d70aa2-7082-42d0-b81b-2ec5065b49be -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.1.4 - Solana - Kamino USDG Instance Configuration Document](8b972495-2f93-4d88-b1f4-d447e2d821a3).

###### A.6.1.1.3.2.6.1.1.2.1.1.5 - Solana - Kamino PYUSD Instance Configuration Document Location [Core]  <!-- UUID: efde31d7-efae-463b-8c85-f104c284992d -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.1.5 - Solana - Kamino PYUSD Instance Configuration Document](dd6cf5ec-6ccd-46af-9c4e-0858f79948f7)

###### A.6.1.1.3.2.6.1.1.2.1.2 - Drift [Core]  <!-- UUID: e9748bec-bdee-440c-bde1-a2c7bb450a74 -->

The Solana Instances Directory of the Drift Protocol with `Active` Status are stored herein.

###### A.6.1.1.3.2.6.1.1.2.1.2.1 - Solana - Drift USDS Instance Configuration Document Location [Core]  <!-- UUID: 32707a35-c0a8-47b8-abb3-03022a5df11d -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.2.1 - Solana - Drift USDS Instance Configuration Document](5e934067-e691-4247-bfa1-7df9d4625f21).

###### A.6.1.1.3.2.6.1.1.2.1.2.2 - Solana - Drift USDC Instance Configuration Document Location [Core]  <!-- UUID: 8b23bd05-aa9a-4298-be16-03a2f8165a84 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.2.2 - Solana - Drift USDC Instance Configuration Document](ddf9f671-bf5c-4f21-af92-63cce7815af4).

###### A.6.1.1.3.2.6.1.1.2.1.2.3 - Solana - Drift USDT Instance Configuration Document Location [Core]  <!-- UUID: d720a25c-2e97-4b52-bdc4-3e1400789448 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.2.3 - Solana - Drift USDT Instance Configuration Document](300e6f12-800f-4f55-900b-a0697acfb257).

###### A.6.1.1.3.2.6.1.1.2.1.2.4 - Solana - Drift PYUSD Instance Configuration Document Location [Core]  <!-- UUID: 04889d34-faf3-4619-ad82-bd12a8c0e28e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.3.2.6.1.3.1.2.4 - Solana - Drift PYUSD Instance Configuration Document](ea272eb2-0ffd-4704-a02c-ee4f047cb8a3).

###### A.6.1.1.3.2.6.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: ca7557db-6f08-4352-a1b8-5d098ece70ec -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.6.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: c0753031-d528-4f41-affc-aed720bd018a -->

This document contains a Directory of all prospective Instances of the Allocation System Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to[A.6.1.1.3.2.6.1.1.2 - Active Instances Directory](134c14e9-28ed-4e18-b15a-26899644dc0b), whereas failed Invocations are Archived in [A.6.1.1.3.2.6.1.1.5 - Hub Data Repository](99be2bd2-c065-43b7-82f9-d51dfeeeaa58).

###### A.6.1.1.3.2.6.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 99be2bd2-c065-43b7-82f9-d51dfeeeaa58 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.6.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 3326fd03-88b1-4ab4-a0ab-24c8023d2c01 -->

The subtrees for archived Invocations and Instances of the Allocation System Primitive are stored here.

###### A.6.1.1.3.2.6.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: e080e3ed-c786-46bc-b68a-e46b6a752f17 -->

The subtrees for failed Invocations of the Allocation System Primitive are stored here.

###### A.6.1.1.3.2.6.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 7bf3b5c6-6cc5-46fe-b4a8-08b9a0108bec -->

The subtrees for Instances of the Allocation System Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.6.1.2 - Multi-Instance Coordinator Document [Core]  <!-- UUID: d4a7f9b4-7ee0-4f99-a9b9-eebe0219fa8c -->

The documents herein provide general specifications of the Keel Liquidity Layer and define Keel’s overarching strategy and operational framework for managing across all Instances.

###### A.6.1.1.3.2.6.1.2.1 - General Specifications [Core]  <!-- UUID: 5a1327e3-8c53-43d4-96b8-61483557e27d -->

The documents herein contain general specifications for the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.1.1 - Keel Liquidity Layer Architecture [Core]  <!-- UUID: 0ab7adfb-1f39-479a-b8a0-546410401bba -->

The documents herein describe the high-level design of the Keel Liquidity Layer, including its key smart contracts and their functionality.

###### A.6.1.1.3.2.6.1.2.1.1.1 - Keel Liquidity Layer Addresses [Core]  <!-- UUID: c65bd264-cb23-4587-add5-d3091a16613d -->

The subdocuments herein provide the addresses of the Keel Liquidity Layer’s constituent contracts.

###### A.6.1.1.3.2.6.1.2.1.1.1.1 - Allocator Contract Addresses [Core]  <!-- UUID: 54f36966-b656-4f51-9272-ac60fd90e1cc -->

The documents herein contain global key addresses for the Allocator Contracts.

###### A.6.1.1.3.2.6.1.2.1.1.1.1.1 - Ethereum Mainnet [Core]  <!-- UUID: 14887966-f73a-4abd-bd5e-51df5a7fe061 -->

The documents herein contain the Allocator Contract Addresses on the Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.1.1.1.1.1.1 - Allocator Buffer Contract [Core]  <!-- UUID: 7aa8974f-04fe-4e51-9452-c01296250068 -->

The address of the ALLOCATOR_BUFFER contract is: `0x065E5De3D3A08c9d14BF79Ce5A6d3D0E8794640c`

###### A.6.1.1.3.2.6.1.2.1.1.1.1.1.2 - Allocator Oracle Contract [Core]  <!-- UUID: 05259994-3a57-4249-82f4-f47eb881b5ee -->

The address of the ALLOCATOR_ORACLE contract is: `0xc7B91C401C02B73CBdF424dFaaa60950d5040dB7`

###### A.6.1.1.3.2.6.1.2.1.1.1.1.1.3 - Allocator Registry Contract [Core]  <!-- UUID: 2052c0df-8888-48cf-990c-735899d60a47 -->

The address of the ALLOCATOR_REGISTRY contract is: `0xCdCFA95343DA7821fdD01dc4d0AeDA958051bB3B`

###### A.6.1.1.3.2.6.1.2.1.1.1.1.1.4 - Allocator Roles Contract [Core]  <!-- UUID: 60f119c3-ba99-4370-8f77-f163374f73eb -->

The address of the ALLOCATOR_ROLES contract is: `0x9A865A710399cea85dbD9144b7a09C889e94E803`

###### A.6.1.1.3.2.6.1.2.1.1.1.1.1.5 - Allocator Vault (Nova) Contract [Core]  <!-- UUID: 7fd991d5-e2f4-4f8e-b4a6-13ab01509894 -->

The address of the ALLOCATOR_VAULT (ALLOCATOR Nova) contract is: `0xe4470DD3158F7A905cDeA07260551F72d4bB0e77`

###### A.6.1.1.3.2.6.1.2.1.1.1.2 - ALM Contracts [Core]  <!-- UUID: d655a727-9a7c-4f7d-84e1-dc26395983fe -->

The documents herein contain addresses for the ALM Contracts for the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.1.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: 0a39fe78-c262-495a-96fa-cb50077a0d53 -->

The documents herein contain the ALM Contract Addresses for the Keel Liquidity Layer on the Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.1.1.1.2.1.1 - ALM Controller Contract Address [Core]  <!-- UUID: 8ea07623-dc66-4e6b-8478-6fc3fadf049b -->

The address of the ALM_CONTROLLER (`MainnetController`) contract is: `0xEF26BDc34F35669C235345aeF24A251B1EE80EF3`

###### A.6.1.1.3.2.6.1.2.1.1.1.2.1.2 - ALM Controller Contract Version [Core]  <!-- UUID: b0980c40-fd44-492b-8435-b71fa0217819 -->

The ALM_CONTROLLER contract version is: `1.7.0`

###### A.6.1.1.3.2.6.1.2.1.1.1.2.1.3 - ALM Freezer Multisig Address [Core]  <!-- UUID: bd6847f1-093d-44a7-8971-98628de6fa8d -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.3.2.6.1.2.1.2.2.3 - Freezer Multisig](50ef16ee-1309-4172-befa-186529eb91c3).

###### A.6.1.1.3.2.6.1.2.1.1.1.2.1.4 - ALM Relayer Multisig Addresses [Core]  <!-- UUID: 9e280969-f099-4b67-8528-41f2248e634a -->

The addresses of the Multisigs that have the Relayer Role are specified in [A.6.1.1.3.2.6.1.2.1.2.2.1 - Prime Relayer Multisig](0bdf0649-1446-4ea7-b8dd-e41dc26b9be7) and [A.6.1.1.3.2.6.1.2.1.2.2.2 - Core Operator Relayer Multisig](b17a4a11-7340-4113-972d-76362f816b8a).

###### A.6.1.1.3.2.6.1.2.1.1.1.2.1.5 - ALM Proxy Contract [Core]  <!-- UUID: 796968ee-aa7b-40f2-acc8-a784eb41b21a -->

The address of the ALM_PROXY contract is: `0xa5139956eC99aE2e51eA39d0b57C42B6D8db0758`

###### A.6.1.1.3.2.6.1.2.1.1.1.2.1.6 - ALM Rate Limits Contract [Core]  <!-- UUID: 0a1eaef9-84e5-4ebe-a6b7-328349b5f310 -->

The address of the ALM_RATE_LIMITS contract is: `0x65E7B39e508944F7C4278d3e4580f84Eb20b26a7`

###### A.6.1.1.3.2.6.1.2.1.1.1.2.2 - Solana [Core]  <!-- UUID: 63dcc42b-87ba-43db-a9f6-4eb2b47ecb79 -->

The documents herein contain the ALM Program Addresses for the Keel Liquidity Layer on Solana.

###### A.6.1.1.3.2.6.1.2.1.1.1.2.2.1 - Solana ALM Controller Program [Core]  <!-- UUID: 286d26d1-4737-4c3a-9344-4a6d0cdefa93 -->

The address of the SOLANA_ALM_CONTROLLER (`SvmAlmController`) program is: `ALM1JSnEhc5PkNecbSZotgprBuJujL5objTbwGtpTgTd`.

###### A.6.1.1.3.2.6.1.2.1.1.1.2.2.2 - Solana ALM Controller State [Core]  <!-- UUID: 725952f6-ed88-4869-8105-c43de12bb9a5 -->

The address of the state instance configured for Keel is: `EeobZr57FSmNvw8Hs719iULJNqv3XLrTB5uPezvC2ND3`.

###### A.6.1.1.3.2.6.1.2.1.1.1.2.2.3 - Solana ALM Controller’s PDA [Core]  <!-- UUID: 844da5c2-cc3b-4bc2-8d2d-2ee9ee09f3a1 -->

The address of the instance’s PDA, configured for Keel is `EeWDutgcKNTdQGJkGRrWYmTXXuKnPUZNvXepbLkQrxW4`. This is the address that ‘owns’ any positions or tokens.

###### A.6.1.1.3.2.6.1.2.1.1.1.2.2.4 - Solana ALM Controller Contract Version [Core]  <!-- UUID: aec3b22f-5d75-4c27-b6f8-68babb1211ed -->

The ALM_CONTROLLER contract version is: `1.0.0`

###### A.6.1.1.3.2.6.1.2.1.1.1.2.2.5 - Solana ALM Controller’s USDC TokenAccount Address [Core]  <!-- UUID: 812bd84c-3826-4cda-9897-a6a50050494f -->

The Instance’s USDC TokenAccount Address is `4UA2CC9fQDTbX1SnJcanYn2QU5PtyB1MGfezDvGFPVwd`.

###### A.6.1.1.3.2.6.1.2.1.1.1.2.2.6 - ALM Freezer Multisig Address [Core]  <!-- UUID: d321eb55-3592-400a-970d-3ed194c57988 -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.3.2.6.1.2.1.2.3.4 - Freezer Multisig](aeee4280-ab46-4269-9430-fef8c2ee6d43).

###### A.6.1.1.3.2.6.1.2.1.1.1.2.2.7 - ALM Relayer Multisig Addresses [Core]  <!-- UUID: 21ec6877-82e9-4897-ac67-f23de2917a4b -->

The addresses of the Multisigs that have the Relayer Role are specified in [A.6.1.1.3.2.6.1.2.1.2.3.1 - Prime Primary Relayer Address](600dfd83-d3a1-4b26-a906-c412673855b9), [A.6.1.1.3.2.6.1.2.1.2.3.2 - Prime Secondary Relayer Address](3b538bc7-3d18-4091-908d-dc0c3a6e8a62) and [A.6.1.1.3.2.6.1.2.1.2.3.3 - Core Operator Relayer Multisig](ced26169-892b-4ec4-9a16-8fb90e94a9ef).

###### A.6.1.1.3.2.6.1.2.1.1.2 - Off-chain Operational Parameters [Core]  <!-- UUID: 6a9eed19-76e3-42c5-a3ac-2fda937600f4 -->

The documents herein list the off-chain operational parameters for the Keel Liquidity Layer. These operational parameters are protocol settings managed outside of smart contracts (off-chain), used by operators and off-chain systems to guide the functioning of the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.1.1.2.1 - Off-chain Operational Parameters For Ethereum Mainnet [Core]  <!-- UUID: 8477f75e-2800-4511-af34-dd25e590aa1f -->

The document herein lists the current off-chain operational parameters for the Keel Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.1.1.2.1.1 - Minimum Operation Size Ethereum Mainnet [Core]  <!-- UUID: 387e28bf-7748-416c-9a62-6696e131f975 -->

The minimum transaction size for operations on Ethereum Mainnet is (`MAINNET_MIN_OPERATION_SIZE`)

- This parameter will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.1.1.2.1.2 - Debt Ceiling Buffer Ethereum Mainnet [Core]  <!-- UUID: 6d4807f2-c6d0-4731-a315-3eb64397e4b0 -->

The buffer amount below the maximum debt ceiling is (`DEBT_CEILING_BUFFER`)

- This parameter will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.1.1.2.2 - Off-chain Operational Parameters For Solana [Core]  <!-- UUID: 297df822-cb2a-40ca-b42b-2f88f669122d -->

The document herein lists the current off-chain operational parameters for the Keel Liquidity Layer on Solana.

###### A.6.1.1.3.2.6.1.2.1.1.2.2.1 - Minimum Operation Size Solana [Core]  <!-- UUID: 68a562ac-e43d-4aa7-971e-b9c13d0465c7 -->

The minimum transaction size for operations on Solana is (`SOLANA_MIN_OPERATION_SIZE`)

- This parameter will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.1.1.3 - Rate Limits [Core]  <!-- UUID: bdbfe3ef-b848-4095-872d-66d189668fd3 -->

The documents herein list the Rate Limits for the Keel Liquidity Layer on each blockchain.

###### A.6.1.1.3.2.6.1.2.1.1.3.1 - Ethereum Mainnet [Core]  <!-- UUID: f783b89a-c2c7-4b78-91d3-08794358bb5f -->

The documents herein list the current `RateLimits` for the Keel Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.1.1.3.1.1 - Ethereum Mainnet USDS [Core]  <!-- UUID: 8c2ffb6e-0f1b-458d-9066-ee65b6099e87 -->

The maximum mint, burn and swap for USDS on Ethereum Mainnet are located herein.

###### A.6.1.1.3.2.6.1.2.1.1.3.1.1.1 - USDS Mint Maximum [Core]  <!-- UUID: 568f6fae-4680-4090-8eee-fe0b8e920155 -->

The maximum amount of USDS that can be minted within the Keel Liquidity Layer (`LIMIT_USDS_MINT`) is specified in the document herein.

- `maxAmount`: 10,000 USDS
- `slope`: 10,000 USDS per day

###### A.6.1.1.3.2.6.1.2.1.1.3.1.1.2 - USDS Burn Maximum [Core]  <!-- UUID: 308b6a69-7b8d-4631-a8c7-cfa2cd260ea4 -->

The maximum amount of USDS that can be burned within the Keel Liquidity Layer (`LIMIT_USDS_BURN`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.3.2.6.1.2.1.1.3.1.1.3 - USDS For USDC Swap Maximum [Core]  <!-- UUID: b5c9efe7-4240-4a29-bd4d-9dcb7bbe3840 -->

The maximum amount of USDS that can be swapped for USDC by the Keel Liquidity Layer in the Mainnet PSM (`LIMIT_USDS_TO_USDC`) is specified in the document herein.

- `maxAmount`: 100,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.3.2.6.1.2.1.1.3.1.1.4 - Maximum USDS Bridged From Ethereum Mainnet To Solana Via SkyLink [Core]  <!-- UUID: 5ee088fb-53b0-46f9-bf40-b59101cc2f24 -->

The maximum amount of USDS that can be sent to Keel’s Solana ALM Controller (`LIMIT_LAYERZERO_TRANSFER`, hashed with Solana USDS OFT address and Solana destination domain) is specified in the document herein.

- `maxAmount`: 100,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.3.2.6.1.2.1.1.3.1.2 - Ethereum Mainnet sUSDS [Core]  <!-- UUID: b593503f-ba6d-4f04-8fae-cf1971b55cbf -->

The maximum deposit and withdrawal amounts for sUSDS on Ethereum Mainnet are located herein.

###### A.6.1.1.3.2.6.1.2.1.1.3.1.2.1 - Ethereum Mainnet sUSDS Deposit Maximum [Core]  <!-- UUID: 28831fcf-2e28-4760-a4cd-27ae538edd9a -->

The maximum amount of sUSDS that can be deposited (`LIMIT_4626_DEPOSIT`) is specified in the document herein.

- `maxAmount`: 100,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.3.2.6.1.2.1.1.3.1.2.2 - Ethereum Mainnet sUSDS Withdrawal Maximum [Core]  <!-- UUID: 26dd35a7-0c0e-46e4-8717-84e974e27239 -->

The maximum amount of sUSDS that can be withdrawn (`LIMIT_4626_WITHDRAW`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: 0

###### A.6.1.1.3.2.6.1.2.1.1.3.1.3 - Ethereum Mainnet USDC [Core]  <!-- UUID: 6e47f3c2-1f5a-4d78-a74e-333e705a2257 -->

The maximum amount that can be transferred and sent to Keel’s Solana ALM Controller for USDC are located herein.

###### A.6.1.1.3.2.6.1.2.1.1.3.1.3.1 - Maximum USDC Bridged From Ethereum Mainnet To Solana Via Circle CCTP [Core]  <!-- UUID: cada0328-a57d-49c6-9d47-6e70400fc668 -->

The maximum amount of USDC that can be sent to Keel’s Solana ALM Controller (`LIMIT_USDC_TO_DOMAIN`, hashed with Solana domain) is specified in the document herein.

- `maxAmount`: 100,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.3.2.6.1.2.1.1.3.1.3.2 - Maximum USDC Bridged From Ethereum Mainnet Via Circle CCTP [Core]  <!-- UUID: 4d8f22cb-194c-4a92-8c2e-ea258d52986a -->

The maximum aggregate amount of USDC that can be bridged from Ethereum Mainnet to other domains using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP`) is specified in the document herein.

- `maxAmount`: 100,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2 - Solana [Core]  <!-- UUID: 2edb355c-541a-44e3-bcf0-87227fad560b -->

The documents herein list the current rate limits for the Keel Liquidity Layer on Solana.

###### A.6.1.1.3.2.6.1.2.1.1.3.2.1 - Solana USDS [Core]  <!-- UUID: a9868620-43c5-419a-a1ff-691d7618ab8c -->

The maximum mint, burn and swap for USDS on Solana are located herein

###### A.6.1.1.3.2.6.1.2.1.1.3.2.1.1 - USDS Reserve [Core]  <!-- UUID: d9e9085a-cc04-41b9-8708-fe41fc2ef0f3 -->

The maximum amount of USDS that can leave the USDS `Reserve` in aggregate across any integrations is specified in the document herein.

- `maxAmount`: 25,000,000 USDS
- `slope`: 10,000,000 USDS per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.1.2 - USDS For USDC Swap Maximum [Core]  <!-- UUID: 5f86844e-579b-425c-8f7b-e6521cfe55b9 -->

The maximum amount of USDS that can be swapped for USDC by the Keel Liquidity Layer on Solana is specified in the document herein.

- `maxAmount`: 100,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.1.3 - Maximum USDS Bridged From Solana To Ethereum Mainnet Via SkyLink [Core]  <!-- UUID: 3e48b867-07ff-4af7-a0d8-66e95b935a8f -->

The maximum amount of USDS that can be sent to Keel’s Ethereum Mainnet ALM Controller is specified in the document herein.

- `maxAmount`: 25,000,000 USDS
- `slope`: 10,000,000 USDS per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.2 - Solana USDC [Core]  <!-- UUID: 081d2895-b10a-44cf-871f-c2efc60d17ea -->

The maximum mint, burn and swap for USDC on Solana are located herein

###### A.6.1.1.3.2.6.1.2.1.1.3.2.2.1 - USDC Reserve [Core]  <!-- UUID: 7f7a3441-7bf4-46e7-9e03-5144d47091f5 -->

The maximum amount of USDC that can leave the USDC `Reserve` in aggregate across any integrations is specified in the document herein.

- `maxAmount`: 25,000,000 USDC
- `slope`: 10,000,000 USDC per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.2.2 - USDC For USDS Swap Maximum [Core]  <!-- UUID: 06081a43-075d-48c1-a26d-6578c1aa2fd3 -->

The maximum amount of USDC that can be swapped for USDC by the Keel Liquidity Layer on Solana is specified in the document herein.

- `maxAmount`: 25,000,000 USDC
- `slope`: 10,000,000 USDC per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.2.3 - USDC For USDT Swap Maximum [Core]  <!-- UUID: ed93fa5c-eb76-480d-9462-bd5d0af2bad2 -->

The maximum amount of USDC that can be swapped for USDT by the Keel Liquidity Layer on Solana is specified in the document herein.

- `maxAmount`: 25,000,000 USDC
- `slope`: 10,000,000 USDC per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.2.4 - USDC For USDG Swap Maximum [Core]  <!-- UUID: bb63cc13-3e51-43fa-becb-6b4a8e2df939 -->

The maximum amount of USDC that can be swapped for USDG by the Keel Liquidity Layer on Solana is specified in the document herein.

- `maxAmount`: 25,000,000 USDC
- `slope`: 10,000,000 USDC per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.2.5 - USDC For PYUSD Swap Maximum [Core]  <!-- UUID: 58cf4236-d399-45b9-b650-b1cc8392459e -->

The maximum amount of USDC that can be swapped for PYUSD by the Keel Liquidity Layer on Solana is specified in the document herein.

- `maxAmount`: 25,000,000 USDC
- `slope`: 10,000,000 USDC per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.2.6 - Maximum USDC Bridged From Solana To Ethereum Mainnet Via Circle CCTP [Core]  <!-- UUID: 3aeb4993-17b2-4959-ae81-d1518bb7d333 -->

The maximum amount of USDC that can be sent to Keel’s Ethereum Mainnet ALM Controller is specified in the document herein.

- `maxAmount`: 25,000,000 USDC
- `slope`: 10,000,000 USDC per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.3 - Solana USDT [Core]  <!-- UUID: 492f7297-f350-45d7-baca-88f1fb9f6b5c -->

The maximum mint, burn and swap for USDT on Solana are located herein

###### A.6.1.1.3.2.6.1.2.1.1.3.2.3.1 - USDT Reserve [Core]  <!-- UUID: ddfd7cfe-ebc0-413f-8060-f564a559b8fb -->

The maximum amount of USDT that can leave the USDT `Reserve` in aggregate across any integrations is specified in the document herein.

- `maxAmount`: 25,000,000 USDT
- `slope`: 10,000,000 USDT per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.3.2 - USDT For USDC Swap Maximum [Core]  <!-- UUID: 23c8500f-0866-4aa4-99a1-e9f513ad4fa8 -->

The maximum amount of USDT that can be swapped for USDC by the Keel Liquidity Layer on Solana is specified in the document herein.

- `maxAmount`: 25,000,000 USDT
- `slope`: 10,000,000 USDT per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.4 - Solana USDG [Core]  <!-- UUID: d37a9ed4-8945-4076-8e05-dd2319bcb033 -->

The maximum mint, burn and swap for USDG on Solana are located herein

###### A.6.1.1.3.2.6.1.2.1.1.3.2.4.1 - USDG Reserve [Core]  <!-- UUID: dfd32464-7a3b-454d-99e4-c1652cb57c5d -->

The maximum amount of USDG that can leave the USDG `Reserve` in aggregate across any integrations is specified in the document herein.

- `maxAmount`: 25,000,000 USDG
- `slope`: 10,000,000 USDG per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.4.2 - USDG For USDC Swap Maximum [Core]  <!-- UUID: e6ab3642-13a1-40bc-9f95-ba68b25a7b89 -->

The maximum amount of USDG that can be swapped for USDC by the Keel Liquidity Layer on Solana is specified in the document herein.

- `maxAmount`: 25,000,000 USDG
- `slope`: 10,000,000 USDG per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.5 - Solana PYUSD [Core]  <!-- UUID: eff69ee3-46bb-44c5-b7e2-df7cc9848618 -->

The maximum mint, burn and swap for PYUSD on Solana are located herein

###### A.6.1.1.3.2.6.1.2.1.1.3.2.5.1 - PYUSD Reserve [Core]  <!-- UUID: 2037a597-0dd7-4887-ab21-e4a6ff103af0 -->

The maximum amount of PYUSD that can leave the PYUSD `Reserve` in aggregate across any integrations is specified in the document herein.

- `maxAmount`: 25,000,000 PYUSD
- `slope`: 10,000,000 PYUSD per day

###### A.6.1.1.3.2.6.1.2.1.1.3.2.5.2 - PYUSD For USDC Swap Maximum [Core]  <!-- UUID: 9e4ef1e5-95fd-4052-ab4d-778806a4e27a -->

The maximum amount of PYUSD that can be swapped for USDC by the Keel Liquidity Layer on Solana is specified in the document herein.

- `maxAmount`: 25,000,000 PYUSD
- `slope`: 10,000,000 PYUSD per day

###### A.6.1.1.3.2.6.1.2.1.1.4 - On-chain Parameters [Core]  <!-- UUID: 09f65586-bd5d-47fc-847b-3f3c087c6b62 -->

The documents herein list general on-chain parameters for the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.1.1.4.1 - Allocator Vault Parameters [Core]  <!-- UUID: 6952b3d2-7b66-46ba-90f7-700f244c5ee0 -->

The Allocator Vault parameters for ALLOCATOR-NOVA-A are defined in [A.3.7.1.2.1.4 - ALLOCATOR-NOVA-A Parameters](08321783-f31a-4a80-8f0c-898afb4d8f9b).

###### A.6.1.1.3.2.6.1.2.1.1.4.2 - Whitelisting Of ALMProxy [Core]  <!-- UUID: 810671ff-8674-4178-a7ce-dd98c112688d -->

The ALMProxy for Keel is whitelisted on the LitePSM. This allows Keel to call `buyGemNoFee` and `sellGemNoFee` on the `MCD_LITE_PSM_USDC_A` contract.

###### A.6.1.1.3.2.6.1.2.1.1.4.3 - Whitelisting of Keel SubProxy Cross‑Chain Messaging [Core]  <!-- UUID: b319a7e6-d484-44e7-b622-6df9754c5973 -->

Keel’s SubProxy must be authorized by the Pause Proxy contract to send cross‑chain messages on Solana.

###### A.6.1.1.3.2.6.1.2.1.2 - Governance Processes [Core]  <!-- UUID: 21742792-9418-4857-a143-664f9d7d44d9 -->

The documents herein describe the specific governance processes for the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.1.2.1 - Invoking New Instances [Core]  <!-- UUID: ca0026a1-a4d2-4ebd-a99a-0a089dea8c82 -->

The governance process to invoke a new Instance of the Allocation System Primitive follows the Root Edit process see [A.6.1.1.3.2.2.2.2.1.2 - Operational Process Definition](53987e91-b86c-42be-bb4b-20af084d622d).

###### A.6.1.1.3.2.6.1.2.1.2.2 - Ethereum Multisigs [Core]  <!-- UUID: fcdf3c3c-fc8e-4bcc-af84-4aae709d5411 -->

The documents herein define multisigs that have privileged access to manage the Keel Liquidity Layer on Ethereum.

###### A.6.1.1.3.2.6.1.2.1.2.2.1 - Prime Relayer Multisig [Core]  <!-- UUID: 0bdf0649-1446-4ea7-b8dd-e41dc26b9be7 -->

The Prime Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.3.2.6.1.2.2.1.1.1.2 - Relayer Role](1b64d5b8-ea7d-408e-a409-3e9e72989396) and is controlled by Keel.

###### A.6.1.1.3.2.6.1.2.1.2.2.1.1 - Address [Core]  <!-- UUID: 76265560-4bc8-42fd-b5d7-85be52e11648 -->

The address of the Prime Relayer Multisig on the Ethereum Mainnet is `0xA4F39dAae4Dc86c27c46b9a0605AE2c911451F95`.

###### A.6.1.1.3.2.6.1.2.1.2.2.1.2 - Required Number Of Signers [Core]  <!-- UUID: 90059aef-0d59-4174-9076-e894ce9cf730 -->

The Prime Relayer Multisig currently has a 1/2 signing requirement.

###### A.6.1.1.3.2.6.1.2.1.2.2.1.3 - Signers [Core]  <!-- UUID: 10d25644-72b7-406e-ac02-97a6cc31322d -->

The signers of the Prime Relayer Multisig are two (2) addresses controlled by Keel.

###### A.6.1.1.3.2.6.1.2.1.2.2.1.4 - Usage Standards [Core]  <!-- UUID: c0928c5e-9679-4e4c-929e-865a15007006 -->

The signers of the Prime Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.1.2.2.1.5 - Modification [Core]  <!-- UUID: 8e1357dc-80a7-4716-becf-9a50ef7ae3a0 -->

Keel can change the signers of the Prime Relayer Multisig at any time, so long as there are at least two (2) signers and at least a majority of signers are required to execute transactions.

###### A.6.1.1.3.2.6.1.2.1.2.2.2 - Core Operator Relayer Multisig [Core]  <!-- UUID: b17a4a11-7340-4113-972d-76362f816b8a -->

The Core Operator Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.3.2.6.1.2.2.1.1.1.2 - Relayer Role](1b64d5b8-ea7d-408e-a409-3e9e72989396) and is controlled by Operational GovOps Soter Labs.

###### A.6.1.1.3.2.6.1.2.1.2.2.2.1 - Address [Core]  <!-- UUID: 8028f164-6410-4f0a-bbba-dc175fc77f58 -->

The address of the Core Operator Relayer Multisig on the Ethereum Mainnet is `0x0f72935f6de6C54Ce8056FD040d4Ddb012B7cd54`.

###### A.6.1.1.3.2.6.1.2.1.2.2.2.2 - Required Number Of Signers [Core]  <!-- UUID: e92ff3c5-581b-4d5e-bab4-e244348991e4 -->

The Core Operator Relayer Multisig currently has a 2/3 signing requirement.

###### A.6.1.1.3.2.6.1.2.1.2.2.2.3 - Signers [Core]  <!-- UUID: 17a98019-f677-471b-aebd-7885108c614b -->

The signers of the Core Operator Relayer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs.

###### A.6.1.1.3.2.6.1.2.1.2.2.2.4 - Usage Standards [Core]  <!-- UUID: 6c744f15-9dc2-47a6-b1f5-33e534697baf -->

The signers of the Core Operator Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.1.2.2.2.5 - Modification [Core]  <!-- UUID: f9bf39ea-a02f-4eac-bd81-7c0b4daeb970 -->

Operational GovOps Soter Labs can change the signers of the Core Operator Relayer Multisig at any time, so long as there are at least three (3) signers and at least two-thirds of signers are required to execute transactions.

###### A.6.1.1.3.2.6.1.2.1.2.2.3 - Freezer Multisig [Core]  <!-- UUID: 50ef16ee-1309-4172-befa-186529eb91c3 -->

The Freezer Multisig has the `FREEZER_ROLE` as defined in [A.6.1.1.3.2.6.1.2.2.1.1.1.4 - Freezer Role](45b602fb-9427-4555-a3f7-8ad5b17a1cf2).

###### A.6.1.1.3.2.6.1.2.1.2.2.3.1 - Address [Core]  <!-- UUID: 5a0b849f-fbfc-4a4d-88f2-d639924548bf -->

The address of the Freezer Multisig on the Ethereum Mainnet is `0xBCCB60cf518391d3315D63313F7bb764d02541fE`.

###### A.6.1.1.3.2.6.1.2.1.2.2.3.2 - Required Number Of Signers [Core]  <!-- UUID: 354e8b0c-4883-4ae9-9d18-b95fcfe56b3c -->

The Freezer Multisig currently has a 2/5 signing requirement.

###### A.6.1.1.3.2.6.1.2.1.2.2.3.3 - Signers [Core]  <!-- UUID: 81708b61-3321-42f2-af55-204c56b32eb3 -->

The signers of the Freezer Multisig are two (2) addresses controlled by Operational GovOps Soter Labs, two (2) addresses controlled by Operational Facilitator Endgame Edge, and one (1) address controlled by Keel.

###### A.6.1.1.3.2.6.1.2.1.2.2.3.4 - Usage Standards [Core]  <!-- UUID: b375c2b6-b52d-42cf-bfd3-01e46af44248 -->

The signers of the Freezer Multisig should exercise their authority to freeze the Keel Liquidity Layer in the event that Keel is not complying with rules regarding Risk Capital or Asset Liability Management, or in the event of another emergency.

Each action executed by the Freezer Multisig, including any function calls and their parameters, must be reported to the Sky community within a reasonable time frame through a post on the Sky Forum.

###### A.6.1.1.3.2.6.1.2.1.2.2.3.5 - Modification [Core]  <!-- UUID: d9ec1326-2e1c-45a9-918e-bbedfa5235c8 -->

Modification of the signers of the Freezer Multisig must be approved through an Atlas Edit Proposal.

The only exceptions to this are if: 1) a signer self-reports a loss of access to their private key due to any reason; or 2) a signer explicitly expresses their wish to be removed as a signer. In both cases, the signer is required to communicate the loss of access to their private key, or the wish to be removed as a signer, in the form of a public Sky Forum post. The specific signer should be replaced as soon as possible.

Any changes to the Multisig signers that do not fall within the two exceptions listed above, or that have not been ratified by Sky Governance, should be questioned immediately and treated as malicious. Where malicious activity is suspected, the Core Facilitator must prepare an expedited Executive Vote so that Sky Governance can vote on removing external security access from the Multisig.

###### A.6.1.1.3.2.6.1.2.1.2.3 - Solana Multisigs And Addresses [Core]  <!-- UUID: 5c25417a-8698-47f4-821c-06e51e6447b6 -->

The documents herein define multisigs and addresses that have privileged access to manage the Keel Liquidity Layer on Solana.

###### A.6.1.1.3.2.6.1.2.1.2.3.1 - Prime Primary Relayer Address [Core]  <!-- UUID: 600dfd83-d3a1-4b26-a906-c412673855b9 -->

The Prime Primary Relayer Address holds a [A.6.1.1.3.2.6.1.2.2.2.1.1.2 - Relayer Role](2b42015c-c76a-4364-b8b5-c9a2b9f6f484) and is controlled by Keel.

###### A.6.1.1.3.2.6.1.2.1.2.3.1.1 - Address [Core]  <!-- UUID: e4c22be8-bae8-45a3-9fe6-84d007282786 -->

The address of the Prime Primary Relayer is `99J5Vcf3tav2dorWmB1qxdXtD4MKk6pyayQwS8RCXZKc`.

###### A.6.1.1.3.2.6.1.2.1.2.3.1.2 - State Address [Core]  <!-- UUID: b9643943-7dac-4ba6-bd47-56d907ed802e -->

The address of the Prime Primary Relayer’s permission configurations is `2MeJkkKPfHs6qJgTKZJGnrpq8jBRsvty6zB5iA8SkoVU`.

###### A.6.1.1.3.2.6.1.2.1.2.3.1.3 - Signer [Core]  <!-- UUID: 19f801cf-4014-4ebc-8512-5e0b7efc544d -->

The signer of the Prime Relayer Address is controlled by Keel.

###### A.6.1.1.3.2.6.1.2.1.2.3.1.4 - Usage Standards [Core]  <!-- UUID: d5bbbab6-ab49-4b45-90c8-31c2bbce5e65 -->

The signers of the Prime Relayer Address must use it to exercise the[A.6.1.1.3.2.6.1.2.2.2.1.1.2 - Relayer Role](2b42015c-c76a-4364-b8b5-c9a2b9f6f484) in accordance with the instructions specified in the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.1.2.3.1.5 - Modification [Core]  <!-- UUID: e7492c8c-10b6-4ee1-9d62-fb3c292f1308 -->

Changes to the Prime Relayer Addresses is a controller action which must be invoked by a [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367).

###### A.6.1.1.3.2.6.1.2.1.2.3.2 - Prime Secondary Relayer Address [Core]  <!-- UUID: 3b538bc7-3d18-4091-908d-dc0c3a6e8a62 -->

The Prime Secondary Relayer Address holds a [A.6.1.1.3.2.6.1.2.2.2.1.1.2 - Relayer Role](2b42015c-c76a-4364-b8b5-c9a2b9f6f484) and is controlled by Keel.

###### A.6.1.1.3.2.6.1.2.1.2.3.2.1 - Address [Core]  <!-- UUID: 0cacb86a-aaaa-4857-b1d5-b4ac69bf5111 -->

The address of the Prime Secondary Relayer is `2gDBGyhU8M96JDMWzCfiGb3Pw2HvrEvdL5MkfwosBYnh`.

###### A.6.1.1.3.2.6.1.2.1.2.3.2.2 - State Address [Core]  <!-- UUID: 03cabe40-5ddf-47ef-9cf2-d2f33e8c39a1 -->

The address of the Prime Secondary Relayer’s permission configurations is `6TdcW3qX25JcN9nMgSkFka5wXTXBFhb5J2tVRdG3pw3w`.

###### A.6.1.1.3.2.6.1.2.1.2.3.2.3 - Signer [Core]  <!-- UUID: 35c732d2-113a-4b05-bbd1-866938c01470 -->

The signer of the Prime Relayer Address is controlled by Keel.

###### A.6.1.1.3.2.6.1.2.1.2.3.2.4 - Usage Standards [Core]  <!-- UUID: 3ca26d03-bb4d-4fe0-8f3f-3f9e6d92e2ed -->

The signers of the Prime Relayer Address must use it to exercise the [A.6.1.1.3.2.6.1.2.2.2.1.1.2 - Relayer Role](2b42015c-c76a-4364-b8b5-c9a2b9f6f484) in accordance with the instructions specified in the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.1.2.3.2.5 - Modification [Core]  <!-- UUID: e471ce78-e775-4aff-a331-7e581a4606e6 -->

Changes to the Prime Relayer Addresses is a controller action which must be invoked by a [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367).

###### A.6.1.1.3.2.6.1.2.1.2.3.3 - Core Operator Relayer Multisig [Core]  <!-- UUID: ced26169-892b-4ec4-9a16-8fb90e94a9ef -->

The Core Operator Relayer Multisig holds a [A.6.1.1.3.2.6.1.2.2.2.1.1.2 - Relayer Role](2b42015c-c76a-4364-b8b5-c9a2b9f6f484) and is controlled by Operational GovOps Soter Labs.

###### A.6.1.1.3.2.6.1.2.1.2.3.3.1 - Address [Core]  <!-- UUID: f027ec03-4e5a-4262-9992-07fab72dc014 -->

The address of the Core Operator Relayer Multisig on Solana is `7JvfSy4mWcw1EAy7vjvsHnKeC28UZeAURhVi4nQjUM6h`.

###### A.6.1.1.3.2.6.1.2.1.2.3.3.2 - State Address [Core]  <!-- UUID: 310849fb-a67d-4e9a-aadb-8c39ff2a8b8e -->

The address of the Core Operator Relayer’s permission configurations is `2YLLgUuWHwf8hFnWXWUL9V5Vk68yBswVtJED1h4vnPjX`.

###### A.6.1.1.3.2.6.1.2.1.2.3.3.3 - Required Number Of Signers [Core]  <!-- UUID: e8868f7c-3033-4355-9f87-81956961bedb -->

The Core Operator Relayer Multisig currently has a 2/3 signing requirement.

###### A.6.1.1.3.2.6.1.2.1.2.3.3.4 - Signers [Core]  <!-- UUID: 08036115-62a3-40c8-9b70-61f8dc38035c -->

The signers of the Core Operator Relayer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs.

###### A.6.1.1.3.2.6.1.2.1.2.3.3.5 - Usage Standards [Core]  <!-- UUID: f2730835-93da-4616-989d-a38f1bd6416a -->

The signers of the Core Operator Relayer Multisig must use the Multisig to exercise the Relayer Role in accordance with the instructions specified in the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.1.2.3.3.6 - Modification [Core]  <!-- UUID: 2cf82458-eae4-4fad-9504-0fee8effd172 -->

Operational GovOps Soter Labs can change the signers of the Core Operator Relayer Multisig at any time, so long as there are at least three (3) signers and at least two thirds of signers are required to execute transactions.

###### A.6.1.1.3.2.6.1.2.1.2.3.4 - Freezer Multisig [Core]  <!-- UUID: aeee4280-ab46-4269-9430-fef8c2ee6d43 -->

The Freezer Multisig has the `FREEZER_ROLE` as defined in [A.6.1.1.3.2.6.1.2.2.2.1.1.3 - Freezer Role](6f7becc7-2e70-44e5-8662-25ba7dd1a5f8).

###### A.6.1.1.3.2.6.1.2.1.2.3.4.1 - Address [Core]  <!-- UUID: b76dbc30-602e-4464-b797-8b6643d8e2b8 -->

The address of the Freezer Multisig on Solana is `AUAJeXgLDNoDbBZ1uRguj9hWDZJSQkmoy4xk9U5zJF8h`.

###### A.6.1.1.3.2.6.1.2.1.2.3.4.2 - State Address [Core]  <!-- UUID: f9d1c2bc-5903-4581-9b0d-9c68f7c64ac8 -->

The address of the Freezer Multisig permission configurations is `B24DtbKAV25fcZ6e3buqfB8CSuuiFLRsHHojBGigntff`.

###### A.6.1.1.3.2.6.1.2.1.2.3.4.3 - Required Number Of Signers [Core]  <!-- UUID: c900500f-d44a-4c6f-9429-032a28262b68 -->

The Freezer Multisig currently has a 2/5 signing requirement.

###### A.6.1.1.3.2.6.1.2.1.2.3.4.4 - Signers [Core]  <!-- UUID: e6c86321-bef0-435c-a2db-2b82dc7f1c77 -->

The signers of the Freezer Multisig are two (2) addresses controlled by Operational GovOps Soter Labs, two (2) addresses controlled by Operational Facilitator Endgame Edge, and one (1) address controlled by Keel.

###### A.6.1.1.3.2.6.1.2.1.2.3.4.5 - Usage Standards [Core]  <!-- UUID: 9a900853-f703-4454-92bf-416fbb157aea -->

The signers of the Freezer Multisig should exercise their authority to freeze the Keel Liquidity Layer in the event that Keel is not complying with rules regarding Risk Capital or Asset Liability Management, or in the event of another emergency.

Each action executed by the Freezer Multisig, including any function calls and their parameters, must be reported to the Sky community within a reasonable time frame through a post on the Sky Forum.

###### A.6.1.1.3.2.6.1.2.1.2.3.4.6 - Modification [Core]  <!-- UUID: 6369ddc9-8898-40b3-b454-c324c75d7d39 -->

Modification of the signers of the Freezer Multisig must be approved through an Atlas Edit Proposal.

The only exceptions to this are if: 1) a signer self-reports a loss of access to their private key due to any reason; or 2) a signer explicitly expresses their wish to be removed as a signer. In both cases, the signer is required to communicate the loss of access to their private key, or the wish to be removed as a signer, in the form of a public Sky Forum post. The specific signer should be replaced as soon as possible.

Any changes to the Multisig signers that do not fall within the two exceptions listed above, or that have not been ratified by Sky Governance, should be questioned immediately and treated as malicious. Where malicious activity is suspected, the Core Facilitator must prepare an expedited Executive Vote so that Sky Governance can vote on removing external security access from the Multisig.

###### A.6.1.1.3.2.6.1.2.1.3 - Total Risk Capital (TRC) Management [Core]  <!-- UUID: 921ca242-451a-4013-90b4-611696fb1a41 -->

The documents herein specify requirements related to Keel’s Total Risk Capital (TRC) management.

###### A.6.1.1.3.2.6.1.2.1.3.1 - Keel’s Operation Of Keel Liquidity Layer And Agreement Regarding Encumbrance Ratio [Core]  <!-- UUID: e6b81e35-8a04-4d66-ac37-80b0a91d553b -->

Keel will operate the Keel Liquidity Layer and agrees to stay at or below a 90% Encumbrance Ratio. See[A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9).

###### A.6.1.1.3.2.6.1.2.1.3.2 - Keel’s Total Risk Capital (TRC) Management Processes [Core]  <!-- UUID: afdffc09-3a0f-450f-beb8-e4a5107b434c -->

As operators of the Keel Liquidity Layer, Keel automatically inherits, and is subject to, the base class of operational requirements related to Total Risk Capital management defined in [A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capital (TRC) Management](3af8a3a2-25e5-44b3-87a4-7df1f2712685). Modifications to the base operational logic automatically propagate to the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.2 - Keel Liquidity Layer Operational Processes [Core]  <!-- UUID: 44a6cfcc-26d3-414b-99a7-cf57d2b6c5d6 -->

The documents herein describe common operational procedures for the Keel Liquidity Layer applicable across multiple Instances.

###### A.6.1.1.3.2.6.1.2.2.1 - Ethereum Mainnet [Core]  <!-- UUID: d0dd4281-e342-43d9-9aa7-41d42ee6279d -->

The documents herein describe common operational procedures for the Keel Liquidity Layer applicable across multiple Instances on Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.2.1.1 - Routine Protocol [Core]  <!-- UUID: 0a382c05-5a2b-43a5-83ac-94032e065094 -->

The documents herein define the protocol for routine ongoing management of the Keel Liquidity Layer and its active Instances on Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.2.1.1.1 - Role Hierarchy And Permissions [Core]  <!-- UUID: 70617021-ff70-4a9b-97aa-56be5ec2038d -->

The documents herein define roles (Admin, Relayer, ALM Controller and Freezer) and their responsibilities/permissions for managing the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.2.1.1.1.1 - Default Admin Role [Core]  <!-- UUID: 26cac5a1-6313-4aff-952c-70eb84513815 -->

The admin role (`DEFAULT_ADMIN_ROLE`) is the role that can grant and revoke any role, including itself and all other roles defined in the contract. The admin role is also used for general admin functions in all contracts. This role is fully controlled by Sky Governance via the Keel Proxy.

`constructor(address admin) {
_grantRole(DEFAULT_ADMIN_ROLE, admin);`

###### A.6.1.1.3.2.6.1.2.2.1.1.1.2 - Relayer Role [Core]  <!-- UUID: 1b64d5b8-ea7d-408e-a409-3e9e72989396 -->

The `RELAYER_ROLE` is the address for the Keel Liquidity Layer ALM Planner off-chain system that calls functions on `Controller` contracts to perform actions on behalf of the `ALMProxy` contract. The Relayer Role may be granted to an address by any address holding the `DEFAULT_ADMIN_ROLE`. The Relayer Role may be removed from an address by any address holding the `DEFAULT_ADMIN_ROLE` or the `FREEZER_ROLE`.

###### A.6.1.1.3.2.6.1.2.2.1.1.1.3 - ALM Controller Role [Core]  <!-- UUID: 6ebd37e7-5234-4ac6-a48b-b75e86f29e82 -->

The `ALM_CONTROLLER_ROLE` is the address of the role that can call the `call` functions on the `ALMProxy` contract and update `RateLimits` contract. It includes the `MainnetController` and `ForeignController` contracts. ALM Controller contracts are accessed and modified via the Relayer Role.

###### A.6.1.1.3.2.6.1.2.2.1.1.1.4 - Freezer Role [Core]  <!-- UUID: 45b602fb-9427-4555-a3f7-8ad5b17a1cf2 -->

The `FREEZER_ROLE` is the address of the emergency role that can remove a compromised Relayer.

###### A.6.1.1.3.2.6.1.2.2.1.1.2 - Controller Functions [Core]  <!-- UUID: 777db288-7558-4e07-b649-fbf15c7ab202 -->

The documents herein describe the purpose and operational use of key functions within Keel Liquidity Layer `MainnetController` contracts: USDS management (mint/burn USDS), Asset Transfer Management (direct transfers, protocol deposits/withdrawals), Cross-chain Operations (CCTP bridging)

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1 - Mainnet Controller Contract Functions [Core]  <!-- UUID: 93b5cec4-1398-4adf-a14f-3c8fb5281cc9 -->

The documents herein define the functions controlled by the Controller contract for Keel Liquidity Layer operations on Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.1 - Admin Functions [Core]  <!-- UUID: 91ed43a8-98d6-4954-8d4d-a79e49d17cbe -->

The documents herein define the operations performed by the admin role (see [A.6.1.1.3.2.6.1.2.2.1.1.1.1 - Default Admin Role](26cac5a1-6313-4aff-952c-70eb84513815)) within the `MainnetController` contract.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.1.1 - Set Mint Recipient For Destination Domain [Core]  <!-- UUID: d54329a6-eeaa-4741-9518-d7d24e2d418c -->

The documents herein define the steps for an admin to specify which address should receive newly minted tokens on a particular destination domain.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.1.1.1 - Call setMintRecipient Function [Core]  <!-- UUID: 0d2d22cf-1ee4-44ee-8e10-95f516da51a9 -->

Only an operator with the admin role is able to set the mint recipient for a destination domain. To do so, they must call the `setMintRecipient` function on the Controller contract on mainnet providing the destination domain and the mint recipient address. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role the transaction will revert.
- The contract will set the selected mint recipient for the specified destination domain.
- The contract will emit a `MintRecipientSet` event to the blockchain logs.

The function call is as follows:

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.1.2 - Set LayerZero Recipient [Core]  <!-- UUID: 753bcc77-e4a6-438b-942c-bf2b4ef908be -->

The documents herein define the steps for an admin to specify which address should receive LayerZero messages on a particular destination endpoint.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.1.2.1 - Call setLayerZeroRecipient Function [Core]  <!-- UUID: aceb66dc-7349-4d49-a893-7ed417e83797 -->

Only an operator with the admin role is able to set the LayerZero recipient for a destination endpoint. To do so, they must call the `setLayerZeroRecipient` function on the Controller contract on mainnet, providing the destination endpoint ID and the recipient address. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the selected LayerZero recipient for the specified destination endpoint.
- The contract will emit a `LayerZeroRecipientSet` event to the blockchain logs.

The function call is as follows:

`function setLayerZeroRecipient(uint32 destinationEndpointId, bytes32 layerZeroRecipient) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.1.3 - Set Maximum Slippage [Core]  <!-- UUID: 323bb906-f37c-470d-8124-b133a050ffa6 -->

The documents herein define the steps for an admin to set the maximum allowed slippage for a specific pool.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.1.3.1 - Set The Maximum Slippage Function [Core]  <!-- UUID: 8838da61-5edf-4ad5-b910-d4536aecd822 -->

Only an operator with the admin role is able to set the maximum slippage for a pool. To do so, they must call the `setMaxSlippage` function on the Controller contract on mainnet, providing the pool address and the maximum slippage value. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the maximum slippage for the specified pool.
- The contract will emit a `MaxSlippageSet` event to the blockchain logs.

The function call is as follows:

`function setMaxSlippage(address pool, uint256 maxSlippage) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2 - Relayer Functions [Core]  <!-- UUID: 0a7927fb-3301-423a-9b8f-6eff2c995dd0 -->

The documents herein define the operations performed by the relayer role (see [A.6.1.1.3.2.6.1.2.2.1.1.1.2 - Relayer Role](1b64d5b8-ea7d-408e-a409-3e9e72989396)) within the `MainnetController` contract.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1 - Relayer Vault Functions [Core]  <!-- UUID: 1a335368-4c05-49b1-b5fb-e0a9c572b28c -->

The documents herein define the operations that are performed to maintain the desired level of liquidity and debt balance of the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1.1 - Mint USDS [Core]  <!-- UUID: 6090ffba-788d-465c-b5d9-34e710745647 -->

The documents herein define the steps for a relayer to mint USDS from the Sky Allocation Vault to the Keel ALM Proxy.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1.1.1 - Call mintUSDS Function [Core]  <!-- UUID: 768ca90b-8432-456c-8f75-2469514d6969 -->

Only an operator with the relayer role is able to mint USDS. To do so, they must call the mintUSDS function on the Controller contract on mainnet with the amount of USDS that is required for minting. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will ensure the `RateLimits` allow for minting the required amount. If the mint amount does not fall within the available Rate Limit the transaction will revert.
- The contract will reduce the Rate Limit by the amount of USDS minted in this transaction.
- The contract will mint the required USDS into the buffer contract.
- The contract will transfer the newly minted USDS from the buffer to the Proxy.

The function call is as follows:

`function mintUSDS(uint256 usdsAmount) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1.2 - Burn USDS [Core]  <!-- UUID: 9c9536a8-bb2d-4d37-98cf-4c25a5699026 -->

The documents herein define the steps for a relayer to return and then burn Keel’s USDS debt in the Sky Allocation Vault.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1.2.1 - Call burnUSDS Function [Core]  <!-- UUID: 59b093a0-9025-4c60-ba6f-7a2e78a35ed4 -->

Only an operator with the relayer role is able to repay vault debt and burn USDS. To do so, they must call the burnUSDS function of the Controller contract on mainnet with the amount of USDS that they wish to burn. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will increase the available Rate Limit for minting USDS by the amount of USDS being burned. This increase will be limited by the maxAmount parameter in the `Rate Limit` contract.
- The contract will transfer USDS from the proxy to the buffer.
- The contract will burn the USDS from the buffer and `wipe` an equivalent amount from the vault's debt.

The function call is as follows:

`function burnUSDS(uint256 usdsAmount) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.2 - ERC-20 Functions [Core]  <!-- UUID: 7f8d8294-d5d6-437e-aae1-a1ee36c11e7e -->

The documents herein define the operations that are performed to transfer ERC-20 assets to specified destinations.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.2.1 - Transfer Asset [Core]  <!-- UUID: 0a409cf8-a66d-4fd4-beaf-ca518eaa77c1 -->

The documents herein define the steps for a relayer to transfer ERC-20 tokens to a destination address.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.2.1.1 - Call transferAsset Function [Core]  <!-- UUID: fa55c1fb-83b5-4f73-a7a4-116d2c7814dd -->

Only an operator with the relayer role is able to transfer ERC-20 assets. To do so, they must call the `transferAsset` function on the Controller contract on mainnet, providing the ERC20 asset address, the destination address, and the amount to transfer. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will ensure the `RateLimits` allow for transferring the specified amount of the asset to the destination. If the transfer amount does not fall within the available Rate Limit, the transaction will revert.
- The contract will execute the ERC-20 `transfer` function, sending the specified amount of the asset to the destination address.

The function call is as follows:

`function transferAsset(address asset, address destination, uint256 amount) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3 - ERC-4626 Functions [Core]  <!-- UUID: 3de32801-e895-4a21-84da-aa5818d16349 -->

The documents herein define the general Keel Liquidity Layer operational procedures for interacting with ERC-4626-compliant tokenized vaults. ERC-4626 is a standard interface for vaults representing shares of an underlying ERC-20 token. Keel Liquidity Layer can integrate with various ERC-4626 vaults. For instance-specific parameters (such as vault addresses, asset addresses, and rate limits), refer to the relevant ERC-4626 Instance Configuration Document.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.1 - Deposit To ERC-4626 Vault [Core]  <!-- UUID: a01273a3-0fc3-44ce-931a-cdc3d3983a73 -->

The documents herein define the steps for a relayer to deposit assets from the ALM Proxy to an ERC-4626 vault to receive yield-bearing shares.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.1.1 - Call depositERC4626 Function [Core]  <!-- UUID: 4e2c13af-7f66-4b87-9662-693e94212c28 -->

Only an operator with the relayer role can deposit assets into an ERC-4626 vault. To do so, they must call the `depositERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to deposit. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for deposit; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the deposit amount is within the allowed rate limit for the specified vault.
- The contract will approve the vault to spend the underlying asset from the ALM Proxy. The approval and deposit are both performed from the ALM Proxy address.
- The contract will deposit the specified amount into the vault, and the ALM Proxy will receive the corresponding number of vault shares.

The function call is as follows:

`function depositERC4626(address token, uint256 amount) external returns (uint256 shares)`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.2 - Withdraw From ERC-4626 Vault [Core]  <!-- UUID: ad2c7a22-96aa-428d-a373-b92fec3b529f -->

The documents herein define the steps for a relayer to withdraw a specified amount of the underlying asset from an ERC-4626 vault to the ALM Proxy.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.2.1 - Call withdrawERC4626 Function [Core]  <!-- UUID: 37c09b7c-6aa0-4c3c-861e-984de4e3ba4d -->

Only an operator with the relayer role can withdraw assets from an ERC-4626 vault. To do so, call the `withdrawERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to withdraw. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for withdrawal; otherwise, the transaction will revert. When this function is called:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the withdrawal amount is within the allowed rate limit for the specified vault.
- The contract will withdraw the specified amount from the vault, burning the necessary number of vault shares held by the ALM Proxy as part of the withdrawal process.
- The withdrawn assets will be sent to the ALM Proxy.

The function call is as follows:

`function withdrawERC4626(address token, uint256 amount) external returns (uint256 shares)`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.3 - Redeem ERC-4626 Shares [Core]  <!-- UUID: eec2b12a-6578-483a-824e-1442f3b0410c -->

The documents herein define the steps for a relayer to redeem vault shares for the underlying asset from an ERC-4626 vault, with the assets sent to the ALM Proxy.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3.3.1 - Call redeemERC4626 Function [Core]  <!-- UUID: a6474ee7-317b-430b-abd7-bf81a50ca898 -->

Only an operator with the relayer role can redeem vault shares for the underlying asset. To do so, they must call the `redeemERC4626` function on the Controller contract on mainnet, providing the number of shares to redeem. The address is the ALM Proxy acting as both the owner of the shares being redeemed and the receiver of the resulting assets. The operation will only succeed if the ALM Proxy holds at least the number of shares specified for redemption; otherwise, the transaction will revert. When this function is called:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will redeem the specified number of shares from the vault, sending the resulting assets to the ALM Proxy.
- After redemption, the contract will update the withdrawal rate limit based on the amount of assets received.

The function call is as follows:

`function redeemERC4626(address token, uint256 shares) external returns (uint256 assets)`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4 - ERC-7540 Functions [Core]  <!-- UUID: ff9638aa-a4d5-4a5e-a2bb-9b924b9987f9 -->

The documents herein define the general Keel Liquidity Layer operational procedures for interacting with ERC-7540-compliant tokenized vaults. ERC-7540 is a standard interface for vaults representing and managing multiple underlying assets within a single vault. Keel Liquidity Layer can integrate with various ERC-7540 vaults. For instance-specific parameters (such as vault addresses, asset addresses, and rate limits), refer to the relevant ERC-7540 Instance Configuration Document.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4.1 - Deposit To ERC-7540 Vault [Core]  <!-- UUID: 0ab348c1-50f9-4215-a78b-2b9dcf22aa03 -->

The documents herein define the steps for a relayer to request and claim deposit of assets from the ALM Proxy to an ERC-7540 vault.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4.1.1 - Call requestDepositERC7540 Function [Core]  <!-- UUID: e86cf2c1-31f6-4f83-8120-89b52611adae -->

Only an operator with the relayer role can request a deposit into an ERC-7540 vault. To do so, they must call the `requestDepositERC7540` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to deposit. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for deposit; otherwise, the transaction will revert. The Rate Limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the deposit amount is within the allowed rate limit for the specified vault.
- The contract will approve the vault to spend the underlying asset from the ALM Proxy. The approval and deposit request are both performed from the ALM Proxy address.
- The contract will submit a deposit request to the vault. Shares will not be received immediately; they must be claimed in a separate step after the vault processes the deposit.

The function call is as follows:

`function requestDepositERC7540(address token, uint256 amount) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4.1.2 - Call claimDepositERC7540 Function [Core]  <!-- UUID: cb81a01a-74b8-4e35-a83d-0848dd1f9f14 -->

Only an operator with the relayer role can claim shares from an ERC-7540 vault after a deposit request. To do so, they must call the `claimDepositERC7540` function on the Controller contract on mainnet, providing the vault token address. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will determine the maximum number of shares that can be claimed by the ALM Proxy.
- The contract will claim the shares from the vault, and the ALM Proxy will receive the corresponding number of vault shares.

The function call is as follows:

`function claimDepositERC7540(address token) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4.2 - Redeem From ERC-7540 Vault [Core]  <!-- UUID: 7077efbf-91fb-402c-831f-8f15e13f0a6a -->

The documents herein define the steps for a relayer to request and redeem vault shares for the underlying asset from an ERC-7540 vault, with the assets sent to the ALM Proxy.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4.2.1 - Call requestRedeemERC7540 Function [Core]  <!-- UUID: 19e6bba4-8d6f-4d1c-95d5-000b2dbf948c -->

Only an operator with the relayer role can request the redemption of shares from an ERC-7540 vault. To do so, they must call the `requestRedeemERC7540` function on the Controller contract on mainnet, providing the vault token address and the number of shares to redeem. The rate limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the redemption amount is within the allowed rate limit for the specified vault.
- The contract will submit a redemption request to the vault. Assets will not be received immediately; they must be claimed in a separate step after the vault processes the redemption.

The function call is as follows:

`function requestRedeemERC7540(address token, uint256 amount) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.4.2.2 - Call claimRedeemERC7540 Function [Core]  <!-- UUID: 9b43cc7e-dfb9-4868-b9a6-8848c837691b -->

Only an operator with the relayer role can claim assets from an ERC-7540 vault after a redemption request. To do so, they must call the `claimRedeemERC7540` function on the Controller contract on mainnet, providing the vault token address. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will determine the maximum amount of assets that can be claimed by the ALM Proxy.
- The contract will claim the assets from the vault, and the ALM Proxy will receive the corresponding amount of underlying assets.

The function call is as follows:

`function claimRedeemERC7540(address token) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5 - PSM Functions [Core]  <!-- UUID: 19d426c4-9846-4ea8-91f7-5b6d71055491 -->

The documents herein define the swap operations performed by the Keel Liquidity Layer in the PSM.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.1 - Swap USDS To USDC [Core]  <!-- UUID: cb52a3c2-6b2a-43a0-b2e0-728101c409bd -->

The documents herein define a series of operations for an operator to `swap` USDS to USDC through the PSM.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.1.1 - Call swapUSDSToUSDC Function [Core]  <!-- UUID: df09edaf-7a92-4d8e-ae86-a9666a0bf082 -->

Only an operator with the relayer role can swap USDS to USDC via the PSM. To do so, they must call the swapUSDSToUSDC function on the Controller contract on mainnet, providing the usdcAmount (denominated in 1e6 precision to match PSM USDC handling). The operation will only succeed if the ALM Proxy holds at least the equivalent amount of USDS for the swap; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for swaps. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the swap amount is within the allowed rate limit (LIMIT_USDS_TO_USDC) for the PSM.
- The contract will convert the USDC amount to an 18-decimal format using psmTo18ConversionFactor.
- The contract will approve the daiUsds contract to spend the converted amount from the ALM Proxy.
- The contract will swap USDS to DAI at a 1:1 ratio via daiUsds, sending DAI to the proxy.
- The contract will approve the PSM to spend the DAI.
- The contract will swap DAI to USDC at a 1:1 ratio with no fee via psm.buyGemNoFee, sending USDC to the proxy.

The function call is as follows:

`function swapUSDSToUSDC(uint256 usdcAmount) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.2 - Swap USDC To USDS [Core]  <!-- UUID: da2164e3-03bc-447c-89c5-119d01feddaa -->

The documents herein define a series of operations for an operator to `swap` USDC to USDS through the PSM.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.2.1 - Call swapUSDCToUSDS Function [Core]  <!-- UUID: 1b18072b-c409-4d2f-a333-1e5c3ae8ab90 -->

Only an operator with the relayer role can swap USDC to USDS via the PSM. To do so, they must call the `swapUSDCToUSDS` function on the Controller contract on mainnet, providing the usdcAmount (denominated in 1e6 precision to match PSM USDC handling). The operation will only succeed if the ALM Proxy holds at least the amount of USDC specified for the swap; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for swaps. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the swap amount is within the allowed rate limit (LIMIT_USDC_TO_USDS) for the PSM.
- The contract will approve the PSM to spend the USDC from the ALM Proxy.
- The contract will calculate the swap limit per transaction based on the DAI balance held by the PSM, converting with psmTo18ConversionFactor.
- If the usdcAmount is less than or equal to the limit, the contract will perform a direct swap of USDC to DAI.
- If the usdcAmount exceeds the limit, the contract will split the swap into multiple smaller swaps: refill the PSM with DAI via psm.fill, recalculate the limit, swap the maximum allowed amount, update the remaining amount, and repeat until complete (reverting with "DssLitePsm/nothing-to-fill" if PSM cannot be filled).
- The contract will convert the USDC amount to a DAI amount, accounting for token decimal differences.
- The contract will approve the daiUsds contract to spend the DAI amount from the ALM Proxy.
- The contract will swap DAI to USDS at a 1:1 ratio via daiUsds, sending USDS to the proxy.

The function call is as follows:

`function swapUSDCToUSDS(uint256 usdcAmount) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.3 - Transfer Token Via LayerZero [Core]  <!-- UUID: 030c5483-6126-40f7-b7ff-a99186ab105d -->

The documents herein define the steps for a relayer to transfer a token via LayerZero to a destination endpoint, with the assets sent according to the configured recipient.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.3.1 - Call transferTokenLayerZero Function [Core]  <!-- UUID: f88e14a0-fa64-44cc-a52c-cb35b7704ee8 -->

Only an operator with the relayer role can transfer tokens via LayerZero. To do so, they must call the `transferTokenLayerZero` function on the Controller contract on mainnet, providing the oftAddress, amount, and destinationEndpointId (payable for native fees). The operation will only succeed if the ALM Proxy holds sufficient tokens and fees; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the transfer amount is within the allowed rate limit (built from LIMIT_LAYERZERO_TRANSFER, oftAddress, and destinationEndpointId).
- If approval is required, the contract will approve the token for the oftAddress.
- The contract will build LayerZero send options and a SendParam struct with destination details, amount, and recipient from layerZeroRecipients.
- The contract will quote the OFT receipt to set the minimum amount received.
- The contract will quote the messaging fee and execute the send via proxy.doCallWithValue, passing the fee value.

The function call is as follows:

`function transferTokenLayerZero(address oftAddress, uint256 amount, uint32  destinationEndpointId) external payable`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.6 - Bridging Functions [Core]  <!-- UUID: 66d40b48-7f80-46a2-8ee0-503580a42d4c -->

The documents herein define the operations performed by an operator to bridge liquidity between Ethereum Mainnet and the destination blockchains for the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.6.1 - Bridge USDC Using Circle Cross-Chain Transfer Protocol [Core]  <!-- UUID: e4b91efa-ff29-4a8e-a28c-d54127ad2480 -->

The documents herein define the process to bridge USDC using the Circle Cross-Chain Transfer Protocol.

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.6.1.1 - Call transferUSDCToCCTP Function [Core]  <!-- UUID: 46a74cd0-5e4e-4ea6-8fe6-ab38a8930f32 -->

Only an operator with the relayer role can initiate a USDC transfer to a specified destination domain using CCTP, handling rate limits, approvals, and splitting large amounts if needed. It requires parameters like proxy, Rate Limits, cctp, usdc, rate limit IDs, mintRecipient, destinationDomain, and usdcAmount. To do so, they must call the `transferUSDCToCCTP` function on the Controller contract on mainnet. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will trigger a rate limit decrease for the CCTP limit ID and amount.
- The contract will trigger a rate limit decrease for a domain-specific key and amount.
- The contract will require that mintRecipient is not zero, reverting if it is.
- The contract will approve the CCTP contract to spend the USDC amount from the proxy, assuming that the proxy has enough USDC.
- The contract will retrieve the burn limit per message for the USDC address (if the amount is larger than the limit it must be split into multiple calls).
- If the usdcAmount exceeds the burn limit, the contract will initiate a CCTP transfer for the burn limit amount and subtract it from the remaining usdcAmount.
- If any usdcAmount remains after the loop, the contract will initiate a final CCTP transfer for that amount.

The function call is as follows:

`function transferUSDCToCCTP(uint256 usdcAmount, uint32 destinationDomain) external`

###### A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.6.2 - Bridge USDS / sUSDS Using SkyBridge (LayerZero OFT) Token Bridge [Core]  <!-- UUID: d239ba22-9a09-49f1-9fdc-a1d306ffe697 -->

This document defines the process for an operator to bridge USDS or sUSDS using the OP Token Bridge. This process will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.2.1.1.3 - Rate Limit Management [Core]  <!-- UUID: bf81a7dd-9483-48e4-b489-cb3cb2e61b37 -->

The documents herein define the protocol for querying, setting, and adjusting `RateLimits` for Instances using their `RateLimitID`s. The Rate Limits must be maintained in line with Keel’s strategy, market conditions, and security considerations.

###### A.6.1.1.3.2.6.1.2.2.1.1.3.1 - Get Rate Limit Data [Core]  <!-- UUID: 921dd8b4-763e-4edf-9cb9-f2e0cb012109 -->

Anyone can query the full rate limit data for a specific key. Calling this function will carry out the following actions:

- The contract will return the stored RateLimitData struct from the _data mapping for the key.

The function call is as follows:

`function getRateLimitData(bytes32 key) external override view returns (RateLimitData memory)`

###### A.6.1.1.3.2.6.1.2.2.1.1.3.2 - Set Rate Limit Data [Core]  <!-- UUID: 132f4de3-5b4c-462b-8f03-4cc15706baaf -->

Only an operator with the admin role is able to set or update rate limit data for a specific key, including maxAmount, slope, and historical values. There are two overloads for flexibility. Calling these functions will carry out the following actions:

- The contract will require that lastAmount is less than or equal to maxAmount, reverting with "RateLimits/invalid-lastAmount" if not.
- The contract will require that lastUpdated is less than or equal to the current block timestamp, reverting with "RateLimits/invalid-lastUpdated" if not.
- The contract will store the provided data in the _data mapping as a RateLimitData struct.
- The contract will emit a RateLimitDataSet event with the key and provided values.

The function calls are as follows:

`function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope, uint256 lastAmount, uint256 lastUpdated) public override onlyRole(DEFAULT_ADMIN_ROLE)

function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope) external override`

###### A.6.1.1.3.2.6.1.2.2.1.1.3.3 - Set Unlimited Rate Limit Data [Core]  <!-- UUID: 0a5ccc61-eaf4-4b49-80d7-770e29178c1a -->

Only an operator with the admin role is able to set unlimited rate limit data for a specific key by configuring it with maximum values. Calling this function will carry out the following actions:

- The contract will call setRateLimitData internally with type(uint256).max for maxAmount and lastAmount, 0 for slope, and the current block timestamp for lastUpdated.

The function call is as follows:

`function setUnlimitedRateLimitData(bytes32 key) external override`

###### A.6.1.1.3.2.6.1.2.2.1.1.3.4 - Get Current Rate Limit [Core]  <!-- UUID: 99f4fe4c-04af-4efe-b099-f5d92122de78 -->

Anyone can query the current rate limit value for a specific key, accounting for time-based slope accrual. Calling this function will carry out the following actions:

- The contract will retrieve the RateLimitData for the key from the _data mapping.
- If maxAmount is type(uint256).max (unlimited case), the contract will return type(uint256).max.
- Otherwise, the contract will calculate and return the minimum of (slope * time elapsed since lastUpdated + lastAmount) and maxAmount.

The function call is as follows:

`function getCurrentRateLimit(bytes32 key) public override view returns (uint256)`

###### A.6.1.1.3.2.6.1.2.2.1.1.3.5 - Trigger Rate Limit Decrease [Core]  <!-- UUID: a710528f-e695-4262-bab1-e5ee57241315 -->

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

###### A.6.1.1.3.2.6.1.2.2.1.1.4 - Instance Lifecycle Management [Core]  <!-- UUID: 724970e4-e5e7-41ff-9448-d984c2c9a9e3 -->

The documents herein define processes for invoking (onboarding) new Keel Liquidity Layer Instances and offboarding existing ones. This process will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.2.1.1.5 - Upgrading Controller [Core]  <!-- UUID: f427c73d-fa0a-4183-89da-595ac1f5792e -->

The documents herein define the process for deploying new Controller contracts. This process will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.2.1.2 - Non-Routine Protocol [Core]  <!-- UUID: 0ca77e89-5598-46f6-a829-ff85c8c41e5e -->

The documents herein define the process for non-routine ongoing management of the Keel Liquidity Layer and its active Instances on Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.2.1.3 - Emergency Protocol [Core]  <!-- UUID: 61b08883-4417-4f10-acb3-2cafdc5eda21 -->

The documents herein define all the possible actions that can be taken in case of an emergency within Keel Liquidity Layer operations on Ethereum Mainnet.

###### A.6.1.1.3.2.6.1.2.2.1.3.1 - Remove Compromised Relayer As Freezer [Core]  <!-- UUID: 00a56799-7803-460a-bda3-eab312fc296d -->

In the event of a compromised Relayer, the `FREEZER_ROLE` can call the function to `removeRelayer` from the Controller contract. Only an operator with the freezer role can remove a relayer. To do so, they must call the `removeRelayer` function on the Controller contract on mainnet, providing the compromised relayer’s address. Calling this function will carry out the following actions:

- The contract will confirm the caller holds the freezer role. If the caller does not have the freezer role, the transaction will revert.
- The contract will revoke the relayer role from the specified address.
- The contract will emit a `RelayerRemoved(relayer)` event.

The function call is as follows:

`function removeRelayer(address relayer) external`

###### A.6.1.1.3.2.6.1.2.2.1.3.2 - Redeem All Ethereum Mainnet Positions [Core]  <!-- UUID: 23a36776-11e0-4c65-a25d-500a44e14eb4 -->

The documents herein define the actions that should be performed by an operator if there is a need to recover the liquidity from Mainnet Protocols and centralize it in the Mainnet Keel ALM Proxy.

###### A.6.1.1.3.2.6.1.2.2.1.3.2.1 - ERC-4626 Withdrawal Action [Core]  <!-- UUID: 98208afa-5810-4591-b261-efe0c1b882e5 -->

In order to withdraw all ERC-4626 balances, the operator must call the `redeemERC4626` function.

The function call is as follows:

`function redeemERC4626(address(token), token.balanceOf(address(proxy)))`

For more detailed instructions on the code to execute this, see [A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.3 - ERC-4626 Functions](3de32801-e895-4a21-84da-aa5818d16349).

###### A.6.1.1.3.2.6.1.2.2.1.3.3 - USDC to USDS Swap Action [Core]  <!-- UUID: 23770b76-5a1f-49d2-b970-dbf908c05817 -->

This document defines the action that should be performed by an operator if there is a need to centralize all recovered liquidity in USDS. The operator must call the `swapUSDCToUSDS` function.

The function call is as follows:

`function swapUSDCToUSDS(usdc.balanceOf(address(proxy))`

For more detailed instructions on the code to execute this see [A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.2 - Swap USDC To USDS](da2164e3-03bc-447c-89c5-119d01feddaa).

###### A.6.1.1.3.2.6.1.2.2.1.3.4 - USDS Burn Action [Core]  <!-- UUID: 44ca2425-03dd-4913-919a-666a77854709 -->

This document defines the action that should be performed if there is a need to repay and then burn Keel’s USDS debt. The operator must call the `burnUSDS` function.

The function call is as follows:

`function burnUSDS(usds.balanceOf(address(proxy))`

More detailed instructions on the code to execute this, see [A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.1.2 - Burn USDS](9c9536a8-bb2d-4d37-98cf-4c25a5699026).

###### A.6.1.1.3.2.6.1.2.2.2 - Solana [Core]  <!-- UUID: f70746e5-a879-4d13-bd48-74bf79478f4d -->

The documents herein describe common operational procedures for the Keel Liquidity Layer applicable across multiple Instances on Solana.

###### A.6.1.1.3.2.6.1.2.2.2.1 - Routine Protocol [Core]  <!-- UUID: 828e1609-88b5-4d6d-a31a-607183901ea1 -->

The documents herein define the protocol for routine ongoing management of the Keel Liquidity Layer and its active Instances on Solana.

###### A.6.1.1.3.2.6.1.2.2.2.1.1 - Role Hierarchy And Permissions [Core]  <!-- UUID: 6c7d3476-9e97-495d-a491-3194e7c061a3 -->

The documents herein define roles (Admin, Relayer, ALM Controller and Freezer) and their responsibilities/permissions for managing the Keel Liquidity Layer.

###### A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role [Core]  <!-- UUID: 0270b595-8957-4fb2-a9cd-2bc197dc3367 -->

The admin role is configured with the following permissions: `can_freeze_controller`, `can_unfreeze_controller`, `can_manage_permissions`, `can_suspend_permissions`, `can_manage_reserves_and_integrations`, `can_invoke_external_transfer`. This role can grant and revoke any role, including itself and all other roles defined in the contract. The admin role is also used for general admin functions in all contracts. This role is fully controlled by Sky Governance via the Keel Proxy.

`constructor(address admin) {
_grantRole(DEFAULT_ADMIN_ROLE, admin);`

###### A.6.1.1.3.2.6.1.2.2.2.1.1.2 - Relayer Role [Core]  <!-- UUID: 2b42015c-c76a-4364-b8b5-c9a2b9f6f484 -->

The Relayer role is the address(es) for the Keel Liquidity Layer ALM Planner off-chain system that calls functions on `SvmAlmController` program to perform actions on funds held by Keel's Solana Controller. The Relayer Role has `can_execute_swap` and `can_reallocate` permissions. The Relayer Role may be granted to an address by any address with `can_manage_permissions` privileges and can be revoked by one with `can_suspend_permissions` privileges.

###### A.6.1.1.3.2.6.1.2.2.2.1.1.3 - Freezer Role [Core]  <!-- UUID: 6f7becc7-2e70-44e5-8662-25ba7dd1a5f8 -->

The Freezer role is the address of the emergency role that can remove a compromised Relayer. The Freezer role has `can_freeze_controller` , `can_suspend_permissions` and `can_liquidate` permissions.

###### A.6.1.1.3.2.6.1.2.2.2.1.2 - Controller Functions [Core]  <!-- UUID: 78b48a5e-d4f8-46f3-bf32-c60cdc213be4 -->

The documents herein describe the purpose and operational use of key functions within Keel Liquidity Layer `SvmAlmController` programs: Asset Transfer Management (direct transfers, protocol deposits/withdrawals) and Cross-chain Operations (CCTP bridging, SkyBridge bridging).

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1 - Controller Contract Functions [Core]  <!-- UUID: 397928f4-0d80-4ed9-8a51-6e22f962ab94 -->

The documents herein define the functions controlled by the Controller contract for Keel Liquidity Layer operations on Solana.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.1 - Admin Functions [Core]  <!-- UUID: ab262163-ec0a-49c7-be21-578ed120ca56 -->

The documents herein define the operations performed by the admin role (see [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367)) within the `SvmAlmController` contract.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.1.1 - Configure Integrations [Core]  <!-- UUID: 10be5f11-b678-45b9-8ba2-f636ec3c83c7 -->

The admin can configure and update configurations on permitted integrations with third party protocols. For example, permitting bridge interfaces, setting slippage rules for permitted swap routes or permitting certain lending market interfaces.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.1.2 - Configure Reserves [Core]  <!-- UUID: 85dbd095-10fd-46bf-9d6b-96a7b1a8c979 -->

The admin can configure and update configurations on permitted tokens which the `SvmAlmController` can hold or transact in.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.1.3 - Configure Rate Limits [Core]  <!-- UUID: 7f7333d4-c1a8-4bb0-8dec-47ce46aac125 -->

The admin can configure and update the rate limits for `Integration`s and `Reserve`s.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.2 - Relayer Function [Core]  <!-- UUID: ee2f8a2e-8225-4747-9f3a-cc1b4624987b -->

The documents herein define the operations performed by the relayer role (see [A.6.1.1.3.2.6.1.2.2.2.1.1.2 - Relayer Role](2b42015c-c76a-4364-b8b5-c9a2b9f6f484)) within the `SvmAlmController` contract.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.2.1 - CctpBridge Actions [Core]  <!-- UUID: 619a94f1-05ac-4b47-80d5-cafd9515b7e5 -->

The Relayer can perform CCTP Bridge actions which facilitates transferring of assets across networks using Circle’s CCTP Interoperability protocol.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.2.1.1 - Push Action [Core]  <!-- UUID: 1294a5b5-316b-4a05-bdb3-87ed33067d39 -->

The Relayer can transfer tokens via a permitted bridging protocol, to a pre-configured destination chain and address, subject to rate limits.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.2.2 - LzBridge Actions [Core]  <!-- UUID: e408605b-d029-42ca-b9cb-8974d64f5be6 -->

The Relayer can perform OFT Bridge actions which facilitates transferring of assets across networks using LayerZero's OFT Interoperability protocol.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.2.2.1 - Push Action [Core]  <!-- UUID: 5d174ad0-e955-40f9-b64e-e07a72b60216 -->

The push action can transfer tokens via a permitted bridging protocol, to a pre-configured destination chain and address, subject to rate limits.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.2.3 - AtomicSwap Action [Core]  <!-- UUID: 2f6f0f93-6a3b-4dec-a862-a78080b23736 -->

The Relayer can perform swapping actions from one token to another. This action is split across two instructions which are applied as bookends to inner swap instructions.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.2.3.1 - Borrow Action [Core]  <!-- UUID: 544c4bae-7d5c-494f-8bdc-4ee47203e1e7 -->

The borrow action temporarily funds the Relayers account with tokens to support an intended swap on a permitted swap route, subject to rate limits and validating that the corresponding `Repay` instruction is present at the end of the transaction.

###### A.6.1.1.3.2.6.1.2.2.2.1.2.1.2.3.2 - Repay Action [Core]  <!-- UUID: f19c7438-54ee-47ef-b92d-9313b581da29 -->

The repay action validates that the proceeds of the swap meet minimum slippage requirements, or fails the overall transaction.

###### A.6.1.1.3.2.6.1.2.2.2.1.3 - Rate Limit Management [Core]  <!-- UUID: 7e6e8dea-5c3e-430f-a984-926bc726e992 -->

The documents herein define the protocol for querying, setting, and adjusting Rate Limits. The Rate Limits must be maintained in line with Keel’s strategy, market conditions, and security considerations.

###### A.6.1.1.3.2.6.1.2.2.2.1.3.1 - Reserve Level Rate Limits [Core]  <!-- UUID: f5b98691-5237-427b-8d8e-2b08262da8eb -->

`Reserve` level rate limits constrain the outflow that can occur from a given token’s `Reserve` in aggregate across all Integrations.

###### A.6.1.1.3.2.6.1.2.2.2.1.3.1.1 - Get Rate Limit Data [Core]  <!-- UUID: 21590f17-8e03-4fc3-9a37-e8364bbee322 -->

The properties associated with a Reserve level rate limit can be read from the `Reserve` account corresponding to a particular token, as follows:

`pub struct Reserve {
// ...
pub rate_limit_slope: u64,
pub rate_limit_max_outflow: u64,
pub rate_limit_outflow_amount_available: u64,
pub rate_limit_remainder: u64
// ...
}`

###### A.6.1.1.3.2.6.1.2.2.2.1.3.1.2 - Set Rate Limit Data [Core]  <!-- UUID: aa43f1e6-6ee6-4596-a288-f79685cd8144 -->

Only an operator with the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) is able to set or update rate limit data for a specific `Reserve`, including `rate_limit_slope` and `rate_limit_max_outflow`.

`manage_reserves(
ManageReserveArgs {
status: None,
rate_limit_slope: Some(rate_limit_slope),
rate_limit_max_outflow: Some(rate_limit_max_outflow),
}
)`

###### A.6.1.1.3.2.6.1.2.2.2.1.3.1.3 - Set Unlimited Rate Limit Data [Core]  <!-- UUID: 76946aaf-70dc-43cf-a6e0-ce947f19b93b -->

Only an operator with the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) is able to set unlimited rate limit data for a specific key by configuring it with maximum values.

`manage_reserves(
ManageReserveArgs {
status: None,
rate_limit_slope: Some(0),
rate_limit_max_outflow: Some(u64::MAX),
}
)`

###### A.6.1.1.3.2.6.1.2.2.2.1.3.2 - Integration Level Rate Limits [Core]  <!-- UUID: 3bf06ac1-44d2-4901-92fb-7af3cebef5a0 -->

`Integration` level rate limits constrain the flow of assets into a particular `Integration`.

###### A.6.1.1.3.2.6.1.2.2.2.1.3.2.1 - Get Rate Limit Data [Core]  <!-- UUID: c75e8c0d-0b16-4808-a14c-dac919ef9269 -->

The properties associated with a Reserve level rate limit can be read from the `Integration` account corresponding to a particular token, as follows:

`pub struct Integration {
// ...
pub rate_limit_slope: u64,
pub rate_limit_max_outflow: u64,
pub rate_limit_outflow_amount_available: u64,
pub rate_limit_remainder: u64
// ...
}`

###### A.6.1.1.3.2.6.1.2.2.2.1.3.2.2 - Set Rate Limit Data [Core]  <!-- UUID: 62654961-cf70-4455-a7df-c81861944395 -->

Only an operator with the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) is able to set or update rate limit data for a specific `Integration`, including `rate_limit_slope` and `rate_limit_max_outflow`.

`manage_integration(
ManageIntegrationArgs {
status: None,
description: None,
rate_limit_slope: Some(rate_limit_slope),
rate_limit_max_outflow: Some(rate_limit_max_outflow),
}
)`

###### A.6.1.1.3.2.6.1.2.2.2.1.3.2.3 - Set Unlimited Rate Limit Data [Core]  <!-- UUID: bd904ac0-32d2-4592-92cd-3eb01a3ce7de -->

Only an operator with the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) is able to set unlimited rate limit data for a specific key by configuring it with maximum values.

`manage_integration(
ManageIntegrationArgs {
status: None,
description: None,
rate_limit_slope: Some(0),
rate_limit_max_outflow: Some(u64::MAX),
}
)`

###### A.6.1.1.3.2.6.1.2.2.2.1.4 - Instance Lifecycle Management [Core]  <!-- UUID: 5fcff9f8-7f6d-427d-a12d-02df83b4db6e -->

The documents herein define processes for invoking (onboarding) new Keel Liquidity Layer Instances and off-boarding existing ones.

###### A.6.1.1.3.2.6.1.2.2.2.1.5 - Upgrading Controller [Core]  <!-- UUID: 7675ad2a-f865-4756-8da9-49062e785074 -->

The documents herein define the process for deploying new Controller contracts. This process will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 0aa16a2c-b0a0-427e-b822-1d9a399c65db -->

The documents herein define the process for non-routine ongoing management of the Keel Liquidity Layer and its active Instances on Solana.

###### A.6.1.1.3.2.6.1.2.2.2.3 - Emergency Protocol [Core]  <!-- UUID: 6cc9260a-88f8-4bf2-8819-8897000c5e5d -->

The documents herein define all the possible actions that can be taken in case of an emergency within Keel Liquidity Layer operations on Solana.

###### A.6.1.1.3.2.6.1.2.2.2.3.1 - Remove Compromised Relayer As Freezer [Core]  <!-- UUID: c4932ae7-0bf2-46fe-bbca-4bdd675368c9 -->

In the event of a compromised Relayer, the [A.6.1.1.3.2.6.1.2.2.2.1.1.3 - Freezer Role](6f7becc7-2e70-44e5-8662-25ba7dd1a5f8) and [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) can call the instruction to suspend the compromised Relayer from the Controller program, thereby preventing it from doing any further harm to the system. The backstop Relayer can then take over. This function should only be used if the keys to the Relayer multisig have been leaked or compromised, and the Relayer is now in the hands of an external bad actor.

`manage_permission(
ManagePermissionArgs {
status: PermissionStatus::Suspended,
can_manage_permissions: false,
can_invoke_external_transfer: false,
can_execute_swap: false,
can_reallocate: false,
can_freeze_controller: false,
can_unfreeze_controller: false,
can_manage_reserves_and_integrations: false,
can_suspend_permissions: false,
can_liquidate: false,
}
)`

###### A.6.1.1.3.2.6.1.2.2.2.3.2 - Freeze the Controller [Core]  <!-- UUID: de48d076-bad2-4edd-a740-0e5ee9173d0d -->

In the event of a more severe threat to the Controller, the [A.6.1.1.3.2.6.1.2.2.2.1.1.3 - Freezer Role](6f7becc7-2e70-44e5-8662-25ba7dd1a5f8) can call the instruction to suspend the entire Controller instance.

###### A.6.1.1.3.2.6.1.2.2.2.3.2.1 - Full Freeze [Core]  <!-- UUID: 4f8c8aa3-fffc-46dd-aeb7-b23e996619d7 -->

This action leads to a complete freeze and prevents any actions on the Controller until the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) subsequently lifts this status. Integrations, Reserves nor Permissions cannot be managed during this period, and funds cannot be moved.

`manage_controller(
ManageControllerArgs {
status: ControllerStatus::PushPullFrozen,
}
)`

###### A.6.1.1.3.2.6.1.2.2.2.3.2.2 - Reallocation Freeze [Core]  <!-- UUID: 2ed41eef-989b-4253-8de7-5e368da0242a -->

A complete freeze prevents any movement of funds within the Controller until the [A.6.1.1.3.2.6.1.2.2.2.1.1.1 - Default Admin Role](0270b595-8957-4fb2-a9cd-2bc197dc3367) subsequently lifts this status. Integrations, Reserves and Permissions cannot be configured during this period.

`manage_controller(
ManageControllerArgs {
status: ControllerStatus::Frozen,
}
)`

###### A.6.1.1.3.2.6.1.2.2.2.3.3 - Redeem All Positions [Core]  <!-- UUID: 4f4a2911-a604-4203-8103-e9a05fe4cb80 -->

The documents herein define the actions that should be performed by an operator if there is a need to recover the liquidity from Solana Protocols and centralize it in the Keel ALM Controller.

###### A.6.1.1.3.2.6.1.2.2.2.3.3.1 - Integrations [Core]  <!-- UUID: 22943595-8338-47b6-b3d2-55bd131895e9 -->

This will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.2.2.3.3.2 - Reserves [Core]  <!-- UUID: 8d1232fa-d714-48e5-9cca-798543c02e65 -->

This will be specified in a future iteration of the Keel Artifact.

###### A.6.1.1.3.2.6.1.2.2.2.3.4 - AtomicSwap Action [Core]  <!-- UUID: 1bc17a00-a5b7-4390-bec5-46674053222b -->

This document defines the action that should be performed by an operator if there is a need to centralize all recovered liquidity in USDS.

`mainnetController.swapUSDCToUSDS(usdc.balanceOf(address(proxy))`

For more detailed instructions on the code to execute this see [A.6.1.1.3.2.6.1.2.2.1.1.2.1.2.5.2 - Swap USDC To USDS](da2164e3-03bc-447c-89c5-119d01feddaa).

###### A.6.1.1.3.2.6.1.2.2.2.3.5 - Bridge to Ethereum Mainnet [Core]  <!-- UUID: c60fe936-a500-4366-bcf2-ae813e64584a -->

This document defines the action that should be performed by an operator if there is a need to return recovered liquidity to Keel’s Ethereum Mainnet ALM Controller.

###### A.6.1.1.3.2.6.1.2.3 - Allocation Strategy [Core]  <!-- UUID: cebfc91d-1b4e-49ca-9e4d-4c9b7043db81 -->

In the future, additional logic will be added herein regarding the strategy by which capital is allocated between different Instances of the Keel Liquidity Layer.

##### A.6.1.1.3.2.6.1.3 - Active Instances [Core]  <!-- UUID: b9316097-ab93-4a8b-aa51-1e44ceb69c4d -->

The Instances of the Keel Liquidity Layer with `Active` Status are stored herein. The `RRC Framework Full Implementation Coverage` status defines whether the Instance Financial RRC is calculated based on a fully implemented risk model (see [A.3.2.1.1.4.3.1 - Fully Implemented Risk Models](419a1d00-fbae-4d26-bd47-8f57677d8001)) or a pending risk model (see [A.3.2.1.1.4.3.2 - Pending Risk Models](81ca88bf-3f6a-4d10-a3e2-d47cf6636d7d)). If the Instance Financial RRC is calculated based on a fully implemented risk model the status is `Covered`. If the Instance Financial RRC is calculated based on a pending risk model the status is `Pending`.

###### A.6.1.1.3.2.6.1.3.1 - Solana Instances [Core]  <!-- UUID: 77c4c83d-199b-412b-abf5-999b94e93531 -->

The Solana Instances of the Keel Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.3.2.6.1.3.1.1 - Kamino [Core]  <!-- UUID: 39979f83-5da3-45c9-9ad4-bb17cca5513c -->

The Solana Instances of the Kamino Protocol with `Active` Status are stored herein.

###### A.6.1.1.3.2.6.1.3.1.1.1 - Solana - Kamino USDS Instance Configuration Document [Core]  <!-- UUID: fa6f6aa7-410e-4515-8458-9f3efb30c942 -->

The documents herein contain the Instance Configuration Document for the Kamino USDS Instance.

###### A.6.1.1.3.2.6.1.3.1.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 5a235b70-b3d0-4a33-a88d-32b0c3aec917 -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.1.1.2 - Parameters [Core]  <!-- UUID: 3fc55a0d-c568-4b70-9771-ba125a89782e -->

The documents herein define the parameters of the Kamino USDS Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 77832cc0-aa05-4a84-952d-54efb83b6ec0 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.1.1.2.1.1 - Network [Core]  <!-- UUID: 32e1e642-91bd-4f67-b271-771f32da87d9 -->

Solana

###### A.6.1.1.3.2.6.1.3.1.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 3eba506a-6482-424d-8cc9-752c65e634c5 -->

Kamino

###### A.6.1.1.3.2.6.1.3.1.1.1.2.1.3 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: 7198e08b-080d-46c7-87fe-2387461b3473 -->

USDS

###### A.6.1.1.3.2.6.1.3.1.1.1.2.1.4 - Market [Core]  <!-- UUID: 5569d20b-c7ac-4736-b5a1-c6017cff4520 -->

Main

###### A.6.1.1.3.2.6.1.3.1.1.1.2.1.5 - Token [Core]  <!-- UUID: d86162cd-defd-431c-8cac-5b0f6eecc1ac -->

kUSDS

###### A.6.1.1.3.2.6.1.3.1.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 2bd4ac66-9878-42f1-9873-4708ed2a44c6 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.1.1.2.2.1 - Token Address [Core]  <!-- UUID: e8d610ec-9514-46fb-9431-3c4260edc7be -->

`6nnt6N4Ay9tBeMWnVWKS24hDtE6R3fshi5TteUcSKJcQ`

###### A.6.1.1.3.2.6.1.3.1.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 1de01d57-847c-4b6d-afc9-d841d63228c0 -->

`USDSwr9ApdHk5bvJKMjzff41FfuX8bSxdKcR81vTwcA`

###### A.6.1.1.3.2.6.1.3.1.1.1.2.3 - Rate Limit Information [Core]  <!-- UUID: d625d675-4667-4464-af41-95d35414fad4 -->

The specific `Integration` account contains the rate limit information to control inflows into the Kamino USDS Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.1.2.3.1 - Integration Account Address [Core]  <!-- UUID: 28537d8e-fe00-46db-b2ce-726fd718bd86 -->

`H5Vix4RGchYq1cemoe61y7J4j4v3XgWPGLBeqvPEgvzr`

###### A.6.1.1.3.2.6.1.3.1.1.1.2.4 - Rate Limits [Core]  <!-- UUID: ecde5b24-7807-40ee-b352-f509d4e2daf7 -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.1.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 9577670b-0f91-45e8-b7e9-faf072e2d7e9 -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 USDS
- `slope`: 10,000,000 USDS per day

###### A.6.1.1.3.2.6.1.3.1.1.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 1d393362-1b05-4dc3-9531-233d748c2394 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 3503046a-a936-46d1-93f6-dbce0b6b55d3 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 0a1e41de-51bb-4da5-972d-d1e7cfd13ace -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

###### A.6.1.1.3.2.6.1.3.1.1.2 - Solana - Kamino USDC Instance Configuration Document [Core]  <!-- UUID: 2510c2ba-c304-478f-84b1-a421e62de8b4 -->

The documents herein contain the Instance Configuration Document for the Kamino USDC Instance.

###### A.6.1.1.3.2.6.1.3.1.1.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: f0715f96-8cc2-4bc9-88d4-11542aa9c288 -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.1.2.2 - Parameters [Core]  <!-- UUID: dae88d4b-670f-47e4-b9bb-11c5f8ce3833 -->

The documents herein define the parameters of the Kamino USDC Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 2b1419e1-a279-4172-88dc-a897905ab17e -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.1.2.2.1.1 - Network [Core]  <!-- UUID: b9ca0b9a-e633-4902-9b56-39593690a455 -->

Solana

###### A.6.1.1.3.2.6.1.3.1.1.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 11ebac06-18a7-4105-8523-0ae4020eb669 -->

Kamino

###### A.6.1.1.3.2.6.1.3.1.1.2.2.1.3 - Market [Core]  <!-- UUID: 6d5a7c41-5630-4df4-8995-f7f75df9a866 -->

Main

###### A.6.1.1.3.2.6.1.3.1.1.2.2.1.4 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: 47b8761c-6f72-48dd-a014-05e29c8d6680 -->

USDC

###### A.6.1.1.3.2.6.1.3.1.1.2.2.1.5 - Token [Core]  <!-- UUID: 8d7a5c83-d917-40ed-9fc7-f912fe9933f6 -->

kUSDC

###### A.6.1.1.3.2.6.1.3.1.1.2.2.2 - Contract Addresses [Core]  <!-- UUID: 76c37fb1-f74c-486f-8523-d485de5c278c -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.1.2.2.2.1 - Token Address [Core]  <!-- UUID: 3f3deb3c-e023-4b37-94af-5e93a592ce3a -->

`9DrvZvyWh1HuAoZxvYWMvkf2XCzryCpGgHqrMjyDWpmo`

###### A.6.1.1.3.2.6.1.3.1.1.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 537e73fd-f7d6-4776-af11-1cc83433dd43 -->

`EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

###### A.6.1.1.3.2.6.1.3.1.1.2.2.3 - Rate Limit Information [Core]  <!-- UUID: 3740064f-912c-4ab0-8b79-8f2c5970ed0b -->

The specific `Integration` account contains the rate limit information to control inflows into the Kamino USDC Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.2.2.3.1 - Integration Account Address [Core]  <!-- UUID: 9f0cdd10-d1fe-4da5-9b64-6757195ebf8b -->

`GZ6vUcBZk4QiaBUhhn1TpX6S7FiXK71Pogke1RnBc3zA`

###### A.6.1.1.3.2.6.1.3.1.1.2.2.4 - Rate Limits [Core]  <!-- UUID: a1cf8da0-dc37-4abb-9205-aee0a825363a -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.1.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 564245a6-2191-4434-ba16-52a2f76d4acd -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 USDC
- `slope`: 10,000,000 USDC per day

###### A.6.1.1.3.2.6.1.3.1.1.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: f21f04b3-30d3-4b5e-81e0-2e83dda36b37 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.1.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: fe79db33-1328-4baa-867d-141173666215 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.1.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 44ed77d2-a81c-41d3-a77c-84b6e9293a3e -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

###### A.6.1.1.3.2.6.1.3.1.1.3 - Solana - Kamino USDT Instance Configuration Document [Core]  <!-- UUID: 4adbf528-4a16-496c-974f-ce612af69162 -->

The documents herein contain the Instance Configuration Document for the Kamino USDT Instance.

###### A.6.1.1.3.2.6.1.3.1.1.3.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 1c188d86-597d-414b-bb2f-8cc6250303d0 -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.1.3.2 - Parameters [Core]  <!-- UUID: d10c9266-b16b-4914-aba8-796acda503d0 -->

The documents herein define the parameters of the Kamino USDT Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 52324ef9-2f4b-4774-8b67-0cd4397c8194 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.1.3.2.1.1 - Network [Core]  <!-- UUID: 3597fd3c-b4ed-4d7b-b4fa-74c816879966 -->

Solana

###### A.6.1.1.3.2.6.1.3.1.1.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 54e8166d-a2fd-42b6-a716-5a342c4f6f86 -->

Kamino

###### A.6.1.1.3.2.6.1.3.1.1.3.2.1.3 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: 68d30595-356b-4ca3-a820-91a96fd7ac88 -->

USDT

###### A.6.1.1.3.2.6.1.3.1.1.3.2.1.4 - Market [Core]  <!-- UUID: 704864d1-80d7-4e63-8389-ef58bac891f7 -->

Main

###### A.6.1.1.3.2.6.1.3.1.1.3.2.1.5 - Token [Core]  <!-- UUID: 99b7437e-97a0-4788-828e-bfc3ed5a2d29 -->

kUSDT

###### A.6.1.1.3.2.6.1.3.1.1.3.2.2 - Contract Addresses [Core]  <!-- UUID: 7c2ea693-828d-4c7a-9cfb-c6ae164622af -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.1.3.2.2.1 - Token Address [Core]  <!-- UUID: 916d9d97-14f4-4e03-b7ae-fe81a69b664b -->

`B8zf4kojJbwgCRKA7rLaLhRCZBGhgAJp8wPBVZZHMhSv`

###### A.6.1.1.3.2.6.1.3.1.1.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: e14b47e9-9da0-475d-bfe7-001a7339f745 -->

`Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`

###### A.6.1.1.3.2.6.1.3.1.1.3.2.3 - Rate Limit Information [Core]  <!-- UUID: 4ce2bc6f-e280-4056-9d0c-d640a722fadb -->

The specific `Integration` account contains the rate limit information to control inflows into the Kamino USDT Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.3.2.3.1 - Integration Account Address [Core]  <!-- UUID: 77b012a2-0e1f-4674-9984-86ac5eb2b53c -->

`ArpjQUCqHvtDQZFR2tFbPPEKYiQHuaJkcFQBdW5NQC4U`

###### A.6.1.1.3.2.6.1.3.1.1.3.2.4 - Rate Limits [Core]  <!-- UUID: 522805d9-5d8c-4147-ab77-f7472512852e -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.1.3.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 7168f4a2-c928-41f5-a4c9-8a8da5fbd2d1 -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 USDT
- `slope`: 10,000,000 USDT per day

###### A.6.1.1.3.2.6.1.3.1.1.3.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: bdbed1a4-1957-442f-b6b6-f68ccb2c372a -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.1.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: d00abdfb-bc4b-476a-9962-06469889ace7 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.1.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 7c687440-6b84-40a7-8fa1-db0d15a33309 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

###### A.6.1.1.3.2.6.1.3.1.1.4 - Solana - Kamino USDG Instance Configuration Document [Core]  <!-- UUID: 8b972495-2f93-4d88-b1f4-d447e2d821a3 -->

The documents herein contain the Instance Configuration Document for the Kamino USDG Instance.

###### A.6.1.1.3.2.6.1.3.1.1.4.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 65169498-1d46-4f29-8144-535eb26bd9b2 -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.1.4.2 - Parameters [Core]  <!-- UUID: a37d7fbb-8326-4419-8d1d-7056ec48254a -->

The documents herein define the parameters of the Kamino USDG Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.4.2.1 - Instance Identifiers [Core]  <!-- UUID: db7a0534-1a4b-4a75-af13-5e1af34a5726 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.1.4.2.1.1 - Network [Core]  <!-- UUID: f2493a5e-7bd7-42f3-8f8a-9e8d2f526d71 -->

Solana

###### A.6.1.1.3.2.6.1.3.1.1.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 71c5639c-26e8-4ea5-b99f-46208feca2b1 -->

Kamino

###### A.6.1.1.3.2.6.1.3.1.1.4.2.1.3 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: 4ec9542e-700c-4e1f-b25d-33823fa13f54 -->

USDG

###### A.6.1.1.3.2.6.1.3.1.1.4.2.1.4 - Market [Core]  <!-- UUID: de1bbb96-f280-4d42-9aa7-dacb6474d6a1 -->

Main

###### A.6.1.1.3.2.6.1.3.1.1.4.2.1.5 - Token [Core]  <!-- UUID: 1416747d-d36c-48d8-ad9c-45c9c538788b -->

kUSDG

###### A.6.1.1.3.2.6.1.3.1.1.4.2.2 - Contract Addresses [Core]  <!-- UUID: 1d1fc05b-ac3c-4991-a3c1-3b90f8eaad29 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.1.4.2.2.1 - Token Address [Core]  <!-- UUID: 852f18fd-9ca0-4d7c-8f5b-4ce1adf6e447 -->

`BG6gsv8goyoJguEbLquUZFNiZ8aGTXgo4DyH9h8z9qao`

###### A.6.1.1.3.2.6.1.3.1.1.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 96e864d5-57b9-44e7-9b9b-5de29477569d -->

`2u1tszSeqZ3qBWF3uNGPFc8TzMk2tdiwknnRMWGWjGWH`

###### A.6.1.1.3.2.6.1.3.1.1.4.2.3 - Rate Limit Information [Core]  <!-- UUID: 07f18f84-22d3-468d-8a2d-5874ec703a23 -->

The specific `Integration` account contains the rate limit information to control inflows into the Kamino USDG Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.4.2.3.1 - Integration Account Address [Core]  <!-- UUID: 2857d96b-1196-48a5-9983-b629f708d75a -->

`5JYk4vbZTFcBiHK5HzQTmYcT6kosEKJV62tYTCTpT6xy`

###### A.6.1.1.3.2.6.1.3.1.1.4.2.4 - Rate Limits [Core]  <!-- UUID: 1e88d799-a269-44e7-9ce4-2b3f871ece01 -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.1.4.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: bbb53065-3606-45db-9c40-d49cfa6193e3 -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 USDG
- `slope`: 10,000,000 USDG per day

###### A.6.1.1.3.2.6.1.3.1.1.4.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 5af501f7-f554-4b02-9cf0-742fa8aeee82 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.1.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 1c475afa-a3ed-4b6f-99ee-ec1073880484 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.1.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 770281c7-e626-4f05-8c64-0f0af533a7ea -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

###### A.6.1.1.3.2.6.1.3.1.1.5 - Solana - Kamino PYUSD Instance Configuration Document [Core]  <!-- UUID: dd6cf5ec-6ccd-46af-9c4e-0858f79948f7 -->

The documents herein contain the Instance Configuration Document for the Kamino PYUSD Instance.

###### A.6.1.1.3.2.6.1.3.1.1.5.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 951520fb-c20b-4962-82fa-b41a5a3ae4d3 -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.1.5.2 - Parameters [Core]  <!-- UUID: 6f476ccf-09ce-4390-8ca0-8e92cd089fb3 -->

The documents herein define the parameters of the Kamino PYUSD Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.5.2.1 - Instance Identifiers [Core]  <!-- UUID: d9eb7260-03e4-4a82-9d7c-c3cd5c6e5bdb -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.1.5.2.1.1 - Network [Core]  <!-- UUID: ff242d99-5c3c-439c-a02a-751781177aef -->

Solana

###### A.6.1.1.3.2.6.1.3.1.1.5.2.1.2 - Target Protocol [Core]  <!-- UUID: 267fcf21-2917-45d3-a7fa-ee55bcfe78b9 -->

Kamino

###### A.6.1.1.3.2.6.1.3.1.1.5.2.1.3 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: cb3adf9b-1ab7-40c4-b7d2-52a457af1048 -->

PYUSD

###### A.6.1.1.3.2.6.1.3.1.1.5.2.1.4 - Market [Core]  <!-- UUID: 7e4fe3c6-f252-4ee2-abb8-fbf2faa1b54c -->

Main

###### A.6.1.1.3.2.6.1.3.1.1.5.2.1.5 - Token [Core]  <!-- UUID: a54c7a30-48e2-4512-8541-4d87be565f13 -->

kPYUSD

###### A.6.1.1.3.2.6.1.3.1.1.5.2.2 - Contract Addresses [Core]  <!-- UUID: 5309d275-c87d-47e0-9323-a1150b2d9453 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.1.5.2.2.1 - Token Address [Core]  <!-- UUID: b2442469-85ca-4458-a2b9-fa11ae1c9022 -->

`2dQkXr1e9LBvT2QcfKrzZaWY6gGAAVoCjLgkWFk3Mhkj`

###### A.6.1.1.3.2.6.1.3.1.1.5.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 6bca9d2a-c670-431c-b48d-3bfb3a6055e0 -->

`2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo`

###### A.6.1.1.3.2.6.1.3.1.1.5.2.3 - Rate Limit Information [Core]  <!-- UUID: 2da72590-96a3-4ad7-a346-0a07034356d8 -->

The specific `Integration` account contains the rate limit information to control inflows into the Kamino PYUSD Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.1.5.2.3.1 - Integration Account Address [Core]  <!-- UUID: 627adb56-d243-42e7-8268-579c417db818 -->

`9DULRsF4Cfj2BbYZp9n6deLf16yYnR5EcFicvzLNMC2s`

###### A.6.1.1.3.2.6.1.3.1.1.5.2.4 - Rate Limits [Core]  <!-- UUID: cb14e916-8015-46a0-812c-be780edec54f -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.1.5.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: e9130658-124d-4788-8c2d-6a4352276bd2 -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 PYUSD
- `slope`: 10,000,000 PYUSD per day

###### A.6.1.1.3.2.6.1.3.1.1.5.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 86989052-581b-4b06-b906-f8b85e661b64 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.1.5.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: b8b3c21f-e712-46cf-b36a-79b0682f107f -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.1.5.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 54403309-9bbe-4cac-bc6c-22cfc7ea9748 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

###### A.6.1.1.3.2.6.1.3.1.2 - Drift [Core]  <!-- UUID: 94351aff-0a88-4d30-a954-f710b136e32e -->

The Solana Instances of the Drift Protocol with `Active` Status are stored herein.

###### A.6.1.1.3.2.6.1.3.1.2.1 - Solana - Drift USDS Instance Configuration Document [Core]  <!-- UUID: 5e934067-e691-4247-bfa1-7df9d4625f21 -->

The documents herein contain the Instance Configuration Document for the Drift USDS Instance.

###### A.6.1.1.3.2.6.1.3.1.2.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 5a8a55c4-3e8a-4f08-9a28-4e125b4b5dc0 -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.2.1.2 - Parameters [Core]  <!-- UUID: 60970f9a-c632-462f-b3c9-83c33899b48c -->

The documents herein define the parameters of the Drift USDS Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 12d6850f-1d4c-4eb7-9bf6-a3686534930a -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.2.1.2.1.1 - Network [Core]  <!-- UUID: 2c80a41b-04ce-4dd9-9d9e-e02f4ed04222 -->

Solana

###### A.6.1.1.3.2.6.1.3.1.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 1db37f5c-f9f9-4ab3-b3b8-98095c22a145 -->

Drift

###### A.6.1.1.3.2.6.1.3.1.2.1.2.1.3 - Market [Core]  <!-- UUID: 68739838-07ae-49d6-9f9b-699a06478e31 -->

Main

###### A.6.1.1.3.2.6.1.3.1.2.1.2.1.4 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: d44bb449-b540-4e7c-8e81-f5781ea9fb7c -->

USDS

###### A.6.1.1.3.2.6.1.3.1.2.1.2.1.5 - Token [Core]  <!-- UUID: ef18b85f-9ba1-4877-b488-4f4c254f2ec7 -->

N/A

###### A.6.1.1.3.2.6.1.3.1.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: 89f44d6a-c066-47d7-9411-4d1b733ff69e -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.2.1.2.2.1 - Token Address [Core]  <!-- UUID: 0c03ae38-d4cb-4d24-9e7a-74dcc077367a -->

N/A

###### A.6.1.1.3.2.6.1.3.1.2.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 1ef8c53e-e019-45ee-a91e-76e32c324a36 -->

`USDSwr9ApdHk5bvJKMjzff41FfuX8bSxdKcR81vTwcA`

###### A.6.1.1.3.2.6.1.3.1.2.1.2.3 - Rate Limit Information [Core]  <!-- UUID: 1bd446ed-d9e7-41a0-89c2-40291f9c0e36 -->

The specific `Integration` account contains the rate limit information to control inflows into the Drift USDS Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.2.1.2.3.1 - Integration Account Address [Core]  <!-- UUID: 19468eb6-4192-4db4-9289-b3110b296b29 -->

`DFrV1Nyfvoucz3nofVRGFmhWAxV1qz1xQxz5rQi4MNot`

###### A.6.1.1.3.2.6.1.3.1.2.1.2.4 - Rate Limits [Core]  <!-- UUID: e9d53583-526e-441e-87a6-79038aad553e -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.2.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 305929f9-e0f3-494e-9679-264ca1d6026c -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 USDS
- `slope`: 10,000,000 USDS per day

###### A.6.1.1.3.2.6.1.3.1.2.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 09c83fd0-73ec-482b-8c87-bee7c0e5e57b -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: b03fa016-bec9-45b5-accb-b1edec40114a -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: c2bc44bc-1c9e-46d1-977f-abe117105d88 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

###### A.6.1.1.3.2.6.1.3.1.2.2 - Solana - Drift USDC Instance Configuration Document [Core]  <!-- UUID: ddf9f671-bf5c-4f21-af92-63cce7815af4 -->

The documents herein contain the Instance Configuration Document for the Drift USDC Instance.

###### A.6.1.1.3.2.6.1.3.1.2.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 1cf7cf5e-c80f-43d6-bfa8-2b9088c5745d -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.2.2.2 - Parameters [Core]  <!-- UUID: 4f7d5f5c-7d07-4aa6-a5c4-f3a25e67135d -->

The documents herein define the parameters of the Drift USDC Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.2.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 154f31f7-6c8b-4948-b8f3-377e64b14bfb -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.2.2.2.1.1 - Network [Core]  <!-- UUID: 36b5102d-817e-4b01-8dcb-f0d1c31578a4 -->

Solana

###### A.6.1.1.3.2.6.1.3.1.2.2.2.1.2 - Target Protocol [Core]  <!-- UUID: d814206c-ecbb-4e0d-b404-a5946f76f429 -->

Drift

###### A.6.1.1.3.2.6.1.3.1.2.2.2.1.3 - Market [Core]  <!-- UUID: 4fce1780-e418-4080-9e19-4b7cba7b7d9b -->

Main

###### A.6.1.1.3.2.6.1.3.1.2.2.2.1.4 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: 2378b485-cdcf-4417-b283-a5ca2462ef27 -->

USDC

###### A.6.1.1.3.2.6.1.3.1.2.2.2.1.5 - Token [Core]  <!-- UUID: b486d70e-c793-41b8-a70b-e4b8e71276b0 -->

N/A

###### A.6.1.1.3.2.6.1.3.1.2.2.2.2 - Contract Addresses [Core]  <!-- UUID: 5642e99a-b127-4e2c-8055-66cfdae46972 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.2.2.2.2.1 - Token Address [Core]  <!-- UUID: 63026c1f-8a06-4cb4-9bcc-6509bda69cc6 -->

N/A

###### A.6.1.1.3.2.6.1.3.1.2.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: f8f92260-eda4-484c-ae9e-ab74174f7572 -->

`EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

###### A.6.1.1.3.2.6.1.3.1.2.2.2.3 - Rate Limit Information [Core]  <!-- UUID: 963b3617-57ac-4ebb-a240-ed186225d16e -->

The specific `Integration` account contains the rate limit information to control inflows into the Drift USDC Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.2.2.2.3.1 - Integration Account Address [Core]  <!-- UUID: 69610d1d-df89-4169-966e-808d96b35044 -->

`ET3k7uBeXLmeVQW5Tm8xBnLte9FgUSRebgneT57wjuqL`

###### A.6.1.1.3.2.6.1.3.1.2.2.2.4 - Rate Limits [Core]  <!-- UUID: b722ec68-1d66-49c7-a728-e64e3667059e -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.2.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 7268c2b8-b83b-480c-a51a-66e15e66d4f3 -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 USDC
- `slope`: 10,000,000 USDC per day

###### A.6.1.1.3.2.6.1.3.1.2.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: f2c12b28-6cea-400e-af47-f8c0acade37e -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.2.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 72896ba0-86c9-4291-b8a7-95de8f76acc5 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.2.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 074a32ed-ca95-4dea-b9de-10dcc9e2b02c -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

###### A.6.1.1.3.2.6.1.3.1.2.3 - Solana - Drift USDT Instance Configuration Document [Core]  <!-- UUID: 300e6f12-800f-4f55-900b-a0697acfb257 -->

The documents herein contain the Instance Configuration Document for the Drift USDT Instance.

###### A.6.1.1.3.2.6.1.3.1.2.3.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: f8408ed4-839d-481b-8099-8756d568c91c -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.2.3.2 - Parameters [Core]  <!-- UUID: 55df082a-1982-4880-8e45-d3c3309008fd -->

The documents herein define the parameters of the Drift USDT Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.2.3.2.1 - Instance Identifiers [Core]  <!-- UUID: f3c5a79b-f87f-4d5c-8df2-dad8d6ad6a50 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.2.3.2.1.1 - Network [Core]  <!-- UUID: ce9ee0fb-2f77-4cc7-a1b7-accaf3426521 -->

Solana

###### A.6.1.1.3.2.6.1.3.1.2.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 782880a8-2b84-400c-91f3-2048004c74f2 -->

Drift

###### A.6.1.1.3.2.6.1.3.1.2.3.2.1.3 - Market [Core]  <!-- UUID: f5a6429e-f8c4-4606-8e41-c24efb324129 -->

Main

###### A.6.1.1.3.2.6.1.3.1.2.3.2.1.4 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: 1cfaeb94-1d8f-40ca-8e03-59684c39ce09 -->

USDT

###### A.6.1.1.3.2.6.1.3.1.2.3.2.1.5 - Token [Core]  <!-- UUID: 932d4502-14fe-49d5-adfe-4a5835784e55 -->

N/A

###### A.6.1.1.3.2.6.1.3.1.2.3.2.2 - Contract Addresses [Core]  <!-- UUID: 8862cc3f-cbfa-4781-989a-e7bc5914610a -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.2.3.2.2.1 - Token Address [Core]  <!-- UUID: 04ab961e-8169-457c-887f-9427909910bc -->

N/A

###### A.6.1.1.3.2.6.1.3.1.2.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: fb3ea256-b870-475a-82d9-5c1223154c87 -->

`Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`

###### A.6.1.1.3.2.6.1.3.1.2.3.2.3 - Rate Limit Information [Core]  <!-- UUID: 2537cc72-26f4-44d5-9b87-8cd6fa6c6f55 -->

The specific `Integration` account contains the rate limit information to control inflows into the Drift USDT Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.2.3.2.3.1 - Integration Account Address [Core]  <!-- UUID: 5eb625d1-f3ea-4b5a-99ab-0fd668aeb19f -->

`Gb8TLtzWtUVVm5VaEXeZS7hdeXMc675PBvWimeep6aU1`

###### A.6.1.1.3.2.6.1.3.1.2.3.2.4 - Rate Limits [Core]  <!-- UUID: c9fcbc68-412f-4c62-a59d-a100ccb1e9f2 -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.2.3.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 7ad9224b-5ad1-4aa5-9249-11823d8fdd39 -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 USDT
- `slope`: 10,000,000 USDT per day

###### A.6.1.1.3.2.6.1.3.1.2.3.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: fdb802a9-5100-4951-b9d6-a7307e2c8cbe -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.2.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: d7c17775-2373-4214-b125-3f9ff3055b54 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.2.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: a276dc64-2505-43fa-a3d5-82cebeaeabff -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

###### A.6.1.1.3.2.6.1.3.1.2.4 - Solana - Drift PYUSD Instance Configuration Document [Core]  <!-- UUID: ea272eb2-0ffd-4704-a02c-ee4f047cb8a3 -->

The documents herein contain the Instance Configuration Document for the Drift PYUSD Instance.

###### A.6.1.1.3.2.6.1.3.1.2.4.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 10cda4cd-9cdc-45f8-a63f-094abe5adc3b -->

**`Pending`**

###### A.6.1.1.3.2.6.1.3.1.2.4.2 - Parameters [Core]  <!-- UUID: 8387df83-2229-4b49-bd90-142c370c550d -->

The documents herein define the parameters of the Drift PYUSD Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.2.4.2.1 - Instance Identifiers [Core]  <!-- UUID: f332c28d-9fa7-4d29-bddf-c9367265fa0e -->

The documents herein define the Instance identifiers.

###### A.6.1.1.3.2.6.1.3.1.2.4.2.1.1 - Network [Core]  <!-- UUID: cd79375b-5836-4661-8272-08c5a64403a8 -->

Solana

###### A.6.1.1.3.2.6.1.3.1.2.4.2.1.2 - Target Protocol [Core]  <!-- UUID: a9ce9a01-ab10-49fa-915a-9045a9d175a1 -->

Drift

###### A.6.1.1.3.2.6.1.3.1.2.4.2.1.3 - Market [Core]  <!-- UUID: cefe0e20-f880-43d6-b447-31df98c89646 -->

Main

###### A.6.1.1.3.2.6.1.3.1.2.4.2.1.4 - Asset Supplied By Keel Liquidity Layer [Core]  <!-- UUID: dce9457e-6054-4230-a28b-ad9db2705cf9 -->

PYUSD

###### A.6.1.1.3.2.6.1.3.1.2.4.2.1.5 - Token [Core]  <!-- UUID: 6bff132c-66c9-43c9-a0fb-88f558b41829 -->

N/A

###### A.6.1.1.3.2.6.1.3.1.2.4.2.2 - Contract Addresses [Core]  <!-- UUID: 217ebbef-bf36-4636-b61c-3751b2d56065 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.3.2.6.1.3.1.2.4.2.2.1 - Token Address [Core]  <!-- UUID: 67e955f5-75d9-4428-8f10-4ffe48fdc933 -->

N/A

###### A.6.1.1.3.2.6.1.3.1.2.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: d4cbf289-dd54-43ad-b608-35eb7a71b49e -->

`2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo`

###### A.6.1.1.3.2.6.1.3.1.2.4.2.3 - Rate Limit Information [Core]  <!-- UUID: 9f4549ed-69c5-4660-a8da-9648cecf5836 -->

The specific `Integration` account contains the rate limit information to control inflows into the Drift PYUSD Instance of the Allocation System Primitive.

###### A.6.1.1.3.2.6.1.3.1.2.4.2.3.1 - Integration Account Address [Core]  <!-- UUID: 9d7cc1c8-9ad0-4cc2-84ad-9e54687eb60d -->

`5rqJu2NrbMBnW2B2mejSPUV589gb7pvHSGrWQyQqnQz5`

###### A.6.1.1.3.2.6.1.3.1.2.4.2.4 - Rate Limits [Core]  <!-- UUID: 715c3865-bf52-41cd-84e3-d57508c27b5f -->

The current `maxAmount` and `slope` for this conduit’s deposit and withdrawal are defined in the subdocuments herein.

###### A.6.1.1.3.2.6.1.3.1.2.4.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: f888618b-acc1-4ef8-9e02-d292448da6f0 -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 PYUSD
- `slope`: 10,000,000 PYUSD per day

###### A.6.1.1.3.2.6.1.3.1.2.4.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 074d5acf-8e9c-40bc-a1a0-f31bafb4f3b6 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.3.2.6.1.3.1.2.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 474e5b21-e27b-466d-b337-3a4b205d1f96 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.3.2.6.1.3.1.2.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: d05923ef-0b89-4870-a080-920a6e81f417 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Keel Liquidity Layer processes.

##### A.6.1.1.3.2.6.1.4 - Completed Instances [Core]  <!-- UUID: a1286844-4299-49fd-b744-51b8a0c84494 -->

The Instances of the Keel Liquidity Layer with `Completed` Status are stored herein.

##### A.6.1.1.3.2.6.1.5 - In Progress Invocations [Core]  <!-- UUID: 712b3441-b303-4296-8f07-dc298109308e -->

The in progress Invocations of the Allocation System Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.6.1.3 - Active Instances](b9316097-ab93-4a8b-aa51-1e44ceb69c4d).

#### A.6.1.1.3.2.6.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: af316389-e11d-4205-a14e-bb3c230ba2b5 -->

The documents herein contain all data and specifications for Keel’s Instances of the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.6.1.1.3.2.6.2.1 - Primitive Hub Document [Core]  <!-- UUID: fcf3b78f-e91e-45f2-bd4d-14c1a3a97c1f -->

The documents herein organize all base information relevant to Keel’s usage of the Risk Capital Rental Primitive.

###### A.6.1.1.3.2.6.2.1.1 - Global Activation Status [Core]  <!-- UUID: 45fe1729-7481-4215-8399-dd9718e37abf -->

`Inactive`

###### A.6.1.1.3.2.6.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 9264bed6-21a2-4e39-8546-0ab157380740 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.6.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7585f2d5-a12a-4526-9dbd-88fb210dd4aa -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.6.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 23138f00-8867-4b18-81fa-713007909f8f -->

This document contains a Directory of all prospective Instances of the Risk Capital Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.6.2.2 - Active Instances](ee196317-63fc-4f69-a985-2a4f5a5be4e5), whereas failed Invocations are Archived in [A.6.1.1.3.2.6.2.1.5 - Hub Data Repository](74b8a03c-e123-4517-9c60-f445fc958174).

###### A.6.1.1.3.2.6.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 74b8a03c-e123-4517-9c60-f445fc958174 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.6.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 67e1b1e7-eb74-4b14-a125-0e9245266878 -->

The subtrees for archived Invocations and Instances of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.3.2.6.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 45ecc8cb-5ae7-4ea3-9edf-d1ac8ce2b860 -->

The subtrees for failed Invocations of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.3.2.6.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 50cf8700-8938-4dce-b7b5-4dfc3bd92836 -->

The subtrees for Instances of the Risk Capital Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.6.2.2 - Active Instances [Core]  <!-- UUID: ee196317-63fc-4f69-a985-2a4f5a5be4e5 -->

The Instances of the Risk Capital Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.6.2.3 - Completed Instances [Core]  <!-- UUID: 14b1b9d8-c60a-4cb5-a06b-a059f354bcec -->

The Instances of the Risk Capital Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.3.2.6.2.4 - In Progress Invocations [Core]  <!-- UUID: 2b4b1b5a-e6a7-4743-9263-0fa8872d2f68 -->

The in progress Invocations of the Risk Capital Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.6.2.2 - Active Instances](ee196317-63fc-4f69-a985-2a4f5a5be4e5).

#### A.6.1.1.3.2.6.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: d12e1955-a592-4cf8-8b98-24ccfb431409 -->

The documents herein contain all data and specifications for Keel’s Instances of the Asset Liability Management Rental Primitive. See [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

##### A.6.1.1.3.2.6.3.1 - Primitive Hub Document [Core]  <!-- UUID: df75861d-ff07-4d63-9d39-f43bfb2b5b75 -->

The documents herein organize all base information relevant to Keel’s usage of the Asset Liability Management Rental Primitive.

###### A.6.1.1.3.2.6.3.1.1 - Global Activation Status [Core]  <!-- UUID: 029950f2-bacc-4941-9ebe-b7c6770dbb1b -->

`Inactive`

###### A.6.1.1.3.2.6.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 7b21f5bd-68dd-4cf6-8048-cb5eef547b47 -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.6.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 793d20ec-54b7-4f18-9da5-5ecc864eec06 -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.6.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: d0c0850d-9f45-4d6c-bc22-b191a41d1e2a -->

This document contains a Directory of all prospective Instances of the Asset Liability Management Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.6.3.2 - Active Instances](537fef57-4e7f-49d7-ac58-b23ed98aff7c), whereas failed Invocations are Archived in [A.6.1.1.3.2.6.3.1.5 - Hub Data Repository](ce1d1572-7f0f-45d2-9f08-2eaae70c7b61).

###### A.6.1.1.3.2.6.3.1.5 - Hub Data Repository [Core]  <!-- UUID: ce1d1572-7f0f-45d2-9f08-2eaae70c7b61 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.6.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: b315b2ed-16b0-4abd-ad83-693c3252fbdc -->

The subtrees for archived Invocations and Instances of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.3.2.6.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 8f99b878-ab18-44f3-aaeb-43fb443b7798 -->

The subtrees for failed Invocations of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.3.2.6.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 93503a72-77c3-4701-b545-3c0f3700ecd2 -->

The subtrees for Instances of the Asset Liability Management Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.6.3.2 - Active Instances [Core]  <!-- UUID: 537fef57-4e7f-49d7-ac58-b23ed98aff7c -->

The Instances of the Asset Liability Management Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.6.3.3 - Completed Instances [Core]  <!-- UUID: 2b2af026-ff7e-476b-aa1a-e77eb1fc667a -->

The Instances of the Asset Liability Management Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.3.2.6.3.4 - In Progress Invocations [Core]  <!-- UUID: 9663607e-e54c-49fb-941f-a1fa5d91542b -->

The in progress Invocations of the Asset Liability Management Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.6.3.2 - Active Instances](537fef57-4e7f-49d7-ac58-b23ed98aff7c).

### A.6.1.1.3.2.7 - Core Governance Primitives [Core]  <!-- UUID: a99ec5d3-25e3-4391-8914-3ee55203218f -->

The documents herein implement the Core Governance Primitives for Keel. See [A.2.2.11 - Core Governance Primitives](6fa54611-c744-4b9d-897d-b2a20e9cae5d).

#### A.6.1.1.3.2.7.1 - Core Governance Reward Primitive [Core]  <!-- UUID: a3d5bf7f-19fd-47d8-8815-6eb03b9bee1d -->

The documents herein contain all data and specifications for Keel’s Instances of the Core Governance Reward Primitive. See [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a).

##### A.6.1.1.3.2.7.1.1 - Primitive Hub Document [Core]  <!-- UUID: 0841bc09-e502-4a45-a5fc-e30d793a423f -->

The documents herein organize all base information relevant to Keel’s usage of the Core Governance Reward Primitive.

###### A.6.1.1.3.2.7.1.1.1 - Global Activation Status [Core]  <!-- UUID: 2aa1d719-9af8-47db-a190-d43677ef0e28 -->

`Inactive`

###### A.6.1.1.3.2.7.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 11bc952d-781a-439b-9760-83a007fb9dd2 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Active`.

###### A.6.1.1.3.2.7.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: fc74cce7-ae3b-4ab8-8d4d-cc0f7636c523 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.3.2.7.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 66c63d9c-6bb6-44b7-a754-29a15475e4c0 -->

This document contains a Directory of all prospective Instances of the Core Governance Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.3.2.7.1.2 - Active Instances](0b4cc335-c2ed-4b7f-8cb5-eeb1bab394b8), whereas failed Invocations are Archived in [A.6.1.1.3.2.7.1.1.5 - Hub Data Repository](3ab2001f-f1eb-4249-852c-96604a85e987).

###### A.6.1.1.3.2.7.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 3ab2001f-f1eb-4249-852c-96604a85e987 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.3.2.7.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 5e66b56a-fe9d-4d4c-94c6-2d919171e924 -->

The subtrees for archived Invocations and Instances of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.3.2.7.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 6794a591-d126-42b6-ba59-c61c3c7e9486 -->

The subtrees for failed Invocations of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.3.2.7.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: c84bc632-6972-443a-a02c-f2b45a3678ac -->

The subtrees for Instances of the Core Governance Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.3.2.7.1.2 - Active Instances [Core]  <!-- UUID: 0b4cc335-c2ed-4b7f-8cb5-eeb1bab394b8 -->

The Instances of the Core Governance Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.3.2.7.1.3 - Completed Instances [Core]  <!-- UUID: d4d144fb-eaf6-40ab-90c2-e86dc9494a42 -->

The Instances of the Core Governance Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.3.2.7.1.4 - In Progress Invocations [Core]  <!-- UUID: 6a200f7a-611d-4969-8046-6b5b88f6979a -->

The in progress Invocations of the Core Governance Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.3.2.7.1.2 - Active Instances](0b4cc335-c2ed-4b7f-8cb5-eeb1bab394b8).

## A.6.1.1.3.3 - Omni Documents [Core]  <!-- UUID: bafbbf28-95dc-41a4-9c55-f3befde4e991 -->

The documents herein define Keel’s strategic intent and operational processes relating to infrastructure inherited from Sky Core, activities unrelated to Sky Primitives, or activities spanning multiple Sky Primitives.

### A.6.1.1.3.3.1 - Governance Information Unrelated To Root Edit Primitive [Core]  <!-- UUID: 1889a2a0-7378-487a-a278-aabe3177efff -->

The documents herein specify Keel governance information that is unrelated to the use of the Root Edit Primitive. The governance process for updating the Keel Artifact is specified in the Root Edit Primitive above at [A.6.1.1.3.2.2.2 - Root Edit Primitive](3d02dcbc-6a31-4f63-b464-c8c3ecebb744).

#### A.6.1.1.3.3.1.1 - Sky Forum [Core]  <!-- UUID: 63fec69d-a4df-42c3-bb5f-b959e711df56 -->

Keel uses the Sky Forum for governance-related discussion. Posts should use the "Keel Prime" category.

#### A.6.1.1.3.3.1.2 - Sky Ecosystem Emergency Response [Core]  <!-- UUID: 8613cc87-2809-4716-8c91-93ff0345f7a8 -->

The documents herein specify Keel’s emergency response protocol in situations that impact the entire Sky Ecosystem. This protocol will be specified in a future iteration of the Keel Artifact.

#### A.6.1.1.3.3.1.3 - Agent-Specific Emergency Response [Core]  <!-- UUID: ef98d5b6-3542-4b2f-a926-a0648713fa70 -->

The documents herein specify Keel’s emergency response protocol in situations solely impacting Keel versus the broader Sky Ecosystem. This protocol will be specified in a future iteration of the Keel Artifact.

### A.6.1.1.3.3.2 - Use Of Idle Funds [Core]  <!-- UUID: 41ad175e-48c8-4caf-8cb7-638f90ff0ad6 -->

In the short term prior to Keel's implementation of the Allocation System Primitive, Keel may invest idle funds in low-risk decentralized finance opportunities, including providing liquidity to established lending protocols on Solana. These deployments will be subject to the approval of Operational GovOps.

### A.6.1.1.3.3.3 - Ecosystem Accords [Core]  <!-- UUID: e2db688f-a6f1-476a-b7da-dd67d94da35b -->

Keel has formally agreed to the Ecosystem Accords herein.

#### A.6.1.1.3.3.3.1 - Ecosystem Accord 3 [Core]  <!-- UUID: 962d4b79-2dea-4b86-a72f-8a460189327f -->

Keel engaged in terms of agreement with Sky in Ecosystem Accord 3, located in [A.2.8.2.3 - Ecosystem Accord 3: Sky And Keel](63a88b08-e6cd-48bf-9cec-64ce7e42ae0e).
