# A.6.1.1.5 - Obex [Core]  <!-- UUID: f558e673-cbab-4696-8ca1-3af9b90fe5d4 -->

The documents herein specify all of the logic for Obex, including Obex’s strategy and how it uses the Sky Primitives to operationalize this strategy.

## A.6.1.1.5.1 - Introduction [Core]  <!-- UUID: e395a323-3c53-4154-a7e6-d54c363f56f2 -->

Obex is an 'incubator' Agent operationalizing a turnkey solution for the Sky Ecosystem's development and deployment of Prime and Halo Agents. This will give Agent founders a streamlined pathway to establish, build, operationalize, fundraise, and launch new Agents. The overall goal of the Obex Agent is to produce Agents for the Sky Ecosystem at scale, supporting cohorts of new Agent founders through leveraging rich content, workstreams and turnkey services for legal, risk, tech, and operational requirements.

## A.6.1.1.5.2 - Sky Primitives [Core]  <!-- UUID: de2892b7-087c-49ee-8b85-e3753987d38e -->

The documents herein implement the Sky Primitives for Obex. See [A.2.2 - Sky Primitives](fcde2604-a138-4c1b-9d9a-14895835c907).

### A.6.1.1.5.2.1 - Genesis Primitives [Core]  <!-- UUID: d5354d3f-8281-49e2-9ff6-c36091afa18a -->

The documents herein implement the Genesis Primitives for Obex. See [A.2.2.5 - Genesis Primitives](3d5e3668-8333-4908-adcc-5784cfe7f6b5).

#### A.6.1.1.5.2.1.1 - Agent Creation Primitive [Core]  <!-- UUID: de89dc5f-7351-4ea0-bc7b-4a6eb25d6a4d -->

The documents herein contain all data and specifications for Obex's Instance of the Agent Creation Primitive. See [A.2.2.5.1 - Agent Creation Primitive](82b95f6d-4883-4f08-ac3a-9d8189013fbe).

##### A.6.1.1.5.2.1.1.1 - Primitive Hub Document [Core]  <!-- UUID: 38ef6c16-11fb-400f-ba72-88e7f50fc1e8 -->

The documents herein organize all base information relevant to Obex's usage of the Agent Creation Primitive.

###### A.6.1.1.5.2.1.1.1.1 - Global Activation Status [Core]  <!-- UUID: d812fe0d-1128-4824-b0df-ea61ba23a624 -->

`Completed`

###### A.6.1.1.5.2.1.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 6229b346-ecd5-474a-bfd4-e22066a365f0 -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.1.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7c3e364b-84e7-4b47-9b5a-54978a127f97 -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.1.1.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: a1b0f1ed-1e3e-47ff-9690-afb6bfd22192 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.5.2.1.1.3.1 - Single Instance Configuration Document](9d67690d-87df-4fcf-bac0-0b2bcf75bf12).

###### A.6.1.1.5.2.1.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: c9952aea-58df-4a2e-a706-8f342a6d525c -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.5.2.1.1.1.5 - Hub Data Repository [Core]  <!-- UUID: d8bb6ab7-07b3-4224-9612-5c10b1a4cab2 -->

The document herein contains the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.1.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 2d301483-65e6-4501-828f-67012966cbae -->

The subtrees for archived Invocations and Instances of the Agent Creation Primitive are stored here.

###### A.6.1.1.5.2.1.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 7c5074c6-0cf3-4f96-bd35-ecd14d4a8cf5 -->

The subtrees for failed Invocations of the Agent Creation Primitive are stored here.

###### A.6.1.1.5.2.1.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 637cb4d7-f5d1-4181-bd60-d54f8893a4bd -->

The subtrees for Instances of the Agent Creation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.1.1.2 - Active Instances [Core]  <!-- UUID: 5f6b104e-2310-45d4-ba62-92d3a9a5ed0b -->

The Instances of the Agent Creation Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 31bafd0d-b417-4759-88af-7589f9a32518 -->

The Instances of the Agent Creation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.5.2.1.1.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 9d67690d-87df-4fcf-bac0-0b2bcf75bf12 -->

The documents herein contain the Instance Configuration Document for the Single Agent Creation Primitive Instance.

###### A.6.1.1.5.2.1.1.3.1.1 - Parameters [Core]  <!-- UUID: 151d3bb0-77bb-4aeb-8bcb-be120968400b -->

The documents herein define the parameters of the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.5.2.1.1.3.1.1.1 - Name [Core]  <!-- UUID: 05cdc5d1-c73e-4ccd-abe0-dd0a58d0c65c -->

The name of the Agent is Obex.

###### A.6.1.1.5.2.1.1.3.1.1.2 - SubProxy Account [Core]  <!-- UUID: 510817f8-7ce6-4b32-b598-186610760525 -->

The address of Obex’s SubProxy Account on the Ethereum Mainnet is `0x8be042581f581E3620e29F213EA8b94afA1C8071`.

###### A.6.1.1.5.2.1.1.3.1.1.3 - StarGuard Contract [Core]  <!-- UUID: 509c948c-1ddd-4bd2-8343-357f7981d296 -->

The address of Obex’s StarGuard contract on the Ethereum Mainnet is `0x987f1C31f9935e9926555BcFB76516bb2EcEccaD`.

###### A.6.1.1.5.2.1.1.3.1.1.3.1 - StarGuard Max Delay [Core]  <!-- UUID: b037c4fd-759b-4ea1-9b6b-3f9f86391f60 -->

The Obex StarGuard `maxDelay` is seven (7) days.

###### A.6.1.1.5.2.1.1.3.1.1.4 - Genesis Account [Core]  <!-- UUID: d77522ec-0987-474d-87b3-9377f107c9b6 -->

The address of Obex’s Genesis Account will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.1.1.3.1.1.5 - Foundation [Core]  <!-- UUID: 57b0ac97-ddd8-424c-a407-6f6ab91a3806 -->

Rubicon is the Prime Foundation associated with Obex. Its mandate is to support the development, growth, and adoption of Obex.

###### A.6.1.1.5.2.1.1.3.1.1.6 - Development Company [Core]  <!-- UUID: 44a4e626-eb16-44cb-8502-9133c97c0773 -->

Treadstone is the development company that provides services to Rubicon.

###### A.6.1.1.5.2.1.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 8171b404-5ea7-47ed-869d-8bd94f6e9e86 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.5.2.1.1.3.1.3 - Data Repository [Core]  <!-- UUID: fab9e798-14f5-4105-8dec-1e49eacc2b36 -->

The documents herein contain data relevant to the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.5.2.1.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: a5498802-b2d9-46d2-9a2e-30e546ba6110 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.1.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: a09fca08-e196-49b1-99e2-21e5c01a59cb -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.1.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 2e5c5930-3805-47c2-8c11-b05b8c5bdddc -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.5.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 3731f5d8-ff05-4c80-9f3f-2b056b6b9b38 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.5.2.1.2 - Prime Transformation Primitive [Core]  <!-- UUID: 5c7d376d-ebb0-4477-8d96-129d362e7799 -->

The documents herein contain all data and specifications for Obex's instance of the Prime Transformation Primitive. See [A.2.2.5.2 - Prime Transformation Primitive](81411106-fd6d-4f9c-b3ae-7af7b5e62482).

##### A.6.1.1.5.2.1.2.1 - Primitive Hub Document [Core]  <!-- UUID: b9e7cf68-feff-4a8b-9126-bc44bf3e7283 -->

The documents herein organize all base information relevant to Obex's usage of the Prime Transformation Primitive.

###### A.6.1.1.5.2.1.2.1.1 - Global Activation Status [Core]  <!-- UUID: 32f5e8a7-fdce-4e77-b032-4c1670ecb9da -->

`Completed`

###### A.6.1.1.5.2.1.2.1.2 - Active Instances Directory [Core]  <!-- UUID: e4e7adc0-7c85-464c-a60c-87dafb800e48 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.1.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 1ad29165-0b55-4b7d-a908-c8e097a9d053 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.1.2.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: b404798f-056d-4c57-b252-4b30d960b8e3 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.5.2.1.2.3.1 - Single Instance Configuration Document](2fd59b03-9278-4371-a3f1-fe9514ab322b).

###### A.6.1.1.5.2.1.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 79851842-32b3-4e42-bbbc-2e4240a7b875 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.5.2.1.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 3e55f8cd-3aff-4f45-a213-bb59f869ab84 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.1.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 175640b2-a33d-4a0a-af98-8aa895344eca -->

The subtrees for archived Invocations and Instances of the Prime Transformation Primitive are stored here.

###### A.6.1.1.5.2.1.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 8a61c3ea-fe8d-41a5-ade2-e338754f0666 -->

The subtrees for failed Invocations of the Prime Transformation Primitive are stored here.

###### A.6.1.1.5.2.1.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 6b3b64ef-26b1-45ee-8596-7c78c243f1ae -->

The subtrees for Instances of the Prime Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.1.2.2 - Active Instances [Core]  <!-- UUID: e54ec47c-4526-4cc2-9722-43ed3cee7768 -->

The Instances of the Prime Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.1.2.3 - Completed Instances [Core]  <!-- UUID: 1a8ffef1-7997-452c-9f58-6b8d9af23c04 -->

The Instances of the Prime Transformation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.5.2.1.2.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 2fd59b03-9278-4371-a3f1-fe9514ab322b -->

The documents herein contain the Instance Configuration Document for the Single Prime Transformation Primitive Instance.

###### A.6.1.1.5.2.1.2.3.1.1 - Parameters [Core]  <!-- UUID: ff8bd343-f602-4a9c-a5b6-2048496d4ec8 -->

The documents herein define the parameters of the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.5.2.1.2.3.1.1.1 - Agent Type [Core]  <!-- UUID: 3275f4de-18d6-4fca-8023-d6f2e3fb4f01 -->

Obex is a Prime Agent.

###### A.6.1.1.5.2.1.2.3.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 65c00572-3f2f-41fa-892d-e568ef1cf7ba -->

The documents herein define the custom parameters of the Single Instance of the Prime Transformation Primitive, if any.

###### A.6.1.1.5.2.1.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 91999490-cd47-4523-aa5b-f71216472a3c -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.5.2.1.2.3.1.3 - Data Repository [Core]  <!-- UUID: e70d36bc-8e5e-44b4-ab3b-492308ab7196 -->

The documents herein contain data relevant to the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.5.2.1.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: c0cc5f1c-0cc5-44c8-bf92-d28b371e05b0 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.1.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: aa23e483-3205-4843-92c9-5906b244e662 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.1.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 9e54e190-a5f0-466e-945b-a9075fbc20b1 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.5.2.1.2.4 - In Progress Invocations [Core]  <!-- UUID: 685248fb-8b9c-44d0-8ba3-ada4ada84e06 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.5.2.1.3 - Executor Transformation Primitive [Core]  <!-- UUID: ad55a2b2-7b47-401f-967e-f89e601e567c -->

The documents herein contain all data and specifications for Obex's instance of the Executor Transformation Primitive. See [A.2.2.5.3 - Executor Transformation Primitive](2f249be5-8edb-41e4-b429-734e1ba2cbc7).

##### A.6.1.1.5.2.1.3.1 - Primitive Hub Document [Core]  <!-- UUID: 7b3f85c4-e618-4071-b07f-5c771a3bc873 -->

The documents herein organize all base information relevant to Obex's usage of the Executor Transformation Primitive.

###### A.6.1.1.5.2.1.3.1.1 - Global Activation Status [Core]  <!-- UUID: 7e92d813-a224-495a-b2c7-ad83304b977c -->

`Inactive`

###### A.6.1.1.5.2.1.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 5f9f5d64-6e5b-466e-a4c0-a194ec24161f -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.1.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 8f2c269a-20d6-4d3c-82e8-1a98123d663b -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.1.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 1a4b9edf-b153-4f7f-be3a-27a87ef58185 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.5.2.1.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 15635343-8607-45d0-a675-e5486ca08c7b -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.1.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 84461fee-fe8d-4008-8bb1-0e72f22e0921 -->

The subtrees for archived Invocations and Instances of the Executor Transformation Primitive are stored here.

###### A.6.1.1.5.2.1.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 5b36399c-c01b-445a-ad21-f4f057575621 -->

The subtrees for failed Invocations of the Executor Transformation Primitive are stored here.

###### A.6.1.1.5.2.1.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 87d42440-89ee-4d33-8f3e-8a9cf56b0fc6 -->

The subtrees for Instances of the Executor Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.1.3.2 - Active Instances [Core]  <!-- UUID: 697d6019-9769-49cb-8394-c74c9c2240f3 -->

The Instances of the Executor Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.1.3.3 - Completed Instances [Core]  <!-- UUID: 0dfb0a6f-af53-45d5-badb-0383c76f2515 -->

The Instances of the Executor Transformation Primitive with `Completed` Status are contained herein.

##### A.6.1.1.5.2.1.3.4 - In Progress Invocations [Core]  <!-- UUID: 7ee33331-fa25-4c43-b3e8-de3362118dea -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.5.2.1.4 - Agent Token Primitive [Core]  <!-- UUID: 29c1a185-926e-42e0-a15c-1aad1dbe9068 -->

The documents herein contain all data and specifications for Obex's Instance of the Agent Token Primitive. See [A.2.2.5.4 - Agent Token Primitive](2047c361-db28-4952-a70c-83d07b562064).

##### A.6.1.1.5.2.1.4.1 - Primitive Hub Document [Core]  <!-- UUID: ea5efaa6-992d-4e59-9ebb-4c027ee7aa87 -->

The documents herein organize all base information relevant to Obex's usage of the Agent Token Primitive.

###### A.6.1.1.5.2.1.4.1.1 - Global Activation Status [Core]  <!-- UUID: 0dbea81d-1a7b-4c83-8817-20ee5aa3e90b -->

`Active`

###### A.6.1.1.5.2.1.4.1.2 - Active Instances Directory [Core]  <!-- UUID: 6a9df4c5-fe51-4bfa-b661-69e313df475c -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.1.4.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: ccaebb1f-f68d-4f07-89a0-a18afea052d4 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.5.2.1.4.2.1 - Single Instance Configuration Document](81d78b70-e460-4588-8e37-d2cf7ec87d32).

###### A.6.1.1.5.2.1.4.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7e49543e-ee1f-4a60-9b80-e290e961931d -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.1.4.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 5d1fa3e0-cafc-4667-951e-0ea439d13a95 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.5.2.1.4.1.5 - Hub Data Repository [Core]  <!-- UUID: 70cf9e11-7eed-4eba-8ef1-47bd21974a5f -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.1.4.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 38877b86-ed6e-49fb-ae28-4c0b7f0df215 -->

The subtrees for archived Invocations and Instances of the Agent Token Primitive are stored here.

###### A.6.1.1.5.2.1.4.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: c87625a9-a7f2-4302-8104-739664173433 -->

The subtrees for failed Invocations of the Agent Token Primitive are stored here.

###### A.6.1.1.5.2.1.4.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 7b49d757-66c0-4a34-b715-729a64801fca -->

The subtrees for Instances of the Agent Token Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.1.4.2 - Active Instances [Core]  <!-- UUID: df170b7f-303a-4029-8f10-7548dab07f8a -->

The Instances of the Agent Token Primitive with `Active` Status are stored herein.

###### A.6.1.1.5.2.1.4.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 81d78b70-e460-4588-8e37-d2cf7ec87d32 -->

The documents herein contain the Instance Configuration Document for the Single Agent Token Primitive Instance.

###### A.6.1.1.5.2.1.4.2.1.1 - Parameters [Core]  <!-- UUID: dcca537a-8364-4306-8f54-0113652e187c -->

The documents herein define the parameters of the Single Instance of the Agent Token Primitive.

###### A.6.1.1.5.2.1.4.2.1.1.1 - Token Name [Core]  <!-- UUID: 86cff886-c2dd-447b-b300-7f3ac0334624 -->

The name of Obex's token is Obex.

###### A.6.1.1.5.2.1.4.2.1.1.2 - Token Symbol [Core]  <!-- UUID: 65767abc-766f-43e0-88c1-12b9a1855868 -->

The symbol of Obex's token is OBEX.

###### A.6.1.1.5.2.1.4.2.1.1.3 - Genesis Supply [Core]  <!-- UUID: 19ad3fe9-9161-4ddd-af93-d3fc854d51ed -->

The Genesis Supply of OBEX is 10 billion.

###### A.6.1.1.5.2.1.4.2.1.1.4 - Token Address [Core]  <!-- UUID: a954b3b9-4230-448e-b926-e7daaad542c5 -->

The address of OBEX will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.1.4.2.1.1.5 - Token Admin [Core]  <!-- UUID: 2646a808-056e-4907-88bb-b504afe61946 -->

