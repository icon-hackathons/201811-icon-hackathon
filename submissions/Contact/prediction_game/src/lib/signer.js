const secp256k1 = require('secp256k1');
const sha3_256 = require('js-sha3').sha3_256;

const biconUrl = "https://bicon.net.solidwallet.io/api/v3"
const scoreAddress = "cx30dbe641968a0c280a92d70c55f5072e5daa0888"
const eoa = "hx8f4ef11d2df14b66de3a6e5be4be987959287c75"

let transactionFormat = {
    "jsonrpc": "2.0",
    "method": "icx_sendTransaction",
    "id": 1234,
    "params": {
        "version": "0x3",
        "from": "hx8f4ef11d2df14b66de3a6e5be4be987959287c75",
        "to": scoreAddress,
        "stepLimit": "0x50000000",
        "timestamp": `0x${(Date.now()*1000).toString(16)}`,
        "nid": "0x3",
        "nonce": "0x1",
        "dataType": "call",
        "data": {
            "method": "transfer",
            "params": {
                "to": "hxab2d8215eab14bc6bdd8bfb2c8151257032ecd8b",
                "value": "0x1"
            }
        }
    }
}

let callFormat = {
    "jsonrpc": "2.0",
    "method": "icx_call",
    "id": 1234,
    "params": {
        "from": "hxbe258ceb872e08851f1f59694dac2558708ece11",
        "to": scoreAddress,
        "dataType": "call",
        "data": {
            "method": "get_balance",
            "params": {
                "address": "hx1f9a3310f60a03934b917509c86442db703cbd52"
            }
        }
    }
}

let getBalance = {
    "jsonrpc": "2.0",
    "method": "icx_getBalance",
    "id": 1234,
    "params": {
        "address": "hx8f4ef11d2df14b66de3a6e5be4be987959287c75"
    }
}

const getLastBlock = {
    "jsonrpc": "2.0",
    "method": "icx_getLastBlock",
    "id": 1234
}

String.prototype.escape = function () {
   let tagsToReplace = {
        '\\': '\\\\',
        '{': '\\{',
        '}': '\\}',
        '[': '\\[',
        ']': '\\]',
        '.': '\\.',
    };
    return this.replace(/[\\\{\}\[\]\.]/g, function (tag) {
        return tagsToReplace[tag] || tag;
    });
};

function serialize_params(json_data) {
    function encode(data) {
        return encode_dict(data).slice(1, -1);
    }

    function encode_dict(data) {
        let result = "";
        const keys = Object.keys(data);
        keys.sort();
        for (let i = 0; i < keys.length; i++) {
            if (data[keys[i]].constructor === Array) {
                result += `${keys[i]}.`;
                result += `${encode_list(data[keys[i]])}.`;
                continue;
            } else if (data[keys[i]].constructor !== String) {
                result += `${keys[i]}.`;
                result += `${encode_dict(data[keys[i]])}.`;
                continue;
            }
            result += `${escape(keys[i])}.`;
            result += `${escape(data[keys[i]])}.`;
        }
        return `{${result.slice(0, -1)}}`;
    }

    function encode_list(data) {
        for (let i = 0; i < data.length; i++) {
            if (data[i].constructor === Array) {
                data[i] = `${encode_list(data[i])}`;
            } else if (data[i].constructor !== String) {
                data[i] = `${encode_dict(data[i])}`;
            } else {
                data[i] = escape(data[i]);
            }
        }
        return `[${data.join(".")}]`
    }

    function escape(data) {
        if (data === null)
            return "\\0";

        return data.escape();
    }

    return `icx_sendTransaction.${encode(json_data)}`;
}

function concatTypedArrays(a, b) {
    let c = new (a.constructor)(a.length + b.length);
    c.set(a, 0);
    c.set(b, a.length);
    return c;
}

function putsig(jsonData, privKey) {
    const msgPhrase = serialize_params(jsonData['params']);
    const msgHash = sha3_256.update(msgPhrase).hex();
    const message = new Buffer(msgHash, 'hex');
    const privateKey = new Buffer(privKey, 'hex');
    const sign = secp256k1.sign(message, privateKey);
    const recovery = new Uint8Array(1);
    recovery[0] = sign.recovery;
    const signature = concatTypedArrays(sign.signature, recovery);
    const b64encoded = Buffer.from(signature).toString('base64');
    jsonData['params']['signature'] = b64encoded;
    return jsonData;
}

export default {
    putsig,
    callFormat,
    transactionFormat,
    getBalance,
    getLastBlock,
    biconUrl,
    scoreAddress,
    eoa
}