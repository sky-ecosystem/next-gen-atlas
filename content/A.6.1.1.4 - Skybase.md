# A.6.1.1.4 - Skybase [Core]  <!-- UUID: c88439b5-f456-4e51-8825-42e0ba83546f -->

The documents herein specify all of the logic for Skybase, including Skybase's strategy and how it uses the Sky Primitives to operationalize this strategy.

## A.6.1.1.4.1 - Introduction [Core]  <!-- UUID: a09ca807-8649-45d0-8e80-62baeb042995 -->

Skybase is an Agent specializing in creating accessible and user-friendly DeFi interfaces. It operates the Sky.money user interface. Sky.money is a non-custodial web application serving as a gateway to the Sky Protocol. Through its AI-powered interface, Sky.money makes digital asset interactions intuitive and accessible for users of all experience levels—all while ensuring users maintain complete control of their assets. Sky.money never takes custody of users' private keys or assets; users retain full responsibility for managing their private keys and digital wallet access. Skybase also operates select key Sky websites utilizing Sky.money subdomains, such as the Sky Governance Voting Portal (vote.sky.money).

## A.6.1.1.4.2 - Sky Primitives [Core]  <!-- UUID: 614f046c-829b-4330-a462-adff2245b36d -->

The documents herein implement the Sky Primitives for Skybase. See [A.2.2 - Sky Primitives](fcde2604-a138-4c1b-9d9a-14895835c907).

### A.6.1.1.4.2.1 - Genesis Primitives [Core]  <!-- UUID: f08231e6-caa9-490d-9d7f-4f65f9076084 -->

The documents herein implement the Genesis Primitives for Skybase. See [A.2.2.5 - Genesis Primitives](3d5e3668-8333-4908-adcc-5784cfe7f6b5).

#### A.6.1.1.4.2.1.1 - Agent Creation Primitive [Core]  <!-- UUID: 301c4673-0279-49e8-9c3b-e810e8223234 -->

The documents herein contain all data and specifications for Skybase's Instance of the Agent Creation Primitive. See [A.2.2.5.1 - Agent Creation Primitive](82b95f6d-4883-4f08-ac3a-9d8189013fbe).

##### A.6.1.1.4.2.1.1.1 - Primitive Hub Document [Core]  <!-- UUID: df8efa45-85c4-4c66-b984-a5ddfc3f3522 -->

The documents herein organize all base information relevant to Skybase's usage of the Agent Creation Primitive.

###### A.6.1.1.4.2.1.1.1.1 - Global Activation Status [Core]  <!-- UUID: 487d9253-c2ac-44be-a3b4-7474ba38fddd -->

`Completed`

###### A.6.1.1.4.2.1.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 0f377ebd-60bd-45ad-9996-a2adc324e2cf -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.1.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: a36c4c17-6870-4458-8f38-7a966871b085 -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.1.1.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 385addb0-9ee7-4cc0-8fb1-22d6d229198b -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.1.1.3.1 - Single Instance Configuration Document](b53a6744-c772-47bf-9bc3-26ffb933a6d6).

###### A.6.1.1.4.2.1.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 462d376c-2f8d-497a-beb2-af3e96895733 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.4.2.1.1.1.5 - Hub Data Repository [Core]  <!-- UUID: c2ab6cb7-f482-4993-b9ba-760cf06a7730 -->

The document herein contains the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.1.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 90432b91-3439-4dee-8005-43af1cf2572a -->

The subtrees for archived Invocations and Instances of the Agent Creation Primitive are stored here.

###### A.6.1.1.4.2.1.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 0d52617d-d303-4133-9523-0638d65be070 -->

The subtrees for failed Invocations of the Agent Creation Primitive are stored here.

###### A.6.1.1.4.2.1.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: aa957ab8-fa9a-4ce0-bb47-e34350f16027 -->

The subtrees for Instances of the Agent Creation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.1.1.2 - Active Instances [Core]  <!-- UUID: 0334421f-a3a0-4016-94fd-5cb0fc026b25 -->

The Instances of the Agent Creation Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 87ad87f5-5441-4003-8029-b7ce10442119 -->

The Instances of the Agent Creation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.4.2.1.1.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: b53a6744-c772-47bf-9bc3-26ffb933a6d6 -->

The documents herein contain the Instance Configuration Document for the Single Agent Creation Primitive Instance.

###### A.6.1.1.4.2.1.1.3.1.1 - Parameters [Core]  <!-- UUID: b34cf681-4d8d-406d-997d-a805c2a9911c -->

The documents herein define the parameters of the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.4.2.1.1.3.1.1.1 - Name [Core]  <!-- UUID: 46d00c31-8877-4db8-981a-659276a86938 -->

The name of the Agent is Skybase.

###### A.6.1.1.4.2.1.1.3.1.1.2 - SubProxy Account [Core]  <!-- UUID: daed1676-6039-459e-9136-5e31617d756b -->

The address of Skybase's SubProxy Account on the Ethereum Mainnet is `0x08978E3700859E476201c1D7438B3427e3C81140`.

###### A.6.1.1.4.2.1.1.3.1.1.3 - StarGuard Contract [Core]  <!-- UUID: 9ae04b66-c6b3-492d-a37f-ae60b583ea62 -->

The address of Skybase's StarGuard contract on the Ethereum Mainnet is `0xA170086AeF9b3b81dD73897A0dF56B55e4C2a1F7`.

###### A.6.1.1.4.2.1.1.3.1.1.3.1 - StarGuard Max Delay [Core]  <!-- UUID: 26e062c6-d49e-4f49-b14e-0884d899cbe1 -->

The Skybase StarGuard `maxDelay` is seven (7) days.

###### A.6.1.1.4.2.1.1.3.1.1.4 - Genesis Account [Core]  <!-- UUID: 082cb114-b47e-4371-afe5-d7bcba70704a -->

The address of Skybase's Genesis Account will be specified in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.1.1.3.1.1.5 - Foundation [Core]  <!-- UUID: fe988ac4-6a04-46cd-89b0-c78ba8683f14 -->

The Skybase Foundation is the Prime Foundation associated with Skybase. Its mandate is to support the development, growth, and adoption of Skybase.

###### A.6.1.1.4.2.1.1.3.1.1.6 - Development Company [Core]  <!-- UUID: 095eabf8-26a4-484a-bdb7-b581799f4679 -->

Skybase's Development Company will be updated in a future iteration of the Artifact.

###### A.6.1.1.4.2.1.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: c38b8c86-828d-4d31-9ce6-0ba8d8694f1f -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.4.2.1.1.3.1.3 - Data Repository [Core]  <!-- UUID: 638682f2-1973-4c77-afc2-b745b950fbf4 -->

The documents herein contain data relevant to the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.4.2.1.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: d6d7788a-4702-4e7f-8bd0-0e1bdb535e79 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.1.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: efc466bf-6681-4c38-ac6a-281d4c1593be -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.1.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 587c4557-6622-49af-b64b-9fd48dbc85b1 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.4.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 58ddd7d7-28af-4ca3-ac6a-f5d2105f9e79 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.4.2.1.2 - Prime Transformation Primitive [Core]  <!-- UUID: 4da364d5-3b83-4858-a820-12d4980f6977 -->

The documents herein contain all data and specifications for Skybase's instance of the Prime Transformation Primitive. See [A.2.2.5.2 - Prime Transformation Primitive](81411106-fd6d-4f9c-b3ae-7af7b5e62482).

##### A.6.1.1.4.2.1.2.1 - Primitive Hub Document [Core]  <!-- UUID: f4d35d37-831f-4eee-b18f-d9a3d266655e -->

The documents herein organize all base information relevant to Skybase's usage of the Prime Transformation Primitive.

###### A.6.1.1.4.2.1.2.1.1 - Global Activation Status [Core]  <!-- UUID: 8d69ca15-79c9-4351-b185-a7cd40c4ad71 -->

`Completed`

###### A.6.1.1.4.2.1.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 190a4493-15a5-4656-9151-b0b9407e03ff -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.1.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 67062ef3-c534-4ca3-a852-db5529f7e0f4 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.1.2.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 1f0cc3ff-862b-4a44-9603-1f7368e963dc -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.1.2.3.1 - Single Instance Configuration Document](61e2585d-2ef1-43f5-af89-9f68a66dea12).

###### A.6.1.1.4.2.1.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 78abc4a4-9a0f-4ee4-b716-db593325bd34 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.4.2.1.2.1.5 - Hub Data Repository [Core]  <!-- UUID: c67c2fad-a4d9-43ce-b6a0-94ab916b8ece -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.1.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: f4a6295d-6cca-48b9-b692-03fc742e00be -->

The subtrees for archived Invocations and Instances of the Prime Transformation Primitive are stored here.

###### A.6.1.1.4.2.1.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9ae8a7b5-d386-47e1-aa51-d80c8d781cfb -->

The subtrees for failed Invocations of the Prime Transformation Primitive are stored here.

###### A.6.1.1.4.2.1.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 0eb68a5c-3785-4085-8385-b052711f903c -->

The subtrees for Instances of the Prime Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.1.2.2 - Active Instances [Core]  <!-- UUID: e8a80c86-33b0-4c9e-9331-5916e9355b28 -->

The Instances of the Prime Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.1.2.3 - Completed Instances [Core]  <!-- UUID: 2bd4f3c4-9d79-4acf-afa9-7fbb2160ef58 -->

The Instances of the Prime Transformation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.4.2.1.2.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 61e2585d-2ef1-43f5-af89-9f68a66dea12 -->

The documents herein contain the Instance Configuration Document for the Single Prime Transformation Primitive Instance.

###### A.6.1.1.4.2.1.2.3.1.1 - Parameters [Core]  <!-- UUID: 2d442b0e-6f55-4a41-9599-e494a4da5cc1 -->

The documents herein define the parameters of the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.4.2.1.2.3.1.1.1 - Agent Type [Core]  <!-- UUID: afa9a16f-e776-40f1-8e34-923ae661517a -->

Skybase is a Prime Agent.

###### A.6.1.1.4.2.1.2.3.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: de857100-9b4b-4fcd-942c-a3b67a5f9a45 -->

The documents herein define the custom parameters of the Single Instance of the Prime Transformation Primitive, if any.

###### A.6.1.1.4.2.1.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: d8eca741-b371-4e0a-b2f5-f10663683efa -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.4.2.1.2.3.1.3 - Data Repository [Core]  <!-- UUID: 6f45d32b-f377-480c-b67f-a1d7b2d09ba8 -->

The documents herein contain data relevant to the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.4.2.1.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: 70203ad1-71b6-4a80-97a4-d18227cd736e -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.1.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 84e3ba93-7ba4-4f52-b54e-5ea6e73da623 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.1.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 102b2492-34f9-4f2f-8f42-593aa8871129 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.4.2.1.2.4 - In Progress Invocations [Core]  <!-- UUID: 42f47668-ba50-430e-ac11-245eef79e712 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.4.2.1.3 - Executor Transformation Primitive [Core]  <!-- UUID: 4e2edd9e-61c2-4be1-8cb3-f2be5e1587f3 -->

The documents herein contain all data and specifications for Skybase's instance of the Executor Transformation Primitive. See [A.2.2.5.3 - Executor Transformation Primitive](2f249be5-8edb-41e4-b429-734e1ba2cbc7).

##### A.6.1.1.4.2.1.3.1 - Primitive Hub Document [Core]  <!-- UUID: f60f5f5f-3aa8-49de-85fb-95841bb73bdb -->

The documents herein organize all base information relevant to Skybase's usage of the Executor Transformation Primitive.

###### A.6.1.1.4.2.1.3.1.1 - Global Activation Status [Core]  <!-- UUID: b1246162-614d-42b8-b648-474ba79b22aa -->

`Inactive`

###### A.6.1.1.4.2.1.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 33335844-6cd7-4135-9134-bc1ebbd06690 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.1.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: dddd885e-2600-4947-8c0a-8082e4121753 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.1.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 09e544ef-8565-49d2-8dd6-e1b0aa53cb21 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.4.2.1.3.1.5 - Hub Data Repository [Core]  <!-- UUID: fecb494b-fbc2-467d-88df-df2a8a0e0786 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.1.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 838893af-76a9-4d49-94d4-51f7e82fa537 -->

The subtrees for archived Invocations and Instances of the Executor Transformation Primitive are stored here.

###### A.6.1.1.4.2.1.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 4f338613-eee5-40c7-bcb4-7dd32e81008d -->

The subtrees for failed Invocations of the Executor Transformation Primitive are stored here.

###### A.6.1.1.4.2.1.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: e526b717-2105-41c5-9686-4387d7ef3b24 -->

The subtrees for Instances of the Executor Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.1.3.2 - Active Instances [Core]  <!-- UUID: 661072a0-b9cd-4ac9-b1d0-cc0f5626dd6d -->

The Instances of the Executor Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.1.3.3 - Completed Instances [Core]  <!-- UUID: 08f562a1-4694-45a4-91b8-008876a413ff -->

The Instances of the Executor Transformation Primitive with `Completed` Status are contained herein.

##### A.6.1.1.4.2.1.3.4 - In Progress Invocations [Core]  <!-- UUID: 3218078d-249f-4d41-ae72-c53ac02ab033 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.4.2.1.4 - Agent Token Primitive [Core]  <!-- UUID: a4708a14-1030-4935-a4a5-103826d9d4a5 -->

The documents herein contain all data and specifications for Skybase's Instance of the Agent Token Primitive. See [A.2.2.5.4 - Agent Token Primitive](2047c361-db28-4952-a70c-83d07b562064).

##### A.6.1.1.4.2.1.4.1 - Primitive Hub Document [Core]  <!-- UUID: ffa68419-fc61-4b60-a4d5-7c1ca4aace6d -->

The documents herein organize all base information relevant to Skybase's usage of the Agent Token Primitive.

###### A.6.1.1.4.2.1.4.1.1 - Global Activation Status [Core]  <!-- UUID: 3ac79f75-348c-4329-ba78-53b4882662cc -->

`Active`

###### A.6.1.1.4.2.1.4.1.2 - Active Instances Directory [Core]  <!-- UUID: e1785e8c-71e2-4646-867d-bcca3e4704a7 -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.1.4.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 5402a5c2-0b48-4ebd-9689-ab990578a72c -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.1.4.2.1 - Single Instance Configuration Document](6e4d6787-4bd7-485f-b378-6dc83dc860cc).

###### A.6.1.1.4.2.1.4.1.3 - Completed Instances Directory [Core]  <!-- UUID: 42ff09a3-7286-419f-a64c-fd69e480300b -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.1.4.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: f6b2bff2-c924-45f9-ae70-32e25fd621fc -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.4.2.1.4.1.5 - Hub Data Repository [Core]  <!-- UUID: 4e57c90f-df6f-41e6-ba60-129e515967b5 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.1.4.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: feb8e6d3-298d-4f4f-ba31-1113cc2a9e24 -->

The subtrees for archived Invocations and Instances of the Agent Token Primitive are stored here.

###### A.6.1.1.4.2.1.4.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: fa96fe93-4825-4d52-9050-05e922e44682 -->

The subtrees for failed Invocations of the Agent Token Primitive are stored here.

###### A.6.1.1.4.2.1.4.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 4fa6c164-ab33-49c3-9a94-d044d6a9e551 -->

The subtrees for Instances of the Agent Token Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.1.4.2 - Active Instances [Core]  <!-- UUID: 67fce1f3-961f-479c-b0f9-ccb03a260b83 -->

The Instances of the Agent Token Primitive with `Active` Status are stored herein.

###### A.6.1.1.4.2.1.4.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 6e4d6787-4bd7-485f-b378-6dc83dc860cc -->

The documents herein contain the Instance Configuration Document for the Single Agent Token Primitive Instance.

###### A.6.1.1.4.2.1.4.2.1.1 - Parameters [Core]  <!-- UUID: 50b46486-6b4c-494a-90dc-e077e77564eb -->

The documents herein define the parameters of the Single Instance of the Agent Token Primitive.

###### A.6.1.1.4.2.1.4.2.1.1.1 - Token Name [Core]  <!-- UUID: 1b5f18b6-ca5f-4c2a-be90-a8e270643e9b -->

The name of Skybase's token is Skybase.

###### A.6.1.1.4.2.1.4.2.1.1.2 - Token Symbol [Core]  <!-- UUID: 8eb04812-6fe7-43dc-a461-afa09b992cc8 -->

The symbol of Skybase's token is SKYBASE.

###### A.6.1.1.4.2.1.4.2.1.1.3 - Genesis Supply [Core]  <!-- UUID: bc80a5e5-4ef7-4255-9e97-848c9cbbeb36 -->

The Genesis Supply of SKYBASE will be specified in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.1.4.2.1.1.4 - Token Address [Core]  <!-- UUID: b2270863-75e9-42f6-8c25-749a0f83dcb5 -->

The address of SKYBASE will be specified in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.1.4.2.1.1.5 - Token Admin [Core]  <!-- UUID: 1f692794-fc64-4cf8-86a7-fabc865eb428 -->

The token Admin will be specified in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.1.4.2.1.1.6 - Token Emissions [Core]  <!-- UUID: f56670f9-5a43-4b47-b94a-99026f8d87c0 -->

