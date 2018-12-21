package com.nomad.dice.domain;

import lombok.*;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;

@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
@Setter
@ToString
@Entity
@Table(name = "house_seeds")
public class HouseSeeds {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private long id;

    @NotBlank
    @Column(name = "player_account")
    private String playerAccount;

    @NotBlank
    @Column(name = "house_seed")
    private String houseSeed;

    @NotBlank
    @Column(name = "house_hash")
    private String houseHash;

    @Builder
    public HouseSeeds(String playerAccount, String houseSeed, String houseHash) {
        this.playerAccount = playerAccount;
        this.houseSeed = houseSeed;
        this.houseHash = houseHash;
    }
}
