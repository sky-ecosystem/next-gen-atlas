---
id: 9b43b664-fcfc-484e-9faa-5ca0ffabd10e
docNo: A.1.9.2.5.3
name: Continuous Approval Voting
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.1.9.2.5.3 - Continuous Approval Voting [Core]

Executive Votes operate under a Continuous Approval Voting mechanism. Voters can support multiple proposals by allocating their SKY vote-weight to each, with the goal of helping a favored proposal surpass the current "hat"—the proposal with the most approval in the DSChief contract. Voters can apply their full SKY vote-weight to up to 5 different proposals simultaneously (as defined by the `max_yays` limit in the contract), rather than splitting their tokens between them. If SKY token holders disagree with a new proposal, they can redirect their SKY vote-weight to the inactive proposal with the highest vote-weight (often the last successfully passed proposal) to maintain the status quo or support an alternative. An active proposal can become the hat if it accumulates more votes than any other, including the current hat, at which point it is "lifted" to become the new hat. This lifting process marks the active proposal, and it may now be scheduled and later executed, provided it meets other conditions like the GSM Pause Delay. There are three key aspects to Continuous Approval Voting:

- Victory threshold set by the hat: The vote-weight on the current hat proposal establishes the "victory threshold" that new proposals must exceed to become eligible for execution. This ensures only the most supported changes advance.
- Dynamic vote-weight movement: Vote-weight can shift from the hat to a new proposal, simultaneously lowering the victory threshold for the hat while boosting the new proposal’s chances. This fluidity allows for real-time community consensus shifts.
- Securing the hat: Vote-weight is encouraged to remain on the hat proposal even after it’s lifted, acting as a security measure against "rogue" or less-supported proposals that might attempt to overtake it with minimal backing.