Token emissions beyond the Genesis Supply are permanently disabled; this cannot be reverted by Skybase Governance. Sky Governance retains the ability to revert where Skybase is in violation of Risk Capital requirements and emissions are required by the Risk Framework. See [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.6.1.1.4.2.1.4.2.1.1.7 - Custom Instance Parameters [Core]  <!-- UUID: 65437b13-60b3-4e22-ab0c-c6e5b29756a0 -->

The documents herein define the custom parameters of the Single Instance of the Agent Token Primitive, if any.

###### A.6.1.1.4.2.1.4.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 652b94ef-66e3-40fe-ba80-4ce5c3d27f03 -->

The documents herein define the operational processes for minting and initial distribution of the tokens from the Genesis Supply.

- These processes will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.1.4.2.1.3 - Data Repository [Core]  <!-- UUID: 5f286327-f846-432a-98d5-31b8ecff7a8c -->

The documents herein contain data relevant to the Single Instance of the Agent Token Primitive.

###### A.6.1.1.4.2.1.4.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 05259bea-0f5e-4afc-8279-fbd98516d7ac -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.1.4.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: b146e772-2d00-456b-8ba7-536ea733c34a -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.1.4.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: a66316d6-e4be-4ff5-b894-4c8fa3d1285c -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.4.2.1.4.3 - Completed Instances [Core]  <!-- UUID: ba6be9cd-0812-4098-89f3-2e813948a3f8 -->

The Instances of the Agent Token Primitive with `Completed` Status are contained herein.

##### A.6.1.1.4.2.1.4.4 - In Progress Invocations [Core]  <!-- UUID: 24237950-dcfc-4ca7-932f-c808bc521a10 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

### A.6.1.1.4.2.2 - Operational Primitives [Core]  <!-- UUID: b0336f9e-09fd-415f-a86d-57220811dc80 -->

The documents herein implement the Operational Primitives for Skybase. See [A.2.2.6 - Operational Primitives](0192ec95-9207-480e-8c51-88d2a1da95ad).

#### A.6.1.1.4.2.2.1 - Executor Accord Primitive [Core]  <!-- UUID: bb6c188b-ae69-4573-8104-44f9577427a1 -->

The documents herein contain all data and specifications for Skybase's Instances of the Executor Accord Primitive. See [A.2.2.6.1 - Executor Accord Primitive](88017877-3ec1-4c43-a035-6bebdf11d9bb).

##### A.6.1.1.4.2.2.1.1 - Primitive Hub Document [Core]  <!-- UUID: 8f799c9e-618c-407f-a4a1-899f32d13d52 -->

The documents herein organize all base information relevant to Skybase's usage of the Executor Accord Primitive.

###### A.6.1.1.4.2.2.1.1.1 - Global Activation Status [Core]  <!-- UUID: 3018b2d6-65e3-41af-90ae-f4275e862e13 -->

`Active`

###### A.6.1.1.4.2.2.1.1.2 - Active Instances Directory [Core]  <!-- UUID: d9493bdc-074e-4a87-af74-5e7826b541be -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.2.1.1.2.1 - Ozone Instance Configuration Document Location [Core]  <!-- UUID: e396aca8-3823-452e-8bdd-21b0e0e54083 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.2.1.2.1 - Ozone Instance Configuration Document](ff142a80-adb5-49da-87d8-62aabdb36b10).

###### A.6.1.1.4.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: f1f78b17-7c65-4d8c-9066-315c25ed8f2d -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 9b42623e-e6fb-4c18-a291-d5ed18634e39 -->

This document contains a Directory of all prospective Instances of the Executor Accord Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.2.1.1.2 - Active Instances Directory](d9493bdc-074e-4a87-af74-5e7826b541be), whereas failed Invocations are Archived in [A.6.1.1.4.2.2.1.1.5 - Hub Data Repository](c2daebbe-e96d-4201-a5df-725b9ef64780).

###### A.6.1.1.4.2.2.1.1.5 - Hub Data Repository [Core]  <!-- UUID: c2daebbe-e96d-4201-a5df-725b9ef64780 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.2.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 3d2a4d73-e717-4276-a608-13a92cd5b33c -->

The subtrees for archived Invocations and Instances of the Executor Accord Primitive are stored here.

###### A.6.1.1.4.2.2.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 85735314-b04b-48f5-b5cd-f1c9f8ff3614 -->

The subtrees for failed Invocations of the Executor Accord Primitive are stored here.

###### A.6.1.1.4.2.2.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 2250b3d8-6d7f-4454-80a7-3a2beba3cb37 -->

The subtrees for Instances of the Executor Accord Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.2.1.2 - Active Instances [Core]  <!-- UUID: 830ba0df-d50e-4d8f-bef4-a8febf06d276 -->

The Instances of the Executor Accord Primitive with `Active` Status are stored herein.

###### A.6.1.1.4.2.2.1.2.1 - Ozone Instance Configuration Document [Core]  <!-- UUID: ff142a80-adb5-49da-87d8-62aabdb36b10 -->

The documents herein contain the Instance Configuration Document for the Ozone Executor Accord Primitive Instance.

###### A.6.1.1.4.2.2.1.2.1.1 - Parameters [Core]  <!-- UUID: cdcae493-a9b6-4b08-8b03-6f4c7c76eb25 -->

The documents herein define the parameters of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.4.2.2.1.2.1.1.1 - Operational Executor Agent [Core]  <!-- UUID: 82200234-6b7c-4299-a552-66ceac3be5e6 -->

The Operational Facilitator and Operational GovOps for Ozone are specified in [A.6.1.2.2 - Operational Executor Agent Ozone](565660dd-7850-4c3a-8dba-554542bf103a).

###### A.6.1.1.4.2.2.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 822596a6-882f-416f-bc13-4986b1bf4052 -->

The documents herein define the custom parameters of the Ozone Instance of the Executor Accord Primitive, if any.

###### A.6.1.1.4.2.2.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 27e3f4f9-6433-4cd5-b4db-7f67b3fb6cdf -->

The documents herein define the process for the ongoing management of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.4.2.2.1.2.1.3 - Data Repository [Core]  <!-- UUID: 5120e81d-c44f-47ec-a19a-dff5d4abf152 -->

The documents herein contain data relevant to the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.4.2.2.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 0f2d0ae7-1aa7-4692-9f36-dd00b119885e -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.2.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 0bb80f80-c2c0-43f1-8783-b2a2bdbcc09b -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.2.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 659ad2e7-f1af-4bd4-b5c1-8624ba7f169e -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.4.2.2.1.3 - Completed Instances [Core]  <!-- UUID: 03bf33b4-f74d-4b40-a1a0-e34e19b30318 -->

The Instances of the Executor Accord Primitive with `Completed` Status are stored herein.

##### A.6.1.1.4.2.2.1.4 - In Progress Invocations [Core]  <!-- UUID: a25a57e2-64b9-4e78-89d6-c2d68b388348 -->

The in progress Invocations of the Executor Accord Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.2.1.2 - Active Instances](830ba0df-d50e-4d8f-bef4-a8febf06d276).

#### A.6.1.1.4.2.2.2 - Root Edit Primitive [Core]  <!-- UUID: 24517c43-dec9-44ec-bc03-e76671dc2e74 -->

The documents herein contain all data and specifications for Skybase's Instance of the Root Edit Primitive. See [A.2.2.6.2 - Root Edit Primitive](78488c6b-d77f-4344-b954-476e415a2c7d).

##### A.6.1.1.4.2.2.2.1 - Primitive Hub Document [Core]  <!-- UUID: 787f01b6-0503-49aa-8dd1-f08ad222a5c9 -->

The documents herein organize all base information relevant to Skybase's usage of the Root Edit Primitive.

###### A.6.1.1.4.2.2.2.1.1 - Global Activation Status [Core]  <!-- UUID: a70572a2-e643-49a1-afa2-3b25c5118c92 -->

`Active`

###### A.6.1.1.4.2.2.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 0a03859b-466d-43bf-905d-fd6410fecc19 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.2.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 318fedce-fb39-450e-986a-4e0886b33dc5 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.2.2.2.1 - Single Instance Configuration Document](5c13949f-831a-4574-8942-ceaa4da11b9d).

###### A.6.1.1.4.2.2.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: e5d7b405-1839-472b-8b3d-fd30818e17fb -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.2.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: b754f376-5aef-4631-bf68-fb34dc02ac62 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.4.2.2.2.1.5 - Hub Data Repository [Core]  <!-- UUID: e2d6993d-f8e2-4e39-9e30-6693eddb5643 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.2.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 7af6212a-d0e0-4148-8d06-f825a97289ec -->

The subtrees for archived Invocations and Instances of the Root Edit Primitive are stored here.

###### A.6.1.1.4.2.2.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9ac66a16-2aa3-4909-bf50-168e118bb5ba -->

The subtrees for failed Invocations of the Root Edit Primitive are stored here.

###### A.6.1.1.4.2.2.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 19493456-a088-49db-b65a-34ce5928b750 -->

The subtrees for Instances of the Root Edit Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.2.2.2 - Active Instances [Core]  <!-- UUID: ab9a8ca8-5bcf-4846-8740-12ea03ee8158 -->

The Instances of the Root Edit Primitive with `Active` Status are stored herein.

###### A.6.1.1.4.2.2.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 5c13949f-831a-4574-8942-ceaa4da11b9d -->

The documents herein contain the Instance Configuration Document for the Single Root Edit Primitive Instance.

###### A.6.1.1.4.2.2.2.2.1.1 - Parameters [Core]  <!-- UUID: 9d5d586e-1840-49f3-9716-20d661f023ce -->

The parameters of the Root Edit Primitive are fully specified by the Operational Process Definition in [A.6.1.1.4.2.2.2.2.1.2 - Operational Process Definition](010ed495-c693-4d27-8c18-aa24b64e2715).

###### A.6.1.1.4.2.2.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 010ed495-c693-4d27-8c18-aa24b64e2715 -->

The documents herein define the process for using the Root Edit Primitive to update the Skybase Agent Artifact. Information on Skybase governance that is unrelated to the use of the Root Edit Primitive is located at [A.6.1.1.4.3.1 - Governance Information Unrelated To Root Edit Primitive](70804058-8a1b-45ee-bf21-b09a5daefdb9).

###### A.6.1.1.4.2.2.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 759db362-3e1b-4ee8-b07e-9c61f7818154 -->

The documents herein define the process for using the Root Edit Primitive to update the Skybase Agent Artifact in routine or normal conditions (i.e., non-emergency situations).

###### A.6.1.1.4.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission [Core]  <!-- UUID: f57f157c-c260-4671-8150-01acabcd286d -->

The Root Edit process begins with a SKYBASE token holder submitting a proposal through the Powerhouse system containing a draft Artifact Edit Proposal. A SKYBASE token holder must hold at least 1% of the circulating token supply to submit a proposal. The proposal must also be posted on the Sky Forum under the "Skybase Prime" category.

###### A.6.1.1.4.2.2.2.2.1.2.1.1.1 - Root Edit Proposal Submission Requirements Exception [Core]  <!-- UUID: 502d08e5-d705-4443-bb71-f29580847d74 -->

For proposals that solely entail a buyback or a grant of SKYBASE tokens, the requirement that SKYBASE token holders must hold at least 1% of the circulating token supply to submit a proposal is waived. However, all other procedural requirements within the Root Edit process continue to apply.

###### A.6.1.1.4.2.2.2.2.1.2.1.1.2 - Short-Term Transitionary Measures [Core]  <!-- UUID: f88fc097-7e41-41d7-aac9-992a9a11919f -->

Until the Powerhouse system supports submitting Artifact Edit Proposals, SKYBASE token holders may submit Artifact Edit Proposals by posting them to the Sky Forum under the "Skybase Prime" category. The title of the post must include the text "Skybase Artifact Edit Proposal". The post must include cryptographic proof that the author controls an account holding the required percentage of the total SKYBASE token supply specified in [A.6.1.1.4.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](f57f157c-c260-4671-8150-01acabcd286d).

###### A.6.1.1.4.2.2.2.2.1.2.1.2 - Root Edit Expert Advisor Review [Core]  <!-- UUID: 451079fe-fd11-4fef-ae51-6cb533a644c5 -->

A future iteration of the Skybase Artifact will specify guidelines for obtaining specialized review of proposals requiring advanced technical or financial analysis.

###### A.6.1.1.4.2.2.2.2.1.2.1.3 - Root Edit Proposal Review By Operational Facilitator [Core]  <!-- UUID: 76b51e97-ff82-4f52-8c24-7b75d629bb4a -->

Within seven (7) days of the proposal being submitted, the Operational Facilitator must review the Root Edit Proposal for alignment.

If the proposal is aligned, the Operational Facilitator must respond to the Forum post to announce their finding. In this Forum post, the Operational Facilitator must also confirm that the proposal is feasible for Operational GovOps to operationalize.

If the proposal is misaligned, the Operational Facilitator must respond to the Forum post to announce their finding and provide the reasoning for it.

###### A.6.1.1.4.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote [Core]  <!-- UUID: 836b9942-8fdf-46df-bf38-f5adf87eb390 -->

Where their review of the proposal results in a finding of alignment with the Sky Core Atlas and Skybase Artifact, the Operational Facilitator next triggers a Snapshot poll to allow token holders to vote on the proposal. The poll is open for three (3) days. A poll must have at least 10% of the circulating token supply participating and must have more than 50% of votes cast, excluding abstentions, in favor to be approved.

###### A.6.1.1.4.2.2.2.2.1.2.1.5 - Root Edit Artifact Update [Core]  <!-- UUID: b91f0f85-680d-4eeb-9a2e-7e0e245e4c6d -->

At the conclusion of the poll, if the proposal is approved, the Operational Facilitator submits the edit to Powerhouse to formally update the Agent Artifact. Regardless of the outcome, the Operational Facilitator updates the Powerhouse System to include the result of the vote, including any pertinent documents.

###### A.6.1.1.4.2.2.2.2.1.2.1.5.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: 1adf5e90-53a8-4036-9964-11430891137e -->

Until the Powerhouse system supports updating Agent Artifacts, the Operational Facilitator works with the Core Facilitator to update the Atlas GitHub repository located at [https://github.com/sky-ecosystem/next-gen-atlas/pulls](https://github.com/sky-ecosystem/next-gen-atlas/pulls) to reflect proposals approved by Prime Governance.

###### A.6.1.1.4.2.2.2.2.1.2.1.6 - Artifact Edit Restrictions [Core]  <!-- UUID: f3e8ecec-cb08-4682-9218-d13f567fc00e -->

The Skybase Artifact cannot be edited in any way that violates the Sky Core Atlas or its specifications of the Sky Primitives, or in any way that is otherwise misaligned. The Operational Facilitator must enforce this rule through their review of Artifact Edit Proposals.

###### A.6.1.1.4.2.2.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: e5477d87-ecc4-4eab-9e11-fe8d76791048 -->

The documents herein define the process for using the Root Edit Primitive to update the Skybase Agent Artifact in non-routine conditions.

###### A.6.1.1.4.2.2.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 368ff139-9c2c-4b41-955e-e374996ad274 -->

The documents herein define the process for using the Root Edit Primitive to update the Skybase Agent Artifact in urgent or emergency situations.

###### A.6.1.1.4.2.2.2.2.1.2.3.1 - Root Edit Voting Process in Urgent and Emergency Situations [Core]  <!-- UUID: 5edc65d7-8023-4c03-b399-958c5f8869ff -->

In an Urgent or Emergency Situation, as defined by the Sky Core Atlas in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225), the Operational Facilitator may allow a Root Edit to occur more quickly than the timeline specified above. Where feasible, the Operational Facilitator should announce the decision to deploy the emergency Root Edit protocol and provide their reasoning via a public Sky Forum post (under the "Skybase Prime" category), unless doing so would endanger Skybase or its users.

###### A.6.1.1.4.2.2.2.2.1.3 - Data Repository [Core]  <!-- UUID: 6f533a79-4263-4b1b-9d47-9ab9e670f0f0 -->

The documents herein contain data relevant to the Single Instance of the Root Edit Primitive.

###### A.6.1.1.4.2.2.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 112386b9-0c60-4224-8d39-a43b2805f351 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.2.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: d9ebdf09-8d8e-4b14-a3f3-08a0d7579e92 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.2.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 91159367-dcf2-4c55-ae77-0ca91da4fb91 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.4.2.2.2.3 - Completed Instances [Core]  <!-- UUID: 6840069f-a930-42ad-8fad-8224876da285 -->

The Instances of the Root Edit Primitive with `Completed` Status are contained herein.

##### A.6.1.1.4.2.2.2.4 - In Progress Invocations [Core]  <!-- UUID: 492351ef-6e00-450c-8689-e7dd0c171a55 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.4.2.2.3 - Light Agent Primitive [Core]  <!-- UUID: ceb79469-e43e-4640-9507-5d1d4eaea3cb -->

The documents herein contain all data and specifications for Skybase's Instances of the Light Agent Primitive. See [A.2.2.6.3 - Light Agent Primitive](44028423-2cd1-40cb-89ac-3f762b602b90).

##### A.6.1.1.4.2.2.3.1 - Primitive Hub Document [Core]  <!-- UUID: 04e7dd63-49ab-42dd-b195-1e309d7295c9 -->

The documents herein organize all base information relevant to Skybase's usage of the Light Agent Primitive.

###### A.6.1.1.4.2.2.3.1.1 - Global Activation Status [Core]  <!-- UUID: 1db03594-b529-4330-a4d9-536178be4303 -->

`Inactive`

###### A.6.1.1.4.2.2.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 66f80060-6404-4cde-8059-ee8f220f952b -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.2.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7802509b-d232-4e04-b658-1f34621112a0 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.2.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 8f764154-a5d2-4cd6-ba54-537dbe785f6c -->

This document contains a Directory of all prospective Instances of the Light Agent Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.2.3.1.2 - Active Instances Directory](66f80060-6404-4cde-8059-ee8f220f952b), whereas failed Invocations are Archived in [A.6.1.1.4.2.2.3.1.5 - Hub Data Repository](7561a59b-425a-405d-ba35-1892a282dd2b).

###### A.6.1.1.4.2.2.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 7561a59b-425a-405d-ba35-1892a282dd2b -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.2.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 52ce096b-fba4-40ef-9164-a5ec944c59ad -->

The subtrees for archived Invocations and Instances of the Light Agent Primitive are stored here.

###### A.6.1.1.4.2.2.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 4bfb3a1c-ac80-4a42-8760-0e83dd562fed -->

The subtrees for failed Invocations of the Light Agent Primitive are stored here.

###### A.6.1.1.4.2.2.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 5c197fb1-5da3-414e-aa18-17eaf2f1701f -->

The subtrees for Instances of the Light Agent Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.2.3.2 - Active Instances [Core]  <!-- UUID: 1a09ba55-2b66-40e7-83d0-7ff144d2575b -->

The Instances of the Light Agent Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.2.3.3 - Completed Instances [Core]  <!-- UUID: 2546a8ae-ca91-4190-96e3-b06f160d073c -->

The Instances of the Light Agent Primitive with `Completed` Status are contained herein.

##### A.6.1.1.4.2.2.3.4 - In Progress Invocations [Core]  <!-- UUID: fe73fbe5-570b-4388-8934-ab6605d89dd5 -->

The in progress Invocations of the Light Agent Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.2.3.2 - Active Instances](1a09ba55-2b66-40e7-83d0-7ff144d2575b).

### A.6.1.1.4.2.3 - Ecosystem Upkeep Primitives [Core]  <!-- UUID: 833c1933-d81e-4653-af2c-aa03aac70883 -->

