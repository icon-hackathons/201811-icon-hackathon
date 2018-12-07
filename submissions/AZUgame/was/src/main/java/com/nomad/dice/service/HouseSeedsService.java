package com.nomad.dice.service;

import com.nomad.dice.domain.HouseSeeds;
import com.nomad.dice.domain.HouseSeedsRepository;
import com.nomad.dice.exception.ResourceNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class HouseSeedsService {

    @Autowired
    private HouseSeedsRepository houseSeedsRepository;

    public String generateHouseSeeds() {
        return UUID.randomUUID().toString();
    }

    public HouseSeeds create(HouseSeeds houseSeeds) {
        return houseSeedsRepository.save(houseSeeds);
    }

    public String getHouseSeed(Long id, String houseHash) {
        return houseSeedsRepository.findByIdAndHouseHash(id, houseHash)
                .orElseThrow(() -> ResourceNotFoundException.builder().resourceName("houseSeed").fieldName("id | houseHash").fieldValue(id + " | "+ houseHash).build())
                .getHouseSeed();
    }
}
