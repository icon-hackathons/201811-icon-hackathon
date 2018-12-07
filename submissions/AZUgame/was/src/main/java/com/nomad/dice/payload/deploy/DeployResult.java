package com.nomad.dice.payload.deploy;

import foundation.icon.icx.data.Bytes;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
public class DeployResult {

    private String scoreAddress;
    private String txHash;

    @Builder
    public DeployResult(String scoreAddress, Bytes txHash) {
        this.scoreAddress = scoreAddress;
        this.txHash = txHash.toString();
    }
}
