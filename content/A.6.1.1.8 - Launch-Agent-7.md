# A.6.1.1.8 - Launch Agent 7 [Core]  <!-- UUID: d0d77316-0b08-447c-b75a-ae7926b07019 -->

The documents herein specify all of the logic for Launch Agent 7, including Launch Agent 7's strategy and how it uses the Sky Primitives to operationalize this strategy.

## A.6.1.1.8.1 - Introduction [Core]  <!-- UUID: ff01e448-1d0a-49e9-8490-5b1a497f1f27 -->

Launch Agent 7 is an Agent focused on building structured credit infrastructure across traditional and digital financial markets. In addition to originating and managing institutional-grade credit facilities, Launch Agent 7 serves as a bridge between sophisticated capital and high-quality borrowers—including large enterprises and leading fintech platforms—through a suite of scalable credit solutions designed to support durable liquidity and long-term growth.

## A.6.1.1.8.2 - Sky Primitives [Core]  <!-- UUID: d3c6d7a2-f399-40bd-ac22-4a565cfa253a -->

The documents herein implement the Sky Primitives for Launch Agent 7. See [A.2.2 - Sky Primitives](fcde2604-a138-4c1b-9d9a-14895835c907).

### A.6.1.1.8.2.1 - Genesis Primitives [Core]  <!-- UUID: 23287614-9f6f-4d35-8a89-23e7de347c0e -->

The documents herein implement the Genesis Primitives for Launch Agent 7. See [A.2.2.5 - Genesis Primitives](3d5e3668-8333-4908-adcc-5784cfe7f6b5).

#### A.6.1.1.8.2.1.1 - Agent Creation Primitive [Core]  <!-- UUID: 208e19e0-65df-4c08-a788-bb7908d1aa17 -->

The documents herein contain all data and specifications for Launch Agent 7's Instance of the Agent Creation Primitive. See [A.2.2.5.1 - Agent Creation Primitive](82b95f6d-4883-4f08-ac3a-9d8189013fbe).

##### A.6.1.1.8.2.1.1.1 - Primitive Hub Document [Core]  <!-- UUID: 306be3c1-f4dd-4899-b66c-7992bd2f00dd -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Agent Creation Primitive.

###### A.6.1.1.8.2.1.1.1.1 - Global Activation Status [Core]  <!-- UUID: 95c76b6a-6044-4178-a673-50c7e0db5c7e -->

`Completed`

###### A.6.1.1.8.2.1.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 8ff31ad2-37fb-4d0c-8865-57d14ab1821c -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.1.1.1.3 - Completed Instances [Core]  <!-- UUID: 9378730b-3ec4-4b75-918d-1dc4163f4c45 -->

This document contains a Directory of all Instances of the Agent Creation Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.1.1.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 1e930120-a453-475f-ab1a-c35d839ed4fc -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.8.2.1.1.3.1 - Single Instance Configuration Document](d557f7bc-8db5-4b63-acbf-5a5b54931932).

###### A.6.1.1.8.2.1.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 06f93b92-d9d2-4689-9607-99f6f03e23ca -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.8.2.1.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 99a7317c-54eb-4480-a4e6-850afb59019f -->

The document herein contains the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.1.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e1714823-ea3d-49af-af1b-81a4d06dc7ec -->

The subtrees for archived Invocations and Instances of the Agent Creation Primitive are stored here.

###### A.6.1.1.8.2.1.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 7f226306-4280-4eb5-93ef-3d23ea275366 -->

The subtrees for failed Invocations of the Agent Creation Primitive are stored here.

###### A.6.1.1.8.2.1.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: da9d9da4-e7a3-46d9-9b46-01634fb1ba02 -->

The subtrees for Instances of the Agent Creation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.1.1.2 - Active Instances [Core]  <!-- UUID: c99398df-c653-4623-a3bf-0ac407116b91 -->

The Instances of the Agent Creation Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: f661d4a1-a5ff-4cbd-8d57-82418669a279 -->

The Instances of the Agent Creation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.8.2.1.1.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: d557f7bc-8db5-4b63-acbf-5a5b54931932 -->

The documents herein contain the Instance Configuration Document for the Single Agent Creation Primitive Instance.

###### A.6.1.1.8.2.1.1.3.1.1 - Parameters [Core]  <!-- UUID: 5086285a-0bac-433d-bb2c-f9a3bee1ec7e -->

The documents herein define the parameters of the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.8.2.1.1.3.1.1.1 - Name [Core]  <!-- UUID: 65776660-e4a8-4385-aede-31b73b855cb1 -->

The name of the Agent is Launch Agent 7.

###### A.6.1.1.8.2.1.1.3.1.1.2 - SubProxy Account [Core]  <!-- UUID: a5a06fb8-2ae7-4af3-8e96-e1fb57eef916 -->

The address of Launch Agent 7's SubProxy Account on the Ethereum Mainnet is `0x56a9bA5FE133EF4Ab1131E8ac7c4312a52284f5B`.

###### A.6.1.1.8.2.1.1.3.1.1.3 - StarGuard Contract [Core]  <!-- UUID: fa741bad-9966-4ff7-8300-238d1c58df9a -->

The address of Launch Agent 7's StarGuard contract on the Ethereum Mainnet is `0xB36e88c02E4619Ef34C0Db76C5BCb6655747FB28`.

###### A.6.1.1.8.2.1.1.3.1.1.3.1 - StarGuard Max Delay [Core]  <!-- UUID: 68ce7040-9954-4339-8fa8-d5679eb2a1d5 -->

The Launch Agent 7 StarGuard `maxDelay` is seven (7) days.

###### A.6.1.1.8.2.1.1.3.1.1.4 - Genesis Account [Core]  <!-- UUID: 9646935e-2406-4187-b43d-9158bdf71856 -->

The address of Launch Agent 7's Genesis Account will be specified in a future iteration of the Launch Agent 7 Artifact.

###### A.6.1.1.8.2.1.1.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 9fa056b9-0961-4858-b610-3ddd8f728058 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.8.2.1.1.3.1.3 - Data Repository [Core]  <!-- UUID: 0e086a31-8f5c-452e-b9b6-6840f5e9c90d -->

The documents herein contain data relevant to the Single Instance of the Agent Creation Primitive.

###### A.6.1.1.8.2.1.1.3.1.3.1 - Initial Planning [Core]  <!-- UUID: e0b544df-ad91-46a7-8c4e-da665c1ba9f5 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.1.1.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: bc83f510-98d9-4088-b775-3fca976df4ed -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.1.1.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 904a4c5e-7d06-45ee-b0e5-b327f131276d -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.8.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 6cf9e5bd-a6a9-4f8c-b823-17c99c6d3805 -->

Because the Agent Creation Primitive is deployed solely for the one-time creation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.8.2.1.2 - Prime Transformation Primitive [Core]  <!-- UUID: 3ba02850-d20f-4c96-b4b5-956c46c68be9 -->

The documents herein contain all data and specifications for Launch Agent 7's instance of the Prime Transformation Primitive. See [A.2.2.5.2 - Prime Transformation Primitive](81411106-fd6d-4f9c-b3ae-7af7b5e62482).

##### A.6.1.1.8.2.1.2.1 - Primitive Hub Document [Core]  <!-- UUID: ec52fb9d-30d6-4ccb-830d-eb8878e58e64 -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Prime Transformation Primitive.

###### A.6.1.1.8.2.1.2.1.1 - Global Activation Status [Core]  <!-- UUID: adda8707-63b5-414a-b30c-bb07bb09ec47 -->

`Completed`

###### A.6.1.1.8.2.1.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 8251dc77-6944-4ccb-b653-f93b70b43ec5 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.1.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 6ec0cf3b-a2b7-4fa8-88d8-c64af3fdea83 -->

This document contains a Directory of all Instances of the Prime Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.1.2.1.3.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 1ecf0cd6-aac0-4706-a34b-fb5adb3daa32 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.8.2.1.2.3.1 - Single Instance Configuration Document](7b97df7e-67b7-4d4d-b4b5-9e1612793b7c).

###### A.6.1.1.8.2.1.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 04f57d55-373b-40bf-a453-cc1803f26d19 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.8.2.1.2.1.5 - Hub Data Repository [Core]  <!-- UUID: a50b9d4f-49b5-4c28-a8ba-03f3cd498ce5 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.1.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 6f75f229-9835-442b-b718-ca9d426c1e6a -->

The subtrees for archived Invocations and Instances of the Prime Transformation Primitive are stored here.

###### A.6.1.1.8.2.1.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 7c44f5b5-109b-4c78-afd5-bc331207b8fe -->

The subtrees for failed Invocations of the Prime Transformation Primitive are stored here.

###### A.6.1.1.8.2.1.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: a718f498-b0dd-41ed-8837-58f279b94e78 -->

The subtrees for Instances of the Prime Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.1.2.2 - Active Instances [Core]  <!-- UUID: 4b3f09cc-abc1-4b44-8ce9-079b9ca1a3ff -->

The Instances of the Prime Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.1.2.3 - Completed Instances [Core]  <!-- UUID: 4479d30b-8fa6-4dad-8dc9-9a93abadf267 -->

The Instances of the Prime Transformation Primitive with `Completed` Status are contained herein.

###### A.6.1.1.8.2.1.2.3.1 - Single Instance Configuration Document [Core]  <!-- UUID: 7b97df7e-67b7-4d4d-b4b5-9e1612793b7c -->

The documents herein contain the Instance Configuration Document for the Single Prime Transformation Primitive Instance.

###### A.6.1.1.8.2.1.2.3.1.1 - Parameters [Core]  <!-- UUID: bf3d16ff-82f7-4804-a0bf-153eccda8a66 -->

The documents herein define the parameters of the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.8.2.1.2.3.1.1.1 - Agent Type [Core]  <!-- UUID: f74decac-e2cb-4403-b3d7-4cef0a90fda5 -->

Launch Agent 7 is a Prime Agent.

###### A.6.1.1.8.2.1.2.3.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: e6e419d7-ce14-4123-b22a-62f94075ff52 -->