The token Admin will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.1.4.2.1.1.6 - Token Emissions [Core]  <!-- UUID: e687b86c-f6b8-4f2e-aabf-b7922b2d3f6d -->

Token emissions beyond the Genesis Supply are permanently disabled; this cannot be reverted by Obex Governance. Sky Governance retains the ability to revert where Obex is in violation of Risk Capital requirements and emissions are required by the Risk Framework. See [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.6.1.1.5.2.1.4.2.1.1.7 - Custom Instance Parameters [Core]  <!-- UUID: c40b84ff-e133-434a-bef9-e12aba5ac87c -->

The documents herein define the custom parameters of the Single Instance of the Agent Token Primitive, if any.

###### A.6.1.1.5.2.1.4.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 1cd77356-66a5-449c-a573-71a44a628044 -->

The documents herein define the operational processes for minting and initial distribution of the tokens from the Genesis Supply.

- These processes will be defined in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.1.4.2.1.3 - Data Repository [Core]  <!-- UUID: 596d5aa9-8116-44a0-aca7-e53b5181e62e -->

The documents herein contain data relevant to the Single Instance of the Agent Token Primitive.

###### A.6.1.1.5.2.1.4.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 6fe2485a-225f-41e3-b791-0b98363df1e8 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.1.4.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 44b64f9f-aa20-4aeb-b2e3-6abda1cfa77d -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.1.4.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: c6ec5fe6-691b-4ac7-a863-2be65a28ea3f -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.5.2.1.4.3 - Completed Instances [Core]  <!-- UUID: c0ee9726-7ae8-4176-a3f3-01152a53f0d1 -->

The Instances of the Agent Token Primitive with `Completed` Status are contained herein.

##### A.6.1.1.5.2.1.4.4 - In Progress Invocations [Core]  <!-- UUID: ec1f15fa-3059-4fd3-9467-7a796d7050a5 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

### A.6.1.1.5.2.2 - Operational Primitives [Core]  <!-- UUID: 91762197-a7e2-4e0c-bce5-4490f23f9667 -->

The documents herein implement the Operational Primitives for Obex. See [A.2.2.6 - Operational Primitives](0192ec95-9207-480e-8c51-88d2a1da95ad).

#### A.6.1.1.5.2.2.1 - Executor Accord Primitive [Core]  <!-- UUID: e0baddbe-f261-4439-8fc0-e03b521c10ad -->

The documents herein contain all data and specifications for Obex's Instances of the Executor Accord Primitive. See [A.2.2.6.1 - Executor Accord Primitive](88017877-3ec1-4c43-a035-6bebdf11d9bb).

##### A.6.1.1.5.2.2.1.1 - Primitive Hub Document [Core]  <!-- UUID: 4f398e78-1f12-447d-bb28-71cfc4e9ce4c -->

The documents herein organize all base information relevant to Obex's usage of the Executor Accord Primitive.

###### A.6.1.1.5.2.2.1.1.1 - Global Activation Status [Core]  <!-- UUID: 4bb8c2f6-b020-4f18-aa1e-9ac5962c6fac -->

`Active`

###### A.6.1.1.5.2.2.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 5db0baf4-141b-4eb9-8d5b-bd5386e6786c -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.2.1.1.2.1 - Ozone Instance Configuration Document Location [Core]  <!-- UUID: e08db2e2-b978-473f-be58-cf4a304bf15c -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.5.2.2.1.2.1 - Ozone Instance Configuration Document](7634c378-486d-4d5b-823a-aee5c1c8b3a6).

###### A.6.1.1.5.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 0a0ddb4d-d708-4b2d-b9f2-1c7524fa2038 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 1310aa75-5080-4291-9de9-e4ce0cd7adcc -->

This document contains a Directory of all prospective Instances of the Executor Accord Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.2.1.1.2 - Active Instances Directory](5db0baf4-141b-4eb9-8d5b-bd5386e6786c), whereas failed Invocations are Archived in [A.6.1.1.5.2.2.1.1.5 - Hub Data Repository](6c78d193-aa70-45a1-b807-77dcba6b6543).

###### A.6.1.1.5.2.2.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 6c78d193-aa70-45a1-b807-77dcba6b6543 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.2.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 8eb2aa7f-71ca-4c91-a0f9-5d433dcf22f3 -->

The subtrees for archived Invocations and Instances of the Executor Accord Primitive are stored here.

###### A.6.1.1.5.2.2.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 8e1fddae-22a6-4dc9-9e1b-78861747d2ca -->

The subtrees for failed Invocations of the Executor Accord Primitive are stored here.

###### A.6.1.1.5.2.2.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 4a6fc07c-c28c-499d-93c4-bd469e8b2012 -->

The subtrees for Instances of the Executor Accord Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.2.1.2 - Active Instances [Core]  <!-- UUID: 2fd90ea2-b604-4a06-8c73-888c08365dba -->

The Instances of the Executor Accord Primitive with `Active` Status are stored herein.

###### A.6.1.1.5.2.2.1.2.1 - Ozone Instance Configuration Document [Core]  <!-- UUID: 7634c378-486d-4d5b-823a-aee5c1c8b3a6 -->

The documents herein contain the Instance Configuration Document for the Ozone Executor Accord Primitive Instance.

###### A.6.1.1.5.2.2.1.2.1.1 - Parameters [Core]  <!-- UUID: 182988e8-96c8-4c3c-ab19-6b9b88b9532b -->

The documents herein define the parameters of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.5.2.2.1.2.1.1.1 - Operational Executor Agent [Core]  <!-- UUID: e3e97ee0-1ef7-48dd-acf0-3e1e6a6de47e -->

The Operational Facilitator and Operational GovOps for Ozone are specified in [A.6.1.2.2 - Operational Executor Agent Ozone](565660dd-7850-4c3a-8dba-554542bf103a).

###### A.6.1.1.5.2.2.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 4b5e6287-583b-40c0-8ec4-87675a15f802 -->

The documents herein define the custom parameters of the Ozone Instance of the Executor Accord Primitive, if any.

###### A.6.1.1.5.2.2.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 520a274c-6b18-4fb7-953a-8f562c5ca111 -->

The documents herein define the process for the ongoing management of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.5.2.2.1.2.1.3 - Data Repository [Core]  <!-- UUID: 2a655bfa-fbcb-4888-b4df-0d0ec8398a14 -->

The documents herein contain data relevant to the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.5.2.2.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: b7eb3de8-9b56-4e2a-b0c0-5d3f8dddccb7 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.2.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 0ab58c7d-7bb4-4d33-bd7a-2eca8e80b62a -->

The materials associated with Operational GovOps review during the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.2.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 248099c5-af01-490c-b248-4441accf889f -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.5.2.2.1.3 - Completed Instances [Core]  <!-- UUID: 33eff493-0a21-4bb0-899e-f3fab9ef6f27 -->

The Instances of the Executor Accord Primitive with `Completed` Status are stored herein.

##### A.6.1.1.5.2.2.1.4 - In Progress Invocations [Core]  <!-- UUID: dfca9a54-ab85-476a-ab49-345ec43a1294 -->

The in progress Invocations of the Executor Accord Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.2.1.2 - Active Instances](2fd90ea2-b604-4a06-8c73-888c08365dba).

#### A.6.1.1.5.2.2.2 - Root Edit Primitive [Core]  <!-- UUID: b69559bf-1acb-4f9c-8638-19fb8ef20fc2 -->

The documents herein contain all data and specifications for Obex's Instance of the Root Edit Primitive. See [A.2.2.6.2 - Root Edit Primitive](78488c6b-d77f-4344-b954-476e415a2c7d).

##### A.6.1.1.5.2.2.2.1 - Primitive Hub Document [Core]  <!-- UUID: f6e6bc46-aa12-4a74-8433-85ffcfad4917 -->

The documents herein organize all base information relevant to Obex's usage of the Root Edit Primitive.

###### A.6.1.1.5.2.2.2.1.1 - Global Activation Status [Core]  <!-- UUID: 363d6ab5-1065-4cb5-8326-506a7dc62db6 -->

`Active`

###### A.6.1.1.5.2.2.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 0a66c55d-66c6-4fae-819b-c1bce486a03e -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.2.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 48d674cd-633b-40b7-ab4f-9ff4028ea1e6 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.5.2.2.2.2.1 - Single Instance Configuration Document](f5cb7958-d3a3-4179-9541-8a603745a5f1).

###### A.6.1.1.5.2.2.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 67ec15f0-3610-42e3-bbd4-1d35c5944aa6 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.2.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 155d502c-8c81-47dc-aaa5-0944a565cd8c -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.5.2.2.2.1.5 - Hub Data Repository [Core]  <!-- UUID: f5bcf120-3af4-4b17-b63c-1adcf745ce75 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.2.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 988302bd-3993-4833-9611-456285591f89 -->

The subtrees for archived Invocations and Instances of the Root Edit Primitive are stored here.

###### A.6.1.1.5.2.2.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 64ae8942-a1ac-4904-ba13-43ee7334551e -->

The subtrees for failed Invocations of the Root Edit Primitive are stored here.

###### A.6.1.1.5.2.2.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 75008710-7942-45ef-87ee-f342f0a571f4 -->

The subtrees for Instances of the Root Edit Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.2.2.2 - Active Instances [Core]  <!-- UUID: 2bc00f12-93cd-4431-8d6c-6a1170ca474c -->

The Instances of the Root Edit Primitive with `Active` Status are stored herein.

###### A.6.1.1.5.2.2.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: f5cb7958-d3a3-4179-9541-8a603745a5f1 -->

The documents herein contain the Instance Configuration Document for the Single Root Edit Primitive Instance.

###### A.6.1.1.5.2.2.2.2.1.1 - Parameters [Core]  <!-- UUID: 5034d53f-d21f-471b-a796-e62893aeab03 -->

The parameters of the Root Edit Primitive are fully specified by the Operational Process Definition in [A.6.1.1.5.2.2.2.2.1.2 - Operational Process Definition](ef3c8fc4-d958-492b-bee6-d96b5f972720).

###### A.6.1.1.5.2.2.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: ef3c8fc4-d958-492b-bee6-d96b5f972720 -->

The documents herein define the process for using the Root Edit Primitive to update the Obex Agent Artifact. Information on Obex governance that is unrelated to the use of the Root Edit Primitive is located at [A.6.1.1.5.3.1 - Governance Information Unrelated To Root Edit Primitive](bdad4ea3-7cf2-40fb-a8ab-4bb8b320e4c9).

###### A.6.1.1.5.2.2.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: da6d3815-d49e-47a4-8e62-81b66dbab51f -->

The documents herein define the process for using the Root Edit Primitive to update the Obex Agent Artifact in routine or normal conditions (i.e., non-emergency situations).

###### A.6.1.1.5.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission [Core]  <!-- UUID: fcb1b51e-8bb3-4a55-8cc0-9bec637086c8 -->

The Root Edit process begins with a OBEX token holder submitting a proposal through the Powerhouse system containing a draft Artifact Edit Proposal. A OBEX token holder must hold at least 1% of the circulating token supply to submit a proposal. The proposal must also be posted on the Sky Forum under the "Obex Prime" category.

###### A.6.1.1.5.2.2.2.2.1.2.1.1.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: e0020160-9ee8-4f35-90f1-ba375d625689 -->

Until the Powerhouse system supports submitting Artifact Edit Proposals, OBEX token holders may submit Artifact Edit Proposals by posting them to the Sky Forum under the "Obex Prime" category. The title of the post must include the text "Obex Artifact Edit Proposal". The post must include cryptographic proof that the author controls an account holding the required percentage of the total OBEX token supply specified in [A.6.1.1.5.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](fcb1b51e-8bb3-4a55-8cc0-9bec637086c8).

###### A.6.1.1.5.2.2.2.2.1.2.1.2 - Root Edit Expert Advisor Review [Core]  <!-- UUID: 432c532c-3e3a-41e9-b9dc-88c20d944541 -->

A future iteration of the Obex Artifact will specify guidelines for obtaining specialized review of proposals requiring advanced technical or financial analysis.

###### A.6.1.1.5.2.2.2.2.1.2.1.3 - Root Edit Proposal Review By Operational Facilitator [Core]  <!-- UUID: d21854da-165b-455d-893c-147db514d31c -->

Within seven (7) days of the proposal being submitted, the Operational Facilitator must review the Root Edit Proposal for alignment.

If the proposal is aligned, the Operational Facilitator must respond to the Forum post to announce their finding. In this Forum post, the Operational Facilitator must also confirm that the proposal is feasible for Operational GovOps to operationalize.

If the proposal is misaligned, the Operational Facilitator must respond to the Forum post to announce their finding and provide the reasoning for it.

###### A.6.1.1.5.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote [Core]  <!-- UUID: b60fe2f0-2aa6-4f36-9d87-e81c2294abc9 -->

Where their review of the proposal results in a finding of alignment with the Sky Core Atlas and Obex Artifact, the Operational Facilitator next triggers a Snapshot poll to allow token holders to vote on the proposal. The poll is open for three (3) days. A poll must have at least 10% of the circulating token supply participating and must have 50% of votes in favor to be approved.

###### A.6.1.1.5.2.2.2.2.1.2.1.5 - Root Edit Artifact Update [Core]  <!-- UUID: e0a6abf0-6191-4605-afa3-cc0de7b72a05 -->

At the conclusion of the poll, if the proposal is approved, the Operational Facilitator submits the edit to Powerhouse to formally update the Agent Artifact. Regardless of the outcome, the Operational Facilitator updates the Powerhouse System to include the result of the vote, including any pertinent documents.

###### A.6.1.1.5.2.2.2.2.1.2.1.5.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: a418eef2-bbfc-43eb-8d79-62c7bb940c3d -->

Until the Powerhouse system supports updating Agent Artifacts, the Operational Facilitator works with the Core Facilitator to update the Atlas GitHub repository located at [https://github.com/sky-ecosystem/next-gen-atlas/pulls](https://github.com/sky-ecosystem/next-gen-atlas/pulls) to reflect proposals approved by Prime Governance.

###### A.6.1.1.5.2.2.2.2.1.2.1.6 - Artifact Edit Restrictions [Core]  <!-- UUID: c14e9e4d-2819-46cb-b267-a9b13600192a -->

The Obex Artifact cannot be edited in any way that violates the Sky Core Atlas or its specifications of the Sky Primitives, or in any way that is otherwise misaligned. The Operational Facilitator must enforce this rule through their review of Artifact Edit Proposals.

###### A.6.1.1.5.2.2.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 2dcc5cd2-5936-4779-8ff6-072ad863756f -->

The documents herein define the process for using the Root Edit Primitive to update the Obex Agent Artifact in non-routine conditions.

###### A.6.1.1.5.2.2.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: d12b8cf2-2668-4466-ac2e-7404fce6c718 -->

The documents herein define the process for using the Root Edit Primitive to update the Obex Agent Artifact in emergency situations.

###### A.6.1.1.5.2.2.2.2.1.2.3.1 - Root Edit Voting Process in Emergency Situations [Core]  <!-- UUID: f8b1cf73-d16d-4ca0-aeea-3f95d25245a8 -->

In an Emergency Situation, as defined by the Sky Core Atlas in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225), the Operational Facilitator may allow a Root Edit to occur more quickly than the timeline specified above. Where feasible, the Operational Facilitator should announce the decision to deploy the emergency Root Edit protocol and provide their reasoning via a public Sky Forum post (under the "Obex Prime" category), unless doing so would endanger Obex or its users.

###### A.6.1.1.5.2.2.2.2.1.3 - Data Repository [Core]  <!-- UUID: 8f8ef2ba-1071-40df-98bc-384d1f6782b5 -->

The documents herein contain data relevant to the Single Instance of the Root Edit Primitive.

###### A.6.1.1.5.2.2.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: b2f9aa29-8e29-4123-8996-12dad34b51e5 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.2.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 91cbbea6-33e4-49a4-ab2a-1c01d2b3eed8 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.2.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: efce80bb-4637-4bdf-8ddb-ad412154a521 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.5.2.2.2.3 - Completed Instances [Core]  <!-- UUID: 4d6ec316-b444-4550-a591-006a6b8080cd -->

The Instances of the Root Edit Primitive with `Completed` Status are contained herein.

##### A.6.1.1.5.2.2.2.4 - In Progress Invocations [Core]  <!-- UUID: 77be1f27-3cd0-4e3f-a05d-8ce0880f37a7 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.5.2.2.3 - Light Agent Primitive [Core]  <!-- UUID: 32cf649f-13f7-41e2-bbe4-347a14532114 -->

The documents herein contain all data and specifications for Obex's Instances of the Light Agent Primitive. See [A.2.2.6.3 - Light Agent Primitive](44028423-2cd1-40cb-89ac-3f762b602b90).

