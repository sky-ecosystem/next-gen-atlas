---
id: a900623d-15e0-4fc6-a393-bae5da03c139
docNo: A.1.9.2.4.13.4
name: Casting And Execution Of Approved Spell
type: Core
depth: 7
childType: sections_and_primary_docs
---

###### A.1.9.2.4.13.4 - Casting And Execution Of Approved Spell [Core]

Once the current time exceeds the `eta` value set during scheduling, the Spell can be `cast` (see [A.1.9.2.4.13.3 - Execution Setup For Approved Vote](e06f6a83-7c74-4abd-b4da-771cbfdf2fb9)). Casting and the subsequent execution path occur atomically within the same transaction. This entire process is permissionless, meaning any Ethereum address can trigger the execution without requiring special permissions.
