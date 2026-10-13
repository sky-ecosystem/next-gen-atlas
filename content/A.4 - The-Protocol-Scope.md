# A.4 - The Protocol Scope [Scope]  <!-- UUID: 5c20d9af-0bb9-4ca1-a944-1e2cb6f8bb6b -->

The Protocol Scope regulates the maintenance and development of the core Sky Protocol and its critical, non-collateral components. The Protocol Scope defines all rules for protocol engineering.

## A.4.1 - Core Tokens [Article]  <!-- UUID: e5089a2a-22b0-47fd-b0c2-a93017a2c71a -->

The two core tokens, USDS and SKY, play the central role in the usability and tokenomics of the Sky Ecosystem.

### A.4.1.1 - USDS [Section]  <!-- UUID: 7e356a45-3d05-4125-9fd7-d3d454e54cdb -->

USDS is the Stablecoin product of the Sky Protocol. It is designed to remain stable against USD, and its supply is regulated through the Peg Stability Module and the Allocation System, as governed by the Stability Scope.

#### A.4.1.1.1 - USDS Launch [Core]  <!-- UUID: 3e00cf4d-8b10-4182-bb3d-08b63bc55aeb -->

In the Endgame Token Launch Phase, USDS was launched as an upgrade to Dai, offering new features, including Token Rewards. Dai can be exchanged to and from USDS at a rate of 1:1.

##### A.4.1.1.1.1 - Gnosis Payment [Core]  <!-- UUID: 8f721d05-6f9b-4efe-b737-18f634f9703d -->

Sky has agreed to compensate Gnosis for the difference between the Sky Savings Rate and the Dai Savings Rate on xDai balances for the period between March 1, 2025 and October 28, 2025.

The amount of this payment is 1,806,670 USDS and the recipient address on the Ethereum Mainnet is `0x849d52316331967b6ff1198e5e32a0eb168d039d`. This payment should be included in the next available Executive Vote as determined by the Core Facilitator and is authorized to proceed directly to an Executive Vote without a prior Governance Poll.

###### A.4.1.1.1.1.1 - Transfer Of USDS To Gnosis [Core]  <!-- UUID: 418d496b-2e2e-4ee2-b37a-8178de5d656c -->

The payment authorized in this document was made from the Surplus Buffer to the recipient address in one (1) transfer of 1,806,670 USDS, included in the November 27, 2025 Executive Vote.

### A.4.1.2 - SKY [Section]  <!-- UUID: 8e505278-67d9-4c89-afe4-992d5d846fb8 -->

SKY is the governance token of the Sky Protocol. It grants voting rights in the Sky Governance system. Its liquidity is boosted by the Smart Burn Engine, as governed by the Stability Scope.

#### A.4.1.2.1 - MKR To SKY Upgrade [Core]  <!-- UUID: 6bb8b5b2-a2a8-4728-bddb-28bf054de9b6 -->

Historically, MKR was the governance token of the Sky Protocol. As part of the transition to the Endgame, the technical infrastructure of the Sky Protocol was upgraded to use SKY as its governance token rather than MKR.

##### A.4.1.2.1.1 - MKR To SKY Upgrade Approval [Core]  <!-- UUID: eaa5f1ae-f336-49f8-b5d3-7bb01984ba0e -->

**MKR holders have voted to approve the deprecation of MKR as the governance token of the Sky Protocol with full knowledge of the changes being proposed. See **[**https://vote.makerdao.com/polling/QmcZNZg3**](https://vote.makerdao.com/polling/QmcZNZg3)**. This deprecation includes all actions defined in **[**A.4.1.2.1 - MKR To SKY Upgrade**](6bb8b5b2-a2a8-4728-bddb-28bf054de9b6)**, including, but not limited to, the removal of voting rights from MKR and the Delayed Upgrade Penalty**.

##### A.4.1.2.1.2 - MKR To SKY Conversion Contract [Core]  <!-- UUID: 0a26f6d0-1b50-4015-b094-499724796f9e -->

The MKR to SKY conversion contract MKR_SKY allows users to upgrade from MKR to SKY at a conversion rate of 1 MKR to 24,000 SKY, subject to the Delayed Upgrade Penalty specified in [A.4.1.2.1.3 - MKR To SKY Upgrade Penalty](ec820ddb-5d12-43d8-81b7-a7602a70332a).

##### A.4.1.2.1.3 - MKR To SKY Upgrade Penalty [Core]  <!-- UUID: ec820ddb-5d12-43d8-81b7-a7602a70332a -->

In the September 18, 2025 Executive Vote, the Delayed Upgrade Penalty for the MKR to SKY conversion contract was set to 1%. The Delayed Upgrade Penalty is increased via an Executive Vote by one (1) percentage point every three (3) months thereafter.

###### A.4.1.2.1.3.1 - Current Value [Core]  <!-- UUID: 2b209018-e632-47a4-bc1b-11c5d101c952 -->

The current value of the Delayed Upgrade Penalty can be read from the MKR to SKY conversion contract MKR_SKY, as specified in [A.4.1.2.1.2 - MKR To SKY Conversion Contract](0a26f6d0-1b50-4015-b094-499724796f9e), located on the Ethereum Mainnet at `0xA1Ea1bA18E88C381C724a75F23a130420C403f9a`, by calling the `fee` function [https://etherscan.io/address/0xA1Ea1bA18E88C381C724a75F23a130420C403f9a#readContract#F1](https://etherscan.io/address/0xA1Ea1bA18E88C381C724a75F23a130420C403f9a#readContract#F1).

#### A.4.1.2.2 - Deflationary Tokenomics [Core]  <!-- UUID: c72ca16f-14d1-4aca-978e-ba9efe6d80bc -->

The documents herein set forth the core deflationary tokenomics of the SKY token.

##### A.4.1.2.2.1 - Initial Token Supply [Core]  <!-- UUID: fd196f2c-c36f-479f-9254-c03c8886b559 -->

The initial token supply of SKY tokens is derived from the total number of legacy MKR tokens as of the launch of Sky, multiplied by the conversion ratio of 24,000. SKY is the exclusive governance token of the Sky Protocol and takes over all governance and economic rights previously held by MKR. See [A.4.1.2.1 - MKR To SKY Upgrade](6bb8b5b2-a2a8-4728-bddb-28bf054de9b6).

##### A.4.1.2.2.2 - No New Token Emissions [Core]  <!-- UUID: 60519e2c-77f7-43ed-8eb4-a7b138bebf2d -->

No new SKY tokens may be emitted except for (1) emissions required to recapitalize the protocol if it is at risk of insolvency (see [A.3.6 - SKY Backstop](4d8b0d82-97da-4041-b185-4b98c2779cbe)) and (2) temporary emissions that are being deprecated and fully offset by corresponding burns, resulting in no net increase to the intended long-term token supply (see [A.4.1.2.2.4 - Deprecated Emissions Mechanisms](2f3962e4-c79e-4583-82df-31239dfb84a4)).

##### A.4.1.2.2.3 - Burning Of Existing Tokens [Core]  <!-- UUID: 5b94d42a-28fa-40fa-8948-ba3113a4d5b8 -->

At the same time that no new SKY tokens are issued, SKY tokens are bought back and burned on a regular basis, using a portion of the Net Revenue of the Protocol as dictated by the Treasury Management Function. See [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121). As a result, the total supply of SKY tokens will continue to decrease over time.

##### A.4.1.2.2.4 - Deprecated Emissions Mechanisms [Core]  <!-- UUID: 2f3962e4-c79e-4583-82df-31239dfb84a4 -->

The subdocuments herein define legacy mechanisms involving the issuance of new SKY tokens. Each of these mechanisms has been deprecated. While these mechanisms did not increase the net supply of SKY tokens, they have been replaced with solutions that do not involve any emissions of SKY tokens, as defined in the documents herein.

###### A.4.1.2.2.4.1 - SKY Token Rewards Emissions [Core]  <!-- UUID: 8189e776-d631-44a0-81e5-3b2d5d88ef54 -->

USDS users may be able to earn SKY Rewards. See [A.4.3.2 - Token Reward Mechanism](3ff5a7b2-db91-41ab-be19-ddb068b36cc7). These rewards were previously funded by emissions of new SKY tokens.

These ongoing emissions were eliminated and replaced with a solution that funds these rewards using SKY held by the Sky Protocol.

At the same time that this new solution was implemented, SKY tokens equal to the total SKY emissions previously used to fund SKY Rewards, including the Early Bird Reward (see [A.5.3.1.1.1 - Token Distribution](eaf8cf29-90fd-4b9b-b0a8-02ce8386908c)), were burned from SKY held by the Sky Protocol.

The combination of these actions achieved a state where the number of total SKY tokens is exactly the same as if SKY Rewards had never been funded with protocol emissions.

###### A.4.1.2.2.4.2 - MKR To SKY Conversion Emissions [Core]  <!-- UUID: 676636df-729d-46e3-bf34-89d0d33e8051 -->

The legacy MKR to SKY conversion contract (Legacy Conversion Contract) burned MKR and minted new SKY. The new MKR to SKY conversion contract (New Conversion Contract) instead burns MKR and issues SKY from the existing supply of preminted SKY.

The Legacy Conversion Contract was disabled as specified in [A.4.1.2.2.4.2.1 - Disabling Legacy Conversion Contract](1b8248bf-5d88-4d67-8c4a-21981a0aa937). To offset SKY minted by the Legacy Conversion Contract after the deployment of the New Conversion Contract, an equivalent amount of preminted SKY was burned. This action ensured the total SKY token supply remains as if these specific emissions from the Legacy Conversion Contract had not occurred.

###### A.4.1.2.2.4.2.1 - Disabling Legacy Conversion Contract [Core]  <!-- UUID: 1b8248bf-5d88-4d67-8c4a-21981a0aa937 -->

The disabling of the Legacy Conversion Contract was executed in the June 26, 2025 Executive Vote.

## A.4.2 - SkyLink [Article]  <!-- UUID: f6d2bae6-7ebc-42cd-a507-900f4bcfb98f -->

SkyLink is a multichain system that enables native crosschain transfer of Sky Ecosystem-related tokens to other blockchains, including Ethereum L2s and major L1s.

### A.4.2.1 - Multichain Support Native Mechanisms [Section]  <!-- UUID: 9538d851-c874-4eba-9efd-0c3e0f29a0d4 -->

SkyLink deployments support features including the Savings Rate Mechanism (including sUSDS), the Token Rewards Mechanism and the SKY Staking Mechanism.

### A.4.2.2 - SkyLink Bridges [Section]  <!-- UUID: bd68f60c-f2dc-4c0e-9209-ba5aa20b6f2f -->

The documents herein define the LayerZero-based SkyLink bridges deployed by the Sky Ecosystem, as well as shared security infrastructure across these bridges.

#### A.4.2.2.1 - Ethereum SkyLink Freezer Multisig [Core]  <!-- UUID: 21fa6749-6209-4280-9b5f-b2a73d400421 -->

The Ethereum SkyLink Freezer Multisig has the ability to freeze SkyLink bridges deployed in the Sky Ecosystem from Ethereum Mainnet.

##### A.4.2.2.1.1 - Ethereum SkyLink Freezer Multisig Address [Core]  <!-- UUID: 4192a2f6-a660-476d-bbb8-677a78b1c3a3 -->

The address of the Ethereum SkyLink Freezer Multisig on the Ethereum Mainnet is `0x38d1114b4cE3e079CC0f627df6aC2776B5887776`.

##### A.4.2.2.1.2 - Ethereum SkyLink Freezer Multisig Required Number Of Signers [Core]  <!-- UUID: 861347b3-320f-48fb-ab9a-e9030cb9e44f -->

The Ethereum SkyLink Freezer Multisig has a 2/5 signing requirement.

##### A.4.2.2.1.3 - Ethereum SkyLink Freezer Multisig Signers [Core]  <!-- UUID: 2a86809e-8b34-4692-92fe-bcb75b00ce6d -->

The signers of the Ethereum SkyLink Freezer Multisig are two (2) addresses controlled by the Core Facilitator and three (3) addresses controlled by Core GovOps.

##### A.4.2.2.1.4 - Ethereum SkyLink Freezer Multisig Usage Standards [Core]  <!-- UUID: c0337114-d46d-436f-892d-4f6feb192b29 -->

The Ethereum SkyLink Freezer Multisig can only be used in urgent or emergency situations (e.g., potential code exploits). Such situations are characterized by the fact that 1) they have the potential to harm the Sky Ecosystem or its users; and 2) the preparation time required for an Executive Vote would leave the ecosystem vulnerable to harm (e.g., an exploit).

