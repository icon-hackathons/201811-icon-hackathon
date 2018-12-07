package com.nomad.dice.payload.deploy;

import lombok.Builder;
import lombok.Data;

import javax.validation.constraints.Positive;
import javax.validation.constraints.PositiveOrZero;
import java.math.BigInteger;

@Data
public class DeployScoreRequest {

    @PositiveOrZero
    private BigInteger roleUnderMin;

    @Positive
    private BigInteger roleUnderMax;

    @PositiveOrZero
    private BigInteger betMin;

    @Positive
    private BigInteger betMax;

    @Builder
    public DeployScoreRequest(BigInteger roleUnderMin, BigInteger roleUnderMax, BigInteger betMin, BigInteger betMax) {
        this.roleUnderMin = roleUnderMin;
        this.roleUnderMax = roleUnderMax;
        this.betMin = betMin;
        this.betMax = betMax;
    }
}