##### A.6.1.1.5.2.2.3.1 - Primitive Hub Document [Core]  <!-- UUID: c4b311b3-3f2c-483f-b24a-845ef5c6a6df -->

The documents herein organize all base information relevant to Obex's usage of the Light Agent Primitive.

###### A.6.1.1.5.2.2.3.1.1 - Global Activation Status [Core]  <!-- UUID: afc008c0-e6d3-4973-b501-0f9f2db1cfa4 -->

`Inactive`

###### A.6.1.1.5.2.2.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 848c213e-5478-448c-9c7b-a8ea119823e5 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.2.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 88717821-a8d4-480e-91c6-ba996685746c -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.2.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: c38da3e3-0dbc-4deb-833f-0a124d55f0f7 -->

This document contains a Directory of all prospective Instances of the Light Agent Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.2.3.1.2 - Active Instances Directory](848c213e-5478-448c-9c7b-a8ea119823e5), whereas failed Invocations are Archived in [A.6.1.1.5.2.2.3.1.5 - Hub Data Repository](19e005fe-f719-407f-b788-5bc13f3ffb11).

###### A.6.1.1.5.2.2.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 19e005fe-f719-407f-b788-5bc13f3ffb11 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.2.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 8dfdbffe-91f9-44c5-8e28-45cbda1cbdfb -->

The subtrees for archived Invocations and Instances of the Light Agent Primitive are stored here.

###### A.6.1.1.5.2.2.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: a7910404-5064-4d72-946d-2b9cb2f7d944 -->

The subtrees for failed Invocations of the Light Agent Primitive are stored here.

###### A.6.1.1.5.2.2.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: d9955aca-f64d-41a3-9c5c-16ad98f98956 -->

The subtrees for Instances of the Light Agent Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.2.3.2 - Active Instances [Core]  <!-- UUID: d7b02050-890e-4b86-9bbf-2d4183a97f44 -->

The Instances of the Light Agent Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.2.3.3 - Completed Instances [Core]  <!-- UUID: 5ef59d24-d4c8-445c-8385-08801b24be3a -->

The Instances of the Light Agent Primitive with `Completed` Status are contained herein.

##### A.6.1.1.5.2.2.3.4 - In Progress Invocations [Core]  <!-- UUID: 041daa3a-41b4-47fd-8e2b-bb288fd8342b -->

The in progress Invocations of the Light Agent Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.2.3.2 - Active Instances](d7b02050-890e-4b86-9bbf-2d4183a97f44).

### A.6.1.1.5.2.3 - Ecosystem Upkeep Primitives [Core]  <!-- UUID: ea7388bc-3689-4b90-80d8-920eb7f25411 -->

The documents herein implement the Ecosystem Upkeep Primitives for Obex. See [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

#### A.6.1.1.5.2.3.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: 518b0729-7d39-4e94-96ae-4e1dce577b3a -->

The documents herein contain all data and specifications for Obex's Instance of the Ecosystem Upkeep Fee Primitive. See [A.2.2.7.1 - Ecosystem Upkeep Fee Primitive](a21616f4-1611-4e0b-87b2-efbdff9f6f28).

##### A.6.1.1.5.2.3.1.1 - Primitive Hub Document [Core]  <!-- UUID: 367db765-3d90-449f-88d7-356eb2e5df6b -->

The documents herein organize all base information relevant to Obex's usage of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.5.2.3.1.1.1 - Global Activation Status [Core]  <!-- UUID: 6a8a9da7-4c67-4553-84fd-5ad743f50847 -->

`Active`

###### A.6.1.1.5.2.3.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 590456d2-baea-411e-bd00-dccbd12387c0 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.3.1.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 347ce0a4-ad9c-4a54-975b-939c932edbba -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.5.2.3.1.2.1 - Single Instance Configuration Document](7ef7b4b1-d8c1-4f9d-bf00-c1cf292b0c02).

###### A.6.1.1.5.2.3.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 1d7ff736-dd46-4b6f-b5c1-c52e50f34846 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.3.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 14a2006a-764a-4526-8d9f-ff3dfc4591fe -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.5.2.3.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 2087141c-ab9c-404e-bba8-1a1843350bb5 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.3.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 8898ed9a-e7fc-403e-a061-8399a6b132b8 -->

The subtrees for archived Invocations and Instances of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.5.2.3.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 2ef60c48-9590-4e1f-b00a-48cb9edbcd20 -->

The subtrees for failed Invocations of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.5.2.3.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: a300b6cf-1826-4b4a-b49a-b9fe4f75ccda -->

The subtrees for Instances of the Ecosystem Upkeep Fee Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.3.1.2 - Active Instances [Core]  <!-- UUID: a27eeee1-ce9a-4b26-9bef-57199b921eda -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Active` Status are stored herein.

###### A.6.1.1.5.2.3.1.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 7ef7b4b1-d8c1-4f9d-bf00-c1cf292b0c02 -->

The documents herein contain the Instance Configuration Document for the Single Ecosystem Upkeep Fee Primitive Instance.

###### A.6.1.1.5.2.3.1.2.1.1 - Parameters [Core]  <!-- UUID: c3c06c49-ce92-4eac-b7e9-00783b4c6902 -->

The documents herein define the parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.5.2.3.1.2.1.1.1 - Term [Core]  <!-- UUID: 49fe9982-412f-4da4-b81d-92786d3a7709 -->

Obex will pay 0.50% of its market capitalization per year in USDS.

###### A.6.1.1.5.2.3.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: d58f7727-d553-43b9-b513-d4d490abc16f -->

The documents herein define the custom parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive, if any.

###### A.6.1.1.5.2.3.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: dfafe9f2-4bc7-450a-b227-008d37b88249 -->

The documents herein define the process for the ongoing management of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.5.2.3.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 0fa4e4f4-a123-42d4-9353-997480ee8d14 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.5.2.3.1.2.1.2.1.1 - Process Definition For Upkeep Fee Payment [Core]  <!-- UUID: ec192467-881e-4af6-9378-1fa4e36a6c18 -->

The process to pay 0.50% of Obex's market capitalization per year in USDS will be specified in future iterations of the Obex Artifact.

###### A.6.1.1.5.2.3.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: fc2e23dd-7ca5-4487-b7ba-283156adab6f -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.5.2.3.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: e68b9b15-fd96-4e9b-93d6-8feab64f8d7b -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.5.2.3.1.2.1.3 - Data Repository [Core]  <!-- UUID: 4ba98afe-bd9c-49bb-938e-1475ceddd30b -->

The documents herein contain data relevant to the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.5.2.3.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 1f1e7bb2-dfa7-4189-84bd-9a6759aec3e7 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.3.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 8f8f951d-8768-457d-9c56-3a81b92c395a -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.3.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 2e866803-811d-4220-b336-ebe239402921 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.5.2.3.1.3 - Completed Instances [Core]  <!-- UUID: beeba9d9-39bb-4f36-9447-9456966975eb -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Completed` Status are stored herein.

##### A.6.1.1.5.2.3.1.4 - In Progress Invocations [Core]  <!-- UUID: 3c7049bc-3c9f-4088-94bc-0fc242dca76a -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.5.2.3.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: 1cec73ac-6b70-48ff-a7ff-1d0f689d602f -->

The documents herein contain all data and specifications for Obex's instance of the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

##### A.6.1.1.5.2.3.2.1 - Primitive Hub Document [Core]  <!-- UUID: 36f57327-abff-4ac1-890b-c5097c449b02 -->

The documents herein organize all base information relevant to Obex's usage of the Upkeep Rebate Primitive.

###### A.6.1.1.5.2.3.2.1.1 - Global Activation Status [Core]  <!-- UUID: 28f93080-7f1f-45f1-a9c6-a78cea11cbbd -->

`Active`

###### A.6.1.1.5.2.3.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 47f2fe76-ba5f-437e-8110-799c1e3fe7f5 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.3.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 4800d116-8fa3-40b4-ac3b-dce8629d2984 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.5.2.3.2.2.1 - Single Instance Configuration Document](8a327b83-b508-480b-8e97-038c6e35c64f).

###### A.6.1.1.5.2.3.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 41b96ba1-f506-498a-803f-d4067053b6ed -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.3.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 8850b00e-dd0a-44d7-b64a-7e4ef5cf7d37 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.5.2.3.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 0daa3c8b-dbce-4c8c-bfd6-30a3d5ae7486 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.3.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: a8cd1289-22f9-4e01-878b-01a7b0e90a80 -->

The subtrees for archived Invocations and Instances of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.5.2.3.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 49d6d2d2-1052-44d5-a9a9-0935d26f99ff -->

The subtrees for failed Invocations of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.5.2.3.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 28085731-4ac7-4016-807c-652fe1447bb8 -->

The subtrees for Instances of the Upkeep Rebate Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.3.2.2 - Active Instances [Core]  <!-- UUID: c4e5deff-2cf9-492c-af8c-cfbd33327686 -->

The Instances of the Upkeep Rebate Primitive with `Active` Status are stored herein.

###### A.6.1.1.5.2.3.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 8a327b83-b508-480b-8e97-038c6e35c64f -->

The documents herein contain the Instance Configuration Document for the Single Upkeep Rebate Primitive Instance.

###### A.6.1.1.5.2.3.2.2.1.1 - Parameters [Core]  <!-- UUID: 439a27ef-945c-43dc-ab3b-836e5ab6372b -->

Every Prime Agent is entitled to the Upkeep Rebate Primitive for tokens of other Prime Agents that they hold. Because this right automatically applies, there are no parameters.

###### A.6.1.1.5.2.3.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 1d3eb5ff-4a71-4eff-a1f0-935f434644c1 -->

The documents herein define the process for the ongoing management of the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.5.2.3.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 144cfca6-e760-4f34-8ba3-effb1a1b9681 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.5.2.3.2.2.1.2.1.1 - Obex Holds Tokens Of Other Agents In Its SubProxy Account [Core]  <!-- UUID: 93599af2-bf73-4598-8b78-dfb74549f90d -->

Obex keeps all tokens of other Agents it holds in its SubProxy account.

###### A.6.1.1.5.2.3.2.2.1.2.1.2 - Obex Deducts Rebate From Ecosystem Upkeep Fees [Core]  <!-- UUID: eb954d3d-94d9-46d8-a118-a74e0d9da8c0 -->

When paying Ecosystem Upkeep fees, Obex deducts the rebate from the fees it pays.

###### A.6.1.1.5.2.3.2.2.1.2.1.3 - Operational GovOps Reviews Rebate [Core]  <!-- UUID: a8afed5e-3721-40a3-847c-3589a5dfce95 -->

Operational GovOps reviews Obex's calculation of the rebate before executing a return of surplus to token holders. In the event of any issues, Operational GovOps cannot execute the distribution. If Operational GovOps does not execute the distribution, Operational GovOps must post an explanation on the Sky Forum under the "Obex Prime" category and work with Obex to resolve the disagreement. If Operational GovOps and Obex cannot resolve the disagreement, it must be escalated to Core GovOps.

###### A.6.1.1.5.2.3.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 025b8abf-69a3-4749-95f3-60a7268983ff -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.5.2.3.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: e68e712a-cf58-45c0-8065-f81a5f259b18 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.5.2.3.2.2.1.3 - Data Repository [Core]  <!-- UUID: dd6c0d05-79f9-4663-85bb-916d12a29ce1 -->

The documents herein contain data relevant to the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.5.2.3.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: df002eaa-d6d5-4b27-9ccb-26193cc65ec5 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.3.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 5bf870c7-57bc-40f8-82d4-f6094b484a5b -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.5.2.3.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: d94ae414-18e8-432b-9f17-f58e8cc0cce3 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.5.2.3.2.3 - Completed Instances [Core]  <!-- UUID: 0723c247-7b2d-48aa-a1f1-1166aad05319 -->

The Instances of the Upkeep Rebate Primitive with `Completed` Status are contained herein.

##### A.6.1.1.5.2.3.2.4 - In Progress Invocations [Core]  <!-- UUID: 4e8268eb-b8f4-4d45-bf11-a6c03f262275 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

### A.6.1.1.5.2.4 - SkyLink Primitives [Core]  <!-- UUID: e66cbbd1-df57-418d-9699-73d050388fd6 -->

The documents herein implement the SkyLink Primitives for Obex. See [A.2.2.8 - SkyLink Primitives](7b5d8965-a64c-4c44-b742-607f51f69d8f).

#### A.6.1.1.5.2.4.1 - Token SkyLink Primitive [Core]  <!-- UUID: 5642de19-bfb3-4d54-9bc9-19b11b60a3c2 -->

The documents herein contain all data and specifications for Obex's Instances of the Token SkyLink Primitive. See [A.2.2.8.1 - Token SkyLink Primitive](4504d2d4-ee45-4a07-8c5b-9baf20b12e76).

##### A.6.1.1.5.2.4.1.1 - Primitive Hub Document [Core]  <!-- UUID: 3ce6f8aa-7a27-4701-83cb-d1fc4c41bb28 -->

The documents herein organize all base information relevant to Obex's usage of the Token SkyLink Primitive.

###### A.6.1.1.5.2.4.1.1.1 - Global Activation Status [Core]  <!-- UUID: 9d778551-1fd4-4206-a0e0-cb555f6d1e34 -->

`Inactive`

###### A.6.1.1.5.2.4.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 5c2fbcb7-e90b-44a5-854b-1616d9ad45a9 -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.4.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: a4ca44ca-4663-4d7d-8640-f173dfad1054 -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.4.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 3fd9d534-7c71-411b-84ed-afbe997589d0 -->

This document contains a Directory of all prospective Instances of the Token SkyLink Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.4.1.1.2 - Active Instances Directory](5c2fbcb7-e90b-44a5-854b-1616d9ad45a9), whereas failed Invocations are Archived in [A.6.1.1.5.2.4.1.1.5 - Hub Data Repository](930899b8-232d-4015-a594-317b682ca460).

###### A.6.1.1.5.2.4.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 930899b8-232d-4015-a594-317b682ca460 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.4.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: f11e195b-b8ad-43fd-93a1-001b297d0dcf -->

The subtrees for archived Invocations and Instances of the Token SkyLink Primitive are stored here.

###### A.6.1.1.5.2.4.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 13a369a4-5eb1-4301-98a1-eff12149501a -->

The subtrees for failed Invocations of the Token SkyLink Primitive are stored here.

###### A.6.1.1.5.2.4.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: aea6d389-e1d1-4cd1-bd96-24a29c1b3ecc -->

The subtrees for Instances of the Token SkyLink Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.4.1.2 - Active Instances [Core]  <!-- UUID: e8a2afff-b4b0-4b47-8b7a-32119eca9091 -->

The Instances of the Token SkyLink Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.4.1.3 - Completed Instances [Core]  <!-- UUID: b08f8e0b-5cc8-4b0a-b148-4ef44fa7ae03 -->

The Instances of the Token SkyLink Primitive with `Completed` Status are stored herein.

##### A.6.1.1.5.2.4.1.4 - In Progress Invocations [Core]  <!-- UUID: 01dcfdbb-70a4-4986-bf38-28db96dba4c4 -->

The in progress Invocations of the Token SkyLink Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.4.1.2 - Active Instances](e8a2afff-b4b0-4b47-8b7a-32119eca9091).

### A.6.1.1.5.2.5 - Demand Side Stablecoin Primitives [Core]  <!-- UUID: 66ca6538-89c2-442e-87c2-9fe2d586b516 -->

The documents herein implement the Demand Side Stablecoin Primitives for Obex. See [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d).

#### A.6.1.1.5.2.5.1 - Distribution Reward Primitive [Core]  <!-- UUID: f055e990-51e6-44c2-8d14-4e8694e62c1d -->

The documents herein contain all data and specifications for Obex's instances of the Distribution Reward Primitive. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

##### A.6.1.1.5.2.5.1.1 - Primitive Hub Document [Core]  <!-- UUID: f11e8f01-a17f-44e7-aac1-56dbd5e9272e -->

The documents herein organize all base information relevant to Obex's usage of the Distribution Reward Primitive.

###### A.6.1.1.5.2.5.1.1.1 - Global Activation Status [Core]  <!-- UUID: 94bbd7ec-e724-41e7-b74a-0e567768f219 -->

`Active`

###### A.6.1.1.5.2.5.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 6d07d8e0-e37e-47f0-8534-e0c67effd267 -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.5.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: f3d16b8f-4ac2-41b8-8744-13beb396588e -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.5.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: e1234baf-b923-4837-a279-96a76208f78d -->

This document contains a Directory of all prospective Instances of the Distribution Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.5.1.1.2 - Active Instances Directory](6d07d8e0-e37e-47f0-8534-e0c67effd267), whereas failed Invocations are Archived in [A.6.1.1.5.2.5.1.1.5 - Hub Data Repository](27d2b846-1278-4cf6-9a2f-09114d659813).