The multisig should be used to prevent technical vulnerabilities; prevent unwanted functionality of the smart contracts or corresponding parts of the system (e.g., price oracles); or prevent unwanted usage of the smart contracts or corresponding parts of the system which deviates from intended behavior.

The Core Council must ensure that use of the multisig is generally aligned and specifically accords with these requirements.

##### A.4.2.2.1.5 - Ethereum SkyLink Freezer Multisig Modification [Core]  <!-- UUID: af5b97be-bf52-431d-8fa9-9b1c6164e328 -->

The Core Facilitator and Core GovOps can change the signers of the Ethereum SkyLink Freezer Multisig so long as:

- there are five (5) signers;
- two (2) signers are required to execute transactions;
- two (2) signers are controlled by the Core Facilitator; and
- three (3) signers are controlled by Core GovOps.

#### A.4.2.2.2 - Solana SkyLink Bridge [Core]  <!-- UUID: 56593663-55e5-45d5-8682-5eede11aa14a -->

Sky uses a SkyLink bridge to securely move assets between Ethereum Mainnet and Solana, as well as to provide governance controls for Sky-issued tokens on Solana.

##### A.4.2.2.2.1 - Introduction [Core]  <!-- UUID: 1157a0cd-9acc-4149-9258-d7f8946df475 -->

The Solana SkyLink Bridge consists of both a Token Bridge that allows bridging USDS between Ethereum Mainnet and Solana as well as a Governance Bridge that allows exercising governance control for Sky-issued tokens on Solana.

##### A.4.2.2.2.2 - Deployment [Core]  <!-- UUID: 593095a6-aec4-4ca5-9c2e-87ce748ac198 -->

The Solana SkyLink Bridge was deployed in two phases. The first phase occurred in the November 13, 2025 Executive Vote and the second phase occurred in the November 17, 2025 Out-Of-Schedule Executive Vote.

##### A.4.2.2.2.3 - Security Parameters [Core]  <!-- UUID: 2cf3dc2e-2a2a-4f8a-a959-611e5654a29c -->

The documents herein define the security parameters of the Solana SkyLink Bridge.

###### A.4.2.2.2.3.1 - Freezer Multisigs [Core]  <!-- UUID: d70d5580-760f-4441-9f93-7494e0d05808 -->

The Solana SkyLink Bridge can be frozen from Ethereum Mainnet by the Ethereum SkyLink Freezer Multisig as specified in [A.4.2.2.1 - Ethereum SkyLink Freezer Multisig](21fa6749-6209-4280-9b5f-b2a73d400421). The document herein defines the Solana-side freezer multisig.

###### A.4.2.2.2.3.1.1 - Solana SkyLink Freezer Multisig [Core]  <!-- UUID: 8e618196-257a-49d8-834d-665dba345fcd -->

The Solana SkyLink Freezer Multisig has the ability to freeze the Solana SkyLink Bridge from Solana.

###### A.4.2.2.2.3.1.1.1 - Solana SkyLink Freezer Multisig Address [Core]  <!-- UUID: bb0b31dd-f68c-4ea1-b36e-ceda655bee7d -->

The address of the Solana SkyLink Freezer Multisig on Solana is `5hARLsT1VA2AmuGL2AXUeSyyFG6o2Fcpb9S6aKXNsbeK`.

###### A.4.2.2.2.3.1.1.2 - Solana SkyLink Freezer Multisig Required Number Of Signers [Core]  <!-- UUID: f376a4da-0818-4d13-a496-25451577fe32 -->

The Solana SkyLink Freezer Multisig has a 2/4 signing requirement.

###### A.4.2.2.2.3.1.1.3 - Solana SkyLink Freezer Multisig Signers [Core]  <!-- UUID: a9f95fb4-690e-43c2-a231-b8705d62036d -->

The signers of the Solana SkyLink Freezer Multisig are two (2) addresses controlled by Operational GovOps Soter Labs and two (2) addresses controlled by Operational Facilitator Endgame Edge.

###### A.4.2.2.2.3.1.1.4 - Solana SkyLink Freezer Multisig Usage Standards [Core]  <!-- UUID: 9f845d09-4304-4aa7-8bd0-2dda747e52e6 -->

The Solana SkyLink Freezer Multisig can only be used in urgent or emergency situations (e.g., potential code exploits). Such situations are characterized by the fact that 1) they have the potential to harm the Sky Ecosystem or its users; and 2) the preparation time required for an Executive Vote would leave the ecosystem vulnerable to harm (e.g., an exploit).

The multisig should be used to prevent technical vulnerabilities; prevent unwanted functionality of the smart contracts or corresponding parts of the system (e.g., price oracles); or prevent unwanted usage of the smart contracts or corresponding parts of the system which deviates from intended behavior.

The Core Council must ensure that use of the multisig is generally aligned and specifically accords with these requirements.

###### A.4.2.2.2.3.1.1.5 - Solana SkyLink Freezer Multisig Modification [Core]  <!-- UUID: b70ebff7-355c-46c2-bc36-f08561c5ded1 -->

Operational GovOps Soter Labs and Operational Facilitator Endgame Edge can change the signers of the Solana SkyLink Freezer Multisig so long as:

- there are four (4) signers;
- two (2) signers are required to execute transactions; and
- an equal number of signers are controlled by Operational GovOps Soter Labs and Operational Facilitator Endgame Edge.

###### A.4.2.2.2.3.2 - Rate Limits [Core]  <!-- UUID: 36626f77-52da-4bb6-9e32-851420133922 -->

The documents herein define the rate limits for the Solana SkyLink Bridge.

###### A.4.2.2.2.3.2.1 - Rate Limit Accounting [Core]  <!-- UUID: 7c0eeee4-ce0d-45fe-8eab-1be501e367c0 -->

The Solana SkyLink Bridge uses net accounting.

Net accounting means that the rate limit applies to the net amount of tokens transferred from one side of the bridge to the other. For example, if 25,000,000 USDS were transferred from Ethereum Mainnet to Solana and 15,000,000 USDS were transferred from Solana to Ethereum Mainnet, the net amount transferred would be 10,000,000 USDS.

###### A.4.2.2.2.3.2.2 - Rate Limit [Core]  <!-- UUID: 8414b48b-932e-430e-a236-727807fd73ba -->

The Solana SkyLink Bridge currently has a rate limit of 5,000,000 USDS per day. This limit should be gradually increased over time as the bridge becomes more mature.

The rate limit for the Solana SkyLink Bridge may be modified by the Core Facilitator, in consultation with the Core Council Risk Advisor, through the Operational Weekly Cycle. Such modifications can be effected directly via an Executive Vote, without requiring a prior Governance Poll.

###### A.4.2.2.2.3.3 - Validators [Core]  <!-- UUID: 6d04b42a-9e3c-4490-840a-dbe98388ee78 -->

The documents herein specify the selection and configuration of validators for the Solana SkyLink Bridge.

###### A.4.2.2.2.3.3.1 - Token Bridge [Core]  <!-- UUID: 16b49e7d-7360-41bf-ae7a-3c7380972987 -->

The documents herein specify the selection and configuration of validators for the Token Bridge component of the Solana SkyLink Bridge.

###### A.4.2.2.2.3.3.1.1 - Validators [Core]  <!-- UUID: ffb71c51-44cc-4b9e-ae50-ee6975d7bc31 -->

The validators for the Token Bridge are LayerZero and Nethermind.

###### A.4.2.2.2.3.3.1.2 - Quorum Requirement [Core]  <!-- UUID: 30a6d20d-fd23-4fa1-96a6-494b044c023e -->

The quorum requirement for the Token Bridge is 2/2.

###### A.4.2.2.2.3.3.2 - Governance Bridge [Core]  <!-- UUID: 07d43b8c-1230-4de9-959b-8593d69e922a -->

The documents herein specify the selection and configuration of validators for the Governance Bridge component of the Solana SkyLink Bridge.

###### A.4.2.2.2.3.3.2.1 - Validators [Core]  <!-- UUID: 0939f4bf-93d2-4d32-859f-ae4cfdff33b4 -->

The validators for the Governance Bridge are LayerZero, Nethermind, Canary, Deutsche Telekom, P2P, Horizen, and Luganodes.

###### A.4.2.2.2.3.3.2.2 - Quorum Requirement [Core]  <!-- UUID: c5850a58-948d-4c19-bf7f-ba2644cd5001 -->

The quorum requirement for the Governance Bridge is 4/7.

#### A.4.2.2.3 - Avalanche SkyLink Bridge [Core]  <!-- UUID: 6b0eaa0d-d2d3-44b6-b2d4-9344efbf453b -->

Sky uses a SkyLink bridge to securely move assets between Ethereum Mainnet and Avalanche C-Chain ("Avalanche"), as well as to provide governance controls for Sky-issued tokens on Avalanche.

##### A.4.2.2.3.1 - Introduction [Core]  <!-- UUID: b71e1dec-357c-4009-a11d-e236667e4086 -->

The Avalanche SkyLink Bridge consists of a Token Bridge that allows bridging USDS and sUSDS between Ethereum Mainnet and Avalanche, as well as a Governance Bridge that allows exercising governance control for Sky-issued tokens on Avalanche.

##### A.4.2.2.3.2 - Deployment [Core]  <!-- UUID: 1c0d2cf1-dc44-4b7f-b709-61fcc5c1612c -->

The Avalanche SkyLink Bridge was deployed in the April 9, 2026 Executive Vote.

##### A.4.2.2.3.3 - Security Parameters [Core]  <!-- UUID: 413852e0-23b8-4630-a8a1-de0d9018c482 -->

The documents herein define the security parameters of the Avalanche SkyLink Bridge.

###### A.4.2.2.3.3.1 - Freezer Multisigs [Core]  <!-- UUID: 199661f2-b3d9-4308-a5d9-9ed15880b00d -->

The Avalanche SkyLink Bridge can be frozen from Ethereum Mainnet by the Ethereum SkyLink Freezer Multisig as specified in [A.4.2.2.1 - Ethereum SkyLink Freezer Multisig](21fa6749-6209-4280-9b5f-b2a73d400421). The document herein defines the Avalanche-side freezer multisig.

###### A.4.2.2.3.3.1.1 - Avalanche SkyLink Freezer Multisig [Core]  <!-- UUID: 0b1162f6-6a30-4a30-b693-68e077093e7c -->

The Avalanche SkyLink Freezer Multisig has the ability to freeze the Avalanche SkyLink Bridge from Avalanche.

###### A.4.2.2.3.3.1.1.1 - Avalanche SkyLink Freezer Multisig Address [Core]  <!-- UUID: 3f9645b2-ae99-4c6a-a49a-dfe39ead218c -->

The address of the Avalanche SkyLink Freezer Multisig on Avalanche is `0x4deb1B5372dd3271691A9E80bCBfd98F5aa27f30`.

