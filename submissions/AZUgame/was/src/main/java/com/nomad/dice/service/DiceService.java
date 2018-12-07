package com.nomad.dice.service;

import com.nomad.dice.Wallets;
import com.nomad.dice.exception.IconGenerateTransactionFailureException;
import com.nomad.dice.exception.IconSendTransactionFailureException;
import com.nomad.dice.payload.deploy.DeployResult;
import com.nomad.dice.payload.deploy.DeployScoreRequest;
import com.nomad.dice.repository.DiceRepository;
import com.nomad.dice.repository.TxRepository;
import foundation.icon.icx.KeyWallet;
import foundation.icon.icx.SignedTransactionWithoutWallet;
import foundation.icon.icx.Transaction;
import foundation.icon.icx.data.Address;
import foundation.icon.icx.data.TransactionResult;
import foundation.icon.icx.transport.jsonrpc.RpcError;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Path;
import java.nio.file.Paths;

@Service
@Slf4j
public class DiceService {

    @Value("${app.file.ownerKey}")
    private String ownerKey;

    @Value("${app.owner.password}")
    private String ownerPassword;

    @Autowired
    private DiceRepository diceRepository;

    @Autowired
    private TxRepository txRepository;

    private Path getKeyStorePath(String fileName) {
        return Paths.get(System.getProperty("user.dir"), fileName);
    }

    public DeployResult deploy(DeployScoreRequest deployScoreRequest) {
        long timestamp = System.currentTimeMillis() * 1000L;
        try {
            String keystorePath = getKeyStorePath(ownerKey).toString();
            KeyWallet ownerWallet = Wallets.readWalletFromFile(keystorePath, ownerPassword);

            Transaction transaction = diceRepository.deployScore(ownerWallet.getAddress(), deployScoreRequest, timestamp);

            SignedTransactionWithoutWallet signedTransactionWithoutWallet = new SignedTransactionWithoutWallet(transaction);
            String txHash = signedTransactionWithoutWallet.sha256();
            String json = signedTransactionWithoutWallet.toJson();

            String signature = Wallets.sign(ownerWallet, txHash);

            signedTransactionWithoutWallet = SignedTransactionWithoutWallet.fromJsonWithSignature(json, signature);

            TransactionResult result = diceRepository.sendTransaction(signedTransactionWithoutWallet);

            if (result.getStatus().intValue() == 1) {
                return DeployResult.builder().scoreAddress(result.getScoreAddress()).txHash(result.getTxHash()).build();
            } else {
                throw IconSendTransactionFailureException.builder().code(result.getFailure().getCode()).message(result.getFailure().getMessage()).build();
            }
        } catch (IOException e) {
            if (e instanceof RpcError) throw IconSendTransactionFailureException.builder().code(BigInteger.valueOf(((RpcError)e).getCode())).message(e.getMessage()).build();
            e.printStackTrace();
        }

        return null;
    }

    public String getHashFromString(String diceAddress, String content) {
        try {
            return diceRepository.getHashFromStr(new Address(diceAddress), content);
        } catch (IOException e) {
            e.printStackTrace();
            throw IconGenerateTransactionFailureException.builder().message("Failed to get hash from string content").cause(e.getCause()).build();
        }
    }

    public boolean generateTxToRoll(String diceAddress, BigInteger betIndex, String houseSeed) {
        try {
            String keystorePath = getKeyStorePath(ownerKey).toString();
            KeyWallet ownerWallet = Wallets.readWalletFromFile(keystorePath, ownerPassword);

            Transaction transaction = diceRepository.roll(new Address(diceAddress), ownerWallet.getAddress(), betIndex, houseSeed);

            SignedTransactionWithoutWallet signedTransactionWithoutWallet = new SignedTransactionWithoutWallet(transaction);
            String txHash = signedTransactionWithoutWallet.sha256();
            String json = signedTransactionWithoutWallet.toJson();
            String signature = Wallets.sign(ownerWallet, txHash);
            signedTransactionWithoutWallet = SignedTransactionWithoutWallet.fromJsonWithSignature(json, signature);

            TransactionResult result = diceRepository.sendTransaction(signedTransactionWithoutWallet);

            if (result.getStatus().intValue() == 1) {
                return txRepository.getResultOfRolled(result);
            } else {
                throw IconSendTransactionFailureException.builder().code(result.getFailure().getCode()).message(result.getFailure().getMessage()).build();
            }
        } catch (IOException e) {
            e.printStackTrace();
            throw IconGenerateTransactionFailureException.builder().message("Failed to create a tx to roll").cause(e.getCause()).build();
        }
    }
}
