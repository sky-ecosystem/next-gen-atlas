---
id: 12c126be-0535-4147-a17e-91f670ad8339
docNo: A.1.9.2.4.7.2.5
name: Tests Must Pass Before Crafter Provides Spell to Reviewers
type: Core
depth: 8
childType: sections_and_primary_docs
---

###### A.1.9.2.4.7.2.5 - Tests Must Pass Before Crafter Provides Spell to Reviewers [Core]

Before marking a spell’s Pull Request as "ready for review", the Crafter must ensure that both continuous integration tests and locally run tests are all passing successfully. The only exception to this rule is when the continuous integration tests are broken at no fault of the Spell Team - due to a GitHub failure or otherwise - in which case the spell can be marked as "ready for review" if locally run tests are passing. The Crafter must not remove or disable failing tests in order to bypass this rule.
