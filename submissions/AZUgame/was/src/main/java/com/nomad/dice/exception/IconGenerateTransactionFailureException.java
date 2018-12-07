package com.nomad.dice.exception;

import lombok.Builder;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.INTERNAL_SERVER_ERROR)
public class IconGenerateTransactionFailureException extends RuntimeException {

    @Builder
    public IconGenerateTransactionFailureException(String message, Throwable cause) {
        super(String.format("%s; Caused by: '%s'", message, cause.toString()));
    }
}