###### A.6.1.1.5.2.5.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 27d2b846-1278-4cf6-9a2f-09114d659813 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.5.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: d345b6e5-cf01-4c2c-a177-6d4f5549dcff -->

The subtrees for archived Invocations and Instances of the Distribution Reward Primitive are stored here.

###### A.6.1.1.5.2.5.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 1cb40bb8-ab91-4fb8-82ba-84e71bd84504 -->

The subtrees for failed Invocations of the Distribution Reward Primitive are stored here.

###### A.6.1.1.5.2.5.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: ce59ab47-8c7a-4893-a3f2-c9eeafac5168 -->

The subtrees for Instances of the Distribution Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.5.1.2 - Active Instances [Core]  <!-- UUID: bbe5be33-f895-48a4-a8de-7d65d83d4321 -->

The Instances of the Distribution Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.5.1.3 - Completed Instances [Core]  <!-- UUID: 51861e24-08e4-4828-a5ea-0f0ac08f67db -->

The Instances of the Distribution Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.5.2.5.1.4 - In Progress Invocations [Core]  <!-- UUID: 12cf9640-3b5b-4255-b7d9-e84baa973d9f -->

The in progress Invocations of the Distribution Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.5.1.2 - Active Instances](bbe5be33-f895-48a4-a8de-7d65d83d4321).

#### A.6.1.1.5.2.5.2 - Integration Boost Primitive [Core]  <!-- UUID: edc5cd33-99a9-4687-b3fe-8c3e07da92e8 -->

The documents herein contain all data and specifications for Obex's Instances of the Integration Boost Primitive. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

##### A.6.1.1.5.2.5.2.1 - Primitive Hub Document [Core]  <!-- UUID: f9d5c302-4695-436f-9a06-595c06da2fc9 -->

The documents herein organize all base information relevant to Obex's usage of the Integration Boost Primitive.

###### A.6.1.1.5.2.5.2.1.1 - Global Activation Status [Core]  <!-- UUID: f6c8017d-81cc-4ad5-ac3c-c68a354f2a61 -->

`Active`

###### A.6.1.1.5.2.5.2.1.2 - Active Instances Directory [Core]  <!-- UUID: bf82c8f9-c7d4-42ac-b590-f28982863ef5 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.5.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: c206ac89-c13e-4fae-886e-3014d0640b05 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.5.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: daad121e-7835-4c61-90fb-eb15f987329e -->

This document contains a Directory of all prospective Instances of the Integration Boost Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.5.2.1.2 - Active Instances Directory](bf82c8f9-c7d4-42ac-b590-f28982863ef5), whereas failed Invocations are Archived in [A.6.1.1.5.2.5.2.1.5 - Hub Data Repository](7b523fb3-f463-4f10-90d6-6dd1211dbc24).

###### A.6.1.1.5.2.5.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 7b523fb3-f463-4f10-90d6-6dd1211dbc24 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.5.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 3aa560cf-c7bd-47f8-b156-e3422c5dfc9b -->

The subtrees for archived Invocations and Instances of the Integration Boost Primitive are stored here.

###### A.6.1.1.5.2.5.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 64cbff91-cacc-492e-97de-d412bb860190 -->

The subtrees for failed Invocations of the Integration Boost Primitive are stored here.

###### A.6.1.1.5.2.5.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: d229d7d4-efdf-413c-9d9d-d4af3b43164b -->

The subtrees for Instances of the Integration Boost Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.5.2.2 - Active Instances [Core]  <!-- UUID: 0607bde3-cffa-4597-8ad9-fdb38272a843 -->

The Instances of the Integration Boost Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.5.2.3 - Completed Instances [Core]  <!-- UUID: 4dca2418-b9ea-4bdb-ae27-f34a09c7e761 -->

The Instances of the Integration Boost Primitive with `Completed` Status are contained herein.

##### A.6.1.1.5.2.5.2.4 - In Progress Invocations [Core]  <!-- UUID: 7fdf50ff-7d49-4ffc-9e2d-c1db6ce4a33a -->

The in progress Invocations of the Integration Boost Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.5.2.2 - Active Instances](0607bde3-cffa-4597-8ad9-fdb38272a843).

#### A.6.1.1.5.2.5.3 - Pioneer Chain Primitive [Core]  <!-- UUID: 2f0a0b71-759e-4f14-b63d-0286450855fe -->

The documents herein contain all data and specifications for Obex's Instances of the Pioneer Chain Primitive. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).

##### A.6.1.1.5.2.5.3.1 - Primitive Hub Document [Core]  <!-- UUID: 7e7dc6f6-bfe1-460e-9fb1-35a906f75259 -->

The documents herein organize all base information relevant to Obex's usage of the Pioneer Chain Primitive.

###### A.6.1.1.5.2.5.3.1.1 - Global Activation Status [Core]  <!-- UUID: c13df592-a35a-4d72-b33e-65c3ee9ba799 -->

`Inactive`

###### A.6.1.1.5.2.5.3.1.2 - Active Instances Directory [Core]  <!-- UUID: b0507c60-c43a-4ba2-b2d1-e0dbc4694720 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.5.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 18bcb4c7-6147-4231-a7fc-0d0c43cec037 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.5.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: e9e9cbf4-87cb-4e48-bf7c-f1a4caa934fa -->

This document contains a Directory of all prospective Instances of the Pioneer Chain Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.5.3.1.2 - Active Instances Directory](b0507c60-c43a-4ba2-b2d1-e0dbc4694720), whereas failed Invocations are Archived in [A.6.1.1.5.2.5.3.1.5 - Hub Data Repository](be430718-d9f5-4104-bdd0-26e333bd0a13).

###### A.6.1.1.5.2.5.3.1.5 - Hub Data Repository [Core]  <!-- UUID: be430718-d9f5-4104-bdd0-26e333bd0a13 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.5.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: cd28b1ad-9837-4db4-bcb5-7b35ee89d7a0 -->

The subtrees for archived Invocations and Instances of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.5.2.5.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: fd0b30aa-9a67-428f-8414-ed99818c58b0 -->

The subtrees for failed Invocations of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.5.2.5.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 20face9e-9216-44e9-b195-7d5fcb4c8465 -->

The subtrees for Instances of the Pioneer Chain Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.5.3.2 - Active Instances [Core]  <!-- UUID: 4fd3fe8d-e5d8-49ce-95b5-15e14e165abf -->

The Instances of the Pioneer Chain Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.5.3.3 - Completed Instances [Core]  <!-- UUID: 504497a1-14b9-4119-b520-bdcf4bedc4f9 -->

The Instances of the Pioneer Chain Primitive with `Completed` Status are stored herein.

##### A.6.1.1.5.2.5.3.4 - In Progress Invocations [Core]  <!-- UUID: cafab30a-9a0e-46ba-8eb9-889d85a57bb0 -->

The in progress Invocations of the Pioneer Chain Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.5.3.2 - Active Instances](4fd3fe8d-e5d8-49ce-95b5-15e14e165abf).

### A.6.1.1.5.2.6 - Supply Side Stablecoin Primitives [Core]  <!-- UUID: c63a813f-b434-4c81-8826-df78171f61f0 -->

The documents herein implement the Supply Side Stablecoin Primitives for Obex. See [A.2.2.10 - Supply Side Stablecoin Primitives](d1142876-33c2-4e21-9339-d8711525d46f).

#### A.6.1.1.5.2.6.1 - Allocation System Primitive [Core]  <!-- UUID: fe98c7e7-b7f8-4f2c-800a-bca5192576ac -->

The documents herein contain all data and specifications for Obex's Allocation System Primitive Instances.

##### A.6.1.1.5.2.6.1.1 - Primitive Hub Document [Core]  <!-- UUID: cbf426ee-7754-49c5-9040-b29a5126da39 -->

The documents herein organize all base information relevant to Obex's usage of the Obex Liquidity Layer.

###### A.6.1.1.5.2.6.1.1.1 - Global Activation Status [Core]  <!-- UUID: 02a794ce-0d32-4044-80c2-1ba5bf0b1ca0 -->

`Active`

###### A.6.1.1.5.2.6.1.1.2 - Active Instances Directory [Core]  <!-- UUID: b8d74925-677a-48e8-be42-b9e2614c9e0f -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.6.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: 7b8f5dc5-643d-4eb8-be6f-1663cc0856ac -->

The documents herein contain a Directory of all Instances on Ethereum Mainnet of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.6.1.1.2.1.1 - Maple [Core]  <!-- UUID: 59ef3080-82eb-4c0f-96cf-5d973128e4ef -->

The Ethereum Mainnet Instances Directory of the Maple Protocol with `Active` Status are stored herein.

###### A.6.1.1.5.2.6.1.1.2.1.1.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document Location [Core]  <!-- UUID: 7188ea33-de7a-4d97-a52e-4a6acbcb608c -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.5.2.6.1.3.1.1.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document](7488a14c-2464-4649-b476-48ee93bb438f).

###### A.6.1.1.5.2.6.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: f98d5f67-2cf0-4691-b13b-23e11caad05b -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.6.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 492c60d5-d5eb-4fab-b8eb-a4858c7b6033 -->

This document contains a Directory of all prospective Instances of the Allocation System Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.6.1.1.2 - Active Instances Directory](b8d74925-677a-48e8-be42-b9e2614c9e0f), whereas failed Invocations are Archived in [A.6.1.1.5.2.6.1.1.5 - Hub Data Repository](1a4ddf66-20ba-42e8-b7a9-6a71106f891a).

###### A.6.1.1.5.2.6.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 1a4ddf66-20ba-42e8-b7a9-6a71106f891a -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.6.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 1b2334f1-f766-4b58-94b2-8cfbceb90ac6 -->

The subtrees for archived Invocations and Instances of the Allocation System Primitive are stored here.

###### A.6.1.1.5.2.6.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 224c6cc9-f120-4a4c-b708-3df8b9c50faf -->

The subtrees for failed Invocations of the Allocation System Primitive are stored here.

###### A.6.1.1.5.2.6.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: a685b24a-59a8-49e4-94d5-20db465f316e -->

The subtrees for Instances of the Allocation System Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.6.1.2 - Multi-Instance Coordinator Document [Core]  <!-- UUID: aa59c9ff-7347-407f-9d55-59fa499a58c9 -->

The documents herein provide general specifications of the Obex Liquidity Layer and define Obex's overarching strategy and operational framework for managing across all Instances.

###### A.6.1.1.5.2.6.1.2.1 - General Specifications [Core]  <!-- UUID: 1fa01b00-08d6-4344-ab6c-7a0cbea5e06c -->

The documents herein contain general specifications for the Obex Liquidity Layer.

###### A.6.1.1.5.2.6.1.2.1.1 - Obex Liquidity Layer Architecture [Core]  <!-- UUID: c29faa6d-d657-47a0-9379-21b8cd831d02 -->

The documents herein describe the high-level design of the Obex Liquidity Layer, including its key smart contracts and their functionality.

###### A.6.1.1.5.2.6.1.2.1.1.1 - Obex Liquidity Layer Addresses [Core]  <!-- UUID: ef875c4e-2303-4b94-8c92-6831ec96fac9 -->

The documents herein provide the addresses of the Obex Liquidity Layer's constituent contracts.

###### A.6.1.1.5.2.6.1.2.1.1.1.1 - Allocator Contract Addresses [Core]  <!-- UUID: 4cd1c7c9-f246-40b1-a31c-4512638f7fd3 -->

The documents herein contain global key addresses for the Allocator Contracts.

###### A.6.1.1.5.2.6.1.2.1.1.1.1.1 - Ethereum Mainnet [Core]  <!-- UUID: 3dbd11b0-2713-40e1-b0ca-66f5ebdf213c -->

The documents herein contain the Allocator Contract Addresses on the Ethereum Mainnet.

###### A.6.1.1.5.2.6.1.2.1.1.1.1.1.1 - Allocator Buffer Contract [Core]  <!-- UUID: 0d4e4822-8b33-4306-9f32-c08cd4014484 -->

The address of the ALLOCATOR_BUFFER contract is: `0x51E9681D7a05abFD33EfaFd43e5dd3Afc0093F1D`

###### A.6.1.1.5.2.6.1.2.1.1.1.1.1.2 - Allocator Oracle Contract [Core]  <!-- UUID: 87e95c06-0f81-4908-8282-8067346b3200 -->

The address of the ALLOCATOR_ORACLE contract is: `0xc7B91C401C02B73CBdF424dFaaa60950d5040dB7`

###### A.6.1.1.5.2.6.1.2.1.1.1.1.1.3 - Allocator Registry Contract [Core]  <!-- UUID: 850fc16c-496e-4148-a86a-d2d2e5f03685 -->

The address of the ALLOCATOR_REGISTRY contract is: `0xCdCFA95343DA7821fdD01dc4d0AeDA958051bB3B`

###### A.6.1.1.5.2.6.1.2.1.1.1.1.1.4 - Allocator Roles Contract [Core]  <!-- UUID: 0b889cc8-0fa2-476e-ae62-77bc09ca556e -->

The address of the ALLOCATOR_ROLES contract is: `0x9A865A710399cea85dbD9144b7a09C889e94E803`

###### A.6.1.1.5.2.6.1.2.1.1.1.1.1.5 - Allocator Vault Contract [Core]  <!-- UUID: a4310d54-9535-43ec-8d6a-c92c854f8a98 -->

The address of the ALLOCATOR_VAULT contract is: `0xF275110dFE7B80df66a762f968f59B70BABE2b29`

###### A.6.1.1.5.2.6.1.2.1.1.1.2 - ALM Contracts [Core]  <!-- UUID: 656c09f6-93a7-4b0b-a268-a495adeffaf0 -->

The documents herein contain addresses for the ALM Contracts for the Obex Liquidity Layer.

###### A.6.1.1.5.2.6.1.2.1.1.1.2.1 - Ethereum Mainnet [Core]  <!-- UUID: 5d99d731-c3ed-461c-a6ea-50ebd741b3d2 -->

The documents herein contain the ALM Contract Addresses for the Obex Liquidity Layer on the Ethereum Mainnet.

###### A.6.1.1.5.2.6.1.2.1.1.1.2.2 - ALM Controller Contract [Core]  <!-- UUID: cdb42b2b-e506-4e5e-a088-651b10880cde -->

The address of the ALM_CONTROLLER (MainnetController) contract is: `0xF2bB664f16E2df4b0c71F9d2cFc386504E795b7A`

###### A.6.1.1.5.2.6.1.2.1.1.1.2.3 - ALM Controller Contract Version [Core]  <!-- UUID: 4f345770-ead0-41ce-a821-96ab1291d033 -->

The ALM_CONTROLLER contract version is: V.1.6.0

###### A.6.1.1.5.2.6.1.2.1.1.1.2.4 - ALM Freezer Multisig Address [Core]  <!-- UUID: 855a0165-ff72-4d0f-bddf-62bae68be333 -->

The address of the Multisig that has the Freezer Role is specified in [A.6.1.1.5.2.6.1.2.1.2.2.3 - Freezer Multisig](49e6c234-7102-43e0-80a6-fb14e259e1f7).

###### A.6.1.1.5.2.6.1.2.1.1.1.2.5 - ALM Relayer Multisig Address [Core]  <!-- UUID: 86586cb8-ccbb-4ab7-8244-add51cca65fe -->

The address of the Multisigs that has the Relayer Role is specified in [A.6.1.1.5.2.6.1.2.1.2.2.1 - Prime Relayer Multisig](3b53c3b4-1d13-4197-8078-54523949784f) and [A.6.1.1.5.2.6.1.2.1.2.2.2 - Core Operator Relayer Multisig](b32dec2f-51e1-44b0-a81b-679b648ed659).

###### A.6.1.1.5.2.6.1.2.1.1.1.2.6 - ALM Proxy Contract [Core]  <!-- UUID: 53aa9c70-f2c8-4c0b-a30c-9c541d7dbbd4 -->

The address of the ALM_PROXY contract is: `0xb6dD7ae22C9922AFEe0642f9Ac13e58633f715A2`

###### A.6.1.1.5.2.6.1.2.1.1.1.2.7 - ALM Rate Limits Contract [Core]  <!-- UUID: 837cd549-5b8f-4d00-974b-f53af0f53f82 -->

The address of the ALM_RATE_LIMITS contract is: `0x81f8f5306cF80655Edff78f89860a8D89118E150`

###### A.6.1.1.5.2.6.1.2.1.1.2 - Off-chain Operational Parameters [Core]  <!-- UUID: 3f4a771a-ed2f-43ae-b8ad-a4d27e206779 -->

