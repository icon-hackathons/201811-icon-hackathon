package com.nomad.dice;

import foundation.icon.icx.Wallet;
import foundation.icon.icx.data.Address;

public class EmptyWallet implements Wallet {
    @Override
    public Address getAddress() {
        return null;
    }

    @Override
    public byte[] sign(byte[] data) {
        return new byte[0];
    }
}
