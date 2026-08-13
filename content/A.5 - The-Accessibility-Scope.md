# A.5 - The Accessibility Scope [Scope]  <!-- UUID: 99b1b47d-3c7a-4859-ac00-8c0849f9070e -->

The Accessibility Scope governs accessibility and distribution efforts, and regulates user-facing frontends.

## A.5.1 - Brand Identity [Article]  <!-- UUID: 580a0254-4406-4e30-a148-123ac71507fd -->

This Article governs the brand identity of Sky.

### A.5.1.1 - Brand Identity [Section]  <!-- UUID: ccb424f7-af2c-45eb-a702-5586fd783b44 -->

This Section defines the management and use of Sky’s brand identity.

#### A.5.1.1.1 - Website And Domain [Core]  <!-- UUID: ff80ab10-5b93-4eb2-a347-937e6ee0c625 -->

The IP rights of the Sky website must be transferred to an entity similar to the Dai Foundation.

#### A.5.1.1.2 - Dai [Core]  <!-- UUID: fa6e009c-d487-4b32-a5c1-109bff7a6ff0 -->

Dai must remain as a valid token and product, with no actively maintained brand presence beyond community assets, educational material and its token name.

## A.5.2 - Accessibility Communication Channels [Article]  <!-- UUID: e47feeb0-2b82-4908-aa5b-2c78e0c21d68 -->

This Article regulates accessibility assets, including communication channels and Sky’s communication presence on external websites.

### A.5.2.1 - Accessibility Communication Channels [Section]  <!-- UUID: 8942c3c7-61bd-4cf6-a3f5-4366290801b4 -->

This Section defines rules for managing accessible communication channels to enhance public access to, and interaction with, the Sky Ecosystem. These communication channels are distinct from Sky’s governance-focused communication channels.

#### A.5.2.1.1 - External Platforms [Core]  <!-- UUID: a4a1d3b4-fdcc-41ec-9af6-f501376599a0 -->

Sky must support the accessibility of the Sky Ecosystem by paying Ecosystem Actors to maintain accounts and channels on external platforms, such as Twitter and Telegram. These accounts may develop and share Accessibility content that follows the brand guidelines.

#### A.5.2.1.2 - Moderation [Core]  <!-- UUID: 005b77d2-d3c8-4b6d-8722-b86a18aba2e6 -->

Accessibility Communication channels are subject to the moderation policies specified in [A.2.7.1.2 - Moderation](be3da4c5-6882-4694-9ccd-3fa7c5f6e09a).

#### A.5.2.1.3 - Budget [Core]  <!-- UUID: 985891a2-71e0-4e45-a004-f31e6fd72281 -->

The Accessibility communication channel budget is available to maintain the tasks described in [A.5.2.1 - Accessibility Communication Channels](8942c3c7-61bd-4cf6-a3f5-4366290801b4) and its subdocuments.

##### A.5.2.1.3.1 - Amount [Core]  <!-- UUID: 65625a56-0d3e-45b3-958d-0517fd861bd2 -->

The Accessibility communication channel budget is:

- 0 USDS per month, implemented with DssVest.

It is a monthly recurring budget.

## A.5.3 - Accessibility Campaigns [Article]  <!-- UUID: 8b12566b-31d0-4b87-818b-3949cd1a2f74 -->

This Article regulates accessibility campaigns.

### A.5.3.1 - Accessibility Campaigns [Section]  <!-- UUID: 332d3fb0-2d8b-4b5e-aac4-8cdd2659c4ca -->

This Section defines infrastructure and processes pertaining to accessibility campaigns.

#### A.5.3.1.1 - Early Bird Reward [Core]  <!-- UUID: 88c9f2dc-1963-419b-852b-204e13f377be -->

As a part of the brand reveal phase, the Accessibility Facilitators set up an Early Bird Reward System. The Early Bird Reward System rewarded all users signing up before the launch date of USDS and SKY with double the SKY rewards for the first month following launch.