The documents herein define the custom parameters of the Single Instance of the Prime Transformation Primitive, if any.

###### A.6.1.1.8.2.1.2.3.1.2 - Operational Process Definition [Core]  <!-- UUID: 3a52a82f-7d54-4124-90ed-6007b217a174 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further operational process is needed post-deployment.

###### A.6.1.1.8.2.1.2.3.1.3 - Data Repository [Core]  <!-- UUID: 7967c2b8-181c-4582-a265-7e60654503e1 -->

The documents herein contain data relevant to the Single Instance of the Prime Transformation Primitive.

###### A.6.1.1.8.2.1.2.3.1.3.1 - Initial Planning [Core]  <!-- UUID: cd906df7-aeb9-4859-a364-3fb03d4f2f78 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.1.2.3.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: dcbe59e5-5d72-49f3-92cc-fce16bd6d5f9 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.1.2.3.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 11420736-9467-412e-81ee-389e254b4ac3 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.8.2.1.2.4 - In Progress Invocations [Core]  <!-- UUID: ea18a0a9-b7dd-47d8-97da-3f55b3eeb645 -->

Because the Prime Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.8.2.1.3 - Executor Transformation Primitive [Core]  <!-- UUID: 073db45c-4a8f-4d59-be5e-f9dcba60ed98 -->

The documents herein contain all data and specifications for Launch Agent 7's instance of the Executor Transformation Primitive. See [A.2.2.5.3 - Executor Transformation Primitive](2f249be5-8edb-41e4-b429-734e1ba2cbc7).

##### A.6.1.1.8.2.1.3.1 - Primitive Hub Document [Core]  <!-- UUID: acd47616-d33c-4a8e-81cf-9f75cf83187d -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Executor Transformation Primitive.

###### A.6.1.1.8.2.1.3.1.1 - Global Activation Status [Core]  <!-- UUID: 33e40429-53c4-488f-be4e-192d0769c517 -->

`Inactive`

###### A.6.1.1.8.2.1.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 412f680a-f756-4180-b2de-b93caf7eecb2 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.1.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 1cbf2b10-57e5-45fa-a1fd-ed63ac2b83f5 -->

This document contains a Directory of all Instances of the Executor Transformation Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.1.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 6d2ec280-7635-4cd2-928d-1bad6b86b785 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.8.2.1.3.1.5 - Hub Data Repository [Core]  <!-- UUID: ada314c1-b67d-47d7-9d3d-b45ceba4eb3f -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.1.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: ce8182d8-bcde-411d-b0ae-03967a75b31c -->

The subtrees for archived Invocations and Instances of the Executor Transformation Primitive are stored here.

###### A.6.1.1.8.2.1.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 77c26627-04f7-4838-ab37-8a192c0d7040 -->

The subtrees for failed Invocations of the Executor Transformation Primitive are stored here.

###### A.6.1.1.8.2.1.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 5461ddf6-6698-43bf-b5b0-d8e04d07382c -->

The subtrees for Instances of the Executor Transformation Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.1.3.2 - Active Instances [Core]  <!-- UUID: 10ac7a6e-6436-4969-9c90-9132f9d4bb24 -->

The Instances of the Executor Transformation Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.1.3.3 - Completed Instances [Core]  <!-- UUID: adc67dcc-b853-472f-8805-3ede35b2b17e -->

The Instances of the Executor Transformation Primitive with `Completed` Status are contained herein.

##### A.6.1.1.8.2.1.3.4 - In Progress Invocations [Core]  <!-- UUID: fc0b759f-7211-41fb-99cb-729a289677f4 -->

Because the Executor Transformation Primitive is deployed solely for the one-time transformation of the Agent, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.8.2.1.4 - Agent Token Primitive [Core]  <!-- UUID: 10cf4cab-179b-4e1b-a9c9-22b09af8b6fc -->

The documents herein contain all data and specifications for Launch Agent 7's Instance of the Agent Token Primitive. See [A.2.2.5.4 - Agent Token Primitive](2047c361-db28-4952-a70c-83d07b562064).

##### A.6.1.1.8.2.1.4.1 - Primitive Hub Document [Core]  <!-- UUID: 9739918e-5d1a-4113-8127-a6470a54ace1 -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Agent Token Primitive.

###### A.6.1.1.8.2.1.4.1.1 - Global Activation Status [Core]  <!-- UUID: 1e052e06-8467-4542-8cc5-ebe39b451141 -->

`Active`

###### A.6.1.1.8.2.1.4.1.2 - Active Instances Directory [Core]  <!-- UUID: cc39cc3b-1f15-4dd8-9429-06703b0619e5 -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.1.4.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 3040332e-af07-4555-bc2e-6d7e91237108 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.8.2.1.4.2.1 - Single Instance Configuration Document](2af5a57c-23fa-4299-a4f4-fe6f33ef2b6d).

###### A.6.1.1.8.2.1.4.1.3 - Completed Instances Directory [Core]  <!-- UUID: e6befbe6-c577-43db-a262-c148ebd7236f -->

This document contains a Directory of all Instances of the Agent Token Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.1.4.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: b158dd8d-b867-49dc-b7c9-aaa743eaa0f7 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.8.2.1.4.1.5 - Hub Data Repository [Core]  <!-- UUID: 4d03af47-7a50-468c-bdee-2b95eb721784 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.1.4.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 26b1ead4-dd0b-4dcb-b6cb-0e72bae7cfe6 -->

The subtrees for archived Invocations and Instances of the Agent Token Primitive are stored here.

###### A.6.1.1.8.2.1.4.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 9ca435e5-75ca-4444-83d6-89e3fdc56a6b -->

The subtrees for failed Invocations of the Agent Token Primitive are stored here.

###### A.6.1.1.8.2.1.4.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: ee1536f2-7de8-4c65-8e36-1c3b10354020 -->

The subtrees for Instances of the Agent Token Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.1.4.2 - Active Instances [Core]  <!-- UUID: 41298826-6bc3-4f30-a304-2268579084ed -->

The Instances of the Agent Token Primitive with `Active` Status are stored herein.

###### A.6.1.1.8.2.1.4.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 2af5a57c-23fa-4299-a4f4-fe6f33ef2b6d -->

The documents herein contain the Instance Configuration Document for the Single Agent Token Primitive Instance.

###### A.6.1.1.8.2.1.4.2.1.1 - Parameters [Core]  <!-- UUID: 837ff40f-de82-436a-9332-0def187295fb -->

The documents herein define the parameters of the Single Instance of the Agent Token Primitive.

###### A.6.1.1.8.2.1.4.2.1.1.1 - Token Name [Core]  <!-- UUID: 2de22e5a-1850-4973-b045-794752a6817a -->

The name of Launch Agent 7's token is Launch Agent 7.

###### A.6.1.1.8.2.1.4.2.1.1.2 - Token Symbol [Core]  <!-- UUID: 072c99dd-2564-4d56-a469-0cd1861d2f74 -->

The symbol of Launch Agent 7's token is AGENT7.

###### A.6.1.1.8.2.1.4.2.1.1.3 - Genesis Supply [Core]  <!-- UUID: da510ee7-7b5d-4964-8778-b6f76ededdbb -->

The Genesis Supply of AGENT7 is 1 billion.

###### A.6.1.1.8.2.1.4.2.1.1.4 - Token Address [Core]  <!-- UUID: 9d142adb-8741-43b0-b36b-a222c17ed6e5 -->

The address of AGENT7 will be specified in a future iteration of the Launch Agent 7 Artifact.

###### A.6.1.1.8.2.1.4.2.1.1.5 - Token Admin [Core]  <!-- UUID: 76bec570-320e-4590-91ba-0ebd7307742f -->

The token Admin will be specified in a future iteration of the Launch Agent 7 Artifact.

###### A.6.1.1.8.2.1.4.2.1.1.6 - Token Emissions [Core]  <!-- UUID: 7262e995-db8b-4db7-860c-60b2250ba04a -->

Token emissions beyond the Genesis Supply are permanently disabled; this cannot be reverted by Launch Agent 7 Governance. Sky Governance retains the ability to revert where Launch Agent 7 is in violation of Risk Capital requirements and emissions are required by the Risk Framework. See [A.3.2 - Risk Capital](55999acf-75fe-4adf-8584-9746ef50d3e4).

###### A.6.1.1.8.2.1.4.2.1.1.7 - Custom Instance Parameters [Core]  <!-- UUID: b290ffad-9860-40cd-a05f-d8fc2a53c03c -->

The documents herein define the custom parameters of the Single Instance of the Agent Token Primitive, if any.

###### A.6.1.1.8.2.1.4.2.1.2 - Operational Process Definition [Core]  <!-- UUID: e4c6a219-2904-4d2a-bdfd-f8ab7cc379aa -->

The documents herein define the operational processes for minting and initial distribution of the tokens from the Genesis Supply.

- These processes will be defined in a future iteration of the Launch Agent 7 Artifact.

###### A.6.1.1.8.2.1.4.2.1.3 - Data Repository [Core]  <!-- UUID: a0b0274a-6b4f-42cf-81aa-97cc675f997c -->

The documents herein contain data relevant to the Single Instance of the Agent Token Primitive.

###### A.6.1.1.8.2.1.4.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 3fa4e43c-9de9-4778-92b2-2adfb9dfdc92 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.1.4.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 8ee40481-70c1-450b-b6e0-aa054cc8daca -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.1.4.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 293be631-ea6f-4a3c-a6db-f1cc99b322e9 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.8.2.1.4.3 - Completed Instances [Core]  <!-- UUID: 21ccd43b-b2e2-4404-bdf2-b041c42a8764 -->

The Instances of the Agent Token Primitive with `Completed` Status are contained herein.

##### A.6.1.1.8.2.1.4.4 - In Progress Invocations [Core]  <!-- UUID: 739fcfb1-6792-4739-8a3e-bf7d650754e7 -->

Because the Agent Token Primitive is Invoked solely for the one-time deployment of the Agent’s token, no further Instances of the Primitive can be Invoked.

