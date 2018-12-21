package com.nomad.dice;

import foundation.icon.icx.KeyWallet;
import foundation.icon.icx.Wallet;
import foundation.icon.icx.data.Bytes;
import org.web3j.crypto.CipherException;
import org.web3j.utils.Numeric;

import java.io.File;
import java.io.IOException;
import java.security.InvalidAlgorithmParameterException;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.util.Base64;
import java.util.Objects;

@SuppressWarnings({"unused", "WeakerAccess"})
public class Wallets {
    private Wallets() { }

    public static KeyWallet readWalletFromFile(String path, String password) throws IOException {
        try {
            File file = new File(path);
            return KeyWallet.load(password, file);
        } catch (CipherException e) {
            throw new IOException("Key load failed!");
        }
    }

    public static String sign(Wallet wallet, String data) {
        return Base64.getEncoder().encodeToString(wallet.sign(Numeric.hexStringToByteArray(data)));
    }
}
