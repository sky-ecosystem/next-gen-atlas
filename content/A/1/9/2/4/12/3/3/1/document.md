---
id: 2662dc31-d68b-4b63-91d9-8ca420632eb2
docNo: A.1.9.2.4.12.3.3.1
name: Spell Validators Should Validate Executive Document
type: Core
depth: 9
childType: sections_and_primary_docs
---

###### A.1.9.2.4.12.3.3.1 - Spell Validators Should Validate Executive Document [Core]

The Spell validator should confirm that the smart contract developers referenced the correct governance copy when building the Spell and that the document voters see on the Voting Portal matches the Spell contents. This is done by verifying that the hash in the Spell corresponds to the version of the Executive Document stored in the GitHub repository.

To perform this validation, the validator must first locate the Executive Hash, which can be found on the voting platform under "Spell Details" for the Executive Vote. Validators should be aware that the hash refers to an earlier commit of the Executive Document markdown, prior to the inclusion of the contract address. After validating the hash against this earlier commit, validators must conduct a diff check between the commit associated with the Executive Hash and the final version of the document to confirm that the only difference is the replacement of the Spell address placeholder.

The check can be performed in two ways:

1. Using an Online Tool:
    - Copy and paste the body of the Executive Document from GitHub into the online Keccak-256 hash generator tool ([https://emn178.github.io/online-tools/keccak_256.html](https://emn178.github.io/online-tools/keccak_256.html)).
    - Compare the generated hash with the hash included in the Spell.
2. Using `cast`
    - Generate the hash directly from the raw GitHub URL at the specific commit:
        - Run the following command to generate the hash: `cast keccak -- "$(wget $RAW_EXEC_URL -O -)"`
        - Use the raw file URL at the specific commit.
    - Compare the generated hash with the hash included in the Spell.