The documents herein list the off-chain operational parameters for the Obex Liquidity Layer. These operational parameters are protocol settings managed outside of smart contracts (off-chain), used by operators and off-chain systems to guide the functioning of the Obex Liquidity Layer.

###### A.6.1.1.5.2.6.1.2.1.1.2.1 - Off-chain Operational Parameters For Ethereum Mainnet [Core]  <!-- UUID: 5915e763-fa01-4202-95c9-b446b94bc92a -->

The document herein lists the current off-chain operational parameters for the Obex Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.5.2.6.1.2.1.1.2.1.1 - Minimum Operation Size Ethereum Mainnet [Core]  <!-- UUID: 319b996c-7563-4d56-a7b2-4302cebc91f5 -->

The minimum transaction size for operations on Ethereum Mainnet is (`MAINNET_MIN_OPERATION_SIZE`):

- This parameter will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.1.2.1.2 - Debt Ceiling Buffer Ethereum Mainnet [Core]  <!-- UUID: ff5d0ea1-bfb0-4e18-8768-603230a3dea6 -->

The buffer amount below the maximum debt ceiling is (`DEBT_CEILING_BUFFER`):

- This parameter will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.1.3 - Rate Limits [Core]  <!-- UUID: 3dea2074-9594-44af-80b9-f67d831bde1a -->

The documents herein list the Rate Limits for the Obex Liquidity Layer on each blockchain.

###### A.6.1.1.5.2.6.1.2.1.1.3.1 - Ethereum Mainnet [Core]  <!-- UUID: cecaa353-2826-4e19-a641-ee24989d42b6 -->

The documents herein list the current `RateLimits` for the Obex Liquidity Layer on Ethereum Mainnet.

###### A.6.1.1.5.2.6.1.2.1.1.3.1.1 - Ethereum Mainnet USDS [Core]  <!-- UUID: a97961ff-de69-4a13-b2a4-830a2458e3b9 -->

The maximum mint, burn and swap for USDS on Ethereum Mainnet are located herein

###### A.6.1.1.5.2.6.1.2.1.1.3.1.1.1 - USDS Mint Maximum [Core]  <!-- UUID: 1b4f0be7-31d8-4217-9961-08789613fbb1 -->

The maximum amount of USDS that can be minted within the Obex Liquidity Layer (`LIMIT_USDS_MINT`) is specified in the document herein.

- `maxAmount`: 100,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.5.2.6.1.2.1.1.3.1.1.2 - USDS Burn Maximum [Core]  <!-- UUID: 312ab6a0-55b8-4974-b918-bbd0f69085b3 -->

The maximum amount of USDS that can be burned within the Obex Liquidity Layer (`LIMIT_USDS_BURN`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Obex Artifact.
- `slope`: This parameter will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.1.3.1.1.3 - USDS For USDC Swap Maximum [Core]  <!-- UUID: 1bae9188-f480-49d7-91c5-c3f271260e60 -->

The maximum amount of USDS that can be swapped for USDC by the Obex Liquidity Layer in the Mainnet PSM (`LIMIT_USDS_TO_USDC`) is specified in the document herein.

- `maxAmount`: 100,000,000 USDS
- `slope`: 50,000,000 USDS per day

###### A.6.1.1.5.2.6.1.2.1.1.3.1.2 - Ethereum Mainnet sUSDS [Core]  <!-- UUID: d6cbd2a4-e0cb-4339-8354-5c11f6a72c93 -->

The maximum deposit and withdraw amounts for sUSDS on Ethereum Mainnet are located herein.

###### A.6.1.1.5.2.6.1.2.1.1.3.1.2.1 - Ethereum Mainnet sUSDS Deposit Maximum [Core]  <!-- UUID: a5d4f47c-615d-4bc7-bd7d-7cf694b7b02c -->

The maximum amount of sUSDS that can be deposited (`LIMIT_4626_DEPOSIT`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Obex Artifact.
- `slope`: This parameter will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.1.3.1.2.2 - Ethereum Mainnet sUSDS Withdrawal Maximum [Core]  <!-- UUID: 40959dc7-e554-4611-b615-25d3ff557bdf -->

The maximum amount of sUSDS that can be withdrawn (`LIMIT_4626_WITHDRAW`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Obex Artifact.
- `slope`: This parameter will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.1.3.1.3 - Ethereum Mainnet USDC ALM Proxy [Core]  <!-- UUID: 8505febf-f853-4de9-89dc-d483d5439cbc -->

The maximum amount that can be transferred and sent to the Ethereum Mainnet ALM Proxy for USDC are located herein.

###### A.6.1.1.5.2.6.1.2.1.1.3.1.3.1 - USDC ALM Proxy Maximum [Core]  <!-- UUID: 212d5d8b-7d1c-4e25-864b-f9e072d9d345 -->

The maximum amount of USDC that can be sent to the Ethereum Mainnet ALM Proxy (`LIMIT_USDC_TO_DOMAIN`, hashed with Ethereum domain) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Obex Artifact.
- `slope`: This parameter will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.1.3.1.3.1.1 - Maximum USDC Bridged To Ethereum Mainnet Via Circle CCTP [Core]  <!-- UUID: 17827367-6342-4e4e-bc1f-652c0f5b079e -->

The maximum amount of USDC that can be bridged to Ethereum Mainnet ALM Proxy using the Circle Cross-Chain Transfer Protocol (`LIMIT_USDC_TO_CCTP_ETH`) is specified in the document herein.

- `maxAmount`: This parameter will be specified in a future iteration of the Obex Artifact.
- `slope`: This parameter will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.1.4 - On-chain Parameters [Core]  <!-- UUID: 97d35c04-2b5b-430d-b297-b2b4703d71c0 -->

The documents herein list general on-chain parameters for the Obex Liquidity Layer

###### A.6.1.1.5.2.6.1.2.1.1.4.1 - Allocator Vault Parameters [Core]  <!-- UUID: c30d6144-4cbd-4ef4-90d5-312d24c9858e -->

The Allocator Vault parameters for ALLOCATOR-OBEX-A are defined in [A.3.7.1.2.1.5 - ALLOCATOR-OBEX-A Parameters](1ee3efd3-fe75-4766-bc6a-ec204f6a3bca).

###### A.6.1.1.5.2.6.1.2.1.1.4.2 - Whitelisting Of ALMProxy [Core]  <!-- UUID: 5c795414-020c-432d-91b6-a7d72495452e -->

The ALMProxy for Obex must be whitelisted on the LitePSM. This will effectively allow Obex to call `buyGemNoFee` and `sellGemNoFee` on the `MCD_LITE_PSM_USDC_A` contract.

###### A.6.1.1.5.2.6.1.2.1.2 - Governance Processes [Core]  <!-- UUID: 94015de1-4d83-43d3-998b-093c1a2099fa -->

The documents herein describe the specific governance processes for the Obex Liquidity Layer.

###### A.6.1.1.5.2.6.1.2.1.2.1 - Invoking New Instances [Core]  <!-- UUID: f6be405d-fae7-474e-882d-5c98985324b6 -->

The governance process to invoke a new Instance of the Allocation System Primitive follows the Root Edit process see Operational Process Definition.

###### A.6.1.1.5.2.6.1.2.1.2.2 - Multisigs [Core]  <!-- UUID: 7b3aa284-2872-4ffe-9938-2bbfa7d4525d -->

The documents herein define multisigs that have privileged access to manage the Obex Liquidity Layer.

###### A.6.1.1.5.2.6.1.2.1.2.2.1 - Prime Relayer Multisig [Core]  <!-- UUID: 3b53c3b4-1d13-4197-8078-54523949784f -->

The Prime Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.5.2.6.1.2.2.1.1.2 - Relayer Role](0a8458ff-499e-4ac6-85a3-6ce200df18ae) and is controlled by Obex.

###### A.6.1.1.5.2.6.1.2.1.2.2.1.1 - Address [Core]  <!-- UUID: 5d2d1cef-96c5-4881-a7b7-d70e75541fac -->

The address of the Prime Relayer Multisig on the Ethereum Mainnet is `0x5d36918C8F4726a62257AA79a50E53D553465663`.

###### A.6.1.1.5.2.6.1.2.1.2.2.1.2 - Required Number Of Signers [Core]  <!-- UUID: 2f7dbfea-075e-4208-bb37-abf05599b1d1 -->

The Prime Relayer Multisig currently has a 4/7 signing requirement.

###### A.6.1.1.5.2.6.1.2.1.2.2.1.3 - Signers [Core]  <!-- UUID: b14ad946-9e1c-494a-8849-45c30d625e3d -->

The signers of the Prime Relayer Multisig are seven (7) addresses controlled by Obex.

###### A.6.1.1.5.2.6.1.2.1.2.2.1.4 - Usage Standards [Core]  <!-- UUID: c96f7c83-92e7-4874-9c03-4a450cc904ff -->

The signers of the Prime Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.2.2.1.5 - Modification [Core]  <!-- UUID: 3212cf2f-ec75-4418-9fe2-f4b751bd19d8 -->

Obex can change the signers of the Prime Relayer Multisig at any time, so long as there are at least seven (7) signers and at least a majority of signers are required to execute transactions.

###### A.6.1.1.5.2.6.1.2.1.2.2.2 - Core Operator Relayer Multisig [Core]  <!-- UUID: b32dec2f-51e1-44b0-a81b-679b648ed659 -->

The Core Operator Relayer Multisig has the `RELAYER_ROLE` as defined in [A.6.1.1.5.2.6.1.2.2.1.1.2 - Relayer Role](0a8458ff-499e-4ac6-85a3-6ce200df18ae) and is controlled by Operational GovOps Soter Labs.

###### A.6.1.1.5.2.6.1.2.1.2.2.2.1 - Address [Core]  <!-- UUID: 17c29741-7ed5-4a6e-96ff-55514df2a8f5 -->

The address of the Core Operator Relayer Multisig on the Ethereum Mainnet is `0x2b1D60B11B7015fB83361a219BE01B7564436054`.

###### A.6.1.1.5.2.6.1.2.1.2.2.2.2 - Required Number Of Signers [Core]  <!-- UUID: ecc50ea6-d4f0-41be-b0f4-af11a34bd60e -->

The Core Operator Relayer Multisig currently has a 2/3 signing requirement.

###### A.6.1.1.5.2.6.1.2.1.2.2.2.3 - Signers [Core]  <!-- UUID: 2c9c02a4-86a1-4862-90aa-e314d9177f37 -->

The signers of the Core Operator Relayer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs.

###### A.6.1.1.5.2.6.1.2.1.2.2.2.4 - Usage Standards [Core]  <!-- UUID: 476f94f2-3e35-4d99-9664-c91984104b6b -->

The signers of the Core Operator Relayer Multisig must use the Multisig to exercise the `RELAYER_ROLE` in accordance with the instructions specified in the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.1.2.2.2.5 - Modification [Core]  <!-- UUID: a342e39a-ba3e-4871-ad17-17ce3323e6f2 -->

Operational GovOps Soter Labs can change the signers of the Core Operator Relayer Multisig at any time, so long as there are at least three (3) signers and at least two thirds of signers are required to execute transactions.

###### A.6.1.1.5.2.6.1.2.1.2.2.3 - Freezer Multisig [Core]  <!-- UUID: 49e6c234-7102-43e0-80a6-fb14e259e1f7 -->

The Freezer Multisig has the `FREEZER_ROLE` as defined in [A.6.1.1.5.2.6.1.2.2.1.1.4 - Freezer Role](afcfa58a-fc3d-4f5d-9bc8-bf40e7fa3ec7).

###### A.6.1.1.5.2.6.1.2.1.2.2.3.1 - Address [Core]  <!-- UUID: 6624912c-1cf6-443c-925f-ba1451a1644f -->

The address of the Freezer Multisig on the Ethereum Mainnet is `0x1924b6990B63c5f820b81a23CD40383808D416D8`.

###### A.6.1.1.5.2.6.1.2.1.2.2.3.2 - Required Number Of Signers [Core]  <!-- UUID: b1b34a90-ead4-4e45-8a88-72c1149f716b -->

The Freezer Multisig currently has a 2/5 signing requirement.

###### A.6.1.1.5.2.6.1.2.1.2.2.3.3 - Signers [Core]  <!-- UUID: cac6b239-3d5f-4014-98a2-df082c1c6cdb -->

The signers of the Freezer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs, one (1) address controlled by Operational Facilitator Redline Facilitation Group, and one (1) address controlled by Obex.

###### A.6.1.1.5.2.6.1.2.1.2.2.3.4 - Usage Standards [Core]  <!-- UUID: 0535c9cd-dd37-4a76-815d-836ad1dd1974 -->

The signers of the Freezer Multisig should exercise their authority to freeze the Obex Liquidity Layer in the event that Obex is not complying with rules regarding Risk Capital or Asset Liability Management, or in the event of another emergency.

Each action executed by the Freezer Multisig, including any function calls and their parameters, must be reported to the Sky community within a reasonable time frame through a post on the Sky Forum.

###### A.6.1.1.5.2.6.1.2.1.2.2.3.5 - Modification [Core]  <!-- UUID: 247ea87b-5649-4c92-aebe-5a5fc45c2c75 -->

Modification of the signers of the Freezer Multisig must be approved through an Atlas Edit Proposal.

The only exceptions to this are if: 1) a signer self-reports a loss of access to their private key due to any reason; or 2) a signer explicitly expresses their wish to be removed as a signer. In both cases, the signer is required to communicate the loss of access to their private key, or the wish to be removed as a signer, in the form of a public Sky Forum post. The specific signer should be replaced as soon as possible.

Any changes to the Multisig signers that do not fall within the two exceptions listed above, or that have not been ratified by Sky Governance, should be questioned immediately and treated as malicious. Where malicious activity is suspected, the Core Facilitator must prepare an expedited Executive Vote so that Sky Governance can vote on removing external security access from the Multisig.

###### A.6.1.1.5.2.6.1.2.1.3 - Total Risk Capital (TRC) Management [Core]  <!-- UUID: f65883db-3b01-4c25-be16-d05c8b95494a -->

The documents herein specify requirements related to Obex’s Total Risk Capital (TRC) management.

###### A.6.1.1.5.2.6.1.2.1.3.1 - Treadstone's Operation Of Obex Liquidity Layer And Agreement Regarding Encumbrance Ratio [Core]  <!-- UUID: d915471b-230e-41ab-bc86-68bc9453e417 -->

Treadstone will operate the Obex Liquidity Layer and agrees to stay at or below a 90% Encumbrance Ratio. See [A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9).

###### A.6.1.1.5.2.6.1.2.1.3.2 - Treadstone's Total Risk Capital (TRC) Management Processes [Core]  <!-- UUID: 8248b6dc-0dd9-4019-98e6-83c8d5892317 -->

As operators of the Obex Liquidity Layer, Treadstone automatically inherits, and is subject to, the base class of operational requirements related to Total Risk Capital management defined in [A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capital (TRC) Management](3af8a3a2-25e5-44b3-87a4-7df1f2712685). Modifications to the base operational logic automatically propagate to the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.2 - Obex Liquidity Layer Operational Processes [Core]  <!-- UUID: f0393207-2bae-42a2-9ca0-df8ffd4d2a39 -->

The documents herein describe common operational procedures for the Obex Liquidity Layer applicable across multiple Instances.

###### A.6.1.1.5.2.6.1.2.2.1 - Routine Protocol [Core]  <!-- UUID: cea1c91e-e940-41ab-99bb-254b821b24ff -->

The documents herein define the protocol for routine ongoing management of the Obex Liquidity Layer and its active Instances.

###### A.6.1.1.5.2.6.1.2.2.1.1 - Role Hierarchy And Permissions [Core]  <!-- UUID: 4eb0b4dc-9ffe-4201-b0cf-31e1cde8fcdb -->

The documents herein defines roles (Admin, Relayer, ALM Controller and Freezer) and their responsibilities/permissions for managing the Obex Liquidity Layer.

###### A.6.1.1.5.2.6.1.2.2.1.1.1 - Default Admin Role [Core]  <!-- UUID: d0dfc54e-e06e-434b-9194-9b1ad5b6be8a -->

The admin role (DEFAULT_ADMIN_ROLE) is the role that can grant and revoke any role, including itself and all other roles defined in the contract. The admin role is also used for general admin functions in all contracts. This role is fully controlled by Sky Governance via the Obex Proxy.

`constructor(address admin) {
_grantRole(DEFAULT_ADMIN_ROLE, admin);`

###### A.6.1.1.5.2.6.1.2.2.1.1.2 - Relayer Role [Core]  <!-- UUID: 0a8458ff-499e-4ac6-85a3-6ce200df18ae -->

