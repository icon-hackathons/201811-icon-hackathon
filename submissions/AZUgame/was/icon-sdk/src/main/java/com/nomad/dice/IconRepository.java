package com.nomad.dice;

import foundation.icon.icx.Call;
import foundation.icon.icx.SignedTransactionWithoutWallet;
import foundation.icon.icx.Transaction;
import foundation.icon.icx.data.*;
import foundation.icon.icx.transport.jsonrpc.RpcError;

import java.io.IOException;
import java.math.BigInteger;
import java.util.List;

@SuppressWarnings("unused")
public interface IconRepository {

    IconServiceWrapper getIconService();

    default TransactionResult sendTransaction(SignedTransactionWithoutWallet signedTransaction) throws IOException {
        Bytes txHash = getIconService().sendTransaction(signedTransaction).execute();
        return getTransactionResult(txHash);
    }

    default TransactionResult sendTransaction(Transaction transaction, String signature) throws IOException {
        SignedTransactionWithoutWallet signedTransaction = new SignedTransactionWithoutWallet(transaction);
        signedTransaction.setSignature(signature);
        return sendTransaction(signedTransaction);
    }

    default ConfirmedTransaction getTransaction(Bytes hash) throws IOException {
        return getIconService().getTransaction(hash).execute();
    }

    default TransactionResult getTransactionResult(Bytes hash) throws IOException {
        TransactionResult result = null;
        while (result == null) {
            try {
                Thread.sleep(1000);
                result = getIconService().getTransactionResult(hash).execute();
            } catch (RpcError e) {
                // pending
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        return result;
    }

    default BigInteger getTotalSupply() throws IOException {
        return getIconService().getTotalSupply().execute();
    }

    default BigInteger getBalance(Address address) throws IOException {
        return getIconService().getBalance(address).execute();
    }

    default Block getBlock(BigInteger height) throws IOException {
        return getIconService().getBlock(height).execute();
    }

    default Block getBlock(Bytes hash) throws IOException {
        return getIconService().getBlock(hash).execute();
    }

    default Block getLastBlock() throws IOException {
        return getIconService().getLastBlock().execute();
    }

    default List<ScoreApi> getScoreApi(Address scoreAddress) throws IOException {
        return getIconService().getScoreApi(scoreAddress).execute();
    }

    default <O> O call(Call<O> call) throws IOException {
        return getIconService().call(call).execute();
    }

}
