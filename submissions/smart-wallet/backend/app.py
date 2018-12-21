import json
import os
from time import sleep

from flask import Flask, render_template, request, jsonify
from iconsdk import icon_service
from iconsdk.builder.call_builder import CallBuilder
from iconsdk.builder.transaction_builder import (
    TransactionBuilder,
    DeployTransactionBuilder,
    CallTransactionBuilder
)

from iconsdk.icon_service import IconService
from iconsdk.libs.in_memory_zip import gen_deploy_data_content
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.utils.convert_type import convert_int_to_hex_str, convert_hex_str_to_int
from iconsdk.wallet.wallet import KeyWallet


from backend.wallet_container import IconServiceContainer


template_dir = os.path.abspath('./static/hackathon')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def hello_world():
    return render_template("load.html")


@app.route('/account')
def account_page():
    return render_template("setting_change.html")


@app.route('/main')
def main_pane():
    return render_template("main_succ.html", accounts=IconServiceContainer.accounts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.args.get('privateKey'))
    # init wallet
    private_key = request.args.get('privateKey')
    wallet = KeyWallet.load(bytes.fromhex(private_key))
    IconServiceContainer.wallet = wallet

    return jsonify({"result": True})


@app.route('/accounts', methods=['POST'])
def create_account():
    account_info = request.json
    print(account_info)
    """
            accountinfo = {
              "account" : $("#account").val(),
              "tokenType" : isIcx ? "icx" : "IRC2",
              "tokenName" : isIcx ? "" : $("#tokenName").val(),
              "contractAddr" : isIcx ? "" : $("#contractAddr").val(),
              "sendLimit": $("#limit").val(),
              "dids" : dids
            }
    """
    _deploy_smart_wallet(wallet=IconServiceContainer.wallet,
                         token_type=account_info['tokenType'],
                         contract_addr=account_info['contractAddr'],
                         sendLimit=account_info['sendLimit'],
                         dids=account_info['dids'])

    _send_icx_to_smart_wallet(wallet=IconServiceContainer.wallet, name=account_info['account'])

    return jsonify({"result": True})


@app.route('/transfer', methods=['POST'])
def transfer():
    transfer_info = request.json
    print(transfer_info)
    info = _transfer(wallet=IconServiceContainer.wallet,
              account_id=int(transfer_info['from']),
              to=transfer_info['to'],
              token_type=transfer_info['tokenType'],
              contract_addr=transfer_info['contractAddr'],
              amount=int(transfer_info['amount']))
    return jsonify({"success": True, 'pending': True, 'info': info})


def _deploy_smart_wallet(wallet, token_type, contract_addr, sendLimit, dids):
    deploy_contract = gen_deploy_data_content("../smart_wallet")
    print(deploy_contract)
    account = {
        "tokenType": token_type,
        "contractAddr": contract_addr,
        "balance": 0,
        "totalUsed": 0,
        "sendLimit": int(sendLimit),
        "lastUsedDate": "2018-11-12",
        "dids": dids
    }

    transaction = DeployTransactionBuilder() \
        .from_(wallet.get_address()) \
        .to("cx0000000000000000000000000000000000000000") \
        .step_limit(2000000000000) \
        .nid(3) \
        .nonce(100) \
        .content_type("application/zip") \
        .content(deploy_contract) \
        .params({"account": json.dumps(account)}) \
        .build()
    result = _send_transaction(transaction, wallet, 10)
    IconServiceContainer.contract_addr = result['scoreAddress']


def _send_icx_to_smart_wallet(wallet, name):
    balance = IconServiceContainer.icon_service.get_balance(IconServiceContainer.wallet.get_address())
    print(f"wallet balance: {balance}")
    transaction = TransactionBuilder() \
        .from_(wallet.get_address()) \
        .to(IconServiceContainer.contract_addr) \
        .value(800) \
        .step_limit(100000000000) \
        .nid(3) \
        .nonce(100) \
        .build()
    result = _send_transaction(transaction, wallet, 10)
    account_info = json.loads(result['eventLogs'][0]['indexed'][1])
    print(f"created init account  : {account_info}")
    account_info['name'] = name
    IconServiceContainer.accounts.append(account_info)


def _send_transaction(transaction, wallet, sec):
    signed_tx = SignedTransaction(transaction, wallet)
    tx_hash = IconServiceContainer.icon_service.send_transaction(signed_tx)
    sleep(sec)
    tx_result = IconServiceContainer.icon_service.get_transaction_result(tx_hash)
    print(tx_result)
    return tx_result


def _transfer(wallet, account_id: int, token_type: str, contract_addr: str=None, to: str=0, amount: int=0):
    """ Send icx or token with Smart wallet

    :param wallet:
    :param account_id: from account id
    :param token_type:
    :param contract_addr: if token, it needed
    :param to: from account id or wallet address
    :param amount: amount to transfer
    :return:
    """

    params = {"account_id": convert_int_to_hex_str(account_id), "token_type": token_type,
              "contract_addr": contract_addr,
              "to": to,
              "amount": convert_int_to_hex_str(amount)}

    transaction = CallTransactionBuilder()\
        .from_(wallet.get_address())\
        .to(IconServiceContainer.contract_addr)\
        .step_limit(100000000000000)\
        .nid(3)\
        .nonce(2) \
        .method("transfer") \
        .params(params) \
        .build()

    result = _send_transaction(transaction, wallet, 9)
    for log in result['eventLogs']:
        if log['indexed'] == ['Pending(str)']:
            return json.loads(log['data'][0])


if __name__ == '__main__':
    wallet = KeyWallet.create()
    IconServiceContainer.icon_service = IconService(HTTPProvider("http://localhost:9000/api/v3"))
    app.run(port=3004)