###### A.4.2.2.3.3.1.1.2 - Avalanche SkyLink Freezer Multisig Required Number Of Signers [Core]  <!-- UUID: 542e7e15-da27-488b-a192-baaa4ec1a9b9 -->

The Avalanche SkyLink Freezer Multisig has a 2/5 signing requirement.

###### A.4.2.2.3.3.1.1.3 - Avalanche SkyLink Freezer Multisig Signers [Core]  <!-- UUID: 22d693e8-4dd9-4673-ba8a-a372069cee43 -->

The signers of the Avalanche SkyLink Freezer Multisig are two (2) addresses controlled by Operational GovOps Soter Labs, two (2) addresses controlled by Operational Facilitator Endgame Edge, and one (1) address controlled by Prime Agent Grove.

###### A.4.2.2.3.3.1.1.4 - Avalanche SkyLink Freezer Multisig Usage Standards [Core]  <!-- UUID: 8596233b-db6e-4787-b601-32d4f5f0393f -->

The Avalanche SkyLink Freezer Multisig can only be used in urgent or emergency situations (e.g., potential code exploits). Such situations are characterized by the fact that 1) they have the potential to harm the Sky Ecosystem or its users; and 2) the preparation time required for an Executive Vote would leave the ecosystem vulnerable to harm (e.g., an exploit).

The multisig should be used to prevent technical vulnerabilities; prevent unwanted functionality of the smart contracts or corresponding parts of the system (e.g., price oracles); or prevent unwanted usage of the smart contracts or corresponding parts of the system which deviates from intended behavior.

The Core Council must ensure that use of the multisig is generally aligned and specifically accords with these requirements.

###### A.4.2.2.3.3.1.1.5 - Avalanche SkyLink Freezer Multisig Modification [Core]  <!-- UUID: 8514341b-bbce-4e6e-a9c4-e41519cac67c -->

Operational GovOps Soter Labs, Operational Facilitator Endgame Edge, and Prime Agent Grove can change the signers of the Avalanche SkyLink Freezer Multisig so long as:

- there are five (5) signers;
- two (2) signers are required to execute transactions;
- two (2) signers are controlled by Operational GovOps Soter Labs;
- two (2) signers are controlled by Operational Facilitator Endgame Edge; and
- one (1) signer is controlled by Prime Agent Grove.

###### A.4.2.2.3.3.2 - Rate Limits [Core]  <!-- UUID: 2fb5eb69-2f10-4173-8d26-36890db8fe83 -->

The documents herein define the rate limits for the Avalanche SkyLink Bridge.

###### A.4.2.2.3.3.2.1 - Rate Limit Accounting [Core]  <!-- UUID: 49041287-546d-48bb-b85d-8ec48960d2f8 -->

The Avalanche SkyLink Bridge uses net accounting.

Net accounting means that the rate limit applies to the net amount of tokens transferred from one side of the bridge to the other. For example, if 5,000,000 USDS were transferred from Ethereum Mainnet to Avalanche and 3,000,000 USDS were transferred from Avalanche to Ethereum Mainnet, the net amount transferred would be 2,000,000 USDS.

###### A.4.2.2.3.3.2.2 - USDS Rate Limit [Core]  <!-- UUID: 6d550b28-1299-456f-879b-9f66dd8085a6 -->

The Avalanche SkyLink Bridge currently has a USDS rate limit of 0 USDS per day.

The rate limit for the Avalanche SkyLink Bridge may be modified by the Core Facilitator, in consultation with the Core Council Risk Advisor, through the Operational Weekly Cycle. Such modifications can be effected directly via an Executive Vote, without requiring a prior Governance Poll.

###### A.4.2.2.3.3.2.3 - sUSDS Rate Limit [Core]  <!-- UUID: 186450c7-25a8-4a4e-a945-3366e9d65b13 -->

The Avalanche SkyLink Bridge currently has no rate limit for sUSDS. A rate limit for sUSDS may be set or subsequently modified by the Core Facilitator, in consultation with the Core Council Risk Advisor, through the Operational Weekly Cycle. Such changes can be effected directly via an Executive Vote, without requiring a prior Governance Poll.

###### A.4.2.2.3.3.3 - Validators [Core]  <!-- UUID: 483d9616-cde4-490a-9291-766733b83de4 -->

The documents herein specify the selection and configuration of validators for the Avalanche SkyLink Bridge.

###### A.4.2.2.3.3.3.1 - Token Bridge [Core]  <!-- UUID: 3a3bcbb1-0989-4d62-80c3-7a71de0b022a -->

The documents herein specify the selection and configuration of validators for the Token Bridge component of the Avalanche SkyLink Bridge.

###### A.4.2.2.3.3.3.1.1 - Validators [Core]  <!-- UUID: a9f87e05-2b53-40e7-b477-ec55136ee95d -->

The validators for the Token Bridge are LayerZero and Nethermind.

###### A.4.2.2.3.3.3.1.2 - Quorum Requirement [Core]  <!-- UUID: 2c6b25de-b2ed-4874-9ab3-2a379cbaf601 -->

The quorum requirement for the Token Bridge is 2/2.

###### A.4.2.2.3.3.3.2 - Governance Bridge [Core]  <!-- UUID: 6a24fd94-9915-468d-a2a4-14f222ff5980 -->

The documents herein specify the selection and configuration of validators for the Governance Bridge component of the Avalanche SkyLink Bridge.

###### A.4.2.2.3.3.3.2.1 - Validators [Core]  <!-- UUID: ae25a37a-9699-4811-93ab-88379227578e -->

The validators for the Governance Bridge are Horizen, LayerZero, Nethermind, Deutsche Telekom, Canary, Luganodes, and P2P.

###### A.4.2.2.3.3.3.2.2 - Quorum Requirement [Core]  <!-- UUID: d1a78b46-a227-4551-9bcd-2a5a6e5d3e56 -->

The quorum requirement for the Governance Bridge is 4/7.

#### A.4.2.2.4 - Plasma SkyLink Bridge [Core]  <!-- UUID: aca54441-3738-4aee-b7a8-f2a4b9ef02fa -->

Sky uses a SkyLink bridge to securely move assets between Ethereum Mainnet and Plasma, as well as to provide governance controls for Sky-issued tokens on Plasma.

##### A.4.2.2.4.1 - Introduction [Core]  <!-- UUID: b8241202-6305-4485-b938-e5e8fe6c2e50 -->

The Plasma SkyLink Bridge consists of a Token Bridge that allows bridging USDS and sUSDS between Ethereum Mainnet and Plasma, as well as a Governance Bridge that allows exercising governance control for Sky-issued tokens on Plasma.

##### A.4.2.2.4.2 - Deployment [Core]  <!-- UUID: 44af823e-841b-4b2e-a4dd-363925a8bf7b -->

The Plasma SkyLink Bridge will be deployed in a future Executive Vote. The timing will be determined by the Core Facilitator in consultation with relevant Ecosystem Actors.

##### A.4.2.2.4.3 - Security Parameters [Core]  <!-- UUID: 0b2674c5-f9e2-4592-9358-c35e06ed5214 -->

The documents herein define the security parameters of the Plasma SkyLink Bridge.

###### A.4.2.2.4.3.1 - Freezer Multisigs [Core]  <!-- UUID: 022129be-e83f-417f-a0b6-4a066fc66d62 -->

The Plasma SkyLink Bridge can be frozen from Ethereum Mainnet by the Ethereum SkyLink Freezer Multisig as specified in [A.4.2.2.1 - Ethereum SkyLink Freezer Multisig](21fa6749-6209-4280-9b5f-b2a73d400421). The document herein defines the Plasma-side freezer multisig.

###### A.4.2.2.4.3.1.1 - Plasma SkyLink Freezer Multisig [Core]  <!-- UUID: f833edaa-9f5f-4445-afcb-a9cfc3620b10 -->

The Plasma SkyLink Freezer Multisig has the ability to freeze the Plasma SkyLink Bridge from Plasma.

###### A.4.2.2.4.3.1.1.1 - Plasma SkyLink Freezer Multisig Address [Core]  <!-- UUID: 88cb9621-d10f-49b6-85e6-2c822bb5beda -->

The address of the Plasma SkyLink Freezer Multisig on Plasma is `0xB3d26eF66F53C9546d1365F417a85B0Aa69049eE`.

###### A.4.2.2.4.3.1.1.2 - Plasma SkyLink Freezer Multisig Required Number Of Signers [Core]  <!-- UUID: cb8707d5-ff3f-4312-b8cc-97b3734fa81c -->

The Plasma SkyLink Freezer Multisig has a 2/5 signing requirement.

###### A.4.2.2.4.3.1.1.3 - Plasma SkyLink Freezer Multisig Signers [Core]  <!-- UUID: f9cd34cb-802e-4322-9307-0e72bb4a4f66 -->

The signers of the Plasma SkyLink Freezer Multisig are three (3) addresses controlled by Operational GovOps Soter Labs, one (1) address controlled by Operational Facilitator Redline Facilitation Group, and one (1) address controlled by Osero.

###### A.4.2.2.4.3.1.1.4 - Plasma SkyLink Freezer Multisig Usage Standards [Core]  <!-- UUID: 5b79ed95-6a02-47dc-8ac1-9ba55b513e32 -->

The Plasma SkyLink Freezer Multisig can only be used in urgent or emergency situations (e.g., potential code exploits). Such situations are characterized by the fact that 1) they have the potential to harm the Sky Ecosystem or its users; and 2) the preparation time required for an Executive Vote would leave the ecosystem vulnerable to harm (e.g., an exploit).

The multisig should be used to prevent technical vulnerabilities; prevent unwanted functionality of the smart contracts or corresponding parts of the system (e.g., price oracles); or prevent unwanted usage of the smart contracts or corresponding parts of the system which deviates from intended behavior.

The Core Council must ensure that use of the multisig is generally aligned and specifically accords with these requirements.

###### A.4.2.2.4.3.1.1.5 - Plasma SkyLink Freezer Multisig Modification [Core]  <!-- UUID: a8be9d0a-629b-4a2c-a2f2-6b2b7f965b16 -->

Operational GovOps Soter Labs, Operational Facilitator Redline Facilitation Group, and Osero can change the signers of the Plasma SkyLink Freezer Multisig so long as:

- there are five (5) signers;
- two (2) signers are required to execute transactions;
- three (3) signers are controlled by Operational GovOps Soter Labs;
- one (1) signer is controlled by Operational Facilitator Redline Facilitation Group; and
- one (1) signer is controlled by Osero.

###### A.4.2.2.4.3.2 - Rate Limits [Core]  <!-- UUID: cc4b7dac-9754-473a-ae3a-bdb0de0a2d88 -->

The documents herein define the rate limits for the Plasma SkyLink Bridge.

###### A.4.2.2.4.3.2.1 - Rate Limit Accounting [Core]  <!-- UUID: 7b6ca79a-66f8-40c8-a76b-4497ddc6518f -->

The Plasma SkyLink Bridge uses net accounting.

Net accounting means that the rate limit applies to the net amount of tokens transferred from one side of the bridge to the other. For example, if 5,000,000 USDS were transferred from Ethereum Mainnet to Plasma and 3,000,000 USDS were transferred from Plasma to Ethereum Mainnet, the net amount transferred would be 2,000,000 USDS.

###### A.4.2.2.4.3.2.2 - USDS Rate Limit [Core]  <!-- UUID: 527a2195-dcfd-4bd2-b20c-d47edf1797b9 -->

The Plasma SkyLink Bridge currently has a USDS rate limit of 5,000,000 USDS per day.

