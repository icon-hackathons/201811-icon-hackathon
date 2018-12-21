#!/usr/bin/env python
import base64
import hashlib
import logging
import random
import time

from hashing import build_hash_generator
from secp256k1 import PrivateKey, PublicKey

ICX_FACTOR = 10 ** 18
ICX_FEE = 0.01


class IcxWallet:
    def __init__(self, private_key=None):
        self.__private_key = private_key or PrivateKey()
        self.__address = self.create_address(self.__private_key.pubkey)
        self.__last_tx_hash = ""

        tx_hash_version = 1
        self.__hash_generator = build_hash_generator(tx_hash_version, "icx_sendTransaction")

        self.to_address = None
        self.value = None
        self.message = None
        self.fee = ICX_FEE
        self.nid = '0x3'
        self.is_logging = True

    @property
    def address(self):
        return self.__address

    @property
    def last_tx_hash(self):
        return self.__last_tx_hash

    @last_tx_hash.setter
    def last_tx_hash(self, last_tx_hash):
        self.__last_tx_hash = last_tx_hash

    def create_icx_origin_v3(self, data):
        params = dict()
        params["version"] = "0x3"
        params["from"] = self.address
        params["to"] = "cx6a84c2f001b8f58564a4411c4403294cd8cd9caf"
        params["value"] = '0x0'
        params["stepLimit"] = "0x3000000"
        params["timestamp"] = hex(int(time.time() * 1_000_000))
        params["nonce"] = "0x0"
        params["nid"] = self.nid
        params["dataType"] = "call"
        params["data"] = data

        hash_for_sign = self.__hash_generator.generate_hash(params)
        params["signature"] = self.create_signature(hash_for_sign)

        return params

    def create_address(self, public_key: PublicKey) -> str:
        serialized_pub = public_key.serialize(compressed=False)
        hashed_pub = hashlib.sha3_256(serialized_pub[1:]).hexdigest()
        return f"hx{hashed_pub[-40:]}"

    def create_signature(self, tx_hash):
        signature = self.__private_key.ecdsa_sign_recoverable(msg=tx_hash,
                                                              raw=True,
                                                              digest=hashlib.sha3_256)
        serialized_sig = self.__private_key.ecdsa_recoverable_serialize(signature)
        sig_message = b''.join([serialized_sig[0], bytes([serialized_sig[1]])])
        signature = base64.b64encode(sig_message).decode()
        return signature
