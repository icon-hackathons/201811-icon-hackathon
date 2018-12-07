package com.nomad.dice.controller;

import com.nomad.dice.domain.HouseSeeds;
import com.nomad.dice.payload.deploy.DeployResult;
import com.nomad.dice.payload.deploy.DeployScoreRequest;
import com.nomad.dice.payload.roll.HouseSeedResponse;
import com.nomad.dice.payload.roll.RollRequest;
import com.nomad.dice.service.DiceService;
import com.nomad.dice.service.HouseSeedsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.math.BigInteger;

@RestController
public class DiceController {

    @Autowired
    private DiceService diceService;

    @Autowired
    private HouseSeedsService houseSeedsService;

    @GetMapping("/healthCheck")
    public ResponseEntity<?> healthCheck() {
        return ResponseEntity.ok().build();
    }

    @PostMapping("/score/deploy")
    public ResponseEntity<?> deploy(@Valid @RequestBody DeployScoreRequest deployScoreRequest) {
        DeployResult deployResult = diceService.deploy(deployScoreRequest);

        return ResponseEntity.ok().body(deployResult);
    }

    @GetMapping("/dice/{diceAddress}/player/{playerAccount}/houseSeed")
    public ResponseEntity<?> getHouseSeed(@PathVariable String diceAddress,
                                          @PathVariable String playerAccount) {
        String houseSeed = houseSeedsService.generateHouseSeeds();
        String houseHash = diceService.getHashFromString(diceAddress, houseSeed);

        HouseSeeds houseSeeds = houseSeedsService.create(HouseSeeds.builder().houseHash(houseHash).houseSeed(houseSeed).playerAccount(playerAccount).build());

        return ResponseEntity.ok().body(HouseSeedResponse.builder().houseSeeds(houseSeeds).build());
    }

    @PostMapping("/dice/{diceAddress}/roll/{betIndex}")
    public ResponseEntity<?> roll(@PathVariable String diceAddress,
                                  @PathVariable BigInteger betIndex,
                                  @Valid @RequestBody RollRequest rollRequest) {
        String houseSeed = houseSeedsService.getHouseSeed(rollRequest.getHouseHashId(), rollRequest.getHouseHash());

        boolean success = diceService.generateTxToRoll(diceAddress, betIndex, houseSeed);

        return ResponseEntity.ok().body(success);
    }
}
