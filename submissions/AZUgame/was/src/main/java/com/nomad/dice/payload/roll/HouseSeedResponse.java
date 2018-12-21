package com.nomad.dice.payload.roll;

import com.nomad.dice.domain.HouseSeeds;
import lombok.Builder;
import lombok.Data;

@Data
public class HouseSeedResponse {

    private Long id;
    private String houseHash;

    @Builder
    public HouseSeedResponse(HouseSeeds houseSeeds) {
        this.id = houseSeeds.getId();
        this.houseHash = houseSeeds.getHouseHash();
    }
}