The rate limit for the Plasma SkyLink Bridge may be modified by the Core Facilitator, in consultation with the Core Council Risk Advisor, through the Operational Weekly Cycle. Such modifications can be effected directly via an Executive Vote, without requiring a prior Governance Poll.

###### A.4.2.2.4.3.2.3 - sUSDS Rate Limit [Core]  <!-- UUID: 5c722eb6-22fd-4be4-bb19-4b40159ca007 -->

The Plasma SkyLink Bridge currently has no rate limit for sUSDS. A rate limit for sUSDS may be set or subsequently modified by the Core Facilitator, in consultation with the Core Council Risk Advisor, through the Operational Weekly Cycle. Such changes can be effected directly via an Executive Vote, without requiring a prior Governance Poll.

###### A.4.2.2.4.3.3 - Validators [Core]  <!-- UUID: 84e98241-3071-49d4-9a9d-9006acaef72e -->

The documents herein specify the selection and configuration of validators for the Plasma SkyLink Bridge.

###### A.4.2.2.4.3.3.1 - Token Bridge [Core]  <!-- UUID: 658d9408-ecdd-4279-8f88-d1ed9e6bcd45 -->

The documents herein specify the selection and configuration of validators for the Token Bridge component of the Plasma SkyLink Bridge.

###### A.4.2.2.4.3.3.1.1 - Validators [Core]  <!-- UUID: 07c605cc-9023-457d-aa88-ae9950063f4b -->

The validators for the Token Bridge are LayerZero and Nethermind.

###### A.4.2.2.4.3.3.1.2 - Quorum Requirement [Core]  <!-- UUID: ccdc870c-b61c-4c80-9958-a30f74d2f7af -->

The quorum requirement for the Token Bridge is 2/2.

###### A.4.2.2.4.3.3.2 - Governance Bridge [Core]  <!-- UUID: 6aea3973-59ed-4f64-ad7f-4d1ad53e4357 -->

The documents herein specify the selection and configuration of validators for the Governance Bridge component of the Plasma SkyLink Bridge.

###### A.4.2.2.4.3.3.2.1 - Validators [Core]  <!-- UUID: b314c96f-45c9-4726-967e-66153c0a8a0c -->

The validators for the Governance Bridge are Canary, Deutsche Telekom, Horizen, LayerZero, Luganodes, Nethermind, and P2P.

###### A.4.2.2.4.3.3.2.2 - Quorum Requirement [Core]  <!-- UUID: 8b278dd8-e0c5-4f08-97be-dc9cce9f0680 -->

The quorum requirement for the Governance Bridge is 4/7.

## A.4.3 - Savings Rate And Token Reward Mechanism [Article]  <!-- UUID: c64a37d4-08a8-41bb-beae-4e976b6d0982 -->

This Article regulates the rewards benefiting Dai users and USDS users for holding each Stablecoin. DAI users can access the legacy DAI Savings Rate Mechanism. USDS users can access a built-in Savings Rate, and also potentially earn rewards through Token Reward Mechanisms, including SKY and Agent tokens, as specified in the subdocuments herein.

### A.4.3.1 - Savings Rates [Section]  <!-- UUID: 95f2454b-c1c3-476c-b5f8-3f4fead2e2cc -->

The Savings Rate Mechanism includes both the legacy Dai Savings Rate Mechanism and the Sky Savings Rate. The Sky Savings Rate includes a built-in sUSDS mechanism. The Savings Rate is governed by the Stability Scope.

### A.4.3.2 - Token Reward Mechanism [Section]  <!-- UUID: 3ff5a7b2-db91-41ab-be19-ddb068b36cc7 -->

The Token Rewards Mechanism allows USDS users to potentially earn SKY and Agent token rewards as specified in the subdocuments herein.

#### A.4.3.2.1 - SKY Token Rewards [Core]  <!-- UUID: caba97e4-4d4d-4aa9-9ed4-f0d1c8b1c552 -->

SKY token rewards are not currently available to USDS users.

#### A.4.3.2.2 - SPK Token Rewards [Core]  <!-- UUID: 4f56e3a5-7d4d-4da7-9045-d4d88fabc756 -->

SPK token rewards are available to USDS users as specified in [A.2.8.2.2.2.1.2.2.2 - Spark Token Reward Distribution Schedule](1f412288-af14-4aab-84e9-79f2e0c39100).

#### A.4.3.2.3 - GROVE Token Rewards [Core]  <!-- UUID: b2ede2ee-565d-4de9-9c5a-0610e508f0d5 -->

GROVE token rewards are available to USDS users as specified in [A.2.8.2.2.2.1.2.2.1 - Grove Token Reward Distribution Schedule](5b43f4d8-9728-411c-92c7-a7ebaf368ca0).

## A.4.4 - SKY Staking Mechanism [Article]  <!-- UUID: b8891a30-f255-4694-895c-4399df916da3 -->

This Article governs the SKY Staking Mechanism that grants rewards on staked SKY tokens and its associated SKY-backed borrowing mechanism funded via the stUSDS token.

### A.4.4.1 - SKY Staking [Section]  <!-- UUID: 626bd71c-b413-41b7-a5fe-39fd0d43dbf5 -->

SKY holders can stake their tokens via the SKY Staking Mechanism available on Ethereum Mainnet and SkyLink Deployments. SKY stakers earn rewards sourced from the Sky Treasury Management Function. SKY stakers may be able to earn USDS rewards, SKY rewards, and Agent Token Rewards, as determined by Sky Governance. SKY stakers can also borrow USDS against their staked collateral using the SKY-backed borrowing mechanism defined herein.

#### A.4.4.1.1 - SKY Unstaking [Core]  <!-- UUID: e945372c-f526-45b9-af12-135f0eb6e830 -->

SKY stakers can unstake their staked SKY at any time without penalty, provided the SKY is unencumbered by any borrowed USDS.

#### A.4.4.1.2 - SKY Staking Rewards [Core]  <!-- UUID: a98a1bfe-5713-43f5-a8bd-83c5808900b8 -->

The documents herein define the SKY Staking Rewards. SKY stakers may choose between receiving USDS or SKY rewards. Agent Token rewards may also be made available as specified in [A.4.5 - Distribution Of Agent Tokens](e2f1f01f-3303-41c3-b337-f09eb41ba6be).

##### A.4.4.1.2.1 - Sources Of Rewards [Core]  <!-- UUID: e1c77a6a-5b94-4d40-a205-43c703a780e2 -->

SKY stakers are eligible to receive rewards sourced from the Sky Treasury Management Function (TMF) or the Agent Token Distribution mechanism defined in [A.4.5 - Distribution Of Agent Tokens](e2f1f01f-3303-41c3-b337-f09eb41ba6be).

###### A.4.4.1.2.1.1 - Treasury Management Function-Derived Rewards [Core]  <!-- UUID: 6cacdc1c-bdfa-4f68-bdb4-bf31943dcfba -->

USDS rewards and SKY rewards for SKY stakers are funded from the Staking Rewards allocation of the Sky Treasury Management Function (see [A.2.3.1.2.5 - Step 4: Staking Rewards](bb163691-630e-4fda-88f1-96381a649fa0)) and distributed continuously, pro-rata based on the SKY stake of eligible wallets. Distribution parameters are adjusted as specified in [A.2.3.1.4.1 - Staking Rewards Rate Adjustment](de233df4-34cc-4e88-a065-9a9dde9add3c). SKY rewards are funded as specified in [A.4.4.1.2.2.4 - Source Of SKY Rewards](349a350c-c9b7-4232-a83f-2fb49b91fc74) and distributed, at the vesting rate set as specified in [A.2.3.1.4.1 - Staking Rewards Rate Adjustment](de233df4-34cc-4e88-a065-9a9dde9add3c), through the implementation specified in [A.4.4.1.2.2 - SKY Rewards Implementation](ca151bc7-87fc-4749-9776-ea4308817e81).

###### A.4.4.1.2.1.2 - Agent Token Distribution Rewards [Core]  <!-- UUID: 6aa85298-4f1c-4dc5-a973-99bc1e5293d1 -->

SKY stakers may be eligible to receive Agent Token rewards as specified in [A.4.5 - Distribution Of Agent Tokens](e2f1f01f-3303-41c3-b337-f09eb41ba6be). When available, Agent Tokens are distributed continuously, pro‑rata by staked SKY, among wallets that have opted to receive a specific Agent Token. Distribution parameters are updated at each Monthly Settlement Cycle.

##### A.4.4.1.2.2 - SKY Rewards Implementation [Core]  <!-- UUID: ca151bc7-87fc-4749-9776-ea4308817e81 -->

The documents herein specify the implementation and funding of SKY rewards for SKY stakers through the Staking Rewards contract, Rewards Distribution contract, and Vesting Stream contract.

###### A.4.4.1.2.2.1 - Staking Rewards Contract [Core]  <!-- UUID: cf65f0d8-ae2f-45df-80bd-1014ce66509d -->

The Staking Rewards contract is the user facing contract that allows SKY stakers to stake their SKY to receive SKY rewards. It maintains the balance of staked SKY receiving SKY rewards for each user and the associated accumulated rewards balance.

###### A.4.4.1.2.2.1.1 - Staking Rewards Contract Address [Core]  <!-- UUID: b4989cd9-f45e-4747-8861-fac4175624cc -->

The address of the Staking Rewards contract on the Ethereum Mainnet is `0xB44C2Fb4181D7Cb06bdFf34A46FdFe4a259B40Fc`.

###### A.4.4.1.2.2.1.2 - Staking Rewards Contract Parameters [Core]  <!-- UUID: 2bfed9a4-9d7f-4544-b331-5e196a13a108 -->

The parameters of the Staking Rewards contract are specified in the documents herein.

###### A.4.4.1.2.2.1.2.1 - Owner [Core]  <!-- UUID: 3db49535-c663-425d-81b9-3ffa6e2e722d -->

The `owner` of the Staking Rewards contract is the contract that has the ability to control administrative functions for the Staking Rewards contract. The value of the `owner` parameter is the `MCD_PAUSE_PROXY`.

###### A.4.4.1.2.2.1.2.2 - Rewards Distribution Contract Address [Core]  <!-- UUID: 12b11af8-08d6-4b42-a323-cac0a60e78d3 -->

The Rewards Distribution contract address `rewardsDistribution` is the address of the Rewards Distribution contract associated with the Staking Rewards contract. The value of the `rewardsDistribution` parameter is the address of the Rewards Distribution contract specified in [A.4.4.1.2.2.2.1 - Rewards Distribution Contract Address](fdebe206-2f58-4056-8adf-c42dffb47026).

###### A.4.4.1.2.2.1.2.3 - Rewards Token [Core]  <!-- UUID: 9c3bd61a-25ee-43bc-8c93-89142dce6b49 -->

The Rewards Token `rewardsToken` is the token that users receive as rewards. The value of the `rewardsToken` parameter is `SKY`, representing SKY Tokens.

###### A.4.4.1.2.2.1.2.4 - Staking Token [Core]  <!-- UUID: 7e88d6b2-a76b-4aae-a045-bc0eb44d9657 -->

The Staking Token `stakingToken` is the token that users stake to earn rewards. The value of the `stakingToken` parameter is `LSSKY`, representing staked SKY Tokens.

###### A.4.4.1.2.2.2 - Rewards Distribution Contract [Core]  <!-- UUID: 1317764a-d07f-40de-8ff7-f43a3337ca19 -->

The Rewards Distribution contract is the contract that handles the regular transfer of reward tokens from the Vesting Stream contract to the Staking Rewards contract for distribution to end users.

###### A.4.4.1.2.2.2.1 - Rewards Distribution Contract Address [Core]  <!-- UUID: fdebe206-2f58-4056-8adf-c42dffb47026 -->

