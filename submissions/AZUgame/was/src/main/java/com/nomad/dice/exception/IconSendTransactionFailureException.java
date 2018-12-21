package com.nomad.dice.exception;

import lombok.Builder;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

import java.math.BigInteger;

@ResponseStatus(value = HttpStatus.INTERNAL_SERVER_ERROR)
public class IconSendTransactionFailureException extends RuntimeException {

    private BigInteger code;
    private String message;

    @Builder
    public IconSendTransactionFailureException(BigInteger code, String message) {
        super(String.format("{\"CODE\":%s,\"MESSAGE\":\"%s\"}", code, message));
        this.code = code;
        this.message = message;
    }
}
