# A.6.1.1.2 - Grove [Core]  <!-- UUID: 727b0de6-095b-485e-bf9c-02108a364480 -->

The documents herein specify all of the logic for Grove, including Grove’s strategy and how it uses the Sky Primitives to operationalize this strategy.

## A.6.1.1.2.1 - Introduction [Core]  <!-- UUID: 197ef51d-d785-491d-b929-cc659f3f3bb9 -->

Grove is an Agent focused on unlocking the full potential of USDS through higher savings rates and new products and opportunities. Its main focus will be building an institutional-grade credit platform designed to facilitate credit creation and seamlessly move yield in and out of the onchain economy.

## A.6.1.1.2.2 - Sky Primitives [Core]  <!-- UUID: 6b9bbf5e-0a76-4082-a042-811d4c426e6e -->

The documents herein implement the Sky Primitives for Grove. See [A.2.2 - Sky Primitives](fcde2604-a138-4c1b-9d9a-14895835c907).

### A.6.1.1.2.2.1 - Genesis Primitives [Core]  <!-- UUID: 96294c0f-de02-40e1-b2b3-4434116ccfd3 -->

The documents herein implement the Genesis Primitives for Grove. See [A.2.2.5 - Genesis Primitives](3d5e3668-8333-4908-adcc-5784cfe7f6b5).

#### A.6.1.1.2.2.1.1 - Agent Creation Primitive [Core]  <!-- UUID: f1d5f01a-3072-4c73-a039-7dcf19421640 -->

The documents herein contain all data and specifications for Grove’s Instance of the Agent Creation Primitive. See [A.2.2.5.1 - Agent Creation Primitive](82b95f6d-4883-4f08-ac3a-9d8189013fbe).

##### A.6.1.1.2.2.1.1.1 - Primitive Hub Document [Core]  <!-- UUID: 28443b6e-bf44-4a2b-9592-c1b55f2d4679 -->

The documents herein organize all base information relevant to Grove’s usage of the Agent Creation Primitive.

###### A.6.1.1.2.2.1.1.1.1 - Global Activation Status [Core]  <!-- UUID: 7eee7726-9e35-4ed6-83a2-9b2b2ea8e84c -->

`Completed`

###### A.6.1.1.2.2.1.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 9e147616-5d78-4663-b474-eaa4b2b75b46 -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.1.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 8e823923-d5d6-4de9-b007-f9b112477cad -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.1.1.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: fc302db6-8265-4ec8-8139-9d3855411de6 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.1.1.3.1 - Single Instance Configuration Document](ce345522-2e73-4a7b-80f5-40eef6ad3ed1).

###### A.6.1.1.2.2.1.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: ee1648c8-65e9-445e-9a1a-1fd3df03ea61 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.2.2.1.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 729bf0cf-8449-4fea-8510-f93da02ceb45 -->

The document herein contains the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.1.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 33ee18a0-e672-469e-9d4f-3167346810f6 -->

The subtrees for archived Invocations and Instances of the Agent Creation Primitive are stored here.

###### A.6.1.1.2.2.1.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 67170ab4-0ecf-46b4-beca-96668986ccbf -->

The subtrees for failed Invocations of the Agent Creation Primitive are stored here.

###### A.6.1.1.2.2.1.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 81c5fa7b-856b-44fe-a361-2bbce3fbac56 -->

The subtrees for Instances of the Agent Creation Primitive with Suspended Status are stored here.

##### A.6.1.1.2.2.1.1.2 - Active Instances [Core]  <!-- UUID: 2549581e-c635-4389-bb57-0780bb24c37e -->

The Instances of the Agent Creation Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 994395c0-c61d-4fc9-8167-00ee3134bd5a -->

The Instances of the Agent Creation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.2.2.1.1.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: ce345522-2e73-4a7b-80f5-40eef6ad3ed1 -->

The documents herein contain the Instance Configuration Document for the Single Agent Creation Primitive Instance.

###### A.6.1.1.2.2.1.1.3.1.1 - Parameters [Core]  <!-- UUID: 9052b1a5-340b-4f19-a53f-357c4c690411 -->

The documents herein define the parameters of the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.2.2.1.1.3.1.1.1 - Name [Core]  <!-- UUID: 228cadd3-6dc4-4b08-8e57-4022c4f30cba -->

The name of the Agent is Grove.

###### A.6.1.1.2.2.1.1.3.1.1.2 - SubProxy Account [Core]  <!-- UUID: d143241d-5819-432d-a6ba-892961502838 -->

The address of Grove’s SubProxy Account on the Ethereum Mainnet is `0x1369f7b2b38c76B6478c0f0E66D94923421891Ba`.

###### A.6.1.1.2.2.1.1.3.1.1.3 - Genesis Account [Core]  <!-- UUID: 9f6f0416-1efa-4986-aec9-0ee66cd13758 -->

The address of Grove’s Genesis Account will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.1.1.3.1.1.4 - Foundation [Core]  <!-- UUID: 70d75e6f-009f-4ac0-b430-881b86d573ca -->

The Grove Foundation is the Prime Foundation associated with Grove. Its mandate is to support the development, growth, and adoption of Grove.

###### A.6.1.1.2.2.1.1.3.1.1.5 - Development Company [Core]  <!-- UUID: 830f6fb5-1037-4516-9efa-d7101553a3d0 -->

Grove Development Company is a development company that provides services to the Grove Foundation. Grove Development Company is a "Nested Contributor", i.e., a core contributor to both Grove and Sky.

###### A.6.1.1.2.2.1.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 8ff8bfe6-5311-4f5f-9daf-c56219ac0a77 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.2.2.1.1.3.1.3 - Data Repository [Core]  <!-- UUID: db6a125d-1b36-460e-874e-539cfb4ef1a2 -->

The documents herein contain data relevant to the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.2.2.1.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 8d9cbbed-b242-4ed5-8d87-bd9e84c68bc4 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.1.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 36e78589-bf94-4abc-b656-0041afb5062a -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.1.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 528d1e34-12b8-464f-bfbc-13daa1cd5047 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: a7a1d15b-4d7f-4224-adc2-645c9b8dfdcb -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.2.2.1.2 - Prime Transformation Primitive [Core]  <!-- UUID: 815b45f1-a157-482c-967b-472283a5ab29 -->

The documents herein contain all data and specifications for Grove’s Instance of the Prime Transformation Primitive. See [A.2.2.5.2 - Prime Transformation Primitive](81411106-fd6d-4f9c-b3ae-7af7b5e62482).

##### A.6.1.1.2.2.1.2.1 - Primitive Hub Document [Core]  <!-- UUID: 9062717c-fe70-4a96-b063-25fc05bf68da -->

The documents herein organize all base information relevant to Grove’s usage of the Prime Transformation Primitive.

###### A.6.1.1.2.2.1.2.1.1 - Global Activation Status [Core]  <!-- UUID: fb90f38d-0222-4b27-a7f4-b05900306d70 -->

`Completed`

###### A.6.1.1.2.2.1.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 871ce4b9-27e9-40d7-aaad-293223ea2fa6 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.1.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: d448f7ac-6bf5-42b5-94ac-2c1c822b4837 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.1.2.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: e191f839-2e50-46b0-8415-95258bc8c302 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.1.2.3.1 - Single Instance Configuration Document](4661ec23-639b-4fab-b7ff-99a1f6b36aaa).

###### A.6.1.1.2.2.1.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 5ae3059b-9c39-4fe2-8ad9-2d2300dfd280 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.2.2.1.2.1.5 - Hub Data Repository [Core]  <!-- UUID: b9a2b59e-866f-48ab-a34c-dc3368a5ab28 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.1.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e2c36640-249f-467c-82c3-a558c910acc1 -->

The subtrees for archived Invocations and Instances of the Prime Transformation Primitive are stored here.

###### A.6.1.1.2.2.1.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 4db5063a-13c5-400d-9774-dca5147b7653 -->

The subtrees for failed Invocations of the Prime Transformation Primitive are stored here.

###### A.6.1.1.2.2.1.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 04b81008-b4f3-4b5b-a59c-c075e2c12d10 -->

The subtrees for Instances of the Prime Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.1.2.2 - Active Instances [Core]  <!-- UUID: 6131c7e6-63e8-40fc-91f7-a1d873ceeeff -->

The Instances of the Prime Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.1.2.3 - Completed Instances [Core]  <!-- UUID: 442e6d79-7f69-48ae-8758-05347b5efb7c -->

The Instances of the Prime Transformation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.2.2.1.2.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 4661ec23-639b-4fab-b7ff-99a1f6b36aaa -->

The documents herein contain the Instance Configuration Document for the Single Prime Transformation Primitive Instance.

###### A.6.1.1.2.2.1.2.3.1.1 - Parameters [Core]  <!-- UUID: 8d62a853-c13b-4c10-93d7-ae10b20a8e9a -->

The documents herein define the parameters of the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.2.2.1.2.3.1.1.1 - Agent Type [Core]  <!-- UUID: b6bd02e4-8e81-43ca-a2c7-2418304e9e6d -->

Grove is a Prime Agent.

###### A.6.1.1.2.2.1.2.3.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 78d2887b-bc52-44e9-9ac1-335491058347 -->

The documents herein define the custom parameters of the Single Instance of the Prime Transformation Primitive, if any.

###### A.6.1.1.2.2.1.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 3bbb10c7-56d8-46f0-b663-40fbf8764967 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.2.2.1.2.3.1.3 - Data Repository [Core]  <!-- UUID: fd32256c-72b5-4435-8fa1-b9de99b14a48 -->

The documents herein contain data relevant to the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.2.2.1.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 51eb148f-c010-4e2a-a977-a6a2cb465e2d -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.1.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 69cbf93f-2d99-4900-af0e-8e5d5609e2ca -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.1.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 4bb102d6-3cdf-41c2-a285-20f2db76902c -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.2.2.1.2.4 - In Progress Invocations [Core]  <!-- UUID: 57c07fc2-51cc-442d-bf1b-326022ae71a2 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.2.2.1.3 - Executor Transformation Primitive [Core]  <!-- UUID: 999bd004-5dfa-40cd-89fe-1957515a0bb5 -->

The documents herein contain all data and specifications for Grove’s Instance of the Executor Transformation Primitive. See [A.2.2.5.3 - Executor Transformation Primitive](2f249be5-8edb-41e4-b429-734e1ba2cbc7).

##### A.6.1.1.2.2.1.3.1 - Primitive Hub Document [Core]  <!-- UUID: 3d4fc87f-c02b-4e39-bbca-8cd90919479a -->

The documents herein organize all base information relevant to Grove’s usage of the Executor Transformation Primitive.

###### A.6.1.1.2.2.1.3.1.1 - Global Activation Status [Core]  <!-- UUID: 1eac6dfe-960d-4625-925b-a4d074d36d4f -->

`Inactive`

###### A.6.1.1.2.2.1.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 84d992af-ac27-49af-806b-2616736987ef -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.1.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 40033336-9318-4a3d-a08e-9ce426ec302b -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.1.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: a653f42c-31ad-48c7-ac25-6ba2c54f8ff3 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.2.2.1.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 07058335-a298-4542-aea3-09959c18746d -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.1.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: fabc93a3-02b4-44a8-9876-c23a5aaa9078 -->

The subtrees for archived Invocations and Instances of the Executor Transformation Primitive are stored here.

###### A.6.1.1.2.2.1.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: adf7addb-1fe6-48a9-bb35-5d6bd6b1b2f0 -->

The subtrees for failed Invocations of the Executor Transformation Primitive are stored here.

###### A.6.1.1.2.2.1.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 23572a29-d807-47f0-ab23-2e538a6d02aa -->

The subtrees for Instances of the Executor Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.1.3.2 - Active Instances [Core]  <!-- UUID: 9bceeba9-9bd7-4f23-91df-9424007e4373 -->

The Instances of the Executor Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.1.3.3 - Completed Instances [Core]  <!-- UUID: d26312b9-a479-476e-ad23-929ee4d7caf0 -->

The Instances of the Executor Transformation Primitive with `Completed` Status are contained herein.

##### A.6.1.1.2.2.1.3.4 - In Progress Invocations [Core]  <!-- UUID: 9c98d05c-bf6a-49fe-9ac2-08c063df8a75 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.2.2.1.4 - Agent Token Primitive [Core]  <!-- UUID: 79d2d527-745b-4fad-88ae-fc9b0d04643d -->

The documents herein contain all data and specifications for Grove’s Instance of the Agent Token Primitive. See [A.2.2.5.4 - Agent Token Primitive](2047c361-db28-4952-a70c-83d07b562064).

##### A.6.1.1.2.2.1.4.1 - Primitive Hub Document [Core]  <!-- UUID: 2bb3fe7a-046f-4109-bd32-2647fa919086 -->

The documents herein organize all base information relevant to Grove’s usage of the Agent Token Primitive.

###### A.6.1.1.2.2.1.4.1.1 - Global Activation Status [Core]  <!-- UUID: 5f7693e2-82d2-4838-9a7b-93cd2521c2b9 -->

`Active`

###### A.6.1.1.2.2.1.4.1.2 - Active Instances Directory [Core]  <!-- UUID: d64f369d-05fc-4f2e-9634-af68df978b19 -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.1.4.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 8a2340d6-0526-45bf-99ac-068a51966ead -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.1.4.2.1 - Single Instance Configuration Document](6d4ca2d6-58be-40ee-84b6-b1983d30f38e).

###### A.6.1.1.2.2.1.4.1.3 - Completed Instances Directory [Core]  <!-- UUID: 216eaced-019f-4a04-bfc3-efc1be763af8 -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.1.4.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 6b2832fe-aaaa-4034-bc3c-821d08cc9a58 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.2.2.1.4.1.5 - Hub Data Repository [Core]  <!-- UUID: 12424c5a-1555-4e1e-9818-1c7eb4eaeec3 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.1.4.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 06eacd45-af50-4bbe-bdad-d44bf806613b -->

The subtrees for archived Invocations and Instances of the Agent Token Primitive are stored here.

###### A.6.1.1.2.2.1.4.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: f8b37bae-f093-41c1-aaa1-6fe2ee608ff0 -->

The subtrees for failed Invocations of the Agent Token Primitive are stored here.

###### A.6.1.1.2.2.1.4.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 1b4e14d7-85b1-4465-825a-71919e6c32a1 -->

The subtrees for Instances of the Agent Token Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.1.4.2 - Active Instances [Core]  <!-- UUID: 8cde8c68-6f3a-467a-8fdb-42665dd322a9 -->

The Instances of the Agent Token Primitive with `Active` Status are stored herein.

###### A.6.1.1.2.2.1.4.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 6d4ca2d6-58be-40ee-84b6-b1983d30f38e -->

The documents herein contain the Instance Configuration Document for the Single Agent Token Primitive Instance.

###### A.6.1.1.2.2.1.4.2.1.1 - Parameters [Core]  <!-- UUID: f4e00e07-2243-4a78-a316-be6ec0ec7d73 -->

The documents herein define the parameters of the Single Instance of the Agent Token Primitive.

###### A.6.1.1.2.2.1.4.2.1.1.1 - Token Name [Core]  <!-- UUID: 6d278d01-23ee-4be2-90aa-19a878f61ac8 -->

The name of Grove’s token is Grove.

###### A.6.1.1.2.2.1.4.2.1.1.2 - Token Symbol [Core]  <!-- UUID: c4aa4ea7-8dfe-411e-9ab8-2c6ace976a78 -->

The symbol of Grove’s token is GROVE.

###### A.6.1.1.2.2.1.4.2.1.1.3 - Genesis Supply [Core]  <!-- UUID: 24ab5d8a-1587-460f-8fd2-19a5558ad7b2 -->

The Genesis Supply of GROVE is 10 billion.

###### A.6.1.1.2.2.1.4.2.1.1.4 - Token Address [Core]  <!-- UUID: 1e92dae7-7e0a-4392-bcbe-3458082eb2ca -->

The address of GROVE on the Ethereum Mainnet is `0xB30FE1Cf884B48a22a50D22a9282004F2c5E9406`.

###### A.6.1.1.2.2.1.4.2.1.1.5 - Token Admin [Core]  <!-- UUID: 6664bb57-161a-4530-805d-38f5eb73751c -->

The Token Admin is Grove’s SubProxy.

###### A.6.1.1.2.2.1.4.2.1.1.6 - Token Emissions [Core]  <!-- UUID: a0325b38-1884-410e-9940-1dc5300cd65d -->

Token emissions beyond the Genesis Supply are permanently disabled; this cannot be reverted by Grove Governance. Sky Governance retains the ability to revert where Grove is in violation of Risk Capital requirements and emissions are required by the Risk Framework. See [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.6.1.1.2.2.1.4.2.1.1.7 - Custom Instance Parameters [Core]  <!-- UUID: 13765437-eb17-450a-bbea-7bf1ec5bc9d3 -->

The documents herein define the custom parameters of the Single Instance of the Agent Token Primitive, if any.

###### A.6.1.1.2.2.1.4.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 330deacc-c7f8-415f-a8cb-244c055b8a3c -->

The documents herein define the operational processes for minting and initial distribution of the tokens from the Genesis Supply.

###### A.6.1.1.2.2.1.4.2.1.2.1 - Minting Of Tokens To Grove Foundation [Core]  <!-- UUID: a9bae1cc-2a92-4465-b7cf-9f97121f7aa7 -->

The Genesis Supply was minted to an account owned by the Grove Foundation. The address of the account on the Ethereum Mainnet is `0x22F443740Aa13e9d9A1Fb3dadfbEAfd3d43099fF`.

###### A.6.1.1.2.2.1.4.2.1.2.2 - Transfer Of Tokens To Sky [Core]  <!-- UUID: 57b9095b-6bea-4d99-ad42-d1a580f611e5 -->

The Grove Foundation transferred 7 billion GROVE tokens from the Grove Foundation account, specified in [A.6.1.1.2.2.1.4.2.1.2.1 - Minting Of Tokens To Grove Foundation](a9bae1cc-2a92-4465-b7cf-9f97121f7aa7), to the Sky Pause Proxy.

###### A.6.1.1.2.2.1.4.2.1.2.3 - Transfer Of Tokens To Grove [Core]  <!-- UUID: fa25a039-762a-4a94-a6dc-1651f7396e75 -->

The Grove Foundation transferred 3 billion GROVE tokens from the Grove Foundation account, specified in [A.6.1.1.2.2.1.4.2.1.2.1 - Minting Of Tokens To Grove Foundation](a9bae1cc-2a92-4465-b7cf-9f97121f7aa7), to the Grove SubProxy. The documents herein specify the subsequent distribution of those tokens from the Grove SubProxy.

###### A.6.1.1.2.2.1.4.2.1.2.3.1 - Transfer Of Tokens To Grove Labs Multisig [Core]  <!-- UUID: ebca156f-a86a-4b40-ab1e-208e6d8f0f39 -->

Grove transferred 2.5 billion GROVE tokens from the Grove SubProxy to the Grove Labs Multisig. The address of the Grove Labs Multisig on the Ethereum Mainnet is `0x1EBC4425B16FD76F01f9260d8bfFE0c2C6ecCe70`.

###### A.6.1.1.2.2.1.4.2.1.2.3.2 - Transfer Of Tokens To Grove Foundation Multisig [Core]  <!-- UUID: 0bff1d91-449d-4fc7-a1c6-ee9e033036a4 -->

Grove will transfer 500 million GROVE tokens from the Grove SubProxy to the Grove Foundation Multisig. The address of the Grove Foundation Multisig on the Ethereum Mainnet is `0xE3EC4CC359E68c9dCE15Bf667b1aD37Df54a5a42`.

###### A.6.1.1.2.2.1.4.2.1.3 - Data Repository [Core]  <!-- UUID: e582003e-4acc-4690-bff8-ddf66209a9cd -->

The documents herein contain data relevant to the Single Instance of the Agent Token Primitive.

###### A.6.1.1.2.2.1.4.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 7f6a1a86-3be4-450f-82fd-3c4b8ffa4c37 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.1.4.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 183d8611-6c51-4b92-ab69-d8cf00b68cb4 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.1.4.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: aefe1e9e-8bcb-4dfd-aa58-05778d4d4326 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.2.2.1.4.3 - Completed Instances [Core]  <!-- UUID: 573d5df7-1147-4735-b3a5-f2fea1c569c7 -->

The Instances of the Agent Token Primitive with `Completed` Status are contained herein.

##### A.6.1.1.2.2.1.4.4 - In Progress Invocations [Core]  <!-- UUID: 4cba9d0d-52fd-4364-89f3-5425f89af772 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

### A.6.1.1.2.2.2 - Operational Primitives [Core]  <!-- UUID: 82f990e4-f44f-47ef-807c-e7a4d6c73a8c -->

The documents herein implement the Operational Primitives for Grove. See [A.2.2.6 - Operational Primitives](0192ec95-9207-480e-8c51-88d2a1da95ad).

#### A.6.1.1.2.2.2.1 - Executor Accord Primitive [Core]  <!-- UUID: e5a70b27-f322-48d8-9970-9d5e68566deb -->

The documents herein contain all data and specifications for Grove’s Instances of the Executor Accord Primitive. See [A.2.2.6.1 - Executor Accord Primitive](88017877-3ec1-4c43-a035-6bebdf11d9bb).

##### A.6.1.1.2.2.2.1.1 - Primitive Hub Document [Core]  <!-- UUID: 456f2f2e-b578-499a-ae8e-52c2dee6651e -->

The documents herein organize all base information relevant to Grove’s usage of the Executor Accord Primitive.

###### A.6.1.1.2.2.2.1.1.1 - Global Activation Status [Core]  <!-- UUID: 84cef275-a189-4413-bacc-c1c1c1c660b3 -->

`Active`

###### A.6.1.1.2.2.2.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 22b27ed2-345c-4c6e-b20a-4da40e763745 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.2.1.1.2.1 - Amatsu Instance Configuration Document Location [Core]  <!-- UUID: 0fee90de-5460-4dea-a9c1-d451271d30e1 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.2.1.2.1 - Amatsu Instance Configuration Document](82aa705b-b3eb-42e1-9a81-e4dfe5d721ad).

###### A.6.1.1.2.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 19bd168f-90bf-4a6f-859f-95c31bd53141 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 163e4dcb-8614-434b-884e-3a20eef260f1 -->

This document contains a Directory of all prospective Instances of the Executor Accord Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.2.1.1.2 - Active Instances Directory](22b27ed2-345c-4c6e-b20a-4da40e763745) , whereas failed Invocations are Archived in [A.6.1.1.2.2.2.1.1.5 - Hub Data Repository](dd89d92c-6aef-4dc6-a218-fe498d4f1756).

###### A.6.1.1.2.2.2.1.1.5 - Hub Data Repository [Core]  <!-- UUID: dd89d92c-6aef-4dc6-a218-fe498d4f1756 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.2.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 2813b706-4058-41f3-bd01-ef27c66007fc -->

The subtrees for archived Invocations and Instances of the Executor Accord Primitive are stored here.

###### A.6.1.1.2.2.2.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 8e572907-768b-4d12-899a-8fcc3c2d600f -->

The subtrees for failed Invocations of the Executor Accord Primitive are stored here.

###### A.6.1.1.2.2.2.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: eb6955b2-cf21-418f-86ed-153fa2faa02b -->

The subtrees for Instances of the Executor Accord Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.2.1.2 - Active Instances [Core]  <!-- UUID: 7da4fef1-0a6b-4ac6-b797-34095d491d04 -->

The Instances of the Executor Accord Primitive with `Active` Status are stored herein.

###### A.6.1.1.2.2.2.1.2.1 - Amatsu Instance Configuration Document [Core]  <!-- UUID: 82aa705b-b3eb-42e1-9a81-e4dfe5d721ad -->

The documents herein contain the Instance Configuration Document for the Amatsu Executor Accord Primitive Instance.

###### A.6.1.1.2.2.2.1.2.1.1 - Parameters [Core]  <!-- UUID: cae448f3-41f3-487c-afe7-981019f9c804 -->

The documents herein define the parameters of the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.2.2.2.1.2.1.1.1 - Operational Executor Agent [Core]  <!-- UUID: cae67502-6f93-462f-82b6-0a6462e71e1c -->

The Operational Facilitator and Operational GovOps for Amatsu are specified in [A.6.1.2.1 - Operational Executor Agent Amatsu](c57df14a-fde0-43f3-89ed-c2e4981d6bd5).

###### A.6.1.1.2.2.2.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 5821d38f-b791-47f1-9c96-9517cd61f848 -->

The documents herein define the custom parameters of the Amatsu Instance of the Executor Accord Primitive, if any.

###### A.6.1.1.2.2.2.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: a00c5047-11d3-432b-9f1d-0745b5321476 -->

The documents herein define the process for the ongoing management of the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.2.2.2.1.2.1.3 - Data Repository [Core]  <!-- UUID: 03f354c3-72b7-4ed5-95c8-0ae8181fd33f -->

The documents herein contain data relevant to the Amatsu Instance of the Executor Accord Primitive.

###### A.6.1.1.2.2.2.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: ccb322ea-75dd-4c19-a95e-fd9d43f92f7a -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.2.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 977891ae-07b1-4330-9ce2-e2ea4a7e4f75 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.2.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: fb51f784-8c62-4bf9-92d1-f47e42c26439 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.2.2.2.1.3 - Completed Instances [Core]  <!-- UUID: bd479d49-6929-4eff-8809-2d440e541748 -->

The Instances of the Executor Accord Primitive with `Completed` Status are stored herein.

##### A.6.1.1.2.2.2.1.4 - In Progress Invocations [Core]  <!-- UUID: 3e6ee2de-3801-49bd-884b-d0b758ea39ca -->

The in progress Invocations of the Executor Accord Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.2.1.2 - Active Instances](7da4fef1-0a6b-4ac6-b797-34095d491d04).

#### A.6.1.1.2.2.2.2 - Root Edit Primitive [Core]  <!-- UUID: da862b9f-ca77-443a-ac56-5a287c50b4db -->

The documents herein contain all data and specifications for Grove’s Instance of the Root Edit Primitive. See [A.2.2.6.2 - Root Edit Primitive](78488c6b-d77f-4344-b954-476e415a2c7d).

##### A.6.1.1.2.2.2.2.1 - Primitive Hub Document [Core]  <!-- UUID: f52af41f-b3a7-4218-bce6-11104e7d941b -->

The documents herein organize all base information relevant to Grove’s usage of the Root Edit Primitive.

###### A.6.1.1.2.2.2.2.1.1 - Global Activation Status [Core]  <!-- UUID: 5e279bef-d668-4023-9096-89116ab51b89 -->

`Active`

###### A.6.1.1.2.2.2.2.1.2 - Active Instances Directory [Core]  <!-- UUID: cc85ca83-3d53-42d4-8cc3-2db2c31c20d7 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.2.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: d67d1089-48c9-4dd5-ba29-48de446f5113 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.2.2.2.1 - Single Instance Configuration Document](31babaee-9849-486f-8631-74a2ca9a7da8).

###### A.6.1.1.2.2.2.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7a112fc5-64c8-4cd9-81c4-9b3fba9eb6aa -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.2.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 4c3bcaca-94f0-4682-a1ab-d61491c04214 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.2.2.2.2.1.5 - Hub Data Repository [Core]  <!-- UUID: be6770ee-2f7c-4845-ac49-8b996ed61d23 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.2.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 9d0c94c8-e109-4885-ab41-3d93f331642b -->

The subtrees for archived Invocations and Instances of the Root Edit Primitive are stored here.

###### A.6.1.1.2.2.2.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: c9217525-b93f-4188-b54c-dbf2430880ea -->

The subtrees for failed Invocations of the Root Edit Primitive are stored here.

###### A.6.1.1.2.2.2.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 7210d615-787f-47a7-930e-0a70157dd891 -->

The subtrees for Instances of the Root Edit Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.2.2.2 - Active Instances [Core]  <!-- UUID: a4332a72-d0a3-4540-9354-d4888100ad9e -->

The Instances of the Root Edit Primitive with `Active` Status are stored herein.

###### A.6.1.1.2.2.2.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 31babaee-9849-486f-8631-74a2ca9a7da8 -->

The documents herein contain the Instance Configuration Document for the Single Root Edit Primitive Instance.

###### A.6.1.1.2.2.2.2.2.1.1 - Parameters [Core]  <!-- UUID: 741abe62-8d1c-4e07-949a-2f81295bc459 -->

The parameters of the Root Edit Primitive are fully specified by the Operational Process Definition in [A.6.1.1.2.2.2.2.2.1.2 - Operational Process Definition](40826926-adb2-4de3-936d-702e2d8cb3b9).

###### A.6.1.1.2.2.2.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 40826926-adb2-4de3-936d-702e2d8cb3b9 -->

The documents herein define the process for using the Root Edit Primitive to update the Grove Agent Artifact. Information on Grove governance that is unrelated to the use of the Root Edit Primitive is located at [A.6.1.1.2.3.1 - Governance Information Unrelated To Root Edit Primitive](c1c86e47-a7db-4080-ab1f-99ed8e4892f7).

###### A.6.1.1.2.2.2.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: d919ea0f-f819-45f3-b065-7f2cbdba5b08 -->

The documents herein define the process for using the Root Edit Primitive to update the Grove Agent Artifact in routine or normal conditions (i.e., non-emergency situations).

###### A.6.1.1.2.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission [Core]  <!-- UUID: e9ae4a8a-3e61-488c-8f8b-d0062f46644d -->

The Root Edit process begins with a GROVE token holder submitting a proposal through the Powerhouse system containing a draft Artifact Edit Proposal. A GROVE token holder must hold at least 1% of the total token supply to submit a proposal. The proposal must also be posted on the Sky Forum under the "Grove Prime" category.

###### A.6.1.1.2.2.2.2.2.1.2.1.1.1 - Root Edit Proposal Submission Requirements Exception For Nested Contributors [Core]  <!-- UUID: 6120ba4b-afcf-49db-9a9a-55e1fd00e933 -->

Nested Contributors are always authorized to submit Artifact Edit Proposals and do not have to fulfill the token-holding requirements defined in [A.6.1.1.2.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](e9ae4a8a-3e61-488c-8f8b-d0062f46644d). However, all other procedural requirements within the Root Edit process continue to apply.

To see the Agent’s Nested Contributors, see [A.6.1.1.2.2.1.1.3.1.1.5 - Development Company](830f6fb5-1037-4516-9efa-d7101553a3d0).

###### A.6.1.1.2.2.2.2.2.1.2.1.1.2 - Short-Term Transitionary Measures [Core]  <!-- UUID: a0b401ae-1ced-43af-ab0b-2eb16b797270 -->

Until the Powerhouse system supports submitting Artifact Edit Proposals, GROVE token holders may submit Artifact Edit Proposals by posting them to the Sky Forum under the "Grove Prime" category. The title of the post must include the text "Grove Artifact Edit Proposal". The post must include cryptographic proof that the author controls an account holding the required percentage of the total GROVE token supply specified in [A.6.1.1.2.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](e9ae4a8a-3e61-488c-8f8b-d0062f46644d).

###### A.6.1.1.2.2.2.2.2.1.2.1.2 - Root Edit Expert Advisor Review [Core]  <!-- UUID: 3cdc7302-7f68-4143-8243-685e0681991d -->

A future iteration of the Grove Artifact will specify guidelines for obtaining specialized review of proposals requiring advanced technical or financial analysis.

###### A.6.1.1.2.2.2.2.2.1.2.1.3 - Root Edit Proposal Review By Operational Facilitator [Core]  <!-- UUID: 381ed4ee-5ec6-460e-b613-3a4610eb0aed -->

Within seven (7) days of the proposal being submitted, the Operational Facilitator must review the Root Edit Proposal for alignment.

If the proposal is aligned, the Operational Facilitator must respond to the Forum post to announce their finding. In this Forum post, the Operational Facilitator must also confirm that the proposal is feasible for Operational GovOps to operationalize.

If the proposal is misaligned, the Operational Facilitator must respond to the Forum post to announce their finding and provide the reasoning for it.

As part of this review, the Operational Facilitator must determine whether the proposal results in an increase in the on-chain risk to the protocol as described in [A.6.1.1.2.2.2.2.2.1.2.4 - Short-Term Transitionary Measures](a65302b4-5222-48a9-b37f-282498acb4d6), and must state this determination in its finding on the Forum post.

###### A.6.1.1.2.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote [Core]  <!-- UUID: f6dd56ae-ee72-4109-be99-eaf69c92c3be -->

Where their review of the proposal results in a finding of alignment with the Sky Core Atlas and Grove Artifact, the Operational Facilitator next triggers a Snapshot poll to allow token holders to vote on the proposal. Token holders may vote directly or through Delegates. See [A.6.1.1.2.3.1.4 - Delegation Framework](2cdb1ad7-17d3-4c5c-af64-b44ac7b25f0b). The poll is open for three (3) days. A poll must have more than 50% of votes cast, excluding abstentions, in favor to be approved.

Grove's governance runs in a weekly cycle that begins every Monday. Upon receiving all approvals, the proposal is automatically included in the next cycle. The cut-off time for submitting the proposal in a Forum post is Wednesday 16:00 UTC. After the cut-off time, it is at the discretion of the Operational Facilitator whether the proposal can be included in the immediate next cycle, or the following cycle.

Where the proposal is risk-increasing (see [A.6.1.1.2.2.2.2.2.1.2.4 - Short-Term Transitionary Measures](a65302b4-5222-48a9-b37f-282498acb4d6)), the Operational Facilitator triggers the Snapshot poll only after the Core Council Risk Advisor's approval has been obtained.

Proposals that do not require Core Council Risk Advisor approval may instead follow the later end-of-Friday submission deadline.

###### A.6.1.1.2.2.2.2.2.1.2.1.5 - Root Edit Artifact Update [Core]  <!-- UUID: a3dcb3c9-7e5a-48b1-aac8-9af4b5dfcfc2 -->

At the conclusion of the poll, if the proposal is approved, the Operational Facilitator submits the edit to Powerhouse to formally update the Agent Artifact. Regardless of the outcome, the Operational Facilitator updates the Powerhouse System to include the result of the vote, including any pertinent documents.

###### A.6.1.1.2.2.2.2.2.1.2.1.5.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: c05f5877-d0e5-49dd-9608-86aa70d58cc0 -->

Until the Powerhouse system supports updating Agent Artifacts, the Operational Facilitator works with the Core Facilitator to update the Atlas GitHub repository located at [https://github.com/sky-ecosystem/next-gen-atlas/pulls](https://github.com/sky-ecosystem/next-gen-atlas/pulls) to reflect proposals approved by Prime Governance.

###### A.6.1.1.2.2.2.2.2.1.2.1.6 - Artifact Edit Restrictions [Core]  <!-- UUID: d3c68da3-81ff-4b73-a50c-1f9de5b6ff7f -->

The Grove Artifact cannot be edited in any way that violates the Sky Core Atlas or its specifications of the Sky Primitives, or in any way that is otherwise misaligned. The Operational Facilitator must enforce this rule through their review of Artifact Edit Proposals.

###### A.6.1.1.2.2.2.2.2.1.2.1.6.1 - Time-Limited Root Edit Restrictions On Removal Of Nested Contributors [Core]  <!-- UUID: 2a438f59-854c-4281-8bca-2bef58163c9d -->

For a period of three years after the Genesis Supply emissions of GROVE tokens take place, any Artifact Edit that would have the effect of removing a Nested Contributor must be approved by a vote of SKY holders in addition to a vote of GROVE holders to be effective.

###### A.6.1.1.2.2.2.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: f96c5429-a5d5-40cd-b9eb-60fe06d59860 -->

The documents herein define the process for using the Root Edit Primitive to update the Grove Agent Artifact in non-routine conditions.

###### A.6.1.1.2.2.2.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: e41f9cb5-5f2c-4a90-bbf0-c221cb37cdcb -->

The documents herein define the process for using the Root Edit Primitive to update the Grove Agent Artifact in urgent or emergency situations.

###### A.6.1.1.2.2.2.2.2.1.2.3.1 - Root Edit Voting Process in Urgent and Emergency Situations [Core]  <!-- UUID: 09e744a5-cf02-4a56-8acb-d30ee74f8a3f -->

In an Urgent or Emergency Situation, as defined by the Sky Core Atlas in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225), the Operational Facilitator may allow a Root Edit to occur more quickly than the timeline specified above. Where feasible, the Operational Facilitator should announce the decision to deploy the emergency Root Edit protocol and provide their reasoning via a public Sky Forum post (under the "Grove Prime" category), unless doing so would endanger Grove or its users.

###### A.6.1.1.2.2.2.2.2.1.2.4 - Short-Term Transitionary Measures [Core]  <!-- UUID: a65302b4-5222-48a9-b37f-282498acb4d6 -->

During the initial decentralization phase of GROVE token, all decisions on the parameters specified in [A.6.1.1.2.2.6.1 - Allocation System Primitive](fecdf649-666c-4196-a046-b2eaf76574d3) resulting in an increase in the on-chain risk to the protocol will be subject to approval by the [A.1.8.1.1 - Core Council Risk Advisor](d80c8f64-b3f6-430d-bf62-8e50a3783e73). The two items excluded from that requirement are:

- The onboarding of Morpho vaults on Ethereum Mainnet that are controlled by Sky Governance and backed by cbBTC, ETH, or stETH
- The onboarding of Laniakea Halo class assets, once that framework is live

A proposal cannot move to the [A.6.1.1.2.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote](f6dd56ae-ee72-4109-be99-eaf69c92c3be) without the Core Council Risk Advisor's approval.

This transitionary phase will last until Sky determines that the GROVE token is decentralized enough to allow for meaningful governance by token holders.

###### A.6.1.1.2.2.2.2.2.1.3 - Data Repository [Core]  <!-- UUID: 13875c96-2c30-4629-864e-8a94f9fa3779 -->

The documents herein contain data relevant to the Single Instance of the Root Edit Primitive.

###### A.6.1.1.2.2.2.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 07447068-8892-4154-b3d0-7a2b4f1412cc -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.2.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 619ee46a-6a8c-4f13-9a04-e8cf4f8f4b86 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.2.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: e02ff5f7-7a4f-48f6-a28e-1e1fc362072e -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.2.2.2.2.3 - Completed Instances [Core]  <!-- UUID: 9784ad9e-ecb8-49f1-95a6-fd3987482733 -->

The Instances of the Root Edit Primitive with `Completed` Status are contained herein.

##### A.6.1.1.2.2.2.2.4 - In Progress Invocations [Core]  <!-- UUID: 398631e5-af29-49bf-9f9c-1d8fbd7a2dc2 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.2.2.2.3 - Light Agent Primitive [Core]  <!-- UUID: 3a7273a8-da6b-4e1c-b59f-7b25003d1401 -->

The documents herein contain all data and specifications for Grove’s Instances of the Light Agent Primitive. See [A.2.2.6.3 - Light Agent Primitive](44028423-2cd1-40cb-89ac-3f762b602b90).

##### A.6.1.1.2.2.2.3.1 - Primitive Hub Document [Core]  <!-- UUID: 659ba048-7352-449d-8d89-d4ba9c72c2df -->

The documents herein organize all base information relevant to Grove’s usage of the Light Agent Primitive.

###### A.6.1.1.2.2.2.3.1.1 - Global Activation Status [Core]  <!-- UUID: b7d6cbd8-c8fe-41a6-a4f0-06e78017c1c5 -->

`Inactive`

###### A.6.1.1.2.2.2.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 04eb437f-4664-487f-86e8-0454bb872081 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.2.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: c4b24078-dd71-4d9b-b71d-f7030d4fdd71 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.2.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: d0fd8e41-7f83-40ef-b0fd-fc32a3621f98 -->

This document contains a Directory of all prospective Instances of the Light Agent Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.2.3.1.2 - Active Instances Directory](04eb437f-4664-487f-86e8-0454bb872081), whereas failed Invocations are Archived in [A.6.1.1.2.2.2.3.1.5 - Hub Data Repository](9572d7c3-5472-4a06-9e59-4e0307bea775).

###### A.6.1.1.2.2.2.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 9572d7c3-5472-4a06-9e59-4e0307bea775 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.2.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 35399b0c-a972-4a77-83cd-1a86982441bb -->

The subtrees for archived Invocations and Instances of the Light Agent Primitive are stored here.

###### A.6.1.1.2.2.2.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 1efd6936-c9d7-4f38-922c-b12b9de41801 -->

The subtrees for failed Invocations of the Light Agent Primitive are stored here.

###### A.6.1.1.2.2.2.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 7770f51a-89af-42f9-bcd3-3ffebadaf840 -->

The subtrees for Instances of the Light Agent Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.2.3.2 - Active Instances [Core]  <!-- UUID: 25b9dd1a-045c-4ef6-8b3a-7d97622e4f3c -->

The Instances of the Light Agent Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.2.3.3 - Completed Instances [Core]  <!-- UUID: 93909689-5956-495c-995b-f553ce7a4611 -->

The Instances of the Light Agent Primitive with `Completed` Status are contained herein.

##### A.6.1.1.2.2.2.3.4 - In Progress Invocations [Core]  <!-- UUID: c0c6f3ea-db96-493f-af49-9393c31ca800 -->

The in progress Invocations of the Light Agent Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.2.3.2 - Active Instances](25b9dd1a-045c-4ef6-8b3a-7d97622e4f3c).

### A.6.1.1.2.2.3 - Ecosystem Upkeep Primitives [Core]  <!-- UUID: 4360c7ca-0f42-4ad8-8cad-ffe042e2f2b4 -->

The documents herein implement the Ecosystem Upkeep Primitives for Grove. See [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

#### A.6.1.1.2.2.3.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: 360c4fcc-fb40-482d-b3a7-4da11dce9da9 -->

The documents herein contain all data and specifications for Grove’s Instance of the Ecosystem Upkeep Fee Primitive. See [A.2.2.7.1 - Ecosystem Upkeep Fee Primitive](a21616f4-1611-4e0b-87b2-efbdff9f6f28).

##### A.6.1.1.2.2.3.1.1 - Primitive Hub Document [Core]  <!-- UUID: d8588e0b-0acd-4bed-989e-8da4016d0aa9 -->

The documents herein organize all base information relevant to Grove’s usage of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.2.2.3.1.1.1 - Global Activation Status [Core]  <!-- UUID: f03feadf-740b-4a9f-95bd-d34c14476df4 -->

`Active`

###### A.6.1.1.2.2.3.1.1.2 - Active Instances Directory [Core]  <!-- UUID: be81c9fd-51a3-41cb-9cd3-ae75dc5e4a1f -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.3.1.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: d303d116-aaa4-4696-82f6-3e91134a7e65 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.3.1.2.1 - Single Instance Configuration Document](f462656b-7c8a-4e2c-bbc8-24552dc6cfc8).

###### A.6.1.1.2.2.3.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: f89e1ba4-a944-4448-82cb-daecf0d56d97 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.3.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: b4657323-1dfc-4754-92a0-49fce826ed6e -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.2.2.3.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 7eb4aec2-75b3-4f7a-a4b1-18833a110d49 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.3.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 4a56ae75-633e-4806-b226-831611e3f8f1 -->

The subtrees for archived Invocations and Instances of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.2.2.3.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: b84bdc68-c82e-4466-b1c8-b16cf8b3901e -->

The subtrees for failed Invocations of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.2.2.3.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 5435ff31-2051-4863-9dc2-971fa12fb25e -->

The subtrees for Instances of the Ecosystem Upkeep Fee Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.3.1.2 - Active Instances [Core]  <!-- UUID: 7e2eb143-8264-40e3-9151-9c6a9a44012b -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Active` Status are stored herein.

###### A.6.1.1.2.2.3.1.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: f462656b-7c8a-4e2c-bbc8-24552dc6cfc8 -->

The documents herein contain the Instance Configuration Document for the Single Ecosystem Upkeep Fee Primitive Instance.

###### A.6.1.1.2.2.3.1.2.1.1 - Parameters [Core]  <!-- UUID: 3b2cd856-880f-474d-a64e-dca106d7f1d3 -->

The documents herein define the parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.2.2.3.1.2.1.1.1 - Terms [Core]  <!-- UUID: 46e8244b-d159-4884-b07f-e758424e4ec9 -->

Grove will pay 0.50% of its market capitalization per year in USDS.

###### A.6.1.1.2.2.3.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 2331102b-2095-4ff4-8755-1f7bde27a6ac -->

The documents herein define the custom parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive, if any.

###### A.6.1.1.2.2.3.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: e267d1d2-d9e7-430b-b879-9d60ef8ad348 -->

The documents herein define the process for the ongoing management of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.2.2.3.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: d37c033b-2a45-46d4-b7dd-741c1e902d47 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.2.2.3.1.2.1.2.1.1 - Process Definition For Upkeep Fee Payment [Core]  <!-- UUID: 9a359283-1c1b-4755-aa52-995f278e688d -->

The process to pay 0.50% of Grove’s market capitalization per year in USDS will be specified in future iterations of the Grove Artifact.

###### A.6.1.1.2.2.3.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: bf4a3785-8570-46ae-94ca-ac00cf709f02 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.2.2.3.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 9036e0b9-a7d7-45a6-9800-3f97c47e86e9 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.2.2.3.1.2.1.3 - Data Repository [Core]  <!-- UUID: 95ee5c6a-4556-4d94-bda4-fc322ba4f112 -->

The documents herein contain data relevant to the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.2.2.3.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 13c839b0-85fa-4582-a3e0-196627b68220 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.3.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 644df4fe-8018-42cb-aa19-611b7a2f35b1 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.3.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 7b2e3d7a-c6ee-4d20-911a-2ca78b8eb12e -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.2.2.3.1.3 - Completed Instances [Core]  <!-- UUID: 370e4310-69e9-40e9-ae26-46518187cd47 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Completed` Status are stored herein.

##### A.6.1.1.2.2.3.1.4 - In Progress Invocations [Core]  <!-- UUID: 3c264e80-11c3-47a6-b496-852059d8826e -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.2.2.3.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: ef8a7a1d-4e4d-474b-97fd-801c8285e9fc -->

The documents herein contain all data and specifications for Groves Instance of the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

##### A.6.1.1.2.2.3.2.1 - Primitive Hub Document [Core]  <!-- UUID: 52031d37-fadd-4112-b2e9-53cc04ac44b8 -->

The documents herein organize all base information relevant to Grove’s usage of the Upkeep Rebate Primitive.

###### A.6.1.1.2.2.3.2.1.1 - Global Activation Status [Core]  <!-- UUID: 4466d3ec-d8a2-4ffd-b5bb-f5df7e58a7e3 -->

`Active`

###### A.6.1.1.2.2.3.2.1.2 - Active Instances Directory [Core]  <!-- UUID: c418d3f5-4a8b-4932-afe9-d0131c28aff1 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.3.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: cca7ba1c-8ba0-42f6-8d32-0310e7dc4067 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.3.2.2.1 - Single Instance Configuration Document](e09238d0-83f5-4163-b3d3-613e218014fa).

###### A.6.1.1.2.2.3.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 2a87028d-9eea-47a9-9416-be32a71c94ed -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.3.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: d95b16c0-0980-4401-ad83-9b4e4c8f947e -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.2.2.3.2.1.5 - Hub Data Repository [Core]  <!-- UUID: d99c0146-440f-45f2-8363-fe30f270e191 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.3.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 5d2ceb86-dc91-47ae-94d1-1664fb672d5a -->

The subtrees for archived Invocations and Instances of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.2.2.3.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 0c01a5fa-f900-4642-9d63-32571651a5cf -->

The subtrees for failed Invocations of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.2.2.3.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: d4945245-9089-4464-ae63-2facab16a444 -->

The subtrees for Instances of the Upkeep Rebate Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.3.2.2 - Active Instances [Core]  <!-- UUID: 0bc120ca-79b5-4998-a7d6-73d401e1a93c -->

The Instances of the Upkeep Rebate Primitive with `Active` Status are stored herein.

###### A.6.1.1.2.2.3.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: e09238d0-83f5-4163-b3d3-613e218014fa -->

The documents herein contain the Instance Configuration Document for the Single Upkeep Rebate Primitive Instance.

###### A.6.1.1.2.2.3.2.2.1.1 - Parameters [Core]  <!-- UUID: 437e2df9-8afe-48cd-af5c-6271c04ce4c0 -->

Every Prime Agent is entitled to the Upkeep Rebate Primitive for tokens of other Prime Agents that they hold. Because this right automatically applies, there are no parameters.

###### A.6.1.1.2.2.3.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 4e5243ed-13cd-4f24-abee-d3c11886d3cc -->

The documents herein define the process for the ongoing management of the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.2.2.3.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: f0f37117-6d8d-4c0f-94c9-8b0842bc1ce0 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.2.2.3.2.2.1.2.1.1 - Grove Holds Tokens Of Other Agents In Its SubProxy Account [Core]  <!-- UUID: dca8ad49-39fe-4542-92ee-da36a1a96a31 -->

Grove keeps all tokens of other Agents it holds in its SubProxy account.

###### A.6.1.1.2.2.3.2.2.1.2.1.2 - Grove Deducts Rebate From Ecosystem Upkeep Fees [Core]  <!-- UUID: de9ff4be-acd3-4d10-a66a-4f18d81d73c1 -->

When paying Ecosystem Upkeep fees, Grove deducts the rebate from the fees it pays.

###### A.6.1.1.2.2.3.2.2.1.2.1.3 - Operational GovOps Reviews Rebate [Core]  <!-- UUID: 75305e17-8f4b-46cc-8bb5-39fd3680a8e0 -->

Operational GovOps reviews Grove’s calculation of the rebate before executing a return of surplus to token holders. In the event of any issues, Operational GovOps cannot execute the distribution. If Operational GovOps does not execute the distribution, Operational GovOps must post an explanation on the Sky Forum under the "Grove Prime" category and work with Grove to resolve the disagreement. If Operational GovOps and Grove cannot resolve the disagreement, it must be escalated to Core GovOps.

###### A.6.1.1.2.2.3.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: be43f527-f839-49c3-aea6-b2d592f7da6b -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.2.2.3.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 9e2e5c70-3d46-4e82-ab1c-f7bd87427a07 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.2.2.3.2.2.1.3 - Data Repository [Core]  <!-- UUID: bad21323-3b52-4851-85be-bdf165f0b560 -->

The documents herein contain data relevant to the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.2.2.3.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 0003325e-7d02-41af-b61b-110aba99540c -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.3.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 3753d344-3218-4171-be0e-9654f690439e -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.3.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 7b87b8a2-5e30-46a3-b12b-5fe0053eafc4 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.2.2.3.2.3 - Completed Instances [Core]  <!-- UUID: d659568c-ebea-462e-8d75-0fd3d848c884 -->

The Instances of the Upkeep Rebate Primitive with `Completed` Status are contained herein.

##### A.6.1.1.2.2.3.2.4 - In Progress Invocations [Core]  <!-- UUID: 742884ea-1851-4c44-8cbc-cc8cc69dd8da -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

### A.6.1.1.2.2.4 - SkyLink Primitives [Core]  <!-- UUID: 6ba46f75-fc23-4697-9c3d-e33b29d49bad -->

The documents herein implement the SkyLink Primitives for Grove. See [A.2.2.8 - SkyLink Primitives](7b5d8965-a64c-4c44-b742-607f51f69d8f).

#### A.6.1.1.2.2.4.1 - Token SkyLink Primitive [Core]  <!-- UUID: 9f614096-200c-48cb-abba-9f2ea3a35073 -->

The documents herein contain all data and specifications for Grove’s Instances of the Token SkyLink Primitive. See [A.2.2.8.1 - Token SkyLink Primitive](4504d2d4-ee45-4a07-8c5b-9baf20b12e76).

##### A.6.1.1.2.2.4.1.1 - Primitive Hub Document [Core]  <!-- UUID: d6e99512-2f90-4c90-8d99-8b2dec137ace -->

The documents herein organize all base information relevant to Grove’s usage of the Token SkyLink Primitive.

###### A.6.1.1.2.2.4.1.1.1 - Global Activation Status [Core]  <!-- UUID: 8b7eb17f-1925-44c2-b6bb-e67130b9aea8 -->

`Inactive`

###### A.6.1.1.2.2.4.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 09e7789c-4644-4a12-aef9-72d86cc488f2 -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.4.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 54de0b4a-0e2a-40f0-84fe-2e71a65e5aac -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.4.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 19184c86-0c06-4301-ae72-90969476ef71 -->

This document contains a Directory of all prospective Instances of the Token SkyLink Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.4.1.1.2 - Active Instances Directory](09e7789c-4644-4a12-aef9-72d86cc488f2), whereas failed Invocations are Archived in [A.6.1.1.2.2.4.1.1.5 - Hub Data Repository](7afcf75e-ab7c-4e1e-b856-cab87541d1e3).

###### A.6.1.1.2.2.4.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 7afcf75e-ab7c-4e1e-b856-cab87541d1e3 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.4.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 2fd0c2b3-7155-46c2-9b9b-e334a88ff9e3 -->

The subtrees for archived Invocations and Instances of the Token SkyLink Primitive are stored here.

###### A.6.1.1.2.2.4.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 376f3393-e5af-41ad-9247-31fbe63799ac -->

The subtrees for failed Invocations of the Token SkyLink Primitive are stored here.

###### A.6.1.1.2.2.4.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 54893d32-c54c-4550-96a7-60dc45e9962e -->

The subtrees for Instances of the Token SkyLink Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.4.1.2 - Active Instances [Core]  <!-- UUID: da5c971b-7758-486d-bddb-fba2e1b5cdc5 -->

The Instances of the Token SkyLink Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.4.1.3 - Completed Instances [Core]  <!-- UUID: 0a3bd259-7320-40d0-b98b-17a094fc2fcd -->

The Instances of the Token SkyLink Primitive with `Completed` Status are stored herein.

##### A.6.1.1.2.2.4.1.4 - In Progress Invocations [Core]  <!-- UUID: 9fcd2b86-f3a9-494e-936e-45614c466ccd -->

The in progress Invocations of the Token SkyLink Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.4.1.2 - Active Instances](da5c971b-7758-486d-bddb-fba2e1b5cdc5).

### A.6.1.1.2.2.5 - Demand Side Stablecoin Primitives [Core]  <!-- UUID: 79933ed7-8378-437d-a546-b03f59668a38 -->

The documents herein implement the Demand Side Stablecoin Primitives for Grove. See [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d).

#### A.6.1.1.2.2.5.1 - Distribution Reward Primitive [Core]  <!-- UUID: 8c46d61f-9b02-4898-be15-f875692f3715 -->

The documents herein contain all data and specifications for Grove’s Instances of the Distribution Reward Primitive. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

##### A.6.1.1.2.2.5.1.1 - Primitive Hub Document [Core]  <!-- UUID: 21b5e889-c9f9-45e7-becb-fde3e070e063 -->

The documents herein organize all base information relevant to Groves usage of the Distribution Reward Primitive.

###### A.6.1.1.2.2.5.1.1.1 - Global Activation Status [Core]  <!-- UUID: 95daf547-3e90-48e2-93cf-1bb2b3240b3c -->

`Active`

###### A.6.1.1.2.2.5.1.1.2 - Active Instances Directory [Core]  <!-- UUID: c1d594d3-4303-451e-9efb-2baa8ffaa034 -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.5.1.1.2.1 - Grove Finance Instance Configuration Document Location [Core]  <!-- UUID: 974d281c-9ad2-4531-9c39-fb44281b3ed0 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.5.1.2.1 - Grove Finance Instance Configuration Document](006f040b-63e1-4847-abd5-9dce1190706b).

###### A.6.1.1.2.2.5.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 11f1f7ba-82ed-4d1e-a457-344406a158f3 -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.5.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 1caf1f9a-040b-4687-ad2d-e4ad0c7709d5 -->

This document contains a Directory of all prospective Instances of the Distribution Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.5.1.1.2 - Active Instances Directory](c1d594d3-4303-451e-9efb-2baa8ffaa034), whereas failed Invocations are Archived in [A.6.1.1.2.2.5.1.1.5 - Hub Data Repository](8ea4b4ad-e167-4772-b7d6-0c87357a10e8).

###### A.6.1.1.2.2.5.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 8ea4b4ad-e167-4772-b7d6-0c87357a10e8 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.5.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 6be994b9-97fa-4768-9e71-2f8c2c110cd4 -->

The subtrees for archived Invocations and Instances of the Distribution Reward Primitive are stored here.

###### A.6.1.1.2.2.5.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: e20a22c1-1cac-4dc5-9194-8e474ac53f4c -->

The subtrees for failed Invocations of the Distribution Reward Primitive are stored here.

###### A.6.1.1.2.2.5.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 50eb902b-79db-47c4-8927-94303313595d -->

The subtrees for Instances of the Distribution Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.5.1.2 - Active Instances [Core]  <!-- UUID: a4df61c2-514e-46e4-a84d-d2782f2f183f -->

The Instances of the Distribution Reward Primitive with `Active` Status are stored herein.

###### A.6.1.1.2.2.5.1.2.1 - Grove Finance Instance Configuration Document [Core]  <!-- UUID: 006f040b-63e1-4847-abd5-9dce1190706b -->

The documents herein contain the Instance Configuration Document for the Grove Finance Distribution Reward Primitive Instance.

###### A.6.1.1.2.2.5.1.2.1.1 - Parameters [Core]  <!-- UUID: e6847aa6-4668-4cf6-a757-0b292871a703 -->

The documents herein define the parameters of the Grove Finance Instance of the Distribution Reward Primitive.

###### A.6.1.1.2.2.5.1.2.1.1.1 - Reward Code [Core]  <!-- UUID: b5b1f4eb-10a3-472b-b675-008ef0cee259 -->

`2002`.

###### A.6.1.1.2.2.5.1.2.1.1.2 - Tracking Methodology [Core]  <!-- UUID: 78948530-a5e9-456f-bcaf-f74a70bdc0b8 -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.2.2.5.1.2.1.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 4b91017e-ee25-4cc3-a97a-25d234e50151 -->

The documents herein define the custom parameters of the Grove Finance Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.2.2.5.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 9237ad33-0759-4637-86a8-e7ad6317ebb1 -->

The documents herein define the process for the ongoing management of the Grove Finance Instance of the Distribution Reward Primitive.

###### A.6.1.1.2.2.5.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: fe11d361-a9c7-460e-ae67-1b2e8a6142a1 -->

This document defines the protocol for routine ongoing management of the Grove Finance Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Grove Artifact, a version of the full process definition customized to Grove will be included herein.

###### A.6.1.1.2.2.5.1.2.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: 3fecb22f-ccd8-4bb9-8221-d354b080bef6 -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.2.2.5.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: cf4777c8-e272-4b30-9027-b391191f6473 -->

The documents herein define the protocol for non-routine ongoing management of the Grove Finance Instance of this Distribution Reward Primitive.

###### A.6.1.1.2.2.5.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: e3079d41-3785-4ee6-a5d0-90fd1c111093 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Grove Finance Instance of this Distribution Reward Primitive.

###### A.6.1.1.2.2.5.1.2.1.3 - Data Repository [Core]  <!-- UUID: 67d2e983-09c7-41da-8b4d-99a9fb00fb2d -->

The documents herein contain data relevant to the Grove Finance Instance of the Distribution Reward Primitive.

###### A.6.1.1.2.2.5.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 7259ff43-eaf7-484e-af71-8b6a0ecdde09 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.5.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 06a7389f-65b0-48bb-a0ee-b7b9dcbeeaa6 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.5.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 74019895-896c-4ab1-bb8c-f0e9741e69eb -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.2.2.5.1.2.1.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 698d68f4-8d3f-4ab4-bfd0-95dbd34b9099 -->

The Distribution Reward payments for the Grove Finance Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.6.1.1.2.2.5.1.2.1.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: bbd8de10-0899-4c16-ae48-a3d0afed9c6f -->

The Distribution Reward Payments are:

##### A.6.1.1.2.2.5.1.3 - Completed Instances [Core]  <!-- UUID: cca65b4d-5cf9-449e-9178-195b611ddc06 -->

The Instances of the Distribution Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.2.2.5.1.4 - In Progress Invocations [Core]  <!-- UUID: 1169df23-b14e-492d-9602-996c3aa0d577 -->

The in progress Invocations of the Distribution Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.5.1.2 - Active Instances](a4df61c2-514e-46e4-a84d-d2782f2f183f).

#### A.6.1.1.2.2.5.2 - Integration Boost Primitive [Core]  <!-- UUID: 634971ac-f579-4673-afbd-6a4366d26db9 -->

The documents herein contain all data and specifications for Grove’s Instances of the Integration Boost Primitive. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

##### A.6.1.1.2.2.5.2.1 - Primitive Hub Document [Core]  <!-- UUID: c5a92bcd-69d3-41ee-a12a-33dce8af4686 -->

The documents herein organize all base information relevant to Grove’s usage of the Integration Boost Primitive.

###### A.6.1.1.2.2.5.2.1.1 - Global Activation Status [Core]  <!-- UUID: c6414cd5-4efa-446d-876e-3fcf2dbb816a -->

`Inactive`

###### A.6.1.1.2.2.5.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 8e0e2f27-cc60-419b-8533-8ae1cbaf427e -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.5.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: b400b223-0b70-462d-a69e-11eb6c91fa35 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.5.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 83d45b11-4497-473b-b3c4-80c0543dd5dd -->

This document contains a Directory of all prospective Instances of the Integration Boost Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.5.2.1.2 - Active Instances Directory](8e0e2f27-cc60-419b-8533-8ae1cbaf427e), whereas failed Invocations are Archived in [A.6.1.1.2.2.5.2.1.5 - Hub Data Repository](732e99b3-3a0c-4116-b3f6-5b9d2ad4d351) .

###### A.6.1.1.2.2.5.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 732e99b3-3a0c-4116-b3f6-5b9d2ad4d351 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.5.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 1f22572f-5c05-4ef4-8fd7-a1a21c6ad050 -->

The subtrees for archived Invocations and Instances of the Integration Boost Primitive are stored here.

###### A.6.1.1.2.2.5.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: ac3d0e12-3328-43ac-9632-2cf1ac50e2a7 -->

The subtrees for failed Invocations of the Integration Boost Primitive are stored here.

###### A.6.1.1.2.2.5.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: da15a221-360f-4c7e-a324-6b5933eb8572 -->

The subtrees for Instances of the Integration Boost Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.5.2.2 - Active Instances [Core]  <!-- UUID: b1265577-1f7d-48be-941b-9a2b0f62818e -->

The Instances of the Integration Boost Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.5.2.3 - Completed Instances [Core]  <!-- UUID: 90e4294a-089b-4f34-bb05-a5c10e469d0b -->

The Instances of the Integration Boost Primitive with `Completed` Status are contained herein.

##### A.6.1.1.2.2.5.2.4 - In Progress Invocations [Core]  <!-- UUID: b7fe4d93-cd99-4223-853e-9eebe7bdaa91 -->

The in progress Invocations of the Integration Boost Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.5.2.2 - Active Instances](b1265577-1f7d-48be-941b-9a2b0f62818e).

#### A.6.1.1.2.2.5.3 - Pioneer Chain Primitive [Core]  <!-- UUID: f8ffe054-1981-457e-abc6-412f3ee37927 -->

The documents herein contain all data and specifications for Grove’s Instances of the Pioneer Chain Primitive. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).

##### A.6.1.1.2.2.5.3.1 - Primitive Hub Document [Core]  <!-- UUID: 63c25970-e1dd-475c-bb77-487ac7640aaa -->

The documents herein organize all base information relevant to Grove’s usage of the Pioneer Chain Primitive.

###### A.6.1.1.2.2.5.3.1.1 - Global Activation Status [Core]  <!-- UUID: 180defb8-541e-4de9-a7a5-d117144af928 -->

`Active`

###### A.6.1.1.2.2.5.3.1.2 - Active Instances Directory [Core]  <!-- UUID: d9fca80a-1cbc-413b-83ca-3c19428732e7 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.5.3.1.2.1 - Avalanche Instance Configuration Document Location [Core]  <!-- UUID: 796c25b9-f650-4321-962e-3f19414a2674 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.5.3.2.1 - Avalanche Instance Configuration Document](1fecc114-523e-4a7f-aceb-a5805aea6356).

###### A.6.1.1.2.2.5.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: f1007e17-0599-455f-8afb-f5e965a12683 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.5.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 6ed7f41d-b5bb-49b8-9f4c-c0b37d6ea5f0 -->

This document contains a Directory of all prospective Instances of the Pioneer Chain Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.5.3.1.2 - Active Instances Directory](d9fca80a-1cbc-413b-83ca-3c19428732e7), whereas failed Invocations are Archived in [A.6.1.1.2.2.5.3.1.5 - Hub Data Repository](495128f2-64bb-4192-bf4a-7df6259b4010).

###### A.6.1.1.2.2.5.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 495128f2-64bb-4192-bf4a-7df6259b4010 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.5.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 5dd58057-07cd-4ccb-97b9-6bd85855d2c6 -->

The subtrees for archived Invocations and Instances of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.2.2.5.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: f6788dae-477c-4a19-9302-7f42f3c7023c -->

The subtrees for failed Invocations of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.2.2.5.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 82ab7549-0214-413e-9b14-493c15a9beca -->

The subtrees for Instances of the Pioneer Chain Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.5.3.2 - Active Instances [Core]  <!-- UUID: 33a1baf4-9922-40a1-b121-558f620da186 -->

The Instances of the Pioneer Chain Primitive with `Active` Status are stored herein.

###### A.6.1.1.2.2.5.3.2.1 - Avalanche Instance Configuration Document [Core]  <!-- UUID: 1fecc114-523e-4a7f-aceb-a5805aea6356 -->

The documents herein contain the Instance Configuration Document for the Avalanche Instance of the Pioneer Chain Primitive.

###### A.6.1.1.2.2.5.3.2.1.1 - Parameters [Core]  <!-- UUID: 7870de5f-4051-4936-a73f-9b9903a83d3b -->

The documents herein define the parameters of the Avalanche Instance of the Pioneer Chain Primitive.

###### A.6.1.1.2.2.5.3.2.1.1.1 - Instance Identifiers [Core]  <!-- UUID: cd8395d4-5466-44f5-b002-12646312942b -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.5.3.2.1.1.1.1 - Network [Core]  <!-- UUID: 29ad76ea-72f5-42bc-910a-fa57a62d501a -->

Avalanche

###### A.6.1.1.2.2.5.3.2.1.1.2 - Pioneer Incentive Pool [Core]  <!-- UUID: 9b11e488-7c8f-4a6f-a5b6-0c4c526ad86a -->

The documents herein contain the terms that govern this Instance's Pioneer Incentive Pool and its address.

###### A.6.1.1.2.2.5.3.2.1.1.2.1 - Network [Core]  <!-- UUID: 027429d2-2a2c-4735-8bea-8bdcdf42d45f -->

Ethereum Mainnet

###### A.6.1.1.2.2.5.3.2.1.1.2.2 - Address [Core]  <!-- UUID: ea4f2336-3f9f-49f6-af4e-00a8736e19d5 -->

`0x1369f7b2b38c76B6478c0f0E66D94923421891Ba`

###### A.6.1.1.2.2.5.3.2.1.1.2.3 - Terms [Core]  <!-- UUID: 1702148c-fdd5-4c87-af3e-8f99f2f90f05 -->

The Pioneer Incentive Pool for this Instance is governed by the terms specified in [A.2.2.9.3.1.4 - Pioneer Incentive Pool](04edac33-19d5-4a87-a8ab-945a0cd57771).

###### A.6.1.1.2.2.5.3.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 11351bed-db55-44e7-a316-9996446adca7 -->

The documents herein define the process for the ongoing management of the Single Instance of the Pioneer Chain Primitive.

###### A.6.1.1.2.2.5.3.2.1.3 - Data Repository [Core]  <!-- UUID: 5c3f4cab-ed95-4ac9-a717-c67b4a6754f8 -->

The documents herein contain data relevant to the Single Instance of the Pioneer Chain Primitive.

##### A.6.1.1.2.2.5.3.3 - Completed Instances [Core]  <!-- UUID: ad66bcf7-bd92-4c71-be17-89310e6d0a83 -->

The Instances of the Pioneer Chain Primitive with `Completed` Status are stored herein.

##### A.6.1.1.2.2.5.3.4 - In Progress Invocations [Core]  <!-- UUID: 3299b4ea-60e5-4f46-9c4a-24c5da64a5fc -->

The in progress Invocations of the Pioneer Chain Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.5.3.2 - Active Instances](33a1baf4-9922-40a1-b121-558f620da186).

### A.6.1.1.2.2.6 - Supply Side Stablecoin Primitives [Core]  <!-- UUID: fb59210b-5a2f-4be4-a4bb-5a908d9850e7 -->

The documents herein implement the Supply Side Stablecoin Primitives for Grove. See [A.2.2.10 - Supply Side Stablecoin Primitives](d1142876-33c2-4e21-9339-d8711525d46f).

#### A.6.1.1.2.2.6.1 - Allocation System Primitive [Core]  <!-- UUID: fecdf649-666c-4196-a046-b2eaf76574d3 -->

The documents herein contain all data and specifications for Grove’s Allocation System Primitive Instances.

##### A.6.1.1.2.2.6.1.1 - Primitive Hub Document [Core]  <!-- UUID: 408b026b-09d3-4154-8fc2-e7270b76a053 -->

The documents herein organize all base information relevant to Grove’s usage of the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.1.1 - Global Activation Status [Core]  <!-- UUID: 0ac08ba4-1b98-4d83-8abd-3efdcf966dcc -->

`Active`

###### A.6.1.1.2.2.6.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 1edfe612-6f19-4aa7-b0f9-1b3a2aae8a47 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: e6fe9576-9677-4bed-b779-cd2a52e4fdc0 -->

The documents herein contain a Directory of all Instances on the Ethereum Mainnet of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.1.1.2.1.1 - Centrifuge [Core]  <!-- UUID: 2f175df9-3b8c-4c2c-a700-52f741abf501 -->

The Ethereum Mainnet Instances Directory of the Centrifuge Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.1.1 - Ethereum Mainnet - Centrifuge JTRSY Instance Configuration Document Location [Core]  <!-- UUID: 69e59a73-e7c8-4277-a804-0cc945497241 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.1.1 - Ethereum Mainnet - Centrifuge JTRSY Instance Configuration Document](292d1098-9fe4-481f-a3e7-72e345bdca81).

###### A.6.1.1.2.2.6.1.1.2.1.1.2 - Ethereum Mainnet - Centrifuge JAAA Instance Configuration Document Location [Core]  <!-- UUID: d1c474c6-9071-4110-90d6-36d81e73e98e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.1.2 - Ethereum Mainnet - Centrifuge JAAA Instance Configuration Document](10f4641c-2ed1-4430-ae71-1e830e779269).

###### A.6.1.1.2.2.6.1.1.2.1.1.3 - Ethereum Mainnet - Centrifuge ACRDX Instance Configuration Document Location [Core]  <!-- UUID: 7db7e977-cf6d-4186-b20c-43715314cb2c -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.1.3 - Ethereum Mainnet - Centrifuge ACRDX Instance Configuration Document](b0d889d1-8465-4229-ba69-ca4b5d866131).

###### A.6.1.1.2.2.6.1.1.2.1.1.4 - Ethereum Mainnet - Centrifuge JTRSY USDS Vault Instance Configuration Document Location [Core]  <!-- UUID: e50bfc41-5c93-4e29-87ef-dd1b0af9140c -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.1.4 - Ethereum Mainnet - Centrifuge JTRSY USDS Vault Instance Configuration Document](acbe1bed-7639-45a4-9a5d-73c7d434bd0a).

###### A.6.1.1.2.2.6.1.1.2.1.2 - Blackrock [Core]  <!-- UUID: f1de44d8-9dc4-4513-ac06-295d5ccc427d -->

The Ethereum Mainnet Instances Directory of the Blackrock Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.2.1 - Ethereum Mainnet - Blackrock BUIDL-I Instance Configuration Document Location [Core]  <!-- UUID: 44299e83-18ec-4bdd-990c-2f61f3d11276 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.2.1 - Ethereum Mainnet - Blackrock BUIDL-I Instance Configuration Document](8bc44388-0d97-4d5e-aa33-fdd1938f03ff).

###### A.6.1.1.2.2.6.1.1.2.1.3 - Superstate [Core]  <!-- UUID: a54ef112-49c1-456b-bee9-720b5683440c -->

The Ethereum Mainnet Instances Directory of the Superstate Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.3.1 - Ethereum Mainnet - Superstate USTB Instance Configuration Document Location [Core]  <!-- UUID: 59096f55-3b2c-432c-bea1-e48f2277dec8 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.3.1 - Ethereum Mainnet - Superstate USTB Instance Configuration Document](a49f5e48-6e00-434b-bd85-26539c7a9cfe).

###### A.6.1.1.2.2.6.1.1.2.1.4 - Ethena [Core]  <!-- UUID: df36f5df-f45e-49a3-a6ee-508d1970740c -->

The Ethereum Mainnet Instances Directory of the Ethena Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.4.1 - Ethereum Mainnet - Ethena USDe Instance Configuration Document Location [Core]  <!-- UUID: 0f7c80ec-f26a-4952-991c-c92cd9b902c1 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.4.1 - Ethereum Mainnet - Ethena USDe Instance Configuration Document](dbe15588-fa00-4573-ae8a-f69e095532f5).

###### A.6.1.1.2.2.6.1.1.2.1.4.2 - Ethereum Mainnet - Ethena sUSDe Instance Configuration Document Location [Core]  <!-- UUID: bac8cfff-f26f-4cc2-aac4-a5ac7232e99c -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.4.2 - Ethereum Mainnet - Ethena sUSDe Instance Configuration Document](5847fff3-ff82-4c01-ac24-7f06fac8c2a4).

###### A.6.1.1.2.2.6.1.1.2.1.4.3 - Ethereum Mainnet - Ethena PT-USDe Instance Configuration Document Location [Core]  <!-- UUID: 39fdf5a1-92e9-40de-a1f4-23732d6bbb1a -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.4.3 - Ethereum Mainnet - Ethena PT-USDe Instance Configuration Document](e3f9abf3-0cd0-46cc-8295-175c1bc8afbd).

###### A.6.1.1.2.2.6.1.1.2.1.4.4 - Ethereum Mainnet - Ethena PT-sUSDe Instance Configuration Document Location [Core]  <!-- UUID: 46eb0e66-2594-4bb6-8e2b-0651a6ce39c8 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.4.4 - Ethereum Mainnet - Ethena PT-sUSDe Instance Configuration Document](ba45e20f-b6df-4836-94ea-b4f2f062e658).

###### A.6.1.1.2.2.6.1.1.2.1.5 - Aave [Core]  <!-- UUID: 23bbcb38-c473-4ccf-83c5-59fe292bb13c -->

The Ethereum Mainnet Instances Directory of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.5.1 - Ethereum Mainnet - Aave Core v3 USDC Instance Configuration Document Location [Core]  <!-- UUID: 7115f3e1-549f-458b-990a-756b679ce2b0 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.5.1 - Ethereum Mainnet - Aave Core v3 USDC Instance Configuration Document](7f4eb111-6751-4308-88ce-efe2445e5455).

###### A.6.1.1.2.2.6.1.1.2.1.5.2 - Ethereum Mainnet - Aave Core v3 RLUSD Instance Configuration Document Location [Core]  <!-- UUID: 6149518b-ccd9-48ad-85f2-3a57c8d2bb6d -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.5.2 - Ethereum Mainnet - Aave Core v3 RLUSD Instance Configuration Document](6b5a19f9-7810-4066-b2ca-df7eff376971).

###### A.6.1.1.2.2.6.1.1.2.1.5.3 - Ethereum Mainnet - Aave Horizon USDC Instance Configuration Document Location [Core]  <!-- UUID: f7cb82e7-bb79-4e0a-9c92-652f8d24fcad -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.5.3 - Ethereum Mainnet - Aave Horizon USDC Instance Configuration Document](3050edfd-dd88-4fa4-91b4-4870d4fed089).

###### A.6.1.1.2.2.6.1.1.2.1.5.4 - Ethereum Mainnet - Aave Horizon RLUSD Instance Configuration Document Location [Core]  <!-- UUID: dbe0fa43-026b-467f-8108-879f4fe94e3b -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.5.4 - Ethereum Mainnet - Aave Horizon RLUSD Instance Configuration Document](15200deb-9894-4f54-95b6-7bab90a6f395).

###### A.6.1.1.2.2.6.1.1.2.1.6 - Curve [Core]  <!-- UUID: 74f2556f-fb78-45f3-95d7-f360b9982d09 -->

The Ethereum Mainnet Instances Directory of the Curve Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.6.1 - Ethereum Mainnet - Curve RLUSD/USDC Pool Instance Configuration Document Location [Core]  <!-- UUID: 654eac37-dbe6-4bf1-a300-e04645c0652a -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.6.1 - Ethereum Mainnet - Curve RLUSD/USDC Pool Instance Configuration Document](67b85f8a-3857-461d-a214-d3bf990f9111).

###### A.6.1.1.2.2.6.1.1.2.1.6.2 - Ethereum Mainnet - Curve RLUSD/USDC Pool LP Deposits Instance Configuration Document Location [Core]  <!-- UUID: e09057c5-3a44-4e92-a38c-5695a6ad08d9 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.6.3 - Ethereum Mainnet - Curve RLUSD/USDC Pool LP Deposits Instance Configuration Document](ea9afb08-8f81-4ee9-b9a7-321862bad5d8).

###### A.6.1.1.2.2.6.1.1.2.1.6.3 - Ethereum Mainnet - Curve AUSD/USDC Swaps Instance Configuration Document Location [Core]  <!-- UUID: b46fedbe-4c43-4924-970f-703e8e6d3876 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.6.4 - Ethereum Mainnet - Curve AUSD/USDC Swaps Instance Configuration Document](207cc62c-29ee-4a03-afd9-37f279b2c25b).

###### A.6.1.1.2.2.6.1.1.2.1.6.4 - Ethereum Mainnet - Curve AUSD/USDC LP Instance Configuration Document Location [Core]  <!-- UUID: ad345081-935c-4fce-ba70-69992bc908c5 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.6.5 - Ethereum Mainnet - Curve AUSD/USDC LP Instance Configuration Document](6d7f468e-e32c-4077-8dbc-66095e7b8f84).

###### A.6.1.1.2.2.6.1.1.2.1.6.5 - Ethereum Mainnet - Curve PYUSD/USDS Swaps Instance Configuration Document Location [Core]  <!-- UUID: afeb8a74-9f57-4729-ba91-f87a63eaa6e5 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.6.6 - Ethereum Mainnet - Curve PYUSD/USDS Swaps Instance Configuration Document](f168c4a8-f526-471e-8410-4f3f339e99d5).

###### A.6.1.1.2.2.6.1.1.2.1.7 - Morpho [Core]  <!-- UUID: c7201d8e-ea9a-4283-ad53-8f1851bde413 -->

The Ethereum Mainnet Instances Directory of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.7.1 - Ethereum Mainnet - Morpho Grove x Steakhouse High Yield Vault USDC Instance Configuration Document Location [Core]  <!-- UUID: 03708e1d-f0e9-41e6-a792-01ef1b2d969b -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.7.1 - Ethereum Mainnet - Morpho Grove x Steakhouse High Yield Vault USDC Instance Configuration Document](29cb8322-96f5-4f18-b4fe-eb31826af580).

###### A.6.1.1.2.2.6.1.1.2.1.7.2 - Ethereum Mainnet - Grove x Steakhouse USDC Morpho Vault v2 Instance Configuration Document Location [Core]  <!-- UUID: c0daf824-060e-449e-be48-f86efd1447e2 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.7.2 - Ethereum Mainnet - Grove x Steakhouse USDC Morpho Vault v2 Instance Configuration Document](6ec606f0-bc47-4f36-8591-75784bb78b00).

###### A.6.1.1.2.2.6.1.1.2.1.7.3 - Ethereum Mainnet - Steakhouse PYUSD Morpho Vault Instance Configuration Document Location [Core]  <!-- UUID: d0a21cdb-ba69-4f0c-9b67-575996a01c4d -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.7.3 - Ethereum Mainnet - Steakhouse PYUSD Morpho Vault Instance Configuration Document](0b7e1d3d-1f56-48a6-9729-88479aa5ff92).

###### A.6.1.1.2.2.6.1.1.2.1.7.4 - Ethereum Mainnet - Grove x Steakhouse AUSD Morpho Vault V2 Instance Configuration Document Location [Core]  <!-- UUID: 1281f13b-4435-46c5-9e8a-b602aac42c7a -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.7.4 - Ethereum Mainnet - Grove x Steakhouse AUSD Morpho Vault V2 Instance Configuration Document](2c21462b-2925-48d8-9578-5fc21aa96563).

###### A.6.1.1.2.2.6.1.1.2.1.7.5 - Ethereum Mainnet - Sentora PYUSD Morpho Vault V2 Instance Configuration Document Location [Core]  <!-- UUID: db6ff295-bf78-450f-a272-f4a5f01b0cdc -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.7.5 - Ethereum Mainnet - Sentora PYUSD Morpho Vault V2 Instance Configuration Document](3e940e02-80eb-4e37-bce6-95939089da46).

###### A.6.1.1.2.2.6.1.1.2.1.7.6 - Ethereum Mainnet - Sentora RLUSD Morpho Vault V2 Instance Configuration Document Location [Core]  <!-- UUID: 329dae6d-08a0-4628-b494-b533e69c26ce -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.7.6 - Ethereum Mainnet - Sentora RLUSD Morpho Vault V2 Instance Configuration Document](dff6df5f-f8ab-4df1-be1e-f71510c3534e).

###### A.6.1.1.2.2.6.1.1.2.1.7.7 - Ethereum Mainnet - Grove x Steakhouse RLUSD Morpho Vault V2 Instance Configuration Document Location [Core]  <!-- UUID: d6cab49c-2cfd-4f70-a101-fbdb294c16db -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.7.7 - Ethereum Mainnet - Grove x Steakhouse RLUSD Morpho Vault V2 Instance Configuration Document](cfb29474-ea48-4370-aad6-23af1cf4d11a).

###### A.6.1.1.2.2.6.1.1.2.1.8 - Securitize [Core]  <!-- UUID: 12a0d375-8f1e-4e62-83ba-d56bc6d3f2ab -->

The Ethereum Mainnet Instances Directory of the Securitize Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.8.1 - Ethereum Mainnet - Securitize Tokenized AAA CLO Fund (STAC) Instance Configuration Document Location [Core]  <!-- UUID: f43479d2-2c76-4a18-8e9b-f59f1e1b493b -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.8.1 - Ethereum Mainnet - Securitize Tokenized AAA CLO Fund (STAC) Instance Configuration Document](a0c4fcd6-ebf9-4124-8767-cf14ab6ab397).

###### A.6.1.1.2.2.6.1.1.2.1.9 - Galaxy [Core]  <!-- UUID: 040d21e6-c423-45b6-81c0-fc05c1e45bae -->

The Ethereum Mainnet Instances Directory of the Galaxy Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.9.1 - Ethereum Mainnet - Galaxy Arch CLOs Instance Configuration Document Location [Core]  <!-- UUID: af6212d3-fc1a-4c34-9352-ea18f8a2a294 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.9.1 - Ethereum Mainnet - Galaxy Arch CLOs Instance Configuration Document](61afae62-1210-4d80-aa6c-cdb26ef0a287).

###### A.6.1.1.2.2.6.1.1.2.1.9.2 - Ethereum Mainnet - Galaxy Warehouse Instance Configuration Document Location [Core]  <!-- UUID: ad3557aa-ec4e-4cc5-8673-f3aa5818a288 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.9.2 - Ethereum Mainnet - Galaxy Warehouse Instance Configuration Document](2e3e057e-0b48-4e3f-b03d-1ed84299ccfc).

###### A.6.1.1.2.2.6.1.1.2.1.10 - Ripple [Core]  <!-- UUID: 39843e09-154a-497a-8824-54393ea15915 -->

The Ethereum Mainnet Instances Directory of the Ripple Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.10.1 - Ethereum Mainnet - Ripple RLUSD Instance Configuration Document Location [Core]  <!-- UUID: 6bf29031-456e-4f6e-bb43-1ceb4a2eb11e -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.10.1 - Ethereum Mainnet - Ripple RLUSD Instance Configuration Document](2e28c162-c608-452c-b796-4654ac1139d8).

###### A.6.1.1.2.2.6.1.1.2.1.11 - Agora [Core]  <!-- UUID: 2417db38-50a7-4394-9cfb-7afcf01e8c85 -->

The Ethereum Mainnet Instances Directory of the Agora Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.11.1 - Ethereum Mainnet - Agora AUSD Instance Configuration Document Location [Core]  <!-- UUID: ec9d4393-2e68-40a7-b428-efc0452e35d8 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.11.1 - Ethereum Mainnet - Agora AUSD Instance Configuration Document](0d71b879-0dd7-4c37-9a42-f16d868c4482).

###### A.6.1.1.2.2.6.1.1.2.1.12 - Uniswap [Core]  <!-- UUID: 6285def0-e537-4d18-9776-7534196576e6 -->

The Ethereum Mainnet Instances Directory of the Uniswap Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.12.1 - Ethereum Mainnet - Uniswap v3 AUSD/USDC Swaps Instance Configuration Document Location [Core]  <!-- UUID: 6fcc9608-b482-4d67-872f-828c0dad3a89 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.12.1 - Ethereum Mainnet - Uniswap v3 AUSD/USDC Swaps Instance Configuration Document](ffa0ca69-c416-4163-a1c6-b863f5d38c3f).

###### A.6.1.1.2.2.6.1.1.2.1.12.2 - Ethereum Mainnet - Uniswap v3 AUSD/USDC LP Instance Configuration Document Location [Core]  <!-- UUID: d8c0e975-1902-4fcf-b228-c3e75d3b6dee -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.12.2 - Ethereum Mainnet - Uniswap v3 AUSD/USDC LP Instance Configuration Document](cca4236a-47f9-4b4f-81ef-c31a5ee624aa).

###### A.6.1.1.2.2.6.1.1.2.1.12.3 - Ethereum Mainnet - Grove Diamond PAU Uniswap v3 AUSD/USDC Instance Configuration Document Location [Core]  <!-- UUID: bac4c092-547f-4af1-b6fd-a678421b1efb -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.12.3 - Ethereum Mainnet - Grove Diamond PAU Uniswap v3 AUSD/USDC Instance Configuration Document](4a3fdcf1-e754-413a-b7af-5336fa162d83).

###### A.6.1.1.2.2.6.1.1.2.1.13 - Maple [Core]  <!-- UUID: 3fb5412d-23fd-4b1e-bddb-6e684e954050 -->

The Ethereum Mainnet Instances Directory of the Maple Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.13.1 - Ethereum Mainnet - Maple syrupUSDC Instance Configuration Document Location [Core]  <!-- UUID: 20b30bc3-c3e8-4098-bdf2-ca288e8bee1a -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.13.1 - Ethereum Mainnet - Maple syrupUSDC Instance Configuration Document](7502f64c-3276-478e-8f98-53a2377ca1a2).

###### A.6.1.1.2.2.6.1.1.2.1.14 - Tokenized Treasury [Core]  <!-- UUID: 53a37417-5900-4b8d-a750-339782c838cb -->

The Ethereum Mainnet Tokenized Treasury Instances Directory with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.14.1 - Ethereum Mainnet - Tokenized Treasury JTRSY Instance Configuration Document Location [Core]  <!-- UUID: e6582be2-cb08-4788-a011-32e3509a42e5 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.14.1 - Ethereum Mainnet - Tokenized Treasury JTRSY Instance Configuration Document](5e38198e-1577-4ab0-900a-91b6d8284387).

###### A.6.1.1.2.2.6.1.1.2.1.14.2 - Ethereum Mainnet - Tokenized Treasury BUIDL Instance Configuration Document Location [Core]  <!-- UUID: 8ebc6bfc-0981-40b6-8094-2be55470dfcc -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.14.2 - Ethereum Mainnet - Tokenized Treasury BUIDL Instance Configuration Document](867aa6c2-4d44-4734-8d77-ff435dc89463).

###### A.6.1.1.2.2.6.1.1.2.1.15 - Paxos [Core]  <!-- UUID: f1c5403d-8796-4c70-a734-47f2bf408431 -->

The Ethereum Mainnet Instances Directory of Paxos with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.1.15.1 - Ethereum Mainnet - USDC To USDG Via Paxos Instance Configuration Document Location [Core]  <!-- UUID: 55536ff1-79a3-4710-bc23-8e718ecfeb48 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.1.15.1 - Ethereum Mainnet - USDC To USDG Via Paxos Instance Configuration Document](4bf8eae7-b19c-4572-ad05-efff5a5310a6).

###### A.6.1.1.2.2.6.1.1.2.2 - Avalanche [Core]  <!-- UUID: 7f10aaf2-b3e8-4dc8-b91f-ff27200a9ccf -->

The documents herein contain a Directory of all Instances on Avalanche of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.1.1.2.2.1 - Centrifuge [Core]  <!-- UUID: bc3f2a84-6f20-448a-9f2a-9173cfe65204 -->

The Avalanche Instances Directory of the Centrifuge Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.2.1.1 - Avalanche - Centrifuge JTRSY Instance Configuration Document Location [Core]  <!-- UUID: af1d1da5-f77a-4d0e-9fa8-0fef4851eafc -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.2.1.1 - Avalanche - Centrifuge JTRSY Instance Configuration Document](3c731296-858a-4c27-a5cc-6b7ff208cc16).

###### A.6.1.1.2.2.6.1.1.2.2.1.2 - Avalanche - Centrifuge JAAA Instance Configuration Document Location [Core]  <!-- UUID: 975aa703-54ac-4593-a027-7cff0b5e25be -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.2.1.2 - Avalanche - Centrifuge JAAA Instance Configuration Document](bd37d6c9-2e05-4ce3-86dc-3a50d6887e6b).

###### A.6.1.1.2.2.6.1.1.2.2.2 - Curve [Core]  <!-- UUID: aad65f08-6a6f-4246-a356-ba74b83e142c -->

The Avalanche Instances Directory of the Curve Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.2.2.1 - Avalanche - Curve USDS/USDC Swaps Instance Configuration Document Location [Core]  <!-- UUID: b92c6d2f-1b11-42e6-aa63-5a67c40dd487 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.2.2.1 - Avalanche - Curve USDS/USDC Swaps Instance Configuration Document](241a6ad1-ac18-496c-84f8-e2624497c7d9).

###### A.6.1.1.2.2.6.1.1.2.2.2.2 - Avalanche - Curve USDS/USDC LP Instance Configuration Document Location [Core]  <!-- UUID: 2c8a48e0-00c4-41f7-a59a-a7ffc966a6db -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.2.2.2 - Avalanche - Curve USDS/USDC LP Instance Configuration Document](72325c96-455c-4c19-aefc-541206494bd3).

###### A.6.1.1.2.2.6.1.1.2.3 - Base [Core]  <!-- UUID: a53e977f-7bc9-406e-9be1-1f52d9c51416 -->

The documents herein contain a Directory of all Instances on Base of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.1.1.2.3.1 - Morpho [Core]  <!-- UUID: 4953ca03-359c-46a0-b7f1-3625023492d5 -->

The Base Instances Directory of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.3.1.1 - Base - Morpho Grove x Steakhouse High Yield Vault USDC Instance Configuration Document Location [Core]  <!-- UUID: be020cd4-73d4-4fc3-ae39-d38b252defd0 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.3.1.1 - Base - Morpho Grove x Steakhouse High Yield Vault USDC Instance Configuration Document](43d78089-ba75-480c-a277-edaa6eaa6336).

###### A.6.1.1.2.2.6.1.1.2.3.1.2 - Base - Steakhouse Prime Instant USDC Morpho Vault V2 Instance Configuration Document Location [Core]  <!-- UUID: 363c5d9f-9486-4091-8ed6-f909f66ead65 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.3.2 - Base - Steakhouse Prime Instant USDC Morpho Vault V2 Instance Configuration Document](d47ec9c3-b308-453a-989a-7396504f6a99).

###### A.6.1.1.2.2.6.1.1.2.4 - Plasma [Core]  <!-- UUID: 00ec8ca9-deee-45b2-9acc-f24560ad4a13 -->

The documents herein contain a Directory of all Instances on Plasma of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.1.1.2.4.1 - Aave [Core]  <!-- UUID: 8bf1db06-958b-4037-82f4-5b8463eb22a3 -->

The Plasma Instances Directory of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.4.1.1 - Plasma - Aave v3 USDT0 Instance Configuration Document Location [Core]  <!-- UUID: 76b30e0f-543c-43e1-8f8b-2d1145a9cd4e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.4.1.1 - Plasma - Aave v3 USDT0 Instance Configuration Document](7a620ce6-c67a-4c15-b7fb-c8b869a28a0f).

###### A.6.1.1.2.2.6.1.1.2.5 - Plume [Core]  <!-- UUID: 6caa7e89-332b-4f69-a128-7920ef97c4dd -->

The documents herein contain a Directory of all Instances on Plume of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.1.1.2.5.1 - Centrifuge [Core]  <!-- UUID: 6f8bcd5a-5fe1-46ad-b308-761822ac8110 -->

The Plume Instances of the Centrifuge Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.5.1.1 - Plume - Centrifuge ACRDX Instance Configuration Document Location [Core]  <!-- UUID: 71a02530-2732-409f-b45f-486fc3c14387 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.5.1.1 - Plume - Centrifuge ACRDX Instance Configuration Document](a1a1fa83-6c86-49fe-9629-d5ce4b24ed8b).

###### A.6.1.1.2.2.6.1.1.2.6 - Monad [Core]  <!-- UUID: 6018029d-cd76-4ee5-ae14-abd944a5a8ee -->

The documents herein contain a Directory of all Instances on Monad of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.1.1.2.6.1 - Uniswap [Core]  <!-- UUID: 4d7223b6-e446-4a3f-89db-7c98501487e6 -->

The Monad Instances Directory of the Uniswap Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.6.1.1 - Monad - Uniswap AUSD/USDC Instance Configuration Document Location [Core]  <!-- UUID: e033416b-635b-42c0-9757-4797614d6f7f -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.6.1.1 - Monad - Uniswap AUSD/USDC Instance Configuration Document](c4d60460-2694-4d88-bf96-4f4141482cb5).

###### A.6.1.1.2.2.6.1.1.2.7 - Robinhood Chain [Core]  <!-- UUID: c10c4d5a-7eb9-48ef-9d4b-490a894501f1 -->

The documents herein contain a Directory of all Instances on Robinhood Chain of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.1.1.2.7.1 - Morpho [Core]  <!-- UUID: f0d42104-1421-4ad3-9c27-a8f4e01e349d -->

The Robinhood Chain Instances Directory of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.7.1.1 - Robinhood Chain - Grove x Steakhouse USDG Morpho Vault V2 Instance Configuration Document Location [Core]  <!-- UUID: b72252f6-fc92-4dc7-b902-7b93c763ec51 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.7.1.1 - Robinhood Chain - Grove x Steakhouse USDG Morpho Vault V2 Instance Configuration Document](5cd87e2a-a92f-4110-950b-329c7de0d76d).

###### A.6.1.1.2.2.6.1.1.2.7.2 - Paxos [Core]  <!-- UUID: 94adc6f3-dd62-40f6-9d83-1c532be2024c -->

The Robinhood Chain Instances Directory of Paxos with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.1.2.7.2.1 - Robinhood Chain - USDG To USDC Via Paxos Instance Configuration Document Location [Core]  <!-- UUID: 8e6b7785-0e4d-4a9a-90e1-966ede44c252 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.2.2.6.1.3.7.2.1 - Robinhood Chain - USDG To USDC Via Paxos Instance Configuration Document](34064628-ef20-4803-bd03-91c4890c9f85).

###### A.6.1.1.2.2.6.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 70ddaca1-07ca-402f-bf3b-cfab52a8f360 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.6.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 19280fed-ef24-4c95-843a-4abaec1d8bb6 -->

This document contains a Directory of all prospective Instances of the Allocation System Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.6.1.1.2 - Active Instances Directory](1edfe612-6f19-4aa7-b0f9-1b3a2aae8a47), whereas failed Invocations are Archived in [A.6.1.1.2.2.6.1.1.5 - Hub Data Repository](20dc2ba0-0668-4975-b2d7-4f70af20d11b).

###### A.6.1.1.2.2.6.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 20dc2ba0-0668-4975-b2d7-4f70af20d11b -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.6.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: adac5df0-d7b2-424e-a311-cccd58a65437 -->

The subtrees for archived Invocations and Instances of the Allocation System Primitive are stored here.

###### A.6.1.1.2.2.6.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: bd47fcfa-249b-4601-8112-39a8d66d57ad -->

The subtrees for failed Invocations of the Allocation System Primitive are stored here.

###### A.6.1.1.2.2.6.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 230f8964-47e8-4422-905e-d120a06acab0 -->

The subtrees for Instances of the Allocation System Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.6.1.2 - Multi-Instance Coordinator Document [Core]  <!-- UUID: 8dce92af-5b9c-48dd-b40b-d81aa9a0e41b -->

The documents herein provide general specifications of the Grove Liquidity Layer and define Grove’s overarching strategy and operational framework for managing across all Instances.

###### A.6.1.1.2.2.6.1.2.1 - General Specifications [Core]  <!-- UUID: 09be2207-cc0f-4456-b0bc-e9bd91462a47 -->

The documents herein contain general specifications for the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.1.1 - Grove Liquidity Layer Architecture [Core]  <!-- UUID: 8ceb8f78-6c83-4bdb-909f-2dec3875558e -->

The documents herein describe the high-level design of the Grove Liquidity Layer, including its key smart contracts and their functionality.

###### A.6.1.1.2.2.6.1.2.1.1.1 - Grove Liquidity Layer Addresses [Core]  <!-- UUID: 338ff66d-d755-4364-a066-08d43c88c49c -->

The subdocuments herein provide the addresses of the Grove Liquidity Layer’s constituent contracts.

###### A.6.1.1.2.2.6.1.2.1.1.1.1 - Allocator Contract Addresses [Core]  <!-- UUID: 152e89bc-81a5-4bd9-affe-10d9e3e94fce -->

The documents herein contain global key addresses for the Allocator Contracts.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1 - Ethereum Mainnet [Core]  <!-- UUID: f8956105-115a-4873-abb8-68458cbacfcf -->

The documents herein contain the Allocator Contract Addresses on the Ethereum Mainnet.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1.1 - Allocator Vaults And Buffers [Core]  <!-- UUID: 256b2a67-aefc-4294-af1a-9c37ee42794f -->

The Grove Liquidity Layer operates two Allocator Vaults, each with an associated Allocator Buffer. The ALLOCATOR-BLOOM-A Allocator Vault and Buffer serve the monolithic ALM Controller for general allocation activity. The ALLOCATOR-GROVE-A Allocator Vault and Buffer serve the Diamond PAU.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1.1.1 - Allocator Buffer (BLOOM-A) Contract [Core]  <!-- UUID: 599b6748-597f-4a9a-b35b-6638a2f8785f -->

The address of the ALLOCATOR_BLOOM_A_BUFFER contract is: `0x629aD4D779F46B8A1491D3f76f7E97Cb04D8b1Cd`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1.1.2 - Allocator Vault (BLOOM-A) Contract [Core]  <!-- UUID: a2060039-8764-412d-a55b-1f705a0612b3 -->

The address of the ALLOCATOR_BLOOM_A_VAULT contract is: `0x26512A41C8406800f21094a7a7A0f980f6e25d43`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1.1.3 - Allocator Buffer (GROVE-A) Contract [Core]  <!-- UUID: 41b76952-bba6-439f-846c-e761c0e2f1ca -->

The address of the ALLOCATOR_GROVE_A_BUFFER contract is: `0x436DABce608f73BeA2b75fba35bffe72739697d5`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1.1.4 - Allocator Vault (GROVE-A) Contract [Core]  <!-- UUID: 03b954d4-3b94-4815-94fc-bfb66f8ed17f -->

The address of the ALLOCATOR_GROVE_A_VAULT contract is: `0xf739a30c74927dc6cFA3B67E4933872a1FC5F4EB`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1.2 - Allocator Oracle Contract [Core]  <!-- UUID: 49c84e7b-8885-4107-9dd6-05de425c6217 -->

The address of the ALLOCATOR_ORACLE contract is: `0xc7B91C401C02B73CBdF424dFaaa60950d5040dB7`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1.3 - Allocator Registry Contract [Core]  <!-- UUID: d2fdbf24-f6bf-4f67-8c7c-4619e57411c8 -->

The address of the ALLOCATOR_REGISTRY contract is: `0xCdCFA95343DA7821fdD01dc4d0AeDA958051bB3B`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.1.4 - Allocator Roles Contract [Core]  <!-- UUID: b5ab51c6-e66f-418b-9073-25728227847a -->

The address of the ALLOCATOR_ROLES contract is: `0x9A865A710399cea85dbD9144b7a09C889e94E803`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.2 - Base [Core]  <!-- UUID: 366a6ebc-a35d-42a2-ad9b-86932dd3aac4 -->

The documents herein contain the Allocator Contract Addresses on Base.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.2.1 - Grove Executor [Core]  <!-- UUID: ac9b04d0-cd27-45a8-9008-6799dbdb6038 -->

The address of the Grove executor on Base is: `0x491EDFB0B8b608044e227225C715981a30F3A44E`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.2.2 - Grove Receiver [Core]  <!-- UUID: 52f4881b-134f-4eb1-bfe2-ae34abee1a72 -->

The address of the Grove receiver on Base is: `0x5F5cfCB8a463868E37Ab27B5eFF3ba02112dF19a`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.2.3 - Circle CCTP v2 TokenMessenger [Core]  <!-- UUID: 5fa11eb9-4399-4ac0-a6c0-ef03a5875254 -->

The address of the Circle CCTP v2 TokenMessenger contract for transferring USDC between Ethereum Mainnet and Base is: `0x28b5a0e9C621a5BadaA536219b3a228C8168cf5d`.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.3 - Avalanche [Core]  <!-- UUID: b69eb9db-c986-4c19-a718-f0b747640c61 -->

The documents herein contain the Allocator Contract Addresses on Avalanche.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.3.1 - Grove Executor [Core]  <!-- UUID: 4a1a3c1d-2291-4251-bbe5-8afdb1c9b725 -->

The address of the Grove executor on Avalanche is: `0x4b803781828b76EaBF21AaF02e5ce23596b4d60c`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.3.2 - Grove LayerZero v2 Governance Relay Receiver [Core]  <!-- UUID: ae039fcd-37a2-4a47-843c-d079a2508941 -->

The address of the Grove LayerZero v2 governance relay receiver on Avalanche is: `0x380Be2b91B63BF75B194913b6e2C07Df09598c22`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.3.3 - Grove Circle CCTP Governance Relay Receivers [Core]  <!-- UUID: fa8dccc5-6a4d-4e3f-9359-17820060ebc4 -->

The Grove Circle CCTP governance relay receivers on Avalanche are:

- Circle CCTP v1: `0x26e9512547feC1906C55256e491DfB6673D8C23f`
- Circle CCTP v2: `0x8Ea8Dff8c29f568eA1E716E2C3AfbD003EB83cfA`

###### A.6.1.1.2.2.6.1.2.1.1.1.1.3.4 - Circle CCTP v2 TokenMessenger [Core]  <!-- UUID: 2d54c733-b341-41d3-83f2-d3c2d9b8b16d -->

The address of the Circle CCTP v2 TokenMessenger contract for transferring USDC between Ethereum Mainnet and Avalanche is: `0x28b5a0e9C621a5BadaA536219b3a228C8168cf5d`.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.4 - Robinhood Chain [Core]  <!-- UUID: 3b6d2fe2-df1d-4b3e-b3d3-4feb20a9f1ef -->

The documents herein contain the Allocator Contract Addresses on Robinhood Chain.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.4.1 - Grove Executor [Core]  <!-- UUID: bf6cb739-26f4-4e52-a35f-370aac57bd98 -->

The address of the Grove executor on Robinhood Chain is: `0x5ff98717a18833de1A49e11B498866d6Fa1c9296`.

###### A.6.1.1.2.2.6.1.2.1.1.1.1.4.2 - Grove Arbitrum Governance Relay Receiver [Core]  <!-- UUID: 86721704-d060-4fb2-b861-0d35b84e30f4 -->

The address of the Grove Arbitrum governance relay receiver on Robinhood Chain is: `0xa02eC279eEA9E56F4E14449a07C5ca5FDAAdc51d`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2 - Monolithic ALM Contracts [Core]  <!-- UUID: f233a46b-8dff-4335-8ccf-dc3f1c18a96f -->

The documents herein contain addresses for the Monolithic ALM Contracts for the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: f6a76596-678a-45dd-900e-a7109102642e -->

The documents herein contain the ALM Contract Addresses for the Grove Liquidity Layer on the Ethereum Mainnet.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.1.1 - ALM Controller (MainnetController) Contract [Core]  <!-- UUID: 53d016e8-dd83-42ca-a74b-7ed440d50bc5 -->

The address of the ALM_CONTROLLER (MainnetController) contract is: `0xfd9dEA9a8D5B955649579Af482DB7198A392A9F5`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.1.2 - ALM Controller Contract Version [Core]  <!-- UUID: 997b6fab-58d4-4d6d-a67f-f857585e829e -->

The ALM_CONTROLLER contract version is: 1.8.0.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.1.3 - ALM Freezer Multisig (Mainnet) Address [Core]  <!-- UUID: fb21540d-950c-4607-90a3-4736b1f0e517 -->

The address of the Multisig that has the Freezer Role is: `0xB0113804960345fd0a245788b3423319c86940e5`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.1.4 - ALM Relayer Multisig Addresses [Core]  <!-- UUID: 51b50a8f-eb29-4424-bb0a-8247d2acce7d -->

The addresses of the multisigs that have the Relayer Role are specified in [A.6.1.1.2.2.6.1.2.1.2.2.1.1 - Address](2ecf77f4-13d5-40dd-a50f-d85aabdbf71b), [A.6.1.1.2.2.6.1.2.1.2.2.2.1 - Address](49588342-eebf-41e2-89eb-eb4f94ba5f36), and [A.6.1.1.2.2.6.1.2.1.2.2.3.1 - Address](712e0f02-b787-4812-8d67-60a81449b238).

###### A.6.1.1.2.2.6.1.2.1.1.1.2.1.5 - ALM Proxy (Mainnet) Contract [Core]  <!-- UUID: fda13ac2-b3ed-4b2a-9be6-9247632dafe3 -->

The address of the ALM_PROXY contract is: `0x491EDFB0B8b608044e227225C715981a30F3A44E`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.1.6 - ALM Rate Limits (Mainnet) Contract [Core]  <!-- UUID: d647b167-e936-4521-805e-f7851e48fe94 -->

The address of the ALM_RATE_LIMITS contract is: `0x5F5cfCB8a463868E37Ab27B5eFF3ba02112dF19a`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.2 - Avalanche [Core]  <!-- UUID: 621734b8-dfaf-42f2-8ab1-9017e5e9c990 -->

This document contains the ALM Contract Addresses for the Grove Liquidity Layer on Avalanche.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.2.1 - ALM Controller (ForeignController Avalanche) Contract [Core]  <!-- UUID: 6445bdc4-6208-407f-820e-9d1e73213694 -->

The address of the ALM_CONTROLLER (ForeignController) contract is: `0x4236B772BEeEAFF57550Aa392A0f227C0b908Ce7`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.2.2 - ALM Controller Contract Version [Core]  <!-- UUID: 6c937922-9c12-4d89-a987-8cca6bc27ebc -->

The ALM_CONTROLLER contract version is: 1.8.0.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.2.3 - ALM Freezer Multisig (Avalanche) Address [Core]  <!-- UUID: 228514c4-9a74-4324-b93a-4c10025d4bc7 -->

The address of the Multisig that has the Freezer Role is: `0xB0113804960345fd0a245788b3423319c86940e5`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.2.4 - ALM Relayer Multisig (Avalanche) Address [Core]  <!-- UUID: 79a7fa54-db2c-4850-b56b-55b1db8e7463 -->

The address of the Multisig that has the Relayer Role is: `0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.2.5 - ALM Proxy (Avalanche) Contract [Core]  <!-- UUID: 0704f4b5-ee5c-455c-932f-94591b8a6594 -->

The address of the ALM_PROXY contract is: `0x7107DD8F56642327945294a18A4280C78e153644`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.2.6 - ALM Rate Limits (Avalanche) Contract [Core]  <!-- UUID: fae298c2-f505-4d8f-904e-28220926b6d8 -->

The address of the ALM_RATE_LIMITS contract is: `0x6ba2e6bCCe3d2A31F1e3e1d3e11CDffBaA002A21`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.3 - Base [Core]  <!-- UUID: 50e8937a-ae76-49ac-8c50-e2ca21270303 -->

The documents herein contain the ALM Contract Addresses for the Grove Liquidity Layer on Base.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.3.1 - ALM Controller Contract [Core]  <!-- UUID: c3c11dd2-3b15-4f6b-8771-ff1da05f1115 -->

The address of the ALM_CONTROLLER contract is: `0x7f8408eBbBC3504F83eeDa52910dd75Eba92C955`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.3.2 - ALM Controller Contract Version [Core]  <!-- UUID: 312c1860-7eec-4a60-9add-1b64204c2228 -->

The ALM_CONTROLLER contract version is: 1.8.0.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.3.3 - ALM Freezer Multisig Address [Core]  <!-- UUID: 45278dad-c140-4671-9e33-59ba395d8d11 -->

The address of the Multisig that has the Freezer Role is: `0xB0113804960345fd0a245788b3423319c86940e5`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.3.4 - ALM Relayer Multisig Addresses [Core]  <!-- UUID: b8053bf5-44d3-49b7-9eeb-9653df45abd1 -->

The addresses of the Multisigs that have the Relayer Role are: `0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f` and `0x9187807e07112359C481870feB58f0c117a29179`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.3.5 - ALM Proxy Contract [Core]  <!-- UUID: 5c382a94-ce36-4ffa-862b-4718382450fe -->

The address of the ALM_PROXY contract is: `0x9B746dBC5269e1DF6e4193Bcb441C0FbBF1CeCEe`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.3.6 - ALM Rate Limits Contract [Core]  <!-- UUID: a92d0054-8cc7-429b-91bb-dea4f0896e20 -->

The address of the ALM_RATE_LIMITS contract is: `0xAc8BF0669223197ac8B94Cbb53E725e40B3919E8`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.4 - Plasma [Core]  <!-- UUID: eae5ccc0-69e4-4210-8676-0f425e599f87 -->

The documents herein contain the ALM Contract Addresses for the Grove Liquidity Layer on Plasma.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.4.1 - ALM Controller Contract [Core]  <!-- UUID: 04952825-fe04-4459-ba45-01b44d21f606 -->

The address of the ALM_CONTROLLER contract is: `0x85b0E7F3A7C1aB0E1aDea7dfAaD416D8A6e00f0e`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.4.2 - ALM Controller Contract Version [Core]  <!-- UUID: ed9f98fd-bdaf-4779-a5d2-66b8194aa796 -->

The ALM_CONTROLLER contract version will be specified in a future iteration of the Atlas.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.4.3 - ALM Freezer Multisig Address [Core]  <!-- UUID: c7c722e6-f0d7-4182-afe1-ac260ce2482b -->

The address of the Multisig that has the Freezer Role is `0xB0113804960345fd0a245788b3423319c86940e5`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.4.4 - ALM Relayer Multisig Address [Core]  <!-- UUID: 9a69f651-4e37-4c7e-8ecc-e93d0d36e358 -->

The address of the Multisig that has the Relayer Role is `0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.4.5 - ALM Proxy Contract [Core]  <!-- UUID: 9d0bcc23-02d4-4389-9c85-707acf900dee -->

The address of the ALM_PROXY contract is: `0x0C462Fff7Cc975bC9F2B0aEB8270febA5FD71e1B`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.4.6 - ALM Rate Limits Contract [Core]  <!-- UUID: 59485651-9961-4382-8aa0-71b140a9105e -->

The address of the ALM_RATE_LIMITS contract is: `0x1e993F992B90eE50115CD7bA2E7432a9c345d0c4`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.5 - Plume [Core]  <!-- UUID: f2a1de37-0a71-45be-9dbb-8501c1a98252 -->

The documents herein contain the ALM Contract Addresses for the Grove Liquidity Layer on Plume.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.5.1 - ALM Controller Contract [Core]  <!-- UUID: 15083990-2c69-45c1-93ab-8d48d140159c -->

The address of the ALM_CONTROLLER contract is: `0x0C462Fff7Cc975bC9F2B0aEB8270febA5FD71e1B`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.5.2 - ALM Controller Contract Version [Core]  <!-- UUID: 51739c12-4a4b-429c-a238-b1bdd554decf -->

The ALM_CONTROLLER contract version is: 1.6.0.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.5.3 - ALM Freezer Multisig Address [Core]  <!-- UUID: f655efd0-cbce-4c42-9c80-64f8358a339e -->

The address of the Multisig that has the Freezer Role is `0xB0113804960345fd0a245788b3423319c86940e5`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.5.4 - ALM Relayer Multisig Address [Core]  <!-- UUID: 9e0a7a51-7cc1-4dce-9465-8b3961d14f1d -->

The address of the Multisig that has the Relayer Role is `0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.5.5 - ALM Proxy Contract [Core]  <!-- UUID: dcf0beac-b93e-41a7-b8b6-98c1d4cc819b -->

The address of the ALM_PROXY contract is: `0x1DB91ad50446a671e2231f77e00948E68876F812`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.5.6 - ALM Rate Limits Contract [Core]  <!-- UUID: 441a9fa5-4dcc-45f5-83a7-644128c23b05 -->

The address of the ALM_RATE_LIMITS contract is: `0x7f8408eBbBC3504F83eeDa52910dd75Eba92C955`

###### A.6.1.1.2.2.6.1.2.1.1.1.2.6 - Robinhood Chain [Core]  <!-- UUID: 51488328-7902-4f92-be88-b21f976c9c79 -->

The documents herein contain the ALM Contract Addresses for the Grove Liquidity Layer on Robinhood Chain.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.6.1 - ALM Controller Contract [Core]  <!-- UUID: 645a2973-0c56-4675-852a-47c8b646621d -->

The address of the ALM_CONTROLLER contract is: `0x2c10885ddec8d52ecF3Ad2B3833765bf36eD80cf`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.6.2 - ALM Controller Contract Version [Core]  <!-- UUID: 83c9f653-12a7-43c2-992e-9244293965f8 -->

The ALM_CONTROLLER contract version is: 1.8.0.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.6.3 - ALM Freezer Multisig Address [Core]  <!-- UUID: fa3e13f2-6837-499b-82b6-b4b9f78a9d08 -->

The address of the Multisig that has the Freezer Role is: `0xB0113804960345fd0a245788b3423319c86940e5`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.6.4 - ALM Relayer Multisig Addresses [Core]  <!-- UUID: 4210841c-c76a-4d9b-bfdd-0c11f23c785a -->

The addresses of the Multisigs that have the Relayer Role are: `0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f` and `0x9187807e07112359C481870feB58f0c117a29179`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.6.5 - ALM Proxy Contract [Core]  <!-- UUID: 7ca6e88c-018a-4735-9753-7702d28e292b -->

The address of the ALM_PROXY contract is: `0x29626c2d8Ca49A51E4dECEEc5499e52983c42BD5`.

###### A.6.1.1.2.2.6.1.2.1.1.1.2.6.6 - ALM Rate Limits Contract [Core]  <!-- UUID: 6f07e646-0a9b-422f-88ff-0f6f1ed04086 -->

The address of the ALM_RATE_LIMITS contract is: `0xC13e5ff7993c5df911aE562a7736B0eBA12b2010`.

###### A.6.1.1.2.2.6.1.2.1.1.1.3 - Tokenized Treasury Contracts [Core]  <!-- UUID: fc2fdc98-db17-4c10-91c1-50d05bd5bf9b -->

The documents herein define the addresses of shared Tokenized Treasury contracts used across Tokenized Treasury Instances of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.2.1.1.1.3.1 - Ethereum Mainnet [Core]  <!-- UUID: 87773690-d9bc-4772-a39e-005552df0896 -->

This document contains the shared Tokenized Treasury contract addresses on Ethereum Mainnet.

###### A.6.1.1.2.2.6.1.2.1.1.1.3.1.1 - Basin Factory Contract [Core]  <!-- UUID: 11401b83-fc65-4c0a-8d57-503c1c2041ea -->

The address of the Basin Factory contract, used to deterministically deploy each Basin, is: `0x78Dc98D689Fe9A1b0056ac1cDFC14722bDA6D49a`.

###### A.6.1.1.2.2.6.1.2.1.1.1.3.1.2 - Tokenized Treasury USDS And USDC Rate Provider Contract [Core]  <!-- UUID: 21933aee-36b7-425f-8ad7-5ccd1c046c1a -->

The address of the Fixed Rate Provider contract pricing USDS and USDC, shared across Tokenized Treasury Instances that use USDS and USDC, is: `0x7928A185B8137D1CD2a0996a810A04dB2837419D`.

###### A.6.1.1.2.2.6.1.2.1.1.1.3.1.3 - Sky USDS And USDC PSM Wrapper Contract [Core]  <!-- UUID: 75699288-150e-45e0-8c4a-19c40e4c1e94 -->

The address of the Sky USDS and USDC PSM Wrapper contract is: `0xA188EEC8F81263234dA3622A406892F3D630f98c`.

###### A.6.1.1.2.2.6.1.2.1.1.1.4 - Diamond PAU Contracts [Core]  <!-- UUID: 887ff8b9-ccdb-49e2-a87a-ef92e38e1416 -->

The documents herein define the addresses of the Diamond Parallelized Allocation Unit (Diamond PAU) contracts deployed for the Grove Liquidity Layer. The Diamond PAU is a modular implementation of the Allocation System in which the Controller dispatches operations to shared Facet contracts, with integration configurations held in a shared Beacon contract. The Beacon and the Facet contracts are shared across Diamond PAU implementations and are specified in [A.2.2.10.1.1.1.2.3 - Liquidity Layer Shared Contracts](a2677d19-1f2c-4361-bedc-34cb2e7eaab5).

###### A.6.1.1.2.2.6.1.2.1.1.1.4.1 - Ethereum Mainnet [Core]  <!-- UUID: d7a4d3e1-cfe9-4c6c-a902-0fe066edf7e4 -->

The documents herein define the addresses of the Diamond PAU contracts on Ethereum Mainnet.

###### A.6.1.1.2.2.6.1.2.1.1.1.4.1.1 - ALM Proxy Contract [Core]  <!-- UUID: c10638fb-177c-4a90-8af5-3e3b4ee3faed -->

The address of the ALM Proxy contract is: `0x0DcD9298e163dFD3c0B5b00F0d9093C36e40A153`. The ALM Proxy custodies the Instance's funds and routes calls to external contracts as directed by the Controller contract.

###### A.6.1.1.2.2.6.1.2.1.1.1.4.1.2 - Controller Contract [Core]  <!-- UUID: 6c83e356-0ac3-47aa-8ae5-bad377564e7a -->

The address of the Controller contract is: `0xbf83F5974B932c7D842254042717D6A2706CE5eE`. The Controller is the entry point for all allocator operations; it synchronizes integration configurations from the Beacon contract and dispatches calls to the appropriate facet contract.

###### A.6.1.1.2.2.6.1.2.1.1.1.4.1.3 - AccessControls Contract [Core]  <!-- UUID: 0b4d0fb8-01ed-42fc-92f6-b24e09cf0f48 -->

The address of the AccessControls contract is: `0x4F6d1704700cd494DD4cd9bF59c0C39DA1Bc9164`. The AccessControls contract manages the roles and permissions of the Diamond PAU, as specified in [A.6.1.1.2.2.6.1.2.2.1.1.3 - Diamond PAU Role Hierarchy And Permissions](c4149166-7e65-48d3-81f9-177a4f3f6364).

###### A.6.1.1.2.2.6.1.2.1.1.1.4.1.4 - ALM Rate Limits Contract [Core]  <!-- UUID: 01a29f9f-ff48-4e40-9b6d-592af97e1204 -->

The address of the ALM Rate Limits contract is: `0xE016Ae733A77Ba77E7907aAA749394Fc5e75C0e1`. The ALM Rate Limits contract enforces the rate limits on operations performed through the Controller contract.

###### A.6.1.1.2.2.6.1.2.1.1.1.4.1.5 - AdministeredAgent Contract [Core]  <!-- UUID: d58e14aa-0901-4aa9-af44-6281161be162 -->

The address of the AdministeredAgent contract is: `0xdBD17832df0e57b1732cE1C84c652E820e549BAa`. The AdministeredAgent holds the Allocator Role of the Diamond PAU and mediates relayer access to the Controller: the relayer multisigs are registered as its actors and submit operations through it, while the Freezer Multisig is registered as a revoker authorized to remove a compromised actor, as specified in [A.6.1.1.2.2.6.1.2.2.1.1.3 - Diamond PAU Role Hierarchy And Permissions](c4149166-7e65-48d3-81f9-177a4f3f6364).

###### A.6.1.1.2.2.6.1.2.1.1.2 - Off-chain Operational Parameters [Core]  <!-- UUID: ec6cc8a0-3811-485a-9f9a-78f388659d46 -->

The documents herein list the off-chain operational parameters for the Grove Liquidity Layer. These operational parameters are protocol settings managed outside of smart contracts (off-chain), used by operators and off-chain systems to guide the functioning of the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.1.1.2.1 - Off-chain Operational Parameters For Ethereum Mainnet [Core]  <!-- UUID: 15554f42-3b63-4f11-a7e3-2e02c91d7171 -->

The document herein lists the current off-chain operational parameters for the Grove Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.2.2.6.1.2.1.1.2.1.1 - Minimum Operation Size Ethereum Mainnet [Core]  <!-- UUID: cad9056b-c097-4b3c-9958-e8962d8ef1ca -->

The minimum transaction size for operations on Ethereum Mainnet is (`MAINNET_MIN_OPERATION_SIZE`):

- This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.1.2.1.2 - Debt Ceiling Buffer Ethereum Mainnet [Core]  <!-- UUID: 1500fd24-2b7e-4a1c-8725-84e7a0b8adc5 -->

The buffer amount below the maximum debt ceiling is (`DEBT_CEILING_BUFFER`):

- This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.1.2.2 - Off-chain Operational Parameters For Avalanche [Core]  <!-- UUID: ad3dbd7b-602b-4457-bc5e-25ed5708fbc2 -->

The document herein lists the current off-chain operational parameters for the Grove Liquidity Layer on Avalanche.

###### A.6.1.1.2.2.6.1.2.1.1.2.2.1 - Minimum Operation Size Avalanche [Core]  <!-- UUID: 29e17dd9-c575-496a-9c20-658aa92a260b -->

The minimum transaction size for operations on Avalanche is (`AVALANCHE_MIN_OPERATION_SIZE`):

- This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.1.3 - RateLimits [Core]  <!-- UUID: c485dc9b-e21b-4df9-8323-0d2856524a71 -->

The documents herein list the rate limits for the Grove Liquidity Layer, covering the monolithic ALM Controller and the Diamond PAU.

###### A.6.1.1.2.2.6.1.2.1.1.3.1 - Monolithic ALM Rate Limits [Core]  <!-- UUID: 40aaa27c-4afa-4e6b-bc3b-422b46ad2640 -->

The documents herein list the rate limits for the monolithic ALM Controller of the Grove Liquidity Layer on each blockchain.

###### A.6.1.1.2.2.6.1.2.1.1.3.1.1 - Ethereum Mainnet [Core]  <!-- UUID: 7fe3ae46-d78e-428d-b41e-c2c49417fc3e -->

The documents herein list the current `RateLimits` for the Grove Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.2.2.6.1.2.1.1.3.1.1.1 - USDS Mint Maximum [Core]  <!-- UUID: 104541de-f257-405a-8870-ab26d099f57b -->

The maximum amount of USDS that can be minted within the Grove Liquidity Layer (`LIMIT_USDS_MINT`) is specified in the document herein.

- `maxAmount`: 500,000,000 USDS
- `slope`: 500,000,000 USDS per day

###### A.6.1.1.2.2.6.1.2.1.1.3.1.1.2 - USDS Burn Maximum [Core]  <!-- UUID: cf829503-02cf-4b84-8c04-7d05de1d82dd -->

The maximum amount of USDS that can be burned within the Grove Liquidity Layer (`LIMIT_USDS_BURN`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Grove Artifact.
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.1.3.1.1.3 - USDS For USDC Swap Maximum [Core]  <!-- UUID: a591104c-5c45-480d-a156-46484440e163 -->

The maximum amount of USDS that can be swapped for USDC by the Grove Liquidity Layer in the Mainnet PSM (`LIMIT_USDS_TO_USDC`) is specified in the document herein.

- `maxAmount`: 500,000,000 USDC
- `slope`: 500,000,000 USDC per day

###### A.6.1.1.2.2.6.1.2.1.1.3.1.1.4 - USDC Mainnet ALM Proxy Maximum [Core]  <!-- UUID: 8a462b2a-68dc-4caf-ab26-855552f57d4f -->

The maximum amount of USDC that can be sent to the Ethereum Mainnet ALM Proxy (`LIMIT_USDC_TO_DOMAIN`, hashed with Ethereum domain) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Grove Artifact.
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.1.3.1.1.5 - Maximum USDC Bridged To Ethereum Mainnet Via Circle CCTP [Core]  <!-- UUID: b43ee2cd-06b9-4615-bcb4-ac44e2b8c693 -->

The maximum amount of USDC that can be bridged to Ethereum Mainnet ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_ETH`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: 0

###### A.6.1.1.2.2.6.1.2.1.1.3.1.1.6 - Maximum USDS Bridged From Ethereum Mainnet To Avalanche Via SkyLink [Core]  <!-- UUID: f6094634-372c-4235-beba-0862922809fb -->

The maximum amount of USDS that can be sent to the Avalanche ALM Controller via SkyLink (`LIMIT_LAYERZERO_TRANSFER`, hashed with Avalanche USDS OFT address and Avalanche destination domain) is specified in the document herein.

- `maxAmount`: 50,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.2.2.6.1.2.1.1.3.1.2 - Avalanche [Core]  <!-- UUID: b650c48d-435c-47e3-ac33-17ab6187492f -->

The documents herein list the current `RateLimits` for the Grove Liquidity Layer on Avalanche.

###### A.6.1.1.2.2.6.1.2.1.1.3.1.2.1 - USDC Avalanche ALM Proxy Maximum [Core]  <!-- UUID: 00b438d4-d359-4e2f-a1fa-4c12aaf8c978 -->

The maximum amount of USDC that can be sent to the Avalanche ALM Proxy (`LIMIT_USDC_TO_DOMAIN`, hashed with Avalanche domain) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Grove Artifact.
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.1.3.1.2.2 - Maximum USDC Bridged From Ethereum Mainnet To Avalanche Via Circle CCTP [Core]  <!-- UUID: d5b284c1-8cb7-4e49-8efc-6253b517f36e -->

The maximum amount of USDC that can be bridged to Avalanche ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_Avalanche`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.2.1.1.3.1.2.3 - Maximum USDC Bridged From Avalanche To Ethereum Mainnet Via Circle CCTP [Core]  <!-- UUID: a3b52620-db3f-40fa-80d5-a7eacf52090c -->

The maximum amount of USDC that can be bridged to Ethereum Mainnet from the Avalanche ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_Ethereum`) is specified in the document herein.

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.2.2.6.1.2.1.1.3.1.2.4 - Maximum USDS Bridged From Avalanche To Ethereum Mainnet Via SkyLink [Core]  <!-- UUID: dec9ce16-90ba-48bd-b299-9462cb50de2c -->

The maximum amount of USDS that can be sent to the Ethereum Mainnet ALM Controller from Avalanche via SkyLink (`LIMIT_LAYERZERO_TRANSFER`, hashed with Ethereum Mainnet USDS OFT address and Ethereum Mainnet destination domain) is specified in the document herein.

- `maxAmount`: 20,000,000 USDS
- `slope`: 20,000,000 USDS per day

###### A.6.1.1.2.2.6.1.2.1.1.3.1.3 - Base [Core]  <!-- UUID: cedb7b47-c7e6-4948-8835-5862a65592cc -->

The documents herein list the current `RateLimits` for the Grove Liquidity Layer on Base.

###### A.6.1.1.2.2.6.1.2.1.1.3.1.3.1 - USDC Base ALM Proxy Maximum [Core]  <!-- UUID: dba2c846-ecbe-4227-abfc-63dbd654af48 -->

The maximum amount of USDC that can be sent to the Base ALM Proxy (`LIMIT_USDC_TO_DOMAIN`, hashed with Base domain) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Grove Artifact.
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.1.3.1.3.2 - Maximum USDC Bridged From Ethereum Mainnet To Base Via Circle CCTP [Core]  <!-- UUID: 34e5a190-ec23-4449-8cf1-1125f78a6e44 -->

The maximum amount of USDC that can be bridged to Base ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_Base`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.2.1.1.3.1.3.3 - Maximum USDC Bridged From Base To Ethereum Mainnet Via Circle CCTP [Core]  <!-- UUID: 9575357d-2778-4556-80d8-ca1e4ab293a6 -->

The maximum amount of USDC that can be bridged to Ethereum Mainnet from the Base ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_Ethereum`) is specified in the document herein.

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.2.1.1.3.2 - Diamond PAU Rate Limits [Core]  <!-- UUID: c5d3d2f9-cd88-4b00-a6df-da369c27674f -->

The documents herein list the controller-wide rate limits for the Grove Diamond PAU on Ethereum Mainnet. Instance-specific rate limits are specified in each Instance Configuration Document.

###### A.6.1.1.2.2.6.1.2.1.1.3.2.1 - USDS Mint Maximum [Core]  <!-- UUID: 659aaf71-7899-47f6-977d-afc23a188833 -->

The maximum amount of USDS that can be minted by the Grove Diamond PAU (`LIMIT_USDS_MINT`) is specified in the document herein.

- `maxAmount`: 5,000,000 USDS
- `slope`: 5,000,000 USDS per day

###### A.6.1.1.2.2.6.1.2.1.1.3.2.2 - USDS Burn Maximum [Core]  <!-- UUID: a444f64b-519a-4e52-a538-395c9ee04956 -->

The maximum amount of USDS that can be burned by the Grove Diamond PAU (`LIMIT_USDS_BURN`) is specified in the document herein.

- `maxAmount`: 5,000,000 USDS
- `slope`: 5,000,000 USDS per day

###### A.6.1.1.2.2.6.1.2.1.1.3.2.3 - USDS For USDC Swap Maximum [Core]  <!-- UUID: 7e53acf8-10e7-4250-a05c-bab8354aa738 -->

The maximum amount of USDS that can be swapped for USDC by the Grove Diamond PAU in the Mainnet PSM (`LIMIT_USDS_TO_USDC`) is specified in the document herein.

- `maxAmount`: 5,000,000 USDC
- `slope`: 5,000,000 USDC per day

###### A.6.1.1.2.2.6.1.2.1.1.3.2.4 - USDC For USDS Swap Maximum [Core]  <!-- UUID: 6ca30d6e-df7f-47f9-93c3-b20bae6762a3 -->

The maximum amount of USDC that can be swapped for USDS by the Grove Diamond PAU in the Mainnet PSM (`LIMIT_USDC_TO_USDS`) is specified in the document herein.

- `maxAmount`: 5,000,000 USDC
- `slope`: 5,000,000 USDC per day

###### A.6.1.1.2.2.6.1.2.1.1.4 - On-chain Parameters [Core]  <!-- UUID: 21a390bd-ffc4-4f14-b8fd-e30aacdcee89 -->

The documents herein list general on-chain parameters for the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.1.1.4.1 - Allocator Vault Parameters [Core]  <!-- UUID: 4db4b613-f06c-4aae-a091-2a78521fb6de -->

The Allocator Vault parameters for ALLOCATOR-BLOOM-A are defined in [A.3.7.1.2.1.2 - ALLOCATOR-BLOOM-A Parameters](53cba245-68c6-4af9-a280-b200dabebec7).

###### A.6.1.1.2.2.6.1.2.1.1.4.2 - Whitelisting Of ALM Proxy [Core]  <!-- UUID: 6823cc5a-6667-4754-a030-9ac7126b006e -->

The ALM Proxy for the Grove Diamond PAU has been whitelisted on the Lite PSM. This allows it to call `buyGemNoFee` and `sellGemNoFee` on the `MCD_LITE_PSM_USDC_A` contract, enabling the PSM Facet swap operations, as specified in [A.2.2.10.1.1.1.2.5.2.4.1 - Swap USDS To USDC](bff6ae57-ce3e-4520-ad46-5fe87b721408) and [A.2.2.10.1.1.1.2.5.2.4.2 - Swap USDC To USDS](3fd327ea-7043-434a-996a-3419e7692959).

###### A.6.1.1.2.2.6.1.2.1.2 - Governance Processes [Core]  <!-- UUID: 6859900b-3d53-4a5c-8a00-ddb1cf0c07a4 -->

The documents herein describe the specific governance processes for the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.1.2.1 - Invoking New Instances [Core]  <!-- UUID: edf44383-44e6-4aaa-972a-7dfdaee0998d -->

The governance process to invoke a new Instance of the Allocation System Primitive follows the Root Edit process see [A.6.1.1.2.2.2.2.2.1.2 - Operational Process Definition](40826926-adb2-4de3-936d-702e2d8cb3b9).

###### A.6.1.1.2.2.6.1.2.1.2.2 - Multisigs [Core]  <!-- UUID: 355db9eb-fc32-4a27-819a-42e8c2f26b1b -->

The documents herein define multisigs that have privileged access to manage the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.1.2.2.1 - Prime Primary Relayer Multisig [Core]  <!-- UUID: 5e6f63a8-d0e5-441d-927b-13830f5f9b24 -->

The Prime Primary Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.2.2.6.1.2.2.1.1.1.2 - Relayer Role](4639e60c-111f-4018-bc8d-501b88c20edd) and is controlled by Grove.

###### A.6.1.1.2.2.6.1.2.1.2.2.1.1 - Address [Core]  <!-- UUID: 2ecf77f4-13d5-40dd-a50f-d85aabdbf71b -->

The address of the Prime Primary Relayer Multisig is `0x0eEC86649E756a23CBc68d9EFEd756f16aD5F85f`.

###### A.6.1.1.2.2.6.1.2.1.2.2.1.2 - Required Number Of Signers [Core]  <!-- UUID: 7c9c4334-71c3-4e55-ad66-7970d244a1a0 -->

The Prime Primary Relayer Multisig currently has a 4/7 signing requirement.

###### A.6.1.1.2.2.6.1.2.1.2.2.1.3 - Signers [Core]  <!-- UUID: 10b61bac-2e7a-4607-b464-75ac1635c102 -->

The signers of the Prime Primary Relayer Multisig are seven (7) addresses controlled by Grove.

###### A.6.1.1.2.2.6.1.2.1.2.2.1.4 - Usage Standards [Core]  <!-- UUID: b3f2fd41-9682-46ff-b85e-4a0f0d0885b5 -->

The signers of the Prime Primary Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.2.2.1.5 - Modification [Core]  <!-- UUID: 8baba39e-0d83-4d64-b15a-cf9948583a5e -->

Grove can change the signers of the Prime Primary Relayer Multisig at any time, so long as there are at least two (2) signers and at least a majority of signers are required to execute transactions.

###### A.6.1.1.2.2.6.1.2.1.2.2.2 - Prime Secondary Relayer Multisig [Core]  <!-- UUID: bc712bee-9788-4f31-b671-fbc5aafaf42c -->

The Prime Secondary Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.2.2.6.1.2.2.1.1.1.2 - Relayer Role](4639e60c-111f-4018-bc8d-501b88c20edd) and is controlled by Grove.

###### A.6.1.1.2.2.6.1.2.1.2.2.2.1 - Address [Core]  <!-- UUID: 49588342-eebf-41e2-89eb-eb4f94ba5f36 -->

The address of the Prime Secondary Relayer Multisig is `0x9187807e07112359C481870feB58f0c117a29179`.

###### A.6.1.1.2.2.6.1.2.1.2.2.2.2 - Required Number Of Signers [Core]  <!-- UUID: 8f0b88bf-0fcd-4103-a4c2-e03b61a2e8a7 -->

The Prime Secondary Relayer Multisig currently has a 1/2 signing requirement.

###### A.6.1.1.2.2.6.1.2.1.2.2.2.3 - Signers [Core]  <!-- UUID: 2ff0395a-f47a-478a-8621-28bae36bc2f7 -->

The signers of the Prime Secondary Relayer Multisig are two (2) addresses controlled by Grove.

###### A.6.1.1.2.2.6.1.2.1.2.2.2.4 - Usage Standards [Core]  <!-- UUID: d50351e8-6cca-4d49-abb8-0c7ce3b16b92 -->

The signers of the Prime Secondary Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.2.2.2.5 - Modification [Core]  <!-- UUID: eecf9254-7939-492a-a4c8-938bbb19c7a0 -->

Grove can change the signers of the Prime Secondary Relayer Multisig at any time, so long as there are at least two (2) signers and at least a majority of signers are required to execute transactions.

###### A.6.1.1.2.2.6.1.2.1.2.2.3 - Core Operator Relayer Multisig [Core]  <!-- UUID: be75c381-80e1-4c95-8b8b-e990f00a178e -->

The Core Operator Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.2.2.6.1.2.2.1.1.1.2 - Relayer Role](4639e60c-111f-4018-bc8d-501b88c20edd), and is controlled by Operational GovOps Soter Labs.

###### A.6.1.1.2.2.6.1.2.1.2.2.3.1 - Address [Core]  <!-- UUID: 712e0f02-b787-4812-8d67-60a81449b238 -->

The address of the Core Operator Relayer Multisig on the Ethereum Mainnet is `0x4364D17B578b0eD1c42Be9075D774D1d6AeAFe96`.

###### A.6.1.1.2.2.6.1.2.1.2.2.3.2 - Required Number Of Signers [Core]  <!-- UUID: 9a1af2ad-da1b-460f-89f6-84c513c71418 -->

The Core Operator Relayer Multisig currently has a 2/3 signing requirement.

###### A.6.1.1.2.2.6.1.2.1.2.2.3.3 - Signers [Core]  <!-- UUID: 7a7df887-8cdf-447e-8d8e-aad3360c7417 -->

The signers of the Core Operator Relayer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs.

###### A.6.1.1.2.2.6.1.2.1.2.2.3.4 - Usage Standards [Core]  <!-- UUID: 2014eee2-c5e7-4da7-8925-04b5e4bfd6f5 -->

The signers of the Core Operator Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.1.2.2.3.5 - Modification [Core]  <!-- UUID: f789a1aa-ddfb-4ddd-85c4-76387ef6d516 -->

Operational GovOps Soter Labs can change the signers of the Core Operator Relayer Multisig at any time, so long as there are at least three (3) signers and at least two-thirds of signers are required to execute transactions.

###### A.6.1.1.2.2.6.1.2.1.2.2.4 - Freezer Multisig [Core]  <!-- UUID: 99bc2dd5-5573-4bb9-9210-5af299d058d9 -->

The Freezer Multisig has the `FREEZER_ROLE` for the monolithic ALM Controller as defined in [A.6.1.1.2.2.6.1.2.2.1.1.1.4 - Freezer Role](37871a80-dc8f-4804-bce1-5f082e9bca9f), and holds the equivalent Freezer Role for the Diamond PAU as defined in [A.6.1.1.2.2.6.1.2.2.1.1.3.4 - Freezer Role](d910ae36-1251-4385-b989-f303878ed094).

###### A.6.1.1.2.2.6.1.2.1.2.2.4.1 - Address [Core]  <!-- UUID: 33cb22ad-7032-4eec-ab47-4c5f5d28e064 -->

The address of the Freezer Multisig on the Ethereum Mainnet is `0xB0113804960345fd0a245788b3423319c86940e5`.

###### A.6.1.1.2.2.6.1.2.1.2.2.4.2 - Required Number Of Signers [Core]  <!-- UUID: 939338a1-df49-47cb-9206-810059b6c16a -->

The Freezer Multisig currently has a 2/5 signing requirement.

###### A.6.1.1.2.2.6.1.2.1.2.2.4.3 - Signers [Core]  <!-- UUID: 0a18da19-36e2-4948-93cc-ee86d20617b3 -->

The signers of the Freezer Multisig are two (2) addresses controlled by Operational GovOps Soter Labs, two (2) addresses controlled by Operational Facilitator Endgame Edge, and one (1) address controlled by Grove.

###### A.6.1.1.2.2.6.1.2.1.2.2.4.4 - Usage Standards [Core]  <!-- UUID: 1bd5fe5c-6cb4-4a5a-a84a-03e59736c98a -->

The signers of the Freezer Multisig should exercise their authority to freeze the Grove Liquidity Layer in the event that Grove is not complying with rules regarding Risk Capital or Asset Liability Management, or in the event of another emergency.

Each action executed by the Freezer Multisig, including any function calls and their parameters, must be reported to the Sky community within a reasonable time frame through a post on the Sky Forum.

###### A.6.1.1.2.2.6.1.2.1.2.2.4.5 - Modification [Core]  <!-- UUID: 827f87da-917e-4acf-af0a-9e220641b145 -->

Modification of the signers of the Freezer Multisig must be approved through an Atlas Edit Proposal.

The only exceptions to this are if: 1) a signer self-reports a loss of access to their private key due to any reason; or 2) a signer explicitly expresses their wish to be removed as a signer. In both cases, the signer is required to communicate the loss of access to their private key, or the wish to be removed as a signer, in the form of a public Sky Forum post. The specific signer should be replaced as soon as possible.

Any changes to the Multisig signers that do not fall within the two exceptions listed above, or that have not been ratified by Sky Governance, should be questioned immediately and treated as malicious. Where malicious activity is suspected, the Core Facilitator must prepare an expedited Executive Vote so that Sky Governance can vote on removing external security access from the Multisig.

###### A.6.1.1.2.2.6.1.2.1.2.3 - USD Stablecoin To USDS Swap Authorization [Core]  <!-- UUID: aa16daa3-ee62-49eb-851e-cb0708670144 -->

Grove is authorized to swap USD stablecoins held in the Grove SubProxy Account, as specified in [A.6.1.1.2.2.1.1.3.1.1.2 - SubProxy Account](d143241d-5819-432d-a6ba-892961502838), to USDS. Such swaps must be executed at a rate of approximately 1:1 (divergence not to exceed 0.1%) and each swap must be documented in a Forum post under the "Grove Prime" category, containing the Technical Scope as specified in [A.1.10.2.3.2.2.3.2.2 - Prime Agent Publishes Spell Actions On Sky Forum](2c577553-830f-4b9f-ab5f-dddd0fd62cfa). Swaps meeting these requirements may be included directly in a Grove Spell submitted to a Sky Executive Vote, with no prior token holder vote needed.

###### A.6.1.1.2.2.6.1.2.1.3 - Total Risk Capital (TRC) Management [Core]  <!-- UUID: 3567039f-c74a-4f4c-85c9-e68ac880009a -->

The documents herein specify requirements related to Grove’s Total Risk Capital (TRC) management.

###### A.6.1.1.2.2.6.1.2.1.3.1 - Grove Development Company’s Operation Of Grove Liquidity Layer And Agreement Regarding Encumbrance Ratio [Core]  <!-- UUID: b5120b66-7007-4f0c-977f-a441a7067f92 -->

Grove Development Company will operate the Grove Liquidity Layer and agrees to stay at or below a 90% Encumbrance Ratio. See [A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9).

###### A.6.1.1.2.2.6.1.2.1.3.2 - Grove Development Company’s Total Risk Capital (TRC) Management Processes [Core]  <!-- UUID: 35b828fe-4bf3-49e3-a87b-95751562f2b5 -->

As operators of the Grove Liquidity Layer, Grove Development Company automatically inherits, and is subject to, the base class of operational requirements related to Total Risk Capital management defined in [A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capital (TRC) Management](3af8a3a2-25e5-44b3-87a4-7df1f2712685). Modifications to the base operational logic automatically propagate to the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.2 - Grove Liquidity Layer Operational Processes [Core]  <!-- UUID: e5d30bed-ae48-459e-92f1-2a97f21855b7 -->

The documents herein describe common operational procedures for the Grove Liquidity Layer applicable across multiple Instances.

###### A.6.1.1.2.2.6.1.2.2.1 - Routine Protocol [Core]  <!-- UUID: eed08bf3-af5a-4cae-ae12-95ef5c6b6798 -->

The documents herein define the protocol for routine ongoing management of the Grove Liquidity Layer and its active Instances.

###### A.6.1.1.2.2.6.1.2.2.1.1 - Role Hierarchies And Permissions [Core]  <!-- UUID: 6b494fe8-3482-4309-9fb5-1f26631b0191 -->

The documents herein define the role hierarchies and permissions for each Instance of the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.1.1 - Monolithic ALM Role Hierarchy And Permissions [Core]  <!-- UUID: dd9524c4-136c-4e52-a9af-0390517361d5 -->

The documents herein define roles (Admin, Relayer, Freezer) and their responsibilities/permissions for the monolithic ALM Controller of the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.1.1.1 - Default Admin Role [Core]  <!-- UUID: dc515367-2fa0-4f98-b3d1-1b82d7ce782f -->

The admin role (`DEFAULT_ADMIN_ROLE`) is the role that can grant and revoke any role, including itself and all other roles defined in the contract. The admin role is also used for general admin functions in all contracts. This role is fully controlled by Sky Governance via the Grove Proxy.

`constructor(address admin) {
        _grantRole(DEFAULT_ADMIN_ROLE, admin);`

###### A.6.1.1.2.2.6.1.2.2.1.1.1.2 - Relayer Role [Core]  <!-- UUID: 4639e60c-111f-4018-bc8d-501b88c20edd -->

The `RELAYER_ROLE` is the address for the Grove Liquidity Layer ALM Planner off-chain system that calls functions on `Controller` contracts to perform actions on behalf of the `ALMProxy` contract. The Relayer Role may be granted to an address by any address holding the `DEFAULT_ADMIN_ROLE`. The Relayer Role may be removed from an address by any address holding the `DEFAULT_ADMIN_ROLE` or the `FREEZER_ROLE`. This role applies to the monolithic ALM Controller implementation; the equivalent role for the Diamond PAU implementation is the Allocator Role, as specified in [A.6.1.1.2.2.6.1.2.2.1.1.3.3 - Allocator Role](6d6622aa-5d56-48e0-b8e9-1addd309fc9b).

###### A.6.1.1.2.2.6.1.2.2.1.1.1.3 - ALM Controller Role [Core]  <!-- UUID: 955c8db9-7bd7-4e49-b23c-7b482c84ca97 -->

The `ALM_CONTROLLER_ROLE` is the address of the role that can call the `call` functions on the `ALMProxy` contract and update `RateLimits` contract. It includes the `MainnetController` and `ForeignController` contracts. ALM Controller contracts are accessed and modified via the Relayer Role. This role applies to the monolithic ALM Controller implementation; the equivalent role for the Diamond PAU implementation is specified in [A.6.1.1.2.2.6.1.2.2.1.1.3.2 - Controller Role](1597253b-b936-46f6-98c7-d41d4306d2c5).

###### A.6.1.1.2.2.6.1.2.2.1.1.1.4 - Freezer Role [Core]  <!-- UUID: 37871a80-dc8f-4804-bce1-5f082e9bca9f -->

The `FREEZER_ROLE` is the address of the emergency role that can remove a compromised Relayer.

###### A.6.1.1.2.2.6.1.2.2.1.1.2 - Tokenized Treasury Role Hierarchy And Permissions [Core]  <!-- UUID: 92908b02-e1eb-4c14-b44e-92968cccd881 -->

The documents herein define the roles and permissions on Tokenized Treasury Instances of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.2.2.1.1.2.1 - Tokenized Treasury Owner Role [Core]  <!-- UUID: 41a7e6fb-59e1-40e8-a05a-68c1520fb361 -->

The `OWNER_ROLE` on a Tokenized Treasury Instance is authorized to set purchase and redemption fee rates within bounds established by the `MANAGER_ADMIN_ROLE`, and to grant or revoke any role in the contract. The `OWNER_ROLE` is held by an OpenZeppelin `TimelockController` operated by the credit token issuer. The Timelock address and the holders of its `PROPOSER_ROLE` are specified in each Instance Configuration Document. The holders of the Timelock's `EXECUTOR_ROLE` and `CANCELLER_ROLE` are specified in [A.6.1.1.2.2.6.1.2.2.1.1.2.7 - Tokenized Treasury Owner Timelock Executor Role](35e4cd97-0d88-4a47-8fbe-487c48ecc92e) and [A.6.1.1.2.2.6.1.2.2.1.1.2.8 - Tokenized Treasury Owner Timelock Canceller Role](0ff6a176-d3c5-45c6-a55a-5fec89d3c709).

###### A.6.1.1.2.2.6.1.2.2.1.1.2.2 - Tokenized Treasury Manager Admin Role [Core]  <!-- UUID: 4554fa6d-a03a-488d-a37e-a3be7b72323e -->

The `MANAGER_ADMIN_ROLE` on a Tokenized Treasury Instance is authorized to configure rate providers, bounds for maximum swap size, oracle staleness, and fees, the Pocket contract, authorized redeemer contracts, and the fee claimer. The `MANAGER_ADMIN_ROLE` manages role assignments for the `MANAGER_ROLE`, `PAUSER_ROLE`, `REDEEMER_CONTRACT_ROLE`, and `REDEEMER_ROLE`. The `MANAGER_ADMIN_ROLE` is held by the Grove [A.6.1.1.2.2.1.1.3.1.1.2 - SubProxy Account](d143241d-5819-432d-a6ba-892961502838) across all Tokenized Treasury Instances.

###### A.6.1.1.2.2.6.1.2.2.1.1.2.3 - Tokenized Treasury Manager Role [Core]  <!-- UUID: 191435aa-436b-4ef9-a95a-2357a314be01 -->

The `MANAGER_ROLE` on a Tokenized Treasury Instance is authorized to adjust the maximum swap size and oracle staleness threshold within bounds established by the `MANAGER_ADMIN_ROLE`. The `MANAGER_ROLE` is held by the [A.6.1.1.2.2.6.1.2.1.2.2.1 - Prime Primary Relayer Multisig](5e6f63a8-d0e5-441d-927b-13830f5f9b24) across all Tokenized Treasury Instances.

###### A.6.1.1.2.2.6.1.2.2.1.1.2.4 - Tokenized Treasury Pauser Role [Core]  <!-- UUID: abdc489a-6478-4e2a-9f22-423fd71d3700 -->

The `PAUSER_ROLE` on a Tokenized Treasury Instance is authorized to pause individual swap directions, credit token deposits and withdrawals, or all contract operations. Unpausing requires the `MANAGER_ADMIN_ROLE`. Additionally, the `PAUSER_ROLE` is authorized to revoke the `MANAGER_ROLE` and the `REDEEMER_ROLE` directly, bypassing the standard role-admin requirement. The `PAUSER_ROLE` is held by the [A.6.1.1.2.2.6.1.2.1.2.2.4 - Freezer Multisig](99bc2dd5-5573-4bb9-9210-5af299d058d9) across all Tokenized Treasury Instances.

###### A.6.1.1.2.2.6.1.2.2.1.1.2.5 - Tokenized Treasury Redeemer Role [Core]  <!-- UUID: fbeb1921-37eb-465b-97fa-004c8e0925b1 -->

The `REDEEMER_ROLE` on a Tokenized Treasury Instance is authorized to initiate and complete the two-step redemption of credit tokens back into collateral tokens through an authorized redeemer contract. The `REDEEMER_ROLE` is controlled by the credit token issuer; the holder address is specified in each Instance Configuration Document.

###### A.6.1.1.2.2.6.1.2.2.1.1.2.6 - Tokenized Treasury Redeemer Contract Role [Core]  <!-- UUID: 493bc01d-1c2e-4ef1-8605-1183c77a8cf2 -->

The `REDEEMER_CONTRACT_ROLE` on a Tokenized Treasury Instance is granted to authorized redeemer contracts that execute the two-step redemption of credit tokens on behalf of holders of the `REDEEMER_ROLE`. `REDEEMER_CONTRACT_ROLE` holders are added and removed via the `addTokenRedeemer` and `removeTokenRedeemer` functions, which are authorized for the `MANAGER_ADMIN_ROLE`.

###### A.6.1.1.2.2.6.1.2.2.1.1.2.7 - Tokenized Treasury Owner Timelock Executor Role [Core]  <!-- UUID: 35e4cd97-0d88-4a47-8fbe-487c48ecc92e -->

The `EXECUTOR_ROLE` on the OpenZeppelin `TimelockController` holding the `OWNER_ROLE` of a Tokenized Treasury Instance is authorized to execute queued operations once the Timelock delay period has elapsed. Across Tokenized Treasury Instances, this role is held by the Grove [A.6.1.1.2.2.1.1.3.1.1.2 - SubProxy Account](d143241d-5819-432d-a6ba-892961502838).

###### A.6.1.1.2.2.6.1.2.2.1.1.2.8 - Tokenized Treasury Owner Timelock Canceller Role [Core]  <!-- UUID: 0ff6a176-d3c5-45c6-a55a-5fec89d3c709 -->

The `CANCELLER_ROLE` on the OpenZeppelin `TimelockController` holding the `OWNER_ROLE` of a Tokenized Treasury Instance is authorized to cancel queued Timelock operations before execution. The `CANCELLER_ROLE` is held by the [A.6.1.1.2.2.6.1.2.1.2.2.4 - Freezer Multisig](99bc2dd5-5573-4bb9-9210-5af299d058d9) across all Tokenized Treasury Instances, and additionally by the credit token issuer's address that holds the Timelock's `PROPOSER_ROLE`. The issuer's address is specified in each Instance Configuration Document.

###### A.6.1.1.2.2.6.1.2.2.1.1.3 - Diamond PAU Role Hierarchy And Permissions [Core]  <!-- UUID: c4149166-7e65-48d3-81f9-177a4f3f6364 -->

The documents herein define the roles and permissions of the Diamond PAU Instance of the Allocation System Primitive. Roles are managed by the AccessControls contract.

###### A.6.1.1.2.2.6.1.2.2.1.1.3.1 - Default Admin Role [Core]  <!-- UUID: 987dc000-4453-4beb-93b3-aad8a4d819fc -->

The `DEFAULT_ADMIN_ROLE` is the administrative role of the AccessControls contract, authorized to grant and revoke all other roles of the Diamond PAU. The Default Admin Role is held by the Grove Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.1.3.2 - Controller Role [Core]  <!-- UUID: 1597253b-b936-46f6-98c7-d41d4306d2c5 -->

The `CONTROLLER` role is authorized to call the `call` functions on the ALM Proxy contract and to update the ALM Rate Limits contract. The Controller Role is held by the Controller contract, which dispatches operations to the relevant Facet contract on behalf of the Allocator Role.

###### A.6.1.1.2.2.6.1.2.2.1.1.3.3 - Allocator Role [Core]  <!-- UUID: 6d6622aa-5d56-48e0-b8e9-1addd309fc9b -->

The `ALLOCATOR_ROLE` is authorized to call functions on the Controller contract to perform operations on behalf of the ALM Proxy contract. The Allocator Role is held by the AdministeredAgent contract, as specified in [A.6.1.1.2.2.6.1.2.1.1.1.4.1.5 - AdministeredAgent Contract](d58e14aa-0901-4aa9-af44-6281161be162), which mediates access for the Grove Liquidity Layer relayer system. The same relayer multisigs used by the monolithic ALM Controller, whose addresses are specified in [A.6.1.1.2.2.6.1.2.1.1.1.2.1.4 - ALM Relayer Multisig Addresses](51b50a8f-eb29-4424-bb0a-8247d2acce7d), are registered as actors of the AdministeredAgent and submit operations through it. An actor may be removed from the AdministeredAgent by any address holding the Freezer Role, as specified in [A.6.1.1.2.2.6.1.2.2.1.1.3.4 - Freezer Role](d910ae36-1251-4385-b989-f303878ed094).

###### A.6.1.1.2.2.6.1.2.2.1.1.3.4 - Freezer Role [Core]  <!-- UUID: d910ae36-1251-4385-b989-f303878ed094 -->

The Freezer Role is authorized to remove a compromised or malicious relayer actor from the AdministeredAgent contract as a rapid-response measure, without recourse to the standard governance process. Removing an actor revokes its ability to submit operations through the Allocation System, while the Allocator Role itself remains held by the AdministeredAgent. The Freezer Role is held by the Freezer Multisig, as specified in [A.6.1.1.2.2.6.1.2.1.2.2.4 - Freezer Multisig](99bc2dd5-5573-4bb9-9210-5af299d058d9).

###### A.6.1.1.2.2.6.1.2.2.1.2 - Controller Functions [Core]  <!-- UUID: 4d77a9ba-d186-48e8-a70d-53aa66e01c65 -->

The documents herein specify the functions performed by the Controller contracts of the Grove Liquidity Layer, covering both the monolithic ALM Controller and the Diamond PAU.

###### A.6.1.1.2.2.6.1.2.2.1.2.1 - Monolithic Mainnet Controller Contract Functions [Core]  <!-- UUID: 1ee14921-5883-4533-aba0-b96d44e3cf6b -->

The documents herein define the functions controlled by the Controller contract for Grove Liquidity Layer operations on Ethereum Mainnet.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1 - Admin Functions [Core]  <!-- UUID: cdc104ee-6c78-404e-95bd-362dcec206bb -->

The documents herein define the operations performed by the `DEFAULT_ADMIN_ROLE` within the `MainnetController` contract.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.1 - Set The Mint Recipient [Core]  <!-- UUID: c4c09a75-ef25-4aa7-825a-73d386cbc87f -->

The documents herein define the process to set the `mintRecipient` for a specific `destinationDomain`. This is used in cross-chain transfers to specify the address that will receive minted tokens on the target chain.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.1.1 - Admin Role [Core]  <!-- UUID: 310f2d02-371c-4fa1-b0bf-1e07d80464ee -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMintRecipient`.

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.1.2 - Associate Mint Recipient With Domain [Core]  <!-- UUID: c639083a-417f-45c8-ba94-c0713d1539ac -->

The operator must associate the `mintRecipient` with the `destinationDomain` such that any tokens minted on this domain will go to this recipient.

`{
        mintRecipients[destinationDomain] = mintRecipient;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.1.3 - Emit Event To Logs [Core]  <!-- UUID: e3e6ca9d-7cd6-44f1-a688-80f1e744ed0f -->

The operator must emit the event to the blockchain logs.

`        emit MintRecipientSet(destinationDomain, mintRecipient);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.2 - Set The LayerZero Recipient [Core]  <!-- UUID: cd46a4fa-1281-4e3e-9ac5-0ca7f2160ec2 -->

The documents herein define the process to set the `layerZeroRecipient` for a specific `destinationEndpointId`. This is used in cross-chain transfers to specify the address that will receive bridged tokens on the target chain.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.1 - Admin Role [Core]  <!-- UUID: 3b4bb347-5f04-4fec-bb34-e0072a80c012 -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setLayerZeroRecipient`.

`function setLayerZeroRecipient(uint32 destinationEndpointId, bytes32 layerZeroRecipient)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.2 - Associate LayerZero Recipient With Endpoint [Core]  <!-- UUID: 9e079e2a-6b46-4261-b3ce-cc001d676011 -->

The operator must associate the `layerZeroRecipient` with the `destinationEndpointId` such that any tokens bridged to this endpoint will go to this recipient.

`{
        layerZeroRecipients[destinationEndpointId] = layerZeroRecipient;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.2.3 - Emit Event To Logs [Core]  <!-- UUID: 9817844a-0e56-48ba-844d-64d4e01096a4 -->

The operator must emit the event to the blockchain logs.

`        emit LayerZeroRecipientSet(destinationEndpointId, layerZeroRecipient);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.3 - Set The Max Slippage [Core]  <!-- UUID: 7aedf5dd-c454-4eb3-b97c-63d810f1c616 -->

The documents herein define the process to set the `maxSlippage` for a specific `pool`. This value bounds the acceptable slippage for operations that interact with the `pool`, and is stored in the `maxSlippages` mapping with `1e18` precision.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.1 - Admin Role [Core]  <!-- UUID: 7ae5334c-61e6-41b9-b6a3-7ac3e61cc6a5 -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMaxSlippage`.

`function setMaxSlippage(address pool, uint256 maxSlippage)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.2 - Validate Max Slippage Bound [Core]  <!-- UUID: a3ff9791-9ea0-49ed-a311-72a5868ea4a3 -->

The operator must ensure the provided `maxSlippage` does not exceed `1e18`, reverting with `MainnetController/max-slippage-out-of-bounds` otherwise. The `maxSlippage` value is expressed with `1e18` precision.

`{
        require(maxSlippage <= 1e18, "MainnetController/max-slippage-out-of-bounds");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.3 - Set Max Slippage For Pool [Core]  <!-- UUID: e55c742b-8aed-4afd-aab9-ae9dc0bdc007 -->

The operator must record the `maxSlippage` for the given `pool` in the `maxSlippages` mapping, which is stored with `1e18` precision.

`        maxSlippages[pool] = maxSlippage;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.3.4 - Emit Event To Logs [Core]  <!-- UUID: 9af74118-2d78-4092-b695-0d95ffcd5a54 -->

The operator must emit the event to the blockchain logs.

`        emit MaxSlippageSet(pool, maxSlippage);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.4 - Set The Uniswap V3 Pool Max Tick Delta [Core]  <!-- UUID: bf5c8eae-451a-4a1b-9b53-bd5deefd9c21 -->

The documents herein define the process to set the `swapMaxTickDelta` for a given Uniswap V3 `pool`. This bounds the maximum tick movement permitted when swapping through the pool, constraining the acceptable price impact of a swap.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.1 - Admin Role [Core]  <!-- UUID: 078273b1-aac9-410d-849b-2e1898b1f784 -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setUniswapV3PoolMaxTickDelta`.

`function setUniswapV3PoolMaxTickDelta(address pool, uint24 maxTickDelta) external {
        _checkRole(DEFAULT_ADMIN_ROLE);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.2 - Check Max Tick Delta Bounds [Core]  <!-- UUID: b83bc58c-f6b0-45a1-9ff8-4e705f8f5476 -->

The operator must ensure the `maxTickDelta` is greater than `0` and does not exceed `UniswapV3Lib.MAX_TICK_DELTA` (`887272`), otherwise the call reverts with `max-tick-delta-out-of-bounds`.

`        require(
            maxTickDelta > 0 &&
            maxTickDelta <= UniswapV3Lib.MAX_TICK_DELTA,
            "MainnetController/max-tick-delta-out-of-bounds"
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.3 - Set The Pool Max Tick Delta [Core]  <!-- UUID: 6646540e-4b82-4cc0-bcbc-b733648be9ea -->

The operator must set the `swapMaxTickDelta` on the `uniswapV3PoolParams` for the given `pool` to the supplied `maxTickDelta`.

`        UniswapV3Lib.UniswapV3PoolParams storage params = uniswapV3PoolParams[pool];
        params.swapMaxTickDelta = maxTickDelta;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.4.4 - Emit Event To Logs [Core]  <!-- UUID: 4b5fc77a-4c21-457d-a2f2-5a86c7800148 -->

The operator must emit the event to the blockchain logs.

`        emit UniswapV3PoolMaxTickDeltaSet(pool, maxTickDelta);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.5 - Set The Uniswap V3 Add Liquidity Lower Tick Bound [Core]  <!-- UUID: 2f4ebdcc-b203-410d-aaab-19b395c2368c -->

The documents herein define the process to set the lower `addLiquidityTickBounds` bound for a specific Uniswap V3 `pool`. This lower tick bound constrains the lower end of the price range within which the Grove Liquidity Layer may add liquidity to the pool.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.1 - Admin Role [Core]  <!-- UUID: 8dc5ac2f-1fda-476f-80bb-b6c05e924af3 -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setUniswapV3AddLiquidityLowerTickBound`.

`function setUniswapV3AddLiquidityLowerTickBound(address pool, int24 lowerTickBound)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.2 - Validate The Lower Tick Bound [Core]  <!-- UUID: 020bdec4-2ffb-4ad7-aa21-38d290405cfa -->

The operator must retrieve the stored `UniswapV3PoolParams` for the `pool` and ensure the supplied `lowerTickBound` is greater than or equal to `MIN_TICK` (-887272) and strictly less than the pool's current upper `addLiquidityTickBounds`. Otherwise the call reverts with `MainnetController/lower-tick-out-of-bounds`.

`{
        UniswapV3Lib.UniswapV3PoolParams storage params = uniswapV3PoolParams[pool];
        require(lowerTickBound >= MIN_TICK && lowerTickBound < params.addLiquidityTickBounds.upper, "MainnetController/lower-tick-out-of-bounds");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.3 - Set The Lower Tick Bound [Core]  <!-- UUID: 153007a4-f8ac-460b-984e-bc736def634c -->

The operator must set the pool's lower `addLiquidityTickBounds` to the supplied `lowerTickBound`, which constrains the lower end of the price range used when adding liquidity to the `pool`.

`
        params.addLiquidityTickBounds.lower = lowerTickBound;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.5.4 - Emit Event To Logs [Core]  <!-- UUID: 1484df4a-395b-4e10-a521-f8fcf1e755eb -->

The operator must emit the event to the blockchain logs.

`        emit UniswapV3PoolLowerTickUpdated(pool, lowerTickBound);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.6 - Set The Uniswap V3 Add Liquidity Upper Tick Bound [Core]  <!-- UUID: dc3dd2d9-4b0a-4958-b9b6-6b2b9e91525b -->

The documents herein define the process to set the `upper` bound of the `addLiquidityTickBounds` for a given Uniswap V3 `pool`. This bound constrains the upper tick within which the Grove Liquidity Layer is permitted to add liquidity to the `pool`.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.1 - Admin Role [Core]  <!-- UUID: b4560318-fad0-43cf-a218-7c777d3b924f -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setUniswapV3AddLiquidityUpperTickBound`.

`function setUniswapV3AddLiquidityUpperTickBound(address pool, int24 upperTickBound)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.2 - Validate The Upper Tick Bound [Core]  <!-- UUID: fac137fb-ba7f-474b-8406-77be9e9a3a25 -->

The operator must load the `uniswapV3PoolParams` for the `pool` and ensure the provided `upperTickBound` is greater than the pool's current `addLiquidityTickBounds.lower` and is less than or equal to the `MAX_TICK` of `887272`. Otherwise, the request reverts with `MainnetController/upper-tick-out-of-bounds`.

`{
        UniswapV3Lib.UniswapV3PoolParams storage params = uniswapV3PoolParams[pool];
        require(upperTickBound > params.addLiquidityTickBounds.lower && upperTickBound <= MAX_TICK, "MainnetController/upper-tick-out-of-bounds");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.3 - Set The Upper Tick Bound [Core]  <!-- UUID: 2d139388-9697-4ae2-865d-19793b9e9cff -->

The operator must set the `upper` bound of the pool's `addLiquidityTickBounds` to the provided `upperTickBound`.

`        params.addLiquidityTickBounds.upper = upperTickBound;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.6.4 - Emit Event To Logs [Core]  <!-- UUID: 8445c9bd-2bd6-48dc-a801-dd6aa99d8714 -->

The operator must emit the event to the blockchain logs.

`        emit UniswapV3PoolUpperTickUpdated(pool, upperTickBound);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.7 - Set The Uniswap V3 TWAP Seconds Ago [Core]  <!-- UUID: cfdaafcb-d91d-4c6e-8af5-9d21fa6f4033 -->

The documents herein define the process to set the `twapSecondsAgo` for a Uniswap V3 `pool`. This defines the length of the time-weighted average price window used when the contract consults the pool for pricing.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.1 - Admin Role [Core]  <!-- UUID: 5e388832-64cb-424b-a36a-ef1dd3eeb22a -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setUniswapV3TwapSecondsAgo`.

`function setUniswapV3TwapSecondsAgo(address pool, uint32 twapSecondsAgo)
        external
        onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.2 - Validate The TWAP Seconds Ago [Core]  <!-- UUID: 33cee360-03fb-4c0a-a412-0d037a14640f -->

The operator must load the `UniswapV3PoolParams` for the `pool` and ensure the supplied `twapSecondsAgo` is less than `uint32(type(int32).max)`, which caps the value at approximately 68 years; this bound is required due to the casting in `UniswapV3OracleLibrary.consult`. Otherwise the call reverts with `MainnetController/twap-seconds-ago-out-of-bounds`.

`{
        UniswapV3Lib.UniswapV3PoolParams storage params = uniswapV3PoolParams[pool];
        // Required due to casting in UniswapV3OracleLibrary.consult
        // Limits twapSecondsAgo to approximately 68 years
        require(twapSecondsAgo < uint32(type(int32).max), "MainnetController/twap-seconds-ago-out-of-bounds");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.3 - Set The Pool TWAP Seconds Ago [Core]  <!-- UUID: 40842834-d8eb-455f-b69f-f57d5f1ae330 -->

The operator must set the `twapSecondsAgo` on the pool's `UniswapV3PoolParams`, which defines the length of the time-weighted average price window used when the contract consults the `pool`.

`        params.twapSecondsAgo = twapSecondsAgo;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.7.4 - Emit Event To Logs [Core]  <!-- UUID: 02c3f20c-c95e-4f3c-8d69-a29d289a3557 -->

The operator must emit the event to the blockchain logs.

`        emit UniswapV3PoolTwapSecondsAgoUpdated(pool, twapSecondsAgo);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.8 - Set The Centrifuge Recipient [Core]  <!-- UUID: 869c8941-5660-4d6f-b5ab-c464e444b5b6 -->

The documents herein define the process to set the recipient in the `centrifugeRecipients` mapping for a specific `centrifugeId`. This is used in cross-chain transfers to specify the address that will receive tokens on the target Centrifuge chain.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.1 - Admin Role [Core]  <!-- UUID: 60246e35-6a75-4640-8507-bae8aa5f813f -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setCentrifugeRecipient`.

`function setCentrifugeRecipient(uint16 centrifugeId, bytes32 recipient) external {
        _checkRole(DEFAULT_ADMIN_ROLE);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.2 - Associate Recipient With Centrifuge ID [Core]  <!-- UUID: 42d05753-9759-4054-93cb-27c2c7bd3245 -->

The operator must associate the `recipient` with the `centrifugeId` such that any tokens transferred to this Centrifuge chain will go to this recipient.

`        centrifugeRecipients[centrifugeId] = recipient;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.8.3 - Emit Event To Logs [Core]  <!-- UUID: 119b2a51-d64c-4d9d-9e84-329f5f6a16f9 -->

The operator must emit the event to the blockchain logs.

`        emit CentrifugeRecipientSet(centrifugeId, recipient);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.9 - Set The Max Exchange Rate [Core]  <!-- UUID: 662ec211-4b25-43db-aca4-48acb08090ec -->

The documents herein define the process to set the maximum expected exchange rate for a specific `token`. This value is stored in the `maxExchangeRates` mapping with `1e36` precision and caps the exchange rate accepted when depositing into the `token` through `depositERC4626`, reverting with `MainnetController/exchange-rate-too-high` when the realized rate exceeds it.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.1 - Admin Role [Core]  <!-- UUID: 4e999d40-1303-4e5a-98b4-45eb808c62e9 -->

The operator must ensure they are working as an Admin. Only the `DEFAULT_ADMIN_ROLE` is allowed to `setMaxExchangeRate`.

`function setMaxExchangeRate(address token, uint256 shares, uint256 maxExpectedAssets) external {
        _checkRole(DEFAULT_ADMIN_ROLE);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.2 - Validate Token Address [Core]  <!-- UUID: 3129dc03-3fff-4f4d-86df-639689b2498e -->

The operator must ensure the `token` is not the zero address, reverting with `MainnetController/token-zero-address` otherwise.

`        require(token != address(0), "MainnetController/token-zero-address");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.1.9.3 - Set And Emit Max Exchange Rate [Core]  <!-- UUID: a6b7dd4b-6935-4d69-8af7-34d34734b455 -->

The operator must set the maximum exchange rate for the `token` to the value computed by `_getExchangeRate` from the provided `shares` and `maxExpectedAssets`, which returns `1e36 * assets / shares` at `1e36` precision and reverts with `MainnetController/zero-shares` when `shares` is zero while assets are non-zero. This value is written to the `maxExchangeRates` mapping for the `token` and emitted through the `MaxExchangeRateSet` event to the blockchain logs.

`        emit MaxExchangeRateSet(
            token,
            maxExchangeRates[token] = _getExchangeRate(shares, maxExpectedAssets)
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2 - Relayer Functions [Core]  <!-- UUID: 609939e3-81c4-4096-9f74-e4a410982b73 -->

The documents herein define the operations performed by the `RELAYER_ROLE` within the `MainnetController` contract.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1 - Core Vault Functions [Core]  <!-- UUID: a5229ab8-f310-4a83-97c7-555782b1f61b -->

The documents herein define the operations that are performed to maintain the desired level of liquidity and debt balance of the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1 - Mint USDS [Core]  <!-- UUID: 36126625-ab5d-4071-b805-5bd3ac4b246b -->

The documents herein define a series of operations for an operator to `mintUSDS`, drawing USDS from the Sky Allocation Vault into the buffer and transferring it to the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.1 - Relayer Role [Core]  <!-- UUID: 044fed6d-5a18-48d1-89df-777f86e4652a -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `mintUSDS`, enforced by the `onlyRole(RELAYER)` gate on the function; there is no other precondition or active-state check.

`function mintUSDS(uint256 usdsAmount)
        external
        onlyRole(RELAYER)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.2 - Check RateLimits [Core]  <!-- UUID: e3f04b74-9b6d-45e9-9363-e76bda9ba6dc -->

The operator's call decreases the `LIMIT_USDS_MINT` rate limit by `usdsAmount`, consuming available mint capacity. Internally `_rateLimited` calls `rateLimits.triggerRateLimitDecrease(LIMIT_USDS_MINT, usdsAmount)`, which reverts if `usdsAmount` exceeds the currently available limit.

`_rateLimited(LIMIT_USDS_MINT, usdsAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.3 - Draw USDS To Buffer [Core]  <!-- UUID: 8230c4c2-71d4-4d1b-800b-0684e2de136e -->

The operator draws USDS from the Sky Allocation Vault into the buffer by having the `proxy` call `vault.draw` for `usdsAmount`.

`// Mint USDS into the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.draw, (usdsAmount))
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.1.4 - Transfer USDS To ALM Proxy [Core]  <!-- UUID: b51fa176-1c34-4ad3-9154-46a6d1b6f60d -->

The operator moves the drawn USDS from the buffer to the `proxy` by having the `proxy` call `usds.transferFrom`, pulling `usdsAmount` from the buffer to the ALM Proxy.

`// Transfer USDS from the buffer to the proxy
        proxy.doCall(
            address(usds),
            abi.encodeCall(usds.transferFrom, (buffer, address(proxy), usdsAmount))
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS [Core]  <!-- UUID: 25706c25-2b74-486e-8234-c45f6630f379 -->

The documents herein define a series of operations for an operator to `burnUSDS`, returning USDS from the Grove ALM Proxy to the buffer and burning it to repay Grove's USDS debt in the Sky Allocation Vault.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.1 - Relayer Role [Core]  <!-- UUID: 23d1b504-bd08-4759-b2d6-9067fdbcaedd -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `burnUSDS`, enforced by the `onlyRole(RELAYER)` gate on the function; there is no other precondition or active-state check.

`function burnUSDS(uint256 usdsAmount)
        external
        onlyRole(RELAYER)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.2 - Check RateLimits [Core]  <!-- UUID: 6449fd5a-ec8b-4d71-aa03-7cac23780c2c -->

Burning USDS restores previously consumed mint capacity. The operator's call increases (refunds) the `LIMIT_USDS_MINT` rate limit by `usdsAmount`, reversing the decrease applied when that USDS was minted. Internally `_cancelRateLimit` calls `rateLimits.triggerRateLimitIncrease(LIMIT_USDS_MINT, usdsAmount)`; it does not check or consume a separate burn allowance.

`_cancelRateLimit(LIMIT_USDS_MINT, usdsAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.3 - Transfer USDS To Buffer [Core]  <!-- UUID: 2e633940-12fd-4a3b-9b02-6fae976fd7e5 -->

The operator returns `usdsAmount` of USDS from the `proxy` to the buffer via `ERC20Lib.transfer`, which has the `proxy` call `transfer` on the USDS contract and requires the transfer to succeed.

`// Transfer USDS from the proxy to the buffer
        ERC20Lib.transfer(proxy, address(usds), buffer, usdsAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2.4 - Burn USDS From Buffer [Core]  <!-- UUID: df488122-2d82-4a54-8285-b24b86eb2e49 -->

The operator burns the returned USDS from the buffer by having the `proxy` call `vault.wipe` for `usdsAmount`, repaying Grove's USDS debt in the Sky Allocation Vault.

`// Burn USDS from the buffer
        proxy.doCall(
            address(vault),
            abi.encodeCall(vault.wipe, (usdsAmount))
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2 - ERC-4626 Functions [Core]  <!-- UUID: 2d92707b-e08a-49a5-8b31-a22cf6f458af -->

The documents herein define the Grove Liquidity Layer operational procedures for interacting with ERC-4626 tokenized vaults, including depositing an asset for shares, withdrawing an asset by burning shares, and redeeming shares for an asset. ERC-4626 is a standard interface for vaults that represent shares of an underlying ERC-20 asset, and each vault is whitelisted through its configured `RateLimits`.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1 - Deposit To ERC-4626 Vault [Core]  <!-- UUID: 4876005c-31a8-4be8-8133-e239bd0ac53b -->

The documents herein define a series of operations for an operator to `depositERC4626`, depositing an underlying asset from the Grove ALM Proxy into an ERC-4626 vault in exchange for vault shares.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.1 - Relayer Role [Core]  <!-- UUID: b2767d8e-f753-4dab-abd7-798dcd7b2311 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `depositERC4626`.

`function depositERC4626(address token, uint256 amount)
        external
        onlyRole(RELAYER)
        returns (uint256 shares)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.2 - Check RateLimits [Core]  <!-- UUID: 36c94503-8627-4eab-baba-e257c8796514 -->

The operator must ensure that `RateLimits` allow for depositing the required `amount` of the asset into the ERC-4626 vault. The rate limit is keyed to the specific `token` through `makeAssetKey`, and its available amount is decreased by the deposited `amount`. This rate limit also serves as the whitelist, since only vaults with a configured rate limit can be used.

`        _rateLimitedAsset(LIMIT_4626_DEPOSIT, token, amount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.3 - Get Vault Asset [Core]  <!-- UUID: e4132ae2-cdaa-4221-a69c-0b332e71337b -->

The operator must resolve the underlying `asset` of the ERC-4626 vault by calling `asset` on the `token`. This is the ERC-20 asset that will be deposited from the Grove ALM Proxy.

`        IERC20 asset = IERC20(IERC4626(token).asset());`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.4 - Approve Vault Spend [Core]  <!-- UUID: 02f75eaa-e4cf-462f-ae8d-6222c78bb066 -->

The operator must approve the `token` to spend `amount` of the underlying `asset` on behalf of the Grove ALM Proxy. The approval is executed through `proxy.doCall` and reverts unless the token's `approve` returns empty or `true`. This assumes the `proxy` already holds sufficient underlying asset.

`        ERC20Lib.approve(proxy, address(asset), token, amount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.5 - Deposit Asset [Core]  <!-- UUID: 58b13044-b093-4cd4-a006-0557360ece3e -->

The operator must call `deposit` on the `token` through the `proxy`, depositing `amount` of the underlying asset and directing the minted vault shares to the `proxy`. The number of `shares` received is decoded from the return data.

`        shares = abi.decode(
            proxy.doCall(
                token,
                abi.encodeCall(IERC4626(token).deposit, (amount, address(proxy)))
            ),
            (uint256)
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1.6 - Enforce Exchange Rate [Core]  <!-- UUID: 381cbdf4-6778-421c-8565-b8de2e8672ba -->

The operator must ensure the realized exchange rate of the deposit does not exceed the configured `maxExchangeRates` for the `token`, otherwise the call reverts with `MainnetController/exchange-rate-too-high`. The exchange rate is computed by `_getExchangeRate(shares, amount)` as `EXCHANGE_RATE_PRECISION * amount / shares` at `1e36` precision, guarding against depositing into a vault whose shares are priced above the acceptable threshold.

`        require(
            _getExchangeRate(shares, amount) <= maxExchangeRates[token],
            "MainnetController/exchange-rate-too-high"
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2 - Withdraw From ERC-4626 Vault [Core]  <!-- UUID: 7b560160-e427-45a2-a3ac-3c23cf6fe943 -->

The documents herein define a series of operations for an operator to `withdrawERC4626`, withdrawing a specified `amount` of the underlying asset from an ERC-4626 vault to the Grove ALM Proxy by burning the corresponding vault shares.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.1 - Relayer Role [Core]  <!-- UUID: 75c217fb-18f8-458b-a933-5c57b4abeeaa -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `withdrawERC4626`.

`function withdrawERC4626(address token, uint256 amount)
        external
        onlyRole(RELAYER)
        returns (uint256 shares)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.2 - Check RateLimits [Core]  <!-- UUID: 6c441069-db6a-4097-a322-440adf356191 -->

The operator must ensure that `RateLimits` allow for withdrawing the required `amount` of the asset from the ERC-4626 vault. The rate limit is keyed to the specific `token` through `makeAssetKey`, and its available amount is decreased by the withdrawn `amount`. This rate limit also serves as the whitelist, since only vaults with a configured rate limit can be used.

`        _rateLimitedAsset(LIMIT_4626_WITHDRAW, token, amount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2.3 - Withdraw Asset [Core]  <!-- UUID: acda4904-4a23-47f3-84bb-211d53cc4463 -->

The operator must call `withdraw` on the `token` through the `proxy`, withdrawing `amount` of the underlying asset with the `proxy` as both the `receiver` of the asset and the `owner` of the shares being burned. The number of `shares` burned is decoded from the return data. This assumes the `proxy` holds adequate vault shares.

`        shares = abi.decode(
            proxy.doCall(
                token,
                abi.encodeCall(IERC4626(token).withdraw, (amount, address(proxy), address(proxy)))
            ),
            (uint256)
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3 - Redeem From ERC-4626 Vault [Core]  <!-- UUID: 7e90e505-42b9-474d-9cc5-9b4da6af7375 -->

The documents herein define a series of operations for an operator to `redeemERC4626`, burning a specified number of `shares` in an ERC-4626 vault to receive the corresponding underlying assets into the Grove ALM Proxy. The withdraw rate limit is decreased after redemption, based on the actual assets received.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.1 - Relayer Role [Core]  <!-- UUID: 73d565c3-561c-4b54-a491-0fa2257bf9dd -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `redeemERC4626`. Unlike deposits and withdrawals, this operation applies its rate limit after redemption rather than before, since the resulting assets are not known until the shares are redeemed.

`function redeemERC4626(address token, uint256 shares)
        external
        onlyRole(RELAYER)
        returns (uint256 assets)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.2 - Redeem Shares [Core]  <!-- UUID: 0d0eae8c-8b1f-4493-a574-53ad8d96322b -->

The operator must call `redeem` on the `token` through the `proxy`, redeeming `shares` with the `proxy` as both the `receiver` of the underlying asset and the `owner` of the shares being redeemed. The amount of underlying `assets` received is decoded from the return data. This assumes the `proxy` holds adequate vault shares.

`        assets = abi.decode(
            proxy.doCall(
                token,
                abi.encodeCall(IERC4626(token).redeem, (shares, address(proxy), address(proxy)))
            ),
            (uint256)
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3.3 - Decrease Withdraw Rate Limit [Core]  <!-- UUID: 6370eada-cbd1-4bc1-8ba4-d985b05b1a21 -->

The operator must decrease the `LIMIT_4626_WITHDRAW` rate limit for the `token` by the actual `assets` received, after the redemption is executed. The rate limit is keyed to the `token` through `makeAssetKey`. Because redemption is limited by the same rate limit as withdrawal, the redeemed value counts against the shared withdraw allowance.

`        rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(LIMIT_4626_WITHDRAW, token),
            assets
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3 - PSM Functions [Core]  <!-- UUID: 2df8d8c7-17ee-4427-a75b-fc3ce08913d4 -->

The documents herein define the swap operations performed by the Grove Liquidity Layer in the PSM.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1 - Swap USDS To USDC [Core]  <!-- UUID: e159020b-6b20-4894-b001-ce13f389734a -->

The documents herein define a series of operations for an operator to `swapUSDSToUSDC`, converting USDS into USDC through the DAI-USDS migrator and the PSM.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.1 - Relayer Role [Core]  <!-- UUID: bd3ff49e-77af-4757-984d-f8e91346e702 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `swapUSDSToUSDC`, which the controller enforces with `onlyRole(RELAYER)` before delegating the swap to `PSMLib.swapUSDSToUSDC`.

`function swapUSDSToUSDC(uint256 usdcAmount)
        external
        onlyRole(RELAYER)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.2 - Check RateLimits [Core]  <!-- UUID: 532d5769-4224-48c0-9282-9c19e9fe6455 -->

The operator must ensure that `RateLimits` allows swapping the requested USDC amount. `PSMLib.swapUSDSToUSDC` consumes the `LIMIT_USDS_TO_USDC` rate limit by triggering a decrease of `usdcAmount`, which reverts if the remaining limit is insufficient.

`_rateLimited(params.rateLimits, params.rateLimitId, params.usdcAmount);`

The helper decreases the limit keyed by `LIMIT_USDS_TO_USDC`.

`function _rateLimited(IRateLimits rateLimits,bytes32 key, uint256 amount) internal {
        rateLimits.triggerRateLimitDecrease(key, amount);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.3 - Convert To 18 Token Format [Core]  <!-- UUID: aa417e52-f42f-4653-a820-e0cdafac9aea -->

The operator must convert the 6-decimal `usdcAmount` into the 18-decimal `usdsAmount` using `psmTo18ConversionFactor`, since USDS and DAI are denominated in 18 decimals.

`uint256 usdsAmount = params.usdcAmount * params.psmTo18ConversionFactor;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.4 - Approve Migrator Spend [Core]  <!-- UUID: c4b00dec-4cc9-49e8-97d1-a5c64560c8ce -->

The operator must approve the `daiUsds` migrator to spend `usdsAmount` of USDS on behalf of the `proxy`. `daiUsds` is the contract that facilitates a 1:1 swap between USDS and DAI. The operation assumes the `proxy` holds enough USDS.

`ERC20Lib.approve(params.proxy, address(params.usds), address(params.daiUsds), usdsAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.5 - Swap USDS To DAI [Core]  <!-- UUID: 348d05d6-74cb-484e-85dc-68bbce3e97df -->

The operator must swap USDS to DAI. USDS is converted to DAI at a 1:1 ratio through the `daiUsds` migrator and returned to the `proxy`.

`params.proxy.doCall(
            address(params.daiUsds),
            abi.encodeCall(params.daiUsds.usdsToDai, (address(params.proxy), usdsAmount))
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.6 - Approve PSM Spend [Core]  <!-- UUID: 97c2db26-16e7-4aee-a257-86bef4189fa7 -->

The operator must approve the PSM to spend the newly acquired DAI on behalf of the `proxy`. The approved amount equals `usdsAmount` because the conversion from USDS to DAI was 1:1.

`ERC20Lib.approve(params.proxy, address(params.dai), address(params.psm), usdsAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.1.7 - Swap DAI To USDC [Core]  <!-- UUID: 0e02d0f4-a9b1-4f2f-8016-274c26db9fa2 -->

The operator must swap DAI to USDC. DAI is exchanged for USDC through the PSM at a 1:1 ratio with no fee, using `buyGemNoFee`, and the USDC is returned to the `proxy`.

`params.proxy.doCall(
            address(params.psm),
            abi.encodeCall(params.psm.buyGemNoFee, (address(params.proxy), params.usdcAmount))
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2 - Swap USDC To USDS [Core]  <!-- UUID: 1ec9a718-44f4-4ce9-97b3-bebeb207b280 -->

The documents herein define a series of operations for an operator to `swapUSDCToUSDS`, converting USDC into USDS through the PSM and the DAI-USDS migrator.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.1 - Relayer Role [Core]  <!-- UUID: a3637c8d-ce3e-4cc8-ae15-2a8623a841db -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `swapUSDCToUSDS`, which the controller enforces with `onlyRole(RELAYER)` before delegating the swap to `PSMLib.swapUSDCToUSDS`.

`function swapUSDCToUSDS(uint256 usdcAmount)
        external
        onlyRole(RELAYER)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.2 - Refund RateLimit [Core]  <!-- UUID: 462537ca-626a-4516-afd6-a3a344d1e241 -->

The operator does not consume a rate limit in this direction. Instead, `PSMLib.swapUSDCToUSDS` cancels usage of the opposite direction's limit: it increases the `LIMIT_USDS_TO_USDC` rate limit by `usdcAmount`, refunding capacity that a prior USDS-to-USDC swap had consumed.

`_cancelRateLimit(params.rateLimits, params.rateLimitId, params.usdcAmount);`

The helper increases the limit keyed by `LIMIT_USDS_TO_USDC`.

`function _cancelRateLimit(IRateLimits rateLimits, bytes32 key, uint256 amount) internal {
        rateLimits.triggerRateLimitIncrease(key, amount);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.3 - Approve PSM Spend [Core]  <!-- UUID: f5d1b5d7-3968-4b49-99ff-21d7e3a5d2b7 -->

The operator must approve the PSM to spend `usdcAmount` of USDC on behalf of the `proxy`. The operation assumes the `proxy` holds enough USDC.

`ERC20Lib.approve(params.proxy, address(params.usdc), address(params.psm), params.usdcAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.4 - Swap USDC To DAI [Core]  <!-- UUID: 2c2b3e9a-5135-4379-bd4f-9f52884bd8da -->

The operator must swap USDC to DAI through the PSM using `sellGemNoFee` (1:1, no fee), routed through the `_swapUSDCToDAI` helper. The PSM can only supply as much DAI as it currently holds, so the operation first computes the maximum USDC swappable in one call as the PSM's DAI balance divided by `psmTo18ConversionFactor`. If `usdcAmount` fits within that limit, a single swap is performed. Otherwise the operation repeatedly calls `psm.fill()` to top up the PSM's DAI, recomputes the limit, and swaps in chunks until the full `usdcAmount` is exchanged. If the PSM cannot be filled enough to cover the full amount, `psm.fill()` reverts with `DssLitePsm/nothing-to-fill`, so the operation only succeeds when the entire `usdcAmount` can be swapped.

`uint256 limit = params.dai.balanceOf(address(params.psm)) / params.psmTo18ConversionFactor;

        if (params.usdcAmount <= limit) {
            _swapUSDCToDAI(params.proxy, params.psm, params.usdcAmount);
        } else {
            uint256 remainingUsdcToSwap = params.usdcAmount;

            while (remainingUsdcToSwap > 0) {
                params.psm.fill();

                limit = params.dai.balanceOf(address(params.psm)) / params.psmTo18ConversionFactor;

                uint256 swapAmount = remainingUsdcToSwap < limit ? remainingUsdcToSwap : limit;

                _swapUSDCToDAI(params.proxy, params.psm, swapAmount);

                remainingUsdcToSwap -= swapAmount;
            }
        }`

Each chunk is swapped through the `_swapUSDCToDAI` helper.

`function _swapUSDCToDAI(IALMProxy proxy, IPSMLike psm, uint256 usdcAmount) internal {
        proxy.doCall(
            address(psm),
            abi.encodeCall(psm.sellGemNoFee, (address(proxy), usdcAmount))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.5 - Convert To 18 Token Format [Core]  <!-- UUID: 0b3c6086-9e48-4587-a182-59ddf73000e2 -->

The operator must convert the 6-decimal `usdcAmount` into the 18-decimal `daiAmount` using `psmTo18ConversionFactor`, since DAI and USDS are denominated in 18 decimals.

`uint256 daiAmount = params.usdcAmount * params.psmTo18ConversionFactor;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.6 - Approve Migrator Spend [Core]  <!-- UUID: f060c012-dad4-4509-8ed8-1d68a88b7ca7 -->

The operator must approve the `daiUsds` migrator to spend `daiAmount` of DAI on behalf of the `proxy`. `daiUsds` is the contract that facilitates a 1:1 swap between DAI and USDS. The operation assumes the `proxy` holds enough DAI.

`ERC20Lib.approve(params.proxy, address(params.dai), address(params.daiUsds), daiAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2.7 - Swap DAI To USDS [Core]  <!-- UUID: f64c4f1d-f7e3-4673-a43a-6891892a8d0d -->

The operator must swap DAI to USDS. DAI is converted to USDS at a 1:1 ratio through the `daiUsds` migrator and returned to the `proxy`.

`params.proxy.doCall(
            address(params.daiUsds),
            abi.encodeCall(params.daiUsds.daiToUsds, (address(params.proxy), daiAmount))
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.4 - ERC-20 Functions [Core]  <!-- UUID: ad4e80d9-abac-4cb3-bdf7-e97dc7b1c8e2 -->

The documents herein define the operations performed by the Grove Liquidity Layer to transfer ERC-20 assets from the Grove ALM Proxy to an approved destination.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1 - Transfer Asset [Core]  <!-- UUID: daa8abb8-db47-4dec-845f-fefbd6b8835a -->

The documents herein define the steps for an operator to `transfer` an ERC-20 `asset` from the Grove ALM Proxy to a `destination`.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.1 - Relayer Role [Core]  <!-- UUID: 2ff99ee2-a0ce-4280-a9e3-5aa0042e5cd5 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferAsset`.

`function transferAsset(address asset, address destination, uint256 amount) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.2 - Check RateLimits [Core]  <!-- UUID: 2fbc62d7-432c-4913-bee2-82764adba306 -->

The operator must ensure the `RateLimits` allow for transferring the required `amount` of the `asset` to the `destination`. The rate limit is keyed on the `asset` and `destination` pair through `makeAssetDestinationKey`.

`        _rateLimited(
            RateLimitHelpers.makeAssetDestinationKey(LIMIT_ASSET_TRANSFER, asset, destination),
            amount
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1.3 - Transfer Asset To Destination [Core]  <!-- UUID: 1bac7288-5cd8-4632-9ff1-ef98977f57d8 -->

The operator must call the `MainnetController` contract to `transfer` the `amount` of the `asset` from the Grove ALM Proxy to the `destination`. The transfer is executed through `proxy.doCall` and reverts unless the token's `transfer` returns empty or `true`.

`        ERC20Lib.transfer(proxy, asset, destination, amount);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5 - ERC-7540 Functions [Core]  <!-- UUID: 78f3cc3d-4ab4-4a30-9d21-76f1be2c72af -->

The documents herein define the Grove Liquidity Layer operational procedures for interacting with ERC-7540 asynchronous tokenized vaults. ERC-7540 extends the ERC4626 standard to support asynchronous deposit and redemption flows, where a request is submitted in one transaction and the resulting shares or assets are claimed in a later transaction once the request has been fulfilled.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1 - Request Deposit To ERC-7540 Vault [Core]  <!-- UUID: f305d6fb-d948-4890-ad9f-d5ad6197674d -->

The documents herein define a series of operations for an operator to `requestDepositERC7540`, submitting an asynchronous deposit request of an asset into an ERC-7540 vault on behalf of the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.1 - Relayer Role [Core]  <!-- UUID: b5bbbdfc-362f-4e71-a09d-2b52e200afb7 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `requestDepositERC7540`.

`function requestDepositERC7540(address token, uint256 amount) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.2 - Check RateLimits [Core]  <!-- UUID: 94dc3a5c-569d-4759-99d7-d5062f558937 -->

The operator must ensure that `RateLimits` allows for depositing the required `amount` of the asset into the ERC-7540 vault. The rate limit is keyed to the specific `token` and its available amount is decreased by the deposited `amount`. This rate limit also serves as the whitelist, since only vaults with a configured rate limit can be used.

`        _rateLimitedAsset(LIMIT_7540_DEPOSIT, token, amount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.3 - Get Vault Asset [Core]  <!-- UUID: b60a2f0c-397f-4814-bf94-a3b3e671507b -->

The operator must retrieve the underlying `asset` of the ERC-7540 vault by calling `asset` on the `token`. This is the ERC20 asset that will be deposited into the vault.

`        // Note that whitelist is done by rate limits
        IERC20 asset = IERC20(IERC7540(token).asset());`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.4 - Approve Contract Spend [Core]  <!-- UUID: 79029ed0-7c9d-443e-b928-b528d0a66d00 -->

The operator must approve the ERC-7540 vault (`token`) to spend the `amount` of the underlying `asset` on behalf of the `proxy`. This assumes the `proxy` holds enough of the asset.

`        // Approve asset to vault from the proxy (assumes the proxy has enough of the asset).
        ERC20Lib.approve(proxy, address(asset), token, amount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1.5 - Submit Deposit Request [Core]  <!-- UUID: 74415da6-e8d4-4da7-887d-ce27e5ecc307 -->

The operator must submit the deposit request by calling `requestDeposit` on the ERC-7540 vault, transferring the `amount` of the asset from the `proxy` into the vault. The `proxy` is set as both the controller and owner of the request, so the resulting shares can later be claimed to the `proxy`.

`        // Submit deposit request by transferring assets
        proxy.doCall(
            token,
            abi.encodeCall(IERC7540(token).requestDeposit, (amount, address(proxy), address(proxy)))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2 - Claim Deposit From ERC-7540 Vault [Core]  <!-- UUID: 1ea24541-a1ad-4b0f-bcee-2fc369d5b17b -->

The documents herein define a series of operations for an operator to `claimDepositERC7540`, claiming the shares of a previously fulfilled asynchronous deposit request from an ERC-7540 vault to the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.1 - Relayer Role [Core]  <!-- UUID: 61690505-13a7-4b3d-ad1d-a27802e0c69a -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `claimDepositERC7540`.

`function claimDepositERC7540(address token) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.2 - Check RateLimits [Core]  <!-- UUID: 637a65c8-84a6-4670-b782-1bed08475969 -->

The operator must ensure that a rate limit exists for depositing into the ERC-7540 vault. This is an existence check only: it requires the `LIMIT_7540_DEPOSIT` rate limit keyed to the `token` to have a non-zero `maxAmount`, reverting otherwise, and it neither decreases nor increases the available amount. This confirms the vault is whitelisted before shares are claimed.

`        _rateLimitExists(RateLimitHelpers.makeAssetKey(LIMIT_7540_DEPOSIT, token));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.3 - Get Claimable Shares [Core]  <!-- UUID: 20f412f9-ed6b-4579-bd0c-550f492b4bb7 -->

The operator must determine the number of `shares` that can be claimed by calling `maxMint` for the `proxy` on the ERC-7540 vault. This is the maximum amount of shares the fulfilled deposit request entitles the `proxy` to mint.

`        uint256 shares = IERC7540(token).maxMint(address(proxy));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2.4 - Claim Shares [Core]  <!-- UUID: c6d58a58-9d15-45d1-a886-5c405f2350ee -->

The operator must claim the `shares` from the vault to the `proxy` by calling `mint` on the ERC-7540 vault. The `proxy` receives the minted shares.

`        // Claim shares from the vault to the proxy
        proxy.doCall(
            token,
            abi.encodeCall(IERC4626(token).mint, (shares, address(proxy)))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3 - Request Redeem From ERC-7540 Vault [Core]  <!-- UUID: 01e72e75-9bde-4951-804e-1c422e2c1265 -->

The documents herein define a series of operations for an operator to `requestRedeemERC7540`, submitting an asynchronous redemption request of vault shares to an ERC-7540 vault on behalf of the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.1 - Relayer Role [Core]  <!-- UUID: 31251f84-cfab-483f-b98c-9cf72f2c348b -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `requestRedeemERC7540`.

`function requestRedeemERC7540(address token, uint256 shares) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.2 - Check RateLimits [Core]  <!-- UUID: 82e54145-e633-4c73-bf11-948df17267be -->

The operator must ensure that `RateLimits` allows for redeeming the requested `shares` from the ERC-7540 vault. The rate limit is keyed to the specific `token` and is decreased by the asset-equivalent value of the `shares`, obtained by calling `convertToAssets` on the vault.

`        _rateLimitedAsset(
            LIMIT_7540_REDEEM,
            token,
            IERC7540(token).convertToAssets(shares)
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3.3 - Submit Redeem Request [Core]  <!-- UUID: 8a55fb60-99d2-4780-ab6c-9cf3df788872 -->

The operator must submit the redeem request by calling `requestRedeem` on the ERC-7540 vault, transferring the `shares` from the `proxy` into the vault. The `proxy` is set as both the controller and owner of the request, so the resulting assets can later be claimed to the `proxy`.

`        // Submit redeem request by transferring shares
        proxy.doCall(
            token,
            abi.encodeCall(IERC7540(token).requestRedeem, (shares, address(proxy), address(proxy)))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4 - Claim Redeem From ERC-7540 Vault [Core]  <!-- UUID: ecec5578-ccb1-440e-bad6-ab5c5918becd -->

The documents herein define a series of operations for an operator to `claimRedeemERC7540`, claiming the assets of a previously fulfilled asynchronous redemption request from an ERC-7540 vault to the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.1 - Relayer Role [Core]  <!-- UUID: 0c80de53-a7d0-45c1-9b5a-9efccb990b77 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `claimRedeemERC7540`.

`function claimRedeemERC7540(address token) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.2 - Check RateLimits [Core]  <!-- UUID: c0dd6e35-13bb-4a42-8694-48a84c06a91e -->

The operator must ensure that a rate limit exists for redeeming from the ERC-7540 vault. This is an existence check only: it requires the `LIMIT_7540_REDEEM` rate limit keyed to the `token` to have a non-zero `maxAmount`, reverting otherwise, and it neither decreases nor increases the available amount. This confirms the vault is whitelisted before assets are claimed.

`        _rateLimitExists(RateLimitHelpers.makeAssetKey(LIMIT_7540_REDEEM, token));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.3 - Get Claimable Assets [Core]  <!-- UUID: b86ea1fb-a897-41b5-8483-d3473c5e5f32 -->

The operator must determine the amount of `assets` that can be claimed by calling `maxWithdraw` for the `proxy` on the ERC-7540 vault. This is the maximum amount of the underlying asset the fulfilled redeem request entitles the `proxy` to withdraw.

`        uint256 assets = IERC7540(token).maxWithdraw(address(proxy));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4.4 - Claim Assets [Core]  <!-- UUID: 1c1acaaa-8f4c-46b4-b336-429597968dc7 -->

The operator must claim the `assets` from the vault to the `proxy` by calling `withdraw` on the ERC-7540 vault. The `proxy` receives the withdrawn assets.

`        // Claim assets from the vault to the proxy
        proxy.doCall(
            token,
            abi.encodeCall(IERC7540(token).withdraw, (assets, address(proxy), address(proxy)))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6 - Centrifuge Functions [Core]  <!-- UUID: 541710cd-5aa9-4ef6-a032-4c9213d28395 -->

The documents herein define the Grove Liquidity Layer operations for interacting with Centrifuge V3 asynchronous vaults, including canceling and claiming pending deposit and redeem requests and transferring vault shares across chains.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1 - Cancel Centrifuge Deposit Request [Core]  <!-- UUID: 70b5154e-16a4-4bfc-abe4-1b338da9d155 -->

The documents herein define the steps for an operator to `cancel` a pending deposit request in a Centrifuge V3 vault.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.1 - Relayer Role [Core]  <!-- UUID: 69881982-618e-46bc-9ffb-af5c673a06f9 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cancelCentrifugeDepositRequest`.

`function cancelCentrifugeDepositRequest(address token) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.2 - Check RateLimits [Core]  <!-- UUID: 76cdbff4-b175-483f-9349-9105ad8837f1 -->

The operator must ensure a rate limit is configured for depositing this `token` into the Centrifuge vault. This is an existence check only — the action reverts with `invalid-action` unless the configured `maxAmount` is greater than zero.

`rateLimitExists(makeAssetKey(LIMIT_7540_DEPOSIT, token));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1.3 - Cancel Deposit Request [Core]  <!-- UUID: cedbc7ec-6356-4bf7-a5af-2c71353af7fd -->

The operator must call the Centrifuge vault to `cancelDepositRequest` on behalf of the `proxy`. These cancelation methods are compatible with ERC-7887, and while the cancelation is pending no new deposit request can be submitted.

`proxy.doCall(
            token,
            abi.encodeCall(
                ICentrifugeV3VaultLike(token).cancelDepositRequest,
                (CENTRIFUGE_REQUEST_ID, address(proxy))
            )
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2 - Claim Centrifuge Cancel Deposit Request [Core]  <!-- UUID: 157f11ce-0ac9-4ac4-98c8-c6206a9c57e6 -->

The documents herein define the steps for an operator to `claim` the assets returned by a canceled deposit request in a Centrifuge V3 vault.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.1 - Relayer Role [Core]  <!-- UUID: f4095845-57ef-4e67-9260-c0dfe347c5a5 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `claimCentrifugeCancelDepositRequest`.

`function claimCentrifugeCancelDepositRequest(address token) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.2 - Check RateLimits [Core]  <!-- UUID: efebd3e3-ff1e-49ba-8402-8a3280cc74f0 -->

The operator must ensure a rate limit is configured for depositing this `token` into the Centrifuge vault. This is an existence check only — the action reverts with `invalid-action` unless the configured `maxAmount` is greater than zero.

`rateLimitExists(makeAssetKey(LIMIT_7540_DEPOSIT, token));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2.3 - Claim Canceled Deposit Request [Core]  <!-- UUID: 09b2795e-e171-4756-9a41-db7f22ca9ae2 -->

The operator must call the Centrifuge vault to `claimCancelDepositRequest`, returning the canceled deposit assets to the `proxy`.

`proxy.doCall(
            token,
            abi.encodeCall(
                ICentrifugeV3VaultLike(token).claimCancelDepositRequest,
                (CENTRIFUGE_REQUEST_ID, address(proxy), address(proxy))
            )
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3 - Cancel Centrifuge Redeem Request [Core]  <!-- UUID: efdae580-028a-4fbd-b737-2f755cd2f0b8 -->

The documents herein define the steps for an operator to `cancel` a pending redeem request in a Centrifuge V3 vault.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.1 - Relayer Role [Core]  <!-- UUID: 01fe4914-7846-43ff-820b-52a70bf6ef17 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cancelCentrifugeRedeemRequest`.

`function cancelCentrifugeRedeemRequest(address token) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.2 - Check RateLimits [Core]  <!-- UUID: bb74b0c1-b817-4088-918e-75c69db8e27e -->

The operator must ensure a rate limit is configured for redeeming this `token` from the Centrifuge vault. This is an existence check only — the action reverts with `invalid-action` unless the configured `maxAmount` is greater than zero.

`rateLimitExists(makeAssetKey(LIMIT_7540_REDEEM, token));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3.3 - Cancel Redeem Request [Core]  <!-- UUID: 723f0161-d2aa-467c-9423-115afa55d14e -->

The operator must call the Centrifuge vault to `cancelRedeemRequest` on behalf of the `proxy`. These cancelation methods are compatible with ERC-7887, and while the cancelation is pending no new redeem request can be submitted.

`proxy.doCall(
            token,
            abi.encodeCall(
                ICentrifugeV3VaultLike(token).cancelRedeemRequest,
                (CENTRIFUGE_REQUEST_ID, address(proxy))
            )
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4 - Claim Centrifuge Cancel Redeem Request [Core]  <!-- UUID: 42d9e84a-725f-4d86-b5f2-9b36d2cbe3fd -->

The documents herein define the steps for an operator to `claim` the shares returned by a canceled redeem request in a Centrifuge V3 vault.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.1 - Relayer Role [Core]  <!-- UUID: b2a472a5-d4c5-4504-ae75-842f8fb90a01 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `claimCentrifugeCancelRedeemRequest`.

`function claimCentrifugeCancelRedeemRequest(address token) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.2 - Check RateLimits [Core]  <!-- UUID: ab6e2866-3bd7-4663-bc17-99dd8e72475d -->

The operator must ensure a rate limit is configured for redeeming this `token` from the Centrifuge vault. This is an existence check only — the action reverts with `invalid-action` unless the configured `maxAmount` is greater than zero.

`rateLimitExists(makeAssetKey(LIMIT_7540_REDEEM, token));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4.3 - Claim Canceled Redeem Request [Core]  <!-- UUID: b2ae94d5-bdca-4435-b8cd-8bdceac86823 -->

The operator must call the Centrifuge vault to `claimCancelRedeemRequest`, returning the canceled redeem shares to the `proxy`.

`proxy.doCall(
            token,
            abi.encodeCall(
                ICentrifugeV3VaultLike(token).claimCancelRedeemRequest,
                (CENTRIFUGE_REQUEST_ID, address(proxy), address(proxy))
            )
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5 - Transfer Shares Centrifuge [Core]  <!-- UUID: c7ede989-e153-4593-b428-2787f5daaad9 -->

The documents herein define the steps for an operator to `transferSharesCentrifuge`, initiating a cross-chain transfer of Centrifuge V3 vault shares to a configured recipient on a destination chain.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.1 - Relayer Role [Core]  <!-- UUID: 00b5dd72-7013-4fd5-8ad8-e00f0935cd19 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferSharesCentrifuge`. The function is `payable` so the operator can forward the cross-chain messaging fee.

`function transferSharesCentrifuge(
        address token,
        uint128 amount,
        uint16  destinationCentrifugeId
    )
        external payable
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.2 - Get Configured Recipient [Core]  <!-- UUID: b838767a-5a78-47f5-9c54-b7928cb6f553 -->

The operator must look up the configured recipient for the `destinationCentrifugeId` from the `centrifugeRecipients` mapping.

`bytes32 recipient = centrifugeRecipients[destinationCentrifugeId];`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.3 - Check RateLimits [Core]  <!-- UUID: afbf5683-4b25-4286-9b9f-98e8a9cbc2e6 -->

The operator must ensure the `RateLimits` allow for transferring the required `amount` of shares. The rate limit is keyed on the `LIMIT_CENTRIFUGE_TRANSFER` identifier together with the `token` and `destinationCentrifugeId`, and is decreased by `amount`.

`rateLimited(
            keccak256(abi.encode(LIMIT_CENTRIFUGE_TRANSFER, token, destinationCentrifugeId)),
            amount
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.4 - Check Recipient Configured [Core]  <!-- UUID: 79cb1503-2f4f-4367-b9c9-71a5dddb39fa -->

The operator must ensure a recipient is configured for the `destinationCentrifugeId`. The action reverts with `centrifuge-id-not-configured` if the recipient is unset.

`require(recipient != 0, "MainnetController/centrifuge-id-not-configured");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.5 - Get Spoke Address [Core]  <!-- UUID: 219de76c-8db5-457f-a6ad-297c04ef597f -->

The operator must resolve the `spoke` contract that initiates the cross-chain transfer, obtained from the vault's async redeem `manager`.

`address spoke = IAsyncRedeemManagerLike(
            ICentrifugeV3VaultLike(token).manager()
        ).spoke();`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5.6 - Transfer Shares Cross-Chain [Core]  <!-- UUID: 695ec457-b53f-4521-b238-e8dccd377c2e -->

The operator must initiate the cross-chain share transfer through the resolved `spoke`, forwarding `msg.value` to cover the messaging fee. The call passes the vault `poolId` and `scId`, the configured `recipient`, and the `amount` of shares.

`proxy.doCallWithValue{value: msg.value}(
            spoke,
            abi.encodeCall(
                ISpokeLike(spoke).crosschainTransferShares,
                (
                    destinationCentrifugeId,
                    ICentrifugeV3VaultLike(token).poolId(),
                    ICentrifugeV3VaultLike(token).scId(),
                    recipient,
                    amount,
                    0
                )
            ),
            msg.value
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7 - Aave Functions [Core]  <!-- UUID: 6ee853cb-144f-4070-8572-f8c94353cd4d -->

The documents herein define the operations performed by the Grove Liquidity Layer to supply and withdraw assets through the Aave protocol.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1 - Deposit Into Aave [Core]  <!-- UUID: c159a99f-da73-477e-8052-f62b78b7b93e -->

The documents herein define the steps for an operator to `depositAave` underlying tokens from the Grove ALM Proxy into an Aave pool in exchange for `aToken`.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.1 - Relayer Role [Core]  <!-- UUID: ef00ff33-d1a0-49c0-bf6c-50f8e8b83706 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `depositAave`, which is enforced by the `_checkRole` check at the start of the function.

`function depositAave(address aToken, uint256 amount) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.2 - Check RateLimits [Core]  <!-- UUID: 2ace0a4a-e569-40de-b5f0-8d69d43843bb -->

The operator must ensure the `RateLimits` allow for depositing the required `amount` of the underlying asset. The limit is keyed per `aToken` through `makeAssetKey(LIMIT_AAVE_DEPOSIT, aToken)`, and the rate limit is decreased before the deposit is performed.

`        _rateLimitedAsset(LIMIT_AAVE_DEPOSIT, aToken, amount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.3 - Check Max Slippage [Core]  <!-- UUID: 8356f5f0-758d-4c7f-b649-b21243d5d346 -->

The operator must ensure a maximum slippage has been configured for the `aToken`. The transaction reverts with `max-slippage-not-set` when `maxSlippages[aToken]` is zero.

`        require(maxSlippages[aToken] != 0, "MainnetController/max-slippage-not-set");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.4 - Resolve Pool And Snapshot Balance [Core]  <!-- UUID: 5138afb5-60e9-4805-b329-254f0cd090e8 -->

The operator must resolve the `underlying` asset and the Aave `pool` from the `aToken`, then snapshot the `proxy` current `aToken` balance so the amount of newly minted `aToken` can be measured after the deposit.

`        IERC20    underlying = IERC20(IATokenWithPool(aToken).UNDERLYING_ASSET_ADDRESS());
        IAavePool pool       = IAavePool(IATokenWithPool(aToken).POOL());

        uint256 aTokenBalance = IERC20(aToken).balanceOf(address(proxy));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.5 - Approve Aave Pool Spend [Core]  <!-- UUID: 9f28cd92-e805-4579-a509-69e01db491f2 -->

The operator must approve the Aave `pool` to spend the `amount` of `underlying` on behalf of the `proxy`, which assumes the `proxy` holds enough of the `underlying` asset.

`        // Approve underlying to Aave pool from the proxy (assumes the proxy has enough underlying).
        ERC20Lib.approve(proxy, address(underlying), address(pool), amount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.6 - Supply To Aave Pool [Core]  <!-- UUID: 028a06d5-c91d-42ff-8a0d-a6f272948d90 -->

The operator must `supply` the `underlying` into the Aave `pool` on behalf of the `proxy`, so that the `proxy` receives the corresponding `aToken`.

`        // Deposit underlying into Aave pool, proxy receives aTokens
        proxy.doCall(
            address(pool),
            abi.encodeCall(pool.supply, (address(underlying), amount, address(proxy), 0))
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1.7 - Check Slippage [Core]  <!-- UUID: 443a2d00-b7e3-4302-8088-35c801092988 -->

The operator must verify the `proxy` received enough `aToken`, measured as the balance increase since the snapshot. The transaction reverts with `slippage-too-high` when the newly minted `aToken` are below `amount` scaled by `maxSlippages[aToken]`.

`        uint256 newATokens = IERC20(aToken).balanceOf(address(proxy)) - aTokenBalance;

        require(
            newATokens >= amount * maxSlippages[aToken] / 1e18,
            "MainnetController/slippage-too-high"
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2 - Withdraw From Aave [Core]  <!-- UUID: 793e928c-9b1f-480f-ab56-1b19f9e5c60d -->

The documents herein define the steps for an operator to `withdrawAave` underlying tokens from an Aave pool back to the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.1 - Relayer Role [Core]  <!-- UUID: 49603674-9276-4588-9855-e45fbd67b57b -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `withdrawAave`, which is enforced by the `_checkRole` check at the start of the function.

`function withdrawAave(address aToken, uint256 amount)
        external
        returns (uint256 amountWithdrawn)
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.2 - Resolve Aave Pool [Core]  <!-- UUID: dbadb917-8810-4515-84da-c68c6a6002a3 -->

The operator must resolve the Aave `pool` from the `aToken` in order to withdraw the underlying asset.

`        IAavePool pool = IAavePool(IATokenWithPool(aToken).POOL());`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.3 - Withdraw Underlying [Core]  <!-- UUID: 8c1cd838-4032-4f43-a5cf-cf35f6fef967 -->

The operator must `withdraw` the underlying asset from the Aave `pool` to the `proxy`, assuming the `proxy` holds adequate `aToken`, and decode the returned `amountWithdrawn`.

`        // Withdraw underlying from Aave pool, decode resulting amount withdrawn.
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

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2.4 - Update RateLimits [Core]  <!-- UUID: b845955c-8963-4234-af56-569cd65bb4bb -->

The operator must decrease the `RateLimits` by the `amountWithdrawn` after the withdrawal completes. The limit is keyed per `aToken` through `makeAssetKey(LIMIT_AAVE_WITHDRAW, aToken)`, so `withdrawAave` is rate limited at the end of the function rather than before.

`        rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(LIMIT_AAVE_WITHDRAW, aToken),
            amountWithdrawn
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8 - Curve Functions [Core]  <!-- UUID: fc9d9964-f22d-4024-aab2-913b322a627b -->

The documents herein define the Curve StableSwap operations performed by the Grove Liquidity Layer, including swapping tokens and providing or withdrawing pool liquidity.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1 - Swap On Curve [Core]  <!-- UUID: fce783bb-d1b9-4b5e-9577-5149dc494af4 -->

The documents herein define a series of operations for an operator to `swapCurve`, exchanging one pool token for another through a Curve StableSwap pool.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.1 - Relayer Role [Core]  <!-- UUID: 363b3afa-134c-4650-bd83-74e25152d5de -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `swapCurve`, which enforces `_checkRole(RELAYER)` before delegating the swap to `CurveLib.swap`.

`function swapCurve(
        address pool,
        uint256 inputIndex,
        uint256 outputIndex,
        uint256 amountIn,
        uint256 minAmountOut
    )
        external returns (uint256 amountOut)
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.2 - Validate Swap Parameters [Core]  <!-- UUID: 3bd2d8ce-12a5-4519-9e7a-720ef48667ba -->

The operator must ensure the `inputIndex` and `outputIndex` differ, otherwise the call reverts with `CurveLib/invalid-indices`. They must also ensure a `maxSlippage` has been configured for the `pool`, otherwise the call reverts with `CurveLib/max-slippage-not-set`.

`require(params.inputIndex != params.outputIndex, "CurveLib/invalid-indices");

        require(params.maxSlippage != 0, "CurveLib/max-slippage-not-set");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.3 - Check Pool Coin Count [Core]  <!-- UUID: 8bde4dd3-aead-466e-ae9f-49dc8dcf8457 -->

The operator must ensure both `inputIndex` and `outputIndex` are less than the pool's `N_COINS`, otherwise the call reverts with `CurveLib/index-too-high`.

`ICurvePoolLike curvePool = ICurvePoolLike(params.pool);

        uint256 numCoins = curvePool.N_COINS();
        require(
            params.inputIndex < numCoins && params.outputIndex < numCoins,
            "CurveLib/index-too-high"
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.4 - Enforce Minimum Output [Core]  <!-- UUID: a07d408e-d0d1-4386-bdf3-a7b9f00b5e3e -->

The operator must ensure `minAmountOut` is at least the minimum output implied by the pool's `stored_rates` and the configured `maxSlippage`, otherwise the call reverts with `CurveLib/min-amount-not-met`.

`uint256[] memory rates = curvePool.stored_rates();

        uint256 minimumMinAmountOut = params.amountIn
            * rates[params.inputIndex]
            * params.maxSlippage
            / rates[params.outputIndex]
            / 1e18;

        require(
            params.minAmountOut >= minimumMinAmountOut,
            "CurveLib/min-amount-not-met"
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.5 - Decrease Swap Rate Limit [Core]  <!-- UUID: 616673d0-6961-495e-b8b0-335c0eedba25 -->

The operator must decrease the `LIMIT_CURVE_SWAP` rate limit for the `pool` by the value of the tokens being swapped in, before the exchange is executed.

`params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.rateLimitId, params.pool),
            params.amountIn * rates[params.inputIndex] / 1e18
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.6 - Approve Pool Spend [Core]  <!-- UUID: f4cccce9-ded8-4924-8398-81bd43b95e51 -->

The operator must approve the `pool` to spend `amountIn` of the input token on behalf of the `proxy`.

`ERC20Lib.approve(params.proxy, curvePool.coins(params.inputIndex), params.pool, params.amountIn);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1.7 - Execute Swap [Core]  <!-- UUID: 39d942fe-5c37-4950-bc50-d898c0a5f997 -->

The operator must call `exchange` on the `pool` through the `proxy`, swapping the input token for the output token and returning the received `amountOut` to the `proxy`.

`amountOut = abi.decode(
            params.proxy.doCall(
                params.pool,
                abi.encodeCall(
                    curvePool.exchange,
                    (
                        int128(int256(params.inputIndex)),
                        int128(int256(params.outputIndex)),
                        params.amountIn,
                        params.minAmountOut,
                        address(params.proxy)
                    )
                )
            ),
            (uint256)
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2 - Add Liquidity On Curve [Core]  <!-- UUID: 69c7bee3-40d6-449f-97c2-db591e5fb831 -->

The documents herein define a series of operations for an operator to `addLiquidityCurve`, depositing tokens into a Curve StableSwap pool in exchange for LP shares.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.1 - Relayer Role [Core]  <!-- UUID: de2ec5fb-8fbb-48e0-8f57-d53cc0d0eee3 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `addLiquidityCurve`, which enforces `_checkRole(RELAYER)` before delegating the deposit to `CurveLib.addLiquidity`.

`function addLiquidityCurve(
        address pool,
        uint256[] memory depositAmounts,
        uint256 minLpAmount
    )
        external returns (uint256 shares)
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.2 - Validate Deposit Amounts [Core]  <!-- UUID: 88916197-b09b-4a25-8ecb-1fb2221b2951 -->

The operator must ensure a `maxSlippage` has been configured for the `pool`, otherwise the call reverts with `CurveLib/max-slippage-not-set`. They must also ensure the length of `depositAmounts` matches the pool's `N_COINS`, otherwise the call reverts with `CurveLib/invalid-deposit-amounts`.

`require(params.maxSlippage != 0, "CurveLib/max-slippage-not-set");

        ICurvePoolLike curvePool = ICurvePoolLike(params.pool);

        require(
            params.depositAmounts.length == curvePool.N_COINS(),
            "CurveLib/invalid-deposit-amounts"
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.3 - Approve And Aggregate Deposit Value [Core]  <!-- UUID: 14e225e3-5667-49bb-9773-7cb58cd32874 -->

The operator must approve the `pool` to spend each deposited token on behalf of the `proxy` and aggregate the total value deposited using the pool's `stored_rates`.

`uint256[] memory rates = curvePool.stored_rates();

        uint256 valueDeposited;
        for (uint256 i = 0; i < params.depositAmounts.length; i++) {
            ERC20Lib.approve(params.proxy, curvePool.coins(i), params.pool, params.depositAmounts[i]);
            valueDeposited += params.depositAmounts[i] * rates[i];
        }
        valueDeposited /= 1e18;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.4 - Enforce Minimum LP Amount [Core]  <!-- UUID: 4d815893-dcbd-4321-97c0-c377c5a4565e -->

The operator must ensure `minLpAmount` is at least the aggregated deposit value scaled by `maxSlippage` and the pool's `get_virtual_price`, otherwise the call reverts with `CurveLib/min-amount-not-met`.

`require(
            params.minLpAmount >= valueDeposited
                * params.maxSlippage
                / curvePool.get_virtual_price(),
            "CurveLib/min-amount-not-met"
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.5 - Decrease Deposit Rate Limit [Core]  <!-- UUID: 8730991d-81ee-42f1-9a0e-0225593e11de -->

The operator must decrease the `LIMIT_CURVE_DEPOSIT` rate limit for the `pool` by the aggregated value deposited, before liquidity is added.

`params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.addLiquidityRateLimitId, params.pool),
            valueDeposited
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.6 - Add Liquidity [Core]  <!-- UUID: 3b14adbf-eb29-4ae2-ae3c-3366ae7db9ce -->

The operator must call `add_liquidity` on the `pool` through the `proxy`, depositing the tokens and returning the minted LP `shares` to the `proxy`.

`shares = abi.decode(
            params.proxy.doCall(
                params.pool,
                abi.encodeCall(
                    curvePool.add_liquidity,
                    (params.depositAmounts, params.minLpAmount, address(params.proxy))
                )
            ),
            (uint256)
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2.7 - Decrease Swap Rate Limit [Core]  <!-- UUID: e3993529-77fc-4b49-ab37-d3510dff56fb -->

The operator must compute the swap implied by the imbalance between the deposited amounts and the value of the minted shares, then decrease the `LIMIT_CURVE_SWAP` rate limit for the `pool` by this implied `averageSwap`, after liquidity is added.

`uint256 totalSwapped;
        for (uint256 i; i < params.depositAmounts.length; i++) {
            totalSwapped += MathLib._absSubtraction(
                curvePool.balances(i) * rates[i] * shares / curvePool.totalSupply(),
                params.depositAmounts[i] * rates[i]
            );
        }
        uint256 averageSwap = totalSwapped / 2 / 1e18;

        params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.swapRateLimitId, params.pool),
            averageSwap
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3 - Remove Liquidity On Curve [Core]  <!-- UUID: 7f63d8d5-5111-48e1-8d33-071bf2de6a30 -->

The documents herein define a series of operations for an operator to `removeLiquidityCurve`, burning LP shares to withdraw the underlying tokens from a Curve StableSwap pool.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.1 - Relayer Role [Core]  <!-- UUID: 66cab13d-bdbf-4116-9be6-204e136f6829 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to call `removeLiquidityCurve`, which enforces `_checkRole(RELAYER)` before delegating the withdrawal to `CurveLib.removeLiquidity`.

`function removeLiquidityCurve(
        address   pool,
        uint256   lpBurnAmount,
        uint256[] memory minWithdrawAmounts
    )
        external returns (uint256[] memory withdrawnTokens)
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.2 - Validate Minimum Withdraw Amounts [Core]  <!-- UUID: ce61aae1-480f-4e87-855d-c2dab99ede1c -->

The operator must ensure a `maxSlippage` has been configured for the `pool`, otherwise the call reverts with `CurveLib/max-slippage-not-set`. They must also ensure the length of `minWithdrawAmounts` matches the pool's `N_COINS`, otherwise the call reverts with `CurveLib/invalid-min-withdraw-amounts`.

`require(params.maxSlippage != 0, "CurveLib/max-slippage-not-set");

        ICurvePoolLike curvePool = ICurvePoolLike(params.pool);

        require(
            params.minWithdrawAmounts.length == curvePool.N_COINS(),
            "CurveLib/invalid-min-withdraw-amounts"
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.3 - Aggregate Minimum Withdrawal Value [Core]  <!-- UUID: 43167a40-dcb7-4b17-a615-1e359771822d -->

The operator must aggregate the minimum value to be withdrawn from `minWithdrawAmounts` using the pool's `stored_rates`.

`uint256[] memory rates = curvePool.stored_rates();

        uint256 valueMinWithdrawn;
        for (uint256 i = 0; i < params.minWithdrawAmounts.length; i++) {
            valueMinWithdrawn += params.minWithdrawAmounts[i] * rates[i];
        }
        valueMinWithdrawn /= 1e18;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.4 - Enforce Minimum Withdrawal Value [Core]  <!-- UUID: c1a41667-2cf5-4794-91cc-718d593e4fef -->

The operator must ensure the aggregated minimum withdrawal value is at least `lpBurnAmount` scaled by the pool's `get_virtual_price` and `maxSlippage`, otherwise the call reverts with `CurveLib/min-amount-not-met`.

`require(
            valueMinWithdrawn >= params.lpBurnAmount
                * curvePool.get_virtual_price()
                * params.maxSlippage
                / 1e36,
            "CurveLib/min-amount-not-met"
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.5 - Remove Liquidity [Core]  <!-- UUID: 44e41f28-d634-460b-b084-1c3a356a355e -->

The operator must call `remove_liquidity` on the `pool` through the `proxy`, burning `lpBurnAmount` LP shares and returning the withdrawn tokens to the `proxy`.

`withdrawnTokens = abi.decode(
            params.proxy.doCall(
                params.pool,
                abi.encodeCall(
                    curvePool.remove_liquidity,
                    (params.lpBurnAmount, params.minWithdrawAmounts, address(params.proxy), false)
                )
            ),
            (uint256[])
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3.6 - Decrease Withdraw Rate Limit [Core]  <!-- UUID: a75cdaf7-8ad5-41aa-84c3-2d80a1d09495 -->

The operator must aggregate the value of the withdrawn tokens using the pool's `stored_rates`, then decrease the `LIMIT_CURVE_WITHDRAW` rate limit for the `pool` by this value, after liquidity is removed.

`uint256 valueWithdrawn;
        for (uint256 i = 0; i < withdrawnTokens.length; i++) {
            valueWithdrawn += withdrawnTokens[i] * rates[i];
        }
        valueWithdrawn /= 1e18;

        params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.rateLimitId, params.pool),
            valueWithdrawn
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9 - Uniswap V3 Functions [Core]  <!-- UUID: 6f7d6270-3294-4707-a300-46edc2649af6 -->

The documents herein define the operations performed by the Grove Liquidity Layer to swap tokens and provide liquidity through Uniswap V3 pools.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1 - Swap Tokens Through Uniswap V3 [Core]  <!-- UUID: 6dde4141-4930-4b59-bd78-ead1c3568c5d -->

The documents herein define the steps for an operator to `swapUniswapV3`, exchanging one of a Uniswap V3 pool's tokens for the other through the pool `router`.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.1 - Relayer Role [Core]  <!-- UUID: 3bf9b752-398b-4c53-8a32-608619621193 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapUniswapV3`. The function exchanges `tokenIn` for the pool's other token through the Uniswap V3 `router`.

`function swapUniswapV3(
        address pool,
        address tokenIn,
        uint256 amountIn,
        uint256 minAmountOut,
        uint24  swapMaxTickDelta
    )
        external returns (uint256 amountOut)
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.2 - Validate Swap Parameters [Core]  <!-- UUID: 228b1526-0ddb-48ae-ae8b-cbe3bea71685 -->

The operator must ensure the requested `tickDelta` does not exceed the pool's configured `swapMaxTickDelta`, that the pool's `twapSecondsAgo` is set, and that `minAmountOut` is greater than zero before the swap is routed through `UniswapV3Lib`.

`function swap(UniV3Context calldata context, SwapParams calldata params) external returns (uint256 amountOut) {
        require(params.tickDelta <= params.poolParams.swapMaxTickDelta, "UniswapV3Lib/invalid-max-tick-delta");
        require(params.poolParams.twapSecondsAgo != 0,                  "UniswapV3Lib/zero-twap-seconds");
        require(params.minAmountOut > 0,                                "UniswapV3Lib/min-amount-not-set");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.3 - Compute Price Limit [Core]  <!-- UUID: b559e279-2bf0-4047-8e23-023c1eaf1928 -->

The operator must confirm `tokenIn` is one of the pool's two tokens, consult the pool's TWAP tick, and compute the `sqrtPriceLimitX96` bound from the TWAP tick offset by `tickDelta` and bounded to the `TickMath` minimum and maximum, so the swap cannot move the price beyond the configured limit.

`SwapCache memory cache = _populateSwapCache(context, params);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.4 - Approve The Router [Core]  <!-- UUID: e6362ec9-4c75-49d3-9706-fec84f814126 -->

The operator must approve the Uniswap V3 `router` to spend `amountIn` of `tokenIn` on behalf of the `proxy`, then record the `proxy` starting balance of `tokenIn`.

`ERC20Lib.approve(context.proxy, params.tokenIn, address(params.router), params.amountIn);

        uint256 startingBalance = IERC20(params.tokenIn).balanceOf(address(context.proxy));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.5 - Execute The Swap [Core]  <!-- UUID: 5ddf7a99-ba35-4fc0-984a-1fa59e697695 -->

The operator must execute the swap by calling `exactInputSingle` on the `router` through the `proxy`, receiving `amountOut` of the output token, then record the `proxy` ending balance of `tokenIn`.

`amountOut               = _callSwap(context, params, cache);
        uint256 endingBalance   = IERC20(params.tokenIn).balanceOf(address(context.proxy));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.6 - Clear Dust Approval [Core]  <!-- UUID: e7f4ee84-ede7-464a-adbe-f20a22280dda -->

The operator must reset the `router` allowance for `tokenIn` back to zero to clear any dust approval left after the swap.

`// Clear approvals of dust
        ERC20Lib.approve(context.proxy, params.tokenIn, address(params.router), 0);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1.7 - Decrease RateLimit [Core]  <!-- UUID: d23acaaf-29b8-4a8b-a5a8-40e24238c892 -->

The operator must decrease the `LIMIT_UNISWAP_V3_SWAP` rate limit for the `tokenIn` and `pool` pair by the amount of `tokenIn` actually spent, which is the difference between the starting and ending balances.

`context.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, params.tokenIn, context.pool),
            startingBalance - endingBalance
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2 - Add Liquidity To Uniswap V3 [Core]  <!-- UUID: 222d77a8-3cd1-46da-a720-1c474b760cfa -->

The documents herein define the steps for an operator to `addLiquidityUniswapV3`, minting a new liquidity position or increasing an existing one within governance-set tick bounds.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.1 - Relayer Role [Core]  <!-- UUID: d2558ce3-2378-4794-938f-81dae9846231 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `addLiquidityUniswapV3`. The function mints or increases a liquidity position in the given Uniswap V3 `pool`.

`function addLiquidityUniswapV3(
        address                   pool,
        uint256                   tokenId,
        UniswapV3Lib.Tick         calldata tick,
        UniswapV3Lib.TokenAmounts calldata target,
        UniswapV3Lib.TokenAmounts calldata min,
        uint256                   deadline
    )
        external
        returns (uint256 tokenId_, uint128 liquidity_, uint256 amount0_, uint256 amount1_)
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.2 - Validate Deposit Parameters [Core]  <!-- UUID: c3aab084-e3f1-4e7b-af33-0c1ea9a15d06 -->

The operator must ensure at least one of the target amounts is greater than zero, that `maxSlippage` is set for the pool, and that the pool's `twapSecondsAgo` is set before the deposit is routed through `UniswapV3Lib`.

`function addLiquidity(UniV3Context calldata context, AddLiquidityParams calldata params)
        external
        returns (uint256 tokenId, uint128 liquidity, uint256 amount0, uint256 amount1)
    {
        require(
            params.target.amount0 > 0 || params.target.amount1 > 0,
            "UniswapV3Lib/zero-amount"
        );

        require(params.maxSlippage > 0,     "UniswapV3Lib/max-slippage-not-set");
        require(params.twapSecondsAgo != 0, "UniswapV3Lib/zero-twap-seconds");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.3 - Approve The Position Manager [Core]  <!-- UUID: 0639862b-3640-48d1-9117-b713d8ba89b7 -->

The operator must read `token0` and `token1` from the pool and approve the `positionManager` to spend the target amount of each token on behalf of the `proxy`.

`IUniswapV3PoolLike pool = IUniswapV3PoolLike(context.pool);

        address token0 = pool.token0();
        address token1 = pool.token1();

        ERC20Lib.approve(context.proxy, token0, address(params.positionManager), params.target.amount0);
        ERC20Lib.approve(context.proxy, token1, address(params.positionManager), params.target.amount1);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.4 - Validate Minimum Amounts [Core]  <!-- UUID: d48bbd5d-da24-472f-83cc-20d817e13487 -->

The operator must validate the minimum amounts by consulting the TWAP tick, computing the expected token amounts for the target liquidity, and requiring each `min` amount to be at least the expected amount scaled by `maxSlippage`.

`_validateAddLiquidityMinAmounts(context, params);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.5 - Mint Or Increase Liquidity [Core]  <!-- UUID: c03bfbe1-1712-44a8-87a7-68a3fc720f66 -->

The operator must, when `tokenId` is zero, mint a new position after checking the requested `tick` range is within the governance-set bounds and aligned to the pool's tick spacing; otherwise the operator must increase liquidity on the existing position owned by the `proxy`.

`if (params.tokenId == 0) {
            (tokenId, liquidity, amount0, amount1) = _mintLiquidity(context, params);
        } else {
            (tokenId, liquidity, amount0, amount1) = _addLiquidityToExistingPosition(context, params);
        }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.6 - Clear Dust Approvals [Core]  <!-- UUID: 5bbe99a6-c616-4857-a220-7f2f0bd0ac0d -->

The operator must ensure that the liquidity added is not zero, then reset the `positionManager` allowance for both tokens back to zero to clear any dust approval.

`require(liquidity != 0, "UniswapV3Lib/no-liquidity-increased");

        // Clear approvals of dust
        ERC20Lib.approve(context.proxy, token0, address(params.positionManager), 0);
        ERC20Lib.approve(context.proxy, token1, address(params.positionManager), 0);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2.7 - Decrease RateLimits [Core]  <!-- UUID: c646989c-15cc-4d74-892c-30f3593c8515 -->

The operator must decrease the `LIMIT_UNISWAP_V3_DEPOSIT` rate limit for the `token0` and `pool` pair by `amount0`, and for the `token1` and `pool` pair by `amount1`, reflecting the tokens actually deposited.

`context.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, token0, address(pool)),
            amount0
        );
        context.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, token1, address(pool)),
            amount1
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3 - Remove Liquidity From Uniswap V3 [Core]  <!-- UUID: 2ed22524-d397-4239-bc35-d4c2e13bf0c2 -->

The documents herein define the steps for an operator to `removeLiquidityUniswapV3`, decreasing a liquidity position and collecting the withdrawn tokens to the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.1 - Relayer Role [Core]  <!-- UUID: 1eb0e395-bd23-4088-ab1c-8971f2acbb17 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `removeLiquidityUniswapV3`. The function decreases a liquidity position and collects the withdrawn tokens to the `proxy`.

`function removeLiquidityUniswapV3(
        address                   pool,
        uint256                   tokenId,
        uint128                   liquidity,
        UniswapV3Lib.TokenAmounts calldata min,
        uint256                   deadline
    )
        external
        onlyRole(RELAYER)
        returns (uint256 amount0Collected, uint256 amount1Collected)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.2 - Validate Position Parameters [Core]  <!-- UUID: d96cfa41-45bd-43c1-a0b8-22d6ec624104 -->

The operator must validate the removal parameters, ensuring the position's tokens and fee match the `pool` and that the requested `liquidity` is greater than zero and does not exceed the position's liquidity.

`function removeLiquidity(UniV3Context calldata context, RemoveLiquidityParams calldata params)
        external
        returns (uint256 amount0Collected, uint256 amount1Collected)
    {
        IUniswapV3PoolLike pool = IUniswapV3PoolLike(context.pool);

        (address token0, address token1) = _validateRemoveLiquidityParams(pool, params);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.3 - Verify Ownership And Snapshot Balances [Core]  <!-- UUID: 499b7fbe-d555-4d5d-8025-4611ed308d9b -->

The operator must ensure the `proxy` owns the position `tokenId`, then record the `proxy` starting balances of `token0` and `token1` before the withdrawal.

`require(params.positionManager.ownerOf(params.tokenId) == address(context.proxy), "UniswapV3Lib/proxy-does-not-own-token-id");

        uint256 amount0CollectedBefore = IERC20(token0).balanceOf(address(context.proxy));
        uint256 amount1CollectedBefore = IERC20(token1).balanceOf(address(context.proxy));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.4 - Decrease Liquidity [Core]  <!-- UUID: 93a4feb6-687b-44a4-b5c8-5ac466a356eb -->

The operator must decrease the position's liquidity by calling `decreaseLiquidity` on the `positionManager` through the `proxy`, passing the requested `liquidity`, the minimum amounts, and the `deadline`.

`_decreaseLiquidityCall(
            context.proxy,
            address(params.positionManager),
            params.tokenId,
            params.liquidity,
            params.min,
            params.deadline
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.5 - Collect Tokens [Core]  <!-- UUID: 3b093990-0f1e-47d5-bbc2-ab49385e8383 -->

The operator must collect the withdrawn tokens by calling `collect` on the `positionManager` through the `proxy`, receiving `amount0Collected` and `amount1Collected`, then record the `proxy` ending balances of `token0` and `token1`.

`(amount0Collected, amount1Collected) = _collectAll(
            context.proxy,
            address(params.positionManager),
            params.tokenId,
            address(context.proxy)
        );

        uint256 amount0CollectedAfter = IERC20(token0).balanceOf(address(context.proxy));
        uint256 amount1CollectedAfter = IERC20(token1).balanceOf(address(context.proxy));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.6 - Validate Minimum Amounts [Core]  <!-- UUID: fd3a1c0a-631c-46a7-bac3-6a8d05afa58e -->

The operator must ensure each `min` amount is at least the collected balance delta scaled by `maxSlippage`, so the withdrawal does not settle below the acceptable bound.

`require(params.min.amount0 >= (amount0CollectedAfter - amount0CollectedBefore) * params.maxSlippage / 1e18, "UniswapV3Lib/min-amount-below-bound");
        require(params.min.amount1 >= (amount1CollectedAfter - amount1CollectedBefore) * params.maxSlippage / 1e18, "UniswapV3Lib/min-amount-below-bound");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3.7 - Decrease RateLimits [Core]  <!-- UUID: afb2942a-2f4c-4201-8d46-eca71f2672b8 -->

The operator must, for each token collected in a non-zero amount, decrease the `LIMIT_UNISWAP_V3_WITHDRAW` rate limit for that token and `pool` pair by the amount collected.

`if (amount0Collected > 0) {
            context.rateLimits.triggerRateLimitDecrease(
                RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, token0, context.pool),
                amount0Collected
            );
        }
        if (amount1Collected > 0) {
            context.rateLimits.triggerRateLimitDecrease(
                RateLimitHelpers.makeAssetDestinationKey(context.rateLimitId, token1, context.pool),
                amount1Collected
            );
        }
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10 - Ethena Functions [Core]  <!-- UUID: 6c06a28a-d752-4263-813f-07491c37d02d -->

The documents herein define the operations performed by the Grove Liquidity Layer to prepare USDe mint and burn through the Ethena minter, manage delegated signers, and cool down and unstake sUSDe.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1 - Set Delegated Signer [Core]  <!-- UUID: 8bf863fd-4a89-404f-91ff-a48e3a67b770 -->

The documents herein define the steps for an operator to `setDelegatedSigner`, authorizing a signer to sign Ethena mint and redeem orders on behalf of the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1.1 - Relayer Role [Core]  <!-- UUID: 9ef24c37-3164-437f-b0b6-2f19105022db -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `setDelegatedSigner`, which is enforced by the `_checkRole` check at the start of the function.

`function setDelegatedSigner(address delegatedSigner) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.1.2 - Set Delegated Signer On Ethena Minter [Core]  <!-- UUID: a542c364-ce22-44c3-816d-97742b2d6a8f -->

The operator must call the `MainnetController` contract to set the `delegatedSigner` on the `ethenaMinter`. The call is executed against the Ethena minter through `proxy.doCall`, authorizing the `delegatedSigner` to sign mint and redeem orders on behalf of the Grove ALM Proxy.

`        proxy.doCall(
            address(ethenaMinter),
            abi.encodeCall(ethenaMinter.setDelegatedSigner, (address(delegatedSigner)))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2 - Remove Delegated Signer [Core]  <!-- UUID: bca725d8-9e81-4d63-9ff2-6399c1e14244 -->

The documents herein define the steps for an operator to `removeDelegatedSigner`, revoking a signer previously authorized to sign Ethena mint and redeem orders on behalf of the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2.1 - Relayer Role [Core]  <!-- UUID: e2c8aec9-1ab9-4ac0-af1b-8e0dce1cef93 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `removeDelegatedSigner`, which is enforced by the `_checkRole` check at the start of the function.

`function removeDelegatedSigner(address delegatedSigner) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.2.2 - Remove Delegated Signer On Ethena Minter [Core]  <!-- UUID: c638b0e2-9986-48f8-9652-cda49296d85d -->

The operator must call the `MainnetController` contract to remove the `delegatedSigner` on the `ethenaMinter`. The call is executed against the Ethena minter through `proxy.doCall`, revoking the `delegatedSigner`'s authorization to sign mint and redeem orders on behalf of the Grove ALM Proxy.

`        proxy.doCall(
            address(ethenaMinter),
            abi.encodeCall(ethenaMinter.removeDelegatedSigner, (address(delegatedSigner)))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3 - Prepare USDe Mint [Core]  <!-- UUID: 5e5d34de-b8ce-4626-8b53-12a5a8153da3 -->

The documents herein define the steps for an operator to `prepareUSDeMint`, approving the Ethena minter to spend USDC from the Grove ALM Proxy so that USDe can be minted. The actual mint is executed off-contract by Ethena against this approval.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.1 - Relayer Role [Core]  <!-- UUID: 0b72eee2-1068-4d6a-8a47-f342d7672c89 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeMint`, which is enforced by the `_checkRole` check at the start of the function.

`function prepareUSDeMint(uint256 usdcAmount) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.2 - Check RateLimits [Core]  <!-- UUID: 5159b62c-b5c3-4a5e-b788-fe89550bb120 -->

The operator must ensure the `RateLimits` allow for minting the required amount, keyed on `LIMIT_USDE_MINT`, and the rate limit is decreased before the approval is set. Note that Ethena's per-block mint limits are shared with other users, so a mint may still fail even when the `RateLimits` allow the `usdcAmount`.

`        _rateLimited(LIMIT_USDE_MINT, usdcAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.3.3 - Approve USDC To Ethena Minter [Core]  <!-- UUID: 4ac9dee5-c673-4061-a636-702b3da8fbe5 -->

The operator must approve the `ethenaMinter` to spend the `usdcAmount` of `usdc` on behalf of the `proxy`. This step only sets the approval; the USDe mint itself is executed off-contract by Ethena against this approval.

`        ERC20Lib.approve(proxy, address(usdc), address(ethenaMinter), usdcAmount);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4 - Prepare USDe Burn [Core]  <!-- UUID: a97278cf-aa36-433e-9d60-4d05edfe4291 -->

The documents herein define the steps for an operator to `prepareUSDeBurn`, approving the Ethena minter to spend USDe from the Grove ALM Proxy so that USDe can be redeemed. The actual redemption is executed off-contract by Ethena against this approval.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.1 - Relayer Role [Core]  <!-- UUID: a4ee29f7-f12f-4da4-89eb-997c7dc30c35 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeBurn`, which is enforced by the `_checkRole` check at the start of the function.

`function prepareUSDeBurn(uint256 usdeAmount) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.2 - Check RateLimits [Core]  <!-- UUID: 69b6ebfe-0a0a-4252-bc99-9e4df4dde4b1 -->

The operator must ensure the `RateLimits` allow for redeeming the required amount, keyed on `LIMIT_USDE_BURN`, and the rate limit is decreased before the approval is set. Note that Ethena's per-block redeem limits are shared with other users, so a redemption may still fail even when the `RateLimits` allow the `usdeAmount`.

`        _rateLimited(LIMIT_USDE_BURN, usdeAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.4.3 - Approve USDe To Ethena Minter [Core]  <!-- UUID: ea08a00b-dc11-4793-a533-d23410b06b8f -->

The operator must approve the `ethenaMinter` to spend the `usdeAmount` of `usde` on behalf of the `proxy`. This step only sets the approval; the USDe redemption itself is executed off-contract by Ethena against this approval.

`        ERC20Lib.approve(proxy, address(usde), address(ethenaMinter), usdeAmount);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5 - Cooldown sUSDe Assets [Core]  <!-- UUID: 8c286f75-c49b-41ad-9763-6d1a401cce8b -->

The documents herein define the steps for an operator to `cooldownAssetsSUSDe`, initiating a cooldown on sUSDe held by the Grove ALM Proxy for a specified amount of USDe assets to be received once the cooldown period elapses.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.1 - Relayer Role [Core]  <!-- UUID: ec105dad-7ddc-4973-b3f5-c1cb92667a5b -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownAssetsSUSDe`, which is enforced by the `_checkRole` check at the start of the function.

`function cooldownAssetsSUSDe(uint256 usdeAmount) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.2 - Check RateLimits [Core]  <!-- UUID: 612346e6-7a94-4409-a05d-63e02fa6b6a2 -->

The operator must ensure the `RateLimits` allow for cooling down the required amount, keyed on `LIMIT_SUSDE_COOLDOWN`, and the rate limit is decreased before the cooldown is initiated.

`        _rateLimited(LIMIT_SUSDE_COOLDOWN, usdeAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.5.3 - Cooldown Assets On sUSDe [Core]  <!-- UUID: 3b6f10ae-e696-4c3c-9097-e9a9e7765dec -->

The operator must call the `MainnetController` contract to `cooldownAssets` on `susde` for the `usdeAmount`. The call is executed against the sUSDe vault through `proxy.doCall`, starting the cooldown period after which the specified `usdeAmount` of USDe can be unstaked to the Grove ALM Proxy.

`        proxy.doCall(
            address(susde),
            abi.encodeCall(susde.cooldownAssets, (usdeAmount))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6 - Cooldown sUSDe Shares [Core]  <!-- UUID: f167892c-c613-4550-aa2e-2c74e94ad097 -->

The documents herein define the steps for an operator to `cooldownSharesSUSDe`, initiating a cooldown on a specified amount of sUSDe shares held by the Grove ALM Proxy and returning the resulting amount of USDe assets to be received once the cooldown period elapses.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.1 - Relayer Role [Core]  <!-- UUID: 7e85c9ff-3548-4a98-8d86-71b6fae340d8 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownSharesSUSDe`, which is enforced by the `_checkRole` check at the start of the function.

`function cooldownSharesSUSDe(uint256 susdeAmount)
        external
        returns (uint256 cooldownAmount)
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.2 - Cooldown Shares On sUSDe [Core]  <!-- UUID: 11f21172-0294-4c61-8234-562b63aa5681 -->

The operator must call the `MainnetController` contract to `cooldownShares` on `susde` for the `susdeAmount`. The call is executed against the sUSDe vault through `proxy.doCall`, and the returned `cooldownAmount` of USDe assets is decoded from the result.

`        cooldownAmount = abi.decode(
            proxy.doCall(
                address(susde),
                abi.encodeCall(susde.cooldownShares, (susdeAmount))
            ),
            (uint256)
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.6.3 - Check RateLimits [Core]  <!-- UUID: 42ac9925-cdd6-4c01-b9c7-ab8ccbedd8f4 -->

The operator must ensure the `RateLimits` allow for the cooldown. Because the resulting `cooldownAmount` of USDe is only known after the cooldown is initiated, the rate limit keyed on `LIMIT_SUSDE_COOLDOWN` is decreased at the end of the function using the resulting `cooldownAmount`.

`        rateLimits.triggerRateLimitDecrease(LIMIT_SUSDE_COOLDOWN, cooldownAmount);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7 - Unstake sUSDe [Core]  <!-- UUID: 42db9403-b5ce-42f1-bba2-f562a03ec86d -->

The documents herein define the steps for an operator to `unstakeSUSDe`, withdrawing the USDe assets to the Grove ALM Proxy once the sUSDe cooldown period has elapsed.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7.1 - Relayer Role [Core]  <!-- UUID: 10230cbb-8a2a-47c5-919c-93716d0ae170 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `unstakeSUSDe`, which is enforced by the `_checkRole` check at the start of the function.

`function unstakeSUSDe() external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.10.7.2 - Unstake To ALM Proxy [Core]  <!-- UUID: da4abe97-3014-4a48-ad17-7beb0e12b451 -->

The operator must call the `MainnetController` contract to `unstake` from `susde` to the `proxy`. The call is executed against the sUSDe vault through `proxy.doCall`, withdrawing the USDe assets to the Grove ALM Proxy once the cooldown period has elapsed.

`        proxy.doCall(
            address(susde),
            abi.encodeCall(susde.unstake, (address(proxy)))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11 - Pendle Functions [Core]  <!-- UUID: fdfa763a-137a-4a39-8ff7-3f0b6d6391d7 -->

The documents herein define the operations performed by the Grove Liquidity Layer to redeem expired Pendle Principal Tokens (PT) for their underlying token.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1 - Redeem Pendle PT [Core]  <!-- UUID: ed3e546f-88a2-4a74-b768-58c64a9e22c8 -->

The documents herein define a series of operations for an operator to `redeem` expired Pendle Principal Tokens (PT) for their underlying token through the `PENDLE_ROUTER`.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.1 - Relayer Role [Core]  <!-- UUID: 3cbd5aaf-8ff5-4009-884a-71d776c3769a -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `redeemPendlePT`; the function calls `_checkRole(RELAYER)` before delegating the redemption logic to `PendleLib`.

`function redeemPendlePT(address pendleMarket, uint256 pyAmountIn, uint256 minAmountOut)
        external`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.2 - Validate Market Expiry And Minimum Output [Core]  <!-- UUID: 3970df59-0e49-415c-ac0f-504f92d533f8 -->

The operator must ensure the Pendle market has reached expiry and that a non-zero `minAmountOut` was provided. `PendleLib` reverts with `market-not-expired` if `pendleMarket.isExpired()` is false, and with `min-amount-out-not-set` if `minAmountOut` is zero.

`{
        require(params.pendleMarket.isExpired(), "PendleLib/market-not-expired");
        require(params.minAmountOut != 0,        "PendleLib/min-amount-out-not-set");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.3 - Read Market Tokens And Compute Minimum Output [Core]  <!-- UUID: 1489f2dc-bc7b-4f73-a9e2-ba7a2e08a338 -->

The operator must read the market's `SY`, `PT`, and `YT` tokens, resolve the underlying `tokenOut` via `ISY(sy).yieldToken()`, and derive the expected minimum output from the current PY index using `IYT(yt).pyIndexCurrent()`. A rounding buffer of `5` is subtracted from `minTokenOut` to avoid reverts caused by potential rounding errors.

`        (address sy, address pt, address yt) = params.pendleMarket.readTokens();

        address tokenOut = ISY(sy).yieldToken();

        uint256 pyIndexCurrent = IYT(yt).pyIndexCurrent();

        uint256 minTokenOut = params.pyAmountIn * 1e18 / pyIndexCurrent - 5;`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.4 - Approve Router Spend And Snapshot Balance [Core]  <!-- UUID: df5d543b-00e3-4c7c-bd85-4c766025ee32 -->

The operator must approve the `PENDLE_ROUTER` to spend `pyAmountIn` of the `PT` token on behalf of the `proxy`, then record the `proxy`'s `tokenOut` balance before the redemption so the amount received can be measured afterwards.

`        ERC20Lib.approve(params.proxy, pt, params.pendleRouter, params.pyAmountIn);

        uint256 tokenOutAmountBefore = IERC20(tokenOut).balanceOf(address(params.proxy));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.5 - Redeem PT To Token [Core]  <!-- UUID: 3b8311b9-a8db-45a0-9fd3-84970c0eb246 -->

The operator must redeem the principal tokens for the underlying `tokenOut` by calling `redeemPyToToken` on the `PENDLE_ROUTER` through the `proxy`, sending the proceeds to the `proxy`.

`        params.proxy.doCall(
            params.pendleRouter,
            abi.encodeCall(
                IPendleRouter.redeemPyToToken, (
                    address(params.proxy),
                    yt,
                    params.pyAmountIn,
                    createSimpleTokenOutput(tokenOut, minTokenOut)
                )
            )
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.6 - Verify Amount Received [Core]  <!-- UUID: 267a7de0-dd91-4cbc-bbd8-22b8de98067e -->

The operator must compute the amount of `tokenOut` actually received by the `proxy` and ensure it meets the caller's `minAmountOut`. `PendleLib` reverts with `min-amount-not-met` if the received amount is below `minAmountOut`.

`        uint256 totalTokenOutAmount = IERC20(tokenOut).balanceOf(address(params.proxy)) - tokenOutAmountBefore;

        require(totalTokenOutAmount >= params.minAmountOut, "PendleLib/min-amount-not-met");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1.7 - Decrease RateLimit [Core]  <!-- UUID: 8bfd464e-eb67-48bf-8a83-ae10fecb783d -->

The operator must decrease the rate limit after the redemption by the amount of `tokenOut` received, using a key derived from `LIMIT_PENDLE_PT_REDEEM` and the `pendleMarket` address. Note that `redeemPendlePT` must not be used for markets with non-standard SYs (such as ePENDLE, mPENDLE, or aTokens like aUSDC and aUSDT) without additional testing targeting each such market.

`        params.rateLimits.triggerRateLimitDecrease(
            RateLimitHelpers.makeAssetKey(params.rateLimitId, address(params.pendleMarket)),
            totalTokenOutAmount
        );

    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12 - DAI-USDS Migrator Functions [Core]  <!-- UUID: ed0ce400-13c0-4456-aeae-a14c8545786d -->

The documents herein define the swap operations performed by the Grove Liquidity Layer through the `daiUsds` migrator.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1 - Swap USDS To DAI [Core]  <!-- UUID: 243aebab-95da-45c5-a33b-7291973b7c6f -->

The documents herein define a series of operations for an operator to `swap` USDS to DAI through the `daiUsds` migrator.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.1 - Relayer Role [Core]  <!-- UUID: b0e0d442-ee24-4916-8c95-fe96ff066808 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapUSDSToDAI`.

`function swapUSDSToDAI(uint256 usdsAmount)
        external
        onlyRole(RELAYER)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.2 - Approve USDS To Migrator [Core]  <!-- UUID: c4ca6c96-3daf-4a05-b19b-2bce3243a735 -->

The operator must approve the `daiUsds` migrator to spend the `usdsAmount` on behalf of the `proxy`. `daiUsds` is a contract that facilitates a 1:1 swap between USDS and DAI. This assumes the `proxy` holds enough USDS.

`    {
        // Approve USDS to DaiUsds migrator from the proxy (assumes the proxy has enough USDS)
        ERC20Lib.approve(proxy, address(usds), address(daiUsds), usdsAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.1.3 - Swap USDS To DAI [Core]  <!-- UUID: 904ecbac-b3a5-4c79-8afc-a9218c3b38e4 -->

The operator must swap USDS to DAI. USDS is swapped to DAI in a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`        // Swap USDS to DAI 1:1
        proxy.doCall(
            address(daiUsds),
            abi.encodeCall(daiUsds.usdsToDai, (address(proxy), usdsAmount))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2 - Swap DAI To USDS [Core]  <!-- UUID: 8fc8d158-5605-4889-ba49-4685035cc112 -->

The documents herein define a series of operations for an operator to `swap` DAI to USDS through the `daiUsds` migrator.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.1 - Relayer Role [Core]  <!-- UUID: 4c6fb82f-4c19-453a-a91c-f96a5979c39c -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `swapDAIToUSDS`.

`function swapDAIToUSDS(uint256 daiAmount)
        external
        onlyRole(RELAYER)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.2 - Approve DAI To Migrator [Core]  <!-- UUID: e549765f-8494-4842-875d-a206131c9daa -->

The operator must approve the `daiUsds` migrator to spend the `daiAmount` on behalf of the `proxy`. `daiUsds` is a contract that facilitates a 1:1 swap between DAI and USDS. This assumes the `proxy` holds enough DAI.

`    {
        // Approve DAI to DaiUsds migrator from the proxy (assumes the proxy has enough DAI)
        ERC20Lib.approve(proxy, address(dai), address(daiUsds), daiAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.12.2.3 - Swap DAI To USDS [Core]  <!-- UUID: 30349bb4-c5b0-44e0-b60c-0d83f29fa297 -->

The operator must swap DAI to USDS. DAI is swapped to USDS in a 1:1 ratio through the `daiUsds` contract and sent back to the `proxy`.

`        // Swap DAI to USDS 1:1
        proxy.doCall(
            address(daiUsds),
            abi.encodeCall(daiUsds.daiToUsds, (address(proxy), daiAmount))
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13 - LayerZero Bridging Functions [Core]  <!-- UUID: 3362e36b-56db-4a73-a877-26e78c5d086c -->

The documents herein define the operations performed by the Grove Liquidity Layer to bridge tokens cross-chain through LayerZero OFTs from the Grove ALM Proxy to a recipient on a destination endpoint.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1 - Transfer Token LayerZero [Core]  <!-- UUID: 8d26ccbe-5b1f-482e-a22d-6492f4dbec0b -->

The documents herein define the steps for an operator to `transferTokenLayerZero`, bridging an OFT `token` cross-chain from the Grove ALM Proxy to the recipient configured for the destination endpoint.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.1 - Relayer Role [Core]  <!-- UUID: 123fc395-d16c-431e-8d09-8bbd78b0e405 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferTokenLayerZero`. The function is `payable` so that the operator can supply the native gas required to pay the LayerZero messaging fee.

`    function transferTokenLayerZero(
        address oftAddress,
        uint256 amount,
        uint32  destinationEndpointId
    )
        external payable
    {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.2 - Check RateLimits [Core]  <!-- UUID: 1224be29-4148-4720-919d-8d15d519763d -->

The operator must ensure the `RateLimits` allow for transferring the required `amount`. The rate limit is keyed on the `oftAddress` and `destinationEndpointId` pair through `LIMIT_LAYERZERO_TRANSFER`. Note that this function was deployed without integration testing, so its rate limit must be kept at `0` until the LayerZero dependencies are live and the functionality has been thoroughly integration tested.

`        _rateLimited(
            keccak256(abi.encode(LIMIT_LAYERZERO_TRANSFER, oftAddress, destinationEndpointId)),
            amount
        );`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.3 - Approve Token Transfer [Core]  <!-- UUID: 37850859-598b-4a40-9f29-5a2622683fad -->

The operator must, when the OFT reports that `approvalRequired` is `true`, approve the `oftAddress` to spend the `amount` of the underlying `token` on behalf of the Grove ALM Proxy through `ERC20Lib.approve`. The approval is skipped for OFT implementations that do not require it.

`        // NOTE: Full integration testing of this logic is not possible without OFTs with
        //       approvalRequired == false. Add integration testing for this case before
        //       using in production.
        if (ILayerZero(oftAddress).approvalRequired()) {
            ERC20Lib.approve(proxy, ILayerZero(oftAddress).token(), oftAddress, amount);
        }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.4 - Build Send Parameters [Core]  <!-- UUID: fca03c59-2f40-4ac6-8ea6-3f0b89b7660e -->

The operator must build the LayerZero `SendParam`. The executor gas limit is set through `OptionsBuilder` with `addExecutorLzReceiveOption`, `dstEid` is set to the `destinationEndpointId`, the recipient is read from `layerZeroRecipients` for that endpoint, `amountLD` is set to the `amount`, and `minAmountLD` is initialized to `0` with empty `composeMsg` and `oftCmd`.

`        bytes memory options = OptionsBuilder.newOptions().addExecutorLzReceiveOption(200_000, 0);

        SendParam memory sendParams = SendParam({
            dstEid       : destinationEndpointId,
            to           : layerZeroRecipients[destinationEndpointId],
            amountLD     : amount,
            minAmountLD  : 0,
            extraOptions : options,
            composeMsg   : "",
            oftCmd       : ""
        });`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.5 - Quote The Transfer [Core]  <!-- UUID: c513c254-32a7-4870-98f2-1b9f0d43b263 -->

The operator must call `quoteOFT` to determine the `amountReceivedLD` on the destination chain and set `sendParams.minAmountLD` to that value, then call `quoteSend` to obtain the native `MessagingFee` required to deliver the message.

`        // Query the min amount received on the destination chain and set it.
        ( ,, OFTReceipt memory receipt ) = ILayerZero(oftAddress).quoteOFT(sendParams);
        sendParams.minAmountLD = receipt.amountReceivedLD;

        MessagingFee memory fee = ILayerZero(oftAddress).quoteSend(sendParams, false);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.6 - Execute Cross-Chain Transfer [Core]  <!-- UUID: 46731c27-e45f-4ccf-8f1b-199141570bff -->

The operator must call the `MainnetController` contract to execute the transfer. The `send` call is forwarded to the `oftAddress` through `proxy.doCallWithValue`, passing `fee.nativeFee` as the native value, with the Grove ALM Proxy set as the refund address.

`        proxy.doCallWithValue{value: fee.nativeFee}(
            oftAddress,
            abi.encodeCall(ILayerZero.send, (sendParams, fee, address(proxy))),
            fee.nativeFee
        );
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.14 - Merkl Functions [Core]  <!-- UUID: 8d3cf392-9a3c-4a7c-963d-3f37484482f3 -->

The documents herein define the operations performed by the Grove Liquidity Layer to manage the operators authorized to claim Merkl rewards on behalf of the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1 - Toggle Operator Merkl [Core]  <!-- UUID: b21fe176-bcb6-4f59-97c9-54b28331394b -->

The documents herein define the steps for an operator to `toggleOperatorMerkl`, authorizing or deauthorizing an `operator` to claim Merkl rewards on behalf of the Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1.1 - Relayer Role [Core]  <!-- UUID: fbd75855-2a62-4572-bb63-f0907343f033 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `toggleOperatorMerkl`.

`function toggleOperatorMerkl(address operator) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1.2 - Toggle Operator [Core]  <!-- UUID: 6dc805cb-36ca-4c2c-af85-4657fcf82d2d -->

The operator must toggle the authorization of the `operator` on the Merkl Distributor. This calls `toggleOperator` on the `MERKL_DISTRIBUTOR` through the `proxy` to authorize or deauthorize the `operator` to claim Merkl rewards on the `proxy`'s behalf.

`
        MerklLib.toggleOperator(MerklLib.MerklToggleOperatorParams({
            proxy       : proxy,
            distributor : Ethereum.MERKL_DISTRIBUTOR,
            operator    : operator
        }));
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15 - CCTP Bridging Functions [Core]  <!-- UUID: 5511c7f2-c2f6-471b-a797-4a232daf3c38 -->

The documents herein define the cross-chain bridging operations performed by the Grove Liquidity Layer through Circle's Cross-Chain Transfer Protocol (CCTP).

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1 - Transfer USDC To CCTP [Core]  <!-- UUID: e8a77685-3069-4888-8964-81fdc8f60a38 -->

The documents herein define a series of operations for an operator to `transfer` USDC through Circle's Cross-Chain Transfer Protocol (CCTP) to a `destinationDomain`.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.1 - Relayer Role [Core]  <!-- UUID: f0f317d1-5c78-4de8-956e-dba3a3256eff -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `transferUSDCToCCTP`.

`function transferUSDCToCCTP(uint256 usdcAmount, uint32 destinationDomain) external {
        _checkRole(RELAYER);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.2 - Check RateLimits [Core]  <!-- UUID: ccec5230-f1df-4dde-be4b-9f9a948d379d -->

The operator must ensure that `RateLimits` allows the transfer, both against the global `LIMIT_USDC_TO_CCTP` limit and the per-destination `LIMIT_USDC_TO_DOMAIN` limit for the target `destinationDomain`.

`        rateLimited(LIMIT_USDC_TO_CCTP, usdcAmount);
        rateLimited(makeDomainKey(LIMIT_USDC_TO_DOMAIN, destinationDomain), usdcAmount);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.3 - Check Domain Configuration [Core]  <!-- UUID: ffa66264-41fa-4425-9c01-155810c5b25d -->

The operator must ensure a `mintRecipient` has been configured for the target `destinationDomain`. If `mintRecipient` is zero the transfer reverts, as the destination domain has not been configured.

`        bytes32 mintRecipient = mintRecipients[destinationDomain];
        require(mintRecipient != 0, "CCTPLib/domain-not-configured");`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.4 - Approve Contract Spend [Core]  <!-- UUID: 6255c62f-5a22-4f7a-9ffe-e9d8353f83da -->

The operator must approve the `cctp` contract to spend the `usdcAmount` on behalf of the `proxy`, then read the per-message `burnLimit` from the CCTP local minter to determine whether the transfer must be split across multiple messages.

`        ERC20Lib.approve(proxy, address(usdc), address(cctp), usdcAmount);
        uint256 burnLimit = cctp.localMinter().burnLimitsPerMessage(address(usdc));`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.5 - Split Transfer Over Burn Limit [Core]  <!-- UUID: 7bba47ea-4bad-4223-bdd5-29a852402a92 -->

The operator must, while the remaining amount exceeds the `burnLimit`, initiate a CCTP transfer of `burnLimit` USDC per message and reduce the remaining amount by `burnLimit` on each iteration. Each transfer calls `depositForBurn` on `cctp` through the `proxy` with `destinationCaller` set to zero, `maxFee` of zero, and a `minFinalityThreshold` of 2000, and emits `CCTPTransferInitiated`.

`        while (usdcAmount > burnLimit) {
            _initiateCCTPTransfer(burnLimit, destinationDomain, mintRecipient);
            usdcAmount -= burnLimit;
        }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1.6 - Transfer Remaining Amount [Core]  <!-- UUID: 2a7cbcdc-de92-4c4e-ac2b-4277af33d578 -->

The operator must transfer the remaining amount, which is at or below the `burnLimit`, by calling `depositForBurn` on `cctp` through the `proxy` with `destinationCaller` set to zero, `maxFee` of zero, and a `minFinalityThreshold` of 2000, then emit `CCTPTransferInitiated` to the blockchain logs.

`        if (usdcAmount > 0) {
            _initiateCCTPTransfer(usdcAmount, destinationDomain, mintRecipient);
        }
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.3 - Freezer Functions [Core]  <!-- UUID: 9e827633-665c-4ed5-a1f9-d6dfce07cc56 -->

The documents herein define the operations performed by the freezer role (see Freezer Role) within the `MainnetController` contract.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.3.1 - Remove Relayer [Core]  <!-- UUID: a9be43b5-8ddd-4b8e-b64c-c93f05a13589 -->

The documents herein define the process to remove the `RELAYER` role from a relayer address. This is used to revoke a relayer's ability to operate the `MainnetController` contract.

###### A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.1 - Freezer Role [Core]  <!-- UUID: 838e55d5-6673-42c0-a590-c0fb4501e078 -->

The operator must ensure they are working as a `FREEZER`. Only the `FREEZER` role is allowed to `removeRelayer`.

`function removeRelayer(address relayer)
        external
        onlyRole(FREEZER)`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.2 - Revoke Relayer Role [Core]  <!-- UUID: fae744c3-d737-44c3-bc85-3cb14b9dc031 -->

The operator must revoke the `RELAYER` role from the relayer address being removed so that it can no longer operate the contract.

`{
        _revokeRole(RELAYER, relayer);`

###### A.6.1.1.2.2.6.1.2.2.1.2.1.3.1.3 - Emit Event To Logs [Core]  <!-- UUID: 87272b12-7a1d-4aef-963c-4c45b514cf6d -->

The operator must emit the event to the blockchain logs.

`        emit RelayerRemoved(relayer);
    }`

###### A.6.1.1.2.2.6.1.2.2.1.2.2 - Diamond PAU Controller Functions [Core]  <!-- UUID: 6c060c28-5619-48f4-8536-b74c153b1641 -->

The Diamond PAU Controller functions for the Grove Liquidity Layer are the shared Diamond PAU Controller functions specified in [A.2.2.10.1.1.1.2.5.2 - Diamond PAU Controller Functions](5e941add-bf8d-4623-95a1-69795e7f7034). The Facets used by the Grove Liquidity Layer are specified in the documents herein.

###### A.6.1.1.2.2.6.1.2.2.1.2.2.1 - Basin Facet [Core]  <!-- UUID: 3e54ecce-73fc-4f85-be3c-0c89d3d005d2 -->

The Grove Liquidity Layer uses the Basin Facet ([A.2.2.10.1.1.1.2.3.2.2 - Basin Facet](d9cbf883-119e-403d-8efa-125997cd8897)) to deposit assets into and withdraw them from Basins.

###### A.6.1.1.2.2.6.1.2.2.1.2.2.2 - USDS Facet [Core]  <!-- UUID: bdf5ef63-d436-4ffb-bf37-2c1790d1a68d -->

The Grove Liquidity Layer uses the USDS Facet ([A.2.2.10.1.1.1.2.3.2.22 - USDS Facet](917e1162-3c06-4508-b0e9-02c5eefc1346)) to mint and burn USDS through the allocator vault.

###### A.6.1.1.2.2.6.1.2.2.1.2.2.3 - PSM Facet [Core]  <!-- UUID: 0cf2ffe0-cb0b-4c3c-bd11-349cad3d4c98 -->

The Grove Liquidity Layer uses the PSM Facet ([A.2.2.10.1.1.1.2.3.2.16 - PSM Facet](afa3da61-c32a-4efd-900b-16e1c262c842)) to swap between USDS and USDC via DAI, through the DAI-USDS migrator and the PSM. These swaps require the ALM Proxy to be whitelisted on the Lite PSM, as specified in [A.6.1.1.2.2.6.1.2.1.1.4.2 - Whitelisting Of ALM Proxy](6823cc5a-6667-4754-a030-9ac7126b006e).

###### A.6.1.1.2.2.6.1.2.2.1.2.2.4 - Uniswap v3 Facet [Core]  <!-- UUID: 5b6d7110-3662-4ee5-a339-43e6bb8e4517 -->

The Grove Liquidity Layer uses the Uniswap v3 Facet ([A.2.2.10.1.1.1.2.3.2.20 - Uniswap v3 Facet](b808a829-2f31-42f1-ac9f-6801d3eb8437)) to add liquidity to, remove liquidity from, and swap through a Uniswap v3 pool.

###### A.6.1.1.2.2.6.1.2.2.1.2.3 - Monolithic Foreign Controller Contract Functions [Core]  <!-- UUID: a3d8a2af-90e1-40a8-8573-48a84954ea54 -->

The documents herein define the functions controlled by the `ForeignController` contract for Grove Liquidity Layer operations on foreign chains.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1 - Admin Functions [Core]  <!-- UUID: 759288c4-873a-4e78-a3c2-eb99b3b042f0 -->

The documents herein define the operations performed by the `DEFAULT_ADMIN_ROLE` within the `ForeignController` contract.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.1 - Set The Mint Recipient [Core]  <!-- UUID: 440ae811-4e1f-4f07-9c04-dc6bb32144ae -->

The process for setting the mint recipient through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.1 - Set The Mint Recipient](c4c09a75-ef25-4aa7-825a-73d386cbc87f).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.2 - Set The LayerZero Recipient [Core]  <!-- UUID: 369d145a-04e6-4ab0-a388-a83c870c76f2 -->

The process for setting the LayerZero recipient through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.2 - Set The LayerZero Recipient](cd46a4fa-1281-4e3e-9ac5-0ca7f2160ec2).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.3 - Set The Max Slippage [Core]  <!-- UUID: d5878d00-dd33-4ff8-8e2d-25d0ec6d681e -->

The process for setting the max slippage through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.3 - Set The Max Slippage](7aedf5dd-c454-4eb3-b97c-63d810f1c616).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.4 - Set The Centrifuge Recipient [Core]  <!-- UUID: 6660a3cb-fefd-41aa-b882-59081e5dbd32 -->

The process for setting the Centrifuge recipient through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.8 - Set The Centrifuge Recipient](869c8941-5660-4d6f-b5ab-c464e444b5b6).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.5 - Set The Uniswap V3 Pool Max Tick Delta [Core]  <!-- UUID: 62d94c33-2f49-4e83-98e3-ae06e84aadf4 -->

The process for setting the Uniswap V3 pool max tick delta through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.4 - Set The Uniswap V3 Pool Max Tick Delta](bf5c8eae-451a-4a1b-9b53-bd5deefd9c21).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.6 - Set The Uniswap V3 Add Liquidity Lower Tick Bound [Core]  <!-- UUID: 0ca50f1e-58f2-456b-93bb-127bd5d683e4 -->

The process for setting the Uniswap V3 add liquidity lower tick bound through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.5 - Set The Uniswap V3 Add Liquidity Lower Tick Bound](2f4ebdcc-b203-410d-aaab-19b395c2368c).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.7 - Set The Uniswap V3 Add Liquidity Upper Tick Bound [Core]  <!-- UUID: deec4da4-307d-4b73-8714-f3886010e604 -->

The process for setting the Uniswap V3 add liquidity upper tick bound through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.6 - Set The Uniswap V3 Add Liquidity Upper Tick Bound](dc3dd2d9-4b0a-4958-b9b6-6b2b9e91525b).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.8 - Set The Uniswap V3 TWAP Seconds Ago [Core]  <!-- UUID: ec0865cc-f3ab-44c7-859d-c222431bba98 -->

The process for setting the Uniswap V3 TWAP seconds ago through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.7 - Set The Uniswap V3 TWAP Seconds Ago](cfdaafcb-d91d-4c6e-8af5-9d21fa6f4033).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.9 - Set The Merkl Distributor [Core]  <!-- UUID: 5f279a4e-5c7f-4b59-aef0-2dffe4666b67 -->

The document herein defines the process to set the `merklDistributor` address used by the `ForeignController` contract to claim Merkl rewards. Only the `DEFAULT_ADMIN_ROLE` is allowed to call `setMerklDistributor`, which updates the `merklDistributor` state variable and emits the `MerklDistributorSet` event.

`function setMerklDistributor(address merklDistributor_) external onlyRole(DEFAULT_ADMIN_ROLE)`

###### A.6.1.1.2.2.6.1.2.2.1.2.3.1.10 - Set The Max Exchange Rate [Core]  <!-- UUID: 8d3ab71f-4305-4a31-a9e9-90aa2aa52af5 -->

The process for setting the max exchange rate through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.1.9 - Set The Max Exchange Rate](662ec211-4b25-43db-aca4-48acb08090ec).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.2 - Freezer Functions [Core]  <!-- UUID: 3a26c55a-89bb-40d2-af02-84799bdfc85d -->

The documents herein define the operations performed by the freezer role (see Freezer Role) within the `ForeignController` contract.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.2.1 - Remove Relayer [Core]  <!-- UUID: 4312498b-f4e3-4160-8f92-082820058c35 -->

The process for removing a relayer through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.3.1 - Remove Relayer](a9be43b5-8ddd-4b8e-b64c-c93f05a13589).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3 - Relayer Functions [Core]  <!-- UUID: c4d4f667-5c7a-4b2b-8427-272dc17505c0 -->

The documents herein define the operations performed by the `RELAYER` role within the `ForeignController` contract.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.1 - PSM Functions [Core]  <!-- UUID: 0054112d-5f25-4108-92f1-a008b8673d1f -->

The documents herein define the deposit and withdrawal operations performed by the Grove Liquidity Layer in the PSM.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.1.1 - Deposit To PSM [Core]  <!-- UUID: 41cdf6f8-78c7-4aa0-8675-060fecf24d42 -->

The operator, acting as a Relayer, calls `depositPSM` to deposit `amount` of `asset` from the ALM Proxy into the PSM, receiving the corresponding PSM `shares` in return. The function approves the PSM to spend the `asset` from the ALM Proxy and then deposits it, crediting the shares to the ALM Proxy. Only an address holding the `RELAYER` role may call this function, and the deposit is rate limited per asset by `LIMIT_PSM_DEPOSIT`.

`function depositPSM(address asset, uint256 amount)
        external
        onlyRole(RELAYER)
        rateLimitedAsset(LIMIT_PSM_DEPOSIT, asset, amount)
        returns (uint256 shares)`

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.1.2 - Withdraw From PSM [Core]  <!-- UUID: 742945a7-1031-483f-873c-6bd229b58b4c -->

The operator, acting as a Relayer, calls `withdrawPSM` to withdraw up to `maxAmount` of `asset` from the PSM to the ALM Proxy, returning the amount actually withdrawn as `assetsWithdrawn`. The withdrawn amount is then applied against the `LIMIT_PSM_WITHDRAW` rate limit for the asset. Only an address holding the `RELAYER` role may call this function.

`function withdrawPSM(address asset, uint256 maxAmount)
        external
        onlyRole(RELAYER)
        returns (uint256 assetsWithdrawn)`

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.2 - CCTP Bridging Functions [Core]  <!-- UUID: 57afa40f-6653-46fa-b25e-65ff646b4886 -->

The documents herein define the CCTP bridging operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.2.1 - Transfer USDC To CCTP [Core]  <!-- UUID: 06d67a94-7d76-4c13-8952-0d3b9813e06e -->

The process for transferring USDC to CCTP through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.15.1 - Transfer USDC To CCTP](e8a77685-3069-4888-8964-81fdc8f60a38).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.3 - LayerZero Bridging Functions [Core]  <!-- UUID: 2ca22d56-951f-4932-a549-c5e3a1be124c -->

The documents herein define the LayerZero bridging operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.3.1 - Transfer Token LayerZero [Core]  <!-- UUID: 2e3ddf0c-8e7b-4d3f-9661-6b3132ef0e8d -->

The process for transferring a token through LayerZero through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1 - Transfer Token LayerZero](8d26ccbe-5b1f-482e-a22d-6492f4dbec0b).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.4 - ERC-20 Functions [Core]  <!-- UUID: 8f5e1531-e978-40f3-9c74-9fbb61b9f756 -->

The documents herein define the ERC-20 token operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.4.1 - Transfer Asset [Core]  <!-- UUID: 1781b7a1-6801-40b9-b11e-696fb161da01 -->

The process for transferring an asset through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.4.1 - Transfer Asset](daa8abb8-db47-4dec-845f-fefbd6b8835a).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.5 - ERC-4626 Functions [Core]  <!-- UUID: 699fd226-7b82-473e-9a69-f5a949274e77 -->

The documents herein define the ERC-4626 token operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.5.1 - General Deposit to ERC-4626 Tokens Procedure [Core]  <!-- UUID: fae8a2cd-0ae7-4c80-838d-48d11b9451f0 -->

The process for depositing into ERC-4626 tokens through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.1 - Deposit To ERC-4626 Vault](4876005c-31a8-4be8-8133-e239bd0ac53b).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.5.2 - General Withdraw from ERC-4626 Tokens Procedure [Core]  <!-- UUID: d275f766-a5d6-4356-a5b8-55ae17d651e0 -->

The process for withdrawing from ERC-4626 tokens through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2 - Withdraw From ERC-4626 Vault](7b560160-e427-45a2-a3ac-3c23cf6fe943).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.5.3 - General Redeem from ERC-4626 Tokens Procedure [Core]  <!-- UUID: 5028d29a-e1cb-4340-944c-2026e25416b6 -->

The process for redeeming from ERC-4626 tokens through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3 - Redeem From ERC-4626 Vault](7e90e505-42b9-474d-9cc5-9b4da6af7375).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.6 - ERC-7540 Functions [Core]  <!-- UUID: 87689fcb-ede5-4ae8-9060-5983ab1ed637 -->

The documents herein define the ERC-7540 vault operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.6.1 - Request Deposit To ERC-7540 Vault [Core]  <!-- UUID: 29c2ebcf-0bf9-49ee-a559-2d8220be5ecb -->

The process for requesting a deposit to an ERC-7540 vault through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.1 - Request Deposit To ERC-7540 Vault](f305d6fb-d948-4890-ad9f-d5ad6197674d).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.6.2 - Claim Deposit From ERC-7540 Vault [Core]  <!-- UUID: 282ef2e8-780c-493d-a4dc-03ed32cf8b50 -->

The process for claiming a deposit from an ERC-7540 vault through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.2 - Claim Deposit From ERC-7540 Vault](1ea24541-a1ad-4b0f-bcee-2fc369d5b17b).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.6.3 - Request Redeem From ERC-7540 Vault [Core]  <!-- UUID: a282fc7f-5684-4779-be1b-341c8f3c799e -->

The process for requesting a redeem from an ERC-7540 vault through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.3 - Request Redeem From ERC-7540 Vault](01e72e75-9bde-4951-804e-1c422e2c1265).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.6.4 - Claim Redeem From ERC-7540 Vault [Core]  <!-- UUID: 96624d86-162e-4236-a5b2-5f6890d6cdcf -->

The process for claiming a redeem from an ERC-7540 vault through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.5.4 - Claim Redeem From ERC-7540 Vault](ecec5578-ccb1-440e-bad6-ab5c5918becd).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.7 - Centrifuge Functions [Core]  <!-- UUID: 427d7158-2f11-489f-a0d8-0b8496605ccc -->

The documents herein define the Centrifuge operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.1 - Cancel Centrifuge Deposit Request [Core]  <!-- UUID: d9083457-a8d5-4dc1-9a47-afd68fdb8f9c -->

The process for cancelling a Centrifuge deposit request through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.1 - Cancel Centrifuge Deposit Request](70b5154e-16a4-4bfc-abe4-1b338da9d155).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.2 - Claim Centrifuge Cancel Deposit Request [Core]  <!-- UUID: 3194ca6c-7b3d-472a-ad73-97597133a089 -->

The process for claiming a Centrifuge cancel deposit request through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.2 - Claim Centrifuge Cancel Deposit Request](157f11ce-0ac9-4ac4-98c8-c6206a9c57e6).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.3 - Cancel Centrifuge Redeem Request [Core]  <!-- UUID: c8a6437f-812f-4d24-b397-8984cf1f872e -->

The process for cancelling a Centrifuge redeem request through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.3 - Cancel Centrifuge Redeem Request](efdae580-028a-4fbd-b737-2f755cd2f0b8).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.4 - Claim Centrifuge Cancel Redeem Request [Core]  <!-- UUID: ec9466c3-4396-4e28-9c3e-135579ca9745 -->

The process for claiming a Centrifuge cancel redeem request through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.4 - Claim Centrifuge Cancel Redeem Request](42d9e84a-725f-4d86-b5f2-9b36d2cbe3fd).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.7.5 - Transfer Shares Centrifuge [Core]  <!-- UUID: 3ad55b8f-31cc-4263-b657-56ade7766e04 -->

The process for transferring shares through Centrifuge through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.6.5 - Transfer Shares Centrifuge](c7ede989-e153-4593-b428-2787f5daaad9).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.8 - Aave Functions [Core]  <!-- UUID: ea576bab-e435-4243-9d47-7851c497495a -->

The documents herein define the Aave operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.8.1 - Deposit Into Aave [Core]  <!-- UUID: 05f60233-b2dd-47af-8552-146277184b8e -->

The process for depositing into Aave through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.1 - Deposit Into Aave](c159a99f-da73-477e-8052-f62b78b7b93e).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.8.2 - Withdraw From Aave [Core]  <!-- UUID: d58c74ce-d55e-45da-8254-e64b4657ed3c -->

The process for withdrawing from Aave through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.7.2 - Withdraw From Aave](793e928c-9b1f-480f-ab56-1b19f9e5c60d).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.9 - Curve Functions [Core]  <!-- UUID: bbbe257d-62dc-4e89-ac0a-2d05db059d97 -->

The documents herein define the Curve operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.9.1 - Swap On Curve [Core]  <!-- UUID: b81c3c6a-3fc7-4175-b9e7-f49e7099eda8 -->

The process for swapping on Curve through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.1 - Swap On Curve](fce783bb-d1b9-4b5e-9577-5149dc494af4).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.9.2 - Add Liquidity On Curve [Core]  <!-- UUID: 8d3457b4-a99e-4301-a415-c65b384ecc8f -->

The process for adding liquidity on Curve through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.2 - Add Liquidity On Curve](69c7bee3-40d6-449f-97c2-db591e5fb831).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.9.3 - Remove Liquidity On Curve [Core]  <!-- UUID: 0fb203c8-a2f9-43b5-b0dc-90290401d385 -->

The process for removing liquidity on Curve through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.8.3 - Remove Liquidity On Curve](7f63d8d5-5111-48e1-8d33-071bf2de6a30).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.10 - Merkl Functions [Core]  <!-- UUID: b429945d-f983-455d-bf39-c458aab9ccc3 -->

The documents herein define the Merkl operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.10.1 - Toggle Operator Merkl [Core]  <!-- UUID: 778e7737-d3ac-4bb2-9415-c369b2175d9c -->

The process for toggling an operator on Merkl through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.14.1 - Toggle Operator Merkl](b21fe176-bcb6-4f59-97c9-54b28331394b).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.11 - Pendle Functions [Core]  <!-- UUID: 553cd2d4-6026-4027-89b2-a93f62ce9e86 -->

The documents herein define the Pendle operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.11.1 - Redeem Pendle PT [Core]  <!-- UUID: a4b87e6f-f768-47e3-984d-aa4328846740 -->

The process for redeeming a Pendle PT through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.11.1 - Redeem Pendle PT](ed3e546f-88a2-4a74-b768-58c64a9e22c8).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.12 - Uniswap V3 Functions [Core]  <!-- UUID: b4d102d5-de11-4eb0-b1d0-05d942aa1027 -->

The documents herein define the Uniswap V3 operations performed by the Grove Liquidity Layer.

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.12.1 - Swap Tokens Through Uniswap V3 [Core]  <!-- UUID: 5debb9cf-608d-4899-8006-a8085249092e -->

The process for swapping tokens through Uniswap V3 through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.1 - Swap Tokens Through Uniswap V3](6dde4141-4930-4b59-bd78-ead1c3568c5d).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.12.2 - Add Liquidity To Uniswap V3 [Core]  <!-- UUID: ea4269f3-de42-4b27-8041-e48b85282664 -->

The process for adding liquidity to Uniswap V3 through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.2 - Add Liquidity To Uniswap V3](222d77a8-3cd1-46da-a720-1c474b760cfa).

###### A.6.1.1.2.2.6.1.2.2.1.2.3.3.12.3 - Remove Liquidity From Uniswap V3 [Core]  <!-- UUID: ae1fb5ac-9be7-4b42-a883-3417b8988ce5 -->

The process for removing liquidity from Uniswap V3 through the Foreign Controller contract is the same as through the Monolithic Mainnet Controller contract, as specified in [A.6.1.1.2.2.6.1.2.2.1.2.1.2.9.3 - Remove Liquidity From Uniswap V3](2ed22524-d397-4239-bc35-d4c2e13bf0c2).

###### A.6.1.1.2.2.6.1.2.2.1.3 - Rate Limit Management [Core]  <!-- UUID: 873c16ce-2d4d-4d10-bb97-fb1634114311 -->

The documents herein define the protocol for querying, setting, and adjusting `RateLimits` for Instances using their `RateLimitID`s. The ratelimits must be maintained in line with Grove’s strategy, market conditions, and security considerations.

###### A.6.1.1.2.2.6.1.2.2.1.3.1 - RateLimits Query [Core]  <!-- UUID: 5aea6114-5e7e-4bb1-86fa-c54135015397 -->

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

###### A.6.1.1.2.2.6.1.2.2.1.3.2 - Set RateLimit [Core]  <!-- UUID: aec1d10f-a5df-48d4-bbea-1b02c279c919 -->

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

###### A.6.1.1.2.2.6.1.2.2.1.3.3 - Set Unlimited RateLimit [Core]  <!-- UUID: 533d7220-75e3-43aa-8f1b-5512fdb9b828 -->

The following code sets out instructions for the operator to set an unlimited `RateLimit` for a specific key:

`function setUnlimitedRateLimitData(bytes32 key) external override {
        setRateLimitData(key, type(uint256).max, 0, type(uint256).max, block.timestamp);`

###### A.6.1.1.2.2.6.1.2.2.1.3.4 - Set Trigger For RateLimit Decrease [Core]  <!-- UUID: bc991d91-b79f-488c-b5d7-d632898c676e -->

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

###### A.6.1.1.2.2.6.1.2.2.1.3.5 - Set Trigger For RateLimit Increase [Core]  <!-- UUID: d1dbab82-8be1-41f4-a4a3-ddc3cd0a917c -->

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

###### A.6.1.1.2.2.6.1.2.2.1.4 - Instance Lifecycle Management [Core]  <!-- UUID: 7402f24b-ee72-4b19-9690-fceec083c7e9 -->

The documents herein define processes for invoking (onboarding) new Grove Liquidity Layer Instances and offboarding existing ones. This process will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.2.1.5 - Upgrading Controller [Core]  <!-- UUID: 3b49838e-423b-42b9-b3ca-2365e8e68725 -->

The documents herein define the process for deploying new Controller contracts. This process will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 7a8f34ed-ae14-4c93-94d2-9d08c4d18e82 -->

The documents herein define the process for non-routine ongoing management of the Grove Liquidity Layer and its active Instances.

###### A.6.1.1.2.2.6.1.2.2.3 - Emergency Protocol [Core]  <!-- UUID: 7ed2b9e8-1a29-421c-9186-d62ad6ffce50 -->

The documents herein define all the possible actions that can be taken in case of an emergency within Grove Liquidity Layer operations.

###### A.6.1.1.2.2.6.1.2.2.3.1 - Remove Compromised Relayer As Freezer [Core]  <!-- UUID: 53ff94d4-d7b5-4696-a66e-f6102deef3ac -->

In the event of a compromised Relayer, the `FREEZER_ROLE` can call the function to `removeRelayer` from the Controller contract. This function takes an address, and then the Freezer can remove the compromised Relayer, thereby preventing it from doing any harm to the system. The backstop relayer can then take over. This function should only be used if the keys to the relayer multisig have been leaked or compromised, and the relayer is now in the hands of an external bad actor.

`mainnetController.removeRelayer(compromisedRelayer)`

###### A.6.1.1.2.2.6.1.2.2.3.2 - Redeem All Mainnet Positions [Core]  <!-- UUID: 550a6aa3-88b8-4b5a-a614-e06099d6898a -->

The documents herein define the actions that should be performed by an operator if there is a need to recover the liquidity from Mainnet Protocols and centralize it in the Mainnet Grove ALM Proxy.

###### A.6.1.1.2.2.6.1.2.2.3.2.1 - ERC-4626 Withdrawal Action [Core]  <!-- UUID: 8991b422-bd6b-4ea1-b0b9-b787ee4b1000 -->

In order to withdraw all ERC-4626 balances, the operator must execute the following action:

`mainnetController.redeemERC4626(address(token), token.balanceOf(address(proxy)))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.2 - Withdraw From ERC-4626 Vault](7b560160-e427-45a2-a3ac-3c23cf6fe943) and [A.6.1.1.2.2.6.1.2.2.1.2.1.2.2.3 - Redeem From ERC-4626 Vault](7e90e505-42b9-474d-9cc5-9b4da6af7375).

###### A.6.1.1.2.2.6.1.2.2.3.3 - USDC to USDS Swap Action [Core]  <!-- UUID: 03c4e450-6fbf-4194-9620-43e253379aa9 -->

This document defines the action that should be performed by an operator if there is a need to centralize all recovered liquidity in USDS.

`mainnetController.swapUSDCToUSDS(usdc.balanceOf(address(proxy))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.2.2.6.1.2.2.1.2.1.2.3.2 - Swap USDC To USDS](1ec9a718-44f4-4ce9-97b3-bebeb207b280).

###### A.6.1.1.2.2.6.1.2.2.3.4 - USDS Burn Action [Core]  <!-- UUID: c0bc880f-818c-44cc-a02a-d66c01443a39 -->

This document defines the action that should be performed if there is a need to repay and then burn Grove’s USDS debt.

`mainnetController.burnUSDS(usds.balanceOf(address(proxy))
`
More detailed instructions on the code to execute this, see [A.6.1.1.2.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS](25706c25-2b74-486e-8234-c45f6630f379).

###### A.6.1.1.2.2.6.1.2.3 - Allocation Strategy [Core]  <!-- UUID: 0806984d-5799-4c19-8eda-d355bcc43524 -->

In the future, additional logic will be added herein regarding the strategy by which capital is allocated between different Instances of the Grove Liquidity Layer.

##### A.6.1.1.2.2.6.1.3 - Active Instances [Core]  <!-- UUID: 1f16c7b1-eddf-4106-85f7-3425bf67ef1e -->

The Instances of the Grove Liquidity Layer with `Active` Status are stored herein. The `RRC Framework Full Implementation` status defines whether the Instance Financial RRC is calculated based on a fully implemented risk model (see [A.3.2.1.1.4.3.1 - Fully Implemented Risk Models](419a1d00-fbae-4d26-bd47-8f57677d8001)) or a pending risk model (see [A.3.2.1.1.4.3.2 - Pending Risk Models](81ca88bf-3f6a-4d10-a3e2-d47cf6636d7d)). If the Instance Financial RRC is calculated based on a fully implemented risk model the status is `Covered`. If the Instance Financial RRC is calculated based on a pending risk model the status is `Pending`.

###### A.6.1.1.2.2.6.1.3.1 - Ethereum Mainnet Instances [Core]  <!-- UUID: 25fe7f58-6025-4498-8847-5ac6330e8b2c -->

The Ethereum Mainnet Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.2.2.6.1.3.1.1 - Centrifuge [Core]  <!-- UUID: 422e75c6-bb9e-4a2f-b58c-bfbd0ede789d -->

The Ethereum Mainnet Instances of the Centrifuge Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.1.1 - Ethereum Mainnet - Centrifuge JTRSY Instance Configuration Document [Core]  <!-- UUID: 292d1098-9fe4-481f-a3e7-72e345bdca81 -->

The documents herein contain the Instance Configuration Document for the Centrifuge JTRSY Instance.

###### A.6.1.1.2.2.6.1.3.1.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: b2981f26-c563-4014-8460-36b74905a2a9 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.1.1.2 - Parameters [Core]  <!-- UUID: 3609697d-1d35-4dbf-ab8e-fcebfbc258f4 -->

The documents herein define the parameters of the Centrifuge JTRSY Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: a43153dc-fe0a-49bc-84c7-1fd8fadf1c8e -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.1.1.2.1.1 - Network [Core]  <!-- UUID: 2c0d8ede-45bc-4e75-8931-5ddfccf24a02 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: ec81f2d8-5050-4b1b-9acf-bb25574c71c7 -->

Centrifuge

###### A.6.1.1.2.2.6.1.3.1.1.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 6213ce59-e16a-41be-9f80-7ba335c0dd7b -->

USDC

###### A.6.1.1.2.2.6.1.3.1.1.1.2.1.4 - Token [Core]  <!-- UUID: 38e94216-daa1-4e05-bb5f-66c282c19d46 -->

JTRSY

###### A.6.1.1.2.2.6.1.3.1.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 29fe2123-0565-4ba0-95d0-9de487877441 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 39cf2050-ef55-49d4-b59d-fc1b0a11ac59 -->

`0xFE6920eB6C421f1179cA8c8d4170530CDBdfd77A`

###### A.6.1.1.2.2.6.1.3.1.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: fbe40152-f7e6-4a4e-87ed-4e419687e40d -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 2ecfcbd7-953a-44f8-b964-083f238b2da9 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 44eccfe2-b96a-4b76-bd9d-9a28aee10fb7 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 9af18990-c582-46f9-a78e-0c4e4ce233fc -->

The inflow rate limits are:
- `maxAmount`: 500,000,000 USDC
- `slope`: 500,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: ad10bea9-b609-4be9-bce8-56aba87da4c9 -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 7d0e7474-55c1-46b8-b283-917171b72081 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: d5d38c79-1333-4772-9db9-6b3cf7d213b0 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.1.2 - Ethereum Mainnet - Centrifuge JAAA Instance Configuration Document [Core]  <!-- UUID: 10f4641c-2ed1-4430-ae71-1e830e779269 -->

The documents herein contain the Instance Configuration Document for the Centrifuge JAAA Instance.

###### A.6.1.1.2.2.6.1.3.1.1.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 05a8b7ae-7274-4ff7-a6f3-c7df85c2e591 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.1.2.2 - Parameters [Core]  <!-- UUID: 2318f007-26bf-463a-a275-535188ecb1b0 -->

The documents herein define the parameters of the Centrifuge JAAA Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.1.2.2.1 - Instance Identifiers [Core]  <!-- UUID: e1b41201-bf02-4c0b-a248-6f8e90f3e25f -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.1.2.2.1.1 - Network [Core]  <!-- UUID: c80c1dbe-6f51-4877-aea6-98ae4959fa80 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.1.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 38eee5f5-3e8a-4519-9370-cfe95d807c69 -->

Centrifuge

###### A.6.1.1.2.2.6.1.3.1.1.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: a7002c17-f04c-4c77-9c36-0882c97b132f -->

USDC

###### A.6.1.1.2.2.6.1.3.1.1.2.2.1.4 - Token [Core]  <!-- UUID: 684afb30-ebb4-4928-829d-8f9f0001f3e6 -->

JAAA

###### A.6.1.1.2.2.6.1.3.1.1.2.2.2 - Contract Addresses [Core]  <!-- UUID: 12e79979-2299-4d8b-9aef-d7cd07868007 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.1.2.2.2.1 - Token Address [Core]  <!-- UUID: fe31ba7d-30cc-4fec-b74a-0dea0f633730 -->

`0x4880799eE5200fC58DA299e965df644fBf46780B`

###### A.6.1.1.2.2.6.1.3.1.1.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 14d69bb4-b7a8-4780-8563-4a798768d8b3 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.1.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: f5a93d42-0c5d-4065-9a36-d900d4798ee4 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.1.2.2.4 - Rate Limits [Core]  <!-- UUID: d408bd88-f680-4696-912a-5918bb08cc83 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.1.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 52d37b01-d8f2-4b9f-b251-c0f6e025c078 -->

The inflow rate limits are:

- `maxAmount`: 100,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.1.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: f8705bd9-bc30-49c5-89fa-b529ebaee123 -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.1.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 6a41f1e9-8e61-4598-9a37-4f504fb50019 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.1.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 44c38f07-4f72-41fd-832c-ce06c2d514e0 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.1.3 - Ethereum Mainnet - Centrifuge ACRDX Instance Configuration Document [Core]  <!-- UUID: b0d889d1-8465-4229-ba69-ca4b5d866131 -->

The documents herein contain the Instance Configuration Document for the Centrifuge ACRDX Instance.

###### A.6.1.1.2.2.6.1.3.1.1.3.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 7c02c1e6-c967-44cd-bebe-7b5adb071484 -->

`Pending`

###### A.6.1.1.2.2.6.1.3.1.1.3.2 - Parameters [Core]  <!-- UUID: 1c2f901d-4128-4bc6-b369-f31e568b3087 -->

The documents herein define the parameters of the Centrifuge ACRDX Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.1.3.2.1 - Instance Identifiers [Core]  <!-- UUID: b88a0c50-f937-40e1-85a4-293a0f11b534 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.1.3.2.1.1 - Network [Core]  <!-- UUID: 91a95c0d-32d2-404d-b4c8-9f02398080f2 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.1.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 71aa102a-e0cb-4c5b-a3cb-0a5200d83c2b -->

Centrifuge ACRDX

###### A.6.1.1.2.2.6.1.3.1.1.3.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 76fca48e-a4c4-4253-9c14-f3835d906d44 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.1.3.2.1.4 - Token [Core]  <!-- UUID: a0fe0b4a-851e-4a3b-b040-309cb3ba23d2 -->

ACRDX

###### A.6.1.1.2.2.6.1.3.1.1.3.2.2 - Contract Addresses [Core]  <!-- UUID: c11a5f0f-11da-46e6-a08f-5e6722207bfe -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.1.3.2.2.1 - Token Address [Core]  <!-- UUID: af5632c6-6a6f-4692-8cf4-3d4e8b617dc8 -->

`0x9477724Bb54AD5417de8Baff29e59DF3fB4DA74f`

###### A.6.1.1.2.2.6.1.3.1.1.3.2.2.2 - Deposit Address (Mainnet) [Core]  <!-- UUID: a6946602-348a-408a-9cbf-d566efe96cbf -->

`0x74A739EA1Dc67c5a0179ebad665D1D3c4b80B712`

###### A.6.1.1.2.2.6.1.3.1.1.3.2.2.3 - Underlying Asset Address [Core]  <!-- UUID: 904c9554-0fff-4d9d-9993-bf4c281e02c4 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.1.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: 5b60c33b-7a48-43a7-bb78-0cd2e03f0079 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.1.3.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: bb056a14-2a9f-41ef-9226-3beb5867592c -->

The inflow RateLimitID is: `0xb8139d1c2486c30929b3cb3a487a3d9c3885f49cff1f07e9393262b15ef1158a`

###### A.6.1.1.2.2.6.1.3.1.1.3.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 6c04d78a-61d7-4e9a-b156-ef08168704f7 -->

The outflow RateLimitID is: `0x58aa7b39a6c9894ea4a4cd6868d014c718d09913cdf5d793e21509f0ccd32495`

###### A.6.1.1.2.2.6.1.3.1.1.3.2.4 - Rate Limits [Core]  <!-- UUID: fb4b9380-ecef-4d3c-a2b0-6b2af6a960a9 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.1.3.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 2305ac7b-a8dc-4611-b242-0996d4d22a88 -->

The deposit rate limits are:

- `maxAmount`: 20,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.1.3.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 512819c7-6e39-4bdc-add6-0fc892f54ccb -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.1.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 2fad60e4-4c86-48b7-a7b9-0c0f0ef88459 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.1.3.2.5.1 - Maximum Exposure [Core]  <!-- UUID: 96e8ca2f-4e71-4ab0-ba0f-1958ea8e637b -->

Total ACRDX exposure may not exceed 50.97 million USDS and should be reduced to zero over time.

###### A.6.1.1.2.2.6.1.3.1.1.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 1faafb47-66b2-49a4-abf5-5cd6f1555361 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.1.4 - Ethereum Mainnet - Centrifuge JTRSY USDS Vault Instance Configuration Document [Core]  <!-- UUID: acbe1bed-7639-45a4-9a5d-73c7d434bd0a -->

The documents herein contain the Instance Configuration Document for the Centrifuge JTRSY USDS Vault Instance.

###### A.6.1.1.2.2.6.1.3.1.1.4.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 72120c5a-c08c-40cf-935e-eb4c28649aff -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.1.4.2 - Parameters [Core]  <!-- UUID: aa4c9779-aa53-47ad-9780-a9978fae5334 -->

The documents herein define the parameters of the Centrifuge JTRSY USDS Vault Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.1.4.2.1 - Instance Identifiers [Core]  <!-- UUID: e0b55a83-1e4c-4f6b-bd92-fe334bc220e5 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.1.4.2.1.1 - Network [Core]  <!-- UUID: ebe72c81-05ca-4dda-9e91-177ebcd1d83e -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.1.4.2.1.2 - Target Protocol [Core]  <!-- UUID: aed0cab3-1498-4bd1-8361-ef4be5c06ebc -->

Centrifuge

###### A.6.1.1.2.2.6.1.3.1.1.4.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 80d0c003-7941-41ad-bc2b-ed2a27446ff5 -->

USDS

###### A.6.1.1.2.2.6.1.3.1.1.4.2.1.4 - Token [Core]  <!-- UUID: a6c0d662-dbd0-44e4-9e73-a1b455629f52 -->

JTRSY

###### A.6.1.1.2.2.6.1.3.1.1.4.2.2 - Contract Addresses [Core]  <!-- UUID: e155bd93-6ce4-497e-8e69-abc199b6e223 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.1.4.2.2.1 - Token Address [Core]  <!-- UUID: baa2fd47-b45a-4d03-9393-0351d4fa70a8 -->

`0x381f4F3B43C30B78C1f7777553236e57bB8AE9ff`

###### A.6.1.1.2.2.6.1.3.1.1.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 9a061684-5c54-4448-bdc7-cb21578db5cb -->

`0xdC035D45d973E3EC169d2276DDab16f1e407384F`

###### A.6.1.1.2.2.6.1.3.1.1.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: ae198061-322e-486c-b6a3-69c9f44a0092 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.1.4.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: bbb15d43-e8e6-47a1-9f26-bbd0b9a34574 -->

The inflow RateLimitID is: `0x12a7aab841b7cc5a82aa3f431a00634d363fa012c2e247229a80509ab0426359`

###### A.6.1.1.2.2.6.1.3.1.1.4.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: d4f11693-8a00-44ec-bc44-07b3b9e13fe7 -->

The outflow RateLimitID is: `0x90f60b9802ce2da6196f5558e32abf7b583c646525d836146bfa7938caaaa935`

###### A.6.1.1.2.2.6.1.3.1.1.4.2.4 - Rate Limits [Core]  <!-- UUID: de12ee28-f435-43ce-beac-5b1ecff3b0d5 -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.1.4.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: aac8ee49-9414-4fe5-8594-7ecdecdaddd4 -->

The inflow rate limits are:

- `maxAmount`: 500,000,000 USDS
- `slope`: 500,000,000 USDS per day

###### A.6.1.1.2.2.6.1.3.1.1.4.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: a1fa5391-2481-4e75-9070-4bb11d7598df -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.1.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 019ca238-986e-4033-9d81-245845a0eadd -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.1.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 35ac515f-6832-4e41-88fe-7eb32e6f2702 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.2 - Blackrock [Core]  <!-- UUID: 61ab2f32-60b9-459e-99d5-0e59958c8561 -->

The Ethereum Mainnet Instances of the Blackrock Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.2.1 - Ethereum Mainnet - Blackrock BUIDL-I Instance Configuration Document [Core]  <!-- UUID: 8bc44388-0d97-4d5e-aa33-fdd1938f03ff -->

The documents herein contain the Instance Configuration Document for the Blackrock BUIDL-I Instance.

###### A.6.1.1.2.2.6.1.3.1.2.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: b565fc42-5f82-444c-95ae-bd560cb7e0e2 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.2.1.2 - Parameters [Core]  <!-- UUID: b2eabff0-ab16-4840-8e75-79c2f8fd9bcf -->

The documents herein define the parameters of the Blackrock BUIDL-I Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 7bc4d289-e05c-410f-b72f-e15ab6665119 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.2.1.2.1.1 - Network [Core]  <!-- UUID: e9ae782a-3edc-4d11-acd3-4055dc6a836c -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: c58fffd4-4905-4749-a7fa-55b69f0f44f3 -->

Blackrock

###### A.6.1.1.2.2.6.1.3.1.2.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 9e20f087-373b-439c-ba49-a697c2d5e089 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.2.1.2.1.4 - Token [Core]  <!-- UUID: bab41936-4c79-4821-9e78-fd1dd6511003 -->

BUIDL-I

###### A.6.1.1.2.2.6.1.3.1.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: bc0020b6-33fe-4297-bd2d-950583288718 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.2.1.2.2.1 - Token Address [Core]  <!-- UUID: 2c3d5162-5aac-4b5d-838d-8bc2952b7852 -->

`0x6a9DA2D710BB9B700acde7Cb81F10F1fF8C89041`

###### A.6.1.1.2.2.6.1.3.1.2.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 45250d99-f5d0-48f7-a8b6-a92bcbb95c05 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.2.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: e40c4ab5-15a9-4d56-a01e-609388d38bac -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.2.1.2.4 - Rate Limits [Core]  <!-- UUID: 6aeaafb3-c78d-4a20-9da7-2d88adb2f7d9 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.2.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 5edb937d-c579-42e3-ae25-821150cddda2 -->

The inflow rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.2.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 0b80d875-47a9-4863-8cf9-7a564e49d7ff -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 96d4e794-64f4-428d-a4e0-294576b64856 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 123ded95-dc31-4f9b-9240-6180be9efa8c -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.3 - Superstate [Core]  <!-- UUID: feb10c4e-f51f-4707-8794-df0e0c28069f -->

The Ethereum Mainnet Instances of the Superstate Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.3.1 - Ethereum Mainnet - Superstate USTB Instance Configuration Document [Core]  <!-- UUID: a49f5e48-6e00-434b-bd85-26539c7a9cfe -->

The documents herein contain the Instance Configuration Document for the Superstate USTB Instance.

###### A.6.1.1.2.2.6.1.3.1.3.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: b3388919-4af4-4cd8-8d2e-76ba1e35a119 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.3.1.2 - Parameters [Core]  <!-- UUID: 2b146ad3-e8ba-4aa8-99e9-73b0b8d90f36 -->

The documents herein define the parameters of the Superstate USTB Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 671f6c1e-5bba-4e80-93b3-91cc2547dd24 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.1.1 - Network [Core]  <!-- UUID: 74595227-8083-4620-a9c2-fc7b7ccb97bf -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.3.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 02307043-77c0-40d5-bec0-cc969dc2eb1e -->

Superstate

###### A.6.1.1.2.2.6.1.3.1.3.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 6eb81d2f-e7c0-4306-a10f-fdf38e3eed5f -->

USDC

###### A.6.1.1.2.2.6.1.3.1.3.1.2.1.4 - Token [Core]  <!-- UUID: af5bb5fe-b41f-4e8d-ad1c-8015813ad323 -->

USTB

###### A.6.1.1.2.2.6.1.3.1.3.1.2.2 - Contract Addresses [Core]  <!-- UUID: cdb0f02e-2fd4-48cb-a38c-17badb67f8da -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.2.1 - Token Address [Core]  <!-- UUID: c1b16951-4e99-45a3-a89f-259c5214f26d -->

This address will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 10bd480c-d536-47ec-ba10-d09b053300c4 -->

This address will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 24a76d96-4369-476d-baa8-82f0a0276fe2 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.4 - Rate Limits [Core]  <!-- UUID: adc16c56-8f93-4598-ae41-e6e96f16936f -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: bde14e56-5d3b-4797-9ab4-6cd689d74a8c -->

The inflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Grove Artifact.
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 35aaf86f-8a8e-487a-8f1d-65f263223da1 -->

The outflow rate limits are:

- `maxAmount`: This parameter will be specified in a future iteration of the Grove Artifact.
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.3.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: a9787ff0-1082-4e6e-b77b-b86f9a3aeade -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.3.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 8488e826-76ee-47bd-aee1-4fea72109903 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.4 - Ethena [Core]  <!-- UUID: 39ed1591-d474-4ed1-a794-b178d64aa948 -->

The Ethereum Mainnet Instances of the Ethena Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.4.1 - Ethereum Mainnet - Ethena USDe Instance Configuration Document [Core]  <!-- UUID: dbe15588-fa00-4573-ae8a-f69e095532f5 -->

The documents herein contain the Instance Configuration Document for the Ethena USDe Instance.

###### A.6.1.1.2.2.6.1.3.1.4.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: dfd44d17-c702-4e46-84e3-4361b95696cf -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.4.1.2 - Parameters [Core]  <!-- UUID: 14d7c28e-1ca0-4430-a9a2-a80625b292b8 -->

The documents herein define the parameters of the Ethena USDe Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.4.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 53baf614-c4e3-41e1-ae1a-7002964bafcd -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.4.1.2.1.1 - Network [Core]  <!-- UUID: 4b9deda5-4a2a-4da3-9e03-85a04f232110 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.4.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 6f33f060-c24e-4c24-b6f8-7882bb19f7c0 -->

Ethena Protocol

###### A.6.1.1.2.2.6.1.3.1.4.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 45b293a2-10f7-4a5e-95c0-fc7375870e78 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.4.1.2.1.4 - Token [Core]  <!-- UUID: 8f59e11f-8e45-4daa-b47e-9034c992b840 -->

USDe

###### A.6.1.1.2.2.6.1.3.1.4.1.2.2 - Contract Addresses [Core]  <!-- UUID: 0582245f-0b92-468a-868d-d7f83269b24a -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.4.1.2.2.1 - Token Address [Core]  <!-- UUID: 7dd0f228-265b-4411-87e9-5fff688a4bae -->

`0x4c9EDD5852cd905f086C759E8383e09bff1E68B3`

###### A.6.1.1.2.2.6.1.3.1.4.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 5f107bd7-9fcb-433a-a6a6-f6db9f2f018b -->

This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.4.1.2.2.3 - EthenaMinter [Core]  <!-- UUID: be1ccf23-f306-4c8e-a43c-26fb8d8d7d1a -->

`0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3`

###### A.6.1.1.2.2.6.1.3.1.4.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: d20a3198-86da-403b-8509-4cc374a5a1ed -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.4.1.2.4 - Rate Limits [Core]  <!-- UUID: f1fa0280-9862-4e66-9e4f-4c410bbdf437 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.4.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: cb1ffa0f-bdc8-4bd5-80ce-1592429758b8 -->

The inflow rate limits are:

- `maxAmount`: 250,000,000
- `slope`: 100,000,000 per day

###### A.6.1.1.2.2.6.1.3.1.4.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 6cf9b977-565d-44f3-9400-0ad1b05f57bd -->

The outflow rate limits are:

- `maxAmount`: 500,000,000
- `slope`: 200,000,000 per day

###### A.6.1.1.2.2.6.1.3.1.4.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 620c1687-bf39-4e90-a9dd-ab191a66f166 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.4.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 80844016-8ae5-4ea3-b4b7-970a33158425 -->

The documents herein defines the operations performed to manage the Ethena Instance, including rate limiting, role-based access control, and cooldown functionality.

###### A.6.1.1.2.2.6.1.3.1.4.1.3.1 - Delegated Signers [Core]  <!-- UUID: 98191437-0437-496e-ad1a-ceeba3c3b9d6 -->

The documents herein contain the addresses authorized as `delegatedSigners` in the `ethenaMinter` contract. `delegatedSigners` are set up and removed in the `MainnetController` contract by the `Relayer` role.

###### A.6.1.1.2.2.6.1.3.1.4.1.3.1.1 - Addresses Of Delegated Signers [Core]  <!-- UUID: ba1c514f-026a-4ecd-bb9a-c736cca59728 -->

`delegatedSigner` addresses

- These addesses will be specified in a future iteration of the Spark Artifact.

###### A.6.1.1.2.2.6.1.3.1.4.1.3.2 - Set A Delegated Signer In The EthenaMinter Contract [Core]  <!-- UUID: 18b6c02a-45bc-419d-bcb6-acbbd44f75c0 -->

The documents herein define the process for an operator to set a delegated signer to the EthenaMinter contract.

###### A.6.1.1.2.2.6.1.3.1.4.1.3.2.1 - Relayer Role [Core]  <!-- UUID: be6df08e-d837-4ad8-bce4-69adbaec2213 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `setDelegatedSigner`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function setDelegatedSigner(address delegatedSigner)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.2.2 - Encode Function [Core]  <!-- UUID: 0338eae8-0c00-4eb4-858f-50d66f2c65d7 -->

The operator must use `proxy.doCall()` to forward the call to the `ethenaMinter` contract and call `setDelegatedSigner` function to set the address that will be authorized as a `delegatedSigner`. To call on `ethenaMinter` contract, the function must be encoded using `abi.encodeCall`.

`{
    proxy.doCall(
        address(ethenaMinter),
        abi.encodeCall(ethenaMinter.setDelegatedSigner, (address(delegatedSigner)))
    );
}`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.3 - Remove A Delegated Signer In The Ethena Minter Contract [Core]  <!-- UUID: a9007256-ac47-4807-a3c5-3686f8b688b7 -->

The documents herein define the process for an operator to remove a delegated signer from the Ethena Minter contract.

###### A.6.1.1.2.2.6.1.3.1.4.1.3.3.1 - Relayer Role [Core]  <!-- UUID: 55d5ce02-6dc2-49c8-a482-8b10fa24f8b6 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `removeDelegatedSigner`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function removeDelegatedSigner(address delegatedSigner)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.3.2 - Encode Function [Core]  <!-- UUID: e3f7d68f-d4af-4809-b6c9-2457b00ec991 -->

The operator must use `proxy.doCall()` to forward the call to the `ethenaMinter` contract and call `removeDelegatedSigner` function to remove the authorization for the `address` to act as a `delegatedSigner`. To call on `ethenaMinter` contract, the function must be encoded using `abi.encodeCall`.

`{
    proxy.doCall(
        address(ethenaMinter),
        abi.encodeCall(ethenaMinter.removeDelegatedSigner, (address(delegatedSigner)))
    );
}`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.4 - Approve Minting of USDe By Ethena Minter Contract [Core]  <!-- UUID: 704d4083-3af2-491b-93c5-0dcaf19f0927 -->

The documents herein define the process for an operator to approve the minting of USDe by the EthenaMinter contract.

###### A.6.1.1.2.2.6.1.3.1.4.1.3.4.1 - Relayer Role [Core]  <!-- UUID: 47f20c86-d122-4ab2-a9b0-5458e4b5797f -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeMint`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function prepareUSDeMint(uint256 usdcAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.4.2 - Enforce Rate Limit [Core]  <!-- UUID: 3b26a2c4-fb16-4f72-8b46-ca96f0352681 -->

The operator must enforce a rate limit on how much USDC can be approved for minting USDe.

`rateLimited(LIMIT_USDE_MINT, usdcAmount)`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.4.3 - Encode Function [Core]  <!-- UUID: 5a33accd-3e23-4e64-be97-a0a981620a6f -->

The operator must use `proxy.doCall()` to send an approval call to the `usdc` contract, allowing the `ethenaMinter` contract to spend up to the specified `amount` of USDC. They must encode the function using `abi.encodeCall`.

` {
    proxy.doCall(
        address(usdc),
        abi.encodeCall(usdc.approve, (address(ethenaMinter), usdcAmount))
    );
}`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.5 - Approve Burning of USDe By EthenaMinter Contract [Core]  <!-- UUID: ffdc8734-a58e-4298-a98e-f379862e705e -->

The documents herein define the process for an operator to approve the burning of USDe by the EthenaMinter contract.

###### A.6.1.1.2.2.6.1.3.1.4.1.3.5.1 - Relayer Role [Core]  <!-- UUID: 5d3210e1-2ad4-440f-9c61-6adcc22abc90 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `prepareUSDeBurn`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function prepareUSDeBurn(uint256 usdeAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.5.2 - Enforce Rate Limit [Core]  <!-- UUID: e2f185ba-fcd6-4f46-8f7e-9b09c111a75d -->

The operator must enforce a rate limit on how much USDe can be approved for burning.

`rateLimited(LIMIT_USDE_BURN, usdeAmount)`

###### A.6.1.1.2.2.6.1.3.1.4.1.3.5.3 - Encode Function [Core]  <!-- UUID: 230f7b75-df50-417a-8d02-16089a5831c6 -->

The operator must use `proxy.doCall()` to send an approval call to the `usde` contract, allowing the `ethenaMinter` contract to spend up to the specified `amount` of USDe. They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(usde),
        abi.encodeCall(usde.approve, (address(ethenaMinter), usdeAmount))
    );
}`

###### A.6.1.1.2.2.6.1.3.1.4.2 - Ethereum Mainnet - Ethena sUSDe Instance Configuration Document [Core]  <!-- UUID: 5847fff3-ff82-4c01-ac24-7f06fac8c2a4 -->

The documents herein contain the Instance Configuration Document for the Ethena sUSDe Instance.

###### A.6.1.1.2.2.6.1.3.1.4.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 54635681-871e-4c36-8090-b55a760219ca -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.4.2.2 - Parameters [Core]  <!-- UUID: b483ba5f-7570-4ab4-82e6-f8296553f3e4 -->

The documents herein define the parameters of the Ethena sUSDe Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.4.2.2.1 - Instance Identifiers [Core]  <!-- UUID: a544cec4-f067-477c-8cc5-f74e59d56d45 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.4.2.2.1.1 - Network [Core]  <!-- UUID: f68d33ff-4092-46aa-92e2-e592b8f84c14 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.4.2.2.1.2 - Target Protocol [Core]  <!-- UUID: b31f534a-7268-4500-be69-abc662541b55 -->

Ethena Protocol

###### A.6.1.1.2.2.6.1.3.1.4.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 0f400550-8477-490d-bdd2-17cb3f808be1 -->

USDe

###### A.6.1.1.2.2.6.1.3.1.4.2.2.1.4 - Token [Core]  <!-- UUID: c4f40f7e-84da-4cc1-8a45-9eeb27e92255 -->

sUSDe

###### A.6.1.1.2.2.6.1.3.1.4.2.2.2 - Contract Addresses [Core]  <!-- UUID: 83e0f89d-08df-476a-bbb1-4566f69fafd4 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.4.2.2.2.1 - Token Address [Core]  <!-- UUID: 002874e2-43a6-4daa-8e02-1b6f9291d02f -->

`0x9D39A5DE30e57443BfF2A8307A4256c8797A3497`

###### A.6.1.1.2.2.6.1.3.1.4.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: be355bce-80b5-4e9d-a78f-ee5b87aa7117 -->

`0x4c9EDD5852cd905f086C759E8383e09bff1E68B3`

###### A.6.1.1.2.2.6.1.3.1.4.2.2.2.3 - EthenaMinter [Core]  <!-- UUID: 368f88e3-5570-4a60-b15b-f4ee23519caa -->

`0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3`

###### A.6.1.1.2.2.6.1.3.1.4.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 5ecd37de-d09e-438c-838a-9070c42c2802 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.4.2.2.4 - Rate Limits [Core]  <!-- UUID: cd0d2be7-92af-47e1-af84-efd52c36d4d9 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.4.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: d25089f6-ed8a-4af9-adb1-9830e0daf0bc -->

The inflow rate limits are:

- `maxAmount`: 250,000,000
- `slope`: 100,000,000 per day

###### A.6.1.1.2.2.6.1.3.1.4.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: d33504c7-812f-43fb-b825-fc23aa177a3e -->

The outflow rate limits are:

- `maxAmount`: unlimited
- `slope`: unlimited

###### A.6.1.1.2.2.6.1.3.1.4.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 12935140-ad9b-42b4-a2e2-b84573e8ec0b -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.4.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: e1e9bdd9-5301-4efb-80d8-ffc0b29a6ec1 -->

For operational processes defining the operations performed to manage the Ethena Instance, including rate limiting, role-based access control, and minting of USDe functionality see Instance-specific Operational Processes. For detailed logic specific for this instance see [A.6.1.1.2.2.6.1.3.1.4.2.3.1 - Initiate A sUSDe Cooldown Period](2e467f99-83b9-48a0-adf5-9cc5c538fb23), [A.6.1.1.2.2.6.1.3.1.4.2.3.2 - Cool Down sUSDe Shares](8f029eaf-a208-4f7c-8f00-d34b1e15ca08), [A.6.1.1.2.2.6.1.3.1.4.2.3.3 - Unstake sUSDe And Return It To ALM Proxy](bf0523c1-7c37-4073-b565-202c5497825c) and [A.6.1.1.2.2.6.1.3.1.4.2.3.4 - Emergency Procedure To Withdraw Ethena Balances](8d926497-9fe7-4189-83c8-10f649ff0b1d).

###### A.6.1.1.2.2.6.1.3.1.4.2.3.1 - Initiate A sUSDe Cooldown Period [Core]  <!-- UUID: 2e467f99-83b9-48a0-adf5-9cc5c538fb23 -->

The documents herein define the process for an operator to initiate a sUSDe Cooldown period.

###### A.6.1.1.2.2.6.1.3.1.4.2.3.1.1 - Relayer Role [Core]  <!-- UUID: fc7b35c1-185a-41b1-83df-8d8e04349864 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownAssetsSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function cooldownAssetsSUSDe(uint256 usdeAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.2.2.6.1.3.1.4.2.3.1.2 - Enforce Rate Limit [Core]  <!-- UUID: c9040dc5-3f47-4e47-861c-6ddac774ecb6 -->

The operator must enforce a rate limit on how much sUSDe can be cooled down.

`rateLimited(LIMIT_SUSDE_COOLDOWN, usdeAmount)`

###### A.6.1.1.2.2.6.1.3.1.4.2.3.1.3 - Encode Function [Core]  <!-- UUID: 3c9e6628-3441-4d53-aed1-6dc973d8f8cc -->

The operator must use `proxy.doCall()` to make a call to the `susde` contract, invoking the `cooldownAssets` function with the specified amount of sUSDe. They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(susde),
        abi.encodeCall(susde.cooldownAssets, (usdeAmount))
    );
}`

###### A.6.1.1.2.2.6.1.3.1.4.2.3.2 - Cool Down sUSDe Shares [Core]  <!-- UUID: 8f029eaf-a208-4f7c-8f00-d34b1e15ca08 -->

The documents herein define the process for an operator to cool down sUSDe shares.

###### A.6.1.1.2.2.6.1.3.1.4.2.3.2.1 - Relayer Role [Core]  <!-- UUID: ba771f78-163f-4ec6-990d-ec8cc25e0393 -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `cooldownSharesSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function cooldownSharesSUSDe(uint256 susdeAmount)
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.2.2.6.1.3.1.4.2.3.2.2 - Encode Function [Core]  <!-- UUID: 038cb6fe-4040-4f3a-b1a8-9c6f2f3a4f72 -->

The operator must use `proxy.doCall()` to make a call to the `susde` contract, initiating the `cooldown` on the specified amount of sUSDe shares. They must encode the function using `abi.encodeCall`.

###### A.6.1.1.2.2.6.1.3.1.4.2.3.2.2.1 - Decode For Underlying Shares [Core]  <!-- UUID: 9e6e0eef-e29c-4e99-ad36-36c4eeac37ea -->

The operator must decode the result returned by the `cooldownShares` function into a `uint256` value, representing the amount of shares that were actually cooled down (`cooldownAmount`).

`{
    cooldownAmount = abi.decode(
        proxy.doCall(
            address(susde),
            abi.encodeCall(susde.cooldownShares, (susdeAmount))
        ),
        (uint256)
    );`

###### A.6.1.1.2.2.6.1.3.1.4.2.3.2.3 - Decrease RateLimit [Core]  <!-- UUID: 42943bad-504a-4b59-9164-d6cc2acf6a95 -->

The operator must decrease the `RateLimit`, effectively reducing the available `cooldown` limit, based on the `cooldownAmount`.

`rateLimits.triggerRateLimitDecrease(LIMIT_SUSDE_COOLDOWN, cooldownAmount);
}`

###### A.6.1.1.2.2.6.1.3.1.4.2.3.3 - Unstake sUSDe And Return It To ALM Proxy [Core]  <!-- UUID: bf0523c1-7c37-4073-b565-202c5497825c -->

The documents herein define the process for an operator to unstake sUSDe and return it to the ALM Proxy.

###### A.6.1.1.2.2.6.1.3.1.4.2.3.3.1 - Relayer Role [Core]  <!-- UUID: 1f19cb45-1934-4e2e-8d07-0d4b78e7188c -->

The operator must ensure they are working as a `RELAYER`. Only the `RELAYER` role is allowed to `unstakeSUSDe`. Also, they must ensure the contract `isActive` i.e. can process the request.

`function unstakeSUSDe()
        external
        onlyRole(RELAYER)
        isActive`

###### A.6.1.1.2.2.6.1.3.1.4.2.3.3.2 - Encode Function [Core]  <!-- UUID: 516ca684-b183-4d57-9feb-97a7a9b58e42 -->

The operator must use `proxy.doCall()` to make a call to the `susde` contract to invoke the `unstake` function, which unstakes sUSDe and sends the resulting tokens back to the `proxy` address (i.e. ALM Proxy). They must encode the function using `abi.encodeCall`.

`{
    proxy.doCall(
        address(susde),
        abi.encodeCall(susde.unstake, (address(proxy)))
    );
}`

###### A.6.1.1.2.2.6.1.3.1.4.2.3.4 - Emergency Procedure To Withdraw Ethena Balances [Core]  <!-- UUID: 8d926497-9fe7-4189-83c8-10f649ff0b1d -->

In order to withdraw all Ethena balances, the operator must execute the following actions:

###### A.6.1.1.2.2.6.1.3.1.4.2.3.4.1 - sUSDe Cooldown Action [Core]  <!-- UUID: bc67845f-f3e8-45d3-b17b-93b669072f77 -->

The operator must start the cooldown for sUSDe using the following action:

`mainnetController.cooldownSharesSUSDe(susde.balanceOf(address(proxy))
`
For more detailed instructions on the code to execute this, see [A.6.1.1.2.2.6.1.3.1.4.2.3.2 - Cool Down sUSDe Shares](8f029eaf-a208-4f7c-8f00-d34b1e15ca08).

###### A.6.1.1.2.2.6.1.3.1.4.2.3.4.2 - sUSDe Unstake Action [Core]  <!-- UUID: 44ee472f-41a4-45c4-bce3-34615132e5d2 -->

The operator must unstake sUSDe using the following action:

`mainnetController.unstakeSUSDe()
`
For more detailed instructions on the code to execute this, see [A.6.1.1.2.2.6.1.3.1.4.2.3.3 - Unstake sUSDe And Return It To ALM Proxy](bf0523c1-7c37-4073-b565-202c5497825c).

###### A.6.1.1.2.2.6.1.3.1.4.3 - Ethereum Mainnet - Ethena PT-USDe Instance Configuration Document [Core]  <!-- UUID: e3f9abf3-0cd0-46cc-8295-175c1bc8afbd -->

The documents herein contain the Instance Configuration Document for the Ethena PT-USDe Instance.

###### A.6.1.1.2.2.6.1.3.1.4.3.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 65922d1d-0866-480a-9e56-5c47f2ed24c0 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.4.3.2 - Parameters [Core]  <!-- UUID: f96e5493-ce45-496c-a9c0-833962329075 -->

The documents herein define the parameters of the Ethena PT-USDe Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.4.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 5882a708-164c-49c4-8348-1bc2f81066a4 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.4.3.2.1.1 - Network [Core]  <!-- UUID: 7ff517b4-069c-4f73-adc8-028756a8e3f3 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.4.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 0d4e39d3-5b1a-44ad-aba5-4171bf22e370 -->

Ethena

###### A.6.1.1.2.2.6.1.3.1.4.3.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: f716ae3f-7c95-4ccc-8280-2e62a8a121d1 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.4.3.2.1.4 - Token [Core]  <!-- UUID: 34447618-cb6c-4d05-874e-68e2d8c5ea95 -->

PT-USDe

###### A.6.1.1.2.2.6.1.3.1.4.3.2.2 - Contract Addresses [Core]  <!-- UUID: bb7c88fe-0f4f-4384-a9ca-a6a974e460c6 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.4.3.2.2.1 - Token Address [Core]  <!-- UUID: 9008b149-de3d-429d-824f-48524063d657 -->

`0x4c9EDD5852cd905f086C759E8383e09bff1E68B3`

###### A.6.1.1.2.2.6.1.3.1.4.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: dd7eaa92-d40a-4ffc-9359-ce7d8a9f01fe -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.4.3.2.2.3 - Broker Address [Core]  <!-- UUID: 88303bee-82c3-4d78-8b31-e319c760ee31 -->

`0xD94F9ef3395BBE41C1f05ced3C9a7dc520D08036`

###### A.6.1.1.2.2.6.1.3.1.4.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: 93e8e5e9-2e38-45ff-b325-7ff52f73017d -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.4.3.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 7e3cf2f7-1371-426e-881a-99878625cd2e -->

The inflow RateLimitID is: `0x098ad67dc41c1a5892ec3ef5fd411198dc11962475e9ef2e0362e6cb7f5a2174`.

###### A.6.1.1.2.2.6.1.3.1.4.3.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 49a086b0-0d77-4d9a-b899-9b1177181b4b -->

The outflow RateLimitID is: `0x6dd53d41cd67732ec6166a0927bd9c2da9e20940bd174778b44787531d32d42e`.

###### A.6.1.1.2.2.6.1.3.1.4.3.2.4 - Rate Limits [Core]  <!-- UUID: c13e1a1b-4104-4964-a901-4c7bcb19c868 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.4.3.2.4.1 - Deposit Rate Limits (via FalconX) [Core]  <!-- UUID: 7a93740b-d794-4ca9-aece-6c7db42bebf2 -->

The deposit rate limits are:

- `maxAmount`: 50 million USDC
- `slope`: 50 million USDC

###### A.6.1.1.2.2.6.1.3.1.4.3.2.4.2 - Withdrawal Rate Limits (via FalconX) [Core]  <!-- UUID: e198f465-0b25-4f45-860f-66eacc575f9f -->

The withdrawal rate limits are:

- `maxAmount`: 50 million USDC
- `slope`: 50 million USDC

###### A.6.1.1.2.2.6.1.3.1.4.3.2.4.3 - Redemption Rate Limits (via Pendle Protocol) [Core]  <!-- UUID: 9dce58c1-0c6d-44f4-8145-c4243e8c02a9 -->

The redemption rate limits are:

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.4.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: a0fbf90a-75dc-4ee7-a4a6-e9a39314f8b3 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.4.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 64fc397b-a8e4-425a-814f-d22570dfadc7 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.4.4 - Ethereum Mainnet - Ethena PT-sUSDe Instance Configuration Document [Core]  <!-- UUID: ba45e20f-b6df-4836-94ea-b4f2f062e658 -->

The documents herein contain the Instance Configuration Document for the Ethena PT-sUSDe Instance.

###### A.6.1.1.2.2.6.1.3.1.4.4.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: c0a78c43-bbd6-4735-b1b9-15772514223b -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.4.4.2 - Parameters [Core]  <!-- UUID: 5799c20d-bed8-4e81-bffb-5ec49e95d303 -->

The documents herein define the parameters of the Ethena PT-sUSDe Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.4.4.2.1 - Instance Identifiers [Core]  <!-- UUID: 6b772ff5-77a0-4f96-8ce7-896c4a221e31 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.4.4.2.1.1 - Network [Core]  <!-- UUID: 88cf47cb-a94e-475e-9fb8-1b9f2540ba9a -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.4.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 6dbd0693-3ebd-4175-82ef-991f085b6942 -->

Ethena

###### A.6.1.1.2.2.6.1.3.1.4.4.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 3246daa1-29ee-447e-ad83-b5b7f8f8a931 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.4.4.2.1.4 - Token [Core]  <!-- UUID: dd3b11cd-ca9d-4c7b-9769-9624c3085954 -->

PT-sUSDe

###### A.6.1.1.2.2.6.1.3.1.4.4.2.1.5 - Broker [Core]  <!-- UUID: fc28e9fd-a4db-4963-8935-f2b05dd2a8bd -->

FalconX

###### A.6.1.1.2.2.6.1.3.1.4.4.2.2 - Contract Addresses [Core]  <!-- UUID: 46e15661-6ee9-4ac6-88ad-d07d7f7fa6a4 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.4.4.2.2.1 - Token Address [Core]  <!-- UUID: 3b108b97-6f88-4d96-a55a-38c39191281e -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.4.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 914e6bcf-a73b-4c80-bfa8-04dbd58a7805 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.4.4.2.2.3 - Broker Address [Core]  <!-- UUID: 4d4d42ae-76e3-4de8-87a0-14ce30a4ebe5 -->

`0xD94F9ef3395BBE41C1f05ced3C9a7dc520D08036`

###### A.6.1.1.2.2.6.1.3.1.4.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: 3af5241e-5b72-4466-9e69-dccb8a8d203b -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.1.4.4.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 230f8de3-d642-460c-bbff-4e75f110e584 -->

The inflow RateLimitID is: `0x098ad67dc41c1a5892ec3ef5fd411198dc11962475e9ef2e0362e6cb7f5a2174`.

###### A.6.1.1.2.2.6.1.3.1.4.4.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 39d3f488-0d5a-4207-a010-64a5bc6cd8db -->

The outflow RateLimitID is: `0x027191d7c552bd41037422747bcde7caca7d1f6afc5ea9b85f8a47432c70be67`.

###### A.6.1.1.2.2.6.1.3.1.4.4.2.4 - Rate Limits [Core]  <!-- UUID: df99c910-17a9-4374-989e-906bd81d621a -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.4.4.2.4.1 - Deposit Rate Limits (via FalconX) [Core]  <!-- UUID: e66a0529-5419-46ef-8b9c-e6f6c255c3e3 -->

The deposit rate limits are:

- `maxAmount`: 50 million USDC
- `slope`: 50 million USDC

###### A.6.1.1.2.2.6.1.3.1.4.4.2.4.2 - Withdrawal Rate Limits (via FalconX) [Core]  <!-- UUID: c3fa15e7-7193-4e4d-9463-9dc6001f3d75 -->

The withdrawal rate limits are:

- `maxAmount`: 50 million USDC
- `slope`: 50 million USDC

###### A.6.1.1.2.2.6.1.3.1.4.4.2.4.3 - Redemption Rate Limits (via Pendle Protocol) [Core]  <!-- UUID: 5d0649b9-c4ce-4a8a-bd2c-c6c0cc3de322 -->

The redemption rate limits are:

- `maxAmount`: Unlimited
- `slope`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.4.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 917cd220-0d0e-4c34-82a5-acb1a0013bf6 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.4.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: ab1c8923-2cf6-4825-b380-a17db876e3a9 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.5 - Aave [Core]  <!-- UUID: 2316e0fb-c6f0-43c9-b8d4-1fd1c966b9f0 -->

The Ethereum Mainnet Instances of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.5.1 - Ethereum Mainnet - Aave Core v3 USDC Instance Configuration Document [Core]  <!-- UUID: 7f4eb111-6751-4308-88ce-efe2445e5455 -->

The documents herein contain the Instance Configuration Document for the Aave Core v3 USDC Instance.

###### A.6.1.1.2.2.6.1.3.1.5.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: ad0109ba-cdb8-40d8-8856-a1c21873af79 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.5.1.2 - Parameters [Core]  <!-- UUID: 0283a372-0055-443f-aa39-2239180a65b1 -->

The documents herein define the parameters of the Aave Core v3 USDC Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.5.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 9138c237-b95f-41fe-8189-8612f75deae5 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.5.1.2.1.1 - Network [Core]  <!-- UUID: 92f14d2c-140d-4d9b-841d-f869d46be687 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.5.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 56c581d0-5f0d-49cb-a149-42ff50a74ce3 -->

Aave Core v3

###### A.6.1.1.2.2.6.1.3.1.5.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: b605f289-bf6a-40bd-89ce-4457be0767fd -->

USDC

###### A.6.1.1.2.2.6.1.3.1.5.1.2.1.4 - Token [Core]  <!-- UUID: c9a9635e-70d4-4c45-9641-5d11a7b66815 -->

aEthUSDC

###### A.6.1.1.2.2.6.1.3.1.5.1.2.2 - Contract Addresses [Core]  <!-- UUID: 78b79abf-d431-42c6-8fa0-6749768936f2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.5.1.2.2.1 - Token Address [Core]  <!-- UUID: 1899a80c-f660-488a-8ec1-7c9322bd602c -->

`0x98C23E9d8f34FEFb1B7BD6a91B7FF122F4e16F5c`

###### A.6.1.1.2.2.6.1.3.1.5.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 39624e4c-91c2-4520-b353-b8c06b7bb4d8 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.5.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 098e86e2-8f31-49a4-a6e3-00f60ed0ca43 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.5.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 8735fbad-b2a1-417d-87e8-097f6f883717 -->

The inflow RateLimitID is: `0x5b6ed3b27d9aa6a9aaf68fc5c0980d9122ac4123093cce0241e4e047c154e214`.

###### A.6.1.1.2.2.6.1.3.1.5.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 74f07aa8-e24d-4e7d-a1f5-beb8d499666c -->

The outflow RateLimitID is: `0xc0a083c57c21570181e9781d750d04917923daac34e804bad63a5a241c92a850`.

###### A.6.1.1.2.2.6.1.3.1.5.1.2.4 - Rate Limits [Core]  <!-- UUID: bb488181-e690-4fe1-8be3-ceac0b5df9de -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.5.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 879f17bd-6d4a-48b4-8de7-cca31542ddfe -->

The deposit rate limits are:

- `maxAmount`: 50 million USDC
- `slope`: 25 million USDC per day

###### A.6.1.1.2.2.6.1.3.1.5.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 3c8495c0-5a34-48e6-9442-0c11420e2c79 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.5.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: dc4a21a8-0051-43a8-a43f-f2aefd6aa7d4 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.5.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 6428151d-e10c-49c1-b6df-2d4354c5a5cb -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.5.2 - Ethereum Mainnet - Aave Core v3 RLUSD Instance Configuration Document [Core]  <!-- UUID: 6b5a19f9-7810-4066-b2ca-df7eff376971 -->

The documents herein contain the Instance Configuration Document for the Aave Core v3 RLUSD Instance.

###### A.6.1.1.2.2.6.1.3.1.5.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 0414a985-558c-4b0c-910a-8cdc6d16afd9 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.5.2.2 - Parameters [Core]  <!-- UUID: efb946ad-f34b-4794-a3a1-51359518ad8f -->

The documents herein define the parameters of the Aave Core v3 RLUSD Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.5.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 4f7e9f76-1d35-49d3-99c4-f909bedf1331 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.5.2.2.1.1 - Network [Core]  <!-- UUID: 6a167e9d-cd54-4be0-8cc3-cb3a44d39dd2 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.5.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 3a20c3e1-f1ac-4bb3-bf98-7207fa344390 -->

Aave Core v3

###### A.6.1.1.2.2.6.1.3.1.5.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 59252087-9578-4b5c-9dd8-a206f5397424 -->

RLUSD

###### A.6.1.1.2.2.6.1.3.1.5.2.2.1.4 - Token [Core]  <!-- UUID: 5ef9ba8f-d51a-45a3-b2a4-51419b479dc6 -->

aEthRLUSD

###### A.6.1.1.2.2.6.1.3.1.5.2.2.2 - Contract Addresses [Core]  <!-- UUID: 79c4e91e-4f9a-4ea5-84d6-d92f76309e26 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.5.2.2.2.1 - Token Address [Core]  <!-- UUID: 9e6c6c25-b323-4406-a327-2da9de622c3b -->

`0xFa82580c16A31D0c1bC632A36F82e83EfEF3Eec0`

###### A.6.1.1.2.2.6.1.3.1.5.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 02e46eb2-5c2e-4d28-861a-aba2b729fb7a -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.2.2.6.1.3.1.5.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: ed234f28-3636-44cc-9c48-62429f67a896 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.5.2.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 6531616f-1a98-497e-aea9-674a577c3c57 -->

The inflow RateLimitID is: `0xd8ebadbd4eb7be4a44bcadbfa0d3e4ca014faa5e1973f993a4193ce396a61208`.

###### A.6.1.1.2.2.6.1.3.1.5.2.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 1979d5a0-4a01-4ac9-b735-22d7c4f849d5 -->

The outflow RateLimitID is: `0x574251b6fde351d987ce5235618a87bef48d50787414912b19ff8992cb2ae476`.

###### A.6.1.1.2.2.6.1.3.1.5.2.2.4 - Rate Limits [Core]  <!-- UUID: adeda437-130a-42d7-ae13-eba5f524fbc8 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.5.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 2826e338-7b71-4c03-8f6a-2c17fa45863f -->

The deposit rate limits are:

- `maxAmount`: 50 million RLUSD
- `slope`: 25 million RLUSD per day

###### A.6.1.1.2.2.6.1.3.1.5.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 2709008d-ca7f-45ab-a8c1-ef6bebedea30 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.5.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 5e72ea64-b12f-4dc0-afaf-e3da966a947a -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.5.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 6056f3fa-9fd0-4abc-8733-adb33cb4c725 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.5.3 - Ethereum Mainnet - Aave Horizon USDC Instance Configuration Document [Core]  <!-- UUID: 3050edfd-dd88-4fa4-91b4-4870d4fed089 -->

The documents herein contain the Instance Configuration Document for the Aave Horizon USDC Instance.

###### A.6.1.1.2.2.6.1.3.1.5.3.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 87384721-3137-429e-aeda-53edac6e6b39 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.5.3.2 - Parameters [Core]  <!-- UUID: 6df58738-91f6-412d-a06a-9d9448161903 -->

The documents herein define the parameters of the Aave Horizon USDC Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.5.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 0feddcb0-9621-4d77-be92-234469d95599 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.5.3.2.1.1 - Network [Core]  <!-- UUID: f519baad-ab33-453a-93f0-8c191f120ea7 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.5.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 5eb9bb64-1e7a-4160-a105-d23752979bf1 -->

Aave Horizon

###### A.6.1.1.2.2.6.1.3.1.5.3.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 2ef8ee0b-a046-409a-9179-800d8deee24d -->

USDC

###### A.6.1.1.2.2.6.1.3.1.5.3.2.1.4 - Token [Core]  <!-- UUID: 349e2499-1e49-4382-b028-0296907de7eb -->

aHorRwaUSDC

###### A.6.1.1.2.2.6.1.3.1.5.3.2.2 - Contract Addresses [Core]  <!-- UUID: a0574f24-3165-48dd-98e4-bacdb83724ac -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.5.3.2.2.1 - Token Address [Core]  <!-- UUID: 6a88f6e1-07be-4994-b7c5-a9f7a9b0d2cc -->

`0x68215B6533c47ff9f7125aC95adf00fE4a62f79e`

###### A.6.1.1.2.2.6.1.3.1.5.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 8c65206c-cba3-4e4b-bb97-7ce46b5bcf91 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.5.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: 4fc579d0-f95b-4776-adcf-9773a3ee07ce -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.5.3.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 69a9863f-cacc-4d15-bcc6-6cafbf70e1b5 -->

The inflow RateLimitID is: `0x3edeff8ad9d5510b3b4ff6dddd278ffc0f8ec084f9d49d9dd0d2936054dd27ca`.

###### A.6.1.1.2.2.6.1.3.1.5.3.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: b55b4606-d7ad-485d-80b5-55fccdb53af2 -->

The outflow RateLimitID is: `0xb890cfc1ed93b136aef2cb34337fae5000d57dd88285b4fd6f886e5a06ede5bc`.

###### A.6.1.1.2.2.6.1.3.1.5.3.2.4 - Rate Limits [Core]  <!-- UUID: b43cdb63-c017-4777-a184-bf255fd5ac97 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.5.3.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: f8ef4e6d-aa05-4b8e-abcf-47afa908b1cc -->

The deposit rate limits are:

- `maxAmount`: 50 million USDC
- `slope`: 25 million USDC per day

###### A.6.1.1.2.2.6.1.3.1.5.3.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 08e95e2d-2390-40ed-8a79-f312162f7640 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.5.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 9f7a4a5a-dcad-4fe4-9276-9352b7f8538c -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.5.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 48413486-b0ac-4dc5-bbed-6a300a581872 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.5.4 - Ethereum Mainnet - Aave Horizon RLUSD Instance Configuration Document [Core]  <!-- UUID: 15200deb-9894-4f54-95b6-7bab90a6f395 -->

The documents herein contain the Instance Configuration Document for the Aave Horizon RLUSD Instance.

###### A.6.1.1.2.2.6.1.3.1.5.4.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: b78f0da7-001e-43d0-acd0-2704ad5f831c -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.5.4.2 - Parameters [Core]  <!-- UUID: 9c98bbee-a499-48e8-9155-4b140d0f5cb6 -->

The documents herein define the parameters of the Aave Horizon RLUSD Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.5.4.2.1 - Instance Identifiers [Core]  <!-- UUID: 2a8f42ef-f0f8-483e-b4be-74e530e860b1 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.5.4.2.1.1 - Network [Core]  <!-- UUID: b80ce6f0-ca13-4ff9-88c9-e8996fc886ee -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.5.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 3e19da9b-628e-4058-bf9a-0d9fcd9c1213 -->

Aave Horizon

###### A.6.1.1.2.2.6.1.3.1.5.4.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: a77a3f3d-3ead-48b8-b774-693c698232aa -->

RLUSD

###### A.6.1.1.2.2.6.1.3.1.5.4.2.1.4 - Token [Core]  <!-- UUID: 5bc6234b-f8ef-4c2c-8571-c751a1f35d8a -->

aHorRwaRLUSD

###### A.6.1.1.2.2.6.1.3.1.5.4.2.2 - Contract Addresses [Core]  <!-- UUID: ab136525-3878-4024-995d-eb28f4b412a9 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.5.4.2.2.1 - Token Address [Core]  <!-- UUID: 9d0c9c24-3982-44a7-b96f-c1bf25c41b10 -->

`0xE3190143Eb552456F88464662f0c0C4aC67A77eB`

###### A.6.1.1.2.2.6.1.3.1.5.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 80dd4ee6-eb44-4a56-8679-5d9df5a18fb2 -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.2.2.6.1.3.1.5.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: 15c531fe-68c8-4fe6-8beb-d18fb7174da9 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.5.4.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 92f01c9e-95a2-4364-b8ec-de494a7784b6 -->

The inflow RateLimitID is: `0x5b8bd7b86efeb854063affedcbe0439d750ca9e5cf53217dd4c82b91be92524c`.

###### A.6.1.1.2.2.6.1.3.1.5.4.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 808c067c-b464-4f1f-a35c-017e373a3a59 -->

The outflow RateLimitID is: `0xa33f2f500dd7f4baa10d882fd974f197a507f7b61f245ae2689510311379df7a`.

###### A.6.1.1.2.2.6.1.3.1.5.4.2.4 - Rate Limits [Core]  <!-- UUID: 220946bd-aa72-4690-a423-e728019bda4d -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.5.4.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: f2f286bd-6cea-4010-81b5-ab11edbbe6ad -->

The deposit rate limits are:

- `maxAmount`: 50 million RLUSD
- `slope`: 25 million RLUSD per day

###### A.6.1.1.2.2.6.1.3.1.5.4.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: db19cefb-7b08-4d82-8a21-66e97b23d435 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.5.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: f8a05090-7057-43b2-ab09-13acfadf118a -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.5.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 9e8aea1d-c1c1-4493-b1f2-383a07175591 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.6 - Curve [Core]  <!-- UUID: 6a6e239a-cc18-47ab-b1e0-8cf8cf2c2957 -->

The Ethereum Mainnet Instances of the Curve Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.6.1 - Ethereum Mainnet - Curve RLUSD/USDC Pool Instance Configuration Document [Core]  <!-- UUID: 67b85f8a-3857-461d-a214-d3bf990f9111 -->

The documents herein contain the Instance Configuration Document for the Curve RLUSD/USDC Pool Instance.

###### A.6.1.1.2.2.6.1.3.1.6.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: f457fb43-c250-4111-b370-3e875e13db65 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.6.1.2 - Parameters [Core]  <!-- UUID: ef903d8d-08fe-4be2-b68f-adb87d7449e3 -->

The documents herein define the parameters of the Curve RLUSD/USDC Pool Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.6.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 49528c46-1220-46a7-b693-cf0433129077 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.6.1.2.1.1 - Network [Core]  <!-- UUID: 4b77a1d9-18bc-4144-ad5f-8b1bdf2974db -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.6.1.2.1.2 - Target Protocol [Core]  <!-- UUID: d7ad7cbd-774d-4ef7-b35c-897e1d66b766 -->

Curve

###### A.6.1.1.2.2.6.1.3.1.6.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: aadd33fa-45a8-4df8-963a-2ee40ea6075b -->

RLUSD and USDC

###### A.6.1.1.2.2.6.1.3.1.6.1.2.1.4 - Token [Core]  <!-- UUID: b787771e-42f4-4a11-b683-1be8d536546c -->

RLUSD/USDC

###### A.6.1.1.2.2.6.1.3.1.6.1.2.2 - Contract Addresses [Core]  <!-- UUID: 3a2d436e-e498-46ae-aa93-5eaf2b1c3adf -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.6.1.2.2.1 - Pool Address [Core]  <!-- UUID: 869f4a71-5a20-4e34-b718-cfe844630475 -->

`0xD001aE433f254283FeCE51d4ACcE8c53263aa186`

###### A.6.1.1.2.2.6.1.3.1.6.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 29aee46d-b94b-4402-ba84-2029422965e6 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.6.1.2.2.3 - Underlying Asset Address [Core]  <!-- UUID: bcb5e6e4-1616-4e0f-96d5-a08d4c4dda84 -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.2.2.6.1.3.1.6.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 5c5d80a6-c0cc-491c-9e4b-75480d2a7a30 -->

The specific `RateLimitID`(s) for this conduit’s inflow, outflow and swap are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 385325de-b8c3-4e9f-96ee-c8499fca7848 -->

The inflow RateLimitID is: N/A - swap only.

###### A.6.1.1.2.2.6.1.3.1.6.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 4f630380-8ca6-4ce6-9482-9af88826ea07 -->

The outflow RateLimitID is: N/A - swap only.

###### A.6.1.1.2.2.6.1.3.1.6.1.2.3.3 - Swap RateLimitID [Core]  <!-- UUID: 3edab299-1530-48bb-9c89-0a2aee6902ce -->

The swap RateLimitID is: `0x8dcb7a359e6824ce9fd1c1f50ba67cd468764f690da2589aa3c262ac142c333a`.

###### A.6.1.1.2.2.6.1.3.1.6.1.2.4 - Rate Limits [Core]  <!-- UUID: d9cb1721-0f26-41db-a929-4725ac227d3e -->

The current `maxAmount`, `slope` and `maxSlippage` for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 172836ec-2f76-4e64-96db-fb60c9885d12 -->

The deposit rate limits are:

- `maxAmount`: N/A - swap only
- `slope`: N/A - swap only

###### A.6.1.1.2.2.6.1.3.1.6.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: a3a60b38-055f-42e4-b35d-bb04eb829b67 -->

The withdrawal rate limits are:

- `maxAmount`: N/A - swap only

###### A.6.1.1.2.2.6.1.3.1.6.1.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 511cec98-4c5b-488e-8b5b-c088d04cd46b -->

The swap rate limits are:

- `maxAmount`: 20 million
- `slope`: 100 million per day
- `maxSlippage`: 0.1%

###### A.6.1.1.2.2.6.1.3.1.6.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 8dbe4e53-e70b-4b52-b607-558e9b023b56 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.6.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 7a0d7698-5f64-47f8-b81e-c2e71e6e15dc -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.6.2 - Ethereum Mainnet - Curve RLUSD/USDC Pool Instance Configuration Document [Core]  <!-- UUID: f6501dc9-f8e9-4130-9390-a1d9f142fcc7 -->

The documents herein contain the Instance Configuration Document for the Curve RLUSD/USDC Pool Instance.

###### A.6.1.1.2.2.6.1.3.1.6.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 438f0f65-8e66-40c6-a17b-b861d57da301 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.6.2.2 - Parameters [Core]  <!-- UUID: 23317c4d-a0ce-48c5-b2ac-7ce4cd93cf83 -->

The documents herein define the parameters of the Curve RLUSD/USDC Pool Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.6.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 987eb2cc-420e-40d7-b5b2-31452ed7bcc7 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.6.2.2.1.1 - Network [Core]  <!-- UUID: a4fa782e-587c-46d5-b2d0-4a77d778ab07 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.6.2.2.1.2 - Target Protocol [Core]  <!-- UUID: e727e42d-e275-4122-9ba0-fe98bb7eedcf -->

Curve

###### A.6.1.1.2.2.6.1.3.1.6.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 7b685931-6f16-40b5-ae0e-86c46751da93 -->

RLUSD and USDC

###### A.6.1.1.2.2.6.1.3.1.6.2.2.1.4 - Token [Core]  <!-- UUID: 8bc9fd15-00f7-44c5-b48d-1916ea567117 -->

RLUSD/USDC

###### A.6.1.1.2.2.6.1.3.1.6.2.2.2 - Contract Addresses [Core]  <!-- UUID: 8aecdc5f-0f1a-4394-9306-a60c2f7daf69 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.6.2.2.2.1 - Pool Address [Core]  <!-- UUID: ef88cdfb-f431-4897-b9e6-11a16c6b8188 -->

`0xD001aE433f254283FeCE51d4ACcE8c53263aa186`

###### A.6.1.1.2.2.6.1.3.1.6.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: c3b33e2f-23b6-42f9-a6d7-abb5372217ae -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.6.2.2.2.3 - Underlying Asset Address [Core]  <!-- UUID: f1c52fdb-5856-4fce-b99e-6cbcc13296b1 -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.2.2.6.1.3.1.6.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 8b1cc07a-58fd-4657-99c7-e1feecc13ab3 -->

The specific `RateLimitID`(s) for this conduit’s inflow, outflow and swap are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.2.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 6cff8544-7a7d-43a6-8db6-3f2b1939b656 -->

The inflow RateLimitID is: N/A - swap only.

###### A.6.1.1.2.2.6.1.3.1.6.2.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: e5752190-a5a0-4d6f-9738-b07898e0dccb -->

The outflow RateLimitID is: N/A - swap only.

###### A.6.1.1.2.2.6.1.3.1.6.2.2.3.3 - Swap RateLimitID [Core]  <!-- UUID: d2d15203-f105-401f-8d0b-19f67771fb1e -->

The swap RateLimitID is: `0x8dcb7a359e6824ce9fd1c1f50ba67cd468764f690da2589aa3c262ac142c333a`.

###### A.6.1.1.2.2.6.1.3.1.6.2.2.4 - Rate Limits [Core]  <!-- UUID: c9ac1f48-8dbf-4c72-8a77-27c6e8863a83 -->

The current `maxAmount`, `slope` and `maxSlippage` for this conduit’s inflow/outflow/swap are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 84d948f0-8a23-4710-a6d4-8fc094befc91 -->

The deposit rate limits are:

- `maxAmount`: N/A - swap only
- `slope`: N/A - swap only

###### A.6.1.1.2.2.6.1.3.1.6.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 91eeb3a6-3b06-4e33-b835-51614136ce2e -->

The withdrawal rate limits are:

- `maxAmount`: N/A - swap only

###### A.6.1.1.2.2.6.1.3.1.6.2.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 8885e8e3-1ab5-4b0a-998c-07e692db7054 -->

The swap rate limits are:

- `maxAmount`: 20 million
- `slope`: 100 million per day
- `maxSlippage`: 0.1%

###### A.6.1.1.2.2.6.1.3.1.6.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: fb386f16-e7f8-4cba-b10f-346c0e19b8f1 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.6.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 502790de-8ab5-4359-86e0-d40b8ceda9ff -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.6.3 - Ethereum Mainnet - Curve RLUSD/USDC Pool LP Deposits Instance Configuration Document [Core]  <!-- UUID: ea9afb08-8f81-4ee9-b9a7-321862bad5d8 -->

The documents herein contain the Instance Configuration Document for the Curve RLUSD/USDC Pool LP Deposits Instance.

###### A.6.1.1.2.2.6.1.3.1.6.3.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: d2362b8a-bbed-499c-9d76-9b646bc67024 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.6.3.2 - Parameters [Core]  <!-- UUID: 4d218b64-f137-43c1-a8b3-430e12677225 -->

The documents herein define the parameters of the Curve RLUSD/USDC Pool LP Deposits Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.6.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 5a429e97-4796-45f4-b79d-3bc370074a42 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.6.3.2.1.1 - Network [Core]  <!-- UUID: dfc15cd1-2c3f-4943-baa3-2c1a09c40c51 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.6.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 5c60815c-de1b-4cde-86b4-4c70984c8ad7 -->

Curve

###### A.6.1.1.2.2.6.1.3.1.6.3.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: f52ce77b-6823-4afe-a841-f4a50eb8093c -->

RLUSD and USDC

###### A.6.1.1.2.2.6.1.3.1.6.3.2.1.4 - Token [Core]  <!-- UUID: 104bb526-03c2-4940-bf92-019fd6cf9c9a -->

RLUSD/USDC

###### A.6.1.1.2.2.6.1.3.1.6.3.2.2 - Contract Addresses [Core]  <!-- UUID: 60cfaf1e-cfab-4869-aa7b-403a81bd9864 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.6.3.2.2.1 - Pool Address [Core]  <!-- UUID: 7e88794d-21d2-43ba-9e72-924dc4c23af5 -->

`0xD001aE433f254283FeCE51d4ACcE8c53263aa186`

###### A.6.1.1.2.2.6.1.3.1.6.3.2.2.2 - Underlying Asset Address (USDC) [Core]  <!-- UUID: b7168555-b5c9-4f72-871f-7ce226124cff -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.6.3.2.2.3 - Underlying Asset Address (RLUSD) [Core]  <!-- UUID: 99fde67c-857d-4ba1-89a5-3b237acdba6e -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.2.2.6.1.3.1.6.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: e63c5013-fbfc-40df-bfac-801f0ddb43d2 -->

The specific `RateLimitID`(s) for this conduit’s inflow, outflow and swap are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.3.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 710450c0-a5ee-4eb5-9011-0da07b39ae79 -->

The inflow RateLimitID is: `0x450c909d837693f4f47c753eb316c7221dd923fff8e28ec3cfbf1cd548f544e7`.

###### A.6.1.1.2.2.6.1.3.1.6.3.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 8a956435-6a32-407d-bb1e-1af3db54bb7b -->

The outflow RateLimitID is: `0xca9b793f7b515f76fb88684bec4850e8c12afbb7f27a81eab232c966c9eb9e96`.

###### A.6.1.1.2.2.6.1.3.1.6.3.2.4 - Rate Limits [Core]  <!-- UUID: 09b73b1b-969c-485a-822b-9b61840494bc -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.3.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 15679304-3b86-43f4-be14-d02f33f72d2d -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 RLUSD or USDC
- `slope`: 25,000,000 RLUSD or USDC per day

###### A.6.1.1.2.2.6.1.3.1.6.3.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 34276745-bc02-4e02-aaac-20284debe350 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.6.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: ca62ee2b-3ced-4798-9c39-8687f3f11bef -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.6.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 045a13d9-a6a4-4d50-8cf5-0a762252d9de -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.6.4 - Ethereum Mainnet - Curve AUSD/USDC Swaps Instance Configuration Document [Core]  <!-- UUID: 207cc62c-29ee-4a03-afd9-37f279b2c25b -->

The documents herein contain the Instance Configuration Document for the Curve AUSD/USDC Swaps Instance.

###### A.6.1.1.2.2.6.1.3.1.6.4.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 4b0df25d-62db-4165-b225-0285a56838a1 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.6.4.2 - Parameters [Core]  <!-- UUID: 73dc573f-443e-4340-bfa5-a1773a839af8 -->

The documents herein define the parameters of the Curve AUSD/USDC Swaps Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.6.4.2.1 - Instance Identifiers [Core]  <!-- UUID: 8df69912-f3f3-4225-bed8-e47865580a63 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.6.4.2.1.1 - Network [Core]  <!-- UUID: f6ec618e-7eeb-4ca2-b702-9a9c978536c4 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.6.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 196f8840-a3f0-435b-90f6-f8e0d46235f9 -->

Curve AUSD/USDC

###### A.6.1.1.2.2.6.1.3.1.6.4.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 5a3a318d-bba2-44f0-abe6-e413964e9b5d -->

USDC and AUSD

###### A.6.1.1.2.2.6.1.3.1.6.4.2.1.4 - Token [Core]  <!-- UUID: 7b862a65-b8d3-4034-a47b-649f18550393 -->

AUSDUSDC

###### A.6.1.1.2.2.6.1.3.1.6.4.2.2 - Contract Addresses [Core]  <!-- UUID: 318ca1d7-f02c-4520-97b8-0b28762f5301 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.6.4.2.2.1 - Underlying Asset Address (USDC) [Core]  <!-- UUID: ff266150-7da7-468a-b6cc-f8833c55d3b0 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.6.4.2.2.2 - Underlying Asset Address (AUSD) [Core]  <!-- UUID: f83f01f9-6963-4512-81ee-f632349a94d3 -->

`0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`

###### A.6.1.1.2.2.6.1.3.1.6.4.2.2.3 - Pool Address [Core]  <!-- UUID: 8e89d41b-075c-4a4b-bfa8-7129421fdf65 -->

`0xE79C1C7E24755574438A26D5e062Ad2626C04662`

###### A.6.1.1.2.2.6.1.3.1.6.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: 4e47589f-4860-4d14-a74e-3b4536690f83 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.4.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 75afb0be-ec4f-49c2-9b86-0a4846ab1663 -->

The inflow RateLimitID is: `0x69758792004c0221462c6e75cf130926aea2203ca8540d22f2a5e570e341bc14`.

###### A.6.1.1.2.2.6.1.3.1.6.4.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 32bd5b6f-fa63-4919-8286-ecfcf962bee1 -->

The outflow RateLimitID is: N/A.

###### A.6.1.1.2.2.6.1.3.1.6.4.2.4 - Rate Limits [Core]  <!-- UUID: 6022cee7-31ec-4356-acc7-537cda385855 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.4.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 33800c50-8d1e-4339-88a1-8c07e5c35496 -->

The deposit rate limits are:

- `maxAmount`: N/A - swaps only
- `slope`: N/A - swaps only

###### A.6.1.1.2.2.6.1.3.1.6.4.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 1a78fd44-9483-4063-bbd5-80fef10bf85a -->

The withdrawal rate limits are:

- `maxAmount`: N/A - swaps only

###### A.6.1.1.2.2.6.1.3.1.6.4.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: 5fdeea04-0bf6-475f-b7ed-1232040c6a32 -->

The swap rate limits are:

- `maxAmount`: 5,000,000 USDC/AUSD
- `slope`: 100,000,000 USDC/AUSD per day
- `maxSlippage`: 0.1%

###### A.6.1.1.2.2.6.1.3.1.6.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 337c72cd-b626-458f-a4d3-a7e855a0c4fa -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.6.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 77e3d9d0-7a70-4811-b60a-7bb91202e5df -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.6.5 - Ethereum Mainnet - Curve AUSD/USDC LP Instance Configuration Document [Core]  <!-- UUID: 6d7f468e-e32c-4077-8dbc-66095e7b8f84 -->

The documents herein contain the Instance Configuration Document for the Curve AUSD/USDC LP Instance.

###### A.6.1.1.2.2.6.1.3.1.6.5.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 0ba7698b-d0ed-413e-8652-c2822c3ea7c3 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.6.5.2 - Parameters [Core]  <!-- UUID: 5beb96b1-7975-42e2-90b6-67b92c01b60b -->

The documents herein define the parameters of the Curve AUSD/USDC LP Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.6.5.2.1 - Instance Identifiers [Core]  <!-- UUID: 1e8008c4-10c5-443e-85ae-36140449783f -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.6.5.2.1.1 - Network [Core]  <!-- UUID: f16f6599-e1f2-482e-a1d0-7fac482abec3 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.6.5.2.1.2 - Target Protocol [Core]  <!-- UUID: 79b0bed6-362b-4fb3-a3a1-0accb41ad704 -->

Curve AUSD/USDC

###### A.6.1.1.2.2.6.1.3.1.6.5.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 1c81fb59-4bfa-4635-ad2c-c3b0901128d6 -->

USDC and AUSD

###### A.6.1.1.2.2.6.1.3.1.6.5.2.1.4 - Token [Core]  <!-- UUID: 19bd5fb8-1f47-4be9-823c-8eea21bcab20 -->

AUSDUSDC

###### A.6.1.1.2.2.6.1.3.1.6.5.2.2 - Contract Addresses [Core]  <!-- UUID: 37940251-3bd5-47f2-abe0-03aa036f2e51 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.6.5.2.2.1 - Underlying Asset Address (USDC) [Core]  <!-- UUID: 31b957ea-deb5-4143-a597-a5a094bd8c25 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.6.5.2.2.2 - Underlying Asset Address (AUSD) [Core]  <!-- UUID: 06c5e743-4d01-4325-a4c1-17680d1a79c1 -->

`0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`

###### A.6.1.1.2.2.6.1.3.1.6.5.2.2.3 - Pool Address [Core]  <!-- UUID: 63058463-a3d7-4a74-8a1b-a43e6cc20baa -->

`0xE79C1C7E24755574438A26D5e062Ad2626C04662`

###### A.6.1.1.2.2.6.1.3.1.6.5.2.3 - Rate Limit IDs [Core]  <!-- UUID: 3c1c8cd1-ebaf-4138-a1c3-293af4849223 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.5.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: e1565876-ecba-467b-9890-ebde7cf956d1 -->

The inflow RateLimitID is: `0x67abf1af1d8f5f281e50b2b1f4587dacee38c7c1325bab70aa144056ba560538`.

###### A.6.1.1.2.2.6.1.3.1.6.5.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 84b03f91-b152-4e24-a10c-4729908df9da -->

The outflow RateLimitID is: `0x8b0ebe103264ec6caf8c9a6b03eeb13f101d3d1ece1fe8b70b17efb9153bb3fb`.

###### A.6.1.1.2.2.6.1.3.1.6.5.2.4 - Rate Limits [Core]  <!-- UUID: 6ce30263-7c13-4b45-ab75-e2b79e678272 -->

The current `maxAmount` and `slope` for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.5.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: fe7ce511-f51b-4ed8-8ea1-30c4ae30e0bf -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 USDC/AUSD
- `slope`: 25,000,000 USDC/AUSD per day

###### A.6.1.1.2.2.6.1.3.1.6.5.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 5968dc38-0ac9-4c05-83b1-117fbe71c64c -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.6.5.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: bff6b95b-dad1-4d5a-a8cf-26bd6944d93e -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.6.5.3 - Instance-specific Operational Processes [Core]  <!-- UUID: ce053035-2796-4461-bbc8-b3c0ee0bcba3 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.6.6 - Ethereum Mainnet - Curve PYUSD/USDS Swaps Instance Configuration Document [Core]  <!-- UUID: f168c4a8-f526-471e-8410-4f3f339e99d5 -->

The documents herein contain the Instance Configuration Document for the Curve PYUSD/USDS Swaps Instance.

###### A.6.1.1.2.2.6.1.3.1.6.6.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: a0f62040-5099-4e38-8db7-2fee0953ed21 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.6.6.2 - Parameters [Core]  <!-- UUID: 84afba1f-7050-4c57-94dc-f0d4ff5e976b -->

The documents herein define the parameters of the Curve PYUSD/USDS Swaps Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.6.6.2.1 - Instance Identifiers [Core]  <!-- UUID: 83097786-002d-405f-966e-5502f4ef3d78 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.6.6.2.1.1 - Network [Core]  <!-- UUID: 18b5144f-0fb4-4e58-ab17-ad5f4656a080 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.6.6.2.1.2 - Target Protocol [Core]  <!-- UUID: 2d7dbfa2-3dd3-43ee-9613-d9c4d6b8f830 -->

Curve PYUSD/USDS

###### A.6.1.1.2.2.6.1.3.1.6.6.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 78ade625-90af-4a60-a4da-d261f12cdca9 -->

USDS and PYUSD

###### A.6.1.1.2.2.6.1.3.1.6.6.2.1.4 - Token [Core]  <!-- UUID: 61025ace-5e86-4671-88e9-5e6db1170890 -->

PYUSD/USDS

###### A.6.1.1.2.2.6.1.3.1.6.6.2.2 - Contract Addresses [Core]  <!-- UUID: 8bd50aee-8888-4a08-ac32-49ed69ef2b6f -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.6.6.2.2.1 - Underlying Asset Address (USDS) [Core]  <!-- UUID: 77037711-fb38-435a-85e1-a177701710e9 -->

`0xdC035D45d973E3EC169d2276DDab16f1e407384F`

###### A.6.1.1.2.2.6.1.3.1.6.6.2.2.2 - Underlying Asset Address (PYUSD) [Core]  <!-- UUID: f02df9d0-e495-4896-ba88-806dca35d82c -->

`0x6c3ea9036406852006290770BEdFcAbA0e23A0e8`

###### A.6.1.1.2.2.6.1.3.1.6.6.2.2.3 - Pool Address [Core]  <!-- UUID: dc239910-11ff-4b37-bffe-a98af705090b -->

`0xA632D59b9B804a956BfaA9b48Af3A1b74808FC1f`

###### A.6.1.1.2.2.6.1.3.1.6.6.2.3 - Rate Limit IDs [Core]  <!-- UUID: 2a4bd826-18f2-4a58-b311-6fabb52b4f28 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.6.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 2383066f-a8f7-4a7e-a953-5915ef366f60 -->

The inflow RateLimitID is: `0x495d2d5778d2cbf1ff13da2634eb38b1c7cfc08d120249eb740c796e40d80fb1`.

###### A.6.1.1.2.2.6.1.3.1.6.6.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 72f0d0c1-4f88-4b4d-86ce-f7b558f05fd5 -->

The outflow RateLimitID is: N/A.

###### A.6.1.1.2.2.6.1.3.1.6.6.2.4 - Rate Limits [Core]  <!-- UUID: 4693cf03-c0fe-4ede-a83c-9af83d3cdcee -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.6.6.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: ad363791-a7e1-4a0c-8a8a-6102994c2876 -->

The deposit rate limits are:

- `maxAmount`: N/A - swaps only
- `slope`: N/A - swaps only

###### A.6.1.1.2.2.6.1.3.1.6.6.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: b0b22bed-1cb0-43cd-bbdc-5f7fa48ebdab -->

The withdrawal rate limits are:

- `maxAmount`: N/A - swaps only

###### A.6.1.1.2.2.6.1.3.1.6.6.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: e3773f0c-33c5-4f55-93bf-69730b447deb -->

The swap rate limits are:

- `maxAmount`: 5,000,000 USDS/PYUSD
- `slope`: 100,000,000 USDS/PYUSD per day
- `maxSlippage`: 0.1%

###### A.6.1.1.2.2.6.1.3.1.6.6.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: f484c818-9696-4cde-994d-d4218277a486 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.6.6.3 - Instance-specific Operational Processes [Core]  <!-- UUID: fb16c677-3521-4250-8c9d-3e68155f9afd -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.7 - Morpho [Core]  <!-- UUID: d03f121c-7853-4dc7-85d8-f231aaa64a68 -->

The Ethereum Mainnet Instances of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.7.1 - Ethereum Mainnet - Morpho Grove x Steakhouse High Yield Vault USDC Instance Configuration Document [Core]  <!-- UUID: 29cb8322-96f5-4f18-b4fe-eb31826af580 -->

The documents herein contain the Instance Configuration Document for the Morpho Grove x Steakhouse High Yield Vault USDC Instance.

###### A.6.1.1.2.2.6.1.3.1.7.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 6127e31a-798c-41eb-90d5-044d9b214d2a -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.7.1.2 - Parameters [Core]  <!-- UUID: 7cdf8908-1adc-421d-9c71-37d138f99b20 -->

The documents herein define the parameters of the Morpho Grove x Steakhouse High Yield Vault USDC Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.7.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 260778ff-223a-4aca-a262-cd20aafe5f49 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.7.1.2.1.1 - Network [Core]  <!-- UUID: f4e45e27-3775-46e7-9f7f-ada5fb72bc27 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.7.1.2.1.2 - Target Protocol [Core]  <!-- UUID: a9e1a42f-d92b-4658-814a-2ad449de6eb5 -->

Morpho

###### A.6.1.1.2.2.6.1.3.1.7.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: a810c912-a460-4a1f-ac0d-838eb6ff2f04 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.7.1.2.1.4 - Token [Core]  <!-- UUID: 4e19d59e-628e-4478-a986-6418879f03b2 -->

grove-bbqUSDC

###### A.6.1.1.2.2.6.1.3.1.7.1.2.2 - Contract Addresses [Core]  <!-- UUID: 94042273-29a0-4538-833b-1ea63b737db1 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.7.1.2.2.1 - Token Address [Core]  <!-- UUID: dcdff78c-809f-4ec8-80a2-36c124ca9ae8 -->

`0xBEEf2B5FD3D94469b7782aeBe6364E6e6FB1B709`

###### A.6.1.1.2.2.6.1.3.1.7.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: ff7b0875-7f6d-4b18-b609-34eec3f725a0 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.7.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 35269818-4f06-49a8-8675-f7da3f616976 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: e258f0cd-0b47-464a-bcdb-78fdfb3451a2 -->

The inflow RateLimitID is: `0x82fb6a87781d1c18617960e9528d0633bfbc534f5ae8109347f10bb49a2f4f19`.

###### A.6.1.1.2.2.6.1.3.1.7.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: a7ad7e2a-5c2e-4231-94d4-cdd14d526c1d -->

**Outflow RateLimitID** _(Core)_ - The outflow RateLimitID is: `0xe668276e49fbcb8fc24c716adf328ec4602ad894aaeabc608d172aadfd5cd485`.

###### A.6.1.1.2.2.6.1.3.1.7.1.2.4 - Rate Limits [Core]  <!-- UUID: a907ce48-a651-4cc9-a382-82e989f3ee50 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: dbb8ef9e-c2ce-43b5-b320-bae57f6cb993 -->

The deposit rate limits are:

- `maxAmount`: 20,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.7.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: b4ca4845-a846-479b-aaf8-e83e73bf25f7 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.7.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 1ab38f81-28f4-4262-8529-37ef7d43e087 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.7.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 9c79b4b9-8584-4414-bddf-36158d01dc20 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.7.2 - Ethereum Mainnet - Grove x Steakhouse USDC Morpho Vault v2 Instance Configuration Document [Core]  <!-- UUID: 6ec606f0-bc47-4f36-8591-75784bb78b00 -->

The documents herein contain the Instance Configuration Document for the Grove x Steakhouse USDC Morpho Vault v2 Instance.

###### A.6.1.1.2.2.6.1.3.1.7.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 87d15c86-c604-465b-b920-050a1aabcb0c -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.7.2.2 - Parameters [Core]  <!-- UUID: 74f5efe4-582c-4b44-9235-71495f81ae51 -->

The documents herein define the parameters of the Grove x Steakhouse USDC Morpho Vault v2 Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.7.2.2.1 - Instance Identifiers [Core]  <!-- UUID: b9e733de-e621-42eb-b000-37195c47f395 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.7.2.2.1.1 - Network [Core]  <!-- UUID: 7d5a86c8-1d10-49cc-9547-58bf93fb7eb0 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.7.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 25ee9e5c-32d3-488a-82c2-495496964b23 -->

Grove x Steakhouse USDC High Yield Vault V2

###### A.6.1.1.2.2.6.1.3.1.7.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: d1a9b070-f3c7-48e7-9bff-f2f0e17acc14 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.7.2.2.1.4 - Token [Core]  <!-- UUID: 45924aa7-76e2-4375-9b20-cd781f0a8e09 -->

grove-bbqUSDC

###### A.6.1.1.2.2.6.1.3.1.7.2.2.2 - Contract Addresses [Core]  <!-- UUID: a6b3dc78-d595-4224-ac9f-bc38d87f683b -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.7.2.2.2.1 - Token Address [Core]  <!-- UUID: 3c0cd2b5-035d-460d-92dd-b45c1e7a64a1 -->

`0xBeefF08dF54897e7544aB01d0e86f013DA354111`

###### A.6.1.1.2.2.6.1.3.1.7.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 76adcd24-8473-4e8e-a42c-0c7583e13936 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.7.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 23ecc971-d297-4a06-98da-1e7620f5a823 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.2.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: f6b59efd-b87c-4d35-b416-f582359c98ac -->

The inflow RateLimitID is: `0xe9ff67ad8829919752eee93c75433e7e23f3460ca6b1d9576fae94f669fbc4d6`.

###### A.6.1.1.2.2.6.1.3.1.7.2.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 76749308-cb2d-4c39-ad38-90c3baebb6e8 -->

The outflow RateLimitID is: `0xb6204f88cd26e1d2b5c27fe0beb10cc2c6a33aac17f228baffcb5cc3c8429a7b`.

###### A.6.1.1.2.2.6.1.3.1.7.2.2.4 - Rate Limits [Core]  <!-- UUID: fdf5c673-201d-4866-8e95-d041f481f3cc -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 506f5294-ad79-4ace-98b9-75d694072a3d -->

The deposit rate limits are:

- `maxAmount`: 20,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.7.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 7e38063c-c6a7-4d45-9344-bd3b22047019 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.7.2.2.4.3 - Max Exchange Rate [Core]  <!-- UUID: 6894aa1a-4e6d-4372-a989-34258aeddf00 -->

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 2 USDC.

- `setMaxExchangeRate(GROVE_X_STEAKHOUSE_USDC_V2, 1e18, 2e6)`

###### A.6.1.1.2.2.6.1.3.1.7.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 0de4574b-adc6-4e83-9a8d-e6bcf97bf73e -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.7.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: feabeb3e-73d4-4acc-acb9-33cd0cc5bf53 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.7.3 - Ethereum Mainnet - Steakhouse PYUSD Morpho Vault Instance Configuration Document [Core]  <!-- UUID: 0b7e1d3d-1f56-48a6-9729-88479aa5ff92 -->

The documents herein contain the Instance Configuration Document for the Steakhouse PYUSD Morpho Vault Instance.

###### A.6.1.1.2.2.6.1.3.1.7.3.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: b9d9d24c-2d3a-4eec-88fe-2b7a47ab369c -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.7.3.2 - Parameters [Core]  <!-- UUID: f7048cf9-6517-48b9-8768-74a0160a8cea -->

The documents herein define the parameters of the Steakhouse PYUSD Morpho Vault Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.7.3.2.1 - Instance Identifiers [Core]  <!-- UUID: 42f30ffc-3820-4965-a112-1ab3c303d51b -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.7.3.2.1.1 - Network [Core]  <!-- UUID: 99b185bd-c32d-4454-9c22-579f6ac4fd15 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.7.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 0963963e-de9c-4470-9d89-6932657f8283 -->

Steakhouse PYUSD Morpho Vault

###### A.6.1.1.2.2.6.1.3.1.7.3.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: f1b5c4b3-9d93-4c2e-b7fb-6e42f5987ea5 -->

PYUSD

###### A.6.1.1.2.2.6.1.3.1.7.3.2.1.4 - Token [Core]  <!-- UUID: 051f1879-4b97-41cb-90be-1ac54da4cab4 -->

grove-bbqPYUSD

###### A.6.1.1.2.2.6.1.3.1.7.3.2.2 - Contract Addresses [Core]  <!-- UUID: 958415c3-8983-4cd1-926e-5ec2029926b3 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.7.3.2.2.1 - Token Address [Core]  <!-- UUID: b7a5cbbf-15c4-4b0e-ba18-4dfa9994a212 -->

`0xd8A6511979D9C5D387c819E9F8ED9F3a5C6c5379`

###### A.6.1.1.2.2.6.1.3.1.7.3.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: c9d27694-0ebd-4f06-b5b3-07c3879bf438 -->

`0x6c3ea9036406852006290770BEdFcAbA0e23A0e8`

###### A.6.1.1.2.2.6.1.3.1.7.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: d0a539f7-83a1-4aef-9a4a-050d4ba8596a -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.3.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 288e9dc2-d8a6-40c9-b501-aec06f7c1e11 -->

The inflow RateLimitID is: `0xfc4e1f8ba7b0389a287411c3f6b97cc0ec60fb2816bfaa31e12a21561486321a`.

###### A.6.1.1.2.2.6.1.3.1.7.3.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 79ed24a8-d0ca-4da7-861a-66ae676eafcb -->

The outflow RateLimitID is: `0xa0c827fea02219c83969babf0bd29df5bb5fe923e6b38491a5eea797984995e8`.

###### A.6.1.1.2.2.6.1.3.1.7.3.2.4 - Rate Limits [Core]  <!-- UUID: 72af86dd-3a15-4245-8a90-5ae8100f49d9 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.3.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: aec6eb4d-103c-49e0-9d05-befc5dda716c -->

The deposit rate limits are:

- `maxAmount`: 20,000,000 PYUSD
- `slope`: 20,000,000 PYUSD per day

###### A.6.1.1.2.2.6.1.3.1.7.3.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 77112a8a-c39e-49da-b476-c97ebcb2d197 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.7.3.2.4.3 - Max Exchange Rate [Core]  <!-- UUID: c5fa2d90-df64-406e-a53d-9694d448b161 -->

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 4 PYUSD (current share price is 2).

- `setMaxExchangeRate(STEAKHOUSE_PYUSD_MAIN, 1e18, 4e6)`

###### A.6.1.1.2.2.6.1.3.1.7.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 9f9f27c9-ad65-4afe-8ef7-de0eacfe3acc -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.7.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: fa6a6475-92d9-48b1-9033-6b1c196d9ead -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.7.4 - Ethereum Mainnet - Grove x Steakhouse AUSD Morpho Vault V2 Instance Configuration Document [Core]  <!-- UUID: 2c21462b-2925-48d8-9578-5fc21aa96563 -->

The documents herein contain the Instance Configuration Document for the Grove x Steakhouse AUSD Morpho Vault V2 Instance.

###### A.6.1.1.2.2.6.1.3.1.7.4.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 72d9d7fd-d236-43b7-9f02-77686a08be2b -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.7.4.2 - Parameters [Core]  <!-- UUID: 284c435d-c60f-4d62-82e6-f70b9fd18170 -->

The documents herein define the parameters of the Grove x Steakhouse AUSD Morpho Vault V2 Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.7.4.2.1 - Instance Identifiers [Core]  <!-- UUID: 0a6567d0-f433-4403-9bf0-e5f420e25759 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.7.4.2.1.1 - Network [Core]  <!-- UUID: b2ce1772-2114-4042-873f-6434878c7b7e -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.7.4.2.1.2 - Target Protocol [Core]  <!-- UUID: 70d6adc5-11a6-4058-887c-d277141bb1a8 -->

Grove x Steakhouse AUSD Morpho Vault

###### A.6.1.1.2.2.6.1.3.1.7.4.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 9cba6bc2-2481-4fca-922c-160b02c59c70 -->

AUSD

###### A.6.1.1.2.2.6.1.3.1.7.4.2.1.4 - Token [Core]  <!-- UUID: 3ae27c28-7005-4b95-84e9-2eadfd88987a -->

grove-bbqAUSD

###### A.6.1.1.2.2.6.1.3.1.7.4.2.2 - Contract Addresses [Core]  <!-- UUID: aee5af4c-bc06-4e40-a046-61c8fae70d5f -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.7.4.2.2.1 - Token Address [Core]  <!-- UUID: 69648727-b4ab-45e7-85f9-c2846917d944 -->

`0xBEEfF0d672ab7F5018dFB614c93981045D4aA98a`

###### A.6.1.1.2.2.6.1.3.1.7.4.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 5ec16337-978a-4b21-bf47-326db289a2ef -->

`0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`

###### A.6.1.1.2.2.6.1.3.1.7.4.2.3 - Rate Limit IDs [Core]  <!-- UUID: 112d2a3d-0241-446e-96e8-36a25715c275 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.4.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: e7301d05-fbbf-4786-bd6e-55bfc1d4247a -->

The inflow RateLimitID is: `0x09b5f924263c1b33d619ff1c9c794ddf57bc2eb0f618e2cf5cfd838abecb541d`.

###### A.6.1.1.2.2.6.1.3.1.7.4.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 0e535792-539f-42a5-b8a0-d309fd7ac3d0 -->

The outflow RateLimitID is: `0xdd975e5dc9904260242e80bbe7035784e9108c619e23f21b62342fae3226e0fe`.

###### A.6.1.1.2.2.6.1.3.1.7.4.2.4 - Rate Limits [Core]  <!-- UUID: 194a91d6-902b-4e2f-b416-cfd681addbde -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.4.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: c2b5471f-85af-4c3f-91af-3bf8d9492178 -->

The deposit rate limits are:

- `maxAmount`: 20,000,000 AUSD
- `slope`: 20,000,000 AUSD per day

###### A.6.1.1.2.2.6.1.3.1.7.4.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: ee2bb8e1-0e9d-4372-875c-22c8fbeafdf2 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.7.4.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: b8064e80-74cf-428e-9783-e03ed597a1f7 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.7.4.3 - Instance-specific Operational Processes [Core]  <!-- UUID: ac75dba3-94e0-4bd9-8a4a-24eb93c488dd -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.7.4.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 32ccb033-854c-45b2-b5f4-364e5eabc5f5 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.7.4.4.1 - Max Exchange Rate [Core]  <!-- UUID: c7a016f1-0d8d-47ad-b91e-39d1a285b149 -->

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 2 AUSD:

- `setMaxExchangeRate(GROVE_X_STEAKHOUSE_AUSD_V2, 1e18, 2e6)`

###### A.6.1.1.2.2.6.1.3.1.7.5 - Ethereum Mainnet - Sentora PYUSD Morpho Vault V2 Instance Configuration Document [Core]  <!-- UUID: 3e940e02-80eb-4e37-bce6-95939089da46 -->

The documents herein contain the Instance Configuration Document for the Sentora PYUSD Morpho Vault V2 Instance.

###### A.6.1.1.2.2.6.1.3.1.7.5.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 3fd05c9a-1d93-47f6-967d-6edb31f522fd -->

`Pending`

###### A.6.1.1.2.2.6.1.3.1.7.5.2 - Parameters [Core]  <!-- UUID: 7b251172-7a60-4240-af72-cacaca9fe3cc -->

The documents herein define the parameters of the Sentora PYUSD Morpho Vault V2 Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.7.5.2.1 - Instance Identifiers [Core]  <!-- UUID: 3d387fde-f4b9-47c0-8852-f4d9367c0369 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.7.5.2.1.1 - Network [Core]  <!-- UUID: 0075ec52-7324-41b5-8849-e91bac55e742 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.7.5.2.1.2 - Target Protocol [Core]  <!-- UUID: be9b2600-3021-4bb6-9eaf-ba92f17ccd61 -->

Sentora PYUSD Morpho Vault V2

###### A.6.1.1.2.2.6.1.3.1.7.5.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 8ba12c10-ec4f-4f37-a59c-4c34e14e1a8d -->

PYUSD

###### A.6.1.1.2.2.6.1.3.1.7.5.2.1.4 - Token [Core]  <!-- UUID: dbf0b180-07ad-4a4b-8cdb-b2c1ae7f2c7a -->

senPYUSDmain

###### A.6.1.1.2.2.6.1.3.1.7.5.2.2 - Contract Addresses [Core]  <!-- UUID: 6a5becdf-2cb6-44c3-b93a-793072d5ff7b -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.7.5.2.2.1 - Token Address [Core]  <!-- UUID: 9a0baa90-6aec-4be5-9ae5-4d3c790473a8 -->

`0xb576765fB15505433aF24FEe2c0325895C559FB2`

###### A.6.1.1.2.2.6.1.3.1.7.5.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 412793f2-1e8e-490c-8604-3c457d54d6ed -->

`0x6c3ea9036406852006290770BEdFcAbA0e23A0e8`

###### A.6.1.1.2.2.6.1.3.1.7.5.2.3 - Rate Limit IDs [Core]  <!-- UUID: fce963cb-ade1-463e-a88f-898a30586e51 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.5.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 31d24068-b9bf-43d7-8333-df129e00ee61 -->

The inflow RateLimitID is: `0x4dc0c7cd471560aa12324cb36f720d7d301ef230d3ae772ae07b681725ae7b66`

###### A.6.1.1.2.2.6.1.3.1.7.5.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: cdd99b5b-34aa-42d5-b93a-0abda5ae7f0f -->

The outflow RateLimitID is: `0x8edef92c8bf76460b6b832a88c63768022ac5aa2bd862fb858905a0f024bff8b`

###### A.6.1.1.2.2.6.1.3.1.7.5.2.4 - Rate Limits [Core]  <!-- UUID: b94aa9b1-62c6-40dc-8b92-cc677ebac016 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.5.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 0a4b26e1-5757-4ed9-bfc5-2614cc79500f -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 PYUSD
- `slope`: 50,000,000 PYUSD per day

###### A.6.1.1.2.2.6.1.3.1.7.5.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 3d7d307c-ffdc-4ca3-b9fa-951b02d46e3f -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.7.5.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 143d4637-38b8-404c-ba4c-932796445fc8 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.7.5.2.5.1 - Maximum Exposure [Core]  <!-- UUID: 8c1e6098-3342-4d00-b314-d4e87f005dc2 -->

The Maximum Exposure for this Instance is 0 USD.

###### A.6.1.1.2.2.6.1.3.1.7.5.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 4eb5ab52-f412-4d4f-8d9e-5ac9b883eb77 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.7.5.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 8f2a06dd-60cb-4930-9f15-e8dae35444a9 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.7.5.4.1 - Max Exchange Rate [Core]  <!-- UUID: 1f14f407-9eeb-4e6b-bf6e-c837b5560f28 -->

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 3 PYUSD:

- `setMaxExchangeRate(SENTORA_PYUSD_MAIN_V2, 1e18, 3e6)`

###### A.6.1.1.2.2.6.1.3.1.7.6 - Ethereum Mainnet - Sentora RLUSD Morpho Vault V2 Instance Configuration Document [Core]  <!-- UUID: dff6df5f-f8ab-4df1-be1e-f71510c3534e -->

The documents herein contain the Instance Configuration Document for the Sentora RLUSD Morpho Vault V2 Instance.

###### A.6.1.1.2.2.6.1.3.1.7.6.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 35bdc1b6-604d-44ad-a577-ceb33bc20bd9 -->

`Pending`

###### A.6.1.1.2.2.6.1.3.1.7.6.2 - Parameters [Core]  <!-- UUID: da718c05-b351-43dd-a12a-75fe5bc0b4cf -->

The documents herein define the parameters of the Sentora RLUSD Morpho Vault V2 Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.7.6.2.1 - Instance Identifiers [Core]  <!-- UUID: 958bd3b4-0650-44fc-8765-28392fe92df3 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.7.6.2.1.1 - Network [Core]  <!-- UUID: 8baa615c-fc38-4bf7-8c44-47a6bb168ad8 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.7.6.2.1.2 - Target Protocol [Core]  <!-- UUID: bfc9f2f7-e69f-4685-b666-57bb2d55442f -->

Sentora RLUSD Morpho Vault V2

###### A.6.1.1.2.2.6.1.3.1.7.6.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 0b1dbb71-5087-4db2-98e1-f4aafe4e46b5 -->

RLUSD

###### A.6.1.1.2.2.6.1.3.1.7.6.2.1.4 - Token [Core]  <!-- UUID: e7b16e69-cfb2-4877-a0c2-9cbc7f4ff1ff -->

senRLUSDv2

###### A.6.1.1.2.2.6.1.3.1.7.6.2.2 - Contract Addresses [Core]  <!-- UUID: d2e8af21-8db9-43b3-8f52-7e080897d54e -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.7.6.2.2.1 - Token Address [Core]  <!-- UUID: dde53de4-3778-44b3-9f65-064eaab3bf93 -->

`0x6dC58a0FdfC8D694e571DC59B9A52EEEa780E6bf`

###### A.6.1.1.2.2.6.1.3.1.7.6.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: b041fa2f-e7cd-4c64-98d0-a1b67f50d6a2 -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.2.2.6.1.3.1.7.6.2.3 - Rate Limit IDs [Core]  <!-- UUID: 991d7839-4dfd-466f-aafd-8c397cd7af6b -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.6.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: a5775dc3-6444-4234-825d-7e0ae6b05f6b -->

The inflow RateLimitID is: `0x944bbb34c3717aacc72419f43d62f5a01d2ebd7a9157ba9975fd7d971deb803f`

###### A.6.1.1.2.2.6.1.3.1.7.6.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 2441cde7-6e2e-47d9-9fd3-62b1bfbb9c9c -->

The outflow RateLimitID is: `0xfc41a8cf89ec93b54bbf6960204c29c48a7ed98ec4a88dade68149dee919e788`

###### A.6.1.1.2.2.6.1.3.1.7.6.2.4 - Rate Limits [Core]  <!-- UUID: 5ecbe8da-00f2-4d72-ab79-6276eae3bc0f -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.6.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: c7c4c3a1-ca25-4e9e-b4ab-cbcd01519535 -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 RLUSD
- `slope`: 50,000,000 RLUSD per day

###### A.6.1.1.2.2.6.1.3.1.7.6.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 3593ce57-8cf0-42c8-b0ce-0bfef547e4a6 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.7.6.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 55c42f45-b94d-4e4d-959f-ae1cc1880fc5 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.7.6.2.5.1 - Maximum Exposure [Core]  <!-- UUID: 4e3fae3f-b450-4f0b-bff4-4f4767c8f7a7 -->

The Maximum Exposure for this Instance is 0 USD.

###### A.6.1.1.2.2.6.1.3.1.7.6.3 - Instance-specific Operational Processes [Core]  <!-- UUID: e63662b0-149e-4e80-b7e0-6cf281f85ddd -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.7.6.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 9aed2f2d-6a17-41a5-9104-bb622b3cb04e -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.7.6.4.1 - Max Exchange Rate [Core]  <!-- UUID: fd4778b5-78e7-49fc-a785-c2dfed2e5246 -->

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 3 RLUSD:

- `setMaxExchangeRate(SENTORA_RLUSD_MAIN_V2, 1e18, 3e18)`

###### A.6.1.1.2.2.6.1.3.1.7.7 - Ethereum Mainnet - Grove x Steakhouse RLUSD Morpho Vault V2 Instance Configuration Document [Core]  <!-- UUID: cfb29474-ea48-4370-aad6-23af1cf4d11a -->

The documents herein contain the Instance Configuration Document for the Grove x Steakhouse RLUSD Morpho Vault V2 Instance.

###### A.6.1.1.2.2.6.1.3.1.7.7.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: a1136418-1914-4543-aa3c-a77e7e8b60c7 -->

`Pending`

###### A.6.1.1.2.2.6.1.3.1.7.7.2 - Parameters [Core]  <!-- UUID: d4091127-bd5c-4ff6-ba9c-de7bd8553e61 -->

The documents herein define the parameters of the Grove x Steakhouse RLUSD Morpho Vault V2 Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.7.7.2.1 - Instance Identifiers [Core]  <!-- UUID: 64527d65-8389-4d0c-859c-fe2da103f62d -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.7.7.2.1.1 - Network [Core]  <!-- UUID: 74b876ee-2891-413b-bd1f-58b2c96b4585 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.7.7.2.1.2 - Target Protocol [Core]  <!-- UUID: 70e811cc-0a98-454a-b555-0f88a65187f1 -->

Grove x Steakhouse RLUSD Morpho Vault V2

###### A.6.1.1.2.2.6.1.3.1.7.7.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: b3ad456b-d6de-4ed1-8576-01366e21bd5d -->

RLUSD

###### A.6.1.1.2.2.6.1.3.1.7.7.2.1.4 - Token [Core]  <!-- UUID: 9325e9e9-4c9d-44ac-a732-64c8353bbff7 -->

grove-bbqRLUSD

###### A.6.1.1.2.2.6.1.3.1.7.7.2.2 - Contract Addresses [Core]  <!-- UUID: 02fa5674-392e-4d0c-8e42-2adc3692881c -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.7.7.2.2.1 - Token Address [Core]  <!-- UUID: 8ac9a401-96a6-4cbc-9d23-9374cb626d2b -->

`0xBeEff4fD39F8e48b6a6e475445D650cb11e9599F`

###### A.6.1.1.2.2.6.1.3.1.7.7.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: de701477-61aa-4d32-81b7-9ab044bb2b74 -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.2.2.6.1.3.1.7.7.2.3 - Rate Limit IDs [Core]  <!-- UUID: 41f9c281-d313-47d4-af75-8df48c9e260c -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.7.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: e868b5a4-e469-4e32-869d-2c904d31d221 -->

The inflow RateLimitID is: `0xf655bc101a615fbcb591acce756dacae96cb119ff1beec548d9cc5d4558ea53a`

###### A.6.1.1.2.2.6.1.3.1.7.7.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 3944007b-9f6f-4c0a-a71b-dd3a1775cd94 -->

The outflow RateLimitID is: `0xa6e68f8214d2fb32e0deb2888ef4644c36401d18605447843e4f936529f6a3cb`

###### A.6.1.1.2.2.6.1.3.1.7.7.2.4 - Rate Limits [Core]  <!-- UUID: 93fbe9e3-88b0-4160-b4cb-52b5333a0926 -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.7.7.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: adfeeede-027a-4b98-8636-c53975c4b7cf -->

The deposit rate limits are:

- `maxAmount`: 100,000,000 RLUSD
- `slope`: 100,000,000 RLUSD per day

###### A.6.1.1.2.2.6.1.3.1.7.7.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: c455e62e-79a6-478e-aa06-f35d2ab6779f -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.7.7.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: f298feba-925d-4f87-99d8-855fc7adffe0 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.7.7.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 2952337f-8152-44ca-9d3e-0363c6f2b1c9 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.7.7.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 8638d88f-8ac2-4deb-849e-6100eeea4b82 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.7.7.4.1 - Max Exchange Rate [Core]  <!-- UUID: ea2bbd07-134d-459d-bb20-2dbb756766b0 -->

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 3 RLUSD:

- `setMaxExchangeRate(GROVE_X_STEAKHOUSE_RLUSD_V2, 1e18, 3e18)`

###### A.6.1.1.2.2.6.1.3.1.8 - Securitize [Core]  <!-- UUID: b05d9fc2-9a93-4f3b-b0d8-b4f77bc294ce -->

The Ethereum Mainnet Instances of the Securitize Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.8.1 - Ethereum Mainnet - Securitize Tokenized AAA CLO Fund (STAC) Instance Configuration Document [Core]  <!-- UUID: a0c4fcd6-ebf9-4124-8767-cf14ab6ab397 -->

The documents herein contain the Instance Configuration Document for the Securitize Tokenized AAA CLO Fund (STAC) Instance.

###### A.6.1.1.2.2.6.1.3.1.8.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 96b8832b-b6b9-4550-b211-8df9adbf163c -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.8.1.2 - Parameters [Core]  <!-- UUID: 1258f424-862a-4e22-9281-658b7dcca2c5 -->

The documents herein define the parameters of the Securitize Tokenized AAA CLO Fund (STAC) Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.8.1.2.1 - Instance Identifiers [Core]  <!-- UUID: a5c55b02-742c-4172-a6d0-88155fd3b73f -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.8.1.2.1.1 - Network [Core]  <!-- UUID: ca21487e-43e1-4fd7-a67c-7389e59bf46d -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.8.1.2.1.2 - Target Protocol [Core]  <!-- UUID: f29e4e19-73d2-4a9b-812f-0226be26687a -->

Securitize

###### A.6.1.1.2.2.6.1.3.1.8.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 5e3282b6-3920-43e8-9659-ad9d0a4f2efe -->

USDC

###### A.6.1.1.2.2.6.1.3.1.8.1.2.1.4 - Token [Core]  <!-- UUID: c448bf3a-b51d-40e9-ba3c-8bdeadad1dc2 -->

STAC

###### A.6.1.1.2.2.6.1.3.1.8.1.2.2 - Contract Addresses [Core]  <!-- UUID: 9ab65d47-267a-4be6-b298-8a636b909e13 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.8.1.2.2.1 - Token Address [Core]  <!-- UUID: b6737216-3829-40ae-b033-846080f61d34 -->

`0x51C2d74017390CbBd30550179A16A1c28F7210fc`

###### A.6.1.1.2.2.6.1.3.1.8.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 19b23b6a-f8a5-4db8-8768-88b045bab3d2 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.8.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: dd63b171-c94f-4082-8719-24870cb173c1 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.8.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: ae0239af-eed4-40d6-8d21-c53bda72249d -->

The inflow RateLimitID is: `0x01ccccb0233955b3de85eca4dcc78aaf2aa6da1cf048b496e85a91396c2feab6`.

###### A.6.1.1.2.2.6.1.3.1.8.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: d451d2b1-70ea-458a-b2bb-dde38d29e9c0 -->

The outflow RateLimitID is: `0xcbb4d6e874245392c78f0f249b7dc876e5462bb0dce135a6e5c4cc21d774390b`.

###### A.6.1.1.2.2.6.1.3.1.8.1.2.4 - Rate Limits [Core]  <!-- UUID: fd676948-7b31-4f11-b4b0-933226a193e7 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.8.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: ee33b709-1239-44c3-9c94-4211433877c4 -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.8.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 3cafebb2-cf4d-4830-9787-1c2d7d7da030 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.8.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 174ba214-cfe9-4d35-83cb-3c0795e1936c -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.8.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 0f3ebd6c-2b7f-4125-aea8-68e84476da06 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.9 - Galaxy [Core]  <!-- UUID: e5507edb-8e06-48d2-a341-47de592d2a60 -->

The Ethereum Mainnet Instances of the Galaxy Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.9.1 - Ethereum Mainnet - Galaxy Arch CLOs Instance Configuration Document [Core]  <!-- UUID: 61afae62-1210-4d80-aa6c-cdb26ef0a287 -->

The documents herein contain the Instance Configuration Document for the Galaxy Arch CLOs Instance.

###### A.6.1.1.2.2.6.1.3.1.9.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 21f548d0-71cc-4a8a-8942-514e87cbd893 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.9.1.2 - Parameters [Core]  <!-- UUID: da740e11-eb97-4647-9186-8cce66532f2a -->

The documents herein define the parameters of the Galaxy Arch CLOs Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.9.1.2.1 - Instance Identifiers [Core]  <!-- UUID: b993eda4-2f51-470b-b0a9-e0213576a88d -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.9.1.2.1.1 - Network [Core]  <!-- UUID: d8cf82e0-4c80-4378-844c-ce2dd0a5d04e -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.9.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 357d0b0e-7db7-4c2c-9b06-e6e0134c4259 -->

Galaxy

###### A.6.1.1.2.2.6.1.3.1.9.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 0d3d52df-eb9b-4df4-8023-295be72f1193 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.9.1.2.1.4 - Token [Core]  <!-- UUID: 72e3fb43-419f-437a-b7f4-59ebe16ccd20 -->

GACLO-1

###### A.6.1.1.2.2.6.1.3.1.9.1.2.2 - Contract Addresses [Core]  <!-- UUID: 221c015b-f830-48d0-9c0e-dbdfcf0865bf -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.9.1.2.2.1 - Token Address (Avalanche) [Core]  <!-- UUID: 931d7521-9740-4913-8f36-52bbb856dca2 -->

`0x2C0aDFF8e114f3cA106051144353aC703D24B901`

###### A.6.1.1.2.2.6.1.3.1.9.1.2.2.2 - Deposit Address (Mainnet) [Core]  <!-- UUID: 01affe4d-8bba-4783-a6b3-ff32193b63e3 -->

`0x2E3A11807B94E689387f60CD4BF52A56857f2eDC`

###### A.6.1.1.2.2.6.1.3.1.9.1.2.2.3 - Underlying Asset Address [Core]  <!-- UUID: 44803afa-e8f9-4247-afda-a25fcedd8226 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.9.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 43ad16bf-2a53-492a-a9aa-187e5f3820ec -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.9.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: df18f3e6-bde8-4241-86d3-aa98edf3179c -->

The inflow RateLimitID is: `0x0de7fd8a7d8060b09965787f4841cca8a448925e555aaf7ecb4894782ffa2e17`.

###### A.6.1.1.2.2.6.1.3.1.9.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: be343d84-8e63-4e4e-99a3-77323db1f048 -->

The outflow RateLimitID is: N/A.

###### A.6.1.1.2.2.6.1.3.1.9.1.2.4 - Rate Limits [Core]  <!-- UUID: 23517c75-2462-4def-bab9-3a33c3c03e71 -->

The current `maxAmount` and `slope` for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.9.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 2e5f7349-fe4b-4c1b-8cc2-541d2ce86bf5 -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.9.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: c2f613ac-e271-4cbc-9ca7-f644082e5e8e -->

The withdrawal rate limits are:

- `maxAmount`: N/A
- `slope`: N/A

###### A.6.1.1.2.2.6.1.3.1.9.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: efac2756-89e0-4b0e-8313-3097c2660608 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.9.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 65650ce9-1f1f-4e51-b60b-12f17efc2e67 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.9.2 - Ethereum Mainnet - Galaxy Warehouse Instance Configuration Document [Core]  <!-- UUID: 2e3e057e-0b48-4e3f-b03d-1ed84299ccfc -->

The documents herein contain the Instance Configuration Document for the Galaxy Warehouse Instance.

###### A.6.1.1.2.2.6.1.3.1.9.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 91f2537e-d391-4e7a-9206-5f162cd6325a -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.9.2.2 - Parameters [Core]  <!-- UUID: cdcd20ed-3cc9-457f-8f26-9a3770146089 -->

The documents herein define the parameters of the Galaxy Warehouse Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.9.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 02ee19aa-2e46-4d77-90ac-a37bb0163b83 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.9.2.2.1.1 - Network [Core]  <!-- UUID: 06807734-cc8c-4e05-a069-df86fe101a0a -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.9.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 39071e33-187b-46e3-b1dc-54c70e98e742 -->

Galaxy

###### A.6.1.1.2.2.6.1.3.1.9.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: d8696c8d-94dc-4783-9da1-be62d2d7962c -->

USDC

###### A.6.1.1.2.2.6.1.3.1.9.2.2.1.4 - Token [Core]  <!-- UUID: 40cf48fc-fa14-4853-91db-334f0d5e1c2b -->

N/A

###### A.6.1.1.2.2.6.1.3.1.9.2.2.2 - Contract Addresses [Core]  <!-- UUID: 3874bdfc-77f3-4f2c-ae91-c4a4c0337c8e -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.9.2.2.2.1 - Deposit Address (Mainnet) [Core]  <!-- UUID: 51575781-6189-4bf3-9d6b-ae76fabbc2f7 -->

`0x3E23311f9FF660E3c3d87E4b7c207b3c3D7e04f0`

###### A.6.1.1.2.2.6.1.3.1.9.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 39b83634-f5b2-4b7c-9e98-d5616fad62b2 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.9.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: cc6e09bc-a2d0-4e4b-bf94-4fccebbd5995 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.9.2.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 8e16ecba-2c99-49f7-b979-a0108194873f -->

The inflow RateLimitID is: `0x110ff25f20e1f05ba3e82592752f6cd7e0ca645023d71d143b970e3689efc9f9`.

###### A.6.1.1.2.2.6.1.3.1.9.2.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: c2111eab-6850-46e1-9543-fe5d8966c9da -->

The outflow RateLimitID is: N/A.

###### A.6.1.1.2.2.6.1.3.1.9.2.2.4 - Rate Limits [Core]  <!-- UUID: 306c8538-fda8-4d3f-bf1d-ec249e4292e9 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.9.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 282c02b2-9b9d-4934-be9d-5228d50a0918 -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.9.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: c38e4cd8-1be2-475d-8670-848d8eba3078 -->

The withdrawal rate limits are:

- `maxAmount`: N/A

###### A.6.1.1.2.2.6.1.3.1.9.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 68cad9ca-620b-4aef-b47f-781d01640c87 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.9.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 6a1719f2-bd99-4407-addc-dc9e7a84bf58 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.10 - Ripple [Core]  <!-- UUID: 9b416c43-4ed8-4c13-ba9f-5f12c9c3e7a0 -->

The Ethereum Mainnet Instances of the Ripple Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.10.1 - Ethereum Mainnet - Ripple RLUSD Instance Configuration Document [Core]  <!-- UUID: 2e28c162-c608-452c-b796-4654ac1139d8 -->

The documents herein contain the Instance Configuration Document for the Ripple RLUSD Instance.

###### A.6.1.1.2.2.6.1.3.1.10.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 3860f545-4d08-45ff-b8b6-98bf78b78c3c -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.10.1.2 - Parameters [Core]  <!-- UUID: 060ff03e-4aa5-47ce-8d9c-ad6bcca8ac02 -->

The documents herein define the parameters of the Ripple RLUSD Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.10.1.2.1 - Instance Identifiers [Core]  <!-- UUID: fcccfc28-a6fe-4aaa-b0be-e34ffd36fba9 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.10.1.2.1.1 - Network [Core]  <!-- UUID: 7bf6a865-5eb4-4693-b45e-e13dc2e45ef7 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.10.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 8c0f9245-59c0-4119-b06e-461e043055f0 -->

Ripple

###### A.6.1.1.2.2.6.1.3.1.10.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: ac03ab87-6983-4202-ab96-3b467887430c -->

USDC

###### A.6.1.1.2.2.6.1.3.1.10.1.2.1.4 - Token [Core]  <!-- UUID: 026d2917-1690-44ac-97e8-248ca299d1d3 -->

RLUSD

###### A.6.1.1.2.2.6.1.3.1.10.1.2.2 - Contract Addresses [Core]  <!-- UUID: 9a0b58c8-d674-4a3c-8a68-4856ad42484e -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.10.1.2.2.1 - Token Address [Core]  <!-- UUID: a7a0518a-cc8a-460c-b9a4-58eae7130455 -->

`0x8292Bb45bf1Ee4d140127049757C2E0fF06317eD`

###### A.6.1.1.2.2.6.1.3.1.10.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 6f3ad27d-cb6d-4135-a0ad-444c3d3b2df6 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.10.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 84298bdc-2033-47d4-89f7-d8d244c1a3bc -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.10.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: c52f70d9-7910-4f5b-8ffc-5e48a4d7ac39 -->

The inflow RateLimitID is:

`0x1fd0baaf4707a3525f15888ddf89e29b1a008d0f3cf7fb75171233c72003a588`.

###### A.6.1.1.2.2.6.1.3.1.10.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: de5079d5-deaa-4cac-abfa-f4032a0d29a2 -->

The outflow RateLimitID is:

`0x786ff17c8a3c0f645317f91a3247bc843ba1ee4d248ab539acec8ba3bf4557ae`.

###### A.6.1.1.2.2.6.1.3.1.10.1.2.4 - Rate Limits [Core]  <!-- UUID: 5cc1e823-b15a-4792-8b33-ce92a02fd0b0 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.10.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 1b66e040-0e9d-4fb7-a3a4-66068899c344 -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.10.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 8cd46ad3-7589-4ac0-8cb6-a6dbe42bdc81 -->

The withdrawal rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.10.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 193f9b5d-a33e-44a0-ba8e-33e480d96243 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.10.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 8b96b7dc-9269-4d51-8b2f-a77d337736fc -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.11 - Agora [Core]  <!-- UUID: 1e4049b8-cd1d-42ef-be21-7f365b6a5341 -->

The Ethereum Mainnet Instances of the Agora Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.11.1 - Ethereum Mainnet - Agora AUSD Instance Configuration Document [Core]  <!-- UUID: 0d71b879-0dd7-4c37-9a42-f16d868c4482 -->

The documents herein contain the Instance Configuration Document for the Agora AUSD Instance.

###### A.6.1.1.2.2.6.1.3.1.11.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: fbfc3072-984e-4538-be7d-4a2dfc1b6057 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.11.1.2 - Parameters [Core]  <!-- UUID: fbc9a192-1171-4a09-a223-a5ce4bfdf227 -->

The documents herein define the parameters of the Agora AUSD Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.11.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 386b5c26-965d-43c9-b6a7-6f2d9717f57c -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.11.1.2.1.1 - Network [Core]  <!-- UUID: 9c207b7e-5f87-490c-a209-44157b596745 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.11.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 7c6e311b-c4b6-498f-a9b1-7c1812d96006 -->

Agora AUSD

###### A.6.1.1.2.2.6.1.3.1.11.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 2f2d0122-0b55-4c6a-be9b-05f0a1378ca9 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.11.1.2.1.4 - Token [Core]  <!-- UUID: a4320ef3-98d4-4c6c-ba33-dd58fd40293c -->

AUSD

###### A.6.1.1.2.2.6.1.3.1.11.1.2.2 - Contract Addresses [Core]  <!-- UUID: 33e1ff50-f11e-4a94-be47-ac2014ed172e -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.11.1.2.2.1 - Token Address [Core]  <!-- UUID: b4a55280-bf9d-477a-9d42-1b2a421f6028 -->

`0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`

###### A.6.1.1.2.2.6.1.3.1.11.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: f8bcf8e0-e5a8-41c3-9963-2ba85697265f -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.11.1.2.2.3 - Deposit Address [Core]  <!-- UUID: 978c5bd7-a3ad-42f2-a7d3-2166008e2e6b -->

`0x748b66a6b3666311F370218Bc2819c0bEe13677e`

###### A.6.1.1.2.2.6.1.3.1.11.1.2.2.4 - Withdrawal Address [Core]  <!-- UUID: b811a795-e342-4578-9acb-447a7027c3f5 -->

`0xab8306d9FeFBE8183c3C59cA897A2E0Eb5beFE67`

###### A.6.1.1.2.2.6.1.3.1.11.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: c5462c4a-eb73-40c3-bc66-6224fb0d7359 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.11.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 94e3de3e-d8b7-4d23-8b97-8fd6d4c56281 -->

The inflow RateLimitID is: `0xf49540d3618324319b2da1f511b10e85ace863c455904b9deb9348c495f6f0c5`.

###### A.6.1.1.2.2.6.1.3.1.11.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: d585ab62-9de7-4b98-88b3-c6b70428fd66 -->

The outflow RateLimitID is: `0x42ad76bdc643205fd16f00e7e67f0d5e7ae13541010329da7677ea4ddc7e59e3`.

###### A.6.1.1.2.2.6.1.3.1.11.1.2.4 - Rate Limits [Core]  <!-- UUID: d60717bb-c122-49b9-9617-d121c05f60cb -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.11.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 880c8154-4959-4875-b696-3133f795fe02 -->

The deposit rate limits are:

- `maxAmount`: 10,000,000 USDC
- `slope`: 100,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.11.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: ce3f0a10-568d-4525-b69d-1669c3cb2e8c -->

The withdrawal rate limits are:

- `maxAmount`: 10,000,000 AUSD
- `slope`: 100,000,000 AUSD per day

###### A.6.1.1.2.2.6.1.3.1.11.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: b13534e8-3758-4255-8c2d-60520fa36ed5 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.11.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 3b346059-5587-43d2-addd-92e12f26f83a -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.12 - Uniswap [Core]  <!-- UUID: e8924df2-b3af-4867-8eda-1aa41ebcb785 -->

The Ethereum Mainnet Instances of the Uniswap Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.12.1 - Ethereum Mainnet - Uniswap v3 AUSD/USDC Swaps Instance Configuration Document [Core]  <!-- UUID: ffa0ca69-c416-4163-a1c6-b863f5d38c3f -->

The documents herein contain the Instance Configuration Document for the Uniswap v3 AUSD/USDC Swaps Instance.

###### A.6.1.1.2.2.6.1.3.1.12.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: f13c08b4-db8a-4b52-9c99-55b2b2537153 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.12.1.2 - Parameters [Core]  <!-- UUID: e33ee131-43d9-472f-b8da-3a1a365cf884 -->

The documents herein define the parameters of the Uniswap v3 AUSD/USDC Swaps Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.12.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 575d774f-ca5c-4f77-a56a-a818c6313f0e -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.12.1.2.1.1 - Network [Core]  <!-- UUID: b797c786-724a-4355-905c-211c8eedbbcc -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.12.1.2.1.2 - Target Protocol [Core]  <!-- UUID: c742ce08-484e-4f55-a422-00d6b4852ef8 -->

Uniswap v3 AUSD/USDC

###### A.6.1.1.2.2.6.1.3.1.12.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 7156baa8-7cbf-4739-8b35-ae2dcf60601d -->

USDC and AUSD

###### A.6.1.1.2.2.6.1.3.1.12.1.2.1.4 - Token [Core]  <!-- UUID: 0f2e4756-a0ad-4d33-b17a-a2fa5148ce80 -->

Uniswap V3 AUSD/USDC Pool

###### A.6.1.1.2.2.6.1.3.1.12.1.2.2 - Contract Addresses [Core]  <!-- UUID: fb504b91-0e11-405a-bfb4-3dce679857b6 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.12.1.2.2.1 - Underlying Asset Address (USDC) [Core]  <!-- UUID: 9dacb60c-fa1c-48cf-94c7-6b25cfbf9b28 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.12.1.2.2.2 - Underlying Asset Address (AUSD) [Core]  <!-- UUID: 5adc9cd0-d960-45b9-9c35-23e5dc0d1ff9 -->

`0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`

###### A.6.1.1.2.2.6.1.3.1.12.1.2.2.3 - Pool Address [Core]  <!-- UUID: 75920dcb-2cbb-4be7-b0a8-4ed1b5eef507 -->

`0xbAFeAd7c60Ea473758ED6c6021505E8BBd7e8E5d`

###### A.6.1.1.2.2.6.1.3.1.12.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 1de93819-97a2-450c-9a2f-5ad1d3c5ac9f -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.12.1.2.3.1 - Inflow RateLimitID (USDC) [Core]  <!-- UUID: 5e3c790b-5e6f-472c-845e-017bc8023c52 -->

The inflow RateLimitID is: `0x6e850dcb18bea10055c82d1e3753f551b1228d04b81350ba117235de19f9a0da`.

###### A.6.1.1.2.2.6.1.3.1.12.1.2.3.2 - Outflow RateLimitID (AUSD) [Core]  <!-- UUID: 5520059a-dca9-4212-8578-2fbefe501034 -->

The outflow RateLimitID is: `0x7dd93dac252469b97c259284118454a6a09efd0e5f781dec59acc240f8f88402`.

###### A.6.1.1.2.2.6.1.3.1.12.1.2.4 - Rate Limits [Core]  <!-- UUID: a4bfb5a5-7313-4d78-b9e9-eaa093dd510f -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.12.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 37b74730-eeef-4f2a-89cc-699fa51b176b -->

The deposit rate limits are:

- `maxAmount`: N/A - swaps only
- `slope`: N/A - swaps only

###### A.6.1.1.2.2.6.1.3.1.12.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 52f681eb-f0eb-4d36-95dd-4d239fef72b9 -->

The withdrawal rate limits are:

- `maxAmount`: N/A - swaps only

###### A.6.1.1.2.2.6.1.3.1.12.1.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: e21c0b53-fc2a-46d1-b820-f9a5471c7efb -->

The swap rate limits are:

- `maxAmount`: 5,000,000 AUSD/USDC
- `slope`: 100,000,000 AUSD/USDC per day
- `maxSlippage`: 0.1%

###### A.6.1.1.2.2.6.1.3.1.12.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 9e2b3dee-8c09-4a75-888a-b1608201f1bc -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.12.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 4bfb42c0-cb39-4d13-bf80-6d0a0a51c47d -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.12.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 960ce9e1-84f5-4798-81a6-6619ea153552 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.12.1.4.1 - Parameters For Stable Stable Pools [Core]  <!-- UUID: dab70e48-7329-4bb4-87cc-3737c3c6336e -->

- `twapSecondsAgo`: 600
- `maxTickDelta`: 200
- `lowerTickBound`: -10
- `upperTickBound`: +10

###### A.6.1.1.2.2.6.1.3.1.12.2 - Ethereum Mainnet - Uniswap v3 AUSD/USDC LP Instance Configuration Document [Core]  <!-- UUID: cca4236a-47f9-4b4f-81ef-c31a5ee624aa -->

The documents herein contain the Instance Configuration Document for the Uniswap v3 AUSD/USDC LP Instance.

###### A.6.1.1.2.2.6.1.3.1.12.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 9e34658e-136a-4f6e-baf3-e2f31805dc61 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.12.2.2 - Parameters [Core]  <!-- UUID: 2db140cc-9052-4ba6-bd8d-3662c4257d9e -->

The documents herein define the parameters of the Uniswap v3 AUSD/USDC LP Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 9aa5a907-0c1a-405c-8a8b-04f95b236c8c -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.1.1 - Network [Core]  <!-- UUID: 68768ca1-ac88-4629-adbb-df3351dc14ef -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.12.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 0311d64a-06f8-474e-bfcc-46a21e09aca7 -->

Uniswap v3 AUSD/USDC

###### A.6.1.1.2.2.6.1.3.1.12.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 8d7b7008-1e6f-4f9a-b786-637b33734ebc -->

USDC and AUSD

###### A.6.1.1.2.2.6.1.3.1.12.2.2.1.4 - Token [Core]  <!-- UUID: 8b10ab2e-d491-46de-994c-9c8fe4958b33 -->

Uniswap V3 AUSD/USDC Pool

###### A.6.1.1.2.2.6.1.3.1.12.2.2.2 - Contract Addresses [Core]  <!-- UUID: 8bdcceab-3308-47b6-87f7-c137be46e2ba -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.2.1 - Underlying Asset Address (USDC) [Core]  <!-- UUID: a534cc96-a00b-41db-8120-156faddbdc56 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.12.2.2.2.2 - Underlying Asset Address (AUSD) [Core]  <!-- UUID: d3d0525b-c3d0-42e6-bba4-519d22247856 -->

`0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`

###### A.6.1.1.2.2.6.1.3.1.12.2.2.2.3 - Pool Address [Core]  <!-- UUID: 5ef626d9-9f44-4088-b874-5a06b0730f12 -->

`0xbAFeAd7c60Ea473758ED6c6021505E8BBd7e8E5d`

###### A.6.1.1.2.2.6.1.3.1.12.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: a0cd0ff3-ffba-4b49-945b-06f0b402989a -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.3.1 - Inflow RateLimitID (USDC) [Core]  <!-- UUID: 369980d8-10a0-4aa9-a3ef-b3ef5112ad5a -->

The inflow RateLimitID is: `0x71efb11b03476e40dcc1ade629d360114fcbf838d70a3211270f69414ba9a187`.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.3.2 - Inflow RateLimitID (AUSD) [Core]  <!-- UUID: fc8163c7-99af-416f-ad27-9a805c592778 -->

The inflow RateLimitID is: `0x89c0cb8c17898781d7c1776eafcf73fd0b570659ad5c3791ddcbefe66b001541`.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.3.3 - Outflow RateLimitID (USDC) [Core]  <!-- UUID: 3377cf40-41df-4cb8-9b0b-e0fa0c89b20e -->

The outflow RateLimitID is: `0x17c7a2da0785bd1ad67b8207080dbc243cfc4e573cbac18a68d0bd4b788a1dfc`.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.3.4 - Outflow RateLimitID (AUSD) [Core]  <!-- UUID: 7e8b0d83-300b-4127-a738-0c6c833b115b -->

The outflow RateLimitID is: `0xf353a8cb19089be9c21260f788c98069b2cef6a8a4bf9d061b3e5e7629a85671`.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.4 - Rate Limits [Core]  <!-- UUID: fe6667c8-268e-4f3b-9d08-0538d47df313 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.12.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 2a16ab46-2924-4c7d-8c47-26f8119fcf62 -->

The deposit rate limits are:

- `maxAmount`: 25,000,000 AUSD/USDC
- `slope`: 25,000,000 AUSD/USDC per day

###### A.6.1.1.2.2.6.1.3.1.12.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 2f0a3fb8-6b7a-4c37-90c8-f2b277289969 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.12.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 5a987f26-765c-4464-9b18-9f2d88098304 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.12.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: f33d7fc9-9654-4aa8-8ed5-13881c37ba24 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.12.2.3.1 - Fee Collection [Core]  <!-- UUID: 2e23a8a7-cec9-4fa8-8033-2961fe3c2bcd -->

Grove is authorized to execute a one-time collect of all fees accrued on this Instance's Uniswap V3 position (tokenId 1192575 in the Uniswap V3 `NonfungiblePositionManager`), with proceeds received by the ALM Proxy.

###### A.6.1.1.2.2.6.1.3.1.12.2.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 6b6dd157-be7c-4170-a25d-f65f529e48b5 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.12.2.4.1 - Parameters For Stable Stable Pools [Core]  <!-- UUID: cabd3b71-0346-4be4-9b5c-bf13dd7a0ab9 -->

- `twapSecondsAgo`: 600
- `maxTickDelta`: 200
- `lowerTickBound`: -10
- `upperTickBound`: +10

###### A.6.1.1.2.2.6.1.3.1.12.3 - Ethereum Mainnet - Grove Diamond PAU Uniswap v3 AUSD/USDC Instance Configuration Document [Core]  <!-- UUID: 4a3fdcf1-e754-413a-b7af-5336fa162d83 -->

The documents herein contain the Instance Configuration Document for the Grove Diamond PAU Uniswap v3 AUSD/USDC Instance.

###### A.6.1.1.2.2.6.1.3.1.12.3.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 63edf0b8-b6a8-43a6-a7ff-a66339be7831 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.12.3.2 - Parameters [Core]  <!-- UUID: 92028aef-8300-4f70-8f36-05c9f7d2efb9 -->

The documents herein define the Instance parameters.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.1 - Instance Identifiers [Core]  <!-- UUID: fab622a4-8a40-4e2b-9ca4-803d194d533c -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.1.1 - Network [Core]  <!-- UUID: f9a56281-3a76-4df8-8328-cf525893a6c1 -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.12.3.2.1.2 - Target Protocol [Core]  <!-- UUID: 15fe5647-c858-4e28-a7e2-ca49910a1c63 -->

Uniswap v3 AUSD/USDC

###### A.6.1.1.2.2.6.1.3.1.12.3.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 06d579c8-697e-49e4-956c-df2f3cb16fcb -->

USDC and AUSD

###### A.6.1.1.2.2.6.1.3.1.12.3.2.1.4 - Token [Core]  <!-- UUID: dcff1420-badf-442f-b607-d41ee41485a1 -->

Uniswap V3 AUSD/USDC Pool

###### A.6.1.1.2.2.6.1.3.1.12.3.2.2 - Contract Addresses [Core]  <!-- UUID: ef1ea36a-9333-4fb9-b687-df46bca8d46a -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.2.1 - Underlying Asset Address (USDC) [Core]  <!-- UUID: 9ea7e513-0d0e-40a4-8c47-0a70ed2aff9c -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.12.3.2.2.2 - Underlying Asset Address (AUSD) [Core]  <!-- UUID: 6aa5c522-be2d-4def-9055-e829fdf7251c -->

`0x00000000eFE302BEAA2b3e6e1b18d08D69a9012a`

###### A.6.1.1.2.2.6.1.3.1.12.3.2.2.3 - Pool Address [Core]  <!-- UUID: 4cc55c15-78a0-46ae-a81b-686eccb1a621 -->

`0xbAFeAd7c60Ea473758ED6c6021505E8BBd7e8E5d`

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3 - Rate Limit IDs [Core]  <!-- UUID: 12b9ddef-1ee9-4b42-ae83-41dcdf698602 -->

The specific `RateLimitID`(s) for this Instance's deposit, withdrawal, and swap operations are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.1 - Aggregate Deposit RateLimitID [Core]  <!-- UUID: 86eeaa4c-3009-4ca1-abae-ceece92b5725 -->

The aggregate deposit RateLimitID is: `0xd3384d5424cd179640223010fed859f38b86b26e5e0b9ee88b87321b98882f57`.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.2 - Deposit RateLimitID (AUSD) [Core]  <!-- UUID: e4fc1219-d1ba-4ac7-826a-6407e12a513f -->

The deposit RateLimitID for AUSD is: `0x89c0cb8c17898781d7c1776eafcf73fd0b570659ad5c3791ddcbefe66b001541`.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.3 - Deposit RateLimitID (USDC) [Core]  <!-- UUID: 1ba6991c-a422-4358-befb-61acdd670be3 -->

The deposit RateLimitID for USDC is: `0x71efb11b03476e40dcc1ade629d360114fcbf838d70a3211270f69414ba9a187`.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.4 - Aggregate Withdrawal RateLimitID [Core]  <!-- UUID: a4f06e32-943a-4dfa-8f1f-78769945bd54 -->

The aggregate withdrawal RateLimitID is: `0xbe8cbf4b779bbe60101d88f64a8afcc8fdf78863df4303da9047b66fcf427734`.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.5 - Withdrawal RateLimitID (AUSD) [Core]  <!-- UUID: b3552bb8-9e92-4d21-bb44-fadfaf3fbc3e -->

The withdrawal RateLimitID for AUSD is: `0xf353a8cb19089be9c21260f788c98069b2cef6a8a4bf9d061b3e5e7629a85671`.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.6 - Withdrawal RateLimitID (USDC) [Core]  <!-- UUID: 44a609fc-ef14-4582-a844-2762541938c4 -->

The withdrawal RateLimitID for USDC is: `0x17c7a2da0785bd1ad67b8207080dbc243cfc4e573cbac18a68d0bd4b788a1dfc`.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.7 - Swap RateLimitID (AUSD) [Core]  <!-- UUID: 9dec6725-fc20-4f60-8e09-c4de22c05ab5 -->

The swap RateLimitID for AUSD is: `0x7dd93dac252469b97c259284118454a6a09efd0e5f781dec59acc240f8f88402`.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.3.8 - Swap RateLimitID (USDC) [Core]  <!-- UUID: 43563484-779a-4ba8-8211-808cb2a1a7d6 -->

The swap RateLimitID for USDC is: `0x6e850dcb18bea10055c82d1e3753f551b1228d04b81350ba117235de19f9a0da`.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.4 - Rate Limits [Core]  <!-- UUID: df218aec-13d6-4238-bff9-a0eda5eb11a7 -->

The current `maxAmount` and `slope` for this Instance's deposit, withdrawal, and swap operations are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 805c6feb-74c9-4e43-90c8-446dd937a618 -->

The deposit rate limits are:

- Aggregate: `maxAmount`: 5,000,000 (normalized), `slope`: 0
- AUSD: `maxAmount`: 5,000,000 AUSD, `slope`: 0
- USDC: `maxAmount`: 5,000,000 USDC, `slope`: 0

###### A.6.1.1.2.2.6.1.3.1.12.3.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: e675980b-5189-47c1-ac1b-c47eee3b87d1 -->

The withdrawal rate limits are:

- Aggregate: `maxAmount`: Unlimited
- AUSD: `maxAmount`: Unlimited
- USDC: `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.12.3.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: d2527702-e69e-484e-9e39-3244c5836ceb -->

The swap rate limits are:

- AUSD: `maxAmount`: 1,000,000 AUSD, `slope`: 5,000,000 AUSD per day
- USDC: `maxAmount`: 1,000,000 USDC, `slope`: 5,000,000 USDC per day
- `maxSlippage`: 0.1%

###### A.6.1.1.2.2.6.1.3.1.12.3.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 2e60fa48-4088-4ea3-86d5-80d7fb45979c -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.5.1 - Maximum Exposure [Core]  <!-- UUID: 8cf235df-5cf8-42d3-8a10-8d408a90f56d -->

Total exposure through this Instance may not exceed 5,000,000 USDS.

###### A.6.1.1.2.2.6.1.3.1.12.3.2.5.2 - CRR [Core]  <!-- UUID: 1b49ac8a-e3bd-4764-bb6f-497b2c8c203c -->

The CRR for this Instance, as specified in [A.3.2.1.1.1 - Capital Ratio Requirement](3828778e-0197-4ce9-a836-6770d04f2ea9), is 100%.

###### A.6.1.1.2.2.6.1.3.1.12.3.3 - Instance-specific Operational Processes [Core]  <!-- UUID: e6340bc2-ea2a-4df6-802c-1d68ce5d653d -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.12.3.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 0aecfefc-bc60-4b63-b7b5-0327c8fe5cf0 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.12.3.4.1 - Parameters For Stable Stable Pools [Core]  <!-- UUID: 737c6432-5c4e-45cd-b1ab-dc0656d6dc56 -->

- `twapSecondsAgo`: 600
- `maxTickDelta`: 200
- `lowerTickBound`: -10
- `upperTickBound`: +10

###### A.6.1.1.2.2.6.1.3.1.13 - Maple [Core]  <!-- UUID: edcc1342-e0ca-4860-90bf-f5b4053d79df -->

The Ethereum Mainnet Instances of the Maple Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.13.1 - Ethereum Mainnet - Maple syrupUSDC Instance Configuration Document [Core]  <!-- UUID: 7502f64c-3276-478e-8f98-53a2377ca1a2 -->

The documents herein contain the Instance Configuration Document for the Maple syrupUSDC Instance.

###### A.6.1.1.2.2.6.1.3.1.13.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 5801de75-952f-4f5d-a0de-fd1643adb3f2 -->

`Covered`

###### A.6.1.1.2.2.6.1.3.1.13.1.2 - Parameters [Core]  <!-- UUID: 9fda752d-6c8a-4bb2-bea9-da336d41586f -->

The documents herein define the parameters of the Maple syrupUSDC Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.13.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 18cadbf1-8268-46a4-867c-5b8d3639f840 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.13.1.2.1.1 - Network [Core]  <!-- UUID: 933bb96c-0f5c-4ad1-a137-21442969b44c -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.13.1.2.1.2 - Target Protocol [Core]  <!-- UUID: facc3c45-33a1-46f6-8e93-0474f87f40d6 -->

Maple

###### A.6.1.1.2.2.6.1.3.1.13.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 5da95711-2be7-4ff8-bbd1-245cd12f8b62 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.13.1.2.1.4 - Token [Core]  <!-- UUID: b81399bc-f30a-4abb-a4f4-380517147462 -->

syrupUSDC

###### A.6.1.1.2.2.6.1.3.1.13.1.2.2 - Contract Addresses [Core]  <!-- UUID: 68f4487a-c475-400f-9a24-0eaba47da45b -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.13.1.2.2.1 - Token Address [Core]  <!-- UUID: f4f3bc84-0544-47a0-ac5d-e605714c2354 -->

`0x80ac24aA929eaF5013f6436cdA2a7ba190f5Cc0b`

###### A.6.1.1.2.2.6.1.3.1.13.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 166f7435-79ad-4e4c-be93-85ca69ec63ec -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.13.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 891be5d8-3a84-4d51-98d5-85f0e18dc791 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.13.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 19362744-13c9-4f42-98af-18eae4946290 -->

The inflow RateLimitID is: `0x99a69e57b2f387f999d6adff6eb2e707b59fdb54f06ca6211b4f20956e9bfe10`

###### A.6.1.1.2.2.6.1.3.1.13.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 63e7a899-dfd5-489b-9ea0-6ccb527e64b7 -->

The outflow RateLimitID will be specified in a future iteration of the Atlas.

###### A.6.1.1.2.2.6.1.3.1.13.1.2.4 - Rate Limits [Core]  <!-- UUID: f69051f4-25f1-4519-8776-30c753eb351e -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.13.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 5ce46c5d-978e-4fe3-a109-8a11833b1b09 -->

The deposit rate limits are:

- `maxAmount`: 0
- `slope`: 0

###### A.6.1.1.2.2.6.1.3.1.13.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 2068313d-3791-4771-9e0d-f74dffa4d729 -->

The withdrawal rate limits are:

- `maxAmount`: 0

###### A.6.1.1.2.2.6.1.3.1.13.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 69ce0ff7-8847-43a1-93c8-47d143d86f69 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.13.1.2.5.1 - Max Exchange Rate [Core]  <!-- UUID: 38bc059a-09d1-4a86-bade-4b0da4bf8413 -->

`setMaxExchangeRate(MAPLE_SYRUP_USDC, 1e6, 3e6)`

###### A.6.1.1.2.2.6.1.3.1.13.1.2.5.2 - Maximum Exposure [Core]  <!-- UUID: d86392f8-071a-4167-9d44-64a8150c2b18 -->

The Maximum Exposure for this Instance is 0 USD.

###### A.6.1.1.2.2.6.1.3.1.14 - Tokenized Treasury [Core]  <!-- UUID: be7157cb-9469-4f59-b1a0-d22a62e97242 -->

The Ethereum Mainnet Tokenized Treasury Instances with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.14.1 - Ethereum Mainnet - Tokenized Treasury JTRSY Instance Configuration Document [Core]  <!-- UUID: 5e38198e-1577-4ab0-900a-91b6d8284387 -->

The documents herein contain the Instance Configuration Document for the Tokenized Treasury JTRSY Instance.

###### A.6.1.1.2.2.6.1.3.1.14.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: fde7f4bb-0873-4d99-bef5-694a53300eae -->

`Pending`

###### A.6.1.1.2.2.6.1.3.1.14.1.2 - Parameters [Core]  <!-- UUID: 1834c864-183a-4835-bb17-b1107e41abbb -->

The documents herein define the parameters of the Tokenized Treasury JTRSY Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.14.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 3a505b8a-4ff1-40bf-aa03-ea7c4550422a -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.14.1.2.1.1 - Network [Core]  <!-- UUID: cdd4e8c9-b1be-4f96-9b65-d0ba9942202d -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.14.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 6f3423c8-3aba-4852-9011-09dc0d90fa3b -->

Centrifuge

###### A.6.1.1.2.2.6.1.3.1.14.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 3f39032c-cc00-4ea9-be78-9e02e9fc4a25 -->

USDS

###### A.6.1.1.2.2.6.1.3.1.14.1.2.1.4 - Token [Core]  <!-- UUID: 6a11e241-9dba-423f-b9aa-31fa37c96ab3 -->

JTRSY

###### A.6.1.1.2.2.6.1.3.1.14.1.2.2 - Contract Addresses [Core]  <!-- UUID: 75e8bf90-46f3-4e53-b6b9-f8b30dd80da7 -->

The documents herein define the Instance-specific contract addresses.

###### A.6.1.1.2.2.6.1.3.1.14.1.2.2.1 - Token Address [Core]  <!-- UUID: 5c346c1b-a942-4ced-9267-7087d5c718a4 -->

`0x8c213ee79581Ff4984583C6a801e5263418C4b86`

###### A.6.1.1.2.2.6.1.3.1.14.1.2.2.2 - Centrifuge ERC-7540 Vault Address [Core]  <!-- UUID: c519baf9-b02c-4c07-a113-ac73738a217c -->

`0xFE6920eB6C421f1179cA8c8d4170530CDBdfd77A`

###### A.6.1.1.2.2.6.1.3.1.14.1.2.2.3 - JTRSY Rate Provider Address [Core]  <!-- UUID: e13f54bc-19d3-4a0f-a846-2c3c4154a19e -->

`0x29209ceCFeFa6f675E6f1f829320D67cE2b025E5`

###### A.6.1.1.2.2.6.1.3.1.14.1.2.2.4 - Pocket Contract Address [Core]  <!-- UUID: fd19b075-d30d-4a8e-90f0-c7ab8a2cd48b -->

`0x2Cd296095788A2741e72056D66B3Ae1fAeE23ea2`

###### A.6.1.1.2.2.6.1.3.1.14.1.2.2.5 - Token Redeemer Contract Address [Core]  <!-- UUID: 536e4413-c923-45e8-a126-8120fd9d2c72 -->

`0x7c5Ce1a1D50a6cb3Da97C9e202B3E7CD8e5b5b6c`

###### A.6.1.1.2.2.6.1.3.1.14.1.2.2.6 - Owner Timelock Contract Address [Core]  <!-- UUID: d2069cde-3b55-487a-9b1d-919bd3f76197 -->

`0xA52dC9876aB4A9DB6dAfbb83410554086054d140`

###### A.6.1.1.2.2.6.1.3.1.14.1.2.2.7 - Basin Contract Address [Core]  <!-- UUID: 7f011dc2-7624-402e-86cb-c036d1cf9afc -->

`0xf08943f817e1F902dEbC884c7B19Ea5764594Ac9`

###### A.6.1.1.2.2.6.1.3.1.14.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 850f1210-d355-48ef-8ba9-dcc70bb90f0e -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Atlas.

###### A.6.1.1.2.2.6.1.3.1.14.1.2.4 - Rate Limits [Core]  <!-- UUID: abc0b1fc-4922-40f1-8ea9-60fba89f0e5f -->

The inflow and outflow rate limit configuration for this conduit is specified in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.14.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 2e5234f6-0cae-4689-b8da-61ad99f20c31 -->

The inflow rate limits are:

- `maxAmount`: 5,000,000 USDS
- `slope`: 5,000,000 USDS per day

###### A.6.1.1.2.2.6.1.3.1.14.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: e460967c-baf1-4c39-89c8-38bb329e492e -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.14.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 1daedcbc-29a1-4dbd-8442-21cefec40c3a -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.14.1.2.5.1 - Interim Deployment [Core]  <!-- UUID: 71230664-ebd2-4be0-b83f-7582223fa04e -->

This Instance is currently defined as an Interim Deployment (see [A.1.10.2.3.2.2.2 - Interim Deployments](9b3edbbf-89d1-42da-a9c3-18f858f8471f)) and as such has CRR of 100%. The testing parameters of this Interim Deployment are specified in the documents herein.

###### A.6.1.1.2.2.6.1.3.1.14.1.2.5.1.1 - Maximum Allocation [Core]  <!-- UUID: f0bb4021-60a7-49fc-a8ed-b25d9666ed95 -->

The maximum allocation for the Tokenized Treasury Basin Interim Deployments is $5 million, combined across the JTRSY and BUIDL Instances.

###### A.6.1.1.2.2.6.1.3.1.14.1.2.5.1.2 - Rate Limits [Core]  <!-- UUID: 6487bd5d-34d0-4430-81fa-99c644abae0f -->

The Rate Limits for this Interim Deployment are defined in [A.6.1.1.2.2.6.1.3.1.14.1.2.4 - Rate Limits](abc0b1fc-4922-40f1-8ea9-60fba89f0e5f).

###### A.6.1.1.2.2.6.1.3.1.14.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: a46f85c1-48be-4070-8848-74d392c3fed5 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.14.1.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 65ca009e-8d70-4dd5-80d3-e6e0b9beae2e -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.14.1.4.1 - Instance Configuration Parameters [Core]  <!-- UUID: 16a4b87f-156e-407f-a882-d91b15a7909b -->

The configuration parameters for this Instance are as follows:

- Max Swap Size: 50,000,000 USD
- Staleness Threshold: seven (7) days
- Fees: 0
- Credit Token Deposits: Disabled
- Credit Token Withdrawals: Disabled
- Stablecoin Swaps: Disabled

###### A.6.1.1.2.2.6.1.3.1.14.1.4.2 - Issuer-Specific Role Holders [Core]  <!-- UUID: 7fbed34a-d69f-49eb-af6f-56a7522e6fda -->

The documents herein define the role holders that are specific to this Instance's credit token issuer.

###### A.6.1.1.2.2.6.1.3.1.14.1.4.2.1 - Owner Role Holder [Core]  <!-- UUID: 6c15b0a1-b9f1-40be-80b1-4c5565c30044 -->

The `OWNER_ROLE`, as defined in [A.6.1.1.2.2.6.1.2.2.1.1.2.1 - Tokenized Treasury Owner Role](41a7e6fb-59e1-40e8-a05a-68c1520fb361), is held by Anemoy via an OpenZeppelin `TimelockController` at the address specified in [A.6.1.1.2.2.6.1.3.1.14.1.2.2.6 - Owner Timelock Contract Address](d2069cde-3b55-487a-9b1d-919bd3f76197).

###### A.6.1.1.2.2.6.1.3.1.14.1.4.2.1.1 - Proposer Role Holder [Core]  <!-- UUID: dee0bbce-9f64-47e3-bbb5-3eb5204be9c5 -->

The `PROPOSER_ROLE` of the Owner Timelock is held by Anemoy at `0x9184DdBCc4824B76CE2AEFA72534a1a87aA5037c`.

###### A.6.1.1.2.2.6.1.3.1.14.1.4.2.2 - Redeemer Role Holder [Core]  <!-- UUID: 5ffebcfd-ba9b-401b-a35d-42b4426709de -->

The `REDEEMER_ROLE`, as defined in [A.6.1.1.2.2.6.1.2.2.1.1.2.5 - Tokenized Treasury Redeemer Role](fbeb1921-37eb-465b-97fa-004c8e0925b1), is held by Anemoy at `0xb6e8D3E47c4FC5606E6C24D097Dd1791885Ce05a`.

###### A.6.1.1.2.2.6.1.3.1.14.2 - Ethereum Mainnet - Tokenized Treasury BUIDL Instance Configuration Document [Core]  <!-- UUID: 867aa6c2-4d44-4734-8d77-ff435dc89463 -->

The documents herein contain the Instance Configuration Document for the Tokenized Treasury BUIDL Instance.

###### A.6.1.1.2.2.6.1.3.1.14.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 14e39363-0cc0-4dae-96f6-f2c3971a279c -->

`Pending`

###### A.6.1.1.2.2.6.1.3.1.14.2.2 - Parameters [Core]  <!-- UUID: 723c6536-0696-473c-a341-2ca940447d77 -->

The documents herein define the parameters of the Tokenized Treasury BUIDL Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.14.2.2.1 - Instance Identifiers [Core]  <!-- UUID: e4a90bfe-7d62-4b81-85f5-ae4833673cc0 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.14.2.2.1.1 - Network [Core]  <!-- UUID: 9b013484-dffa-41f0-bf70-20dc35b79b0f -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.14.2.2.1.2 - Target Protocol [Core]  <!-- UUID: b76ed652-f11a-4e34-a891-45591a468d13 -->

Securitize

###### A.6.1.1.2.2.6.1.3.1.14.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 83aac972-7196-445f-9402-10c83ce6398b -->

USDS

###### A.6.1.1.2.2.6.1.3.1.14.2.2.1.4 - Token [Core]  <!-- UUID: 6ce0fe5c-e571-4af9-a19a-91720dbbe98e -->

BUIDL

###### A.6.1.1.2.2.6.1.3.1.14.2.2.2 - Contract Addresses [Core]  <!-- UUID: 789b31ac-d6e5-4dfb-a9cd-10ddb04911d3 -->

The documents herein define the Instance-specific contract addresses.

###### A.6.1.1.2.2.6.1.3.1.14.2.2.2.1 - Token Address [Core]  <!-- UUID: 1863c073-e38e-48e3-97d3-b722080e4812 -->

`0x7712c34205737192402172409a8F7ccef8aA2AEc`

###### A.6.1.1.2.2.6.1.3.1.14.2.2.2.2 - Securitize Redemption Wallet Address [Core]  <!-- UUID: 66c7fcb2-1936-49b4-886e-922b38144d24 -->

`0x8780Dd016171B91E4Df47075dA0a947959C34200`

###### A.6.1.1.2.2.6.1.3.1.14.2.2.2.3 - BUIDL Rate Provider Address [Core]  <!-- UUID: faf47b08-b705-4f99-ac0e-041769afd5b9 -->

`0x69a171853575FFD41574EA80Abfc6337AcbC4d43`

###### A.6.1.1.2.2.6.1.3.1.14.2.2.2.4 - Pocket Contract Address [Core]  <!-- UUID: 5cbc3fb2-842e-450e-b2de-34b20563f59e -->

`0x39548FeF138370Db06e172eF0739894b2a613DF9`

###### A.6.1.1.2.2.6.1.3.1.14.2.2.2.5 - Token Redeemer Contract Address [Core]  <!-- UUID: 6a893fc2-b5f5-415c-8988-ef36e1cdcd15 -->

`0x73414528187A4986E2Af5D551fD14871b723E506`

###### A.6.1.1.2.2.6.1.3.1.14.2.2.2.6 - Owner Timelock Contract Address [Core]  <!-- UUID: b691c3af-39ce-4e62-b6f9-e7f3f493ae25 -->

`0xdB8C7c814E9780659B23478EF4Bda9032CC9Ff34`

###### A.6.1.1.2.2.6.1.3.1.14.2.2.2.7 - Basin Contract Address [Core]  <!-- UUID: 06199a1e-16ff-4ab8-bcdb-1ade95fda639 -->

`0xCBa428fB052B365557DAf52b744DFfF20d5FbEdD`

###### A.6.1.1.2.2.6.1.3.1.14.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: e1c20c48-2fc0-402f-948f-dac6ea8ab71f -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Atlas.

###### A.6.1.1.2.2.6.1.3.1.14.2.2.4 - Rate Limits [Core]  <!-- UUID: 8e7f9afb-d4c6-49ac-a956-1a65817d709f -->

The inflow and outflow rate limit configuration for this conduit is specified in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.14.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 05baee1c-f5af-45e0-b6a9-e19a6fa443b8 -->

The inflow rate limits are:

- `maxAmount`: 5,000,000 USDS
- `slope`: 5,000,000 USDS per day

###### A.6.1.1.2.2.6.1.3.1.14.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: ca94003e-2652-4ea5-8ade-a382975f44dd -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.1.14.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 7b9e163d-594c-4387-84e6-17c44174266c -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.14.2.2.5.1 - Interim Deployment [Core]  <!-- UUID: edcc2e69-0da1-4a74-82a0-52c6694e390f -->

This Instance is currently defined as an Interim Deployment (see [A.1.10.2.3.2.2.2 - Interim Deployments](9b3edbbf-89d1-42da-a9c3-18f858f8471f)) and as such has CRR of 100%. The testing parameters of this Interim Deployment are specified in the documents herein.

###### A.6.1.1.2.2.6.1.3.1.14.2.2.5.1.1 - Maximum Allocation [Core]  <!-- UUID: 5997c784-200f-49ec-b7dd-173e5c3447e9 -->

The maximum allocation for the Tokenized Treasury Basin Interim Deployments is $5 million, combined across the JTRSY and BUIDL Instances.

###### A.6.1.1.2.2.6.1.3.1.14.2.2.5.1.2 - Rate Limits [Core]  <!-- UUID: ff295b39-4fad-4b11-a9f9-318b8d25e344 -->

The Rate Limits for this Interim Deployment are defined in [A.6.1.1.2.2.6.1.3.1.14.2.2.4 - Rate Limits](8e7f9afb-d4c6-49ac-a956-1a65817d709f).

###### A.6.1.1.2.2.6.1.3.1.14.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 886bf57e-0a75-4346-8449-7cdeba8c6dca -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.1.14.2.4 - Instance-specific Operational Parameters [Core]  <!-- UUID: 5e0b2df6-745a-40ce-81cc-f8e810af2e43 -->

The documents herein contain operational parameters or configuration details unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer parameters.

###### A.6.1.1.2.2.6.1.3.1.14.2.4.1 - Instance Configuration Parameters [Core]  <!-- UUID: 259dfe6c-2fd9-4414-9838-447a55fce5d2 -->

The configuration parameters for this Instance are as follows:

- Max Swap Size: 50,000,000 USD
- Staleness Threshold: seven (7) days
- Fees: 0
- Credit Token Deposits: Disabled
- Credit Token Withdrawals: Disabled
- Stablecoin Swaps: Disabled

###### A.6.1.1.2.2.6.1.3.1.14.2.4.2 - Issuer-Specific Role Holders [Core]  <!-- UUID: 8634bdc4-3821-44e4-af29-c3802ec269ee -->

The documents herein define the role holders that are specific to this Instance's credit token issuer.

###### A.6.1.1.2.2.6.1.3.1.14.2.4.2.1 - Owner Role Holder [Core]  <!-- UUID: dea31796-e9ed-420c-9c16-a19e4ee388f6 -->

The `OWNER_ROLE`, as defined in [A.6.1.1.2.2.6.1.2.2.1.1.2.1 - Tokenized Treasury Owner Role](41a7e6fb-59e1-40e8-a05a-68c1520fb361), is held by Securitize via an OpenZeppelin `TimelockController` at the address specified in [A.6.1.1.2.2.6.1.3.1.14.2.2.2.6 - Owner Timelock Contract Address](b691c3af-39ce-4e62-b6f9-e7f3f493ae25).

###### A.6.1.1.2.2.6.1.3.1.14.2.4.2.1.1 - Proposer Role Holder [Core]  <!-- UUID: c2ebcaec-88f4-40a9-9eea-f433d47825c2 -->

The `PROPOSER_ROLE` of the Owner Timelock is held by Securitize at `0x453A28B31fdc31858C35B02bc3A42BCD8bfbAd3a`.

###### A.6.1.1.2.2.6.1.3.1.14.2.4.2.2 - Redeemer Role Holder [Core]  <!-- UUID: db98a289-3bb6-475d-b71c-dd7804171977 -->

The `REDEEMER_ROLE`, as defined in [A.6.1.1.2.2.6.1.2.2.1.1.2.5 - Tokenized Treasury Redeemer Role](fbeb1921-37eb-465b-97fa-004c8e0925b1), is held by Securitize at `0x488F27168a19472c51f003fbC5b75B1ACc3B7b4c`.

###### A.6.1.1.2.2.6.1.3.1.15 - Paxos [Core]  <!-- UUID: bc8cc6e7-9110-43a5-bfb3-3edb7d0aff04 -->

The Ethereum Mainnet Instances of Paxos with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.1.15.1 - Ethereum Mainnet - USDC To USDG Via Paxos Instance Configuration Document [Core]  <!-- UUID: 4bf8eae7-b19c-4572-ad05-efff5a5310a6 -->

The documents herein contain the Instance Configuration Document for the USDC To USDG Via Paxos Instance.

###### A.6.1.1.2.2.6.1.3.1.15.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 6d116c27-ae74-4b72-868b-9162a966cb31 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.1.15.1.2 - Parameters [Core]  <!-- UUID: 0b817f6e-586b-4ffd-94c0-0c69eb42387b -->

The documents herein define the parameters of the USDC To USDG Via Paxos Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.1.15.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 0bce7e22-242b-449b-b50b-2cb92d8d92b8 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.1.15.1.2.1.1 - Network [Core]  <!-- UUID: 0b5dec27-2968-4a4b-8472-b5f51a0147ea -->

Ethereum Mainnet

###### A.6.1.1.2.2.6.1.3.1.15.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 32389891-ec5f-4dbb-adbd-9379f29eb9a0 -->

Paxos

###### A.6.1.1.2.2.6.1.3.1.15.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: aa76bbe6-5181-4fb2-9084-25ea34ab4695 -->

USDC

###### A.6.1.1.2.2.6.1.3.1.15.1.2.1.4 - Token to Receive [Core]  <!-- UUID: 398180c0-83d9-4328-8e07-cf8c117967a8 -->

USDG

###### A.6.1.1.2.2.6.1.3.1.15.1.2.2 - Contract Addresses [Core]  <!-- UUID: 91233ce6-542d-4813-b929-3c723559103f -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.1.15.1.2.2.1 - Token Address [Core]  <!-- UUID: 60a0bddf-ade3-4be9-8142-06880cec308d -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.15.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 955c5866-657c-4e20-b1ae-6a3e543ecf0e -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.2.2.6.1.3.1.15.1.2.2.3 - Paxos Deposit Address [Core]  <!-- UUID: 6c773216-b79c-49f7-ab94-420d3c8a4e3b -->

`0x8C0A9E5939B97979f85d9aDA3d983C6E713Cc2dB`

###### A.6.1.1.2.2.6.1.3.1.15.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 17253587-03c7-48bd-809d-a88dcfdffa14 -->

The transferAssets `RateLimitID` for this conduit is: `0x4139045de2f11ba23865c6cdf20084f6566d834b50716e469c5dbd8ed71faaf1`.

###### A.6.1.1.2.2.6.1.3.1.15.1.2.4 - Rate Limits [Core]  <!-- UUID: a4419273-8de4-4d67-a438-6c356e9b85a4 -->

The current TransferAsset rate limits for this conduit’s transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.1.15.1.2.4.1 - TransferAssets Rate Limits [Core]  <!-- UUID: 52a84bbf-b322-4705-9909-19cc3319b308 -->

The transferAssets rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.1.15.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: c72686fa-378b-4e4c-bd56-88a4f845e6d8 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.1.15.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 989edafa-ff42-455b-9f4e-2c7bb63911a6 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.2 - Avalanche Instances [Core]  <!-- UUID: fbb34f07-a5c8-475e-9842-fc5c9b9bd359 -->

The Avalanche Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.2.2.6.1.3.2.1 - Centrifuge [Core]  <!-- UUID: 87310712-edfa-4882-a22e-7b891f566026 -->

The Avalanche Instances of the Centrifuge Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.2.1.1 - Avalanche - Centrifuge JTRSY Instance Configuration Document [Core]  <!-- UUID: 3c731296-858a-4c27-a5cc-6b7ff208cc16 -->

The documents herein contain the Instance Configuration Document for the Centrifuge JTRSY Instance.

###### A.6.1.1.2.2.6.1.3.2.1.1.1 - RRC Framework Full Implementation [Core]  <!-- UUID: 6b0ac1c6-dd10-4996-8924-2525d50abdbb -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.2.1.1.2 - Parameters [Core]  <!-- UUID: 5bc93313-446b-4dc2-a964-c565ee7718cf -->

The documents herein define the parameters of the Centrifuge JTRSY Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.2.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: a8ac0ffa-f5f0-40e9-8b82-910ed3a00231 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.2.1.1.2.1.1 - Network [Core]  <!-- UUID: 0d7aa581-b3d4-4041-8be0-4bbf824dfe71 -->

Avalanche

###### A.6.1.1.2.2.6.1.3.2.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: e916d986-41b1-4f76-ab3f-3bd0f233adc1 -->

Centrifuge

###### A.6.1.1.2.2.6.1.3.2.1.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 1c1e18f7-1202-4b9e-81d2-27736659ea42 -->

USDC

###### A.6.1.1.2.2.6.1.3.2.1.1.2.1.4 - Token [Core]  <!-- UUID: 3ea884e0-bb0e-4dcc-8644-2840b524c8b7 -->

JTRSY

###### A.6.1.1.2.2.6.1.3.2.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: bbcf802e-a2bd-4382-91e7-bc3e813683e9 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.2.1.1.2.2.1 - Token Address [Core]  <!-- UUID: f9f790ea-f67a-4e6d-ac63-cd84faf208fe -->

`0xFE6920eB6C421f1179cA8c8d4170530CDBdfd77A`

###### A.6.1.1.2.2.6.1.3.2.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: fcf231c8-f8a5-4073-be59-cde9a5f86a29 -->

`0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E`

###### A.6.1.1.2.2.6.1.3.2.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: d926a814-26d2-4f62-a92b-b05b3253ed89 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.2.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 5a1eb061-1050-45e0-9b31-157440e84790 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.2.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 0c432f68-5bbf-449e-b9fb-c089f3c750c7 -->

The inflow rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.2.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 6e549221-bbf2-4c58-922d-649e7beee41c -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.2.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 76b4c9cd-d637-40f1-a83d-b7f4a7c46d1b -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.2.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 905f3980-1d3c-4703-b7f4-6edd1d97ea9a -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.2.1.2 - Avalanche - Centrifuge JAAA Instance Configuration Document [Core]  <!-- UUID: bd37d6c9-2e05-4ce3-86dc-3a50d6887e6b -->

The documents herein contain the Instance Configuration Document for the Centrifuge JAAA Instance.

###### A.6.1.1.2.2.6.1.3.2.1.2.1 - RRC Framework Full Implementation [Core]  <!-- UUID: d29cee92-1484-47ad-a253-42670e3f2839 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.2.1.2.2 - Parameters [Core]  <!-- UUID: 2428f891-6e70-4bc2-93b8-080af94a569c -->

The documents herein define the parameters of the Centrifuge JAAA Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.2.1.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 08fcf58b-bb1c-416e-a0e6-6c4177341d7f -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.2.1.2.2.1.1 - Network [Core]  <!-- UUID: 787ada98-2320-476f-8abd-20ff2df52c91 -->

Avalanche

###### A.6.1.1.2.2.6.1.3.2.1.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 9acb96f8-cdf9-42a3-97b0-7300353a5919 -->

Centrifuge

###### A.6.1.1.2.2.6.1.3.2.1.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 803ac88c-2a85-4e75-87a4-1484b47a8c07 -->

USDC

###### A.6.1.1.2.2.6.1.3.2.1.2.2.1.4 - Token [Core]  <!-- UUID: 3e847695-3ad3-4b39-b01e-44787c8dcc4c -->

JAAA

###### A.6.1.1.2.2.6.1.3.2.1.2.2.2 - Contract Addresses [Core]  <!-- UUID: e240e244-f34c-41b2-a3a8-ef9c4293d97b -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.2.1.2.2.2.1 - Token Address [Core]  <!-- UUID: c0f78cfe-30ca-4026-a8ad-a0391debe389 -->

`0x1121F4e21eD8B9BC1BB9A2952cDD8639aC897784`

###### A.6.1.1.2.2.6.1.3.2.1.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 87989bfc-6d92-4d66-b26b-e007d0b7bbc0 -->

`0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E`

###### A.6.1.1.2.2.6.1.3.2.1.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: f1dd540e-feb7-44f2-a8f8-df4861f584de -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.2.1.2.2.4 - Rate Limits [Core]  <!-- UUID: 2e51243e-6f14-4c72-97c4-e873f449bdc9 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.2.1.2.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 338e8892-584c-4ca3-9a8c-8872e4105717 -->

The inflow rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.2.1.2.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 9c214444-96bf-4982-9c96-7ae79769262a -->

The outflow rate limits are:

- `maxAmount`: Unlimited
- `slope`: This parameter will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.2.1.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: c03dd770-73f8-4894-8e6d-314d22aec2df -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.2.1.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 74e35297-1d5e-4c4a-be08-741c88329039 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.2.2 - Curve [Core]  <!-- UUID: c17ab278-4750-4e54-b6c9-f1fb31d36039 -->

The Avalanche Instances of the Curve Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.2.2.1 - Avalanche - Curve USDS/USDC Swaps Instance Configuration Document [Core]  <!-- UUID: 241a6ad1-ac18-496c-84f8-e2624497c7d9 -->

The documents herein contain the Instance Configuration Document for the Curve USDS/USDC Swaps Instance.

###### A.6.1.1.2.2.6.1.3.2.2.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: b4ce834c-f831-432c-9b0d-114c7e69e386 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.2.2.1.2 - Parameters [Core]  <!-- UUID: f770ab85-be68-40ed-b63d-bcd63b240485 -->

The documents herein define the parameters of the Curve USDS/USDC Swaps Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.2.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 425a5441-4bfe-494e-b0fb-bb040ec92973 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.2.2.1.2.1.1 - Network [Core]  <!-- UUID: 24009c3a-58b6-4280-aa73-6a90ef36c706 -->

Avalanche

###### A.6.1.1.2.2.6.1.3.2.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 47f6b57c-b563-47fd-a97f-e7f69a4d9ebf -->

Curve USDS/USDC

###### A.6.1.1.2.2.6.1.3.2.2.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 4a2677c5-9a63-4e04-80c3-a1bf57a7558c -->

USDS and USDC

###### A.6.1.1.2.2.6.1.3.2.2.1.2.1.4 - Token [Core]  <!-- UUID: 47af1c25-51d3-46cb-87f3-9576568d0f62 -->

USDSUSDC

###### A.6.1.1.2.2.6.1.3.2.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: 43cebf0e-dc61-4206-8fad-32ae9a2c865d -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.2.2.1.2.2.1 - Underlying Asset Address (USDS) [Core]  <!-- UUID: 741efad1-425e-4290-a398-2923e4f88537 -->

`0x86Ff09db814ac346a7C6FE2Cd648F27706D1D470`

###### A.6.1.1.2.2.6.1.3.2.2.1.2.2.2 - Underlying Asset Address (USDC) [Core]  <!-- UUID: c079b224-7cbb-4959-b087-19fb0d9260fd -->

`0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E`

###### A.6.1.1.2.2.6.1.3.2.2.1.2.2.3 - Pool Address [Core]  <!-- UUID: 33e4a492-5a15-4e59-be41-5e66d6cfb10c -->

`0xA9d7d3D7e68a0cae89FB33c736199172f405C8D3`

###### A.6.1.1.2.2.6.1.3.2.2.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 2e7ae859-1656-4267-b747-e062a44ca251 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.2.2.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 14ef09b9-2372-48cd-9749-3408c9fcb754 -->

The inflow RateLimitID is: `0x747102351e768926d4e5f06c0ea6ac35e4dcefa77fd901f2f8ff46e4710ab4cf`

###### A.6.1.1.2.2.6.1.3.2.2.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 8b119935-a2e9-4c11-9a03-33cf025148cc -->

The outflow RateLimitID is: N/A.

###### A.6.1.1.2.2.6.1.3.2.2.1.2.4 - Rate Limits [Core]  <!-- UUID: bfbca274-613d-43f8-92dd-45481bc53b8f -->

The current `maxAmount` and `slope` for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.2.2.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 3fc2060c-29d2-41fa-a9e6-1b47e4073cee -->

The deposit rate limits are:

- `maxAmount`: N/A - swaps only
- `slope`: N/A - swaps only

###### A.6.1.1.2.2.6.1.3.2.2.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 67213d51-ed52-4c6d-96b6-bf0718b935b1 -->

The withdrawal rate limits are:

- `maxAmount`: N/A - swaps only

###### A.6.1.1.2.2.6.1.3.2.2.1.2.4.3 - Swap Rate Limits [Core]  <!-- UUID: e23f36a6-c5f5-40d4-bdd0-77e862d7a8bb -->

The swap rate limits are:

- `maxAmount`: 5,000,000 USDS/USDC
- `slope`: 100,000,000 USDS/USDC per day
- `maxSlippage`: 0.1%

###### A.6.1.1.2.2.6.1.3.2.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: e1b88e2f-2890-4b09-a4c5-d3d76b411692 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.2.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: a13b40ae-ba04-44f0-8b66-84fbed85a765 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.2.2.2 - Avalanche - Curve USDS/USDC LP Instance Configuration Document [Core]  <!-- UUID: 72325c96-455c-4c19-aefc-541206494bd3 -->

The documents herein contain the Instance Configuration Document for the Curve USDS/USDC LP Instance.

###### A.6.1.1.2.2.6.1.3.2.2.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: cbbb4d16-1c71-4274-a0c3-3806101582d9 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.2.2.2.2 - Parameters [Core]  <!-- UUID: bb03ff8f-5dc3-4dcb-886c-09e94a526e6c -->

The documents herein define the parameters of the Curve USDS/USDC LP Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.2.2.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 695932ec-127e-4661-a647-1ae96db7612c -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.2.2.2.2.1.1 - Network [Core]  <!-- UUID: 832878c8-9d48-48eb-ab8e-88f53d3aa19c -->

Avalanche

###### A.6.1.1.2.2.6.1.3.2.2.2.2.1.2 - Target Protocol [Core]  <!-- UUID: 93bda922-82d8-4d77-a4a2-c62583fc697f -->

Curve USDS/USDC

###### A.6.1.1.2.2.6.1.3.2.2.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: bb93289c-ef4a-4305-8f9b-d791186be836 -->

USDS and USDC

###### A.6.1.1.2.2.6.1.3.2.2.2.2.1.4 - Token [Core]  <!-- UUID: 681fba5c-0e27-4bbc-ba2a-6d8fec26aab1 -->

USDSUSDC

###### A.6.1.1.2.2.6.1.3.2.2.2.2.2 - Contract Addresses [Core]  <!-- UUID: 8c668b50-96e3-44fc-9cf4-9b445b614608 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.2.2.2.2.2.1 - Underlying Asset Address (USDS) [Core]  <!-- UUID: 80d06fa8-f274-4cb2-a10c-d9899dd64687 -->

`0x86Ff09db814ac346a7C6FE2Cd648F27706D1D470`

###### A.6.1.1.2.2.6.1.3.2.2.2.2.2.2 - Underlying Asset Address (USDC) [Core]  <!-- UUID: 22c5c59d-0353-4b6e-95eb-eaa0a589b8d9 -->

`0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E`

###### A.6.1.1.2.2.6.1.3.2.2.2.2.2.3 - Pool Address [Core]  <!-- UUID: ce06313e-0cf1-4c24-9770-edf1aca08f3c -->

`0xA9d7d3D7e68a0cae89FB33c736199172f405C8D3`

###### A.6.1.1.2.2.6.1.3.2.2.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: 18189c82-4fa4-4013-8002-2e76aa8f29af -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.2.2.2.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 3c77c07a-6092-4a43-b26a-2a975cfaa6d1 -->

The inflow RateLimitID is: `0xeff5bd77b02bef14ff90eb3c87a6ab879b3b894eed4fd904ab94e425137e9a36`

###### A.6.1.1.2.2.6.1.3.2.2.2.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 0181c16f-79e5-4054-8d31-874674efb80e -->

The outflow RateLimitID is: `0x3361a251fa0f068ec6ce72e830c34ff0f5839a56c13e17e4c569c7c9d75217cf`

###### A.6.1.1.2.2.6.1.3.2.2.2.2.4 - Rate Limits [Core]  <!-- UUID: 196540fd-72be-4d7c-8c2c-ae7f48426034 -->

The current `maxAmount` and `slope` for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.2.2.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 2bc7c072-65e9-4b06-821c-3cc378758de1 -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 USDS/USDC
- `slope`: 50,000,000 USDS/USDC per day

###### A.6.1.1.2.2.6.1.3.2.2.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 7e5dd377-9028-4fa0-950f-d65f3364911a -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.2.2.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 12c90f28-75d6-4560-987a-6428e8ec5a47 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.2.2.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 6fe4c2f1-102e-4b71-b829-edff00a8be14 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.3 - Base [Core]  <!-- UUID: 14c653d1-6667-47c3-bea4-8bb8553bf7b9 -->

The Base Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.2.2.6.1.3.3.1 - Morpho [Core]  <!-- UUID: 469f2edf-0a5b-4d3a-a32f-e93c0a99b04b -->

The Base Instances of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.3.1.1 - Base - Morpho Grove x Steakhouse High Yield Vault USDC Instance Configuration Document [Core]  <!-- UUID: 43d78089-ba75-480c-a277-edaa6eaa6336 -->

The documents herein contain the Instance Configuration Document for the Morpho Grove x Steakhouse High Yield Vault USDC Instance.

###### A.6.1.1.2.2.6.1.3.3.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 766f35b4-24a6-4393-9a3f-c511a1bce0cc -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.3.1.1.2 - Parameters [Core]  <!-- UUID: b72d1498-2f89-40ec-8c14-08ce2a84af8c -->

The documents herein define the parameters of the Morpho Grove x Steakhouse High Yield Vault USDC Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.3.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 89b9b814-e433-4b20-bdb0-3c8189501f5f -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.3.1.1.2.1.1 - Network [Core]  <!-- UUID: 9b88ee71-1097-431f-8fbe-a5be36ef6128 -->

Base

###### A.6.1.1.2.2.6.1.3.3.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 4e1857f5-a3c8-408d-96c1-913fd81c3848 -->

Morpho

###### A.6.1.1.2.2.6.1.3.3.1.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: b08511eb-0c49-4077-9676-da153fbf2797 -->

USDC

###### A.6.1.1.2.2.6.1.3.3.1.1.2.1.4 - Token [Core]  <!-- UUID: 6ff4aa1b-d139-44af-baae-b8c10220b107 -->

grove-bbqUSDC

###### A.6.1.1.2.2.6.1.3.3.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 99a5b0c0-88a8-4f3a-9bf3-b87b6f0fdf39 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.3.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 1dc90986-481b-4e3a-a38c-7a9a636bb1da -->

`0xBeEf2d50B428675a1921bC6bBF4bfb9D8cF1461A`

###### A.6.1.1.2.2.6.1.3.3.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 200c6217-d44c-4a1e-90b3-94735e35959a -->

`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`

###### A.6.1.1.2.2.6.1.3.3.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: f8e73145-23c5-48f6-b48b-62e4f7b8af0d -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.3.1.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 9e4275e9-c6b0-43a3-a5ff-1e12dc215267 -->

The inflow RateLimitID is: `0xb5c3e377398c99e28d39340657bbc979bef79e01e2af3d0ff742e30722cd0d5a`.

###### A.6.1.1.2.2.6.1.3.3.1.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 24179f21-d109-4298-b0c8-b0a182d94bce -->

The outflow RateLimitID is: `0x13e37cfd8b7a0e3f59d4b4424894c2a3693ccf0c313905615ae9848a32e2db97`.

###### A.6.1.1.2.2.6.1.3.3.1.1.2.4 - Rate Limits [Core]  <!-- UUID: d394483b-e739-4346-948b-488fb942a48f -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.3.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: a1c1cca8-b6a3-440b-ae26-9393b95d328f -->

The inflow rate limits are:

- `maxAmount`: 20,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.3.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: b39a0a7f-3e17-4cf3-b96b-a1a16fc8ae13 -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.3.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 9a9ad1a3-ce48-4947-9da1-13dfcd450ee3 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.3.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: a274fcdf-dc71-4b78-be4d-e41d1622e076 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.3.2 - Base - Steakhouse Prime Instant USDC Morpho Vault V2 Instance Configuration Document [Core]  <!-- UUID: d47ec9c3-b308-453a-989a-7396504f6a99 -->

The documents herein contain the Instance Configuration Document for the Steakhouse Prime Instant USDC Morpho Vault V2 Instance.

###### A.6.1.1.2.2.6.1.3.3.2.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 7bc64313-cdc1-4877-947e-df6c7c22a28e -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.3.2.2 - Parameters [Core]  <!-- UUID: 8a19e28f-444a-4603-8905-0c6b1bfa9155 -->

The documents herein define the parameters of the Steakhouse Prime Instant USDC Morpho Vault V2 Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.3.2.2.1 - Instance Identifiers [Core]  <!-- UUID: 8f4a9995-4963-4d49-8694-725617a2c074 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.3.2.2.1.1 - Network [Core]  <!-- UUID: 1dae9d3c-8010-48d5-9ee4-620f72b345cd -->

Base

###### A.6.1.1.2.2.6.1.3.3.2.2.1.2 - Target Protocol [Core]  <!-- UUID: c9751457-f617-4bc3-bf8a-0fe0ac7d086f -->

Morpho

###### A.6.1.1.2.2.6.1.3.3.2.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: 3acf8d38-4eae-4ceb-b482-4754d2aafad2 -->

USDC

###### A.6.1.1.2.2.6.1.3.3.2.2.1.4 - Token [Core]  <!-- UUID: fb07802c-ae95-4214-9762-db19fae2b671 -->

steakUSDC

###### A.6.1.1.2.2.6.1.3.3.2.2.2 - Contract Addresses [Core]  <!-- UUID: 9a607af8-7f0a-4686-98c2-f62afc557f51 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.3.2.2.2.1 - Token Address [Core]  <!-- UUID: e85ae1d4-c31d-4eae-a05c-6a1844918cfd -->

`0xbeef0e0834849aCC03f0089F01f4F1Eeb06873C9`

###### A.6.1.1.2.2.6.1.3.3.2.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 889f7585-dcca-4e87-a9ca-bb1308115252 -->

`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`

###### A.6.1.1.2.2.6.1.3.3.2.2.3 - Rate Limit IDs [Core]  <!-- UUID: a4d71080-74e8-48dd-ba3f-1810b4ba08c4 -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.3.2.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 3269cc14-28bd-405e-8d72-dd22528573cf -->

The inflow RateLimitID is: `0xcc33156879fb03deee37b5ff243fa9afa95b94d13a2ab710f8096c0b5f053f3b`.

###### A.6.1.1.2.2.6.1.3.3.2.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 35e4b715-6409-490c-b42d-c1a24611d452 -->

The outflow RateLimitID is: `0x6cbf2a3469ddd029ba9744291f720dfed49b9d475ef870978c70f12ee6831646`.

###### A.6.1.1.2.2.6.1.3.3.2.2.4 - Rate Limits [Core]  <!-- UUID: 881815fb-a206-4e1a-9852-c701d5ba4e92 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.3.2.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 0ebb71f7-71c7-4668-9e70-1771e58cec79 -->

The deposit rate limits are:

- `maxAmount`: 20,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.3.2.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: bec9a1fa-aace-47eb-a663-08d1abd70b60 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.3.2.2.4.3 - Max Exchange Rate [Core]  <!-- UUID: 3b96571e-bd04-44dd-b729-3c59288d80b1 -->

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 2 USDC.

- `setMaxExchangeRate(STEAKHOUSE_PRIME_INSTANT_USDC_V2, 1e18, 2e6)`

###### A.6.1.1.2.2.6.1.3.3.2.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 9418d9ac-66d4-41c7-80cc-b0de328ac09c -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.3.2.3 - Instance-specific Operational Processes [Core]  <!-- UUID: aac6839f-b2a7-40f6-9fe3-c2366a0aa957 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.4 - Plasma [Core]  <!-- UUID: 348787e7-de5d-465c-9e19-3e8740f04efc -->

The Plasma Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.2.2.6.1.3.4.1 - Aave [Core]  <!-- UUID: 9587d7aa-8ac3-41d1-ba77-ee5a086a2706 -->

The Plasma Instances of the Aave Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.4.1.1 - Plasma - Aave v3 USDT0 Instance Configuration Document [Core]  <!-- UUID: 7a620ce6-c67a-4c15-b7fb-c8b869a28a0f -->

The documents herein contain the Instance Configuration Document for the Aave v3 USDT0 Instance.

###### A.6.1.1.2.2.6.1.3.4.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 5e65df67-fa1e-414d-8f0c-7a9b99db4640 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.4.1.1.2 - Parameters [Core]  <!-- UUID: d6f69e43-7f2a-4116-992c-526ef48c100e -->

The documents herein define the parameters of the Aave v3 USDT0 Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.4.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 8b7a0db8-da51-43c2-8d0a-512a8d95e348 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.4.1.1.2.1.1 - Network [Core]  <!-- UUID: 2783ab68-e321-4635-886c-6cb3f84ee88f -->

Plasma

###### A.6.1.1.2.2.6.1.3.4.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 6ebe8640-bc0f-4637-a49f-645002785274 -->

Aave v3

###### A.6.1.1.2.2.6.1.3.4.1.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: c3aa0280-f998-4510-a1fd-45bb47c62f4b -->

USDC

###### A.6.1.1.2.2.6.1.3.4.1.1.2.1.4 - Token [Core]  <!-- UUID: f8e5ff09-11a4-42da-b5f8-f3f2152be978 -->

USDT0

###### A.6.1.1.2.2.6.1.3.4.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 3c791810-2663-432b-9f8a-7276c721c3d2 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.4.1.1.2.2.1 - Token Address [Core]  <!-- UUID: c1b87980-9050-48ba-82ef-b5f65ba0840f -->

`0x5D72a9d9A9510Cd8cBdBA12aC62593A58930a948`

###### A.6.1.1.2.2.6.1.3.4.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: bfacb6db-078c-49f1-9e68-0e8a1c9ddef8 -->

`0xB8CE59FC3717ada4C02eaDF9682A9e934F625ebb`

###### A.6.1.1.2.2.6.1.3.4.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 49ae5000-35bb-497f-a545-2369859b651a -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.4.1.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: a54c1592-0be9-45f8-8a46-8dd2da0e0e24 -->

The inflow RateLimitID is: `0xd97a9a164c3a3da9ba6f443e90f688c005720ace173ac2c6fbd10cc9c67a174e`.

###### A.6.1.1.2.2.6.1.3.4.1.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 3895d9f5-bde8-4b8a-95f4-0fae627ee25e -->

The outflow RateLimitID is: `0xc170dc947a54b39bf03cfdfa8249447fdacf93d397502740f6703d80ed3d98e7`.

###### A.6.1.1.2.2.6.1.3.4.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 9c8fc963-4a61-4157-a665-bd1ff47f0ae0 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.4.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 3035fcf7-9426-46a7-9223-3204d922ca14 -->

The inflow rate limits are:

- `maxAmount`: 20,000,000 USDT0
- `slope`: 20,000,000 USDT0 per day

###### A.6.1.1.2.2.6.1.3.4.1.1.2.4.2 - Outflow Rate Limits [Core]  <!-- UUID: 8eeb5709-8e90-44ed-a384-d99df2a89e85 -->

The outflow rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.4.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: dfc74dd9-8390-4428-96e4-9b09c1ce0955 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.4.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 5ad3319c-8c5a-4ba3-8578-29ab5bd51830 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.5 - Plume [Core]  <!-- UUID: 0e282f82-8b41-4657-92c3-4939b112ec77 -->

The Plume Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.2.2.6.1.3.5.1 - Centrifuge [Core]  <!-- UUID: 75f40bed-64ab-4240-b0fe-d38ba928e237 -->

The Plume Instances of the Centrifuge Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.5.1.1 - Plume - Centrifuge ACRDX Instance Configuration Document [Core]  <!-- UUID: a1a1fa83-6c86-49fe-9629-d5ce4b24ed8b -->

The documents herein contain the Instance Configuration Document for the Centrifuge ACRDX Instance.

###### A.6.1.1.2.2.6.1.3.5.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 4392f549-4d6e-4b80-8618-29483d1b7c7e -->

`Pending`

###### A.6.1.1.2.2.6.1.3.5.1.1.2 - Parameters [Core]  <!-- UUID: 415f9bbf-2f2d-439e-91e0-415b0e800555 -->

The documents herein define the parameters of the Centrifuge ACRDX Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.5.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 4a716487-e052-4f94-8515-b86a7800cbc9 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.5.1.1.2.1.1 - Network [Core]  <!-- UUID: 8eb8159a-9148-4b56-a39b-57443c29f5fb -->

Plume

###### A.6.1.1.2.2.6.1.3.5.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 23d754de-f3fd-47f1-b5e9-6f4a78e7034d -->

Centrifuge ACRDX

###### A.6.1.1.2.2.6.1.3.5.1.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: ed660630-a95e-43d4-ac72-cfd514ec9067 -->

USDC

###### A.6.1.1.2.2.6.1.3.5.1.1.2.1.4 - Token [Core]  <!-- UUID: 9a69776f-e214-42aa-a249-1bc5835ff71a -->

ACRDX

###### A.6.1.1.2.2.6.1.3.5.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 170397f2-f92a-40c5-9560-8c5be6eaf9c0 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.5.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 08beab86-27af-4c89-8d68-c8b1ad0c8476 -->

`0x9477724Bb54AD5417de8Baff29e59DF3fB4DA74f`

###### A.6.1.1.2.2.6.1.3.5.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: e9d21b2c-cfec-4abd-a611-c7586d5acdb2 -->

`0x222365EF19F7947e5484218551B56bb3965Aa7aF`

###### A.6.1.1.2.2.6.1.3.5.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 870debbb-51c3-4b1b-892e-aa434de29442 -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.5.1.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: eb02a060-d1b3-4113-a484-8f497fbded01 -->

The inflow RateLimitID is: `0xb8139d1c2486c30929b3cb3a487a3d9c3885f49cff1f07e9393262b15ef1158a`

###### A.6.1.1.2.2.6.1.3.5.1.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: e0b46e30-c702-4c8c-a471-f0ece288a71b -->

The outflow RateLimitID is: `0x58aa7b39a6c9894ea4a4cd6868d014c718d09913cdf5d793e21509f0ccd32495`

###### A.6.1.1.2.2.6.1.3.5.1.1.2.4 - Rate Limits [Core]  <!-- UUID: b14eb131-1eea-423f-8ad2-71de61e00897 -->

The current `maxAmount` and `slope` for this conduit's inflow/outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.5.1.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 1a7f2fdf-1c26-4638-881d-02f5cc1ae1b5 -->

The deposit rate limits are:

- `maxAmount`: 20,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.5.1.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 7c1b8e7c-3004-4c98-a078-8ce0bbdf1141 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.5.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 2b814864-8ffe-420e-a060-24224fccf1b9 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.5.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: efbb5106-cc25-4d93-9fa7-50f3b8f3ad29 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.6 - Monad Instances [Core]  <!-- UUID: 27de13c9-de42-4846-816e-10ae03d61136 -->

The Monad Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.2.2.6.1.3.6.1 - Uniswap [Core]  <!-- UUID: 58c75470-5232-46fc-8e2a-28f4bdc6dfd5 -->

The Monad Instances of the Uniswap Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.6.1.1 - Monad - Uniswap AUSD/USDC Instance Configuration Document [Core]  <!-- UUID: c4d60460-2694-4d88-bf96-4f4141482cb5 -->

The documents herein contain the Instance Configuration Document for the Monad Uniswap AUSD/USDC Instance.

###### A.6.1.1.2.2.6.1.3.6.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 69723e54-7c6b-4ddc-854c-6477b1884e15 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.6.1.1.2 - Parameters [Core]  <!-- UUID: f27e8a20-88f9-4f85-8e3f-28324751cd6d -->

The documents herein define the parameters of the Monad Uniswap AUSD/USDC Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.6.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 09991d1f-ecd9-44c4-a15f-726494579136 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.6.1.1.2.1.1 - Network [Core]  <!-- UUID: 9b511ae4-773f-41e3-a170-070b05026fa9 -->

Monad

###### A.6.1.1.2.2.6.1.3.6.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: fce86e17-2a7c-4ff2-ada6-6f3ec57b7cf9 -->

Uniswap AUSD/USDC

###### A.6.1.1.2.2.6.1.3.6.1.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: ae4d43f2-e97f-4aa4-ab78-674a11cc246a -->

USDC

###### A.6.1.1.2.2.6.1.3.6.1.1.2.1.4 - Token [Core]  <!-- UUID: 9ad52308-e46b-463b-ba6a-6bf541323206 -->

Uniswap AUSD/USDC Pool

###### A.6.1.1.2.2.6.1.3.6.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 22326048-1218-49b7-99bd-b71bf9f8212c -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.6.1.1.2.2.1 - Pool Address [Core]  <!-- UUID: 65f7e17e-61c6-452c-a352-abc2f9e92fb3 -->

`0x6B405DCA74897c9442d369DcF6c0EC230f7E1c7C`

###### A.6.1.1.2.2.6.1.3.6.1.1.2.2.2 - Underlying Asset Address (USDC) [Core]  <!-- UUID: 4e680b6a-9f48-41d7-b7aa-655a36a5c068 -->

`0x754704Bc059F8C67012fEd69BC8A327a5aafb603`

###### A.6.1.1.2.2.6.1.3.6.1.1.2.2.3 - Broker Address (Ethereum Mainnet) [Core]  <!-- UUID: f2093974-27c4-48ef-94d7-2c4f5b3df3f9 -->

`0xD94F9ef3395BBE41C1f05ced3C9a7dc520D08036`

###### A.6.1.1.2.2.6.1.3.6.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 2e3e8ebe-335d-4a66-a466-ca87e4bf42ab -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.6.1.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 5f26f655-a1e1-4e47-b0cb-a59fb7b40e19 -->

The inflow RateLimitID is: `0x098ad67dc41c1a5892ec3ef5fd411198dc11962475e9ef2e0362e6cb7f5a2174`.

###### A.6.1.1.2.2.6.1.3.6.1.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 6e491073-f15f-49bd-ab06-3d5277c75dbb -->

The outflow RateLimitID is: N/A

###### A.6.1.1.2.2.6.1.3.6.1.1.2.4 - Rate Limits [Core]  <!-- UUID: d7fdb0e6-5763-4cf2-ba60-25b24e9ca655 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.6.1.1.2.4.1 - Deposit Rate Limits (via FalconX) [Core]  <!-- UUID: 607a906a-da69-4105-a519-6e4cfa529c1d -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 USDC
- `slope`: 50,000,000 USDC per day

###### A.6.1.1.2.2.6.1.3.6.1.1.2.4.2 - Withdrawal Rate Limits (via FalconX) [Core]  <!-- UUID: a3862cd4-ff0e-4f7d-bcf9-cc1a207c74d6 -->

The withdrawal rate limits are:

- `maxAmount`: N/A
- `slope`: N/A

###### A.6.1.1.2.2.6.1.3.6.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: ad810569-b88a-4d10-9563-cc0e2cfb27f4 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.6.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 53743f66-97ba-44ed-b386-b0ab75d9b8e4 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.7 - Robinhood Chain [Core]  <!-- UUID: f6cfd29f-04f3-45b7-b21e-e44f88096aae -->

The Robinhood Chain Instances of the Grove Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.2.2.6.1.3.7.1 - Morpho [Core]  <!-- UUID: 586e6ab6-feeb-486e-b267-9883f59b1105 -->

The Robinhood Chain Instances of the Morpho Protocol with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.7.1.1 - Robinhood Chain - Grove x Steakhouse USDG Morpho Vault V2 Instance Configuration Document [Core]  <!-- UUID: 5cd87e2a-a92f-4110-950b-329c7de0d76d -->

The documents herein contain the Instance Configuration Document for the Grove x Steakhouse USDG Morpho Vault V2 Instance.

###### A.6.1.1.2.2.6.1.3.7.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: f8fc00b4-61b6-4b11-90a2-06fe4832b56f -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.7.1.1.2 - Parameters [Core]  <!-- UUID: 2fd231b4-2065-4d8f-ae7b-bfc3411f597a -->

The documents herein define the parameters of the Grove x Steakhouse USDG Morpho Vault V2 Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: fa3e9179-67d1-448d-a54d-d72e3d66dfaa -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.1.1 - Network [Core]  <!-- UUID: bc1ea5d3-6e21-4e77-b819-631f7a97cf47 -->

Robinhood Chain

###### A.6.1.1.2.2.6.1.3.7.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: ee5646dc-9faa-4903-ab3d-113614de2398 -->

Morpho

###### A.6.1.1.2.2.6.1.3.7.1.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: e7bf240d-e630-42b8-8d01-c23092c80ff0 -->

USDG

###### A.6.1.1.2.2.6.1.3.7.1.1.2.1.4 - Token [Core]  <!-- UUID: 9efebab1-78cd-4c2c-8ae6-243ef4ed9073 -->

groveUSDG

###### A.6.1.1.2.2.6.1.3.7.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: e2ac9d21-1065-4ad6-9c32-2d3393b10b65 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 72eb8dad-5d11-4600-8c0c-c37f560f7201 -->

`0xBEEff039907422219Fb367e525954DDC092854d9`

###### A.6.1.1.2.2.6.1.3.7.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: e767deb9-75d4-493a-992e-3691e666ab2f -->

`0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168`

###### A.6.1.1.2.2.6.1.3.7.1.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 674c9991-ba05-4bc9-8de0-9b1ea52d8a3d -->

The specific `RateLimitID`(s) for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 9765bde3-8b0f-478c-a230-89958bcdef99 -->

The inflow RateLimitID is: `0x056c8e9e2046ef2d9e785dd5ffd9eeb475b862bf46f551cf91825eab45225e48`.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: 63cef06c-7a72-47e3-8e49-6842c87159cb -->

The outflow `RateLimitID` will be specified in a future iteration of the Grove Artifact.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.4 - Rate Limits [Core]  <!-- UUID: 98848df5-201c-45ad-9cc6-11281649ef97 -->

The current `maxAmount` and `slope` for this conduit’s inflow and outflow are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.4.1 - Deposit Rate Limits [Core]  <!-- UUID: 7352db9b-9177-4ffb-8554-8d131008c607 -->

The deposit rate limits are:

- `maxAmount`: 50,000,000 USDG
- `slope`: 50,000,000 USDG per day

###### A.6.1.1.2.2.6.1.3.7.1.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: 63c0f9fd-e862-4928-9e36-eaa13767ae90 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.2.2.6.1.3.7.1.1.2.4.3 - Max Exchange Rate [Core]  <!-- UUID: e9ed6ba5-c7a8-4400-acd4-abe0e3f75fb3 -->

Controllers now have protections that require a `maxExchangeRate` to be set for deposits. The following ensures 1 share can represent at most 1.15 USDG (current share price is ~1.00).

- `setMaxExchangeRate(GROVE_X_STEAKHOUSE_USDG_V2, 1e18, 1.15e6)`

###### A.6.1.1.2.2.6.1.3.7.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: 5c7888fe-ba8c-460e-b00e-460e6b4e01da -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.5.1 - Maximum Exposure [Core]  <!-- UUID: 689ed5dc-1843-4a75-bc7a-a4147caa062e -->

Total USDG exposure may not exceed 100 million USDS.

###### A.6.1.1.2.2.6.1.3.7.1.1.2.5.2 - CRR [Core]  <!-- UUID: 29aa32da-c270-4ebd-82f3-3ecfd483dd6d -->

The CRR for this Instance, as specified in [A.3.2.1.1.1 - Capital Ratio Requirement](3828778e-0197-4ce9-a836-6770d04f2ea9), applies to the approved spUSDG/USDG market and is initialized at 3%, decreasing linearly to 0.65% over the four (4) weeks following its onboarding. Any allocation to the syrupUSDG/USDG market, which is not approved, is subject to a 100% CRR.

###### A.6.1.1.2.2.6.1.3.7.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: fdc10843-70fb-444c-99a5-6bc104898fda -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

###### A.6.1.1.2.2.6.1.3.7.2 - Paxos [Core]  <!-- UUID: 89858132-1cc9-43c4-a607-68a3c45224ea -->

The Robinhood Chain Instances of Paxos with `Active` Status are stored herein.

###### A.6.1.1.2.2.6.1.3.7.2.1 - Robinhood Chain - USDG To USDC Via Paxos Instance Configuration Document [Core]  <!-- UUID: 34064628-ef20-4803-bd03-91c4890c9f85 -->

The documents herein contain the Instance Configuration Document for the USDG To USDC Via Paxos Instance.

###### A.6.1.1.2.2.6.1.3.7.2.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 15687a43-834a-40ad-8ef4-157d7ef54bc0 -->

**`Pending`**

###### A.6.1.1.2.2.6.1.3.7.2.1.2 - Parameters [Core]  <!-- UUID: 582c7771-4179-4bc4-8697-1f74983795b4 -->

The documents herein define the parameters of the USDG To USDC Via Paxos Instance of the Allocation System Primitive.

###### A.6.1.1.2.2.6.1.3.7.2.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 3e72827a-aca1-40e0-b332-a31cc1da4bb1 -->

The documents herein define the Instance identifiers.

###### A.6.1.1.2.2.6.1.3.7.2.1.2.1.1 - Network [Core]  <!-- UUID: 62d200cb-9bdb-46e8-8472-0d1ceba8447a -->

Robinhood Chain

###### A.6.1.1.2.2.6.1.3.7.2.1.2.1.2 - Target Protocol [Core]  <!-- UUID: 5d7a51e8-0b96-4178-aa89-fca37a8df4f8 -->

Paxos

###### A.6.1.1.2.2.6.1.3.7.2.1.2.1.3 - Asset Supplied By Grove Liquidity Layer [Core]  <!-- UUID: e962eaf4-1f71-4d01-b98f-640d91198fbe -->

USDG

###### A.6.1.1.2.2.6.1.3.7.2.1.2.1.4 - Token to Receive [Core]  <!-- UUID: 3e1e9958-47bc-43bf-8706-7fe94da65ee5 -->

USDC

###### A.6.1.1.2.2.6.1.3.7.2.1.2.2 - Contract Addresses [Core]  <!-- UUID: bc30ad8a-75fb-421d-aa40-41f4d4214af8 -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.2.2.6.1.3.7.2.1.2.2.1 - Token Address [Core]  <!-- UUID: 82df3c6c-85a2-4ba2-917f-f3ea230b610d -->

`0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168`

###### A.6.1.1.2.2.6.1.3.7.2.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: 67c02040-d434-4a46-b252-cb9c569e78c4 -->

`0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168`

###### A.6.1.1.2.2.6.1.3.7.2.1.2.2.3 - Paxos Deposit Address [Core]  <!-- UUID: 957f4dbd-5183-4689-8760-cc0ed11bdc78 -->

`0xfC0a7Ed7C5146B26eB38FA92c71F434A7178b06e`

###### A.6.1.1.2.2.6.1.3.7.2.1.2.3 - Rate Limit IDs [Core]  <!-- UUID: 0b2635b7-e0a5-4186-a90a-de346682fade -->

The transferAssets `RateLimitID` for this conduit is: `0x6514f636131e8989437496ad745c5671d7794873c5c1cd6d0a8b5b42031e5c9d`.

###### A.6.1.1.2.2.6.1.3.7.2.1.2.4 - Rate Limits [Core]  <!-- UUID: 5325d4d3-6e93-4ea1-86f3-91d538be03ed -->

The current TransferAsset rate limits for this conduit’s transferAssets operations are defined in the subdocuments herein.

###### A.6.1.1.2.2.6.1.3.7.2.1.2.4.1 - TransferAssets Rate Limits [Core]  <!-- UUID: e75d1516-8cd4-4a21-9441-e93f40692118 -->

The transferAssets rate limits are:

- `maxAmount`: 50,000,000 USDG
- `slope`: 50,000,000 USDG per day

###### A.6.1.1.2.2.6.1.3.7.2.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: e672e1c6-bdbb-45f9-bf71-d68d42b6ffa6 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.2.2.6.1.3.7.2.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 9c66cd58-6464-4259-ac10-34f57a1adb6d -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Grove Liquidity Layer processes.

##### A.6.1.1.2.2.6.1.4 - Completed Instances [Core]  <!-- UUID: fd06fedd-819d-4e0a-a266-ecf5ede0343b -->

The Instances of the Grove Liquidity Layer with `Completed` Status are stored herein.

##### A.6.1.1.2.2.6.1.5 - In Progress Invocations [Core]  <!-- UUID: 0bf496c2-5a2a-4ec3-8354-bc0dea0657c8 -->

The in progress Invocations of the Allocation System Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.6.1.3 - Active Instances](1f16c7b1-eddf-4106-85f7-3425bf67ef1e).

#### A.6.1.1.2.2.6.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: 5c6804a0-df8c-4a47-82d4-cff1b44f680b -->

The documents herein contain all data and specifications for Grove’s Instances of the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.6.1.1.2.2.6.2.1 - Primitive Hub Document [Core]  <!-- UUID: 6f06a403-ef8f-4623-ad1f-f136adf3a533 -->

The documents herein organize all base information relevant to Grove’s usage of the Risk Capital Rental Primitive.

###### A.6.1.1.2.2.6.2.1.1 - Global Activation Status [Core]  <!-- UUID: f6dac7a5-a35c-4ead-979a-b5dba1e89f0c -->

`Inactive`

###### A.6.1.1.2.2.6.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 75fef570-0632-4721-91c7-72b904dd7c78 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 9b363d62-f785-48e8-bf4c-248262af6d9d -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.6.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 5c973874-a0c1-4fa9-a5b5-3d5ae92ffe86 -->

This document contains a Directory of all prospective Instances of the Risk Capital Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.6.2.1.2 - Active Instances Directory](75fef570-0632-4721-91c7-72b904dd7c78), whereas failed Invocations are Archived in [A.6.1.1.2.2.6.2.1.5 - Hub Data Repository](b222a1c8-a369-45cb-8179-221c29179564).

###### A.6.1.1.2.2.6.2.1.5 - Hub Data Repository [Core]  <!-- UUID: b222a1c8-a369-45cb-8179-221c29179564 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.6.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: b276c0f8-15f5-492b-b7b9-f3df603354c6 -->

The subtrees for archived Invocations and Instances of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.2.2.6.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 3d09f988-872e-46a4-871d-b176052fb3a7 -->

The subtrees for failed Invocations of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.2.2.6.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 5a3df9c1-35de-4fbc-8533-8fe93f111594 -->

The subtrees for Instances of the Risk Capital Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.6.2.2 - Active Instances [Core]  <!-- UUID: 07287112-4dbb-4bfa-a73d-ea3f2845718e -->

The Instances of the Risk Capital Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.6.2.3 - Completed Instances [Core]  <!-- UUID: 3f553aac-54e2-40f5-8545-53a8065feaef -->

The Instances of the Risk Capital Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.2.2.6.2.4 - In Progress Invocations [Core]  <!-- UUID: a08608f5-a6a7-43dc-ba2f-34c685af073a -->

The in progress Invocations of the Risk Capital Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.6.2.2 - Active Instances](07287112-4dbb-4bfa-a73d-ea3f2845718e).

#### A.6.1.1.2.2.6.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: 0ec0b58d-9332-49ba-bdf8-8e0201480d1d -->

The documents herein contain all data and specifications for Groves Instances of the Asset Liability Management Rental Primitive. See [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

##### A.6.1.1.2.2.6.3.1 - Primitive Hub Document [Core]  <!-- UUID: 9ab7f0cb-ed9e-4fe5-9dfb-78b084563435 -->

The documents herein organize all base information relevant to Grove’s usage of the Asset Liability Management Rental Primitive.

###### A.6.1.1.2.2.6.3.1.1 - Global Activation Status [Core]  <!-- UUID: d57353cc-9987-44c3-8498-432704107e38 -->

`Inactive`

###### A.6.1.1.2.2.6.3.1.2 - Active Instances Directory [Core]  <!-- UUID: c2d4d693-c42c-4607-a667-f081665b4a88 -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.6.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: b6e794cb-06a3-4a97-897a-0da8b7592e6e -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.6.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 07dd6a23-424a-4eda-b47c-92e84d46025c -->

This document contains a Directory of all prospective Instances of the Asset Liability Management Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.6.3.1.2 - Active Instances Directory](c2d4d693-c42c-4607-a667-f081665b4a88), whereas failed Invocations are Archived in [A.6.1.1.2.2.6.3.1.5 - Hub Data Repository](722a01cb-c72f-41eb-be97-0adb41096e33).

###### A.6.1.1.2.2.6.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 722a01cb-c72f-41eb-be97-0adb41096e33 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.6.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 22a8dc60-26f5-4a48-853d-ffab6f6275a3 -->

The subtrees for archived Invocations and Instances of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.2.2.6.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: e64a0b04-1c8f-4092-bdb6-992876835617 -->

The subtrees for failed Invocations of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.2.2.6.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 898b5220-2c1e-4784-b241-21349c244930 -->

The subtrees for Instances of the Asset Liability Management Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.6.3.2 - Active Instances [Core]  <!-- UUID: 2b0e3614-6608-4a08-aced-531daf476b7d -->

The Instances of the Asset Liability Management Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.6.3.3 - Completed Instances [Core]  <!-- UUID: 95a17d1f-3aa5-4625-9eb3-f4dd8e391f79 -->

The Instances of the Asset Liability Management Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.2.2.6.3.4 - In Progress Invocations [Core]  <!-- UUID: 1051e006-9490-4eb5-b45c-bc644fec7ae0 -->

The in progress Invocations of the Asset Liability Management Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.6.3.2 - Active Instances](2b0e3614-6608-4a08-aced-531daf476b7d).

### A.6.1.1.2.2.7 - Core Governance Primitives [Core]  <!-- UUID: a98aca77-3ecb-47f9-bb3c-dc80cecc7052 -->

The documents herein implement the Core Governance Primitives for Grove. See [A.2.2.11 - Core Governance Primitives](6fa54611-c744-4b9d-897d-b2a20e9cae5d).

#### A.6.1.1.2.2.7.1 - Core Governance Reward Primitive [Core]  <!-- UUID: ae98d071-3e9e-4f8c-9573-f5d113596d15 -->

The documents herein contain all data and specifications for Grove’s Instances of the Core Governance Reward Primitive. See [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a).

##### A.6.1.1.2.2.7.1.1 - Primitive Hub Document [Core]  <!-- UUID: 883eaf9b-ea56-4a24-ae1e-b207ca83c281 -->

The documents herein organize all base information relevant to Grove’s usage of the Core Governance Reward Primitive.

###### A.6.1.1.2.2.7.1.1.1 - Global Activation Status [Core]  <!-- UUID: 0ce2345e-7d51-4c14-8ce2-f1fc972a8f5b -->

`Inactive`

###### A.6.1.1.2.2.7.1.1.2 - Active Instances Directory [Core]  <!-- UUID: d321600d-53e8-411e-b705-a7c6407e0343 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Active`.

###### A.6.1.1.2.2.7.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: a2bdbb72-4b08-4a55-892c-be41750ffeb3 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.2.2.7.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: ded59861-0c71-4466-b31f-c0e301f9deee -->

This document contains a Directory of all prospective Instances of the Core Governance Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.2.2.7.1.1.2 - Active Instances Directory](d321600d-53e8-411e-b705-a7c6407e0343), whereas failed Invocations are Archived in [A.6.1.1.2.2.7.1.1.5 - Hub Data Repository](b5892d1c-a837-468d-bedd-b92cc99a92cc).

###### A.6.1.1.2.2.7.1.1.5 - Hub Data Repository [Core]  <!-- UUID: b5892d1c-a837-468d-bedd-b92cc99a92cc -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.2.2.7.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: bffe84e5-d5de-4ce7-bc4f-27e03ba26eb2 -->

The subtrees for archived Invocations and Instances of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.2.2.7.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 1263a14d-8a7f-4b66-8ec5-54600c9c6288 -->

The subtrees for failed Invocations of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.2.2.7.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 0dd7d900-7ee6-428c-a637-0b072a3dd58d -->

The subtrees for Instances of the Core Governance Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.2.2.7.1.2 - Active Instances [Core]  <!-- UUID: 2e50776e-e2d8-4223-accb-67e72770e16e -->

The Instances of the Core Governance Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.2.2.7.1.3 - Completed Instances [Core]  <!-- UUID: 869969a7-22d0-4f5a-8932-5b70fcf6b1b4 -->

The Instances of the Core Governance Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.2.2.7.1.4 - In Progress Invocations [Core]  <!-- UUID: fff36d24-346a-4721-b11c-cb1a801d3dbc -->

The in progress Invocations of the Core Governance Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.2.2.7.1.2 - Active Instances](2e50776e-e2d8-4223-accb-67e72770e16e).

## A.6.1.1.2.3 - Omni Documents [Core]  <!-- UUID: df257205-6b3a-4afc-bbfd-0a35c950bb87 -->

The documents herein define Grove’s strategic intent and operational processes relating to infrastructure inherited from Sky Core, activities unrelated to Sky Primitives, or activities spanning multiple Sky Primitives.

### A.6.1.1.2.3.1 - Governance Information Unrelated To Root Edit Primitive [Core]  <!-- UUID: c1c86e47-a7db-4080-ab1f-99ed8e4892f7 -->

The documents herein specify Grove governance information that is unrelated to the use of the Root Edit Primitive. The governance process for updating the Grove Artifact is specified in the Root Edit Primitive above at [A.6.1.1.2.2.2.2 - Root Edit Primitive](da862b9f-ca77-443a-ac56-5a287c50b4db).

#### A.6.1.1.2.3.1.1 - Sky Forum [Core]  <!-- UUID: 2eaeb1d9-99ea-478d-9fba-d7410885b4e5 -->

Grove uses the Sky Forum for governance-related discussion. Posts should use the "Grove Prime" category.

#### A.6.1.1.2.3.1.2 - Sky Ecosystem Emergency Response [Core]  <!-- UUID: 33bf516a-c9e1-4ee0-8a09-69b1f2bb5604 -->

The documents herein specify Grove’s emergency response protocol in situations that impact the entire Sky Ecosystem. This protocol will be specified in a future iteration of the Grove Artifact.

#### A.6.1.1.2.3.1.3 - Agent-Specific Emergency Response [Core]  <!-- UUID: 98930f9c-13eb-433c-b485-2fb0e37d0029 -->

The documents herein specify Grove’s emergency response protocol in situations solely impacting Grove versus the broader Sky Ecosystem. This protocol will be specified in a future iteration of the Grove Artifact.

#### A.6.1.1.2.3.1.4 - Delegation Framework [Core]  <!-- UUID: 2cdb1ad7-17d3-4c5c-af64-b44ac7b25f0b -->

The documents herein specify Grove's governance delegation system, defining the rights and duties of Delegates and Delegators, as well as the processes for onboarding and offboarding Delegates.

##### A.6.1.1.2.3.1.4.1 - Delegate Definition [Core]  <!-- UUID: 98ddc3c0-3659-427c-89fa-ec1c9a3a9c15 -->

A "Delegate" is a recognized actor empowered to exercise governance voting power on behalf of one or more GROVE holders ("Delegators"). Delegates act as trusted representatives and are expected to vote in the long-term best interest of the Grove ecosystem.

A Delegate can be in one of three possible states at any given time: Active, Inactive, or Suspended. Only Active Delegates can cast votes. The current status of Delegates is recorded in [A.6.1.1.2.3.1.4.8.2.0.6.1 - List Of Delegates](d3210b97-f007-4502-b8d5-dfaf01257001).

##### A.6.1.1.2.3.1.4.2 - How Delegation Works [Core]  <!-- UUID: b742c40b-2185-4468-8d86-6825f2cc90ae -->

GROVE holders may assign ("delegate") the full voting power of their wallet to an Active Delegate at any time (see [A.6.1.1.2.3.1.4.8 - Registry Of Delegates](74727b0c-b0f2-40de-98b4-c35c509e2ecc)). The key features of delegation are specified in the subdocuments herein.

###### A.6.1.1.2.3.1.4.2.1 - Interfaces [Core]  <!-- UUID: 3b796ff6-7a10-4cc3-ae25-4b6246358c30 -->

Delegation can be executed through (i) the Grove App or (ii) directly on Grove's Snapshot page.

###### A.6.1.1.2.3.1.4.2.2 - Snapshot Voting-Power Lock [Core]  <!-- UUID: 9bce7b3d-a978-4e18-95d4-09693dcea552 -->

A snapshot records voting power at each proposal snapshot-block height. Voting power (including delegations) cannot be altered for the duration of a specific active proposal. Changes in voting power are reflected in future votes.

###### A.6.1.1.2.3.1.4.2.3 - Undelegation and Re-delegation [Core]  <!-- UUID: 4c2ff2a4-4581-4f23-9128-9fbf33e28352 -->

Delegators may revoke or move their delegation whenever no proposal is live. All changes take effect at the next snapshot-block.

###### A.6.1.1.2.3.1.4.2.4 - Restrictions [Core]  <!-- UUID: d34cb23c-e457-4d4c-832d-15c2a63218ff -->

GROVE holders may only assign their voting power to Active Delegates. This also means Delegators cannot delegate to another wallet they themselves control, unless it is an Active Delegate wallet.

##### A.6.1.1.2.3.1.4.3 - Delegate Responsibilities [Core]  <!-- UUID: 4493277e-8568-4507-8f7c-ee72529a55e4 -->

The responsibilities for Delegates are defined in the subdocuments herein.

###### A.6.1.1.2.3.1.4.3.1 - Monitor Governance Channels [Core]  <!-- UUID: f5591603-68d9-4994-b4d8-bfc1afc934d8 -->

The Delegate must track the Sky Forum ("Grove Prime" category), Discord, and any other official communication venues for new proposals and discussions.

###### A.6.1.1.2.3.1.4.3.2 - Review Proposals Thoroughly [Core]  <!-- UUID: 0d6353fb-d30c-4cb4-8047-62ffa460be30 -->

The Delegate must evaluate technical, economic, and risk implications before voting.

###### A.6.1.1.2.3.1.4.3.3 - Vote on Every Proposal [Core]  <!-- UUID: 639efd61-f4cc-485a-acfb-810c3c19e2e4 -->

The Delegate is expected to cast a vote on every governance proposal within the designated voting window. See [A.6.1.1.2.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote](f6dd56ae-ee72-4109-be99-eaf69c92c3be).

Failure to achieve this may result in non-eligibility for payment or offboarding. See [A.6.1.1.2.3.1.4.6 - Incentives And Compensation](b4efab71-53c2-4b0c-aba0-853bbc584952) and [A.6.1.1.2.3.1.4.5.2 - Non-Performance Removal](9894c47d-c281-4a7c-a888-659fbd1b731d).

###### A.6.1.1.2.3.1.4.3.4 - Abstain Only for Disclosed Conflicts [Core]  <!-- UUID: edd6351a-77c1-4dbb-85ae-5df21b48ea0a -->

The "Abstain" option may be used solely in cases where the Delegate has a documented conflict of interest for the specific proposal.

###### A.6.1.1.2.3.1.4.3.4.1 - Disclosure Of Conflicts [Core]  <!-- UUID: 1e6a5686-1965-4912-be8a-c2978ef4b9b1 -->

Conflicts must be disclosed to the Grove Foundation before the voting window (see [A.6.1.1.2.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote](f6dd56ae-ee72-4109-be99-eaf69c92c3be)) for the proposal begins.

###### A.6.1.1.2.3.1.4.3.4.2 - Abstaining For Non-Disclosed Conflicts [Core]  <!-- UUID: c5929252-d0c3-4b42-9ddf-0ffd4c204728 -->

Abstaining for any reason other than a disclosed conflict is treated as non-performance under [A.6.1.1.2.3.1.4.5 - Delegate Offboarding](c916719b-99d5-4725-868a-8c40cfa64d79).

###### A.6.1.1.2.3.1.4.3.5 - Report Rationale [Core]  <!-- UUID: b474e36a-0e08-4f86-b53e-2b69f871528f -->

The Delegate must post a concise rationale for each vote on the proposal thread.

###### A.6.1.1.2.3.1.4.3.6 - Maintain Independence [Core]  <!-- UUID: a6be0eaa-50f1-44cd-aa9d-dd4ace04b6a5 -->

The Delegate must disclose conflicts of interest and abstain where impartiality is compromised (see [A.6.1.1.2.3.1.4.3.4.1 - Disclosure Of Conflicts](1e6a5686-1965-4912-be8a-c2978ef4b9b1)). Failure to meet these obligations is grounds for offboarding (see [A.6.1.1.2.3.1.4.5 - Delegate Offboarding](c916719b-99d5-4725-868a-8c40cfa64d79)).

##### A.6.1.1.2.3.1.4.4 - Delegate Onboarding [Core]  <!-- UUID: 12f5afad-4622-4536-bb28-a71c391126ae -->

The Delegate onboarding process is specified in the subdocuments herein.

###### A.6.1.1.2.3.1.4.4.1 - Delegate Onboarding Process [Core]  <!-- UUID: c2eda7f5-882c-49cb-802b-91845a0c7889 -->

The Grove Foundation manages Delegate onboarding. The Grove Foundation may onboard a Delegate at its discretion. The Grove Foundation conducts identity verification, conflict-of-interest collection, and sanctions and undue-risk checks as it deems necessary. Upon acceptance, the Foundation notifies the Operational Facilitator, who updates [A.6.1.1.2.3.1.4.8 - Registry Of Delegates](74727b0c-b0f2-40de-98b4-c35c509e2ecc) and posts a notice on the Sky Forum.

###### A.6.1.1.2.3.1.4.4.2 - Application Requirements [Core]  <!-- UUID: 44956efb-9c81-474a-a4b5-e51969ff67a4 -->

Prospective Delegates must submit (i) identity and contact information, (ii) delegate wallet address, and (iii) a signed statement accepting the responsibilities in [A.6.1.1.2.3.1.4.3 - Delegate Responsibilities](4493277e-8568-4507-8f7c-ee72529a55e4). These requirements are further specified in the subdocuments herein.

###### A.6.1.1.2.3.1.4.4.2.1 - Requirement To Verify Identity [Core]  <!-- UUID: 2cf9981e-d879-42f9-ae9e-12facd69c117 -->

Every prospective Delegate must complete an initial, confidential identity verification process with the Grove Foundation, subject to additional KYC verification as necessary in the future. Delegates may remain anonymous or pseudonymous to the public.

###### A.6.1.1.2.3.1.4.4.2.2 - Conflict-of-Interest Disclosure [Core]  <!-- UUID: 72daa5ef-b7f5-4e0a-bc67-967670fdbc79 -->

At onboarding, prospective Delegates must provide any known conflicts of interest to the Grove Foundation. Disclosures must be updated as new conflicts arise.

###### A.6.1.1.2.3.1.4.4.2.3 - Eligibility [Core]  <!-- UUID: efb0166c-6ab5-4068-a9a5-40d1b5dea3ed -->

Individuals or entities listed on any international sanctions list are ineligible to serve as Delegates. In addition, a prospective Delegate may be deemed ineligible if, in the Grove Foundation's sole discretion, their participation would be unlawful or would pose undue risk to Grove.

###### A.6.1.1.2.3.1.4.4.2.4 - Ongoing Compliance [Core]  <!-- UUID: e14788a8-56d3-468c-be05-7570c8780bd8 -->

Delegates must promptly update the Grove Foundation on any material change in their legal status. Failure to do so results in automatic suspension until rectified.

###### A.6.1.1.2.3.1.4.4.2.5 - Grounds For Disqualification [Core]  <!-- UUID: df7c0931-4e78-4e68-8891-5c80f5272705 -->

Submission of fraudulent information, criminal indictment for financial crime, or repeated governance negligence (see [A.6.1.1.2.3.1.4.5.2 - Non-Performance Removal](9894c47d-c281-4a7c-a888-659fbd1b731d)) constitutes grounds for the Grove Foundation to remove the Delegate under [A.6.1.1.2.3.1.4.5.3 - Emergency Removal](82a88107-8e09-4322-a92e-4e7f5f51835d).

###### A.6.1.1.2.3.1.4.4.2.6 - Application Does Not Guarantee Acceptance [Core]  <!-- UUID: 9c597485-5b24-4d33-a9c4-448d74bc7f7c -->

Submission of a Delegate Application does not guarantee acceptance. Acceptance is at the Grove Foundation's sole discretion. The Grove Foundation may approve or deny any application at any time, for any reason or no stated reason including legal, sanctions, risk, operational, or capacity considerations even if the applicant satisfies the minimum requirements in [A.6.1.1.2.3.1.4.4.2 - Application Requirements](44956efb-9c81-474a-a4b5-e51969ff67a4). The Grove Foundation is not required to provide individualized rationale. Decisions are final unless otherwise provided in this Artifact.

###### A.6.1.1.2.3.1.4.4.3 - Minimum Term [Core]  <!-- UUID: 2e484aa5-73d1-4773-a97d-cccf9323c576 -->

Delegates are appointed by the Grove Foundation to fixed six (6) month terms aligned to calendar half-years (January 1 – June 30; July 1 – December 31). For any given Delegate, terms renew automatically unless determined otherwise by the Grove Foundation.

As an exception, the initial term begins on August 1, 2026 and runs until December 31, 2026; all subsequent terms follow the calendar half-years above.

###### A.6.1.1.2.3.1.4.4.4 - Delegate Record [Core]  <!-- UUID: 26fa3dac-a92d-4482-bfd2-5c6ba714e167 -->

Accepted Delegates are appended to [A.6.1.1.2.3.1.4.8 - Registry Of Delegates](74727b0c-b0f2-40de-98b4-c35c509e2ecc).

##### A.6.1.1.2.3.1.4.5 - Delegate Offboarding [Core]  <!-- UUID: c916719b-99d5-4725-868a-8c40cfa64d79 -->

The delegation offboarding process is specified in the subdocuments herein.

###### A.6.1.1.2.3.1.4.5.1 - Voluntary Offboarding [Core]  <!-- UUID: e150148c-b8ba-413f-9502-8702c7749de5 -->

A Delegate can voluntarily offboard by submitting a resignation message in the Grove Prime category of Sky Forum with a signed message from their Delegate wallet as proof. The offboarding takes effect immediately after all active proposals conclude.

###### A.6.1.1.2.3.1.4.5.2 - Non-Performance Removal [Core]  <!-- UUID: 9894c47d-c281-4a7c-a888-659fbd1b731d -->

A Delegate is automatically offboarded if they:

- Fail to vote on at least three (3) proposals in a row; or
- Maintain a voting percentage less than 85%.

###### A.6.1.1.2.3.1.4.5.3 - Emergency Removal [Core]  <!-- UUID: 82a88107-8e09-4322-a92e-4e7f5f51835d -->

The Grove Foundation can immediately offboard a delegate if they:

- Breach disclosure / conflict-of-interest duties;
- Engage in malicious or negligent conduct; or
- Fail to provide acceptable KYC or updated KYC when requested.

###### A.6.1.1.2.3.1.4.5.4 - Updating Of Status [Core]  <!-- UUID: ea0c2f9f-6af2-4251-badc-be74211b1642 -->

Upon offboarding, the Delegate's status in [A.6.1.1.2.3.1.4.8 - Registry Of Delegates](74727b0c-b0f2-40de-98b4-c35c509e2ecc) is updated to Inactive. GROVE Delegators must manually revoke their delegations and redelegate if they wish to continue participating in Grove governance.

##### A.6.1.1.2.3.1.4.6 - Incentives And Compensation [Core]  <!-- UUID: b4efab71-53c2-4b0c-aba0-853bbc584952 -->

Delegates are compensated for their service as follows:

1. Compensation amount. Active Delegates receive USD 4,000 per calendar month.
2. Administration. The Grove Foundation administers compensation from its approved operating budget.
3. Timing and proration. Payment is made monthly in arrears and prorated for partial months of service.
4. Eligibility and clawback. Payment requires the Delegate to be in good standing and to have met responsibilities in [A.6.1.1.2.3.1.4.3 - Delegate Responsibilities](4493277e-8568-4507-8f7c-ee72529a55e4) during the covered period; the Grove Foundation may withhold or claw back amounts for non-performance or breach.
5. No waiver of oversight. Compensation does not limit or waive any onboarding, renewal, or offboarding requirements.

##### A.6.1.1.2.3.1.4.7 - Security Requirements And Compromise Procedure [Core]  <!-- UUID: 00605e88-27a6-40f1-ae7e-5be7467a2da6 -->

The security requirements and procedure for a compromised key are specified in the subdocuments herein.

###### A.6.1.1.2.3.1.4.7.1 - Operational Security [Core]  <!-- UUID: 563611a3-4670-4787-9a53-31892aee9390 -->

Delegates must:

- Sign votes from a hardware wallet or an equivalent secure device.
- Use unique signing keys that are never reused for personal transactions.
- Enable Multi-Factor Authentication on any platform accounts used for governance communication.

###### A.6.1.1.2.3.1.4.7.2 - Compromised Key Response [Core]  <!-- UUID: dfb209e9-8cf2-4c08-9eda-88caf9cb3004 -->

If a Delegate suspects key compromise, the following steps must be taken:

- The Delegate must notify the Grove Foundation as soon as the breach is discovered.
- The Grove Foundation flags the Delegate in Registry of Delegates as "Suspended - Security Review" and notifies the governance community on the Sky Forum. All voting power to the suspended address is annulled.
- The Delegate may submit a new verified address; upon Grove Foundation approval, suspensions are lifted and delegations migrate at the next snapshot-block.

###### A.6.1.1.2.3.1.4.7.3 - Non-Compliance [Core]  <!-- UUID: 49f12d6e-3c59-4727-a703-56869f39363c -->

Failure to execute the steps in [A.6.1.1.2.3.1.4.7.2 - Compromised Key Response](dfb209e9-8cf2-4c08-9eda-88caf9cb3004) within 48 hours constitutes grounds for emergency removal.

##### A.6.1.1.2.3.1.4.8 - Registry Of Delegates [Core]  <!-- UUID: 74727b0c-b0f2-40de-98b4-c35c509e2ecc -->

The subdocuments herein list each active Delegate's name, wallet address, effective date, and status. Entries are maintained via an Active Data document updated by the Operational Facilitator.

###### A.6.1.1.2.3.1.4.8.1 - Template Information For Each Delegate [Core]  <!-- UUID: b6f96d7d-82a7-47fc-b0ff-86b590685bb8 -->

The list of Delegates must follow this template for each recorded Delegate:

[Insert Delegate Handle]

- Delegate Name: [Insert Handle]
- Delegate Wallet Address:
- Effective Date:
- Status: Active/Inactive/Suspended

###### A.6.1.1.2.3.1.4.8.2 - Updating List Of Delegates [Active Data Controller]  <!-- UUID: c73d762d-a4e9-425b-a293-6bb7afd7bf18 -->

The list of Delegates is defined as Active Data in [A.6.1.1.2.3.1.4.8.2.0.6.1 - List Of Delegates](d3210b97-f007-4502-b8d5-dfaf01257001).

The Active Data is updated as follows:

- Responsible Party: Operational Facilitator.
- Trigger: Receipt of onboarding, renewal, non-renewal, or discretionary offboarding notice from the Grove Foundation.
- Update Process: Direct Edit.
- Publication: The Operational Facilitator posts a notice on the Sky Forum.

###### A.6.1.1.2.3.1.4.8.2.0.6.1 - List Of Delegates [Active Data]  <!-- UUID: d3210b97-f007-4502-b8d5-dfaf01257001 -->

The information for each Delegate is listed below:

- Northbridge
    - Delegate Name: Northbridge
    - Delegate Wallet Address: `0xb5f1A4a55337493f82640E1Bed84fa9290b6EC2d`
    - Effective Date: 2026-08-01
    - Status: Active
- Yvonpipi
    - Delegate Name: Yvonpipi
    - Delegate Wallet Address: `0x1C8f136b3c8F40B82f6676f09f44E8e2b52677a8`
    - Effective Date: 2026-08-01
    - Status: Active
- Docgriffin
    - Delegate Name: Docgriffin
    - Delegate Wallet Address: `0x9eA908bd2d294161c40B9ACcB095E91FF27F09Df`
    - Effective Date: 2026-08-01
    - Status: Active

##### A.6.1.1.2.3.1.4.9 - Subject to Change [Core]  <!-- UUID: 1bd9a18e-d0b2-4e0f-b52f-62d60de06d04 -->

Grove reserves the right to vary or amend the terms set out in this Delegation Framework (see [A.6.1.1.2.3.1.4 - Delegation Framework](2cdb1ad7-17d3-4c5c-af64-b44ac7b25f0b)) at its discretion, subject to the established Grove Artifact governance procedures related to Artifact edits.

### A.6.1.1.2.3.2 - Strategic Intent [Core]  <!-- UUID: 56fec44a-f8ca-4a03-a614-2c0eb0dde262 -->

Grove will unlock the full potential of USDS by building an institutional-grade credit platform designed to facilitate credit creation and seamlessly move yield in and out of the onchain economy. Grove's priority is to make USDS more attractive through diversified stability fee streams, more efficient rates, and greater utility, with CLOs as the first step into accessing higher yielding investment-grade credit assets. To accomplish these goals, Grove will deploy a RWA Allocation Conduit focused on traditional credit opportunities, as well as crypto-native Conduits for Morpho and Curve.

#### A.6.1.1.2.3.2.1 - Collateralized Loan Obligation Strategy [Core]  <!-- UUID: 2cd87922-d450-4cc2-bce5-81c26239a015 -->

Grove will prioritize Collateralized Loan Obligations (CLOs) as the initial pathway to provide Sky ecosystem with rapid exposure to higher yielding investment-grade credit assets, establishing a scalable model for offchain credit with onchain governance.

#### A.6.1.1.2.3.2.2 - RWA Conduit [Core]  <!-- UUID: 0e6f2c26-31a2-4ce4-8ed3-2d235561e3d3 -->

Grove will begin with onboarding winners of the Grand Prix ([https://forum.skyeco.com/t/announcement-spark-tokenization-grand-prix-request-for-proposal/24631](https://forum.skyeco.com/t/announcement-spark-tokenization-grand-prix-request-for-proposal/24631)).

#### A.6.1.1.2.3.2.3 - Institutional Credit Platform [Core]  <!-- UUID: d89b9da2-caf7-423f-9305-efcd66df62d8 -->

Grove will build partnerships with leading financial institutions to scale credit opportunities. This will provide transparent insight into balance sheet allocations while delivering higher, more stable yields through diversified institutional-grade assets.

#### A.6.1.1.2.3.2.4 - Crypto-Native Conduits [Core]  <!-- UUID: f1793c13-0022-4c27-a439-17ea98d2e1d1 -->

Grove will deploy Allocation Conduits for Morpho and Curve to capture high-yield, low-risk DeFi opportunities.

##### A.6.1.1.2.3.2.4.1 - Morpho Allocation Conduit [Core]  <!-- UUID: e834343d-e67a-4e8e-acde-34e0a85ea4cd -->

Grove will allocate capital to low risk collateral to take advantage of opportunities for high rates in these markets.

##### A.6.1.1.2.3.2.4.2 - Curve Allocation Conduit [Core]  <!-- UUID: 9a76d9e7-b648-4a32-b097-1466902a4309 -->

Grove will partner with emerging stablecoins to deploy liquidity against fiat-backed stablecoins.

#### A.6.1.1.2.3.2.5 - Exploratory Allocation Opportunities [Core]  <!-- UUID: e629ebcb-4588-4305-b6ef-9a568b35d554 -->

Grove will consider allocations to basis trades, Pendle PTs, and other delta-neutral crypto primitives.

### A.6.1.1.2.3.3 - Projected Operational Roadmap [Core]  <!-- UUID: 156c9c72-46c9-4668-81b6-7e524e7a4bac -->

Grove’s phased plan to execute its strategy includes:

1. Deploy infrastructure to enable initial allocation conduits;
2. Establish manual reallocation processes; and
3. Develop quantitative reallocation parameters and conditions to optimize and decentralize conduit management over time; and
4. Develop transparent insights into the allocation of the balance sheet.

### A.6.1.1.2.3.4 - Management Of Infrastructure Inherited From Sky Core [Core]  <!-- UUID: 55a72d83-1de3-401c-aef4-9bb330abb774 -->

The documents herein specify Grove's strategy and operational processes for managing infrastructure inherited from Sky Core.

#### A.6.1.1.2.3.4.1 - Andromeda [Core]  <!-- UUID: 631d1b05-9828-4b53-a8ab-80dccf549f05 -->

Control of the Andromeda RWA Arranged Structure is currently being transitioned to Grove. Andromeda is the RWA Arranged Structure inherited from Sky Core that allocates capital into safe, short-term treasury strategies of less than one (1) year duration.

##### A.6.1.1.2.3.4.1.1 - Parameters [Core]  <!-- UUID: 73f483b4-f330-49a8-a6d8-59bccb985b5d -->

The parameters of Andromeda are defined in [A.3.3.2.7.2.1 - Andromeda](1b153f9f-7c70-4ae1-b76c-ef12f87532c6).

##### A.6.1.1.2.3.4.1.2 - Operational Process Definition [Core]  <!-- UUID: 62b93c99-8a06-4dad-a95e-96029cb5372a -->

The documents herein define the process for the ongoing management of Andromeda. Future iterations of the Artifact will specify operational processes owned by Grove.

##### A.6.1.1.2.3.4.1.3 - Data Repository [Core]  <!-- UUID: e16c9799-7be7-4482-a954-6b8fbf873fbb -->

The documents herein contain data relevant to Andromeda.

#### A.6.1.1.2.3.4.2 - Lite Peg Stability Module [Core]  <!-- UUID: beb54246-6454-4716-a381-be605560cba5 -->

Control of the Lite PSM is currently being transitioned to Grove.

##### A.6.1.1.2.3.4.2.1 - Parameters [Core]  <!-- UUID: d83f190a-99d6-4f8c-8502-d3e7e917816d -->

The parameters of the Lite PSM are defined in the Sky Core Atlas.

##### A.6.1.1.2.3.4.2.2 - Operational Process Definition [Core]  <!-- UUID: b935a218-b921-41b3-aaac-3203c2ca3b84 -->

The transfer of ongoing management of the Lite PSM is specified in Ecosystem Accord 2, see [A.2.8.2.2 - Prime Program](aa3b8e65-0ded-48c2-9c40-812debf99f32).

###### A.6.1.1.2.3.4.2.2.1 - Parameter Modification [Core]  <!-- UUID: f22bc9ce-cd9c-4f20-957f-1591b50abad0 -->

The Sky Core Facilitator currently owns the process for modifying the parameters of the Lite PSM, which process is defined in the Sky Core Atlas. This process is currently being transitioned over to Grove.

##### A.6.1.1.2.3.4.2.3 - Data Repository [Core]  <!-- UUID: 165fc3f7-39cf-4f4e-ae94-6460263b8a71 -->

The documents herein contain data relevant to the Lite PSM.

### A.6.1.1.2.3.5 - Ecosystem Accords [Core]  <!-- UUID: 8b3829dd-fb87-4b08-b1dc-224d7c993ee4 -->

Grove has formally agreed to the Ecosystem Accords herein.

#### A.6.1.1.2.3.5.1 - Ecosystem Accord 1 [Core]  <!-- UUID: 867b3512-2c21-41e2-81c2-3a442c441a14 -->

Grove engaged in terms of agreement with the Spark Agent in Ecosystem Accord 1, located in [A.2.8.2.1 - Ecosystem Accord 1: Grove And Spark Agents](9ca40096-937e-431e-af50-9ecd50c0d0a8).

#### A.6.1.1.2.3.5.2 - Ecosystem Accord 2 [Core]  <!-- UUID: dfa20b2f-e803-47f7-95fa-4e457816ae69 -->

Grove engaged in terms of agreement with Sky, Moonbow and the Spark Agent in Ecosystem Accord 2, located in [A.2.8.2.2 - Prime Program](aa3b8e65-0ded-48c2-9c40-812debf99f32).

#### A.6.1.1.2.3.5.3 - Ecosystem Accord 10 [Core]  <!-- UUID: e7057828-ca35-4c1f-8da9-05f54b73e25a -->

Grove engaged in terms of agreement with Sky in Ecosystem Accord 10, located in [A.2.8.2.10 - Ecosystem Accord 10: Sky And Grove](0cb00b28-12a8-4790-974a-a3d98fd4dc97).

### A.6.1.1.2.3.6 - DAO Resolutions [Core]  <!-- UUID: c9c04069-134f-4ab3-b99c-e922edb1cde8 -->

Grove has formally agreed to the DAO Resolutions recorded herein.

#### A.6.1.1.2.3.6.1 - Onboard To FalconX [Core]  <!-- UUID: 287ca9e6-e807-4565-a48d-83805be94b92 -->

On October 16, 2025, Grove agreed to a DAO Resolution authorizing Grove Foundation and Bamboo Grove Ltd to onboard to FalconX. See [https://gateway.pinata.cloud/ipfs/bafkreialsthk4uhtxfd7zbhy4xiwnxxowd2qwpletjefrvdmvmpkxpkola](https://gateway.pinata.cloud/ipfs/bafkreialsthk4uhtxfd7zbhy4xiwnxxowd2qwpletjefrvdmvmpkxpkola).

#### A.6.1.1.2.3.6.2 - Onboard With Ethena [Core]  <!-- UUID: 9629b16e-4f11-49bc-80be-6c85d711716c -->

On October 23, 2025, Grove agreed to a DAO Resolution authorizing Bamboo Grove to onboard with Ethena. See [https://ipfs.io/ipfs/bafkreic5vspzukckcgnx5ykwj2inqidvbfcknafa56jqgo25cveqyi565q](https://ipfs.io/ipfs/bafkreic5vspzukckcgnx5ykwj2inqidvbfcknafa56jqgo25cveqyi565q). The DAO Resolution makes reference to a Deed Poll that is approved as part of the DAO Resolution. See [https://ipfs.io/ipfs/bafkreibvyodjaosdfdzsrqjtuohwte46pol4zzmchky4t5xejaltonzi24](https://ipfs.io/ipfs/bafkreibvyodjaosdfdzsrqjtuohwte46pol4zzmchky4t5xejaltonzi24).

#### A.6.1.1.2.3.6.3 - Onboard With Ripple, Agora And Paxos [Core]  <!-- UUID: 1890a855-9e68-4705-a20c-085ee8b5f463 -->

On November 20, 2025, a DAO Resolution was passed authorizing the Grove Foundation and Bamboo Grove Ltd to onboard with Ripple, Agora, and Paxos. See [https://gateway.pinata.cloud/ipfs/bafkreia77ngaxn54wy33v3dgzqr3cm4bykulrjldvf4iyahbfy2yv3jebi](https://gateway.pinata.cloud/ipfs/bafkreia77ngaxn54wy33v3dgzqr3cm4bykulrjldvf4iyahbfy2yv3jebi).

#### A.6.1.1.2.3.6.4 - Onboard With Wintermute [Core]  <!-- UUID: d2409e5a-a85b-4a51-8f4d-46a437660154 -->

On November 27, 2025, a DAO Resolution was passed authorizing the Grove Foundation and Bamboo Grove Ltd to onboard with Wintermute. See [https://ipfs.io/ipfs/bafkreia72u565ub3iazmbsqsf4jzrobveckb2dtrcspmwn52oenyic72xu](https://ipfs.io/ipfs/bafkreia72u565ub3iazmbsqsf4jzrobveckb2dtrcspmwn52oenyic72xu).

#### A.6.1.1.2.3.6.5 - Authorization With Respect To FalconX [Core]  <!-- UUID: 062461fe-fc60-4f7c-ac28-2238756a67ea -->

On December 4, 2025, a DAO Resolution was passed authorizing the Grove Foundation and Bamboo Grove Ltd with respect to FalconX. See [https://ipfs.io/ipfs/bafkreicfhmyziwispejbngiqhfrqjy3xwvxidqnyaaaacprlp4n6gzvw7u](https://ipfs.io/ipfs/bafkreicfhmyziwispejbngiqhfrqjy3xwvxidqnyaaaacprlp4n6gzvw7u).

#### A.6.1.1.2.3.6.6 - Authorization Of Project Grove [Core]  <!-- UUID: 806e65a3-9322-4ab6-8dcb-ecdc4be13c18 -->

On December 11, 2025, a DAO Resolution was passed authorizing Grove Foundation and Grove (BVI) Ltd to take actions related to Project Grove. See [https://ipfs.io/ipfs/bafkreiamufzul447ja3prczy7cfxccvsij73vmareedlqag2xxpcwtcgxu](https://ipfs.io/ipfs/bafkreiamufzul447ja3prczy7cfxccvsij73vmareedlqag2xxpcwtcgxu).

#### A.6.1.1.2.3.6.7 - Authorization To Subscribe And Purchase Notes Issued By Galaxy CLO [Core]  <!-- UUID: db2e4893-d315-4a65-a5cc-133d7763c693 -->

On December 11, 2025, a DAO Resolution was passed authorizing Grove Foundation and Cedar Grove Ltd to subscribe for and purchase the Class B notes issued by Galaxy CLO 2025-1 LLC. See [https://gateway.pinata.cloud/ipfs/bafkreierc3rxu3d64xakeeibkqujkqbhlz3lcsnjymcckaacix55vhya6u](ttps://gateway.pinata.cloud/ipfs/bafkreierc3rxu3d64xakeeibkqujkqbhlz3lcsnjymcckaacix55vhya6u).
