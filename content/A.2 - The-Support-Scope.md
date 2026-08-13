# A.2 - The Support Scope [Scope]  <!-- UUID: 1ce14bd8-c7b3-4f74-a152-292a8d8ebed0 -->

The Support Scope governs all routine aspects of ecosystem support, including governance process infrastructure and management, Agent support and Ecosystem Actor support.

## A.2.1 - Governance Process Support [Article]  <!-- UUID: f83a880f-6440-49ac-8e28-b16b4e2c9912 -->

The Support Scope regulates the routine governance processes needed to operationalize the Atlas. This Article defines key infrastructure and processes supporting this objective.

### A.2.1.1 - Governance Process Support [Section]  <!-- UUID: ef1ad0bf-069c-4199-8620-a508b34c2348 -->

The Support Scope must facilitate the routine governance processes of the Sky Ecosystem, pursuant to the principles and procedures defined herein.

#### A.2.1.1.1 - In General [Core]  <!-- UUID: 4b76256c-c625-49ce-a91d-88d3fbd2452f -->

Sky Governance deploys various core processes to implement its decision-making, including Aligned Delegate processes, the Weekly Governance Cycle, the Monthly Governance Cycle and the modification of Active Data. The Support Scope regulates routine governance processes based in the explicit rules of the Atlas. In contrast, the Governance Scope governs situations in which a document is appealed or is otherwise contentious for reasons of ambiguity or conflict with other documents.

##### A.2.1.1.1.0.3.1 - Ambiguity - Element Annotation [Annotation]  <!-- UUID: 62e031ef-de5a-4425-8561-439b6f72a548 -->

The element "ambiguity" refers to instances where the language of an Atlas document allows for multiple possible interpretations.

##### A.2.1.1.1.0.3.2 - Contentious - Element Annotation [Annotation]  <!-- UUID: 6691933f-0d3f-4a20-b609-57001a6a3491 -->

The element "contentious" describes a situation where there is disagreement or dispute regarding the interpretation, application, or validity of a document.

##### A.2.1.1.1.0.3.3 - Document Is Appealed - Element Annotation [Annotation]  <!-- UUID: b5be838e-23a8-4ed4-b713-d5a57fe1864d -->

The element means that a formal request has been made to the Core Facilitator to review an Atlas document for potential conflicts with other documents or misalignment. See [A.1.2.3 - Conflict Resolution](e883ceb7-707d-4b1d-af3c-ed6f9aeac565).

#### A.2.1.1.2 - Coordination Of Scope Framework Processes [Core]  <!-- UUID: 53388cf1-7934-4048-a372-2aec5e5b8430 -->

The Scopes establish various specialized processes, including those for submitting governance proposals or modifying the Atlas. Core GovOps is responsible for monitoring and ensuring that these processes are executed in accordance with the established rules. An action carried out through a Scope-defined process is considered valid only if Core GovOps has been properly notified.

##### A.2.1.1.2.0.3.1 - Monitoring And Ensuring - Element Annotation [Annotation]  <!-- UUID: f51addb2-fba3-476f-b3e4-1c5b4b9013fc -->

This element refers to the ongoing responsibility of Core GovOps to monitor the progress of routine governance processes, check for compliance with the rules, and confirm that all necessary documentation and approvals are in place.

##### A.2.1.1.2.0.3.2 - Properly Notified - Element Annotation [Annotation]  <!-- UUID: df31f503-1238-4380-9a0e-25e2ef7c81d0 -->

This element means that Core GovOps have been informed in accordance with the prescribed procedures, including the timing, method, and content of the notification, as required by the relevant Scope.

#### A.2.1.1.3 - Designation Of Governance Process Support Ecosystem Actors [Core]  <!-- UUID: d537c3df-287c-45a5-aa69-2b4242b2259f -->

Core GovOps can designate Ecosystem Actors (including individuals, companies or Forum or Chat pseudonyms) as Governance Process Support Ecosystem Actors. This designation can include granting them moderation rights and other forms of administration rights on the relevant communication channels.

Governance Process Support Ecosystem Actors can assist with governance processes including verifying Atlas Edit Proposals (AEPs), preparing and merging Pull Requests, updating the status of AEPs, preparing Polls, editing the Atlas, etc.

#### A.2.1.1.4 - Resources [Core]  <!-- UUID: 048600dc-3e21-4e1b-9e69-a0b5aff92ff8 -->

Core GovOps is granted a budget to procure the necessary administrative support and services from Governance Process Support Ecosystem Actors. The budget can only be used to perform tasks described in [A.2.1.1 - Governance Process Support](ef1ad0bf-069c-4199-8620-a508b34c2348) and its subdocuments. Core GovOps can modify the budget using an Operational Weekly Cycle poll.

##### A.2.1.1.4.1 - Current Budget [Core]  <!-- UUID: 5efada66-f3d2-4e3e-b26c-123467069437 -->

The budget available to fund Governance Process Support tasks is 0 USDS per quarter.

## A.2.2 - Sky Primitives [Article]  <!-- UUID: fcde2604-a138-4c1b-9d9a-14895835c907 -->

This Article governs the Sky Primitives. A Sky Primitive is a standardized interface that allows Agents to connect to, and leverage, Sky Protocol’s permissioned infrastructure. This Article defines each of the Sky Primitives available for Prime Agents to use to expand the Sky Ecosystem. Each Prime Agent strategy is unique, so each may combine the Sky Primitives differently.

### A.2.2.1 - Primitives In General [Section]  <!-- UUID: df611e97-f99d-4244-8573-e706fbd1dfbc -->

The documents herein define general principles relating to Agent Artifact evolution, enumerate the currently available Sky Primitives, and prescribe the procedures by which Agents can activate, invoke and deploy the Primitives.

#### A.2.2.1.1 - Initial Stages Of Artifact Evolution [Core]  <!-- UUID: 73eb0d53-2746-4db8-8b61-608f7439d560 -->

The documents herein define the initial stages of the lifecycle of an Agent Artifact, beginning with the prerequisite of capital deployment and continuing until the Agent gains full operational status with an active Executor Accord and Root Edit Primitive. At that point, the Agent is interoperable with other Sky Agents and possesses a formal governance process by which token holders can guide its activities.

##### A.2.2.1.1.1 - Founder Deposits Capital And Pays Agent Creation Fee [Core]  <!-- UUID: 96ecd286-9361-4cb0-8062-9dd930780f3e -->

The prospective Agent founder kicks off the lifecycle of an Agent by deploying an initial minimum amount of capital and paying an Agent Creation fee in an off-chain process as defined in [A.2.2.3.1.1 - Capital Injection](bed7471a-54aa-4167-88dd-22ebd63f8827).

##### A.2.2.1.1.2 - Core GovOps Creates Scaffold Agent Artifact [Core]  <!-- UUID: b485d31f-e7e2-45fd-aefb-2a55206390a2 -->

After receiving the initial capital and Agent Creation fee, Core GovOps proceeds to set up a Scaffold Agent Artifact ("Scaffold Artifact"), which serves as a base template containing all Sky Primitives. In the Scaffold Artifact, the Global Activation Status of all Sky Primitives is initially set to `Inactive`. The sole exception is the Upkeep Rebate Primitive, whose Global Activation Status in the newly generated Scaffold Artifact is `Active` by default. See [A.2.2.1.2 - Primitive Global Activation Status](dde8cf4c-4823-4fea-96b8-a9b9d6b24533).

##### A.2.2.1.1.3 - Founder Inputs [Core]  <!-- UUID: 1b66ee09-3e81-4ae3-b3df-69787e0f662a -->

The documents herein specify the Agent Founder’s inputs following the creation of the Scaffold Artifact.

###### A.2.2.1.1.3.1 - Founder Required Primitive Activation [Core]  <!-- UUID: 1a48e833-d960-4bdf-8f67-0f9d9307e00d -->

The Founder is responsible for Globally Activating the Agent Creation, Prime Transformation / Executor Transformation, Agent Token, Executor Accord, Root Edit, and Ecosystem Upkeep Fee Primitives.

The Primitives named above must first be Globally Activated before the Founder can Invoke them to finalize Agent setup. The Founder may choose to Globally Activate these Primitives individually at different times or all at once; only the Primitive Invocation must be done in a specified order.

###### A.2.2.1.1.3.2 - Founder Access [Core]  <!-- UUID: a4f65994-2526-4522-a986-cd444a5cb896 -->

_"_Founder Access" gives the Founder of an Agent the ability to freely edit the Scaffold Artifact, including Activating any desired Primitives and adding custom Omni Documents. "Founder Access" is revoked at the moment the Founder Invokes either the Prime Transformation or Executor Transformation Primitive. From that point on, the Founder cannot add or edit Omni Documents, but can only Activate and Invoke specific Primitives so that the Agent can complete setup. See [A.2.2.1.2.4.1 - Agent Launch And Sequence of Primitive Global Activation](2f5ff5c8-bcd1-44a4-ba56-2075ac8e9c61).

###### A.2.2.1.1.3.2.1 - Short Term Suspension of “Founder Access” [Core]  <!-- UUID: 5dd07957-8e5b-4694-a0ba-a8aa88863552 -->

In the short term, "Founder Access" will not be operational. Instead, if a Prime Founder wishes to edit their Scaffold Artifact, they must use the customary Atlas Edit Proposal processes specified in the Sky Core Atlas at [A.1.11.2 - Atlas Edit Weekly Cycle](14e99d92-71fc-44d9-9dbf-933bce2e1b32) or [A.1.12.2 - Atlas Edit Monthly Cycle](d2cbddd2-58ef-4311-a71d-d2c340364cb5).

###### A.2.2.1.1.3.3 - Founder Invokes Agent Creation Primitive [Core]  <!-- UUID: d0b283e9-dac1-49c6-8dd7-b061c7a87335 -->

To proceed to the next stage, the Founder must Invoke the Agent Creation Primitive. From the Agent’s perspective, invoking, or calling, a Primitive always involves submitting required inputs into the respective Primitive itself. Here, the Agent Founder must input the name of the Agent and an introduction providing a brief overview of the Agent’s vision or business model into the Agent Creation Primitive.

##### A.2.2.1.1.4 - Core GovOps Validates Agent Creation Primitive Inputs [Core]  <!-- UUID: 93d6147b-8760-431e-b38c-4a7afcb27e5f -->

Core GovOps validates the Founder’s inputs into the Agent Creation Primitive and the "Founder Access"-related edits to the Scaffold Artifact, ensuring that all information is well specified and that the Scaffold Artifact is aligned.

##### A.2.2.1.1.5 - Core GovOps Creates Genesis And SubProxy Accounts [Core]  <!-- UUID: 16d9dede-7fbf-4215-8e60-c06a8e6c3218 -->

After validating the Scaffold Artifact and Agent Creation Primitive inputs, Core GovOps creates a Genesis Account and SubProxy Account for the Agent. This data is automatically added to the Agent Creation Primitive.

##### A.2.2.1.1.6 - Founder Invokes Prime / Executor Transformation Primitive [Core]  <!-- UUID: 2592b3d0-531e-42a3-a098-cf4b82bdd567 -->

When ready, the Founder Invokes the Prime Transformation or Executor Transformation Primitive to become either a Prime Agent or Executor Agent, respectively.

##### A.2.2.1.1.7 - Core GovOps Validates Transformation Primitive Inputs [Core]  <!-- UUID: 05e70418-5dbf-4d02-9d2a-9afea6619dd0 -->

Upon successful validation by Core GovOps, the Transformation Primitive is deployed and the Agent Artifact is upgraded to reflect that the Agent is either a Prime Agent or an Executor Agent.

##### A.2.2.1.1.8 - Post-Transformation Primitive Artifact Freeze [Core]  <!-- UUID: 20f4cfe0-1855-4942-ac0d-f5cb738e82fc -->

After the Transformation Primitive is successfully Invoked, the Agent’s "Founder Access" is revoked. The Founder can no longer freely edit the Agent Artifact, but may only Invoke certain Primitives in a specified order until the Agent setup is complete.

##### A.2.2.1.1.9 - Founder Invokes Agent Token Primitive [Core]  <!-- UUID: f5132655-afdd-4a93-adbe-64526759720c -->

The Founder next Invokes the Agent Token Primitive to create a token for the Agent that can be used to raise capital, build a community, and conduct governance processes.

##### A.2.2.1.1.10 - Core GovOps Validates Agent Token Primitive Inputs [Core]  <!-- UUID: 416dc0f2-fb0d-4ea2-975d-9bf2d9b0e1d4 -->

Core GovOps reviews the inputs to the Agent Token Primitive to ensure that they are well specified and aligned.

##### A.2.2.1.1.11 - Core GovOps Mints Tokens [Core]  <!-- UUID: 0e033de5-ce15-45df-ae85-9ed69bd40da0 -->

After validating the Agent Token Primitive inputs, Core GovOps proceeds to mint the Agent’s initial supply of tokens according to the instructions specified in the Primitive.

##### A.2.2.1.1.12 - Agent Invokes Executor Accord Primitive [Core]  <!-- UUID: 9b074b3d-73db-4a3a-9491-571021e4e61b -->

The Agent must reach an understanding with an Operational Executor Agent that will operationalize the Agent’s strategy. After doing so, the Agent records this understanding by invoking the Executor Accord Primitive. Note that this step is only applicable to Prime Agents.

##### A.2.2.1.1.13 - Core GovOps Validates Executor Accord Primitive Inputs [Core]  <!-- UUID: c1ff42c9-1ffc-46f0-9dac-da54eb4eb042 -->

CoreGovOps reviews the inputs to the Executor Accord Primitive to ensure that there is a valid Executor Accord with an Executor Agent and that the terms of the Executor Accord are reasonably specific. Upon successful validation, the Executor Accord Primitive is considered successfully Invoked and the Artifact is upgraded to include the Executor Accord. Now that the Agent has a documented relationship with an Executor Agent, Core GovOps will no longer perform validation of the Agent’s Primitive inputs. Instead, Operational GovOps associated with the Executor Agent specified in the Executor Accord will carry out certain operational tasks on behalf of the Prime Agent see [A.1.14.3.4 - Agent Role Delineation](fdf32ca5-5e2e-481e-9047-4d1599547216).

##### A.2.2.1.1.14 - Agent Invokes Root Edit Primitive [Core]  <!-- UUID: 63f85a1a-da2d-4828-ae32-da56f46d500d -->

The Agent Invokes the Root Edit Primitive and sets up a governance process for voting to occur.

##### A.2.2.1.1.15 - Operational GovOps Validates Root Edit Primitive Inputs [Core]  <!-- UUID: d5ee3f2c-cd2f-4428-974b-341e4cce7295 -->

Operational GovOps reviews the inputs to the Root Edit Primitive to ensure it specifies a process that they can operationalize and does not conflict with any of the requirements regarding the voting process set forth in the Sky Core Atlas.

Upon validation, the Root Edit Primitive is considered successfully Invoked, and the Artifact is upgraded with its functionality. At this point the Agent is fully operational. The Agent Artifact can only be edited through a token holder vote or, if applicable, by the Operational Executor Facilitator as authorized by Omni Documents. The Agent can Invoke and deploy any Primitives that it has previously Activated and can also Activate additional Primitives through a Root Edit.

#### A.2.2.1.2 - Primitive Global Activation Status [Core]  <!-- UUID: dde8cf4c-4823-4fea-96b8-a9b9d6b24533 -->

The documents herein define Primitive Global Activation Status.

##### A.2.2.1.2.1 - Primitives Must First Be Activated To Be Invoked [Core]  <!-- UUID: dcd0bead-7ad1-4fe0-b485-b3565d670c78 -->

An Agent may only Invoke a Primitive that it has previously Globally Activated; the process of Invocation is defined below at [A.2.2.1.3.3 - Changing Primitive Instance Status](263f3b28-9cd4-4ba2-b8e5-152c2ce0c050). In this way, an Agent’s decision regarding which Primitives to Activate allows the Agent to express its strategy to token holders. For example, an Agent that was focused on asset gathering might Globally Activate the Distribution Reward and Integration Boost Primitives, but not the Allocation System Primitive.

##### A.2.2.1.2.2 - Initial Primitive Global Activation Status [Core]  <!-- UUID: 377150b3-d64b-4436-ab6d-758b05d82f26 -->

Scaffold Artifacts by default include all Sky Primitives. To begin with, all Sky Primitives have the Global Activation Status of `Inactive`; the exception is the Upkeep Rebate Primitive, which comes Globally Activated in all Scaffold Artifacts.

##### A.2.2.1.2.3 - Primitive Activation Does Not Require Invocation [Core]  <!-- UUID: 1560f392-db95-43d0-968b-af8d1afa4e84 -->

Activation gives the Agent the ability to Invoke a Primitive (thereby creating an instance of that Primitive), but does not require the Agent to do so.

##### A.2.2.1.2.4 - Changing A Primitive’s Global Activation Status [Core]  <!-- UUID: 51cfca28-c8de-457a-abc4-8ce1f64abb91 -->

An Agent can change the Global Activation Status of a Primitive as defined herein.

###### A.2.2.1.2.4.1 - Agent Launch And Sequence of Primitive Global Activation [Core]  <!-- UUID: 2f5ff5c8-bcd1-44a4-ba56-2075ac8e9c61 -->

Sky Primitives can be Globally Activated (and their instances later Invoked) by an Agent at different points in the Artifact’s lifecycle. The process is divided into three main stages, outlined in the documents herein.

###### A.2.2.1.2.4.1.1 - “Pre Transformation Primitive” Stage [Core]  <!-- UUID: b5cbcb47-ff44-4809-8071-2b5f7b30efbb -->

After the Scaffold Artifact has been established, but before invoking the Prime Transformation or Executor Transformation Primitive, the Agent Founder retains unilateral authority ("Founder Access") to Activate any desired Primitives while freely editing the Agent Artifact. The Founder must Globally Activate the Ecosystem Upkeep Fee Primitive during this stage. No Operational Executor Facilitator approval or token holder vote is required at this stage. See [A.2.2.1.1.3.2 - Founder Access](a4f65994-2526-4522-a986-cd444a5cb896).

###### A.2.2.1.2.4.1.2 - “Pre Root Edit Primitive” Stage [Core]  <!-- UUID: 7b25b220-92f9-4936-8296-31c0f3d8ddbc -->

After the Prime Transformation or Executor Transformation Primitive has been Invoked, but before the Root Edit Primitive is Invoked, the Agent Founder can no longer freely edit the Artifact. During this period, the Agent must Activate and Invoke (1) the Agent Token Primitive, then (2) the Executor Accord Primitive, and finally (3) the Root Edit Primitive, in that order, to complete its governance setup - assuming that these Primitives were not already Globally Activated during the "Pre Transformation Primitive" Stage. No other Primitives can be Globally Activated by the Agent during this period.

###### A.2.2.1.2.4.1.3 - “Post Root Edit Primitive” Stage [Core]  <!-- UUID: 857b85e5-b57e-4043-82eb-6fbb68cf1d51 -->

After the Root Edit Primitive is Invoked, changing the Global Activation Status of a Primitive - whether activating or deactivating - requires a token holder vote and review by the Operational Executor Facilitator.

###### A.2.2.1.2.4.2 - Global Primitive Deactivation [Core]  <!-- UUID: d0fb8761-2fcb-4d81-b498-38cd44f47fb0 -->

Generally, a Prime Agent may freely deactivate a Primitive’s Global Status pursuant to the governance process defined in its Root Edit Primitive. However, there are exceptions to this rule given the special functionality of certain Primitives. See [A.2.2.1.2.4.2.1 - Prohibition On Deactivating Certain Primitives](3ce3a1ae-9300-4159-9676-261d0404360f).

If a Primitive’s Global Status is deactivated, _all_ existing instances of that Primitive immediately become `Suspended`. While the Primitive remains Globally Inactive, the Agent is barred from creating new instances or reactivating existing instances of that Primitive.

###### A.2.2.1.2.4.2.1 - Prohibition On Deactivating Certain Primitives [Core]  <!-- UUID: 3ce3a1ae-9300-4159-9676-261d0404360f -->

The documents herein specify the Sky Primitives that, once Globally Activated, cannot be deactivated.

###### A.2.2.1.2.4.2.1.1 - Prohibition On Deactivating Genesis Primitives [Core]  <!-- UUID: 04bbf091-b2a8-47e4-ad03-f3fd66e70279 -->

Once Activated, the Agent Creation, Prime / Executor Transformation, and Agent Token Primitives cannot be deactivated. These Primitives are deployed once, and thereafter their Global Status is `Completed` and cannot be altered.

###### A.2.2.1.2.4.2.1.2 - Prohibition On Deactivating Executor Accord And Root Edit Primitives [Core]  <!-- UUID: a4797404-1015-4cd5-a2ea-bc1a2699b575 -->

To maintain recognized operational status within the ecosystem, Agents must have active Executor Accord and Root Edit Primitives at all times. Once Globally Activated, these Primitives cannot be deactivated, as doing so renders the Agent unable to operate or make further changes to its Artifact. Should an Agent seek to wind down, rather than deactivating these Primitives, it must follow the approved termination process defined in [A.1.14.5 - Agent Termination Protocol](fe833d0e-8451-45e0-84a5-229d6ec964a8).

###### A.2.2.1.2.4.2.1.3 - Prohibition On Deactivating Upkeep Rebate Primitive [Core]  <!-- UUID: 85121142-aa54-4957-b0e1-8f4294512c7e -->

The Upkeep Rebate Primitive is by default Globally Activated in all Scaffold Agent Artifacts; it is not possible to deactivate it.

###### A.2.2.1.2.4.2.1.4 - Prohibition On Deactivating Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: 984dcacc-d242-4203-90c2-d5cf61c92702 -->

An Agent must always have the Ecosystem Upkeep Fee Primitive Globally Activated; once Activated, it cannot be deactivated.

###### A.2.2.1.2.4.2.2 - Global Primitive Reactivation [Core]  <!-- UUID: cb452f09-007a-4000-a37f-46e8be48c066 -->

An Agent may reactivate a Globally Inactive Primitive according to the governance process defined in its Root Edit Primitive. Reactivating the Primitive restores the Agent’s ability to create new instances (via proper Invocation) but does _not_ automatically revive previously deactivated instances. Each existing instance remains inactive unless separately reactivated through the appropriate governance process.

#### A.2.2.1.3 - Primitive Instance Status [Core]  <!-- UUID: 4531962c-9847-40d6-b534-8a3a301703d0 -->

The documents herein define Primitive Instance Status.

##### A.2.2.1.3.1 - Primitive Instance Status Definition [Core]  <!-- UUID: f507250e-8558-4692-914d-7760ea266a50 -->

Each valid Invocation of a Primitive causes the Agent Artifact to be updated with a specific instance of a Primitive. For example, each Invocation of the Token SkyLink Primitive launches a SkyLink deployment to a specific blockchain. The Agent may manage each Primitive instance independently (e.g., Activate or suspend it as circumstances change). A Primitive instance thus has its own Status or life cycle that is independent of the Primitive’s Global Activation Status.

##### A.2.2.1.3.2 - Instance Status Values [Core]  <!-- UUID: d3908a6c-a5b4-40d3-a982-89ad606a24d9 -->

The documents herein specify the potential values of the Status of an instance of a Primitive. An instance of a Primitive must always have exactly one of these values.

###### A.2.2.1.3.2.1 - Active Instance Status [Core]  <!-- UUID: dfd19e92-2660-4393-8dff-a3a7e4ad75ff -->

The instance Status of `Active` indicates that an instance of a Primitive is fully operational and may be used for its intended purpose by the Agent and potentially other parties. For example, a Token SkyLink deployment is active and can be used to bridge tokens between blockchains.

###### A.2.2.1.3.2.2 - Suspended Instance Status [Core]  <!-- UUID: 3e5de640-5bc2-4953-a233-913e3337b4bb -->

The instance Status of `Suspended` indicates that an instance of a Primitive was `Active` at one point in time and may be `Active` again, but is not currently operational. This may be due to the Primitive not meeting performance expectations (e.g. for an Allocation System instance), security issues, or due to failure of the Agent operating the Primitive to satisfy other requirements such as those specified in the Risk Capital or Asset Liability Management frameworks.

###### A.2.2.1.3.2.3 - Completed Instance Status [Core]  <!-- UUID: 82b88f94-b83a-432a-bb8e-4e726535156a -->

The instance Status of `Completed` indicates that an Instance of a Primitive has reached a terminal state and will not become `Active` again. This status applies in two cases: 1) a previously active Instance has permanently ceased operations; or 2) an Instance designed for a single Invocation has achieved its intended outcome and requires no further management (e.g., the one-time deployment of the Prime Transformation Primitive).

##### A.2.2.1.3.3 - Changing Primitive Instance Status [Core]  <!-- UUID: 263f3b28-9cd4-4ba2-b8e5-152c2ce0c050 -->

A Prime Agent that has a Globally Active Primitive may freely create (assuming the Primitive was properly Invoked), suspend, archive, or update individual instances of that Primitive, subject to the rules defined in the Agent Artifact and the Sky Core Atlas. For example, the Agent may run multiple Integration Boost instances in parallel (each with its own markets and configurations), toggling them on or off as needed, without affecting the underlying Integration Boost Primitive’s Global Activation Status. Changing a Primitive’s Instance-Level Status can be effected through the governance process defined in the Root Edit Primitive, or through an appropriately configured Omni Document. See [A.1.14.2.7.2 - Omni Document Process](26ec6b08-8187-44b4-abb3-aee3868161a4).

#### A.2.2.1.4 - Invocation of Primitive Instance [Core]  <!-- UUID: da763556-c316-431d-b57e-cc4df5a52fb8 -->

The documents herein define the process by which an Agent may Invoke instances of Sky Primitives. If the Invocation is valid, the Agent Artifact is upgraded and the Agent gains the Primitives’ specific functionality.

##### A.2.2.1.4.1 - Invocation Status [Core]  <!-- UUID: 83ac15ef-30e5-4958-95f4-a7bc2de10e97 -->

The documents herein define the Statuses assigned to an Invocation that is in progress.

##### A.2.2.1.4.2 - Required Inputs Into Sky Primitive [Core]  <!-- UUID: 316daff4-3260-45da-afde-eea3d357b9eb -->

To Invoke a Primitive, an Agent must supply all required inputs as defined in the Sky Core Atlas. Every Primitive instance abides by a standardized data model specified at the Sky Core level, ensuring that all Prime Agents, Executor Agents and other actors are able to submit and track the necessary data reliably.

###### A.2.2.1.4.2.1 - Required Inputs Submitted To Powerhouse [Core]  <!-- UUID: 3a8fe63b-a95d-4c6d-b8ae-48f4fe62e4c3 -->

The actual submission and handling of these data inputs occurs exclusively through the Powerhouse interface, which serves as the Sky ecosystem’s shared data infrastructure. Powerhouse thus becomes the canonical gateway for exchanging information with the Primitive, enforcing consistency in both the format of the data and the steps taken to Invoke (and later update) the Primitive.

##### A.2.2.1.4.3 - Validation of Primitive Inputs [Core]  <!-- UUID: c1e8985f-a21d-4264-b0e3-7cebee40e062 -->

Once the Agent has provided all required inputs to the relevant Primitive(s), the proposed Artifact Update undergoes review / validation by designated actors such as Operational Executor Facilitators. The identity and responsibilities of these actors are detailed in subsequent documents of this Article.

##### A.2.2.1.4.4 - Token Holder Vote [Core]  <!-- UUID: a06c8e7a-e20f-459a-99e3-a62a5c0c4fd1 -->

After the Primitive inputs have been validated, Agent token holders vote on whether to upgrade the Artifact with the Primitive(s).

##### A.2.2.1.4.5 - Formal Integration Of Primitives [Core]  <!-- UUID: 6948d758-ad79-47b8-8466-74c75ec9db9e -->

If the vote is successful, the Agent Artifact is officially upgraded with a Primitive Instance, which latter has its own independent Status that is distinct from the Primitive’s Global Activation Status. See [A.2.2.1.3 - Primitive Instance Status](4531962c-9847-40d6-b534-8a3a301703d0). This upgrade means that the respective Primitive(s) is formally integrated into the Agent’s Artifact and the Atlas as a whole; the Prime Agent can now operationalize the Primitive’s special functionality.

#### A.2.2.1.5 - Primitives [Core]  <!-- UUID: 947a5b27-d2dc-41e4-b6fd-696e35e2929d -->

The documents herein list the current Sky Primitives and set forth the process for amending them. Each Primitive is defined in more detail below.

##### A.2.2.1.5.1 - Current Primitives [Core]  <!-- UUID: 203b8c79-c7cf-4fcc-94e3-5bf42f791619 -->

The current Sky Primitives are:

- Genesis Primitives
    - Agent Creation Primitive
    - Prime Transformation Primitive
    - Executor Transformation Primitive
    - Agent Token Primitive
- Operational Primitives
    - Executor Accord Primitive
    - Root Edit Primitive
    - Light Agent Primitive
- Ecosystem Upkeep Primitives
    - Ecosystem Upkeep Fee Primitive
    - Upkeep Rebate Primitive
- SkyLink Primitives
    - Token SkyLink Primitive
- Demand Side Stablecoin Primitives
    - Distribution Reward Primitive
    - Integration Boost Primitive
    - Pioneer Chain Primitive
- Supply Side Stablecoin Primitives
    - Allocation System Primitive
    - Risk Capital Rental Primitive
    - Asset Liability Management Rental Primitive
- Core Governance Primitives
    - Core Governance Reward Primitive

##### A.2.2.1.5.2 - Amendments To Primitives [Core]  <!-- UUID: 1a46fd49-7b37-4a14-a311-eb1dbe947d85 -->

The set of available Sky Primitives may be amended in accordance with the governance processes established in the Sky Core Atlas.

### A.2.2.2 - Primitive Process Definition Schema [Section]  <!-- UUID: bdbb8ac9-d87e-4052-9e69-8267f38a54cf -->

Process Definitions function as the first-class objects through which Sky Primitives transform high-level governance logic into actionable document-driven workflows. All Sky Primitive Process Definitions are structured according to a common data schema - a set of fields that describe when they can start, how they run step by step, and what they must input or produce upon completion.

The documents herein define this data schema for Sky Primitive Process Definitions, which are applied to the universal specifications for each Sky Primitive. This common data schema aligns the entire ecosystem, while each Agent Artifact automatically references and extends the universal rules to incorporate the Agent’s unique Instance-level strategies, parameters and document-driven process flows.

At present, only the Distribution Reward Primitive and the Integration Boost Primitive specifications are structured using this schema. In future iterations of the Atlas, the schema will be applied to all Primitive specifications in this Article.

#### A.2.2.2.1 - Process Initiation Logic [Core]  <!-- UUID: 5df2043c-000a-4627-9c3a-2fdc12b78c47 -->

The documents herein define when a Process is triggered, and what conditions must be satisfied, if any, for the Process to properly initiate.

##### A.2.2.2.1.1 - Triggers [Core]  <!-- UUID: 134d8e80-6ec7-49fe-b7bb-6846694be11c -->

The presence of a Time-Based Trigger or Document Update Trigger for a given Process does not necessarily mean such Trigger is the sole means to initiate the Process. For example, an Atlas Document that is external to the Sky Primitives specifications may authorize a Facilitator to manually initiate a process.

###### A.2.2.2.1.1.1 - Time-Based Trigger [Core]  <!-- UUID: 1040dd2b-e7f8-4f68-b6c6-4b910f394a5a -->

This field defines the triggering date/time for recurring or scheduled Processes.

###### A.2.2.2.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 16be342d-0584-4092-9943-97a8c4eeb672 -->

Document Update Triggers are a type of gating condition that automatically or deterministically compels initiation of a Process in response to a specific Core Atlas or Agent Artifact Document Update in a previous Process Definition.

Once the specified Atlas or Artifact Document Update occurs (and assuming any specified Dependencies are also met), the Process must be initiated.

If no such deterministic Document Update-based trigger exists for a Process to initiate, this field is set to "None."

##### A.2.2.2.1.2 - Dependencies [Core]  <!-- UUID: 64bec5dc-e288-4c8e-b638-c7180a92aca9 -->

Dependencies are gating conditions that must be satisfied for the Process to be able to proceed, regardless of a triggering event.

Examples of Dependencies include actors possessing suitable permissions, or a key stakeholder consenting to move forward.

If a trigger has occurred, but Dependencies are unmet, the Process cannot proceed.

#### A.2.2.2.2 - Process Flow [Core]  <!-- UUID: 6964c2d4-2994-487b-b68a-f1df5fa916f7 -->

This field describes the step-by-step operational procedure that occurs once a Process is properly initiated. A step can reference specific Core Atlas or Artifact Documents and broadly describe how their state is manipulated and decisions are made. More granular specifications regarding Document state changes are defined in the `Required Primitive Inputs` schema component [A.2.2.2.3 - Required Primitive Inputs](1474b30b-7e2b-4c9a-8624-3c2c5f53abc8). Process flow steps can both consume and produce relevant Document data.

#### A.2.2.2.3 - Required Primitive Inputs [Core]  <!-- UUID: 1474b30b-7e2b-4c9a-8624-3c2c5f53abc8 -->

This field specifies the Agent Artifact Documents and their associated fields that must be manipulated using the Powerhouse interface as part of a Process. If any of the required Inputs is missing or incorrect, the Process cannot be completed.

##### A.2.2.2.3.1 - Sequential Stages [Core]  <!-- UUID: e9422783-6196-4117-9099-b5ec0c338c05 -->

Some Processes require Primitive Inputs that are organized into multiple sequential stages (also called "Input stages"). Each Input stage must be completed before progressing to the next, ensuring that all dependencies and validations are met in order. Once an Input stage is completed, the subsequent Input stage is initiated automatically, continuing in this manner until all stages have been finished.

Upon completing the final Primitive Input stage, the Process Definition transitions to the `Required Outputs` schema component; this component defines the necessary updates to Sky Core Atlas or Agent Artifact Documents.

###### A.2.2.2.3.1.1 - Required Output Trigger [Core]  <!-- UUID: 9c4f4cad-5124-44d8-b19e-bd931fae7963 -->

Where a Process Definition has more than one set of `Required Outputs`, with each set corresponding to (or "triggered by") a particular Input stage, the `Required Primitive Inputs` schema component must explicitly correlate each Input stage with the `Required Outputs` it triggers. See [A.2.2.2.4.1 - Multiple Required Outputs And Their Respective Input Stage or Mutually Exclusive Pathway](10c53693-4784-40ad-a8c6-fd2551f14280).

##### A.2.2.2.3.2 - Mutually Exclusive Pathways [Core]  <!-- UUID: 926cd44b-e26c-4ae9-9091-d97c362d7e29 -->

Some Processes require Primitive Inputs that are organized into two or more mutually exclusive pathways (also "mutually exclusive Input pathways"). Once a pathway is chosen—either manually or automatically via the application of a defined decision or condition—the Process follows that pathway through to completion, rendering the other pathways inapplicable.

###### A.2.2.2.3.2.1 - Required Output Trigger [Core]  <!-- UUID: a61d4797-9a1f-455c-8fe1-b62164e702b3 -->

When multiple "sets" of `Required Outputs` exist, with each set corresponding to (or "triggered by") a particular Mutually Exclusive Input Pathway, the `Required Primitive Inputs` schema component must explicitly correlate each Mutually Exclusive Input Pathway with the `Required Outputs` it triggers. Because the pathways are mutually exclusive, only the Required Output set associated with the selected Pathway will be executed. The other Output sets remain inactive.

#### A.2.2.2.4 - Required Outputs [Core]  <!-- UUID: dee40c3b-2f89-44c6-8813-c48888df08a7 -->

This field specifies the particular Sky Core Atlas and/or Agent Artifact Documents that must be updated as an end result of a Process.

Where applicable, a Document Update can serve as a "trigger" that deterministically compels another Process Definition to be initiated by a system or actor. The `Trigger - Process` field links to the respective Process Definition that is triggered by the Required Output.

Some processes do not need formal "Required Outputs" because the only process flow step is a simple update of an Artifact Document. In these edge cases, the change specified in `Required Primitive Inputs` (e.g., toggling a field to Globally Activate a Primitive) fully completes the process, effectively completing it in a single step. Once the designated Document and field are updated as prescribed, the Process is considered finalized.

##### A.2.2.2.4.1 - Multiple Required Outputs And Their Respective Input Stage or Mutually Exclusive Pathway [Core]  <!-- UUID: 10c53693-4784-40ad-a8c6-fd2551f14280 -->

Where a Process Definition has more than one set of Required Outputs, and each set corresponds to (or is "triggered by") either a specific Input stage or a specific Mutually Exclusive Input Pathway, the Process Definition’s `Required Primitive Input` field must define which `Required Output` set is Invoked upon completion of that stage or pathway.

1. **For Sequential Stages**: When multiple sequential stages exist, each stage’s successful completion triggers its corresponding Required Output set. As subsequent stages are completed in turn, each triggers its own distinct Required Outputs, ensuring that all designated outputs eventually execute in sequence.
2. **For Mutually Exclusive Pathways**: If the Required Primitive Input process instead (or additionally) involves mutually exclusive paths, once a pathway is chosen—either manually or automatically by a specified condition—only the Required Output set tied to that pathway is applied. Outputs associated with the unselected/unexecuted pathways remain inactive.

##### A.2.2.2.4.2 - Agent Artifact Document Specification [Core]  <!-- UUID: 3b3e537c-4989-4674-94bc-05928146ab42 -->

In the Sky Primitives Data Schema, references to an Agent Artifact Document are made in terms of the generic Document type. See [A.1.2.2.2 - List Of Document Types And Their Specifications](428b7f2e-30b0-4119-a10a-9c3496f19bd2). In practice, each Agent has its own Instance of that Document type in its Artifact. Thus, when a Primitive’s process flow indicates that an Agent Artifact Document must be updated, it is to be interpreted as referring to the _specific Instance_ of that Document type in the Prime Agent’s Artifact.

### A.2.2.3 - Prerequisites For Activating Agent Creation Primitive [Section]  <!-- UUID: 9204bcaf-cfec-4f49-a115-31fad73ebd62 -->

The Agent Creation Primitive is the first Sky Primitive that must be activated by prospective Agent founders. Because an Agent Artifact does not yet exist at this stage, the prerequisite requirements set forth herein must be met, including off-chain obligations and governance outputs. Only after satisfying these prerequisites does the Agent Creation Primitive become accessible to the prospective founder.

#### A.2.2.3.1 - Agent Inputs [Core]  <!-- UUID: df925d98-2e73-4b26-859b-33caa8865f0f -->

The prospective Agent founder must deploy the required startup capital and pay the Agent creation fee.

##### A.2.2.3.1.1 - Capital Injection [Core]  <!-- UUID: bed7471a-54aa-4167-88dd-22ebd63f8827 -->

The required capital and the process for deploying it will be specified in a future iteration of the Atlas.

##### A.2.2.3.1.2 - Creation Fee [Core]  <!-- UUID: 708ad6b6-8e4a-46b3-9848-523d00a57420 -->

The prospective founder must pay the required creation fee. The required fee and the process for paying it will be specified in a future iteration of the Atlas.

#### A.2.2.3.2 - Core GovOps Outputs [Core]  <!-- UUID: e1cef578-801c-4905-a88b-e9703b048d2a -->

After the prospective Agent founder deploys the required startup capital and pays the Agent creation fee, Core GovOps creates a Proto-Agent and sets up a Scaffold Agent Artifact.

##### A.2.2.3.2.1 - Proto-Agent Creation [Core]  <!-- UUID: 1f577977-2f4c-41a0-a3ba-f09fc77b8d09 -->

Core GovOps creates a Proto-Agent with no specific functionality in the ecosystem.

##### A.2.2.3.2.2 - Scaffold Artifact Setup [Core]  <!-- UUID: f55fdc70-dfe4-4c52-9be4-10bf3a6dc990 -->

Core GovOps prepares a Scaffold Agent Artifact ("Scaffold Artifact") containing all Sky Primitives. In the Scaffold Artifact, the Upkeep Rebate Primitive is globally activated by default. See [A.2.2.1.2.2 - Initial Primitive Global Activation Status](377150b3-d64b-4436-ab6d-758b05d82f26). All other Primitives are initially set to `Inactive`. The Scaffold Artifact also includes an initial set of Omni Documents that provide general information about the Agent and organize the various Sky Primitive Instance Configuration Documents. Core GovOps must add the Scaffold Artifact to the Atlas’ Agent Artifact Scope.

##### A.2.2.3.2.3 - Address Deploying Capital [Core]  <!-- UUID: 39d1cae8-a070-47a2-b69b-96e0f4f6a080 -->

The address deploying the start-up capital is assigned `Founder Access` to the Scaffold Agent Artifact. See [A.2.2.1.1.3.2 - Founder Access](a4f65994-2526-4522-a986-cd444a5cb896).

### A.2.2.4 - Primitive Reward Infrastructure [Section]  <!-- UUID: ef3539fe-6d92-491c-a6a5-301a7875888d -->

The documents herein define the Integrator Program, the rules governing reward payments to Integrators across Sky Primitives, and the Demand Side Buffer that disburses such payments.

#### A.2.2.4.1 - Integrator Program [Core]  <!-- UUID: 37c38f07-b5a0-40df-939c-a54330ea3c7b -->

Integrators are actors that offer access to the Sky Protocol via their frontends or infrastructure. The documents herein define the Integrator Program, which includes the Distribution Reward and Integration Boost. (Base elements specific to the Integration Boost Primitive are defined in [A.2.2.9.2.2.1 - Base Elements](c398b383-3752-4534-aec6-4cd8e7292119))

##### A.2.2.4.1.1 - Integrator Requirements [Core]  <!-- UUID: 1c2b6983-1e03-41b9-a2bf-70f3eca19b98 -->

The documents herein define the requirements for Integrators.

###### A.2.2.4.1.1.1 - Alignment [Core]  <!-- UUID: 98e98f68-e749-4d0a-8972-7e36ed166326 -->

The Integrator must be aligned with Sky’s overall strategy regarding promoting adoption of USDS. This determination is made by Operational GovOps. Sky Core may choose whether to maintain an Integrator’s Reward Code in its sole and absolute discretion.

###### A.2.2.4.1.1.2 - Compliance With Local Laws And Regulations As A Condition Precedent To Integrators Receiving Distribution Rewards [Core]  <!-- UUID: f3b4b43d-b2e5-4f56-aeac-9627d3acc31e -->

This document and its subdocuments define the jurisdictional compliance rules applicable to Integrators that operate user-facing frontends that integrate with, and thus offer access to, the Sky Protocol and receive Distribution Rewards.

Integrators are solely responsible for complying with all relevant legal and regulatory requirements related to their participation in the Integrator Program. Integrators represent and warrant that their participation and activities under the Integrator Program are and will remain in full compliance with all applicable laws and regulations.

In connection with integrating with, and thereby providing access to, the Sky Protocol, Integrators must operate their frontends and infrastructure in compliance with all relevant legal and regulatory requirements in the jurisdictions applicable to their services. This requires compliance with all relevant legal and regulatory requirements in relation to frontend operations, marketing, and promotions in the jurisdictions where the Integrator provides access to the Sky Protocol through the integration.

An Integrator’s right to participate in the Integrator Program is contingent upon its ongoing compliance with all applicable laws and regulations.

###### A.2.2.4.1.1.2.1 - Consequence For Integrator Non-Compliance With Local Laws And Regulations [Core]  <!-- UUID: a01622fa-e81c-4bcb-8e31-7e66e36f2e57 -->

Sky Ecosystem Governance, in its absolute and unilateral discretion, retains the right to withhold, revoke, or demand immediate repayment of any and all Distribution Rewards from any Integrator that is determined, suspected, or alleged to be in violation of the Atlas or any legal, regulatory, or other obligations associated with its integration with, and provision of access to, the Sky Protocol.

###### A.2.2.4.1.1.2.2 - Removal From Integrator Program [Core]  <!-- UUID: 0bdcef8a-b851-42ed-b2e2-77d85c14dad0 -->

If Sky Governance removes an Integrator from the Integrator Program, Operational GovOps must remove the Integrator from the list of Current Integrators in [A.2.2.9.1.2.1.4.1.0.6.1 - List Of Current Integrators](efbe7903-a76e-40f0-a440-56e463283157) and deactivate the Instances of the Distribution Reward and Integration Boost Primitive associated with them.

##### A.2.2.4.1.2 - Integrator Applications [Core]  <!-- UUID: abc79583-78da-4578-9ae0-51dc322ed1cb -->

The documents herein define the process for applying to become an Integrator.

###### A.2.2.4.1.2.1 - Near Term Process [Core]  <!-- UUID: 7fe5dbb2-a07d-4ef9-94de-f54a2d568c57 -->

In the near term, applications are made directly to Operational GovOps. Operational GovOps must create and maintain a thread on the Sky Forum for Integrator Applications. Operational GovOps reviews applications and coordinates with Prime Agents interested in working with specific applicants. Operational GovOps issues Reward Codes to approved applicants.

###### A.2.2.4.1.2.1.1 - Integrator Program Applications [Active Data Controller]  <!-- UUID: d251bbac-df0e-4aff-a26b-33d60e153e19 -->

The list of Integrator Program applicants is defined as Active Data in [A.2.2.4.1.2.1.1.0.6.1 - List Of Integrator Applications](30db9618-ddf2-4df7-ad81-3f8f3395ff62).

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.2.4.1.2.1.1.0.6.1 - List Of Integrator Applications [Active Data]  <!-- UUID: 30db9618-ddf2-4df7-ad81-3f8f3395ff62 -->

The current Integrator Applications are:

###### A.2.2.4.1.2.2 - Long Term Process [Core]  <!-- UUID: 6283379c-d871-40a9-a915-d716d7df5642 -->

In the long term, Integrator applications come exclusively through Prime Agents. Prime Agents may establish whatever processes they deem appropriate to receive inbound requests for potential partnerships.

##### A.2.2.4.1.3 - Integrator Onboarding [Core]  <!-- UUID: 361e2e68-b2ab-4b1e-93ce-030cf25e509e -->

The documents herein define the process for onboarding new Integrators.

###### A.2.2.4.1.3.1 - Process [Core]  <!-- UUID: fc46821f-9d3d-4807-b519-d54faf546702 -->

When a Prime Agent’s Invocation of the Distribution Reward Primitive involves an actor who is not yet an approved Integrator, that actor must submit an Integrator Application to Operational GovOps. Operational GovOps determines whether the Integrator Requirements are met, and if so issues a Reward Code to the applicant. After the Reward Code has been issued, the Invocation of the Primitive may proceed. Operational GovOps may contract with another actor to perform the work of reviewing applications and issuing Reward Codes.

#### A.2.2.4.2 - Reward Recipient And Sharing [Core]  <!-- UUID: 40395562-d447-4c85-b670-c08d2341bcd2 -->

All Sky Primitive reward payments associated with an Integrator, including those provided through the Distribution Reward Primitive (see [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6)), the Integration Boost Primitive (see [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20)), the Core Governance Reward Primitive (see [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a)), the stUSDS Distribution Reward (see [A.4.4.1.3.7 - stUSDS Distribution Reward](673676d8-62a4-4422-b870-fbcdb3c0aabd)), and the srUSDS Distribution Reward (see [A.3.2.2.4.2.4 - srUSDS Distribution Reward](626f0f67-1df9-41e8-a4a6-230aa1ccc824)), are paid to the Prime Agent that manages the relationship with the Integrator. Any sharing of such reward payments with the Integrator is subject to bilateral negotiation between the Prime Agent and the Integrator. No party is contractually obligated to share any specific portion of these reward payments, including any downstream pass-through to end users.

#### A.2.2.4.3 - Demand Side Buffer [Core]  <!-- UUID: 862b6d83-f464-4125-8259-233b7de75ec4 -->

The Demand Side Buffer is the account used for disbursement of Distribution Reward and Integration Boost payments. The Demand Side Buffer is controlled by a multisig as specified in the documents herein. The balance of this account may be topped up through an Executive Vote.

##### A.2.2.4.3.1 - Demand Side Buffer Multisig Address [Core]  <!-- UUID: dadf97b5-1d71-42b2-9954-cd9a18d4345f -->

The address of the Demand Side Buffer Multisig on the Ethereum Mainnet is `0x5e2fEc3a3C4E63A422e45C1BB83EdB3a5aD0543B`.

##### A.2.2.4.3.2 - Demand Side Buffer Multisig Required Number Of Signers [Core]  <!-- UUID: 8e341f8c-be33-49c2-8345-76ecc3e1179c -->

The Demand Side Buffer Multisig has a 2/3 signing requirement.

##### A.2.2.4.3.3 - Demand Side Buffer Multisig Signers [Core]  <!-- UUID: af4edd62-8e3c-42d2-bf70-41a31570ab0b -->

The signers of the Demand Side Buffer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs.

##### A.2.2.4.3.4 - Demand Side Buffer Multisig Usage Standards [Core]  <!-- UUID: f489f6b8-67a9-49bd-ad98-a543757214b8 -->

The signers of the Demand Side Buffer Multisig must use the Multisig to disburse Distribution Reward and Integration Boost payments in accordance with the Atlas.

##### A.2.2.4.3.5 - Demand Side Buffer Multisig Modification [Core]  <!-- UUID: 379f5e3c-3ea4-4d82-a8bb-70e8d750e157 -->

Operational GovOps Soter Labs can change the signers of the Demand Side Buffer Multisig at any time, so long as there are at least three (3) signers and at least two-thirds of signers are required to execute transactions.

##### A.2.2.4.3.6 - Demand Side Buffer Auxiliary Accounts [Core]  <!-- UUID: dfc22e9d-139b-498c-a3d0-408503632f77 -->

Operational GovOps Soter Labs may establish auxiliary accounts on other blockchains to facilitate efficient distribution of Distribution Reward and Integration Boost payments to Integrators operating on those blockchains. Operational GovOps Soter Labs may move funds from the Demand Side Buffer Multisig to auxiliary accounts as necessary to facilitate such payments. Each auxiliary account must conform to the same standards as the Demand Side Buffer Multisig, specifically:

- a minimum of three (3) signers;
- at least two-thirds of signers are required to execute transactions; and
- all signers are controlled by Operational GovOps Soter Labs.

###### A.2.2.4.3.6.1 - List Of Auxiliary Accounts [Active Data Controller]  <!-- UUID: 32e27a27-7d1e-4acc-9b67-805eaedb7b97 -->

The list of auxiliary accounts is defined as Active Data in [A.2.2.4.3.6.1.0.6.1 - Current Auxiliary Accounts](620715c0-6260-4501-9d3f-50ef4f5fc572).

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps Soter Labs.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.2.2.4.3.6.1.0.6.1 - Current Auxiliary Accounts [Active Data]  <!-- UUID: 620715c0-6260-4501-9d3f-50ef4f5fc572 -->

The following auxiliary accounts are currently in use:

- Solana — `7Gf8AqAtmYkkVhQbbJr18RxVUuoGjA8ZEw3Af4NauyaY`

### A.2.2.5 - Genesis Primitives [Section]  <!-- UUID: 3d5e3668-8333-4908-adcc-5784cfe7f6b5 -->

Genesis Primitives are a category of Primitives addressing different aspects of initial Agent setup—such as Agent creation, token launch and configuration, and transformation pathways.

#### A.2.2.5.1 - Agent Creation Primitive [Core]  <!-- UUID: 82b95f6d-4883-4f08-ac3a-9d8189013fbe -->

This Primitive may only be Invoked after the prospective Agent founder meets the prerequisites defined in [A.2.2.3 - Prerequisites For Activating Agent Creation Primitive](9204bcaf-cfec-4f49-a115-31fad73ebd62), resulting in the creation of a Proto-Agent. Invoking the Agent Creation Primitive allows the Proto-Agent to establish its identity by declaring its name, as well as articulate its intended vision, business model or ecosystem goals.

##### A.2.2.5.1.1 - Agent Creation Primitive Process Definition [Core]  <!-- UUID: 46e64020-f283-48a6-b327-75ea15927ee4 -->

The documents herein define the Process Definition for initial setup and ongoing management of an Instance of the Agent Creation Primitive.

###### A.2.2.5.1.1.1 - Agent Creation Instance Setup Process [Core]  <!-- UUID: 754e1599-28d7-499a-b68f-e2155e87105a -->

The documents herein define the process for setting up an Instance of the Agent Creation Primitive.

###### A.2.2.5.1.1.1.1 - Founder Inputs [Core]  <!-- UUID: cfde405d-e7e1-48eb-b044-3e9514c0aa96 -->

The Founder uses the Powerhouse interface to input the Agent's name and an introduction outlining the Agent's vision.

###### A.2.2.5.1.1.1.2 - Validation [Core]  <!-- UUID: d2b0f57b-1596-4355-9c63-aec6466cf316 -->

Core GovOps validates the Founder’s inputs. This includes verifying that all of the documents created by the Founder using Founder Access are well-specified, that the documents are Aligned, and that all necessary Primitives to complete setup have been Activated. The necessary Primitives are the Agent Creation, Prime/Executor Transformation, Agent Token, Executor Accord, Root Edit, and Ecosystem Upkeep Fee Primitives. (See [A.2.2.1.1.3.1 - Founder Required Primitive Activation](1a48e833-d960-4bdf-8f67-0f9d9307e00d).) After confirming these conditions, Core GovOps creates a Genesis Account and a SubProxy Account for the Agent.

###### A.2.2.5.1.1.1.3 - Official Update Of Artifact [Core]  <!-- UUID: c73a1815-b2dc-4cec-9ef4-ae6e6aabf633 -->

After successful validation, the Agent Creation Primitive is considered successfully Invoked, and the Agent Artifact is officially upgraded to reflect an Agent Creation Primitive Instance, with a Status of `Completed`.

###### A.2.2.5.1.1.2 - Agent Creation Instance Ongoing Management [Core]  <!-- UUID: b7238f7c-253d-4881-bbb8-10e3ca2d62ba -->

The documents herein define the process for the ongoing management of an Instance of the Agent Creation Primitive.

###### A.2.2.5.1.1.2.1 - Agent Creation Primitive Results In One-Time Creation [Core]  <!-- UUID: 1ca2f5f3-1be7-4855-bbb7-49630e7e2ae6 -->

Because the Agent Creation Primitive is deployed solely to effect the one-time creation of the Agent, no further management process is needed post-deployment.

##### A.2.2.5.1.2 - Agent Creation Primitive Input Requirements [Core]  <!-- UUID: 7a7a2631-e5e2-4b63-8f2b-45ecaec7af2e -->

The documents herein define the required inputs for a valid Invocation of the Agent Creation Primitive. If any input is noncompliant or omitted, the Primitive will be invalidated.

###### A.2.2.5.1.2.1 - Global Activation Status [Core]  <!-- UUID: f9de4749-2bf4-4871-a5a8-6fb6849af7ad -->

The Agent Creation Primitive must be Globally Activated.

###### A.2.2.5.1.2.2 - Agent Name And Introduction [Core]  <!-- UUID: c7e7507e-4d57-4842-932c-88cf232a53a8 -->

The Agent Creation Primitive must specify the Agent’s Name and provide a brief overview of its vision or business model.

###### A.2.2.5.1.2.3 - Agent Foundation [Core]  <!-- UUID: 1e590ccb-8c81-47e3-900b-72825da38e54 -->

The Agent Creation Primitive must specify the Foundation associated with the Agent, if any.

###### A.2.2.5.1.2.4 - Agent Development Company [Core]  <!-- UUID: eb40af22-a20b-4bf7-b592-d491e6fc33be -->

The Agent Creation Primitive must specify the Development Company associated with the Agent, if any.

###### A.2.2.5.1.2.5 - Agent SubProxy Account [Core]  <!-- UUID: 585dc747-65f1-4443-b61b-9779031f9258 -->

The Agent Creation Primitive must specify the SubProxy address of the Agent. This field is populated by Core GovOps. The SubProxy is an account that serves as the Agent’s treasury. The SubProxy Account is controlled by Sky Governance.

###### A.2.2.5.1.2.6 - Agent Genesis Account [Core]  <!-- UUID: 761966db-e9db-41f8-a9fe-cf8b0c1a7d26 -->

The Agent Creation Primitive must designate the Genesis Account. This field is populated by Core GovOps. The Genesis Account initially controls 100% of the tokens of the Agent. The Genesis Account is initially controlled by the Agent Founder.

#### A.2.2.5.2 - Prime Transformation Primitive [Core]  <!-- UUID: 81411106-fd6d-4f9c-b3ae-7af7b5e62482 -->

Prior to Activating this Primitive, a Proto-Agent has been created, meaning it has not yet adopted any specialized role. Since a Proto-Agent cannot perform actions in the Sky Ecosystem, it must first transform into either a Prime Agent or Executor Agent to gain functionality. The Prime Transformation Primitive defined herein allows an Agent to transform into a Prime Agent, subject to certain conditions.

##### A.2.2.5.2.1 - Prime Transformation Primitive Process Definition [Core]  <!-- UUID: ddfbb811-94f5-43bb-bf5e-a9bab2be046d -->

The documents herein define the Process Definition for initial setup and ongoing management of an Instance of the Prime Transformation Primitive.

###### A.2.2.5.2.1.1 - Prime Transformation Primitive Setup Process [Core]  <!-- UUID: 3f1824b6-5325-43ac-b3d5-151fb0f55dec -->

The documents herein define the process for setting up the Prime Transformation Primitive.

###### A.2.2.5.2.1.1.1 - Agent Inputs [Core]  <!-- UUID: aef13d1b-08d6-4c89-8858-65f8acbe4adc -->

The Proto-Agent must use the Powerhouse interface to input their desired Agent Type into the Primitive. For the Prime Transformation Primitive process, the Proto-Agent must specify ‘Prime Agent’ as their desired Agent Type.

###### A.2.2.5.2.1.1.2 - Validation [Core]  <!-- UUID: 43598845-989e-44fc-8cb4-c60b67fd1f28 -->

Core GovOps validates the Proto-Agent’s inputs, namely, the Agent Type. Additionally, Core GovOps performs a further review to confirm that all the documents created by the Founder using Founder Access are well-specified, that the documents are Aligned, and that all necessary Primitives have been Activated. The necessary Primitives are the Agent Creation, Prime/Executor Transformation, Agent Token, Executor Accord, Root Edit, and Ecosystem Upkeep Fee Primitives. (See [A.2.2.1.1.3.1 - Founder Required Primitive Activation](1a48e833-d960-4bdf-8f67-0f9d9307e00d).)

###### A.2.2.5.2.1.1.3 - Official Update Of Artifact [Core]  <!-- UUID: 2182141b-a2bc-46bc-b9a6-2cb62e55b302 -->

After successful validation, the Prime Transformation Primitive is considered successfully Invoked, and the Agent Artifact is officially upgraded to reflect a Prime Transformation Primitive Instance, with a Status of `Completed`.

###### A.2.2.5.2.1.2 - Prime Transformation Primitive Ongoing Management [Core]  <!-- UUID: c1cae3bb-283e-44bf-9860-b721a1625bae -->

The documents herein define the process for the ongoing management of an Instance of the Prime Transformation Primitive.

###### A.2.2.5.2.1.2.1 - Prime Transformation Primitive Results In One-Time Creation [Core]  <!-- UUID: 248bfb90-8bd8-410a-86d3-527e355eca43 -->

Because the Prime Transformation Primitive is deployed solely to effect the one-time transformation of the Proto-Agent, no further management process is needed post-deployment.

##### A.2.2.5.2.2 - Prime Transformation Primitive Input Requirements [Core]  <!-- UUID: 062b9275-9778-4f24-b0e5-bccf9129c179 -->

The documents herein define the required inputs for a valid Invocation of the Prime Transformation Primitive. If any input is noncompliant or omitted, the Primitive will be invalidated.

###### A.2.2.5.2.2.1 - Global Activation Status [Core]  <!-- UUID: cd67fe26-d82d-4859-be8d-36f1a9c42a65 -->

The Prime Transformation Primitive must be Globally Activated.

###### A.2.2.5.2.2.2 - Prime Agent Type [Core]  <!-- UUID: 857468db-7ff3-4986-b808-a7cd9854000a -->

The Prime Transformation Primitive must specify the Prime Agent’s Type, e.g., that it is a Prime Agent.

#### A.2.2.5.3 - Executor Transformation Primitive [Core]  <!-- UUID: 2f249be5-8edb-41e4-b429-734e1ba2cbc7 -->

The Executor Transformation Primitive allows an Agent to transform into an Executor Agent, subject to certain conditions.

#### A.2.2.5.4 - Agent Token Primitive [Core]  <!-- UUID: 2047c361-db28-4952-a70c-83d07b562064 -->

The Agent Token Primitive enables Agents to define, mint, and distribute their governance tokens including foundation allocations, token rewards, and airdrops.

##### A.2.2.5.4.1 - Agent Token Primitive Process Definition [Core]  <!-- UUID: f7a81be7-057c-4a05-97ab-78a37c674010 -->

The documents herein define the Process Definition for initial setup and ongoing management of an Instance of the Agent Token Primitive.

###### A.2.2.5.4.1.1 - Agent Token Primitive Setup Process [Core]  <!-- UUID: 3e49628d-1f82-4980-9855-75ad5e86aa54 -->

The documents herein define the process for setting up the Agent Token Primitive.

###### A.2.2.5.4.1.1.1 - Agent Inputs [Core]  <!-- UUID: f74588a5-cbde-4635-9e18-bca3d9c80612 -->

The Agent must use the Powerhouse interface to input key data into the Agent Token Primitive, including token name, ticker, symbol, genesis supply, total supply, distribution rules, emissions schedule, pending token address and token admin address. The token admin address should be the Agent SubProxy Account. The Agent must also specify whether token emissions beyond the current supply have been irreversibly disabled.

###### A.2.2.5.4.1.1.2 - Validation [Core]  <!-- UUID: 6f63137d-5385-46e9-96ac-fc16a568f54a -->

Core GovOps validates the Agent’s inputs.

###### A.2.2.5.4.1.1.3 - Official Update Of Artifact [Core]  <!-- UUID: 309e17ed-c75a-48f5-859f-70a5cb29a1f8 -->

After successful validation, the Agent Token Primitive is considered successfully Invoked. The Agent Artifact is officially upgraded to reflect an Agent Token Primitive Instance, with a Status of `Active`.

###### A.2.2.5.4.1.1.4 - Core GovOps Output [Core]  <!-- UUID: d26166c3-b07f-4583-8303-051a90468ed3 -->

Upon successful validation, the token contract can now be deployed on-chain by Core GovOps. The minted supply must be allocated as specified in the Agent Token Primitive Instance. The Primitive is automatically updated to replace the pending token address with the actual token address.

###### A.2.2.5.4.1.2 - Agent Token Primitive Ongoing Management [Core]  <!-- UUID: d8f6b024-f4f8-4897-99f2-d433137c8850 -->

The documents herein define the process for the ongoing management of an Instance of the Agent Token Primitive.

###### A.2.2.5.4.1.2.1 - Agent Token Primitive Results In One-Time Creation [Core]  <!-- UUID: 0489781a-243c-4704-86e5-efe422cdd41c -->

Because the Agent Token Primitive is deployed solely to create a one-off Token for an Agent, no further management process is needed post-deployment.

##### A.2.2.5.4.2 - Agent Token Primitive Input Requirements [Core]  <!-- UUID: 9d88d70e-7dfc-42f3-9d58-0d2a905861fd -->

The documents herein define the required inputs for a valid Invocation of the Agent Token Primitive. If any input is noncompliant or omitted, the Primitive will be invalidated.

###### A.2.2.5.4.2.1 - Global Activation Status [Core]  <!-- UUID: fb858d4e-5d42-4496-807b-979e1946f8f0 -->

The Agent Token Primitive must be Globally Activated.

###### A.2.2.5.4.2.2 - Agent Token Name [Core]  <!-- UUID: 98fa133d-878a-4337-9d47-ad01ef19b9bb -->

The Agent Token Primitive must specify the name of the token.

###### A.2.2.5.4.2.3 - Agent Token Symbol [Core]  <!-- UUID: 46bbc08e-dcfc-4ed5-9e2f-3e78fd8735f9 -->

The Agent Token Primitive must specify the symbol of the token.

###### A.2.2.5.4.2.4 - Agent Token Genesis Supply [Core]  <!-- UUID: ed342c6e-15ae-4c95-ad4e-4702c27eba62 -->

The Agent Token Primitive must specify the genesis supply of the token.

###### A.2.2.5.4.2.5 - Agent Token Address [Core]  <!-- UUID: 745126ca-1d64-461e-b8b9-603216d7e74b -->

The Agent Token Primitive must specify either the pending or permanent address of the token (depending on whether the Primitive has been successfully Invoked).

###### A.2.2.5.4.2.6 - Agent Token Admin [Core]  <!-- UUID: 70e08dd1-8a2d-441b-95c4-92bce3bd37e8 -->

The Agent Token Primitive must specify the Admin of the token.

###### A.2.2.5.4.2.7 - Agent Token Emissions [Core]  <!-- UUID: 0f71bdc3-f18d-4e6f-8041-d73026a91d27 -->

The Agent Token Primitive must specify whether token emissions beyond the current supply have been irreversibly disabled. Once Disabled is set to `True`, the action cannot be undone by the Agent. Sky Governance retains the ability to revert the Disabled setting where the Agent is in violation of Risk Capital requirements and emissions are required by the Risk Framework.

###### A.2.2.5.4.2.8 - Agent Token Distribution Rules [Core]  <!-- UUID: 3d43ba11-ac87-41a5-a98d-c80071aaf1eb -->

The Agent Token Primitive must specify the process for distributing the initial token supply.

### A.2.2.6 - Operational Primitives [Section]  <!-- UUID: 0192ec95-9207-480e-8c51-88d2a1da95ad -->

Operational Primitives are a category of Primitives enabling the Agents’ own operation and governance and AI features, as well as the ability to create derivative Light Agents.

#### A.2.2.6.1 - Executor Accord Primitive [Core]  <!-- UUID: 88017877-3ec1-4c43-a035-6bebdf11d9bb -->

The Executor Accord Primitive is the foundational mechanism that allows Prime Agents to operate autonomously according to the strategy specified in their Agent Artifacts with automated operational insurance provided by separate Operational Executor Agents that delegate the work to GovOps actors.

##### A.2.2.6.1.1 - Executor Accord Primitive Process Definition [Core]  <!-- UUID: b2b42304-f715-4cc2-8fbf-68c794876386 -->

The documents herein define the Process Definition for initial setup and ongoing management of an Instance of the Executor Accord Primitive.

###### A.2.2.6.1.1.1 - Executor Accord Primitive Setup Process [Core]  <!-- UUID: af7c2593-b397-4fff-9b81-3d640508a163 -->

The documents herein define the process for setting up an Instance of the Executor Accord Primitive.

###### A.2.2.6.1.1.1.1 - Agent Inputs [Core]  <!-- UUID: d082d5de-a0b2-4441-8ba8-06d1e5fe2aed -->

The Prime Agent and Operational Executor Agent must come to a consensus about the details of the Executor Accord. These details must be entered into the Powerhouse interface along with independent confirmation from each Agent that they agree to those terms.

###### A.2.2.6.1.1.1.2 - Validation [Core]  <!-- UUID: dad19a7b-769c-43e3-a7b9-ce91d267c3b1 -->

Core GovOps validates the Agent’s inputs, ensuring that the terms of the Executor Accord are reasonably specific.

###### A.2.2.6.1.1.1.3 - Official Update Of Artifact [Core]  <!-- UUID: 458ec13a-5352-4720-a6eb-70f1bec6cb20 -->

After successful validation, the Executor Accord Primitive is considered successfully Invoked. The Agent Artifact is officially upgraded to reflect an Executor Accord Primitive Instance, with a Status of `Active`.

###### A.2.2.6.1.1.1.4 - Operational GovOps Takes Over Operational Duties [Core]  <!-- UUID: 8179ca9b-2875-4f7c-9573-9ed6fc5f91cf -->

Upon successful validation, the Prime Agent has a documented relationship with an Executor Agent and so Core GovOps will no longer perform validation of the Agent’s Primitive inputs. Instead, the Operational GovOps associated with the Executor Agent specified in the Executor Accord will carry out operational tasks on behalf of the Prime Agent.

###### A.2.2.6.1.1.2 - Executor Accord Primitive Ongoing Management [Core]  <!-- UUID: 8fe7d3f4-51bc-41bb-95b0-6dfe26fab562 -->

The documents herein define the process for the ongoing management of an Instance of the Executor Accord Primitive.

##### A.2.2.6.1.2 - Executor Accord Primitive Required Inputs [Core]  <!-- UUID: 5785964a-75ca-4109-af39-5ae1e872b89d -->

The documents herein define the required inputs for a valid Invocation of the Executor Accord Primitive. If any input is noncompliant or omitted, the Primitive will be invalidated and the Executor Accord will not be set up.

###### A.2.2.6.1.2.1 - Executor Accord Primitive Activation Status [Core]  <!-- UUID: 7dcc0b40-f577-4590-92d2-62697bfff33a -->

The Executor Accord Primitive must be Globally Activated.

###### A.2.2.6.1.2.2 - Executor Accord Terms [Core]  <!-- UUID: 2ac80f9d-744d-4dde-9ecd-9497642716dc -->

The Executor Accord Primitive must include the terms of the Executor Accord between the Prime Agent and Operational Executor Agent.

###### A.2.2.6.1.2.3 - Agent Agreement [Core]  <!-- UUID: bf03d18d-e5f9-434c-9aff-f6f0679f5746 -->

The Executor Accord Primitive must include independent confirmation from each Agent that they agree to the terms of the Executor Accord.

#### A.2.2.6.2 - Root Edit Primitive [Core]  <!-- UUID: 78488c6b-d77f-4344-b954-476e415a2c7d -->

The Root Edit Primitive allows Prime Agents, through a token holder vote, to direct the Operational Executor Agent specified in the Executor Accord Primitive to directly modify the Prime Agent Artifact.

##### A.2.2.6.2.1 - Root Edit Primitive Process Definition [Core]  <!-- UUID: f543db65-dac7-494d-bd0d-a24bf600157d -->

The documents herein define the Process Definition for initial setup and ongoing management of an Instance of the Root Edit Primitive.

###### A.2.2.6.2.1.1 - Root Edit Primitive Setup Process [Core]  <!-- UUID: 1fbca4e2-e89f-4819-afba-e58702ca2ed9 -->

The documents herein define the process for setting up an Instance of the Root Edit Primitive.

###### A.2.2.6.2.1.1.1 - Agent Inputs [Core]  <!-- UUID: 131380cc-df22-4862-a275-49e6a7302cf8 -->

The Agent must use the Powerhouse interface to specify the process by which Root Edits occur. See [A.1.14.2.7 - Artifact Edit Processes](2be8d2f0-bf02-4aa1-ad37-afb7a811a3b8).

###### A.2.2.6.2.1.1.2 - Validation [Core]  <!-- UUID: 2a466974-af55-4d3f-84a5-7ac840ffb620 -->

Core GovOps validates the Agent’s inputs.

###### A.2.2.6.2.1.1.3 - Official Update Of Artifact [Core]  <!-- UUID: 3a95c852-efc0-43aa-b4fe-358332aaaf74 -->

After successful validation, the Root Edit Primitive is considered successfully Invoked. The Agent Artifact is officially upgraded to reflect a Root Edit Primitive Instance, with a Status of `Active`.

###### A.2.2.6.2.1.2 - Root Edit Primitive Ongoing Management [Core]  <!-- UUID: 023847b4-9987-449f-9f2c-6c719856295f -->

The documents herein define the process for the ongoing management of an Instance of the Root Edit Primitive.

###### A.2.2.6.2.1.2.1 - Root Edit Primitive Artifact Edit Proposal [Core]  <!-- UUID: 71ae684b-da79-4ece-ab38-91a498b3bdb1 -->

The process for using the Root Edit Primitive begins with a party presenting a proposal for an Artifact Edit. The Root Edit Primitive specifies the requirements to submit a proposal, the required form of the proposal, and any other prerequisites that must be satisfied prior to the proposal being voted on.

###### A.2.2.6.2.1.2.2 - Root Edit Primitive Review By Operational Facilitator [Core]  <!-- UUID: 823cad54-4438-4ec3-9e13-d2624795fabd -->

The Operational Facilitator reviews the proposal. This review encompasses two aspects. First, the Operational Executor reviews the proposal for alignment with the Atlas. Second, the Facilitator reviews the proposal for compliance with any requirements set out in the Root Edit Primitive for the Agent, such as eligible actors to submit proposals, form of the proposal, or required time for review before submitting a proposal.

###### A.2.2.6.2.1.2.3 - Root Edit Primitive Voting [Core]  <!-- UUID: 7e4574c0-a83c-4e3f-bfa6-1f66db2a0aed -->

If the Operational Facilitator concludes that the proposal is aligned with the Atlas and consistent with the process specified in the Root Edit Primitive, then the Operational Facilitator moves forward with conducting the vote. The Root Edit Primitive specifies how the vote should be conducted (e.g. on-chain or off-chain), the time period over which voting should occur, and other relevant parameters for the vote such as quorum and approval requirements.

###### A.2.2.6.2.1.2.4 - Root Edit Primitive Artifact Update [Core]  <!-- UUID: 34d06691-afc4-4ade-9ada-ad180c2aef0f -->

After the voting period ends, the Operational Facilitator reviews the outcome of the vote. If the vote is successful, the Operational Facilitator actions the Artifact Edit in the Powerhouse system. In either case, the Operational Facilitator records the outcome of the vote, including all pertinent materials, in the Powerhouse system.

##### A.2.2.6.2.2 - Root Edit Primitive Required Inputs [Core]  <!-- UUID: cec43505-2bf3-48ce-81d9-852f65edc468 -->

The documents herein define the required inputs for a valid Invocation of the Root Edit Primitive. If any input is noncompliant or omitted, the Primitive will be invalidated and the Root Edit Primitive will not be set up.

###### A.2.2.6.2.2.1 - Root Edit Primitive Activation Status [Core]  <!-- UUID: 416b0a3a-fa97-40ad-8b58-50650f4a956b -->

The Root Edit Primitive must be Globally Activated.

###### A.2.2.6.2.2.2 - Artifact Edit Process [Core]  <!-- UUID: dc7fd889-80dd-4ac0-b807-f01ab440ba8a -->

The Root Edit Primitive must specify the process by which updates to the Agent Artifact may be made by Agent token holder vote. The details of this process may be specified by the Agent, subject to the following conditions: (1) Agent token holders must vote to approve Artifact Edit proposals, (2) the Operational Facilitator must review each proposal for alignment and conformance with the process specified in the Root Edit Primitive, (3) the vote must be conducted by the Operational Facilitator, and (4) the Operational Facilitator must action the Artifact Edit if the vote passes. The process definition must include the elements included in the documents herein.

###### A.2.2.6.2.2.2.1 - Proposal Format [Core]  <!-- UUID: 7a473c50-f947-481b-8466-468b8d1708d9 -->

The Root Edit Primitive must specify the required format of proposals.

###### A.2.2.6.2.2.2.2 - Actors Eligible To Submit Proposals [Core]  <!-- UUID: b5e21f94-5239-44c5-8eec-b5a5e6e05cf9 -->

The Root Edit Primitive must specify the requirements for actors to be eligible to submit proposals.

###### A.2.2.6.2.2.2.3 - Requirements For Proposals To Be Included In Vote [Core]  <!-- UUID: 0580f68b-06b4-41b0-b091-c88c8e6a0f81 -->

The Root Edit Primitive must specify the requirements for proposals to be included in a vote, such as any required review period or any reviews that must be conducted by other parties such as expert advisors.

###### A.2.2.6.2.2.2.4 - Voting Period [Core]  <!-- UUID: 0ca3f0ee-92ee-420e-915d-37aae1ab4848 -->

The Root Edit Primitive must specify the period over which voting should occur.

###### A.2.2.6.2.2.2.5 - Quorum Requirement [Core]  <!-- UUID: d4ad86a0-ec69-49b6-a794-6826cde3be0e -->

The Root Edit Primitive must specify the percent of outstanding tokens that must participate in a vote for it to be considered valid.

###### A.2.2.6.2.2.2.6 - Approval Threshold [Core]  <!-- UUID: 0c36f76d-17de-4958-bace-d1b1d7473982 -->

The Root Edit Primitive must specify the percent of tokens participating in the vote that must vote in favor of the proposal for it to be approved.

###### A.2.2.6.2.2.2.7 - Handling Of Emergency Or Urgent Situations [Core]  <!-- UUID: dda24bc9-d7e3-4593-9cdd-afe62355d198 -->

The Root Edit Primitive must specify any procedures for expedited voting in emergency or urgent situations.

###### A.2.2.6.2.2.2.8 - Special Voting Processes [Core]  <!-- UUID: b6fa5678-0b62-4607-b0e9-b3d27f57f689 -->

The Root Edit Primitive must specify any exceptions to the general process, such as subject matter requiring supermajority approval.

###### A.2.2.6.2.2.2.8.1 - Agent Termination Process [Core]  <!-- UUID: 82f9f4b9-76db-4ad7-94af-200ffe7c3b75 -->

The Agent Termination Process, as specified in [A.1.14.5 - Agent Termination Protocol](fe833d0e-8451-45e0-84a5-229d6ec964a8), deviates from the general Artifact Edit Process and follows the special voting process specified in the documents herein.

###### A.2.2.6.2.2.2.8.1.1 - Voting Period [Core]  <!-- UUID: 02fb768f-d21e-4c00-baf4-3bc9ac999269 -->

The Root Edit Primitive must specify a voting period of at least 14 days.

###### A.2.2.6.2.2.2.8.1.2 - Quorum Requirement [Core]  <!-- UUID: 119efbc0-f67d-4719-8180-e41333a3edd4 -->

The Root Edit Primitive must specify a minimum quorum of at least 20% of outstanding tokens.

###### A.2.2.6.2.2.2.8.1.3 - Approval Threshold [Core]  <!-- UUID: f6dc0c8e-7c22-445b-a42a-c6ab1250a4d8 -->

The Root Edit Primitive must specify a supermajority approval threshold where at least two-thirds (2/3) of votes cast are in favor.

###### A.2.2.6.2.2.2.8.1.4 - Required Notice [Core]  <!-- UUID: 42cedad0-9458-4f45-a87b-2313df539311 -->

The Root Edit Primitive must require the Operational Facilitator to issue advance notice of the Agent's proposed termination and the subsequent Agent vote in the Sky Forum.

###### A.2.2.6.2.2.2.8.1.5 - Compliance Deadline For Existing Prime Agents [Core]  <!-- UUID: 56c255d4-a827-43a5-8eec-44b9d629023c -->

Existing Prime Agents whose Root Edit Primitive does not already incorporate the requirements specified in [A.2.2.6.2.2.2.8.1 - Agent Termination Process](82f9f4b9-76db-4ad7-94af-200ffe7c3b75) must update their Agent Artifact to include them by September 1, 2026.

##### A.2.2.6.2.3 - Short-Term Limitations On Usage Of Root Edit Primitive [Core]  <!-- UUID: 459f257e-ef68-43b0-8d39-7836d98067ff -->

In the short term, usage of the Root Edit Primitive by Prime Agents will be limited as specified in the documents herein.

###### A.2.2.6.2.3.1 - Limitations On Usage Of Root Edit Primitive Prior To Independent Governance [Core]  <!-- UUID: 8c15762a-ea7e-4c6d-9089-60d30c219c0f -->

Until a Prime Agent has [A.0.1.1.54 - Independent Governance](6e1c1d71-7f57-4842-9767-7de8f27a532a), the Root Edit Primitive will not be operational. Instead, if a Prime Agent wishes to edit its Agent Artifact, it must use the customary Atlas Edit Proposal processes specified in the Sky Core Atlas at [A.1.11.2 - Atlas Edit Weekly Cycle](14e99d92-71fc-44d9-9dbf-933bce2e1b32) or [A.1.12.2 - Atlas Edit Monthly Cycle](d2cbddd2-58ef-4311-a71d-d2c340364cb5). The process for Prime Agents to use the Atlas Edit Proposal process is further specified in [A.2.2.6.2.3.2 - Atlas Edit Proposal Process For Prime Agents](364e52eb-4529-46a9-9852-edaaab88baeb).

###### A.2.2.6.2.3.2 - Atlas Edit Proposal Process For Prime Agents [Core]  <!-- UUID: 364e52eb-4529-46a9-9852-edaaab88baeb -->

Prime Agents that do not have an operational Root Edit Primitive must work with Core GovOps to use the Atlas Edit Weekly Cycle (see [A.1.11.2 - Atlas Edit Weekly Cycle](14e99d92-71fc-44d9-9dbf-933bce2e1b32)) process to update their Agent Artifacts, as specified in the documents herein.

###### A.2.2.6.2.3.2.1 - Prime Agent Submits Draft Proposal To Core GovOps [Core]  <!-- UUID: 461272f0-e9ae-43df-9571-4be49a2286c7 -->

The Prime Agent must submit a draft of the proposed edit to Core GovOps by 23:59 UTC on Monday in a given week. The draft need not be in the form of Atlas documents but should reflect a finished work product of the Prime Agent that is logically organized, contains all pertinent information, and is free of ambiguities to the best of the Prime’s ability.

###### A.2.2.6.2.3.2.2 - Core GovOps Submits Atlas Edit Weekly Cycle Proposal [Core]  <!-- UUID: 07d1ed44-c457-49b9-a054-50e26aa70acc -->

Upon receiving the draft from the Prime Agent, Core GovOps drafts a formal Atlas Edit Weekly Cycle proposal containing the relevant content, shares a draft with the Prime Agent for review, and then submits that proposal to be voted on Monday of the following week.

###### A.2.2.6.2.3.2.2.1 - Potential Delays In Submission [Core]  <!-- UUID: 4b37392d-9c0f-4572-8293-e7c6b3fc3743 -->

Core GovOps may in their discretion delay submitting a proposed edit based on factors including, but not limited to:

- the size of the proposed edit;
- any ambiguities in the proposed edit;
- broader issues raised by the proposed edit requiring other changes or consultation with other stakeholders;
- delays by the Prime Agent in responding to questions or requests to review drafts by Core GovOps; and
- the overall workload of Core GovOps.

###### A.2.2.6.2.3.2.3 - Atlas Edit Weekly Cycle Proposal Is Approved Or Rejected [Core]  <!-- UUID: afeaa98f-b8f5-48d9-adb2-8ceed287667d -->

The Atlas Edit Weekly Cycle proposal, if triggered by a Ranked Delegate and not rejected by the Core Facilitator for misalignment, is either approved or rejected by SKY holders by Thursday of the following week. A proposal that is not triggered or is rejected by the Core Facilitator for misalignment is treated as rejected.

###### A.2.2.6.2.3.2.4 - If Approved Then Prime Agent Begins Operationalizing Change [Core]  <!-- UUID: 61414e64-815d-4bab-8b8b-f81d787453b6 -->

If the Atlas Edit Weekly Cycle proposal is approved by SKY holders, then the Prime Agent may begin operationalizing that logic immediately thereafter.

#### A.2.2.6.3 - Light Agent Primitive [Core]  <!-- UUID: 44028423-2cd1-40cb-89ac-3f762b602b90 -->

The Light Agent Primitive enables users to create Light Agents, which are sub-agents operating on top of the Agent’s Executor Accord, conferring the advantages of Sky GovOps at a lower cost, but without direct access to other Sky Primitives.

### A.2.2.7 - Ecosystem Upkeep Primitives [Section]  <!-- UUID: 25673fd2-76cb-4c4d-8ec6-8c489207bcfc -->

Ecosystem Upkeep Primitives ensure that all Agents contribute to long-term ecosystem sustainability. The Ecosystem Upkeep Fee Primitive specifies a uniform upkeep fee payable by all Prime Agents, and the Upkeep Rebate Primitive specifies rebates that adjust those fees for Agents holding the tokens of other Prime Agents. The term "Ecosystem Upkeep Fees" refers to the upkeep obligation of a Prime Agent as specified in the Ecosystem Upkeep Fee Primitive.

#### A.2.2.7.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: a21616f4-1611-4e0b-87b2-efbdff9f6f28 -->

The Ecosystem Upkeep Fee Primitive requires Prime Agents to pay an annual fee equivalent to 50 basis points (bps) (0.50%) of their market capitalization to Sky, payable in USDS and accounted for monthly. The annual fee of 50 basis points (bps) (0.50%) of the market capitalization is divided into twelve (12) equal monthly payments. Payments must occur on the first day of each month, with the fee transferred to an address designated by Sky Core in [A.2.2.7.1.1 - Sky Core-Designated Address](2a5f0e38-e51a-4a68-a4b8-1a912b8bb12e).

##### A.2.2.7.1.1 - Sky Core-Designated Address [Core]  <!-- UUID: 2a5f0e38-e51a-4a68-a4b8-1a912b8bb12e -->

The address to which the fee must be transferred will be specified in a future iteration of the Atlas.

##### A.2.2.7.1.2 - Valuation [Core]  <!-- UUID: 4b856873-8c6a-449a-8ca6-487d8fed9029 -->

The market capitalization is determined as the total token supply multiplied by the TWAP of the token over the 24-hour period ending at 23:59 UTC on the last day of each month, immediately preceding the payment event. This value is applied in the rebate calculation under the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

#### A.2.2.7.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: 569e1c2b-0e69-43e7-8491-06cc5f7d2988 -->

The Upkeep Rebate Primitive allows a Prime Agent ("Holding Agent") to claim a rebate on its Ecosystem Upkeep Fees when it holds any portion of the token supply of another Prime Agent ("Issuing Agent").

Ecosystem Upkeep Fees are accounted on a monthly basis. The Upkeep Rebate is calculated on the same cadence per Holding Agent as follows:

1. The Holding Agent’s share of the Issuing Agent’s token supply at the time the Issuing Agent pays its Ecosystem Upkeep Fees, multiplied by
2. The total monthly Ecosystem Upkeep Fees paid by the Issuing Agent, calculated as specified in [A.2.2.7.1.2 - Valuation](4b856873-8c6a-449a-8ca6-487d8fed9029).

This resulting rebate amount is applied against the Holding Agent’s Ecosystem Upkeep Fees due in the calendar month immediately following the Issuing Agent’s payment.

### A.2.2.8 - SkyLink Primitives [Section]  <!-- UUID: 7b5d8965-a64c-4c44-b742-607f51f69d8f -->

SkyLink Primitives are Sky Primitives that are technical infrastructure that extends the Sky Protocol. SkyLink Primitives are built autonomously by Prime Agents, but owned by Sky Core and shared among all Prime Agents. Prime Agents are reimbursed for the cost of setting up SkyLink Primitives and given additional first-mover incentives.

#### A.2.2.8.1 - Token SkyLink Primitive [Core]  <!-- UUID: 4504d2d4-ee45-4a07-8c5b-9baf20b12e76 -->

The Token SkyLink Primitive allows users to bridge USDS, sUSDS, SKY, or an Agent token to new blockchains and enables other multichain features.

##### A.2.2.8.1.1 - Token SkyLink Process Definition [Core]  <!-- UUID: 18386a64-1f20-4495-99a0-2271c7d607b0 -->

The documents herein define the Process Definition for initial setup and ongoing management of the Token SkyLink Primitive.

###### A.2.2.8.1.1.1 - Token SkyLink Setup Process Definition [Core]  <!-- UUID: 408400c0-db9d-41d8-b657-de59ac18a288 -->

The documents herein define the process for setting up an Instance of the Token SkyLink Primitive.

###### A.2.2.8.1.1.1.1 - Token SkyLink Setup Real World Agreements And Planning [Core]  <!-- UUID: f1836fc1-8691-4520-8159-e6d451a256b3 -->

The documents herein define the preliminary, off-chain human coordination stage of setting up an Instance of the Token SkyLink Primitive.

###### A.2.2.8.1.1.1.1.1 - Token SkyLink Setup Target Chain Identification And Feasibility Analysis [Core]  <!-- UUID: 298ee5be-2f95-46b2-8dc7-8cf68f99c038 -->

The Prime Agent researches potential target blockchains for token bridging, including evaluation of user base, DeFi ecosystem, and bridging security requirements. The Prime Agent confirms that the target chain supports LayerZero or can be integrated easily with the LayerZero Omnichain Fungible Token standard. The Prime Agent also estimates potential use of the token on the target chain to justify the bridge deployment and audit costs. The output of this step is a preliminary decision to proceed with deploying a bridge to the target chain including a scope of work for the bridge deployment and estimated audit costs.

###### A.2.2.8.1.1.1.1.2 - Token SkyLink Setup Initial Alignment With Operational GovOps [Core]  <!-- UUID: eec4c93e-5012-4547-b1ad-ab6ba6d7042c -->

The Prime Agent presents the bridging plan to Operational GovOps, including a technical summary, proposed timeline, and estimate of audit costs. The Prime Agent and Operational GovOps also discuss any guidelines in the Atlas or the Agent Artifact that may affect bridging. The Prime Agent receives early feedback on the plan and modifies it accordingly. The output of this step is an informal agreement to proceed with developing a bridge deployment along with any documented conditions or feedback from Operational GovOps.

###### A.2.2.8.1.1.1.1.3 - Token SkyLink Setup Audit Preparation And Proposal Of Costs [Core]  <!-- UUID: aa9f9672-2d80-404b-9c6e-fe69615fc125 -->

The Prime Agent contacts a reputable third-party security audit firm for reviewing the bridge implementation. The Prime Agent negotiates audit scope, timeline, and fees with the audit firm. The Prime Agent documents the projected cost for the bridge, including development, audit, and deployment costs, for future reimbursement. The outcome of this step is a formal agreement with the audit firm and a detailed cost breakdown for bridge deployment and auditing.

###### A.2.2.8.1.1.1.2 - Token SkyLink Setup Codification and Validation [Core]  <!-- UUID: 18ce8e21-898d-4bf9-9bf8-ef1c1e7266ee -->

The documents herein define how agreements to setup an Instance of the Token SkyLink Primitive are codified and validated in the Powerhouse system and how governance votes happen.

###### A.2.2.8.1.1.1.2.1 - Agent Inputs [Core]  <!-- UUID: 5027bb60-ea5f-4f1a-9ce6-a9a0afae33e5 -->

The Prime Agent drafts an update to the Prime Agent Artifact adding the Token SkyLink to the list of active Token SkyLink deployments and including the information specified in [A.2.2.8.1.2.2 - List of Active Token SkyLink Deployments](bf3ede73-bba3-4048-b105-a49400611fcb). The Prime Agent submits the draft to the Powerhouse system. The output of this step is a draft Prime Agent Artifact update in the Powerhouse system.

###### A.2.2.8.1.1.1.2.2 - Validation And Off-Chain Vote [Core]  <!-- UUID: cac40223-e628-4248-a44d-2aaa6f03ba00 -->

The Operational Executor Facilitator reviews the proposal to ensure that it is complete and aligned with the Atlas. The Operational Executor Facilitator then initiates an off-chain snapshot vote, following the quorum and majority rules in the Prime Agent Artifact. When complete, the result of the vote is recorded in the Powerhouse system. The output of this step is the snapshot vote result recorded in the Powerhouse system.

###### A.2.2.8.1.1.1.2.3 - Official Update of Artifact [Core]  <!-- UUID: 79abf483-f256-4ef6-9aa7-558a8800e7a8 -->

If the Token SkyLink Invocation is successfully approved, the Operational Executor Facilitator finalizes and publishes the update to the Prime Agent Artifact, making it effective in the Atlas. The output of this step is an updated Prime Agent Artifact with the Token SkyLink Instance Activated.

###### A.2.2.8.1.1.1.3 - Token SkyLink Setup Deployment [Core]  <!-- UUID: 21241867-d25e-47ee-b4c2-13224dcd0292 -->

The documents herein define how the deployment of an Instance of the Token SkyLink Primitive is executed on-chain.

###### A.2.2.8.1.1.1.3.1 - Token SkyLink Setup Bridge Deployment And Initial Audit [Core]  <!-- UUID: af88c454-2171-41ce-a8e8-1d6c40d4e209 -->

The Prime Agent, through Operational GovOps, deploys the Token SkyLink contract on the target chain. The Prime Agent shares the Token SkyLink contract’s final address with the audit firm for verification. Operational GovOps confirms that the bridge contract address and references match the updated Prime Agent Artifact. The audit firm completes and updates the bridging audit registry with the results of the audit. The output of this step is a deployed bridge contract with audit results uploaded to the bridging audit registry.

###### A.2.2.8.1.1.1.3.2 - Token SkyLink Setup Activation On New Chain [Core]  <!-- UUID: c18d8c58-d347-4efd-9c33-4fd89cf40f90 -->

Core GovOps formalizes the audit results with a Sky Core Executive Vote to fully activate bridging functionality. Operational GovOps updates the Prime Agent Reimbursement Module to begin counting any bridged tokens toward the incremental reward. The output of this step is fully enabled bridging on the target chain with the Prime Agent Reimbursement Module updated to track bridging based rewards.

###### A.2.2.8.1.1.2 - Token SkyLink Ongoing Management [Core]  <!-- UUID: d7adf706-c9cc-4408-9668-cec0fdc90be8 -->

The documents herein define the process for managing an Instance of the Token SkyLink Primitive.

###### A.2.2.8.1.1.2.1 - Token SkyLink Management Settlement Cycle [Core]  <!-- UUID: 97fb1954-b9f4-429e-bc29-e9eea9fe2e0e -->

During each settlement cycle, the Prime Agent Reimbursement Module tallies the total token bridging volume on the new chain. The Prime Agent Reimbursement Module calculates the reimbursement due for bridge development costs as a percent of the token bridging volume, in addition to normal Distribution Rewards if applicable. Core GovOps executes a payment to the Prime Agent for the amount due for reimbursement of bridge development costs, to the extent that such costs have not already been fully reimbursed. Core GovOps updates the Powerhouse system to reflect the amount of bridge development costs that have been reimbursed.

##### A.2.2.8.1.2 - Token SkyLink Input Requirements [Core]  <!-- UUID: 7d9a8373-ed56-4b01-8ec7-ebf2ed4ef8b0 -->

The documents herein define the required inputs for a valid Token SkyLink Primitive. If any input is noncompliant or omitted, the Primitive will be invalidated and the SkyLink deployment will not move forward.

###### A.2.2.8.1.2.1 - Token SkyLink Activation Status [Core]  <!-- UUID: 94a0a22c-cbd6-4022-80e8-4681f60c7cec -->

The Token SkyLink Primitive must be Globally Activated.

###### A.2.2.8.1.2.2 - List of Active Token SkyLink Deployments [Core]  <!-- UUID: bf3ede73-bba3-4048-b105-a49400611fcb -->

The Token SkyLink Primitive must list each active Token SkyLink deployment. The listing must include the following information: (1), the token being bridged, (2) the target chain of the bridge, (3) the address of the bridge contract on the Ethereum Mainnet, (4) the address of the bridge contract on the target chain, (5) the audit of the bridge contract, (6) the bridge parameters, (7) the total bridge deployment and audit costs, and (8) the amount of bridge deployment and audit costs that have been reimbursed to date.

### A.2.2.9 - Demand Side Stablecoin Primitives [Section]  <!-- UUID: 26415305-432d-423b-9553-3f325279712d -->

Demand Side Stablecoin Primitives are Sky Primitives that target demand generation for USDS. Prime Agents can create and control multiple instances of these Primitives which exist as technical infrastructure incentivizing the adoption or usage of USDS by end users or third parties.

#### A.2.2.9.1 - Distribution Reward Primitive [Core]  <!-- UUID: e632c38f-3e4e-4c7e-acfd-b6ec45a422e6 -->

The documents herein govern the Distribution Reward Primitive.

##### A.2.2.9.1.1 - Introduction [Core]  <!-- UUID: 02189c79-a529-4388-98ad-a743d2a8980d -->

The documents herein provide an introduction to the Distribution Reward Primitive.

###### A.2.2.9.1.1.1 - Purpose [Core]  <!-- UUID: 6f1bc619-b8a9-4917-a34b-f52016942c01 -->

The purpose of the Distribution Reward is to incentivize Prime Agents and third parties to drive USDS adoption by providing a financial reward to these actors for all USDS and sUSDS balances attributable to them.

###### A.2.2.9.1.1.2 - Allowed Number Of Instances [Core]  <!-- UUID: 45149960-fbf3-4079-be4e-fe2a71e5e43f -->

Multiple instances of the Distribution Reward Primitive are allowed. Each instance corresponds to a Distribution Reward program with an associated Distribution Reward Code.

###### A.2.2.9.1.1.3 - Multi-Instance Coordinator Document [Core]  <!-- UUID: c788ebcf-98a4-4b97-ae3c-db578c75dc2e -->

An Agent Artifact that has more than one active instance of the Distribution Reward Primitive is not required to have a `Multi-Instance Coordinator Document`, since each Instance can be managed independently.

##### A.2.2.9.1.2 - Global Specification [Core]  <!-- UUID: 7f0959dc-c6e2-4e64-9526-76563a2a6d29 -->

The requirements herein apply universally across all possible deployments of the Distribution Reward Primitive by Prime Agents. They include the steps that Agents must take to deploy the Primitive, including Global Activation of the Primitive, Instance Invocation, and ongoing management of the Primitive Instance(s).

###### A.2.2.9.1.2.1 - Base Elements [Core]  <!-- UUID: dc123bca-eac1-40e1-ad1f-f888a6ec8d1f -->

The documents herein define base elements of the Distribution Reward Primitive.

###### A.2.2.9.1.2.1.1 - Reward Codes [Core]  <!-- UUID: cda71b0c-37cc-4f6a-92a3-b6a14895bfe1 -->

The documents herein define base elements related to Reward Codes.

###### A.2.2.9.1.2.1.1.1 - Assignment [Core]  <!-- UUID: 225454ec-ac16-470e-b780-114acbb2a453 -->

The documents herein define the process for assigning Reward Codes.

###### A.2.2.9.1.2.1.1.1.1 - Process [Core]  <!-- UUID: e00e28d1-dad1-4cff-8ea4-1290c27d3b07 -->

Reward Codes are assigned by Operational GovOps. Operational GovOps may contract with another actor to perform this work for them, at their discretion.

###### A.2.2.9.1.2.1.1.2 - Marking [Core]  <!-- UUID: ec2c6d8a-e10f-471a-8f85-67803159cc37 -->

To be eligible for the Distribution Reward, USDS balances must be "marked" with a Reward Code using the agreed-on Tracking Methodology.

###### A.2.2.9.1.2.1.1.2.1 - Ethereum Mainnet General Tracking Methodology [Core]  <!-- UUID: 87fd6861-ba8a-4bde-945e-ee9ad37ae3e2 -->

The general Tracking Methodology for Ethereum Mainnet is to specify the Reward Code as a parameter to depositing USDS into the Sky Savings Rate contract or Token Rewards contracts. This on-chain deposit data is then combined with withdrawal data, which is further processed by Operational GovOps to estimate net deposits associated with the Reward Code. Where a balance has been marked with more than one Reward Code, the balance is attributed to the Reward Code specified in the most recent marking event.

###### A.2.2.9.1.2.1.1.2.2 - Ethereum Mainnet CoW Swap Tracking Methodology [Core]  <!-- UUID: 1b5cc0ee-0ee8-467e-ab49-33c06ad417dc -->

The Tracking Methodology for CoW Swap on the Ethereum Mainnet is the same as the general process for the Ethereum Mainnet, with the exception that events on CoW Swap’s decentralized network of solvers are tracked instead.

###### A.2.2.9.1.2.1.1.2.3 - Base Tracking Methodology [Core]  <!-- UUID: f710bddf-dc1d-483c-9503-483574cb6333 -->

The Tracking Methodology for Base is to specify the Reward Code as a parameter in calls to the Base PSM contract. Conversions from USDS or USDC to sUSDS are considered "deposits" and net deposits are calculated using an approach similar to that on Ethereum Mainnet.

###### A.2.2.9.1.2.1.1.2.4 - Alternative Tracking Methodologies [Core]  <!-- UUID: 5eba1c21-4e93-4a0a-aa10-e99bcfa65f16 -->

The Tracking Methodologies specified above are not exclusive. Prime Agents and Operational GovOps can develop additional Tracking Methodologies, so long as those methodologies reasonably estimate USDS balances that are attributable to the holder of the Reward Code and there is no possibility that the same USDS balances could be "double counted" for multiple Reward Code holders. Tracking methodologies must be based on either (1) on-chain data or (2) off-chain data that can be independently verified or attested to by a third party.

###### A.2.2.9.1.2.1.1.2.5 - Lifetime [Core]  <!-- UUID: c0b77312-5e88-4311-bfe2-d95a1a2c5a7c -->

USDS balances are eligible for a Distribution Reward for a period of ten (10) years from the date of the event marking the USDS balance with the Reward Code. The date of the marking event is determined based on the Primitive Instance’s specified Tracking Methodology.

###### A.2.2.9.1.2.1.1.3 - Management [Core]  <!-- UUID: 75ddec36-c39e-4333-9ec1-2d329128e848 -->

Operational GovOps manages the list of Actor Reward Codes. All current Integrators and onboarding Integrators must be specified in [A.2.2.9.1.2.1.4 - Current And Onboarding Integrators](f3952cc5-cde2-46b9-b575-034dda83570b) so that Prime Agents, through their Operational Executor Agents, can onboard new partners themselves without having to go through a single party.

###### A.2.2.9.1.2.1.1.4 - Reward Code Ranges [Core]  <!-- UUID: af47ab9b-ee80-4352-89db-9c7d819395c2 -->

The following Prime Agents are allocated reserved ranges of Reward Codes for use in their Distribution Reward Primitive instances. The reserved ranges are:

- Skybase: `0`, `1`, and `1000`–`1999`
- Spark: `2`–`999`
- Grove: `2000`–`2999`
- Keel: `4000`–`4999`

###### A.2.2.9.1.2.1.2 - Distribution Reward Rate [Core]  <!-- UUID: 57384c49-e499-4c69-b22c-8e1f1dd34759 -->

The Distribution Reward rate is set at 0.2%. The Distribution Reward rate is annualized on all USDS and sUSDS balances associated with the relevant Reward Code.

###### A.2.2.9.1.2.1.3 - Rewards Distribution [Core]  <!-- UUID: 8dfabd92-aabc-4605-9ca5-d10f413203dc -->

The documents herein define base elements of the Distribution Reward Primitive related to distribution of Distribution Rewards.

###### A.2.2.9.1.2.1.3.1 - Reward Cadence [Core]  <!-- UUID: 02d1e35f-0a24-43d9-9406-347eef58a9d1 -->

The Distribution Reward is calculated and distributed on a monthly basis.

###### A.2.2.9.1.2.1.3.2 - Reward Payment [Core]  <!-- UUID: 38cb0bfe-3733-4a11-8b3a-6728df00d08e -->

The Distribution Reward payment for each month is equal to:

1. the average balance over the month, times
2. the annual Distribution Reward Fee specified in [A.2.2.9.1.2.1.2 - Distribution Reward Rate](57384c49-e499-4c69-b22c-8e1f1dd34759), divided by
3. twelve (12).

###### A.2.2.9.1.2.1.3.3 - Treasury Management [Core]  <!-- UUID: 935b90bb-a854-4c06-b6ea-48a1cf8fd2f1 -->

The documents herein define the treasury management process.

###### A.2.2.9.1.2.1.3.3.1 - Near-Term Process [Core]  <!-- UUID: 05fb732b-de55-4886-81a7-7c5d4c13d2d2 -->

In the near term, Operational GovOps calculates the Distribution Reward. The Distribution Reward is paid from the Demand Side Buffer (see [A.2.2.4.3 - Demand Side Buffer](862b6d83-f464-4125-8259-233b7de75ec4)) within seven (7) days of the end of every month.

###### A.2.2.9.1.2.1.3.3.2 - Long Term Process [Core]  <!-- UUID: 07953e87-c201-4ad5-9c1e-b32efc5fba94 -->

In the long term, Operational GovOps calculates the Distribution Reward for each month. Operational GovOps then pays the Distribution Reward recipient from its Buffer. Later Sky Core reimburses the Operational Agent Buffer for the amount paid as part of the Settlement Cycle. This minimizes the role of Sky Core in Distribution Reward payments and emphasizes the primary role of the Operational Executor Agent, acting through Operational GovOps, in implementing the Sky Primitives. The process is specified in further detail in [A.2.2.9.1.2.4.1 - Routine Protocol](c2abdd22-fe0f-489e-b281-450e066db701).

###### A.2.2.9.1.2.1.3.4 - Payment Errors [Core]  <!-- UUID: 1b5edf68-0825-449a-a404-34141a1892cc -->

If it is discovered that previous Distribution Reward calculations were made erroneously, underpayments are resolved retroactively. In cases of overpayment, the Prime Agent associated with the affected Reward Code must reimburse Sky the overpayment amount and can use future Distribution Reward payments to reimburse itself.

###### A.2.2.9.1.2.1.4 - Current And Onboarding Integrators [Core]  <!-- UUID: f3952cc5-cde2-46b9-b575-034dda83570b -->

The documents herein specify current and onboarding Integrators.

###### A.2.2.9.1.2.1.4.1 - Current Integrators [Active Data Controller]  <!-- UUID: 883f1b52-a6d2-417b-bb24-12917de83b53 -->

Current Integrators are Integrators who have a Reward Code specified in an `Active` Instance of the Distribution Reward Primitive. The list of Current Integrators is defined as Active Data in [A.2.2.9.1.2.1.4.1.0.6.1 - List Of Current Integrators](efbe7903-a76e-40f0-a440-56e463283157).

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.2.9.1.2.1.4.1.0.6.1 - List Of Current Integrators [Active Data]  <!-- UUID: efbe7903-a76e-40f0-a440-56e463283157 -->

The current Active Integrators are:

###### A.2.2.9.1.2.1.4.2 - Onboarding Integrators [Active Data Controller]  <!-- UUID: 9a7f47ae-760f-44b5-9b5f-dd4fef86e1cc -->

Onboarding Integrators are actors whose application to the Integrator Program has been approved, but are specified in an Instance of the Distribution Reward Primitive or Integration Boost Primitive that is "Pending", or is not `Active` yet. The list of Onboarding Integrators is defined as Active Data in [A.2.2.9.1.2.1.4.2.0.6.1 - List Of Onboarding Integrators](eb644108-94fc-430f-ae5a-e3294b9dd9be).

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.2.9.1.2.1.4.2.0.6.1 - List Of Onboarding Integrators [Active Data]  <!-- UUID: eb644108-94fc-430f-ae5a-e3294b9dd9be -->

The current Onboarding Integrators are:

###### A.2.2.9.1.2.1.5 - Distribution Reward Reimbursement [Core]  <!-- UUID: fd551536-2177-4e78-87a1-c2528ff2fcaf -->

The documents herein specify the Distribution Reward reimbursement.

###### A.2.2.9.1.2.1.5.1 - Sky Core Distribution Reward Reimbursement [Active Data Controller]  <!-- UUID: 2c0eb02c-144e-4326-b5ec-85805653f0b7 -->

The Distribution Reward reimbursement payments are defined as Active Data in [A.2.2.9.1.2.1.5.1.0.6.1 - Sky Core Distribution Reward Reimbursement Amounts](169eb312-ed63-4a83-9f5d-43b621c0705e).

The Active Data is updated as follows:

- The Responsible Party is Core GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.2.9.1.2.1.5.1.0.6.1 - Sky Core Distribution Reward Reimbursement Amounts [Active Data]  <!-- UUID: 169eb312-ed63-4a83-9f5d-43b621c0705e -->

The current Sky Core Distribution Reward Reimbursement Amounts are:

###### A.2.2.9.1.2.2 - Global Activation [Core]  <!-- UUID: 49513ac9-43d6-4766-8a51-195e221de3f2 -->

An Agent who intends to deploy the Distribution Reward Primitive must first Globally Activate it.

###### A.2.2.9.1.2.2.1 - Process Initiation Logic [Core]  <!-- UUID: 776d926e-70d0-4771-bd60-d3fcef0a7ea3 -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.2.1.1 - Triggers [Core]  <!-- UUID: 090b3f8e-78a8-4df1-8db9-b9a6a2e23a33 -->

Triggers are specified herein.

###### A.2.2.9.1.2.2.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: b4271bcd-12f5-4a14-bf5a-c77c9afd3629 -->

None.

###### A.2.2.9.1.2.2.1.1.2 - Document Update Triggers [Core]  <!-- UUID: e2766ea3-ddf9-434d-a6ab-6e13ca23e164 -->

None.

###### A.2.2.9.1.2.2.1.2 - Dependencies [Core]  <!-- UUID: 4e4476d8-0b98-4a2a-a3af-e879af06e01c -->

See [A.2.2.1.2.4.1 - Agent Launch And Sequence of Primitive Global Activation](2f5ff5c8-bcd1-44a4-ba56-2075ac8e9c61) for constraints on when an Agent can Globally Activate this Primitive.

###### A.2.2.9.1.2.2.2 - Process Flow [Core]  <!-- UUID: 89d26f82-b662-41df-8935-44aa7e93be6d -->

The Prime Agent uses the Powerhouse interface to Globally Activate (toggle on) the Distribution Reward Primitive.

###### A.2.2.9.1.2.2.3 - Required Primitive Inputs [Core]  <!-- UUID: 108c6d9c-8ecf-48bf-bc8b-365f8cf65c0c -->

The following inputs must be submitted into the Primitive using the Powerhouse interface:

- **Create** `Primitive Hub Document`
    - Updated Field: Global Activation Status
        - New Value: set to `Activated`

###### A.2.2.9.1.2.2.4 - Required Outputs [Core]  <!-- UUID: faf79404-fe20-406d-a0a2-f3ac9e8592ab -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.2.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 74003afb-d603-4898-bd2a-bcf988e8c039 -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.1.2.2.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 6af6cd24-9513-42a7-be91-3f16845ebadf -->

No Agent Artifact documents are updated as the output of this process. The requirements specified in [A.2.2.9.1.2.2.3 - Required Primitive Inputs](108c6d9c-8ecf-48bf-bc8b-365f8cf65c0c) fully complete the Process.

###### A.2.2.9.1.2.3 - Instance Invocation Protocol [Core]  <!-- UUID: ad3a3f6b-7bc3-4e5f-b1c3-225b5b4cbe15 -->

After fulfilling the requirements for Global Activation, an Agent can Invoke its first Instance of the Distribution Reward Primitive by following the sequential process specified herein. Subsequent Invocations of the Primitive must also adhere to the same requirements defined below.

###### A.2.2.9.1.2.3.1 - Process Definition For Initial Opportunity Identification And Planning [Core]  <!-- UUID: f07b1cca-5db2-4b1b-b760-ea738d2776f3 -->

The documents herein specify the process definition for initial opportunity identification and planning.

###### A.2.2.9.1.2.3.1.1 - Process Initiation Logic [Core]  <!-- UUID: 005beba7-131f-43f9-93fc-29463905ef69 -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.3.1.1.1 - Triggers [Core]  <!-- UUID: 222fc95e-eead-49ec-9d55-730b2b3cb0a0 -->

Triggers are specified herein.

###### A.2.2.9.1.2.3.1.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: dec5be6c-3123-4808-93e9-0486fc8e9572 -->

None.

###### A.2.2.9.1.2.3.1.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 34497a9f-b623-45b3-a2f2-dc74a06c6700 -->

None.

###### A.2.2.9.1.2.3.1.1.2 - Dependencies [Core]  <!-- UUID: c89c3cd1-20c4-461f-a220-1754d97e2049 -->

This process is dependent on a Prime Agent Globally Activating the Distribution Reward Primitive pursuant to [A.2.2.9.1.2.2 - Global Activation](49513ac9-43d6-4766-8a51-195e221de3f2).

###### A.2.2.9.1.2.3.1.2 - Process Flow [Core]  <!-- UUID: 75ff9b92-47e1-454f-864b-b74742df918e -->

The process flow is defined herein.

- The Prime Agent identifies an opportunity to drive USDS adoption through a Distribution Reward to either 1) reward an existing Integrator for driving USDS adoption or 2) incentivize a new actor to onboard as an Integrator to drive USDS adoption.
- Existing Integrators
    - The Prime Agent and the third party, if applicable, develop a plan to track USDS utilization attributable to the actor using either on-chain or off-chain data.
- Prospective Integrators
    - Near Term process:
        - The Prospective Integrator must first apply to the Integrator program and be approved by Operational GovOps per [A.2.2.4.1.2.1 - Near Term Process](7fe5dbb2-a07d-4ef9-94de-f54a2d568c57). Post approval, Operational GovOps issues a Reward Code to the Integrator.
        - The Prime Agent and the third party develop a plan to track USDS utilization attributable to the actor using either on-chain or off-chain data.
    - Long Term process:
        - The Prospective Integrator must first apply to the Integrator program and be approved by Operational GovOps pursuant to [A.2.2.4.1.2.2 - Long Term Process](6283379c-d871-40a9-a915-d716d7df5642). Post approval, Operational GovOps issues a Reward Code to the Integrator.
        - The Prime Agent develops a plan to track USDS utilization attributable to it using either on-chain or off-chain data. Where applicable, the plan should include how the Prime Agent will support the prospective Integrator in including the Reward Code in their on-chain infrastructure.
- The Prime Agent may also be (or choose to be) an Integrator itself and deploy a Reward Code on its frontend to earn the Distribution Reward.
    - Near Term process:
        - If the Prime Agent is not already an approved Integrator, it must apply to the Program and be approved by Operational GovOps. Post approval, Operational GovOps issues a Reward Code to the Prime Agent.
        - The Prime Agent develops a plan to track USDS utilization attributable to it using either on-chain or off-chain data.
    - Long Term process:
        - The Prime Agent must first apply to the Integrator program and be approved by Operational GovOps pursuant to [A.2.2.4.1.2.2 - Long Term Process](6283379c-d871-40a9-a915-d716d7df5642). Post approval, Operational GovOps issues a Reward Code to the Prime Agent.
        - The Prime Agent develops a plan to track USDS utilization attributable to it using either on-chain or off-chain data.

###### A.2.2.9.1.2.3.1.3 - Required Primitive Inputs [Core]  <!-- UUID: 4d5482ad-7944-4073-8fbe-b9dbcd1a27a3 -->

The required Primitive Inputs for this process are defined herein and organized in sequential stages.

- Drafting of Initial Planning Document
    - Create `Initial Planning Document`
        - Updated fields
            - `Status`
                - New value: set to `Drafting`
            - `Integrator`
                - New Value: set to Integrator Name
            - `Reward Code`
                - New Value: set to Reward Code
            - `Tracking Methodology`
                - New value: populate with details for tracking utilization
            - `Custom Instance Parameters`
                - New Value: populate with details for any custom parameters
        - Responsible Party: Prime Agent Team
        - Trigger - Required Output: After Prime Agent's `Initial planning document` Status is set to `Drafting`
- Initial Planning Document Triggered For GovOps review
    - Edit `Initial Planning Document`
        - Updated fields
            - `Tracking Methodology`
                - New value: updated content, as applicable
            - `Status`
                - New value: set to `Ready for GovOps Review`
        - Responsible party: Prime Agent
        - Trigger - Required Output: After Prime Agent's `Initial planning document` Status is set to `Ready for GovOps review`.

###### A.2.2.9.1.2.3.1.4 - Required Outputs [Core]  <!-- UUID: 1ad17e84-8bde-4669-9967-9f67d1d3c603 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.3.1.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: bab05cb6-532f-41e0-8fba-203b1b92294b -->

The Sky Core Atlas is updated pursuant to the following requirements.

###### A.2.2.9.1.2.3.1.4.1.1 - Onboarding Integrators Active Data Update [Core]  <!-- UUID: 6857396f-f0ce-4471-8e48-ed5f06b86830 -->

[A.2.2.9.1.2.1.4.2.0.6.1 - List Of Onboarding Integrators](eb644108-94fc-430f-ae5a-e3294b9dd9be) is updated as follows:

- Updated fields
    - `Onboarding Integrators/Integrator Name`
        - New value: set to the name of the Integrator
    - `Integrator Name/Reward Code`
        - New value: set to Reward Code
- Responsible Party: Operational GovOps

###### A.2.2.9.1.2.3.1.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 11161730-6568-445f-a250-ba5c67857390 -->

The Agent Artifact is updated pursuant to the following requirements. Each Output "set" is triggered following the completion of its respective Input stage, defined in [A.2.2.9.1.2.3.1.3 - Required Primitive Inputs](4d5482ad-7944-4073-8fbe-b9dbcd1a27a3).

- After Prime Agent's `Initial planning document` Status is set to `Drafting`
    - Create `Instance Configuration` Document for prospective Primitive Instance. The Instance Configuration Document contains a `Data Repository.`
        - Instance Status: (automatically inherits from `Primitive Hub Document`)
    - Edit `Primitive Hub Document/In Progress Invocations Directory/Instance Name`
        - Updated fields:
            - Invocation Status:
                - New value: set to `Planning`
            - Instance Configuration Document Location
                - New value: link to `Instance Configuration Document` (created at Create `Instance Configuration` Document for prospective Primitive Instance. The Instance Configuration Document contains a `Data Repository.`)
    - Responsible party: Operational GovOps [automated]
- After Prime Agent's `Initial planning document` Status is set to `Ready for GovOps review`.
    - Edit `Primitive Hub Document/In Progress Invocations/Instance Name`
        - Updated fields:
            - Invocation Status:
                - New value: set to `Pending GovOps review`
        - Responsible party: Operational GovOps [automated]
        - Trigger - Process: [A.2.2.9.1.2.3.2 - Process Definition For Operational GovOps Review](5fd265ef-17f0-4400-b06c-a6ce9fa87636).

###### A.2.2.9.1.2.3.2 - Process Definition For Operational GovOps Review [Core]  <!-- UUID: 5fd265ef-17f0-4400-b06c-a6ce9fa87636 -->

The documents herein define the process for Operational GovOps Review for an Invocation of the Distribution Reward Primitive.

###### A.2.2.9.1.2.3.2.1 - Process Initiation Logic [Core]  <!-- UUID: da868510-121f-442a-982e-8ab2d2149a25 -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.3.2.1.1 - Triggers [Core]  <!-- UUID: f89a41b2-973b-4eca-b463-e0e77bc719ef -->

Triggers are specified herein.

###### A.2.2.9.1.2.3.2.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: d1d3de53-ad5a-40cb-9155-58db67a6340c -->

None.

###### A.2.2.9.1.2.3.2.1.1.2 - Document Update Triggers [Core]  <!-- UUID: fd211726-1576-4b0a-8489-6e76e83ee92b -->

This process is triggered by the Artifact Document Update specified at Edit `Primitive Hub Document/In Progress Invocations/Instance Name`.

###### A.2.2.9.1.2.3.2.1.2 - Dependencies [Core]  <!-- UUID: abb8f0ef-eae6-4af5-8a70-20630a33e7c9 -->

This process has no dependencies.

###### A.2.2.9.1.2.3.2.2 - Process Flow [Core]  <!-- UUID: ef743f33-32b0-4a51-af00-a9e35c2e1017 -->

The process flow is defined herein:

- Operational GovOps reviews the `Initial Planning Document` to ensure:
    - Operational GovOps has the ability to operationalize the proposed tracking mechanism, and
    - The proposed tracking mechanism accurately reflects USDS usage attributable to the actor and there is no possibility that rewards could be "double counted" (i.e. multiple actors being paid for the same USDS balance).
- Operational GovOps submits its feedback into the `Operational GovOps Review Document` (created at Create `Operational GovOps Review Document`.) along with suggested changes, if any.
- The Prime Agent incorporates feedback from Operational GovOps and edits its `Initial Planning Document` as needed.

###### A.2.2.9.1.2.3.2.3 - Required Primitive Inputs [Core]  <!-- UUID: 9c4653fa-6afe-4567-9e85-54c0a84b9311 -->

The following inputs must be submitted into the Primitive using the Powerhouse interface.

- Create `Operational GovOps Review Document`.
    - Updated fields
        - `Initial Planning Document`
            - New Value: automatically links to respective Document
        - `Feedback Summary`
            - New Value: GovOps populates with its review commentary and suggested changes that are agreed to by Agent and GovOps, if any.
        - Responsible party: Operational GovOps.

###### A.2.2.9.1.2.3.2.4 - Required Outputs [Core]  <!-- UUID: a7a3e2d3-54bd-4c0f-a222-505b5e14a5e4 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.3.2.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 9a94a573-8a51-4b04-9704-d84dc0623bb8 -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.1.2.3.2.4.2 - Agent Artifact Updates [Core]  <!-- UUID: ec050d61-1d48-453a-ac13-4cea23c68292 -->

The Agent Artifact is updated pursuant to the following requirements.

###### A.2.2.9.1.2.3.2.4.2.1 - Initial Planning Document Update [Core]  <!-- UUID: 66a07769-2de9-4b15-a439-4fc84b6a1575 -->

The Document is updated as follows.

- Updated fields
    - `Tracking Methodology`
        - New Value: as applicable, update to reflect any changes agreed to between the Prime Agent and Operational GovOps
    - Responsible Party: Operational GovOps

###### A.2.2.9.1.2.3.2.4.2.2 - Primitive Hub Document/In Progress Invocations Directory/Instance Name Update [Core]  <!-- UUID: 6f457b50-a98c-4516-9b37-932603a59627 -->

The Document is updated as follows.

- Updated fields
    - Invocation Status
        - New value: set to `Proposal drafting in progress`
- Responsible Party: Operational GovOps [automated]
- Triggers: [A.2.2.9.1.2.3.3 - Process Definition For Artifact Update Draft](240e0e2c-64b6-4290-aa23-ec19eb2f6e59)

###### A.2.2.9.1.2.3.3 - Process Definition For Artifact Update Draft [Core]  <!-- UUID: 240e0e2c-64b6-4290-aa23-ec19eb2f6e59 -->

The documents herein define the process for preparing the Artifact Update Draft for an Invocation of the Distribution Reward Primitive.

###### A.2.2.9.1.2.3.3.1 - Process Initiation Logic [Core]  <!-- UUID: 9add3334-5779-4d23-bf5f-6c25cf9fcf9a -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.3.3.1.1 - Triggers [Core]  <!-- UUID: bdc8d447-a140-4580-b439-b3ac8deb5aac -->

Triggers are specified herein.

###### A.2.2.9.1.2.3.3.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: e379a9d8-c0d2-4aa6-ab62-41a6767dc490 -->

None.

###### A.2.2.9.1.2.3.3.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 94d06bae-9bc9-4e8f-a38d-4b879466873b -->

This process is triggered by the Document Update specified at [A.2.2.9.1.2.3.3.4.2.1 - Primitive Hub/In Progress Invocations Directory/Instance Name Update](b37c4266-2dd9-4cce-8b6b-cc35af2b94d9).

###### A.2.2.9.1.2.3.3.1.2 - Dependencies [Core]  <!-- UUID: a6f968d6-0e8c-4962-b982-43beffc602db -->

This process has no dependencies.

###### A.2.2.9.1.2.3.3.2 - Process Flow [Core]  <!-- UUID: ccb71126-1333-453c-aaeb-4359a8013f32 -->

The process flow is defined herein:

- The Prime Agent creates the `Artifact Edit Draft` Document and works to finalize its draft of the Artifact Edit per discussions with Operational GovOps.
- When draft is finalized, the Prime Agent triggers the creation of the `Artifact Edit Proposal`, which inherits content from the finalized `Artifact Edit Draft` Document.
- The Prime Agent submits the `Artifact Edit Proposal` Document to the Powerhouse system.

###### A.2.2.9.1.2.3.3.3 - Required Primitive Inputs [Core]  <!-- UUID: 6f4e7971-1813-4ff6-9e4f-5953c8cb54af -->

The required Primitive Inputs for this process are defined herein and implemented in sequential stages.

- Agent creates `Artifact Edit Draft` document; drafting in progress:
    - Edit `Artifact Edit Draft`
        - Updated fields
            - Status
                - New value: set to `In Progress`
            - Content
                - New value: populate with drafted content
- Agent finalizes `Artifact Edit Draft`
    - Edit `Artifact Edit Draft`
        - Updated fields
            - Status
                - New value: set to `Draft Finalized`
- Powerhouse System Creates `Artifact Edit Proposal` Document
    - Updated fields
        - Content
            - New value: Inherits data from Artifact Edit Draft content field.
    - Responsible party: Operational GovOps [if not automated]
- Agent submits `Artifact Edit Proposal` Document to Powerhouse system
    - Updated fields
        - Status:
            - New value: set to `Pending Facilitator Review`
    - Responsible party: Agent

###### A.2.2.9.1.2.3.3.4 - Required Outputs [Core]  <!-- UUID: c7ed27ce-d296-4a44-83c3-96bb1ed8976d -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.3.3.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 264273c8-7805-45ec-aa87-ebd08faf763d -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.1.2.3.3.4.2 - Agent Artifact Updates [Core]  <!-- UUID: a3294ae2-3fd7-446a-a628-dbddd487931e -->

The Agent Artifact documents specified herein are updated as the output of this process.

###### A.2.2.9.1.2.3.3.4.2.1 - Primitive Hub/In Progress Invocations Directory/Instance Name Update [Core]  <!-- UUID: b37c4266-2dd9-4cce-8b6b-cc35af2b94d9 -->

The Document is updated as follows:

- Updated fields
    - Invocation Status
        - New value: `Proposal Pending Facilitator Review`
- Responsible Party: Operational GovOps
- Triggers: [A.2.2.9.1.2.3.4 - Process Definition For Operational Facilitator Review](fd9aac63-00a0-4fc5-ad7c-8bb131322bd7).

###### A.2.2.9.1.2.3.4 - Process Definition For Operational Facilitator Review [Core]  <!-- UUID: fd9aac63-00a0-4fc5-ad7c-8bb131322bd7 -->

The documents herein define the process for Operational Facilitator Review for an Invocation of the Distribution Reward Primitive.

###### A.2.2.9.1.2.3.4.1 - Process Initiation Logic [Core]  <!-- UUID: 4e87663b-619e-46b6-a672-9bc81d11f4e7 -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.3.4.1.1 - Triggers [Core]  <!-- UUID: 48a12682-0218-4851-8a05-731ae7823b7b -->

Triggers are specified herein.

###### A.2.2.9.1.2.3.4.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 296a23ca-988b-4516-aa78-230ed17b0bbb -->

None.

###### A.2.2.9.1.2.3.4.1.1.2 - Document Update Triggers [Core]  <!-- UUID: bee5a2d9-1e98-4918-a77d-3e3607b51f0f -->

This process is triggered by the Document Update specified at [A.2.2.9.1.2.3.3.4.2.1 - Primitive Hub/In Progress Invocations Directory/Instance Name Update](b37c4266-2dd9-4cce-8b6b-cc35af2b94d9).

###### A.2.2.9.1.2.3.4.1.2 - Dependencies [Core]  <!-- UUID: 967572c4-ba29-4a98-ae05-e3698457d440 -->

This process has no dependencies.

###### A.2.2.9.1.2.3.4.2 - Process Flow [Core]  <!-- UUID: 67dce065-9fed-4c23-abf5-881371792796 -->

The process flow is defined herein.

- The Operational Facilitator reviews the `Artifact Edit Proposal` to ensure alignment with the Sky Core Atlas and the Agent Artifact.
- Where the Proposal is determined to be aligned, the Operational Facilitator updates the `Artifact Edit Proposal` Document to reflect their approval and commentary, if applicable.
- Where the Proposal is determined to be misaligned, the Operational Facilitator updates the `Artifact Edit Proposal` document to reflect their rejection and commentary. Commentary is required where the Operational Facilitator rejects the proposal for misalignment.

###### A.2.2.9.1.2.3.4.3 - Required Primitive Inputs [Core]  <!-- UUID: 967f54c6-9a51-4225-a8fd-e366f7a3d91e -->

The required Primitive Inputs to this process are defined herein and organized as two mutually exclusive pathways. Once the Review outcome is determined by the Facilitator, the corresponding Pathway is followed to the exclusion of the other.

- Operational Facilitator Approves Proposal
    - Edit `Artifact Edit Proposal`
        - Updated fields
            - `Operational Facilitator Review/Review Decision`
                - New value: set to `Approved`
            - `Commentary`
                - New value (optional): populate with reasoning for Approval
            - `Status`
                - New value: set to `Proposal Approved by Facilitator` [automated]
        - Responsible party: Operational Facilitator
        - Trigger-Process: [A.2.2.9.1.2.3.5 - Process Definition For Offchain Vote](3170b9a1-d074-4cbd-bb81-ae1661bc0ed8)
- Operational Facilitator Rejects proposal
    - Edit `Artifact Edit Proposal`
        - Updated fields
            - `Operational Facilitator Review/Review Decision`
                - New value: set to `Rejected`
            - `Commentary`
                - New value (required): populate with reasoning for Rejection
            - `Status`
                - New value: set to `Proposal Rejected By Facilitator` [automated]
        - Responsible party: Operational Facilitator

###### A.2.2.9.1.2.3.4.4 - Required Outputs [Core]  <!-- UUID: b63e78d1-112d-4d48-a647-a1e3fc2f54a5 -->

The documents herein specify the required outputs from this process, if any.

###### A.2.2.9.1.2.3.4.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: dfdf873a-c24a-4856-a3e9-717ea09dd9bb -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.1.2.3.4.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 9cb3ab72-37f5-4501-8661-a204d0747dd8 -->

No Agent Artifact documents are updated as the output of this process. The requirements specified in [A.2.2.9.1.2.3.4.3 - Required Primitive Inputs](967f54c6-9a51-4225-a8fd-e366f7a3d91e) fully complete the Process.

###### A.2.2.9.1.2.3.5 - Process Definition For Offchain Vote [Core]  <!-- UUID: 3170b9a1-d074-4cbd-bb81-ae1661bc0ed8 -->

The documents herein define the process for an Offchain Vote for an Invocation of the Distribution Reward Primitive.

###### A.2.2.9.1.2.3.5.1 - Process Initiation Logic [Core]  <!-- UUID: 3b38ec56-64c1-4093-82f0-fd5a162d549c -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.3.5.1.1 - Triggers [Core]  <!-- UUID: c743c744-a699-4236-b6d9-80563f789421 -->

Triggers are specified herein.

###### A.2.2.9.1.2.3.5.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 51f50be4-00f4-4023-8d43-dff42e8c7571 -->

None.

###### A.2.2.9.1.2.3.5.1.1.2 - Document Update Triggers [Core]  <!-- UUID: b43edb36-1255-4e9d-92e2-9e4435c7bb2f -->

This process is triggered by the Artifact Update specified at Operational Facilitator Approves Proposal.

###### A.2.2.9.1.2.3.5.1.2 - Dependencies [Core]  <!-- UUID: 174e41b1-0e93-491c-8da1-50c0845947c3 -->

This process has no dependencies.

###### A.2.2.9.1.2.3.5.2 - Process Flow [Core]  <!-- UUID: d0ceb4ed-8f65-45c6-808e-fca702dc2a62 -->

The process flow for this process is defined herein:

- Using the finalized `Atlas Edit Proposal` content, the Operational Facilitator sets up an offchain Snapshot vote.
- Prime Agent token holders vote on the proposal.
- After the voting concludes, the Operational Facilitator records the result of the vote in the Powerhouse system.

###### A.2.2.9.1.2.3.5.3 - Required Primitive Inputs [Core]  <!-- UUID: b593ff77-2c46-418d-a7b3-9730437ce804 -->

The required Primitive Inputs to this process are defined herein.

- After Facilitator prepares Snapshot vote:
    - Edit `Artifact Edit Proposal` Document
        - Updated fields
            - Status
                - New value: set to `Pending Poll`
            - Off-chain Snapshot
                - New value: Populate with link to the official Snapshot page
        - Responsible party: Operational Facilitator
- Mutually Exclusive Input Pathways: The two Primitive Inputs below are mutually exclusive pathways. Once the vote concludes, the corresponding Pathway is followed to the exclusion of the other.
    - Proposal Passes
        - Edit `Artifact Edit Proposal` Document
            - Update fields
                - Status
                    - New value: set to `Poll Approved`
            - Responsible party: Operational Facilitator.
            - Trigger - Required Output: Proposal Passes
    - Proposal Fails
        - Updated fields
            - Edit `Artifact Edit Proposal` Document
                - Status
                    - New value: set to `Poll Rejected`
        - Responsible party: Operational Facilitator.
        - Trigger - Required Output: Proposal Fails

###### A.2.2.9.1.2.3.5.4 - Required Outputs [Core]  <!-- UUID: 1e95dff0-2a7f-461f-86f9-70433b888650 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.3.5.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: cc530c80-0c89-4c4a-b108-46a623f4f4c6 -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.1.2.3.5.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 1efa0fc5-5377-428f-a203-8c3c10dcc153 -->

The Agent Artifact documents specified herein are updated as the output of this process. The Output "sets" are mutually exclusive.

- Proposal Passes
    - Required Primitive Input Trigger: Proposal Passes see [A.2.2.9.1.2.3.5.3 - Required Primitive Inputs](b593ff77-2c46-418d-a7b3-9730437ce804)
    - Edit `Primitive Hub Document/In Progress Invocations Directory/Instance Name`
        - Updated fields
            - Invocation Status
                - New value: set to `Proposal Approved`
        - Responsible Party: Operational GovOps
        - Trigger - Process: [A.2.2.9.1.2.3.6 - Process Definition For Artifact Update](b3ed1e74-7ec2-4537-8e1d-2098dc17d984)
- Proposal Fails
    - Required Primitive Input Trigger: Proposal Fails see [A.2.2.9.1.2.3.5.3 - Required Primitive Inputs](b593ff77-2c46-418d-a7b3-9730437ce804)
    - Edit `Primitive Hub Document/In Progress Invocations Directory/Instance Name`
        - Updated fields
            - Invocation Status
                - New value: set to `Proposal Rejected`
        - Other Document Operations:
            - `Instance Configuration Document` is `Archived` in Primitive Hub Document/Hub Data Repository
        - Responsible Party: Operational GovOps

###### A.2.2.9.1.2.3.6 - Process Definition For Artifact Update [Core]  <!-- UUID: b3ed1e74-7ec2-4537-8e1d-2098dc17d984 -->

The documents herein define the Artifact Update process for an Invocation of the Distribution Reward Primitive.

###### A.2.2.9.1.2.3.6.1 - Process Initiation Logic [Core]  <!-- UUID: 005830a0-5845-4460-961a-9d5f15a722ab -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.3.6.1.1 - Triggers [Core]  <!-- UUID: 9e5fb847-18f1-4b86-989f-95ec770236b7 -->

Triggers are specified herein.

###### A.2.2.9.1.2.3.6.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 03ec388b-5e00-42da-a708-e2fd6a7d8775 -->

None.

###### A.2.2.9.1.2.3.6.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 309ac677-8841-4821-aba5-6cf637b8e7a7 -->

This process is triggered by the Artifact update specified in Proposal passes.

###### A.2.2.9.1.2.3.6.1.2 - Dependencies [Core]  <!-- UUID: d7ec33fc-6c67-4632-80b2-1fab854699bc -->

This process has no dependencies.

###### A.2.2.9.1.2.3.6.2 - Process Flow [Core]  <!-- UUID: 3a23ed21-d9ac-4575-9c53-806fddb10f5c -->

The process flow is defined herein.

- Using the Powerhouse interface, the Operational Facilitator updates the Agent Artifact with the approved Proposal content.

###### A.2.2.9.1.2.3.6.3 - Required Primitive Inputs [Core]  <!-- UUID: 6eb0901b-d324-4124-b27e-5f5416264f37 -->

The following inputs must be submitted into the Primitive using the Powerhouse interface.

- Edit `Instance Configuration Document` to reflect ratified Primitive Instance.
    - Updated fields
        - Parameters/Status - automatically inherits from `Primitive Hub Document`
        - Parameters/Reward Code
            - New Value: set to `Reward Code` value from approved Proposal
        - Parameters/Tracking Methodology
            - New Value: set to `Tracking Methodology` value from the approved Proposal
        - Parameters/Custom Instance Parameters
            - New Value: set to `Custom Instance Parameters` value from approved Proposal
        - Responsible Party: Operational GovOps [if not automated]

###### A.2.2.9.1.2.3.6.4 - Required Outputs [Core]  <!-- UUID: 231e3527-5534-42d4-b83e-0f99cb40bf76 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.3.6.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 108174f5-b53d-4bc0-8576-172b27021121 -->

The Sky Core Documents specified herein are updated as the output of this process.

###### A.2.2.9.1.2.3.6.4.1.1 - Onboarding Integrators Active Data Update [Core]  <!-- UUID: 4287ecd9-5ba6-4646-b949-306b494a108c -->

[A.2.2.9.1.2.1.4.2.0.6.1 - List Of Onboarding Integrators](eb644108-94fc-430f-ae5a-e3294b9dd9be) is updated as follows:

- Updated fields
    - `Onboarding Integrators`
        - New value: Delete the Integrator.
- Responsible Party: Operational GovOps
- Triggers: None

###### A.2.2.9.1.2.3.6.4.1.2 - Current Integrators Active Data Update [Core]  <!-- UUID: 1c0708d0-6388-4264-90f2-7a0d0b877012 -->

[A.2.2.9.1.2.1.4.1.0.6.1 - List Of Current Integrators](efbe7903-a76e-40f0-a440-56e463283157) is updated as follows:

- Updated fields
    - `Current Integrators`
        - New value: set to the name of the Integrator from the approved Proposal
    - `Reward Code`
        - New value: set to the Reward Code from the approved Proposal
    - `Tracking Methodology`
        - New value: set to the tracking methodology from the approved Proposal
- Responsible Party: Operational GovOps
- Triggers: None

###### A.2.2.9.1.2.3.6.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 8336c1ad-e182-4c91-b4f9-b5f743500457 -->

The Agent Artifact documents specified herein are updated as the output of this process.

###### A.2.2.9.1.2.3.6.4.2.1 - Instance Configuration Document Update [Core]  <!-- UUID: 3401c95d-3a9f-4af4-bc70-fb1be8f0f676 -->

The Document is updated as follows:

- Document Operations:
    - Document is moved from `In Progress Invocations` to `Active Instances`
- Responsible Party: Operational Facilitator

###### A.2.2.9.1.2.3.6.4.2.2 - Primitive Hub Document/In Progress Invocations Directory/Instance Name Update [Core]  <!-- UUID: f5b8f596-5999-4ed8-a998-9c920bb86c14 -->

The Document is updated as follows:

- Document Operations:
    - Document is converted into `Active Instances Directory` schema and moved into that subtree
- Updated fields
    - Instance Configuration Document location: link to `Instance Configuration Document` in `Active Instances` subtree
- Responsible Party: Operational Facilitator
- Trigger-Process: None.

###### A.2.2.9.1.2.4 - Instance Ongoing Management Protocol [Core]  <!-- UUID: 3af0e156-b5c0-493b-bd6f-80185072b7b1 -->

The documents herein define the process for the ongoing management of an Instance of the Distribution Reward Primitive.

###### A.2.2.9.1.2.4.1 - Routine Protocol [Core]  <!-- UUID: c2abdd22-fe0f-489e-b281-450e066db701 -->

The documents herein define the protocol for routine ongoing management of an Instance of the Distribution Reward Primitive.

###### A.2.2.9.1.2.4.1.1 - Process Definition For Reward Calculation By Operational Govops [Core]  <!-- UUID: 27229032-ddb6-41a5-a5d5-6168ccc3142f -->

The documents herein define the process for Distribution Reward Calculation by Operational GovOps. The Distribution Reward Calculation includes the calculation of the Fees for Unrewarded USDS Balances, the Fees for Rewarded USDS Balances, and the Prime Agent Management Fee. The Distribution Reward is paid to the Prime Agent, as specified in [A.2.2.4.2 - Reward Recipient And Sharing](40395562-d447-4c85-b670-c08d2341bcd2).

###### A.2.2.9.1.2.4.1.1.1 - Process Initiation Logic [Core]  <!-- UUID: a0a60c30-1c73-4bb1-b4c3-92a5541ff4b2 -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.4.1.1.1.1 - Triggers [Core]  <!-- UUID: 7a9450db-0d90-4578-ad14-6a8308b2b4b8 -->

Triggers are specified herein.

###### A.2.2.9.1.2.4.1.1.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 3e14118d-b60b-49c4-a730-90eb3ad606a9 -->

This process is triggered on the 1st of every month for each Instance of the Distribution Reward Primitive with an Instance Status of `Active`.

###### A.2.2.9.1.2.4.1.1.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 351bd87e-1795-4b00-ad05-2b9869394854 -->

None.

###### A.2.2.9.1.2.4.1.1.1.2 - Dependencies [Core]  <!-- UUID: dfd59dc4-365c-4718-833a-b859f00dff9b -->

This process has no dependencies.

###### A.2.2.9.1.2.4.1.1.2 - Process Flow [Core]  <!-- UUID: 70360ef3-14b5-4eaf-abc1-8c3ceb1596a1 -->

The process flow is defined herein:

- Operational GovOps calculates the eligible USDS and sUSDS balances using the Tracking Methodology specified in the Primitive Instance.
- Operational GovOps calculates the Distribution Reward due based on the USDS and sUSDS balances and the Distribution Reward formula for each.
- Operational GovOps updates the Powerhouse system with both the underlying data and their calculations.

###### A.2.2.9.1.2.4.1.1.3 - Required Primitive Inputs [Core]  <!-- UUID: 57921647-2a63-4d01-907b-131a50510d76 -->

The required Primitive Inputs to this process are specified herein.

- Edit `Distribution Reward Payments` Document (Active Data)
    - Updated fields
        - Status
            - New value: set to `In Progress`
        - Underlying data
            - New value: populate with underlying data used to calculate the eligible USDS and sUSDS balances
        - Eligible USDS balance
            - New value: populate with calculated value
        - Eligible sUSDS balance
            - New value: populate with calculated value
        - Distribution Reward Due
            - New value: populate with calculated value.
    - Responsible party: Operational GovOps.
    - Trigger-Process: [A.2.2.9.1.2.4.1.2 - Process Definition For Reward Issuance From Operational Executor Agent Buffer](ddd65b02-3a2b-4478-a435-989324c2f1b8).

###### A.2.2.9.1.2.4.1.1.4 - Required Outputs [Core]  <!-- UUID: 082e5d05-9394-4b4a-8ef2-0e6d8110c2cc -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.4.1.1.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 34264a04-6a76-4bf0-9b32-283992d9364a -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.1.2.4.1.1.4.2 - Agent Artifact Updates [Core]  <!-- UUID: f3ba519f-0d2f-4565-80be-3c095fc49b75 -->

No Agent Artifact documents are updated as the output of this process. The requirements specified [A.2.2.9.1.2.4.1.1.3 - Required Primitive Inputs](57921647-2a63-4d01-907b-131a50510d76) fully complete the Process.

###### A.2.2.9.1.2.4.1.2 - Process Definition For Reward Issuance From Operational Executor Agent Buffer [Core]  <!-- UUID: ddd65b02-3a2b-4478-a435-989324c2f1b8 -->

The documents herein define the process for Distribution Reward issuance from the Operational Executor Agent Buffer as part of ongoing management of an Instance of the Distribution Reward Primitive.

###### A.2.2.9.1.2.4.1.2.1 - Process Initiation Logic [Core]  <!-- UUID: a24bf9e6-3805-4a12-a277-ade2e24e0d77 -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.4.1.2.1.1 - Triggers [Core]  <!-- UUID: 18123d66-7a54-40dd-a4a7-389f83658247 -->

Triggers are specified herein.

###### A.2.2.9.1.2.4.1.2.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: aa6d4d8e-1b6a-41d6-b5f8-29dde7d5a55a -->

None.

###### A.2.2.9.1.2.4.1.2.1.1.2 - Document Update Triggers [Core]  <!-- UUID: a66e1d9d-f113-4e83-8a17-77ce1724c2c9 -->

This process is triggered by the Required Primitive Inputs specified in Edit Distribution Reward Payments Document (Active Data).

###### A.2.2.9.1.2.4.1.2.1.2 - Dependencies [Core]  <!-- UUID: 3741afa3-1593-4ca5-b90c-186f499b111b -->

This process has no dependencies.

###### A.2.2.9.1.2.4.1.2.2 - Process Flow [Core]  <!-- UUID: 3373c13d-907d-420b-9ad8-3cf6b4645359 -->

The process flow is defined herein.

- Operational GovOps makes the payment to the reward address specified in the Primitive Instance from the Operational Executor Agent Buffer.
- Operational GovOps updates the Powerhouse system with the transaction details.

###### A.2.2.9.1.2.4.1.2.3 - Required Primitive Inputs [Core]  <!-- UUID: 63ba8de2-55ed-4df5-9e11-016a006cf828 -->

The required Primitive Inputs to this process are specified herein.

- Edit `Distribution Reward Payments` Document (Active Data)
    - Updated fields
        - Status
            - New value: set to `Paid`
        - Transaction Details/Amount Paid
            - New value: populate with amount paid
        - Transaction Details/Tx hash
            - New value: populate with transaction hash
    - Responsible Party: Operational GovOps
    - Trigger - Process: [A.2.2.9.1.2.4.1.3 - Process Definition For Settlement Cycle And Core GovOps Review](dfd65786-e4be-4dad-9e34-cd6235a30a4f).

###### A.2.2.9.1.2.4.1.2.4 - Required Outputs [Core]  <!-- UUID: f33e0dee-b8e8-4d93-b56e-624dec274739 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.4.1.2.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 810220a0-0694-4174-b438-6fb0a4b98299 -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.1.2.4.1.2.4.2 - Agent Artifact Updates [Core]  <!-- UUID: ede7410d-a632-4209-ae79-7e3ba730cef1 -->

No Agent Artifact documents are updated as the output of this process. The requirements specified in [A.2.2.9.1.2.4.1.2.3 - Required Primitive Inputs](63ba8de2-55ed-4df5-9e11-016a006cf828) fully complete the process.

###### A.2.2.9.1.2.4.1.3 - Process Definition For Settlement Cycle And Core GovOps Review [Core]  <!-- UUID: dfd65786-e4be-4dad-9e34-cd6235a30a4f -->

The documents herein define the process for the Distribution Reward Settlement Cycle and Core GovOps review as part of ongoing management of an Instance of the Distribution Reward Primitive.

###### A.2.2.9.1.2.4.1.3.1 - Process Initiation Logic [Core]  <!-- UUID: e0495e9f-5dbd-4191-b52d-b87c6067d19a -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.4.1.3.1.1 - Triggers [Core]  <!-- UUID: 82b72cd2-b012-4865-9266-bcc35d644ec2 -->

Triggers are specified herein.

###### A.2.2.9.1.2.4.1.3.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 97fba609-d197-43dc-a6e1-72c6b2c48519 -->

This process is triggered at the beginning of every calendar quarter.

###### A.2.2.9.1.2.4.1.3.1.1.2 - Document Update Triggers [Core]  <!-- UUID: c96dd69d-2be3-451e-8551-a17de1c81579 -->

None.

###### A.2.2.9.1.2.4.1.3.1.2 - Dependencies [Core]  <!-- UUID: db7ad152-ee64-4185-b224-ad9ad7ec1093 -->

This process has no dependencies.

###### A.2.2.9.1.2.4.1.3.2 - Process Flow [Core]  <!-- UUID: 8b8308fd-e1ac-431c-8fe1-8e824ba7e978 -->

The process flow is defined herein.

- Core GovOps reviews Distribution Rewards calculations, including underlying data and calculation of balances and rewards due.
- Once Core GovOps has completed review, they update Powerhouse system to indicate that they confirm the accuracy of the Distribution Reward amounts.

###### A.2.2.9.1.2.4.1.3.3 - Required Primitive Inputs [Core]  <!-- UUID: b55afaef-db92-4bbf-8d80-258d5849ef1c -->

The required Primitive Inputs to this process are specified herein and are mutually exclusive pathways.

- Core GovOps Confirms Accuracy of Payment
    - Edit `Distribution Reward Payments` Active Data Document
        - Updated fields
            - Core GovOps Review/Confirmation
                - New value: populate with Yes
            - Core GovOps Review/Commentary
                - New value (optional): populate with reasoning
        - Responsible party: Core GovOps
        - Trigger - Process: [A.2.2.9.1.2.4.1.3.4.1 - Sky Core Atlas Updates](cca17fe9-3dc9-48ce-be26-39a1625b3690)
- Core GovOps Finds Inaccurate Payment
    - Edit `Distribution Reward Payments` Active Data Document
        - Updated fields
            - Core GovOps Review/Confirmation
                - New value: populate with No
            - Core GovOps Review/Commentary
                - New value (required): populate with reasoning
        - Responsible party: Core GovOps
        - Trigger - Process: Payment Inaccuracy Previously Found By Core GovOps

###### A.2.2.9.1.2.4.1.3.4 - Required Outputs [Core]  <!-- UUID: 7cb3c11b-7356-4967-b232-6667b66b6f51 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.4.1.3.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: cca17fe9-3dc9-48ce-be26-39a1625b3690 -->

The Sky Core Atlas documents specified herein are updated as the output of this process.

- Payment Accuracy Previously Confirmed By Core GovOps
    - The document [A.2.2.9.1.2.1.5.1.0.6.1 - Sky Core Distribution Reward Reimbursement Amounts](169eb312-ed63-4a83-9f5d-43b621c0705e) in the Sky Core Atlas is updated as follows:
        - Updated Fields
            - Status
                - New value: populate with `Pending Payment`
            - Confirmed Reimbursement Due
                - New value: populate with total Reimbursement amount
            - Reward Period
                - New Value: populate with reward period
            - Operational Executor Agent
                - New value: Populate with name of Operational Executor Agent
            - Prime Agent
                - New value: Populate with name of Prime Agent.
        - Responsible Party: Core GovOps
        - Triggers: [A.2.2.9.1.2.4.1.4 - Process Definition For Executive Vote Reimbursement](59259360-a288-4412-a39a-da3991c60f8f)
- Payment Inaccuracy Previously Found By Core GovOps
    - TBD

###### A.2.2.9.1.2.4.1.3.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 300fca05-66b1-4f31-966a-d26168ded7c3 -->

No Agent Artifact documents are updated as the output of this process.

###### A.2.2.9.1.2.4.1.4 - Process Definition For Executive Vote Reimbursement [Core]  <!-- UUID: 59259360-a288-4412-a39a-da3991c60f8f -->

The documents herein define the process for Distribution Reward Executive Vote reimbursement as part of ongoing management of an Instance of the Distribution Reward Primitive.

###### A.2.2.9.1.2.4.1.4.1 - Process Initiation Logic [Core]  <!-- UUID: f7bc89b8-424f-4f6a-8f1b-e173ca22f2ce -->

The process initiation logic is specified herein.

###### A.2.2.9.1.2.4.1.4.1.1 - Triggers [Core]  <!-- UUID: 14d233e1-0e8e-4dd5-915a-89f2b94f6e18 -->

Triggers are specified herein.

###### A.2.2.9.1.2.4.1.4.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: b61d8b1d-5a03-41ba-9bc7-49e1e876b855 -->

None.

###### A.2.2.9.1.2.4.1.4.1.1.2 - Document Update Triggers [Core]  <!-- UUID: c298f200-2ac8-4fc3-9d02-e05f4cf2f42f -->

This process is triggered by the Document Update specified in **`Sky Core Distribution Reward Reimbursement`** **Active Data Document Update**.

###### A.2.2.9.1.2.4.1.4.1.2 - Dependencies [Core]  <!-- UUID: ae1c6021-2790-43ce-9d9b-fe8a17a64b60 -->

This process has no dependencies.

###### A.2.2.9.1.2.4.1.4.2 - Process Flow [Core]  <!-- UUID: ffa519f8-71f9-4285-892f-49e79f8ed0de -->

The process flow is defined herein:

- Core GovOps includes the Distribution Reward reimbursement in the next standard Executive Vote.
- After the Executive Vote passes, Core GovOps updates the Powerhouse system with the transaction details.

###### A.2.2.9.1.2.4.1.4.3 - Required Primitive Inputs [Core]  <!-- UUID: 6b90e3a1-48ce-4ac2-852e-00a8e4edf152 -->

The required Primitive Inputs to this process are specified herein and organized as sequential stages.

- Core GovOps adds reimbursement to Executive Vote
    - Edit `Sky Core Distribution Reward Reimbursement Amounts`
        - Updated fields
            - Executive Vote Settlement/Executive Vote
                - New value: links to proposal
            - Status
                - New value: set to `Added to Executive Vote`
- After Executive Vote passes, Core GovOps updates Powerhouse system
    - Edit `Sky Core Distribution Reward Reimbursement Amounts`
        - Updated fields
            - Executive Vote Settlement / Transaction Details/ Amount Paid
                - New value: populate with amount paid to reimburse Operational Executor Agent Buffer
            - Executive Vote Settlement / Transaction Details / Tx Hash
                - New value: Populate with transaction hash
            - Status
                - New value: set to `Completed`

###### A.2.2.9.1.2.4.1.4.4 - Required Outputs [Core]  <!-- UUID: d14fff67-fd16-443b-9d32-763b052dce8b -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.1.2.4.1.4.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 7daf5881-434b-403e-b443-7bbfa0ce0534 -->

The Sky Core Atlas documents specified herein are updated as the output of this process.

###### A.2.2.9.1.2.4.1.4.4.1.1 - Sky Core Distribution Reward Reimbursement Active Data Update [Core]  <!-- UUID: 0c619a26-b9a6-495a-b7e6-a4a5c79c2da6 -->

The Document in the Sky Core Atlas is updated as follows:

- Updated fields
    - Status
        - New value: set to `Paid`
    - Responsible Party: Core GovOps
    - Trigger-Process: None

###### A.2.2.9.1.2.4.1.4.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 594d3b57-107d-44bc-a1bf-3f1291b8cccb -->

No Agent Artifact documents are updated as the output of this process.

###### A.2.2.9.1.2.4.2 - Non-Routine Protocol [Core]  <!-- UUID: e852bd1a-b257-4de9-b25b-63a5492ab720 -->

The documents herein define the protocol for non-routine ongoing management of an Instance of the Distribution Reward Primitive.

###### A.2.2.9.1.2.4.3 - Emergency Protocol [Core]  <!-- UUID: 81b89dda-558c-438e-8ba4-b75a977b8fd3 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of an Instance of the Distribution Reward Primitive.

#### A.2.2.9.2 - Integration Boost Primitive [Core]  <!-- UUID: 73577399-62e4-4a83-ae11-64ef7e7b7f20 -->

The documents herein govern the Integration Boost Primitive.

##### A.2.2.9.2.1 - Introduction [Core]  <!-- UUID: 84b4b5c7-7125-4f8e-815d-72b3be20a8e9 -->

The documents herein provide an introduction to the Integration Boost Primitive.

###### A.2.2.9.2.1.1 - Purpose [Core]  <!-- UUID: a9751ac4-b292-4c43-a5e5-168df9f0e41e -->

The Integration Boost Primitive provides a low complexity version of the Sky Savings Rate to Integration Boost Partners that hold USDS or lending markets that integrate USDS.

###### A.2.2.9.2.1.2 - Allowed Number Of Instances [Core]  <!-- UUID: 7853b196-73d9-4662-a4aa-f057aa64280c -->

Multiple instances of the Integration Boost Primitive are allowed. Each instance corresponds to an Integration Boost program.

###### A.2.2.9.2.1.3 - Multi-Instance Coordinator Document [Core]  <!-- UUID: 71c3bf8e-9c5c-447d-afb8-d6ca66acf45f -->

An Agent Artifact that has more than one active instance of the Integration Boost Primitive is not required to have a `Multi-Instance Coordinator Document`, since each Instance can be managed independently.

##### A.2.2.9.2.2 - Global Specification [Core]  <!-- UUID: eecfa6ad-3419-411e-b25a-1ccde2d6484b -->

The requirements herein apply universally across all possible deployments of the Integration Boost Primitive by Prime Agents. They include the steps that Agents must take to deploy the Primitive, including Global Activation of the Primitive, Instance Invocation, and ongoing management of the Primitive Instance(s).

###### A.2.2.9.2.2.1 - Base Elements [Core]  <!-- UUID: c398b383-3752-4534-aec6-4cd8e7292119 -->

The documents herein define the base elements of the Integration Boost Primitive.

###### A.2.2.9.2.2.1.1 - Integration Boost Partners [Core]  <!-- UUID: 31cb3b86-0125-4a04-996f-634b75b6cea2 -->

The Integration Boost is provided to DeFi protocol partners that allow users to deposit USDS balances. The Integration Boost is calculated as the Sky Savings Rate times the Unrewarded USDS balances in the Integration Boost Partner's protocol. Integration Boost payments are paid to the Prime Agent associated with the Integration Boost Partner, as specified in [A.2.2.4.2 - Reward Recipient And Sharing](40395562-d447-4c85-b670-c08d2341bcd2). The non-binding expectation is that the Integration Boost amount is passed through from the Prime Agent to the Integration Boost Partner, and from the Integration Boost Partner to USDS users, providing those users with the equivalent of the Sky Savings Rate.

Integration Boost Partners are Integrators that receive the Integration Boost, as part of the Integrator Program defined in [A.2.2.4.1 - Integrator Program](37c38f07-b5a0-40df-939c-a54330ea3c7b).

Current and onboarding Integrators are recorded in [A.2.2.9.1.2.1.4 - Current And Onboarding Integrators](f3952cc5-cde2-46b9-b575-034dda83570b).

###### A.2.2.9.2.2.1.2 - Data Submission [Core]  <!-- UUID: 756b466e-2bc0-43af-957f-d827593f5fe2 -->

The documents herein specify data submission requirements related to the Integrator Program.

###### A.2.2.9.2.2.1.2.1 - Data Verifiability Requirement [Core]  <!-- UUID: 6a2ec8d3-0403-46a9-8c96-3a9c86a59792 -->

Integration Boost Partners must submit net deposit data in such a form that the data can be verified by Sky using on-chain data. In the short term, the Core Council Risk Advisor calculates the net deposit data based on on-chain events and makes it available to Operational GovOps through an API endpoint. The API endpoint is [https://info-sky.blockanalitica.com/api/v1/incentivized-pools/](https://info-sky.blockanalitica.com/api/v1/incentivized-pools/) for Integration Boost Partners on Ethereum and [https://info-sky.blockanalitica.com/api/v1/solana-incentives/](https://info-sky.blockanalitica.com/api/v1/solana-incentives/) on Solana. In the long term, Operational GovOps assumes responsibility for ensuring that the data submission meets the on-chain verifiability requirement; this is done as part of their review of Invocations of the Integration Boost Primitive.

###### A.2.2.9.2.2.1.2.2 - Data Submission Responsible Party [Core]  <!-- UUID: 079abfa8-583a-4a95-a2d6-7fe50a1dd2dd -->

Integration Boost Partners must also identify a responsible party that will submit the net deposit data. In the near term, this is the Core Council Risk Advisor. In the long term, this may be the Integration Boost Partner, a third party contractor, or the Prime Agent or Operational GovOps themselves if they agree to do so.

###### A.2.2.9.2.2.1.2.3 - Data Submission Frequency [Core]  <!-- UUID: a26ea73f-ab67-4e02-93cd-b43d22a6e63c -->

Data is calculated on a weekly basis from Monday to Sunday for payment the following Monday. Failure to submit data on time will result in a delay of payment of the Integration Boost until the following week.

###### A.2.2.9.2.2.1.3 - Distribution [Core]  <!-- UUID: 3b3914d0-eb7b-4a49-bbca-5f6237a4a8ac -->

The documents herein define base elements of the Integration Boost Primitive related to the distribution of the Integration Boost.

###### A.2.2.9.2.2.1.3.1 - Cadence [Core]  <!-- UUID: 181954b6-d22c-4605-bffa-b5d964fbb10d -->

The Cadence is the frequency at which the Integration Boost is calculated and distributed. There are only three options available for the Reward Cadence: (1) weekly, (2) biweekly, or (3) monthly.

###### A.2.2.9.2.2.1.3.2 - Treasury Management [Core]  <!-- UUID: e27f2332-1072-4b61-84ab-efe6f2ca056e -->

The documents herein define the treasury management process.

###### A.2.2.9.2.2.1.3.2.1 - Near Term Process [Core]  <!-- UUID: 4ab621b4-ef8e-4b01-a6aa-9296601033c5 -->

In the short term, Integration Boost payments are made from the Demand Side Buffer (see [A.2.2.4.3 - Demand Side Buffer](862b6d83-f464-4125-8259-233b7de75ec4)).

###### A.2.2.9.2.2.1.3.2.2 - Long Term Process [Core]  <!-- UUID: 787276c9-728b-491f-84d6-c1303fe72986 -->

In the long term, Operational GovOps calculates the Integration Boost for each occurrence of the specified Cadence. Operational GovOps then pays the Integration Boost recipient from its Buffer. Later, Sky Core reimburses the Operational Agent Buffer for the amount paid as part of the Settlement Cycle. This minimizes the role of Sky Core in Integration Boost payments and emphasizes the primary role of the Operational Executor Agent, acting through Operational GovOps, in implementing the Sky Primitives. The process is specified in further detail in [A.2.2.9.2.2.4.1 - Routine Protocol](04864587-25ef-4179-b237-4dd0a23485a4).

###### A.2.2.9.2.2.1.3.3 - Payment Errors [Core]  <!-- UUID: 8d19b08f-d10e-4db2-9e21-03e5021bdaec -->

If it is discovered that previous Integration Boost calculations were made erroneously, underpayments are resolved retroactively. In cases of overpayment, the Prime Agent associated with the affected Reward Code must reimburse Sky the overpayment amount and can use future Integration Boost payments to reimburse itself.

###### A.2.2.9.2.2.1.4 - Distribution Rewards [Core]  <!-- UUID: d71a7b9c-3d0e-4383-9671-098bead326c1 -->

Net USDS balances held in a DeFi protocol that is receiving an Integration Boost also receive the Distribution Reward.

###### A.2.2.9.2.2.1.4.1 - Reporting Of Net USDS Balances Is Valid Tracking Methodology [Core]  <!-- UUID: a4ca2e70-d013-4c54-8e17-1d6f352ddbc0 -->

The methodology used to report net USDS balances in the protocol for the Integration Boost is itself an acceptable Tracking Methodology for purposes of the Distribution Reward.

###### A.2.2.9.2.2.1.4.2 - No Double Payments [Core]  <!-- UUID: 5828a3a0-243d-48a5-b537-297015a0c5f5 -->

Distribution Reward may only be paid on net USDS balances of an Integration Boost partner to the extent that a Distribution Reward is not already being paid on those balances.

###### A.2.2.9.2.2.1.4.3 - Distribution Reward Sharing With Integration Boost Partners [Core]  <!-- UUID: c27d41eb-61f4-4daa-a9c3-b463fa840f60 -->

Distribution Reward sharing with Integration Boost Partners is subject to bilateral negotiation between the Prime Agent and the Integration Boost Partner, as specified in [A.2.2.4.2 - Reward Recipient And Sharing](40395562-d447-4c85-b670-c08d2341bcd2).

###### A.2.2.9.2.2.1.5 - Integration Boost Reimbursement [Core]  <!-- UUID: 63ff5ae5-4a50-4d44-b7e4-526608c44598 -->

The documents herein specify the Integration Boost reimbursement.

###### A.2.2.9.2.2.1.5.1 - Sky Core Integration Boost Reimbursement [Active Data Controller]  <!-- UUID: 7ed013c9-f7ac-4459-8675-8bbd398d5133 -->

The Integration Boost reimbursement payments are defined as Active Data in [A.2.2.9.2.2.1.5.1.0.6.1 - Sky Core Integration Boost Reimbursement Amounts](8cbff90b-5633-427e-91da-0fb775812535).

The Active Data is updated as follows:

- The Responsible Party is Core GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.2.9.2.2.1.5.1.0.6.1 - Sky Core Integration Boost Reimbursement Amounts [Active Data]  <!-- UUID: 8cbff90b-5633-427e-91da-0fb775812535 -->

The current Sky Core Integration Boost Reimbursement Amounts are:

###### A.2.2.9.2.2.2 - Global Activation [Core]  <!-- UUID: 4ad2a180-10bd-443d-ba5b-3e46f2b5cf52 -->

An Agent who intends to deploy the Integration Boost Primitive must first Globally Activate it.

###### A.2.2.9.2.2.2.1 - Process Initiation Logic [Core]  <!-- UUID: b68f9009-e002-4d92-bcb6-c0aeca9239a5 -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.2.1.1 - Triggers [Core]  <!-- UUID: ea3fd0be-411c-44e4-9539-2c88000110b5 -->

Triggers are specified herein.

###### A.2.2.9.2.2.2.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 7457b041-e037-43fa-aee9-107bacdb3acb -->

None.

###### A.2.2.9.2.2.2.1.1.2 - Document Update Triggers [Core]  <!-- UUID: a007505e-aa58-40f5-bf83-1ded2aa87588 -->

None.

###### A.2.2.9.2.2.2.1.2 - Dependencies [Core]  <!-- UUID: befbf1d8-aa4e-4326-9536-6620754cc96b -->

See [A.2.2.1.2.4 - Changing A Primitive’s Global Activation Status](51cfca28-c8de-457a-abc4-8ce1f64abb91) for constraints on when an Agent can Globally Activate this Primitive.

###### A.2.2.9.2.2.2.2 - Process Flow [Core]  <!-- UUID: 163b998a-50fe-4bbe-872c-748f526f7604 -->

The Prime Agent uses the Powerhouse interface to Globally Activate (toggle on) the Integration Boost Primitive.

###### A.2.2.9.2.2.2.3 - Required Primitive Inputs [Core]  <!-- UUID: 5e673229-0130-4b2c-94ce-f8597babd9c1 -->

The following inputs must be submitted into the Primitive using the Powerhouse interface:

- **Create** `Primitive Hub Document`
    - Updated Field: Global Activation Status
        - New Value: set to `Activated`

###### A.2.2.9.2.2.2.4 - Required Outputs [Core]  <!-- UUID: 9a9b56f4-eef8-4d31-af06-3b6d5ba4cb60 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.2.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 74f88b57-beef-4cae-a2a6-fafd74812e5c -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.2.2.2.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 35c38264-03ec-4485-9de6-2ff368981066 -->

No Agent Artifact documents are updated as the output of this process. The requirements specified in [A.2.2.9.2.2.2.3 - Required Primitive Inputs](5e673229-0130-4b2c-94ce-f8597babd9c1) fully complete the Process.

###### A.2.2.9.2.2.3 - Instance Invocation Protocol [Core]  <!-- UUID: a1dc075e-6c36-4375-89ff-fe9bb2c7a2fa -->

After fulfilling the requirements for Global Activation, an Agent can Invoke its first Instance of the Integration Boost Primitive by following the sequential process specified herein. Subsequent Invocations of the Primitive must adhere to the same requirements defined below.

###### A.2.2.9.2.2.3.1 - Process Definition For Initial Opportunity Identification And Planning [Core]  <!-- UUID: a14cea92-f114-4cc8-abfe-77b202e3c1f7 -->

The documents herein specify the process definition for initial opportunity identification and planning.

###### A.2.2.9.2.2.3.1.1 - Process Initiation Logic [Core]  <!-- UUID: 2645e2f0-2624-4fd0-bdc7-2eb09fe28498 -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.3.1.1.1 - Triggers [Core]  <!-- UUID: 32cc16f9-2d59-4722-b56a-7f9eae661b57 -->

Triggers are specified herein.

###### A.2.2.9.2.2.3.1.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: e06ee9c9-72a5-47ac-8a20-400b3615994a -->

None.

###### A.2.2.9.2.2.3.1.1.1.2 - Document Update Triggers [Core]  <!-- UUID: def2ad89-c78b-4662-a2c3-5a889dbbd722 -->

None.

###### A.2.2.9.2.2.3.1.1.2 - Dependencies [Core]  <!-- UUID: 85a0d037-6b82-4435-aa6d-2d8b481c8f60 -->

This process is dependent on a Prime Agent Globally Activating the Integration Boost Primitive pursuant to [A.2.2.9.2.2.2 - Global Activation](4ad2a180-10bd-443d-ba5b-3e46f2b5cf52).

###### A.2.2.9.2.2.3.1.2 - Process Flow [Core]  <!-- UUID: 179cb7a5-60ee-4fa0-bc22-d70d4a15c575 -->

The process flow is defined herein.

- The Prime Agent identifies a DeFi protocol or market where an Integration Boost would drive adoption. The Prime Agent estimates the potential earnings from the Distribution Reward associated with the incremental USDS usage versus the operational cost of funding the Sky Savings Rate payouts.
- The Prime Agent and the prospective Integration Boost Partner discuss (1) the proposed Integration Boost cadence and (2) whether and how the Prime Agent will share a portion of the Distribution Reward with the Integration Boost Partner.

###### A.2.2.9.2.2.3.1.3 - Required Primitive Inputs [Core]  <!-- UUID: b91d0eb6-fa86-486c-8350-4564bdb5af09 -->

The required Primitive Inputs for this process are defined herein and organized in sequential stages.

- Drafting of Initial Planning Document
    - Create `Initial Planning Document`
        - Updated fields
            - `Status`
                - New value: set to `Drafting`
            - `Integration Partner Name`
                - New Value: set to Integration Partner name
            - `Integration Partner Reward Address`
                - New Value: set to Integration Partner reward address
            - `Integration Partner Chain`
                - New Value: set to Integration Partner chain
            - `Integration Boost Cadence`
                - New Value: set to Integration Boost cadence
            - `Integration Boost Data Submission Format`
                - New Value: populate with details for format of data submission
            - `Integration Boost Data Submission Responsible Actor`
                - New Value: set to Actor responsible for data submission
            - `Integration Boost Savings Rate Adjustment Strategy`
                - New Value: populate with details for handling adjustments to Sky Savings Rate
            - `Custom Instance Parameters`
                - New Value: populate with details for any custom parameters
        - Responsible Party: Prime Agent Team
        - Trigger - Required Output: After Prime Agent's `Initial planning document` Status is set to `Drafting`
- Initial Planning Document triggered for GovOps review
    - Edit `Initial Planning Document`
        - Updated fields
            - `Integration Boost Savings Rate Adjustment Strategy`
                - New value: updated content, as applicable
            - `Status`
                - New value: set to `Ready for GovOps Review`
        - Responsible party: Prime Agent
        - Trigger - Required Output: After Prime Agent's `Initial planning document` Status is set to `Ready for GovOps review`.

###### A.2.2.9.2.2.3.1.4 - Required Outputs [Core]  <!-- UUID: c0e07df6-d6b9-4268-95a6-f0f42877a639 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.3.1.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 991aaf4f-3d85-41c3-b0c3-d1cf3a84ec0d -->

The Sky Core Atlas is updated pursuant to the following requirements.

###### A.2.2.9.2.2.3.1.4.1.1 - Onboarding Integrators Active Data Update [Core]  <!-- UUID: a227491c-903f-4571-aad0-b76422a5ea7f -->

[A.2.2.9.1.2.1.4.2.0.6.1 - List Of Onboarding Integrators](eb644108-94fc-430f-ae5a-e3294b9dd9be) is updated as follows:

- Updated fields
    - `Onboarding Integrators/Integrator Name`
        - New value: set to the name of the Integrator
- Responsible Party: Operational GovOps

###### A.2.2.9.2.2.3.1.4.2 - Agent Artifact Updates [Core]  <!-- UUID: d86e5f9f-7b1c-4605-9253-4281a6bdbc13 -->

The Agent Artifact is updated pursuant to the following requirements. Each Output "set" is triggered following the completion of its respective Input stage, which latter is defined in [A.2.2.9.2.2.3.1.3 - Required Primitive Inputs](b91d0eb6-fa86-486c-8350-4564bdb5af09).

- After Prime Agent's `Initial planning document` Status is set to `Drafting`
    - Create `Instance Configuration` Document for prospective Primitive Instance. The Instance Configuration Document contains a `Data Repository`.
        - Instance Status: (automatically inherits from `Primitive Hub Document`)
    - Edit `Primitive Hub Document/In Progress Invocations Directory/Instance Name`
        - Updated fields:
            - Invocation Status:
                - New value: set to `Planning`
            - Instance Configuration Document Location
                - New value: link to `Instance Configuration Document` (created at Create `Instance Configuration` Document for prospective Primitive Instance. The Instance Configuration Document contains a `Data Repository`.)
    - Responsible party: Operational GovOps [automated]
- After Prime Agent's `Initial planning document` Status is set to `Ready for GovOps review`.
    - Edit `Primitive Hub Document/In Progress Invocations/Instance Name`
        - Updated fields:
            - Invocation Status:
                - New value: set to `Pending GovOps review`
        - Responsible party: Operational GovOps [ automated]
        - Trigger - Process: [A.2.2.9.2.2.3.2 - Process Definition for Operational GovOps Review](38c54d2b-715b-433d-a9ff-af5cbecc89a2).

###### A.2.2.9.2.2.3.2 - Process Definition for Operational GovOps Review [Core]  <!-- UUID: 38c54d2b-715b-433d-a9ff-af5cbecc89a2 -->

The documents herein define the process for Operational GovOps Review for an Invocation of the Integration Boost Primitive.

###### A.2.2.9.2.2.3.2.1 - Process Initiation Logic [Core]  <!-- UUID: ef37ff82-5639-4b5a-88b3-04cc4a4539cb -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.3.2.1.1 - Triggers [Core]  <!-- UUID: cb905fcc-6834-42a4-a0e8-534e600fad7e -->

Triggers are specified herein.

###### A.2.2.9.2.2.3.2.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: ff9674e1-174c-4365-ba27-4af0aa10539e -->

None.

###### A.2.2.9.2.2.3.2.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 4290c4b4-5c4d-4de5-bcbe-7d4d6db8b755 -->

This process is triggered by the Artifact Update specified at Edit `Primitive Hub Document/In Progress Invocations/Instance Name`.

###### A.2.2.9.2.2.3.2.1.2 - Dependencies [Core]  <!-- UUID: 921d945d-5e36-4ffd-8c30-447aeca18045 -->

This process has no dependencies.

###### A.2.2.9.2.2.3.2.2 - Process Flow [Core]  <!-- UUID: 0eba9704-14c9-4be3-ab41-62129ff9f162 -->

The process flow is defined herein:

- Operational GovOps reviews the `Initial Planning Document` to ensure:
    - The submitted data can be verified using on-chain data;
    - the Savings Rate Adjustment Strategy ensures that the payment on USDS balances equals the Sky Savings Rate, and
    - the submitted data accurately reflects USDS deposits in the Integration Partner protocol and there is no possibility that rewards could be "double counted" (i.e. multiple actors being paid for the same USDS balance).
- Operational GovOps submits its feedback into the `Operational GovOps Review Document` (created at Create `Operational GovOps Review Document`) along with suggested changes, if any.
- The Prime Agent incorporates feedback from Operational GovOps and edits its `Initial Planning Document` as needed.

###### A.2.2.9.2.2.3.2.3 - Required Primitive Inputs [Core]  <!-- UUID: 1eafc42a-1fd2-4f96-988c-8dc37c1ab317 -->

The following inputs must be submitted into the Primitive using the Powerhouse interface.

- Create `Operational GovOps Review Document`
    - Updated fields
        - `Initial Planning Document`
            - New Value: automatically links to respective Document
        - `Feedback Summary`
            - New Value: GovOps populates with its review commentary and suggested changes that are agreed to by Agent and GovOps, if any.
        - Responsible party: Operational GovOps.

###### A.2.2.9.2.2.3.2.4 - Required Outputs [Core]  <!-- UUID: 0bce1c09-ba85-418f-8cf7-0f51c8fa0584 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.3.2.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 689a6ce6-0091-4e6a-b634-27ade6064e6b -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.2.2.3.2.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 22166d2b-40bc-4094-a3d8-fce46699a905 -->

The Agent Artifact is updated pursuant to the following requirements.

###### A.2.2.9.2.2.3.2.4.2.1 - Initial Planning Document Update [Core]  <!-- UUID: ddcfe438-e322-425b-82c6-3bba3ce33823 -->

The Document is updated as follows.

- Updated fields
    - `Integration Boost Savings Rate Adjustment Strategy`
        - New Value: as applicable, update to reflect any changes agreed to between the Prime Agent and Operational GovOps
    - `Integration Boost Data Submission Format`
        - New Value: as applicable, update to reflect any changes agreed to between the Prime Agent and Operational GovOps
    - Responsible Party: Operational GovOps

###### A.2.2.9.2.2.3.2.4.2.2 - Primitive Hub Document Update [Core]  <!-- UUID: 09ddd2c5-3768-4538-b979-629e1b369299 -->

The Document is updated as follows.

- Updated fields
    - Active instances/Instance name/Instance status -
        - New value: set to `Proposal drafting in progress`
- Responsible Party: Operational GovOps [automated]
- Triggers: [A.2.2.9.2.2.3.3 - Process Definition for Artifact Update Draft](6a8b5e8b-cca6-48be-b543-6db468f83ebb).

###### A.2.2.9.2.2.3.3 - Process Definition for Artifact Update Draft [Core]  <!-- UUID: 6a8b5e8b-cca6-48be-b543-6db468f83ebb -->

The documents herein define the process for preparing the Artifact Update Draft for an Invocation of the Integration Boost Primitive.

###### A.2.2.9.2.2.3.3.1 - Process Initiation Logic [Core]  <!-- UUID: cc3d967c-ec99-4c9c-a874-c42b8412791d -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.3.3.1.1 - Triggers [Core]  <!-- UUID: 428d6e85-5c6d-4469-9bc8-e1a127427ac0 -->

Triggers are specified herein.

###### A.2.2.9.2.2.3.3.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 42848ad7-ad2e-402f-8ec5-cf6ee991c46c -->

None.

###### A.2.2.9.2.2.3.3.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 98b5465e-add9-4ae0-a02e-1c5be6006410 -->

This process is triggered by the Document Update specified at [A.2.2.9.2.2.3.2.4.2.2 - Primitive Hub Document Update](09ddd2c5-3768-4538-b979-629e1b369299).

###### A.2.2.9.2.2.3.3.1.2 - Dependencies [Core]  <!-- UUID: a616c3f6-b252-4d85-996a-019dea9f01e7 -->

This process has no dependencies.

###### A.2.2.9.2.2.3.3.2 - Process Flow [Core]  <!-- UUID: c860168e-b88e-4d2a-ad0b-388288d1e0cb -->

The process flow is defined herein:

- The Prime Agent creates the `Artifact Edit Draft` Document and works to finalize its draft of the Artifact Edit per discussions with Operational GovOps.
- When draft is finalized, the Prime Agent triggers the creation of the `Artifact Edit Proposal`, which inherits content from the finalized `Artifact Edit Draft` Document.
- The Prime Agent submits the `Artifact Edit Proposal` Document to the Powerhouse system.

###### A.2.2.9.2.2.3.3.3 - Required Primitive Inputs [Core]  <!-- UUID: 01214a59-5119-4c77-ad41-c9d3dd72a517 -->

The required Primitive Inputs for this process are defined herein and implemented in sequential stages.

- Agent creates `Artifact Edit Draft` document; drafting in progress
    - Edit `Artifact Edit Draft`
        - Updated fields
            - Status
                - New value: set to `In Progress`
            - Content
                - New value: populate with drafted content
- Agent finalizes `Artifact Edit Draft`
    - Edit `Artifact Edit Draft`
        - Updated fields
            - Status
                - New value: set to `Draft Finalized`
- Powerhouse System Creates `Artifact Edit Proposal` Document
    - Updated fields
        - Content
            - New value: Inherits data from `Artifact Edit Draft` Document’s Content field.
    - Responsible party: Operational GovOps [if not automated]
- Agent submits `Artifact Edit Proposal` Document to Powerhouse system
    - Updated fields
        - Status:
            - New value: set to `Pending Facilitator Review`
    - Responsible Party: Agent

###### A.2.2.9.2.2.3.3.4 - Required Outputs [Core]  <!-- UUID: bea2c790-2359-4bb7-8744-3f43deb05d26 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.3.3.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 7e4e6528-b8a7-4aff-8d98-3cc3279c4f28 -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.2.2.3.3.4.2 - Agent Artifact Updates [Core]  <!-- UUID: f654be61-baa0-4d5e-8d66-a9d8b3d5b277 -->

The Agent Artifact documents specified herein are updated as the output of this process.

###### A.2.2.9.2.2.3.3.4.2.1 - Primitive Hub Document Update [Core]  <!-- UUID: e7fc7c2e-b6fc-4e0f-ae10-debb54124e8e -->

The Document in the Agent Artifact is updated as follows:

- Updated fields
    - Active Instances/Instance Name/Instance Status
        - New value: `Proposal Pending Facilitator Review`
- Responsible Party: Operational GovOps
- Triggers: [A.2.2.9.2.2.3.4 - Process Definition for Operational Facilitator Review](2d1d83ea-2a90-4c34-93ea-5bea390f3f62).

###### A.2.2.9.2.2.3.4 - Process Definition for Operational Facilitator Review [Core]  <!-- UUID: 2d1d83ea-2a90-4c34-93ea-5bea390f3f62 -->

The documents herein define the process for Operational Facilitator Review for an Invocation of the Integration Boost Primitive.

###### A.2.2.9.2.2.3.4.1 - Process Initiation Logic [Core]  <!-- UUID: 53016a06-1989-49af-8629-8cac254ef771 -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.3.4.1.1 - Triggers [Core]  <!-- UUID: 9fa7d744-2f7d-4fb5-81e2-0b348eb01bb6 -->

Triggers are specified herein.

###### A.2.2.9.2.2.3.4.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: c3b16255-ecdc-4d42-9345-945ede629203 -->

None.

###### A.2.2.9.2.2.3.4.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 555a08a4-e028-44bd-9ba2-91e4bbf61644 -->

This process is triggered by the Document Update specified at [A.2.2.9.2.2.3.2.4.2.2 - Primitive Hub Document Update](09ddd2c5-3768-4538-b979-629e1b369299).

###### A.2.2.9.2.2.3.4.1.2 - Dependencies [Core]  <!-- UUID: f19c7277-65b4-4755-8756-fb0a242ba6a2 -->

This process has no dependencies.

###### A.2.2.9.2.2.3.4.2 - Process Flow [Core]  <!-- UUID: 1b0c0956-1890-405f-b27b-22399b04526c -->

The process flow is defined herein.

- The Operational Facilitator reviews the `Artifact Edit Proposal` to ensure alignment with the Sky Core Atlas and the Agent Artifact.
- Where the Proposal is determined to be aligned, the Operational Facilitator updates the `Artifact Edit Proposal` Document to reflect their approval and commentary, if any.
- Where the Proposal is determined to be misaligned, the Operational Facilitator updates the `Artifact Edit Proposal` document to reflect their rejection and commentary. Commentary is required where the Operational Facilitator rejects the proposal for misalignment.

###### A.2.2.9.2.2.3.4.3 - Required Primitive Inputs [Core]  <!-- UUID: 7f991abf-3395-4f92-82e1-88e991ebd97a -->

The required Primitive Inputs to this process are defined herein and organized as two mutually exclusive pathways. Once the Review outcome is determined by the Facilitator, the corresponding Pathway is followed to the exclusion of the other.

- Operational Facilitator Approves Proposal
    - Edit `Artifact Edit Proposal`
        - Updated fields
            - `Operational Facilitator Review/Review Decision`
                - New value: set to `Approved`
            - `Commentary`
                - New value (optional): populate with reasoning for Approval
            - `Status`
                - New value: set to `Proposal Approved by Facilitator` [automated]
        - Responsible party: Operational Facilitator
        - Trigger-Process: [A.2.2.9.2.2.3.5 - Process Definition for Offchain Vote](24fa76f6-4728-4f1d-97ff-fd7e72dac2ac).
- Operational Facilitator Rejects Proposal
    - Edit `Artifact Edit Proposal`
        - Updated fields
            - `Operational Facilitator Review/Review Decision`
                - New value: set to `Rejected`
            - `Commentary`
                - New value (required): populate with reasoning for Rejection
            - `Status`
                - New value: set to `Proposal Rejected By Facilitator` [automated]
        - Responsible party: Operational Facilitator

###### A.2.2.9.2.2.3.4.4 - Required Outputs [Core]  <!-- UUID: c7436489-4aac-47cb-be2d-31774bd7ee99 -->

The documents herein specify the required outputs from this process, if any.

###### A.2.2.9.2.2.3.4.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: d7e64cf2-9f1a-4057-8395-fc1eca5c3059 -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.2.2.3.4.4.2 - Agent Artifact Updates [Core]  <!-- UUID: d5cce836-259e-48df-ba77-89d58d1476cc -->

No Agent Artifact documents are updated as the output of this process. The requirements specified in [A.2.2.9.2.2.3.4.3 - Required Primitive Inputs](7f991abf-3395-4f92-82e1-88e991ebd97a) fully complete the Process.

###### A.2.2.9.2.2.3.5 - Process Definition for Offchain Vote [Core]  <!-- UUID: 24fa76f6-4728-4f1d-97ff-fd7e72dac2ac -->

The documents herein define the process for an Offchain Vote for an Invocation of the Integration Boost Primitive.

###### A.2.2.9.2.2.3.5.1 - Process Initiation Logic [Core]  <!-- UUID: e5c0a813-e8d6-4687-a1ac-c9abbd7bb29f -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.3.5.1.1 - Triggers [Core]  <!-- UUID: c5db0c30-6a19-492c-9389-926ffcbbca06 -->

Triggers are specified herein.

###### A.2.2.9.2.2.3.5.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: c6ad2b62-8f38-41cd-987f-f771f1a53e38 -->

None.

###### A.2.2.9.2.2.3.5.1.1.2 - Document Update Triggers [Core]  <!-- UUID: bac65a98-2e36-471a-8d3b-68d207ede4e2 -->

This process is triggered by the Artifact Update specified at Operational Facilitator Approves Proposal.

###### A.2.2.9.2.2.3.5.1.2 - Dependencies [Core]  <!-- UUID: bfdafaa4-e8bb-499b-99e6-f748d86cc569 -->

This process has no dependencies.

###### A.2.2.9.2.2.3.5.2 - Process Flow [Core]  <!-- UUID: 185d7f3b-9612-42ef-bde7-c9a64ad3ceab -->

The process flow for this process is defined herein:

- Using the finalized `Atlas Edit Proposal` content, the Operational Facilitator sets up an offchain Snapshot vote.
- Prime Agent token holders vote on the proposal.
- After the voting concludes, the Operational Facilitator records the result of the vote in the Powerhouse system.

###### A.2.2.9.2.2.3.5.3 - Required Primitive Inputs [Core]  <!-- UUID: d247fec5-a19d-4307-94de-a2cbcc368d64 -->

The required Primitive Inputs to this process are defined herein.

- After Facilitator prepares Snapshot vote:
    - Edit `Artifact Edit Proposal` Document
        - Updated fields
            - Status
                - New value: set to `Pending Poll`
            - Off-chain Snapshot
                - New value: Populate with link to the official Snapshot page
        - Responsible party: Operational Facilitator
- Mutually Exclusive Input Pathways: The two Primitive Inputs below are mutually exclusive pathways. Once the vote concludes, the corresponding Pathway is followed to the exclusion of the other.
    - Proposal Passes
        - Edit `Artifact Edit Proposal` Document
            - Update fields
                - Status
                    - New value: set to `Poll Approved`
            - Responsible party: Operational Facilitator.
            - Trigger - Required Output: Proposal passes
    - Proposal Fails
        - Updated fields
            - Edit `Artifact Edit Proposal` Document
                - Status
                    - New value: set to `Poll Rejected`
            - Responsible party: Operational Facilitator.
            - Trigger - Required Output: Proposal fails

###### A.2.2.9.2.2.3.5.4 - Required Outputs [Core]  <!-- UUID: bae40b55-4f53-4992-a872-228fd3d87671 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.3.5.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 43a3722c-97d0-4389-9d3b-4ac24901d365 -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.2.2.3.5.4.2 - Agent Artifact Updates [Core]  <!-- UUID: adfb66a3-4f73-4fcc-bfa2-f5126503187c -->

The Agent Artifact documents specified herein are updated as the output of this process. The Output "sets" are mutually exclusive.

- Proposal passes
    - Required Primitive Input Trigger: Proposal Passes
    - **Edit** `Primitive Hub Document`
        - Fields Updated
            - Active instances/instance name/instance status - set to `Approved`
        - Responsible Party: Operational GovOps
        - Trigger - Process: [A.2.2.9.2.2.3.6 - Process Definition for Artifact Update](182ca3dc-108f-4941-ae2e-eb01c345125b).
- Proposal fails
    - Required Primitive Input Trigger: Proposal Fails
    - **Edit** `Primitive Hub Document`
        - Fields Updated
            - Active instances/instance name/instance status - set to `Rejected`
        - Other Document Operations:
            - `Instance Configuration Document` is `Archived` in Primitive Hub Document/Data Repository
        - Responsible Party: Operational GovOps

###### A.2.2.9.2.2.3.6 - Process Definition for Artifact Update [Core]  <!-- UUID: 182ca3dc-108f-4941-ae2e-eb01c345125b -->

The documents herein define the Artifact Update process for an Invocation of the Integration Boost Primitive.

###### A.2.2.9.2.2.3.6.1 - Process Initiation Logic [Core]  <!-- UUID: 59306024-9642-4f4c-891e-dc515e1eff8e -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.3.6.1.1 - Triggers [Core]  <!-- UUID: 7ff087ca-2b81-45e2-98e9-08fd184722bc -->

Triggers are specified herein.

###### A.2.2.9.2.2.3.6.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 95379a19-4115-4a94-a525-67ea27ccab85 -->

None.

###### A.2.2.9.2.2.3.6.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 97e2c2b5-f17b-46a4-9e01-9b782429bd39 -->

This process is triggered by the Artifact update specified in Proposal passes.

###### A.2.2.9.2.2.3.6.1.2 - Dependencies [Core]  <!-- UUID: 1c0ce5c0-df9a-417e-a3d4-2b09e96787f6 -->

This process has no dependencies.

###### A.2.2.9.2.2.3.6.2 - Process Flow [Core]  <!-- UUID: 48863e96-796e-4953-b811-cbbfdd294098 -->

The process flow is defined herein.

- Using the Powerhouse interface, the Operational Facilitator updates the Agent Artifact with the approved Proposal content.

###### A.2.2.9.2.2.3.6.3 - Required Primitive Inputs [Core]  <!-- UUID: 51ca2399-8c7f-4c2a-843a-c85f6c670d13 -->

The following inputs must be submitted into the Primitive using the Powerhouse interface.

- Edit `Instance Configuration Document` to reflect ratified Primitive Instance.
    - Updated fields
        - Parameters/Status - automatically inherits from `Primitive Hub Document`
        - Parameters/Integration Partner Name
            - New Value: set to `Integration Partner Name` value from approved Proposal
        - Parameters/Integration Partner Reward Address
            - New Value: set to `Integration Partner Reward Address` value from approved Proposal
        - Parameters/Integration Partner Chain
            - New Value: set to `Integration Partner Chain` value from approved Proposal
        - Parameters/Integration Boost Cadence
            - New Value: set to `Integration Boost Cadence` value from approved Proposal
        - Parameters/Integration Boost Data Submission Format
            - New Value: set to `Integration Boost Data Submission Format` value from approved Proposal
        - Parameters/Integration Boost Data Submission Responsible Actor
            - New Value: set to `Integration Boost Data Submission Responsible Actor` value from approved Proposal
        - Parameters/Integration Boost Savings Rate Adjustment Strategy
            - New Value: set to `Integration Boost Savings Rate Adjustment Strategy` value from approved Proposal
        - Parameters/Custom Instance Parameters
            - New Value: set to `Custom Instance Parameters` value from approved Proposal
        - Responsible party: Operational GovOps [if not automated]

###### A.2.2.9.2.2.3.6.4 - Required Outputs [Core]  <!-- UUID: bd74388f-69d8-48fc-bab8-522f1b3b5806 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.3.6.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 221cde4c-acb8-46c9-866b-7878fc6e5646 -->

The Sky Core Documents specified herein are updated as the output of this process.

###### A.2.2.9.2.2.3.6.4.1.1 - Onboarding Integrators Active Data Update [Core]  <!-- UUID: 847092ba-eb97-47ee-a121-6c8e505bc480 -->

[A.2.2.9.1.2.1.4.2.0.6.1 - List Of Onboarding Integrators](eb644108-94fc-430f-ae5a-e3294b9dd9be) is updated as follows:

- Updated fields
    - `Onboarding Integrators`
        - New value: Delete the Integrator.
- Responsible Party: Operational GovOps
- Triggers: None

###### A.2.2.9.2.2.3.6.4.1.2 - Current Integrators Active Data Update [Core]  <!-- UUID: 1b03bc85-a7f4-4cc5-be41-d13a16b8c379 -->

[A.2.2.9.1.2.1.4.1.0.6.1 - List Of Current Integrators](efbe7903-a76e-40f0-a440-56e463283157) is updated as follows:

- Updated fields
    - `Current Integrators`
        - New value: set to the name of the Integrator from the approved Proposal
    - `Reward Code`
        - New value: set to the Reward Code from the approved Proposal
    - `Tracking Methodology`
        - New value: set to the tracking methodology from the approved Proposal
- Responsible Party: Operational GovOps
- Triggers: None

###### A.2.2.9.2.2.3.6.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 1ba7ea74-00a7-4e45-9fd4-d5222e40746b -->

The Agent Artifact documents specified herein are updated as the output of this process.

###### A.2.2.9.2.2.3.6.4.2.1 - Primitive Hub Document Update [Core]  <!-- UUID: f4323202-b7ef-437b-9667-226dea4f9dce -->

The Document in the Agent Artifact is updated as follows:

- Required Primitive Input Trigger: Proposal passes
- Updated fields
    - Active Instances/Instance Name/Instance Status
        - New value: `Active`
    - Instance Location: [links to `Instance Configuration Document` subtree]
- Responsible Party: Operational Facilitator
- Trigger-Process: None.

###### A.2.2.9.2.2.4 - Instance Ongoing Management Protocol [Core]  <!-- UUID: 805381e5-89e7-4fb9-bda7-a97e84b531ba -->

The documents herein define the process for the ongoing management of an Instance of the Integration Boost Primitive.

###### A.2.2.9.2.2.4.1 - Routine Protocol [Core]  <!-- UUID: 04864587-25ef-4179-b237-4dd0a23485a4 -->

The documents herein define the routine process for ongoing management of an Instance of the Integration Boost Primitive.

###### A.2.2.9.2.2.4.1.1 - Process Definition For Integration Boost Calculation By Operational GovOps [Core]  <!-- UUID: 780719e8-ea6d-4ae1-b519-34d03be483df -->

The documents herein define the process for Integration Boost Calculation by Operational GovOps.

###### A.2.2.9.2.2.4.1.1.1 - Process Initiation Logic [Core]  <!-- UUID: 0930f2b1-38ae-415e-85e6-bf96c7bcb0cb -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.4.1.1.1.1 - Triggers [Core]  <!-- UUID: 52fc6ecc-d3c2-4c6e-babe-2a3bb0e10f22 -->

Triggers are specified herein.

###### A.2.2.9.2.2.4.1.1.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 56e6b01b-5f00-4385-9876-951f3160cb70 -->

This process is triggered at the end of each occurrence of the Cadence for each Instance of the Integration Boost Primitive with an Instance Status of `Active`.

###### A.2.2.9.2.2.4.1.1.1.1.2 - Document Update Triggers [Core]  <!-- UUID: fa1e98b5-18f4-4e9a-b008-50fb2906e35a -->

None.

###### A.2.2.9.2.2.4.1.1.1.2 - Dependencies [Core]  <!-- UUID: f8991663-df3f-49ea-9c96-d7c0f09d8ee8 -->

This process has no dependencies.

###### A.2.2.9.2.2.4.1.1.2 - Process Flow [Core]  <!-- UUID: fa744d67-6609-4b94-9126-dade273d3d4d -->

The process flow is defined herein:

- At the end of each Integration Boost period, the data provider submits the net USDS deposit data to Powerhouse.
- Operational GovOps verifies this data by checking on-chain balances and confirms that there are no discrepancies.
- Operational GovOps then calculates the payout based on the net USDS deposit data and the Sky Savings Rate.

###### A.2.2.9.2.2.4.1.1.3 - Required Primitive Inputs [Core]  <!-- UUID: 4c84f0a6-0d4d-4718-a7c4-04fa29fadfcc -->

The required Primitive Inputs to this process are specified herein.

- Edit `Integration Boost Payments` Document (Active Data)
    - Updated fields
        - Status
            - New value: set to `In Progress`
        - Underlying data
            - New value: populate with underlying data used to calculate the net deposits
        - Net deposits
            - New value: populate with calculated value
        - Integration Boost payment due
            - New value: populate with calculated value.
    - Responsible party: Operational GovOps.
    - Trigger-Process: [A.2.2.9.2.2.4.1.2 - Process Definition For Integration Boost Payment Issuance From Operational Executor Agent Buffer](16474cb5-8af4-4f11-b0c1-2c00f292cc2b).

###### A.2.2.9.2.2.4.1.1.4 - Required Outputs [Core]  <!-- UUID: 08dd7788-9265-46f3-bc91-3215218bc69f -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.4.1.1.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 273db3f1-9da3-4ef9-a5a0-31d537a62bbd -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.2.2.4.1.1.4.2 - Agent Artifact Updates [Core]  <!-- UUID: b785cb0c-1ebb-438d-a5c4-c385e7446977 -->

No Agent Artifact documents are updated as the output of this process. The requirements specified [A.2.2.9.2.2.4.1.1.3 - Required Primitive Inputs](4c84f0a6-0d4d-4718-a7c4-04fa29fadfcc) fully complete the Process.

###### A.2.2.9.2.2.4.1.2 - Process Definition For Integration Boost Payment Issuance From Operational Executor Agent Buffer [Core]  <!-- UUID: 16474cb5-8af4-4f11-b0c1-2c00f292cc2b -->

The documents herein define the process for Integration Boost payment from the Operational Executor Agent Buffer.

###### A.2.2.9.2.2.4.1.2.1 - Process Initiation Logic [Core]  <!-- UUID: c12533a4-9e4c-4618-a02b-cd33178db95b -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.4.1.2.1.1 - Triggers [Core]  <!-- UUID: fd914a13-4bc6-4bfe-a809-a440d1acd1fa -->

Triggers are specified herein.

###### A.2.2.9.2.2.4.1.2.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 9c5455f3-5f3b-484d-a253-62e417d7779c -->

None.

###### A.2.2.9.2.2.4.1.2.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 358d4696-47d3-41a2-a34c-33e47487d3bb -->

This process is triggered by the Required Primitive Inputs specified in Edit Integration Boost Payments Document (Active Data).

###### A.2.2.9.2.2.4.1.2.1.2 - Dependencies [Core]  <!-- UUID: 5cae5183-8c36-4d19-8db6-d6145b282fe6 -->

This process has no dependencies.

###### A.2.2.9.2.2.4.1.2.2 - Process Flow [Core]  <!-- UUID: f894a7d2-8ef7-4130-8955-5a939f6eb535 -->

The process flow is defined herein.

- Operational GovOps makes the payment to the reward address specified in the Primitive Instance from the Operational Executor Agent Buffer.
- Operational GovOps updates the Powerhouse system with the transaction details.

###### A.2.2.9.2.2.4.1.2.3 - Required Primitive Inputs [Core]  <!-- UUID: 862aff47-67fc-4b7f-bc16-b45b7edd9e83 -->

The required Primitive Inputs to this process are specified herein.

- Edit `Integration Boost Payments` Document (Active Data)
    - Updated fields
        - Status
            - New value: set to `Paid`
        - Transaction Details/Amount Paid
            - New value: populate with amount paid
        - Transaction Details/Tx hash
            - New value: populate with transaction hash
    - Responsible Party: Operational GovOps
    - Trigger - Process: [A.2.2.9.2.2.4.1.3 - Process Definition For Settlement Cycle And Core GovOps Review](d9c13a1a-aa81-483a-bc72-453d27980717).

###### A.2.2.9.2.2.4.1.2.4 - Required Outputs [Core]  <!-- UUID: baa296a6-7b9c-4134-b6a2-648d8a24a9bc -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.4.1.2.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 7e7e516a-64d4-48fa-b138-11924474b48d -->

No Sky Core Atlas documents are updated as the output of this process.

###### A.2.2.9.2.2.4.1.2.4.2 - Agent Artifact Updates [Core]  <!-- UUID: f1e0fb16-7f7d-4b91-8a21-e87e21a92979 -->

No Agent Artifact documents are updated as the output of this process. The requirements specified in [A.2.2.9.2.2.4.1.2.3 - Required Primitive Inputs](862aff47-67fc-4b7f-bc16-b45b7edd9e83) fully complete the process.

###### A.2.2.9.2.2.4.1.3 - Process Definition For Settlement Cycle And Core GovOps Review [Core]  <!-- UUID: d9c13a1a-aa81-483a-bc72-453d27980717 -->

The documents herein define the process for the Integration Boost Settlement Cycle and Core GovOps review as part of ongoing management of an Instance of the Integration Boost Primitive.

###### A.2.2.9.2.2.4.1.3.1 - Process Initiation Logic [Core]  <!-- UUID: 0f8e3d69-eeb9-4ab7-9976-ad7fd93b9fb0 -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.4.1.3.1.1 - Triggers [Core]  <!-- UUID: 7ba12eff-207b-4060-9a3e-8db1908cf982 -->

Triggers are specified herein.

###### A.2.2.9.2.2.4.1.3.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: 44fb9520-c7e6-4a6a-8362-6c3a7b9fa765 -->

This process is triggered at the beginning of every calendar quarter.

###### A.2.2.9.2.2.4.1.3.1.1.2 - Document Update Triggers [Core]  <!-- UUID: 30152570-8af2-4e2a-bab2-9dbb871a00f4 -->

None.

###### A.2.2.9.2.2.4.1.3.1.2 - Dependencies [Core]  <!-- UUID: 8f3b3d8b-57cb-4ecf-a264-7818cd01d9b2 -->

This process has no dependencies.

###### A.2.2.9.2.2.4.1.3.2 - Process Flow [Core]  <!-- UUID: 841497f9-b592-4365-8221-3bdbb82b8d4a -->

The process flow is defined herein.

- Core GovOps reviews Integration Boost calculations, including underlying data and calculation of balances and rewards due.
- Once Core GovOps has completed review, they update Powerhouse system to indicate that they confirm the accuracy of the Integration Boost amounts.

###### A.2.2.9.2.2.4.1.3.3 - Required Primitive Inputs [Core]  <!-- UUID: ebbfa305-4d56-45f4-8d06-180dc02cbb2f -->

The required Primitive Inputs to this process are specified herein.

- Edit `Integration Boost Payments` Active Data Document
    - Updated field
        - Core GovOps Review/Confirmation
            - New value: populate with yes or no.
        - Core GovOps Review/Commentary
            - New value: populate with reasoning (required if confirmation value is `No`)
    - Responsible party: Core GovOps

###### A.2.2.9.2.2.4.1.3.4 - Required Outputs [Core]  <!-- UUID: 5a0f038c-c710-4889-882a-a0cb040577a3 -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.4.1.3.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 1f50ce0e-76f8-4436-820f-363bcf8fc017 -->

The Sky Core Atlas documents specified herein are updated as the output of this process.

###### A.2.2.9.2.2.4.1.3.4.1.1 - Sky Core Integration Boost Reimbursement Active Data Document Update [Core]  <!-- UUID: 0f50e796-9486-42cd-a98d-b284f8340307 -->

The document in the Sky Core Atlas is updated as follows:

- Updated Fields
    - Status
        - New value: populate with `Pending Payment`
    - Confirmed Reimbursement Due
        - New value: populate with total Reimbursement amount
    - Reward Period
        - New Value: populate with reward period
    - Operational Executor Agent
        - New value: Populate with name of Operational Executor Agent
    - Prime Agent
        - New value: Populate with name of Prime Agent.
- Responsible Party: Core GovOps
- Triggers: [A.2.2.9.2.2.4.1.4 - Process Definition For Executive Vote Reimbursement](c40a0708-12e4-46da-89d7-0e5a3a839455).

###### A.2.2.9.2.2.4.1.3.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 43aedc35-e90a-48ca-a0fc-346ced2bea0b -->

No Agent Artifact documents are updated as the output of this process.

###### A.2.2.9.2.2.4.1.4 - Process Definition For Executive Vote Reimbursement [Core]  <!-- UUID: c40a0708-12e4-46da-89d7-0e5a3a839455 -->

The documents herein define the process for Integration Boost Executive Vote reimbursement as part of ongoing management of an Instance of the Integration Boost Primitive.

###### A.2.2.9.2.2.4.1.4.1 - Process Initiation Logic [Core]  <!-- UUID: 6dac32e6-593c-44db-908b-9075c8dd68ca -->

The process initiation logic is specified herein.

###### A.2.2.9.2.2.4.1.4.1.1 - Triggers [Core]  <!-- UUID: dea4f41d-b36b-421f-be80-3f495532ab7a -->

Triggers are specified herein.

###### A.2.2.9.2.2.4.1.4.1.1.1 - Time-Based Triggers [Core]  <!-- UUID: fa1aab6f-61a8-493f-b282-6a0e3f64ce29 -->

None.

###### A.2.2.9.2.2.4.1.4.1.1.2 - Document Update Triggers [Core]  <!-- UUID: ee6adeb0-b3e5-4d0f-8d1a-b9fdc1510074 -->

This process is triggered by the Document Update specified in [A.2.2.9.2.2.4.1.3.4.1.1 - Sky Core Integration Boost Reimbursement Active Data Document Update](0f50e796-9486-42cd-a98d-b284f8340307).

###### A.2.2.9.2.2.4.1.4.1.2 - Dependencies [Core]  <!-- UUID: 10cb9c97-e21b-4ad2-af48-eb2fa577aded -->

This process has no dependencies.

###### A.2.2.9.2.2.4.1.4.2 - Process Flow [Core]  <!-- UUID: 9cb825c8-871f-47b7-9918-e48fe2a34d26 -->

The process flow is defined herein:

- Core GovOps includes the Integration Boost reimbursement in the next standard Executive Vote.
- After the Executive Vote passes, Core GovOps updates the Powerhouse system with the transaction details.

###### A.2.2.9.2.2.4.1.4.3 - Required Primitive Inputs [Core]  <!-- UUID: f54de74a-4208-4878-8049-3184ab3f9a0d -->

The required Primitive Inputs to this process are specified herein and organized as sequential stages.

- Core GovOps adds reimbursement to Executive Vote
    - Edit `Sky Core Integration Boost Reimbursement Amounts`
        - Updated fields
            - Executive Vote Settlement/Executive Vote
                - New value: links to proposal
            - Status
                - New value: set to `Added to Executive Vote`
- After Executive Vote passes, Core GovOps updates Powerhouse system
    - Edit `Sky Core Integration Boost Reimbursement Amounts`
        - Updated fields
            - Executive Vote Settlement / Transaction Details/ Amount Paid
                - New value: populate with amount paid to reimburse Operational Executor Agent Buffer.
            - Executive Vote Settlement / Transaction Details / Tx Hash
                - New value: Populate with transaction hash
            - Status
                - New value: set to `Completed`

###### A.2.2.9.2.2.4.1.4.4 - Required Outputs [Core]  <!-- UUID: 8d00d8df-f970-4b2e-8da9-3b9fe2af9e2b -->

The documents herein specify the required outputs from this process.

###### A.2.2.9.2.2.4.1.4.4.1 - Sky Core Atlas Updates [Core]  <!-- UUID: 9478c3d6-ce1d-4c73-a479-9127b5c245e1 -->

The Sky Core Atlas documents specified herein are updated as the output of this process.

###### A.2.2.9.2.2.4.1.4.4.1.1 - Sky Core Integration Boost Reimbursement Active Data Document Update [Core]  <!-- UUID: 0ab76a83-ca8d-4ebf-83c1-b7e7dced0970 -->

The Document in the Sky Core Atlas is updated as follows:

- Updated fields
    - Status
        - New value: set to `Paid`
    - Responsible Party: Core GovOps
    - Trigger-Process: None

###### A.2.2.9.2.2.4.1.4.4.2 - Agent Artifact Updates [Core]  <!-- UUID: 39aba7ed-95ff-4247-acb7-61032649b218 -->

No Agent Artifact documents are updated as the output of this process.

###### A.2.2.9.2.2.4.2 - Non-Routine Protocol [Core]  <!-- UUID: 9cdac621-4677-4c79-8372-68e0a778c27d -->

The documents herein define processes for handling non-routine situations in the ongoing management of an Instance of the Integration Boost Primitive.

###### A.2.2.9.2.2.4.3 - Emergency Protocol [Core]  <!-- UUID: 0bbeab5f-ca17-463a-a9a4-9ab588347a0c -->

The documents herein define processes for handling emergency situations in the ongoing management of an Instance of the Integration Boost Primitive.

#### A.2.2.9.3 - Pioneer Chain Primitive [Core]  <!-- UUID: 4c7be4c6-44b5-407a-94ae-3d7ca7e8039c -->

The documents herein govern the Pioneer Chain Primitive.

##### A.2.2.9.3.1 - Introduction [Core]  <!-- UUID: 4aab68fd-0e8c-4781-b6f6-f94a89cb22fa -->

The documents herein provide an introduction to the Pioneer Chain Primitive.

###### A.2.2.9.3.1.1 - Pioneer Prime Requirements [Core]  <!-- UUID: 219459b3-8333-4e9a-9b79-55e0c20d6dbb -->

Pioneer Primes must be designated by the official team or foundation of the Pioneer Chain. It is only possible for a Pioneer Chain to have a Pioneer Prime once, and for a Pioneer Prime to have the Pioneer Prime status with a single blockchain, once.

###### A.2.2.9.3.1.2 - Pioneer Prime Designation Process [Core]  <!-- UUID: d6d16076-da22-43f1-a303-627af41b486c -->

In order to be confirmed as a Pioneer Prime, a Prime Agent must provide written proof to Operational GovOps that it has been provisionally designated as such by the official team or foundation of the relevant Pioneer Chain. Following a check by Operational GovOps to ensure that the Prime Agent has not been a Pioneer Prime previously and that the Pioneer Chain has not had a Pioneer Prime before, Operational GovOps will add the new Pioneer Prime to the list of Active Pioneer Primes. See [A.2.2.9.3.1.2.1.0.6.1 - List of Active Pioneer Primes](f2ecf6a4-4d5f-4443-b25c-3bd10b1af82e).

###### A.2.2.9.3.1.2.1 - Active Pioneer Primes [Active Data Controller]  <!-- UUID: 65fc0b79-8827-403d-80ee-9f74a6be1069 -->

Active Pioneer Primes are Prime Agents who have been designated by the official team or foundation of the Pioneer Chain and confirmed as Pioneer Primes by Operational GovOps. The list of Current Pioneer Primes is defined as Active Data in [A.2.2.9.3.1.2.1.0.6.1 - List of Active Pioneer Primes](f2ecf6a4-4d5f-4443-b25c-3bd10b1af82e).

The Active Data is updated as follows:

- The Responsible Party is Operational GovOps.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.2.9.3.1.2.1.0.6.1 - List of Active Pioneer Primes [Active Data]  <!-- UUID: f2ecf6a4-4d5f-4443-b25c-3bd10b1af82e -->

The current Active Pioneer Primes are:

- Keel
- Grove
- Osero

###### A.2.2.9.3.1.3 - Pioneer Prime Benefits [Core]  <!-- UUID: f0d5ab5e-bf35-4a9d-a73f-d82baac6e604 -->

Pioneer Primes gain benefits and responsibilities related to the general adoption of USDS on the Pioneer Chain, and this benefit comes in two forms.

First, during the Pioneer Phase, the Pioneer Prime counts as having tagged, for the purposes of calculating the Distribution Reward, all USDS and sUSDS accounts and balances on the Pioneer Chain that have not been tagged by another Prime. At the end of the Pioneer Phase, all untagged USDS accounts and balances are one-time tagged by the Pioneer Prime, and this tag will remain normally for the following ten (10) years unless tagged by a different Prime, or retagged.

Second, during the Pioneer Phase, all Unrewarded USDS bridged to the Pioneer Chain counts towards Pioneer Incentive payments, see [A.2.2.9.3.1.4 - Pioneer Incentive Pool](04edac33-19d5-4a87-a8ab-945a0cd57771).

###### A.2.2.9.3.1.3.1 - Pioneer Phase [Core]  <!-- UUID: 0c7b0644-68d4-441d-8221-88382a6515e4 -->

For purposes of [A.2.2.9.3.1.3 - Pioneer Prime Benefits](f0d5ab5e-bf35-4a9d-a73f-d82baac6e604), the Pioneer Phase is a period beginning on the date that a Prime Agent satisfies the Pioneer Prime Requirements specified in [A.2.2.9.3.1.1 - Pioneer Prime Requirements](219459b3-8333-4e9a-9b79-55e0c20d6dbb) and ending three (3) years thereafter.

###### A.2.2.9.3.1.4 - Pioneer Incentive Pool [Core]  <!-- UUID: 04edac33-19d5-4a87-a8ab-945a0cd57771 -->

All Pioneer Incentive payments are paid through the Monthly Settlement Cycle. Each Monthly Settlement Cycle, an amount of funds equivalent to the Sky Savings Rate multiplied by the balance of Unrewarded USDS is paid into a separate account controlled by the Pioneer Prime (the "Pioneer Incentive Pool"). The Pioneer Prime retains one hundred percent (100%) of the funds in the Pioneer Incentive Pool.

###### A.2.2.9.3.1.4.1 - Pre-Pioneer Incentive Pool [Core]  <!-- UUID: 15e14f25-8d56-4699-ac37-0cef4f0503c5 -->

A Pre-Pioneer Incentive Pool is a temporary, chain-specific incentive mechanism designed to bootstrap USDS adoption on a new blockchain before a formal Pioneer Prime is established for that chain. It allows a designated Agent to direct incentive payments to ecosystem partners on that specific chain. The Pre-Pioneer Incentive Pool may operate under distinct rules that differ from the standard Pioneer Incentive Pool, which rules will be specified in an Ecosystem Accord between the respective Agent and Sky Core. A Pre-Pioneer Incentive Pool serves as a transitional phase until the conditions for a formal Pioneer Incentive Pool are met. See [A.2.2.9.3.1.4 - Pioneer Incentive Pool](04edac33-19d5-4a87-a8ab-945a0cd57771).

### A.2.2.10 - Supply Side Stablecoin Primitives [Section]  <!-- UUID: d1142876-33c2-4e21-9339-d8711525d46f -->

Supply Side Stablecoin Primitives are Sky Primitives focused on capital allocation and risk management.

#### A.2.2.10.1 - Allocation System Primitive [Core]  <!-- UUID: 9db14ab7-bb4b-4751-8084-843bd4359f2a -->

The Allocation System Primitive is the base mechanism that enables Prime Agents to put up Risk Capital to deploy USDS collateral into different opportunities that provide risk-adjusted return, by borrowing at the Base Rate from Sky, and following Asset Liability Management restrictions on the liquidity of deployed assets.

##### A.2.2.10.1.1 - Allocation System Process Definition [Core]  <!-- UUID: 823a12c3-45d2-438a-b061-46ecd09cdca8 -->

The documents herein define the process for initial setup and ongoing management of an Allocation Instance (alternatively referred to as "conduits") as part of the Allocation System Primitive.

###### A.2.2.10.1.1.1 - Base Elements [Core]  <!-- UUID: 39f3ceee-2e0b-41b2-ad62-85cac3895cb0 -->

The documents herein define base elements of the Allocation System Primitive.

###### A.2.2.10.1.1.1.1 - Sky Direct Exposures [Core]  <!-- UUID: b3fb8653-8503-4a9e-81b2-5e9f49ad6703 -->

Sky Direct Exposures are exposures that are held directly by Sky but implemented through the Allocation System of a Prime Agent. The documents herein define the rules for Sky Direct Exposures.

###### A.2.2.10.1.1.1.1.1 - Designation Process [Core]  <!-- UUID: 3161489a-11bd-4dea-b676-09d0cce45ae9 -->

Sky Direct Exposures are designated by the Core Facilitator in consultation with the Core Council Risk Advisor via posts to the Sky Forum under the "Sky Core" category. Sky Direct Exposures are recorded in [A.2.2.10.1.1.1.1.2.0.6.1 - List Of Current Sky Direct Exposures](5f368e33-7a82-4244-a9ba-f285193ec043) and must specify the asset that is being designated as a Sky Direct Exposure and the Prime Agent responsible for implementing the exposure.

###### A.2.2.10.1.1.1.1.2 - Current Sky Direct Exposures [Active Data Controller]  <!-- UUID: 1c0410e4-fe36-4a01-8b82-8ea74f67fbec -->

The list of current Sky Direct Exposures is defined as Active Data in [A.2.2.10.1.1.1.1.2.0.6.1 - List Of Current Sky Direct Exposures](5f368e33-7a82-4244-a9ba-f285193ec043).

The Active Data is updated as follows:

- The Responsible Party is the Core Facilitator.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.2.10.1.1.1.1.2.0.6.1 - List Of Current Sky Direct Exposures [Active Data]  <!-- UUID: 5f368e33-7a82-4244-a9ba-f285193ec043 -->

| Sky Direct Exposure | Description | Designated |
|---|---|---|
| Treasury Bills | Investments by Grove in BUIDL, JTRSY, and USTB on Ethereum Mainnet | 2025-10-30 |
| Peg Stability Modules | Investments by Spark or Grove in USDC in Peg Stability Modules on blockchains other than Ethereum Mainnet | 2025-11-13 |
| Uniswap Pools | Investments by Spark in USDT in USDS/USDT Uniswap pools | 2026-05-26 |

###### A.2.2.10.1.1.1.1.3 - Previous Sky Direct Exposures [Active Data Controller]  <!-- UUID: 3a495464-c4d7-46e7-82a3-2c321b27ee12 -->

The list of previous Sky Direct Exposures is defined as Active Data in [A.2.2.10.1.1.1.1.3.0.6.1 - List Of Previous Sky Direct Exposures](86fce840-f7f3-4617-bb58-d04db8731c9d).

The Active Data is updated as follows:

- The Responsible Party is the Core Facilitator.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.2.10.1.1.1.1.3.0.6.1 - List Of Previous Sky Direct Exposures [Active Data]  <!-- UUID: 86fce840-f7f3-4617-bb58-d04db8731c9d -->

| Sky Direct Exposure | Description | Designated | Ended |
|---|---|---|---|
| Curve Pools | Investments by Spark in USDT in sUSDS/USDT Curve pools | 2025-11-13 | 2026-06-25 |

###### A.2.2.10.1.1.1.1.4 - Parameters For Sky Direct Exposures [Core]  <!-- UUID: cbd64e6c-547b-4b8d-a0cb-b605f780aef1 -->

The Core Facilitator sets the following parameters for Sky Direct Exposures in consultation with the Core Council Risk Advisor:

- Rate limits; and
- Aggregate exposure limits.

The Core Facilitator must post the initial values for these parameters and any updates to them to the Sky Forum under the "Sky Core" category. The values for the parameters for Sky Direct Exposures are set by the Core Facilitator and supersede any values for these parameters specified in the Risk Framework.

###### A.2.2.10.1.1.1.1.4.1 - Treatment Of Exposures In Excess Of Aggregate Exposure Limit [Core]  <!-- UUID: 8bd63c6b-b9ad-46e3-beb0-77c4a47bcd6d -->

Any investments in assets that would otherwise qualify as Sky Direct Exposures by a Prime Agent in excess of the aggregate exposure limit are not Sky Direct Exposures and are subject to the customary requirements pursuant to [A.2.4 - Sky Core Monthly Settlement Cycle](6f8d5065-d6ff-4add-9a28-eadeffa7ed1a) and [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.2.2.10.1.1.1.1.5 - Revenue Sharing For Sky Direct Exposures [Core]  <!-- UUID: 07e0f716-ce23-4394-a5f4-bee537713f48 -->

Because Sky Direct Exposures are held by Sky rather than the Prime Agent implementing the exposure through its Allocation System, Prime Agents are not required to pay the Agent Credit Line Borrow Rate with respect to funds borrowed to finance Sky Direct Exposures. All yield on Sky Direct Exposures is also due exclusively to Sky and is not retained by the Prime Agent. This is implemented as an adjustment to the Monthly Settlement Cycle.

###### A.2.2.10.1.1.1.1.6 - No Risk Capital Requirements With Respect To Sky Direct Exposures [Core]  <!-- UUID: b683953e-d9b0-4e15-a405-978ef1854870 -->

Because Sky Direct Exposures are held by Sky rather than the Prime Agent implementing the exposure through its Allocation System, Prime Agents are not required to hold any Risk Capital with respect to Sky Direct Exposures.

###### A.2.2.10.1.1.1.1.7 - No Actively Stabilizing Collateral Requirements With Respect To Sky Direct Exposures [Core]  <!-- UUID: bfb8013f-9226-4426-84bf-4b0e03b44107 -->

Because Sky Direct Exposures are held by Sky rather than the Prime Agent implementing the exposure through its Allocation System, Prime Agents are not required to hold any Actively Stabilizing Collateral with respect to Sky Direct Exposures. Sky Direct Exposures also do not count towards satisfying a Prime Agent’s Actively Stabilizing Collateral requirements.

###### A.2.2.10.1.1.1.2 - Diamond PAU [Core]  <!-- UUID: d5cfb5ed-20a9-42a0-9838-ef21e1115648 -->

The documents herein define the shared parameters, roles, contracts, and operational processes of the Diamond PAU (Parallelized Allocation Unit), the facet-based Allocation System Primitive controller architecture.

###### A.2.2.10.1.1.1.2.1 - Liquidity Layer Parameter Definitions [Core]  <!-- UUID: a8a3e54d-980e-435d-9e08-0e5775af9aa3 -->

The documents herein define common parameters of implementations of the Allocation System.

###### A.2.2.10.1.1.1.2.1.1 - Rate Limiter [Core]  <!-- UUID: a578830d-18f0-451c-8ff0-4a66094650ae -->

Rate Limiter refers to the overall mechanism or system that limits the volume of token movements over time, implemented via the `RateLimits` contracts. The Rate Limiter manages multiple rate limits and enforces constraints on controller operations to prevent rapid asset drainage and mitigate risks from compromised relayers or other attacks. This ensures that the maximum amount of tokens processed within a specific time period stays within safe bounds. The `RateLimits` contracts and their addresses for each chain can be found in the Allocation System Primitive for a Prime, under ALM Contracts.

###### A.2.2.10.1.1.1.2.1.2 - Rate Limits [Core]  <!-- UUID: 8efb0a11-b798-48eb-af19-f65b38f039b5 -->

Rate limits set the maximum allowable amount of tokens that can be processed for specific operations within a given time period. Each rate limit contains the rate limit data: `maxAmount`, `slope`, `lastAmount` and `lastUpdated`. The current rate limit is calculated using the formula:

`currentRateLimit = min(slope * (block.timestamp - lastUpdated) + lastAmount, maxAmount)`.

The rate limit data `maxAmount` and `slope` are configurable parameters that are set and modified by Governance. The rate limit data `lastAmount` and `lastUpdated` are internal state data dynamically tracked by the Rate Limiter to perform its calculations.

Rate limits set caps on the rate of allocation to a given Instance, they do not act as a limit on the total amount that may be allocated to that Instance.

###### A.2.2.10.1.1.1.2.1.2.1 - MaxAmount [Core]  <!-- UUID: 8b5f1ffd-9dfd-4aa0-8fc2-638a79d9fadb -->

`maxAmount` sets a hard cap on the level of allocation to an Instance at any given time. It sets the absolute rate limit regardless of how much time has passed since the last allocation. For example, if `maxAmount` is set to 1,000,000 tokens, the rate limit will increase over time at the rate determined by the `slope` until it reaches 1,000,000 tokens. At this point the rate limit will stop increasing, but it will resume increasing once an allocation to the Instance has been made.

###### A.2.2.10.1.1.1.2.1.2.2 - Slope [Core]  <!-- UUID: ae8674bc-44ac-4b95-b5df-c6322a1d6e9a -->

`slope` is the linear refill rate of a rate limiter’s allowance over time. It defines how quickly the capacity to perform additional inflow or outflow accrues after prior consumption. For example, if the slope is set to 1,000,000 tokens per day (converted to per second for on-chain execution), the rate limit will recover at that rate until it reaches the maxAmount.

###### A.2.2.10.1.1.1.2.1.2.3 - LastUpdated [Core]  <!-- UUID: 8d0419a4-50c5-4a7b-b68e-84d8c9243694 -->

`lastUpdated` is the timestamp when the rate limit was last updated, serving as the reference point for calculating time-elapsed refills in the formula.

###### A.2.2.10.1.1.1.2.1.2.4 - LastAmount [Core]  <!-- UUID: 02918cfc-5d10-41bc-bb8a-0be9df76cbac -->

`lastAmount` is the remaining allowance available at the last update, used to compute the current rate limit by adding accrued capacity.

###### A.2.2.10.1.1.1.2.1.3 - Inflow Rate Limits [Core]  <!-- UUID: d59a233c-11b9-4140-b15f-51df37475fd8 -->

Inflow rate limits constrain the rate at which allocated liquidity can increase into a scope. "Inflow" means movements that raise exposure or capital allocated to an Instance or market, such as depositing, minting, or rebalancing into a position.

###### A.2.2.10.1.1.1.2.1.4 - Outflow Rate Limits [Core]  <!-- UUID: e50fd86a-ffa4-4387-b212-420730a8d171 -->

Outflow Rate Limits constrain the rate at which allocated liquidity can be withdrawn or exposure reduced from a scope. "Outflow" means movements that lower exposure or capital allocated to an Instance or market, such as withdrawals, redemptions, or unwind operations.

Outflow limits are often configured more permissively to prioritize safety and fast exits. When outflow limits are "unlimited," the rate limits contract simply does not apply a cap in that direction.

###### A.2.2.10.1.1.1.2.1.5 - Rate Limit IDs [Core]  <!-- UUID: b95b3bd8-d316-43d5-af56-df38d557aea3 -->

A `Rate Limit ID` is a bytes32 key that uniquely identifies a rate limit. Rate Limit IDs allow the system to maintain independent allowance state for each relevant transaction.

###### A.2.2.10.1.1.1.2.1.6 - MaxSlippage [Core]  <!-- UUID: 7c6da187-7d17-42ae-8c64-8d828ee83ea7 -->

`maxSlippage` is a configurable parameter that sets the maximum allowed price impact or deviation from expected output when executing trades or liquidity operations in a pool. `maxslippage` is expressed as a decimal and must be a non-zero value. This protects against excessive price impact during volatile market conditions.

###### A.2.2.10.1.1.1.2.1.7 - Maximum Exposure Tolerance [Core]  <!-- UUID: a1b58d9d-7529-463e-af49-cbe9d07b7435 -->

Where the Atlas specifies a maximum exposure, actual exposure may exceed that maximum by up to 5%, provided the excess is solely attributable to accrued interest and not to new principal. A Prime Agent is responsible for claiming and returning accrued interest as necessary to keep exposure within the specified maximum.

###### A.2.2.10.1.1.1.2.2 - Liquidity Layer Role Definitions [Core]  <!-- UUID: 2ae4b91a-6900-41e8-9718-32805b956550 -->

The documents herein define the access-control roles of the Diamond Parallelized Allocation Unit (Diamond PAU) implementation of the Allocation System.

###### A.2.2.10.1.1.1.2.2.1 - Default Admin Role [Core]  <!-- UUID: b76195f2-7494-43a4-919e-fa823303ad06 -->

The Default Admin Role (`DEFAULT_ADMIN_ROLE`) is the administrative role of an Instance's access-control contract, authorized to grant and revoke all other roles. It is held by Sky Governance through the Prime Agent's SubProxy. This per-Instance role is distinct from the Beacon's own `DEFAULT_ADMIN_ROLE`, which is held by the Pause Proxy.

###### A.2.2.10.1.1.1.2.2.2 - Controller Role [Core]  <!-- UUID: 4f77eb6c-4b2f-4fa0-a7c0-d58e9b76ce8e -->

The Controller Role (`CONTROLLER`) is authorized to call the asset-movement functions on the ALM Proxy and to update the Rate Limits contract. It is held by the Controller contract, which dispatches operations to the relevant Facet on behalf of the Allocator Role.

###### A.2.2.10.1.1.1.2.2.3 - Allocator Role [Core]  <!-- UUID: e7a97395-ddd5-4ae8-874f-1bb3f247446a -->

The Allocator Role (`ALLOCATOR_ROLE`) is authorized to initiate allocation operations on behalf of the ALM Proxy, through the Controller. It is held by the AdministeredAgent contract, with the Relayer Multisigs registered as its Actors, as specified in [A.2.2.10.1.1.1.2.2.4 - Actor](636a39e4-5908-4fee-bae8-e0b11e0d9c55), and submitting operations through it.

###### A.2.2.10.1.1.1.2.2.4 - Actor [Core]  <!-- UUID: 636a39e4-5908-4fee-bae8-e0b11e0d9c55 -->

An Actor is an address registered on the AdministeredAgent that is authorized to submit allocation operations to the Controller through the Allocator Role, as specified in [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a). The Relayer Multisigs of a Prime Agent and of the Core Operator are registered as Actors.

###### A.2.2.10.1.1.1.2.2.5 - Revoker [Core]  <!-- UUID: cc7cb4b7-981e-44f5-a0d5-62e5b47d112e -->

A Revoker is an address registered on the AdministeredAgent that is authorized to remove an Actor as a rapid-response measure, without affecting the Allocator Role held by the AdministeredAgent. The Freezer Multisig of a Prime Agent is registered as a Revoker, providing the emergency capability to remove a compromised or malicious Actor outside the standard governance process.

###### A.2.2.10.1.1.1.2.2.6 - Grantor [Core]  <!-- UUID: 82a04ab9-158e-4c6e-9f2a-04ef68c3a2f0 -->

A Grantor is an address registered on the AdministeredAgent that is authorized to add an Actor, as specified in [A.2.2.10.1.1.1.2.2.4 - Actor](636a39e4-5908-4fee-bae8-e0b11e0d9c55), granting it the ability to submit operations through the AdministeredAgent.

###### A.2.2.10.1.1.1.2.2.7 - Administered Agent Admin [Core]  <!-- UUID: d823b872-fe99-4856-9096-55335357d55e -->

The Administered Agent Admin is an address registered on the AdministeredAgent with authority over its role configuration, able to add and remove the AdministeredAgent's Admins, Grantors, Actors, and Revokers. This role is distinct from the Default Admin Role, as specified in [A.2.2.10.1.1.1.2.2.1 - Default Admin Role](b76195f2-7494-43a4-919e-fa823303ad06), which administers the Diamond PAU access-control contract; both are held by Sky Governance through the Prime Agent's SubProxy.

###### A.2.2.10.1.1.1.2.3 - Liquidity Layer Shared Contracts [Core]  <!-- UUID: a2677d19-1f2c-4361-bedc-34cb2e7eaab5 -->

The documents herein define the shared contracts of the Diamond PAU implementation of the Allocation System. These contracts are deployed once at the Sky ecosystem level and controlled by Sky Governance, shared across Prime Agent Instances rather than redeployed per Agent. The addresses are on Ethereum Mainnet.

###### A.2.2.10.1.1.1.2.3.1 - Beacon [Core]  <!-- UUID: 5b0627e8-102b-42ea-8d9b-38463591faf9 -->

The Beacon (`Beacon`) is the registry that whitelists the Facets approved for use by Diamond PAU Instances; an Instance may only delegate calls to Facets registered on the Beacon. It is controlled by Sky Governance through the Pause Proxy. The Beacon's address on Ethereum Mainnet is `0x829dC2b7E94B1954F0764E573f2E0d45Afa28199`, and it is registered in the Chainlog under the key `PAU_BEACON`.

###### A.2.2.10.1.1.1.2.3.2 - Facets [Core]  <!-- UUID: b7c73a0c-456d-4e75-93ac-8eec185ece31 -->

The documents herein define the Facets currently approved on the Beacon for use by Diamond PAU Instances. Each Facet is a singleton contract deployed at the Sky ecosystem level and shared across all such Instances. The set of approved Facets is maintained by Sky Governance.

###### A.2.2.10.1.1.1.2.3.2.1 - Aave v3 Facet [Core]  <!-- UUID: c9ecd9c2-dd1b-426b-8e52-66a2b1892289 -->

The Aave v3 Facet (`AaveFacet`) supplies and withdraws an underlying asset to and from an Aave v3 lending pool, or an Aave v3 fork such as SparkLend, holding the aTokens in the ALM Proxy. Its address on Ethereum Mainnet is `0x8CE890A96a193ff2DD4B2eA3C682326F655f6b62`.

###### A.2.2.10.1.1.1.2.3.2.2 - Basin Facet [Core]  <!-- UUID: d9cbf883-119e-403d-8efa-125997cd8897 -->

The Basin Facet (`BasinFacet`) deposits assets into and withdraws them from a Basin in exchange for Basin shares. Its address on Ethereum Mainnet is `0xC84825BCD13AEddc372400239499380376a44A39`.

###### A.2.2.10.1.1.1.2.3.2.3 - CCTP Facet [Core]  <!-- UUID: ce25217f-c37d-4415-b0d6-adecab3c7855 -->

The CCTP Facet (`CCTPFacet`) bridges USDC cross-chain through Circle's Cross-Chain Transfer Protocol (CCTP), burning on the source domain to a preconfigured mint recipient. Its address on Ethereum Mainnet is `0xADf62692340e46EF90336f2e75ce3b37f1148873`.

###### A.2.2.10.1.1.1.2.3.2.4 - Centrifuge Facet [Core]  <!-- UUID: 0c7d3bb1-6013-4c1b-900e-5232c7c5d595 -->

The Centrifuge Facet (`CentrifugeFacet`) manages Centrifuge v3 async vault positions, cancelling and claiming pending deposit and redeem requests and initiating cross-chain share transfers. Its address on Ethereum Mainnet is `0xa0A10BA97be1412730D694B8dE1afe7eff20eC31`.

###### A.2.2.10.1.1.1.2.3.2.5 - Curve Facet [Core]  <!-- UUID: 0648b191-3f6c-4164-b26d-71666ca1a1cb -->

The Curve Facet (`CurveFacet`) swaps between assets in a Curve pool and adds or removes pool liquidity, under a max-slippage guard. Its address on Ethereum Mainnet is `0x139D81d7d6040fAeF7cF0EF5A2636Ca8a97a30d8`.

###### A.2.2.10.1.1.1.2.3.2.6 - DAI-USDS Facet [Core]  <!-- UUID: b6a37e83-d51e-4bd3-afe6-a6f95cd943fe -->

The DAI-USDS Facet (`DAIUSDSFacet`) converts between DAI and USDS at 1:1 through the DAI-USDS converter. Its address on Ethereum Mainnet is `0x3817F734CAe6AD2BDb79F9ff23091F2AD478da5F`.

###### A.2.2.10.1.1.1.2.3.2.7 - ERC-4626 Facet [Core]  <!-- UUID: 05f5d939-712b-4204-8f77-4ef5ea598dcc -->

The ERC-4626 Facet (`ERC4626Facet`) deposits, withdraws, and redeems against any ERC-4626 vault, under min-shares, min-assets, and max-exchange-rate guards. Its address on Ethereum Mainnet is `0x1dCA18608c89174181153E786778705b4A0E1a06`.

###### A.2.2.10.1.1.1.2.3.2.8 - ERC-7540 Facet [Core]  <!-- UUID: 83d0bf58-6a92-4873-ba9e-e5a23c8dca1c -->

The ERC-7540 Facet (`ERC7540Facet`) runs the asynchronous ERC-7540 vault flow, requesting and claiming deposits and redemptions. Its address on Ethereum Mainnet is `0x4f7e0E3612b0e1E156A2B6570a51d4BD709F1315`.

###### A.2.2.10.1.1.1.2.3.2.9 - Ethena Facet [Core]  <!-- UUID: b009545a-fd85-42f9-ad94-bc0acfe1f27a -->

The Ethena Facet (`EthenaFacet`) drives the Ethena USDe mint and burn and sUSDe staking lifecycle, managing the delegated signer, mint and burn approvals, and sUSDe cooldown and unstake. Its address on Ethereum Mainnet is `0xEc48D773CEef1c6b07CdA1afA2716C478b55187B`.

###### A.2.2.10.1.1.1.2.3.2.10 - Farm Facet [Core]  <!-- UUID: 22387224-d9be-4aee-b47f-07307eb17c90 -->

The Farm Facet (`FarmFacet`) stakes and withdraws a token in a Synthetix-style reward farm and claims accrued rewards. Its address on Ethereum Mainnet is `0xF24E91f5D8529436c9fB92dd94F80d4A6C25d0f0`.

###### A.2.2.10.1.1.1.2.3.2.11 - LayerZero Facet [Core]  <!-- UUID: 17b0a239-b0b0-476e-9a67-b8b6e3156507 -->

The LayerZero Facet (`LayerZeroFacet`) bridges tokens implementing the Omnichain Fungible Token (OFT) standard cross-chain via LayerZero v2 to a preconfigured recipient. Its address on Ethereum Mainnet is `0xA0c323a0acb20F259eA4ff343319D450BE6472e5`.

###### A.2.2.10.1.1.1.2.3.2.12 - Maple Facet [Core]  <!-- UUID: 2561da4c-6e42-4503-b763-4f121236b1e8 -->

The Maple Facet (`MapleFacet`) requests and cancels redemptions of Maple pool tokens. Its address on Ethereum Mainnet is `0x691b5c26aD2B74d2376f4eD87904E9D3E47bD630`.

###### A.2.2.10.1.1.1.2.3.2.13 - Merkl Facet [Core]  <!-- UUID: 8c492c88-d8f9-46c8-85f6-a42ee6f944d6 -->

The Merkl Facet (`MerklFacet`) toggles operator authorization on a Merkl distributor, delegating reward claiming to an operator. Its address on Ethereum Mainnet is `0x321138Db5E056e9d0080D4c278e10A1EdC091Eb0`.

###### A.2.2.10.1.1.1.2.3.2.14 - OTC Facet [Core]  <!-- UUID: 35060c04-e4c8-4dd1-a4fe-09bc9288534d -->

The OTC Facet (`OTCFacet`) executes over-the-counter swaps, sending an asset to an exchange and later claiming the counter-asset from a designated buffer, under recharge-rate and slippage checks. Its address on Ethereum Mainnet is `0x46b24ba00B65CB4f603447590e539b08097fb7Ac`.

###### A.2.2.10.1.1.1.2.3.2.15 - Pendle Facet [Core]  <!-- UUID: 222342b5-aa4c-4be4-8411-c947e96e8fdd -->

The Pendle Facet (`PendleFacet`) redeems Pendle principal and yield tokens (PT and YT) for their underlying token after market expiry via the Pendle router. Its address on Ethereum Mainnet is `0xcC9dD4c9B2a9c08f2692e7060F43d29A03E87348`.

###### A.2.2.10.1.1.1.2.3.2.16 - PSM Facet [Core]  <!-- UUID: afa3da61-c32a-4efd-900b-16e1c262c842 -->

The PSM Facet (`PSMFacet`) swaps between USDS and USDC by routing through DAI and the Lite PSM's no-fee path. Its address on Ethereum Mainnet is `0xE4A5dAc768a310cc2316f258901b32E499653064`.

###### A.2.2.10.1.1.1.2.3.2.17 - Spark Vault Facet [Core]  <!-- UUID: ad11b1de-41d7-4529-920b-55583445648e -->

The Spark Vault Facet (`SparkVaultFacet`) pulls assets from a Spark vault via its `take` function. Its address on Ethereum Mainnet is `0xff0d19920E207e3A17eb5A2E5bA3AFA44836362b`.

###### A.2.2.10.1.1.1.2.3.2.18 - Superstate Facet [Core]  <!-- UUID: 6f3e9682-7628-407b-adc3-9627bad3a419 -->

The Superstate Facet (`SuperstateFacet`) subscribes USDC into Superstate USTB, minting USTB. Its address on Ethereum Mainnet is `0xeE197475607E9a27cCAA4786e740d2F0d0E706A7`.

###### A.2.2.10.1.1.1.2.3.2.19 - Transfer Asset Facet [Core]  <!-- UUID: e59b91c8-05c9-47b2-a115-8a41b12de659 -->

The Transfer Asset Facet (`TransferAssetFacet`) transfers an ERC-20 asset from the ALM Proxy to a rate-limit-authorized destination address. Its address on Ethereum Mainnet is `0x4DA7608C331b8f135df5b985018933780eCd089D`.

###### A.2.2.10.1.1.1.2.3.2.20 - Uniswap v3 Facet [Core]  <!-- UUID: b808a829-2f31-42f1-ac9f-6801d3eb8437 -->

The Uniswap v3 Facet (`UniswapV3Facet`) executes Uniswap v3 exact-input swaps and adds or removes concentrated-liquidity positions, under tick-bound, time-weighted-average-price, and slippage guards. Its address on Ethereum Mainnet is `0x445D9Dc752F269Be48250f1A180CAC4c61cE4bab`.

###### A.2.2.10.1.1.1.2.3.2.21 - Uniswap v4 Facet [Core]  <!-- UUID: c58ae1da-985d-4f85-80be-396de4f8191f -->

The Uniswap v4 Facet (`UniswapV4Facet`) mints, increases, and decreases Uniswap v4 liquidity positions and executes token swaps, under tick-limit and slippage guards. Its address on Ethereum Mainnet is `0x75D35ffB8e6B871E12EB549CcF6afD324c46E47D`.

###### A.2.2.10.1.1.1.2.3.2.22 - USDS Facet [Core]  <!-- UUID: 917e1162-3c06-4508-b0e9-02c5eefc1346 -->

The USDS Facet (`USDSFacet`) mints and burns USDS against an allocator vault, drawing USDS into and wiping it from the vault buffer. Its address on Ethereum Mainnet is `0x1221CC4B85Ab260660aD21C2829e0EB516dffBc7`.

###### A.2.2.10.1.1.1.2.3.2.23 - weETH Facet [Core]  <!-- UUID: abe32bbc-2ac3-4d3c-8133-14c233e6853d -->

The weETH Facet (`WEETHFacet`) stakes ETH (from WETH) into ether.fi eETH and wraps it to weETH, and handles the unwrap, withdrawal-request, and claim flow back to WETH. Its address on Ethereum Mainnet is `0x1d8D089EB7D558F5dc6aA0cf98DDe13B77b3F641`.

###### A.2.2.10.1.1.1.2.3.2.24 - Wrap Proxy ETH Facet [Core]  <!-- UUID: 2dae0ea0-5fff-4806-8c30-27a92e5676dc -->

The Wrap Proxy ETH Facet (`WrapProxyETHFacet`) wraps the ALM Proxy's entire native ETH balance into WETH. Its address on Ethereum Mainnet is `0x081506DE21C695Af5e61a81aD288C8A96B6b59B9`.

###### A.2.2.10.1.1.1.2.3.2.25 - wstETH Facet [Core]  <!-- UUID: 304c403a-ca08-4f49-a2f8-34c3c8a793db -->

The wstETH Facet (`WSTETHFacet`) converts WETH to ETH to wstETH (Lido) and handles the Lido withdrawal-queue request and claim flow back to WETH. Its address on Ethereum Mainnet is `0x3a82D11Cd37Fb0098363262Dc69425d07Fa05516`.

###### A.2.2.10.1.1.1.2.3.3 - PAU Factory [Core]  <!-- UUID: cc980032-b7e4-41c5-ac4d-2f99f89f51dc -->

The PAU Factory (`PAUFactory`) is the contract that deploys new Diamond PAU Instances. Its address on Ethereum Mainnet is `0x69A5d548830AC2A4Ba90A44a2C75BDA71f97fc66`.

###### A.2.2.10.1.1.1.2.3.4 - PAU Assembler [Core]  <!-- UUID: 8772a459-55ea-4387-889d-08fb01ad40d4 -->

The PAU Assembler (`DefaultPAUAssembler`) is the contract that assembles a Diamond PAU Instance from its Beacon-approved Facets at deployment. Its address on Ethereum Mainnet is `0xc812aAD3FaE2D3511C664374B601a9BeBFeCCa2E`.

###### A.2.2.10.1.1.1.2.3.5 - Administered Agent Factory [Core]  <!-- UUID: 833a0750-ff91-4fdc-95a8-af77df301dbc -->

The Administered Agent Factory (`AdministeredAgentFactory`) is the contract that deploys the `AdministeredAgent` contracts that hold the Allocator Role on the Controller of a Diamond PAU Instance, with the Prime Agent's Relayer system registered as their Actors. Its address on Ethereum Mainnet is `0x2968c3b5478cF93B70aB1e24255d4EDBBd27a089`.

###### A.2.2.10.1.1.1.2.3.6 - Configurator [Core]  <!-- UUID: 5e1f82c7-bcd6-46f8-aec0-3e767e55a93c -->

The Configurator (`Configurator`) is the contract through which designated actors operate a Diamond PAU's rate limits and pre-approved controller actions, within the ceilings and permissions as specified in [A.2.2.10.1.1.1.2.4 - PAS](989171ed-5424-42ee-83f4-199e1149699c). Further details will be specified in a future iteration of the Atlas.

###### A.2.2.10.1.1.1.2.3.7 - Beam State [Core]  <!-- UUID: 2e36bb4f-91db-4dca-bdb1-e4aa385b1129 -->

Beam State (`BeamState`) is the contract that records which actors, rate limits, and controller actions are authorized under [A.2.2.10.1.1.1.2.4 - PAS](989171ed-5424-42ee-83f4-199e1149699c). Further details will be specified in a future iteration of the Atlas.

###### A.2.2.10.1.1.1.2.4 - PAS [Core]  <!-- UUID: 989171ed-5424-42ee-83f4-199e1149699c -->

The PAS (Parallelized Allocation System) is a permissioned layer that lets designated actors operate a Diamond PAU's rate limits and pre-approved controller actions, within governance-set ceilings, without direct administrative control over the Diamond PAU. Further details will be specified in a future iteration of the Atlas.

###### A.2.2.10.1.1.1.2.5 - Liquidity Layer Operational Processes [Core]  <!-- UUID: 3b387169-c279-4d0f-918c-e6c424c6ea2c -->

The documents herein define the operational processes of the Diamond PAU implementation of the Allocation System — including the addition and removal of Facets approved on the Beacon, the functions performed through the Controller, and the management of rate limits.

###### A.2.2.10.1.1.1.2.5.1 - Facet Management [Core]  <!-- UUID: 892588a3-c9ca-407d-a3d7-bbb25a57d4c6 -->

The documents herein define the processes for adding and removing Facets available to Diamond PAU Instances.

###### A.2.2.10.1.1.1.2.5.1.1 - Adding a Facet [Core]  <!-- UUID: 9b6c5e8f-2148-4e2c-8971-9f516a7910c3 -->

The process for adding a Facet will be specified in a future iteration of the Atlas.

###### A.2.2.10.1.1.1.2.5.1.2 - Removing a Facet [Core]  <!-- UUID: 91c8c247-31ad-4e7b-a8b0-73e32c2a1367 -->

The process for removing a Facet will be specified in a future iteration of the Atlas.

###### A.2.2.10.1.1.1.2.5.2 - Diamond PAU Controller Functions [Core]  <!-- UUID: 5e941add-bf8d-4623-95a1-69795e7f7034 -->

The documents herein define the functions performed through the Diamond PAU Controller contract. The Controller dispatches each function to the corresponding Facet contract, which performs the operation on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.1 - USDS Facet [Core]  <!-- UUID: cc0dd1cb-5377-4186-be60-1112ba0340e4 -->

The documents herein define the Controller functions available for the [A.2.2.10.1.1.1.2.3.2.22 - USDS Facet](917e1162-3c06-4508-b0e9-02c5eefc1346).

###### A.2.2.10.1.1.1.2.5.2.1.1 - Mint USDS [Core]  <!-- UUID: d9173f82-6a6b-432a-a6e4-c8f80f70ba35 -->

The documents herein define the steps to mint USDS from the allocator vault to the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.1.1.1 - Allocator Role [Core]  <!-- UUID: 8eea7011-c299-4861-bf2e-0adb78e3ef30 -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a USDS mint by calling the `usds_mint` function on the Diamond PAU Controller, passing the amount of USDS to mint. The Controller dispatches the call to the USDS Facet, which performs the mint on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.1.1.2 - Rate Limit [Core]  <!-- UUID: b6d5f36b-3832-4cb7-b9e3-ea2543fc7d4e -->

The minting of USDS is subject to the on-chain rate limit identified by `LIMIT_USDS_MINT`. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.

###### A.2.2.10.1.1.1.2.5.2.1.1.3 - Mint USDS To ALM Proxy [Core]  <!-- UUID: 1490a13f-c897-4f0d-9ba3-205f40900321 -->

The USDS Facet's `mint` function draws the specified amount of USDS from the allocator vault by calling the vault's `draw` function, then transfers that USDS from the vault's buffer to the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.1.2 - Burn USDS [Core]  <!-- UUID: f01e63b7-dde7-422a-89a1-6931839d49f5 -->

The documents herein define the steps to burn USDS held by the ALM Proxy, returning it to the allocator vault.

###### A.2.2.10.1.1.1.2.5.2.1.2.1 - Allocator Role [Core]  <!-- UUID: 53d3749c-ef45-45ed-9657-373580abe3cf -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a USDS burn by calling the `usds_burn` function on the Diamond PAU Controller, passing the amount of USDS to burn. The Controller dispatches the call to the USDS Facet, which performs the burn on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.1.2.2 - Rate Limit [Core]  <!-- UUID: b900fd43-5f7c-438f-a1dd-0e89db98f4db -->

The burning of USDS is subject to the on-chain rate limit identified by `LIMIT_USDS_BURN`. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit. The burn additionally increases the `LIMIT_USDS_MINT` rate limit by the same amount, where that rate limit is configured, restoring minting capacity.

###### A.2.2.10.1.1.1.2.5.2.1.2.3 - Burn USDS From ALM Proxy [Core]  <!-- UUID: feace76a-e48a-42da-8732-74bbf55c530f -->

The USDS Facet's `burn` function transfers the specified amount of USDS from the ALM Proxy to the allocator vault's buffer, then wipes the corresponding debt by calling the vault's `wipe` function.

###### A.2.2.10.1.1.1.2.5.2.2 - Aave v3 Facet [Core]  <!-- UUID: e679e470-17f3-40ef-b455-dd424a498992 -->

The documents herein define the Controller functions available for the [A.2.2.10.1.1.1.2.3.2.1 - Aave v3 Facet](c9ecd9c2-dd1b-426b-8e52-66a2b1892289).

###### A.2.2.10.1.1.1.2.5.2.2.1 - Deposit To Aave v3 Market [Core]  <!-- UUID: 5592661d-78e9-4185-9c6e-15ffa47e0aef -->

The documents herein define the steps to deposit an asset held by the ALM Proxy into an Aave v3 market, which mints aTokens to the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.2.1.1 - Allocator Role [Core]  <!-- UUID: 26eec581-240e-4214-85a4-ee9309b986d4 -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate an Aave v3 market deposit by calling the `aave_deposit` function on the Diamond PAU Controller, passing the address of the aToken and the amount to deposit. The Controller dispatches the call to the Aave v3 Facet, which performs the deposit on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.2.1.2 - Rate Limit [Core]  <!-- UUID: 989bca9d-f56a-4965-8684-62de547f605a -->

The deposit is subject to the on-chain deposit rate limit identified by `LIMIT_AAVE_DEPOSIT` for the underlying asset, the address of the pool, and the address of the aToken. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.

###### A.2.2.10.1.1.1.2.5.2.2.1.3 - Deposit Asset Into Aave v3 Market [Core]  <!-- UUID: d783250a-d160-4f1f-8648-e2c9a6d95816 -->

The Aave v3 Facet's `deposit` function supplies the specified amount of the asset to the Aave v3 market on behalf of the ALM Proxy, and aTokens are minted to the ALM Proxy. The aTokens received must satisfy the configured maximum slippage.

###### A.2.2.10.1.1.1.2.5.2.2.2 - Withdraw From Aave v3 Market [Core]  <!-- UUID: 038eaa5c-d4c0-4a56-8d30-bc3a04508f0e -->

The documents herein define the steps to withdraw an asset from an Aave v3 market to the ALM Proxy by burning the corresponding aTokens.

###### A.2.2.10.1.1.1.2.5.2.2.2.1 - Allocator Role [Core]  <!-- UUID: c5a30d6c-6f3a-48a1-af35-39c0ee0bece4 -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate an Aave v3 market withdrawal by calling the `aave_withdraw` function on the Diamond PAU Controller, passing the address of the aToken and the amount to withdraw. The Controller dispatches the call to the Aave v3 Facet, which performs the withdrawal on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.2.2.2 - Rate Limit [Core]  <!-- UUID: ef6077eb-1cd4-4c17-bbf5-ce98c2cc1b92 -->

The withdrawal is subject to the on-chain withdrawal rate limit identified by `LIMIT_AAVE_WITHDRAW` for the address of the pool and the address of the aToken. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.

###### A.2.2.10.1.1.1.2.5.2.2.2.3 - Withdraw Asset From Aave v3 Market [Core]  <!-- UUID: ee2933f7-b7c6-4002-92f1-8b69c063a4a8 -->

The Aave v3 Facet's `withdraw` function withdraws the specified amount of the asset from the Aave v3 market to the ALM Proxy, burning the corresponding aTokens.

###### A.2.2.10.1.1.1.2.5.2.3 - Basin Facet [Core]  <!-- UUID: 7ab0c0f2-fc41-4b3f-9dc8-e62463bb3e62 -->

The documents herein define the Controller functions available for the [A.2.2.10.1.1.1.2.3.2.2 - Basin Facet](d9cbf883-119e-403d-8efa-125997cd8897).

###### A.2.2.10.1.1.1.2.5.2.3.1 - Deposit To Basin [Core]  <!-- UUID: d0c0a142-6ed5-4423-acbd-35ae6fdacb9f -->

The documents herein define the steps to deposit an asset held by the ALM Proxy into a Basin, which mints Basin shares to the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.3.1.1 - Allocator Role [Core]  <!-- UUID: b2e3b84d-acbd-4704-b55e-e2026aa63058 -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a Basin deposit by calling the `basin_deposit` function on the Diamond PAU Controller, passing the address of the Basin contract, the address of the asset, the amount to deposit, and the minimum number of shares to receive (`minSharesOut`). The Controller dispatches the call to the Basin Facet, which performs the deposit on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.3.1.2 - Rate Limit [Core]  <!-- UUID: 34b6d2ab-837c-4fb0-a397-77d776a32bc3 -->

The deposit is subject to the on-chain deposit rate limit identified by `LIMIT_BASIN_DEPOSIT` for the address of the asset and the address of the Basin contract. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.

###### A.2.2.10.1.1.1.2.5.2.3.1.3 - Deposit Asset Into Basin [Core]  <!-- UUID: 8d3420d5-86a7-4468-8f08-92cc00fed557 -->

The Basin Facet's `deposit` function deposits the specified amount of the asset into the Basin on behalf of the ALM Proxy, and Basin shares are minted to the ALM Proxy. The deposit does not complete unless the number of shares minted is at least the specified minimum (`minSharesOut`).

###### A.2.2.10.1.1.1.2.5.2.3.2 - Withdraw From Basin [Core]  <!-- UUID: 8aad3588-6c58-4539-a1e2-46b0e6f97e92 -->

The documents herein define the steps to withdraw an asset from a Basin to the ALM Proxy by burning the corresponding Basin shares.

###### A.2.2.10.1.1.1.2.5.2.3.2.1 - Allocator Role [Core]  <!-- UUID: 75edeae6-46e4-4761-b2c7-0416038c97cf -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a Basin withdrawal by calling the `basin_withdraw` function on the Diamond PAU Controller, passing the address of the Basin contract, the address of the asset, the maximum amount to withdraw, and the minimum conversion rate (`minConversionRate`). The Controller dispatches the call to the Basin Facet, which performs the withdrawal on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.3.2.2 - Rate Limit [Core]  <!-- UUID: d915bc35-e8d8-4d48-a285-92335bd09343 -->

The withdrawal is subject to the on-chain withdrawal rate limit identified by `LIMIT_BASIN_WITHDRAW` for the address of the asset and the address of the Basin contract. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.

###### A.2.2.10.1.1.1.2.5.2.3.2.3 - Withdraw Asset From Basin [Core]  <!-- UUID: 25da7163-b052-459f-91b5-8da3aafa61c7 -->

The Basin Facet's `withdraw` function withdraws up to the specified maximum amount of the asset from the Basin to the ALM Proxy, burning the corresponding Basin shares. The withdrawal does not complete unless the assets received satisfy the specified minimum conversion rate (`minConversionRate`) relative to the shares burned.

###### A.2.2.10.1.1.1.2.5.2.4 - PSM Facet [Core]  <!-- UUID: 6d22c2b8-bc80-4248-a690-7b858c925014 -->

The documents herein define the Controller functions available for the [A.2.2.10.1.1.1.2.3.2.16 - PSM Facet](afa3da61-c32a-4efd-900b-16e1c262c842).

###### A.2.2.10.1.1.1.2.5.2.4.1 - Swap USDS To USDC [Core]  <!-- UUID: bff6ae57-ce3e-4520-ad46-5fe87b721408 -->

The documents herein define the steps to swap USDS held by the ALM Proxy for USDC via DAI, through the DAI-USDS migrator and the Lite PSM.

###### A.2.2.10.1.1.1.2.5.2.4.1.1 - Allocator Role [Core]  <!-- UUID: f3c79493-8704-4d20-9eaa-e2e381f3920d -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a USDS to USDC swap by calling the `psm_swapUSDSToUSDC` function on the Diamond PAU Controller, passing the amount of USDC to receive. The Controller dispatches the call to the PSM Facet, which performs the swap on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.4.1.2 - Rate Limit [Core]  <!-- UUID: 1a1d74ec-888d-4f0a-93c2-3669fa4efe45 -->

The swap is subject to the on-chain rate limit identified by `LIMIT_USDS_TO_USDC`. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit.

###### A.2.2.10.1.1.1.2.5.2.4.1.3 - Swap USDS For USDC [Core]  <!-- UUID: 58631630-a9e3-4bd6-a1ea-59b0ef8f5bee -->

The PSM Facet's `swapUSDSToUSDC` function swaps USDS held by the ALM Proxy for the specified amount of USDC via DAI, through the DAI-USDS migrator and the Lite PSM.

###### A.2.2.10.1.1.1.2.5.2.4.2 - Swap USDC To USDS [Core]  <!-- UUID: 3fd327ea-7043-434a-996a-3419e7692959 -->

The documents herein define the steps to swap USDC held by the ALM Proxy for USDS via DAI, through the DAI-USDS migrator and the Lite PSM.

###### A.2.2.10.1.1.1.2.5.2.4.2.1 - Allocator Role [Core]  <!-- UUID: 85a2ac37-da60-4a04-96eb-600f635ab388 -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a USDC to USDS swap by calling the `psm_swapUSDCToUSDS` function on the Diamond PAU Controller, passing the amount of USDC to swap. The Controller dispatches the call to the PSM Facet, which performs the swap on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.4.2.2 - Rate Limit [Core]  <!-- UUID: b489a966-f631-429d-85da-cb6258f001c9 -->

The swap is subject to the on-chain rate limit identified by `LIMIT_USDC_TO_USDS`. This limit is enforced automatically within the call; the transaction reverts if the amount exceeds the current rate limit. The swap additionally increases the `LIMIT_USDS_TO_USDC` rate limit by the same amount, where that rate limit is configured, restoring capacity in the opposite swap direction.

###### A.2.2.10.1.1.1.2.5.2.4.2.3 - Swap USDC For USDS [Core]  <!-- UUID: fa1364a3-081c-4327-8ef4-637a3fdd1105 -->

The PSM Facet's `swapUSDCToUSDS` function swaps the specified amount of USDC held by the ALM Proxy for USDS via DAI, through the DAI-USDS migrator and the Lite PSM.

###### A.2.2.10.1.1.1.2.5.2.5 - Uniswap v3 Facet [Core]  <!-- UUID: 417edcc0-3d50-48ba-8fc2-38b361dbc297 -->

The documents herein define the Controller functions available for the [A.2.2.10.1.1.1.2.3.2.20 - Uniswap v3 Facet](b808a829-2f31-42f1-ac9f-6801d3eb8437). Each function is restricted to an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a).

###### A.2.2.10.1.1.1.2.5.2.5.1 - Add Liquidity To Uniswap v3 [Core]  <!-- UUID: 32d3213a-e40a-4169-94d7-e65bb6c23c19 -->

The documents herein define the steps to add liquidity to a Uniswap v3 pool on behalf of the ALM Proxy, minting a new position or increasing an existing one.

###### A.2.2.10.1.1.1.2.5.2.5.1.1 - Allocator Role [Core]  <!-- UUID: 955f7809-40e6-43a3-900d-6992a6e1d2ef -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may add liquidity by calling the `uniswapV3_addLiquidity` function on the Diamond PAU Controller. The call passes the address of the pool, the identifier of an existing position to increase (or zero to mint a new position), the lower and upper tick bounds, the target amounts of each pool token to deposit, the minimum amounts to accept, and a deadline. The Controller dispatches the call to the Uniswap v3 Facet, which performs the deposit on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.5.1.2 - Rate Limit [Core]  <!-- UUID: 7e771c08-d37b-4e44-b5d2-b21aabde6a3a -->

The aggregate deposit limit sums one unit of either pool token as equivalent, so it is only meant to work with a stable-stable pool. Using it on a pool with two tokens of different value would produce a cap unrelated to actual exposure.

Adding liquidity is subject to three (3) on-chain deposit rate limits, each identified by `LIMIT_UNISWAP_V3_DEPOSIT`. One is the aggregate limit described above, metered in a normalized unit summed across both pool tokens. The other two are per-token limits, one for each of the pool's two (2) tokens, each metered in that token's own unit. All three limits are enforced automatically within the call; the transaction reverts if the amount attributed to any of the three exceeds its current rate limit.

###### A.2.2.10.1.1.1.2.5.2.5.1.3 - Add Liquidity To Uniswap v3 Position [Core]  <!-- UUID: 164268cf-b6e5-4c1a-83e5-d199f453cc1b -->

The Uniswap v3 Facet's `addLiquidity` function attempts to deposit the target amounts of the pool's two (2) tokens on behalf of the ALM Proxy. To open a new position, it calls the Uniswap v3 position manager's `mint` function. To add to an existing position, it calls the position manager's `increaseLiquidity` function instead — but only after confirming the ALM Proxy is the current owner of that position. Depositing into a tick range does not necessarily use the full target amount of both tokens; the Uniswap v3 Facet measures the amounts actually deposited by comparing the ALM Proxy's token balances before and after the call, rather than relying on the target amounts or the position manager's own return values. The deposit does not complete unless the tick bounds fall within the configured bounds for the pool. Before depositing, the Uniswap v3 Facet checks the specified minimums against expected amounts derived from the pool's time-weighted average price, not its current spot price. Those minimums must in turn satisfy the configured maximum slippage for the pool, and the deposit does not complete unless this check passes.

###### A.2.2.10.1.1.1.2.5.2.5.2 - Remove Liquidity From Uniswap v3 [Core]  <!-- UUID: e37d1163-b801-4cba-ab3a-2440a1f36ae6 -->

The documents herein define the steps to remove liquidity from a Uniswap v3 position held by the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.5.2.1 - Allocator Role [Core]  <!-- UUID: 6cfcbc24-2d8d-40fe-bc90-ec679c084ef0 -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may remove liquidity by calling the `uniswapV3_removeLiquidity` function on the Diamond PAU Controller. The call passes the address of the pool, the identifier of the position, the amount of liquidity to remove, the minimum amounts of each pool token to accept, and a deadline. The Controller dispatches the call to the Uniswap v3 Facet, which performs the withdrawal on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.5.2.2 - Rate Limit [Core]  <!-- UUID: a60193f3-3af2-4a50-a42d-4b2dad8adc6a -->

The aggregate withdrawal limit sums one unit of either pool token as equivalent, so it is only meant to work with a stable-stable pool. Using it on a pool with two tokens of different value would produce a cap unrelated to actual exposure.

Removing liquidity is subject to three (3) on-chain withdrawal rate limits, each identified by `LIMIT_UNISWAP_V3_WITHDRAW`. One is the aggregate limit described above, metered in a normalized unit summed across both pool tokens. The other two are per-token limits, one for each of the pool's two (2) tokens, each metered in that token's own unit. All three limits are enforced automatically within the call; the transaction reverts if the amount attributed to any of the three exceeds its current rate limit.

These limits meter only the amount returned by decreasing liquidity. Fees already accrued on the position are collected in the same call but are not counted against them.

###### A.2.2.10.1.1.1.2.5.2.5.2.3 - Remove Liquidity From Uniswap v3 Position [Core]  <!-- UUID: 315b3614-18bb-4ca0-b1c7-3459fd449ad8 -->

The Uniswap v3 Facet's `removeLiquidity` function first confirms the ALM Proxy is the current owner of the position, then decreases the specified amount of liquidity from it. It does this by calling the Uniswap v3 position manager's `decreaseLiquidity` function. Before the decrease, the facet collects any fees the position has already accrued. The `decreaseLiquidity` call itself does not transfer any tokens to the ALM Proxy; it only credits the withdrawn amounts to the position as tokens owed. After the decrease, the facet collects again, and this second collection is what delivers the withdrawn principal to the ALM Proxy. The withdrawal does not complete unless the resulting amounts satisfy the specified minimums, and those minimums must in turn satisfy the configured maximum slippage for the pool. Unlike the deposit-side check on adding liquidity, this check is against the amounts actually withdrawn, measured after the decrease and both collections have already executed; it is not checked against an independent price reference computed before execution.

###### A.2.2.10.1.1.1.2.5.2.5.3 - Swap On Uniswap v3 [Core]  <!-- UUID: 137e7a7b-9488-409c-85ed-f91d31303f7b -->

The documents herein define the steps to swap one pool token for the other through a Uniswap v3 pool on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.5.3.1 - Allocator Role [Core]  <!-- UUID: 9b0217c7-8617-42c3-9e2e-b0b377607f50 -->

Only an address holding the [A.2.2.10.1.1.1.2.2.3 - Allocator Role](e7a97395-ddd5-4ae8-874f-1bb3f247446a) (`ALLOCATOR_ROLE`) may initiate a swap by calling the `uniswapV3_swap` function on the Diamond PAU Controller. The call passes the address of the pool, the address of the token to sell, the amount to sell, the minimum amount to receive, and the maximum allowed tick deviation from the pool's time-weighted average price. The Controller dispatches the call to the Uniswap v3 Facet, which performs the swap on behalf of the ALM Proxy.

###### A.2.2.10.1.1.1.2.5.2.5.3.2 - Rate Limit [Core]  <!-- UUID: d2bd2910-494c-4a4e-b276-8f325c69e36b -->

The swap is subject to the on-chain rate limit identified by `LIMIT_UNISWAP_V3_SWAP` for the address of the token being sold and the address of the pool. This limit is enforced automatically within the call; the transaction reverts if the amount sold exceeds the current rate limit.

###### A.2.2.10.1.1.1.2.5.2.5.3.3 - Swap Tokens Through Uniswap v3 Pool [Core]  <!-- UUID: 3986fe17-e84d-407a-9192-61e6b842426a -->

The Uniswap v3 Facet's `swap` function attempts to sell the specified amount of the given token through the Uniswap v3 router for the pool's other token. The execution price is bounded against the pool's time-weighted average price by the specified maximum tick deviation. If the swap reaches this price limit before selling the full specified amount, execution stops without reverting, and part of the specified amount goes unsold. The Uniswap v3 Facet measures the amount actually sold by comparing the ALM Proxy's balance of the given token before and after the swap, and applies the Rate Limit against that measured amount rather than the specified amount. The swap does not complete unless the specified tick deviation falls within the configured maximum for the pool and the amount received is at least the specified minimum, which must be a non-zero value. The maximum tick deviation is the only governance-configured control on the swap's execution quality; the minimum amount received has no equivalent governance floor beyond being non-zero.

###### A.2.2.10.1.1.1.2.5.3 - Rate Limit Management [Core]  <!-- UUID: 6f5bc654-a053-4b1f-9ada-6aa13d0a2109 -->

The documents herein define the protocol for querying, setting, and adjusting `RateLimits` for Diamond PAU Instances using their `RateLimitID`s. Rate limits are maintained in line with the operating Prime Agent's strategy, market conditions, and security considerations.

###### A.2.2.10.1.1.1.2.5.3.1 - RateLimits Query [Core]  <!-- UUID: 1cb17b82-a294-4942-8183-4d90b224a79d -->

The following code implements the public view functions that query the current `RateLimits` for a specific key:

`function getRateLimitData(bytes32 key) external override view returns (RateLimitData memory) {
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

###### A.2.2.10.1.1.1.2.5.3.2 - Set RateLimit [Core]  <!-- UUID: f671061e-11a0-4d3b-bb6e-9f4ee9a012a9 -->

The following code sets the `RateLimit` for a specific key, restricted to the `DEFAULT_ADMIN_ROLE` holder (Sky Governance acting through the Prime Agent's SubProxy):

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

###### A.2.2.10.1.1.1.2.5.3.3 - Set Unlimited RateLimit [Core]  <!-- UUID: a85b7e8b-c4e9-44de-b717-efa4c8268d3b -->

The following code sets an unlimited `RateLimit` for a specific key, restricted to the `DEFAULT_ADMIN_ROLE` holder (Sky Governance acting through the Prime Agent's SubProxy):

`function setUnlimitedRateLimitData(bytes32 key) external override {
        setRateLimitData(key, type(uint256).max, 0, type(uint256).max, block.timestamp);
    }`

###### A.2.2.10.1.1.1.2.5.3.4 - Set Trigger For RateLimit Decrease [Core]  <!-- UUID: 39217368-efa1-4168-a231-b010d6e23dfa -->

The following code decreases the `RateLimit` for a specific key, restricted to the `CONTROLLER` role (the Controller contract), called as allocations consume the limit:

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

###### A.2.2.10.1.1.1.2.5.3.5 - Set Trigger For RateLimit Increase [Core]  <!-- UUID: ee55aa72-1405-49cb-a7fe-3e8adc9ee64c -->

The following code increases the `RateLimit` for a specific key, restricted to the `CONTROLLER` role (the Controller contract), called as allocations return the limit:

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

        emit RateLimitIncreaseTriggered(key, amountToIncrease, currentRateLimit, newLimit);
    }`

###### A.2.2.10.1.1.2 - Allocation Instance Setup Process Definition [Core]  <!-- UUID: f47513f6-34e4-40a4-b7ff-8d68d75070be -->

The documents herein define the process for setting up an Allocation Instance as part of the Allocation System Primitive.

###### A.2.2.10.1.1.2.1 - Real World Agreements And Planning [Core]  <!-- UUID: eeeeb5ff-3f11-4857-a3da-ad354569f833 -->

The documents herein define the preliminary, off-chain human coordination stage of setting up an Allocation Instance.

###### A.2.2.10.1.1.2.1.1 - Initial Concept And Feasibility Discussions [Core]  <!-- UUID: b60b170f-9e8c-4577-a046-313039ff25ba -->

The Prime Agent identifies a yield opportunity on a target chain that can exceed the Base Rate. The Prime Agent estimates Required Risk Capital (RRC) and Asset Liability Management requirements associated with the opportunity and evaluates options for fulfilling them. The Prime Agent also considers exchange and bridging costs, if applicable. Based on this, the Prime Agent develops a net yield target for the opportunity factoring in all of these costs. The output of this step is an internal meeting note summarizing the idea as well as estimates of Required Risk Capital, Asset Liability Management, and exchange / bridging costs.

###### A.2.2.10.1.1.2.1.2 - Preliminary Required Risk Capital and Asset Liability Management Arrangement [Core]  <!-- UUID: 8d3b553c-440d-4c67-b661-37ab1edc1c58 -->

If necessary, the Prime Agent reaches out to other Prime Agents that could provide Junior Risk Capital (JRC) / Senior Risk Capital (SRC) or assume Asset Liability Management obligations. The Prime Agent negotiates with these other Prime Agents and documents these potential deals. The output of this step is an informal confirmation of JRC/SRC and Asset Liability Management transfer details.

###### A.2.2.10.1.1.2.1.3 - Prime Agent Preparation Of Capital And Operational Plan [Core]  <!-- UUID: 4aa05a21-86d6-451e-a1b1-2afd1107edba -->

The Capital and Operational Plan ("C&O Plan") articulates the Prime Agent’s strategy for a proposed new Allocation Instance or a modification to an existing Instance. In addition to articulating the Instance’s strategic objectives and operational parameters, the C&O Plan includes a pro-forma Required Risk Capital (RRC) estimate and a strategy for ensuring sufficient Total Risk Capital (TRC) coverage.

The C&O Plan is the major input into the Artifact Edit Proposal that codifies the new or modified Instance. Following the approval of such a proposal by Prime governance, the details and commitments outlined in the C&O Plan are formally integrated into the respective Instance Configuration Document of the Prime Agent’s Artifact.

###### A.2.2.10.1.1.2.1.3.1 - Pro-Forma Instance RRC Estimate [Core]  <!-- UUID: c3b53ee8-328a-4a79-8afe-ac0de99d8706 -->

As a critical component of the Capital & Operational Plan, the Prime Agent must prepare an initial pro-forma Instance Required Risk Capital (RRC) estimate. This estimate serves as the basis for the Prime’s capital planning prior to the availability of official RRC figures from Sky Core. The estimate must strictly adhere to the implementation of RRC-models defined in [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.2.2.10.1.1.2.1.3.2 - Notional Total Risk Capital (TRC) Coverage Strategy [Core]  <!-- UUID: a30447be-5214-4398-82aa-7306eeabd6f5 -->

As a critical component of the Capital & Operational Plan, the Prime Agent must articulate its strategy for ensuring its Total Risk Capital (TRC) adequately covers the pro-forma Instance RRC of a new or modified Instance and the resulting impact on its Aggregate RRC.

The Prime’s notional TRC coverage strategy must outline how this new Instance’s RRC will be notionally accounted for or supported by the Prime’s overall TRC pool. If the Prime’s current TRC is not sufficient to cover its estimated increased Aggregate RRC, the strategy should outline the Prime Agent’s intended steps for acquiring additional JRC/SRC.

For instance, this risk-capital acquisition strategy could involve:

1. Renting Junior Risk Capital (JRC)
    - Sourcing Prime-External Junior Risk Capital (PEJRC) by renting it from other Primes through Ecosystem Accords.
    - Sourcing Tokenized External Junior Risk Capital (TEJRC) from external capital providers.
2. Sourcing Senior Risk Capital (SRC):
    - Originating SRC through the Sky monthly auction.
    - Renting OSRC from other Primes through Ecosystem Accords.
3. Increasing Internal Junior Risk Capital (IJRC): A Prime might have plans to bolster its own IJRC through retained earnings or other internal means.
4. Decreasing exposure in an existing Instance(s) to lower Aggregate RRC.

The Prime’s capital-acquisition strategy should indicate how the Prime will remain in compliance with all relevant Atlas rules, such as sourcing ratios that constrain how much Senior Risk Capital can be "enabled" or counted toward a Prime’s Aggregate RRC. See [A.3.2.1.2.3 - Total Risk Capital Sourcing Ratios](9e99b084-f15a-4f60-b831-d6c0bd9aec04).

###### A.2.2.10.1.1.2.1.3.3 - Additional Elements Of Capital And Operational Plan [Core]  <!-- UUID: a156b120-8b27-4a31-95fe-4154205ca102 -->

The Capital & Operational Plan includes the following additional elements:

- Operational Parameters: defines the Instance’s target chain(s), protocols, initial capital, maximum deposit sizes, and any other parameters that underpin the pro-forma RRC calculation.
- Data Submission Protocol: defines how yields, Required Risk Capital usage, ALM costs, exchange data, etc. will be reported and audited.
- Emergency Procedures: defines mechanisms to be triggered if security or risk capital thresholds are breached, such as a kill switch or partial freeze.
- Asset Liability Management (ALM) Strategy: details if the Prime will meet its ALM requirements through its own direct asset management or by transferring its obligations to another Prime Agent via the ASC Rental Primitive. If the latter, the C&O Plan must reference the governing Ecosystem Accord and its key terms.
- Performance-based Adjustments: define the conditions or KPIs that allow adjustments to Instance deposit caps or yield expansions without requiring a formal Artifact edit.

###### A.2.2.10.1.1.2.1.4 - Preliminary Informal Check With Operational GovOps [Core]  <!-- UUID: e7d3d696-e2d0-4d4b-b4d6-c7a0c47b7cc6 -->

The Prime Agent presents the Capital and Operational Plan for the Allocation Instance to Operational GovOps, including any associated JRC/SRC and Asset Liability Management arrangements. Operational GovOps reviews and either provides an informal greenlight or requests modifications to the Plan. The output of this step is Operational GovOps approval to proceed with a request to revise the C&O Plan, as applicable.

###### A.2.2.10.1.1.2.2 - Instance Codification and Validation [Core]  <!-- UUID: 410c84be-ab41-4444-a7cb-1c19a0448948 -->

The documents herein define how agreements to set up an Allocation Instance are codified and validated in the Powerhouse system and how governance votes happen.

###### A.2.2.10.1.1.2.2.1 - Agent Inputs [Core]  <!-- UUID: 7a36f228-0438-43da-ae5f-a43af70c0121 -->

The Prime Agent drafts an update to the Prime Agent Artifact adding the Allocation Instance to the list of active Allocation Instances and including the information specified in [A.2.2.10.1.2.6 - List Of Allocation Instances](e4975062-6d19-438b-a5d5-cfc1a7fd8cb9). The Prime Agent submits the draft to the Powerhouse system. The output of this step is a draft Prime Agent Artifact update in the Powerhouse system.

###### A.2.2.10.1.1.2.2.2 - Validation And Off-Chain Vote [Core]  <!-- UUID: dbae3918-75f7-469d-b623-8faa5ea7aa70 -->

The Operational Executor Facilitator reviews the proposal to ensure that it is complete and aligned with the Atlas. The Operational Executor Facilitator then initiates an off-chain snapshot vote, following the quorum and majority rules in the Prime Agent Artifact. When complete, the result of the vote is recorded in the Powerhouse system. The output of this step is the snapshot vote result recorded in the Powerhouse system.

###### A.2.2.10.1.1.2.2.3 - Official Update of Artifact [Core]  <!-- UUID: 2b1612b8-480c-49b3-a304-6a6f593340de -->

If the Allocation Instance is successfully approved, the Operational Executor Facilitator finalizes and publishes the update to the Prime Agent Artifact, making it effective in the Atlas. The output of this step is an updated Prime Agent Artifact with the new Allocation Instance.

Once a new Instance is deployed, its data is integrated into risk-capital monitoring systems and its RRC will be officially determined and tracked via the Sky Core RRC Dashboard. See [A.2.2.10.1.1.3.2.1.1 - Sky Core Required Risk Capital (RRC) Dashboard](4eac2c9e-2718-4881-a3f1-ed10fb3f4d13). This official RRC figure supersedes the Prime-prepared pro-forma RRC.

###### A.2.2.10.1.1.2.3 - Instance Setup Deployments [Core]  <!-- UUID: 3766cb8c-ab6c-41af-9465-b8dea76d0532 -->

The documents herein define how the deployment of an Allocation Instance is executed on-chain. In the short-term, an Allocation Instance may also be deployed using the process for Interim Deployments specified in [A.1.10.2.3.2.2.2 - Interim Deployments](9b3edbbf-89d1-42da-a9c3-18f858f8471f).

The Prime Agent must subsequently prepare a pro-forma Required Risk Capital estimate, which must be approved by the Core Council Risk Advisor, before the parameters of the Instance can be updated for normal operation.

###### A.2.2.10.1.1.2.3.1 - Conduit Development And Testing [Core]  <!-- UUID: 6899a722-3d1a-4bd1-80f2-f36be91bbab0 -->

Once formally validated, the Prime Agent implements the new Allocation Instance based on the specifications in the Prime Agent Artifact. Operational GovOps must test the Allocation Instance with minimal funds from the Prime Agent’s Central Allocation Buffer, verifying deposit / withdrawal logic, slippage constraints, and oracle checks. If this testing is successful Operational GovOps confirms that the Allocation Instance satisfies all risk constraints specified in the Prime Agent Artifact. The output of this step is validated contracts for the Allocation Instance and a green light to proceed with a scaled deployment.

###### A.2.2.10.1.1.2.3.2 - Initial Deployment and Required Risk Capital / Asset Liability Management Execution [Core]  <!-- UUID: 648bcae7-9723-4282-81fe-fcc77fd6f90e -->

The Prime Agent finalizes JRC/SRC and Asset Liability Management Arrangements. Operational GovOps records these arrangements in the Powerhouse interface. If Operational GovOps is charged with operationalizing an Instance, it deploys funds from the Prime Agent’s Operational Buffer into the Allocation Instance, performing any necessary DEX exchanges. See [A.2.2.10.1.1.3.1 - Operationalization Of Allocation Instances](989512c2-4fa1-46b8-947c-00e3c0b56024). In doing so, Operational GovOps follows instructions in the Agent Artifact regarding the amount of capital to deploy and slippage tolerances. The output of this step is a fully deployed Allocation Instance conforming to Risk Capital and Asset Liability Management requirements.

###### A.2.2.10.1.1.3 - Allocation Instance Ongoing Management [Core]  <!-- UUID: 2db14aa7-ccfa-42f7-82a8-118048574d4c -->

The documents herein define the process for managing an Allocation Instance as part of the Allocation System Primitive.

###### A.2.2.10.1.1.3.1 - Operationalization Of Allocation Instances [Core]  <!-- UUID: 989512c2-4fa1-46b8-947c-00e3c0b56024 -->

Prime Agent teams may choose to directly operationalize their Allocation System Primitive Instances ("Instances") using internal, proprietary strategies that are not defined in their Artifacts. Alternatively, Prime Agents may elect to have the Instances operationalized by their Operational Executor Agent. This constitutes an exception to the general rule that Operational Executor Agents operationalize all Sky Primitives on behalf of Prime Agents. See [A.1.14.3.4 - Agent Role Delineation](fdf32ca5-5e2e-481e-9047-4d1599547216).

For Prime Agent teams that operationalize their Instances, they will be required to formulate KPIs for their proprietary strategies; should an Instance under-perform these KPIs, Operational GovOps is authorized to step in and operationalize the Instance(s) via a back-up strategy that is defined in the Agent Artifact. Additional logic on this point will be defined in a future iteration of the Atlas.

###### A.2.2.10.1.1.3.2 - Requirements And Infrastructure For Risk Capital And Asset Liability Management [Core]  <!-- UUID: 13eb2346-07e5-48b6-9740-ce60a20146ab -->

The documents herein define Risk Capital and Asset Liability Management requirements and infrastructure.

###### A.2.2.10.1.1.3.2.1 - Risk Capital Management [Core]  <!-- UUID: 1c5fb5bb-ec03-478c-89b7-4017d935276e -->

The documents herein detail the obligations, processes, standards and infrastructure related to risk-capital management.

###### A.2.2.10.1.1.3.2.1.1 - Sky Core Required Risk Capital (RRC) Dashboard [Core]  <!-- UUID: 4eac2c9e-2718-4881-a3f1-ed10fb3f4d13 -->

The Sky Core Required Risk Capital (RRC) Dashboard serves as the official system for determining and disseminating RRC figures for Prime Agents and their Allocation System Primitive Instances.

Prior to the full operational deployment of the Powerhouse system, Prime Agents must utilize the Sky Core RRC Dashboard as the authoritative source for their official Instance Total RRCs and Aggregate RRC. Data from this source is to be used for all internal TRC management, required reporting and compliance assessments.

The Sky Core RRC Dashboard is located at [https://info.skyeco.com/required-risk-capital](https://info.skyeco.com/required-risk-capital).

###### A.2.2.10.1.1.3.2.1.1.1 - Role and Functionality of the RRC Dashboard [Core]  <!-- UUID: f7da0f56-00f5-4bcf-bd31-b77c284c7992 -->

The RRC Dashboard provides a user interface for Prime Agents to view their official RRC figures. The Dashboard provides the following key information:

- Instance Total RRC: For each specific Allocation System Primitive Instance, the system displays its Instance Total RRC. This figure is the sum of all applicable risk-specific RRC calculations for that Instance, including:
    - Instance Financial RRC ([A.3.2.1.1.4 - Instance Financial RRC](ba1d5c0e-399f-47a6-b5d4-b3f5477d5787))
    - Instance Smart Contract RRC ([A.3.2.1.1.5 - Instance Smart Contract RRC](4b4ea578-28b4-481c-9abd-d34c5a4f383c))
    - Instance Administrative RRC ([A.3.2.1.1.6 - Instance Administrative RRC](c2b60f0d-6555-463c-9ad3-2a9746be77c5))

The models for certain risk-factors are still currently under development. See [A.2.2.10.1.1.3.2.1.1.2 - Interim Notice Regarding RRC Dashboard Coverage](18243e7a-5b62-459d-83fb-e50b9df05f9d).

- Aggregate RRC: For each Prime Agent, the system displays its Aggregate RRC, which is the sum of all its Instance Total RRCs. This is the figure against which a Prime Agent’s Total Risk Capital (TRC) adequacy is assessed.

###### A.2.2.10.1.1.3.2.1.1.2 - Interim Notice Regarding RRC Dashboard Coverage [Core]  <!-- UUID: 18243e7a-5b62-459d-83fb-e50b9df05f9d -->

Some Allocation System Instances displayed on the RRC Dashboard concern asset types whose risk models have not yet been fully developed. See [A.3.2.1.1.4.3 - Financial Risk Models](2af9fa64-ab25-4017-920c-f1c07dff4c06). An active Instance’s respective Instance Configuration Document will specify its `RRC Framework Full Implementation` status as either `Covered` or `Pending`.

###### A.2.2.10.1.1.3.2.1.2 - Primes' Total Risk Capital (TRC) Management [Core]  <!-- UUID: 3af8a3a2-25e5-44b3-87a4-7df1f2712685 -->

Prime Agent teams are responsible for managing their Total Risk Capital (TRC) to continuously meet their Aggregate Required Risk Capital (RRC). The accounting of TRC considers all on-chain holdings and any off-chain agreements, encumbrances, or conditions that may affect the immediate availability or eligibility of capital for RRC coverage. For a definition of Total Risk Capital, see [A.3.2.1.2.1 - Total Risk Capital Definition](6f6b25d6-f73c-4733-ba37-12a0a411433c).

The documents herein define requirements and standards for a Prime Agent’s internal TRC management systems.

###### A.2.2.10.1.1.3.2.1.2.1 - Objective of Prime TRC Management [Core]  <!-- UUID: 9a8120c4-0a5b-426f-97a5-283c708413f5 -->

To comply with Atlas risk capital requirements, Prime Agent teams must establish, maintain, and operate an internal system for TRC management. A Prime Agent’s internal TRC management system should enable proactive operational risk management. This entails ongoing capital adequacy assessment and strategic capital allocation planning for current and future Allocation System Primitive Instances, including the ability to perform scenario analyses for potential deployments or market stresses.

Prime Agents’ internal TRC management systems should enable them to maintain continuous sufficiency of the Prime Agent’s held TRC against its official Aggregate RRC. This requires real-time or near real-time comparison and internal alerting mechanisms to prevent and address potential shortfalls.
Primes must ensure that their internal TRC management systems maintain comprehensive, verifiable internal records of all TRC components, related transactions, and compliance activities to support internal governance and external verification processes, such as the submission of TRC Reports to Core GovOps. See [A.2.2.10.1.1.3.2.1.2.3 - Primes’ TRC Report](41ca2085-d71b-47e5-8b1a-b183b6e2b6fc).

###### A.2.2.10.1.1.3.2.1.2.2 - Minimum Capabilities of Prime TRC Management Systems [Core]  <!-- UUID: d034533f-9b6f-411c-8b60-3bccb374765f -->

A Prime Agent’s internal TRC management system should possess the following capabilities to meet the objectives outlined in [A.2.2.10.1.1.3.2.1.2.1 - Objective of Prime TRC Management](9a8120c4-0a5b-426f-97a5-283c708413f5).

1. Prime Agents’ internal TRC management systems should enable compliant sourcing and tracking of all TRC components, including Internal Junior Risk Capital (IJRC), Prime-External Junior Risk Capital (PEJRC), Tokenized External Junior Risk Capital (TEJRC), and Originated Senior Risk Capital (OSRC). Compliance in this context includes strict adherence to eligibility criteria and capital-sourcing ratios (e.g., External Per Internal, Senior Per Junior) as defined in the Atlas. See [A.3.2.1.2.3 - Total Risk Capital Sourcing Ratios](9e99b084-f15a-4f60-b831-d6c0bd9aec04).
The system must provide real-time or near real-time tracking of all held Total Risk Capital (TRC) components. This includes, for each TRC component:
    - Accurate valuation of the assets comprising each component.
    - Clear identification of the source of each component (e.g., Prime’s own SubProxy for IJRC, specific Ecosystem Accord references for rented PEJRC or OSRC, TEJRC encumbrance details, OSRC origination details).
    - Verification of each TRC component’s eligibility status according to Atlas rules. This includes tracking whether capital is “enabled” or “active” for RRC coverage purposes (e.g., based on Ecosystem Accord status, compliance with sourcing ratios, etc.).
    - Distinction between capital directly held by the Prime Agent and capital that is encumbered (e.g., PEJRC where the lending Prime retains custody but the capital is contractually committed).
2. Prime Agents' internal TRC management systems should enable dynamic-state accounting. The system must account for TRC components that are in dynamic, pending, or off-chain states, as these can impact the true risk capital available to a Prime Agent. This includes:
    - Pending transactions such as PEJRC or OSRC rental Ecosystem Accords that have been committed to by the parties, but not yet codified in the Atlas.
    - Capital in transit, e.g., assets that are committed to be IJRC, but currently moving between chains via bridges or locked in Cross-Chain Transfer Protocol (CCTP) messages awaiting finality.
    - Operational expenditures funded by TRC components (typically IJRC), such as blockchain transaction fees, oracle service fees, audit costs, and other operational overhead that reduces available risk capital. The system should track these expenditures in real-time or near real-time.
    - Any off-chain factors that could impair the immediate deployability or availability of TRC components.
3. Prime Agents' internal TRC management systems should enable continuous capital adequacy monitoring. The system must enable the near real-time comparison of the Prime Agent's internally tracked and calculated TRC against its official Aggregate RRC, as obtained from the Sky Core RRC Dashboard. See [A.2.2.10.1.1.3.2.1.1 - Sky Core Required Risk Capital (RRC) Dashboard](4eac2c9e-2718-4881-a3f1-ed10fb3f4d13). This core functionality is essential for the Prime Agent to proactively monitor its capital adequacy, identify potential or actual TRC shortfalls, and make timely operational and capital management decisions to maintain compliance.
4. Prime Agents' internal TRC management systems should define a RRC-incident (e.g., TRC shortfall) response protocol. The system should enable internal alerting mechanisms that detect when a Prime Agent’s TRC approaches predefined internal buffer thresholds relative to its Aggregate RRC. See [A.3.2.2.7.2.1.1.1 - Encumbrance Ratio](5435f680-aaaa-461a-bcae-4056bb8964d9). The system should also detect an actual shortfall where the Prime Agent’s held TRC falls below its Aggregate RRC. Furthermore, Prime Agent teams should establish and document internal processes for responding to such alerts. Such internal processes should include: 1) internal escalation and assessment of the shortfall’s cause and magnitude; 2) formulation of potential responses or corrective actions, which may include sourcing additional TRC, reducing risk-weighted exposures, or other measures; 3) internal decision-making framework for the evaluation of potential responses and selection of the most appropriate one; and 4) notifying any pertinent parties (Operational GovOps) as needed for the purpose of planning or implementing follow-up action.

Prime Agent teams' internal decision-making framework may consider the economic trade-offs of various actions, including the strategic acceptance of penalties for a TRC shortfall where such an approach is determined to be economically advantageous compared to immediate rebalancing (e.g., avoiding excessive transaction costs or market impact).

###### A.2.2.10.1.1.3.2.1.2.3 - Primes’ TRC Report [Core]  <!-- UUID: 41ca2085-d71b-47e5-8b1a-b183b6e2b6fc -->

Prime Agents are required to submit periodic Total Risk Capital (TRC) Reports to provide an accurate and verifiable attestation of their TRC composition and adherence to capital requirements.

###### A.2.2.10.1.1.3.2.1.2.3.1 - Mandate and Rationale [Core]  <!-- UUID: 7e95efa7-e409-48dc-9b5a-96edce54bf31 -->

Prime Agents are required to periodically submit TRC Reports to Core GovOps. This report serves a dual purpose. It provides a verifiable snapshot of the Prime Agent's TRC composition and key capital ratios as of the end of the reporting period; and second, it provides a formal attestation regarding the Prime Agent's maintenance of TRC at or above its dynamically changing Aggregate Required Risk Capital (RRC) throughout the entire reporting period. See [A.3.2.1.1.2 - Aggregate RRC](6aed5cc1-9671-4b73-88a9-fdd86ac93ece).

This comprehensive reporting, encompassing both an end-of-period statement and disclosures of any intra-period events affecting TRC, is essential. On-chain data alone (such as that captured by the planned OVRC system) cannot definitively prove the full eligibility and unimpaired availability of a Prime Agent's capital position for continuous RRC coverage, nor can it capture all off-chain factors. These factors include, but are not limited to, whether assets are subject to Prime-initiated off-chain contractual pledges, if the economic value or redeemability of its bridged assets is compromised by issues with their originating bridge, or if its assets are encumbered by derivative structures or other off-chain commitments that would impair their immediate use at any point during the period.

The TRC Report serves as an important basis for Core GovOps’ verification procedures. This entails: 1) reconciling reported end-of-period TRC components against the Sky Atlas, on-chain data, and other relevant sources to validate the period-end capital position and adherence to Atlas-defined capital requirements; and 2) reviewing Prime Agents’ attestations and disclosures regarding its TRC management and any material events throughout the reporting period to assess continuous compliance with its dynamically changing Aggregate RRC. The outcome of this validation is a critical input for the monthly settlement cycles, which latter includes the determination and retroactive application of penalties for any identified discrepancies or violations of capital requirements during the period.

The long-term vision is for the Powerhouse system to enable the automation of TRC data aggregation and verification. The Powerhouse system will have capabilities such as directly querying Prime Agent SubProxy accounts for IJRC assets, programmatically accessing and interpreting Ecosystem Accords recorded in the Atlas, interfacing with TEJRC and OSRC smart contract systems, and automatically applying Atlas-defined eligibility rules. See [A.2.2.10.1.1.3.2.1.3.1 - Continuous Monitoring Of On-chain Verifiable Risk Capital (OVRC)](8048bdf0-84b7-4546-8f1a-98b62d073c84). Even in this advanced state, the TRC Report, or a similar form of periodic attestation, may remain necessary to cover elements of TRC verification that are not fully able to be automated or require explicit Prime Agent declaration.

###### A.2.2.10.1.1.3.2.1.2.3.2 - TRC Report Contents [Core]  <!-- UUID: 4887e971-be6c-4f98-9137-7cdec3ed0fa0 -->

The Total Risk Capital (TRC) Report submitted by a Prime Agent must provide an accurate and verifiable breakdown of all TRC components held by the Prime Agent as of the end of the specified reporting period. The TRC Report should include the following essential information:

- Aggregate TRC Value As of End of Period: The total declared value in USD of all eligible TRC components held by the Prime Agent as of the end of the reporting period.
- Detailed Breakdown of TRC Components As of End of Period: For each category of TRC held, the report must detail the following values as of the end of the reporting period:
    - Internal Junior Risk Capital (IJRC): The total amount of IJRC, a breakdown of its constituent asset types, and their respective values in USD.
    - Prime-External Junior Risk Capital (PEJRC): The total amount of PEJRC. For each portion of PEJRC sourced from another Prime Agent, the report must include the amount in USD, the identifier of the counterparty Prime Agent, the expiry date of the arrangement, and a direct reference to the Ecosystem Accord that governs the PEJRC arrangement.
    - Tokenized External Junior Risk Capital (TEJRC): The total amount of TEJRC. For each TEJRC source, the report must include the amount in USD, the identifier of the TEJRC smart contract or facility and any relevant encumbrance identifier.
    - Originated Senior Risk Capital (OSRC): The total amount of OSRC. The report must specify the amount originated directly by the Prime Agent from the Total Senior Risk Capital (TSRC) pool and any amount of OSRC rented from other Prime Agents. For any rented OSRC, the report must include the amount in USD, the identifier of the counterparty Prime Agent, the expiry date, and a direct reference to the pertinent Ecosystem Accord.
    - Key Ratio Inputs and Computed Totals (Prime Internal Calculation) As Of End Of Period: Based on the component values reported above (as of the end of the reporting period), the report must include key figures used in and resulting from the Prime Agent's internal capital adequacy calculations. These figures reflect the capital structure and ratios as of the end of the reporting period and include:
        - Internal Junior Risk Capital (IJRC)
        - External Junior Risk Capital (EJRC) generated via External Per Internal Ratio (Prime External Junior Risk Capital + Tokenized External Junior Risk Capital sourced via the EPI ratio still carries Senior Per Junior or SPJ capacity)
        - EJRC-via-SPJ (sourced by spending SPJ capacity; zero-SPJ-capacity thereafter)
        - Enabled Senior Risk Capital (SRC)
        - Total Senior Per Junior capacity
            - Allocation of SPJ capacity to 1) enable SRC; or to 2) source EJRC
        - Prime-computed eligible Total Risk Capital (IJRC + EJRC-via-EPI + EJRC-via-SPJ + enabled SRC)
        - Official Aggregate RRC
        - Capital buffer = TRC – Aggregate RRC
        - Effective ratios
            - EPI = EJRC-via-EPI ÷ IJRC
            - SPJ utilisation:
                - enabled SRC ÷ total SPJ capacity
                - EJRC-via-SPJ ÷ total SPJ capacity
- Dynamic Period Attestation and Disclosures: In addition to the end-of-period snapshot figures, the TRC Report must include an Attestation from the Prime Agent confirming it maintained TRC at or above its Aggregate RRC at all times throughout the entire reporting period. In addition, the TRC Report must include disclosure of any events, Prime-initiated off-chain contractual obligations, impairments to the value or redeemability of held assets (such as RWA backing or bridged asset viability), encumbrances, or other conditions that occurred at any point during the reporting period which materially affected its TRC, even if such conditions were temporary or not continuously visible to on-chain monitoring systems. This disclosure must include the nature of the event/condition, its precise timing and duration, and its quantified impact on the Prime Agent's TRC.

###### A.2.2.10.1.1.3.2.1.3 - Sky Core TRC Monitoring And Verification Infrastructure [Core]  <!-- UUID: 18d692ce-7a5d-47a7-ada9-dc73abd87987 -->

The documents herein define infrastructure for TRC monitoring and verification.

###### A.2.2.10.1.1.3.2.1.3.1 - Continuous Monitoring Of On-chain Verifiable Risk Capital (OVRC) [Core]  <!-- UUID: 8048bdf0-84b7-4546-8f1a-98b62d073c84 -->

An autonomous monitoring system must be designed and implemented to enable continuous tracking of Prime Agents’ on-chain verifiable risk-capital components in near real-time. The on-chain, verifiable risk-capital components that can be tracked by such a monitoring system in real time are termed "On-chain Verifiable Risk Capital" (OVRC).

OVRC is not necessarily equivalent to Total Risk Capital (TRC). A Prime Agent’s actual TRC cannot be determined definitively without accounting for off-chain agreements, encumbrances or other relevant conditions affecting capital eligibility or availability, which conditions must be disclosed in the TRC Reports submitted by Prime Agents. See [A.2.2.10.1.1.3.2.1.2.3 - Primes’ TRC Report](41ca2085-d71b-47e5-8b1a-b183b6e2b6fc).

Where the OVRC of a Prime Agent is less than its Aggregate RRC, the shortfall will be logged and penalty accrual will commence on a pro-rata, per-second basis for the duration and magnitude of the observed shortfall, according to the penalty schedule defined in the Atlas. Thus, this on-chain monitoring system serves as an interim penalty ledger.

###### A.2.2.10.1.1.3.2.1.3.2 - Validation of TRC Report In General [Core]  <!-- UUID: 482fc286-9969-40cc-b3c9-6233ecbb659c -->

Prime Agents are required to submit periodic Total Risk Capital (TRC) Reports to Core GovOps. See [A.2.2.10.1.1.3.2.1.2.3 - Primes’ TRC Report](41ca2085-d71b-47e5-8b1a-b183b6e2b6fc). The protocol for validation of Primes’ TRC reports is defined in the documents herein.

###### A.2.2.10.1.1.3.2.1.3.2.1 - Core GovOps TRC Report Validation Process [Core]  <!-- UUID: 1ac3e606-f1c7-4a20-a9b6-a425920e98d3 -->

Core GovOps receives TRC Reports from Primes on a regular basis and must perform the following validation process.

Core GovOps verifies against the Atlas any Ecosystem Accord referenced in the TRC Report for sourced Prime-External Junior Risk Capital (PEJRC) or rented Originated Senior Risk Capital (OSRC). This includes confirming the existence, current validity, and terms of such Accords as formally recorded within the Atlas.

Core GovOps validates the Prime Agent's reported IJRC by reconciling the reported IJRC amount and its constituent asset composition against the actual on-chain state of the Prime Agent’s designated SubProxy account. This involves direct on-chain verification of asset balances. Core GovOps verifies that all assets reported as IJRC and held within the SubProxy account meet the definition of "eligible assets" for IJRC as defined by the Atlas. See [A.3.2.1.2.2.1.1.1 - Internal Junior Risk Capital (IJRC)](8728abee-0dc5-449b-b4c2-78698da16f10).

For reported Tokenized External Junior Risk Capital (TEJRC) and Originated Senior Risk Capital directly originated by the Prime, Core GovOps validates the reported amounts and statuses by cross-referencing data from the relevant smart contract systems. This may involve querying TEJRC pool contracts, OSRC auction records, and other on-chain infrastructure to confirm the existence, ownership, and eligibility of these capital components.

Core GovOps reviews all attestations and disclosures made by the Prime Agent in the TRC Report. This review focuses on understanding the Prime Agent's TRC compliance with Aggregate RRC throughout the entire reporting period. This assessment is critical for identifying intra-period shortfalls that might not be visible to on-chain monitoring systems or reflected in the end-of-period snapshot alone. The assessment process may include requiring the Prime Agent to provide supplementary documentation, verifiable evidence, or independent third-party confirmations for material off-chain claims or attestations concerning intra-period events; and/or cross-referencing disclosed off-chain information with relevant on-chain indicators or transactions that might corroborate or contradict the attestations.

Finally, Core GovOps independently calculates and verifies the Prime Agent's compliance with all Atlas-defined capital sourcing ratios (e.g., External Per Internal (EPI), Senior Per Junior (SPJ)).

###### A.2.2.10.1.1.3.2.1.3.3 - Finalized Determination Of TRC Position And Penalties [Core]  <!-- UUID: 36f3e675-d372-4d25-a50f-f0ba84a36273 -->

After reaching a definitive accounting of Prime Agents’ capital position and TRC adequacy, penalties are finalized by Core GovOps. This involves reconciling the interim penalty ledger (derived from the OVRC system) with the definitive TRC history, which incorporates all validated information from the TRC Report including any intra-period shortfalls.

1. If the validated TRC Report indicates that the Prime Agent's TRC was below its Aggregate RRC during the reporting period, and this actual shortfall was more severe than, or not detected by, the OVRC monitoring system, then penalties will be finalized as follows: if the OVRC system had already accrued penalties, these will be adjusted upwards to match the actual shortfall; if the OVRC system had not detected a shortfall, penalties will be assessed and applied retroactively based on the full duration and magnitude of the actual shortfall.
2. If the validated TRC Report confirms that TRC shortfalls were identical in duration and magnitude to those logged by the OVRC monitoring system throughout the reporting period: the penalties accrued in the interim penalty ledger will be confirmed and finalized.
3. If the validated TRC Report confirms that TRC was higher than a misleading OVRC reading during a specific portion of the reporting period which led to an erroneously logged penalty: Core GovOps will adjust or void the penalty accordingly.

###### A.2.2.10.1.1.3.2.1.4 - Risk-Capital Incident Response [Core]  <!-- UUID: 12b7d480-68a0-4493-9534-d6915f86c112 -->

Where a Prime Agent’s Allocation System Instances are operationalized by its Operational Executor Agent, the management of and response to Required Risk Capital (RRC)-related incidents requires a defined framework within each Prime Agent's Artifact (the Multi-Instance Coordinator Document for the Allocation System Primitive) and its associated Executor Accord.

While the Prime Agent's strategic team ("Prime Team") determines the specific rectification strategy for an RRC incident—considering its holistic portfolio, prevailing market conditions, and the potential for strategic acceptance of penalties—this discretion is exercised subject to the authority of Sky Core to impose penalties and take corrective measures, up to and including the conservatorship of a Prime Agent, to protect the ecosystem and make any losses whole.

This document will be developed further in a future iteration of the Atlas.

###### A.2.2.10.1.1.3.2.1.5 - Instance Operational Conformance [Core]  <!-- UUID: 1ec5f16f-194d-4163-b1ba-5c196ffa554b -->

Operational deviation from Artifact specifications can render an Instance’s RRC, and thus the Prime’s Aggregate RRC, invalid. Prime Agents must therefore ensure that each Allocation System Instance adheres to its respective Instance Configuration Document. Whether a Prime self-operationalizes its Allocation System or contracts with an Operational Executor Agent, its Agent Artifact must define processes for monitoring for, and addressing deviations of, Instance operational conformance. This document will be developed further in a future iteration of the Atlas.

###### A.2.2.10.1.1.3.2.2 - Asset Liability Management [Core]  <!-- UUID: ed10830e-6b17-4117-8ab4-5ea388b518bb -->

Requirements and infrastructure related to Asset Liability Management shall be defined in a future iteration of the Atlas.

###### A.2.2.10.1.1.3.3 - Allocation Instance Adjustments, Scaling, And Settlement [Core]  <!-- UUID: 93bfb0f9-d662-467d-b8bc-ef585e5b081e -->

On an ongoing basis, the Prime Agent team or Operational GovOps operates the Allocation Instance, scaling exposure up and down. Any change to the Allocation Instance outside of the limits specified in the Prime Agent Artifact or requiring judgment on the part of Operational GovOps (where the Allocation System Instance is operationalized by the Operational Executor Agent) requires a new vote of Prime Agent token holders. See [A.2.2.10.1.1.3.3.1 - Modification Of Existing Instances](c1b5708c-e88f-45e0-92e1-b76e68b34f13). As part of monthly and quarterly settlement cycles, Core GovOps reviews yields and obligations, applying penalties retroactively for any previously undisclosed violations. In the event of any such violations, Operational GovOps may be required to take escalatory steps based on the fallback strategy in the Prime Agent Artifact.

###### A.2.2.10.1.1.3.3.1 - Modification Of Existing Instances [Core]  <!-- UUID: c1b5708c-e88f-45e0-92e1-b76e68b34f13 -->

When a Prime Agent wishes to modify an existing Allocation System Primitive Instance in a manner that cannot be accommodated by the existing operational parameters defined in its Agent Artifact, the Prime Agent must initiate an Artifact Edit Proposal process as detailed herein.

###### A.2.2.10.1.1.3.3.1.1 - Conditions Requiring Artifact Edit Proposal [Core]  <!-- UUID: 3db4c73f-f480-4da4-9af3-8ecedd89e166 -->

An Artifact Edit Proposal is mandatory for an Instance modification under the following conditions:

1. a desired modification to the Instance's operational parameters falls outside the pre-defined operational ranges codified in the respective Instance Configuration Document or other applicable Artifact Documents; or
2. a desired modification, even if notionally within defined ranges in the Artifact, is determined by Operational GovOps to materially alter the Instance's risk profile in a way that could invalidate the underlying Capital and Operational Plan and, consequently, the premises driving the current Required Risk Capital (RRC) for that Instance. Operational GovOps retains the discretion to require an Artifact Edit Proposal if a proposed change, regardless of its fit within existing operational ranges, is determined to pose a material change to the assessed risk.

###### A.2.2.10.1.1.3.3.1.2 - Revision of Capital and Operational Plan for Instance Modification [Core]  <!-- UUID: 235a7317-ef29-48ed-a37f-5892108f8dc8 -->

Prior to submitting an Artifact Edit Proposal for an Instance modification, the Prime Agent must revise the Capital and Operational Plan (C&O Plan) associated with that Instance to reflect the desired new state.

The revised Capital and Operational Plan for an Instance modification must include the following information:

1. Updates to the Instance's strategy and operational parameters;
2. A new pro-forma Required Risk Capital (RRC) estimate specifically calculated to reflect the Instance's proposed modified state; and
3. A revised notional Total Risk Capital (TRC) coverage strategy, detailing how the Prime Agent will manage any changes to the Instance RRC and the consequential impact on its Aggregate RRC, including plans for acquiring additional JRC or SRC if necessary.

###### A.2.2.10.1.1.3.3.1.3 - Governance Process for Instance Modification [Core]  <!-- UUID: aee1d848-eee8-4590-a596-1884efcb474a -->

The Prime Agent's revised Capital and Operational Plan forms the core of the Artifact Edit Proposal for the Instance modification. This proposal must be submitted to the Operational Executor Facilitator for review. The Facilitator assesses the proposal for completeness and general alignment. Following this review, the proposal is subjected to the Prime Agent's governance process for approval to edit the Agent Artifact, typically involving a token holder vote as defined in the Prime Agent's Root Edit Primitive.

###### A.2.2.10.1.1.3.3.1.4 - Post-Approval Integration and RRC Update [Core]  <!-- UUID: e3a00c33-9da7-4fa9-80ff-55d3a70100fa -->

If the Artifact Edit Proposal for the Instance modification is approved through the Prime Agent’s governance process, the relevant content from the revised Capital and Operational Plan is formally integrated into the respective Instance Configuration Document within the Prime Agent's Artifact.

Once the modified Instance is operational under its new, approved parameters and its data is integrated into the ecosystem’s monitoring systems, its adjusted Required Risk Capital (RRC) will be officially determined and tracked via the Sky Core RRC Dashboard. This official RRC figure then supersedes the Prime-prepared pro-forma RRC that was part of the modification proposal.

##### A.2.2.10.1.2 - Allocation System Input Requirements [Core]  <!-- UUID: b6ccdee2-a5e4-4d63-9af5-60b8163673af -->

The documents herein define the required inputs for a valid Invocation of the Allocation System Primitive. If any input is noncompliant or omitted, the Primitive will be invalidated and the Allocation Instance deployment will not move forward.

###### A.2.2.10.1.2.1 - Global Activation Status [Core]  <!-- UUID: 5a9cf81d-19dd-4f75-9ddc-be35c6b5cfb5 -->

The Allocation System Primitive must be Globally Activated.

###### A.2.2.10.1.2.2 - Core Allocation Vault Address [Core]  <!-- UUID: 4655b643-b03f-49b7-a474-493c3e059b62 -->

The Prime Agent Artifact must specify the address of the Prime Agent’s Core Allocation Vault.

###### A.2.2.10.1.2.3 - Core Allocation Buffer Address [Core]  <!-- UUID: 2cdb447e-ebf5-4e57-a722-181178fbe80f -->

The Prime Agent Artifact must specify the address of the Prime Agent’s Core Allocation Buffer.

###### A.2.2.10.1.2.4 - Allocation System Core Security Parameters [Core]  <!-- UUID: 9c5e2e23-7756-4856-951b-0bcbecaa867d -->

The Prime Agent Artifact must specify the rate limiters for the Allocation Vault and Core Allocation Buffer, including the address and parameters for each.

###### A.2.2.10.1.2.5 - Capital Faucet [Core]  <!-- UUID: 4b8cf927-d5e3-4e5b-8626-62523fb286be -->

The Prime Agent Artifact must specify the address of the Prime Agent’s Capital Faucet and its rate limits.

###### A.2.2.10.1.2.6 - List Of Allocation Instances [Core]  <!-- UUID: e4975062-6d19-438b-a5d5-cfc1a7fd8cb9 -->

If the Allocation System Primitive is Activated, then the Prime Agent Artifact must list each active Allocation Instance, grouped by blockchain. For each blockchain, the Prime Agent Artifact must specify: (1) the name of the blockchain, (2) the bridging mechanism for the blockchain, if any, (3) the allocation buffer on the blockchain, and (4) the Allocation Instances on the blockchain. For each Allocation Instance, the Prime Agent Artifact must contain the information specified herein.

###### A.2.2.10.1.2.6.1 - Required Allocation Instance Parameters [Core]  <!-- UUID: 6ad0fdb4-bd11-4d5a-a436-0d106873e0ec -->

For each Allocation Instance, the Prime Agent Artifact must specify: (1) the name of the Allocation Instance, (2) the address of the Allocation Instance, (3) the rate limit of the conduit for inflows and outflows, (4) any other technical parameters of the Allocation Instance (e.g. maximum slippage, oracles used), (5) data submission protocols, and (6) specification of emergency measures that can be used by Operational GovOps if Required Risk Capital or Asset Liability Management obligations are breached.

###### A.2.2.10.1.2.6.2 - Required Allocation Instance Allocation Strategy [Core]  <!-- UUID: 0e4a5264-1365-4e5c-9be4-dac85ed6b46b -->

For each Allocation Instance, the Prime Agent Artifact must specify the strategy documents contained herein. These strategy documents must describe in detail how the Allocation Instance should be operated so that the Operational Executor Agent that the Prime Agent has contracted with can operate the Allocation Instance without further input from the Prime Agent or having to make "judgment calls". To the extent that the Prime Agent’s strategy cuts across different Allocation Instances, the Prime Agent may include a single set of strategy documents covering all Allocation Instances.

###### A.2.2.10.1.2.6.2.1 - Required Allocation Instance Asset Liability Management Strategy [Core]  <!-- UUID: 3f48dff7-3bf1-44d2-a92f-531ce42be318 -->

The allocation strategy for each Allocation Instance should specify how Operational GovOps should adjust the amount of funds allocated to the Conduit based on performance, market conditions, or other factors. It should also specify limits to the amount by which the allocation can be adjusted before a vote of Prime Agent token holders is required.

###### A.2.2.10.1.2.6.2.2 - Required Allocation Conduit Asset Liability Management Strategy [Core]  <!-- UUID: 2cdd38d7-7f85-411b-854e-5768d564c275 -->

The asset liability management strategy for each Allocation Instance must specify what steps Operational GovOps should take to ensure that the Prime Agent continues to satisfy its Asset Liability Management obligations as the amount of funds allocated to the Conduit changes.

###### A.2.2.10.1.2.6.2.3 - Required Allocation Instance Fallback Strategy [Core]  <!-- UUID: 4363d9c4-afb3-44d1-a72a-9edbd40d415e -->

The fallback strategy for each Allocation Instance must specify how Operational GovOps should determine when an emergency situation is occurring regarding the Allocation Instance and what actions it should take to protect the Prime Agent from losses associated with the Allocation Instance. The fallback strategy must include emergency measures for Operational GovOps to reduce exposure to, drain, and ultimately shut down the Allocation Instance if Required Risk Capital or Asset Liability Management obligations are breached.

#### A.2.2.10.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: d8086dc0-7e77-4c6b-98c7-5fc41337a1ce -->

The Risk Capital Rental Primitive is a mechanism enabling Prime Agents to rapidly rent Risk Capital from each other, ensuring that capital gets deployed to where the best opportunities are. The Primitive facilitates the rental of both Junior Risk Capital, as specified in [A.3.2.1.2.2.1.1.2 - Prime-External Junior Risk Capital (PEJRC)](00f61aa6-7bb4-4c7f-9492-2e2b2b4e78b2), and Originated Senior Risk Capital, as specified in [A.3.2.2.4.4 - Originated Senior Risk Capital (OSRC) Rental Implementation](268b4b1f-9a19-42f8-b7c6-d8dc01e32517).

#### A.2.2.10.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c -->

The Asset Liability Management Rental Primitive is a mechanism enabling Prime Agents to trade Asset Liability Management obligations between each other, providing more flexibility in how capital is deployed through the Allocation System and reducing duplicate work.

### A.2.2.11 - Core Governance Primitives [Section]  <!-- UUID: 6fa54611-c744-4b9d-897d-b2a20e9cae5d -->

Core Governance Primitives allow Prime Agents to earn incentives for maintaining and securing Sky Governance frontends as well as borrow from the Smart Burn Engine.

#### A.2.2.11.1 - Core Governance Reward Primitive [Core]  <!-- UUID: b22d1c08-042a-4466-94fe-9d28951e4d4a -->

The Core Governance Reward Primitive is a reward that Sky pays to Prime Agents that provide SKY holders with secure access to the core Sky Governance features, ensuring that the Governance Security of Sky is maintained over time.

##### A.2.2.11.1.1 - Reward Pool [Core]  <!-- UUID: 111bedd1-35aa-4c72-91e1-963550d909bf -->

The total reward pool for the Core Governance Reward Primitive is 1% of the Net Revenue of Sky, funded out of the Core Council Allocation (see [A.2.3.1.2.2.2 - Core Council Allocation](91b281c2-0687-45a3-939d-0480c7c33f9f)). These rewards are paid to the Prime Agent that manages the relationship with each eligible Integrator, with sharing subject to bilateral negotiation as specified in [A.2.2.4.2 - Reward Recipient And Sharing](40395562-d447-4c85-b670-c08d2341bcd2).

##### A.2.2.11.1.2 - Eligible Recipients [Core]  <!-- UUID: a59cee2a-864e-4dbb-9364-bdf121573cb2 -->

In order for an Integrator and the Prime Agent that manages the relationship with such Integrator to be eligible for the Core Governance Reward, the frontend maintained by the Integrator must satisfy compliance requirements as specified in [A.2.2.11.1.3 - Compliance Requirements](068c37b5-2cda-4bcc-90af-7b70c746dbc3).

The current eligible recipients for the Core Governance Reward Primitive are specified in the documents herein.

###### A.2.2.11.1.2.1 - Current Eligible Recipients [Core]  <!-- UUID: e8272862-e80d-470c-a0da-f964b6df110d -->

The current eligible recipients for the Core Governance Reward Primitive are:

- **Skybase** - Skybase is eligible to receive the Core Governance Reward with respect to the [https://sky.money/](https://sky.money/) frontend.

##### A.2.2.11.1.3 - Compliance Requirements [Core]  <!-- UUID: 068c37b5-2cda-4bcc-90af-7b70c746dbc3 -->

Security and information standards for compliant frontends are specified in the documents herein.

###### A.2.2.11.1.3.1 - Security Standards [Core]  <!-- UUID: a6ab8a87-bd53-4227-9ede-1dd65094989c -->

Specific security standards for compliant frontends will be specified in a future iteration of the Atlas.

###### A.2.2.11.1.3.2 - Information Standards [Core]  <!-- UUID: 6c53d0a0-f5ce-4005-a887-6f94b08e4a28 -->

Specific information and disclosure standards for compliant frontends will be specified in a future iteration of the Atlas.

##### A.2.2.11.1.4 - Distribution Mechanism [Core]  <!-- UUID: 72ce2c27-6d72-4b64-8a3c-083be9fe7659 -->

The documents herein define how the total reward pool is distributed to individual recipients.

###### A.2.2.11.1.4.1 - Integration With Treasury Management Function [Core]  <!-- UUID: dc825d62-60cf-4701-ac8f-b48257b4f9a6 -->

Distributions of Core Governance Rewards are made on a monthly basis as part of the Treasury Management Function.

###### A.2.2.11.1.4.2 - Allocation Based On Staked SKY [Core]  <!-- UUID: f8d35814-d8bb-423f-97ce-35629bcc7a5e -->

Each Prime Agent is allocated a share of the Core Governance Reward proportional to the SKY staked through eligible frontends maintained by the Integrators it manages. The Prime Agent may share a portion of this reward with those Integrators, as specified in [A.2.2.4.2 - Reward Recipient And Sharing](40395562-d447-4c85-b670-c08d2341bcd2).

###### A.2.2.11.1.4.2.1 - Tracking Via Reward Codes [Core]  <!-- UUID: b16cb8a3-aea3-4fda-b904-eb782ea7a8e1 -->

The amount of SKY staked through each eligible frontend is tracked using Reward Codes. Eligible frontends pass a Reward Code identifying the Integrator and associated Prime Agent when users stake SKY. Each eligible Integrator is assigned a unique Reward Code by Operational GovOps for the Prime Agent managing the relationship with the Integrator. Reward Codes for each Integrator are recorded in the associated Instance of the Core Governance Reward Primitive in the Agent Artifact of the Prime Agent managing the relationship with the Integrator.

##### A.2.2.11.1.5 - Retroactive Effectiveness [Core]  <!-- UUID: b3f97303-4d41-497c-b931-9337c518bd7e -->

The allocations to the Core Governance Reward Primitive are effective retroactive to May 19, 2025. Amounts accrued and not yet disbursed are funded out of the Core Council Buffer (see [A.2.3.1.2.2.2.1 - Core Council Buffer](8b6781d7-f35c-4ffe-b8ed-299fa98e3da7)).

## A.2.3 - Treasury Management [Article]  <!-- UUID: 6c0af059-5d33-4e2b-90f1-1606957b8f85 -->

The Sky Treasury Management Function defines how all Net Revenue of the Sky Protocol is distributed among various downstream functions or buffers. This ensures that all necessary functions are adequately funded, allowing all actors to focus on growing the ecosystem in a positive sum way.

### A.2.3.1 - Treasury Management [Section]  <!-- UUID: 9bd2f02c-8111-4431-9b3a-46d3695af1e1 -->

The documents herein define the Sky Treasury Management Function.

#### A.2.3.1.1 - Integration With Monthly Settlement Cycle [Core]  <!-- UUID: 6e187fc0-6e5a-4384-b0b6-cdfd87a7d400 -->

The Sky Treasury Management Function is synchronized with the Monthly Settlement Cycle. See [A.2.4 - Sky Core Monthly Settlement Cycle](6f8d5065-d6ff-4add-9a28-eadeffa7ed1a). At the conclusion of each MSC, the Net Revenue of the Sky Protocol for the preceding month is calculated and allocated according to the waterfall process defined in [A.2.3.1.2 - Allocation Steps](7932c8f3-ce44-49ea-adc4-f6391c621c6e).

#### A.2.3.1.2 - Allocation Steps [Core]  <!-- UUID: 7932c8f3-ce44-49ea-adc4-f6391c621c6e -->

The documents herein define the allocation steps of the Sky Treasury Management Function. The process is divided into steps beginning with Net Revenue. These steps form a "waterfall" with each previous step needing to be fully funded before any funds can be allocated to later steps.

##### A.2.3.1.2.1 - Step 0: Net Revenue [Core]  <!-- UUID: c09435ff-d876-442a-899c-ad494175500b -->

The sole function of Step 0 is to establish the Net Revenue of the Sky Protocol. It performs no allocations to downstream functions or buffers, unlike subsequent steps for which this Net Revenue serves as the input.

All items of Income and Expense are recognized on a "cash basis" based on when USDS/DAI enter or leave the Sky Surplus Buffer. Transfers out of accounts other than the Sky Surplus Buffer are not recognized as Expenses, except as provided in [A.2.3.1.2.2.2.1.6.4 - Expense Recognition For Legacy Account Consolidation](1760b35f-da5a-4504-a014-dd7a611b4c0e).

###### A.2.3.1.2.1.1 - Net Revenue [Core]  <!-- UUID: bddce7bf-c568-444b-b196-e15a99016696 -->

Net Revenue is equal to Income minus Expenses. Income is defined in [A.2.3.1.2.1.2 - Income](a0fab275-399d-41ad-a9b0-411d3e5ea5c9). Expenses are defined in [A.2.3.1.2.1.3 - Expenses](88e3c367-fe30-4d59-8ba1-eddc0d88a0ea). Income and Expenses are defined such that Net Revenue must always be positive

###### A.2.3.1.2.1.2 - Income [Core]  <!-- UUID: a0fab275-399d-41ad-a9b0-411d3e5ea5c9 -->

The documents herein define each of the components of the Income of the Sky Protocol. These components are added together to arrive at total Income.

###### A.2.3.1.2.1.2.1 - Stability Fees From Base Rate [Core]  <!-- UUID: 13d342a7-e9cf-4fb2-afc1-a1dd36c47054 -->

Stability Fees are the fees that Sky Core charges Prime Agents to borrow from Sky. See [A.3.1.2.1 - Base Rate](228f9955-6bba-4252-a101-5529e7a300b9). Sky Core’s legacy ALM infrastructure is currently being transferred to Prime Agents; during this transition period and until this transfer is fully complete, income generated from the Sky Core Collateral Portfolio contributes to net revenue. See [A.3.3.1.4 - Application To Sky Core](6e050b66-0bc8-43f1-b32d-2220c9df466b).

###### A.2.3.1.2.1.2.2 - Internal Senior Risk Capital Income [Core]  <!-- UUID: 02b5422a-093d-4e21-86ff-5cfcd5af8ed5 -->

Internal Senior Risk Capital income is the revenue attributed to Sky from the total payments made by Primes for Originated Senior Risk Capital (OSRC). ISRC itself is sourced from Aggregate Backstop Capital, as specified in [A.2.3.1.3 - Sourcing Of Internal Senior Risk Capital](ac7a6636-acbc-40c9-abc1-4543c0beb300). While Primes pay a single clearing price for their OSRC based on the monthly Origination Process, the total revenue received by Sky is subsequently allocated proportionally, with the portion corresponding to ISRC's share of the Total Senior Risk Capital (TSRC) pool designated as ISRC Income.

###### A.2.3.1.2.1.2.3 - External Senior Risk Capital Fees [Core]  <!-- UUID: f01ce2f4-6bbe-4d70-8b22-edb80d8fb624 -->

External Senior Risk Capital Fees are levied by Sky and calculated as 5% of the net interest earnings generated by the External Senior Risk Capital (ESRC) pool each Monthly Settlement Cycle. These earnings represent the portion of the total revenue from Primes' Originated Senior Risk Capital (OSRC) payments that is attributed proportionally to ESRC, based on its contribution to the Total Senior Risk Capital (TSRC) pool for that cycle. This 5% fee is deducted before the remaining ESRC earnings contribute to the srUSDS conversion rate. See [A.3.2.2.4.2.3.3.2 - ESRC Earnings Fee](559f6fb6-daf6-41b2-9882-53a91aaf132f).

###### A.2.3.1.2.1.2.4 - Agent Upkeep Fees [Core]  <!-- UUID: c650b38c-aa7c-42b4-94ed-6320238b0264 -->

Agent Upkeep Fees are fees paid by Agents to contribute to the long-term sustainability of the Sky Ecosystem. See [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

###### A.2.3.1.2.1.2.5 - Agent Creation Fees [Core]  <!-- UUID: 1b1c9cc0-e410-4bb3-aa37-c639ca392dd7 -->

Agent Creation Fees are one-time payments collected from founding teams when establishing new Prime Agents. See [A.2.2.3.1.2 - Creation Fee](708ad6b6-8e4a-46b3-9848-523d00a57420).

###### A.2.3.1.2.1.2.6 - Other Income [Core]  <!-- UUID: aebc1c92-6538-4a1c-a90c-4928d9924eeb -->

Other Income includes all sources of income of the Sky Protocol not identified in the other subdocuments of [A.2.3.1.2.1.2 - Income](a0fab275-399d-41ad-a9b0-411d3e5ea5c9), including, without limitation, the sources of income specified in the documents herein.

###### A.2.3.1.2.1.2.6.1 - Sky Core Vault Income [Core]  <!-- UUID: 4a3e1d4d-a1d7-4207-9af8-fa0fd195a929 -->

Sky Core Vault Income is all income from Sky Core Vaults, including, without limitation, liquidation penalties. Sky Core Vaults include, without limitation, (1) all Sky Core Vaults specified in [A.3.7.1.1.1 - Vault Types](64971463-0650-4462-b9c4-1eecb704fa1a) and (2) the Sky Core Vault associated with SKY-Backed Borrowing (see [A.4.4.1.3 - SKY-Backed Borrowing](264b1787-cd75-4d28-9c14-c7d5a724eba7)).

###### A.2.3.1.2.1.2.6.2 - LitePSM Income [Core]  <!-- UUID: edb32ca7-329f-437b-bf02-2bf0e78e7ea7 -->

LitePSM Income is all income from the LitePSM.

###### A.2.3.1.2.1.3 - Expenses [Core]  <!-- UUID: 88e3c367-fe30-4d59-8ba1-eddc0d88a0ea -->

The documents herein define each of the components of Expenses. These components are added together to arrive at total Expenses.

###### A.2.3.1.2.1.3.1 - Sky Savings Rate Paid To sUSDS Holders [Core]  <!-- UUID: e6b86b0e-163d-4be4-928d-a81dd6700d57 -->

The Sky Savings Rate is the interest expense paid to sUSDS holders on their balances. It also includes all other savings-related expenses (other than those paid through the Integration Boost), such as the Dai Savings Rate expense and interest on stUSDS.

###### A.2.3.1.2.1.3.2 - Sky Savings Rate Paid Through Integration Boost [Core]  <!-- UUID: feb95aa7-e1b1-4ba8-a9a5-f99b5a21477e -->

The Integration Boost is intended to provide the equivalent of the Sky Savings Rate to users of decentralized finance protocols who hold USDS balances. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

###### A.2.3.1.2.1.3.3 - Distribution Rewards [Core]  <!-- UUID: 2177f303-a0a7-4807-b815-d17aa76a264e -->

The Distribution Reward is paid to Prime Agents that drive adoption of USDS. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

###### A.2.3.1.2.1.3.4 - Reimbursement Rewards [Core]  <!-- UUID: 3aa5b01e-6661-4b01-b32c-ea7b02fbedcb -->

Reimbursement Rewards are paid to Prime Agents to reimburse them for the costs of building common infrastructure used by the entire Sky Ecosystem, such as Token SkyLink deployments.

###### A.2.3.1.2.1.3.5 - Pioneer Rewards [Core]  <!-- UUID: 33c56bad-c422-48f4-bcca-dc8794c6a0da -->

Pioneer Rewards are paid to Pioneer Primes as specified in [A.2.2.9.3.1.4 - Pioneer Incentive Pool](04edac33-19d5-4a87-a8ab-945a0cd57771).

##### A.2.3.1.2.2 - Step 1: Security And Maintenance [Core]  <!-- UUID: 324e9d22-70fe-4e44-82ab-118815f5c42e -->

All of the Net Revenue from Step 0 (see [A.2.3.1.2.1.1 - Net Revenue](bddce7bf-c568-444b-b196-e15a99016696)) becomes Step 1 Capital. Twenty percent (20%) of Step 1 Capital is allocated for security and maintenance of the Sky Ecosystem as specified in the documents herein. The remaining eighty percent (80%) of Step 1 Capital becomes Step 2 Capital and is allocated as specified in [A.2.3.1.2.3 - Step 2: Aggregate Backstop Capital](2b28d464-e683-48ba-9a66-2fee05ea0a88).

###### A.2.3.1.2.2.1 - Fortification Foundation Allocation [Core]  <!-- UUID: 728ea3d3-606a-4080-bc56-4a9e2c7fecb3 -->

Ten percent (10%) of Step 1 Capital is allocated to the Fortification Foundation, covering legal defense, resilience, and unquantifiable risk management. See [A.2.13.1.2 - Fortification Foundation Grants](ec2ebbba-6944-44cb-a04d-4572c6bea1e7). Until the Fortification Foundation is fully operational, this allocation may be directed to the Sky Frontier Foundation on an interim basis to support protocol development and growth.

###### A.2.3.1.2.2.2 - Core Council Allocation [Core]  <!-- UUID: 91b281c2-0687-45a3-939d-0480c7c33f9f -->

Ten percent (10%) of Step 1 Capital is allocated to the Core Council, which directs these funds across governance operations and development work. This allocation funds, without limitation, active Core Executor Agents, Core Executor Agents whose terms have ended in the last four (4) years, Aligned Delegates, the Core Governance Reward Primitive (see [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a)), and grants to the Sky Frontier Foundation (see [A.2.13.1.1 - Sky Frontier Foundation Grants](1f5d9b2d-d94d-4945-bcf5-74b9152de90c)). At the discretion of the Core Council, funds may be allocated to pay these recipients directly or to fund the Core Council Buffer (see [A.2.3.1.2.2.2.1 - Core Council Buffer](8b6781d7-f35c-4ffe-b8ed-299fa98e3da7)) and Aligned Delegates Buffer (see [A.2.3.1.2.2.2.2 - Aligned Delegates Buffer](05fa5c41-26ca-4c25-94dd-834ef72c318a)) for subsequent disbursement.

The Core Council is authorized to direct grants from this allocation to the Sky Frontier Foundation without a separate governance decision for each grant.

The specific allocation among the components of the Core Council Allocation, including the mechanism by which Core Executor Agents are elected to Core Executor Slots, will be specified in a future iteration of the Atlas.

###### A.2.3.1.2.2.2.1 - Core Council Buffer [Core]  <!-- UUID: 8b6781d7-f35c-4ffe-b8ed-299fa98e3da7 -->

The Core Council Buffer is a multisig used to transfer funds on behalf of the Core Council.

###### A.2.3.1.2.2.2.1.1 - Core Council Buffer Multisig Address [Core]  <!-- UUID: af082bd0-fdcd-4ec1-980a-7fce50e77ed1 -->

The address of the Core Council Buffer Multisig on the Ethereum Mainnet is `0x210CFcF53d1f9648C1c4dcaEE677f0Cb06914364`.

###### A.2.3.1.2.2.2.1.2 - Core Council Buffer Multisig Required Number Of Signers [Core]  <!-- UUID: 7f9cc28d-75af-4fe0-b090-8c85cda9656a -->

The Core Council Buffer Multisig has a 5/6 signing requirement.

###### A.2.3.1.2.2.2.1.3 - Core Council Buffer Multisig Signers [Core]  <!-- UUID: 5aeba17d-3869-447d-adcd-8c55f41afc01 -->

The signers of the Core Council Buffer Multisig are two (2) addresses controlled by the Core Facilitator, three (3) addresses controlled by Core GovOps, and one (1) address controlled by Operational GovOps Soter Labs.

###### A.2.3.1.2.2.2.1.4 - Core Council Buffer Multisig Usage Standards [Core]  <!-- UUID: dc6474f6-d285-4e1e-9902-406def4b72be -->

The signers must use the Core Council Buffer Multisig to disburse funds on behalf of the Core Council.

###### A.2.3.1.2.2.2.1.5 - Core Council Buffer Multisig Modification [Core]  <!-- UUID: a56fe3ee-c11a-4df0-9cc3-677688c5563d -->

The signers can change the signers of the Core Council Buffer Multisig so long as:

- there are exactly six (6) signers;
- exactly five (5) signers are required to execute transactions; and
- two (2) signers are controlled by the Core Facilitator, three (3) signers are controlled by Core GovOps, and one (1) signer is controlled by Operational GovOps Soter Labs.

###### A.2.3.1.2.2.2.1.6 - Consolidation Of Funds From Legacy Accounts [Core]  <!-- UUID: 8c8778c4-ff4c-4add-ae03-5f32a052f433 -->

All funds in Legacy Accounts (see [A.2.3.1.2.2.2.1.6.1 - Legacy Accounts](6f7153e1-c535-4a35-a7cf-7a66180a1c0e)) must be consolidated into the Core Council Buffer or the Demand Side Buffer (see [A.2.2.4.3 - Demand Side Buffer](862b6d83-f464-4125-8259-233b7de75ec4)) as specified in the documents herein.

###### A.2.3.1.2.2.2.1.6.1 - Legacy Accounts [Core]  <!-- UUID: 6f7153e1-c535-4a35-a7cf-7a66180a1c0e -->

Legacy Accounts are all accounts controlled by Sky Core, with the exception of the Core Council Buffer, the Aligned Delegates Buffer (see [A.2.3.1.2.2.2.2 - Aligned Delegates Buffer](05fa5c41-26ca-4c25-94dd-834ef72c318a)), and the Demand Side Buffer and its auxiliary accounts (see [A.2.2.4.3 - Demand Side Buffer](862b6d83-f464-4125-8259-233b7de75ec4)). This includes, without limitation:

- the former Distribution Reward Controller Wallet;
- the former Integration Boost Wallets; and
- the Sky Ecosystem Liquidity Bootstrapping Budget.

###### A.2.3.1.2.2.2.1.6.2 - Ecosystem Actors Must Consolidate All Funds From Legacy Accounts [Core]  <!-- UUID: 294154f2-8d36-4104-a660-89a7b52eeac7 -->

Relevant Ecosystem Actors must take all necessary actions to transfer all funds from Legacy Accounts into the Core Council Buffer or the Demand Side Buffer (see [A.2.2.4.3 - Demand Side Buffer](862b6d83-f464-4125-8259-233b7de75ec4)).

###### A.2.3.1.2.2.2.1.6.3 - Legacy Accounts Are Replaced [Core]  <!-- UUID: fae8cff1-5ecc-4f4f-a4e1-622df4112eeb -->

All funds that would otherwise be transferred into or out of Legacy Accounts must instead be transferred into or out of the Core Council Buffer or the Demand Side Buffer (see [A.2.2.4.3 - Demand Side Buffer](862b6d83-f464-4125-8259-233b7de75ec4)).

###### A.2.3.1.2.2.2.1.6.4 - Expense Recognition For Legacy Account Consolidation [Core]  <!-- UUID: 1760b35f-da5a-4504-a014-dd7a611b4c0e -->

The consolidation of funds from Legacy Accounts into the Core Council Buffer or the Demand Side Buffer (see [A.2.2.4.3 - Demand Side Buffer](862b6d83-f464-4125-8259-233b7de75ec4)) is recognized as a one-time expense for purposes of [A.2.3.1.2.1 - Step 0: Net Revenue](c09435ff-d876-442a-899c-ad494175500b). This achieves the same result as if the funds in Legacy Accounts had been returned to the Sky Surplus Buffer and subsequently transferred to the relevant downstream account.

###### A.2.3.1.2.2.2.2 - Aligned Delegates Buffer [Core]  <!-- UUID: 05fa5c41-26ca-4c25-94dd-834ef72c318a -->

The Aligned Delegates Buffer is a multisig controlled by the Core Facilitator and Core GovOps to transfer funds to Aligned Delegates.

###### A.2.3.1.2.2.2.2.1 - Aligned Delegates Buffer Multisig Address [Core]  <!-- UUID: 744ffdce-188e-403a-a0f4-532a27879cf5 -->

The address of the Aligned Delegates Buffer Multisig on the Ethereum Mainnet is `0x37FC5d447c8c54326C62b697f674c93eaD2A93A3`.

###### A.2.3.1.2.2.2.2.2 - Aligned Delegates Buffer Multisig Required Number Of Signers [Core]  <!-- UUID: b3672c98-07ca-488f-8a26-461bf8d14aae -->

The Aligned Delegates Buffer Multisig has a 3/4 signing requirement.

###### A.2.3.1.2.2.2.2.3 - Aligned Delegates Buffer Multisig Signers [Core]  <!-- UUID: f0652394-ec87-4b08-abed-e15fd0799ab1 -->

The signers of the Aligned Delegates Buffer Multisig are two (2) addresses controlled by the Core Facilitator and two (2) addresses controlled by Core GovOps.

###### A.2.3.1.2.2.2.2.4 - Aligned Delegates Buffer Multisig Usage Standards [Core]  <!-- UUID: 3ce8a599-f70b-4dad-9d71-a69d812c4ea8 -->

The Core Facilitator and Core GovOps must use the Aligned Delegates Buffer Multisig to disburse funds to Aligned Delegates.

###### A.2.3.1.2.2.2.2.5 - Aligned Delegates Buffer Multisig Modification [Core]  <!-- UUID: b8b38333-2763-47e1-9e34-0b37c750201a -->

The Core Facilitator and Core GovOps can change the signers of the Aligned Delegates Buffer Multisig so long as:

- there are at least four (4) signers;
- a majority of signers are required to execute transactions; and
- an equal number of signers are controlled by the Core Facilitator and Core GovOps.

##### A.2.3.1.2.3 - Step 2: Aggregate Backstop Capital [Core]  <!-- UUID: 2b28d464-e683-48ba-9a66-2fee05ea0a88 -->

Step 1 Capital that remains after the Step 1 allocation becomes Step 2 Capital.

The allocation of Step 2 Capital depends on the level of Aggregate Backstop Capital (see [A.3.5.3.1.2 - Aggregate Backstop Capital](6dbead44-5ac4-4c5b-be3c-64eddd004e5c)) relative to the Turbo-Fill Floor (see [A.3.5.3.2.2 - Turbo-Fill Floor](db2aaf07-4ebb-4e5d-ae5e-575717d8fbcd)) and the Target Aggregate Backstop Capital (see [A.3.5.3.2.1 - Target Aggregate Backstop Capital](f73dda95-0b1c-4bdc-b957-469253d27281)).

When Aggregate Backstop Capital is below the Turbo-Fill Floor, fifty percent (50%) of Step 2 Capital is retained to grow Aggregate Backstop Capital. The remainder of Step 2 Capital becomes Step 3 Capital and is allocated as specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121).

When Aggregate Backstop Capital is at or above the Turbo-Fill Floor and below the Target Aggregate Backstop Capital, the portion of Step 2 Capital retained to grow Aggregate Backstop Capital is calculated as fifty percent (50%) multiplied by the fill factor, where the fill factor is one (1) minus the ratio of current Aggregate Backstop Capital to the Target Aggregate Backstop Capital. The remainder of Step 2 Capital becomes Step 3 Capital and is allocated as specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121).

When Aggregate Backstop Capital is at or above the Turbo-Fill Floor and at or above the Target Aggregate Backstop Capital, none of Step 2 Capital is retained; all of Step 2 Capital becomes Step 3 Capital and is allocated as specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121).

##### A.2.3.1.2.4 - Step 3: Smart Burn Engine [Core]  <!-- UUID: 5ce73730-4d5d-479c-b01e-40e87f072121 -->

Step 3 Capital is allocated as follows:

- Forty-five percent (45%) of Step 3 Capital is used by the Smart Burn Engine to buy back SKY, and the SKY tokens acquired through these buybacks are distributed to SKY stakers as SKY Staking Rewards as specified in [A.2.3.1.2.5 - Step 4: Staking Rewards](bb163691-630e-4fda-88f1-96381a649fa0).
- Forty-five percent (45%) of Step 3 Capital is distributed to SKY stakers as USDS Staking Rewards as specified in [A.2.3.1.2.5 - Step 4: Staking Rewards](bb163691-630e-4fda-88f1-96381a649fa0).
- Ten percent (10%) of Step 3 Capital is used by the Smart Burn Engine to buy back SKY, and the SKY tokens acquired through these buybacks are burned.

The specific parameters governing the execution of Smart Burn Engine buybacks are specified in [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a).

##### A.2.3.1.2.5 - Step 4: Staking Rewards [Core]  <!-- UUID: bb163691-630e-4fda-88f1-96381a649fa0 -->

Step 4 Capital is distributed to SKY stakers as Staking Rewards. Step 4 Capital comprises (1) USDS allocated from Step 3, distributed as USDS Staking Rewards, and (2) SKY tokens acquired by the Smart Burn Engine through buybacks specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121), distributed as SKY Staking Rewards.

#### A.2.3.1.3 - Sourcing Of Internal Senior Risk Capital [Core]  <!-- UUID: ac7a6636-acbc-40c9-abc1-4543c0beb300 -->

Internal Senior Risk Capital (ISRC) consists of a portion of the excess capital of the Sky Protocol that is reinvested in providing Senior Risk Capital to Prime Agents. ISRC is sourced from Aggregate Backstop Capital (see [A.3.5.3.1.2 - Aggregate Backstop Capital](6dbead44-5ac4-4c5b-be3c-64eddd004e5c)) in two components: one hundred percent (100%) of any Aggregate Backstop Capital in excess of the Target Aggregate Backstop Capital (see [A.3.5.3.2.1 - Target Aggregate Backstop Capital](f73dda95-0b1c-4bdc-b957-469253d27281)), plus one third (1/3) of Aggregate Backstop Capital up to the Target Aggregate Backstop Capital.

#### A.2.3.1.4 - Implementation [Core]  <!-- UUID: f67a5780-11d5-4014-8254-795080c77133 -->

The Sky Treasury Management Function is implemented through Executive Votes that update the corresponding on-chain parameters. Changes to the documents herein define the intended operation of the Sky Treasury Management Function; operational effect on the Sky Protocol requires a subsequent Executive Vote. Until such an Executive Vote is executed, prior on-chain parameters remain in force.

Pending activation of the USDS Staking Rewards specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121), the Smart Burn Engine continues to operate under existing on-chain parameters specified in [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a), and SKY staking rewards continue to be funded from the Protocol Treasury via the Vesting Stream Contract specified in [A.4.4.1.4.2.1.3 - Vesting Stream Contract](21a8978d-10a5-4151-b99a-ca8115fe0a6d). The USDS Staking Rewards become operational when the SKY tokens funding the Vesting Stream Contract approach depletion. The Core Facilitator, in consultation with the Core Council Risk Advisor, determines when this activation occurs and effects the corresponding on-chain parameter changes through an Executive Vote.

##### A.2.3.1.4.1 - Short Term SKY Staking Rewards Rate [Core]  <!-- UUID: de233df4-34cc-4e88-a065-9a9dde9add3c -->

Pending activation of the USDS Staking Rewards specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121), no Step 4 Capital is allocated to SKY Staking Rewards. Instead, SKY Staking Rewards are funded from SKY token reserves held by the Protocol Treasury via the Vesting Stream Contract specified in [A.4.4.1.4.2.1.3 - Vesting Stream Contract](21a8978d-10a5-4151-b99a-ca8115fe0a6d), distributed at a rate equivalent to fifty percent (50%) of Step 2 Capital from the prior Monthly Settlement Cycle. The rate is determined by the Core Facilitator in consultation with the Core Council Risk Advisor following each Monthly Settlement Cycle, using the prior Monthly Settlement Cycle's Step 2 Capital and the price of SKY, and is implemented through an Executive Vote.

#### A.2.3.1.5 - Allocation Modification [Core]  <!-- UUID: c4ef7fd6-c70c-4fe9-9665-97ad17443390 -->

In the short term, the Core Council may reduce the allocations of Step 1 Capital (see [A.2.3.1.2.2 - Step 1: Security And Maintenance](324e9d22-70fe-4e44-82ab-118815f5c42e)) and Step 2 Capital (see [A.2.3.1.2.3 - Step 2: Aggregate Backstop Capital](2b28d464-e683-48ba-9a66-2fee05ea0a88)) below their specified levels and restore them up to those levels, and modify the allocation of Step 3 Capital among its three specified uses (see [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121)). A reduction to the Step 1 allocation may be apportioned among its components as the Core Council determines. For Step 2 Capital, the specified level is the retention its allocation formula specifies for the current state. The Core Council exercises this authority through a public post by the Core Facilitator on the Sky Forum, confirmed by Core GovOps and the Core Council Risk Advisor.

The implementation of such modifications is authorized to proceed directly to an Executive Vote without requiring a prior Governance Poll.

## A.2.4 - Sky Core Monthly Settlement Cycle [Article]  <!-- UUID: 6f8d5065-d6ff-4add-9a28-eadeffa7ed1a -->

This Article governs the Sky Core Monthly Settlement Cycle (MSC), a recurring process that synchronizes core financial operations, governance functions, and risk management activities across the ecosystem.

### A.2.4.1 - Monthly Settlement Cycle Overview [Section]  <!-- UUID: e0d89c66-5bab-402e-82a2-6270f1bcac07 -->

The documents herein define the Monthly Settlement Cycle (MSC), a standardized, system-wide process executed at the end of each calendar month.

#### A.2.4.1.1 - Operational Processes [Core]  <!-- UUID: 7f43aea7-9b81-48ef-b3ce-fdfae7e8a551 -->

The Monthly Settlement Cycle (MSC) synchronizes several key operational processes across the ecosystem, including:

1. Sky Protocol’s net revenue from the previous month is calculated and allocated through the steps of the Treasury Management Function. See [A.2.3 - Treasury Management](6c0af059-5d33-4e2b-90f1-1606957b8f85).
2. The monthly Senior Risk Capital (SRC) origination process is settled: the clearing price is established, costs are deducted from winning Prime Agents’ accounts, and their accounts are credited with Originated SRC (OSRC) for the upcoming month. See [A.3.2.2.4.3.5 - Settlement Of Origination](fff0112a-58dd-4041-97f9-7baf113b4e70).
3. Queued conversions between USDS and srUSDS within the SRC system are processed. See [A.3.2.2.4.2.2 - Deposit And Redemption Queues](38a99586-4a13-4ce3-8b2f-cee025e0c390).
4. Pioneer Incentive Pools are funded with an amount equivalent to the Sky Savings Rate multiplied by the balance of Unrewarded USDS. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).
5. Smart Burn Engine parameters are updated at each Monthly Settlement Cycle based on the prior month's state. See [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121) and [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a).
6. Critical Core GovOps functions related to the operationalization of Sky Primitives are executed, including payment/reimbursement processing, compliance monitoring, and the calculation and application of retroactive penalties.

#### A.2.4.1.2 - Implementation [Core]  <!-- UUID: 75473c4b-69ba-4e6b-bbf6-2c926732364c -->

The documents herein define the initial implementation of the Monthly Settlement Cycle. This initial implementation of the Monthly Settlement Cycle does not include the Senior Risk Capital System, which is still being developed.

##### A.2.4.1.2.1 - Process Definition [Core]  <!-- UUID: dd25aba4-7b77-469e-beb2-feaaedbbf143 -->

The documents herein define the initial process for performing the Monthly Settlement Cycle. The calculations to be performed as part of the Monthly Settlement Cycle are defined in [A.2.4.1.2.2 - Implementation Stages](cf1d76c1-fc9f-499d-866f-265276e421f0). This process definition specifies who performs the calculations and how funds are ultimately paid out.

###### A.2.4.1.2.1.1 - Initial Calculation By Operational Executor Agent [Core]  <!-- UUID: e9f6226e-656c-4290-a329-d745f45323ba -->

Within seven (7) calendar days of the end of each month, each Operational Executor Agent posts on the Sky Forum a calculation of the net amounts due to Sky from, or from Sky to, the Prime Agents that it has an Executor Accord with (the "Initial Calculation"), under the "Sky Core" category using the `monthly-settlement-cycle` tag. The first Initial Calculation posted for a given month begins that month's thread for the Monthly Settlement Cycle (the "Monthly Settlement Cycle Post"), and any further Initial Calculations for that month are posted as replies to it. The last Initial Calculation posted for a given month must also include calculation of the amounts to be transferred to the Core Council and Aligned Delegates Buffers (see [A.2.3.1.2.2 - Step 1: Security And Maintenance](324e9d22-70fe-4e44-82ab-118815f5c42e)). The Initial Calculation must contain reasonable supporting detail. The required contents of the Initial Calculation will be further specified in a future iteration of the Atlas.

###### A.2.4.1.2.1.1.1 - Demand Side Stablecoin Primitive Recipients [Core]  <!-- UUID: f62602a6-1c1a-44d4-9c9f-a903ce433330 -->

For each Prime Agent, the Initial Calculation must specify whether payments with respect to Demand Side Stablecoin Primitives (see [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d)) have already been made by the Operational Executor Agent, and thus should be reimbursed to the Operational Executor Agent instead of being paid to the Prime Agent.

###### A.2.4.1.2.1.2 - Final Calculation By Core GovOps [Core]  <!-- UUID: 9de89bf3-9051-44f1-9ec0-d362ee4d4b38 -->

Within twelve (12) calendar days of the end of each month, Core GovOps replies to the Monthly Settlement Cycle Post with the final calculation of the net amounts due to or from each Prime Agent (the "Final Calculation"). The Final Calculation should also include the final amounts to be transferred to the Core Council and Aligned Delegates Buffers (see [A.2.3.1.2.2 - Step 1: Security And Maintenance](324e9d22-70fe-4e44-82ab-118815f5c42e)). If there are any Disputed Amounts (see [A.2.4.1.2.1.2.2 - Disputed Amount](4ddda7cd-9942-4f60-9555-6b3f16770334)), then Core GovOps must resolve them. Core GovOps must work with the relevant Operational Executor Agent and relevant Prime Agents to reach a mutually acceptable resolution and may consult other parties to the extent it deems advisable. Where amounts settled are subsequently determined to be incorrect, they are trued up in a subsequent Monthly Settlement Cycle (see [A.2.4.1.2.1.4 - True Up In Subsequent Monthly Settlement Cycle](de1592f5-dbce-46de-913f-6ec9589d36e8)).

Core GovOps makes the final decision in resolving any Disputed Amounts. The Final Calculation must specify the Final Amount and contain reasonable supporting detail. The required contents of the Final Calculation will be further specified in a future iteration of the Atlas.

###### A.2.4.1.2.1.2.1 - Agreed Amount [Core]  <!-- UUID: 8669ef42-d55b-4be8-839e-646b4ff17e4c -->

The net amount due to or from a Prime Agent in an Initial Calculation is an Agreed Amount if the Prime Agent does not post a Dispute Notice with respect to that amount within the period specified in [A.2.4.1.2.1.2.4 - Disputes By Prime Agents](c204b363-7cc0-4e40-a7dc-68de57358cf9).

###### A.2.4.1.2.1.2.2 - Disputed Amount [Core]  <!-- UUID: 4ddda7cd-9942-4f60-9555-6b3f16770334 -->

The net amount due to or from a Prime Agent in an Initial Calculation is a Disputed Amount if it is not an Agreed Amount.

###### A.2.4.1.2.1.2.3 - Final Amount [Core]  <!-- UUID: c20c38fe-c952-4e75-86fe-d6b561f7f436 -->

The net amount due to or from a Prime Agent in a Final Calculation is a Final Amount.

###### A.2.4.1.2.1.2.4 - Disputes By Prime Agents [Core]  <!-- UUID: c204b363-7cc0-4e40-a7dc-68de57358cf9 -->

A Prime Agent may dispute the calculation of the net amount due to or from it (a "Dispute Notice"). The Dispute Notice must be posted as a reply to the Monthly Settlement Cycle Post within five (5) calendar days of the posting of the Initial Calculation being disputed. The Dispute Notice must specify the errors in the Initial Calculation and the Prime’s own calculation of the net amount due to or from it. The required contents of the Dispute Notice will be further specified in a future iteration of the Atlas.

Core GovOps may at its discretion resolve the dispute using the process specified in [A.2.4.1.2.1.2 - Final Calculation By Core GovOps](9de89bf3-9051-44f1-9ec0-d362ee4d4b38). Alternatively, Core GovOps may elect to determine the correct amount and true up any differences in a subsequent Monthly Settlement Cycle as specified in [A.2.4.1.2.1.4 - True Up In Subsequent Monthly Settlement Cycle](de1592f5-dbce-46de-913f-6ec9589d36e8). In either case Core GovOps must post its decision as a reply to the Dispute Notice.

###### A.2.4.1.2.1.3 - Settlement Through Sky Core Executive Vote [Core]  <!-- UUID: 0d561ea6-8689-459c-85eb-7c861553e116 -->

When Core GovOps has posted the Final Calculation then the Core Facilitator must include payments of these amounts in the next Sky Core Executive Vote as specified herein.

###### A.2.4.1.2.1.3.1 - Payment Of Amounts Due To Prime Agents [Core]  <!-- UUID: 1816e5eb-3cf1-427f-b831-8eeb9408887c -->

Amounts due to Prime Agents, excluding reimbursements made to Operational Executor Agents (see [A.2.4.1.2.1.3.3 - Reimbursement Of Payments Made By Operational Executor Agents](07c5cfd2-d68a-40d6-873d-b82cea9a92be)), are transferred from the Sky Surplus Buffer to the Prime SubProxy Account through an Executive Vote.

###### A.2.4.1.2.1.3.2 - Collection Of Amounts Due From Prime Agents [Core]  <!-- UUID: 6e3d5198-fdb5-47dd-b632-4c71a313a1a6 -->

Amounts due from Prime Agents, excluding reimbursements made to Operational Executor Agents (see [A.2.4.1.2.1.3.3 - Reimbursement Of Payments Made By Operational Executor Agents](07c5cfd2-d68a-40d6-873d-b82cea9a92be)) are settled in a way that is equivalent to a transfer from the Prime to the Sky Surplus Buffer through actions included in an Executive Vote.

###### A.2.4.1.2.1.3.3 - Reimbursement Of Payments Made By Operational Executor Agents [Core]  <!-- UUID: 07c5cfd2-d68a-40d6-873d-b82cea9a92be -->

Reimbursements of payments already made by the Operational Executor Agent with respect to Demand Side Stablecoin Primitives (see [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d)) are transferred to the Operational Executor Agent’s Buffer through an Executive Vote.

###### A.2.4.1.2.1.4 - True Up In Subsequent Monthly Settlement Cycle [Core]  <!-- UUID: de1592f5-dbce-46de-913f-6ec9589d36e8 -->

If the amounts of any payments included in the Sky Core Executive Vote (see [A.2.4.1.2.1.3 - Settlement Through Sky Core Executive Vote](0d561ea6-8689-459c-85eb-7c861553e116)) are subsequently determined to be incorrect, adjustments are included in a subsequent Monthly Settlement Cycle to ensure that each party pays the amount it owes or receives the amount to which it is entitled.

Core GovOps must prepare a statement specifying the errors, the correct amounts, and the adjustments needed (the "Correction Calculation"). The Correction Calculation must be posted to the Sky Forum under the "Sky Core" category with the `monthly-settlement-cycle` tag. The required contents of the Correction Calculation will be further specified in a future iteration of the Atlas.

###### A.2.4.1.2.1.5 - Interim Measures [Core]  <!-- UUID: f2401c5e-0fea-4a50-ab0b-3e03fc413dbb -->

The documents herein define interim exceptions to the process definition for the Monthly Settlement Cycle.

###### A.2.4.1.2.1.5.1 - Scope Of July / August 2025 Monthly Settlement Cycle [Core]  <!-- UUID: bfc3548d-5ad1-4327-a54a-ddd4549c5fdc -->

The initial Monthly Settlement Cycle conducted in September 2025 will be for the two month period from July 1, 2025 to August 31, 2025.

###### A.2.4.1.2.1.5.2 - Process For July / August 2025 Monthly Settlement Cycle [Core]  <!-- UUID: 146d3d9c-7f8a-4dc4-b6b3-349bab4279bb -->

For the initial Monthly Settlement Cycle conducted in September 2025, the Initial Calculation prepared by Operational Executor Agent Amatsu will only include calculations related to Demand Side Stablecoin Primitives (see [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d)). The Independent Calculation prepared by the Core Council Risk Advisor on behalf of the Core Council will be prepared normally. The calculations related to Demand Side Stablecoin Primitives will be subject to the normal resolution process defined in [A.2.4.1.2.1.2 - Final Calculation By Core GovOps](9de89bf3-9051-44f1-9ec0-d362ee4d4b38). For all other calculations, the amounts in the Independent Calculation will be treated as Agreed Amounts. The Initial Calculation and the Independent Calculation will be posted to the Sky Forum by September 10, 2025.

###### A.2.4.1.2.1.5.3 - Process For September 2025 Monthly Settlement Cycle [Core]  <!-- UUID: 8e8ff62f-c6c5-4094-afd1-2cedcf482df6 -->

For the Monthly Settlement Cycle conducted in October 2025, the Initial Calculation prepared by Operational Executor Agent Amatsu will only include calculations related to Spark. The Independent Calculation prepared by the Core Council Risk Advisor on behalf of the Core Council will be prepared normally. The calculations related to Spark will be subject to the normal resolution process defined in [A.2.4.1.2.1.2 - Final Calculation By Core GovOps](9de89bf3-9051-44f1-9ec0-d362ee4d4b38). For all other calculations, the amounts in the Independent Calculation will be treated as Agreed Amounts.

###### A.2.4.1.2.1.5.4 - Process For November / December 2025 Monthly Settlement Cycle [Core]  <!-- UUID: 5aa66a15-d59c-4f66-9d80-96583698f24d -->

There will be no Monthly Settlement Cycle conducted in December 2025. Instead, the Monthly Settlement Cycle conducted in January 2026 will be for the two-month period from November 1, 2025 to December 31, 2025.

For the Monthly Settlement Cycle conducted in January 2026, the Independent Calculation prepared by the Core Council Risk Advisor on behalf of the Core Council will only include calculations related to Spark. The Initial Calculation prepared by Operational Executor Agent Amatsu will be prepared normally. The calculations related to Spark will be subject to the normal resolution process defined in [A.2.4.1.2.1.2 - Final Calculation By Core GovOps](9de89bf3-9051-44f1-9ec0-d362ee4d4b38). For all other calculations, the amounts in the Initial Calculation will be treated as Agreed Amounts.

##### A.2.4.1.2.2 - Implementation Stages [Core]  <!-- UUID: cf1d76c1-fc9f-499d-866f-265276e421f0 -->

The initial implementation of the Monthly Settlement Cycle will occur in three stages as specified in the documents herein.

###### A.2.4.1.2.2.1 - Stage 1 [Core]  <!-- UUID: efb30fa0-99b1-43bd-bdfd-219cf897c44f -->

The documents herein define Stage 1 of the implementation of the Monthly Settlement Cycle.

###### A.2.4.1.2.2.1.1 - Stage 1 Simplified Profit And Loss Calculation [Core]  <!-- UUID: 65bd404f-0fd4-4ae9-9860-2c6e37731fef -->

In Stage 1 of the implementation of the Monthly Settlement Cycle, the net amount due from each Prime to Sky will be calculated using a Simplified Profit And Loss Calculation as specified in the documents herein.

###### A.2.4.1.2.2.1.1.1 - Amount Due From Sky To Primes With Respect To Demand Side Primitives And Agent Rate [Core]  <!-- UUID: 33d1b516-d347-4d44-9af6-95f25e8a8d8c -->

The amount due from Sky to each Prime with respect to Demand Side Primitives and the Agent Rate is calculated as specified in the documents herein.

###### A.2.4.1.2.2.1.1.1.1 - Amount Due From Sky To Primes With Respect To Distribution Reward [Core]  <!-- UUID: 0b2165cb-c10d-474b-ad55-544821ac29c3 -->

The amount due from Sky to a Prime in a month with respect to the Distribution Reward is the amount earned by the Prime with respect to all USDS and sUSDS balances marked with the Prime’s reward codes. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6). This includes any Bonus Distribution Reward. See [A.2.8.2.2.2.3.2 - 2025 Bonus](7ca440d3-03fb-4fba-81a8-d2118dc47aa6).

###### A.2.4.1.2.2.1.1.1.2 - Amount Due From Sky To Primes With Respect To Agent Rate [Core]  <!-- UUID: aeb1d633-d6e2-46ef-9f55-bcb0a16a2e63 -->

The amount due from Sky to a Prime in a month with respect to the Agent Rate is calculated as specified in [A.3.1.2.3 - Agent Rate](012c953b-c522-4ea3-939b-3282af4e1d7e).

###### A.2.4.1.2.2.1.1.1.3 - Amount Due From Sky To Primes With Respect To Distribution Reward And Agent Rate [Core]  <!-- UUID: cef16014-05db-4b21-a5a2-20e62aaca027 -->

The amount due from Sky to a Prime in a month with respect to the Distribution Reward and the Agent Rate is the sum of the amounts specified in [A.2.4.1.2.2.1.1.1.1 - Amount Due From Sky To Primes With Respect To Distribution Reward](0b2165cb-c10d-474b-ad55-544821ac29c3) and [A.2.4.1.2.2.1.1.1.2 - Amount Due From Sky To Primes With Respect To Agent Rate](aeb1d633-d6e2-46ef-9f55-bcb0a16a2e63).

###### A.2.4.1.2.2.1.1.2 - Amount Due From Prime To Sky With Respect To Supply Side Primitives [Core]  <!-- UUID: e98ddd17-a8c3-4523-8464-cc41247c66e8 -->

The amount due from each Prime to Sky with respect to Supply Side Primitives is calculated as specified in the documents herein.

###### A.2.4.1.2.2.1.1.2.1 - Step 1: Calculate Total Allocation System Revenue [Core]  <!-- UUID: fd3ea856-dbef-4fe0-a662-82a58d33d9c0 -->

First, Total Allocation System Revenue is calculated for each Prime for the month. Total Allocation System Revenue for a Prime in a month is the sum of Instance Revenue for each Active Instance of the Allocation System Primitive that the Prime has deployed.

###### A.2.4.1.2.2.1.1.2.1.1 - Instance Revenue [Core]  <!-- UUID: 90acccd5-d7b4-4c03-9ce2-471dc3e82c98 -->

Instance Revenue for an Allocation System Instance for a month is all earnings from that Instance.

###### A.2.4.1.2.2.1.1.2.2 - Step 2: Calculate Total Allocation System Profit [Core]  <!-- UUID: 1eaa2350-e354-4000-baa6-be250853bddc -->

Second, Total Allocation System Profit is calculated for each Prime for the month. Total Allocation System Profit for a Prime in a month is the sum of Instance Profit for each Active Instance of the Allocation System Primitive that the Prime has deployed.

###### A.2.4.1.2.2.1.1.2.2.1 - Instance Profit [Core]  <!-- UUID: 9974c452-216b-45c0-8a1d-621816b8da2a -->

Instance Profit for an Allocation System Instance is equal to the greater of (1) Instance Revenue (see [A.2.4.1.2.2.1.1.2.1.1 - Instance Revenue](90acccd5-d7b4-4c03-9ce2-471dc3e82c98)) minus Instance Expenses (see [A.2.4.1.2.2.1.1.2.2.1.1 - Instance Expense](6cbe7181-419f-4a7b-a659-85972d5100a3)) and (2) zero.

###### A.2.4.1.2.2.1.1.2.2.1.1 - Instance Expense [Core]  <!-- UUID: 6cbe7181-419f-4a7b-a659-85972d5100a3 -->

Instance Expense for an Allocation System Instance for a month is the interest expense on the funds from Sky’s Collateral Portfolio invested in the Instance. It is calculated on a per block basis based on the amount invested from Sky’s Collateral Portfolio and the Agent Credit Line Borrow Rate.

###### A.2.4.1.2.2.1.1.2.3 - Step 3: Calculate Adjusted Allocation System Profit [Core]  <!-- UUID: a9427e1a-77ae-473b-aafd-b4216fcd615c -->

Third, Adjusted Allocation System Profit is calculated for each Prime for the month. Adjusted Allocation System Profit for a Prime in a month is Total Allocation System Profit minus the Distortion Penalty (see [A.2.4.1.2.2.1.1.2.3.1 - Distortion Penalty](2a021208-c964-440f-b491-3c9e034f2d22)) and the Low Yield Actively Stabilizing Collateral Penalty (see [A.2.4.1.2.2.1.1.2.3.2 - Low Yield Actively Stabilizing Collateral Penalty](631e7c75-375f-4298-9d85-b17cb2eb019f)).

###### A.2.4.1.2.2.1.1.2.3.1 - Distortion Penalty [Core]  <!-- UUID: 2a021208-c964-440f-b491-3c9e034f2d22 -->

The Distortion Penalty is a discretionary penalty designed to mitigate the potential misalignment caused by the asymmetric nature of the Simplified Profit And Loss Calculation, where Primes earn profits on Allocation System Instances that earn more than the Agent Credit Line Borrow Rate but do not suffer losses when Instances earn less than the Agent Credit Line Borrow Rate.

The Core Executor Agents, in consultation with the Core Council Risk Advisor, may assess a penalty of up to 100% of Total Allocation System Profit (see [A.2.4.1.2.2.1.1.2.2 - Step 2: Calculate Total Allocation System Profit](1eaa2350-e354-4000-baa6-be250853bddc)) if it determines that a Prime’s decisions were distorted by this incentive structure.

###### A.2.4.1.2.2.1.1.2.3.2 - Low Yield Actively Stabilizing Collateral Penalty [Core]  <!-- UUID: 631e7c75-375f-4298-9d85-b17cb2eb019f -->

The Low Yield Actively Stabilizing Collateral Penalty is a formulaic penalty designed to prevent Primes from holding excessive amounts of low yield Actively Stabilizing Collateral.

The penalty, as a percentage of the Total Allocation System Profit, is the lesser of (1) ten times the Excess Low Yield Actively Stabilizing Collateral Percentage and (2) 100%.

###### A.2.4.1.2.2.1.1.2.3.2.1 - Excess Low Yield Actively Stabilizing Collateral Percentage [Core]  <!-- UUID: 5e78fb21-1208-442f-b215-3babcd69fd69 -->

The Excess Low Yield Actively Stabilizing Collateral Percentage for a Prime is equal to the excess of (1) its Low Yield Actively Stabilizing Collateral (see [A.2.4.1.2.2.1.1.2.3.2 - Low Yield Actively Stabilizing Collateral Penalty](631e7c75-375f-4298-9d85-b17cb2eb019f)) as a percentage of its Collateral Portfolio above (2) its Minimum Actively Stabilizing Collateral (see [A.3.3.2.2 - Minimum Actively Stabilizing Collateral](475fe222-9e4a-4e9d-9be6-a7a424ce02f8)) as a percentage of its Collateral Portfolio.

###### A.2.4.1.2.2.1.1.2.3.2.1.1 - Low Yield Actively Stabilizing Collateral [Core]  <!-- UUID: 858b2ee0-89b8-4505-8324-f3cd315de40c -->

Low Yield Actively Stabilizing Collateral is Actively Stabilizing Collateral (see [A.3.3.2.2.1.1 - Resting Actively Stabilizing Collateral](0e17b35a-c830-4695-b63c-5ef58b249d3f)) that earns less than the Agent Credit Line Borrow Rate.

###### A.2.4.1.2.2.1.1.2.4 - Step 4: Calculate Amount Due To Sky With Respect To Supply Side Primitives [Core]  <!-- UUID: 2617edae-6c22-4d7c-8e14-353bfced35f2 -->

Fourth, the amount due to Sky with respect to Supply Side Primitives is calculated for each Prime for the month. The amount due to Sky with respect to Supply Side Primitives is Total Allocation System Revenue (see [A.2.4.1.2.2.1.1.2.1 - Step 1: Calculate Total Allocation System Revenue](fd3ea856-dbef-4fe0-a662-82a58d33d9c0)) minus Adjusted Allocation System Profit (see [A.2.4.1.2.2.1.1.2.3 - Step 3: Calculate Adjusted Allocation System Profit](a9427e1a-77ae-473b-aafd-b4216fcd615c)).

###### A.2.4.1.2.2.1.1.3 - Settlement [Core]  <!-- UUID: 6dcd7515-3398-443a-9377-99e0c3cd0174 -->

The amounts due from Sky to each Prime with respect to Demand Side Primitives and the Agent Rate (see [A.2.4.1.2.2.1.1.1 - Amount Due From Sky To Primes With Respect To Demand Side Primitives And Agent Rate](33d1b516-d347-4d44-9af6-95f25e8a8d8c)) and the amounts due from each Prime to Sky with respect to Supply Side Primitives (see [A.2.4.1.2.2.1.1.2 - Amount Due From Prime To Sky With Respect To Supply Side Primitives](e98ddd17-a8c3-4523-8464-cc41247c66e8)) are settled as specified in [A.2.4.1.2.1.3 - Settlement Through Sky Core Executive Vote](0d561ea6-8689-459c-85eb-7c861553e116).

###### A.2.4.1.2.2.1.1.4 - Exceptions [Core]  <!-- UUID: db06608a-303d-4b35-864a-f7aad38fcb06 -->

The documents herein define exceptions to the Simplified Profit And Loss Calculation for specific assets held by certain Prime Agents.

###### A.2.4.1.2.2.1.1.4.1 - USDT Held By Spark [Core]  <!-- UUID: 34893b77-2cce-4753-9ce4-2b8ab1f951bb -->

Spark pays the Agent Credit Line Borrow Rate with respect to funds borrowed by Spark to invest in USDT and held in SparkLend. Spark thus realizes the full profit and loss associated with these investments.

###### A.2.4.1.2.2.1.1.4.2 - pyUSD Held By Spark [Core]  <!-- UUID: 8619f00f-84e2-4951-86c4-08876d8a6f6a -->

Spark pays the Agent Credit Line Borrow Rate with respect to funds borrowed by Spark to invest in pyUSD and held in SparkLend or Spark’s ALM Proxy. Spark thus realizes the full profit and loss associated with these investments.

###### A.2.4.1.2.2.1.2 - Stage 1 Timing [Core]  <!-- UUID: ff3aa296-34eb-4783-904f-4510fa0c6c37 -->

Stage 1 is currently expected to be implemented in the August 21, 2025 Executive Vote for the period from July 1, 2025 to July 31, 2025.

###### A.2.4.1.2.2.1.3 - Stage 1 Actions [Core]  <!-- UUID: f87c520a-3324-46a7-ac4e-9c7de2a2af0a -->

The actions specified herein must be completed to achieve Stage 1 implementation of the Monthly Settlement Cycle.

###### A.2.4.1.2.2.1.3.1 - Reduction Of Prime Allocator Vault Stability Fees [Core]  <!-- UUID: 48ec2b03-0885-45d9-b5f6-22267414f587 -->

The Stability Fees for each Prime Allocator Vault must be reduced to zero so that value is transferred from Primes to Sky Core exclusively through Executive Votes. The Core Executor Agents, in consultation with the Core Council Risk Advisor, is directed to use the Stability Parameter Bounded External Access Module to reduce the Stability Fee for each Prime Allocator Vault to zero. See [A.3.7.1.3.3 - Allocator Vault Parameters](6ab6bd12-93d3-419f-96e2-a7f79bfe1afa).

###### A.2.4.1.2.2.1.3.2 - Automation Of Simplified Profit And Loss Calculation [Core]  <!-- UUID: 1782eeb8-8c6f-4b34-beea-7ab140057324 -->

The Core Council must ensure tooling is developed to allow the net amount due from each Prime to Sky each month under the Simplified Profit And Loss Calculation to be computed automatically.

###### A.2.4.1.2.2.2 - Stage 2 [Core]  <!-- UUID: 74bdfafe-e3c7-4670-a8bd-c337f1ad1e49 -->

The documents herein define Stage 2 of the implementation of the Monthly Settlement Cycle.

###### A.2.4.1.2.2.2.1 - Stage 2 Virtual Base Rate [Core]  <!-- UUID: c1fc89f4-b30f-4da1-93c6-822839fed783 -->

In Stage 2 of the implementation of the Monthly Settlement Cycle, the net amount due from each Prime to Sky is calculated as specified in the Atlas without the use of the Simplified Profit And Loss Calculation. However, interest under the Base Rate does not accrue in real time onchain and is instead calculated offchain and paid through Executive Votes as part of the Monthly Settlement Cycle. This is known as the Virtual Base Rate as these calculations occur offchain.

###### A.2.4.1.2.2.2.2 - Stage 2 Timing [Core]  <!-- UUID: ceb3c433-d73f-4c58-bac9-e79b44e66fcf -->

Stage 2 will be implemented in the December 2025 Monthly Settlement Cycle for the period from November 1, 2025 to November 30, 2025. If there is no December 2025 Monthly Settlement Cycle, then Stage 2 will be implemented in the January 2026 Monthly Settlement Cycle for the period from November 1, 2025 to December 31, 2025.

###### A.2.4.1.2.2.2.3 - Stage 2 Actions [Core]  <!-- UUID: b8c86fb3-2ba4-4c53-a509-81d022dffd20 -->

The actions specified herein must be completed to achieve Stage 2 implementation of the Monthly Settlement Cycle.

###### A.2.4.1.2.2.2.3.1 - Automation Of Monthly Settlement Cycle Calculation Including Virtual Base Rate [Core]  <!-- UUID: d98d3753-4230-4ad8-a1e7-7b1fd7e3b679 -->

The Core Council must ensure automated tooling is developed for calculating the net amount due from each Prime to Sky each month, incorporating the Virtual Base Rate.

###### A.2.4.1.2.2.3 - Stage 3 [Core]  <!-- UUID: 1f9811fa-a759-4cd9-b7e1-aa0cc51174ed -->

The documents herein define Stage 3 of the implementation of the Monthly Settlement Cycle.

###### A.2.4.1.2.2.3.1 - Stage 3 Onchain Base Rate [Core]  <!-- UUID: eebbcd6d-2cbe-47cb-89c5-f119cf4eda08 -->

In Stage 3 of the implementation of the Monthly Settlement Cycle, the net amount due from each Prime to Sky is calculated as specified in the Atlas without the use of the Simplified Profit And Loss Calculation. In Stage 3, interest from the Base Rate accrues onchain to the Allocator Vault of each Prime. Thus, in Stage 3 Executive Votes are only required to pay down accrued interest on Allocator Vaults, as necessary, and settle other amounts due to and from Primes.

###### A.2.4.1.2.2.3.2 - Stage 3 Timing [Core]  <!-- UUID: cf7ed710-0302-4169-af70-34194269e184 -->

The timing for Stage 3 implementation of the Monthly Settlement Cycle will be specified in a future iteration of the Atlas.

###### A.2.4.1.2.2.3.3 - Stage 3 Actions [Core]  <!-- UUID: 42dc70f1-1353-40f8-90c3-cbbac317b26f -->

The actions specified herein must be completed to achieve Stage 3 implementation of the Monthly Settlement Cycle.

###### A.2.4.1.2.2.3.3.1 - Integration Of Base Rate Into Allocator Vaults [Core]  <!-- UUID: 2eb1b10f-e959-42ad-87db-2556e7fc7581 -->

Allocator Vaults must be updated to accrue interest in real time based on the Base Rate.

###### A.2.4.1.2.2.3.3.2 - Automation Of Monthly Settlement Cycle Based On Base Rate [Core]  <!-- UUID: 50b52e7e-2f79-4a7a-b887-cda85bc77cd7 -->

The Core Council must ensure the tooling specified in [A.2.4.1.2.2.2.3.1 - Automation Of Monthly Settlement Cycle Calculation Including Virtual Base Rate](d98d3753-4230-4ad8-a1e7-7b1fd7e3b679) is updated to reflect the onchain accrual of the Base Rate.

### A.2.4.2 - Settlement Methodology [Section]  <!-- UUID: b0b7809a-8a4c-4b75-9fe5-9524fa7ed0cd -->

The documents herein define the methodology by which amounts are measured and attributed in the Monthly Settlement Cycle. See [A.2.4.1 - Monthly Settlement Cycle Overview](e0d89c66-5bab-402e-82a2-6270f1bcac07).

#### A.2.4.2.1 - Calculation Of Prime Agent Interest Expense And Corresponding Sky Revenue [Core]  <!-- UUID: 13c35a4e-00a4-438f-a4a2-0ebd170694bc -->

For the purpose of the Monthly Settlement Cycle, the interest a Prime Agent owes to Sky on liquidity borrowed from Sky is an interest expense of the Prime Agent and revenue of Sky. The documents herein specify how that amount is calculated.

##### A.2.4.2.1.1 - Calculation Of Interest Rate [Core]  <!-- UUID: 5072233d-24e1-4882-b747-83465267b0c9 -->

Interest is calculated at the [A.3.1.2.5 - Agent Credit Line Borrow Rate](6b2b7302-e63b-457e-afeb-daab5ca7a7de), including any applicable [A.3.1.2.5.2 - Subsidized Rate](ceceb90b-57d1-43db-9e52-133532c373fd).

##### A.2.4.2.1.2 - Calculation Of Applicable Balance [Core]  <!-- UUID: adbe704f-9c50-4ee1-b632-398cdd87598a -->

Interest is calculated on utilized USDS. Utilized USDS is the liquidity a Prime Agent has borrowed from Sky, less:

- USDS held idle in an ALM Proxy
- USDS held idle in a Peg Stability Module
- USDS attributable to a Sky Direct Exposure, as specified in [A.2.2.10.1.1.1.1 - Sky Direct Exposures](b3fb8653-8503-4a9e-81b2-5e9f49ad6703)
- USDS held idle in an AMM pool
- USDS supplied to a lending pool that is not borrowed from that pool

##### A.2.4.2.1.3 - Netting [Core]  <!-- UUID: e1d1fda8-eac9-4b39-a750-42a2feee6768 -->

A Prime Agent that holds sUSDS earns the Sky Savings Rate on that sUSDS. Where that sUSDS is funded by liquidity borrowed from Sky, the Sky Savings Rate earned and the interest owed to Sky are netted, and the net amount is the interest expense of the Prime Agent and revenue of Sky.

#### A.2.4.2.2 - Positions Held By Third Parties [Core]  <!-- UUID: 70b26ada-adac-4bdf-bd3e-dc3b2347ad78 -->

Gains and losses on positions held by a third party on behalf of a Prime Agent are attributed to the period in which they are received or incurred by the Allocation System Instance, and not to the period in which the third party reports them. Values reported by a third party through an application programming interface are not used to attribute gains or losses.

#### A.2.4.2.3 - Asynchronous Transactions [Core]  <!-- UUID: 5d38602e-46e8-48d2-b661-460a3fe9b0b9 -->

An asynchronous transaction is a transaction that settles in two (2) legs. An asynchronous transaction changes the value attributed to an Allocation System Instance only when the second leg completes.

The value of a redeemed position remains attributed to the Allocation System Instance from the burning of the corresponding shares until the redemption proceeds settle. The value of a deposit is attributed to the Allocation System Instance only when the corresponding shares are minted.

#### A.2.4.2.4 - Assets In Transit Between Blockchains [Core]  <!-- UUID: 12778509-d4b4-4e45-b80f-11a3b7ecbad9 -->

An asset in transit between blockchains remains attributed to the source blockchain, at the value it held before transit, from the time it is locked or burned on the source blockchain until the corresponding tokens are minted or released on the destination blockchain. On the date the asset is minted or released, it ceases to be attributed to the source blockchain and is attributed to the destination blockchain. The asset is attributed to exactly one (1) blockchain at all times.

## A.2.5 - Agent Incubation [Article]  <!-- UUID: bb0c23c6-5123-4c35-ac84-fcb018a72cda -->

This Article governs the incubation of Agents. It defines the necessary infrastructure and processes to ensure Agents are maximally supported to generate as much value as possible for the Sky Ecosystem.

### A.2.5.1 - Support For Agents [Section]  <!-- UUID: a28b1bca-adac-493d-a052-40e36c97e670 -->

This Section defines elements and infrastructure to support Agents.

## A.2.6 - Ecosystem Actor Incubation [Article]  <!-- UUID: b09e86b1-0e95-4111-b141-7a980eeaef08 -->

This Article governs the incubation of new Ecosystem Actors to support the Sky Ecosystem.

### A.2.6.1 - Ecosystem Actor Incubation [Section]  <!-- UUID: 0016dcac-6cf0-4e66-ae6f-112f40eb9767 -->

The Support Scope is responsible for incubating Ecosystem Actors. This Section defines the elements to support this objective.

#### A.2.6.1.1 - Incubating Ecosystem Actors [Core]  <!-- UUID: 0239db13-482e-4a91-b173-ee31569dbb4c -->

Incubating Ecosystem Actors are Ecosystem Actors that are being developed to support the Sky Protocol or its current and future Agents. Sky Governance can assign these actors projects that benefit the Sky Protocol or incubating Agents, such as solutions for branding, marketing, user acquisition; referral marketing and revenue share systems; smart contract development; and protocol development.

#### A.2.6.1.2 - Currently Incubating Ecosystem Actors Template [Core]  <!-- UUID: 3af47ea8-d85b-4bd8-9339-ab053ed7a21a -->

The list of Incubating Ecosystem Actors must follow this template for each recorded Incubating Ecosystem Actor:

- **.x:** [Incubating Ecosystem Actor name and short description]
- **.1:** [Budget information]
- **.2:** [Deliverables and focus areas]
- **.3:** [Team information, including headcount grouped by skill sets]

## A.2.7 - Ecosystem Communication Channels [Article]  <!-- UUID: a520fea9-c2b7-4fda-a2b0-254b76504bc0 -->

This Article regulates the unified communication infrastructure for governance ecosystem communication. This infrastructure must include channels for inter-Agent and Ecosystem Actor interaction.

### A.2.7.1 - Ecosystem Communication Channels [Section]  <!-- UUID: 7574b64b-ccf8-427f-9c32-fa7a1b222f73 -->

The Support Scope maintains the overall unified communication infrastructure used for governance ecosystem communication. This Section defines key elements and infrastructure supporting this objective.

#### A.2.7.1.1 - Communications Infrastructure [Core]  <!-- UUID: 14e381be-b1bb-4b87-a533-212bd135cf27 -->

The Core Facilitator is tasked with maintaining an ecosystem-wide communications infrastructure to enable Agent participants and Ecosystem Actors to interact with each other and discuss the Sky Ecosystem.

##### A.2.7.1.1.1 - Forum [Core]  <!-- UUID: ec33a431-9aa0-443e-9f0c-d0ab0aacfae6 -->

The communications infrastructure must include an ecosystem Forum devoted to discussions on Agent-related business proposals, partnerships and interactions, as well as casual conversation for the broader Sky Ecosystem.

###### A.2.7.1.1.1.1 - Authorized Forum Accounts Requirements [Core]  <!-- UUID: a76f81b5-49bb-4697-a30b-bf009ab24286 -->

The documents herein define the requirements for forum account registration, disclosure, and enforcement applicable to entities participating in Sky governance.

###### A.2.7.1.1.1.1.1 - Registration Requirement [Core]  <!-- UUID: 3f2ba4e7-cc85-406b-94ce-83da549babc5 -->

All forum accounts used to post on the Sky Forum in a governance capacity must be registered in [A.2.7.1.1.1.1.4.0.6.1 - Current Authorized Forum Accounts](b71564fd-22e0-4c69-99d1-5b23fc1fa329). Each registration must include:

- The entity handle, which is the official forum account representing the entity. If an entity does not maintain its own forum handle, it may indicate this in the registry and rely solely on Authorized Representatives.
- All Authorized Representatives, which are forum accounts held by team members, individuals, or other entities that are authorized to post on behalf of the entity.

Each entity is responsible for ensuring that its registration reflects its current handles and Authorized Representatives, and that any changes are promptly updated. A single forum handle may appear as an Authorized Representative of more than one (1) entity.

###### A.2.7.1.1.1.1.2 - Disclosure Requirement [Core]  <!-- UUID: 87a69cf4-cf81-4acc-bb90-7caf644eaa86 -->

When posting on behalf of another entity, the Authorized Representative must clearly indicate in the post that they are acting on behalf of that entity.

###### A.2.7.1.1.1.1.3 - Enforcement [Core]  <!-- UUID: 0fa7211a-81a5-40bd-a364-0a85ebf6577e -->

Posts on governance matters from unregistered forum accounts may be disregarded for governance purposes. Accounts that repeatedly post in a governance capacity without registration are subject to moderation as specified in [A.2.7.1.2 - Moderation](be3da4c5-6882-4694-9ccd-3fa7c5f6e09a).

###### A.2.7.1.1.1.1.4 - List Of Authorized Forum Accounts [Active Data Controller]  <!-- UUID: 248a4fd8-f863-493a-9a38-2a97d9d7203e -->

The list of authorized forum accounts is defined as Active Data in [A.2.7.1.1.1.1.4.0.6.1 - Current Authorized Forum Accounts](b71564fd-22e0-4c69-99d1-5b23fc1fa329).

The Active Data is updated as follows:

- The Responsible Party is the entity to which the registration pertains.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.2.7.1.1.1.1.4.0.6.1 - Current Authorized Forum Accounts [Active Data]  <!-- UUID: b71564fd-22e0-4c69-99d1-5b23fc1fa329 -->

| Entity Name | Role | Entity Handle | Handles of Authorized Representatives |
|---|---|---|---|
| Pattern | Prime Agent | PatternDevCo | N/A |
| Redline | Operational Facilitator | N/A | redlexic |
| BA Labs | Core Council Risk Advisor | BALabs | DeFlamiingo, Sean, 0xmmj, commanderkeen, Primoz, Twigmaester, rema, definikola |
| Spark | Prime Agent | PhoenixLabs | N/A |
| Obex | Prime Agent | Rubicon | N/A |
| Grove | Prime Agent | GroveLabs | steakhouse |
| Soter Labs | Operational GovOps | SoterLabs | N/A |
| Amatsu | Operational GovOps | Amatsu | SoterLabs, Endgame-Edge (and their authorized representatives) |
| Dewiz | Ecosystem Actor | Dewiz | N/A |
| Soter Labs | Core GovOps | SoterLabs | retro, adamfraser, Lex |
| Ozone | Operational Executor Agent | N/A | SoterLabs, Redline (and their authorized representatives) |
| Endgame Edge | Operational Facilitator | Endgame-Edge | votewizard, CivicSage, boet, blimpa |
| Keel | Prime Agent | N/A | N/A |
| Sidestream | Ecosystem Actor | Sidestream | N/A |
| JanSky | Core Facilitator | JanSky-Team | JanSky, ldr |
| Rune | N/A | rune | N/A |
| Amatsu | Operational Executor Agent | Amatsu_OEA | SoterLabs, Endgame-Edge (and their authorized representatives) |

##### A.2.7.1.1.2 - Chatroom [Core]  <!-- UUID: a596136b-a805-420b-be77-bf249e41ada4 -->

The communications infrastructure must include a chatroom for broad discussion related to Agents, Ecosystem Actors and Sky. As an initial bootstrapping measure, the Core Facilitator can use Discord.

#### A.2.7.1.2 - Moderation [Core]  <!-- UUID: be3da4c5-6882-4694-9ccd-3fa7c5f6e09a -->

The documents herein define the moderation policies and responsible moderators for Sky's communication channels.

##### A.2.7.1.2.1 - Moderation Policies [Core]  <!-- UUID: 236ecf52-bd7f-4170-9cc5-f5b25f5ba3d4 -->

The documents herein define the moderation policies applicable to Ecosystem Communication Channels.

###### A.2.7.1.2.1.1 - General Requirements [Core]  <!-- UUID: 63701dcb-d885-4f81-a67b-71f5bf67bde8 -->

This document defines the requirements generally applicable to all Ecosystem Communication Channels.

Responsible moderators are granted the prerogative to ban users from the communication channels for which they are responsible when they deem users to be acting in a misaligned fashion. Misalignment can include maliciously exploiting the communication channel or disrupting its efficient functioning through improper use or antisocial behavior.

However, unless egregiously misaligned or disrupting behavior takes place, responsible moderators should err on the side of charity and issue a public warning for users who engage in bad behavior before resorting to banning them. Egregiously misaligned or disrupting behavior includes spamming, flooding, threatening, or using inappropriate or abusive language.

Only the Core Facilitator may ban a user from the Sky Forum when doing so would operationally block an ongoing governance process (e.g. the user has submitted an otherwise eligible governance proposal).

###### A.2.7.1.2.1.1.1 - Public Communication Of Bans [Core]  <!-- UUID: d18821e4-cee6-41d0-91fb-b5bb963b2594 -->

The documents herein define the requirements regarding public communication of bans. The Sky Forum is subject to special requirements that are defined in [A.2.7.1.2.1.1.1.1 - Sky Forum-Specific Requirements](a3e4d767-56d1-4b1f-8ade-b733bca4244f). Requirements applicable to all other Ecosystem Communication Channels are defined in [A.2.7.1.2.1.1.1.2 - Requirements Applicable To All Other Channels](d64ffda4-097c-47f8-b497-f20e7456b7fa).

###### A.2.7.1.2.1.1.1.1 - Sky Forum-Specific Requirements [Core]  <!-- UUID: a3e4d767-56d1-4b1f-8ade-b733bca4244f -->

For the Sky Forum, the Core Facilitator must publicly communicate the ban and the reasons for banning a user if the ban interrupts the users' exercise of a governance process.

In all other cases involving the Sky Forum, responsible moderators may exercise their best judgment in determining whether to publicly communicate a ban and the reasons for a ban. In doing so, the responsible moderators should consider the importance of transparency and community awareness as well as whether the banned user has engaged in egregiously misaligned and disrupting behavior. In every case, the moderators must still use the built-in forum functionality to register the ban reason for every banned user so that all forum users can see it when visiting the forum profile of the banned user.

If it is assessed that a public communication is necessary, the Core Facilitator is responsible for writing and publishing it.

###### A.2.7.1.2.1.1.1.2 - Requirements Applicable To All Other Channels [Core]  <!-- UUID: d64ffda4-097c-47f8-b497-f20e7456b7fa -->

For all Ecosystem Communication Channels other than the Sky Forum, the responsible moderators may exercise their discretion in determining whether to publicly communicate a ban and the reasons for the ban.

###### A.2.7.1.2.1.1.2 - Use Of Automated Tools [Core]  <!-- UUID: 76247105-be57-4eac-9eb4-793947a43d67 -->

Responsible moderators may use automated tools, including AI and bots, to help fulfill their moderation responsibilities. The responsible moderators retain responsibility for ensuring that these tools conform to moderation policies and must establish a process through which automated decisions can be reviewed by the responsible moderators.

###### A.2.7.1.2.1.1.3 - Unbanning [Core]  <!-- UUID: 4d4a1d9a-c8c7-4c2b-aaec-33e382790d52 -->

Bannings are by default permanent. However, Ranked Delegates can propose the unbanning of users by publishing a forum post that states the handle(s) of the user(s) whose unbanning they request and the rationale for their unbanning. The forum post must tag the Core Facilitator, who will in turn prepare a binary Governance Poll through the Operational Weekly Cycle to be published on the Voting Portal as soon as reasonably possible. The outcome of the Governance Poll is binding.

Where identity can be proven, the ban on unbanned users will be lifted across all communication channels.

###### A.2.7.1.2.1.1.4 - Intrinsic Limitations [Core]  <!-- UUID: 9e2d25b0-227c-4f08-a466-c99dc7243d92 -->

Given the digital nature of these communication channels and the consequent practical unenforceability of permanent bannings, responsible moderators are expected to have to deal with recurring banned users under new aliases. Responsible moderators must exercise best judgement when suspecting a user to be a banned user under a different guise and when assessing whether they pose a risk of recidivism.

##### A.2.7.1.2.2 - List of Responsible Moderators [Core]  <!-- UUID: 1f76a652-0958-4165-8183-51c9eaccdbaa -->

The responsible moderators for each communication channel are:

- Sky Forum - The Core Facilitator
- Sky and Sky Builder Discord - The Core Facilitator and Ecosystem Actor TechOps Services
- Sky X / Twitter Account - Ecosystem Actor Maker Growth
- MakerDAO Subreddit - Ecosystem Actor Maker Growth

#### A.2.7.1.3 - Communications Infrastructure Budget [Core]  <!-- UUID: 72d16b65-95cf-4cff-a2f4-71ce92019f84 -->

The ecosystem communication infrastructure budget is 0 USDS per quarter.

## A.2.8 - Ecosystem Accords [Article]  <!-- UUID: 104c3543-ce94-4a2f-9968-57f1ee858085 -->

This Article governs Ecosystem Accords, agreements between actors in the Sky Ecosystem that are enforceable by Sky Governance.

### A.2.8.1 - Dispute Resolution [Section]  <!-- UUID: f4d827e9-bf60-4180-a1d0-446af1245365 -->

This Section defines the process for resolving disputes regarding Ecosystem Accords.

#### A.2.8.1.1 - Dispute Resolution By Core Council [Core]  <!-- UUID: 82a04a56-8cc9-4adf-9714-da246d541371 -->

Disputes regarding Ecosystem Accords are resolved by the Core Council as specified in the documents herein.

##### A.2.8.1.1.1 - Roles [Core]  <!-- UUID: 4973a9b8-66f1-4486-829e-6c9464b9407c -->

The documents herein define the respective roles of Core GovOps and the Core Facilitator in resolving disputes.

###### A.2.8.1.1.1.1 - Role Of Core GovOps [Core]  <!-- UUID: 59ca12d1-a25c-4974-90d9-ccf7dae184f3 -->

Core GovOps manages the overall dispute resolution process, including establishing communication channels for dispute resolution, communicating with the parties, and gathering and analyzing information relating to the dispute.

###### A.2.8.1.1.1.2 - Role Of Core Facilitator [Core]  <!-- UUID: cf7e0654-f9a6-45e4-9984-14387067cb17 -->

The Core Facilitator decides how the dispute is ultimately resolved. The Core Facilitator is isolated from the parties to maintain impartiality. The Core Facilitator exclusively reviews the information prepared by Core GovOps and delivers a decision to Core GovOps, which communicates it to the parties.

##### A.2.8.1.1.2 - Process Definition [Core]  <!-- UUID: 6151ee33-ff22-4bda-955b-f3731ab9b522 -->

The documents herein define the process for resolving disputes.

###### A.2.8.1.1.2.1 - Dispute Intake [Core]  <!-- UUID: 8bf58bdf-4a6f-4e8b-9829-7e375719ad4a -->

The documents herein define the process for dispute intake for dispute resolution.

###### A.2.8.1.1.2.1.1 - Formal Request For Dispute Resolution [Core]  <!-- UUID: 3f43d965-56e4-4153-a59a-00329e3b00e5 -->

The dispute resolution process begins with an actor in the Sky Ecosystem requesting formal dispute resolution from Core GovOps.

###### A.2.8.1.1.2.1.2 - Preliminary Determination Of Reasonableness By Core GovOps [Core]  <!-- UUID: c2f9e098-b0f5-44ae-b44d-a9481707b787 -->

After receiving the request for dispute resolution, Core GovOps makes a brief preliminary determination regarding whether the request is reasonable (i.e. not vexatious or frivolous), within three (3) working days.

###### A.2.8.1.1.2.1.3 - Handling Of Unreasonable Requests [Core]  <!-- UUID: 7765da19-eae7-4b76-b9e0-155b251be3c7 -->

If Core GovOps determines that the request for dispute resolution is not reasonable, it will inform the actor who submitted the request accordingly, providing their reasons. In this case, there is no further action.

###### A.2.8.1.1.2.1.4 - Handling Of Reasonable Requests [Core]  <!-- UUID: f26cc457-75eb-4b42-9ac0-55fe3d6fcb43 -->

If Core GovOps makes a determination that the request is reasonable, then Core GovOps formally begins the dispute resolution process by notifying all relevant parties that the process is about to begin. The notifications to each party will outline the process to be followed, including relevant steps and timeframes that the party should be aware of.

###### A.2.8.1.1.2.2 - Presentation Of Arguments [Core]  <!-- UUID: f08ccecb-88cc-4d28-8a62-8be9f3b8d19b -->

The documents herein define the process for the presentation of arguments for dispute resolution.

###### A.2.8.1.1.2.2.1 - Statement Of Problem [Core]  <!-- UUID: 550f5cfb-0f3d-4b05-8e86-80315d4f135a -->

The party that initiated the dispute resolution process has five (5) working days from the formal initiation of the process to submit a Statement of Problem, laying out the facts they consider relevant to the dispute and the issues related to the Atlas as they see them.

###### A.2.8.1.1.2.2.2 - Statement Of Response [Core]  <!-- UUID: a1e21e2a-be88-4041-9204-0c2936e693d7 -->

Core GovOps provides the Statement of Problem to the other party/parties. They have five (5) working days to submit a Statement of Response, which sets out their perspective on the relevant facts and issues in the dispute.

###### A.2.8.1.1.2.2.3 - Statement Of Rebuttal [Core]  <!-- UUID: cedc6a69-da33-421a-a090-2cae2f0e7185 -->

Core GovOps provides the Statement of Response to the party that initiated the dispute resolution process. They have three (3) working days to submit a Statement of Rebuttal.

###### A.2.8.1.1.2.3 - Decision [Core]  <!-- UUID: 262a79a0-c5be-4721-ab27-ba7ba45776c5 -->

The documents herein define the decision process for dispute resolution.

###### A.2.8.1.1.2.3.1 - Analysis By Core GovOps [Core]  <!-- UUID: 5594d477-159c-4baf-86dd-3d5f0c1d857b -->

Core GovOps prepares a confidential analysis of the dispute for the Core Facilitator. This analysis must include a summary of all relevant facts as far as it is possible to ascertain, clear identification of any areas of factual ambiguity or disagreement between the parties, a structured presentation of the arguments in favor of each party, and a recommendation if Core GovOps believes one conclusion is clearly supported by the facts.

###### A.2.8.1.1.2.3.2 - Adjudication By Core Facilitator [Core]  <!-- UUID: 056774ab-b584-4f37-90f4-9c17b79ddfb3 -->

The Core Facilitator reviews the analysis prepared by Core GovOps along with the arguments presented by the parties and reaches a decision within three (3) working days.

The Core Facilitator must draft a decision setting out relevant facts and the core reasoning of their decision. In doing so, the Core Facilitator is free to adopt arguments presented by the parties, by Core GovOps, or to advance their own analysis.

###### A.2.8.1.1.2.3.3 - Release Of Decision [Core]  <!-- UUID: c172684d-9564-40f9-8d47-82d736a3d876 -->

The Core Facilitator communicates their decision to Core GovOps. Core GovOps communicates the decision to all related parties.

###### A.2.8.1.1.2.3.4 - Publication Of Decision [Core]  <!-- UUID: 5e4b0330-1469-4fb0-9622-6bf32b8c6afa -->

The Core Facilitator publishes the decision on the Sky Forum and updates the [A.2.8.1.2.0.6.1 - Dispute Resolutions](c48614bb-6f51-4de7-97bd-ef1fed968d72) Active Data document in the Atlas, redacting any confidential information as needed.

#### A.2.8.1.2 - Dispute Resolution Recording [Active Data Controller]  <!-- UUID: e6384df7-246b-4240-93e8-01bf903e072d -->

Resolutions of disputes involving Ecosystem Accords are defined as Active Data in [A.2.8.1.2.0.6.1 - Dispute Resolutions](c48614bb-6f51-4de7-97bd-ef1fed968d72).

The Active Data is updated as follows:

- The Responsible Party is the Core Facilitator.
- The Update Process must follow the protocol for ‘Direct Edit’.

##### A.2.8.1.2.0.6.1 - Dispute Resolutions [Active Data]  <!-- UUID: c48614bb-6f51-4de7-97bd-ef1fed968d72 -->

The resolutions of disputes regarding Ecosystem Accords are:

- **Dispute Between Spark And Grove Regarding Effective Date Of Their Ecosystem Accord** (September 2, 2025) - [Facilitator Decision on Grove/Spark Dispute](https://forum.skyeco.com/t/facilitator-decision-on-grove-spark-dispute/27141)

### A.2.8.2 - Active Ecosystem Accords [Section]  <!-- UUID: be46648d-a154-480a-b202-81fd1ac735d2 -->

The subdocuments herein record currently active Ecosystem Accords.

#### A.2.8.2.1 - Ecosystem Accord 1: Grove And Spark Agents [Core]  <!-- UUID: 9ca40096-937e-431e-af50-9ecd50c0d0a8 -->

The subdocuments herein record the terms of agreement between Grove and Spark as agreed in Ecosystem Accord 1.

##### A.2.8.2.1.1 - Accord Key Details [Core]  <!-- UUID: 4512c23a-2b01-4a38-ad02-9a016e1d0c54 -->

The subdocuments herein set out the key details of Ecosystem Accord 1, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.1.1.1 - Parties To The Accord [Core]  <!-- UUID: 817d9d87-9659-43b5-80ce-8f68b592a625 -->

The Grove and Spark Agents are the parties to Ecosystem Accord 1. These parties are also referred to as Grove and Spark, respectively, in the terms of this Accord.

###### A.2.8.2.1.1.2 - Duration Of The Accord [Core]  <!-- UUID: c2fe6ab2-bec3-48d3-b4b1-9f93cd97f693 -->

The duration of Ecosystem Accord 1 is six (6) months, commencing from May 29, 2025.

##### A.2.8.2.1.2 - Accord Substantive Terms [Core]  <!-- UUID: a20cefff-cd64-4c01-93e0-052915759938 -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 1.

###### A.2.8.2.1.2.1 - Revenue Share [Core]  <!-- UUID: 25743b88-dead-47fe-bd81-b709e69f5949 -->

Grove and Spark agree to a bilateral revenue share, up to 40% maximum with JRC rental, see [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

###### A.2.8.2.1.2.1.1 - Revenue Share Definition [Core]  <!-- UUID: 66089224-1a28-475f-9276-ed2bd956e48e -->

Each Agent retains the right to force the other Prime Agent to do revenue sharing up to 40% by providing that Prime with rented JRC. Sharing is done on the net revenue after deducting the cost to Sky. This is only considered on the spread earned on USDS debt, including any subsidy amounts.

###### A.2.8.2.1.2.2 - Grove Agent Exclusivity [Core]  <!-- UUID: 76d646ca-be88-47e5-b9c6-943155fe2fb1 -->

Grove exclusivity includes Real World Assets (RWAs), which exclusivity does not extend to Treasuries used for ASC purposes or stablecoin liquidity provisioning.

###### A.2.8.2.1.2.3 - Spark Agent Exclusivity [Core]  <!-- UUID: e979e76f-e970-45de-bddb-38c86ac3c007 -->

Spark Agent exclusivity includes Maple, cryptocurrency OTC lending, and Established DeFi Lending Protocols, as defined in [A.2.8.2.1.2.3.1 - Established DeFi Lending Protocol Definition](0d74de1b-bb46-4286-bcbf-d260d1204465).

###### A.2.8.2.1.2.3.1 - Established DeFi Lending Protocol Definition [Core]  <!-- UUID: 0d74de1b-bb46-4286-bcbf-d260d1204465 -->

Established DeFi Lending Protocols are defined as DeFi lending protocols deployed six months ago or earlier.

###### A.2.8.2.1.2.4 - Right Of First Refusal [Core]  <!-- UUID: 8d64aa84-ae79-4bde-ae94-5dd7c18d3019 -->

Grove provides the Spark Agent with a right of first refusal for DeFi opportunities on unclaimed chains and new protocols, including bootstrapping incentive programs.

###### A.2.8.2.1.2.4.1 - DeFi Opportunities Right of First Refusal Duration [Core]  <!-- UUID: 0db1525d-bcce-469a-b414-65b41669432d -->

Grove provides the Spark Agent a right of first refusal for pursuing cross-chain bootstrapping opportunities, which lasts four weeks after notification by Grove. If Spark does not wish to deploy SparkLend or provide capital to the protocol in question, Grove retains the right to pursue the opportunity pending security and risk assessments of the target protocol. Upon written notification from Grove of a new DeFi opportunity via a communications channel mutually agreed by the parties, Spark has four weeks to decide whether it wants to deploy SparkLend or lend to the target chain and protocol. If Spark opts not to do so by the end of the four-week period, Grove is permitted to pursue the opportunity.

_Example:__ A lending protocol (i.e. Aave, Euler, Morpho, etc) plans on deploying on blockchain X. Grove provides written notification to Spark about the potential new deployment. Spark evaluates the opportunity and decides there are better opportunities to pursue. The opportunity reverts to Grove after Spark’s refusal; or, if Spark does not issue a formal refusal, the opportunity reverts to Grove after four weeks._

###### A.2.8.2.1.2.4.2 - DeFi Opportunities Complementary Deployments [Core]  <!-- UUID: 41ad5689-6679-4129-a24d-aa50334e1f26 -->

Grove and Spark may combine efforts if there is a large enough cross-chain opportunity. For example, Grove may deploy stablecoin liquidity on a target chain and Spark may deploy a SparkLend instance. In this case, complementary efforts are made to mutually benefit the cross-chain deployment, with significant economic benefits received by both parties. This chain would also serve as a new distribution channel for Spark, Grove, and Sky products.

###### A.2.8.2.1.2.5 - ASC Provision [Core]  <!-- UUID: 72bad98d-007c-4247-98ba-daeb1c8130b4 -->

Grove retains the right to deploy into repo lending protocols to meet ASC requirements. Deposits must be capped at the lower of either 10% of protocol USDC deposits or the Minimum Actively Stabilizing Collateral, as defined in [A.3.3.2.2 - Minimum Actively Stabilizing Collateral](475fe222-9e4a-4e9d-9be6-a7a424ce02f8). The Spark Agent retains the right to use the PSM for ASC, provided it covers the cost to Grove.

###### A.2.8.2.1.2.6 - Treasuries Provision [Core]  <!-- UUID: 11ad7c74-6163-452c-acf0-a70af3396d03 -->

The Spark Agent retains the right to deploy into tokenized US Treasury Bills to meet ASC requirements.

###### A.2.8.2.1.2.7 - Basis Trade Products [Core]  <!-- UUID: d1a4398c-aa95-462b-a212-d2afc047477b -->

Basis trade products are available to both Grove and Spark.

###### A.2.8.2.1.2.8 - Grand Prix Airdrops [Core]  <!-- UUID: 784feda7-d69e-4ed3-97c3-95b70314b44e -->

Grove receives any airdrops from the Grand Prix.

###### A.2.8.2.1.2.9 - USDe and sUSDe Revenue Share [Core]  <!-- UUID: 56589ad5-4e8e-4af9-926a-fadca7bfa0e3 -->

Spark and Grove agree to share revenue from USDe and sUSDe as specified in the subdocuments herein.

###### A.2.8.2.1.2.9.1 - Revenue Share [Core]  <!-- UUID: 7d16afc8-0eb4-40db-81aa-915a7f052859 -->

Spark and Grove will share 50% of all revenue and expenses associated with Spark’s Allocation System investments in USDe and sUSDe. Revenue includes (1) protocol yield on the amount deployed into these assets, (2) any OTC or negotiated arrangements, payments, or incentives, and (3) manual payments or rebates related to withdrawal activity. Expenses include all costs associated with Spark’s investment in USDe and sUSDe, including mint / burn fees, swap fees, and costs of borrowing funds from Sky.

###### A.2.8.2.1.2.9.2 - Risk Capital Share [Core]  <!-- UUID: ac648f96-3b0d-46c6-9501-a3a88da26961 -->

Grove agrees to rent to Spark 50% of the Required Risk Capital associated with Spark’s investments in USDe and sUSDe as a Junior Risk Capital Rental. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

###### A.2.8.2.1.2.9.2.1 - Implementation [Core]  <!-- UUID: 2bb81311-e501-4d0d-b403-f4c619463538 -->

Spark and Grove expressly intend that Grove shares in 50% of the risks of Spark’s investment in USDe and sUSDe and not in the risk of any other investments by Spark.

To the extent that USDe or sUSDe investments experience losses and Spark is allocated a greater than 50% share of those losses relative to Grove under the TIP JRC mechanism (see [A.3.2.1.2.2.1.2.1 - Initial Loss Absorption By "Tip JRC"](6c33bcf5-c29d-48ca-9ee5-e37dcdeb0630)), Grove will transfer funds to Spark so that Grove and Spark each bear 50% of the losses that occur.

To the extent that Spark experiences losses on investments other than USDe or sUSDe and a portion of those losses is allocated to the Junior Risk Capital rented from Grove, Spark shall reimburse Grove for those losses.

###### A.2.8.2.1.2.9.3 - Term [Core]  <!-- UUID: a768dda1-1075-4762-a904-c523687cbe6c -->

This revenue share shall be effective retroactively, dated back to the launch of Spark’s allocation into USDe and sUSDe beginning the week of July 14, 2025.
It shall remain in effect until one of the following conditions is met, whichever occurs first:

1. Grove begins to allocate capital to USDe or sUSDe directly; or
2. Spark or Grove terminates the revenue share, with reasonable advance notice to the other party.

Any changes to the structure or scope of this arrangement will be discussed transparently and approved by both Spark and Grove.

###### A.2.8.2.1.2.10 - Maple syrupUSDC Transfer [Core]  <!-- UUID: da2c6b16-363f-4741-a9ab-0838506a0429 -->

Grove will transfer the syrupUSDC it currently holds to Spark, and Spark will transfer the equivalent value in USDS to the Grove ALM Proxy.

#### A.2.8.2.2 - Prime Program [Core]  <!-- UUID: aa3b8e65-0ded-48c2-9c40-812debf99f32 -->

The subdocuments herein record the terms of agreement between Sky, Grove, and Spark as agreed in Ecosystem Accord 2.

##### A.2.8.2.2.1 - Accord Key Details [Core]  <!-- UUID: a9f4941d-9d07-4191-a8c6-f1cb25a067cc -->

The subdocuments herein set out the key details of Ecosystem Accord 2, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.2.1.1 - Parties To The Accord [Core]  <!-- UUID: fea17abc-79b6-4b49-81c0-258b303eafe9 -->

The parties to Ecosystem Accord 2 are Sky, Spark, Grove, and Moonbow, as defined in the subdocuments herein.

###### A.2.8.2.2.1.1.1 - Sky Details [Core]  <!-- UUID: 2916297b-e460-409b-85e1-6e1b6d431b98 -->

The party ‘Sky’ comprises Sky Core.

###### A.2.8.2.2.1.1.2 - Spark Details [Core]  <!-- UUID: d40acd19-773c-479f-837a-0291c8b9fcde -->

The party ‘Spark’ comprises the Spark Prime Agent, Spark Foundation, and Phoenix Labs.

###### A.2.8.2.2.1.1.3 - Grove Details [Core]  <!-- UUID: ccc2c16a-68a6-4182-a1a4-4f666a8bce2f -->

The party ‘Grove’ comprises the Grove Prime Agent, and Grove Foundation.

###### A.2.8.2.2.1.1.4 - Moonbow Details [Core]  <!-- UUID: eb3b0811-8b84-4216-ae3e-ac2181935204 -->

The party ‘Moonbow’ is the entity owning relevant intellectual property.

###### A.2.8.2.2.1.2 - Duration Of The Accord [Core]  <!-- UUID: f68cf0ec-47bb-45d7-80a8-3b28f9e8dd1c -->

The duration of Ecosystem Accord 2 is indefinite, commencing from May 29, 2025.

##### A.2.8.2.2.2 - Accord Substantive Terms [Core]  <!-- UUID: ffb7dab9-a276-4968-ab49-f5783250120a -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 2.

###### A.2.8.2.2.2.1 - Tokenomics [Core]  <!-- UUID: ed0308bf-4a87-4c7c-b05e-3a4d46b68a13 -->

The subdocuments herein set out agreed terms with respect to tokenomics.

###### A.2.8.2.2.2.1.1 - Total Token Supply [Core]  <!-- UUID: 63684d7c-09f4-48ab-9daa-f3bb0aac6f28 -->

The total token supply of each of the SPK and GROVE tokens shall be 10,000,000,000 (ten billion).

###### A.2.8.2.2.2.1.2 - Token Allocations [Core]  <!-- UUID: cfac7e47-d20e-4b52-8d25-9ec418bd2c96 -->

Specific token allocations are defined in the subdocuments herein.

###### A.2.8.2.2.2.1.2.1 - Grove Prime Treasury [Core]  <!-- UUID: 9d7a2d3f-3079-4d3b-be89-e06966aec07c -->

3,000,000,000 GROVE tokens are allocated to the Grove Foundation, with an option to further increase this allocation by 5% (500,000,000 tokens). The additional 5% will be distributed to relevant stakeholders / users from Sky’s allocation of GROVE tokens, but that distribution will happen from the Grove Foundation. This distribution plan must be approved by Sky before the transfer.

###### A.2.8.2.2.2.1.2.2 - Sky Retained Tokens And Reward Pools [Core]  <!-- UUID: fb447af6-1581-4711-b73c-dc2e8d65e843 -->

Sky retains 7,000,000,000 GROVE tokens and 6,500,000,000 SPK tokens. These tokens are distributed as token rewards over time as determined by Sky Governance.

###### A.2.8.2.2.2.1.2.2.1 - Grove Token Reward Distribution Schedule [Core]  <!-- UUID: 5b43f4d8-9728-411c-92c7-a7ebaf368ca0 -->

A portion of the GROVE tokens held by Sky are distributed to USDS users as specified in the table below. All other GROVE tokens held by Sky are reserved for future token rewards as determined by Sky Governance.

| Year | Tokens for USDS Users  |
|------|------------------------|
| 1    | 1,225,000,000          |
| 2    | 1,225,000,000          |
| 3    | 612,500,000            |
| 4    | 612,500,000            |
| 5    | 306,250,000            |
| 6    | 306,250,000            |
| 7    | 153,125,000            |
| 8    | 153,125,000            |
| 9    | 153,125,000            |
| 10   | 153,125,000            |
| Total| 4,900,000,000          |

###### A.2.8.2.2.2.1.2.2.2 - Spark Token Reward Distribution Schedule [Core]  <!-- UUID: 1f412288-af14-4aab-84e9-79f2e0c39100 -->

A portion of the SPK tokens held by Sky are distributed to USDS users as specified in the table below. All other SPK tokens held by Sky are reserved for future token rewards as determined by Sky Governance.

| Year | Tokens for USDS Users  |
|------|------------------------|
| 1    | 1,137,500,000          |
| 2    | 1,137,500,000          |
| 3    | 568,750,000            |
| 4    | 568,750,000            |
| 5    | 284,375,000            |
| 6    | 284,375,000            |
| 7    | 142,187,500            |
| 8    | 142,187,500            |
| 9    | 142,187,500            |
| 10   | 142,187,500            |
| Total| 4,550,000,000          |

###### A.2.8.2.2.2.1.3 - Transfer Limit [Core]  <!-- UUID: da03bcb0-734a-4d36-ab0e-e42a43e23d8a -->

Transfer limits for Spark and Grove are specified in the subdocuments herein.

###### A.2.8.2.2.2.1.3.1 - Spark Transfer Limit [Core]  <!-- UUID: ce04d270-d9e1-46e2-9cfc-a122b03e923c -->

A maximum of 1,000,000,000 tokens can be transferred by Spark to the Spark Foundation in the first year for the purpose of rewarding contributors, and 500,000,000 tokens per year thereafter for the purpose of rewarding contributors.

###### A.2.8.2.2.2.1.3.2 - Grove Transfer Limit [Core]  <!-- UUID: 2a1c77ee-de95-415e-b93b-3505d3bd32d5 -->

Grove may transfer its contributor allocation, in whole or in part, to its operating entities, foundations, or affiliated entities in advance of contributor distribution. Tokens allocated for contributor compensation may be granted to contributors upfront, subject to vesting, forfeiture, and clawback arrangements that are consistent with the vesting schedules and distribution parameters set forth in this Atlas.

A maximum of 1,000,000,000 tokens for Grove may vest or otherwise be released into circulation for contributor compensation purposes in the first year, and a maximum of 500,000,000 tokens per year for Grove may vest or otherwise be released into circulation thereafter. Tokens that are unvested or subject to forfeiture shall not be considered distributed, released, or in circulation.

###### A.2.8.2.2.2.1.4 - Prime Token Generation Event [Core]  <!-- UUID: c00b9dad-06d6-4e91-bfb2-7f5afa0bc47e -->

The respective Prime Foundations for Spark and Grove, or one of their subsidiaries or affiliate companies, will conduct the token generation event. In the token generation event, the Agent tokens will be split and sent to the Prime SubProxy and Sky Proxy. In this process, Sky will receive a universal override over the Prime Agent Token in question.

###### A.2.8.2.2.2.2 - Borrowing Capacity And Mechanism [Core]  <!-- UUID: 2c6034e7-d716-4d36-8063-d893c23fc34a -->

The subdocuments herein set out agreed terms with respect to borrowing capacity and the borrow rate mechanism.

###### A.2.8.2.2.2.2.1 - Subsidized Borrowing [Core]  <!-- UUID: 552e7b01-c2d0-4658-ac49-2c74e230aeac -->

Both Spark and Grove are entitled to borrow up to 1,000,000,000 USDS from Sky at a subsidized rate for an initial period of 2 years, beginning January 1, 2026. This subsidized rate is set out in [A.2.8.2.2.2.2.2 - Borrow Rate Mechanism](f97cc4c7-d0d5-47fc-9f86-c00824ae6d7f).

###### A.2.8.2.2.2.2.2 - Borrow Rate Mechanism [Core]  <!-- UUID: f97cc4c7-d0d5-47fc-9f86-c00824ae6d7f -->

The borrow rate subsidy for Spark and Grove will be calculated according to the formula: `SOFR + ((Base_Rate - SOFR) * T/24)`, where SOFR is specified in [A.3.3.2.2.4.1.3 - Secured Overnight Financing Rate](2edd1333-6ca6-4c10-9d71-80b85d4a4265), T represents elapsed months and is a counter that increases monthly over the two (2) year period specified in [A.2.8.2.2.2.2.1 - Subsidized Borrowing](552e7b01-c2d0-4658-ac49-2c74e230aeac), and T is equal to zero (0) for the first month of that period.

###### A.2.8.2.2.2.2.3 - Base Rate [Core]  <!-- UUID: fd39df25-6093-49ae-be12-36df34754612 -->

The Base Rate will be dynamic and aligned with the SSR (Sky Savings Rate).

###### A.2.8.2.2.2.2.4 - Minimum Borrowing Threshold for Grant Eligibility [Core]  <!-- UUID: 23b21d6f-ad66-42ff-9e9f-c5bd5da6e8d4 -->

Primes, including Spark and Grove, must each maintain a minimum borrowing of 1,000,000,000 USDS from Sky at all times to remain eligible for the full monthly reimbursement grant. If the amount borrowed falls below this threshold, the reimbursement grant will be proportionately slashed. This grant will cover the difference between the borrowing Base Rate and SOFR, as specified in [A.3.3.2.2.4.1.3 - Secured Overnight Financing Rate](2edd1333-6ca6-4c10-9d71-80b85d4a4265). Spark and Grove can borrow amounts exceeding the 1,000,000,000 USDS limit at the prevailing Base Rate.

###### A.2.8.2.2.2.2.5 - Borrowing Above Subsidized Limit [Core]  <!-- UUID: c04dcedd-5e17-412f-8a71-55a76c29b80d -->

Spark and Grove can borrow amounts exceeding the 1,000,000,000 USDS limit at the prevailing Base Rate.

###### A.2.8.2.2.2.2.6 - Recourse [Core]  <!-- UUID: daf0ea35-23cb-4550-88f9-7da59027d262 -->

Sky’s recourse for bad debt consists of (1) minting Prime Agent tokens; (2) terminating a Prime’s right to further borrowing; and (3) activation of the Resolution Mechanism which includes, without limitation, the authority to suspend all protocol operations, seize or reallocate all of the Prime assets, override or disable smart contract functions, initiate managed restructuring, or execute full and permanent liquidation of the affected sub-protocol and all of its assets, in order to contain risk and preserve the stability and solvency of the broader ecosystem.

###### A.2.8.2.2.2.3 - Distribution Reward [Core]  <!-- UUID: 85b8e871-2d42-4a85-a887-c33d860bed64 -->

The subdocuments herein set out agreed terms with respect to the Distribution Reward.

###### A.2.8.2.2.2.3.1 - Distribution Reward Rate [Core]  <!-- UUID: 8e3cde6b-3b8b-4e9a-b9a0-8c24d84881f6 -->

The standard Distribution Reward rate is set at 0.2%.

###### A.2.8.2.2.2.3.2 - 2025 Bonus [Core]  <!-- UUID: 7ca440d3-03fb-4fba-81a8-d2118dc47aa6 -->

An additional 0.4% Distribution Reward bonus will apply during the calendar year 2025 (ending December 31, 2025). This bonus is strictly limited to the Prime and does not extend to the Prime Foundation. The bonus is subject to the limitation specified in [A.2.8.2.2.2.3.2.1 - Bonus Limitation](6996e6c9-b936-4680-855f-b9717572082d).

###### A.2.8.2.2.2.3.2.1 - Bonus Limitation [Core]  <!-- UUID: 6996e6c9-b936-4680-855f-b9717572082d -->

USDS and sUSDS balances held by the Prime itself are not eligible for the Distribution Reward bonus specified in [A.2.8.2.2.2.3.2 - 2025 Bonus](7ca440d3-03fb-4fba-81a8-d2118dc47aa6).

###### A.2.8.2.2.2.3.3 - Sky Spread [Core]  <!-- UUID: 5e3e9338-221a-461a-96f9-01e0665ab6a4 -->

The Sky Spread (see [A.3.1.2.6 - Sky Spread](e1b694de-1ee3-4502-a9c9-52eea9539804)) forms part of the overall differential between the Savings Rate and the Base Rate, representing the premium earned by Sky for facilitating the ecosystem’s financing.

###### A.2.8.2.2.2.4 - Genesis Capital Allocation [Core]  <!-- UUID: 23149a25-19a1-4d8f-b4ce-ea4b2adc2e21 -->

The subdocuments herein set out agreed terms with respect to genesis capital allocations.

###### A.2.8.2.2.2.4.1 - Spark Initial Allocation [Core]  <!-- UUID: a339b1d7-34a9-40bd-b452-a86e149f07f7 -->

The Initial Allocation for Spark is 25,000,000 USDS.

###### A.2.8.2.2.2.4.2 - Grove Initial Allocation [Core]  <!-- UUID: 062fdb39-464e-4a5b-a44f-3462d2d38be5 -->

The Initial Allocation for Grove is 25,000,000 USDS.

###### A.2.8.2.2.2.4.3 - Initial Allocation Distribution [Core]  <!-- UUID: 6b8fc0e6-ee0b-4a48-a096-2ccb06f64e3f -->

The Initial Allocation is distributed in USDS to each Prime SubProxy (i.e. the Spark SubProxy and Grove SubProxy). Both Grove and Spark elected to distribute 5% of the total token supply over a period of 20 years, lasting from year 10 to year 30, and will receive USDS 25,000,000 each.

###### A.2.8.2.2.2.4.4 - Initial Allocation Mechanism [Core]  <!-- UUID: eedd0309-b11b-459e-a966-13b16e961ccc -->

Shortly after the Agent Token launch, an Atlas Edit Proposal submitted to Sky Governance will allow the respective founding teams of Spark and Grove to propose an initial cash grant to their respective Prime Foundation. Sky Governance must consent to this initial cash grant via approving the Sky Atlas modification.

###### A.2.8.2.2.2.4.4.1 - Initial Cash Grant To Spark Foundation [Core]  <!-- UUID: 9daea2fa-0fef-48a7-8633-fa33081236da -->

The founding team of Spark has proposed a cash grant of 800,000 USDS per month to the Spark Foundation from Spark’s Genesis Capital Allocation for a three (3) month period, beginning at the time of the Genesis Capital Allocation. The purpose of the grant is to enable Spark Foundation to fulfill its purpose of promoting the growth and development of Spark. This funding will support essential activities such as engineering efforts, community engagement, research, infrastructure, and administrative operations.

Sky Governance hereby consents to this cash grant. The first month’s transfer must be made to the Spark Foundation immediately after the transfer of the Genesis Capital Allocation. See [A.2.8.2.2.2.7.2.1 - Transfer Of Genesis Capital Allocation To Spark SubProxy](e3ec99ec-54c9-4fe7-8104-aee20c57ec57). Transfers for subsequent months will be made proportionally in Spark Spells included in Sky Executive Votes unless otherwise agreed by Sky and Spark.

###### A.2.8.2.2.2.4.5 - Subsequent Allocation Mechanism [Core]  <!-- UUID: aea8a2d8-2203-4123-8c09-17b2bb8427c1 -->

After the initial cash grant (see [A.2.8.2.2.2.4.4 - Initial Allocation Mechanism](eedd0309-b11b-459e-a966-13b16e961ccc)), Spark and Grove may request additional grants to their respective Prime Foundations to fund operations and growth.

The authorization of grant requests is subject to the governance requirements and limitations specified in [A.2.2.6.2.3.1 - Limitations On Usage Of Root Edit Primitive Prior To Independent Governance](8c15762a-ea7e-4c6d-9089-60d30c219c0f).

In all instances, Sky Governance must consent to the transfer of funds via an Atlas Edit.

###### A.2.8.2.2.2.4.5.1 - Spark Foundation Grant Authorizations [Core]  <!-- UUID: 6a9a3a7a-8670-41fc-98aa-d2d9b518bdfc -->

The documents herein record Sky Governance authorizations for grants to the Spark Foundation.

###### A.2.8.2.2.2.4.5.1.1 - Spark Foundation Grant Authorization: October 2025 [Core]  <!-- UUID: 12425328-8344-4fbd-9afb-3ea6316972dd -->

The founding team of Spark has proposed a cash grant of 1,100,000 USDS per month to the Spark Foundation from Spark’s Prime Treasury for a three (3) month period, beginning on October 1, 2025. The purpose of this grant is to enable the Spark Foundation to fulfill its purpose of promoting the growth and development of Spark. This funding will support essential activities such as engineering and product development, community engagement and growth initiatives, research and governance contributions, infrastructure and operational maintenance, and administrative operations.

Sky Governance hereby consents to this cash grant. The transfer for October must be made to the Spark Foundation in a Spark Spell included in the October 2, 2025 Executive Vote. Transfers for subsequent months will be made proportionally in Spark Spells included in Sky Executive Votes unless otherwise agreed by Sky and Spark.

###### A.2.8.2.2.2.4.5.1.2 - Spark Foundation Grant Authorization: December 2025 [Core]  <!-- UUID: bd9673db-225e-42f4-8f26-6e993dc72bd0 -->

The founding team of Spark has proposed a cash grant of 1,100,000 USDS per month to the Spark Foundation from Spark's Prime Treasury for a three (3) month period to cover Q1 2026 Foundation expenses. Additionally, a one-time grant of 150,000 USDS has been proposed to cover expenses for Spark Asset Foundation for Q1 2026 (see [https://forum.skyeco.com/t/december-11-2025-proposed-changes-to-spark-for-upcoming-spell/27481](https://forum.skyeco.com/t/december-11-2025-proposed-changes-to-spark-for-upcoming-spell/27481)).

Sky Governance hereby consents to these grants and authorizes the execution of the associated funding payloads as specified in the referenced proposal.

###### A.2.8.2.2.2.4.5.1.3 - Spark Foundation Grant Authorization: Q2 2026 [Core]  <!-- UUID: b69158da-476a-4d4b-b7ef-2f8b96b73d23 -->

The founding team of Spark has proposed a cash grant of 1,100,000 USDS per month to the Spark Foundation from Spark's Prime Treasury for a three (3) month period to cover Q2 2026 Spark Foundation expenses. Additionally, a grant of 100,000 USDS per month to the Spark Asset Foundation from Spark's Prime Treasury for a three (3) month period to cover Q2 2026 Spark Asset Foundation expenses (see [https://forum.skyeco.com/t/march-26-2026-proposed-changes-to-spark-for-upcoming-spell/27770](https://forum.skyeco.com/t/march-26-2026-proposed-changes-to-spark-for-upcoming-spell/27770)).

Sky Governance hereby consents to these grants and authorizes the execution of the associated funding payloads as specified in the referenced proposal.

###### A.2.8.2.2.2.4.5.1.4 - Spark Foundation Grant Authorization: Q3 2026 [Core]  <!-- UUID: 8dd2eb27-a760-4287-89cf-7b5bdb0c5d7c -->

The founding team of Spark has proposed a cash grant of 1,100,000 USDS per month to the Spark Foundation from Spark's Prime Treasury for a three (3) month period to cover Q3 2026 Spark Foundation expenses. Additionally, the founding team of Spark has proposed a grant of 155,000 USDS per month to the Spark Asset Foundation from Spark's Prime Treasury for a three (3) month period to cover Q3 2026 Spark Asset Foundation expenses (see [https://forum.skyeco.com/t/june-18-2026-proposed-changes-to-spark-for-upcoming-spell/27952](https://forum.skyeco.com/t/june-18-2026-proposed-changes-to-spark-for-upcoming-spell/27952)).

Sky Governance hereby consents to these grants and authorizes the execution of the associated funding payloads as specified in the referenced proposal.

###### A.2.8.2.2.2.4.5.2 - Grove Foundation Grant Authorizations [Core]  <!-- UUID: db86fa15-45c6-4a44-9c2a-652fd3d227b0 -->

The documents herein record Sky Governance authorizations for grants to the Grove Foundation.

###### A.2.8.2.2.2.4.5.2.1 - Grove Foundation Grant Authorization: Q2 2026 [Core]  <!-- UUID: 85f7d545-d56c-40b9-b1b4-05663cd7772a -->

The founding team of Grove has proposed a cash grant of 800,000 USDS per month to the Grove Foundation from Grove's Prime Treasury for a three (3) month period, beginning on April 1, 2026. The purpose of this grant is to enable the Grove Foundation to fulfill its purpose of promoting the growth and development of Grove. This funding will support essential activities such as engineering and product development, community engagement and growth initiatives, research and governance contributions, infrastructure and operational maintenance, and administrative operations.

Sky Governance hereby consents to this grant and authorizes the execution of the associated funding payloads. Transfers must be made to the Grove Foundation Multisig at `0xE3EC4CC359E68c9dCE15Bf667b1aD37Df54a5a42` in Grove Spells included in Sky Executive Votes unless otherwise agreed by Sky and Grove.

###### A.2.8.2.2.2.4.5.2.2 - Grove Foundation Grant Authorization: July 2026 [Core]  <!-- UUID: 7b6820d0-1fc1-49e7-839a-240c6cc7ec74 -->

The founding team of Grove has proposed a cash grant of 800,000 USDS to the Grove Foundation from Grove's Prime Treasury for July 2026. The purpose of this grant is to enable the Grove Foundation to fulfill its purpose of promoting the growth and development of Grove. This funding will support essential activities such as engineering and product development, community engagement and growth initiatives, research and governance contributions, infrastructure and operational maintenance, and administrative operations.

Sky Governance hereby consents to this grant and authorizes the execution of the associated funding payload. The transfer must be made to the Grove Foundation Multisig at `0xE3EC4CC359E68c9dCE15Bf667b1aD37Df54a5a42` in a Grove Spell included in a Sky Executive Vote unless otherwise agreed by Sky and Grove.

###### A.2.8.2.2.2.4.6 - Genesis Capital Backstop [Core]  <!-- UUID: 20e8467f-561c-4020-bd26-e6c1601fb64d -->

Each genesis capital allocation is subject to the Genesis Capital Backstop (see [A.3.7.1.6 - Genesis Capital Backstop](a9965d58-8cda-49fc-8a7f-f8cc2e0d6b98)).

###### A.2.8.2.2.2.5 - Intellectual Property [Core]  <!-- UUID: d276499a-2447-4dfb-a62b-4212c3d4b071 -->

The subdocuments herein set out agreed terms with respect to intellectual property.

###### A.2.8.2.2.2.5.1 - License Agreements [Core]  <!-- UUID: bfd79c66-ba55-46d2-a844-eaf8ef44d6d7 -->

Each Prime Foundation (i.e. the Spark Foundation and Grove Foundation) must sign a license agreement with Moonbow for all relevant intellectual property. This license agreement must contain the following terms:

- Worldwide, commercial, exclusive license, revocable for material breach (immediate revocation in severe cases, 30-day notice for non-severe cases).
- Royalty-free.
- Perpetual term, subject to termination provisions.
- Sublicensing allowed in specified cases without approval; any other sublicenses allowed only with Moonbow's explicit approval (not to be unreasonably withheld).
- Licensee responsible for IP protection and enforcement; license agreement to define specific requirements.
- Quarterly/annual reporting requirements on fraud cases and brand protection actions.
- Moonbow's right to audit (at Moonbow's cost).
- All improvements/developments belong to Moonbow.
- Monetary penalties for IP violations shall be explicitly defined in the full licensing agreement, with specific thresholds for triggering penalties to be mutually agreed and stipulated therein.
- Customary mutual indemnification and limitation of liability provisions.
- Mandatory arbitration except in case of injunctive relief.
- Other customary terms, conditions, representations and warranties.

###### A.2.8.2.2.2.5.2 - Open Source Protocol Code [Core]  <!-- UUID: fa90cec7-7b65-4798-a376-00cd8454bc0c -->

All components of code that form part of the Prime Protocols (i.e. Spark and Grove) will be open source.

###### A.2.8.2.2.2.5.3 - Financial Strategies [Core]  <!-- UUID: eb550b0a-3ffc-4a86-b8fe-9cc1f60f2a7e -->

The financial strategies implemented by the Prime Foundations (i.e. the Spark Foundation and Grove Foundation) will be closed source. Operational specifics are further defined in the subdocuments herein.

###### A.2.8.2.2.2.5.3.1 - Role Of Prime Foundation [Core]  <!-- UUID: ec0b206a-bf87-4ca8-aa7f-aa4ca1bc80f8 -->

The Prime Foundation (i.e. the Spark Foundation and Grove Foundation) will retain ownership of the code and strategies that determine how capital is allocated for its Prime. They will contract with the Development Company for the development and execution of the strategies.

###### A.2.8.2.2.2.5.3.2 - Role Of Development Company [Core]  <!-- UUID: d88e4c91-cce4-4f95-a989-ea876ccdf99b -->

The Development Company for each Prime Agent will execute the strategy and relay the results to the Operational Executor Agent.

###### A.2.8.2.2.2.5.3.3 - Role Of Operational Executor Agent [Core]  <!-- UUID: b0fc4a02-f41c-4556-b3f5-84d262ca00f2 -->

The relevant Operational Executor Agent, which is already engaged to the Prime in question, will conduct a principled compatibility analysis to ensure the strategy aligns with the Sky Atlas and the relevant Prime Artifact. Once validated, the Operational Executor Agent executes the capital allocation in question.

###### A.2.8.2.2.2.5.3.4 - Prime Tokenholder Governance Rights [Core]  <!-- UUID: 63717bcd-4696-4104-a368-eac839a7ba2b -->

To ensure accountability, Prime token holders will retain governance rights, including the ability to revoke the Operational Executor Agent’s Executor Accord through a vote if necessary.

###### A.2.8.2.2.2.6 - Peg Stability Module Management And Ownership [Core]  <!-- UUID: 63922aed-a1e4-43f2-a4a7-437b80ea6711 -->

The subdocuments herein set out agreed terms with respect to the Peg Stability Module (PSM).

###### A.2.8.2.2.2.6.1 - Current and Future Control [Core]  <!-- UUID: b66f99ce-af91-4b32-a37a-fb26d16b57c4 -->

The subdocuments herein set out details about the current control and oversight of the PSM, including the transition to ownership by Grove.

###### A.2.8.2.2.2.6.1.1 - Current Control (Until 2026) [Core]  <!-- UUID: 815fc554-c019-49b1-8b97-9eb62082cb5b -->

The Peg Stability Module (PSM) remains directly managed and controlled by Sky until the full deployment and operationalization of the Actively Stabilizing Collateral (ASC) system. Sky retains responsibility for setting debt ceilings, determining liquidity levels, and overseeing asset management activities within the PSM during this period.

###### A.2.8.2.2.2.6.1.2 - Transition to Grove (2025) [Core]  <!-- UUID: 08896aa0-140a-4289-9027-1772a0109a35 -->

Beginning in 2025, Grove shall assume operational and accounting ownership of the PSM, incorporating the PSM’s assets into its total value locked (TVL). Sky maintains active oversight and retains final control over strategic and operational decision-making within the PSM until full ASC implementation occurs.

###### A.2.8.2.2.2.6.2 - Operational Responsibilities [Core]  <!-- UUID: 704ccd85-e80e-478f-ab73-23d775968ca7 -->

The subdocuments herein set out details about operational responsibilities relating to the PSM.

###### A.2.8.2.2.2.6.2.1 - Base Rate Obligation [Core]  <!-- UUID: ff46baec-15da-4bf7-be18-e145f1809cf6 -->

Grove will be required to pay the Base Rate on all assets within the PSM. The Base Rate is dynamic and will align with the SSR (Sky Savings Rate), expected to fluctuate between the Aave and Ethena rates. See [A.2.8.2.2.2.2.3 - Base Rate](fd39df25-6093-49ae-be12-36df34754612).

###### A.2.8.2.2.2.6.2.2 - Yield on USDC [Core]  <!-- UUID: 223a695c-addd-443a-bfed-b136eeb2eddc -->

Grove shall earn yield through Coinbase Custody on USDC holdings within the PSM, enabling potential positive carry depending upon the spread between custody yield and the Base Rate.

###### A.2.8.2.2.2.6.2.3 - Economic Rationale [Core]  <!-- UUID: b1831dee-c95f-4872-98e0-2e49f3591bf9 -->

Grove will pay the Base Rate on the PSM for the purpose of meeting ASC requirements, if there are no better alternatives available. Unlike other alternatives, USDC in the PSM will have no capital requirement. If other, better options for ASC are available, Grove should empty the PSM and allocate the assets to those options. It is anticipated that other protocols will also be willing to rent ASC "points", potentially allowing for the management of ASC needs across several Prime Agents for a profit.

###### A.2.8.2.2.2.6.3 - Future Transition and Long-Term Vision [Core]  <!-- UUID: 1a26a561-1f03-4d83-81df-3dedc9688597 -->

The subdocuments herein set out agreed terms with respect to the future transition and long-term vision for the PSM.

###### A.2.8.2.2.2.6.3.1 - Short Term (2025-2026) [Core]  <!-- UUID: 54bd8ca5-d078-4b1e-9f0a-e843fe13e5c0 -->

The PSM will remain a central liquidity hub for stablecoin deployment. Grove will manage the PSM, paying the Base Rate while earning USDC yield, under Sky oversight until full ASC implementation. PSM assets will count toward Grove's TVL, enhancing its economic standing and collateral efficiency.

###### A.2.8.2.2.2.6.3.2 - Long Term (Post-2026) [Core]  <!-- UUID: 4478d3b2-f8bc-400f-b6da-3bb43684e94d -->

The PSM's role will diminish as the ASC system becomes the primary liquidity management tool. Grove can wind down the PSM entirely if ASC requirements are fulfilled through other mechanisms (e.g., Uniswap positions, Curve pools). If ASC obligations rise significantly, PSM usage will increase, but as the system matures, its relevance will gradually decline.

###### A.2.8.2.2.2.6.4 - Implications for Grove [Core]  <!-- UUID: 3215686b-a770-484d-9602-6ee9d84c0e44 -->

The subdocuments herein set out implications of the PSM terms with respect to Grove.

###### A.2.8.2.2.2.6.4.1 - Positive Carry And Liquidity Balancing [Core]  <!-- UUID: 9ed13fe5-7b07-4222-93ff-640880a976e2 -->

Grove can generate positive carry if the USDC yield exceeds the Base Rate. If the Base Rate rises significantly, the PSM may become costly, requiring liquidity balancing.

###### A.2.8.2.2.2.6.4.2 - Capital Efficiency [Core]  <!-- UUID: 207d4658-b6f4-4937-853c-b5d23cff3c89 -->

Grove can deploy USDC in high-yield strategies while retaining enough ASC to meet requirements. Aave USDC (aUSDC) and Curve LP positions are likely alternatives to direct PSM usage, albeit potentially with higher JRC requirements.

###### A.2.8.2.2.2.6.4.3 - Risk Management [Core]  <!-- UUID: 00aa264d-4fe6-41a1-91ea-014a2a520001 -->

The PSM serves as a capital buffer, enabling Grove to scale liquidity massively without additional credit enhancement. As ASC obligations fluctuate, the PSM will act as a dynamic backstop, ensuring resilience during periods of high demand.

###### A.2.8.2.2.2.7 - Token Launch Penalty, Capital Transfer, And Income Generation [Core]  <!-- UUID: 2df67c30-1644-4455-a3e4-f3047c4c49ae -->

The subdocuments herein set out agreed terms with respect to a token launch penalty, capital transfer, and income generation.

###### A.2.8.2.2.2.7.1 - Token Launch Penalty [Core]  <!-- UUID: 5a62cc3f-4337-4770-a4d1-8a9b3d158b3f -->

If either Spark or Grove (each, a "Prime") does not complete its Prime Token Generation Event (see [A.2.8.2.2.2.7.1.1 - Prime Token Generation Event](fb80d94d-dd93-40ae-bb4c-8300c1c53d73)) by July 1, 2025, a penalty of thirty percent (30%) will apply. This penalty will be calculated on the income (as defined in [A.2.8.2.2.2.7.6 - Income Definition](fa48f7be-3c7d-4390-8b39-4fdfe9aa06ae)) the Prime is receiving or is meant to receive (including revenue that has accrued but has not been transferred) until the TGE occurs.

The penalty shall be paid as specified in [A.2.8.2.2.2.7.1.2 - Token Launch Penalty Settlement](c680762a-a3f9-46bf-b740-9029b8a97e2b).

###### A.2.8.2.2.2.7.1.1 - Prime Token Generation Event [Core]  <!-- UUID: fb80d94d-dd93-40ae-bb4c-8300c1c53d73 -->

The documents herein define a Prime Token Generation Event ("TGE") for Spark and Grove.

###### A.2.8.2.2.2.7.1.1.1 - Spark Token Generation Event [Core]  <!-- UUID: d703336e-b86f-4e50-99f0-f4a8dff1d0f7 -->

The Spark Token Generation Event occurred on June 17, 2025.

###### A.2.8.2.2.2.7.1.1.2 - Grove Token Generation Event [Core]  <!-- UUID: a69d2ed5-90ea-4d6b-ba6e-287a104017d2 -->

The Grove Token Generation Event will occur on the first date that SKY Staking users are able to earn GROVE Token Rewards. See [A.4.4.1 - SKY Staking](626bd71c-b413-41b7-a5fe-39fd0d43dbf5).

###### A.2.8.2.2.2.7.1.2 - Token Launch Penalty Settlement [Core]  <!-- UUID: c680762a-a3f9-46bf-b740-9029b8a97e2b -->

The Token Launch Penalty will be paid by each Prime at the time of the last Capital Transfer to a Genesis Agent (the "Token Launch Penalty Settlement Date") as specified in the documents herein.

###### A.2.8.2.2.2.7.1.2.1 - Token Launch Penalty Settlement Date [Core]  <!-- UUID: 66269cb6-0828-4977-b9d4-16840c6bc97d -->

When the Core Council determines the date of the last Capital Transfer to a Genesis Agent, it must submit an Atlas Edit Proposal to record the date in this document.

###### A.2.8.2.2.2.7.1.2.2 - Token Launch Penalty Settlement Mechanism [Core]  <!-- UUID: 4c8a37f9-717d-437c-9f38-d17cbb3b3639 -->

The settlement mechanism for the Token Launch Penalty, including the calculation of the penalty for each Prime and how the calculated balance is paid to Sky, will be included in a future iteration of the Atlas.

###### A.2.8.2.2.2.7.2 - Transfer Of Capital Funds [Core]  <!-- UUID: 760c4258-50f7-4334-af21-888759194e64 -->

The transfer of the Genesis Capital Allocation to each Prime SubProxy (i.e. the Spark SubProxy and Grove SubProxy) shall occur once funding from the Surplus Buffer is approved. This condition ensures that capital deployment is aligned with the successful launch of the Prime's token and the commencement of its independent operations.

###### A.2.8.2.2.2.7.2.1 - Transfer Of Genesis Capital Allocation To Spark SubProxy [Core]  <!-- UUID: e3ec99ec-54c9-4fe7-8104-aee20c57ec57 -->

The transfer of 20.6 million USDS from the Surplus Buffer to the Spark SubProxy for the Genesis Capital Allocation must be included in the June 26, 2025 Executive Vote. This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll.

This amount reflects that 4.4 million USDS of pre-TGE expenses were paid by Sky as specified in [A.2.8.2.2.2.7.4 - Treatment of Expenses Paid By Sky Pre-TGE](f3672ca1-b305-4e16-86f0-3dc3267073bb). This includes 2 million USDS transferred from the Sky Ecosystem Liquidity Bootstrapping Budget to Spark to provide liquidity to market makers and 2.4 million USDS transferred from the Ecosystem Liquidity Bootstrapping Budget to Spark to provide liquidity to exchanges. See [A.2.8.2.2.2.7.4.1 - Transfer From Liquidity Bootstrapping Budget To Spark For Market Makers](66abd123-f5cd-4d1a-bf75-2e5f468eae16) and [A.2.8.2.2.2.7.4.2 - Transfer From Liquidity Bootstrapping Budget To Spark For Exchanges](1d7924cd-8105-458f-a959-92f302b971d4).

No penalties were applied under [A.2.8.2.2.2.7.1 - Token Launch Penalty](5a62cc3f-4337-4770-a4d1-8a9b3d158b3f).

###### A.2.8.2.2.2.7.3 - Cessation Of MKR and SKY Token Flow [Core]  <!-- UUID: 91c1a218-ea12-4b75-ad71-efc4d1060e58 -->

Upon the commencement of Income Generation (as defined in [A.2.8.2.2.2.7.6 - Income Definition](fa48f7be-3c7d-4390-8b39-4fdfe9aa06ae)) by a Prime, any existing or previously agreed-upon allocation or distribution of MKR or SKY tokens from Sky to that Prime shall immediately cease. The intent is for the Primes to transition to financial self-sufficiency upon the initiation of their respective income-generating activities. Furthermore, any token vesting to the Prime Foundation will be reduced by 50% until the TGE occurs. Prior to the TGE, Primes agree to share with Sky the Prime Agent Token vesting schedules and lock-ups for their teams to ensure they align with the principles of long-term commitment to the Prime.

###### A.2.8.2.2.2.7.4 - Treatment of Expenses Paid By Sky Pre-TGE [Core]  <!-- UUID: f3672ca1-b305-4e16-86f0-3dc3267073bb -->

Any operational or other expenses incurred by a Prime and paid directly by Sky after July 1, 2025 shall be treated as an advance against the Prime’s Genesis Capital Allocation. The total amount of such expenses shall be documented and shall be deducted from the Prime’s allocated capital funds at the time of the Capital Transfer (as outlined in [A.2.8.2.2.2.7.2 - Transfer Of Capital Funds](760c4258-50f7-4334-af21-888759194e64)).

###### A.2.8.2.2.2.7.4.1 - Transfer From Liquidity Bootstrapping Budget To Spark For Market Makers [Core]  <!-- UUID: 66abd123-f5cd-4d1a-bf75-2e5f468eae16 -->

Sky has transferred 2 million USDS from the Sky Ecosystem Liquidity Bootstrapping Budget to Spark to provide liquidity to market makers. This amount shall be treated as an advance against Spark’s Genesis Capital Allocation and deducted from Spark’s allocated capital funds at the time of the Capital Transfer.

###### A.2.8.2.2.2.7.4.2 - Transfer From Liquidity Bootstrapping Budget To Spark For Exchanges [Core]  <!-- UUID: 1d7924cd-8105-458f-a959-92f302b971d4 -->

Sky has transferred 2.4 million USDS from the Sky Ecosystem Liquidity Bootstrapping Budget to Spark to provide liquidity to exchanges. This amount shall be treated as an advance against Spark’s Genesis Capital Allocation and deducted from Spark’s allocated capital funds at the time of the Capital Transfer.

###### A.2.8.2.2.2.7.5 - Income Generation And Pre-TGE Credit [Core]  <!-- UUID: 3ae9fa89-97e6-46ac-9b8b-ecb77a10574f -->

"Income Generation" shall be deemed to commence on July 1, 2025. From that date until the Prime’s TGE, seventy percent (70%) of any income generated by the Prime’s activities shall be credited to its capital account (net of any expenses paid by Sky as per [A.2.8.2.2.2.7.4 - Treatment of Expenses Paid By Sky Pre-TGE](f3672ca1-b305-4e16-86f0-3dc3267073bb)), subject to any penalties.

###### A.2.8.2.2.2.7.6 - Income Definition [Core]  <!-- UUID: fa48f7be-3c7d-4390-8b39-4fdfe9aa06ae -->

"Income" means all revenues or fees received or accrued by the applicable Prime after July 1, 2025, including: (i) Distribution Rewards (see [A.2.8.2.2.2.3.1 - Distribution Reward Rate](8e3cde6b-3b8b-4e9a-b9a0-8c24d84881f6)), (ii) Distribution Reward Bonus for 2025 (see [A.2.8.2.2.2.3.2 - 2025 Bonus](7ca440d3-03fb-4fba-81a8-d2118dc47aa6)), (iii) any Platform Fees charged to users, and (iv) Real World Asset fees charged to users, including any origination, servicing, or related charges, and (v) the blended cost of allocation spread between Junior and Senior Risk Capital.

#### A.2.8.2.3 - Ecosystem Accord 3: Sky And Keel [Core]  <!-- UUID: 63a88b08-e6cd-48bf-9cec-64ce7e42ae0e -->

The subdocuments herein record the terms of agreement between Sky and Keel as agreed in Ecosystem Accord 3.

##### A.2.8.2.3.1 - Accord Key Details [Core]  <!-- UUID: 40a876f3-e0bb-4bdf-a980-ffa38d9f46d7 -->

The subdocuments herein set out the key details of Ecosystem Accord 3, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.3.1.1 - Parties To The Accord [Core]  <!-- UUID: 0577460f-3f87-44ea-b39b-a614e7507338 -->

The parties to Ecosystem Accord 3 are Sky and Keel, as defined in the subdocuments herein.

###### A.2.8.2.3.1.1.1 - Sky Details [Core]  <!-- UUID: 7042cc09-20d7-4a83-a0f0-c718cdc489f2 -->

The party ‘Sky’ comprises Sky Core.

###### A.2.8.2.3.1.1.2 - Keel Details [Core]  <!-- UUID: 2e888dad-7700-450a-be85-49d7405e3541 -->

The party ‘Keel’ comprises the Keel Prime Agent, Keel Foundation, and Development Company.

###### A.2.8.2.3.1.2 - Duration Of The Accord [Core]  <!-- UUID: d936e118-89d8-4be7-9fcd-dd4d4334b26d -->

The duration of Ecosystem Accord 3 is indefinite, commencing from June 23, 2025.

##### A.2.8.2.3.2 - Accord Substantive Terms [Core]  <!-- UUID: ff6f7572-716f-4959-b312-a5ebf1547134 -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 3.

###### A.2.8.2.3.2.1 - Pioneer Incentive Pool [Core]  <!-- UUID: c929aef7-1b81-4693-8fd8-3d75e62882af -->

Keel is eligible for a Pioneer Incentive Pool as specified in [A.2.2.9.3.1.4 - Pioneer Incentive Pool](04edac33-19d5-4a87-a8ab-945a0cd57771).

The Pioneer Incentive Pool is calculated on a monthly basis as the Sky Savings Rate multiplied by all Unrewarded USDS on Solana. Payments are made on a monthly basis from the Demand Side Buffer (see [A.2.2.4.3 - Demand Side Buffer](862b6d83-f464-4125-8259-233b7de75ec4)) to a Pioneer Incentive Pool wallet controlled by the Pioneer Prime. The address of the Pioneer Incentive Pool wallet on Solana is `8JmDPG5BFQ6gpUPJV9xBixYJLqTKCSNotkXksTmNsQfj`.

###### A.2.8.2.3.2.2 - Tokenomics [Core]  <!-- UUID: b0de2330-3678-4852-8c24-ce85445201a7 -->

The tokenomics for Keel will be specified in a future iteration of the Atlas.

###### A.2.8.2.3.2.3 - Genesis Capital Allocation [Core]  <!-- UUID: 7df88d38-679b-42a2-a8a8-f798ac6a736b -->

The Genesis Capital Allocation for Keel is 10,000,000 USDS. The transfer of the Genesis Capital Allocation to Keel will be included in the March 26, 2026 Executive Vote. This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll. The address of Keel's SubProxy account is specified in [A.6.1.1.3.2.1.1.3.1.1.2 - SubProxy Account](2d5f052a-e32a-472c-884f-4fd8746e0459).

#### A.2.8.2.4 - Ecosystem Accord 4: Sky And Obex [Core]  <!-- UUID: 6bddc5aa-ac80-43d8-b8c8-8cde14e896df -->

The subdocuments herein record the terms of agreement between Sky and Obex as agreed in Ecosystem Accord 4.

##### A.2.8.2.4.1 - Accord Key Details [Core]  <!-- UUID: b82be738-892e-4d55-a42f-84fc1fdf3064 -->

The subdocuments herein set out the key details of Ecosystem Accord 4, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.4.1.1 - Parties To The Accord [Core]  <!-- UUID: 2cd5a1de-89d0-47d0-b671-87d8fec45766 -->

The parties to Ecosystem Accord 4 are Sky and Obex, as defined in the subdocuments herein.

###### A.2.8.2.4.1.1.1 - Sky Details [Core]  <!-- UUID: acb3e4c8-5edb-4ff0-bf47-e0a770cc08e7 -->

The party 'Sky' comprises Sky Core.

###### A.2.8.2.4.1.1.2 - Obex Details [Core]  <!-- UUID: 665a712a-d211-4a7a-b4c9-a8bad61b3f9c -->

The party 'Obex' comprises the Obex Prime Agent, Rubicon, and Treadstone.

###### A.2.8.2.4.1.2 - Duration Of The Accord [Core]  <!-- UUID: 90e40d2a-3baa-411f-9512-b7cf61762a75 -->

The duration of Ecosystem Accord 4 is indefinite, commencing from November 13, 2025.

##### A.2.8.2.4.2 - Accord Substantive Terms [Core]  <!-- UUID: ec71c718-4a93-4cd7-8324-11d00110bbd3 -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 4. Additional detail regarding the substantive terms of Ecosystem Accord 4 will be specified in a future iteration of the Atlas, as agreed by the Parties to the Accord.

###### A.2.8.2.4.2.1 - Genesis Capital Allocation [Core]  <!-- UUID: b9e591ad-fd43-42fa-9262-aa9589c79ea3 -->

The subdocuments herein set out agreed terms with respect to Genesis Capital Allocation.

###### A.2.8.2.4.2.1.1 - Obex Initial Allocation [Core]  <!-- UUID: a15698be-8723-4bab-9b25-f393deec41e2 -->

The Initial Allocation for Obex is 21,000,000 USDS.

###### A.2.8.2.4.2.1.2 - Initial Allocation Distribution [Core]  <!-- UUID: 2ace92dc-2a09-4d9e-9bae-9ea4da1b2f38 -->

The Initial Allocation is distributed in USDS to the Obex SubProxy.

###### A.2.8.2.4.2.1.2.1 - Transfer Of Genesis Capital Allocation To Obex SubProxy [Core]  <!-- UUID: c39702fb-bb6a-43c7-b208-18ddd279b1d3 -->

The transfer of 21,000,000 USDS from the Surplus Buffer to the Obex SubProxy for the Genesis Capital Allocation must be included in the November 13, 2025 Executive Vote. This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll.

#### A.2.8.2.5 - Ecosystem Accord 5: Sky And Core Council Executor Agent 1 [Core]  <!-- UUID: 3aa58bdc-1c86-4a4e-8ca5-5a836cd2e465 -->

The subdocuments herein record the terms of agreement between Sky and Core Council Executor Agent 1 as agreed in Ecosystem Accord 5.

##### A.2.8.2.5.1 - Accord Key Details [Core]  <!-- UUID: b95a2b5e-f0e7-4ae4-ba47-56588d35e559 -->

The subdocuments herein set out the key details of Ecosystem Accord 5, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.5.1.1 - Parties To The Accord [Core]  <!-- UUID: 711e1403-022d-4617-a835-bc98ab4dc521 -->

The parties to Ecosystem Accord 5 are Sky and Core Council Executor Agent 1, as defined in the subdocuments herein.

###### A.2.8.2.5.1.1.1 - Sky Details [Core]  <!-- UUID: 5999930f-429a-411a-9103-203357fd5e99 -->

The party 'Sky' comprises Sky Core.

###### A.2.8.2.5.1.1.2 - Core Council Executor Agent 1 Details [Core]  <!-- UUID: 3e5e6630-0c08-4e89-ae09-a3c45dd654f2 -->

The party 'Core Council Executor Agent 1' comprises the Core Council Executor Agent 1 Executor Agent, Core Council Executor Agent 1 Foundation, and Core Council Executor Agent 1 Development Company.

###### A.2.8.2.5.1.2 - Duration Of The Accord [Core]  <!-- UUID: c24d90d8-de2a-4d07-841b-f72ab8bf2b1b -->

The duration of Ecosystem Accord 5 is indefinite, commencing from December 11, 2025.

##### A.2.8.2.5.2 - Accord Substantive Terms [Core]  <!-- UUID: 265e5d17-6a43-43e0-ac52-ad3bc4f2e8ea -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 5. Additional detail regarding the substantive terms of Ecosystem Accord 5 will be specified in a future iteration of the Atlas, as agreed by the Parties to the Accord.

###### A.2.8.2.5.2.1 - Role As Core Executor Agent [Core]  <!-- UUID: fbf36985-ee32-4426-b809-b26f36c6e8a7 -->

Core Council Executor Agent 1 will serve as the first Core Executor Agent and must carry out the responsibilities of the Core Council. See [A.0.1.1.46 - Core Council](5a03a0c4-a47a-409c-9b23-52ac93e63d45).

###### A.2.8.2.5.2.2 - Genesis Capital Allocation [Core]  <!-- UUID: 6dc349a3-183e-4074-8f6e-cff39867363e -->

To effect the Genesis Capitalization of Core Council Executor Agent 1, Sky Core shall directly transfer (1) 20,000,000 USDS to the Core Council Executor Agent 1 SubProxy and (2) 5,000,000 USDS to the Core Council Buffer (see [A.2.3.1.2.2.2.1 - Core Council Buffer](8b6781d7-f35c-4ffe-b8ed-299fa98e3da7)). The 5,000,000 USDS transfer constitutes part of Core Council Executor Agent 1's Genesis Capital Allocation, deposited directly to its operational payment account.

###### A.2.8.2.5.2.2.1 - Core Council Executor Agent 1 SubProxy Address [Core]  <!-- UUID: 89c19c75-cd5d-4c21-887d-0f4bfe3e42a7 -->

The address of Core Council Executor Agent 1's SubProxy Account on the Ethereum Mainnet is `0x64a2b7CfA832fE83BE6a7C1a67521B350519B9c1`.

###### A.2.8.2.5.2.2.2 - Use Of Genesis Capital [Core]  <!-- UUID: 7935cb9f-2ca1-475a-8b43-bf21b3fa2370 -->

The Genesis Capital Allocation will be used to fund the Core Council Executor Agent 1; the incubating Operational Executor Agents; and broader Core operational expenses, including technical infrastructure, Spell crafting, risk work, and Spell audits.

###### A.2.8.2.5.2.3 - Funding Of Core Council Buffer [Core]  <!-- UUID: 3dd54817-d655-4fc5-b6f3-287623c1ba93 -->

The Core Council Executor Agents holding seats on the Core Council maintain operational authority over the Core Council Buffer, consistent with their mandate to operationalize Sky Core.

Core Council Executor Agent 1 may capitalize the Core Council Buffer from its Genesis Capital allocation to ensure adequate liquidity for operational payments prior to its establishment of dedicated payment infrastructure.

Expenses paid through the Core Council Buffer shall be recorded as operational expenses of Core Council Executor Agent 1, whether funded by the Genesis Capital Allocation deposited directly to the Core Council Buffer or by subsequent transfers from the Core Council Executor Agent 1 SubProxy prior to the establishment of independent payment infrastructure.

###### A.2.8.2.5.2.4 - Transfers To The Sky Frontier Foundation [Core]  <!-- UUID: e93eb85c-a3dc-459b-8774-85c8b16dde8f -->

Core Council Executor Agent 1 is authorized to transfer funds from its Genesis Capital Allocation to the Sky Frontier Foundation without a separate governance decision for each transfer. Such transfers may be included directly in an Executive Vote without a prior Governance Poll.

#### A.2.8.2.6 - Ecosystem Accord 6: Sky And Osero [Core]  <!-- UUID: 45125ff8-5435-4cbf-9b20-9f55a1dbc883 -->

The subdocuments herein record the terms of agreement between Sky and Osero as agreed in Ecosystem Accord 6.

##### A.2.8.2.6.1 - Accord Key Details [Core]  <!-- UUID: 262776d7-3f8e-4884-b858-b1942334ebab -->

The subdocuments herein set out the key details of Ecosystem Accord 6, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.6.1.1 - Parties To The Accord [Core]  <!-- UUID: 0f44e3b9-5fd3-4f1c-8917-97000969d334 -->

The parties to Ecosystem Accord 6 are Sky and Osero, as defined in the subdocuments herein.

###### A.2.8.2.6.1.1.1 - Sky Details [Core]  <!-- UUID: dd7f7030-6020-490b-a8a2-196537ed66cd -->

The party 'Sky' comprises Sky Core.

###### A.2.8.2.6.1.1.2 - Osero Details [Core]  <!-- UUID: d9b2da30-bdae-47a6-96ff-966f92ce2b7e -->

The party 'Osero' comprises the Osero Prime Agent, Osero Foundation, and Stablewatch.

###### A.2.8.2.6.1.2 - Duration Of The Accord [Core]  <!-- UUID: 0b2fcb50-7b46-431a-8ab8-9c95c6ce8fb0 -->

The duration of Ecosystem Accord 6 is indefinite, commencing from December 18, 2025.

##### A.2.8.2.6.2 - Accord Substantive Terms [Core]  <!-- UUID: 8a42e953-8932-41c4-acdc-4bc5b9274e3d -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 6. Additional detail regarding the substantive terms of Ecosystem Accord 6 will be specified in a future iteration of the Atlas, as agreed by the Parties to the Accord.

###### A.2.8.2.6.2.1 - Tokenomics [Core]  <!-- UUID: 66a45926-a68c-41ff-9773-940c627aa03a -->

The subdocuments herein set out agreed terms with respect to tokenomics.

###### A.2.8.2.6.2.1.1 - Total Token Supply [Core]  <!-- UUID: b25e4af5-e97a-4457-83be-c253c7f4d039 -->

The total token supply of OSERO shall be 1,000,000,000.

###### A.2.8.2.6.2.1.2 - Token Allocations [Core]  <!-- UUID: 45a052e0-954d-49d9-a691-7adff194a839 -->

Specific token allocations are defined in the subdocuments herein.

###### A.2.8.2.6.2.1.2.1 - Osero Prime Treasury [Core]  <!-- UUID: 1ae8c439-cc0d-400f-90cd-4f5ef10356d6 -->

677,777,778 OSERO tokens are allocated to the Osero Prime Treasury (Osero’s SubProxy).

Osero will use 150,000,000 OSERO tokens for incentives.

###### A.2.8.2.6.2.1.2.2 - Sky Retained Tokens And Reward Pools [Core]  <!-- UUID: efb7339d-fb3d-4f5d-bdea-16ac8c291510 -->

Sky retains 322,222,222 OSERO tokens, distributing these as specified in a future iteration of the Atlas.

###### A.2.8.2.6.2.2 - Genesis Capital Allocation [Core]  <!-- UUID: f6ab77a4-8ba4-4f67-8c9f-8cc6a921ae53 -->

The subdocuments herein set out agreed terms with respect to Genesis Capital Allocation.

###### A.2.8.2.6.2.2.1 - Osero Initial Allocation [Core]  <!-- UUID: 94b2eef8-f5fd-4df1-8638-e1b81d032c47 -->

The Initial Allocation for Osero is 10,500,000 USDS.

###### A.2.8.2.6.2.2.2 - Initial Allocation Distribution [Core]  <!-- UUID: 20eeeaf4-38bc-4440-be1c-a1ee67ee3491 -->

The Initial Allocation is distributed in USDS to the Osero SubProxy.

###### A.2.8.2.6.2.2.2.1 - Transfer Of Genesis Capital Allocation To Osero Foundation [Core]  <!-- UUID: 4fd99f26-90a3-4385-a3ea-7949f5d56b3f -->

Sky has transferred 500,000 USDS from the Core Council Buffer to the Osero Foundation.

The address of the Osero Foundation on the Ethereum Mainnet is `0xfDD055D3CCEE0D955031CF1FD76c8Db9317cCC58`.

###### A.2.8.2.6.2.2.2.2 - Transfer Of Genesis Capital Allocation To Osero SubProxy [Core]  <!-- UUID: 65638659-eb0d-4e5c-87e8-50705e3595b8 -->

The transfer of 10,000,000 USDS from the Surplus Buffer to the Osero SubProxy for the Genesis Capital Allocation will be included in the March 26, 2026 Executive Vote. This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll. The address of Osero's SubProxy account is `0x24fdcd3bFA5C2553e05B2f9AD0365EBC296278D3`.

#### A.2.8.2.7 - Ecosystem Accord 7: Sky And Skybase [Core]  <!-- UUID: 8a74919c-d9c1-4d9a-9499-302201f96f9c -->

The subdocuments herein record the terms of agreement between Sky and Skybase as agreed in Ecosystem Accord 7.

##### A.2.8.2.7.1 - Accord Key Details [Core]  <!-- UUID: a6b51805-7420-46a5-b5d0-d769eb90e48d -->

The subdocuments herein set out the key details of Ecosystem Accord 7, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.7.1.1 - Parties To The Accord [Core]  <!-- UUID: e5a76dd6-2e8a-425e-b961-664b24097f6e -->

The parties to Ecosystem Accord 7 are Sky and Skybase, as defined in the subdocuments herein.

###### A.2.8.2.7.1.1.1 - Sky Details [Core]  <!-- UUID: 83844293-5cca-45b3-9eb9-fd1d228aa3b5 -->

The party 'Sky' comprises Sky Core.

###### A.2.8.2.7.1.1.2 - Skybase Prime Details [Core]  <!-- UUID: 287bbf07-b29b-46b1-a8a1-d237825424cd -->

The party 'Skybase' comprises the Skybase Prime Agent, Skybase Foundation, and Development Company.

###### A.2.8.2.7.1.2 - Duration Of The Accord [Core]  <!-- UUID: 9d207eb3-955e-4b4d-af1b-056519d0235b -->

The duration of Ecosystem Accord 7 is indefinite, commencing from September 1, 2024.

##### A.2.8.2.7.2 - Accord Substantive Terms [Core]  <!-- UUID: e51d5901-0b0b-42f0-b484-8114516c8e8a -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 7. Additional detail regarding the substantive terms of Ecosystem Accord 7 will be specified in a future iteration of the Atlas, as agreed by the Parties to the Accord.

###### A.2.8.2.7.2.1 - Tokenomics [Core]  <!-- UUID: 28790b12-35f5-4754-9bc2-d5dc527a6e37 -->

The subdocuments herein set out agreed terms with respect to tokenomics.

###### A.2.8.2.7.2.1.1 - Total Token Supply [Core]  <!-- UUID: 709e8307-20ba-48c9-b9b5-71d58d05abb2 -->

The total token supply of SKYBASE will be specified in a future iteration of the Atlas.

###### A.2.8.2.7.2.1.2 - Token Allocations [Core]  <!-- UUID: 6b69c767-ee38-42b3-9e45-3abaa17677f1 -->

Specific token allocations are defined in the subdocuments herein.

###### A.2.8.2.7.2.1.2.1 - Skybase Prime Treasury [Core]  <!-- UUID: 088264de-3158-4200-a5ce-e1eb730d38a6 -->

The amount of SKYBASE tokens allocated to the Skybase Prime Treasury (Skybase's SubProxy) will be specified in a future iteration of the Atlas.

###### A.2.8.2.7.2.1.2.2 - Sky Retained Tokens And Reward Pools [Core]  <!-- UUID: 576ff155-7fc3-4d9d-8359-f9e9cc5da874 -->

The amount of SKYBASE tokens retained by Sky and their distribution will be specified in a future iteration of the Atlas.

###### A.2.8.2.7.2.2 - Genesis Capital Allocation [Core]  <!-- UUID: d5168fa2-5a7f-4dd7-9a00-d3d1732c3bc3 -->

The subdocuments herein set out agreed terms with respect to Genesis Capital Allocation.

###### A.2.8.2.7.2.2.1 - Skybase Initial Allocation [Core]  <!-- UUID: 0ad56e68-ac7a-4660-8bdc-4d11d69511ce -->

The Initial Allocation for Skybase is 15,000,000 USDS.

###### A.2.8.2.7.2.2.2 - Initial Allocation Distribution [Core]  <!-- UUID: 2f2c4f2b-ff7a-4cd1-b1bc-8f3f81fe129f -->

10,000,000 USDS of the Initial Allocation is distributed to the Skybase SubProxy.

5,000,000 USDS of the Initial Allocation is distributed to the USDS Demand Subsidies Multisig.

###### A.2.8.2.7.2.2.2.1 - Transfer Of Genesis Capital Allocation To Skybase SubProxy [Core]  <!-- UUID: 36556509-d2b6-4932-8781-9bf4ecc90987 -->

The transfer of 10,000,000 USDS from the Surplus Buffer to the Skybase SubProxy for the Genesis Capital Allocation will be included in the January 29, 2026 Executive Vote.

This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll.

###### A.2.8.2.7.2.2.2.2 - Transfer Of Genesis Capital Allocation To USDS Demand Multisig [Core]  <!-- UUID: be600bf6-c0f2-42c5-ad5c-fd0cb429b628 -->

The transfer of 5,000,000 USDS from the Surplus Buffer to the USDS Demand Subsidies Multisig (see [A.6.1.1.4.3.4.2 - USDS Demand Subsidies Multisig](20ee784c-115a-40bb-ae74-d4b3726b0c1b)) for the Genesis Capital Allocation will be included in the January 29, 2026 Executive Vote.

This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll.

###### A.2.8.2.7.2.2.3 - Subsequent Allocation Mechanism [Core]  <!-- UUID: 45830abe-1238-4e68-a9c0-6b0a359d16a9 -->

Following its Genesis Capital Allocation, Skybase may request additional grants to the Skybase Foundation to fund operations and growth. The authorization of grant requests is subject to the governance requirements and limitations specified in [A.2.2.6.2.3.1 - Limitations On Usage Of Root Edit Primitive Prior To Independent Governance](8c15762a-ea7e-4c6d-9089-60d30c219c0f). Sky Governance must consent to the transfer of funds for each such grant via an Atlas Edit. The documents herein record these authorizations.

###### A.2.8.2.7.2.2.3.1 - Skybase Foundation Grant Authorization: July 2026 [Core]  <!-- UUID: 0f33f443-14d5-48b0-a20d-e35a44230cdc -->

The founding team of Skybase has proposed a one-time cash grant of 700,000 USDS to the Skybase Foundation from Skybase's SubProxy to provide operational capital. This funding will be used to complete payments for Skybase Agent operational needs and other expenses.

Sky Governance hereby consents to this grant and authorizes the execution of the associated funding payload. The transfer must be made to the Skybase Foundation Operational Multisig at `0x58B945c8Ce34BD8cEA3Fc0437626F9F87d58A621` in a Skybase Spell included in a Sky Executive Vote unless otherwise agreed by Sky and Skybase.

#### A.2.8.2.8 - Ecosystem Accord 8: Sky And Amatsu [Core]  <!-- UUID: 9d187ae2-1106-4b43-a6a6-ff54c329d0da -->

The subdocuments herein record the terms of agreement between Sky and Amatsu as agreed in Ecosystem Accord 8.

##### A.2.8.2.8.1 - Accord Key Details [Core]  <!-- UUID: 7b53595c-b29f-40b4-8098-21949ed4f6e4 -->

The subdocuments herein set out the key details of Ecosystem Accord 8, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.8.1.1 - Parties To The Accord [Core]  <!-- UUID: 511d2f27-51f4-48bb-b147-cfbb81a05096 -->

The parties to Ecosystem Accord 8 are Sky and Amatsu, as defined in the subdocuments herein.

###### A.2.8.2.8.1.1.1 - Sky Details [Core]  <!-- UUID: fa3bcebb-38a6-4541-8349-e07166fb4d81 -->

The party 'Sky' comprises Sky Core.

###### A.2.8.2.8.1.1.2 - Amatsu Details [Core]  <!-- UUID: cef53b14-d230-4f10-a482-0fbacdf3d3bc -->

The party 'Amatsu' comprises the Amatsu Executor Agent.

###### A.2.8.2.8.1.2 - Duration Of The Accord [Core]  <!-- UUID: 918ce6f7-dd4b-419d-8a5c-92fb595b0ec1 -->

The duration of Ecosystem Accord 8 is indefinite, commencing from March 19, 2026.

##### A.2.8.2.8.2 - Accord Substantive Terms [Core]  <!-- UUID: d6624ff1-e50e-4a56-b1c4-2f24af3cb34e -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 8. Additional detail regarding the substantive terms of Ecosystem Accord 8 will be specified in a future iteration of the Atlas, as agreed by the Parties to the Accord.

###### A.2.8.2.8.2.1 - Genesis Capital Allocation [Core]  <!-- UUID: ff5c1b0c-8027-4711-9cc3-a18772c0ba5b -->

The Genesis Capital Allocation for Amatsu is 25,000,000 USDS. The transfer of the Genesis Capital Allocation to Amatsu will be included in the March 26, 2026 Executive Vote. This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll.

###### A.2.8.2.8.2.1.1 - Amatsu SubProxy Address [Core]  <!-- UUID: fa9d102c-39ad-49ea-a30e-5101c3400313 -->

The address of Amatsu's SubProxy Account on the Ethereum Mainnet is `0xF33B14329e7115dD0B40DBb2985E1A0Df10E3fAa`.

###### A.2.8.2.8.2.1.2 - Use Of Genesis Capital [Core]  <!-- UUID: 64bb69a7-6525-44ad-af92-cb7dd400fcc8 -->

The Genesis Capital Allocation will be used to support Amatsu's work in delivering services in the role of Operational Executor Agent for the Sky Ecosystem.

###### A.2.8.2.8.2.2 - Transfers To The Sky Frontier Foundation [Core]  <!-- UUID: 06bac1e1-ae52-4c67-8ca9-0dcec22dddee -->

Amatsu is authorized to transfer funds from its Genesis Capital Allocation to the Sky Frontier Foundation without a separate governance decision for each transfer. Such transfers may be included directly in an Executive Vote without a prior Governance Poll.

#### A.2.8.2.9 - Ecosystem Accord 9: Sky And Ozone [Core]  <!-- UUID: cb3c159b-46fd-4e85-a6d5-e2ab17977ac8 -->

The subdocuments herein record the terms of agreement between Sky and Ozone as agreed in Ecosystem Accord 9.

##### A.2.8.2.9.1 - Accord Key Details [Core]  <!-- UUID: dbbd6557-ff1e-49e2-951b-1457d290b55f -->

The subdocuments herein set out the key details of Ecosystem Accord 9, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.9.1.1 - Parties To The Accord [Core]  <!-- UUID: 81a42abc-2494-493e-9698-68a0c712684e -->

The parties to Ecosystem Accord 9 are Sky and Ozone, as defined in the subdocuments herein.

###### A.2.8.2.9.1.1.1 - Sky Details [Core]  <!-- UUID: 12d48429-0536-4efd-aaa2-2ca433498e81 -->

The party 'Sky' comprises Sky Core.

###### A.2.8.2.9.1.1.2 - Ozone Details [Core]  <!-- UUID: 483798e7-9aac-4a93-9e89-52d108be3c55 -->

The party 'Ozone' comprises the Ozone Executor Agent.

###### A.2.8.2.9.1.2 - Duration Of The Accord [Core]  <!-- UUID: 28433341-af4a-435d-8839-0225f515af64 -->

The duration of Ecosystem Accord 9 is indefinite, commencing from March 19, 2026.

##### A.2.8.2.9.2 - Accord Substantive Terms [Core]  <!-- UUID: 91fabe18-fd56-448e-9485-46427647a675 -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 9. Additional detail regarding the substantive terms of Ecosystem Accord 9 will be specified in a future iteration of the Atlas, as agreed by the Parties to the Accord.

###### A.2.8.2.9.2.1 - Genesis Capital Allocation [Core]  <!-- UUID: ee64a5b7-da29-4b14-aaa7-e2f370a37301 -->

The Genesis Capital Allocation for Ozone is 25,000,000 USDS. The transfer of the Genesis Capital Allocation to Ozone will be included in the March 26, 2026 Executive Vote. This action is authorized to proceed directly to an Executive Vote without a prior Governance Poll.

###### A.2.8.2.9.2.1.1 - Ozone SubProxy Address [Core]  <!-- UUID: 6337ca25-2d6f-4483-9b89-c087138ebabf -->

The address of Ozone's SubProxy Account on the Ethereum Mainnet is `0x9FE628BFc33f0352Bb1f93168881a9Ef93C8d2CF`.

###### A.2.8.2.9.2.1.2 - Use Of Genesis Capital [Core]  <!-- UUID: 9e7acf02-b30c-47fd-aa6f-bef61dc1210d -->

The Genesis Capital Allocation will be used to fund Ozone's work in supporting the Agents that it serves as the Operational Executor Agent for.

###### A.2.8.2.9.2.2 - Transfers To The Sky Frontier Foundation [Core]  <!-- UUID: 9bb85c21-96a3-4f0a-baab-1c3fe340871d -->

Ozone is authorized to transfer funds from its Genesis Capital Allocation to the Sky Frontier Foundation without a separate governance decision for each transfer. Such transfers may be included directly in an Executive Vote without a prior Governance Poll.

#### A.2.8.2.10 - Ecosystem Accord 10: Sky And Grove [Core]  <!-- UUID: 0cb00b28-12a8-4790-974a-a3d98fd4dc97 -->

The subdocuments herein record the terms of agreement between Sky and Grove as agreed in Ecosystem Accord 10.

##### A.2.8.2.10.1 - Accord Key Details [Core]  <!-- UUID: 7b9e976e-f55a-45a4-b0ae-db5142164d98 -->

The subdocuments herein set out the key details of Ecosystem Accord 10, such as parties to the agreement and the duration of the Accord.

###### A.2.8.2.10.1.1 - Parties To The Accord [Core]  <!-- UUID: 6b454041-6333-4da3-94e5-d9a29b1c01d6 -->
    
The parties to Ecosystem Accord 10 are Sky and Grove, as defined in the subdocuments herein.

###### A.2.8.2.10.1.1.1 - Sky Details [Core]  <!-- UUID: e785ccea-cf2a-44f3-a49b-632edfd4bb5a -->

The party 'Sky' comprises Sky Core.

###### A.2.8.2.10.1.1.2 - Grove Details [Core]  <!-- UUID: 71eda1d2-5ea4-4999-89a9-168df36e0c60 -->

The party 'Grove' comprises the Grove Prime Agent and Grove Foundation.

###### A.2.8.2.10.1.2 - Duration Of The Accord [Core]  <!-- UUID: c7d102c8-3d5d-47c2-80a0-66a4c4ee7430 -->

The duration of Ecosystem Accord 10 is indefinite, commencing retroactively from July 24, 2025. The Accord remains in effect unless terminated or modified via an Atlas Edit.

##### A.2.8.2.10.2 - Accord Substantive Terms [Core]  <!-- UUID: c44e816f-dd67-4e35-aa4c-7098f159a05d -->

The subdocuments herein set out the substantive terms of Ecosystem Accord 10.

###### A.2.8.2.10.2.1 - Chronicle Point Reward Program [Core]  <!-- UUID: e1cbc4b9-1a20-47c0-a07c-8788467c1c0c -->

The subdocuments herein set out the terms of the Chronicle Point Reward program established under Ecosystem Accord 10.

###### A.2.8.2.10.2.1.1 - Chronicle Point Reward Instance Definition [Core]  <!-- UUID: a7ccb2d1-970e-4b91-a430-4173ade00396 -->

The "Chronicle Point Reward Instance" refers to the Ethereum mainnet reward mechanism through which USDS is deposited in Sky's Rewards contract to accrue Chronicle Points. Onchain, this instance is the verified `StakingRewards` contract at the address corresponding to the `REWARDS_USDS_01` key in the Chainlog.

###### A.2.8.2.10.2.1.2 - Compensation Formula [Core]  <!-- UUID: d4a5ce00-b041-4e9d-9bed-23253aba1b01 -->

Sky will pay Grove ongoing compensation in USDS, calculated as follows:

$
\text{Chronicle\_Point\_Reward\_Instance\_USDS\_Deposited} \times 20\% \times \text{Base\_Rate}
$

where:

- $\text{Chronicle\_Point\_Reward\_Instance\_USDS\_Deposited}$ is the total amount of USDS deposited in the Chronicle Point Reward Instance at the time of calculation;
- $20\%$ is the fixed compensation percentage; and
- $Base\_Rate$ is the Base Rate as defined in [A.3.1.2.1 - Base Rate](228f9955-6bba-4252-a101-5529e7a300b9).

This compensation recognizes Grove's role in promoting and supporting Chronicle across integrations within the Sky Ecosystem.

###### A.2.8.2.10.2.1.3 - Accrual Method [Core]  <!-- UUID: 4bed0292-a720-4306-b528-5d583fd4ead5 -->

Compensation under this Accord accrues continuously on the basis of the USDS deposited in the Chronicle Point Reward Instance and the Base Rate at each point in time. Where the Base Rate or the amount of USDS deposited changes during an accrual period, the compensation is calculated proportionally for each sub-period in which the relevant parameters remain constant.

###### A.2.8.2.10.2.1.4 - Payment Frequency And Mechanism [Core]  <!-- UUID: 31e070cf-2474-4815-a7da-350feaa97cc7 -->

Compensation under this Accord is settled monthly via the Monthly Settlement Cycle (MSC). Each monthly settlement is calculated as:

$$ 
\text{Monthly Settlement} = \sum \left[ \frac{\text{USDS\_Deposited (sub-period)} \times 0.20 \times \text{Base\_Rate (sub-period)}}{365} \times \text{Sub-Period\_Days} \right] 
$$

where sub-periods are defined by any change to the USDS deposited in the Chronicle Point Reward Instance or the Base Rate during the settlement month, per the accrual method in [A.2.8.2.10.2.1.3 - Accrual Method](4bed0292-a720-4306-b528-5d583fd4ead5).

###### A.2.8.2.10.2.1.5 - Retroactive Compensation [Core]  <!-- UUID: e19ba00b-8509-4cf1-b9af-20f16e9683f8 -->

Grove is entitled to retroactive compensation for the period from July 24, 2025 to March 31, 2026, to be settled in the April 2026 Monthly Settlement Cycle.

###### A.2.8.2.10.2.2 - Prime Revenue Credit [Core]  <!-- UUID: 03bec0ca-5667-40ae-ac54-62ce1a0c66ea -->

Grove is owed 2,528,000 USDS based on the true-up of prior Monthly Settlement Cycles. Until this amount is paid to Grove through the next Monthly Settlement Cycle, this credit counts toward Grove's Total Risk Capital (TRC), as defined in [A.3.2.1.2.1 - Total Risk Capital Definition](6f6b25d6-f73c-4733-ba37-12a0a411433c).

### A.2.8.3 - Modification And Termination Of Ecosystem Accords [Section]  <!-- UUID: 76e2717b-c65a-436e-88db-d9c8c19ea1e5 -->

This Section defines the requirement of mutual consent to modify, suspend, or terminate an Ecosystem Accord, and the circumstances in which Sky Governance may do so without that consent.

#### A.2.8.3.1 - Mutual Consent Requirement [Core]  <!-- UUID: 3c77a2cd-73f7-4e01-9909-50dd5cdd31d1 -->

The modification, suspension, or termination of an Ecosystem Accord requires the mutual consent of each party to the Accord whose rights, obligations, or commercial terms are affected by the modification, suspension, or termination, except in the circumstances specified in [A.2.8.3.2 - Circumstances Permitting Action Without Consent](c9296a9b-32b4-4c27-80ea-a86778228de0). The consent of the affected parties is given as specified in the documents herein.

##### A.2.8.3.1.1 - Consent Of Sky Governance [Core]  <!-- UUID: 0af500ba-6909-4d4e-ad50-e8eca172d58d -->

Where Sky is a party to an Ecosystem Accord, Sky's consent is given by Sky Governance approving the Atlas Edit Proposal that incorporates the modification, suspension, or termination of the Ecosystem Accord into the Atlas.

##### A.2.8.3.1.2 - Consent Of Other Parties [Core]  <!-- UUID: 2b052cfb-ffaa-474b-900c-c9d28eceec86 -->

The consent of each party to an Ecosystem Accord other than Sky must be expressed through a channel through which Core GovOps can verify the party's agreement, as specified in the documents herein. Where such a party is a Prime, its consent is given by an authorized representative of its Prime Agent, which acts on behalf of its affiliates, including its Foundation and Development Company.

###### A.2.8.3.1.2.1 - Consent Through The Sky Forum [Core]  <!-- UUID: 5d16653e-7213-4597-b7d1-299ca4de652f -->

A party other than Sky may express its agreement through the Sky Forum.

###### A.2.8.3.1.2.2 - Consent Through A Communication Channel Established By Core GovOps [Core]  <!-- UUID: 5909ed19-0349-4ec5-9dd8-abda402e9dde -->

A party other than Sky may express its agreement through a private communication channel established for this purpose by Core GovOps.

###### A.2.8.3.1.2.3 - Prior Ratification By Self-Governing Primes [Core]  <!-- UUID: 128f71a4-ad1c-4efa-a1da-706f85d7c89a -->

Where a party to an Ecosystem Accord is a Prime that governs its Prime Agent Artifact through a vote of its token holders, the authorized representative of its Prime Agent may express consent to a modification, suspension, or termination of the Ecosystem Accord only where the Prime's token holders have approved that action through the token-holder voting process provided for in the Prime's Artifact. This approval must be obtained before the Atlas Edit Proposal incorporating the modification, suspension, or termination (see [A.2.8.3.1.3 - Incorporation By Core GovOps](a6ce15bb-d12a-4d5b-8ba0-f2475ee2932e)) is approved.

##### A.2.8.3.1.3 - Incorporation By Core GovOps [Core]  <!-- UUID: a6ce15bb-d12a-4d5b-8ba0-f2475ee2932e -->

Where the parties to an Ecosystem Accord other than Sky have consented to a modification, suspension, or termination, Core GovOps incorporates the agreed change into an Atlas Edit Proposal.

#### A.2.8.3.2 - Circumstances Permitting Action Without Consent [Core]  <!-- UUID: c9296a9b-32b4-4c27-80ea-a86778228de0 -->

Sky Governance may modify, suspend, or terminate an Ecosystem Accord without the consent of the affected parties only in the circumstances specified in the documents herein. Sky Governance may carry out such a modification, suspension, or termination through any means otherwise authorized by the Atlas.

##### A.2.8.3.2.1 - Administrative Correction [Core]  <!-- UUID: 89668940-77ab-4361-a0b2-c89116560e95 -->

Sky Governance may make administrative corrections to an Ecosystem Accord without the consent of the affected parties, provided such corrections do not alter the rights, obligations, or commercial terms of any party. Administrative corrections are limited to the correction of typographical errors, formatting updates to maintain consistency with the Atlas, and reference updates caused by structural changes elsewhere in the Atlas.

##### A.2.8.3.2.2 - Implementation Of Dispute Resolution Decisions [Core]  <!-- UUID: d615f391-5b1a-4ab7-882c-83da331a9812 -->

Where a decision under [A.2.8.1.1 - Dispute Resolution By Core Council](82a04a56-8cc9-4adf-9714-da246d541371) resolves a dispute in a manner that requires the modification, suspension, or termination of an Ecosystem Accord, Sky Governance may implement that decision without the consent of the affected parties.

##### A.2.8.3.2.3 - Misalignment [Core]  <!-- UUID: 94bebf32-12f4-4109-9b24-cb835bc3a964 -->

Sky Governance may modify, suspend, or terminate an Ecosystem Accord without the consent of the affected parties where Sky Governance determines that the Accord, or a party's conduct under it, is misaligned with the Sky Ecosystem. Such misalignment includes, but is not limited to, circumstances where maintaining the Accord would compromise the safety of the Sky Ecosystem or its users.

##### A.2.8.3.2.4 - Terms Specified Within The Accord [Core]  <!-- UUID: f38ed994-683d-4191-98de-194a34e20c46 -->

Where an Ecosystem Accord specifies its own conditions for its modification, suspension, or termination, a modification, suspension, or termination carried out in accordance with those conditions does not require the mutual consent otherwise required under [A.2.8.3.1 - Mutual Consent Requirement](3c77a2cd-73f7-4e01-9909-50dd5cdd31d1). The parties' agreement to those conditions, as expressed in the Accord, constitutes their consent to action taken in accordance with them. Core GovOps gives effect to such a change by incorporating it into the Atlas.

### A.2.8.0.3.1 - Business Activities - Element Annotation [Annotation]  <!-- UUID: 31df7e2b-184f-428c-9c4f-23fd8054c5d3 -->

The element "business activities" refers to the commercial activities, transactions, and interactions that Ecosystem Actors perform within the ecosystem. These may include, but are not limited to, service delivery, product development, collaboration, and information exchange.

### A.2.8.0.3.2 - Ecosystem - Element Annotation [Annotation]  <!-- UUID: ed6d46b7-01bc-4b3f-a951-e75c3f40351a -->

The element "Ecosystem" in the phrase "Ecosystem Accords" should be understood as the collaborative network in which multiple stakeholders (referred to as "Ecosystem Actors") interact to conduct business operations benefiting Sky.

## A.2.9 - Legal Resilience [Article]  <!-- UUID: ac707ae4-65da-4cf9-8a34-8b9304cd9a95 -->

This Article governs the Resilience Fund and defines infrastructure and processes to support legal risk management and legal governance.

### A.2.9.1 - Legal Resilience [Section]  <!-- UUID: 2abdcb34-3863-40d9-8dd1-52516cb1fa96 -->

This Section manages the Resilience Fund (also "RF") and other infrastructure for legal risk management and legal governance.

#### A.2.9.1.1 - Legal Defense Resources [Core]  <!-- UUID: 8f2eb896-4736-4649-a054-1c76dae64dc6 -->

This document defines the resources available for legal defense. Over time, it can include both Sky Governance-controlled assets and external third-party resources and may be used to cover additional risks.

##### A.2.9.1.1.1 - Resilience Fund [Core]  <!-- UUID: ccd36a29-af79-4994-93b4-b07d150b0366 -->

The Resilience Fund (RF) is a self-insurance instrument fully controlled by Sky Governance, which will cover legal defense expenses in case of legal or regulatory action against Sky or active participants in the Sky Ecosystem. The RF will be the primary source for direct legal defense funding. The conditions of use are defined in [A.2.9.1.1.1.4.2 - Resilience Fund Claim Management Process](9ab8fdf3-939c-4096-a0b9-9d9486d5a339).

###### A.2.9.1.1.1.1 - Resilience Fund Budget [Core]  <!-- UUID: 43c65f87-9de3-42ce-ab1c-e9bf420b6920 -->

The budget of the Resilience Fund is defined in [A.2.9.1.1.1.1.1 - Resilience Fund Current Budget](aa1e93e5-8fc0-4e12-ad9d-8bb9f6cd8956). The Core Facilitator can propose to pay out the budget manually through an Operational Weekly Cycle, according to the rules related to claims described in this Section. The Core Facilitator can propose modifications to the document cited above through the Operational Weekly Cycle.

###### A.2.9.1.1.1.1.1 - Resilience Fund Current Budget [Core]  <!-- UUID: aa1e93e5-8fc0-4e12-ad9d-8bb9f6cd8956 -->

The current active budget for the Resilience Fund is: 5,000,000 USDS per year, with the full amount available at the start of each calendar year.

###### A.2.9.1.1.1.1.2 - Resilience Fund Transition Funding [Core]  <!-- UUID: cbcfc2ff-d26a-4e2d-896d-273ed2eb8a94 -->

Legal defense expenses directly related to Sky may be temporarily financed using the resources of the Resilience Fund. However, a separate Claim Protocol and Standard Operational Protocol must be developed to govern cases where Sky is the target of a legal or regulatory action.

###### A.2.9.1.1.1.1.2.0.3.1 - Separate Claim Protocol And Standard Operational Protocol - Element Annotation [Annotation]  <!-- UUID: b1cbe4dd-1df7-461f-b6dd-315d899f922c -->

The element refers to a separate set of procedures to be applied where Sky is the target of a legal or regulatory action. These separate procedures have not yet been defined. Once defined and ratified, they will be detailed in [A.2.9.1.1.4 - Legal Defense Standard Operational Protocols](bd82af2f-6617-4d4e-8acb-e23c7d2c904b). The Resilience Technical Committee must assist in elaborating this ruleset.

###### A.2.9.1.1.1.2 - Resilience Fund Technical Committee [Core]  <!-- UUID: 469a7e0b-0ded-45cf-9911-06723bf0cfd4 -->

The Resilience Technical Committee is a group of Ecosystem Actors authorized by Sky to provide operational support such as onboarding new beneficiaries to the RF, approving quotes, and assessing claims to be supported by the RF. Additional operational support includes providing general advice on the further development of the fund, amendments to the claim procedure, resilience measures and other risk-management topics.

###### A.2.9.1.1.1.2.1 - Resilience Fund Technical Committee Selection And Compensation [Core]  <!-- UUID: 71352327-3ea8-4a47-ae7e-5ccff35d5763 -->

The Core Facilitator selects the members of the Resilience Technical Committee and manages payments for their services on a project basis. The associated budget is defined in [A.2.9.1.1.1.1.1 - Resilience Fund Current Budget](aa1e93e5-8fc0-4e12-ad9d-8bb9f6cd8956).

###### A.2.9.1.1.1.2.2 - Resilience Fund Technical Committee Member Requirements [Core]  <!-- UUID: ad242c8e-81e3-4590-b034-722b3767b9d2 -->

The individual members of the Resilience Technical Committee who are directly involved in providing operational services on behalf of Sky must fulfill the requirements defined in the subdocuments herein.

###### A.2.9.1.1.1.2.2.1 - Resilience Fund Technical Committee Member Skill Set Requirement [Core]  <!-- UUID: 524ad7de-c3ee-4c5f-8c92-a5fdbb4aa29b -->

Members of the Resilience Technical Committee must have relevant experience or current employment in the legal industry, or with a world-leading insurance broker, insurance company, or risk management firm.

###### A.2.9.1.1.1.2.2.2 - Resilience Fund Technical Committee Member Experience Requirement [Core]  <!-- UUID: d931273b-cdcb-40d3-97a5-d4bafcd38981 -->

Members of the Resilience Technical Committee must have at least three (3) years of experience managing self-insurance instruments or experience in legal or regulatory risk analysis.

###### A.2.9.1.1.1.2.2.3 - Resilience Fund Technical Committee Member Professional Degree Requirement [Core]  <!-- UUID: 19e4c5ce-1a9c-4df4-b8e7-5e22d27450b6 -->

Members of the Resilience Technical Committee must have a law, management, risk, or insurance professional degree.

###### A.2.9.1.1.1.2.2.4 - Resilience Fund Technical Committee Member No Conflicts Requirement [Core]  <!-- UUID: a7d9166a-6ac6-4592-a67c-19f1a59f9355 -->

Members of the Resilience Technical Committee must not be involved in any business activity outside Sky or in any role within Sky that could result in a conflict of interest, either directly or indirectly.

###### A.2.9.1.1.1.2.2.5 - Resilience Fund Technical Committee Member Technology Experience Requirement [Core]  <!-- UUID: 9f1b0abd-9000-4df7-8aa4-82a7234608ac -->

Members of the Resilience Technical Committee must have at least three (3) years of experience in the cryptocurrency, DeFi, Web3, or emerging technology sectors.

###### A.2.9.1.1.1.2.3 - Resilience Fund Technical Committee Current Membership [Active Data Controller]  <!-- UUID: ab894e9e-b423-404b-8488-3d0578bbde28 -->

Approved Resilience Technical Committee members are defined as Active Data in [A.2.9.1.1.1.2.3.0.6.1 - Resilience Fund Technical Committee List Of Current Members](10b0e0aa-0338-40d7-b1e6-a29442c206e6).

The Active Data is updated as follows:

- The Responsible Party is the Core Facilitator.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.9.1.1.1.2.3.0.6.1 - Resilience Fund Technical Committee List Of Current Members [Active Data]  <!-- UUID: 10b0e0aa-0338-40d7-b1e6-a29442c206e6 -->

List of active Resilience Technical Committee Members:

- Gallagher

###### A.2.9.1.1.1.3 - Resilience Fund Policy [Core]  <!-- UUID: bf8f69ef-6e55-47be-9203-02036a7f8c0d -->

This provision and its subdocuments will govern the conditions and terms of use of the Resilience Fund.

###### A.2.9.1.1.1.3.1 - Resilience Fund Policy Loss Events [Core]  <!-- UUID: 9cb0c1c3-269b-433b-ac03-de4b0bec43fb -->

The Resilience Process covers legal defense or legal representation expenses incurred by a participant of the Sky Ecosystem when they are the defendant or respondent in a legal or regulatory action ("The Loss Event"). There must be a direct relationship between the legal or regulatory action and the Beneficiary’s activity at Sky.

A (non-exhaustive) list of legal or regulatory actions that may qualify is:

- Official requirements, or communications, from a regulatory body, governmental authority, or a court
- Subpoenas
- Lawsuit
- Writs

###### A.2.9.1.1.1.3.2 - Resilience Fund Policy Exclusions [Core]  <!-- UUID: b6f8e9a3-8e56-41fd-b760-a81834d4e214 -->

The cases specified in the following subelements will generally be excluded from coverage by the legal defense process:

- Prior or pending claims
- Claims between persons involved in the Sky Ecosystem
- Loss covered by other insurance
- Willful criminal offenses, fraud, or dishonesty
- Conflict of interest

###### A.2.9.1.1.1.3.3 - Resilience Fund Policy Beneficiaries [Core]  <!-- UUID: 8b3a5bf0-ac9a-4142-8fc6-dfcab8c385e9 -->

Eligible beneficiaries of the Resilience Fund are persons who fulfill the following requirements:

a) act on their own behalf OR b) act on behalf of a legal entity OR c) act on behalf of a collective AND have one of the following roles:

Previous Structure:

- Recognized Delegates
- Core Unit Facilitators
- Core Unit Contributors
- Dai Foundation Board Members

Current Structure:

- Active SKY or Agent token holders that participate regularly in governance (e.g., voting, writing proposals)
- Alignment Conservers
- Aligned Delegates (ADs)
- Facilitators
- The Guardian ([A.2.9.1.1.3 - The Guardian](0f808bde-fc68-4bda-bc6d-049c6aaaab1b)) or actors that fulfill an equivalent role.

###### A.2.9.1.1.1.3.3.1 - No Acquired Right Or Claim For Resilience Fund Policy Beneficiaries [Core]  <!-- UUID: 5b88e18f-dadc-47b2-af7c-e9ff8039d39e -->

Persons qualified as beneficiaries do not have any acquired right or claim. The claim decision process is described in [A.2.9.1.1.1.4 - Resilience Fund Processes And Principles](06aed112-2636-4478-b2c8-037808adc475), and the payout of a claim is subject to the approval of the Resilience Technical Committee (at their sole and absolute discretion) and further contingent on a SKY vote endorsing payment of the claim.

###### A.2.9.1.1.1.3.4 - Resilience Fund Policy Geographic Coverage [Core]  <!-- UUID: 3b1f2fc4-3d6c-445b-806b-1dbae77d8ad1 -->

Geographical coverage is worldwide.

###### A.2.9.1.1.1.3.5 - Resilience Fund Policy Effective Date [Core]  <!-- UUID: 9de7d51b-32f3-4746-b97d-9eb75a189cb6 -->

A Beneficiary’s eligibility for coverage under this Artifact will start after ratification of MIP106: 2023-03-27. ("Effective Date") and expire twenty-four (24) months after cessation of their role as a Beneficiary.

###### A.2.9.1.1.1.3.6 - Resilience Fund Policy Base Of Coverage [Core]  <!-- UUID: 9204cca6-3e91-4a34-b8be-fa6135d41f24 -->

Coverage is "Claims made". This means the Loss Event ([A.2.9.1.1.1.3.1 - Resilience Fund Policy Loss Events](9cb0c1c3-269b-433b-ac03-de4b0bec43fb)) must occur after the Effective Date ([A.2.9.1.1.1.3.5 - Resilience Fund Policy Effective Date](9de7d51b-32f3-4746-b97d-9eb75a189cb6)).

The facts and circumstances that originated the Loss Event may have occurred in the past for a maximum period of up to twenty-four (24) months before the date representing the later of (a) the Effective Date and (b) the date the Beneficiary is first eligible for coverage under this Artifact (the "Retroactivity Period").

###### A.2.9.1.1.1.4 - Resilience Fund Processes And Principles [Core]  <!-- UUID: 06aed112-2636-4478-b2c8-037808adc475 -->

Overview of the related processes and principles:

- Application process
- Claim management process
- Caps and Exclusions
- Refund of amounts to the Resilience Fund

###### A.2.9.1.1.1.4.1 - Resilience Fund Application Process [Core]  <!-- UUID: 7ee909ce-ae6d-4886-a0ea-c3017eb00bcd -->

The Resilience Fund application process is defined in the subdocuments of this document.

###### A.2.9.1.1.1.4.1.1 - Resilience Fund Proof Of Eligibility [Core]  <!-- UUID: c14521ea-e2fa-4853-a5af-64f4c96a526a -->

To become recognized as a Beneficiary, an Applicant must first select an Ethereum address that is linked to their activity at Sky ("Proof of Eligibility" or "POE"). Each Beneficiary type will have specific Proofs of Eligibility that are suitable for their role.

Valid PoE:

- Address set as owner and used to sign transactions from Sky multisigs, such as Core Unit operational wallets, auditor wallets or SPFs (old structure), or a Facilitator multisig (Endgame Structure)
    - PoE valid for former Core Unit Contributors, Core Unit Facilitators, and Scope Facilitators.
- Address that voted directly or through delegation in at least ten Governance Polls or Executive Votes.
    - PoE valid for active MKR or SKY holders, former Recognized Delegates (old structure), and Aligned Delegates (new structure)
- Address that received compensation from Sky, with the following conditions:
    - at least six (6) payouts spread over at least six (6) months in Dai or USDS OR
    - Dai or USDS DssVest stream spanning at least six (6) months OR
    - 3 MKR or SKY payouts spread over at least three (3) months OR
    - MKR or SKY DssVest stream spanning at least three (3) months
    - PoE valid for former Core Unit Contributors and Facilitators
- Address that holds >1 MKR or >24,000 SKY
- Attestation
    - If no PoE is available, a verified Beneficiary must attest eligibility on behalf of the applicant.
    - This PoE will be used exceptionally if no other Proof is available and will be assessed individually by the Resilience Fund Technical Committee.

###### A.2.9.1.1.1.4.1.2 - Resilience Fund Proof Of Eligibility Template [Core]  <!-- UUID: a457da07-943a-4d98-8153-db7b0eb55fe2 -->

Applications for the Resilience Fund must follow this template:

- .x: [Application RF]
- .x.1: [PoE]
- .x.2: [Active Period]
- .x.3: [Relevant Executive Proposal: Governance decision ratified by a governance vote]
- .x4: [Signature hash]

###### A.2.9.1.1.1.4.1.3 - Resilience Fund Proof Of Eligibility Digital Signature [Core]  <!-- UUID: c83e0e76-f5b2-43f1-9bef-14c6571e72e2 -->

The Applicant for the Resilience Fund must additionally sign an application message from the Ethereum Address (Digital Signature) used as PoE [A.2.9.1.1.1.4.1.1 - Resilience Fund Proof Of Eligibility](c14521ea-e2fa-4853-a5af-64f4c96a526a).

###### A.2.9.1.1.1.4.1.4 - Application Resilience Fund Application Terms And Conditions [Core]  <!-- UUID: 0e430890-6911-4d22-98e7-f46eecb1ac24 -->

By signing this message, the Applicant accepts and agrees:

- To comply with the terms and rules of [A.2.9 - Legal Resilience](ac707ae4-65da-4cf9-8a34-8b9304cd9a95) (the "Legal Resilience Fund Terms").
- That participation in the program is opt-in and voluntary and can be waived anytime by the Beneficiary.
- The Legal Resilience Fund Terms can be amended at any time through the established governance processes.
- That being registered as Beneficiary does not give rise to any right, benefit, entitlement, or claim, nor creates an obligation on any party to pay the Beneficiary.

Additionally, the Beneficiary declares that:

- No situation currently involves or appears to involve a conflict of interest, and any emerging potential conflict of interest shall be disclosed as soon as it happens.
- Any role change in Sky or termination of active engagement will be immediately communicated to the Resilience Technical Committee.

The Resilience Technical Committee will elaborate a user-friendly onboarding manual for the RF.

###### A.2.9.1.1.1.4.1.5 - Resilience Fund Application Confirmation [Core]  <!-- UUID: 12bfa6fd-df07-4222-858c-11ae6b75509d -->

The Applicant for the Resilience Fund will additionally send an encrypted message to the Resilience Technical Committee Member in charge of the onboarding process to confirm the application.

###### A.2.9.1.1.1.4.1.6 - Resilience Fund Approval Process And Verifiability [Core]  <!-- UUID: 980b1bb1-3282-48ec-aff7-54107a580bf5 -->

PoEs rely on a governance decision that was ratified by an Executive Vote.

The Resilience Technical Committee Member must identify this governance decision by verifying the Spell that enacted the Executive Vote ratifying the respective governance decision. This Spell contains the hash of the respective Executive Vote. Exceptional circumstances where no direct governance decision is available or difficult to assert will be handled case by case.

The Resilience Technical Committee Member will confirm the onboarding decision via an encrypted message to the Applicant.

###### A.2.9.1.1.1.4.2 - Resilience Fund Claim Management Process [Core]  <!-- UUID: 9ab8fdf3-939c-4096-a0b9-9d9486d5a339 -->

Overview of the claim management processes:

- Legal Counsel Pre-approval
- Claim approval / Advance Payment
- Reimbursement

###### A.2.9.1.1.1.4.2.1 - Resilience Fund Legal Counsel And Quote Pre-Approval [Core]  <!-- UUID: 49ecea76-a16d-4135-88db-ccd554866715 -->

The first step in the claim management process is to approve the Legal Counsel to undertake legal defense or representation and the quote presented to commence legal work. The Beneficiary must present the quote from the law firm they selected for their legal defense/representation. The request must indicate at least the following:

- Name of Legal Counsel
- Name of Law Firm
- If not in the Lawyer Registry, Proof of Eligibility
- Quote

The quote must include:

1. The initial payment required by Counsel to commence work immediately. This is the initial amount to be claimed against the Resilience Fund.
2. A global estimated fee based on an hourly rate OR fixed fee OR monthly retainer fee.

###### A.2.9.1.1.1.4.2.1.1 - Resilience Fund Qualified Counsel [Core]  <!-- UUID: bdb4beda-794e-42e6-a9d0-06632235c478 -->

If the Legal Counsel is RF-qualified in the Lawyer Registry ([A.2.9.1.1.2 - Lawyer Registry](4c327b04-48f7-4941-b996-1c629eb42bf7)), the claim is automatically submitted to the Claim Approval process ([A.2.9.1.1.1.4.2.2 - Resilience Fund Claim Approval](d9cd69ff-88ed-4869-9ca7-ff87ce8f1ff6)).

###### A.2.9.1.1.1.4.2.1.2 - Not Resilience Fund Qualified Counsel [Core]  <!-- UUID: 9f423880-3184-4172-9ac5-6e8a371f5bb0 -->

If Legal Counsel is NOT RF-qualified in the Lawyer Registry ([A.2.9.1.1.2 - Lawyer Registry](4c327b04-48f7-4941-b996-1c629eb42bf7)), then the Core Facilitator, or alternatively the Resilience Fund Technical Committee Member, will verify if the Legal Counsel complies with requisites in Lawyer Registry Acceptance Criteria and LR Resilience Fund Acceptance Criteria. See: [A.2.9.1.1.2.2 - Lawyer Registry Acceptance Criteria](2b66ce16-d104-4238-b7d5-e4c6fe8d961b) and [A.2.9.1.1.2.3 - Resilience Fund Representation Requirements](b39f4808-18ae-456b-86fc-d449a69ea99a).

If the Legal Counsel of the quote is determined by the Resilience Technical Committee to comply with the requirements of this Artifact, the quote is pre-approved and the legal counsel is added to the LR.

If the Legal Counsel doesn’t comply with the LR requirements, the claim is rejected and the Beneficiary must propose a different Legal Counsel.

###### A.2.9.1.1.1.4.2.2 - Resilience Fund Claim Approval [Core]  <!-- UUID: d9cd69ff-88ed-4869-9ca7-ff87ce8f1ff6 -->

If a Beneficiary incurs a Loss Event, they can submit a Reimbursement Payout Claim against the LD RF according to the process specified in the subdocuments herein.

###### A.2.9.1.1.1.4.2.2.1 - Resilience Fund Claim Approval Payout Claim [Core]  <!-- UUID: d47f9aa8-96d1-4be7-910c-505693b1784a -->

The Core Facilitator must review the Reimbursement Claim and decide whether to trigger a Governance Poll to perform a claims payout, by developing an internal model with input from experts and professionals.

The Payout Reimbursement Claim must contain the following elements:

- Description of Loss Event with relevant commentaries and context
- Advance Payment or Reimbursement
- Type of process
- Date of writ/subpoena/lawsuit
- Supportive Documentation
    - Law firm’s proposal and invoice OR quote
    - Copy of the Lawsuit/writ/ communication OR official requirement issued by a Court or Governmental Agency Supportive documentation is highly sensible. It is required to use encryption tools.

###### A.2.9.1.1.1.4.2.2.2 - Resilience Fund Claim Approval Coverage Framework [Core]  <!-- UUID: fe131e29-a159-453e-a3e0-7577af4e147b -->

In consultation with the Resilience Technical Committee, the Core Facilitator must develop a framework for establishing limits and coverage amounts per case, and apply these limits to individual claims.

###### A.2.9.1.1.1.4.2.2.3 - Resilience Fund Claim Approval Core Facilitator Review [Core]  <!-- UUID: 26044d1d-f92c-4945-9a1c-4907c56d4038 -->

The Core Facilitator will review the Payout Claim and if it contains all required elements and supportive documentation, will immediately transmit it to the Resilience Fund Technical Committee.

###### A.2.9.1.1.1.4.2.2.4 - Resilience Fund Claim Approval Technical Commitee Review [Core]  <!-- UUID: 07cd5714-47aa-46ef-a162-ab96875631d6 -->

The Resilience Fund Technical Committee will verify the merits of the claim according to the following substantial criteria (non-exhaustive list):

- Absence of Exclusions
- Identity and Role of Beneficiary
- Time scope
- Authenticity of writ/lawsuit
- Reasonability of lawyer fees, which must take into account market rates in the respective jurisdiction

###### A.2.9.1.1.1.4.2.2.5 - Resilience Fund Claim Approval Technical Committee Review Process [Core]  <!-- UUID: 313d72e5-62db-4dd4-b125-97467508f44c -->

From the moment the Payout Claim is filed, the Resilience Technical Committee will have five (5) working days to provide a payout recommendation. The recommendations of the Technical Committee are made in their sole and absolute discretion, are definitive, and are not subject to appeal.

###### A.2.9.1.1.1.4.2.2.6 - Resilience Fund Claim Approval Quorum And Decision Majorities [Core]  <!-- UUID: 10662753-b167-4043-b952-225cc9dd9e49 -->

Decisions related to claim payouts require a quorum of three (3) experts from the Resilience Technical Committee with a simple majority (>50%).

###### A.2.9.1.1.1.4.2.2.7 - Resilience Fund Claim Approval Decision Protections [Core]  <!-- UUID: 99079da7-e8e9-4660-96a6-269625d821cc -->

The recommendations of the Resilience Technical Committee are non-binding and will not give rise to any right or claim to the beneficiaries nor give rise to any obligation or responsibility.

###### A.2.9.1.1.1.4.2.2.8 - Resilience Fund Claim Approval Core Facilitator Decision [Core]  <!-- UUID: bf63fc62-3555-4b9b-a561-053fb35721b5 -->

Based on the recommendation of the Resilience Technical Committee, the Core Facilitator will decide whether to trigger a Governance Poll through the Operational Weekly Cycle to perform a claim payout.

###### A.2.9.1.1.1.4.2.3 - Resilience Fund Payout / Reimbursement [Core]  <!-- UUID: 9edd8feb-790b-42de-bf42-ba5d6550df1c -->

If the Governance Poll for paying out a claim is successful, an Executive Vote must be created and approved through Sky Governance processes to draw the funds from the Surplus Buffer and send them to the Beneficiary’s registered wallet. The spend must be accounted for in the budget in [A.2.9.1.1.1.1.1 - Resilience Fund Current Budget](aa1e93e5-8fc0-4e12-ad9d-8bb9f6cd8956).

###### A.2.9.1.1.1.4.3 - Resilience Fund Caps And Exclusions [Core]  <!-- UUID: e99c4433-e55b-49b1-b73a-8bc1ae3a56b6 -->

Unless otherwise approved by a governance vote of Sky, claim funds approved under this Section are subject to the caps and exclusions specified in the subdocuments of this document.

###### A.2.9.1.1.1.4.3.1 - Resilience Fund Aggregate Cap [Core]  <!-- UUID: 327407b2-9c87-4d7a-b772-1a61ac9d2da3 -->

Claims will be subject to an aggregate cap for all claims in relation to a Claim Event determined by the risk models elaborated by the Resilience Technical Committee.

###### A.2.9.1.1.1.4.3.2 - Resilience Fund Direct Costs And Legal Expenses Cap [Core]  <!-- UUID: c103cdb7-0213-492f-b900-96175ac89e5b -->

Claims can only be used to reimburse Beneficiaries for their losses and disbursements directly arising from a Claim Event, and reasonable legal expenses. "Reasonable legal expense" is a variable amount that will be determined taking into account the average market rates of the respective jurisdiction.

###### A.2.9.1.1.1.4.3.3 - Resilience Fund Caps Government Or Regulatory Fines Or Damages Exclusion [Core]  <!-- UUID: f44b8c82-f420-4d14-ad89-8b885408e10e -->

Must not be used to reimburse the payment of government or regulatory fines or damages awarded by the court.

###### A.2.9.1.1.1.4.4 - Refund Of Amounts To Resilience Fund [Core]  <!-- UUID: 608f5fd0-f441-47b2-8775-4f8b019e8c41 -->

Where Beneficiaries receive financial benefit or reimbursement of any type as a result of orders of a court, governmental or investigative body or regulatory agency that results in a windfall to the Beneficiary, these windfall amounts will be returned by the Beneficiary to the Resilience Fund within 14 days of receipt.

###### A.2.9.1.1.1.4.4.1 - Refund Of Amounts To Resilience Fund Examples [Core]  <!-- UUID: 6855b494-f493-4dad-a7be-a43a17959016 -->

By way of example only and without limiting the generality of the principle described in [A.2.9.1.1.1.4.4 - Refund Of Amounts To Resilience Fund](608f5fd0-f441-47b2-8775-4f8b019e8c41), such amounts include, without limitation:

- Amounts awarded by a court towards the Beneficiary’s legal fees or disbursements;
- An award of damages to a Beneficiary in relation to a Claim Event;
- Monies or digital assets located by police or other investigative bodies that were identified as the property of Sky; and
- Interest payable to a Beneficiary in relation to a Claim Event.

###### A.2.9.1.1.1.4.5 - Resilience Fund Litigation / Defense Management [Core]  <!-- UUID: cb5e73d2-0b65-4465-94db-eb70fb8c814c -->

Beneficiaries and their legal teams must, in the conduct of the litigation and as a condition of receiving reimbursement from the Resilience Fund, satisfy all of the conditions listed in the subdocuments of this document.

###### A.2.9.1.1.1.4.5.1 - Good Faith In Resilience Fund Litigation / Defense Management [Core]  <!-- UUID: 4ca172c5-b48c-4e62-8b23-055573cb2376 -->

Beneficiaries and their legal teams must act honestly, consistently, and fairly in handling claims and litigation.

###### A.2.9.1.1.1.4.5.2 - Promptness In Resilience Fund Litigation / Defense Management [Core]  <!-- UUID: 2981a7cf-cdc2-4967-816b-dcbbc21f3ee8 -->

Beneficiaries and their legal teams must make an early assessment of the prospects of success and deal with claims promptly.

###### A.2.9.1.1.1.4.5.3 - Cost Control In Resilience Fund Litigation / Defense Management [Core]  <!-- UUID: 455bd317-a36c-48ba-9c34-0034b824b3e4 -->

Beneficiaries and their legal teams must keep costs to a minimum and avoid reliance on technical defenses which have low probability of success.

###### A.2.9.1.1.1.4.5.4 - Alternative Dispute Resolution In Resilience Fund Litigation / Defense Management [Core]  <!-- UUID: c7222199-c81b-4d67-b7c1-044391c288d5 -->

Beneficiaries and their legal teams must consider alternative dispute resolution (ADR) options at all times.

##### A.2.9.1.1.2 - Lawyer Registry [Core]  <!-- UUID: 4c327b04-48f7-4941-b996-1c629eb42bf7 -->

The Lawyer Registry (also "LR") is a registry of specialized Ecosystem Actors who are qualified to perform legal work for Sky Ecosystem or participants in the Sky Ecosystem, including, but not limited to, legal representation or legal defense.

Lawyers will be onboarded in the Lawyer Registry covering at least the areas specified in [A.2.9.1.1.2.1 - Lawyer Registry Covered Areas](a176f67f-009f-44a0-a19b-169c2eb376a4).

###### A.2.9.1.1.2.1 - Lawyer Registry Covered Areas [Core]  <!-- UUID: a176f67f-009f-44a0-a19b-169c2eb376a4 -->

`| Category                         | Areas of Law                                         | Examples                                                                                                          |
|----------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Disputes/Investigations          | Regulatory Enforcement – Securities/Finance Law      | SEC/FinCEN/CFTC/Central Bank matters, Tax authority actions, OFAC orders, Sanctions                               |
|                                  | Securities Law Disputes (private party claims, class actions, etc.) | Sky investor claims, Lawsuits against Sky CORE actors                                                            |
|                                  | Intellectual Property                                | Patent Claims/Trolls, Trademark Claims/Trolls                                                                     |
|                                  | General Litigation – Any other Party-Party Disputes  | Disputes between Sky and 3rd party suppliers, Breach of contract disputes, Employment law disputes, Disputes between Sky and Ecosystem actors |
| Commercial Matters (non-litigious) | Commercial and Contracts                            | Commercial transactions (Audits, listing agreements, inter-Agent agreements affecting Sky Core etc.), Contracts and Procurement (includes contract management), Competition/Anti-Trust Law, Data protection and Privacy, Insurance Law |
|                                  | Intellectual Property, Information Technology        | IT procurement, licenses, and contracts, Convergent technologies, Intellectual property rights, Data protection and privacy, Trademark/Patent applications |
|                                  | Corporate Structuring, Entity Formation/Reporting, Corporate Financing and Tax | Entity formation assistance provided to Sky Core, Annual Reporting/Filings, Company Law, Corporate Finance, Tax Law |`

###### A.2.9.1.1.2.2 - Lawyer Registry Acceptance Criteria [Core]  <!-- UUID: 2b66ce16-d104-4238-b7d5-e4c6fe8d961b -->

To be included in the Lawyer Registry, lawyers must satisfy all requirements described in the following subelements.

###### A.2.9.1.1.2.2.1 - Lawyer Registry Licensing Criterion [Core]  <!-- UUID: fd8dec1d-6872-439d-b30a-eb4d39e2310b -->

Licensed legal professionals in their respective jurisdiction.

###### A.2.9.1.1.2.2.2 - Lawyer Registry Technology Experience Criterion [Core]  <!-- UUID: bbe5b615-0bfd-4dd4-b6a8-bae4af500261 -->

Proven experience with Sky Ecosystem crypto, or emerging technologies.

###### A.2.9.1.1.2.2.3 - Lawyer Registry No Conflicts Criterion [Core]  <!-- UUID: e74ab7b2-273e-4593-aee5-38af6c45dba6 -->

No Conflict of Interest in the matter over which they have carriage.

###### A.2.9.1.1.2.2.4 - Lawyer Registry Conflict Checks Criterion [Core]  <!-- UUID: e9fd410d-7bf4-483c-b6bf-2206dbb8c513 -->

Lawyers must have internal processes to conduct conflict checks prior to any engagement under this Section.

###### A.2.9.1.1.2.2.5 - Lawyer Registry Conflict Handling Criterion [Core]  <!-- UUID: d2581c75-828d-46dc-aac2-e2ae6ffd4e57 -->

Where conflicts arise within the lawyer’s firm, the firm must:

1. In the case where a Beneficiary is handling the claim, cease all further work and immediately notify the Resilience Technical Committee in writing and cooperate with the Resilience Technical Committee to avoid a continuing conflict or, where this is not practicable, transfer the matter to another LR registered Lawyer, and
2. In the case where the Guardian is handling the claim, cease all further work and immediately notify the Guardian in writing and cooperate with the Guardian to avoid a continuing conflict or, where this is not practicable, transfer the matter to another LR registered Lawyer.

###### A.2.9.1.1.2.3 - Resilience Fund Representation Requirements [Core]  <!-- UUID: b39f4808-18ae-456b-86fc-d449a69ea99a -->

Legal counsel providing services funded through the RF must fulfill additional requirements specified in the subdocuments herein. Legal counsel qualified for RF will be listed as such in the Lawyer Registry.

###### A.2.9.1.1.2.3.1 - Resilience Fund Representation Experience Requirement [Core]  <!-- UUID: 04852c06-a9c0-4775-a891-1fd8946083a7 -->

Lead Counsel, Lead Barristers, and Lead Trial Attorneys (as applicable) must each have a minimum of ten (10) years of relevant legal experience and demonstrable expertise in the specific areas of law, legal processes, and jurisdictions listed on the Lawyer Registry.

###### A.2.9.1.1.2.3.2 - Resilience Fund Representation Expertise Requirement [Core]  <!-- UUID: 23612175-bf87-4c2a-b295-a46900a36bbd -->

Lawyers included on the Lawyer Registry for litigious categories, must have been Lead Counsel in at least 15 cases in the relevant area of law, type of process, and jurisdiction for which they are listed. Lawyers included on the Lawyer Registry for non-litigious matters must have demonstrable experience in the relevant area of law, type of process and jurisdiction indicated in the table set out under [A.2.9.1.1.2.1 - Lawyer Registry Covered Areas](a176f67f-009f-44a0-a19b-169c2eb376a4).

###### A.2.9.1.1.2.4 - Lawyer Registry Template [Core]  <!-- UUID: d4bc5f95-a5a8-4f55-8db8-eb9f30cc0abf -->

Entries in the LR must follow this template:

- .x: [Advisor name and short description]
- .x.1: [Name of Firm]
- .x.2: [Specialization Area]
- .x.3: [Jurisdiction]
- .x.4: [RF qualified (y/n)]

###### A.2.9.1.1.2.5 - Requirements For Resilience Technical Committee [Core]  <!-- UUID: ba0f1c77-3fe8-45b5-bb5b-1bc84a3a5f8f -->

The Resilience Technical Committee will verify the eligibility criteria of new candidates in the Lawyer Registry and submit a list of approved candidates to the Core Facilitator.

###### A.2.9.1.1.2.6 - Lawyer Registry Update Process [Active Data Controller]  <!-- UUID: 2e3f851c-6ee2-472a-aa4f-cf637ff1cd8a -->

The current approved lawyers in the Lawyer Registry are defined as Active Data in [A.2.9.1.1.2.6.0.6.1 - Lawyer Registry Current Approved Legal Counsels](e1f72c98-e3f7-43b5-857c-82294abbbe09).

The Active Data is updated as follows:

- The Responsible Party is the Core Facilitator.
- The Update Process must follow the protocol for ‘Direct Edit’.

###### A.2.9.1.1.2.6.0.6.1 - Lawyer Registry Current Approved Legal Counsels [Active Data]  <!-- UUID: e1f72c98-e3f7-43b5-857c-82294abbbe09 -->

There are no active legal counsels in the Lawyer Registry.

##### A.2.9.1.1.3 - The Guardian [Core]  <!-- UUID: 0f808bde-fc68-4bda-bc6d-049c6aaaab1b -->

The Guardian is a specialized Ecosystem Actor that will be exclusively mandated to retain and instruct counsel to assist with the legal defense of actors in the Sky Ecosystem that, due to their organizational structure or circumstances, may be unable to obtain legal representation when pursuing or defending claims against adversarial parties.

##### A.2.9.1.1.4 - Legal Defense Standard Operational Protocols [Core]  <!-- UUID: bd82af2f-6617-4d4e-8acb-e23c7d2c904b -->

This document must define the Standard Operational Protocols (SOPs) for reacting against legal or regulatory actions against a participant of the Sky Ecosystem.

#### A.2.9.1.2 - Legal Risk Management [Core]  <!-- UUID: f50b0f4d-05c3-48ef-9073-997c9f678feb -->

This document defines the framework for managing, retaining, transferring, and structuring legal risk through instruments such as self-insurance and insurance.

##### A.2.9.1.2.1 - The Policyholder [Core]  <!-- UUID: fbc37039-df17-4146-9cbc-69dbc13c1d85 -->

The Policyholder is a specialized Ecosystem Actor in charge of executing agreements with external entities with the exclusive purpose of structuring and transferring risk to third parties through instruments such as insurances, reinsurances, mutuals, or other types of arrangements. These instruments will provide extended risk coverage for participants of the Sky Ecosystem and Agents.

The object of the Policyholder is to

- Act as a legal counterparty with insurance brokers, insurance, reinsurance, underwriters, or risk management companies.
- Act as a policyholder of insurance contracts, which will have as beneficiaries participants of the Sky Ecosystem.
- Hire suppliers and contractors necessary for the operation of self-insurance or insurance instruments, such as
    - The Resilience Technical Committee for claim management
    - Managers, Directors, and other executive staff of the legal vehicle. The power of directors will be limited to administrative and operative roles.

Sky Governance will have all necessary control mechanisms over the Policyholder:

- Sky Governance can designate and remove Directors, Supervisor, and Committees
- Sky Governance can instruct the entity to act and ratify decisions
- Power of directors is limited to administrative/operative roles
- The Policyholder will not manage Sky's assets nor will be legally affiliated with Sky.

The setup and operational budget of the legal vehicle will be sourced initially from the [A.2.9.1.1.1.1.1 - Resilience Fund Current Budget](aa1e93e5-8fc0-4e12-ad9d-8bb9f6cd8956). This is intended to move later to a separate budget.

##### A.2.9.1.2.2 - Policyholder Management [Core]  <!-- UUID: b376e933-f145-42a6-ac8b-462b6dbce497 -->

This document governs the adding and removing of Policyholders. SKY holders must first approve the structure and associated costs of the Policyholder, based on a Governance Poll initiated by Facilitators if they deem it necessary.

The list of currently approved Policyholders is maintained in [A.2.9.1.2.3 - Current Active Policyholders](6db0f9ee-9011-44da-8b75-521218f91aba).

##### A.2.9.1.2.3 - Current Active Policyholders [Core]  <!-- UUID: 6db0f9ee-9011-44da-8b75-521218f91aba -->

There are currently no active Policyholders.

#### A.2.9.1.3 - Privacy and Operational Security [Core]  <!-- UUID: 42c525ca-c541-4bf5-ac6a-7bd19960d583 -->

This document must define policies pertaining to operational security, privacy, and pseudonymity for participants in the Sky Ecosystem. The general purpose of this framework is to maximize security and safety for contributors and users and minimize potential attack vectors for the Ecosystem.

#### A.2.9.1.4 - Advocacy And Public Policy [Core]  <!-- UUID: 336b0e21-d62a-49d3-9179-14f467b7609c -->

This document defines the framework and processes for public policy, advocacy, and governmental relations. The general purpose of this framework is to develop innovative regulatory frameworks and standards that protect open source resources and position the Public Good Purpose of the Sky Ecosystem.

#### A.2.9.1.5 - Legal And Regulatory Risk Monitoring [Core]  <!-- UUID: 035ec13b-5676-45f0-a3b3-8b8e24a4adcf -->

This document defines the general framework and standard processes for monitoring and assessing risk and implementing responses. Risk assessment will include external/jurisdictional risk monitoring and internal risk monitoring.

Responses will be structured as Standard Operational Protocols (SOPs). The categories of Legal and Regulatory Risk Monitoring responses are:

- Preventive responses that reduce the likelihood of occurrence of a risk event
- Reactive responses that reduce the severity of consequences if the risk event materializes.
- Emergency Responses and Contingency Plans.

#### A.2.9.1.6 - Public Procurement Framework [Core]  <!-- UUID: d5ffcc76-3cde-475d-8336-fcb5ce499988 -->

This document defines a Public Procurement Framework for contributors and actors involved in the Sky Ecosystem. The purpose is to develop a standard framework that governs the entire lifecycle of service providers, which includes the following processes:

- Application process
- Selection process (scoring / evaluating proposals or applications)
- Hiring and payment process
- Performance evaluation and reporting
- Terminating involvement and resolving disputes

#### A.2.9.1.7 - Audit Procedure for Atlas Amendments [Core]  <!-- UUID: 92dcb95c-5a3d-45a4-a1e6-865686909c64 -->

This document must define the procedure for performing ex-post legal and technical audits of amended Atlas documents. The general purpose of this procedure is to ensure internal consistency and alignment of the Atlas as a whole.

#### A.2.9.1.8 - Technical And Legal Standards [Core]  <!-- UUID: 7c4e41ab-c8b4-4938-be92-994c58cf3e2e -->

This document defines the required technical-legal standards and tools such as, but not limited to, legal agreements ([A.2.8 - Ecosystem Accords](104c3543-ce94-4a2f-9968-57f1ee858085)), templates, and legal structures required to perform specific functions or roles in the Sky Ecosystem. The general purpose of this framework is to minimize trust assumptions and dependencies on specific actors, minimize personal exposure, and increase the accountability and predictability in their behavior.

#### A.2.9.1.9 - Code And Asset Licenses [Core]  <!-- UUID: 1d5042e4-d7b9-4a2b-b935-aae25220308a -->

Ecosystem Actors should generally release code and assets under the Apache 2.0 license, unless there are specific and clear reasons to use a different license, as determined by the Core Facilitator.

The Core Facilitator must ensure that a Foundation and other appropriate legal entities exists to properly protect intellectual property and trademarks related to the Sky Ecosystem.

Such Foundations or other entities must over time be set up to follow instructions from Sky Governance.

All Ecosystem Actors must take steps to protect the brands and trademarks relevant to the Sky Ecosystem, and in doing so must follow guidelines and best practice defined by the Foundations related to Trademarks, Code and Asset licenses.

## A.2.10 - Resilience Research and Preparedness [Article]  <!-- UUID: 29b21344-c651-4ea8-9d25-c1b0948c9dca -->

This Article defines infrastructure and processes to support resilience research and legal preparedness.

### A.2.10.1 - Resilience Research And Preparedness [Section]  <!-- UUID: 9bb5e917-2a88-4e9c-bb5c-2d803b0ddcf0 -->

The Support Scope is responsible for conducting ongoing resilience and preparedness research.

#### A.2.10.1.1 - Role Of Core Facilitator [Core]  <!-- UUID: aeb75fe3-f52b-4cdf-a206-1e54ef648d88 -->

The Core Facilitator must ensure that resilience research and preparedness efforts are continuously maintained to ensure the ecosystem is well-positioned to handle any legal uncertainty or risk that should arise. These projects must generally be broadly diversified across all jurisdictions where the Sky Ecosystem could be directly or indirectly exposed, but efforts and resources must be prioritized towards jurisdictions where risks are more likely to emerge.

##### A.2.10.1.1.0.3.1 - Resilience Research And Preparedness - Element Annotation [Annotation]  <!-- UUID: dff5ff4c-acb4-47cd-93a1-b435dd6db87e -->

This element refers to activities and studies aimed at strengthening Sky Ecosystem’s ability to respond effectively to legal uncertainties or risks, including monitoring and analysis of legal trends and regulatory changes; scenario planning and risk modeling; and the development of strategies to mitigate potential threats.

#### A.2.10.1.2 - Budget [Core]  <!-- UUID: 236dc6f0-afe4-4d9f-86ba-7bc975df3f7b -->

The Resilience Research and Preparedness budget is specified in [A.2.10.1.2.1 - Current Budget](afb4b3c3-96ad-422d-9033-bd4e5feca90c). The Core Facilitator can trigger a payout from the budget to a relevant recipient address through a Governance Poll.

##### A.2.10.1.2.1 - Current Budget [Core]  <!-- UUID: afb4b3c3-96ad-422d-9033-bd4e5feca90c -->

The Resilience Research and Preparedness budget is

- Up to 2,000,000 USDS available per year.

The full amount is immediately available at the start of the calendar year.

#### A.2.10.1.3 - Research Objectives [Core]  <!-- UUID: 47c4b698-5cd0-4917-9bf2-96cf385a5098 -->

Resilience Research and Preparedness (also "Resilience Research") projects must fulfill at least one of the following objectives:

- Bootstrap necessary infrastructure to develop one of the high-order legal resilience objectives as defined in this Article:
    - Legal Defense
    - Legal Risk Management
    - Privacy and Operational Security
    - Advocacy and Public Policy
    - Legal and Regulatory Risk Monitoring
    - Public Procurement Framework
    - Atlas Amendment and Audit
    - Technical and Legal Standards
- Design and implement processes that contribute directly to one of the high-order legal resilience objectives defined in this Article.
- Implement specific preventive or reactive legal risk mitigation tools.
- Execute specific activities or tasks necessary to fulfill one of the high-order legal resilience objectives defined in this Article.

#### A.2.10.1.4 - Application Process [Core]  <!-- UUID: f6af14d7-e62d-44c5-aa65-35c9ec979f4c -->

Ecosystem Actors can apply for a Resilience Research Project by submitting a proposal to be processed by the Support Scope. To submit a Resilience Research Proposal, the Ecosystem Actor must make a post on the Sky Forum following the template provided in [A.2.10.1.4.5 - Application Template](6cecf165-923a-4720-91f6-11c434afa641) and comply with all requirements described in the subdocuments herein.

##### A.2.10.1.4.1 - Costs And Benefits [Core]  <!-- UUID: e0eedeec-b982-413d-8381-2ceecf5f2e6b -->

Resilience Research Proposals must provide a clear and detailed account of both direct and indirect costs, as well as the anticipated results and benefits in relation to the Resilience Research Objectives.

##### A.2.10.1.4.2 - Team [Core]  <!-- UUID: e59dcf34-88f7-4ded-9101-b6ea71797cfe -->

Resilience Research Proposals must detail their headcount, team skillset composition, and reliance on third parties.

##### A.2.10.1.4.3 - Timeline And Milestones [Core]  <!-- UUID: 6f62cb26-d7cc-4a97-8837-79b80bd15d1b -->

Resilience Research Proposals must provide a clear timeline with detailed, granular milestones and the KPIs to review at each milestone.

##### A.2.10.1.4.4 - Risk Mitigation Impact [Core]  <!-- UUID: eb9be99b-81d4-46a6-95ff-e81ac56bd33c -->

Resilience Research Proposals must justify how the project will mitigate a specific risk or help bootstrap resources necessary to improve legal resilience.

##### A.2.10.1.4.5 - Application Template [Core]  <!-- UUID: 6cecf165-923a-4720-91f6-11c434afa641 -->

Applications for Resilience Research projects must follow this template:

- .x: [Project Name]
- .x.1: [Project Abstract: In 3-5 sentences, what problem are you trying to solve?]
- .x.2: [Objectives: What are you hoping to accomplish? How do you define and measure success for this project?]
- .x.3: [Outcomes: How does this project benefit the Sky Ecosystem? How does this project help fulfill one of the Legal Resilience Objectives in [A.2.9 - Legal Resilience](ac707ae4-65da-4cf9-8a34-8b9304cd9a95)]
- .x.4: [Scope: What will you research/build /design/implement? What is the expected output?]
- .x.5: [Project Team: How many people are working on this project? Please list their names and roles for the project and how many hours per month each person will work on this project?]
- .x.6: [Background: Relevant links, reference to other projects or research papers]
- .x.7: [Methodology: How do you plan to achieve your objectives?]
- .x.8: [Timeline: Please include a brief explanation of the milestones/roadmap, along with expected deliverables and KPIs.]
- .x.9: [Budget: Requested grant amount and how this will be used. Please provide the requested amount and outline how the funds will be used.]

#### A.2.10.1.5 - Review Process [Core]  <!-- UUID: 35aec115-f27c-42f2-9812-644a2df8f38f -->

The Core Facilitator must ensure that all Research Proposals are reviewed. The Core Facilitator should document their reviews of all Research Proposals they deem high quality, and publish them in the Sky Forum.

##### A.2.10.1.5.1 - Budget Availability [Core]  <!-- UUID: 9fd21b41-d5ca-4c19-ba21-c2120365b051 -->

Proposals should only be reviewed if there are available funds in the Resilience Research and Preparedness budget.

##### A.2.10.1.5.2 - Factors To Consider [Core]  <!-- UUID: d80f4451-c773-4ddf-b448-c42aaf0b64ec -->

Multiple factors should be considered when reviewing Research Proposals, including the amount of remaining budget, the potential impact on the Resilience Research Objectives, and whether the Research Proposal helps improve legal resilience as described in [A.2.9 - Legal Resilience](ac707ae4-65da-4cf9-8a34-8b9304cd9a95).

##### A.2.10.1.5.3 - Approval Process [Core]  <!-- UUID: cbf70252-fde5-4df7-8552-c778ecc3506a -->

Resilience Research Projects require different approval processes depending on the total cost of the project. Projects with a total cost under 15,000 USDS can be directly approved by the Core Facilitator and included in an Executive Vote without a prior Governance Poll. Projects with a total cost of 15,000 USDS or above require a Governance Poll followed by inclusion in an Executive Vote.

The Core Facilitator must formally approve the inclusion of funding in a Governance Poll or directly in an Executive Vote, as applicable, by replying to the Forum Post containing their evaluation (see [A.2.10.1.5 - Review Process](35aec115-f27c-42f2-9812-644a2df8f38f)).

###### A.2.10.1.5.3.0.3.1 - Included In An Executive Vote [Annotation]  <!-- UUID: e7f4ca65-be7d-4c05-b657-5c6243308e71 -->

The element "Included In An Executive Vote" refers to the Core Facilitator’s act of adding a Resilience Research and Preparedness grant payment to an Executive Vote. The Core Facilitator is also responsible for providing provenance for such requests by confirming payment requests on the Executive Sheet. See [A.1.11.1.3.0.3.1 - Executive Sheet - Element Annotation](52aef6ac-9eda-4795-9dab-73ea85b8ca31).

##### A.2.10.1.5.4 - Active Projects [Core]  <!-- UUID: dd379ac9-5e10-48ac-9b64-a1cb63d6ff51 -->

There are currently no active resilience research projects.

## A.2.11 - Ecosystem Security Infrastructure [Article]  <!-- UUID: 2427d573-5e69-4429-a267-97fa6e84ac43 -->

This Article defines ecosystem security infrastructure and processes to protect the Sky Protocol and its users.

### A.2.11.1 - Ecosystem Security Infrastructure [Section]  <!-- UUID: 49398799-ca02-4770-a42f-16292260076d -->

This Section manages Sky Ecosystem security infrastructure and initiatives.

#### A.2.11.1.1 - Bug Bounty Program For Critical Infrastructure [Core]  <!-- UUID: e48aa6f8-7806-40c5-a53d-d577249cc6e4 -->

As one of the most important DeFi protocols with a high TVL, the Sky Protocol is a honeypot for hackers and other nefarious actors. The Sky Protocol must always be protected by an active Bug Bounty Program. This document regulates the budget and processes of the Bug Bounty Program, which serves to protect the Sky Protocol and its users from hacks and exploits. The Bug Bounty Program is conducted on the Immunefi platform.

##### A.2.11.1.1.1 - Introduction [Core]  <!-- UUID: 54134f24-84a2-4130-80a5-a519f291c918 -->

The Bug Bounty Program aims to create incentives for hackers to contribute to the resilience of the Sky Protocol as opposed to exploiting vulnerabilities for personal gain. Immunefi is the party responsible for conducting the Bug Bounty Program; its setup and operations are based on standards set by Immunefi.

The Sky Ecosystem must continue to maintain a Bug Bounty Program for SparkLend until the launch of the Spark Agent.

##### A.2.11.1.1.2 - Scope [Core]  <!-- UUID: b9ed6d24-10e6-48dc-9348-9e2098d8dd31 -->

The subdocuments herein describe the scope of the Sky Bug Bounty Program, which currently includes both Sky Protocol and Spark Protocol.

###### A.2.11.1.1.2.1 - Assets In Scope [Core]  <!-- UUID: bc8630bb-ee26-47d6-9e9a-90c87bfcb7a1 -->

The Assets In Scope of the Sky Core Bug Bounty Program will be those identified as critical infrastructure for the Sky Ecosystem.

For Sky Core, the Assets In Scope accepted for this Bug Bounty Program are specified on Sky’s listing on the Immunefi platform, which can be found at ([https://immunefi.com/bug-bounty/sky/scope/](https://immunefi.com/bug-bounty/sky/scope/)). Assets in Scope include smart contracts, frontend applications, data infrastructure and oracles.

For SparkLend, the Assets In Scope for the Bug Bounty Program is specified on SparkLend’s listing on the Immunefi platform, which can be found at ([https://immunefi.com/bug-bounty/sparklend/scope/](https://immunefi.com/bug-bounty/sparklend/scope/)). For SparkLend, the Assets In Scope only include smart contracts.

The Protocol Security Workstream Lead is responsible for maintaining these lists of Assets In Scope, in consultation with the relevant stakeholders.

###### A.2.11.1.1.2.2 - Severity Classification [Core]  <!-- UUID: 223f562e-3542-4f08-9071-838cb41ad681 -->

The Immunefi Vulnerability Severity Classification System ([https://immunefi.com/severity-updated/](https://immunefi.com/severity-updated/)) is applicable to both Sky Core and SparkLend. The Protocol Security Workstream Lead is authorized to adopt a new severity system for the Bug Bounty Programs in consultation with relevant technical stakeholders.

###### A.2.11.1.1.2.3 - Impacts In Scope [Core]  <!-- UUID: 9a38cad6-c0e0-4ca2-931e-b9999710c6d5 -->

For Sky Core, the Impacts In Scope accepted for the Bug Bounty Program is specified on Sky’s listing on the Immunefi platform, which can be found at ([https://immunefi.com/bug-bounty/sky/scope/](https://immunefi.com/bug-bounty/sky/scope/)). The impacts are categorized into ‘smart contract’ and ‘websites and applications.’

For SparkLend, the Impacts In Scope for the Bug Bounty Program is specified on SparkLend’s listing on the Immunefi platform, which can be found at ([https://immunefi.com/bug-bounty/sparklend/scope/](https://immunefi.com/bug-bounty/sparklend/scope/)).

###### A.2.11.1.1.2.4 - Out Of Scope Vulnerabilities And Other Limitations [Core]  <!-- UUID: bfcb512b-787c-4509-b130-7bf1abd84c36 -->

A selection of vulnerabilities is deemed out of scope for the Bug Bounty Program. An overview of these out of scope vulnerabilities can be found on Sky’s listing on the Immunefi platform ([https://immunefi.com/bug-bounty/sky/scope/](https://immunefi.com/bug-bounty/sky/scope/)). Feasibility limitations also apply, which can be found in the aforementioned listing on the Immunefi website.

Specific rules applying to the Bug Bounty Program can be found at the website above, listed under the following categories:

- Repeatable attack limitations
- Restrictions on security researcher eligibility
- Public disclosure of known issues
- Proof of Concept (PoC) requirements
- Other terms and information
- Prohibited activities

For SparkLend, the rules, terms, and exceptions can be found on SparkLend’s listing on the Immunefi platform ([https://immunefi.com/bug-bounty/sparklend/scope/](https://immunefi.com/bug-bounty/sparklend/scope/)).

##### A.2.11.1.1.3 - Rewards Terms And Conditions [Core]  <!-- UUID: f934a75a-20f1-46d1-ae5e-56fa7da7b4cd -->

The subelements herein describe the Bug Bounty Program’s terms and conditions for rewards.

###### A.2.11.1.1.3.1 - Rewards For Smart Contract Vulnerabilities [Core]  <!-- UUID: 3dea6103-8e97-4602-866c-371054b71a01 -->

The Rewards per Threat Level for Smart Contract Vulnerabilities, including related terms, conditions and exceptions, are specified in Sky’s listing on the Immunefi platform ([https://immunefi.com/bug-bounty/sky/information/](https://immunefi.com/bug-bounty/sky/information/)).

For SparkLend, the Rewards per Threat Level for Smart Contract Vulnerabilities, including related terms, conditions and exceptions, are specified on SparkLend’s listing on the Immunefi platform ([https://immunefi.com/bug-bounty/sparklend/information/](https://immunefi.com/bug-bounty/sparklend/information/)).

###### A.2.11.1.1.3.2 - Rewards For Website And Application Vulnerabilities [Core]  <!-- UUID: 9c4f269d-b365-4e44-89bc-e99d71737f40 -->

The Rewards per Threat Level for Website and Application Vulnerabilities, including related terms, conditions and exceptions, are specified in Sky’s listing on the Immunefi platform ([https://immunefi.com/bug-bounty/sky/information/](https://immunefi.com/bug-bounty/sky/information/)).

###### A.2.11.1.1.3.3 - Rewards Payment Terms [Core]  <!-- UUID: cf4e6968-18a3-48d8-b38e-15ae8009d03d -->

The subelements herein describe the payment terms for the Bug Bounty Program for Sky Critical Infrastructure.

###### A.2.11.1.1.3.3.1 - Rewards Denomination [Core]  <!-- UUID: f06632c1-5c19-4851-ac68-b6d21466f1c4 -->

Payments are denominated in USD. However, payouts are done in USDS assuming a full 1:1 ratio with the USD. However, if the price of USDS deviates from the USD value by more than 1%, the amount of USDS will be adjusted.

###### A.2.11.1.1.3.3.2 - Rewards Payout Process [Core]  <!-- UUID: 07f4faa6-f900-46e6-87d4-137fe2e5cb99 -->

All bounty payouts are handled by Sky Governance. Upon confirmation, bug bounty payouts should be included in the next possible Executive Vote. This would involve sending USDS directly from the protocol’s buffer to the whitehat hacker.

Immunefi will publicly contact the Core Facilitator with the request, including a specification of the respective vulnerability report, the requested amount and the Ethereum mainnet addresses of the beneficiaries. This should also include the payment details of the Immunefi fee, if it applies. Immunefi and the Core Facilitator should make sure the payout is made within one full calendar month after the report was approved.

For Bug Bounty rewards over USD 1,000,000: after the first million is paid out, the remaining amount is paid out over time with up to USD 1,000,000 per consecutive month until the determined amount for payout is reached.

###### A.2.11.1.1.3.3.3 - Rewards Budget [Core]  <!-- UUID: 97359514-045c-4699-8b1e-e68fe13f8840 -->

The Bug Bounty Programs incur fixed and variable costs.

- Variable costs: Bug bounty payouts including related fees to Immunefi are considered variable costs and are covered by the process described in [A.2.11.1.1.3.3 - Rewards Payment Terms](cf4e6968-18a3-48d8-b38e-15ae8009d03d).
- Fixed costs: Fixed costs comprise service fees for the Immunefi Premium Triaging Service, and compensation of a part-time Bug Bounty program steward. These costs will be funded by Sky.

#### A.2.11.1.2 - Safe Harbor [Core]  <!-- UUID: bb494bc1-f3cb-4b7f-826f-437c62d534c8 -->

Sky Ecosystem is adopting the Security Alliance Safe Harbor Agreement ("Safe Harbor") by executing the procedures specified in [A.2.11.1.2.2 - Execution](25015208-5234-4818-8479-c46f927c272c). Safe Harbor is a public agreement that protocols may adopt to waive the right to pursue legal claims against a whitehat hacker, provided that the hacker acts competently, lawfully, and in good faith. Under Safe Harbor, any whitehat hacker who identifies a time-critical active exploit that could result in the loss of funds is authorized to act immediately to rescue those funds. Immediate intervention prevents delays that might otherwise cause irrevocable financial harm. Once the funds have been secured, the whitehat hacker returns them within 72 hours to an Asset Recovery Address (see [A.2.11.1.2.2.3.3.2 - Asset Recovery Addresses](3f125522-dff7-48a3-948f-e99c71fc3929)) designated by the protocol that has adopted the Safe Harbor Agreement.

##### A.2.11.1.2.1 - Agreement [Core]  <!-- UUID: c3705a82-9cda-4626-89bb-2ec21774b371 -->

Safe Harbor is an onchain agreement. The agreement is specified in [https://etherscan.io/address/0xf17bb418b4ec251f300aa3517cb37349f17697a1#readContract#F2](https://etherscan.io/address/0xf17bb418b4ec251f300aa3517cb37349f17697a1#readContract#F2). The agreement located at the IPFS address shown in the smart contract above is the definitive version of the agreement.

##### A.2.11.1.2.2 - Execution [Core]  <!-- UUID: 25015208-5234-4818-8479-c46f927c272c -->

The agreement is executed by calling the `adoptSafeHarbor` function on the Safe Harbor registry contract. The Core Facilitator is directed to include the adoption of Safe Harbor in an upcoming Executive Spell.

###### A.2.11.1.2.2.1 - Safe Harbor Registry Contract [Core]  <!-- UUID: 2b097341-3735-43d4-9a18-8a43626a4f4e -->

The address of the Safe Harbor registry contract on the Ethereum Mainnet is `0x326733493E143b8904716E7A64A9f4fb6A185a2c`.

###### A.2.11.1.2.2.2 - Agreement Address [Core]  <!-- UUID: 0f541963-584d-4bcd-8c00-adbbcb85edf8 -->

The address of the Safe Harbor agreement is `0xf17bB418B4EC251f300Aa3517Cb37349f17697A1`.

###### A.2.11.1.2.2.3 - Execution Parameters [Core]  <!-- UUID: b061e1d9-76c3-444a-9a91-641c5d00315d -->

The `adoptSafeHarbor` function on the Safe Harbor registry contract should be called with the parameters specified herein.

###### A.2.11.1.2.2.3.1 - Agreement URI Parameter [Core]  <!-- UUID: 0064ee74-b8bb-4c83-b7a1-cafee3c6e55f -->

The `agreementURI` parameter is the IPFS address of the agreement. The value of the `agreementURI` parameter is [https://bafkreiernns2f4nv2uzvwtzjc2jboyivsu2mixz33y3xo7cvtllsuao6jy.ipfs.w3s.link/](https://bafkreiernns2f4nv2uzvwtzjc2jboyivsu2mixz33y3xo7cvtllsuao6jy.ipfs.w3s.link/).

###### A.2.11.1.2.2.3.2 - Bounty Terms Parameters [Core]  <!-- UUID: 206c02ae-b87e-4ed4-95c1-0312b8c73e40 -->

The elements of the `bountyTerms` parameter are specified in the documents herein.

###### A.2.11.1.2.2.3.2.1 - Bounty Cap USD Parameter [Core]  <!-- UUID: 062e64d7-647b-4025-b6ea-d0659737b56b -->

The `bountyCapUSD` parameter is the maximum amount in USD of the bounty. The value of the `bountyCapUSD` parameter is `10000000`.

###### A.2.11.1.2.2.3.2.2 - Bounty Percentage Parameter [Core]  <!-- UUID: 226543b7-8cb0-4d26-9569-e5b760f986f5 -->

The `bountyPercentage` parameter is the value to which the whitehat hacker is entitled, expressed as a percentage of the funds recovered. The value of the `bountyPercentage` parameter is `10`.

###### A.2.11.1.2.2.3.2.3 - Diligence Requirements Parameter [Core]  <!-- UUID: 3b5d10d1-16b0-49d8-88e6-9d1185e5de4f -->

The `diligenceRequirements` parameter includes KYC, assessing compliance with sanctions (for instance, ensuring that individuals or entities from sanctioned jurisdictions are excluded), diligence, or other verification that the protocol requires the whitehat hacker to satisfy in order to claim the bounty. The value of the `diligenceRequirements` parameter is:

`"KYC and Sanctions Screening. Sky and Stars require all eligible whitehats to undergo Know Your Customer (KYC) verification and be screened against global sanctions lists, including OFAC, UK, and EU regulations. This ensures that bounty recipients meet legal and regulatory standards before qualifying for payment. The verification process shall be conducted by a trusted third-party provider at Sky and Stars discretion, and all data is deleted, if successful, within 30 days post-verification."`

###### A.2.11.1.2.2.3.2.4 - Identity Parameter [Core]  <!-- UUID: 46f3510c-0dbd-40aa-b9fa-abcb59a7ff75 -->

The `identity` parameter specifies the identity requirements for the whitehat hacker and may either be `0` for `Anonymous` (the whitehat hacker may be anonymous), `1` for `Pseudonymous` (the whitehat hacker must provide at least a pseudonym), or `2` for `Named` (the whitehat hacker must provide their legal name). The value of the `identity` parameter is `2`.

###### A.2.11.1.2.2.3.2.5 - Retainable Parameter [Core]  <!-- UUID: 6ca0bed7-e4b2-4b48-9d03-5ec410ce9fc4 -->

The `retainable` parameter specifies whether the whitehat hacker may retain the bounty out of the funds recovered or must first return the entire recovered amount to the Asset Recovery Address before receiving payment from the protocol. The value of the `retainable` parameter is `false`.

###### A.2.11.1.2.2.3.3 - Chains Parameter [Core]  <!-- UUID: 80c4c6f0-aade-4908-adaa-847de153d75e -->

The `chains` parameter specifies each blockchain on which a funds rescue is authorized. For each chain, the following information must be specified: (1) the `chainId` of the chain, (2) the `assetRecoveryAddress` to which recovered funds should be sent, and (3) the `scope`of contracts on the chain that are covered by Safe Harbor. The chains are specified in the subdocuments herein.

###### A.2.11.1.2.2.3.3.1 - Chain IDs [Core]  <!-- UUID: b5190639-a193-4b8b-8c3a-4d90b369ad07 -->

The value of the `chainId` parameter for each chain is:

- Ethereum Mainnet - `1`
- Arbitrum - `42161`
- Optimism - `10`
- Base - `8453`
- Unichain - `130`
- Solana - `5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp`
- Avalanche - `43114`
- Plasma - `9745`

###### A.2.11.1.2.2.3.3.2 - Asset Recovery Addresses [Core]  <!-- UUID: 3f125522-dff7-48a3-948f-e99c71fc3929 -->

The Asset Recovery Address is the Pause Proxy on Ethereum Mainnet and the Governance Relay on each other chain. The value of the `assetRecoveryAddress` parameter for each chain is:

- Ethereum Mainnet - `0xbe8e3e3618f7474f8cb1d074a26affef007e98fb`
- Arbitrum - `0x10E6593CDda8c58a1d0f14C5164B376352a55f2F`
- Optimism - `0x10E6593CDda8c58a1d0f14C5164B376352a55f2F`
- Base - `0xdD0BCc201C9E47c6F6eE68E4dB05b652Bb6aC255`
- Unichain - `0x3510a7F16F549EcD0Ef018DE0B3c2ad7c742990f`
- Solana - `AYPtjx4Hc8us1ikULUedkmZ3wtiD6tmL7gK3qe4V3oHt`
- Avalanche - `0xe928885BCe799Ed933651715608155F01abA23cA`
- Plasma - `0x5CE28f2dD353945db9AB3273A2a1dD1AB632e24b`

###### A.2.11.1.2.2.3.3.3 - Accounts [Core]  <!-- UUID: c6591c5c-c767-4769-b2d6-80564d96fa48 -->

The `accounts` parameter for each chain is a list of contracts to be included in Safe Harbor. Each contract listed must include the sub-elements of (1) the `accountAddress` of the contract and (2) the `childContractScope`, which specifies whether child contracts of the specified contract are covered. The possible values for the `childContractScope` parameter are: (1) `None` (no child contracts are in scope), (2) `ExistingOnly` (only child contracts created prior to calling `adoptSafeHarbor` are in scope), or (3) `All` (all child contracts are in scope).

The value of the `scope` parameter is all contracts specified in the Bug Bounty Program.

The `childContractScope` parameter for each contract is specified in the Bug Bounty Program.

###### A.2.11.1.2.2.3.4 - Contact Details [Core]  <!-- UUID: 611baee4-7c68-47ba-a683-25e795f55101 -->

The representatives of the protocol should be contacted as specified in the Safe Harbor registry.

###### A.2.11.1.2.2.3.5 - Protocol Name Parameter [Core]  <!-- UUID: 3ecab562-7477-4606-bce3-74da81dc78e6 -->

The `protocolName` parameter specifies a human-readable name for the protocol. The value of the `protocolName` parameter is “Sky”.

##### A.2.11.1.2.3 - Maintenance [Core]  <!-- UUID: fcd868db-4a91-4ee0-baf5-1ebd40fc651e -->

The list of contracts covered by the Safe Harbor agreement for Sky must be updated when new contracts are added. Whenever a contract is added to the Bug Bounty Program, it should also be added to Safe Harbor. The Spell Teams are primarily responsible for updating the Safe Harbor registry each time a contract is added to the Bug Bounty Program. The Core Facilitator is responsible for reviewing the work of the Spell Teams to ensure that this requirement is met.

##### A.2.11.1.2.4 - Frontends [Core]  <!-- UUID: 45ab54e8-309a-4149-91cc-fcdbeb5d1d37 -->

The terms and conditions of frontends operated by Sky must be updated to include consent to the potential rescue of funds. Core GovOps must work with relevant Ecosystem Actors to ensure that the contents contained in Exhibit D of the Safe Harbor agreement are incorporated into the terms of conditions governing the frontends operated by Sky and/or Prime Agents.

##### A.2.11.1.2.5 - Prime Responsibilities [Core]  <!-- UUID: 48d7232f-59c5-459c-b868-498d0ce00457 -->

Primes must develop processes to register contracts they deploy with Safe Harbor. Primes must include the terms and conditions specified in Exhibit D of the Safe Harbor agreement in all frontends that they operate.

##### A.2.11.1.2.6 - Agreement Fact Page [Core]  <!-- UUID: 258e85f5-df03-45c5-874e-c2c7fa0fbe87 -->

[A.2.11.1.2 - Safe Harbor](bb494bc1-f3cb-4b7f-826f-437c62d534c8) constitutes the "Agreement Fact Page" as specified in the Safe Harbor Agreement.


#### A.2.11.1.3 - Multisig Security Enforcement [Core]  <!-- UUID: 142ed420-18a6-4ab9-9889-cbd9c376d48d -->

The documents herein establish the security policies, oversight mechanisms, processes, security requirements, and operational procedures governing the use and administration of Multisigs within the Sky Ecosystem.

##### A.2.11.1.3.1 - Purpose [Core]  <!-- UUID: c2facaa0-f700-49aa-bcbe-ffc0649eb02b -->

The Multisig Security Enforcement Framework establishes binding policies and operational requirements for the use of Multisig wallets across the Sky Ecosystem. Its objective is to ensure that Multisigs used to control smart contracts, allocate capital, and operate under emergency conditions across Sky Core and Prime Agent infrastructure comply with established security and operational requirements, providing clear grounds for oversight, auditing, and enforcement in cases of noncompliance.

###### A.2.11.1.3.1.1 - Multisig Administrator [Core]  <!-- UUID: aa2c4af5-5530-4872-9750-20813f3cd258 -->

A Multisig Administrator is the entity or individual responsible for the setup, configuration, ongoing management, and compliance of a Multisig. Each Multisig must have a designated Multisig Administrator, communicated to the Protocol Security Workstream Lead and Core GovOps prior to the Multisig's activation or operational use.

##### A.2.11.1.3.2 - Multisig Security Guidelines [Core]  <!-- UUID: 6033699f-1d55-45ba-8eb1-bd8982571cc0 -->

The documents herein specify the requirements governing Multisig planning, operation, and administration. All requirements in the documents herein shall take effect on May 20, 2026.

###### A.2.11.1.3.2.1 - Multisig Setup [Core]  <!-- UUID: 2b44acd9-b589-4a4d-b367-e26a387b2358 -->

The documents herein specify requirements and relevant operational processes that must be satisfied prior to Multisig activation or operational use.

###### A.2.11.1.3.2.1.1 - Multisig Administrator Responsibilities - Setup [Core]  <!-- UUID: e5751fe2-fc2b-4bc8-b9c1-828fef7fc38f -->

The documents herein define the responsibilities and requirements applicable to Multisig Administrators prior to Multisig activation or operational use. Multisig Administrators may consult the operational guides specified in [A.2.11.1.3.2.3 - Operational Guides](37f6864d-5f6a-43fd-adbe-f3b2e82c9e01) for guidance on fulfilling these requirements.

###### A.2.11.1.3.2.1.1.1 - Multisig Classification [Core]  <!-- UUID: c2344b39-faa2-45af-ab97-99ff521d0826 -->

The documents herein define relevant processes by which the Multisig Administrator classifies a Multisig in order to determine the appropriate security measures prior to its activation and operational use.

###### A.2.11.1.3.2.1.1.1.1 - Impact Assessment [Core]  <!-- UUID: 3c0847fe-e117-40f8-86a3-9de56c9a3bba -->

Impact Assessment defines the assessment process in which the potential impact of a Multisig compromise or failure is evaluated. The result of this evaluation is the assignment of an Impact Classification level as defined below. The Multisig Administrator is responsible for determining this classification and must provide it to Core GovOps as part of the Multisig registration process in accordance with [A.2.11.1.3.2.1.1.8 - Multisig Registration](110614e9-6375-464a-90b3-3b350d3cf79c).

| **Impact Classification Level** | **Financial Exposure** | **Decision Context** | **Reputational Impact** |
|---|---|---|---|
| Low | <$100k direct exposure | Minimal disruption, alternative paths exist | Limited scope impact |
| Medium | $100k – $1M exposure | Significant operational delays, workarounds available | Moderate reputational concern |
| High | $1M – $10M exposure | Major protocol disruption, difficult recovery | Serious reputational damage |
| Critical | >$10M exposure | Protocol-wide failure, catastrophic impact | Severe reputational damage |

When a Multisig falls between two classification levels, the higher security classification must be selected.

###### A.2.11.1.3.2.1.1.1.2 - Operational Assessment [Core]  <!-- UUID: 35224359-76a6-41fe-adc2-6f70a29f3f4a -->

Operational Assessment defines the assessment process in which the operational response requirements of a Multisig are evaluated. The result of this evaluation is the assignment of an Operational Classification type as defined below. The Multisig Administrator is responsible for determining this classification and must provide it to Core GovOps as part of the Multisig registration process in accordance with [A.2.11.1.3.2.1.1.8 - Multisig Registration](110614e9-6375-464a-90b3-3b350d3cf79c).

| **Operational Classification Type** | **Response Time** | **Decision Context** | **Verification Process** |
|---|---|---|---|
| Routine | 24 - 48 hours | Standard procedures, predictable operations | Full verification protocols |
| Time-Sensitive | 2 - 12 hours | Market conditions, protocol needs | Streamlined but thorough |
| Emergency | <2 hours | Crisis response, preventing immediate damage | Minimal delays, risk-appropriate |

When a Multisig falls between two classification levels, the higher security classification must be selected.

###### A.2.11.1.3.2.1.1.2 - Thresholds And Configuration [Core]  <!-- UUID: e410573b-a92a-4686-9b4b-71b97d73e99c -->

The documents herein define all requirements relating to Multisig thresholds and configuration.

###### A.2.11.1.3.2.1.1.2.1 - Threshold Requirements [Core]  <!-- UUID: 89b7bcf9-8268-4e46-bdfb-dae3a5985a98 -->

The baseline minimum threshold standards applicable to all Multisigs are:

- Multisigs must have a minimum of three (3) signers.
- Multisigs must maintain a signing threshold of at least fifty percent (50%) of total signers.

These requirements apply unless explicitly exempted in [A.2.11.1.3.2.1.1.2.2 - Threshold Exceptions](130a44af-0715-4aa6-b248-f4a267ebe1a4).

Additional threshold requirements or considerations may apply depending on the specific operational use case of the Multisig. Such requirements are defined in [A.2.11.1.3.2.1.1.2.3 - Additional Use-Case Specific Threshold Requirements And Considerations](5af1115e-5155-449a-829d-6e641af49b0f).

###### A.2.11.1.3.2.1.1.2.2 - Threshold Exceptions [Core]  <!-- UUID: 130a44af-0715-4aa6-b248-f4a267ebe1a4 -->

Threshold Exceptions define the limited circumstances under which Multisigs may operate below the baseline threshold requirements defined in [A.2.11.1.3.2.1.1.2.1 - Threshold Requirements](89b7bcf9-8268-4e46-bdfb-dae3a5985a98).

Exceptions may be permitted by Core GovOps, in consultation with the Protocol Security Workstream Lead. Examples include rate-setting or parameter adjustment operations where parameters are tightly bounded and set by governance, and where a defined recovery or replacement mechanism exists in the event of Multisig failure or compromise.

Certain Threshold Exceptions instead apply as standing exemptions to a defined category of Multisig, without requiring a case-by-case grant. These are specified in the documents herein.

###### A.2.11.1.3.2.1.1.2.2.1 - Emergency-Response Multisig Threshold Exception [Core]  <!-- UUID: 55f1c795-0653-4dda-9f05-b3068d2608e3 -->

As a transitionary measure, pending the development of specific threshold requirements for emergency-response Multisigs, a Multisig whose sole capability is an emergency-response function — such as an emergency freeze, pause, or the removal of a compromised Relayer — that cannot move, custody, or allocate assets, is not subject to the minimum signer or signing-threshold requirements specified in [A.2.11.1.3.2.1.1.2.1 - Threshold Requirements](89b7bcf9-8268-4e46-bdfb-dae3a5985a98). Such a Multisig is configured to optimize for rapid emergency response.

###### A.2.11.1.3.2.1.1.2.3 - Additional Use-Case Specific Threshold Requirements And Considerations [Core]  <!-- UUID: 5af1115e-5155-449a-829d-6e641af49b0f -->

Additional threshold requirements and considerations may apply depending on the specific operational use case of the Multisig. These requirements supplement the baseline threshold requirements defined in [A.2.11.1.3.2.1.1.2.1 - Threshold Requirements](89b7bcf9-8268-4e46-bdfb-dae3a5985a98).

###### A.2.11.1.3.2.1.1.2.3.1 - Smart Contract Control Multisig Threshold Consideration [Core]  <!-- UUID: 2a4762e5-b369-45c1-98d6-4dfb34b4ac17 -->

Higher signing thresholds should be used for operations involving contract upgrades or significant protocol changes. As a general guideline, thresholds equivalent to at least seven of nine (7/9) signers, or an equivalent supermajority, should be used where feasible. Lower thresholds may be acceptable for highly constrained operations where execution scope is limited by on-chain parameter bounds.

###### A.2.11.1.3.2.1.1.2.3.2 - High-Value Asset Multisig Threshold Requirement [Core]  <!-- UUID: ca29bdf9-0d6f-42ee-aae5-cb361799cf92 -->

Multisigs managing assets with a value equal to or greater than one million USD ($1,000,000) equivalent must have no fewer than seven (7) signers. This requirement applies to custodial control of assets, not emergency freeze functions.

###### A.2.11.1.3.2.1.1.3 - Multisig Configuration Restrictions [Core]  <!-- UUID: 1f7afd0e-b5b4-47a1-83a0-b15de7a112f8 -->

The documents herein define all requirements relating to Multisig configurations.

###### A.2.11.1.3.2.1.1.3.1 - Module Requirement [Core]  <!-- UUID: 492d766d-908c-4dbc-bbcf-e8b9ad720d73 -->

Multisigs must not utilize any modules or guards, except those explicitly permitted for the applicable use case in [A.2.11.1.3.2.1.1.3.2 - Use-Case Specific Configuration Requirements And Considerations](f8d0e4df-acca-4f20-a030-584efb4a8695).

###### A.2.11.1.3.2.1.1.3.2 - Use-Case Specific Configuration Requirements And Considerations [Core]  <!-- UUID: f8d0e4df-acca-4f20-a030-584efb4a8695 -->

Additional configuration requirements, exceptions or considerations may apply depending on the specific operational use case of the Multisig, and these requirements are specified in the subdocuments herein.

###### A.2.11.1.3.2.1.1.3.2.1 - Treasury Multisig Configuration Requirements [Core]  <!-- UUID: f5ed192d-8c49-4095-9b98-840a1a31d47a -->

Treasury Multisigs must use an allowance module that grants the Sky Pause Proxy allowance equal to the maximum amount of each token held by the Multisig.

###### A.2.11.1.3.2.1.1.3.2.2 - Capital Allocation Multisig Configuration Requirements And Considerations [Core]  <!-- UUID: 925a2690-e538-4406-9f6c-491da4f6c58e -->

Capital Allocation Multisigs should implement on-chain constraints wherever feasible, including, but not limited to, smart contract limits or parameter bounds.

###### A.2.11.1.3.2.1.1.3.2.3 - Smart Contract Control Multisig Configuration Requirements And Considerations [Core]  <!-- UUID: 0f76bf08-c7a2-4088-b5f7-8b5ac25e748e -->

For Multisigs responsible for smart contract control, the following requirements apply:

- Major contract changes, including, but not limited to, upgrades or significant parameter changes, must be subject to timelock contracts or equivalent delay mechanisms where feasible.
- Protocol parameters controlled by Multisigs must be bounded through smart contract enforcement where feasible.

###### A.2.11.1.3.2.1.1.4 - Standard Threshold Recommendations [Core]  <!-- UUID: 022c6cf1-9fba-4c3d-8f15-aa2c616d27c6 -->

Standard Thresholds refer to recommended Multisig threshold configurations based on use case, Impact Classification level (as defined in [A.2.11.1.3.2.1.1.1.1 - Impact Assessment](3c0847fe-e117-40f8-86a3-9de56c9a3bba)), and Operational Classification type (as defined in [A.2.11.1.3.2.1.1.1.2 - Operational Assessment](35224359-76a6-41fe-adc2-6f70a29f3f4a)). These standards serve as guidance to the Multisig Administrator during Multisig setup.

| **Use Case** | **Impact Classification Level** | **Operational Classification Type** | **Standard Threshold** |
|---|---|---|---|
| Treasury - Large | High | Routine | 4/7 |
| Treasury - Small | Medium | Routine | 3/5 |
| Emergency Freeze | Critical | Emergency | 2/4 |
| Capital Allocation | High | Time-Sensitive | 3/5 |
| Protocol Parameters | High | Routine | 4/7 |
| Constrained DeFi | Medium | Time-Sensitive | 2/3 |

###### A.2.11.1.3.2.1.1.5 - Backup Infrastructure Recommendations [Core]  <!-- UUID: 42a339d4-5caa-4ea1-bfeb-a0c49d898591 -->

The documents herein outline recommended practices for establishing and maintaining backup infrastructure to help ensure that Multisig signers can continue to monitor, verify, and execute transactions if primary user interfaces, RPC providers, or block explorers become unavailable.

###### A.2.11.1.3.2.1.1.5.1 - Backup Interface Setup Recommendations [Core]  <!-- UUID: 864fe73b-3fd4-4f95-9f26-ece6ef53d925 -->

The Multisig Administrator should ensure that alternative Multisig user interfaces are available to signers in the event that the primary interface becomes unavailable. These interfaces should ideally be accessible through independent infrastructure and may include self-hosted or locally runnable alternatives where available.

###### A.2.11.1.3.2.1.1.5.2 - RPC Redundancy Recommendations [Core]  <!-- UUID: b5abaa31-031c-4488-a900-05fe5c1afff4 -->

The Multisig Administrator should maintain access to multiple RPC providers for each supported network to help preserve operational continuity if a primary provider becomes unavailable. Where possible, RPC providers should be selected to minimize shared infrastructure dependencies.

###### A.2.11.1.3.2.1.1.6 - Communication Setup [Core]  <!-- UUID: f7950657-3cf5-4dec-939b-17e13f2f7e9d -->

The Multisig Administrator is responsible for establishing and maintaining communication channels and communication readiness in accordance with the requirements defined in the subdocuments herein.

###### A.2.11.1.3.2.1.1.6.1 - Primary Communication Channel Requirement [Core]  <!-- UUID: ebe71281-44d5-46b8-a64f-eda51d5184b5 -->

A dedicated communication channel must be established for Multisig operations. The Multisig Administrator is responsible for ensuring that the channel is restricted to Multisig signers and authorized participants and supports reliable and timely operational communication and coordination between participants.

###### A.2.11.1.3.2.1.1.6.2 - Backup Communication Channel Requirement [Core]  <!-- UUID: fa17d9fc-b505-411b-995b-5bde1ae8ebc3 -->

A backup communication channel, established on a different platform from the primary communication channel, must be established to maintain communication continuity in the event the primary channel becomes unavailable. The Multisig Administrator is responsible for ensuring that the backup channel follows the same access and participation constraints as the primary channel.

###### A.2.11.1.3.2.1.1.6.3 - Emergency Communication Readiness Requirement [Core]  <!-- UUID: 8976fa02-7f24-4d42-8f13-8acfb8757d1b -->

Multisig Administrators are responsible for ensuring that Multisigs classified with an Emergency or Time-Sensitive Operational Classification level, as defined in [A.2.11.1.3.2.1.1.1.2 - Operational Assessment](35224359-76a6-41fe-adc2-6f70a29f3f4a), maintain communication and alerting mechanisms capable of reliably and rapidly reaching signers, enabling timely execution of required actions in accordance with the operational response expectations of the Multisig. Multisig Administrators must also include Signers in the approved Emergency Response contact mechanisms as specified in [A.1.9.1.3.2.2 - Approved Emergency Contact Mechanisms](57006d4e-cd91-4565-97b5-5fab73fa94d5).

###### A.2.11.1.3.2.1.1.6.4 - Communication Access Removal Requirement [Core]  <!-- UUID: 317732f8-d609-42a5-9367-c892451cac81 -->

Any signer removed from a Multisig must be promptly removed from all Multisig communication channels and communication systems associated with that Multisig, including primary and backup communication channels. The Multisig Administrator is responsible for ensuring that access is limited to current authorized participants.

###### A.2.11.1.3.2.1.1.7 - Signer Security Check [Core]  <!-- UUID: e60b83f2-04a5-4c4a-9666-b2f4f2f55330 -->

The Multisig Administrator must ensure that all Multisig signers comply with the applicable signer security requirements as outlined in [A.2.11.1.3.2.1.2.2 - Signer Security Requirements](3f441562-4c03-429c-8934-f0f87fa0eee7), prior to operational use of the Multisig.

###### A.2.11.1.3.2.1.1.8 - Multisig Registration [Core]  <!-- UUID: 110614e9-6375-464a-90b3-3b350d3cf79c -->

All Multisigs currently in use or intended for use within Treasury Management, Emergency Operations (including Freezer or equivalent emergency control Multisigs), Capital Allocation, or Smart Contract Control (including protocol parameter management and constrained DeFi operations) must be registered prior to their inclusion in any Spell or governance execution process.

The Multisig Administrator is responsible for communicating all necessary details about the Multisig to Core GovOps for registration in accordance with the information requirements outlined in [A.2.11.1.3.4 - Multisig Registry](4d80cae1-b28a-4907-8d59-2ebcbba6003d). Core GovOps must coordinate with the Protocol Security Workstream Lead to obtain approval prior to completing the registration.

###### A.2.11.1.3.2.1.2 - Signer Responsibilities - Setup [Core]  <!-- UUID: 3331e101-36f1-45e5-be2e-e22757b3083b -->

The documents herein define the responsibilities and requirements applicable to Multisig signers during the setup phase of a Multisig. Signers may consult with their Multisig Administrator for guidance on fulfilling these requirements.

###### A.2.11.1.3.2.1.2.1 - Signer Verification Process [Core]  <!-- UUID: 002821ab-c67c-4eb1-987c-69e759ab7b3c -->

Multisig signers must verify their addresses prior to being added to a Multisig. The documents herein define the processes and requirements related to the Signer Verification Process.

###### A.2.11.1.3.2.1.2.1.1 - Verification Signature [Core]  <!-- UUID: d1b44379-1e60-480f-b6f8-574e4d2bbb1e -->

The signer must produce a cryptographically signed message demonstrating control of the signer address intended for Multisig participation. The signed message must include the following:

- A statement indicating that the signer intends to join the specified Multisig;
- The Multisig address;
- The signer address intended for participation;
- The signer's handle, entity name, or other identifying affiliation sufficient to establish accountability.

###### A.2.11.1.3.2.1.2.1.2 - Verification Submission [Core]  <!-- UUID: 84a4c85e-0396-499b-955b-7eb64275b21d -->

The verification signature must be shared with the Multisig Administrator.

###### A.2.11.1.3.2.1.2.2 - Signer Security Requirements [Core]  <!-- UUID: 3f441562-4c03-429c-8934-f0f87fa0eee7 -->

Multisig signers must comply with the following security requirements:

- All Multisig signers must use hardware wallets for signing operations. The associated seed phrase must be securely backed up using physical, offline storage methods only. Seed phrases must never be stored digitally, including in photographs, files, password managers, cloud storage, email, or messaging applications. Seed phrase backups must be stored on durable offline media and kept in secure physical locations with appropriate access controls to prevent unauthorized access or single-point compromise.
- Signers must use a unique signing address per Multisig and must not reuse the same signing address across Multisigs.
- Signers participating in Multisigs responsible for critical protocol configuration or security-sensitive operations should not use their signing addresses for personal transactions or other unrelated activities and should instead use a dedicated address created specifically for Multisig participation.

###### A.2.11.1.3.2.2 - Multisig Ongoing Management [Core]  <!-- UUID: c010de5a-57a5-4cdf-9852-d6570b7791ca -->

The documents herein define the responsibilities and requirements relating to the ongoing management of Multisigs during operational use.

###### A.2.11.1.3.2.2.1 - Multisig Administrator Responsibilities - Ongoing Management [Core]  <!-- UUID: 7ff66181-3c64-46e8-b17c-f0a90793b388 -->

The documents herein define the responsibilities and requirements of Multisig Administrators relating to the ongoing management and maintenance of Multisigs during operational use. Multisig Administrators may consult the operational guides specified in [A.2.11.1.3.2.3 - Operational Guides](37f6864d-5f6a-43fd-adbe-f3b2e82c9e01) for guidance on fulfilling these requirements.

###### A.2.11.1.3.2.2.1.1 - Signer Composition And Rotation [Core]  <!-- UUID: d81db018-bce7-44b9-a354-667f128a4db3 -->

The documents herein define requirements governing changes to Multisig signer composition, including the rotation, replacement, and updating of Multisig signers and signer addresses.

###### A.2.11.1.3.2.2.1.1.1 - Signer Rotation Requirement [Core]  <!-- UUID: cb4d28ac-6d54-4d57-99b2-ed80cea73139 -->

Multisig signers may be rotated as operational or security requirements evolve. All signer rotations must be communicated to the Protocol Security Workstream Lead by the Multisig Administrator, accompanied by clear documentation describing the reason for the change, the outgoing signer, and the incoming signer.

###### A.2.11.1.3.2.2.1.1.2 - Signer Composition Documentation Requirement [Core]  <!-- UUID: 2d434d95-a892-404f-9e59-216dce97ce89 -->

Any change to Multisig signer composition must be promptly communicated to the Protocol Security Workstream Lead by the Multisig Administrator, including all updated signer addresses.

###### A.2.11.1.3.2.2.1.1.3 - Threshold Preservation Requirement [Core]  <!-- UUID: 6dc7cb2e-0c20-4698-b183-28b49f76f88c -->

Signer rotations must not reduce the total number of signers or decrease the signing threshold unless the Multisig Administrator provides a clear operational or security justification that is submitted to and approved by the Protocol Security Workstream Lead.

###### A.2.11.1.3.2.2.1.1.4 - Signer Offboarding Requirements [Core]  <!-- UUID: 6bf116c0-657d-454f-8181-cc2677844513 -->

The Multisig Administrator must ensure that signers are offboarded in accordance with the procedures outlined in the documents herein.

###### A.2.11.1.3.2.2.1.1.4.1 - Signer Removal [Core]  <!-- UUID: 5c4850a6-cfd9-4b5e-b8fb-a0500c043bfd -->

The Multisig Administrator must coordinate with the remaining signers to execute a signer removal transaction in accordance with the Multisig's standard signer rotation procedures. After execution, the Multisig Administrator must verify that the departing signer's address has been removed from the Multisig and that the change is appropriately communicated and documented as outlined in [A.2.11.1.3.2.2.1.1.2 - Signer Composition Documentation Requirement](2d434d95-a892-404f-9e59-216dce97ce89).

###### A.2.11.1.3.2.2.1.1.4.2 - Access Revocation And Handover [Core]  <!-- UUID: 6a420118-a76a-4e8f-bd70-e30fca5cf703 -->

The Multisig Administrator must ensure that the departing signer relinquishes access to all Multisig-related communication channels, shared resources, and sensitive operational systems. Any locally stored sensitive Multisig information must be securely deleted. Departing signers should provide relevant operational context, including any pending actions or responsibilities, to the remaining signers to support a smooth transition.

###### A.2.11.1.3.2.2.1.1.5 - Use-Case Specific Signer Requirements And Considerations [Core]  <!-- UUID: f1c6bc31-d2f4-454d-8200-8a2ddc78c695 -->

Additional signer requirements or considerations may apply depending on the specific operational use case of the Multisig. Such requirements are specified in the subdocuments herein.

###### A.2.11.1.3.2.2.1.1.5.1 - Emergency Response Multisig Signer Composition Requirements And Considerations [Core]  <!-- UUID: fdeaaece-d90e-4f47-a8f9-0ea23cf8d49f -->

The signer requirements and considerations applicable to Multisigs classified with a Time-Sensitive or Emergency Operational Classification level, as defined in [A.2.11.1.3.2.1.1.1.2 - Operational Assessment](35224359-76a6-41fe-adc2-6f70a29f3f4a), are as follows:

- Emergency Response Multisigs must maintain 24/7 availability of a number of signers equal to or greater than the Multisig signing threshold.
- Geographic distribution of signers is encouraged for Emergency Response Multisigs where appropriate to support 24/7 operational coverage.

###### A.2.11.1.3.2.2.1.1.5.2 - Capital Allocation Multisig Signer Composition Requirements And Considerations [Core]  <!-- UUID: 8d4d4683-03fc-4e4d-a255-9e7e0c40e059 -->

The Multisig Administrator must ensure that all signers participating in Capital Allocation Multisigs (Multisigs responsible for allocating or reallocating capital) possess sufficient protocol expertise.

###### A.2.11.1.3.2.2.1.2 - Incident Reporting [Core]  <!-- UUID: 8ff4a715-3ca6-4196-8fae-80ea556c2266 -->

Incident Reporting defines the procedures governing the reporting of security incidents, operational issues, and security-relevant events relating to Multisig operations.

###### A.2.11.1.3.2.2.1.2.1 - Reportable Incidents Classification [Core]  <!-- UUID: f604c9b7-a728-4b53-acbc-cc8677dd23d6 -->

All incidents must be reported and classified to ensure appropriate response timelines and escalation. The documents herein define the classification categories, reporting timelines, and applicable reporting processes for Multisig-related incidents.

###### A.2.11.1.3.2.2.1.2.1.1 - Security Incidents [Core]  <!-- UUID: bae73b4f-aa60-4c42-a56c-3d29af2bef36 -->

Security incidents must be reported immediately upon discovery, in accordance with the process outlined in [A.2.11.1.3.2.2.1.2.2 - Emergency Incident Reporting Process](56e44cdc-1ba5-4254-9308-c4cfe189394a). Security incidents include, but are not limited to:

- Signing key compromise or suspected compromise
- Account takeover of email or communication platforms used for Multisig operations
- Device theft or loss involving signing or operational access
- Suspicious or unauthorized activity on Multisig accounts
- Phishing attempts targeting Multisig operations
- Compromise or suspected infiltration of communication channels used for Multisig coordination

###### A.2.11.1.3.2.2.1.2.1.2 - Operational Issues [Core]  <!-- UUID: 8f2bc680-c6f7-40dc-b003-118b71f1de20 -->

Operational issues must be reported within 24 hours of discovery, in accordance with the process outlined in [A.2.11.1.3.2.2.1.2.3 - Standard Incident Reporting Process](ec4cd423-74ba-4e74-82d9-46ba5f6cf526). Operational issues include, but are not limited to:

- Loss of access to signing keys or signing devices
- Hardware wallet or backup device failure
- Communication channel failures affecting Multisig coordination
- Verification tool malfunctions
- Operational difficulties preventing adherence to security procedures

###### A.2.11.1.3.2.2.1.2.1.3 - Near Misses [Core]  <!-- UUID: 32420ad5-4fd2-4088-8564-452d4adf9589 -->

Near misses should be reported in accordance with the process outlined in [A.2.11.1.3.2.2.1.2.3 - Standard Incident Reporting Process](ec4cd423-74ba-4e74-82d9-46ba5f6cf526) when practical. Near misses include events that did not result in compromise but may indicate risk, including, but not limited to:

- Social engineering attempts
- Suspicious emails or messages
- Security procedure confusion or errors
- Training gaps or unclear documentation

###### A.2.11.1.3.2.2.1.2.2 - Emergency Incident Reporting Process [Core]  <!-- UUID: 56e44cdc-1ba5-4254-9308-c4cfe189394a -->

When an emergency incident occurs, the following steps must be completed:

- The reporting signer must take immediate actions to secure the situation and prevent further risk, including isolating affected devices or systems where appropriate.
- The reporting signer must notify the Multisig Administrator and other participants through the primary communication channel.
- The Multisig Administrator must ensure that the reporting signer immediately reports the incident to the Protocol Security Workstream Lead, following the documentation requirements outlined in [A.2.11.1.3.2.2.1.2.2.1 - Emergency Incident Documentation Requirements](6d6e7b53-8fcb-4ecb-8428-e07f682d13d4).
- The Multisig Administrator must ensure that the reporting signer follows up with the Protocol Security Workstream Lead if no acknowledgement is received within 24 hours.

###### A.2.11.1.3.2.2.1.2.2.1 - Emergency Incident Documentation Requirements [Core]  <!-- UUID: 6d6e7b53-8fcb-4ecb-8428-e07f682d13d4 -->

All emergency incident reports must include sufficient documentation to allow review, follow-up, and operational learning. At minimum, security incident documentation must include:

- Multisig details and classification
- Incident type
- Time of incident occurrence and discovery
- Reporting signer
- Description of the incident
- Immediate actions taken
- Next steps required
- Current Multisig status
- Impact

###### A.2.11.1.3.2.2.1.2.3 - Standard Incident Reporting Process [Core]  <!-- UUID: ec4cd423-74ba-4e74-82d9-46ba5f6cf526 -->

When a standard incident occurs, the following steps must be completed:

- The Multisig Administrator must ensure that the reporting signer immediately reports the incident to the Protocol Security Workstream Lead, following the documentation requirements outlined in [A.2.11.1.3.2.2.1.2.3.1 - Standard Incident Documentation Requirements](0aec011a-18d2-4945-90b5-8089fa01cefb).
- Follow-up with the Protocol Security Workstream Lead if no acknowledgement is received within 48 hours.

###### A.2.11.1.3.2.2.1.2.3.1 - Standard Incident Documentation Requirements [Core]  <!-- UUID: 0aec011a-18d2-4945-90b5-8089fa01cefb -->

All standard incident reports must include, at minimum, the following information:

- Multisig details and classification
- Incident type
- Time of incident occurrence and discovery
- Reporting signer
- Description of the incident
- Immediate actions taken
- Current Multisig status
- Impact

###### A.2.11.1.3.2.2.1.3 - Training And Operational Readiness [Core]  <!-- UUID: a0a34154-2789-4ffd-844b-36f27e9900db -->

Multisig Administrators must ensure that signers maintain sufficient operational expertise through ongoing training and familiarity with the Multisig's procedures. This includes, but is not limited to, training and periodic review of transaction verification practices, operational procedures, and incident response processes applicable to the Multisig's function.

###### A.2.11.1.3.2.2.1.3.1 - Backup Infrastructure Readiness Requirements [Core]  <!-- UUID: f9e5507b-1433-47fc-ae41-28c23831c0fc -->

The Multisig Administrator must ensure that signers are prepared to operate using backup infrastructure. This includes providing signers with access to offline or alternative Multisig interfaces, verifying that signers have practiced using backup interfaces, testing backup RPC providers during non-emergency periods, and maintaining documented procedures describing how to switch to backup infrastructure when required.

###### A.2.11.1.3.2.2.1.3.2 - Emergency Operations Training And Readiness Requirement [Core]  <!-- UUID: 3d5068af-cb19-4a10-b712-de8e8be7a4f6 -->

Multisig Administrators are responsible for ensuring that Multisigs classified with a Time-Sensitive or Emergency Operational Classification level, as defined in [A.2.11.1.3.2.1.1.1.2 - Operational Assessment](35224359-76a6-41fe-adc2-6f70a29f3f4a), maintain operational readiness appropriate to their function.

To satisfy this requirement, Multisig Administrators must ensure that the following activities are conducted:

- Periodic operational drills
- Quarterly testing of emergency communication and alerting systems to ensure continued reliability
- Semi-annual paging system tests to verify alert functionality
- An annual full emergency simulation involving all signers

The Multisig Administrator must document the completion and outcome of all required readiness activities and provide testing reports and confirmation of completion to Core GovOps.

###### A.2.11.1.3.2.2.2 - Signer Responsibilities - Ongoing Management [Core]  <!-- UUID: 51431dc2-d731-4570-8e54-de390e565bb1 -->

The documents herein define the responsibilities and requirements of Multisig signers relating to the ongoing management of Multisigs during operational use. Signers may consult with their Multisig Administrator for guidance on fulfilling these requirements.

###### A.2.11.1.3.2.2.2.1 - Signer Address Update Process [Core]  <!-- UUID: 79b5daf4-5c02-4aa8-89a7-879a6d594758 -->

Any update to a Multisig signer address must be performed in accordance with the process defined in the subdocuments herein.

###### A.2.11.1.3.2.2.2.1.1 - Signer Address Update Process If Original Key Is Accessible [Core]  <!-- UUID: c6bcbd5f-7450-4c6e-9aa6-82c49a678bd3 -->

If the original key of the signer address that needs to be changed remains accessible, the following steps must be completed by the signer:

- The signer authorizes the address change by signing a message with the existing signer address. The signed message must clearly state the intent to replace the existing signer address with the new address.
- The signer must follow the steps defined in [A.2.11.1.3.2.1.2.1 - Signer Verification Process](002821ab-c67c-4eb1-987c-69e759ab7b3c) prior to the new address being added to the Multisig.

###### A.2.11.1.3.2.2.2.1.2 - Signer Address Update Process If Original Key Is Lost Or Inaccessible [Core]  <!-- UUID: a2f65561-ba6d-4ef0-b1c0-31da659306f3 -->

If the original key of the signer address that needs to be changed is inaccessible, the signer must verify their identity to the remaining signers through alternative verification methods such as:

- Authentication through a verified social media or publicly associated account
- Live verification via video call with existing signers
- Other comparable verification methods

Upon successful identity verification, the signer must follow the steps defined in [A.2.11.1.3.2.1.2.1 - Signer Verification Process](002821ab-c67c-4eb1-987c-69e759ab7b3c) and notify the Multisig Administrator once completed.

###### A.2.11.1.3.2.2.2.2 - Transaction Verification And Signing Requirements [Core]  <!-- UUID: aa6f2aeb-5c90-4b23-bfc4-e6de0a588915 -->

Multisig signers must verify all transaction data prior to signing in order to reduce the risk of malicious or unintended transactions being executed. The procedures defined in the documents herein establish the relevant transaction verification processes for supported execution environments.

###### A.2.11.1.3.2.2.2.2.1 - Explorer Redundancy Recommendations [Core]  <!-- UUID: 98eeb3a8-8199-417f-a0a7-ab4625aa39aa -->

Signers are encouraged to maintain access to multiple blockchain explorers for each supported network to support transaction monitoring, verification, and investigation if a primary explorer becomes unavailable.

###### A.2.11.1.3.2.2.2.2.2 - EVM Transaction Verification Requirements [Core]  <!-- UUID: 1d4492e8-f2eb-4ff5-9bf8-471a9aef26c5 -->

Multisig signers must verify EVM-based Multisig transactions prior to signing to ensure that the transaction being signed matches the intended operation.

###### A.2.11.1.3.2.2.2.2.2.1 - Transaction Hash Verification [Core]  <!-- UUID: eb5de4dd-2921-439e-bbce-a26f66410c48 -->

Signers must verify that the transaction hash displayed on the signing device matches the expected transaction hash derived from the transaction parameters. When signing transactions involving nested Multisigs, the hash displayed on the signing device may correspond to an approval hash rather than the underlying transaction. In such cases, signers must verify both the nested transaction and the parent Multisig approval.

###### A.2.11.1.3.2.2.2.2.2.2 - Transaction Simulation Review [Core]  <!-- UUID: 35229761-1568-4b00-84c2-878aa64562e1 -->

Where available, signers must review a transaction simulation to confirm that the expected events, asset transfers, and state changes match the intended transaction.

###### A.2.11.1.3.2.2.2.2.2.3 - Transaction Calldata Review [Core]  <!-- UUID: 023b1251-96d0-4784-a11b-1d470444eba2 -->

Signers must review decoded transaction calldata prior to signing to confirm that the function calls, recipient addresses, and transferred amounts match the intended action.

###### A.2.11.1.3.2.2.2.2.2.4 - Verification Tool Diversity [Core]  <!-- UUID: e329c539-16e2-4316-bb2c-6879bb45d391 -->

Signers are encouraged to verify transaction hashes and decoded calldata using independent verification tools where available and should avoid relying on a single verification interface.

###### A.2.11.1.3.2.2.2.2.3 - SVM Transaction Verification Requirements [Core]  <!-- UUID: d6ab5e65-bc6b-4959-9c11-e5612cc07ee0 -->

Multisig signers must verify Solana Virtual Machine (SVM) Multisig transactions prior to signing to ensure that the proposal contains the intended instructions and parameters.

###### A.2.11.1.3.2.2.2.2.3.1 - Proposal Verification [Core]  <!-- UUID: dd520781-597e-4a0f-9120-47d18c0fc7c0 -->

Signers must verify that the transaction proposal reflects the intended operation, including the sender, recipient addresses, asset type, transfer amounts, configuration changes, and associated instructions. Signers must confirm that all instructions correspond to the intended action and that no unauthorized interactions are included.

###### A.2.11.1.3.2.2.2.2.3.2 - Simulation Review [Core]  <!-- UUID: 37d9a254-08e2-43f3-b2a6-4226b6a8429a -->

Where available, signers must review a transaction simulation to confirm that expected token transfers, SOL transfers, or configuration changes match the intended transaction.

###### A.2.11.1.3.2.2.2.2.3.3 - Explorer Verification [Core]  <!-- UUID: 979afea2-e159-46e3-be25-8ce22dac7dd0 -->

Signers are encouraged to inspect the transaction or proposal account using a public blockchain explorer to review the decoded transaction instructions and parameters.

###### A.2.11.1.3.2.2.2.2.3.4 - Tooling Limitations [Core]  <!-- UUID: 388f1cc7-f10c-4410-bc49-e0e3e358a90e -->

Verification tooling for SVM Multisig transactions is currently more limited than for EVM environments. Signers should exercise additional caution and may cross-verify transactions with other signers prior to execution.

###### A.2.11.1.3.2.3 - Operational Guides [Core]  <!-- UUID: 37f6864d-5f6a-43fd-adbe-f3b2e82c9e01 -->

The Protocol Security Workstream Lead must maintain and make available operational guides to support Multisig Administrators in complying with the requirements specified in [A.2.11.1.3.2 - Multisig Security Guidelines](6033699f-1d55-45ba-8eb1-bd8982571cc0). These guides must cover, at minimum, Multisig registration, signer rotation and replacement, signer onboarding and offboarding, incident reporting, and any other processes where standardized documentation is required. The Protocol Security Workstream Lead is responsible for keeping these guides current and accessible to all Multisig Administrators.

##### A.2.11.1.3.3 - Multisig Monitoring And Review [Core]  <!-- UUID: e5a3658b-0218-42a7-b053-ddd276a0a512 -->

The documents herein define the periodic monitoring and review responsibilities performed by Core GovOps to ensure that Multisigs remain compliant with the Multisig Security Enforcement Framework and that Multisig documentation and classification remain accurate. These provisions apply only after the effective date specified in [A.2.11.1.3.2 - Multisig Security Guidelines](6033699f-1d55-45ba-8eb1-bd8982571cc0).

###### A.2.11.1.3.3.1 - Periodic Review Requirement [Core]  <!-- UUID: 94d70a1d-885b-4f46-ade4-0702f65cfc89 -->

Core GovOps must engage the Protocol Security Workstream Lead and third party providers to conduct periodic reviews of registered Multisigs to verify that Multisig documentation, configuration, and operational classification remain accurate and aligned with current usage. At minimum:

- Multisig documentation and classification must be reviewed on a quarterly basis.
- Reviews must be conducted following major operational, financial, or structural changes affecting the Multisig.
- Reviews must be conducted when significant protocol changes materially affect the Multisig's role, authority, or risk exposure.

###### A.2.11.1.3.3.1.1 - Review Scope [Core]  <!-- UUID: 4090334c-d240-49d4-89c1-7901ffbfa299 -->

Periodic reviews may include, but are not limited to:

- Verification that Multisig documentation in the Multisig Registry remains accurate and up to date.
- Reassessment of Multisig operational purpose where operational patterns change.
- Reassessment of financial exposure or protocol impact where asset exposure or operational scope changes.
- Verification that Multisig configuration and operational practices remain consistent with the Multisig Security Enforcement Framework.

###### A.2.11.1.3.3.2 - Monitoring Outcome [Core]  <!-- UUID: 69646ecd-268a-4487-9077-c6efa11f1026 -->

Where monitoring or review activities identify inconsistencies, outdated documentation, or potential noncompliance, Core GovOps must proceed in accordance with [A.2.11.1.3.5 - Determination And Enforcement Of Multisig Security Noncompliance](2a36aafa-cfe3-4ba5-b549-f341fbb4c666).

##### A.2.11.1.3.4 - Multisig Registry [Core]  <!-- UUID: 4d80cae1-b28a-4907-8d59-2ebcbba6003d -->

All Multisigs must be recorded in the Multisig Registry at [A.2.11.1.3.4.2.0.6.1 - Registered Multisigs](7d966e5e-ecb3-4a5b-9111-a70927cfa79a).

###### A.2.11.1.3.4.1 - Multisig Registry Entry Requirements [Core]  <!-- UUID: e525c938-7fd2-4e6e-9c01-86cf0783d728 -->

Each Multisig entry in the Multisig Registry must contain the following information:

- Multisig Name
- Administrator Entity
- Multisig Address

###### A.2.11.1.3.4.2 - List Of Registered Multisigs [Active Data Controller]  <!-- UUID: e063a7c5-eb41-489e-8334-b095b785af62 -->

The list of registered Multisigs is defined as Active Data in [A.2.11.1.3.4.2.0.6.1 - Registered Multisigs](7d966e5e-ecb3-4a5b-9111-a70927cfa79a).

The Active Data is updated as follows:

- The Responsible Party is Core GovOps.
- The Update Process must follow the protocol for 'Direct Edit'.

###### A.2.11.1.3.4.2.0.6.1 - Registered Multisigs [Active Data]  <!-- UUID: 7d966e5e-ecb3-4a5b-9111-a70927cfa79a -->

The Multisigs that are registered are:

| **Multisig Name** | **Administrator Entity** | **Multisig Address** |
|---|---|---|
| | | |

##### A.2.11.1.3.5 - Determination And Enforcement Of Multisig Security Noncompliance [Core]  <!-- UUID: 2a36aafa-cfe3-4ba5-b549-f341fbb4c666 -->

When a Multisig is determined to be noncompliant with the Multisig Security Enforcement Framework, a grace period of forty-eight (48) hours is provided to resolve the issue. If the noncompliance is not resolved within this period, Multisig operations must be immediately stopped, unless an exception is granted by the Protocol Security Workstream Lead. Core GovOps may then determine whether further actions are required to enforce the halt of operations in relation to such Multisig. These provisions apply only after the effective date specified in [A.2.11.1.3.2 - Multisig Security Guidelines](6033699f-1d55-45ba-8eb1-bd8982571cc0).


## A.2.12 - Purpose System [Article]  <!-- UUID: b888a6f2-df29-4254-bc74-8dff265f2697 -->

This Article governs the Purpose System, which aims to fund open-source AI and software projects that benefit the Sky Ecosystem and public good.

### A.2.12.1 - Funding [Section]  <!-- UUID: d6d4b091-8143-4a43-a3cf-b5dfa18a8d35 -->

This Section must define the elements and infrastructure necessary to implement the Purpose System effectively. This includes establishing a process for allocating purpose funds to individual Agents.

### A.2.12.2 - Direct And Specific Impact Solutions [Section]  <!-- UUID: a2de9679-22b6-432b-861f-f315d422e51e -->

At all times, at least 10% of the Purpose System funds must be used for more direct and specific impact solutions.

## A.2.13 - Ecosystem Entity Grants [Article]  <!-- UUID: 7be35f96-8230-41d6-aab4-0a76bd705a25 -->

This Article defines the Ecosystem Entity Grants, which aim to fund the Sky Frontier Foundation and the Fortification Foundation.

### A.2.13.1 - Ecosystem Entity Grants [Section]  <!-- UUID: 5d5759e4-8077-4af5-9a1a-eaeab5088dd7 -->

Information regarding ecosystem entities grants to the Sky Frontier Foundation and the Fortification Foundation is detailed in the documents herein.

#### A.2.13.1.1 - Sky Frontier Foundation Grants [Core]  <!-- UUID: 1f5d9b2d-d94d-4945-bcf5-74b9152de90c -->

Information regarding ecosystem entity grants to the Sky Frontier Foundation is detailed in the documents herein.

##### A.2.13.1.1.1 - August 2025 Grant [Core]  <!-- UUID: ecc26bbd-ee6c-4ede-a3da-176cb8857d87 -->

The approved and disbursed August 2025 grant to the Sky Frontier Foundation is as follows:

- Recipient: Sky Frontier Foundation
- Recipient Address: `0xca5183FB9997046fbd9bA8113139bf5a5Af122A0`
- Transaction Hash: `0x9dff3cf283969f0d6b54347829463aabbcad43e79ebb7ad20c5154e951586e3f`
- USDS amount: 50,000,000
- SKY amount: 1,977,443,914.00
- USDS/SKY LP (UNI-V2) amount: 28,829,858.44
- DAI amount: 35.41
- ENS amount: 46,362.27
- stkAAVE amount: 1,467.08
- COMP amount: 643.73
- AAVE amount: 60
- WETH amount: 0.0296

The amounts above are rounded down; refer to onchain data for exact figures.

#### A.2.13.1.2 - Fortification Foundation Grants [Core]  <!-- UUID: ec2ebbba-6944-44cb-a04d-4572c6bea1e7 -->

Information regarding ecosystem entity grants to the Fortification Foundation is detailed in the documents herein.

##### A.2.13.1.2.1 - August 2025 Grant [Core]  <!-- UUID: fc6b41c6-f9e3-4690-a75a-6d3d68e8d942 -->

The approved and disbursed August 2025 grant to the Fortification Foundation is as follows:

- Recipient: Fortification Foundation
- Recipient Address: `0x483413ccCD796Deddee88E4d3e202425d5E891C6`
- Transaction Hash: `0x9dff3cf283969f0d6b54347829463aabbcad43e79ebb7ad20c5154e951586e3f`
- USDS amount: 10,000,000
- SKY amount: 200,000,000