The address of the Rewards Distribution contract on the Ethereum Mainnet is `0x675671A8756dDb69F7254AFB030865388Ef699Ee`.

###### A.4.4.1.2.2.2.2 - Rewards Distribution Contract Parameters [Core]  <!-- UUID: c13efebc-94fe-408f-93a7-5ee5badb109f -->

The parameters of the Rewards Distribution contract are specified in the documents herein.

###### A.4.4.1.2.2.2.2.1 - Staking Rewards Contract Address [Core]  <!-- UUID: dd30a514-3abb-4e2b-8cc3-03ef2fbf7834 -->

The Staking Rewards contract address `stakingRewards` is the address of the Staking Rewards contract associated with the Rewards Distribution contract. The value of the `stakingRewards` parameter is the address of the Staking Rewards contract specified in [A.4.4.1.2.2.1.1 - Staking Rewards Contract Address](b4989cd9-f45e-4747-8861-fac4175624cc).

###### A.4.4.1.2.2.2.2.2 - Vesting Stream Contract Address [Core]  <!-- UUID: 5348e6c1-13f4-4e5c-8d75-83239ad999ea -->

The Vesting Stream contract address `dssVest` is the address of the Vesting Stream contract associated with the Rewards Distribution contract. The value of the `dssVest` parameter is the address of the Vesting Stream contract specified in [A.4.4.1.2.2.3.1 - Vesting Stream](89155294-6652-481f-938f-a562d5b40e65).

###### A.4.4.1.2.2.3 - Vesting Stream Contract [Core]  <!-- UUID: 21a8978d-10a5-4151-b99a-ca8115fe0a6d -->

The Vesting Stream contract manages various vesting streams that vest SKY Tokens from the Protocol Treasury. One of these vesting streams regularly vests SKY Tokens to the Staking Rewards contract.

###### A.4.4.1.2.2.3.1 - Vesting Stream [Core]  <!-- UUID: 89155294-6652-481f-938f-a562d5b40e65 -->

The address of the Vesting Stream contract is the address corresponding to the `MCD_VEST_SKY_TREASURY` key in the Chainlog.

###### A.4.4.1.2.2.3.2 - Vesting Stream Contract Parameters [Core]  <!-- UUID: 148e2c86-0f30-49c1-923c-9b32f92aa40f -->

The parameters of the vesting stream managed by the Vesting Stream contract that vests SKY Tokens to the Staking Rewards contract are specified in the documents herein.

###### A.4.4.1.2.2.3.2.1 - Vesting Duration [Core]  <!-- UUID: 9cad1b65-5dea-4510-a1cd-c47eddb66309 -->

The Vesting Duration `vestTau` is the total duration over which the Vesting Total number of tokens are to be vested linearly.

###### A.4.4.1.2.2.3.2.2 - Vesting Total [Core]  <!-- UUID: 8bc59b3a-5bf4-4e2c-a793-b51a4ff58ef6 -->

The Vesting Total `vestTot` is the number of rewards tokens to be vested in total over the Vesting Duration.

###### A.4.4.1.2.2.3.3 - Vesting Stream Parameter Modification [Core]  <!-- UUID: 7da0cd7a-238f-400f-89a7-a419ed25ce37 -->

The Core Facilitator, in consultation with the Core Council Risk Advisor, may modify the parameters of the vesting stream to achieve the target reward rate as specified in [A.2.3.1.4.1 - Staking Rewards Rate Adjustment](de233df4-34cc-4e88-a065-9a9dde9add3c). Such modifications can be effected directly via an Executive Vote, without a prior Governance Poll.

###### A.4.4.1.2.2.4 - Source Of SKY Rewards [Core]  <!-- UUID: 349a350c-c9b7-4232-a83f-2fb49b91fc74 -->

SKY rewards distributed through the Vesting Stream contract are funded by SKY acquired through Smart Burn Engine buybacks attributable to the SKY Staking Rewards share specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121). The `vestTot` and `vestTau` parameters are set accordingly.

###### A.4.4.1.2.2.4.1 - Authorization Of Transfer By Sky Frontier Foundation [Core]  <!-- UUID: 2789177b-5bc7-486f-8aab-75ea16e21035 -->

Sky Governance hereby confirms that the transfer of 500,000,000 SKY tokens to initially fund SKY rewards for SKY stakers is consistent with the terms of the grant to the Sky Frontier Foundation. See [A.2.13.1 - Ecosystem Entity Grants](5d5759e4-8077-4af5-9a1a-eaeab5088dd7).

##### A.4.4.1.2.3 - USDS Rewards Implementation [Core]  <!-- UUID: 75784a6a-c6e2-4f74-a92c-dd1ac4f8f124 -->

USDS rewards for SKY stakers are distributed through the USDS rewards contract at the address corresponding to the `REWARDS_LSSKY_USDS` key in the Chainlog. The contract is funded directly by the Splitter Module from the share of Step 3 Capital allocated to USDS Staking Rewards, as specified in [A.2.3.1.4 - Implementation](f67a5780-11d5-4014-8254-795080c77133). Its `rewardsDuration` parameter is maintained equal to the Splitter Module's `hop` parameter as specified in [A.3.5.2 - Smart Burn Engine Parameters](ddb90fee-2851-4bf0-b924-f1d73e30ce7a).

#### A.4.4.1.3 - SKY-Backed Borrowing [Core]  <!-- UUID: 264b1787-cd75-4d28-9c14-c7d5a724eba7 -->

SKY stakers can borrow USDS against their staked SKY collateral. This borrowing will be facilitated exclusively by the stUSDS system which will provide protocol-independent, or segregated, risk capital. The stUSDS elements are outlined in the subdocuments below.

##### A.4.4.1.3.1 - stUSDS Function [Core]  <!-- UUID: f81ed4c8-ccfc-492a-b8f8-6f284158d8c3 -->

stUSDS is a yield-bearing token representing USDS deposited into the stUSDS contract. Its primary function is to provide segregated risk capital for the SKY-backed borrowing mechanism. Users convert USDS to stUSDS to provide this capital and earn the stUSDS Rate. See [A.4.4.1.3.2 - stUSDS Rate](7e51d5a7-0707-4fba-999b-a1becd5f0192). stUSDS can be converted back to USDS subject to available unutilized liquidity in the stUSDS converter contract.

##### A.4.4.1.3.2 - stUSDS Rate [Core]  <!-- UUID: 7e51d5a7-0707-4fba-999b-a1becd5f0192 -->

The stUSDS Rate (`str`) is the variable yield earned by stUSDS holders. The stUSDS Rate is the rate in effect as set by Sky Governance. Sky Governance may set the stUSDS Rate directly through an Executive Vote, or through the stUSDS BEAM Operators, which act on behalf of Sky Governance (see [A.4.4.1.3.8.4 - Operators](8fd15f15-c8cd-480d-86b7-cad524cfa9f1)).

The stUSDS Rate is set together with the SKY Borrow Rate as specified in [A.4.4.1.3.8.5 - Update Process](7e58f5eb-c339-4f04-aca8-681e9acd0752).

##### A.4.4.1.3.3 - stUSDS Holders’ Risk Bearing [Core]  <!-- UUID: 60a37c03-9122-4ef6-9669-2466c335224c -->

Holders of stUSDS accept the risk associated with providing capital for SKY-backed borrowing. In the event that the liquidation of a borrower’s staked SKY collateral does not cover the outstanding debt, stUSDS balances will be subject to a haircut proportional to the shortfall. This mechanism ensures that the Sky Protocol is isolated from losses originating from the SKY-backed borrowing facility.

##### A.4.4.1.3.4 - Debt Ceiling [Core]  <!-- UUID: f7c00726-64a0-4ba5-8c0d-231d0e27e54c -->

The Debt Ceiling is the maximum amount of USDS that can be borrowed against staked SKY. It is determined dynamically and is equal to the lower of (1) the `line` parameter set through the stUSDS BEAM and (2) the total value of stUSDS (the USDS owed to stUSDS holders, including accrued yield) less the debt currently in liquidation auctions, or zero if that difference is negative.

##### A.4.4.1.3.5 - SKY Borrow Rate [Core]  <!-- UUID: 5e546766-a0c0-4744-9ca9-5509db14bc30 -->

The SKY Borrow Rate (`duty`) is the interest rate charged to borrowers against staked SKY. The SKY Borrow Rate is the rate in effect as set by Sky Governance. Sky Governance may set the SKY Borrow Rate directly through an Executive Vote, or through the stUSDS BEAM Operators, which act on behalf of Sky Governance (see [A.4.4.1.3.8.4 - Operators](8fd15f15-c8cd-480d-86b7-cad524cfa9f1)).

###### A.4.4.1.3.5.1 - Rate Setting Mechanism [Core]  <!-- UUID: 5ad3e32c-9b5c-431a-bc20-e236194b65e8 -->

The SKY Borrow Rate is set by Sky Governance, together with the stUSDS Rate, as specified in [A.4.4.1.3.8.5 - Update Process](7e58f5eb-c339-4f04-aca8-681e9acd0752). The SKY Borrow Rate should not be lower than the SKY Borrow Minimum Rate (see [A.4.4.1.3.5.2 - SKY Borrow Minimum Rate](6e329dd6-eda5-43ce-9899-b3a03ede8d0b)).

###### A.4.4.1.3.5.2 - SKY Borrow Minimum Rate [Core]  <!-- UUID: 6e329dd6-eda5-43ce-9899-b3a03ede8d0b -->

The SKY Borrow Minimum Rate is calculated according to the following formula:

`SKY Borrow Minimum Rate = Sky Savings Rate + stUSDS Distribution Reward`

The formula ensures the SKY Borrow Minimum Rate covers the baseline cost of capital (Sky Savings Rate) plus the incentive cost (stUSDS Distribution Reward), preventing value-draining arbitrage where users could borrow below the Sky Savings Rate.

###### A.4.4.1.3.5.2.1 - Parameters Definition [Core]  <!-- UUID: 63e86a25-18f6-4810-a362-d2831781ea2c -->

The parameters of the SKY Borrow Minimum Rate formula are further defined in the documents herein.

###### A.4.4.1.3.5.2.1.1 - Sky Savings Rate Definition [Core]  <!-- UUID: 27839098-86b9-479f-87b7-ffd467c825c8 -->

`Sky Savings Rate` is defined in [A.3.1.2.2 - Sky Savings Rate](2674cccb-d779-4868-b83f-8cb86648c88a).

###### A.4.4.1.3.5.2.1.2 - stUSDS Distribution Reward Definition [Core]  <!-- UUID: a61d98e3-ca01-4945-ba76-46955be3631c -->

`stUSDS Distribution Reward` is defined in [A.4.4.1.3.7 - stUSDS Distribution Reward](673676d8-62a4-4422-b870-fbcdb3c0aabd).

##### A.4.4.1.3.6 - stUSDS Risk Parameters [Core]  <!-- UUID: fac38a01-4c67-4810-af22-3e7b2d855567 -->

The liquidation parameters for SKY-backed loans funded via stUSDS are:

- Liquidation Ratio: 120%
- `Calc`: StairstepExponentialDecrease
- `Tau`: 0 days
- `Tolerance`: 0.5
- `Cut`: 0.99
- `Step`: 60 seconds
- `Buf`: 120%
- `Cusp`: 40%
- `Tail`: 6,000 seconds
- `Chip`: 0.1%
- `Stopped`: 3
- `Tip`: 300 USDS
- `Chop`: 13%
- `Hole`: 250,000
- `Dust`: 30,000

###### A.4.4.1.3.6.1 - Modification Of stUSDS Risk Parameters [Core]  <!-- UUID: 1aa35c85-6a96-4921-a6f0-87a58f3d57d6 -->