The `RELAYER_ROLE` is the address for the Obex Liquidity Layer ALM Planner off-chain system that calls functions on `Controller` contracts to perform actions on behalf of the `ALMProxy` contract. The Relayer Role may be granted to an address by any address holding the `DEFAULT_ADMIN_ROLE`. The Relayer Role may be removed from an address by any address holding the `DEFAULT_ADMIN_ROLE` or the `FREEZER_ROLE`.

###### A.6.1.1.5.2.6.1.2.2.1.1.3 - ALM Controller Role [Core]  <!-- UUID: 9a8f34e4-1e38-48da-8fc7-e97d8b6dc64f -->

The `ALM_CONTROLLER_ROLE` is the address of the role that can call the `call` functions on the `ALMProxy` contract and update `RateLimits` contract. It includes the `MainnetController` and `ForeignController` contracts. ALM Controller contracts are accessed and modified via the Relayer Role.

###### A.6.1.1.5.2.6.1.2.2.1.1.4 - Freezer Role [Core]  <!-- UUID: afcfa58a-fc3d-4f5d-9bc8-bf40e7fa3ec7 -->

The `FREEZER_ROLE` is the address of the emergency role that can remove a compromised Relayer.

###### A.6.1.1.5.2.6.1.2.2.1.2 - Controller Functions [Core]  <!-- UUID: b64040c5-b290-478a-b69f-08cd8b5e7003 -->

The documents herein describe the purpose and operational use of key functions within the Obex Liquidity Layer `MainnetController` contracts: USDS management (mint/burn USDS), Asset Transfer Management (direct transfers, protocol deposits/withdrawals), Cross-chain Operations (CCTP bridging).

###### A.6.1.1.5.2.6.1.2.2.1.2.1 - Mainnet Controller Contract Functions [Core]  <!-- UUID: 39a5aa5c-19b0-4012-9f8d-2cef298bdd4b -->

The documents herein define the functions controlled by the Controller contract for Obex Liquidity Layer operations on Ethereum Mainnet.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.1 - Admin Functions [Core]  <!-- UUID: abb49068-d94b-4569-9014-bb767ceec6cb -->

The documents herein define the operations performed by the admin role (see [A.6.1.1.5.2.6.1.2.2.1.1.1 - Default Admin Role](d0dfc54e-e06e-434b-9194-9b1ad5b6be8a)) within the `MainnetController` contract.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.1.1 - Set Mint Recipient For Destination Domain [Core]  <!-- UUID: 1a834a8b-d87b-4eed-8f17-8276a2ae2dee -->

The documents herein define the steps for an admin to specify which address should receive newly minted tokens on a particular destination domain.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.1.1.1 - Call setMintRecipient Function [Core]  <!-- UUID: 05134536-1b5a-488f-8c82-a9a1aa6ea836 -->

Only an operator with the admin role is able to set the mint recipient for a destination domain. To do so, they must call the `setMintRecipient` function on the Controller contract on mainnet providing the destination domain and the mint recipient address. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role the transaction will revert.
- The contract will set the selected mint recipient for the specified destination domain.
- The contract will emit a `MintRecipientSet` event to the blockchain logs.

The function call is as follows:

`function setMintRecipient(uint32 destinationDomain, bytes32 mintRecipient) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.1.2 - Set LayerZero Recipient [Core]  <!-- UUID: 27f7da97-2cf4-4d32-81e9-c1ef7b8f0199 -->

The documents herein define the steps for an admin to specify which address should receive LayerZero messages on a particular destination endpoint.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.1.2.1 - Call setLayerZeroRecipient Function [Core]  <!-- UUID: 54c019d8-ae0a-4c1c-9f05-1192d7b1cefb -->

Only an operator with the admin role is able to set the LayerZero recipient for a destination endpoint. To do so, they must call the `setLayerZeroRecipient` function on the Controller contract on mainnet, providing the destination endpoint ID and the recipient address. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the selected LayerZero recipient for the specified destination endpoint.
- The contract will emit a `LayerZeroRecipientSet` event to the blockchain logs.

The function call is as follows:

`function setLayerZeroRecipient(uint32 destinationEndpointId, bytes32 layerZeroRecipient) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.1.3 - Set Maximum Slippage [Core]  <!-- UUID: c25f736d-c806-4287-a5ee-9ef81f8e0ab7 -->

The documents herein define the steps for an admin to set the maximum allowed slippage for a specific pool.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.1.3.1 - Call setMaximumSlippage Function [Core]  <!-- UUID: 9926982e-5571-4108-9caa-88b4d8708d45 -->

Only an operator with the admin role is able to set the maximum slippage for a pool. To do so, they must call the `setMaxSlippage` function on the Controller contract on mainnet, providing the pool address and the maximum slippage value. Calling this function will carry out the following actions:

- The contract will confirm the admin status of the operator. If the caller does not have the admin role, the transaction will revert.
- The contract will set the maximum slippage for the specified pool.
- The contract will emit a `MaxSlippageSet` event to the blockchain logs.

The function call is as follows:

`function setMaxSlippage(address pool, uint256 maxSlippage) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2 - Relayer Functions [Core]  <!-- UUID: 04da1a02-47fb-4ecd-9b50-27daf99b6d6f -->

The documents herein define the operations performed by the relayer role (see [A.6.1.1.5.2.6.1.2.2.1.1.2 - Relayer Role](0a8458ff-499e-4ac6-85a3-6ce200df18ae)) within the `MainnetController` contract.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.1 - Relayer Vault Functions [Core]  <!-- UUID: dad796ae-ec65-4aec-b0d4-c47e87f3d148 -->

The documents herein define the operations that are performed to maintain the desired level of liquidity and debt balance of the Obex Liquidity Layer.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.1.1 - Mint USDS [Core]  <!-- UUID: d56d12e9-b513-4e8c-8e3c-cf9e49d59f2b -->

The documents herein define the steps for a relayer to mint USDS from the Sky Allocation Vault to the Obex ALM Proxy.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.1.1.1 - Call mintUSDS Function [Core]  <!-- UUID: e6313c89-b401-468d-882b-bf5e57d0182c -->

Only an operator with the relayer role is able to mint USDS. To do so, they must call the `mintUSDS` function on the Controller contract on mainnet with the amount of USDS that is required for minting. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will ensure the `RateLimits` allow for minting the required amount. If the mint amount does not fall within the available Rate Limit the transaction will revert.
- The contract will reduce the Rate Limit by the amount of USDS minted in this transaction.
- The contract will mint the required USDS into the buffer contract.
- The contract will transfer the newly minted USDS from the buffer to the Proxy.

The function call is as follows:

`function mintUSDS(uint256 usdsAmount) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS [Core]  <!-- UUID: 1e27b007-ed34-4c15-9116-d62145572dce -->

The documents herein define the steps for a relayer to return and then burn Obex’s USDS debt in the Sky Allocation Vault.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.1.2.1 - Call burnUSDS Function [Core]  <!-- UUID: 9faf62a8-812c-4986-8133-5b3493634b9f -->

Only an operator with the relayer role is able to repay vault debt and burn USDS. To do so, they must call the `burnUSDS` function of the Controller contract on mainnet with the amount of USDS that they wish to burn. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will increase the available Rate Limit for minting USDS by the amount of USDS being burned. This increase will be limited by the `maxAmount` parameter in the `Rate Limit` contract.
- The contract will transfer USDS from the proxy to the buffer.
- The contract will burn the USDS from the buffer and `wipe` an equivalent amount from the vault's debt.

The function call is as follows:

`function burnUSDS(uint256 usdsAmount) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.2 - ERC-20 Functions [Core]  <!-- UUID: 4d4dd524-bad6-424b-9d39-0e35f8f889b4 -->

The documents herein define the operations that are performed to transfer ERC-20 assets to specified destinations.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.2.1 - Transfer Asset [Core]  <!-- UUID: 81128daf-2709-465d-bfd3-ff29e5566072 -->

The documents herein define the steps for a relayer to transfer ERC-20 tokens to a destination address.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.2.1.1 - Call transferAsset Function [Core]  <!-- UUID: 77447d4a-137b-4b1c-b266-02ca8c678f61 -->

Only an operator with the relayer role is able to transfer ERC-20 assets. To do so, they must call the `transferAsset` function on the Controller contract on mainnet, providing the ERC20 asset address, the destination address, and the amount to transfer. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role the transaction will revert.
- The contract will ensure the `RateLimits` allow for transferring the specified amount of the asset to the destination. If the transfer amount does not fall within the available Rate Limit, the transaction will revert.
- The contract will execute the ERC-20 `transfer` function, sending the specified amount of the asset to the destination address.

The function call is as follows:

`function transferAsset(address asset, address destination, uint256 amount) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.3 - ERC-4626 Functions [Core]  <!-- UUID: 08d30ec2-c343-4176-aded-dce33e76d69c -->

The documents herein define the general Obex Liquidity Layer operational procedures for interacting with ERC-4626-compliant tokenized vaults. ERC-4626 is a standard interface for vaults representing shares of an underlying ERC-20 token. Obex Liquidity Layer can integrate with various ERC-4626 vaults. For instance-specific parameters (such as vault addresses, asset addresses, and rate limits), refer to the relevant ERC-4626 Instance Configuration Document.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.3.1 - Deposit To ERC-4626 Vault [Core]  <!-- UUID: bab638ed-79fb-4163-aeb2-c569fc79c8e1 -->

The documents herein define the steps for a relayer to deposit assets from the ALM Proxy to an ERC-4626 vault to receive yield-bearing shares.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.3.1.1 - Call depositERC4626 Function [Core]  <!-- UUID: 58edaa80-7dc0-4591-93fb-3552a2bb6a0b -->

Only an operator with the relayer role can deposit assets into an ERC-4626 vault. To do so, they must call the `depositERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to deposit. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for deposit; otherwise, the transaction will revert. The rate limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the deposit amount is within the allowed rate limit for the specified vault.
- The contract will approve the vault to spend the underlying asset from the ALM Proxy. The approval and deposit are both performed from the ALM Proxy address.
- The contract will deposit the specified amount into the vault, and the ALM Proxy will receive the corresponding number of vault shares.

The function call is as follows:

`function depositERC4626(address token, uint256 amount) external returns (uint256 shares)`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.3.2 - Withdraw From ERC-4626 Vault [Core]  <!-- UUID: 3ea615ce-f2a9-4451-aed4-dd52c0703f5b -->

The documents herein define the steps for a relayer to withdraw a specified amount of the underlying asset from an ERC-4626 vault to the ALM Proxy.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.3.2.1 - Call withdrawERC4626 Function [Core]  <!-- UUID: d545d2f1-5973-4a93-889c-9d558ff79be7 -->

Only an operator with the relayer role can withdraw assets from an ERC-4626 vault. To do so, they must call the `withdrawERC4626` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to withdraw. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for withdrawal; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the withdrawal amount is within the allowed rate limit for the specified vault.
- The contract will withdraw the specified amount from the vault, burning the necessary number of vault shares held by the ALM Proxy as part of the withdrawal process.
- The withdrawn assets will be sent to the ALM Proxy.

The function call is as follows:

`function withdrawERC4626(address token, uint256 amount) external returns (uint256 shares)`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.3.3 - Redeem ERC-4626 Shares [Core]  <!-- UUID: 8e6a7981-7658-4c4e-ab87-aad8db8e215e -->

The documents herein define the steps for a relayer to redeem vault shares for the underlying asset from an ERC-4626 vault, with the assets sent to the ALM Proxy.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.3.3.1 - Call redeemERC4626 Function [Core]  <!-- UUID: 5e9546bb-fbb9-4f4f-92f6-5ba41dffb41f -->

Only an operator with the relayer role can redeem vault shares for the underlying asset. To do so, they must call the `redeemERC4626` function on the Controller contract on mainnet, providing the number of shares to redeem. The address is the ALM Proxy acting as both the owner of the shares being redeemed and the receiver of the resulting assets. The operation will only succeed if the ALM Proxy holds at least the number of shares specified for redemption; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will redeem the specified number of shares from the vault, sending the resulting assets to the ALM Proxy.
- After redemption, the contract will update the withdrawal rate limit based on the amount of assets received.

The function call is as follows:

`function redeemERC4626(address token, uint256 shares) external returns (uint256 assets)`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.4 - ERC-7540 Functions [Core]  <!-- UUID: e1a57a43-7bac-4f32-b4cc-4de7c050a89b -->

The documents herein define the general Obex Liquidity Layer operational procedures for interacting with ERC-7540-compliant tokenized vaults. ERC-7540 is a standard interface for vaults representing and managing multiple underlying assets within a single vault. Obex Liquidity Layer can integrate with various ERC-7540 vaults. For instance-specific parameters (such as vault addresses, asset addresses, and rate limits), refer to the relevant ERC-7540 Instance Configuration Document.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.4.1 - Deposit To ERC-7540 Vault [Core]  <!-- UUID: 63200ccb-fb66-4ce8-a9b9-d056f72ec60b -->

The documents herein define the steps for a relayer to request and claim deposit of assets from the ALM Proxy to an ERC-7540 vault.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.4.1.1 - Call requestDepositERC7540 Function [Core]  <!-- UUID: 134e3124-3ba1-43dc-a3e6-9347416f006b -->

Only an operator with the relayer role can request a deposit into an ERC-7540 vault. To do so, they must call the `requestDepositERC7540` function on the Controller contract on mainnet, providing the vault token address and the amount of the underlying asset to deposit. The operation will only succeed if the ALM Proxy holds at least the amount of the underlying asset specified for deposit; otherwise, the transaction will revert. The Rate Limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the deposit amount is within the allowed rate limit for the specified vault.
- The contract will approve the vault to spend the underlying asset from the ALM Proxy. The approval and deposit are both performed from the ALM Proxy address.
- The contract will submit a deposit request to the vault. Shares will not be received immediately; they must be claimed in a separate step after the vault processes the deposit.

The function call is as follows:

`function requestDepositERC7540(address token, uint256 amount) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.4.1.2 - Call claimDepositERC7540 Function [Core]  <!-- UUID: 41f68822-0f26-4fb2-a805-587fc08abb3f -->

Only an operator with the relayer role can claim shares from an ERC-7540 vault after a deposit request. To do so, they must call the `claimDepositERC7540` function on the Controller contract on mainnet, providing the vault token address. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will determine the maximum number of shares that can be claimed by the ALM Proxy.
- The contract will claim the shares from the vault, and the ALM Proxy will receive the corresponding number of vault shares.

The function call is as follows:

`function claimDepositERC7540(address token) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.4.2 - Redeem From ERC-7540 Vault [Core]  <!-- UUID: 6765a298-8ea7-4b1d-8d37-b3ccb069e12b -->

The documents herein define the steps for a relayer to request and redeem vault shares for the underlying asset from an ERC-7540 vault, with the assets sent to the ALM Proxy.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.4.2.1 - Call requestRedeemERC7540 Function [Core]  <!-- UUID: bd723808-6f03-41ed-9b19-72672d38dc36 -->

Only an operator with the relayer role can request the redemption of shares from an ERC-7540 vault. To do so, they must call the `requestRedeemERC7540` function on the Controller contract on mainnet, providing the vault token address and the number of shares to redeem. The rate limit configuration serves as whitelisting for vaults. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the redemption amount is within the allowed rate limit for the specified vault.
- The contract will submit a redemption request to the vault. Assets will not be received immediately; they must be claimed in a separate step after the vault processes the redemption.

The function call is as follows:

`function requestRedeemERC7540(address token, uint256 amount) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.4.2.2 - Call claimRedeemERC7540 Function [Core]  <!-- UUID: 08474241-fee8-4ca3-95e8-564bd6676ea1 -->

Only an operator with the relayer role can claim assets from an ERC-7540 vault after a redemption request. To do so, they must call the `claimRedeemERC7540` function on the Controller contract on mainnet, providing the vault token address. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will determine the maximum amount of assets that can be claimed by the ALM Proxy.
- The contract will claim the assets from the vault, and the ALM Proxy will receive the corresponding amount of underlying assets.

The function call is as follows:

`function claimRedeemERC7540(address token) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.5 - Dai / USDS Functions [Core]  <!-- UUID: df1e38f3-5954-44d6-8500-6d26f03cc8da -->

The documents herein define the swap operations between Dai and USDS.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.5.1 - Swap USDS to Dai [Core]  <!-- UUID: 22b124dd-3e9d-4439-bc4e-2993f2c267dd -->

The documents herein define a series of operations for an operator to `swap` USDS to Dai.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.5.1.1 - Call swapUSDSToDAI Function [Core]  <!-- UUID: ed445f2b-9211-46fe-b79a-6e70cac7fec7 -->

Only an operator with the relayer role can swap USDS to Dai. To do so, they must call the `swapUSDSToDAI` function on the Controller contract on mainnet, providing the usdsAmount. The operation will only succeed if the Proxy holds enough USDS for the swap; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will approve the DaiUsds migrator to spend the specified USDS amount from the Proxy.
- The contract will swap USDS to Dai at a 1:1 ratio by calling the `usdsToDai` function on the migrator, sending the resulting DAI to the proxy.

The function call is as follows:

`function swapUSDSToDAI(uint256 usdsAmount) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.5.2 - Swap Dai to USDS [Core]  <!-- UUID: d536a9fd-fa93-4909-ab75-17f3c4ccce3a -->

