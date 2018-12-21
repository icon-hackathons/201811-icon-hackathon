package com.nomad.dice.payload.roll;

import lombok.Data;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Data
public class RollRequest {

    @NotNull
    private Long houseHashId;

    @NotBlank
    private String houseHash;
}