The accumulated SKY rewards were paid out as an airdrop as specified in [A.5.3.1.1.1 - Token Distribution](eaf8cf29-90fd-4b9b-b0a8-02ce8386908c).

##### A.5.3.1.1.1 - Token Distribution [Core]  <!-- UUID: eaf8cf29-90fd-4b9b-b0a8-02ce8386908c -->

To distribute the Early Bird Reward the following actions have been or will be taken:

- 27,222,832.8 newly minted SKY, equal to 120% of the total estimated Early Bird Reward distributions, was transferred to the multisig wallet operated by the Accessibility Facilitators at the address `0x14D98650d46BF7679BBD05D4f615A1547C87Bf68` on the Ethereum Mainnet.
- The remaining SKY in the `0x14D98650d46BF7679BBD05D4f615A1547C87Bf68` multisig that is not used to fund the MerkleDistributor will be burned by calling the `burn` function on the multisig. The estimated amount of SKY needed to fund the MerkleDistributor is 22,685,694.

## A.5.4 - Location Resilience [Article]  <!-- UUID: c8ed0b06-2be7-4651-9982-91cea0622519 -->

This Article defines the location-filtering rules applicable to Ecosystem Actors that operate Frontends on behalf of Agents; and Ecosystem Actors that operate Frontends and receive Distribution Rewards.

### A.5.4.1 - Location Resilience [Section]  <!-- UUID: 396e9ea2-c964-43be-9164-edb302ab62cf -->

This Section defines requirements for Ecosystem Actors and Agents to implement limited filtering and full blocking of IPs.

#### A.5.4.1.1 - Reduce Exposure To Locations [Core]  <!-- UUID: 58f85237-4d1d-424b-be03-6eea1e8a8d0d -->

Ecosystem Actors in the Sky Ecosystem must actively explore and implement reasonably available options to reduce their infrastructure's exposure to locations identified in the following subdocuments as subject to either IP filtering ("limited filtering") or IP blocking ("full block").

#### A.5.4.1.2 - Consequence For Non-Compliance [Core]  <!-- UUID: b93c94ed-34dd-4269-808d-58ce180a7103 -->

All frontends operated by Ecosystem Actors on behalf of Agents are required to follow the location-filtering rules defined in [A.5.4.1 - Location Resilience](396e9ea2-c964-43be-9164-edb302ab62cf) and its subdocuments. The failure to adhere to these rules will result in penalties.

#### A.5.4.1.3 - Limited Filtering Of Features & IPs [Core]  <!-- UUID: eac552cb-4c8d-4a79-bb8c-cfbe264b880f -->

Limited filtering requires frontends operated by Ecosystem Actors to avoid displaying or describing features to users with IPs flagged for limited filtering.

##### A.5.4.1.3.1 - Restricted Features [Core]  <!-- UUID: 8dc8867d-61cc-4143-a09f-d6035ade5a4a -->

The features that must be restricted from being displayed or described to users flagged for Limited Filtering are:

- Staking Rewards
- Sky Savings Rate
- Any other feature related to yield or rewards.

##### A.5.4.1.3.2 - Flagged IPs [Core]  <!-- UUID: db9e3649-3ccb-4cc4-aede-78ca1d870101 -->

Frontends must develop internal processes to determine their strategy for limited filtering, to ensure optimal balance of resilience and accessibility.

#### A.5.4.1.4 - Full Block [Core]  <!-- UUID: bd6fa353-4f61-4834-887a-37db9f5c8416 -->

Full block requires frontends operated by Ecosystem Actors to deny service of any kind to users with IPs flagged for Full Block.

##### A.5.4.1.4.1 - Flagged IPs [Core]  <!-- UUID: e6b9065e-8dd7-4f23-b7e4-4e3d2736bee4 -->

User IPs flagged for Full Block are:

- Cuba
- Iran
- Syria
- North Korea
- Afghanistan
- Belarus
- Burma
- Russia
- Venezuela
- Crimea and Sevastopol
- Donetsk People’s Republic
- Luhansk People’s Republic of Ukraine
- Kherson Oblast
- Zaporizhzhia Oblast