The documents herein implement the Ecosystem Upkeep Primitives for Skybase. See [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

#### A.6.1.1.4.2.3.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: c6ef4a5c-d6f4-42d6-8800-6b7a40e64f50 -->

The documents herein contain all data and specifications for Skybase's Instance of the Ecosystem Upkeep Fee Primitive. See [A.2.2.7.1 - Ecosystem Upkeep Fee Primitive](a21616f4-1611-4e0b-87b2-efbdff9f6f28).

##### A.6.1.1.4.2.3.1.1 - Primitive Hub Document [Core]  <!-- UUID: 9beebf8b-dfd4-40b4-8de1-f5a3f4a60824 -->

The documents herein organize all base information relevant to Skybase's usage of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.4.2.3.1.1.1 - Global Activation Status [Core]  <!-- UUID: dbb03eb2-d193-4193-93c7-1d874b9995f3 -->

`Active`

###### A.6.1.1.4.2.3.1.1.2 - Active Instances Directory [Core]  <!-- UUID: a5e68fe6-a420-4960-ac74-b02c01366315 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.3.1.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: c0ea44a4-98d9-427c-a570-6f94574bbf94 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.3.1.2.1 - Single Instance Configuration Document](2426a22f-8760-412f-bf21-e69c72787a9b).

###### A.6.1.1.4.2.3.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: f2c07b3e-d18d-4443-8b73-386a2d5c370b -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.3.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: cf55b39f-204e-49b0-82fd-df87a22fd23f -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.4.2.3.1.1.5 - Hub Data Repository [Core]  <!-- UUID: cc9f3e40-bcec-49c9-a0ff-5d204c40b890 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.3.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 9bd4f238-f94c-4532-8001-c80d3f74febf -->

The subtrees for archived Invocations and Instances of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.4.2.3.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 250cba14-19c6-4211-af5b-33f0b78cc3f8 -->

The subtrees for failed Invocations of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.4.2.3.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 2118c398-b73f-401a-b71f-55d1fca06b29 -->

The subtrees for Instances of the Ecosystem Upkeep Fee Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.3.1.2 - Active Instances [Core]  <!-- UUID: 4359d5d0-a404-4004-8cff-d552338df2f0 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Active` Status are stored herein.

###### A.6.1.1.4.2.3.1.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 2426a22f-8760-412f-bf21-e69c72787a9b -->

The documents herein contain the Instance Configuration Document for the Single Ecosystem Upkeep Fee Primitive Instance.

###### A.6.1.1.4.2.3.1.2.1.1 - Parameters [Core]  <!-- UUID: 734f47d3-adf3-46a0-972c-f8d37a8d009e -->

The documents herein define the parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.4.2.3.1.2.1.1.1 - Terms [Core]  <!-- UUID: 69b65ee6-746a-4d78-8d60-ec40ca2bb6b4 -->

Skybase will pay 0.50% of its market capitalization per year in USDS.

###### A.6.1.1.4.2.3.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 61232bcd-4510-4ed1-8ede-14d744329c27 -->

The documents herein define the custom parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive, if any.

###### A.6.1.1.4.2.3.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 8c10d49d-6238-4cdb-b62e-32bb080b7b0b -->

The documents herein define the process for the ongoing management of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.4.2.3.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 6ca26507-85f1-4169-a2a2-156046847257 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.4.2.3.1.2.1.2.1.1 - Process Definition For Upkeep Fee Payment [Core]  <!-- UUID: e2db4ada-d8af-4481-963b-8ed8adfbd18d -->

The process to pay 0.50% of Skybase's market capitalization per year in USDS will be specified in future iterations of the Skybase Artifact.

###### A.6.1.1.4.2.3.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: df35e2e9-116d-4a1c-95d7-1e4b8acdd1c3 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.4.2.3.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 85815a3a-08b9-4917-b8a5-6c87f5dcd391 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.4.2.3.1.2.1.3 - Data Repository [Core]  <!-- UUID: 26c81439-ed26-4d69-bd32-cc486058fb6f -->

The documents herein contain data relevant to the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.4.2.3.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 1285deb9-39ff-400c-a82c-2ec2e7b4d216 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.3.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: db3e6b81-f383-4269-8cab-e94e47abc891 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.3.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: e877196c-33d9-48dd-b188-fe5c70c68d00 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.4.2.3.1.3 - Completed Instances [Core]  <!-- UUID: ce66e2db-bbb6-4f33-9b3b-cc3b913f6459 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Completed` Status are stored herein.

##### A.6.1.1.4.2.3.1.4 - In Progress Invocations [Core]  <!-- UUID: c67cbd36-a096-41fb-a210-8547a733a724 -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.4.2.3.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: dec47cc6-dce7-4256-bd23-6b659ae8bc25 -->

The documents herein contain all data and specifications for Skybase's instance of the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

##### A.6.1.1.4.2.3.2.1 - Primitive Hub Document [Core]  <!-- UUID: 6952060d-f1dd-4d86-b2f8-f07090174d1d -->

The documents herein organize all base information relevant to Skybase's usage of the Upkeep Rebate Primitive.

###### A.6.1.1.4.2.3.2.1.1 - Global Activation Status [Core]  <!-- UUID: aec5c887-c2d2-43ee-b00e-e77716b7bb30 -->

`Active`

###### A.6.1.1.4.2.3.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 89236086-3786-47bb-8b97-6a0ee5013c46 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.3.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 1fe328fd-2a73-45ea-b80a-f5ce76728ae1 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.3.2.2.1 - Single Instance Configuration Document](f1ecc666-e14f-4828-977b-b24be78b1825).

###### A.6.1.1.4.2.3.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 883dcda6-bd15-4c39-9229-b0252e9556f8 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.3.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 16c7d73e-df4d-401a-b8c7-aa5fe7df23f2 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.4.2.3.2.1.5 - Hub Data Repository [Core]  <!-- UUID: dd6c0fe7-480e-492c-b24b-287ebde1fdfe -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.3.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: d9c92153-6411-4b40-9871-615e408cf738 -->

The subtrees for archived Invocations and Instances of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.4.2.3.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: ceb96633-4d3f-4818-bebb-e99243b7b061 -->

The subtrees for failed Invocations of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.4.2.3.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 793bcfab-0f87-4c09-b4f5-0f131075604b -->

The subtrees for Instances of the Upkeep Rebate Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.3.2.2 - Active Instances [Core]  <!-- UUID: 6c2bb4eb-e052-4cb8-a249-d65201b4828e -->

The Instances of the Upkeep Rebate Primitive with `Active` Status are stored herein.

###### A.6.1.1.4.2.3.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: f1ecc666-e14f-4828-977b-b24be78b1825 -->

The documents herein contain the Instance Configuration Document for the Single Upkeep Rebate Primitive Instance.

###### A.6.1.1.4.2.3.2.2.1.1 - Parameters [Core]  <!-- UUID: 0e8a5c2f-ef1b-4c4f-aa4a-ed1659d80663 -->

Every Prime Agent is entitled to the Upkeep Rebate Primitive for tokens of other Prime Agents that they hold. Because this right automatically applies, there are no parameters.

###### A.6.1.1.4.2.3.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: b7be1c16-a7e1-4d22-a697-d30cd1d2bb86 -->

The documents herein define the process for the ongoing management of the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.4.2.3.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 717bb9de-7df5-4fec-8e59-d5d7fde0ac7d -->

This document defines the protocol for routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.4.2.3.2.2.1.2.1.1 - Skybase Holds Tokens Of Other Agents In Its SubProxy Account [Core]  <!-- UUID: 0d37e672-8a82-433c-a5c7-f88ff248cb6a -->

Skybase keeps all tokens of other Agents it holds in its SubProxy account.

###### A.6.1.1.4.2.3.2.2.1.2.1.2 - Skybase Deducts Rebate From Ecosystem Upkeep Fees [Core]  <!-- UUID: d2a0b2dd-353f-46b1-ae2c-1791ce2a0b77 -->

When paying Ecosystem Upkeep fees, Skybase deducts the rebate from the fees it pays.

###### A.6.1.1.4.2.3.2.2.1.2.1.3 - Operational GovOps Reviews Rebate [Core]  <!-- UUID: 911e4409-146c-49e6-9f5c-5abdc58d97d3 -->

Operational GovOps reviews Skybase's calculation of the rebate before executing a return of surplus to token holders. In the event of any issues, Operational GovOps cannot execute the distribution. If Operational GovOps does not execute the distribution, Operational GovOps must post an explanation on the Sky Forum under the "Skybase Prime" category and work with Skybase to resolve the disagreement. If Operational GovOps and Skybase cannot resolve the disagreement, it must be escalated to Core GovOps.

###### A.6.1.1.4.2.3.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 299fa3a2-ce38-4697-b876-faaa5e5ca3a9 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.4.2.3.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: c9eac99e-4444-478a-a0bf-cc5139413bf0 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.4.2.3.2.2.1.3 - Data Repository [Core]  <!-- UUID: 2bc4f7e9-e9a2-465e-b6da-1032ce4a6f42 -->

The documents herein contain data relevant to the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.4.2.3.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: a7718626-05e0-4c62-86ae-62ff9f2fc785 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.3.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 0e9c8eb9-ab4e-4240-9ea9-a2c810ea3698 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.3.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 89f2904b-d250-4643-a84a-083b54a572e0 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.4.2.3.2.3 - Completed Instances [Core]  <!-- UUID: aff0590c-e76d-4734-a139-ef7a67d9a619 -->

The Instances of the Upkeep Rebate Primitive with `Completed` Status are contained herein.

##### A.6.1.1.4.2.3.2.4 - In Progress Invocations [Core]  <!-- UUID: 986814bc-13cc-4e9d-b1ba-f664863ad05e -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

### A.6.1.1.4.2.4 - SkyLink Primitives [Core]  <!-- UUID: 23b316a2-8a07-4295-808f-f787fea871de -->

The documents herein implement the SkyLink Primitives for Skybase. See [A.2.2.8 - SkyLink Primitives](7b5d8965-a64c-4c44-b742-607f51f69d8f).

#### A.6.1.1.4.2.4.1 - Token SkyLink Primitive [Core]  <!-- UUID: ddeb2ecf-ea5c-4087-a44d-0a69de3033f7 -->

The documents herein contain all data and specifications for Skybase's Instances of the Token SkyLink Primitive. See [A.2.2.8.1 - Token SkyLink Primitive](4504d2d4-ee45-4a07-8c5b-9baf20b12e76).

##### A.6.1.1.4.2.4.1.1 - Primitive Hub Document [Core]  <!-- UUID: 052c7deb-75d9-4be2-aa45-cb3a59d14bd5 -->

The documents herein organize all base information relevant to Skybase's usage of the Token SkyLink Primitive.

###### A.6.1.1.4.2.4.1.1.1 - Global Activation Status [Core]  <!-- UUID: e8c65465-9db4-48a7-be8e-5e9616779056 -->

`Inactive`

###### A.6.1.1.4.2.4.1.1.2 - Active Instances Directory [Core]  <!-- UUID: a5aa1884-66a2-4fd0-b35d-f4291f0726f7 -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.4.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 7f0e42ad-c54c-4023-9055-57288d0eeb3f -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.4.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 75c0efb2-0428-4764-9bfd-fdccca850048 -->

This document contains a Directory of all prospective Instances of the Token SkyLink Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.4.1.1.2 - Active Instances Directory](a5aa1884-66a2-4fd0-b35d-f4291f0726f7), whereas failed Invocations are Archived in [A.6.1.1.4.2.4.1.1.5 - Hub Data Repository](1707675b-308e-4ac1-8e29-129b76ed430d).

###### A.6.1.1.4.2.4.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 1707675b-308e-4ac1-8e29-129b76ed430d -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.4.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 18356d1b-545d-4819-a71e-b6d4e8c1ef81 -->

The subtrees for archived Invocations and Instances of the Token SkyLink Primitive are stored here.

###### A.6.1.1.4.2.4.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: a168df08-8c61-4b31-a05b-2a36a3abf2ed -->

The subtrees for failed Invocations of the Token SkyLink Primitive are stored here.

###### A.6.1.1.4.2.4.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: cd2f777f-1c0b-4d1d-a603-ecc6ae1cd0e8 -->

The subtrees for Instances of the Token SkyLink Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.4.1.2 - Active Instances [Core]  <!-- UUID: e9afe0ee-b765-49e0-9268-636b386c8733 -->

The Instances of the Token SkyLink Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.4.1.3 - Completed Instances [Core]  <!-- UUID: a8e875d3-39f8-4040-a6f3-fe411e6d5d4e -->

The Instances of the Token SkyLink Primitive with `Completed` Status are stored herein.

##### A.6.1.1.4.2.4.1.4 - In Progress Invocations [Core]  <!-- UUID: 6947125b-804c-45a1-a730-9f1acc9daa13 -->

The in progress Invocations of the Token SkyLink Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.4.1.2 - Active Instances](e9afe0ee-b765-49e0-9268-636b386c8733).

### A.6.1.1.4.2.5 - Demand Side Stablecoin Primitives [Core]  <!-- UUID: 6a390014-e5c9-4656-bdf8-587264a141cd -->

The documents herein implement the Demand Side Stablecoin Primitives for Skybase. See [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d).

#### A.6.1.1.4.2.5.1 - Distribution Reward Primitive [Core]  <!-- UUID: d8e61fc3-18a2-4952-8e5b-43cfb94b0bab -->

The documents herein contain all data and specifications for Skybase's instances of the Distribution Reward Primitive. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

##### A.6.1.1.4.2.5.1.1 - Primitive Hub Document [Core]  <!-- UUID: 10b6c6e8-edee-4a77-a6c4-bbb05db8b364 -->

The documents herein organize all base information relevant to Skybase's usage of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.1.1 - Global Activation Status [Core]  <!-- UUID: 03230dbb-8896-40b3-b5c3-d3c4ee729606 -->

`Active`

###### A.6.1.1.4.2.5.1.1.2 - Active Instances Directory [Core]  <!-- UUID: c6275b51-9ee0-49df-a4ea-33a24cd2c752 -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.5.1.1.2.1 - Sky.money App Instance Configuration Document Location [Core]  <!-- UUID: ab7ff4b8-7e62-4a36-8573-581c86293e50 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.2.1 - Sky.money App Instance Configuration Document](b52f88c6-427b-45f6-8e1c-81fa27e522c8).

###### A.6.1.1.4.2.5.1.1.2.2 - Sky.money Open Source Widgets Instance Configuration Document Location [Core]  <!-- UUID: 43fbf9b3-7cf6-46f3-a900-c3ef9d193d02 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.2.2 - Sky.money Open Source Widgets Instance Configuration Document](5aada153-29f6-4304-b56e-9d425dc978a4).

###### A.6.1.1.4.2.5.1.1.2.3 - DeFi Saver Instance Configuration Document Location [Core]  <!-- UUID: a8442e7e-67ee-43a2-b0b6-6e18db4bbb41 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.2.3 - DeFi Saver Instance Configuration Document](9907bb75-f389-42bb-8fe4-e03ff3039c46).

###### A.6.1.1.4.2.5.1.1.2.4 - CoW Swap Instance Configuration Document Location [Core]  <!-- UUID: 5341fdbc-78fc-4e15-8b06-d446a3dac8d8 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.2.4 - CoW Swap Instance Configuration Document](80f22d64-0ccf-4bb2-8da4-d170a95d2161).

###### A.6.1.1.4.2.5.1.1.2.5 - ParaSwap Instance Configuration Document Location [Core]  <!-- UUID: ecc841f1-0bd8-4453-b97d-33a05fbbafba -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.2.5 - ParaSwap Instance Configuration Document](d3f7f0e6-b912-4464-be3f-20b0c600bcfa).

###### A.6.1.1.4.2.5.1.1.2.6 - Yearn (Gimme) Instance Configuration Document Location [Core]  <!-- UUID: a1e42939-5c28-4e1c-8940-150f979b4e47 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.2.6 - Yearn (Gimme) Instance Configuration Document](f36ce752-38d1-4dd4-8a51-dd18f2151756).

###### A.6.1.1.4.2.5.1.1.2.7 - MOM Instance Configuration Document Location [Core]  <!-- UUID: c2fccf99-2f21-42df-bfea-e857110d386e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.2.7 - MOM Instance Configuration Document](ee4f9b64-aeb7-4813-b187-996e8172fea1).

###### A.6.1.1.4.2.5.1.1.2.8 - Lazy Summer Protocol Instance Configuration Document Location [Core]  <!-- UUID: 802c6126-3283-4311-b67f-a05003f7e6bf -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.2.8 - Lazy Summer Protocol Instance Configuration Document](74db9986-5277-4c5f-8e27-f6a312ed591f).

###### A.6.1.1.4.2.5.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 3c43db85-3995-4c95-a85c-e72786a28501 -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.5.1.1.3.1 - Summer.fi Instance Configuration Document Location [Core]  <!-- UUID: 0e6a80cb-041c-4dc1-a22b-91fda88ecd92 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.1.3.1 - Summer.fi Instance Configuration Document](fd9c7ace-e72c-4ffb-a74e-7106a0dde80b).

###### A.6.1.1.4.2.5.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 95beed80-4199-4c08-82bd-0ae7827c98b0 -->

This document contains a Directory of all prospective Instances of the Distribution Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.5.1.1.2 - Active Instances Directory](c6275b51-9ee0-49df-a4ea-33a24cd2c752),; whereas failed Invocations are Archived in [A.6.1.1.4.2.5.1.1.5 - Hub Data Repository](86d7913a-b8d0-42a8-a6b7-02c190e74373).

###### A.6.1.1.4.2.5.1.1.4.1 - MetaMask [Core]  <!-- UUID: 91c685ab-75fb-4bd4-ad68-b9a26afc1962 -->

The Invocation Status and Instance Configuration Document location of this prospective Instance are specified below:

Invocation Status: `Planning`

Instance Configuration Document Location: [A.6.1.1.4.2.5.1.4.1 - MetaMask Instance Configuration Document](d43ec3dd-96bf-419f-8387-f85615e6bcc5).

###### A.6.1.1.4.2.5.1.1.4.2 - InstaDapp [Core]  <!-- UUID: 915e98d4-8cec-4598-8906-d9cff11ac5aa -->

The Invocation Status and Instance Configuration Document location of this prospective Instance are specified below:

Invocation Status: `Planning`
Instance Configuration Document Location: [A.6.1.1.4.2.5.1.4.2 - InstaDapp Instance Configuration Document](e870392a-2552-41ca-a148-4be47d34bac7).

