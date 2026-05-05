---
id: 93dddb43-1d2e-4ea8-ab18-eb0518a193ba
docNo: A.6.1.1.1.3.2.2.1.1
name: Conditions For The Pre-launch Token Rewards
type: Core
depth: 10
childType: sections_and_primary_docs
---

###### A.6.1.1.1.3.2.2.1.1 - Conditions For The Pre-launch Token Rewards [Core]

Spark has a pre-launch token rewards program based on the usage of its lending platform. Users of the platform will receive an airdrop of SPK tokens, depending on how much and how long they have used the platform during the pre-launch token reward period. These rewards are only for users on Ethereum Mainnet.

There are two seasons of the Spark pre-launch token rewards: Season 1 and Season 2.

Season 1 of pre-launch token rewards was active from August 20 2023 and lasted for nine months, ending on May 20 2024. 130,434,783 SPK tokens were allocated in this period.

In Season 2 14,478,261 SPK will be rewarded per month to SparkLend users who qualify for the airdrop.

Season 2 is an additional pre-farming period, which runs until the Spark Agent launches as part of Sky Endgame launch season.

The monthly SPK rewards are allocated as follows:

- 80 % is allocated to users borrowing DAI and/or USDS
- 20 % is allocated to users supplying ETH

The proposed full anti-cheat SPK Airdrop for SparkLend is calculated using the following formula:

`Airdrop = 80% * (DAI Borrows + USDS Borrows - sDAI Supplies * sDAI Liquidation Threshold - sUSDS Supplies * sUSDS Liquidation Threshold) + 20% * (ETH Supplies - ETH Borrows / ETH Liquidation Threshold)`

All supplies and borrows are denominated in USD based on the on-chain oracle price at that block to determine the conversion.
