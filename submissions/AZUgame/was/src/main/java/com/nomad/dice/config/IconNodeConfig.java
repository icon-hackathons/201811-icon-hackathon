package com.nomad.dice.config;

import lombok.Getter;
import lombok.Setter;
import org.springframework.boot.context.properties.ConfigurationProperties;

@ConfigurationProperties(prefix = "app.node")
@Getter
@Setter
public class IconNodeConfig {
    private String url;
    private String networkId;
}