Except as specified in [A.4.4.1.3.6.1.1 - Modification Of stUSDS Auction Parameters](0296f17f-b615-4f93-9505-94bd78c24324), the Core Executor Agents, in consultation with the Core Council Risk Advisor, have the ability to modify any of the parameters defined in [A.4.4.1.3.6 - stUSDS Risk Parameters](fac38a01-4c67-4810-af22-3e7b2d855567). The modification of said parameters is pursuant to the Operational Weekly Cycle and can be effected directly via an Executive Vote, without requiring a Governance Poll.

###### A.4.4.1.3.6.1.1 - Modification Of stUSDS Auction Parameters [Core]  <!-- UUID: 0296f17f-b615-4f93-9505-94bd78c24324 -->

A clear justification and analysis must be provided to validate any proposed changes to the `Calc`, `Tau`, `Buf`, `Cusp`, `Tail`, `Chip`, `Tip`, `Chop`, or `Hole` parameters. Before these changes are added to an Executive Vote, the Core Executor Agents must obtain approval through a Governance Poll. However, in an emergency, the Core Executor Agents have the authority to bypass the Governance Poll and add the proposed parameters directly to an Executive Vote. These parameters must be regularly monitored and updated if needed.

##### A.4.4.1.3.7 - stUSDS Distribution Reward [Core]  <!-- UUID: 673676d8-62a4-4422-b870-fbcdb3c0aabd -->

The stUSDS Distribution Reward is an incentive mechanism, similar to the USDS Distribution Reward, designed to encourage Prime Agents and Integrators to promote stUSDS adoption. See [A.2.2.9.1 - Distribution Reward Primitive](e632c38f-3e4e-4c7e-acfd-b6ec45a422e6). It is calculated as a percentage of the stUSDS balance associated with a Reward Code, initially set at 0.1% in total. The stUSDS Distribution Reward is paid to the Prime Agent, and any sharing with the Integrator is subject to bilateral negotiation between the Prime Agent and the Integrator, as specified in [A.2.2.4.2 - Reward Recipient And Sharing](40395562-d447-4c85-b670-c08d2341bcd2).

##### A.4.4.1.3.8 - stUSDS Bounded External Access Module [Core]  <!-- UUID: 37f8f82e-7239-4cfb-8f95-d2cc40515cd9 -->

The stUSDS Bounded External Access Module (stUSDS BEAM) enables designated, Governance-whitelisted operators to adjust the stUSDS Rate (`str`), the SKY Borrow Rate (`duty`), the maximum amount that users can deposit into the stUSDS contract (`cap`), and the maximum Debt Ceiling (`line`). Adjustments are governed by the stUSDS BEAM smart contract logic and specific parameters set by Sky Governance. stUSDS BEAM holds four parameters that can be set for each stUSDS parameter: (i) `min`, (ii) `max`, (iii) `step`, and (iv) `tau`.

###### A.4.4.1.3.8.1 - Definitions [Core]  <!-- UUID: 2875f146-08b2-4b83-84ed-282af9379762 -->

The documents herein define the parameters of the stUSDS BEAM. The basis-point values of the `min`, `max`, and `step` parameters are expressed as annual percentage yields, as specified in [A.3.1.2.7 - Rate Conventions](154c3b5d-7a87-4dae-85f3-7d26deab9a31).

###### A.4.4.1.3.8.1.1 - Min Definition [Core]  <!-- UUID: f1ed4794-7642-4ce4-ae80-c5f4e2ec0eed -->

The `min` parameter defines the minimum value for the `str` and `duty` parameters that can be set using the stUSDS BEAM. Each of the `str` and `duty` parameters has a specific `min`.

###### A.4.4.1.3.8.1.2 - Max Definition [Core]  <!-- UUID: dbb7b9f3-be84-4eaa-93a0-afe997916ce2 -->

The `max` parameter defines the maximum value for the `str` and `duty` parameters that can be set using the stUSDS BEAM. Each of the `str` and `duty` parameters has a specific `max`.

###### A.4.4.1.3.8.1.3 - Step Definition [Core]  <!-- UUID: 9d4cd92b-7e77-475b-a8f5-245ea29fe344 -->

The `step` parameter limits how much the `str` and `duty` parameters can be increased or decreased in a single transaction, bound by the `tau` parameter. Each of the `str` and `duty` parameters has a specific `step`.

###### A.4.4.1.3.8.1.4 - Max Cap Definition [Core]  <!-- UUID: 2ddd3c5d-7fc3-422c-8a61-03404e182270 -->

The `maxCap` parameter defines the maximum value for the `cap` parameter that can be set by the stUSDS BEAM.

###### A.4.4.1.3.8.1.4.1 - Max Cap Current Value [Core]  <!-- UUID: fca6bbee-6c6f-4e0b-a208-d56b136ce729 -->

The `maxCap` is currently set to 1,000,000,000 USDS.

###### A.4.4.1.3.8.1.5 - Max Line Definition [Core]  <!-- UUID: 96dd5de9-b5ba-4249-bcce-09f598d34019 -->

The `maxLine` parameter defines the maximum value for the `line` parameter that can be set by the stUSDS BEAM.

###### A.4.4.1.3.8.1.5.1 - Max Line Current Value [Core]  <!-- UUID: 3067ff3e-5450-48b7-b8b3-fd671739c6b5 -->

The `maxLine` is currently set to 1,000,000,000 USDS.

###### A.4.4.1.3.8.1.6 - Tau Definition [Core]  <!-- UUID: 4f82fc17-4bcc-4623-b09b-b495c43b06f7 -->

The `tau` parameter defines the minimum time interval, in seconds, that must elapse between consecutive uses or operations of the stUSDS BEAM.

A stUSDS BEAM operation may adjust one or more parameters. Once a stUSDS BEAM operation is executed, the `tau` duration must expire before any subsequent stUSDS BEAM operation can be performed.

###### A.4.4.1.3.8.1.6.1 - Tau Current Value [Core]  <!-- UUID: 9e7e18f3-36b2-497a-817a-2fe9054b8745 -->

The `tau` is currently set to 57,600 seconds (16 hours).

###### A.4.4.1.3.8.2 - stUSDS Parameters [Core]  <!-- UUID: 74b7d8e7-5f55-4760-8f4d-1e5e9bda4279 -->

The stUSDS BEAM parameters for each stUSDS parameter set by the stUSDS BEAM are defined in the subdocuments herein.

###### A.4.4.1.3.8.2.1 - Str BEAM Parameters [Core]  <!-- UUID: 516eccc7-dd7f-4782-84d5-55121bc1ae44 -->

The stUSDS BEAM parameters for the `str` stUSDS parameter are as follows:

- `max` - 5,000 basis points,
- `min` - 200 basis points,
- `step` - 500 basis points.

###### A.4.4.1.3.8.2.2 - Duty BEAM Parameters [Core]  <!-- UUID: 94da2be4-e21c-4de7-8c0c-21e17718d32b -->

The stUSDS BEAM parameters for the `duty` stUSDS parameter are as follows:

- `max` - 5,000 basis points,
- `min` - 210 basis points,
- `step` - 500 basis points.

###### A.4.4.1.3.8.3 - Parameter Adjustments [Core]  <!-- UUID: 91152a4b-6f97-4b8a-831a-0f85c16a78ab -->

All stUSDS BEAM parameters can be modified by Core GovOps, in consultation with the Core Council Risk Advisor. This process will be conducted through the Operational Weekly Cycle or, if necessary, through out-of-schedule Executive Votes.

###### A.4.4.1.3.8.4 - Operators [Core]  <!-- UUID: 8fd15f15-c8cd-480d-86b7-cad524cfa9f1 -->

The stUSDS BEAM Operators are whitelisted entities that can directly alter the stUSDS parameters set by the stUSDS BEAM. The stUSDS BEAM Operators act on behalf of Sky Governance. Changes to stUSDS parameters are limited by the `max`, `min`, `step`, and `tau` parameters. Operators can be added or removed by an Executive Vote.

###### A.4.4.1.3.8.4.1 - Operator Multisig [Core]  <!-- UUID: ee9e13e0-23ca-41a3-a1d1-0f1181882c84 -->

The Operator Multisig is an Operator of the stUSDS BEAM and is controlled by Core GovOps.

###### A.4.4.1.3.8.4.1.1 - Operator Multisig Address [Core]  <!-- UUID: 45679e08-a575-444a-8fae-d7ef6472b073 -->

The address of the Operator Multisig on the Ethereum Mainnet is `0xBB865F94B8A92E57f79fCc89Dfd4dcf0D3fDEA16`.

###### A.4.4.1.3.8.4.1.2 - Operator Multisig Required Number Of Signers [Core]  <!-- UUID: 88438441-b858-4a0a-b1bb-f79cc19e7490 -->

The Operator Multisig currently has a 2/3 signing requirement.

###### A.4.4.1.3.8.4.1.3 - Operator Multisig Signers [Core]  <!-- UUID: a9a7503a-d4e2-474f-bbbe-51b45385a00f -->

The signers of the Operator Multisig are three (3) addresses controlled by Core GovOps.

###### A.4.4.1.3.8.4.1.4 - Operator Multisig Usage Standards [Core]  <!-- UUID: 71e28a28-82b9-43eb-9e93-6aee2d5bbbc0 -->

The signers of the Operator Multisig must use the multisig to operate the stUSDS BEAM in accordance with the process specified in [A.4.4.1.3.8.5.2 - Manual Parameter Updates By Operator Multisig](944c2573-1184-4d6b-bbe9-0b84c11956cf).

###### A.4.4.1.3.8.4.1.5 - Operator Multisig Modification [Core]  <!-- UUID: 303ccb86-1411-409f-a3e4-1193e0aa7b9a -->

Core GovOps can change the signers of the Operator Multisig at any time, so long as there are at least three (3) signers and at least a majority of signers are required to execute transactions.

###### A.4.4.1.3.8.4.2 - Operator Hot Wallet [Core]  <!-- UUID: bddf50ca-02ef-4991-abb0-53e09831ee6f -->

The Operator Hot Wallet is a hot wallet used by the stUSDS Keeper, an automated system that updates stUSDS parameters as specified in [A.4.4.1.3.8.5.3 - Automatic Updates By Operator Hot Wallet](a6e1735f-bd82-4ab6-982b-218013c3455f). The stUSDS Keeper and the Operator Hot Wallet are operated by Ecosystem Actor TechOps Services under the supervision of Core GovOps in consultation with the Core Council Risk Advisor.

###### A.4.4.1.3.8.4.2.1 - Operator Hot Wallet Address [Core]  <!-- UUID: bc29e096-972c-4bcc-b589-dad148374d33 -->

The address of the Operator Hot Wallet on the Ethereum Mainnet is `0x068F9c8F33E13c18B852877A5D8Ec61504971376`.

###### A.4.4.1.3.8.4.3 - Operator Update Process [Core]  <!-- UUID: 64d7e377-9870-4563-a073-768bb7d259a4 -->

stUSDS BEAM Operators can be modified by Core GovOps, in consultation with the Core Council Risk Advisor. This process will be conducted through the Operational Weekly Cycle or, if necessary, through out-of-schedule Executive Votes.

###### A.4.4.1.3.8.5 - Update Process [Core]  <!-- UUID: 7e58f5eb-c339-4f04-aca8-681e9acd0752 -->