### A.6.1.1.8.2.2 - Operational Primitives [Core]  <!-- UUID: 54a65766-cc3b-41f5-8be3-a671d1dac3a4 -->

The documents herein implement the Operational Primitives for Launch Agent 7. See [A.2.2.6 - Operational Primitives](0192ec95-9207-480e-8c51-88d2a1da95ad).

#### A.6.1.1.8.2.2.1 - Executor Accord Primitive [Core]  <!-- UUID: eeafc392-5418-43ac-8281-69ac39775941 -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Executor Accord Primitive. See [A.2.2.6.1 - Executor Accord Primitive](88017877-3ec1-4c43-a035-6bebdf11d9bb).

##### A.6.1.1.8.2.2.1.1 - Primitive Hub Document [Core]  <!-- UUID: afe5ecf8-9fde-4d20-b867-192ad174c6b0 -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Executor Accord Primitive.

###### A.6.1.1.8.2.2.1.1.1 - Global Activation Status [Core]  <!-- UUID: f4ce2a59-886f-4e82-bfc3-243f7e0b2e1a -->

`Active`

###### A.6.1.1.8.2.2.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 0580085d-43e0-4c0e-81d9-9d92a9ea0215 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.2.1.1.2.1 - Ozone Instance Configuration Document Location [Core]  <!-- UUID: 370808df-acc5-425a-89f8-2bd72db3ba85 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.8.2.2.1.2.1 - Ozone Instance Configuration Document](204124cd-73cd-4862-9288-a3c8ecd65fcc).

###### A.6.1.1.8.2.2.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 1ddc6150-a963-4086-8e4c-4a878d2a95f9 -->

This document contains a Directory of all Instances of the Executor Accord Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.2.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 012578b7-90f4-42c6-ac63-4bcaf199565e -->

This document contains a Directory of all prospective Instances of the Executor Accord Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.2.1.1.2 - Active Instances Directory](0580085d-43e0-4c0e-81d9-9d92a9ea0215), whereas failed Invocations are Archived in [A.6.1.1.8.2.2.1.1.5 - Hub Data Repository](fbe85851-1f5d-4762-a27e-3c6681a1d7f5).

###### A.6.1.1.8.2.2.1.1.5 - Hub Data Repository [Core]  <!-- UUID: fbe85851-1f5d-4762-a27e-3c6681a1d7f5 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.2.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: f62cf432-f30a-4277-9dfe-79d7bcab8c66 -->

The subtrees for archived Invocations and Instances of the Executor Accord Primitive are stored here.

###### A.6.1.1.8.2.2.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 3902f9f9-a85d-4322-ad5b-3e6c5fa1254d -->

The subtrees for failed Invocations of the Executor Accord Primitive are stored here.

###### A.6.1.1.8.2.2.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 3cbe1f10-f88f-4e74-89f8-591424e9845e -->

The subtrees for Instances of the Executor Accord Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.2.1.2 - Active Instances [Core]  <!-- UUID: e7f6dd4d-2943-40a2-ba6c-8c738e5fc0bd -->

The Instances of the Executor Accord Primitive with `Active` Status are stored herein.

###### A.6.1.1.8.2.2.1.2.1 - Ozone Instance Configuration Document [Core]  <!-- UUID: 204124cd-73cd-4862-9288-a3c8ecd65fcc -->

The documents herein contain the Instance Configuration Document for the Ozone Executor Accord Primitive Instance.

###### A.6.1.1.8.2.2.1.2.1.1 - Parameters [Core]  <!-- UUID: a18b8499-8971-4f2a-a6ad-0d5b03f4db18 -->

The documents herein define the parameters of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.8.2.2.1.2.1.1.1 - Operational Executor Agent [Core]  <!-- UUID: c1f2c961-08b0-4060-abd6-12f4e26dc682 -->

The Operational Facilitator and Operational GovOps for Ozone are specified in [A.6.1.2.2 - Operational Executor Agent Ozone](565660dd-7850-4c3a-8dba-554542bf103a).

###### A.6.1.1.8.2.2.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: 7964aebd-6373-405c-9e7c-d23ca86baf5d -->

The documents herein define the custom parameters of the Ozone Instance of the Executor Accord Primitive, if any.

###### A.6.1.1.8.2.2.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: ce03f140-55da-403f-9ce2-28e27177fe6a -->

The documents herein define the process for the ongoing management of the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.8.2.2.1.2.1.3 - Data Repository [Core]  <!-- UUID: ec907cef-df83-4502-ada8-920c3e020e1b -->

The documents herein contain data relevant to the Ozone Instance of the Executor Accord Primitive.

###### A.6.1.1.8.2.2.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: e60e7340-7e86-4207-b725-2b1380f637d4 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.2.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 15f11c14-4ae7-4e7b-84c8-211fb93b6f8b -->

The materials associated with Operational GovOps review during the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.2.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: b2ef0e67-5e45-43f0-a62b-6a3669db4cc8 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.8.2.2.1.3 - Completed Instances [Core]  <!-- UUID: 0bf3b18f-3381-4f7d-be8d-20edbe53d69d -->

The Instances of the Executor Accord Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.2.1.4 - In Progress Invocations [Core]  <!-- UUID: 896f5790-396e-45c5-a907-b01a6368985a -->

The in progress Invocations of the Executor Accord Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.2.1.2 - Active Instances](e7f6dd4d-2943-40a2-ba6c-8c738e5fc0bd).

#### A.6.1.1.8.2.2.2 - Root Edit Primitive [Core]  <!-- UUID: 526f3ff3-e9d5-4de3-a7d7-60baf979e471 -->

The documents herein contain all data and specifications for Launch Agent 7's Instance of the Root Edit Primitive. See [A.2.2.6.2 - Root Edit Primitive](78488c6b-d77f-4344-b954-476e415a2c7d).

##### A.6.1.1.8.2.2.2.1 - Primitive Hub Document [Core]  <!-- UUID: b872e10d-6077-4a05-af0d-e03faed0f48a -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Root Edit Primitive.

###### A.6.1.1.8.2.2.2.1.1 - Global Activation Status [Core]  <!-- UUID: abdedb78-417e-4b68-9226-f0cd5e0ebfc3 -->

`Active`

###### A.6.1.1.8.2.2.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 1aa5f0b4-7024-4b67-ac0e-85fdb34dc515 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.2.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 8b6cdff1-641d-473c-8942-98dae58c707e -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.8.2.2.2.2.1 - Single Instance Configuration Document](c49e173d-f052-4825-bab1-0506c3db9353).

###### A.6.1.1.8.2.2.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 028d65c5-a40b-43cc-9db7-7f313a3ff257 -->

This document contains a Directory of all Instances of the Root Edit Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.2.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: fd4b8028-02aa-4647-aef8-153d5b8afd6c -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.8.2.2.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 0d0e614d-32d3-4ae3-9c46-113dcc0ec144 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.2.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: e29ca48b-43b6-499d-94eb-136f8e9f8310 -->

The subtrees for archived Invocations and Instances of the Root Edit Primitive are stored here.

###### A.6.1.1.8.2.2.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: c4ec3e46-3c74-4277-9207-09fd89fa46f4 -->

The subtrees for failed Invocations of the Root Edit Primitive are stored here.

###### A.6.1.1.8.2.2.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 63d1d8bd-b89f-4584-87d1-2a0a971d36a1 -->

The subtrees for Instances of the Root Edit Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.2.2.2 - Active Instances [Core]  <!-- UUID: 8d989fff-4cd4-4742-89eb-307e8b2a3404 -->

The Instances of the Root Edit Primitive with `Active` Status are stored herein.

###### A.6.1.1.8.2.2.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: c49e173d-f052-4825-bab1-0506c3db9353 -->

The documents herein contain the Instance Configuration Document for the Single Root Edit Primitive Instance.

###### A.6.1.1.8.2.2.2.2.1.1 - Parameters [Core]  <!-- UUID: 3da1740c-9f67-4e40-9111-5cfee617e244 -->

The parameters of the Root Edit Primitive are fully specified by the Operational Process Definition in [A.6.1.1.8.2.2.2.2.1.2 - Operational Process Definition](881b6df0-56fb-498e-bc1a-d9028c0151ad).

###### A.6.1.1.8.2.2.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 881b6df0-56fb-498e-bc1a-d9028c0151ad -->

The documents herein define the process for using the Root Edit Primitive to update the Launch Agent 7 Agent Artifact. Information on Launch Agent 7 governance that is unrelated to the use of the Root Edit Primitive is located at [A.6.1.1.8.3.1 - Governance Information Unrelated To Root Edit Primitive](c18d1d28-3b1f-4173-87dd-f697ab2d2539).

###### A.6.1.1.8.2.2.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 9d637b4a-868b-47c1-bbaf-099aeede1da2 -->

The documents herein define the process for using the Root Edit Primitive to update the Launch Agent 7 Agent Artifact in routine or normal conditions (i.e., non-emergency situations).

###### A.6.1.1.8.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission [Core]  <!-- UUID: fd43ac8d-5461-46e6-8902-4526ef677e3a -->

The Root Edit process begins with an AGENT7 token holder submitting a proposal through the Powerhouse system containing a draft Artifact Edit Proposal. An AGENT7 token holder must hold at least 1% of the circulating token supply to submit a proposal. The proposal must also be posted on the Sky Forum under the "Launch Agent 7 Prime" category.

###### A.6.1.1.8.2.2.2.2.1.2.1.1.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: 0048952f-30e2-484a-975a-62cc9e84c715 -->

Until the Powerhouse system supports submitting Artifact Edit Proposals, AGENT7 token holders may submit Artifact Edit Proposals by posting them to the Sky Forum under the "Launch Agent 7 Prime" category. The title of the post must include the text "Launch Agent 7 Artifact Edit Proposal". The post must include cryptographic proof that the author controls an account holding the required percentage of the total Launch Agent 7 token supply specified in [A.6.1.1.8.2.2.2.2.1.2.1.1 - Root Edit Proposal Submission](fd43ac8d-5461-46e6-8902-4526ef677e3a).