###### A.6.1.1.4.2.5.1.1.4.3 - Gnosis Protocol [Core]  <!-- UUID: d901f747-bd11-4359-b7d3-05752098586e -->

The Invocation Status and Instance Configuration Document location of this prospective Instance are specified below:

Invocation Status: `Planning`
Instance Configuration Document Location: [A.6.1.1.4.2.5.1.4.3 - Gnosis Protocol Instance Configuration Document](34cde6e0-89a1-44a4-9ce1-58873b83c63b).

###### A.6.1.1.4.2.5.1.1.4.4 - Piku.co [Core]  <!-- UUID: befc9c75-0263-443d-b662-fe667a645d79 -->

The Invocation Status and Instance Configuration Document location of this prospective Instance are specified below:

Invocation Status: `Planning`
Instance Configuration Document Location: [A.6.1.1.4.2.5.1.4.4 - Piku.co Instance Configuration Document](bc145261-ff5d-4937-abbd-0719390ff124).

###### A.6.1.1.4.2.5.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 86d7913a-b8d0-42a8-a6b7-02c190e74373 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.5.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: d2f66b3d-7903-47e7-8f71-3aaa79407c20 -->

The subtrees for archived Invocations and Instances of the Distribution Reward Primitive are stored here.

###### A.6.1.1.4.2.5.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9e28ce11-cd68-4c1a-b872-eae49dc4887e -->

The subtrees for failed Invocations of the Distribution Reward Primitive are stored here.

###### A.6.1.1.4.2.5.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 6e3010db-596c-478b-9aed-8fb4222a53d1 -->

The subtrees for Instances of the Distribution Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.5.1.2 - Active Instances [Core]  <!-- UUID: cb0709e4-c51d-45cc-b385-0c20a0bf4b25 -->

The Instances of the Distribution Reward Primitive with `Active` Status are stored herein.

###### A.6.1.1.4.2.5.1.2.1 - Sky.money App Instance Configuration Document [Core]  <!-- UUID: b52f88c6-427b-45f6-8e1c-81fa27e522c8 -->

The documents herein contain the Instance Configuration Document for the Sky.money App Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.2.1.1 - Parameters [Core]  <!-- UUID: 5455497f-bfb3-49a0-a788-0b7db4da799b -->

The documents herein define the parameters of the Sky.money App Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.1.1.1 - Reward Code [Core]  <!-- UUID: fcff71ae-93ff-49f7-aa39-a97077a921c6 -->

`1`.

###### A.6.1.1.4.2.5.1.2.1.1.2 - Tracking Methodology [Core]  <!-- UUID: f79a1c05-b4f7-4b11-b9be-1e4f7d72f34f -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.4.2.5.1.2.1.1.3 - Custom Instance Parameters [Core]  <!-- UUID: e5ff6cc4-c1d2-4184-a266-010104a6a28f -->

The documents herein define the custom parameters of the Sky.money App Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: cb266ef8-782b-4bef-af06-be12b727b280 -->

The documents herein define the process for the ongoing management of the Sky.money App Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: bd3b25ac-90b8-49f0-ac29-bb51a2290820 -->

This document defines the protocol for routine ongoing management of the Sky.money App Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.2.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: b803a685-e88f-48d9-92e9-7e9e3c574b36 -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: eff49ccd-5874-41d9-aff0-3e3e2a348336 -->

The documents herein define the protocol for non-routine ongoing management of the Sky.money App Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: d7296a92-3a38-42c3-938c-5327725b0fbb -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Sky.money App Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.1.3 - Data Repository [Core]  <!-- UUID: 4ef496cf-201e-4a98-9f7e-e61ad7eebfd6 -->

The documents herein contain data relevant to the Sky.money App Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: c4fead38-31dc-4a6a-8d98-5f28b1a46f7a -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 919d7b43-51e1-4d53-93c6-ff84a633542b -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 8bb175ef-0165-417c-9222-f4ed8df23b3f -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.1.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 8ece0051-0eee-427f-b2ea-1abfd52b80cd -->

The Distribution Reward payments for the Sky.money App Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.1.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 09282f1f-f4fa-40b6-9073-6adc42f31569 -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.2.2 - Sky.money Open Source Widgets Instance Configuration Document [Core]  <!-- UUID: 5aada153-29f6-4304-b56e-9d425dc978a4 -->

The documents herein contain the Instance Configuration Document for the Sky.money Open Source Widgets Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.2.2.1 - Parameters [Core]  <!-- UUID: 159c7e99-c884-4496-aa9b-b7721be4849a -->

The documents herein define the parameters of the Sky.money Open Source Widgets Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.2.1.1 - Reward Code [Core]  <!-- UUID: 9a774d02-8882-4363-87b9-2efebc8142f8 -->

`0`.

###### A.6.1.1.4.2.5.1.2.2.1.2 - Tracking Methodology [Core]  <!-- UUID: 31579503-9b6d-408e-ad44-28cf411c22f5 -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.4.2.5.1.2.2.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 79e22741-ef2b-4b8e-b97c-acead4550deb -->

The documents herein define the custom parameters of the Sky.money Open Source Widgets Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.2.2.2 - Operational Process Definition [Core]  <!-- UUID: 4f94c1ee-d908-412a-b4c9-2f59e5bd4e67 -->

The documents herein define the process for the ongoing management of the Sky.money Open Source Widgets Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.2.2.1 - Routine Protocol [Core]  <!-- UUID: 461e8506-cc90-4c8d-9927-153ee996c432 -->

This document defines the protocol for routine ongoing management of the Sky.money Frontend Open Source Widgets Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.2.2.2.1.1 - Agent Customizations [Core]  <!-- UUID: 5524ef1f-2b23-457a-b1fc-89773f56a7f3 -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.2.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 2ff3ed8b-6466-4a3d-87e0-040fb8940859 -->

The documents herein define the protocol for non-routine ongoing management of the Sky.money Open Source Widgets Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.2.2.3 - Emergency Protocol [Core]  <!-- UUID: 45f2cc2c-e96d-455f-808e-e188e5aece34 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Sky.money Open Source Widgets Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.2.3 - Data Repository [Core]  <!-- UUID: b198cdd7-92c2-4ff5-9f10-b0d315ed5f00 -->

The documents herein contain data relevant to the Sky.money Open Source Widgets Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.2.3.1 - Initial Planning [Core]  <!-- UUID: 8578558a-5bd3-4256-a8f6-0e14da879257 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.2.3.2 - Operational GovOps Review [Core]  <!-- UUID: f3de12e6-9ca6-4969-95a4-50b6c6b928b3 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.2.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 09c5171b-5fe5-4a37-ad78-0e4be7b4c0f9 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.2.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: d96439a8-df0d-4ba9-973e-896fac953fad -->

The Distribution Reward payments for the Sky.money Open Source Widgets Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.2.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: ad573b24-befc-49f9-be30-6c65f8986c61 -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.2.3 - DeFi Saver Instance Configuration Document [Core]  <!-- UUID: 9907bb75-f389-42bb-8fe4-e03ff3039c46 -->

The documents herein contain the Instance Configuration Document for the DeFi Saver Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.2.3.1 - Parameters [Core]  <!-- UUID: a7b36acb-01b2-42a3-8014-d567a82ab81e -->

The documents herein define the parameters of the DeFi Saver Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.3.1.1 - Reward Code [Core]  <!-- UUID: b8b563d3-7b0c-4a35-adb7-4c6f120c7f26 -->

`1002`.

###### A.6.1.1.4.2.5.1.2.3.1.2 - Tracking Methodology [Core]  <!-- UUID: be4e3d61-e28e-48d9-bc04-413ee57859ad -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.4.2.5.1.2.3.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 613151ab-cddd-426e-b4b4-4a7a659efd0c -->

The documents herein define the custom parameters of the DeFi Saver Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.2.3.2 - Operational Process Definition [Core]  <!-- UUID: 352fd637-e23d-4598-998f-a1949f006002 -->

The documents herein define the process for the ongoing management of the DeFi Saver Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.3.2.1 - Routine Protocol [Core]  <!-- UUID: 2e0cdaa7-5d3a-42c2-808d-220c4823c0e2 -->

This document defines the protocol for routine ongoing management of the DeFi Saver Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.2.3.2.1.1 - Agent Customizations [Core]  <!-- UUID: 9cef88a9-952f-460b-92c3-d6bb90974972 -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.2.3.2.2 - Non-Routine Protocol [Core]  <!-- UUID: a1f81f47-953d-4fde-8406-48ef1f4bf55a -->

The documents herein define the protocol for non-routine ongoing management of the DeFi Saver Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.3.2.3 - Emergency Protocol [Core]  <!-- UUID: 8a8a1d60-594e-4042-8252-612d9603dab4 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the DeFi Saver Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.3.3 - Data Repository [Core]  <!-- UUID: 7b55a0f5-cd48-4a95-a637-6cbf10a66ec5 -->

The documents herein contain data relevant to the DeFi Saver Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.3.3.1 - Initial Planning [Core]  <!-- UUID: 3117ffa8-81bb-4fc3-ab15-2e2a41de26fa -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.3.3.2 - Operational GovOps Review [Core]  <!-- UUID: e4cdcd58-9f16-4efe-9671-a0b667267004 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.3.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 63a206b3-3bae-4c14-ac3c-e658b912b238 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.3.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 0f9d7876-d376-4f85-840d-c3cbb96872d3 -->

The Distribution Reward payments for the DeFi Saver Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.3.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 731c96eb-57a2-434c-852c-2c7f461efb46 -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.2.3.3.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: e2a262ce-e59a-421c-ab32-803fe41802c4 -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.3.3.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: 8fc2657e-fb6b-4d43-988c-6f47b71052f1 -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.2.3.3.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: da35cd2c-4113-4656-a5f5-5b804b5f894f -->

DeFi Saver - `0x6467e807dB1E71B9Ef04E0E3aFb962E4B0900B2B`

###### A.6.1.1.4.2.5.1.2.4 - CoW Swap Instance Configuration Document [Core]  <!-- UUID: 80f22d64-0ccf-4bb2-8da4-d170a95d2161 -->

The documents herein contain the Instance Configuration Document for the CoW Swap Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.2.4.1 - Parameters [Core]  <!-- UUID: 014a4af6-2df3-47fe-b0e4-c1238f3ce18b -->

The documents herein define the parameters of the CoW Swap Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.4.1.1 - Reward Code [Core]  <!-- UUID: 3df72746-229c-4b32-bafa-802df1b04401 -->

`1003`.

###### A.6.1.1.4.2.5.1.2.4.1.2 - Tracking Methodology [Core]  <!-- UUID: fc6cd905-6f53-4e3a-9ac8-14ca46fef6af -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.2 - Ethereum Mainnet CoW Swap Tracking Methodology](1b5cc0ee-0ee8-467e-ab49-33c06ad417dc). Specifically, on-chain Settlement Events on the CoW Swap settlement contract ([https://etherscan.io/address/0x9008D19f58AAbD9eD0D60971565AA8510560ab41](https://etherscan.io/address/0x9008D19f58AAbD9eD0D60971565AA8510560ab41)) are checked for where they coincide perfectly with USDS deposit transactions into sUSDS.

###### A.6.1.1.4.2.5.1.2.4.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 947cf303-80e9-4b9f-9403-a9634d876d76 -->

The documents herein define the custom parameters of the CoW Swap Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.2.4.2 - Operational Process Definition [Core]  <!-- UUID: 6c37960a-a6e0-44af-b2fd-148853d0655f -->

The documents herein define the process for the ongoing management of the CoW Swap Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.4.2.1 - Routine Protocol [Core]  <!-- UUID: c6e84f25-85fe-412e-808a-235e713d4ec2 -->

This document defines the protocol for routine ongoing management of the CoW Swap Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.2.4.2.1.1 - Agent Customizations [Core]  <!-- UUID: 1d1a2365-7cf2-409e-9637-5d7f9e6c0752 -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.2.4.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 8f48dd88-d114-4c6f-9b01-a8c7468808b8 -->

The documents herein define the protocol for non-routine ongoing management of the CoW Swap Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.4.2.3 - Emergency Protocol [Core]  <!-- UUID: 61d2a0ea-09d1-4ad3-a668-66ebd5593c2f -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the CoW Swap Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.4.3 - Data Repository [Core]  <!-- UUID: 67188304-6a6e-421a-92b9-bf995cd49e49 -->

The documents herein contain data relevant to the CoW Swap Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.4.3.1 - Initial Planning [Core]  <!-- UUID: d0dcbfc1-826f-4f68-ac22-f356f2b3d3f4 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.4.3.2 - Operational GovOps Review [Core]  <!-- UUID: 7b5a94d3-1bdd-4b06-823e-c31199717e29 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.4.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 4a803925-4c83-44a8-9530-4b0f30b6d928 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.4.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: dc323489-6f9b-4f0d-a5c6-3c74729cef7c -->

The Distribution Reward payments for the CoW Swap Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.4.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 655886dc-7ca2-45cd-be2c-7be8421961c7 -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.2.4.3.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: 84df5c1e-86b7-431d-bb0e-8708f99a572e -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.4.3.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: 88f6d49f-9473-46c2-a030-d3f74f2d1377 -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.2.4.3.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: 910f8a42-b56c-4617-890a-d135b196b168 -->

CoW Swap - `0x616dE58c011F8736fa20c7Ae5352F7f6FB9F0669`

###### A.6.1.1.4.2.5.1.2.5 - ParaSwap Instance Configuration Document [Core]  <!-- UUID: d3f7f0e6-b912-4464-be3f-20b0c600bcfa -->

The documents herein contain the Instance Configuration Document for the ParaSwap Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.2.5.1 - Parameters [Core]  <!-- UUID: 0dbc09fd-557b-4434-a3ac-2ac66da6acb4 -->

The documents herein define the parameters of the ParaSwap Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.5.1.1 - Reward Code [Core]  <!-- UUID: 6940bdf3-78db-4565-8195-1c2fea444c8a -->

`1004`.

###### A.6.1.1.4.2.5.1.2.5.1.2 - Tracking Methodology [Core]  <!-- UUID: df5554b7-1b06-43bb-a112-4768192a73cf -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.4.2.5.1.2.5.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 78a7d271-f5d2-4692-8831-7bf98ea754ac -->

The documents herein define the custom parameters of the ParaSwap Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.2.5.2 - Operational Process Definition [Core]  <!-- UUID: 576943c0-8301-4372-bc8d-4620cf94bb05 -->

The documents herein define the process for the ongoing management of the ParaSwap Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.5.2.1 - Routine Protocol [Core]  <!-- UUID: bf955649-4ac2-45e2-8376-052e884698e4 -->

This document defines the protocol for routine ongoing management of the ParaSwap Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.2.5.2.1.1 - Agent Customizations [Core]  <!-- UUID: 200fb6db-3425-4bf5-adde-b9d3bcff412d -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.2.5.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 0d81e6c2-4586-4aa1-9a1b-c8ce66a05fd1 -->

The documents herein define the protocol for non-routine ongoing management of the ParaSwap Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.5.2.3 - Emergency Protocol [Core]  <!-- UUID: b5583385-2432-40f3-a110-6790c7520754 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the ParaSwap Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.5.3 - Data Repository [Core]  <!-- UUID: 4a18e7da-c6b5-4850-825d-9e7aaf406795 -->

The documents herein contain data relevant to the ParaSwap Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.5.3.1 - Initial Planning [Core]  <!-- UUID: 32dfe611-a223-40af-9100-70688fa0f162 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.5.3.2 - Operational GovOps Review [Core]  <!-- UUID: 20e0c61c-70c8-4d68-b90e-ce664ca5097a -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.5.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 993a4e87-14d0-4d98-9477-446d4bbbfe12 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.5.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 3ea87681-b351-462c-b375-6fb60c817755 -->

The Distribution Reward payments for the ParaSwap Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.5.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 4588c98b-1c51-4f8c-8cc5-baab631950ef -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.2.5.3.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: 81bafe53-8c66-43ec-82fd-5848b9d64555 -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.5.3.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: 3306dbf8-6c7c-4cfe-b98d-08105282272e -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.2.5.3.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: 8088e4e4-a594-448c-a3cb-752b907b4f3c -->

The payment address of this Third Party Partner will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.2.6 - Yearn (Gimme) Instance Configuration Document [Core]  <!-- UUID: f36ce752-38d1-4dd4-8a51-dd18f2151756 -->

The documents herein contain the Instance Configuration Document for the Yearn (Gimme) Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.2.6.1 - Parameters [Core]  <!-- UUID: 49866e74-c131-4e4d-9165-325bba89cd48 -->

The documents herein define the parameters of the Yearn (Gimme) Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.6.1.1 - Reward Code [Core]  <!-- UUID: 30bcc1e7-0c26-4e67-b823-1fd1203c7370 -->

`1007`.

###### A.6.1.1.4.2.5.1.2.6.1.2 - Tracking Methodology [Core]  <!-- UUID: 43ede046-4e45-4bf8-895b-d5823965eeae -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.4.2.5.1.2.6.1.3 - Custom Instance Parameters [Core]  <!-- UUID: f1a4510d-f38c-499c-bc07-405a8ca6816d -->

The documents herein define the custom parameters of the Yearn (Gimme) Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.2.6.2 - Operational Process Definition [Core]  <!-- UUID: a3796610-b310-4dac-872b-21ce3bd835e7 -->

The documents herein define the process for the ongoing management of the Yearn (Gimme) Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.6.2.1 - Routine Protocol [Core]  <!-- UUID: 1c93fd6d-5cff-46e7-86e5-0af4f6c83b4b -->

This document defines the protocol for routine ongoing management of the Yearn (Gimme) Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.2.6.2.1.1 - Agent Customizations [Core]  <!-- UUID: d341791b-eec0-46a8-ada5-f6142ff49034 -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.2.6.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 8998657a-ed5e-4610-b1bc-171f715a5d48 -->

The documents herein define the protocol for non-routine ongoing management of the Yearn (Gimme) Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.6.2.3 - Emergency Protocol [Core]  <!-- UUID: 8146f803-ddf9-4f85-81d3-84666b3f259c -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Yearn (Gimme) Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.6.3 - Data Repository [Core]  <!-- UUID: e2cf9382-81d0-4f38-a9bc-8b7c647805fb -->