Under normal circumstances, the stUSDS parameters set by the stUSDS BEAM are updated automatically by the stUSDS Keeper (see [A.4.4.1.3.8.5.3 - Automatic Updates By Operator Hot Wallet](a6e1735f-bd82-4ab6-982b-218013c3455f)). Core GovOps, in consultation with the Core Council Risk Advisor, may modify or disable the stUSDS Keeper (see [A.4.4.1.3.8.5.4 - Modification And Suspension Of The stUSDS Keeper](7872f3b4-7cfd-459e-8142-4b8988c2f3ad)). The Operator Multisig, in consultation with the Core Council Risk Advisor, may update the stUSDS parameters manually (see [A.4.4.1.3.8.5.2 - Manual Parameter Updates By Operator Multisig](944c2573-1184-4d6b-bbe9-0b84c11956cf)). These processes do not limit the ability of Sky Governance to set the stUSDS parameters via an Executive Vote.

###### A.4.4.1.3.8.5.1 - Initial Parameter Values Set In Executive Vote [Core]  <!-- UUID: 13c51e11-8ea3-4d4e-b631-2e99c559a914 -->

The initial parameters set by the stUSDS BEAM in the Executive Vote deploying stUSDS and the stUSDS BEAM are:

- `str` - 0 basis points
- `duty` - 2,000 basis points
- `cap` - 200,000,000 USDS
- `line` - 200,000,000 USDS

###### A.4.4.1.3.8.5.2 - Manual Parameter Updates By Operator Multisig [Core]  <!-- UUID: 944c2573-1184-4d6b-bbe9-0b84c11956cf -->

The Operator Multisig, in consultation with the Core Council Risk Advisor, may update the stUSDS parameters to the values they determine appropriate.

###### A.4.4.1.3.8.5.2.1 - stUSDS Dashboard [Core]  <!-- UUID: cfd01132-42f2-46c9-867c-bd9aa62bf78a -->