###### A.6.1.1.8.2.2.2.2.1.2.1.2 - Root Edit Expert Advisor Review [Core]  <!-- UUID: 089948f6-f451-4541-bdf5-5cb4113332fa -->

A future iteration of the Launch Agent 7 Artifact will specify guidelines for obtaining specialized review of proposals requiring advanced technical or financial analysis.

###### A.6.1.1.8.2.2.2.2.1.2.1.3 - Root Edit Proposal Review By Operational Facilitator [Core]  <!-- UUID: 7122bf98-1167-4a50-b411-90254d9d4bb7 -->

Within seven (7) days of the proposal being submitted, the Operational Facilitator must review the Root Edit Proposal for alignment.

If the proposal is aligned, the Operational Facilitator must respond to the Forum post to announce their finding. In this Forum post, the Operational Facilitator must also confirm that the proposal is feasible for Operational GovOps to operationalize.

If the proposal is misaligned, the Operational Facilitator must respond to the Forum post to announce their finding and provide the reasoning for it.

###### A.6.1.1.8.2.2.2.2.1.2.1.4 - Root Edit Token Holder Vote [Core]  <!-- UUID: 0c0209b7-fe8c-4d94-8daa-00057bb135cf -->

Where their review of the proposal results in a finding of alignment with the Sky Core Atlas and Launch Agent 7 Artifact, the Operational Facilitator next triggers a Snapshot poll to allow token holders to vote on the proposal. The poll is open for three (3) days. A poll must have at least 10% of the circulating token supply participating and must have 50% of votes in favor to be approved.

###### A.6.1.1.8.2.2.2.2.1.2.1.5 - Root Edit Artifact Update [Core]  <!-- UUID: f121258d-27b1-443a-8734-f170667dde3d -->

At the conclusion of the poll, if the proposal is approved, the Operational Facilitator submits the edit to Powerhouse to formally update the Agent Artifact. Regardless of the outcome, the Operational Facilitator updates the Powerhouse System to include the result of the vote, including any pertinent documents.

###### A.6.1.1.8.2.2.2.2.1.2.1.5.1 - Short-Term Transitionary Measures [Core]  <!-- UUID: f46cd437-80bb-4f7c-b8c0-eef464465349 -->

Until the Powerhouse system supports updating Agent Artifacts, the Operational Facilitator works with the Core Facilitator to update the Atlas GitHub repository located at [https://github.com/sky-ecosystem/next-gen-atlas/pulls](https://github.com/sky-ecosystem/next-gen-atlas/pulls) to reflect proposals approved by Prime Governance.

###### A.6.1.1.8.2.2.2.2.1.2.1.6 - Artifact Edit Restrictions [Core]  <!-- UUID: 0049ae2e-37a7-4bab-ab08-461caba3dcbb -->

The Launch Agent 7 Artifact cannot be edited in any way that violates the Sky Core Atlas or its specifications of the Sky Primitives, or in any way that is otherwise misaligned. The Operational Facilitator must enforce this rule through their review of Artifact Edit Proposals.

###### A.6.1.1.8.2.2.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: cfa59ab2-4a7e-4bcd-96b9-e64b295b372e -->

The documents herein define the process for using the Root Edit Primitive to update the Launch Agent 7 Agent Artifact in non-routine conditions.

###### A.6.1.1.8.2.2.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 3fe13a8c-48dc-4b6b-a0a8-a1b2ba014866 -->

The documents herein define the process for using the Root Edit Primitive to update the Launch Agent 7 Agent Artifact in emergency situations.

###### A.6.1.1.8.2.2.2.2.1.2.3.1 - Root Edit Voting Process In Emergency Situations [Core]  <!-- UUID: ac18c8ca-174b-4504-85e2-eaef85d3e375 -->

In an Emergency Situation, as defined by the Sky Core Atlas in [A.1.9.1.1 - Definition Of Emergency Situations](5eafb29e-84a0-4a53-a798-3f958c880225), the Operational Facilitator may allow a Root Edit to occur more quickly than the timeline specified above. Where feasible, the Operational Facilitator should announce the decision to deploy the emergency Root Edit protocol and provide their reasoning via a public Sky Forum post (under the "Launch Agent 7 Prime" category), unless doing so would endanger Launch Agent 7 or its users.

###### A.6.1.1.8.2.2.2.2.1.3 - Data Repository [Core]  <!-- UUID: 69761497-4868-413b-965d-ff1679ee3ed7 -->

The documents herein contain data relevant to the Single Instance of the Root Edit Primitive.

###### A.6.1.1.8.2.2.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: d29e42dd-0675-47b8-b0c9-8e88a7f17f14 -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.2.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: f8798270-5625-496f-87f5-b79f8981fd54 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.2.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 19d6d80e-edfc-45ed-9909-8130a006c542 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.8.2.2.2.3 - Completed Instances [Core]  <!-- UUID: 2ce26124-5604-42ae-a3ab-9790a4a9a702 -->

The Instances of the Root Edit Primitive with `Completed` Status are contained herein.

##### A.6.1.1.8.2.2.2.4 - In Progress Invocations [Core]  <!-- UUID: 719e16f2-bd1b-4ee3-b86b-7e02de533ac5 -->

Because the Root Edit Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.8.2.2.3 - Light Agent Primitive [Core]  <!-- UUID: 103c14cc-c21d-403b-996e-38f661a63093 -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Light Agent Primitive. See [A.2.2.6.3 - Light Agent Primitive](44028423-2cd1-40cb-89ac-3f762b602b90).

##### A.6.1.1.8.2.2.3.1 - Primitive Hub Document [Core]  <!-- UUID: c45b24ee-844e-4fa4-bdd5-6f4af842fbea -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Light Agent Primitive.

###### A.6.1.1.8.2.2.3.1.1 - Global Activation Status [Core]  <!-- UUID: 8d69c6f7-299f-470f-97fd-ba16bc3077b6 -->

`Inactive`

###### A.6.1.1.8.2.2.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 52113994-f0f0-43a7-859d-01ba0890d5c4 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.2.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 16b11dbf-2840-4db2-9f50-76f3199d4af3 -->

This document contains a Directory of all Instances of the Light Agent Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.2.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: bd37edb0-6a4b-4272-afa1-8fdc9e46434f -->

This document contains a Directory of all prospective Instances of the Light Agent Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.2.3.1.2 - Active Instances Directory](52113994-f0f0-43a7-859d-01ba0890d5c4), whereas failed Invocations are Archived in [A.6.1.1.8.2.2.3.1.5 - Hub Data Repository](4c37b870-fe4e-4313-8b31-5782ee1f2f13).

###### A.6.1.1.8.2.2.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 4c37b870-fe4e-4313-8b31-5782ee1f2f13 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.2.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 18c6c3c3-e208-4f6a-a7d3-9d984fdebad0 -->

The subtrees for archived Invocations and Instances of the Light Agent Primitive are stored here.

###### A.6.1.1.8.2.2.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: b132a4d7-61fe-4f2c-bd6c-0af62795f044 -->

The subtrees for failed Invocations of the Light Agent Primitive are stored here.

###### A.6.1.1.8.2.2.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: af6871dc-4623-4e1f-9282-1e5c658bf879 -->

The subtrees for Instances of the Light Agent Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.2.3.2 - Active Instances [Core]  <!-- UUID: 7b8c9d42-3412-4bc0-8439-8178b3b40bf0 -->

The Instances of the Light Agent Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.2.3.3 - Completed Instances [Core]  <!-- UUID: a0bdc146-76ae-4b11-94ea-523b9151e417 -->

The Instances of the Light Agent Primitive with `Completed` Status are contained herein.

##### A.6.1.1.8.2.2.3.4 - In Progress Invocations [Core]  <!-- UUID: 60754835-87dc-4921-b13c-f9ee34d619ca -->

The in progress Invocations of the Light Agent Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.2.3.2 - Active Instances](7b8c9d42-3412-4bc0-8439-8178b3b40bf0).

### A.6.1.1.8.2.3 - Ecosystem Upkeep Primitives [Core]  <!-- UUID: 137a06da-2db3-4762-9cad-d26a9fc99d4b -->

The documents herein implement the [A.2.2.7 - Ecosystem Upkeep Primitives](25673fd2-76cb-4c4d-8ec6-8c489207bcfc).

#### A.6.1.1.8.2.3.1 - Ecosystem Upkeep Fee Primitive [Core]  <!-- UUID: 235b6631-e033-4c9e-b31d-3a44feab2691 -->

The documents herein contain all data and specifications for Launch Agent 7's Instance of the Ecosystem Upkeep Fee Primitive. See [A.2.2.7.1 - Ecosystem Upkeep Fee Primitive](a21616f4-1611-4e0b-87b2-efbdff9f6f28).

##### A.6.1.1.8.2.3.1.1 - Primitive Hub Document [Core]  <!-- UUID: 2960ee87-c20d-4172-b938-5007663774eb -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.8.2.3.1.1.1 - Global Activation Status [Core]  <!-- UUID: dc299e36-9c46-4b13-81cd-8d4fc85f31d3 -->

`Active`

###### A.6.1.1.8.2.3.1.1.2 - Active Instances Directory [Core]  <!-- UUID: fe90717a-9451-4f01-a5fe-2663342f0283 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.3.1.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: 5c8bdca5-4b57-413a-81fc-bf39f991e12b -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.8.2.3.1.2.1 - Single Instance Configuration Document](2fa1a658-3588-45cd-a6e4-ceb0cc8f57d8).

###### A.6.1.1.8.2.3.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 0ea3700e-3d71-472e-962e-3d3a16e0a020 -->

This document contains a Directory of all Instances of the Ecosystem Upkeep Fee Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.3.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: dea9d796-cd57-413b-9793-1e4d7c46d7d1 -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.8.2.3.1.1.5 - Hub Data Repository [Core]  <!-- UUID: b801d192-aaf7-4b96-aca4-a0574210787f -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.3.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 5ad0a20f-9776-45f7-a616-d23ba788c826 -->

