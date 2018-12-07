package com.nomad.dice.domain;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface HouseSeedsRepository extends JpaRepository<HouseSeeds, Long> {

    Optional<HouseSeeds> findByIdAndHouseHash(Long id, String houseHash);
}
