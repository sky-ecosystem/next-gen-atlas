---
id: fca03c59-2f40-4ac6-8ea6-3f0b89b7660e
docNo: A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.4
name: Build Send Parameters
type: Core
depth: 17
childType: sections_and_primary_docs
---

###### A.6.1.1.2.2.6.1.2.2.1.2.1.2.13.1.4 - Build Send Parameters [Core]

The operator must build the LayerZero `SendParam`. The executor gas limit is set through `OptionsBuilder` with `addExecutorLzReceiveOption`, `dstEid` is set to the `destinationEndpointId`, the recipient is read from `layerZeroRecipients` for that endpoint, `amountLD` is set to the `amount`, and `minAmountLD` is initialized to `0` with empty `composeMsg` and `oftCmd`.

`        bytes memory options = OptionsBuilder.newOptions().addExecutorLzReceiveOption(200_000, 0);

        SendParam memory sendParams = SendParam({
            dstEid       : destinationEndpointId,
            to           : layerZeroRecipients[destinationEndpointId],
            amountLD     : amount,
            minAmountLD  : 0,
            extraOptions : options,
            composeMsg   : "",
            oftCmd       : ""
        });`