The subtrees for archived Invocations and Instances of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.8.2.3.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 8c9cd3a4-82ed-4117-8066-bd77b2c0d922 -->

The subtrees for failed Invocations of the Ecosystem Upkeep Fee Primitive are stored here.

###### A.6.1.1.8.2.3.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: bddcc7eb-5d2d-402b-a2b7-dc8e2be70e1c -->

The subtrees for Instances of the Ecosystem Upkeep Fee Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.3.1.2 - Active Instances [Core]  <!-- UUID: f2c71db2-efde-4d80-800b-945f8ca1dab0 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Active` Status are stored herein.

###### A.6.1.1.8.2.3.1.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 2fa1a658-3588-45cd-a6e4-ceb0cc8f57d8 -->

The documents herein contain the Instance Configuration Document for the Single Ecosystem Upkeep Fee Primitive Instance.

###### A.6.1.1.8.2.3.1.2.1.1 - Parameters [Core]  <!-- UUID: 9f1da224-aad0-4903-8e74-7dbd1dc6c30e -->

The documents herein define the parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.8.2.3.1.2.1.1.1 - Terms [Core]  <!-- UUID: b5a5b8d8-7022-46a7-a351-dc767a5618c4 -->

Launch Agent 7 will pay 0.50% of its market capitalization per year in USDS.

###### A.6.1.1.8.2.3.1.2.1.1.2 - Custom Instance Parameters [Core]  <!-- UUID: f5b52d8f-a131-428a-bc3b-bd87d2493ecb -->

The documents herein define the custom parameters of the Single Instance of the Ecosystem Upkeep Fee Primitive, if any.

###### A.6.1.1.8.2.3.1.2.1.2 - Operational Process Definition [Core]  <!-- UUID: 5a14c374-344f-4073-bbb2-562e1665c2be -->

The documents herein define the process for the ongoing management of the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.8.2.3.1.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 8832e413-3b06-4724-b5eb-eccabc08db82 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.8.2.3.1.2.1.2.1.1 - Process Definition For Upkeep Fee Payment [Core]  <!-- UUID: ee639561-265a-42c1-be31-10e61e817ad0 -->

The process to pay 0.50% of Launch Agent 7's market capitalization per year in USDS will be specified in future iterations of the Launch Agent 7 Artifact.

###### A.6.1.1.8.2.3.1.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: fed0b0c1-a7ee-4839-af72-c6ca6257beca -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.8.2.3.1.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 4aaab4a9-e619-4343-a308-791a5a000ee6 -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.8.2.3.1.2.1.3 - Data Repository [Core]  <!-- UUID: be200704-5152-4884-8acb-4d0ef2f7307c -->

The documents herein contain data relevant to the Single Instance of the Ecosystem Upkeep Fee Primitive.

###### A.6.1.1.8.2.3.1.2.1.3.1 - Initial Planning [Core]  <!-- UUID: 1126acc9-9fb2-493b-b6ed-78cdccb75c5a -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.3.1.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: 4d4d1a09-cb35-4582-bdb1-919ec4e52a16 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.3.1.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: c828c63f-634c-42f6-8741-27edbd83ff68 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.8.2.3.1.3 - Completed Instances [Core]  <!-- UUID: 6aca1d4d-5962-4215-a778-cdad996dc4f8 -->

The Instances of the Ecosystem Upkeep Fee Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.3.1.4 - In Progress Invocations [Core]  <!-- UUID: 92bfea11-2401-4744-8911-59c22d891b77 -->

Because the Ecosystem Upkeep Fee Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

#### A.6.1.1.8.2.3.2 - Upkeep Rebate Primitive [Core]  <!-- UUID: a36bf711-7951-497c-9c4b-c761dbff351a -->

The documents herein contain all data and specifications for Launch Agent 7's instance of the Upkeep Rebate Primitive. See [A.2.2.7.2 - Upkeep Rebate Primitive](569e1c2b-0e69-43e7-8491-06cc5f7d2988).

##### A.6.1.1.8.2.3.2.1 - Primitive Hub Document [Core]  <!-- UUID: e087c1a6-3f6f-4309-952d-71b74691c6de -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Upkeep Rebate Primitive.

###### A.6.1.1.8.2.3.2.1.1 - Global Activation Status [Core]  <!-- UUID: 9479c841-04d0-4a76-bec8-3255106fcc47 -->

`Active`

###### A.6.1.1.8.2.3.2.1.2 - Active Instances Directory [Core]  <!-- UUID: a986a180-e2a6-40bb-aec5-58e6584d958e -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.3.2.1.2.1 - Single Instance Configuration Document Location [Core]  <!-- UUID: b05793b0-6d46-448f-9e83-41ee55141eb0 -->

This Instance’s associated Instance Configuration Document is located at [A.6.1.1.8.2.3.2.2.1 - Single Instance Configuration Document](24e3d323-e9a4-4bb3-ba4d-ae92aa745e96).

###### A.6.1.1.8.2.3.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 4f195e95-65db-432e-80ea-9b77a8b2c355 -->

This document contains a Directory of all Instances of the Upkeep Rebate Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.3.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 98e6bca4-9981-4e38-814b-8394eeb62778 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

###### A.6.1.1.8.2.3.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 1bdaf050-86c4-44a1-8926-a6d083e0ac65 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.3.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 20b38bb0-bcdc-4ded-ac96-2e445e10afc4 -->

The subtrees for archived Invocations and Instances of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.8.2.3.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 62a31c8c-2e86-4df6-a422-f76cfa6610e5 -->

The subtrees for failed Invocations of the Upkeep Rebate Primitive are stored here.

###### A.6.1.1.8.2.3.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: b13c4e9f-7366-4ca3-aeb2-3f7666127a02 -->

The subtrees for Instances of the Upkeep Rebate Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.3.2.2 - Active Instances [Core]  <!-- UUID: b5197e9e-014b-4527-a1b1-399cf3475bef -->

The Instances of the Upkeep Rebate Primitive with `Active` Status are stored herein.

###### A.6.1.1.8.2.3.2.2.1 - Single Instance Configuration Document [Core]  <!-- UUID: 24e3d323-e9a4-4bb3-ba4d-ae92aa745e96 -->

The documents herein contain the Instance Configuration Document for the Single Upkeep Rebate Primitive Instance.

###### A.6.1.1.8.2.3.2.2.1.1 - Parameters [Core]  <!-- UUID: 74e0d2e3-fa72-48d8-b1f1-5f7dc0caacbc -->

Every Prime Agent is entitled to the Upkeep Rebate Primitive for tokens of other Prime Agents that they hold. Because this right automatically applies, there are no parameters.

###### A.6.1.1.8.2.3.2.2.1.2 - Operational Process Definition [Core]  <!-- UUID: ce3e37b2-5061-454e-8b5e-ba08e1e66bb9 -->

The documents herein define the process for the ongoing management of the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.8.2.3.2.2.1.2.1 - Routine Protocol [Core]  <!-- UUID: 33aac9cf-306f-46ce-bdaf-84fdcafcedf3 -->

This document defines the protocol for routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.8.2.3.2.2.1.2.1.1 - Launch Agent 7 Holds Tokens Of Other Agents In Its SubProxy Account [Core]  <!-- UUID: 67240dea-8bc1-4ac7-9da5-7079b7af6424 -->

Launch Agent 7 keeps all tokens of other Agents it holds in its SubProxy account.

###### A.6.1.1.8.2.3.2.2.1.2.1.2 - Launch Agent 7 Deducts Rebate From Ecosystem Upkeep Fees [Core]  <!-- UUID: 22e8780f-64f2-416b-93b5-ef5584583b15 -->

When paying Ecosystem Upkeep fees, Launch Agent 7 deducts the rebate from the fees it pays.

###### A.6.1.1.8.2.3.2.2.1.2.1.3 - Operational GovOps Reviews Rebate [Core]  <!-- UUID: 47d2823b-2e93-4a7e-b181-6c232d7429ed -->

Operational GovOps reviews Launch Agent 7's calculation of the rebate before executing a return of surplus to token holders. In the event of any issues, Operational GovOps cannot execute the distribution. If Operational GovOps does not execute the distribution, Operational GovOps must post an explanation on the Sky Forum under the "Launch Agent 7 Prime" category and work with Launch Agent 7 to resolve the disagreement. If Operational GovOps and Launch Agent 7 cannot resolve the disagreement, it must be escalated to Core GovOps.

###### A.6.1.1.8.2.3.2.2.1.2.2 - Non-Routine Protocol [Core]  <!-- UUID: 455301ee-b352-4bb1-8b11-a215d501e095 -->

The documents herein define the protocol for non-routine ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.8.2.3.2.2.1.2.3 - Emergency Protocol [Core]  <!-- UUID: 6009ee51-2540-44db-946a-8feb400824cb -->

The documents herein define the protocol for handling emergency situations in the ongoing management of the Single Instance of this Upkeep Rebate Primitive.

###### A.6.1.1.8.2.3.2.2.1.3 - Data Repository [Core]  <!-- UUID: 9ac2f1d8-a349-4348-8f66-79fdc605eab8 -->

The documents herein contain data relevant to the Single Instance of the Upkeep Rebate Primitive.

###### A.6.1.1.8.2.3.2.2.1.3.1 - Initial Planning [Core]  <!-- UUID: d4946913-4550-4250-b48e-5fe97e30728c -->

The materials associated with initial planning of the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.3.2.2.1.3.2 - Operational GovOps Review [Core]  <!-- UUID: e07b73b0-079a-45ba-a861-03d6f4d7ac49 -->

The materials associated with Operational GovOps Review during the Invocation of this Instance are contained herein.

###### A.6.1.1.8.2.3.2.2.1.3.3 - Artifact Edit Proposal [Core]  <!-- UUID: 990d5e1a-d9ac-4aa6-a663-ec310f193d84 -->

The materials associated with preparing the Artifact Edit Proposal during the Invocation of this Instance are contained herein.

##### A.6.1.1.8.2.3.2.3 - Completed Instances [Core]  <!-- UUID: ccc58c85-b8b2-429a-a95d-df91902a6697 -->

The Instances of the Upkeep Rebate Primitive with `Completed` Status are contained herein.

##### A.6.1.1.8.2.3.2.4 - In Progress Invocations [Core]  <!-- UUID: c5610121-5800-44d1-bd16-bd0022fd2955 -->

Because the Upkeep Rebate Primitive is deployed only once, no further Instances of the Primitive can be Invoked.

### A.6.1.1.8.2.4 - SkyLink Primitives [Core]  <!-- UUID: 5d27e7f0-7d57-4740-8c08-6df78e9880a7 -->

The documents herein implement the SkyLink Primitives for Launch Agent 7. See [A.2.2.8 - SkyLink Primitives](7b5d8965-a64c-4c44-b742-607f51f69d8f).

#### A.6.1.1.8.2.4.1 - Token SkyLink Primitive [Core]  <!-- UUID: 75507209-dc1e-414a-a112-75f7b076518c -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Token SkyLink Primitive. See [A.2.2.8.1 - Token SkyLink Primitive](4504d2d4-ee45-4a07-8c5b-9baf20b12e76).

##### A.6.1.1.8.2.4.1.1 - Primitive Hub Document [Core]  <!-- UUID: a964694f-360d-4765-b0e0-54907b66559d -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Token SkyLink Primitive.

###### A.6.1.1.8.2.4.1.1.1 - Global Activation Status [Core]  <!-- UUID: ac469feb-2bd9-4fda-925a-3a8efa5c0c74 -->

`Inactive`

###### A.6.1.1.8.2.4.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 0d4a37e4-56d2-49c2-8166-9bc934ebeddf -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.4.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: fa968e1d-c573-4a3c-b1e8-ec96bdf68e96 -->

This document contains a Directory of all Instances of the Token SkyLink Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.4.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: cea9280a-74ca-49fe-a2a4-76762af38073 -->

This document contains a Directory of all prospective Instances of the Token SkyLink Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.4.1.1.2 - Active Instances Directory](0d4a37e4-56d2-49c2-8166-9bc934ebeddf), whereas failed Invocations are Archived in [A.6.1.1.8.2.4.1.1.5 - Hub Data Repository](35b78704-fd3a-4d05-95b3-ba20f73b4c18).

###### A.6.1.1.8.2.4.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 35b78704-fd3a-4d05-95b3-ba20f73b4c18 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.4.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 00aec26a-18b8-4617-a764-05283d14df9e -->

The subtrees for archived Invocations and Instances of the Token SkyLink Primitive are stored here.

###### A.6.1.1.8.2.4.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: f80317dc-9641-4299-ad2c-37b6b20b9b61 -->

The subtrees for failed Invocations of the Token SkyLink Primitive are stored here.

###### A.6.1.1.8.2.4.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 2e48a4ea-2604-44f9-b1a0-b9c3bc38dae1 -->

The subtrees for Instances of the Token SkyLink Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.4.1.2 - Active Instances [Core]  <!-- UUID: 974d0a20-cdff-431f-bc41-dbb7c0dab434 -->

The Instances of the Token SkyLink Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.4.1.3 - Completed Instances [Core]  <!-- UUID: fa9f564b-220c-4b80-b354-3fea21fc4bce -->

The Instances of the Token SkyLink Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.4.1.4 - In Progress Invocations [Core]  <!-- UUID: 3951cd54-791c-46cc-b3e0-2b930d7e4723 -->

The in progress Invocations of the Token SkyLink Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.4.1.2 - Active Instances](974d0a20-cdff-431f-bc41-dbb7c0dab434).

### A.6.1.1.8.2.5 - Demand Side Stablecoin Primitives [Core]  <!-- UUID: d16b5adc-f990-4160-b324-0b687292fef3 -->

The documents herein implement the Demand Side Stablecoin Primitives for Launch Agent 7. See [A.2.2.9 - Demand Side Stablecoin Primitives](26415305-432d-423b-9553-3f325279712d).

#### A.6.1.1.8.2.5.1 - Distribution Reward Primitive [Core]  <!-- UUID: cbfe8a72-d21f-4edd-887e-2d9bbd2012e9 -->

The documents herein contain all data and specifications for Launch Agent 7's instances of the Distribution Reward Primitive. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6).

##### A.6.1.1.8.2.5.1.1 - Primitive Hub Document [Core]  <!-- UUID: 28cc6a65-84be-4019-b0fe-12ed428670a9 -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Distribution Reward Primitive.

###### A.6.1.1.8.2.5.1.1.1 - Global Activation Status [Core]  <!-- UUID: 4740c001-7b76-42ae-a599-6ad4ed7705aa -->

`Active`

###### A.6.1.1.8.2.5.1.1.2 - Active Instances Directory [Core]  <!-- UUID: 91bc2e83-ed71-4343-a527-084001407db0 -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.5.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: ea7b87af-62ff-424e-8994-80eed40570ce -->

This document contains a Directory of all Instances of the Distribution Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.5.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 5f414c27-bd79-4265-a1fa-eb199c270852 -->

This document contains a Directory of all prospective Instances of the Distribution Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.5.1.1.2 - Active Instances Directory](91bc2e83-ed71-4343-a527-084001407db0), whereas failed Invocations are Archived in [A.6.1.1.8.2.5.1.1.5 - Hub Data Repository](cec11621-1805-4b87-8eaf-cfcf5200391f).

###### A.6.1.1.8.2.5.1.1.5 - Hub Data Repository [Core]  <!-- UUID: cec11621-1805-4b87-8eaf-cfcf5200391f -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.5.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 0110092c-d37b-45a4-a6be-a81b1607c2ba -->

The subtrees for archived Invocations and Instances of the Distribution Reward Primitive are stored here.

###### A.6.1.1.8.2.5.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 6514cf35-a87d-45d7-b102-560ed642df7e -->

The subtrees for failed Invocations of the Distribution Reward Primitive are stored here.

###### A.6.1.1.8.2.5.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: df4cd80b-d4e4-4e2c-b6ed-56d70a109072 -->

The subtrees for Instances of the Distribution Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.5.1.2 - Active Instances [Core]  <!-- UUID: 11ae6de4-4ab6-4d0f-bf8c-1ab32aed0635 -->

The Instances of the Distribution Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.5.1.3 - Completed Instances [Core]  <!-- UUID: 96167687-c6bb-4687-8794-3f41e885831b -->

The Instances of the Distribution Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.5.1.4 - In Progress Invocations [Core]  <!-- UUID: f0f80202-cb0f-4480-8223-cac64d6556d6 -->

The in progress Invocations of the Distribution Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.5.1.2 - Active Instances](11ae6de4-4ab6-4d0f-bf8c-1ab32aed0635).

#### A.6.1.1.8.2.5.2 - Integration Boost Primitive [Core]  <!-- UUID: 18446ffd-1206-41bc-b735-6317d8b4f058 -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Integration Boost Primitive. See [A.2.2.9.2 - Integration Boost Primitive](73577399-62e4-4a83-ae11-64ef7e7b7f20).

##### A.6.1.1.8.2.5.2.1 - Primitive Hub Document [Core]  <!-- UUID: 99823d99-ddcd-49bc-8a48-9f1843a962f5 -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Integration Boost Primitive.

###### A.6.1.1.8.2.5.2.1.1 - Global Activation Status [Core]  <!-- UUID: 467eb662-d40b-414a-811b-88d15bb6e7e5 -->

`Active`

###### A.6.1.1.8.2.5.2.1.2 - Active Instances Directory [Core]  <!-- UUID: b25b5713-b5db-4666-af29-f569289df9d4 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.5.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: 18a11b40-1dd1-4aee-9d37-a8bf84fcdd79 -->

This document contains a Directory of all Instances of the Integration Boost Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.5.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 32f63086-f029-4454-952a-1a992833c216 -->

This document contains a Directory of all prospective Instances of the Integration Boost Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.5.2.1.2 - Active Instances Directory](b25b5713-b5db-4666-af29-f569289df9d4), whereas failed Invocations are Archived in [A.6.1.1.8.2.5.2.1.5 - Hub Data Repository](2fa2c7c2-6bfb-4620-bfa4-45c9d7cff7c6).

###### A.6.1.1.8.2.5.2.1.5 - Hub Data Repository [Core]  <!-- UUID: 2fa2c7c2-6bfb-4620-bfa4-45c9d7cff7c6 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.5.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 7af853f8-1d3d-4127-a734-0b22b9b95cdd -->

The subtrees for archived Invocations and Instances of the Integration Boost Primitive are stored here.

###### A.6.1.1.8.2.5.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 0eaad468-2023-4bc3-a9f6-2d58ae9a27f7 -->

The subtrees for failed Invocations of the Integration Boost Primitive are stored here.

###### A.6.1.1.8.2.5.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 78e5fefc-687c-4cae-b448-e7d556e3f088 -->

The subtrees for Instances of the Integration Boost Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.5.2.2 - Active Instances [Core]  <!-- UUID: 9219e0ee-66b9-4ede-b741-ec8b03d92405 -->

The Instances of the Integration Boost Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.5.2.3 - Completed Instances [Core]  <!-- UUID: be5f8fed-3433-4c4c-b199-e62e36f59d96 -->

The Instances of the Integration Boost Primitive with `Completed` Status are contained herein.

##### A.6.1.1.8.2.5.2.4 - In Progress Invocations [Core]  <!-- UUID: 236422d6-f872-4b6f-9b1c-aea12fd8837e -->

The in progress Invocations of the Integration Boost Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.5.2.2 - Active Instances](9219e0ee-66b9-4ede-b741-ec8b03d92405).

#### A.6.1.1.8.2.5.3 - Pioneer Chain Primitive [Core]  <!-- UUID: 388c4c85-a228-4722-8001-02040cbb36ff -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Pioneer Chain Primitive. See [A.2.2.9.3 - Pioneer Chain Primitive](4c7be4c6-44b5-407a-94ae-3d7ca7e8039c).

##### A.6.1.1.8.2.5.3.1 - Primitive Hub Document [Core]  <!-- UUID: e5477412-eb2c-4aba-b0a5-3cbab8b4b1b4 -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Pioneer Chain Primitive.

###### A.6.1.1.8.2.5.3.1.1 - Global Activation Status [Core]  <!-- UUID: 4db04c3a-6884-4a81-b7f6-a17435d478f7 -->

`Inactive`

###### A.6.1.1.8.2.5.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 37c0dfc8-6bb3-4936-840f-08e15d8d13ec -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.5.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 8b3130a4-2849-4b30-b25a-33ccc090902f -->

This document contains a Directory of all Instances of the Pioneer Chain Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.5.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: ea90d778-f105-413f-9534-473aa1fe4b07 -->

This document contains a Directory of all prospective Instances of the Pioneer Chain Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.5.3.1.2 - Active Instances Directory](37c0dfc8-6bb3-4936-840f-08e15d8d13ec), whereas failed Invocations are Archived in [A.6.1.1.8.2.5.3.1.5 - Hub Data Repository](fae1a000-81c8-4a7f-a99e-3f1fccb25366).

###### A.6.1.1.8.2.5.3.1.5 - Hub Data Repository [Core]  <!-- UUID: fae1a000-81c8-4a7f-a99e-3f1fccb25366 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.5.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: a99b1995-c7e9-46a8-a088-b87e3ea65fd2 -->

The subtrees for archived Invocations and Instances of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.8.2.5.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 945ef091-8c0a-4ae4-bf0c-ae122154e35c -->

The subtrees for failed Invocations of the Pioneer Chain Primitive are stored here.

###### A.6.1.1.8.2.5.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: f1f77981-a831-4b0a-b7fc-8f18b35fef76 -->

The subtrees for Instances of the Pioneer Chain Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.5.3.2 - Active Instances [Core]  <!-- UUID: 0ed9935e-1a67-4423-871a-6a5addd51af5 -->

The Instances of the Pioneer Chain Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.5.3.3 - Completed Instances [Core]  <!-- UUID: 20495dd8-7f95-49c3-bb02-047067897e91 -->

The Instances of the Pioneer Chain Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.5.3.4 - In Progress Invocations [Core]  <!-- UUID: 8357b4a0-554e-488f-ad52-5f0e982bfa03 -->

The in progress Invocations of the Pioneer Chain Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.5.3.2 - Active Instances](0ed9935e-1a67-4423-871a-6a5addd51af5).

### A.6.1.1.8.2.6 - Supply Side Stablecoin Primitives [Core]  <!-- UUID: 80e9d9f2-956a-4bb1-a412-6efaad7dda56 -->

The documents herein implement the Supply Side Stablecoin Primitives for Launch Agent 7. See [A.2.2.10 - Supply Side Stablecoin Primitives](d1142876-33c2-4e21-9339-d8711525d46f).

#### A.6.1.1.8.2.6.1 - Allocation System Primitive [Core]  <!-- UUID: 929aa1ad-a1c6-4dd6-89ef-bc18316ec3b0 -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Allocation System Primitive. See [A.2.2.10.1 - Allocation System Primitive](9db14ab7-bb4b-4751-8084-843bd4359f2a).

##### A.6.1.1.8.2.6.1.1 - Primitive Hub Document [Core]  <!-- UUID: b0a3b8d2-e776-4604-aab1-bd68e851d042 -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Allocation System Primitive.

###### A.6.1.1.8.2.6.1.1.1 - Global Activation Status [Core]  <!-- UUID: 7dc4a32d-d14f-4fe1-af90-ff8e3a0f6e8a -->

`Active`

###### A.6.1.1.8.2.6.1.1.2 - Active Instances Directory [Core]  <!-- UUID: d232eaa6-bbbc-4de2-9b7a-d20b3a25ad45 -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.6.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 5c1014cd-2531-4438-84ae-37cf9c12c29b -->

This document contains a Directory of all Instances of the Allocation System Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.6.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: d0c5ad5f-ffe6-469b-b4e8-1f77b1a24739 -->

This document contains a Directory of all prospective Instances of the Allocation System Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.6.1.1.2 - Active Instances Directory](d232eaa6-bbbc-4de2-9b7a-d20b3a25ad45), whereas failed Invocations are Archived in [A.6.1.1.8.2.6.1.1.5 - Hub Data Repository](952b34e6-7983-4dd0-a46f-e3622c2346de).

###### A.6.1.1.8.2.6.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 952b34e6-7983-4dd0-a46f-e3622c2346de -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.6.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 4ba906c3-5163-4188-bcec-1635ad497c54 -->

The subtrees for archived Invocations and Instances of the Allocation System Primitive are stored here.

###### A.6.1.1.8.2.6.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 401da49b-16c4-4101-b0bf-28ef4d7beaf8 -->

The subtrees for failed Invocations of the Allocation System Primitive are stored here.

###### A.6.1.1.8.2.6.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: fe32b46e-7449-416d-a24f-5b3d31b4bbb9 -->

The subtrees for Instances of the Allocation System Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.6.1.2 - Multi-Instance Coordinator Document [Core]  <!-- UUID: a407dee4-36ec-4499-a3e6-e01008dd56cf -->

The documents herein provide general specifications of the Launch Agent 7 Liquidity Layer and define Launch Agent 7's overarching strategy and operational framework for managing across all Instances.

###### A.6.1.1.8.2.6.1.2.1 - General Specifications [Core]  <!-- UUID: d74aa2ed-b6fb-4dd1-83de-a334734bc48d -->

The documents herein contain general specifications for the Launch Agent 7 Liquidity Layer.

###### A.6.1.1.8.2.6.1.2.1.1 - Launch Agent 7 Liquidity Layer Architecture [Core]  <!-- UUID: 4abfa5e7-e1a8-4ade-89fb-a2ef26752877 -->

The documents herein describe the high-level design of the Launch Agent 7 Liquidity Layer, including its key smart contracts and their functionality.

###### A.6.1.1.8.2.6.1.2.1.1.1 - Launch Agent 7 Liquidity Layer Addresses [Core]  <!-- UUID: e9845cfa-2d27-45f0-b955-dbedd5d8ddb4 -->

The subdocuments herein provide the addresses of the Launch Agent 7 Liquidity Layer's constituent contracts.

###### A.6.1.1.8.2.6.1.2.1.1.1.1 - Allocator Contract Addresses [Core]  <!-- UUID: deed6d17-668a-4ebb-844b-19b25a293448 -->

The documents herein contain global key addresses for the Allocator Contracts.

###### A.6.1.1.8.2.6.1.2.1.1.1.1.1 - Allocator Buffer Contract [Core]  <!-- UUID: d5d47c10-f714-4c88-b4ac-e8937ef86134 -->

The address of the ALLOCATOR_BUFFER contract is: `0x67Ac5c8FbFDAc5265c995e9B2ACd830496438AfD`.

###### A.6.1.1.8.2.6.1.2.1.1.1.1.2 - Allocator Vault Contract [Core]  <!-- UUID: 97dfcdfa-9c39-49fe-95cc-a117635b3f52 -->

The address of the ALLOCATOR_VAULT (ALLOCATOR-INTERVAL-A) contract is: `0xDD3bE7650589E6A6171d454b026C4AD1a2C02720`.

##### A.6.1.1.8.2.6.1.3 - Active Instances [Core]  <!-- UUID: 132aaf59-d6fa-4260-b686-91246dba9897 -->

The Instances of the Allocation System Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.6.1.4 - Completed Instances [Core]  <!-- UUID: 122d8a6a-c54e-43c2-9e48-1ddecf8e4ebe -->

The Instances of the Allocation System Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.6.1.5 - In Progress Invocations [Core]  <!-- UUID: b835b079-0e89-4665-afe9-edb7b22c3317 -->

The in progress Invocations of the Allocation System Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.6.1.3 - Active Instances](132aaf59-d6fa-4260-b686-91246dba9897).

#### A.6.1.1.8.2.6.2 - Risk Capital Rental Primitive [Core]  <!-- UUID: d718c63a-1096-46e7-9ff7-c1c851679d45 -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Risk Capital Rental Primitive. See [A.2.2.10.2 - Risk Capital Rental Primitive](d8086dc0-7e77-4c6b-98c7-5fc41337a1ce).

##### A.6.1.1.8.2.6.2.1 - Primitive Hub Document [Core]  <!-- UUID: 796d1eab-a018-4e8f-9d86-8e1f2eea9c5b -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Risk Capital Rental Primitive.

###### A.6.1.1.8.2.6.2.1.1 - Global Activation Status [Core]  <!-- UUID: 24340f8a-a4a7-4002-9c61-c5d7d4e9d4b3 -->

`Inactive`

###### A.6.1.1.8.2.6.2.1.2 - Active Instances Directory [Core]  <!-- UUID: 56655922-1c77-40f7-83f4-3b9af9dc0c59 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.6.2.1.3 - Completed Instances Directory [Core]  <!-- UUID: efae8d35-a014-41fa-8a82-b2a4488e7058 -->

This document contains a Directory of all Instances of the Risk Capital Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.6.2.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 86ca0f50-a33b-4068-abd4-3f6a3adb9874 -->

This document contains a Directory of all prospective Instances of the Risk Capital Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.6.2.1.2 - Active Instances Directory](56655922-1c77-40f7-83f4-3b9af9dc0c59), whereas failed Invocations are Archived in [A.6.1.1.8.2.6.2.1.5 - Hub Data Repository](c054e1a5-5ea9-4f95-a469-d357bc30cd41).

###### A.6.1.1.8.2.6.2.1.5 - Hub Data Repository [Core]  <!-- UUID: c054e1a5-5ea9-4f95-a469-d357bc30cd41 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.6.2.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 33438a68-430e-4e13-b0bd-caa11b5578d0 -->

The subtrees for archived Invocations and Instances of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.8.2.6.2.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: 8b4a66ad-4e68-4a9b-b1a5-c835ec423cb9 -->

The subtrees for failed Invocations of the Risk Capital Rental Primitive are stored here.

###### A.6.1.1.8.2.6.2.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: 3286bcd1-544a-4cc2-8508-1a8bc0aecea5 -->

The subtrees for Instances of the Risk Capital Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.6.2.2 - Active Instances [Core]  <!-- UUID: 9a3c679d-a269-440e-9069-4bd85b428b3f -->

The Instances of the Risk Capital Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.6.2.3 - Completed Instances [Core]  <!-- UUID: f12949d0-1f1d-473f-89b1-f833523345af -->

The Instances of the Risk Capital Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.6.2.4 - In Progress Invocations [Core]  <!-- UUID: f2d93d71-1bf9-4199-8190-e1e0beeb5369 -->

The in progress Invocations of the Risk Capital Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.6.2.2 - Active Instances](9a3c679d-a269-440e-9069-4bd85b428b3f).

#### A.6.1.1.8.2.6.3 - Asset Liability Management Rental Primitive [Core]  <!-- UUID: 52c0af9a-b4e2-4ff5-ad4c-ffb82263d512 -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Asset Liability Management Rental Primitive. See [A.2.2.10.3 - Asset Liability Management Rental Primitive](bd1f1ce5-6c31-42fc-a2aa-694acf5eb08c).

##### A.6.1.1.8.2.6.3.1 - Primitive Hub Document [Core]  <!-- UUID: 3f05c2bb-7f5d-4716-b37e-fdda16d2417e -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Asset Liability Management Rental Primitive.

###### A.6.1.1.8.2.6.3.1.1 - Global Activation Status [Core]  <!-- UUID: 7444959d-c9aa-4e09-8df3-cbc3dd33b5b8 -->

`Inactive`

###### A.6.1.1.8.2.6.3.1.2 - Active Instances Directory [Core]  <!-- UUID: 0997aedd-8432-481a-a8b6-bbbbc1fb76d5 -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.6.3.1.3 - Completed Instances Directory [Core]  <!-- UUID: 3baef0e1-e11f-4ada-8d59-067f5bf10a30 -->

This document contains a Directory of all Instances of the Asset Liability Management Rental Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.6.3.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: 8d26415c-b07b-4236-8c0d-09dde4abdcce -->

This document contains a Directory of all prospective Instances of the Asset Liability Management Rental Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.6.3.1.2 - Active Instances Directory](0997aedd-8432-481a-a8b6-bbbbc1fb76d5), whereas failed Invocations are Archived in [A.6.1.1.8.2.6.3.1.5 - Hub Data Repository](26df5f96-9971-4361-8981-2687c410042c).

###### A.6.1.1.8.2.6.3.1.5 - Hub Data Repository [Core]  <!-- UUID: 26df5f96-9971-4361-8981-2687c410042c -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.6.3.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 4d418bb4-8fce-4784-b854-170f904ccd18 -->

The subtrees for archived Invocations and Instances of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.8.2.6.3.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: a3df996f-3e8b-46e2-ad57-f02f0f6b0b44 -->

The subtrees for failed Invocations of the Asset Liability Management Rental Primitive are stored here.

###### A.6.1.1.8.2.6.3.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: f8913006-a363-43fb-b353-2e6bcdf5291b -->

The subtrees for Instances of the Asset Liability Management Rental Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.6.3.2 - Active Instances [Core]  <!-- UUID: b3810d85-dc67-4ebd-805d-64af73333fd0 -->

The Instances of the Asset Liability Management Rental Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.6.3.3 - Completed Instances [Core]  <!-- UUID: e8c82f4c-ef8c-4f72-9346-fd33c20643a6 -->

The Instances of the Asset Liability Management Rental Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.6.3.4 - In Progress Invocations [Core]  <!-- UUID: eeb2185d-2a4c-45e3-872c-2d241e42d5c4 -->

The in progress Invocations of the Asset Liability Management Rental Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.6.3.2 - Active Instances](b3810d85-dc67-4ebd-805d-64af73333fd0).

### A.6.1.1.8.2.7 - Core Governance Primitives [Core]  <!-- UUID: 324dbc1c-aa4f-4b87-b171-6e7fad67236d -->

The documents herein implement the Core Governance Primitives for Launch Agent 7. See [A.2.2.11 - Core Governance Primitives](6fa54611-c744-4b9d-897d-b2a20e9cae5d).

#### A.6.1.1.8.2.7.1 - Core Governance Reward Primitive [Core]  <!-- UUID: db70350a-fd19-4fca-9341-03bcb7271de7 -->

The documents herein contain all data and specifications for Launch Agent 7's Instances of the Core Governance Reward Primitive. See [A.2.2.11.1 - Core Governance Reward Primitive](b22d1c08-042a-4466-94fe-9d28951e4d4a).

##### A.6.1.1.8.2.7.1.1 - Primitive Hub Document [Core]  <!-- UUID: 328e73e4-a676-45d7-bfc5-7e818010f5bd -->

The documents herein organize all base information relevant to Launch Agent 7's usage of the Core Governance Reward Primitive.

###### A.6.1.1.8.2.7.1.1.1 - Global Activation Status [Core]  <!-- UUID: 035a469d-0046-4380-9518-5e613a4d3268 -->

`Inactive`

###### A.6.1.1.8.2.7.1.1.2 - Active Instances Directory [Core]  <!-- UUID: e76c0b88-7755-4611-a884-9b5bd3d9c4d8 -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Active`.

