package com.nomad.dice.repository;

import com.nomad.dice.IconRepository;
import com.nomad.dice.IconServiceWrapper;
import com.nomad.dice.config.IconNodeConfig;
import com.nomad.dice.payload.deploy.DeployScoreRequest;
import foundation.icon.icx.Transaction;
import foundation.icon.icx.TransactionBuilder;
import foundation.icon.icx.data.Address;
import foundation.icon.icx.transport.jsonrpc.RpcItem;
import foundation.icon.icx.transport.jsonrpc.RpcObject;
import foundation.icon.icx.transport.jsonrpc.RpcValue;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Repository;

import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Path;
import java.nio.file.Paths;

import static com.nomad.dice.IconServiceWrapper.ZERO_ADDRESS;

@Repository
@Slf4j
public class DiceRepository implements IconRepository {

    private IconServiceWrapper iconService;

    @Value("${app.file.iconScore}")
    private String iconScorePath;

    @Autowired
    public DiceRepository(IconNodeConfig config) {
        iconService = IconServiceWrapper.create(config.getUrl(), config.getNetworkId(), true);
    }

    public Transaction deployScore(Address ownerAddress, DeployScoreRequest deployScoreRequest, long timestamp) throws IOException {
        log.info("deployScore -- OWNER_ADDRESS( {} ), TIMESTAMP( {} )", ownerAddress, timestamp);
        log.info("====================================================================================================");
        log.info("\tDEPLOY CONTEXT");
        log.info("----------------------------------------------------------------------------------------------------");
        log.info("\tROLE_UNDER_MIN  : {}", deployScoreRequest.getRoleUnderMin());
        log.info("\tROLE_UNDER_MAX  : {}", deployScoreRequest.getRoleUnderMax());
        log.info("\tBET_MIN         : {}", deployScoreRequest.getBetMin());
        log.info("\tBET_MAX         : {}", deployScoreRequest.getBetMax());
        log.info("====================================================================================================");

        BigInteger stepLimit = new BigInteger("1500000000");
        RpcObject params = new RpcObject.Builder()
                .put("roll_under_min", new RpcValue(deployScoreRequest.getRoleUnderMin()))
                .put("roll_under_max", new RpcValue(deployScoreRequest.getRoleUnderMax()))
                .put("bet_min", new RpcValue(deployScoreRequest.getBetMin()))
                .put("bet_max", new RpcValue(deployScoreRequest.getBetMax()))
                .build();

        byte[] content = iconService.readFile(getScorePath());
        return TransactionBuilder.newBuilder()
                .nid(iconService.getNetworkId())
                .from(ownerAddress)
                .to(ZERO_ADDRESS)
                .stepLimit(stepLimit)
                .timestamp(new BigInteger(String.valueOf(timestamp)))
                .nonce(new BigInteger("1"))
                .deploy("application/zip", content)
                .params(params)
                .build();
    }

    public String getHashFromStr(Address scoreAddress, String content) throws IOException {
        RpcItem result = iconService.diceScore(scoreAddress).getHashFromStr(content);

        if (result != null) {
            return result.asString();
        }

        return null;
    }

    public Transaction roll(Address scoreAddress, Address ownerAddress, BigInteger betIndex, String houseSeed) throws IOException {
        log.info("roll -- PLAYER_ACCOUNT( {} )");
        log.info("====================================================================================================");
        log.info("\tROLL CONTEXT");
        log.info("----------------------------------------------------------------------------------------------------");
        log.info("\tBET_INDEX   : {}", betIndex);
        log.info("\tHOUSE_SEED  : {}", houseSeed);
        log.info("====================================================================================================");

        return iconService.diceScore(scoreAddress).roll(ownerAddress, betIndex, houseSeed);
    }

    @Override
    public IconServiceWrapper getIconService() {
        return iconService;
    }

    public Path getScorePath() {
        return Paths.get(System.getProperty("user.dir"), iconScorePath);
    }
}