The documents herein contain data relevant to the Yearn (Gimme) Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.6.3.1 - Initial Planning [Core]  <!-- UUID: 2a400f84-7251-41ed-a8ce-c3d091c90ad6 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.6.3.2 - Operational GovOps Review [Core]  <!-- UUID: 3bdf7ecb-accd-4b70-b956-a5e05cb60668 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.6.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 1816152b-22ea-4a5a-822f-88da78afe8cf -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.6.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 30be45d8-cd38-4c52-b4d0-ed7225c97b9a -->

The Distribution Reward payments for the Yearn (Gimme) Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.6.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 707956cc-62f8-4620-a95f-b45ebf263218 -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.2.6.3.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: 690e54dd-c88a-422e-a06d-e6812035fc1c -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.6.3.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: 034c4a3d-46fc-46b4-afd0-1187bc29ea07 -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.2.6.3.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: be1b9146-9d66-4ab1-a47d-724d0220f5ef -->

Yearn (Gimme) - `0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52`

###### A.6.1.1.4.2.5.1.2.7 - MOM Instance Configuration Document [Core]  <!-- UUID: ee4f9b64-aeb7-4813-b187-996e8172fea1 -->

The documents herein contain the Instance Configuration Document for the MOM Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.2.7.1 - Parameters [Core]  <!-- UUID: 8adfffaf-011e-4762-9b44-3e35f0f6adaa -->

The documents herein define the parameters of the MOM Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.7.1.1 - Reward Code [Core]  <!-- UUID: d87d51bb-8476-48b7-a8af-795917bb6f0d -->

`1015`.

###### A.6.1.1.4.2.5.1.2.7.1.2 - Tracking Methodology [Core]  <!-- UUID: 0ed5b976-e929-4a38-9f45-6eda54d4cc6c -->

This Instance uses the Tracking Methodologies specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2) and [A.2.2.9.1.2.1.1.2.3 - Base Tracking Methodology](f710bddf-dc1d-483c-9503-483574cb6333).

###### A.6.1.1.4.2.5.1.2.7.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 4c40a025-6ff0-4ee7-9a33-d4c03b68f332 -->

The documents herein define the custom parameters of the MOM Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.2.7.2 - Operational Process Definition [Core]  <!-- UUID: 3c170bd2-4a9e-4461-bf81-d33fd253dfc9 -->

The documents herein define the process for the ongoing management of the MOM Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.7.2.1 - Routine Protocol [Core]  <!-- UUID: 4b22e820-db7b-4f76-8b82-6f60b21ca1d9 -->

This document defines the protocol for routine ongoing management of the MOM Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.2.7.2.1.1 - Agent Customizations [Core]  <!-- UUID: 9bbe0d8a-a65b-4da4-bdd0-8206c564f090 -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.2.7.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 940153fc-b44e-4421-82de-2d196fe1b505 -->

The documents herein define the protocol for non-routine ongoing management of the MOM Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.7.2.3 - Emergency Protocol [Core]  <!-- UUID: 0d0e6b23-5f44-4f0f-98a1-a4c82780c3d7 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the MOM Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.7.3 - Data Repository [Core]  <!-- UUID: 6c8b1217-db6e-4952-bccf-a5635a3a0119 -->

The documents herein contain data relevant to the MOM Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.7.3.1 - Initial Planning [Core]  <!-- UUID: bea56b80-5d46-4a44-81a5-0df050a5255b -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.7.3.2 - Operational GovOps Review [Core]  <!-- UUID: 16f6bff2-ed77-4e02-806d-5fe7941f94ce -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.7.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: df961d91-acfd-45de-8fd6-f17237d34eb8 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.7.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: e1961614-467f-40b0-9e7a-f67e2a70cc97 -->

The Distribution Reward payments for the MOM Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.7.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 8520b41b-cf03-493b-a6ce-9314983f38b3 -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.2.7.3.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: 74b0e9af-0a6d-4cfc-988a-5621713772fc -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.2.7.3.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: fc1a5e0b-0909-48d1-adc4-77e51a900050 -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.2.7.3.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: 4fc18aff-0fd6-41ea-a5e8-92ea54861c99 -->

The payment address of this Third Party Partner will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.2.8 - Lazy Summer Protocol Instance Configuration Document [Core]  <!-- UUID: 74db9986-5277-4c5f-8e27-f6a312ed591f -->

The documents herein contain the Instance Configuration Document for the Lazy Summer Protocol Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.2.8.1 - Parameters [Core]  <!-- UUID: be044103-09bc-410d-872a-1dfefc9410aa -->

The documents herein define the parameters of the Lazy Summer Protocol Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.8.1.1 - Reward Code [Core]  <!-- UUID: a6caf2b3-a62d-495f-a580-1f962df1f994 -->

`1016`.

###### A.6.1.1.4.2.5.1.2.8.1.2 - Tracking Methodology [Core]  <!-- UUID: 02b3a96e-2b37-4cd5-ace8-1849b1ce4840 -->

This parameter will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.2.8.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 73767654-3011-447b-9232-9e46cd6755aa -->

The documents herein define the custom parameters of the Lazy Summer Protocol Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.2.8.2 - Operational Process Definition [Core]  <!-- UUID: d9308330-b4c2-4b7a-9416-3363dc334089 -->

The documents herein define the process for the ongoing management of the Lazy Summer Protocol Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.8.2.1 - Routine Protocol [Core]  <!-- UUID: 4a7215e4-f78e-4a44-9935-d5f18463cb3d -->

This document defines the protocol for routine ongoing management of the Lazy Summer Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.2.8.2.1.1 - Agent Customizations [Core]  <!-- UUID: 65d8cd24-5a71-40b7-8f37-8bd6f07de068 -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.2.8.2.2 - Non-Routine Protocol [Core]  <!-- UUID: f6a4b979-13e6-48da-a53c-aef0b06f657b -->

The documents herein define the protocol for non-routine ongoing management of the Lazy Summer Protocol Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.8.2.3 - Emergency Protocol [Core]  <!-- UUID: d607f30d-740a-4988-834a-e0d3522d1972 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Lazy Summer Protocol Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.8.3 - Data Repository [Core]  <!-- UUID: d6312bd7-c098-4fdd-99b8-a84cee98f64f -->

The documents herein contain data relevant to the Lazy Summer Protocol Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.2.8.3.1 - Initial Planning [Core]  <!-- UUID: 85861627-db6d-4be3-8057-8aff18035130 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.8.3.2 - Operational GovOps Review [Core]  <!-- UUID: 97a92e00-3f0e-481c-ab18-c3ceb1105d42 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.8.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: cd44d715-d147-42b9-b84b-9a8d370ca6bf -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.2.8.3.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 42349b55-1334-478b-bddd-d692e55e07b9 -->

The Distribution Reward payments for the Lazy Summer Protocol Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for `Direct Edit`.

###### A.6.1.1.4.2.5.1.2.8.3.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 928ecae3-ee6f-4961-bae0-90dbf42b3b4d -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.2.8.3.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: 04d4fea9-cc1e-4275-af1a-27f8c9b15d0b -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for `Direct Edit`.

###### A.6.1.1.4.2.5.1.2.8.3.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: 0b55dd49-4787-4895-be75-091f9c2689f3 -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.2.8.3.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: 08771b54-8577-44ee-9edb-1915c0f6f050 -->

The payment address of this Third Party Partner will be defined in a future iteration of the Skybase Artifact.

##### A.6.1.1.4.2.5.1.3 - Completed Instances [Core]  <!-- UUID: 44389e6f-b48e-4426-a6c8-110ec76ebea1 -->

The Instances of the Distribution Reward Primitive with `Completed` Status are stored herein.

###### A.6.1.1.4.2.5.1.3.1 - Summer.fi Instance Configuration Document [Core]  <!-- UUID: fd9c7ace-e72c-4ffb-a74e-7106a0dde80b -->

The documents herein contain the Instance Configuration Document for the Summer.fi Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.3.1.1 - Parameters [Core]  <!-- UUID: a2cbe867-bc51-4a3c-82b6-d921e2b0a4fc -->

The documents herein define the parameters of the Summer.fi Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.3.1.1.1 - Reward Code [Core]  <!-- UUID: 1e8b16e7-b10e-4da7-936d-5cffbac57571 -->

`1001`.

###### A.6.1.1.4.2.5.1.3.1.1.2 - Tracking Methodology [Core]  <!-- UUID: 8abb90c2-c62d-4dbd-96b5-d4e447a3bc4d -->

This Instance uses the Tracking Methodology specified in [A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology](87fd6861-ba8a-4bde-945e-ee9ad37ae3e2).

###### A.6.1.1.4.2.5.1.3.1.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 80314c99-0e54-4449-88a0-828e86da92c5 -->

The documents herein define the custom parameters of the Summer.fi Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 7d73baad-0128-460d-b3b3-6b18ba86e755 -->

The documents herein define the process for the ongoing management of the Summer.fi Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.3.1.2.1 - Routine Protocol [Core]  <!-- UUID: de64fb0f-e867-495f-9e43-c197072e1c3d -->

This document defines the protocol for routine ongoing management of the Summer.fi Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.3.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: 216473d9-6f63-45ff-aa7b-a6bec64dd6dc -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.3.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 47306338-2f28-4c95-b0d3-843744e04165 -->

The documents herein define the protocol for non-routine ongoing management of the Summer.fi Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.3.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 41233dc2-c7d4-4cd4-9e23-cebbbbfaa9ce -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Summer.fi Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.3.1.3 - Data Repository [Core]  <!-- UUID: 72bc2ff0-df12-4156-8300-5c6a09badccf -->

The documents herein contain data relevant to the Summer.fi Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.3.1.3.1 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 7cc02e97-e849-4f19-81bc-2fc85ccd2361 -->

The Distribution Reward payments for the Summer.fi Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.3.1.3.1.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 289e8b48-d1ae-43d0-a9a5-b66672caacde -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.3.1.3.2 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: 73fc6f80-ac05-423f-ac58-e22dbfa8de3f -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.3.1.3.2.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: 1b25a9fd-1bb0-4425-b9a1-372f737d3a45 -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.3.1.3.2.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: cc82491d-cabb-42dd-a63a-4b3c23ee55f0 -->

Summer.fi - `0xC7b548AD9Cf38721810246C079b2d8083aba8909`

###### A.6.1.1.4.2.5.1.3.1.3.3 - Initial Planning [Core]  <!-- UUID: dabb169a-e7d5-44c2-9ed8-f0936aa9c22a -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.3.1.3.4 - Operational GovOps Review [Core]  <!-- UUID: cc50de8e-ac63-4254-bb24-8a4247b8d2b5 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.3.1.3.5 - Artifact Edit Proposal [Core]  <!-- UUID: bff7bad8-b9c9-4fb7-ae9c-08137f427f36 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.4.2.5.1.4 - In Progress Invocations [Core]  <!-- UUID: 05362fab-8fc5-487c-af2e-b6ebf6f4445e -->

The in progress Invocations of the Distribution Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.5.1.2 - Active Instances](cb0709e4-c51d-45cc-b385-0c20a0bf4b25).

###### A.6.1.1.4.2.5.1.4.1 - MetaMask Instance Configuration Document [Core]  <!-- UUID: d43ec3dd-96bf-419f-8387-f85615e6bcc5 -->

The documents herein contain the Instance Configuration Document for the MetaMask Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.4.1.1 - Invocation Status [Core]  <!-- UUID: 650a20a0-362c-431b-bd56-ef13386c3aec -->

`Planning`

###### A.6.1.1.4.2.5.1.4.1.2 - Parameters [Core]  <!-- UUID: f46ff617-d495-402f-a3dc-f4822a018b19 -->

The documents herein define the parameters of the MetaMask Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.1.2.1 - Reward Code [Core]  <!-- UUID: c3f4fb9f-9af6-495d-8261-04bd19c8c552 -->

`1005`.

###### A.6.1.1.4.2.5.1.4.1.2.2 - Tracking Methodology [Core]  <!-- UUID: 98906b92-72db-4f7e-ac79-053a92728025 -->

This parameter will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.4.1.2.3 - Custom Instance Parameters [Core]  <!-- UUID: fc5ec9c3-fad3-455d-8cb8-8be082ea388e -->

The documents herein define the custom parameters of the MetaMask Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.4.1.3 - Operational Process Definition [Core]  <!-- UUID: 81e97a1c-9bf1-4038-be0e-4eece0a2f88b -->

The documents herein define the process for the ongoing management of the MetaMask Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.1.3.1 - Routine Protocol [Core]  <!-- UUID: 02c6ffc8-5fdc-4a1f-8037-a6a1aeb5e51c -->

This document defines the protocol for routine ongoing management of the MetaMask Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.4.1.3.1.1 - Agent Customizations [Core]  <!-- UUID: e739cfa7-90c6-49f2-9b03-ea4744e7f2e9 -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.4.1.3.2 - Non-Routine Protocol [Core]  <!-- UUID: 167f2753-e45f-4d55-b182-2c17c4f1e2c5 -->

The documents herein define the protocol for non-routine ongoing management of the MetaMask Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.1.3.3 - Emergency Protocol [Core]  <!-- UUID: 6c02ae31-2313-46ff-9232-2875186e0255 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the MetaMask Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.1.4 - Data Repository [Core]  <!-- UUID: a4a10d71-42f8-49f3-9eeb-dda2ceb1332a -->

The documents herein contain data relevant to the MetaMask Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.1.4.1 - Initial Planning [Core]  <!-- UUID: 177f02ea-cde5-4d68-b7de-c3cef1a47f32 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.1.4.2 - Operational GovOps Review [Core]  <!-- UUID: 2cc897a5-eb49-4766-9489-3cdca7c74196 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.1.4.3 - Artifact Edit Proposal [Core]  <!-- UUID: a7582742-03a8-4095-b394-6fe1b62f912a -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.1.4.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 6296fedf-c2f4-4cdc-a16f-a2b0e8bd19bc -->

The Distribution Reward payments for the MetaMask Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.4.1.4.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 20376e25-f067-400e-be73-dc2552766c47 -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.4.1.4.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: ded05ed5-e470-4cbc-b3f0-c7d8cd928584 -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.4.1.4.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: aa0ea344-4e89-4b6e-8c32-afc5c19cf8d0 -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.4.1.4.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: b537c8e2-92b6-4d2f-88ff-337acb1e8357 -->

The payment address of this Third Party Partner will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.4.2 - InstaDapp Instance Configuration Document [Core]  <!-- UUID: e870392a-2552-41ca-a148-4be47d34bac7 -->

The documents herein contain the Instance Configuration Document for the InstaDapp Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.4.2.1 - Invocation Status [Core]  <!-- UUID: 2f8dec26-fa98-454d-b035-284359de4fe3 -->

`Planning`

###### A.6.1.1.4.2.5.1.4.2.2 - Parameters [Core]  <!-- UUID: 58b69a0b-a8f3-40cd-bc36-154aa61d8f0c -->

The documents herein define the parameters of the InstaDapp Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.2.2.1 - Reward Code [Core]  <!-- UUID: d57c7da4-c5dd-4e11-b5a3-d08aafdaa65f -->

`1006`.

###### A.6.1.1.4.2.5.1.4.2.2.2 - Tracking Methodology [Core]  <!-- UUID: 1dcac5c2-21ec-4714-bf77-f861a851aec4 -->

This parameter will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.4.2.2.3 - Custom Instance Parameters [Core]  <!-- UUID: 5c7380f4-bb98-4dcc-81de-0f02d4e71bbc -->

The documents herein define the custom parameters of the InstaDapp Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.4.2.3 - Operational Process Definition [Core]  <!-- UUID: 64113652-22f2-487b-b170-675ed1e25741 -->

The documents herein define the process for the ongoing management of the InstaDapp Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.2.3.1 - Routine Protocol [Core]  <!-- UUID: c458078b-ffba-428e-950a-9c20a64967d4 -->

This document defines the protocol for routine ongoing management of the InstaDapp Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.4.2.3.1.1 - Agent Customizations [Core]  <!-- UUID: ae59d85f-0a27-461d-a2ef-4b10dd597fee -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.4.2.3.2 - Non-Routine Protocol [Core]  <!-- UUID: 7a34becd-4afd-405c-bfb2-a367568c516f -->

The documents herein define the protocol for non-routine ongoing management of the InstaDapp Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.2.3.3 - Emergency Protocol [Core]  <!-- UUID: 060f50d5-e37f-430a-a103-a06c6b880c63 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the InstaDapp Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.2.4 - Data Repository [Core]  <!-- UUID: 0d530623-4cf8-4046-ac19-5a2095a805d2 -->

The documents herein contain data relevant to the InstaDapp Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.2.4.1 - Initial Planning [Core]  <!-- UUID: f51aa574-e8c8-4e15-bfba-76082d40ac91 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.2.4.2 - Operational GovOps Review [Core]  <!-- UUID: d35d512a-2c81-4491-b966-6803b68f9834 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.2.4.3 - Artifact Edit Proposal [Core]  <!-- UUID: 57a3bfd7-83e2-4033-9dc0-d64274973784 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.2.4.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 38f84680-46ff-400b-baeb-62a0684d2aa7 -->

The Distribution Reward payments for the InstaDapp Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.4.2.4.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: a75fa6c5-8d93-43fe-acad-dfb07e226668 -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.4.2.4.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: 28b69d1f-44d3-4b97-8aff-809513145245 -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.4.2.4.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: 1d995038-ec86-4f39-a02c-21ee651dd3cc -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.4.2.4.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: 1438c4e7-e15b-443c-b9c6-dcdde63920c6 -->

The payment address of this Third Party Partner will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.4.3 - Gnosis Protocol Instance Configuration Document [Core]  <!-- UUID: 34cde6e0-89a1-44a4-9ce1-58873b83c63b -->

The documents herein contain the Instance Configuration Document for the Gnosis Protocol Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.4.3.1 - Invocation Status [Core]  <!-- UUID: ec6a6561-a5e3-4ec6-8ecf-b8053c98149b -->

`Planning`

###### A.6.1.1.4.2.5.1.4.3.2 - Parameters [Core]  <!-- UUID: a8cf666e-2fb6-4830-bc53-5005e0111408 -->

The documents herein define the parameters of the Gnosis Protocol Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.3.2.1 - Reward Code [Core]  <!-- UUID: 96af997a-cd62-41f4-9e32-c5a9dd243f37 -->

`1050`.

###### A.6.1.1.4.2.5.1.4.3.2.2 - Tracking Methodology [Core]  <!-- UUID: 07ec38da-a0ca-468e-83b7-2059ad5e4016 -->

This parameter will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.4.3.2.3 - Custom Instance Parameters [Core]  <!-- UUID: 6fc01270-3033-45b4-8e88-79751b36448c -->