###### A.6.1.1.8.2.7.1.1.3 - Completed Instances Directory [Core]  <!-- UUID: 15639bce-77a4-471c-a42f-29259fcb293b -->

This document contains a Directory of all Instances of the Core Governance Reward Primitive with Instance status of `Completed`.

###### A.6.1.1.8.2.7.1.1.4 - In Progress Invocations Directory [Core]  <!-- UUID: ae8cfca6-f97a-4f93-8c67-904a98a8a59a -->

This document contains a Directory of all prospective Instances of the Core Governance Reward Primitive whose Invocation is currently in progress. Invocations that are completed successfully are moved to [A.6.1.1.8.2.7.1.1.2 - Active Instances Directory](e76c0b88-7755-4611-a884-9b5bd3d9c4d8), whereas failed Invocations are Archived in [A.6.1.1.8.2.7.1.1.5 - Hub Data Repository](5eb6faea-c685-450c-a9ba-601ce68ac690).

###### A.6.1.1.8.2.7.1.1.5 - Hub Data Repository [Core]  <!-- UUID: 5eb6faea-c685-450c-a9ba-601ce68ac690 -->

The documents herein contain the Data Repository for the Primitive Hub Document.

###### A.6.1.1.8.2.7.1.1.5.1 - Archived Invocations/Instances [Core]  <!-- UUID: 5507a84c-0ff2-47c0-b1cc-9d469586051a -->

