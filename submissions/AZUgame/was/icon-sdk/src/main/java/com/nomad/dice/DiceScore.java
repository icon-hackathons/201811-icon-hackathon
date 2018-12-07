package com.nomad.dice;

import foundation.icon.icx.Transaction;
import foundation.icon.icx.data.Address;
import foundation.icon.icx.transport.jsonrpc.RpcItem;
import foundation.icon.icx.transport.jsonrpc.RpcObject;
import foundation.icon.icx.transport.jsonrpc.RpcValue;

import java.io.IOException;
import java.math.BigInteger;

@SuppressWarnings({"WeakerAccess", "UnusedReturnValue", "unused"})
public class DiceScore implements CallScore  {

    private Address scoreAddress;
    private IconServiceWrapper iconService;
    private static DiceScore instance;

    private DiceScore(IconServiceWrapper iconService, Address scoreAddress) {
        this.iconService = iconService;
        this.scoreAddress = scoreAddress;
    }

    public static DiceScore getInstance(IconServiceWrapper iconService, Address scoreAddress) {
        if (instance == null) {
            instance = new DiceScore(iconService, scoreAddress);
        } else {
            instance.setIconService(iconService);
            instance.setScoreAddress(scoreAddress);
        }
        return instance;
    }

    private void setScoreAddress(Address scoreAddress) {
        this.scoreAddress = scoreAddress;
    }

    private void setIconService(IconServiceWrapper iconService) {
        this.iconService = iconService;
    }

    public Transaction bet(Address playerAddress, BigInteger amount, BigInteger roleUnder, String houseHash, String playerSeed) {
        RpcObject params = new RpcObject.Builder()
                .put("amount", new RpcValue(amount))
                .put("roll_under", new RpcValue(roleUnder))
                .put("house_hash", new RpcValue(houseHash))
                .put("player_seed", new RpcValue(playerSeed))
                .build();
        return buildTransaction(playerAddress, "bet", params);
    }

    public RpcItem getHashFromStr(String content) throws IOException {
        RpcObject params = new RpcObject.Builder()
                .put("content", new RpcValue(content))
                .build();
        return iconService.call(buildCall("get_hash_from_str", params, RpcItem.class)).execute();
    }

    public Transaction roll(Address ownerAddress, BigInteger betIndex, String houseSeed) {
        RpcObject params = new RpcObject.Builder()
                .put("index", new RpcValue(betIndex))
                .put("house_seed", new RpcValue(houseSeed))
                .build();
        return buildTransaction(ownerAddress, "roll", params);
    }

    public RpcItem getAvailableAmount(Address playerAccount) throws IOException {
        RpcObject params = new RpcObject.Builder()
                .put("account", new RpcValue(playerAccount))
                .build();
        return iconService.call(buildCall("get_available_amount", params, RpcItem.class)).execute();
    }

    @Override
    public Address getScoreAddress() {
        return scoreAddress;
    }

    @Override
    public BigInteger getNetworkId() {
        return iconService.getNetworkId();
    }
}
