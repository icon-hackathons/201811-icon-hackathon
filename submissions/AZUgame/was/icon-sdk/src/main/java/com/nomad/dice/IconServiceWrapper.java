package com.nomad.dice;

import foundation.icon.icx.IconService;
import foundation.icon.icx.Provider;
import foundation.icon.icx.data.Address;
import foundation.icon.icx.transport.http.HttpProvider;
import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;

import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.concurrent.TimeUnit;

public class IconServiceWrapper extends IconService {
    public static final Address ZERO_ADDRESS = new Address("cx0000000000000000000000000000000000000000");
    private BigInteger networkId;

    private IconServiceWrapper(Provider provider, BigInteger networkId) {
        super(provider);
        this.networkId = networkId;
    }

    public static IconServiceWrapper create(String url, String networkId) {
        return create(url, networkId, false);
    }

    public static IconServiceWrapper create(String url, String networkId, boolean isDebug) {
        HttpProvider provider;
        if (isDebug) {
            HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
            logging.setLevel(HttpLoggingInterceptor.Level.BODY);
            OkHttpClient httpClient = new OkHttpClient.Builder()
                    .addInterceptor(logging)
                    .readTimeout(100L, TimeUnit.SECONDS)
                    .build();
            provider = new HttpProvider(httpClient, url);
        } else {
            provider = new HttpProvider(url);
        }
        return new IconServiceWrapper(provider, new BigInteger(networkId));
    }

    public DiceScore diceScore(Address scoreAddress) {
        return DiceScore.getInstance(this, scoreAddress);
    }

    public BigInteger getNetworkId() {
        return networkId;
    }

    public byte[] readFile(Path path) throws IOException {
        return Files.readAllBytes(path);
    }
}