The documents herein define the custom parameters of the Gnosis Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.4.3.3 - Operational Process Definition [Core]  <!-- UUID: fac720c6-f7d2-410c-80bb-8b68c77cdd7c -->

The documents herein define the process for the ongoing management of the Gnosis Protocol Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.3.3.1 - Routine Protocol [Core]  <!-- UUID: 34d65ab5-5a03-42a6-848d-ace67c5e9ab0 -->

This document defines the protocol for routine ongoing management of the Gnosis Protocol Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.4.3.3.1.1 - Agent Customizations [Core]  <!-- UUID: 423d68eb-6fdd-44f4-9bd0-885b44abdd6d -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.4.3.3.2 - Non-Routine Protocol [Core]  <!-- UUID: 9b770474-14bd-4846-8813-4df2bfa77a8f -->

The documents herein define the protocol for non-routine ongoing management of the Gnosis Protocol Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.3.3.3 - Emergency Protocol [Core]  <!-- UUID: 06e37d7d-f130-4b78-b207-32769d75c9db -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Gnosis Protocol Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.3.4 - Data Repository [Core]  <!-- UUID: 1bd8546a-db64-46e5-9271-efc314b0a374 -->

The documents herein contain data relevant to the Gnosis Protocol Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.3.4.1 - Initial Planning [Core]  <!-- UUID: c2db568d-6c90-4a62-8fb9-33cfb504fc1d -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.3.4.2 - Operational GovOps Review [Core]  <!-- UUID: 446804db-4495-4621-a504-e3575e5be34b -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.3.4.3 - Artifact Edit Proposal [Core]  <!-- UUID: 711781c6-57a9-4813-9e4d-263f9a70384a -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.3.4.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: 32c6b23b-8c5f-4798-97e2-84248365365d -->

The Distribution Reward payments for the Gnosis Protocol Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.4.3.4.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: 3dd71633-a629-47af-b806-f7930f1332da -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.4.3.4.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: efbea98b-9063-4706-a467-050eb2594339 -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.4.3.4.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: 985b10b4-837a-48c6-884b-80de88e2462a -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.4.3.4.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: 802462c0-d9d1-42fa-8729-54135634f7f5 -->

The payment address of this Third Party Partner will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.4.4 - Piku.co Instance Configuration Document [Core]  <!-- UUID: bc145261-ff5d-4937-abbd-0719390ff124 -->

The documents herein contain the Instance Configuration Document for the Piku.co Distribution Reward Primitive Instance.

###### A.6.1.1.4.2.5.1.4.4.1 - Invocation Status [Core]  <!-- UUID: 76e70fba-b3a1-40dc-8625-6ba5c6447444 -->

`Planning`

###### A.6.1.1.4.2.5.1.4.4.2 - Parameters [Core]  <!-- UUID: 79da10fb-e6c0-491f-8e18-80edc9e642ad -->

The documents herein define the parameters of the Piku.co Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.4.2.1 - Reward Code [Core]  <!-- UUID: e2a11959-ddcf-4b85-b093-92e2924f2d85 -->

`1010`.

###### A.6.1.1.4.2.5.1.4.4.2.2 - Tracking Methodology [Core]  <!-- UUID: 2785cf23-1be4-4c83-b50e-be57a30c1a79 -->

This parameter will be defined in a future iteration of the Skybase Artifact.

###### A.6.1.1.4.2.5.1.4.4.2.3 - Custom Instance Parameters [Core]  <!-- UUID: 0f252ad2-ea66-49a4-9ff5-10d9bb222532 -->

The documents herein define the custom parameters of the Piku.co Instance of the Distribution Reward Primitive, if any.

###### A.6.1.1.4.2.5.1.4.4.3 - Operational Process Definition [Core]  <!-- UUID: 78aaaa71-7843-4910-aefe-6ba166cbbb0d -->

The documents herein define the process for the ongoing management of the Piku.co Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.4.3.1 - Routine Protocol [Core]  <!-- UUID: a08670ae-0bc5-4424-9b65-38db64441e8d -->

This document defines the protocol for routine ongoing management of the [Piku.co](http://Piku.co) Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.1.4.4.3.1.1 - Agent Customizations [Core]  <!-- UUID: af262fdb-d5ac-4a53-9ca5-47e0448f7ff4 -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.1.4.4.3.2 - Non-Routine Protocol [Core]  <!-- UUID: 4eee5be9-976e-4899-8444-a73c41a952e7 -->

The documents herein define the protocol for non-routine ongoing management of the Piku.co Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.4.3.3 - Emergency Protocol [Core]  <!-- UUID: 316c7704-f588-430a-bc71-6a0730810e54 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Piku.co Instance of this Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.4.4 - Data Repository [Core]  <!-- UUID: 07bcf5db-08bd-4091-9416-38e2561e992b -->

The documents herein contain data relevant to the Piku.co Instance of the Distribution Reward Primitive.

###### A.6.1.1.4.2.5.1.4.4.4.1 - Initial Planning [Core]  <!-- UUID: 3fa947ef-d8e4-4315-bccb-b4a1b6e760ca -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.4.4.2 - Operational GovOps Review [Core]  <!-- UUID: 8dd619da-bb48-4efc-8a68-c21754a11372 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.4.4.3 - Artifact Edit Proposal [Core]  <!-- UUID: 7ccfd0ad-4d2c-441f-afbf-dd6f7b5d4293 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.1.4.4.4.4 - Distribution Reward Payments [Active Data Controller]  <!-- UUID: a1f69b33-8bd2-4c68-b4d5-6b8d34ed763e -->

The Distribution Reward payments for the Piku.co Instance of the Distribution Reward Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.4.4.4.4.0.6.1 - List Of Distribution Reward Payments [Active Data]  <!-- UUID: e05bf544-6a9c-42f5-9135-01a41887a75f -->

The Distribution Reward Payments are:

###### A.6.1.1.4.2.5.1.4.4.4.5 - Third Party Partner Payment Addresses And Transaction Records [Active Data Controller]  <!-- UUID: 55ab7dfa-57e5-49d2-9dc3-05b0bfe14d04 -->

This Document records information pertaining to Skybase's payments to the Third Party Partner associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.1.4.4.4.5.0.6.1 - Payment Details Per Reward Period [Active Data]  <!-- UUID: e0517981-c05e-4f31-b8e0-51a690853132 -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.5.1.4.4.4.5.0.6.2 - Third Party Partner Payment Addresses [Active Data]  <!-- UUID: 49aa9d18-aa7e-464d-a965-f56fd014c02f -->

The payment address of this Third Party Partner will be defined in a future iteration of the Skybase Artifact.

#### A.6.1.1.4.2.5.2 - Integration Boost Primitive [Core]  <!-- UUID: 460cd7ec-5947-4f16-bc6e-de5db7c7a139 -->

The documents herein contain all data and specifications for Skybase's Instances of the Integration Boost Primitive. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

##### A.6.1.1.4.2.5.2.1 - Primitive Hub Document [Core]  <!-- UUID: 4d0912c0-d103-43b2-a6bd-c764b83436ec -->

The documents herein organize all base information relevant to Skybase's usage of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.1.1 - Global Activation Status [Core]  <!-- UUID: e5199f4b-1c36-45c6-b555-51221ea2d09d -->

`Active`

###### A.6.1.1.4.2.5.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 5c4c9ad3-b437-463c-8a2d-c87be9da1a0b -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.5.2.1.2.1 - Euler Instance Configuration Document [Core]  <!-- UUID: 3a05c10f-9e73-4599-91ae-ed0d48fa9fc6 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.2.2.1 - Euler Instance Configuration Document](af548686-1935-4f20-b099-0d5238f388a6).

###### A.6.1.1.4.2.5.2.1.2.2 - Curve Instance Configuration Document Location [Core]  <!-- UUID: 46aa3d84-5bf6-4cfd-8b5c-ecbddd086984 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.2.2.2 - Curve Instance Configuration Document](f628b743-4df7-4814-9684-4707250a7284).

###### A.6.1.1.4.2.5.2.1.2.3 - Morpho Instance Configuration Document Location [Core]  <!-- UUID: a050d87d-8918-4bf7-a0ae-0314d7e85b42 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.4.2.5.2.2.3 Morpho Instance Configuration Document](c18c7746-de43-492b-82f6-6735effa6508).

###### A.6.1.1.4.2.5.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: d9541cd3-07a3-41c7-99ee-c486d4271567 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.5.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 2a9c16c1-c8e4-40eb-96a0-f908ee506a8c -->

This document contains a Directory of all prospective Instances of the Integration Boost Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.5.2.1.2 - Active Instances Directory](5c4c9ad3-b437-463c-8a2d-c87be9da1a0b), whereas failed Invocations are Archived in [A.6.1.1.4.2.5.2.1.5 - Hub Data Repository](eea53dfc-ac8a-456b-8775-c9a80052670b).

###### A.6.1.1.4.2.5.2.1.4.1 - Compound [Core]  <!-- UUID: a0d67712-7f2e-4b40-9b07-d3e8173dbb9b -->

The Invocation Status and Instance Configuration Document location of this prospective Instance are specified below:

Invocation Status: `Planning`

Instance Configuration Document Location: [A.6.1.1.4.2.5.2.4.1 - Compound Instance Configuration Document](0f02f958-70e7-477c-9ad4-386ad01cb2f4).

###### A.6.1.1.4.2.5.2.1.5 - Hub Data Repository [Core]  <!-- UUID: eea53dfc-ac8a-456b-8775-c9a80052670b -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.5.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 38990d57-558c-4efd-95c8-846190693dce -->

The subtrees for archived Invocations and Instances of the Integration Boost Primitive are stored here.

###### A.6.1.1.4.2.5.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: df61a722-0030-4edd-9bec-5be8af796083 -->

The subtrees for failed Invocations of the Integration Boost Primitive are stored here.

###### A.6.1.1.4.2.5.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 24c1bfcf-3525-4ba8-86d8-266435c603f0 -->

The subtrees for Instances of the Integration Boost Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.5.2.2 - Active Instances [Core]  <!-- UUID: 29a952d3-7b87-4aa1-b30f-aed5ed3ff3bd -->

The Instances of the Integration Boost Primitive with `Active` Status are stored herein.

###### A.6.1.1.4.2.5.2.2.1 - Euler Instance Configuration Document [Core]  <!-- UUID: af548686-1935-4f20-b099-0d5238f388a6 -->

The documents herein contain the Instance Configuration Document for the Euler Integration Boost Primitive Instance.

###### A.6.1.1.4.2.5.2.2.1.1 - Parameters [Core]  <!-- UUID: a0d70867-be02-4ef6-89c2-40cf796b6696 -->

The documents herein define the parameters of the Euler Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.1.1.1 - Integration Partner Name [Core]  <!-- UUID: fc909b71-8944-425f-aba8-6a5c05eb84cd -->

The partner for the Euler Integration Boost is Euler.

###### A.6.1.1.4.2.5.2.2.1.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: f052604f-63f5-46ce-8fab-606122e66122 -->

The reward address for the Euler Integration Boost is `0x33C71422B3E20ef2472Bc9aa9252220CAeAF207e` on Base.

###### A.6.1.1.4.2.5.2.2.1.1.3 - Integration Partner Chain [Core]  <!-- UUID: 6f530a97-134f-498f-a662-dd54baef5376 -->

The Euler Integration Boost is on Base blockchain.

###### A.6.1.1.4.2.5.2.2.1.1.4 - Integration Boost Cadence [Core]  <!-- UUID: 05c3cbb8-2f47-4dac-9b42-307d0313ad58 -->

The payment cadence for the Euler Integration Boost is weekly.

###### A.6.1.1.4.2.5.2.2.1.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: f82e8ec9-565c-4d5e-9121-c66086d4bb73 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/incentivized-pools/](https://info-sky.blockanalitica.com/api/v1/incentivized-pools/).

###### A.6.1.1.4.2.5.2.2.1.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: ff5a96bc-61f4-4be7-bacd-9a34dd59cbe8 -->

The Data Submission Responsible Actor is Core Council Risk Advisor.

###### A.6.1.1.4.2.5.2.2.1.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: cc7b38a2-0465-461b-a10d-484a5ad192b3 -->

The Integration Boost is calculated based on per block values for USDS in Euler and the Sky Savings Rate.

###### A.6.1.1.4.2.5.2.2.1.1.8 - Custom Instance Parameters [Core]  <!-- UUID: 0aee1540-84c6-415e-b297-bfa085b65188 -->

The documents herein define the custom parameters of the Euler Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.4.2.5.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 568b6e28-10dc-42aa-81cd-9bc7a6e17a57 -->

The documents herein define the process for the ongoing management of the Euler Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 6fe71ca8-3c28-408e-8b11-3c2fcfcc5778 -->

This document defines the protocol for routine ongoing management of the Euler Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.2.2.1.2.1.1 - Agent Customizations [Core]  <!-- UUID: 4f83666c-ef2e-4527-aeb7-79576b60b221 -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: fa57673c-3d0f-426a-b7c2-3954db4e3b8a -->

The documents herein define the protocol for non-routine ongoing management of the Euler Instance of this Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 07b055a7-cf21-4789-9890-bc3d937de558 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Euler Instance of this Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.1.3 - Data Repository [Core]  <!-- UUID: cb71b9fa-f990-41b1-8650-a37c16e0ef74 -->

The documents herein contain data relevant to the Euler Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: abc0866d-8e3f-4bad-879d-6f82cee2b028 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: ec81388d-8320-47c6-8e13-2dbd5ad95dbe -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 81cff123-b17c-4208-9348-fcf2aaf99c4b -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.1.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: 1f3904b0-28b7-48e2-8cc7-ed67f4b90b68 -->

The Integration Boost payments for the Euler Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.2.2.1.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: 358530ef-9012-4e7f-8dc4-192930c180d0 -->

The Integration Boost Payments are:

###### A.6.1.1.4.2.5.2.2.2 - Curve Instance Configuration Document [Core]  <!-- UUID: f628b743-4df7-4814-9684-4707250a7284 -->

The documents herein contain the Instance Configuration Document for the Curve Integration Boost Primitive Instance.

###### A.6.1.1.4.2.5.2.2.2.1 - Parameters [Core]  <!-- UUID: 358e8a04-fb48-4597-abe6-58b955cd9f00 -->

The documents herein define the parameters of the Curve Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.2.1.1 - Integration Partner Name [Core]  <!-- UUID: 48ae657d-86c0-4254-8202-da1564cb347a -->

The partner for the Curve Integration Boost is Curve.

###### A.6.1.1.4.2.5.2.2.2.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: fa241343-8f00-454b-9b95-726cbcbb7b9d -->

The reward address for the Curve Integration Boost is `0xa7843f843d29ca33ba48d9d1335b774eecc328dc`.

###### A.6.1.1.4.2.5.2.2.2.1.3 - Integration Partner Chain [Core]  <!-- UUID: dd776d9a-7a0c-4b87-a5a5-6ae9e7ac829b -->

The Curve Integration Boost is on Ethereum Mainnet blockchain.

###### A.6.1.1.4.2.5.2.2.2.1.4 - Integration Boost Cadence [Core]  <!-- UUID: 4bbd6ba9-0f20-460b-968b-6b795c20ab4f -->

The payment cadence for the Curve Integration Boost is weekly.

###### A.6.1.1.4.2.5.2.2.2.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: 930022db-e936-4e10-8918-9badced679c0 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/incentivized-pools/](https://info-sky.blockanalitica.com/api/v1/incentivized-pools/).

###### A.6.1.1.4.2.5.2.2.2.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: 1371ca2e-38bc-4c5a-9983-06b2b960f2c9 -->

The Data Submission Responsible Actor is Core Council Risk Advisor.

###### A.6.1.1.4.2.5.2.2.2.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: ddc79c0b-b022-4696-88e4-e2b5d482193d -->

The Integration Boost is calculated based on per block values for USDS in Curve and the Sky Savings Rate.

###### A.6.1.1.4.2.5.2.2.2.1.8 - Custom Instance Parameters [Core]  <!-- UUID: eec6574a-8c01-4de9-8766-8185d6814a79 -->

The documents herein define the custom parameters of the Curve Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.4.2.5.2.2.2.2 - Operational Process Definition [Core]  <!-- UUID: 73b0331d-ac57-4d24-9593-c579d64069f6 -->

The documents herein define the process for the ongoing management of the Curve Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.2.2.1 - Routine Protocol [Core]  <!-- UUID: 62d7f115-e6ed-4bce-8c84-abbbdcb8cb76 -->

This document defines the protocol for routine ongoing management of the Curve Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.2.2.1.3.2.1 - Near Term Process](4ab621b4-ef8e-4b01-a6aa-9296601033c5).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.2.2.2.2.1.1 - Agent Customizations [Core]  <!-- UUID: c62e6889-1704-4258-aa32-69ef911dba25 -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.2.2.2.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 15a02312-d93d-4b6c-bf08-e23c6d7c36d9 -->

The documents herein define the protocol for non-routine ongoing management of the Curve Instance of this Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.2.2.3 - Emergency Protocol [Core]  <!-- UUID: 080d6d53-1fa3-41f2-a479-b2fab290c45e -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Curve Instance of this Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.2.3 - Data Repository [Core]  <!-- UUID: cf22699e-1dc0-4526-9c07-fc5165ab3f75 -->

The documents herein contain data relevant to the Curve Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.2.3.1 - Initial Planning [Core]  <!-- UUID: 00b3c481-bf1d-40a7-9fe8-aea7a99c0524 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.2.3.2 - Operational GovOps Review [Core]  <!-- UUID: 4cdcce5d-a4f5-4474-8818-72d13f6c6174 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.2.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 4c26b560-c84a-4e2b-882f-8ea4b821886f -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.2.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: d2f2c0be-765d-4f3b-9dac-e39ab0244a85 -->

The Integration Boost payments for the Curve Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.6.1.1.4.2.5.2.2.2.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: af376688-bb97-4fe1-bda9-58a59f735a69 -->

The Integration Boost Payments are:

###### A.6.1.1.4.2.5.2.2.3 - Morpho Instance Configuration Document [Core]  <!-- UUID: c18c7746-de43-492b-82f6-6735effa6508 -->

The documents herein contain the Instance Configuration Document for the Morpho Integration Boost Primitive Instance.

###### A.6.1.1.4.2.5.2.2.3.1 - Parameters [Core]  <!-- UUID: fda57199-87e2-4e4a-975a-35780fd324f3 -->