The subtrees for archived Invocations and Instances of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.8.2.7.1.1.5.1.1 - Failed Invocations [Core]  <!-- UUID: c63f8814-ba44-424f-bb68-9b38ecbfd31e -->

The subtrees for failed Invocations of the Core Governance Reward Primitive are stored here.

###### A.6.1.1.8.2.7.1.1.5.1.2 - Suspended Instances [Core]  <!-- UUID: d81d6ff9-e211-497d-801f-3a785db803e3 -->

The subtrees for Instances of the Core Governance Reward Primitive with `Suspended` Status are stored here.

##### A.6.1.1.8.2.7.1.2 - Active Instances [Core]  <!-- UUID: 746a2e0b-fd99-41de-84cc-61c8f85efb1a -->

The Instances of the Core Governance Reward Primitive with `Active` Status are stored herein.

##### A.6.1.1.8.2.7.1.3 - Completed Instances [Core]  <!-- UUID: 621b7986-b265-41d6-8b03-bee449211d3d -->

The Instances of the Core Governance Reward Primitive with `Completed` Status are stored herein.

##### A.6.1.1.8.2.7.1.4 - In Progress Invocations [Core]  <!-- UUID: bf457701-f952-4ec5-a2bc-ab356d3e65e2 -->

The in progress Invocations of the Core Governance Reward Primitive are contained herein. Once an Invocation is successfully completed, its subtree will be moved to [A.6.1.1.8.2.7.1.2 - Active Instances](746a2e0b-fd99-41de-84cc-61c8f85efb1a).