The documents herein define a series of operations for an operator to `swap` Dai to USDS.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.5.2.1 - Call swapDAIToUSDS Function [Core]  <!-- UUID: 3941f682-b9ae-483e-93a5-4c756388434e -->

Only an operator with the relayer role can swap Dai to USDS. To do so, they must call the `swapDAIToUSDS` function on the Controller contract on mainnet, providing the daiAmount. The operation will only succeed if the Proxy holds enough Dai for the swap; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will approve the DaiUsds migrator to spend the specified Dai amount from the Proxy.
- The contract will swap Dai to USDS at a 1:1 ratio by calling the `daiToUsds` function on the migrator, sending the resulting USDS to the proxy.

The function call is as follows:

`function swapDAIToUSDS(uint256 daiAmount) external`

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.6 - PSM Functions [Core]  <!-- UUID: 8666d408-4c3a-4646-8cbf-d0752167dcd6 -->

The documents herein define the swap operations performed by the Obex Liquidity Layer in the PSM.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.1 - Swap USDS to USDC [Core]  <!-- UUID: 43917647-67dc-4981-8048-522c19b4caf0 -->

The documents herein define a series of operations for an operator to `swap` USDS to USDC through the PSM.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.1.1 - Call swapUSDSToUSDC Function [Core]  <!-- UUID: 0ec7c5be-32a2-4d3b-b856-71face6612a9 -->

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

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.2 - Swap USDC To USDS [Core]  <!-- UUID: 17675b49-5767-47de-9ccf-e324b7bebec5 -->

The documents herein define a series of operations for an operator to `swap` USDC to USDS through the PSM.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.2.1 - Call swapUSDCToUSDS Function [Core]  <!-- UUID: f0117433-4568-4b4b-bed6-fce75f85939a -->

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

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.3 - Transfer Token Via LayerZero [Core]  <!-- UUID: 7f1746e3-9bc8-467f-97b8-72e4ee51ebfc -->

The documents herein define the steps for a relayer to `transfer` a token via LayerZero to a destination endpoint, with the assets sent according to the configured recipient.

###### A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.3.1 - Call transferTokenLayerZero Function [Core]  <!-- UUID: 04a8ecfb-e8b5-4994-b4f1-1fe99efd8dcd -->

Only an operator with the relayer role can transfer tokens via LayerZero. To do so, they must call the `transferTokenLayerZero` function on the Controller contract on mainnet, providing the oftAddress, amount, and destinationEndpointId (payable for native fees). The operation will only succeed if the ALM Proxy holds sufficient tokens and fees; otherwise, the transaction will revert. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the transfer amount is within the allowed rate limit (built from LIMIT_LAYERZERO_TRANSFER, oftAddress, and destinationEndpointId).
- If approval is required, the contract will approve the token for the oftAddress.
- The contract will build LayerZero send options and a SendParam struct with destination details, amount, and recipient from layerZeroRecipients.
- The contract will quote the OFT receipt to set the minimum amount received.
- The contract will quote the messaging fee and execute the send via proxy.doCallWithValue, passing the fee value.

The function call is as follows:

`function transferTokenLayerZero(address oftAddress, uint256 amount, uint32  destinationEndpointId) external payable`

###### A.6.1.1.5.2.6.1.2.2.1.3 - Rate Limit Management [Core]  <!-- UUID: 73da45c9-78eb-49f3-a1d5-593780e9d362 -->

The documents herein define the protocol for querying, setting, and adjusting `RateLimits` for Instances using their `RateLimitID`s. The Rate Limits must be maintained in line with Obex's strategy, market conditions, and security considerations.

###### A.6.1.1.5.2.6.1.2.2.1.3.1 - Get Rate Limit Data [Core]  <!-- UUID: 716b493e-d102-47c8-8f87-bcb1c809c8ee -->

Anyone can query the full rate limit data for a specific key. Calling this function will carry out the following actions:

- The contract will return the stored RateLimitData struct from the _data mapping for the key.

The function call is as follows:

`function getRateLimitData(bytes32 key) external override view returns (RateLimitData memory)`

###### A.6.1.1.5.2.6.1.2.2.1.3.2 - Set Rate Limit Data [Core]  <!-- UUID: 993bbc35-1692-4c1b-87b2-de5997e90bf5 -->

Only an operator with the admin role is able to set or update rate limit data for a specific key, including maxAmount, slope, and historical values. There are two overloads for flexibility. Calling these functions will carry out the following actions:

- The contract will require that lastAmount is less than or equal to maxAmount, reverting with "RateLimits/invalid-lastAmount" if not.
- The contract will require that lastUpdated is less than or equal to the current block timestamp, reverting with "RateLimits/invalid-lastUpdated" if not.
- The contract will store the provided data in the _data mapping as a RateLimitData struct.
- The contract will emit a RateLimitDataSet event with the key and provided values.

The function calls are as follows:

`function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope, uint256 lastAmount, uint256 lastUpdated) public override onlyRole(DEFAULT_ADMIN_ROLE)

function setRateLimitData(bytes32 key, uint256 maxAmount, uint256 slope) external override`

###### A.6.1.1.5.2.6.1.2.2.1.3.3 - Set Unlimited Rate Limit Data [Core]  <!-- UUID: 37aed332-50c8-4392-91be-095bd13139d1 -->

Only an operator with the admin role is able to set unlimited rate limit data for a specific key by configuring it with maximum values. Calling this function will carry out the following actions:

- The contract will call setRateLimitData internally with type(uint256).max for maxAmount and lastAmount, 0 for slope, and the current block timestamp for lastUpdated.

The function call is as follows:

`function setUnlimitedRateLimitData(bytes32 key) external override`

###### A.6.1.1.5.2.6.1.2.2.1.3.4 - Get Current Rate Limit [Core]  <!-- UUID: f629bb8f-afb2-4bfc-b7fa-3f5fbaa2c2f9 -->

Anyone can query the current rate limit value for a specific key, accounting for time-based slope accrual. Calling this function will carry out the following actions:

- The contract will retrieve the RateLimitData for the key from the _data mapping.
- If maxAmount is type(uint256).max (unlimited case), the contract will return type(uint256).max.
- Otherwise, the contract will calculate and return the minimum of (slope * time elapsed since lastUpdated + lastAmount) and maxAmount.

The function call is as follows:

`function getCurrentRateLimit(bytes32 key) public override view returns (uint256)`

###### A.6.1.1.5.2.6.1.2.2.1.3.5 - Trigger Rate Limit Decrease [Core]  <!-- UUID: 2fc640dc-1f48-4167-a700-cb54f2cb1097 -->

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

###### A.6.1.1.5.2.6.1.2.2.1.4 - Instance Lifecycle Management [Core]  <!-- UUID: 2dde3f2b-925d-42a4-9fe1-0cb5bfd86855 -->

The documents herein define processes for invoking (onboarding) new Obex Liquidity Layer Instances and offboarding existing ones. This process will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.2.1.5 - Upgrading Controller [Core]  <!-- UUID: 4e238661-718b-44ec-8473-bad60d76074d -->

The documents herein define the process for deploying new Controller contracts. This process will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 7fc9e39e-4f3d-435a-84af-7fc74c449ce0 -->

The documents herein define the process for non-routine ongoing management of the Obex Liquidity Layer and its active Instances.

###### A.6.1.1.5.2.6.1.2.2.3 - Emergency Protocol [Core]  <!-- UUID: d99e4cb6-1c6c-4562-948b-c2ac4ea66253 -->

The documents herein define all the possible actions that can be taken in case of an emergency within Obex Liquidity Layer operations.

###### A.6.1.1.5.2.6.1.2.2.3.1 - Remove Compromised Relayer As Freezer [Core]  <!-- UUID: 15c966fc-e579-4277-abb0-6f0b9ad5cbce -->

In the event of a compromised Relayer, the `FREEZER_ROLE` can call the function to `removeRelayer` from the Controller contract. Only an operator with the freezer role can remove a relayer. To do so, they must call the `removeRelayer` function on the Controller contract on mainnet, providing the compromised relayer’s address. Calling this function will carry out the following actions:

- The contract will confirm the caller holds the freezer role. If the caller does not have the freezer role, the transaction will revert.
- The contract will revoke the relayer role from the specified address.
- The contract will emit a `RelayerRemoved(relayer)` event.

The function call is as follows:

`function removeRelayer(address relayer) external`

###### A.6.1.1.5.2.6.1.2.2.3.2 - Redeem All Mainnet Positions [Core]  <!-- UUID: 10597c85-6ce2-4364-a83b-e2d3c93c45c7 -->

The documents herein define the actions that should be performed by an operator if there is a need to recover the liquidity from Mainnet Protocols and centralize it in the Mainnet Obex ALM Proxy.

###### A.6.1.1.5.2.6.1.2.2.3.2.1 - ERC-4626 Withdrawal Action [Core]  <!-- UUID: 6078cd75-f853-49ca-b7c1-eaab4ef85c72 -->

In order to withdraw all ERC-4626 balances, the operator must call the `redeemERC4626` function.

The function call is as follows:

`function redeemERC4626(address(token), token.balanceOf(address(proxy)))`

For more detailed instructions on the code to execute this, see [A.6.1.1.5.2.6.1.2.2.1.2.1.2.3 - ERC-4626 Functions](08d30ec2-c343-4176-aded-dce33e76d69c).

###### A.6.1.1.5.2.6.1.2.2.3.3 - USDC To USDS Swap Action [Core]  <!-- UUID: b93c5c32-642e-4448-9ebd-c908dee78d46 -->

This document defines the action that should be performed by an operator if there is a need to centralize all recovered liquidity in USDS. The operator must call the `swapUSDCToUSDS` function.

The function call is as follows:

`function swapUSDCToUSDS(usdc.balanceOf(address(proxy))`

For more detailed instructions on the code to execute this see [A.6.1.1.5.2.6.1.2.2.1.2.1.2.6.2 - Swap USDC To USDS](17675b49-5767-47de-9ccf-e324b7bebec5).

###### A.6.1.1.5.2.6.1.2.2.3.4 - USDS Burn Action [Core]  <!-- UUID: 3304ecba-6dad-45af-886e-878648d2abb8 -->

This document defines the action that should be performed if there is a need to repay and then burn Obex's USDS debt. The operator must call the `burnUSDS` function.

The function call is as follows:

`function burnUSDS(usds.balanceOf(address(proxy))`

More detailed instructions on the code to execute this, see [A.6.1.1.5.2.6.1.2.2.1.2.1.2.1.2 - Burn USDS](1e27b007-ed34-4c15-9116-d62145572dce).

###### A.6.1.1.5.2.6.1.2.3 - Allocation Strategy [Core]  <!-- UUID: 5611a719-923b-4d95-b246-5bc788d55307 -->

In the future, additional logic will be added herein regarding the strategy by which capital is allocated between different Instances of the Obex Liquidity Layer.

##### A.6.1.1.5.2.6.1.3 - Active Instances [Core]  <!-- UUID: ccde7679-912d-403f-aad1-f9a56c8e3387 -->

The Instances of the Obex Liquidity Layer with `Active` Status are stored herein. The `RRC Framework Full Implementation Coverage` status defines whether the Instance Financial RRC is calculated based on a fully implemented risk model (see [A.3.2.1.1.4.3.1 - Fully Implemented Risk Models](419a1d00-fbae-4d26-bd47-8f57677d8001)) or a pending risk model (see [A.3.2.1.1.4.3.2 - Pending Risk Models](81ca88bf-3f6a-4d10-a3e2-d47cf6636d7d)). If the Instance Financial RRC is calculated based on a fully implemented risk model the status is `Covered`. If the Instance Financial RRC is calculated based on a pending risk model the status is `Pending`.

###### A.6.1.1.5.2.6.1.3.1 - Ethereum Mainnet Instances [Core]  <!-- UUID: a10f4c25-6281-42e5-8247-6ac5cac9f850 -->

The Ethereum Mainnet Instances of the Obex Liquidity Layer with `Active` Status are stored herein and are organized by target protocol.

###### A.6.1.1.5.2.6.1.3.1.1 - Maple [Core]  <!-- UUID: a03f7eb7-4f1f-441c-98ba-41c87f482186 -->

The Ethereum Mainnet Instances of the Maple Protocol with `Active` Status are stored herein.

###### A.6.1.1.5.2.6.1.3.1.1.1 - Ethereum Mainnet - Maple USDC Instance Configuration Document [Core]  <!-- UUID: 7488a14c-2464-4649-b476-48ee93bb438f -->

The documents herein contain the Instance Configuration Document for the Maple USDC Instance.

###### A.6.1.1.5.2.6.1.3.1.1.1.1 - RRC Framework Full Implementation Coverage [Core]  <!-- UUID: 28fa701f-7d0a-45e6-9977-e28bfd32fe0e -->

**`Covered`**

###### A.6.1.1.5.2.6.1.3.1.1.1.2 - Parameters [Core]  <!-- UUID: 82cb8c2b-c551-4ea0-bec2-6afa0d41ab8d -->

The documents herein define the parameters of the Maple USDC Instance of the Allocation System Primitive.

###### A.6.1.1.5.2.6.1.3.1.1.1.2.1 - Instance Identifiers [Core]  <!-- UUID: 87ea484a-cb48-46dc-b97b-ab79e59420bf -->

The documents herein define the Instance identifiers

###### A.6.1.1.5.2.6.1.3.1.1.1.2.1.1 - Network [Core]  <!-- UUID: 8b3a0a62-f92e-43cd-9791-8eab8c36ffe4 -->

Ethereum Mainnet

###### A.6.1.1.5.2.6.1.3.1.1.1.2.1.2 - Target Protocol [Core]  <!-- UUID: c953c251-42d5-4dcd-9952-6329ed7179f2 -->

Maple

###### A.6.1.1.5.2.6.1.3.1.1.1.2.1.3 - Asset Supplied By Obex Liquidity Layer [Core]  <!-- UUID: 7d83e07d-c05f-4917-97ef-7bca6a6cf184 -->

USDC

###### A.6.1.1.5.2.6.1.3.1.1.1.2.1.4 - Token [Core]  <!-- UUID: 0c1296a7-a091-4753-8851-3eb2df18cc33 -->

syrupUSDC

###### A.6.1.1.5.2.6.1.3.1.1.1.2.2 - Contract Addresses [Core]  <!-- UUID: 81a36b20-bf42-40eb-b47f-c5859529a77c -->

The documents herein define the Instance contract addresses.

###### A.6.1.1.5.2.6.1.3.1.1.1.2.2.1 - Token Address [Core]  <!-- UUID: 85a64942-705d-4079-a265-2510ae4310f7 -->

`0x80ac24aA929eaF5013f6436cdA2a7ba190f5Cc0b`

###### A.6.1.1.5.2.6.1.3.1.1.1.2.2.2 - Underlying Asset Address [Core]  <!-- UUID: e9a1b7f7-df7c-4b9c-83d1-96fc3b109089 -->