The documents herein define the parameters of the Morpho Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.3.1.1 - Integration Partner Name [Core]  <!-- UUID: 460f1773-d543-4aad-81a3-ca4de567095b -->

The partner for the Morpho Integration Boost is Morpho.

###### A.6.1.1.4.2.5.2.2.3.1.2 - Integration Partner Reward Address [Core]  <!-- UUID: b70f1003-1159-4d5b-b362-c37aa11403d3 -->

The reward address for the Morpho Integration Boost is `0xa7843f843d29ca33ba48d9d1335b774eecc328dc`.

###### A.6.1.1.4.2.5.2.2.3.1.3 - Integration Partner Chain [Core]  <!-- UUID: fbbbda2e-2eca-4b1f-90b1-9cd2f41015a0 -->

The Morpho Integration Boost is on Ethereum Mainnet blockchain.

###### A.6.1.1.4.2.5.2.2.3.1.4 - Integration Boost Cadence [Core]  <!-- UUID: 39dcdc06-4969-4bc3-a9f5-d3196ab1546f -->

The payment cadence for the Morpho Integration Boost is weekly.

###### A.6.1.1.4.2.5.2.2.3.1.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: a92af254-9677-4ae2-ab31-4785180ba959 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/incentivized-pools/](https://info-sky.blockanalitica.com/api/v1/incentivized-pools/).

###### A.6.1.1.4.2.5.2.2.3.1.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: d6f989ca-e897-499c-8ccf-1db864470ad0 -->

The Data Submission Responsible Actor is Core Council Risk Advisor.

###### A.6.1.1.4.2.5.2.2.3.1.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: 398179cc-7315-45ff-bfe3-e26cd761ef93 -->

The Integration Boost is calculated based on per block values for USDS in Morpho and the Sky Savings Rate.

###### A.6.1.1.4.2.5.2.2.3.1.8 - Custom Instance Parameters [Core]  <!-- UUID: dec45734-5da8-4834-acd9-d905b7fb8934 -->

The documents herein define the custom parameters of the Morpho Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.4.2.5.2.2.3.2 - Operational Process Definition [Core]  <!-- UUID: 6e1c68cd-4b68-40df-a9a1-2e729b3af35a -->

The documents herein define the process for the ongoing management of the Morpho Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.3.2.1 - Routine Protocol [Core]  <!-- UUID: c90ad783-129a-416d-a316-a56938a74147 -->

This document defines the protocol for routine ongoing management of the Morpho Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.2.2.1.3.2.1 - Near Term Process](4ab621b4-ef8e-4b01-a6aa-9296601033c5).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.2.2.3.2.1.1 - Agent Customizations [Core]  <!-- UUID: b16396c1-b9af-4840-ba2d-75761b39c7da -->

The Prime Agent may define Instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.2.2.3.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 20c4a428-1129-42c9-b03f-349418cc0767 -->

The documents herein define the protocol for non-routine ongoing management of the Morpho Instance of this Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.3.2.3 - Emergency Protocol [Core]  <!-- UUID: 36da0ac3-eb57-43e9-a56c-832e2bd73b06 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Morpho Instance of this Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.3.3 - Date Repository [Core]  <!-- UUID: 88095904-1a04-449c-b421-3a3c7e4fa437 -->

The documents herein contain data relevant to the Morpho Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.2.3.3.1 - Initial Planning [Core]  <!-- UUID: ef86b5b0-48ce-471e-8a26-dd59dfa09449 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.3.3.2 - Operational GovOps Review [Core]  <!-- UUID: c1e28481-d41d-40b8-96d9-cd372e46b45d -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.3.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 1024c532-ea70-4d0f-b178-b99529950f25 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.2.3.3.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: 81ee6226-9067-4e72-bd0b-77773b581701 -->

The Integration Boost payments for the Morpho Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.6.1.1.4.2.5.2.2.3.3.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: 71d49eb8-0224-4fe7-831e-e49467e2f90d -->

The Integration Boost Payments are:

##### A.6.1.1.4.2.5.2.3 - Completed Instances [Core]  <!-- UUID: 1f90bc85-18f4-46d1-b13c-e49682361c3e -->

The Instances of the Integration Boost Primitive with `Completed` Status are contained herein.

##### A.6.1.1.4.2.5.2.4 - In Progress Invocations [Core]  <!-- UUID: 77018376-b8b2-4a4f-b9c9-e3fc6838be62 -->

The in progress Invocations of the Integration Boost Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.5.2.2 - Active Instances](29a952d3-7b87-4aa1-b30f-aed5ed3ff3bd).

###### A.6.1.1.4.2.5.2.4.1 - Compound Instance Configuration Document [Core]  <!-- UUID: 0f02f958-70e7-477c-9ad4-386ad01cb2f4 -->

The documents herein contain the Instance Configuration Document for the Compound Integration Boost Primitive Instance.

###### A.6.1.1.4.2.5.2.4.1.1 - Invocation Status [Core]  <!-- UUID: 12313a2b-f15e-47ef-84c1-a170dcb777db -->

`Planning`

###### A.6.1.1.4.2.5.2.4.1.2 - Parameters [Core]  <!-- UUID: 8976aeab-15f0-44a3-8e94-145cc998be81 -->

The documents herein define the parameters of the Compound Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.4.1.2.1 - Integration Partner Name [Core]  <!-- UUID: 31dc4b4c-075d-49ce-bb6a-dfccc5a4fceb -->

The partner for the Compound Integration Boost is Compound.

###### A.6.1.1.4.2.5.2.4.1.2.2 - Integration Partner Reward Address [Core]  <!-- UUID: 8fa189a2-6b3f-4af7-9cb5-c24353732ebc -->

The reward address for the Compound Integration Boost is `0xD66241b84dC4d6ccD4aA072A9da22b4B218FC1b0` on Base.

###### A.6.1.1.4.2.5.2.4.1.2.3 - Integration Partner Chain [Core]  <!-- UUID: 4251b3fc-52fa-4c98-9c27-e596406efdfd -->

The Compound Integration Boost is on Base blockchain.

###### A.6.1.1.4.2.5.2.4.1.2.4 - Integration Boost Cadence [Core]  <!-- UUID: 779345d7-e6fe-4363-afde-0b42384294be -->

The payment cadence for the Compound Integration Boost is weekly.

###### A.6.1.1.4.2.5.2.4.1.2.5 - Integration Boost Data Submission Format [Core]  <!-- UUID: 1174bee1-fca4-403e-bfee-36704e00b3c2 -->

The Data Submission Responsible Actor calculates the net deposits based on on-chain events and makes the data available through an API endpoint located at [https://info-sky.blockanalitica.com/api/v1/incentivized-pools/](https://info-sky.blockanalitica.com/api/v1/incentivized-pools/).

###### A.6.1.1.4.2.5.2.4.1.2.6 - Integration Boost Data Submission Responsible Actor [Core]  <!-- UUID: 45a70053-e0a3-4188-a40b-f6b64ffde9e6 -->

The Data Submission Responsible Actor is The Data Submission Responsible Actor is.

###### A.6.1.1.4.2.5.2.4.1.2.7 - Integration Boost Savings Rate Adjustment Strategy [Core]  <!-- UUID: 7f1d30e9-7eaf-45e1-89a5-603f239a11ff -->

The Integration Boost is calculated based on per block values for USDS in Compound and the Sky Savings Rate.

###### A.6.1.1.4.2.5.2.4.1.2.8 - Custom Instance Parameters [Core]  <!-- UUID: 8b64b909-3db0-4c6e-afea-f822433509a7 -->

The documents herein define the custom parameters of the Compound Instance of the Integration Boost Primitive, if any.

###### A.6.1.1.4.2.5.2.4.1.3 - Operational Process Definition [Core]  <!-- UUID: d6e0908f-7b85-4a0f-acac-233489f70164 -->

The documents herein define the process for the ongoing management of the Compound Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.4.1.3.1 - Routine Protocol [Core]  <!-- UUID: 9ad35e12-7bd0-46c8-a753-4a341ab880a2 -->

This document defines the protocol for routine ongoing management of the Compound Instance. This Instance inherits the base class of operational logic defined in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701), subject to the qualifications specified in [A.2.2.9.1.2.1.3.3.1 - Near-Term Process](05fb732b-de55-4886-81a7-7c5d4c13d2d2).

Modifications to the base operational logic automatically propagate to this Instance. In future iterations of the Skybase Artifact, a version of the full process definition customized to Skybase will be included herein.

###### A.6.1.1.4.2.5.2.4.1.3.1.1 - Agent Customizations [Core]  <!-- UUID: f1e42734-b704-4067-bedb-684bca8a1773 -->

The Prime Agent may define instance-specific customization of the routine protocol to extend the baseline functionality defined in the Sky Core Atlas. This can include custom routines or processes layered on top of the inherited Sky Core logic. Any extensions must remain fully aligned with the requirements specified in the Sky Core Atlas. This document defines those customizations, if any.

[No customization presently.]

###### A.6.1.1.4.2.5.2.4.1.3.2 - Non-Routine Protocol [Core]  <!-- UUID: 3aab09cc-2cdb-4afa-82db-230aae80437d -->

The documents herein define the protocol for non-routine ongoing management of the Compound Instance of this Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.4.1.3.3 - Emergency Protocol [Core]  <!-- UUID: 22f14eff-37fd-4bc0-92c5-6d079ee8724b -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Compound Instance of this Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.4.1.4 - Data Repository [Core]  <!-- UUID: ab31a239-9f46-491f-ab8c-b1954bbdb20f -->

The documents herein contain data relevant to the Compound Instance of the Integration Boost Primitive.

###### A.6.1.1.4.2.5.2.4.1.4.1 - Initial Planning [Core]  <!-- UUID: eecefb67-7692-48f7-9f5b-b4bfde253fac -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.4.1.4.2 - Operational GovOps Review [Core]  <!-- UUID: 28bf469c-af5c-4014-8947-035def7c4077 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.4.1.4.3 - Artifact Edit Proposal [Core]  <!-- UUID: 6543a665-e415-4b54-9c0b-5af10c14f5ce -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

###### A.6.1.1.4.2.5.2.4.1.4.4 - Integration Boost Payments [Active Data Controller]  <!-- UUID: 55b46793-6543-4002-a1d7-9cc33ef46ab6 -->

The Integration Boost payments for the Compound Instance of the Integration Boost Primitive are defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.6.1.1.4.2.5.2.4.1.4.4.0.6.1 - List Of Integration Boost Payments [Active Data]  <!-- UUID: afe3fba8-14b9-47b7-bd71-20be58c47f29 -->

The Integration Boost Payments are:

#### A.6.1.1.4.2.5.3 - Pioneer Chain Primitive [Core]  <!-- UUID: d096b01c-84a2-44a5-9af6-8888a825e0d4 -->

The documents herein contain all data and specifications for Skybase's Instances of the Pioneer Chain Primitive. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).

##### A.6.1.1.4.2.5.3.1 - Primitive Hub Document [Core]  <!-- UUID: a5890268-5a4c-4b8c-890a-6db09c71aced -->

The documents herein organize all base information relevant to Skybase's usage of the Pioneer Chain Primitive.

###### A.6.1.1.4.2.5.3.1.1 - Global Activation Status [Core]  <!-- UUID: 91ae0bcc-bd80-4de1-bbd7-e875d150563a -->

`Inactive`

###### A.6.1.1.4.2.5.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 5aa36020-011e-457b-8605-95988a244606 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.5.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: f7c6c056-bbb0-4dae-9457-4bb4592966a7 -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.5.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 5dde47de-0f14-4cba-aae8-89c5f16a2303 -->

This document contains a Directory of all prospective Instances of the Pioneer Chain Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.5.3.1.2 - Active Instances Directory](5aa36020-011e-457b-8605-95988a244606), whereas failed Invocations are Archived in [A.6.1.1.4.2.5.3.1.5 - Hub Data Repository](352eb7b1-b4bf-405d-970c-d937ffb65ae3).

###### A.6.1.1.4.2.5.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 352eb7b1-b4bf-405d-970c-d937ffb65ae3 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.5.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 6808eba8-aea7-497f-9ca1-3fa360a6ad46 -->

The subtrees for archived Invocations and Instances of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.4.2.5.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: c5a4fb59-8b70-42ef-a43d-c78d6bdb70b6 -->

The subtrees for failed Invocations of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.4.2.5.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 55bf90c4-007c-4cd8-8a37-60659a0404bb -->

The subtrees for Instances of the Pioneer Chain Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.5.3.2 - Active Instances [Core]  <!-- UUID: 204539dc-c8b2-46d2-a6c1-14552870b6e3 -->

The Instances of the Pioneer Chain Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.5.3.3 - Completed Instances [Core]  <!-- UUID: 0e546189-6559-4d2b-b4d1-bdd86e2ab499 -->

The Instances of the Pioneer Chain Primitive with `Completed` Status are stored herein.

##### A.6.1.1.4.2.5.3.4 - In Progress Invocations [Core]  <!-- UUID: 6787cd76-9666-4fb4-9b2c-120ad771afb8 -->

The in progress Invocations of the Pioneer Chain Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.5.3.2 - Active Instances](204539dc-c8b2-46d2-a6c1-14552870b6e3).

### A.6.1.1.4.2.6 - Supply Side Stablecoin Primitives [Core]  <!-- UUID: b58a8d96-b6df-416e-b81f-2898d82924b4 -->

The documents herein implement the Supply Side Stablecoin Primitives for Skybase. See [A.2.2.10 - Supply Side Stablecoin Primitives](d1142876-33c2-4e21-9339-d8711525d46f).

#### A.6.1.1.4.2.6.1 - Allocation System Primitive [Core]  <!-- UUID: 24b63123-f30f-4dc3-aefa-74b4351c4baa -->

The documents herein contain all data and specifications for Skybase's Instances of the Allocation System Primitive. See [A.2.2.10.1 - Allocation System Primitive](9db14ab7-bb4b-4751-8084-843bd4359f2a).

##### A.6.1.1.4.2.6.1.1 - Primitive Hub Document [Core]  <!-- UUID: 72950044-a7ba-44bf-9910-1e655bfbbb76 -->

The documents herein organize all base information relevant to Skybase's usage of the Allocation System Primitive.

###### A.6.1.1.4.2.6.1.1.1 - Global Activation Status [Core]  <!-- UUID: 757a827f-c736-4ac5-8eaf-993567dee621 -->

`Inactive`

###### A.6.1.1.4.2.6.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 05bc1cbc-57a1-462e-8618-b401636ac835 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.6.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 04c05a8f-cb70-4cb3-85e7-ceaa94c75c34 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.6.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: b74ad51a-a372-4706-9084-d22c00318955 -->

This document contains a Directory of all prospective Instances of the Allocation System Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.6.1.1.2 - Active Instances Directory](05bc1cbc-57a1-462e-8618-b401636ac835), whereas failed Invocations are Archived in [A.6.1.1.4.2.6.1.1.5 - Hub Data Repository](b5d982d8-9d61-480b-a6c0-a90b7bbc8221).

###### A.6.1.1.4.2.6.1.1.5 - Hub Data Repository [Core]  <!-- UUID: b5d982d8-9d61-480b-a6c0-a90b7bbc8221 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.6.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: a8aa5d01-48ae-4ade-8a3c-ed42fb40a2b2 -->

The subtrees for archived Invocations and Instances of the Allocation System Primitive are stored here.

###### A.6.1.1.4.2.6.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 21cab16e-58b3-4111-bdff-188d4cf8095e -->

The subtrees for failed Invocations of the Allocation System Primitive are stored here.

###### A.6.1.1.4.2.6.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 560787c2-e593-4d69-aba0-d1708fb92a1a -->

The subtrees for Instances of the Allocation System Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.6.1.2 - Multi-Instance Coordinator Document [Core]  <!-- UUID: fcfbc136-69fe-48aa-986e-b0cc5eea9590 -->

The documents herein specify the logic for coordinating multiple Instances of the Allocation System Primitive. In the future, additional logic will be added herein regarding how capital is allocated between different Instances of the Allocation System Primitive.

##### A.6.1.1.4.2.6.1.3 - Active Instances [Core]  <!-- UUID: d9c177ad-b1c8-4af7-a537-b6a36bf29dc4 -->

The Instances of the Allocation System Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.6.1.4 - Completed Instances [Core]  <!-- UUID: 953249d4-609a-4e03-b069-bbbcd2d1c88e -->

The Instances of the Allocation System Primitive with `Completed` Status are stored herein.

##### A.6.1.1.4.2.6.1.5 - In Progress Invocations [Core]  <!-- UUID: c95c1adc-dd0a-4ddb-b992-3948f1e000c2 -->

The in progress Invocations of the Allocation System Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.6.1.3 - Active Instances](d9c177ad-b1c8-4af7-a537-b6a36bf29dc4).

#### A.6.1.1.4.2.6.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: 09144d1a-2cda-4805-b50d-b3da4f09d48b -->

The documents herein contain all data and specifications for Skybase's Instances of the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.6.1.1.4.2.6.2.1 - Primitive Hub Document [Core]  <!-- UUID: 16bf9c06-af9f-4853-bf8b-5246ada6e580 -->

The documents herein organize all base information relevant to Skybase's usage of the Risk Capital Rental Primitive.

###### A.6.1.1.4.2.6.2.1.1 - Global Activation Status [Core]  <!-- UUID: 84c95412-5704-480d-bf68-7dcffb78cf21 -->

`Inactive`

###### A.6.1.1.4.2.6.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 1c446878-ac5e-46a5-956c-346dfb288381 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.6.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 30d04fa4-801d-468a-b7ea-2b0ffb54c18b -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.6.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: f0296ab8-bf0c-465a-955e-2566580cc810 -->

This document contains a Directory of all prospective Instances of the Risk Capital Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.6.2.1.2 - Active Instances Directory](1c446878-ac5e-46a5-956c-346dfb288381), whereas failed Invocations are Archived in [A.6.1.1.4.2.6.2.1.5 - Hub Data Repository](f3e94987-31d6-47c9-8809-fc90d1f401cd).

###### A.6.1.1.4.2.6.2.1.5 - Hub Data Repository [Core]  <!-- UUID: f3e94987-31d6-47c9-8809-fc90d1f401cd -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.6.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ebbef9e3-ab93-4a98-90d3-57663fac9134 -->

The subtrees for archived Invocations and Instances of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.4.2.6.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 7b34c64e-fda4-40d0-84cd-891c86e8de1c -->