## A.6.1.1.8.3 - Omni Documents [Core]  <!-- UUID: dfb235e1-40fd-4ba1-afd8-e8524acbc077 -->

The documents herein define Launch Agent 7's strategic intent and operational processes relating to infrastructure inherited from Sky Core, activities unrelated to Sky Primitives, or activities spanning multiple Sky Primitives.

### A.6.1.1.8.3.1 - Governance Information Unrelated To Root Edit Primitive [Core]  <!-- UUID: c18d1d28-3b1f-4173-87dd-f697ab2d2539 -->

The documents herein specify Launch Agent 7 governance information that is unrelated to the use of the Root Edit Primitive. The governance process for updating the Launch Agent 7 Artifact is specified in the Root Edit Primitive above at [A.6.1.1.8.2.2.2 - Root Edit Primitive](526f3ff3-e9d5-4de3-a7d7-60baf979e471).

#### A.6.1.1.8.3.1.1 - Sky Forum [Core]  <!-- UUID: e0096e14-8d6d-4ad0-8f4d-91f418271cea -->

Launch Agent 7 uses the Sky Forum for governance-related discussion. Posts should use the “Launch Agent 7 Prime” category.

#### A.6.1.1.8.3.1.2 - Sky Ecosystem Emergency Response [Core]  <!-- UUID: e9af6855-1271-412c-9667-983bd6efc613 -->

The documents herein specify Launch Agent 7's emergency response protocol in situations that impact the entire Sky Ecosystem. This protocol will be specified in a future iteration of the Launch Agent 7 Artifact.

#### A.6.1.1.8.3.1.3 - Agent-Specific Emergency Response [Core]  <!-- UUID: 3581ec81-e5bb-44d1-a44c-56c0a327b361 -->

The documents herein specify Launch Agent 7's emergency response protocol in situations solely impacting Launch Agent 7 versus the broader Sky Ecosystem. This protocol will be specified in a future iteration of the Launch Agent 7 Artifact.