`0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

###### A.6.1.1.5.2.6.1.3.1.1.1.2.3 - RateLimitIDs [Core]  <!-- UUID: d2d46842-e9dd-4f88-bfa5-5e947381f70b -->

The specific `RateLimitID`(s) for this conduit's inflow and outflow will be specified in a future iteration of the Obex Artifact.

###### A.6.1.1.5.2.6.1.3.1.1.1.2.3.1 - Inflow RateLimitID [Core]  <!-- UUID: 97344456-e215-42e5-a149-89f0276e1b4c -->

The inflow RateLimitID is: `0x99a69e57b2f387f999d6adff6eb2e707b59fdb54f06ca6211b4f20956e9bfe10`

###### A.6.1.1.5.2.6.1.3.1.1.1.2.3.2 - Outflow RateLimitID [Core]  <!-- UUID: c4e18b43-5009-4c77-8781-bfc053d2c606 -->

The outflow RateLimitID is: `0x64e6fd9d694640eebeeefc7b5abe32ef09bbabaa3d4e60221461d05a9577dc57`

###### A.6.1.1.5.2.6.1.3.1.1.1.2.4 - Rate Limits [Core]  <!-- UUID: db184982-3dca-493b-b2a9-640196443cd8 -->

The current `maxAmount` and `slope` for this conduit’s inflow/outflow are defined in the documents herein.

###### A.6.1.1.5.2.6.1.3.1.1.1.2.4.1 - Inflow Rate Limits [Core]  <!-- UUID: 3776ec7d-668c-496d-aaa7-094ba92e496f -->

The deposit rate limits are:

- `maxAmount`: 100,000,000 USDC
- `slope`: 20,000,000 USDC per day

###### A.6.1.1.5.2.6.1.3.1.1.1.2.4.2 - Withdrawal Rate Limits [Core]  <!-- UUID: b29ac1d6-4cbd-46db-b77c-2f02d9705936 -->

The withdrawal rate limits are:

- `maxAmount`: Unlimited

###### A.6.1.1.5.2.6.1.3.1.1.1.2.5 - Off-chain Operational Parameters [Core]  <!-- UUID: b7dff5a9-125e-4ee1-9977-4698b5442b26 -->

The documents herein contain specific off-chain parameters for this Instance.

###### A.6.1.1.5.2.6.1.3.1.1.1.3 - Instance-specific Operational Processes [Core]  <!-- UUID: 12bfd1a4-fe27-4a7d-8c1e-d0541c690066 -->

The documents herein contain operational procedures or monitoring requirements unique to this Instance that deviate from or otherwise supplement the general Obex Liquidity Layer processes.

###### A.6.1.1.5.2.6.1.3.1.1.1.3.1 - Redeem Maple Shares [Core]  <!-- UUID: 6fb19cf7-516c-4de4-89b9-02288053f905 -->

The documents herein define the steps for a relayer to redeem vault shares from Maple.

###### A.6.1.1.5.2.6.1.3.1.1.1.3.1.1 - Call RequestMapleRedemption Function [Core]  <!-- UUID: fd047e05-3239-434b-a5d8-81cd72ada783 -->

Only an operator with the relayer role can request the redemption of shares from Maple. To do so, they must call the `requestMapleRedemption` function on the Controller contract on mainnet, providing the Maple token address and the number of shares to request. All Maple redemption operations are performed on behalf of the ALM Proxy and the destination address is always set to the proxy by the contract. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will ensure the redemption amount is within the allowed rate limit for the specified vault and decrease the rate limit for the redemption amount.
- The contract will submit a redemption request to the vault. Assets will not be received immediately; they must be claimed in a separate step after the vault processes the redemption.

The function call is as follows:

`function requestMapleRedemption(address mapleToken, uint256 shares) external`

###### A.6.1.1.5.2.6.1.3.1.1.1.3.1.2 - Call CancelMapleRedemption Function [Core]  <!-- UUID: 7378e3fb-3c6a-4ea4-8e01-c6b84658944d -->

Only an operator with the relayer role can cancel a previously requested redemption of shares from Maple. To do so, they must call the `cancelMapleRedemption` function on the Controller contract on mainnet, providing the Maple token address and the number of shares to cancel. All Maple cancellations of redemption operations are performed on behalf of the ALM Proxy. Calling this function will carry out the following actions:

- The contract will confirm the relayer status of the operator. If the caller does not have the relayer role, the transaction will revert.
- The contract will check that a rate limit exists for the asset. If no rate limit exists the transaction will revert.
- The contract will submit a cancellation request to the vault, removing the specified number of shares from the pending redemption.

The function call is as follows:

`function cancelMapleRedemption(address mapleToken, uint256 shares) external`

##### A.6.1.1.5.2.6.1.4 - Completed Instances [Core]  <!-- UUID: 6b16b0d6-a5a1-44da-a95d-e62d38a35ade -->

The Instances of the Obex Liquidity Layer with `Completed` Status are stored herein.

##### A.6.1.1.5.2.6.1.5 - In Progress Invocations [Core]  <!-- UUID: ca2c0cd1-73e3-49f1-b415-65e5f200b097 -->

The in progress Invocations of the Allocation System Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.6.1.3 - Active Instances](ccde7679-912d-403f-aad1-f9a56c8e3387).

#### A.6.1.1.5.2.6.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: 473d0f9e-a5dc-48ee-84b9-a48cd2b6f215 -->

The documents herein contain all data and specifications for Obex's Instances of the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.6.1.1.5.2.6.2.1 - Primitive Hub Document [Core]  <!-- UUID: 7c5c39de-a531-42a7-8b74-e8e6ffeb2bc3 -->

The documents herein organize all base information relevant to Obex's usage of the Risk Capital Rental Primitive.

###### A.6.1.1.5.2.6.2.1.1 - Global Activation Status [Core]  <!-- UUID: c3a0f75a-d418-411a-bc8e-ccde6aa938b1 -->

`Inactive`

###### A.6.1.1.5.2.6.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 5f9e7e17-d7c4-4c72-9d0f-a2b58de3bbe6 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.6.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 51f16355-24cf-463f-9603-154da3fcb1b3 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.6.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: b60d8075-b908-4086-9bb0-0d8a609b1dd6 -->

This document contains a Directory of all prospective Instances of the Risk Capital Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.6.2.1.2 - Active Instances Directory](5f9e7e17-d7c4-4c72-9d0f-a2b58de3bbe6), whereas failed Invocations are Archived in [A.6.1.1.5.2.6.2.1.5 - Hub Data Repository](a5fea5f5-f6b2-47e4-9ef5-bb23ba08921d).

###### A.6.1.1.5.2.6.2.1.5 - Hub Data Repository [Core]  <!-- UUID: a5fea5f5-f6b2-47e4-9ef5-bb23ba08921d -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.6.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ecd92a2e-9c67-4fb0-b3cf-3ad63cebf8a5 -->

The subtrees for archived Invocations and Instances of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.5.2.6.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 6e6d714e-4700-4aa8-bd61-6e8f012df6d4 -->

The subtrees for failed Invocations of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.5.2.6.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: fd2cdc13-4035-4c91-b17c-7d1d1d5c5b7b -->

The subtrees for Instances of the Risk Capital Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.6.2.2 - Active Instances [Core]  <!-- UUID: b894cf0e-5a3d-4fe2-bb43-668a1f973857 -->

The Instances of the Risk Capital Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.6.2.3 - Completed Instances [Core]  <!-- UUID: 4b2e42f3-064c-4cb8-87a8-96512a581841 -->

The Instances of the Risk Capital Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.5.2.6.2.4 - In Progress Invocations [Core]  <!-- UUID: b83be319-7f7e-4cf5-ad70-ac59302422e4 -->

The in progress Invocations of the Risk Capital Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.6.2.2 - Active Instances](b894cf0e-5a3d-4fe2-bb43-668a1f973857).

#### A.6.1.1.5.2.6.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: fab6088e-5b4c-4ab4-af33-051920120273 -->

The documents herein contain all data and specifications for Obex's Instances of the Asset Liability Management Rental Primitive. See [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

##### A.6.1.1.5.2.6.3.1 - Primitive Hub Document [Core]  <!-- UUID: 804821a4-0344-4642-9575-8bde38f8edef -->

The documents herein organize all base information relevant to Obex's usage of the Asset Liability Management Rental Primitive.

###### A.6.1.1.5.2.6.3.1.1 - Global Activation Status [Core]  <!-- UUID: 80b90a60-c898-4700-8c19-c168709b2bb0 -->

`Inactive`

###### A.6.1.1.5.2.6.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 10f33907-8a83-41ea-8e9c-c4a73882ce79 -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.6.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 6759bef4-337e-4e21-8dfe-4152b5618f0d -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.6.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 70f39980-940c-4f32-9365-a196fcca7858 -->

This document contains a Directory of all prospective Instances of the Asset Liability Management Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.6.3.1.2 - Active Instances Directory](10f33907-8a83-41ea-8e9c-c4a73882ce79), whereas failed Invocations are Archived in [A.6.1.1.5.2.6.3.1.5 - Hub Data Repository](c4856110-03a4-4f52-b13b-f3e99b8aba4f).

###### A.6.1.1.5.2.6.3.1.5 - Hub Data Repository [Core]  <!-- UUID: c4856110-03a4-4f52-b13b-f3e99b8aba4f -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.6.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: b79f57c2-8d27-4147-8b02-9a2794ab9986 -->

The subtrees for archived Invocations and Instances of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.5.2.6.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9ee5b528-4d53-46fb-b2ed-711c99fca801 -->

The subtrees for failed Invocations of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.5.2.6.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 06e80d6f-d630-4fab-99db-cb71211c8f56 -->

The subtrees for Instances of the Asset Liability Management Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.6.3.2 - Active Instances [Core]  <!-- UUID: b1667bfc-be11-4b02-ab99-d39b3f5e510d -->

The Instances of the Asset Liability Management Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.6.3.3 - Completed Instances [Core]  <!-- UUID: 9ce2e9b8-8033-4fae-bd6f-9f7b7590ba1b -->

The Instances of the Asset Liability Management Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.5.2.6.3.4 - In Progress Invocations [Core]  <!-- UUID: 3c1a4517-7097-4964-a687-5dc1de1b00ee -->

The in progress Invocations of the Asset Liability Management Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.6.3.2 - Active Instances](b1667bfc-be11-4b02-ab99-d39b3f5e510d).

### A.6.1.1.5.2.7 - Core Governance Primitives [Core]  <!-- UUID: 901fba8d-ac5f-4809-a3d4-e510fc9b74ca -->

The documents herein implement the Core Governance Primitives for Obex. See [A.2.2.11 - Core Governance Primitives](6fa54611-c744-4b9d-897d-b2a20e9cae5d).

#### A.6.1.1.5.2.7.1 - Core Governance Reward Primitive [Core]  <!-- UUID: 871764eb-5ccb-47fc-8852-0523e989bef6 -->

The documents herein contain all data and specifications for Obex's Instances of the Core Governance Reward Primitive. See [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a).

##### A.6.1.1.5.2.7.1.1 - Primitive Hub Document [Core]  <!-- UUID: e0e1769f-ecbe-4598-a236-318d7b00c929 -->

The documents herein organize all base information relevant to Obex's usage of the Core Governance Reward Primitive.

###### A.6.1.1.5.2.7.1.1.1 - Global Activation Status [Core]  <!-- UUID: a5f4abc0-9d2f-4356-9977-919fcf8ca427 -->

`Inactive`

###### A.6.1.1.5.2.7.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 03941fc1-96ff-454d-aa4d-0658057f7b4c -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Active`.

###### A.6.1.1.5.2.7.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 05d4383b-1140-49f9-857b-00eec596f248 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.5.2.7.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 77ff1220-f6e0-4b35-ad1c-0224aa5098df -->

This document contains a Directory of all prospective Instances of the Core Governance Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.5.2.7.1.1.2 - Active Instances Directory](03941fc1-96ff-454d-aa4d-0658057f7b4c), whereas failed Invocations are Archived in [A.6.1.1.5.2.7.1.1.5 - Hub Data Repository](6f24ea77-43d3-4c4f-84a0-9341114569c9).

###### A.6.1.1.5.2.7.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 6f24ea77-43d3-4c4f-84a0-9341114569c9 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.5.2.7.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 38d8dad5-0503-4d43-9826-a2895e9484cc -->

The subtrees for archived Invocations and Instances of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.5.2.7.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: aa94bd40-29d7-4bec-88e6-e54a658947f3 -->

The subtrees for failed Invocations of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.5.2.7.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 8cf31f6c-e9cc-4d01-97a3-afd2dae271c8 -->

The subtrees for Instances of the Core Governance Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.5.2.7.1.2 - Active Instances [Core]  <!-- UUID: 1627c920-e582-446c-b6a0-39f7a528f28a -->

The Instances of the Core Governance Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.5.2.7.1.3 - Completed Instances [Core]  <!-- UUID: e14a0186-9557-4b1f-b4c1-eddeb88e7e34 -->

The Instances of the Core Governance Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.5.2.7.1.4 - In Progress Invocations [Core]  <!-- UUID: 18f93603-5951-4d2e-9527-f88d81c408a3 -->

The in progress Invocations of the Core Governance Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.5.2.7.1.2 - Active Instances](1627c920-e582-446c-b6a0-39f7a528f28a).

## A.6.1.1.5.3 - Omni Documents [Core]  <!-- UUID: 239c5dd4-46a1-4936-8e31-f37ea2aa802c -->

The documents herein define Obex's strategic intent and operational processes relating to infrastructure inherited from Sky Core, activities unrelated to Sky Primitives, or activities spanning multiple Sky Primitives.

### A.6.1.1.5.3.1 - Governance Information Unrelated To Root Edit Primitive [Core]  <!-- UUID: bdad4ea3-7cf2-40fb-a8ab-4bb8b320e4c9 -->

The documents herein specify Obex governance information that is unrelated to the use of the Root Edit Primitive. The governance process for updating the Obex Artifact is specified in the Root Edit Primitive above at [A.6.1.1.5.2.2.2 - Root Edit Primitive](b69559bf-1acb-4f9c-8638-19fb8ef20fc2).

#### A.6.1.1.5.3.1.1 - Sky Forum [Core]  <!-- UUID: fb92df01-4e93-45ec-8e81-b59d5767ebb7 -->

Obex uses the Sky Forum for governance-related discussion. Posts should use the "Obex Prime" category.

#### A.6.1.1.5.3.1.2 - Sky Ecosystem Emergency Response [Core]  <!-- UUID: ec6dc53f-7398-4242-afc4-81e436541da2 -->

The documents herein specify Obex's emergency response protocol in situations that impact the entire Sky Ecosystem. This protocol will be specified in a future iteration of the Obex Artifact.

#### A.6.1.1.5.3.1.3 - Agent-Specific Emergency Response [Core]  <!-- UUID: e5ac06b5-0f4a-4506-bfa4-a4d18901e1cc -->

The documents herein specify Obex's emergency response protocol in situations solely impacting Obex versus the broader Sky Ecosystem. This protocol will be specified in a future iteration of the Obex Artifact.

### A.6.1.1.5.3.2 - Strategic Intent And Operating Model [Core]  <!-- UUID: b380c021-e579-47a2-ae01-c85340caa135 -->

Obex is an incubation-focused Prime within the Sky Ecosystem. It provides capital, infrastructure, and technical support to early-stage teams building on Sky Primitives. Obex's purpose is to accelerate aligned builders through structured incubation and funding. The subdocuments herein define the operating model, structure, mandate, and operational standards of Obex.

#### A.6.1.1.5.3.2.1 - Operating Model [Core]  <!-- UUID: 7d7658f6-31a9-4d73-8d3f-19b87d0e89ec -->

Obex follows a direct-execution model rather than a multi-layered governance system. Key processes include:

- **Incubation Selection:** Projects are sourced, evaluated, and onboarded based on strategic fit, feasibility, and alignment with Sky objectives.
- **Capital Allocation:** All allocations occur through the Obex Incubator Prime, which deploys first-loss or operational capital under predefined parameters.

#### A.6.1.1.5.3.2.2 - Risk and Compliance [Core]  <!-- UUID: d3466d20-01c9-453a-aee0-e7b8f9e17cf0 -->

Obex adheres to the Sky Ecosystem's standards for risk, transparency, and recourse.

#### A.6.1.1.5.3.2.3 - Ecosystem Accord Alignment [Core]  <!-- UUID: 7f550ce1-dbd5-43dc-8c03-741eb6b9df4a -->

Obex operates in full alignment with the Sky Atlas. All operations, reporting, and capital flows must comply with the standards established by Sky Governance and any applicable Ecosystem Accords.

#### A.6.1.1.5.3.2.4 - First-Loss and Recourse Principles [Core]  <!-- UUID: 909f6c00-369e-4fd1-b052-1e933a17b669 -->

Capital deployed through Obex carries explicit first-loss protection defined by the Incubator Prime. Each funded project must maintain verifiable recourse through token, equity, or revenue participation agreements enforceable by the Prime's legal wrapper.

#### A.6.1.1.5.3.2.5 - Data and Transparency Standards [Core]  <!-- UUID: c861f5fb-e99b-40ca-b535-291b94b69811 -->

Obex maintains an active dashboard reporting total allocations, active projects, utilization, default rates, and realized yields.

### A.6.1.1.5.3.3 - Ecosystem Accords [Core]  <!-- UUID: dba03405-43a8-4ce1-8a16-dfdeb75cda14 -->

Obex has formally agreed to the Ecosystem Accords herein.

#### A.6.1.1.5.3.3.1 - Ecosystem Accord 4 [Core]  <!-- UUID: eab0145b-3b7b-4793-92ff-56717d2e5544 -->

Obex engaged in terms of agreement with Sky in Ecosystem Accord 4, located in [A.2.8.2.4 - Ecosystem Accord 4: Sky And Obex](6bddc5aa-ac80-43d8-b8c8-8cde14e896df).