The subtrees for failed Invocations of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.4.2.6.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 90c24d4a-39b0-40a3-af07-7cd353440b7e -->

The subtrees for Instances of the Risk Capital Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.6.2.2 - Active Instances [Core]  <!-- UUID: 44cbe0d7-fb84-4958-9bd7-29f931e09629 -->

The Instances of the Risk Capital Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.6.2.3 - Completed Instances [Core]  <!-- UUID: 759df9b0-3bac-426e-b08d-3a5fb98d1cb9 -->

The Instances of the Risk Capital Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.4.2.6.2.4 - In Progress Invocations [Core]  <!-- UUID: 08ab0db0-8a0f-45b5-8579-8c4984a69fd1 -->

The in progress Invocations of the Risk Capital Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.6.2.2 - Active Instances](44cbe0d7-fb84-4958-9bd7-29f931e09629).

#### A.6.1.1.4.2.6.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: c2f8c143-52a9-41a5-be4a-05c07ca64f6b -->

The documents herein contain all data and specifications for Skybase's Instances of the Asset Liability Management Rental Primitive. See [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

##### A.6.1.1.4.2.6.3.1 - Primitive Hub Document [Core]  <!-- UUID: 23300804-de11-4f5d-a28f-bc7995b36165 -->

The documents herein organize all base information relevant to Skybase's usage of the Asset Liability Management Rental Primitive.

###### A.6.1.1.4.2.6.3.1.1 - Global Activation Status [Core]  <!-- UUID: d57f7f80-a04b-45be-a9e1-3ce55fdf7b03 -->

`Inactive`

###### A.6.1.1.4.2.6.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 5a9f343e-4513-4ded-ab34-6f76690943d1 -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.6.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: b537b35c-d9a5-4c64-88ab-d2bc54793ecb -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.6.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 92a1b7cd-9f42-4238-b388-d09d2eab1b61 -->

This document contains a Directory of all prospective Instances of the Asset Liability Management Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.6.3.1.2 - Active Instances Directory](5a9f343e-4513-4ded-ab34-6f76690943d1), whereas failed Invocations are Archived in [A.6.1.1.4.2.6.3.1.5 - Hub Data Repository](ca4d7aa2-daae-4806-aeb8-fa2ff48d5a1c).

###### A.6.1.1.4.2.6.3.1.5 - Hub Data Repository [Core]  <!-- UUID: ca4d7aa2-daae-4806-aeb8-fa2ff48d5a1c -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.6.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 9916eb6a-e91a-4fcd-b7fe-09728e5d9229 -->

The subtrees for archived Invocations and Instances of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.4.2.6.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 402c4b86-0fdc-4234-b3c9-81436bdfb5ac -->

The subtrees for failed Invocations of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.4.2.6.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: df448d70-9b59-41e9-b4a7-475c2ad37b8c -->

The subtrees for Instances of the Asset Liability Management Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.6.3.2 - Active Instances [Core]  <!-- UUID: afc7b951-c066-4a6e-8b54-cf706a75c09f -->

The Instances of the Asset Liability Management Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.4.2.6.3.3 - Completed Instances [Core]  <!-- UUID: 662e5da6-5275-4649-991a-1121f4f9773e -->

The Instances of the Asset Liability Management Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.4.2.6.3.4 - In Progress Invocations [Core]  <!-- UUID: 2827ce37-f144-4111-8fd4-2908beeade5a -->

The in progress Invocations of the Asset Liability Management Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.6.3.2 - Active Instances](afc7b951-c066-4a6e-8b54-cf706a75c09f).

### A.6.1.1.4.2.7 - Core Governance Primitives [Core]  <!-- UUID: 095cc4f1-a097-4157-8e81-06031208c39f -->

The documents herein implement the Core Governance Primitives for Skybase. See [A.2.2.11 - Core Governance Primitives](6fa54611-c744-4b9d-897d-b2a20e9cae5d).

#### A.6.1.1.4.2.7.1 - Core Governance Reward Primitive [Core]  <!-- UUID: 79b5a43d-1abe-4945-9f7d-7fa8a5ac182e -->

The documents herein contain all data and specifications for Skybase's Instances of the Core Governance Reward Primitive. See [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a).

##### A.6.1.1.4.2.7.1.1 - Primitive Hub Document [Core]  <!-- UUID: 58a4cf93-5c1c-4fec-8c5b-2c1c6f167c72 -->

The documents herein organize all base information relevant to Skybase's usage of the Core Governance Reward Primitive.

###### A.6.1.1.4.2.7.1.1.1 - Global Activation Status [Core]  <!-- UUID: 3c76baaa-df7f-464e-80ed-6b48eefbea7f -->

`Active`

###### A.6.1.1.4.2.7.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 93f4f2d8-68ae-4b33-98a6-e9d9fa764cd0 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Active`.

###### A.6.1.1.4.2.7.1.1.2.1 - Sky.money Frontend Instance Configuration Document Location [Core]  <!-- UUID: 07f7da42-c12c-4ee1-a45a-7cc342ef5ff2 -->

This Instance's associated Instance Configuration Document is located at [A.6.1.1.4.2.7.1.2.1 - Sky.money Frontend Instance Configuration Document](33a977ad-77eb-45f6-850e-4d00eed8d049).

###### A.6.1.1.4.2.7.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: ed1c95ef-c156-473d-9c9e-b78c84bc2feb -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.4.2.7.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 30c32b90-6471-49f7-ab7b-956ece318a8e -->

This document contains a Directory of all prospective Instances of the Core Governance Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.4.2.7.1.1.2 - Active Instances Directory](93f4f2d8-68ae-4b33-98a6-e9d9fa764cd0), whereas failed Invocations are Archived in [A.6.1.1.4.2.7.1.1.5 - Hub Data Repository](766df1ab-660b-4066-982a-7e99c21c93ec).

###### A.6.1.1.4.2.7.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 766df1ab-660b-4066-982a-7e99c21c93ec -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.4.2.7.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 1afa6e50-af3a-4014-bd38-c53b4b1287e7 -->

The subtrees for archived Invocations and Instances of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.4.2.7.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 3b9b1819-7645-4d38-9766-05d21d6403ad -->

The subtrees for failed Invocations of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.4.2.7.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 8cea9dc7-d1b5-4a26-89fb-675dc896bdb0 -->

The subtrees for Instances of the Core Governance Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.4.2.7.1.2 - Active Instances [Core]  <!-- UUID: 2e2b5ba1-329c-4654-9628-5e5bc50da4d7 -->

The Instances of the Core Governance Reward Primitive with `Active` Status are stored herein.

###### A.6.1.1.4.2.7.1.2.1 - Sky.money Frontend Instance Configuration Document [Core]  <!-- UUID: 33a977ad-77eb-45f6-850e-4d00eed8d049 -->

The documents herein contain the Instance Configuration Document for the Sky.money Frontend Core Governance Reward Primitive Instance.

###### A.6.1.1.4.2.7.1.2.1.1 - Parameters [Core]  <!-- UUID: 715c34a9-79fa-42ab-9e6b-f0f045544cc6 -->

The documents herein define the parameters of the Sky.money Frontend Instance of the Core Governance Reward Primitive.

###### A.6.1.1.4.2.7.1.2.1.1.1 - Reward Code [Core]  <!-- UUID: ecd6843d-d1a3-43d8-af2c-af5fc8d9045f -->

`1`.

###### A.6.1.1.4.2.7.1.2.1.1.2 - Tracking Methodology [Core]  <!-- UUID: e7a6dd83-4b9f-41db-8506-dede902828ce -->

This Instance uses the Tracking Methodology specified in [A.2.2.11.1.4.2.1 - Tracking Via Reward Codes](b16cb8a3-aea3-4fda-b904-eb782ea7a8e1).

###### A.6.1.1.4.2.7.1.2.1.1.3 - Custom Instance Parameters [Core]  <!-- UUID: 228f89fd-a51e-413a-b42b-e117414891be -->

The documents herein define the custom parameters of the Sky.money Frontend Instance of the Core Governance Reward Primitive, if any.

###### A.6.1.1.4.2.7.1.2.1.1.3.1 - Integrator Recipient [Core]  <!-- UUID: 56de7bd0-062d-46f5-acca-6b4466d15777 -->

The Integrator is Sky.money Frontend, which is controlled by Skybase. As such, no additional Integrator payment will be made.

###### A.6.1.1.4.2.7.1.2.1.2 - Data Repository [Core]  <!-- UUID: 3f0387c9-2a45-47f1-8f5e-1cdfa273f237 -->

The documents herein contain data relevant to the Sky.money Frontend Instance of the Core Governance Reward Primitive.

###### A.6.1.1.4.2.7.1.2.1.2.1 - Core Governance Reward Payments And Transaction Records [Active Data Controller]  <!-- UUID: 3dc7cce4-1e15-43e4-907c-d4a074a3531a -->

This Document records information pertaining to payments received by Skybase for Governance Rewards associated with this Instance. This information is defined as Active Data.

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.6.1.1.4.2.7.1.2.1.2.1.0.6.1 - List Of Core Governance Reward Payments [Active Data]  <!-- UUID: adcc7123-ee48-48ae-be34-f6c94b5a973c -->

The payment details consist of a table where each entry represents a single payment. Each entry has the following fields:

- Reward Period
- Payee (Skybase)
- Payment Address
- Amount Paid
- Transaction Hash
- Transaction Date

###### A.6.1.1.4.2.7.1.2.1.2.1.0.6.2 - Governance Reward Payment Address [Active Data]  <!-- UUID: 7d57bc04-a81b-4007-aa2e-8d78ba4ecc52 -->

The Sky.money Frontend Governance Reward payment address is Skybase's SubProxy Account on Ethereum Mainnet: `0x08978E3700859E476201c1D7438B3427e3C81140`.

##### A.6.1.1.4.2.7.1.3 - Completed Instances [Core]  <!-- UUID: 81228652-c70b-42db-bed4-8fbe4c35695f -->

The Instances of the Core Governance Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.4.2.7.1.4 - In Progress Invocations [Core]  <!-- UUID: cd5aeba6-3ba5-4f8e-9246-18319f6986b3 -->

The in progress Invocations of the Core Governance Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.4.2.7.1.2 - Active Instances](2e2b5ba1-329c-4654-9628-5e5bc50da4d7).

## A.6.1.1.4.3 - Omni Documents [Core]  <!-- UUID: 12153a95-5be4-4f5e-8d04-d3046ad9b7bc -->

The documents herein define Skybase's strategic intent and operational processes relating to infrastructure inherited from Sky Core, activities unrelated to Sky Primitives, or activities spanning multiple Sky Primitives.

### A.6.1.1.4.3.1 - Governance Information Unrelated To Root Edit Primitive [Core]  <!-- UUID: 70804058-8a1b-45ee-bf21-b09a5daefdb9 -->

The documents herein specify Skybase governance information that is unrelated to the use of the Root Edit Primitive. The governance process for updating the Skybase Artifact is specified in the Root Edit Primitive above at [A.6.1.1.4.2.2.2 - Root Edit Primitive](24517c43-dec9-44ec-bc03-e76671dc2e74).

#### A.6.1.1.4.3.1.1 - Sky Forum [Core]  <!-- UUID: 0d482d6a-f140-4798-bf9c-a0c6cb5a2aa5 -->

Skybase uses the Sky Forum for governance-related discussion. Posts should use the "Skybase Prime" category.

#### A.6.1.1.4.3.1.2 - Discord [Core]  <!-- UUID: 31f5b013-30a1-4135-8e04-4e9b7ee6a794 -->

Skybase also uses Discord for more immediate communication. The Sky Discord is located at [https://t.co/v6zG0MZtak](https://t.co/v6zG0MZtak).

#### A.6.1.1.4.3.1.3 - Sky Ecosystem Emergency Response [Core]  <!-- UUID: dedeb7e0-af9d-41ef-aec2-cdfb8b3fc437 -->

The documents herein specify Skybase's emergency response protocol in situations that impact the entire Sky Ecosystem. This protocol will be specified in a future iteration of the Skybase Artifact.

#### A.6.1.1.4.3.1.4 - Agent-Specific Emergency Response [Core]  <!-- UUID: 8a9aef44-d044-40e6-91f6-c810d27e9d5c -->

The documents herein specify Skybase's emergency response protocol in situations solely impacting Skybase versus the broader Sky Ecosystem. This protocol will be specified in a future iteration of the Skybase Artifact.

### A.6.1.1.4.3.2 - Sky Primitives Strategy [Core]  <!-- UUID: 8bc018e0-e343-424e-9089-6a813d168dff -->

The documents herein define Skybase's strategic intent with respect to certain Sky Primitives.

#### A.6.1.1.4.3.2.1 - Distribution Reward Strategy [Core]  <!-- UUID: 825f23f7-739b-4a76-8e23-540b11f1854c -->

Skybase's strategy with respect to the Distribution Reward Primitive is to encourage the broad adoption of USDS by bridging into new communities and DeFi platforms, thereby earning and distributing Distribution Rewards for USDS balances facilitated through its frontend. Prospective partners should demonstrate strong alignment with Skybase's mission, and offer clear pathways to engage new user bases and support the sustainable growth of USDS across diverse ecosystems.

The guiding criteria are as follows:

- **Shared Mission Alignment:** Partners must demonstrate a commitment to promoting user-friendly stablecoin usage and responsible financial empowerment.
- **Clear Synergy:** The collaboration should enhance USDS accessibility, by offering either a unique distribution channel or a robust incentive model.
- **Community Benefit**: Proposed partnerships should deliver tangible rewards or advantages that resonate with Sky’s user base.
- **Scalability & Compliance:** Potential integrations should have the capacity to handle increased demand and adhere to the risk management guidelines described in the Atlas.

#### A.6.1.1.4.3.2.2 - Integration Boost Strategy [Core]  <!-- UUID: 8b587f01-c678-4f6d-ba37-a0765f5657b0 -->

Skybase's strategy with respect to the Integration Boost Primitive is to deliver a "Sky Savings Rate" (or similar program) to USDS users across selected DeFi platforms. This approach aims to extend the reach of USDS by tapping into fresh communities and expanding its overall market presence. New collaborations should exhibit compatibility with Skybase's accessibility ethos, showcase steady on-chain activity, and present clear opportunities to onboard broader user segments into the Skybase ecosystem.

The guiding criteria are as follows:

- **Long-Term Viability:** Target platforms must exhibit strong on-chain activity and a track record of stability.
- **Aligned Incentives:** Collaborations should offer meaningful yield enhancements that support the broader Sky mission.
- **Growth Potential:** Partners must show clear prospects for sustainable scaling, ensuring that users can benefit from ongoing improvements.

#### A.6.1.1.4.3.2.3 - Core Governance Reward Strategy [Core]  <!-- UUID: 276d8421-4f07-4ac5-812d-88909b5a9ecd -->

Skybase's strategy with respect to the Core Governance Reward Primitive is to provide continuous, secure, and user-friendly governance frontend hosting for SKY holders, ensuring critical decision-making processes remain accessible and reliable over time.

The guiding criteria are as follows:

- **Security & Reliability:** The Prime Agent will uphold robust security measures and maintain high availability to prevent disruptions or unauthorized access.
- **Governance Framework Alignment:** Any updates to the frontend should integrate smoothly with Skybase's existing governance mechanisms, preserving uninterrupted voting and proposal workflows.

### A.6.1.1.4.3.3 - Ecosystem Accords [Core]  <!-- UUID: 64dd4885-6d75-45c0-86a9-507bc9a55194 -->

Skybase has formally agreed to the Ecosystem Accords herein.

#### A.6.1.1.4.3.3.1 - Ecosystem Accord 7 [Core]  <!-- UUID: b6196792-be39-47cb-9742-620159bf09c2 -->

Skybase engaged in terms of agreement with Sky in Ecosystem Accord 7, located in [A.2.8.2.7 - Ecosystem Accord 7: Sky And Skybase](8a74919c-d9c1-4d9a-9499-302201f96f9c).

### A.6.1.1.4.3.4 - USDS Demand Subsidies [Core]  <!-- UUID: 5e276fe6-1449-47ba-9a7d-cddd1d1a236f -->

Skybase uses capital to provide Subsidies to incentivize strategic markets to promote USDS demand.

#### A.6.1.1.4.3.4.1 - USDS Demand Subsidies Capital [Core]  <!-- UUID: 1d8d603f-33f8-47bb-8562-8eb5701a3aff -->

The source of capital for Skybase's USDS Demand Subsidies is the Skybase Treasury. Skybase Treasury capital is transferred to the USDS Demand Subsidies Multisig for utilization.

#### A.6.1.1.4.3.4.2 - USDS Demand Subsidies Multisig [Core]  <!-- UUID: 20ee784c-115a-40bb-ae74-d4b3726b0c1b -->

The USDS Demand Subsidies Multisig is controlled by two (2) signers from Operational GovOps Soter Labs and one (1) signer from Skybase Foundation.

##### A.6.1.1.4.3.4.2.1 - Address [Core]  <!-- UUID: 615835d8-475b-48f6-9e0f-bcaf041a63ff -->

The USDS Demand Subsidies Multisig address on Ethereum Mainnet is `0x3f32bc09d41ee699844f8296e806417d6bf61bba`.

##### A.6.1.1.4.3.4.2.2 - Required Number of Signers [Core]  <!-- UUID: 740a4a39-f560-437a-962c-4255384298a1 -->

The USDS Demand Subsidies Multisig currently has a 2/3 signing requirement.

##### A.6.1.1.4.3.4.2.3 - Signers [Core]  <!-- UUID: dbb22ec2-97fc-47c1-85d3-9b1cc94d3ce0 -->

The USDS Demand Subsidies Multisig has the following signers:

- Soter Labs: 2 signers
- Skybase Foundation: 1 signer

##### A.6.1.1.4.3.4.2.4 - Usage Standards [Core]  <!-- UUID: 0d896655-0d03-4c73-b164-3f59668256dd -->

The signers must use the USDS Demand Subsidies Multisig to disburse funds on behalf of Skybase to fund strategic USDS demand incentive opportunities.

##### A.6.1.1.4.3.4.2.5 - Modification [Core]  <!-- UUID: 665ca5c5-ca1b-471a-9a10-16c46ee10cfd -->

Operational GovOps Soter Labs can change the signers of the USDS Demand Subsidies Multisig at any time, so long as there are at least two (2) signers from Soter Labs and one (1) signer from Skybase Foundation, and at least two-thirds of signers are required to execute transactions.
