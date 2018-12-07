package com.nomad.dice;

import foundation.icon.icx.Call;
import foundation.icon.icx.Transaction;
import foundation.icon.icx.TransactionBuilder;
import foundation.icon.icx.data.Address;
import foundation.icon.icx.transport.jsonrpc.RpcItem;
import foundation.icon.icx.transport.jsonrpc.RpcObject;

import java.math.BigInteger;

public interface CallScore {

    Address getScoreAddress();

    BigInteger getNetworkId();

    default Transaction buildTransaction(Address address, String function, RpcObject params) {
        return buildTransaction(address, function, params, new BigInteger("87000000", 16));
    }

    default Transaction buildTransaction(Address address, String function, RpcObject params, BigInteger stepLimit) {
        long timestamp = System.currentTimeMillis() * 1000L;
        return TransactionBuilder.newBuilder()
                .nid(getNetworkId())
                .from(address)
                .to(getScoreAddress())
                .stepLimit(stepLimit)
                .timestamp(new BigInteger(Long.toString(timestamp)))
                .call(function)
                .params(params)
                .build();
    }

    default Call<RpcItem> buildCall(String method) {
        return buildCall(method, null, RpcItem.class);
    }

    @SuppressWarnings("unused")
    default Call<RpcItem> buildCall(String method, RpcObject params) {
        return buildCall(method, params, RpcItem.class);
    }

    default <T> Call<T> buildCall(String method, RpcObject params, Class<T> responseType) {
        return new Call.Builder()
                .to(getScoreAddress())
                .method(method)
                .params(params)
                .buildWith(responseType);
    }
}
