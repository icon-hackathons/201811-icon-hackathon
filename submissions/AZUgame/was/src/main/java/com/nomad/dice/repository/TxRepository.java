package com.nomad.dice.repository;

import com.nomad.dice.IconRepository;
import com.nomad.dice.IconServiceWrapper;
import com.nomad.dice.config.IconNodeConfig;
import foundation.icon.icx.data.TransactionResult;
import foundation.icon.icx.transport.jsonrpc.RpcItem;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Slf4j
public class TxRepository implements IconRepository {

    private IconServiceWrapper iconService;

    @Autowired
    public TxRepository(IconNodeConfig config) {
        iconService = IconServiceWrapper.create(config.getUrl(), config.getNetworkId(), true);
    }

    public boolean getResultOfRolled(TransactionResult transactionResult) {
        boolean result = false;
        List<TransactionResult.EventLog> logs = transactionResult.getEventLogs();
        for (TransactionResult.EventLog log : logs) {
            RpcItem function = log.getIndexed().get(0);
            if (function.asString().equals("event_roll(str,str)")) {
                if ("1".equals(log.getIndexed().get(2).asString())) {
                    result = true;
                }
            }
        }
        return result;
    }

    @Override
    public IconServiceWrapper getIconService() {
        return iconService;
    }
}
