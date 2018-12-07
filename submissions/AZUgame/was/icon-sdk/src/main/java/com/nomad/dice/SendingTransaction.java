package com.nomad.dice;

import foundation.icon.icx.Transaction;
import foundation.icon.icx.data.Address;
import foundation.icon.icx.transport.jsonrpc.RpcItem;

import java.math.BigInteger;

public class SendingTransaction implements Transaction {

    private BigInteger version;
    private Address from;
    private Address to;
    private BigInteger value;
    private BigInteger stepLimit;
    private BigInteger timestamp;
    private BigInteger nid;
    private BigInteger nonce;
    private String dataType;
    private RpcItem data;

    @Override
    public BigInteger getVersion() {
        return version;
    }

    @Override
    public Address getFrom() {
        return from;
    }

    @Override
    public Address getTo() {
        return to;
    }

    @Override
    public BigInteger getValue() {
        return value;
    }

    @Override
    public BigInteger getStepLimit() {
        return stepLimit;
    }

    @Override
    public BigInteger getTimestamp() {
        return timestamp;
    }

    @Override
    public BigInteger getNid() {
        return nid;
    }

    @Override
    public BigInteger getNonce() {
        return nonce;
    }

    @Override
    public String getDataType() {
        return dataType;
    }

    @Override
    public RpcItem getData() {
        return data;
    }


    public static final class Builder {
        private BigInteger version;
        private Address from;
        private Address to;
        private BigInteger value;
        private BigInteger stepLimit;
        private BigInteger timestamp;
        private BigInteger nid;
        private BigInteger nonce;
        private String dataType;
        private RpcItem data;

        public Builder() {
            // Do nothing
        }

        public Builder version(RpcItem version) {
            if (version != null) this.version = version.asInteger();
            return this;
        }

        public Builder from(RpcItem from) {
            if (from != null) this.from = from.asAddress();
            return this;
        }

        public Builder to(RpcItem to) {
            if (to != null) this.to = to.asAddress();
            return this;
        }

        public Builder value(RpcItem value) {
            if (value != null) this.value = value.asInteger();
            return this;
        }

        public Builder stepLimit(RpcItem stepLimit) {
            if (stepLimit != null) this.stepLimit = stepLimit.asInteger();
            return this;
        }

        public Builder timestamp(RpcItem timestamp) {
            if (timestamp != null) this.timestamp = timestamp.asInteger();
            return this;
        }

        public Builder nid(RpcItem nid) {
            if (nid != null) this.nid = nid.asInteger();
            return this;
        }

        public Builder nonce(RpcItem nonce) {
            if (nonce != null) this.nonce = nonce.asInteger();
            return this;
        }

        public Builder dataType(RpcItem dataType) {
            if (dataType != null) this.dataType = dataType.asString();
            return this;
        }

        public Builder data(RpcItem data) {
            this.data = data;
            return this;
        }

        public SendingTransaction build() {
            SendingTransaction sendingTransaction = new SendingTransaction();
            sendingTransaction.nonce = this.nonce;
            sendingTransaction.from = this.from;
            sendingTransaction.value = this.value;
            sendingTransaction.timestamp = this.timestamp;
            sendingTransaction.nid = this.nid;
            sendingTransaction.version = this.version;
            sendingTransaction.to = this.to;
            sendingTransaction.data = this.data;
            sendingTransaction.dataType = this.dataType;
            sendingTransaction.stepLimit = this.stepLimit;
            return sendingTransaction;
        }
    }
}
