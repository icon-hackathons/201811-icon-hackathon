package foundation.icon.icx;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.module.SimpleModule;
import com.nomad.dice.EmptyWallet;
import com.nomad.dice.SendingTransaction;
import foundation.icon.icx.transport.jsonrpc.*;
import org.web3j.utils.Numeric;

import java.io.IOException;

public class SignedTransactionWithoutWallet extends SignedTransaction {

    private String signature;

    public SignedTransactionWithoutWallet(Transaction transaction) {
        super(transaction, new EmptyWallet());
    }

    public SignedTransactionWithoutWallet(Transaction transaction, String signature) {
        super(transaction, new EmptyWallet());
        this.signature = signature;
    }

    public static SignedTransactionWithoutWallet fromJsonWithSignature(String json, String signature) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
        SimpleModule module = new SimpleModule();
        module.addDeserializer(RpcItem.class, new RpcItemDeserializer());
        mapper.registerModule(module);
        RpcObject object = mapper.readValue(json, RpcItem.class).asObject();

        Transaction transaction = new SendingTransaction.Builder()
                .version(object.getItem("version"))
                .from(object.getItem("from"))
                .to(object.getItem("to"))
                .value(object.getItem("value"))
                .stepLimit(object.getItem("stepLimit"))
                .timestamp(object.getItem("timestamp"))
                .nid(object.getItem("nid"))
                .nonce(object.getItem("nonce"))
                .dataType(object.getItem("dataType"))
                .data(object.getItem("data"))
                .build();

        return new SignedTransactionWithoutWallet(transaction, signature);
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public String sha256() {
        return Numeric.toHexStringNoPrefix(sha256(serialize(getTransactionProperties())));
    }

    public String toJson() throws JsonProcessingException {
        RpcItem properties = getTransactionProperties();

        ObjectMapper mapper = new ObjectMapper();
        mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
        SimpleModule module = new SimpleModule();
        module.addSerializer(RpcItem.class, new RpcItemSerializer());
        mapper.registerModule(module);
        return mapper.writeValueAsString(properties);
    }

    @Override
    public RpcObject getProperties() {
        RpcObject properties = getTransactionProperties();

        RpcObject.Builder builder = new RpcObject.Builder();
        for (String key : properties.keySet()) {
            builder.put(key, properties.getItem(key));
        }
        builder.put("signature", new RpcValue(signature));
        return builder.build();
    }

}
