---
id: 53ff94d4-d7b5-4696-a66e-f6102deef3ac
docNo: A.6.1.1.2.2.6.1.2.2.3.1
name: Remove Compromised Relayer As Freezer
type: Core
depth: 12
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.3.1 - Remove Compromised Relayer As Freezer [Core]

In the event of a compromised Relayer, the `FREEZER_ROLE` can call the function to `removeRelayer` from the Controller contract. This function takes an address, and then the Freezer can remove the compromised Relayer, thereby preventing it from doing any harm to the system. The backstop relayer can then take over. This function should only be used if the keys to the relayer multisig have been leaked or compromised, and the relayer is now in the hands of an external bad actor.

`mainnetController.removeRelayer(compromisedRelayer)`
