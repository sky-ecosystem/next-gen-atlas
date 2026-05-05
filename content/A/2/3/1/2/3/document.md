---
id: 2b28d464-e683-48ba-9a66-2fee05ea0a88
docNo: A.2.3.1.2.3
name: "Step 2: Aggregate Backstop Capital"
type: Core
depth: 6
childType: sections_and_primary_docs
---

###### A.2.3.1.2.3 - Step 2: Aggregate Backstop Capital [Core]

Step 1 Capital that remains after the Step 1 allocation becomes Step 2 Capital.

The allocation of Step 2 Capital depends on the level of Aggregate Backstop Capital (see [A.3.5.3.1.2 - Aggregate Backstop Capital](6dbead44-5ac4-4c5b-be3c-64eddd004e5c)) relative to the Turbo-Fill Floor (see [A.3.5.3.2.2 - Turbo-Fill Floor](db2aaf07-4ebb-4e5d-ae5e-575717d8fbcd)) and the Target Aggregate Backstop Capital (see [A.3.5.3.2.1 - Target Aggregate Backstop Capital](f73dda95-0b1c-4bdc-b957-469253d27281)).

When Aggregate Backstop Capital is below the Turbo-Fill Floor, fifty percent (50%) of Step 2 Capital is retained to grow Aggregate Backstop Capital. The remainder of Step 2 Capital becomes Step 3 Capital and is allocated as specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121).

When Aggregate Backstop Capital is at or above the Turbo-Fill Floor and below the Target Aggregate Backstop Capital, the portion of Step 2 Capital retained to grow Aggregate Backstop Capital is calculated as fifty percent (50%) multiplied by the fill factor, where the fill factor is one (1) minus the ratio of current Aggregate Backstop Capital to the Target Aggregate Backstop Capital. The remainder of Step 2 Capital becomes Step 3 Capital and is allocated as specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121).

When Aggregate Backstop Capital is at or above the Turbo-Fill Floor and at or above the Target Aggregate Backstop Capital, none of Step 2 Capital is retained; all of Step 2 Capital becomes Step 3 Capital and is allocated as specified in [A.2.3.1.2.4 - Step 3: Smart Burn Engine](5ce73730-4d5d-479c-b01e-40e87f072121).
