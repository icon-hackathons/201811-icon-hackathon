package com.nomad.dice.payload;

import lombok.Builder;
import lombok.Data;

@Data
public class ApiResponse {

    private Boolean success;

    private String message;

    @Builder
    public ApiResponse(Boolean success, String message) {
        this.success = success;
        this.message = message;
    }
}