The Core Council Risk Advisor will develop and maintain a stUSDS Dashboard. The stUSDS Dashboard must display the recommended values for each of the stUSDS parameters as of any point in time. The stUSDS Dashboard is located at [https://stusds.herddefi.com/](https://stusds.herddefi.com/).

The recommended values for each of the stUSDS parameters are the outputs of the Interest Rate Model (see [A.4.4.1.3.8.5.3.5 - Interest Rate Model](5a6e8836-cef2-4b2d-b18c-0a9f47ed24fa)) using the meta-parameters published by the Core Council Risk Advisor (see [A.4.4.1.3.8.5.3.2 - Meta-Parameter Values](dd47b41a-e897-49b2-be8f-162c73b034ed)).

###### A.4.4.1.3.8.5.2.2 - Operator Execution [Core]  <!-- UUID: 420d6ca3-405a-41be-ba0f-cdc52746477c -->

In deciding whether and when to make manual changes, the signers of the Operator Multisig, in consultation with the Core Council Risk Advisor, should consider factors including:

- the recommended values displayed in the stUSDS Dashboard;
- the materiality of the change;
- the occurrence of weekends and holidays, including Calendar Exceptions to the Monthly Governance Cycle (see [A.1.12.1 - Calendar Exceptions](6c0810e2-390d-4efb-8b31-f36a7f6e1a05)); and
- such other factors as the signers of the Operator Multisig and the Core Council Risk Advisor deem relevant.

###### A.4.4.1.3.8.5.2.3 - Review By Core Facilitator And Core Council Risk Advisor [Core]  <!-- UUID: 7318d160-e182-4276-bdf9-7dfc86ca77a5 -->

The Core Facilitator and the Core Council Risk Advisor must review the actions of the stUSDS BEAM Operators, including the Operator Hot Wallet and the stUSDS Keeper, on a regular basis and report any concerns to the Core Council.

###### A.4.4.1.3.8.5.3 - Automatic Updates By Operator Hot Wallet [Core]  <!-- UUID: a6e1735f-bd82-4ab6-982b-218013c3455f -->

Under normal circumstances, the stUSDS parameters set by the stUSDS BEAM are set by the stUSDS Keeper using the Operator Hot Wallet (see [A.4.4.1.3.8.4.2 - Operator Hot Wallet](bddf50ca-02ef-4991-abb0-53e09831ee6f)). These changes must be based on the Interest Rate Model (see [A.4.4.1.3.8.5.3.5 - Interest Rate Model](5a6e8836-cef2-4b2d-b18c-0a9f47ed24fa)) and the results must be publicly visible on the stUSDS Dashboard (see [A.4.4.1.3.8.5.2.1 - stUSDS Dashboard](cfd01132-42f2-46c9-867c-bd9aa62bf78a)).

###### A.4.4.1.3.8.5.3.1 - ValueRegistry [Core]  <!-- UUID: c13944f2-9475-4d26-a945-98ed17dc31b9 -->

The stUSDS Keeper reads its meta-parameters from the ValueRegistry, an on-chain contract that stores named values. Sky Governance retains full, direct control over the ValueRegistry at all times, since the Sky Pause Proxy holds ward authorization on it. Meta-parameters can be set and removed only by the ValueRegistry's authorized operator (`bud`), the ValueRegistry Multisig (see [A.4.4.1.3.8.5.3.3 - ValueRegistry Multisig](c1526b15-d55f-4a09-87c4-2f3224ad510e)), using the `setValues` and `removeValues` functions.

The meta-parameters are the inputs the stUSDS Keeper uses to calculate and submit the stUSDS parameters. In the descriptions below, Utilization is the percentage of the USDS in the stUSDS contract that is used to fund borrowing against staked SKY. The meta-parameters are stored under the following keys:

- `STUSDS_OPT_UTIL_WAD` - the target Utilization;
- `STUSDS_DISTRIBUTION_REWARD_WAD` - the distribution reward;
- `STUSDS_BASE_SPREAD_WAD` - the fixed base spread;
- `STUSDS_SPREAD_PCT_WAD` - the share of the SKY Borrow Rate above the base rate that is retained by the stUSDS module;
- `STUSDS_TIME_DRIFT_SPEED_WAD` - the speed at which the SKY Borrow Rate at the target Utilization drifts over time;
- `STUSDS_ABOVE_KINK_MULT_WAD` - the slope multiplier applied above the target Utilization;
- `STUSDS_AVG_UTILIZATION_HOURS` - the number of hours over which Utilization is averaged;
- `STUSDS_CAP_FACTOR_WAD` - the cap factor used to calculate `cap`;
- `STUSDS_LINE_FACTOR_WAD` - the line factor used to calculate `line`;
- `STUSDS_UPDATE_THRESHOLD_BPS` - the smallest change in `str` or `duty`, in basis points, that triggers an update;
- `STUSDS_KEEPER_RERUN_SECONDS` - the scheduled interval, in seconds, between runs of the stUSDS Keeper (a change to a watched ValueRegistry value triggers an immediate run regardless); and
- `STUSDS_KEEPER_ENABLED` - the on-chain submission switch.

###### A.4.4.1.3.8.5.3.1.1 - ValueRegistry Address [Core]  <!-- UUID: 19806417-5def-45f6-8375-a820b33807d3 -->

The address of the ValueRegistry on the Ethereum Mainnet is `0xcDb55A799A9B9eAe22Ed0E13037bb6D2E3f1d080`.

###### A.4.4.1.3.8.5.3.2 - Meta-Parameter Values [Core]  <!-- UUID: dd47b41a-e897-49b2-be8f-162c73b034ed -->

The Core Council Risk Advisor determines the values of the meta-parameters and publishes them, and any subsequent changes, in a dedicated thread on the Sky Forum. Core GovOps must submit the published values to the ValueRegistry using the ValueRegistry Multisig (see [A.4.4.1.3.8.5.3.3 - ValueRegistry Multisig](c1526b15-d55f-4a09-87c4-2f3224ad510e)).

###### A.4.4.1.3.8.5.3.3 - ValueRegistry Multisig [Core]  <!-- UUID: c1526b15-d55f-4a09-87c4-2f3224ad510e -->

The ValueRegistry Multisig is the authorized operator (`bud`) of the ValueRegistry, able to set and remove meta-parameters, and is controlled by Core GovOps.

###### A.4.4.1.3.8.5.3.3.1 - ValueRegistry Multisig Address [Core]  <!-- UUID: 683cd150-cc5e-4cb6-ad12-15866dfc09cd -->

The address of the ValueRegistry Multisig on the Ethereum Mainnet is `0xeB297173377507640A34cab2dD1B7C212087f9B8`.

###### A.4.4.1.3.8.5.3.3.2 - ValueRegistry Multisig Required Number Of Signers [Core]  <!-- UUID: eda1b2aa-77f6-4547-930e-094cb1bf8dc8 -->

The ValueRegistry Multisig currently has a 2/3 signing requirement.

###### A.4.4.1.3.8.5.3.3.3 - ValueRegistry Multisig Signers [Core]  <!-- UUID: c45c408e-886b-4af4-90d2-2a24257a5b37 -->

The signers of the ValueRegistry Multisig are three (3) addresses controlled by Core GovOps.

###### A.4.4.1.3.8.5.3.3.4 - ValueRegistry Multisig Usage Standards [Core]  <!-- UUID: 0b045986-4dcf-4e23-9581-29b2c4ebfa43 -->

The signers of the ValueRegistry Multisig must use the multisig only to submit the meta-parameter values published by the Core Council Risk Advisor, as specified in [A.4.4.1.3.8.5.3.2 - Meta-Parameter Values](dd47b41a-e897-49b2-be8f-162c73b034ed), or to make the changes specified in [A.4.4.1.3.8.5.4 - Modification And Suspension Of The stUSDS Keeper](7872f3b4-7cfd-459e-8142-4b8988c2f3ad).

###### A.4.4.1.3.8.5.3.3.5 - ValueRegistry Multisig Modification [Core]  <!-- UUID: 8741db7b-f326-4066-b88c-fd71d2ff8ea0 -->

Core GovOps can change the signers of the ValueRegistry Multisig at any time, so long as there are at least three (3) signers and at least a majority of signers are required to execute transactions.

###### A.4.4.1.3.8.5.3.4 - On-Chain Submission Switch [Core]  <!-- UUID: 63d71c15-0dfd-43b1-8adf-8b355178aad2 -->

The `STUSDS_KEEPER_ENABLED` meta-parameter determines whether the stUSDS Keeper submits the stUSDS parameters it calculates to the stUSDS BEAM. When it is set to zero (0), the stUSDS Keeper calculates and records the values it would submit without submitting them. When it is set to one (1), the stUSDS Keeper submits them using the Operator Hot Wallet.

###### A.4.4.1.3.8.5.3.5 - Interest Rate Model [Core]  <!-- UUID: 5a6e8836-cef2-4b2d-b18c-0a9f47ed24fa -->

The Interest Rate Model is the model maintained by the Core Council Risk Advisor that the stUSDS Keeper uses to calculate `str`, `duty`, `cap`, and `line` from the state of the stUSDS contract and the meta-parameters recorded in the ValueRegistry (see [A.4.4.1.3.8.5.3.1 - ValueRegistry](c13944f2-9475-4d26-a945-98ed17dc31b9)).

The stUSDS Keeper submits an update when the newly calculated `str` or `duty` differs from its current value by at least the update threshold set in the `STUSDS_UPDATE_THRESHOLD_BPS` meta-parameter and the `tau` period has elapsed since the last update (see [A.4.4.1.3.8.1.6 - Tau Definition](4f82fc17-4bcc-4623-b09b-b495c43b06f7)). When the stUSDS parameters are updated, `cap` and `line` are recalculated and submitted together with `str` and `duty`. All updates are bounded on-chain by the `min`, `max`, `step`, `tau`, `maxCap`, and `maxLine` parameters of the stUSDS BEAM (see [A.4.4.1.3.8.1 - Definitions](2875f146-08b2-4b83-84ed-282af9379762)).

###### A.4.4.1.3.8.5.3.5.1 - Non-Disclosure Of The Interest Rate Model [Core]  <!-- UUID: 6c74b4fe-db22-46a4-b8d3-1ce48b9ce7ae -->

The algorithm of the Interest Rate Model is not publicly disclosed, in order to reduce the possibility of the rate-setting process being gamed. The algorithm was specified by the Core Council Risk Advisor, implemented and tested by Ecosystem Actor Sidestream, and reviewed by the Core Council Risk Advisor. The meta-parameters used by the Interest Rate Model are recorded on-chain in the ValueRegistry and published as specified in [A.4.4.1.3.8.5.3.2 - Meta-Parameter Values](dd47b41a-e897-49b2-be8f-162c73b034ed).

###### A.4.4.1.3.8.5.4 - Modification And Suspension Of The stUSDS Keeper [Core]  <!-- UUID: 7872f3b4-7cfd-459e-8142-4b8988c2f3ad -->

Core GovOps, in consultation with the Core Council Risk Advisor, may modify the algorithm and meta-parameters used by the stUSDS Keeper, including to adopt changes to the Interest Rate Model specified by the Core Council Risk Advisor, or suspend or disable the stUSDS Keeper. This includes setting the `STUSDS_KEEPER_ENABLED` meta-parameter to zero (0) (see [A.4.4.1.3.8.5.3.4 - On-Chain Submission Switch](63d71c15-0dfd-43b1-8adf-8b355178aad2)), directing Ecosystem Actor TechOps Services to stop operating the stUSDS Keeper, or removing the Operator Hot Wallet as an Operator (see [A.4.4.1.3.8.4.3 - Operator Update Process](64d7e377-9870-4563-a073-768bb7d259a4)).

##### A.4.4.1.3.9 - SKY-Backed Borrowing Capped OSM Wrapper [Core]  <!-- UUID: c0fbc4e6-754c-4838-aa27-4ef6226f2769 -->

In order to prevent excessive price spikes if there is high demand for leverage against SKY tokens, which could potentially lead to excessive USDS borrowing against SKY, a wrapper for the SKY OSM contract has been developed.

The wrapper enforces an upper limit on the price of SKY for the purposes of SKY-Backed Borrowing, which is set to be the minimum value of:

1. The current price reported by [A.4.4.1.3.9.1 - SKY Price Oracle](7e9cf614-291d-43a5-984e-4f3366f42052).
2. The `cap` parameter as specified in [A.4.4.1.3.9.2 - Cap Parameter](532ed9cb-51de-4ac2-ade9-58c07b3ea3d5).

###### A.4.4.1.3.9.1 - SKY Price Oracle [Core]  <!-- UUID: 7e9cf614-291d-43a5-984e-4f3366f42052 -->

The SKY Price Oracle is the `PIP_SKY` contract, deployed on Ethereum Mainnet at `0x511485bBd96e7e3a056a8D1b84C5071071C52D6F`, and serves as the SKY price source for SKY-Backed Borrowing. It applies a one (1) hour delay to price updates from the [A.4.4.1.3.9.1.1 - Chronicle Scribe Oracle](cf54c531-4243-4c3b-b0a4-7badf2ea04d6).

###### A.4.4.1.3.9.1.1 - Chronicle Scribe Oracle [Core]  <!-- UUID: cf54c531-4243-4c3b-b0a4-7badf2ea04d6 -->

The Chronicle Scribe Oracle is the contract at the `src` value of `PIP_SKY`, deployed on Ethereum Mainnet at `0xc2ffbbDCCF1466Eb8968a846179191cb881eCdff`. It provides a SKY/USD price aggregated from multiple authorized feeds via multi-signature consensus, without the one (1) hour delay applied by `PIP_SKY`.

###### A.4.4.1.3.9.2 - Cap Parameter [Core]  <!-- UUID: 532ed9cb-51de-4ac2-ade9-58c07b3ea3d5 -->

The subdocuments herein further describe the `cap` parameter and the process for its modification.

###### A.4.4.1.3.9.2.1 - Definition [Core]  <!-- UUID: b65c4542-5fb3-4379-9412-8113f4d2444a -->

The `cap` parameter represents one of the potential inputs for the SKY-Backed Borrowing Capped OSM Wrapper. The OSM wrapper uses the minimum value of the `cap` or the price reported by [A.4.4.1.3.9.1 - SKY Price Oracle](7e9cf614-291d-43a5-984e-4f3366f42052) to determine the price utilized for SKY-backed borrowing.

###### A.4.4.1.3.9.2.2 - Modification [Core]  <!-- UUID: 0d86a609-e432-4312-8989-4e6c1eb9be83 -->

The Core Facilitator, in consultation with the Core Council Risk Advisor, has the ability to modify the `cap` parameter. The modification of said parameter is pursuant to the Operational Weekly Cycle and can be effected directly via an Executive Vote, without requiring a prior Governance Poll.

###### A.4.4.1.3.9.2.3 - Current Value [Core]  <!-- UUID: 161ee404-89b3-43a1-80a9-f387f73c0f6f -->

The current value of the `cap` parameter is:

- 0.025 USDS.

## A.4.5 - Distribution Of Agent Tokens [Article]  <!-- UUID: e2f1f01f-3303-41c3-b337-f09eb41ba6be -->

When Sky invests capital in Agents, the tokens Sky receives in exchange are distributed in accordance with the terms of the Ecosystem Accord between Sky and the respective Agent.

## A.4.6 - Protocol Mechanisms [Article]  <!-- UUID: 635afa14-3a3c-47fb-b338-a3d64f644b69 -->

This Article defines maintenance or housekeeping mechanisms and contracts used to administer the Sky Ecosystem.

### A.4.6.1 - Token Transfers To Sky [Section]  <!-- UUID: 490bc47f-f3fe-4d88-8cc3-be034973fa61 -->

This Section defines standard procedures for sending tokens to Sky.

#### A.4.6.1.1 - Process for Returning Tokens To Sky When No Specific Process Exists [Core]  <!-- UUID: e6807f67-0d3c-4b6a-a3df-6da987147b72 -->

The documents herein define processes for sending tokens to Sky. These include the DssBlow2 contract for adding Dai and USDS to the Surplus Buffer, and the Pause Proxy contract for non-stablecoins.

##### A.4.6.1.1.1 - Transfer Of Stablecoins To Sky Protocol [Core]  <!-- UUID: c2fdee1e-60f4-464c-8d35-3b2bb5f05870 -->

The documents herein define the instructions for transferring stablecoins to Sky.

###### A.4.6.1.1.1.1 - Send Dai Or USDS To DssBlow2 Contract [Core]  <!-- UUID: c4137383-6a3c-4c0d-bf65-a6efab26ce0c -->

Transfers of Dai or USDS that are not required to pay down vault debt should result in an increase to the Sky Protocol Surplus Buffer (see [A.3.5.1 - Surplus Buffer](9782cdc5-c274-45c2-bf4a-690f22c6a294)). This process is handled via the DssBlow2 contract, as described in the subdocuments.

###### A.4.6.1.1.1.1.1 - DssBlow2 [Core]  <!-- UUID: 764ec592-5ff7-462c-9617-759914e1077b -->

Dai or USDS tokens can be transferred to the DssBlow2 contract, MCD_BLOW2, at `0x81EFc7Dd25241acd8E5620F177E42F4857A02B79`. Calling the `blow` function on this contract will cause any Dai or USDS tokens held by it to be added to the Surplus Buffer. During this process, the ERC-20 tokens are burned and the tokens are instead reflected as an internal balance in the MCD_VAT contract.

###### A.4.6.1.1.1.1.1.1 - Unrecoverability Of Non-Dai Or USDS Tokens [Core]  <!-- UUID: 736476a2-1dd3-4ce5-85e2-e003a1e6a1ed -->

Only Dai or USDS are supported by DssBlow2. Any other tokens sent to DssBlow2 are not recoverable by Sky. Senders bear full responsibility; such transfers are not considered a valid receipt of funds owed.

###### A.4.6.1.1.1.2 - Transfer Of Other Stablecoins [Core]  <!-- UUID: 2e2e0d0b-f021-4958-8863-92cca851736f -->

Stablecoins other than Dai or USDS cannot be added to the Surplus Buffer via DssBlow2. They should either (1) be converted to Dai or USDS and sent to DssBlow2 or (2) be sent to the Pause Proxy contract without conversion. Receipt of Dai or USDS is Sky’s preferred method of receiving stablecoins.

##### A.4.6.1.1.2 - Transfer Of Non-Stablecoins To Sky Protocol [Core]  <!-- UUID: 3c8849b2-f2c6-47be-ba54-b99215d9427d -->

The documents herein define the instructions for transferring non-stablecoins to Sky.

###### A.4.6.1.1.2.1 - Send Non-Stablecoins To Pause Proxy [Core]  <!-- UUID: e1bb61ef-6f67-48ed-9b45-88023926607e -->

Transfers of non-stablecoins to Sky should be sent to the Pause Proxy contract.

###### A.4.6.1.1.2.1.1 - Pause Proxy [Core]  <!-- UUID: 8d8cc32d-f724-4eac-bca8-bab0e6d990ba -->

The Pause Proxy Contract, MCD_PAUSE_PROXY, at `0xbe8e3e3618f7474f8cb1d074a26affef007e98fb`, is under the direct control of Sky Governance. Sky Governance may take actions through Executive Votes to interact with the tokens held by the Pause Proxy, including selling these tokens.

### A.4.6.2 - Sky Ecosystem Administrative Contracts [Section]  <!-- UUID: d06315b0-b8ba-4932-925d-0e49a0fe9dd2 -->

This Section defines smart contracts used to administer the Sky Ecosystem.

#### A.4.6.2.1 - SubProxyMethods [Section]  <!-- UUID: 8f422999-13e3-426a-b5ff-19d6c9de30ae -->

The documents herein define the SubProxyMethods contract, covering its purpose, function calls, execution, and the governance process required before it is used.

##### A.4.6.2.1.1 - Purpose [Core]  <!-- UUID: f64e64ae-56b5-4589-adea-cceb4c1e34e1 -->

The SubProxyMethods contract (`SUBPROXY_METHODS`) is a general-purpose helper the Sky Pause Proxy can invoke on any SubProxy via `exec()`, since the Pause Proxy holds ward authorization on it. This means simple, low-risk operations do not require crafting and reviewing a full Agent Spell. Its current function is specified in [A.4.6.2.1.2 - Function Calls](fe6914cc-7f7d-48f8-9fa4-8945d07c1b5f). Additional functions may be added to the contract in the future.

##### A.4.6.2.1.2 - Function Calls [Core]  <!-- UUID: fe6914cc-7f7d-48f8-9fa4-8945d07c1b5f -->

The current SubProxyMethods function, `transfer()`, when called by the Sky Core Spell, moves ERC20 tokens out of the target SubProxy's balance. It is invoked via `delegatecall`, so the transfer executes in the SubProxy's own context.

The SubProxyMethods contract does not itself restrict which destination is specified for a transfer. The destination is determined by the Sky Core Spell.

##### A.4.6.2.1.3 - Execution [Core]  <!-- UUID: 60000393-7e7c-4aa4-928c-30a1a562fa77 -->

A call to the SubProxyMethods contract is included in the Sky Core Spell and executed as specified in [A.1.10.2.4.13 - Spell Execution Process And Retro (Step 13)](761cd866-17a9-47f5-8ae6-ab1788371be1).

Unlike a standard Agent Spell, it is not executed or whitelisted through the Agent's StarGuard contract.

##### A.4.6.2.1.4 - Governance Process [Core]  <!-- UUID: 813a123a-d6e1-4ef2-bc55-716b50732721 -->

The Agent whose SubProxy is acted on via the SubProxyMethods contract must post a request on the Sky Forum authorizing the action. This request must include a reference to the Atlas document authorizing the action for that Agent.
