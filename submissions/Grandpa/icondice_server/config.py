import binascii

from secp256k1 import PrivateKey

from icx_wallet import IcxWallet


class CONFIG:
    db_path = './.db_user'
    http_uri = 'http://127.0.0.1:8000'
    ws_uri = 'ws://127.0.0.1:8000'
    jwt_key = 'thisissecret'
    v3_uri = 'https://bicon.net.solidwallet.io/api/v3'
    contract_address = 'cx6a84c2f001b8f58564a4411c4403294cd8cd9caf'

    # Fill in the following configurations.

    # deserialized_private_key = "5257a9df23980000000000000000000000000000000000000000000000000000"
    # private_key = PrivateKey(binascii.unhexlify(deserialized_private_key))
    # address = 'hxa94f1eb1ba891c680d00bc000000000000000000'
    # icx_wallet = IcxWallet(private_key)
