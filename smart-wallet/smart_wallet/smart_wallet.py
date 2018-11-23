from datetime import datetime
from typing import List

from iconservice import *

from .irc_2_interface import IRC2Interface
from .pending_tx_db_proxy import LAST_TX_ID, PENDING_TX, PENDING_TX_ID_LIST, PendingTxDbProxy
from .utils import only_owner

TAG = 'SmartWallet'
WALLET_OWNER = 'WalletOwner'


class SmartWallet(IconScoreBase):

    @eventlog(indexed=1)
    def Account(self, account: str):
        pass

    @eventlog
    def Balance(self, balance: int):
        pass

    @eventlog
    def Recieve(self, amount: int):
        pass

    @eventlog
    def TransferSuccess(self, account_id: int, token_type: int, contract_addr: str, to: str, amount: int):
        pass

    @eventlog
    def Pending(self, pending_tx: str):
        pass

    @eventlog
    def Approval(self, tx_id: int, did: str):
        pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._pending_tx_db_proxy = PendingTxDbProxy(db)
        self.wallet_owner = VarDB(WALLET_OWNER, db, bytes)

        # default account DB 생성
        # accounts = ["account_as_str_1", "account_as_str_2", .. ]
        self._accounts = ArrayDB("accounts", db, value_type=bytes)

    @only_owner
    @external
    def add_account(self, account: str):
        self._add_account(account)

    def _add_account(self, account: str):
        """
        Adds an account on the smart wallet
        by setting many values of account such as token type, contract address, total used, last used data, and dids.

        - account as dict = {
                                "id": len(self._accounts),
                                "tokenType": token_type,
                                "contractAddr": contract_addr,
                                "balance": balance,
                                "sendLimit": send_limit,
                                "totalUsed": total_used,
                                "lastUsedDate": last_used_date,
                                "dids": dids
                            }
        """
        account_id = len(self._accounts)
        account_as_dict = json_loads(account)
        account_as_dict["id"] = account_id
        account = json_dumps(account_as_dict)
        self._accounts.put(account)
        self.Account(account)

    @only_owner
    @external
    def change_setting_value(self, account: str):
        self._change_setting_value(account)

    def _change_setting_value(self, account: str):
        """Changes setting values of account on accounts

        :param account: one of accounts
        """
        account = json_loads(account)
        self._accounts[account["id"]] = json_dumps(account)
        self.Account(account)

    @external
    def change_new_wallet(self, did_infos: str):
        # TODO change to specific required dids depending on Did_SCORE
        required_dids = ["A", "B", "C"]
        #did_score = self.create_interface_score(self._did_address.get(), DidScore)
        did_infos_as_dict = json_loads(did_infos)
        # for did in required_dids:
        #     if not did_score.auth(did, self.address.body+self.tx.origin, did_infos[did]):
        #         self.revert(f"Authentication failed ")
        # owner update / test 필요

    # smart wallet 생성
    def on_install(self, account: str) -> None:
        super().on_install()
        self._add_account(account)
        self.msg.sender.to_bytes()
        self.wallet_owner.set(self.msg.sender)

    def on_update(self) -> None:
        super().on_update()

    @payable
    def fallback(self):
        account = json_loads(self._accounts[0])
        account["balance"] = account["balance"] + self.msg.value
        account_as_str = json_dumps(account)
        self._accounts[0] = account_as_str

        self.Account(account_as_str)
        self.Recieve(self.msg.value)
        self.Balance(self.icx.get_balance(self.address))

    @payable
    def tokenFallback(self, _from: Address, _value: int, _data: bytes=b''):
        pass

    @only_owner
    @external
    def transfer(self, account_id: int, token_type: str, contract_addr: str, to: str, amount: int):
        """Transfer depending on results

        :param account_id:
        :param token_type:
        :param contract_addr:
        :param to:
        :param amount:
        :return:
        """
        account = json_loads(self._accounts[account_id])
        required_dids = account['dids']
        if len(required_dids) == 0:
            self._transfer(account, token_type, contract_addr, to, amount)
        else:
            self._verify_transferable(account, token_type, contract_addr, amount)
            self._pending(account_id, token_type, contract_addr, to, amount, required_dids)

    @only_owner
    @external
    def approval(self, tx_id: int, did: str, auth_proof: str):
        """ Approval dids auth

        :param tx_id: tx unique id
        :param did: decentralized id
        :param auth_proof: auth info user input
        """

        pending_tx = self._pending_tx_db_proxy.get(tx_id)
        if pending_tx == {}:
            self.revert(f"tx : {tx_id} is not exist in pending tx")
        did_list = pending_tx["dids"]  # type: List
        if did not in did_list:
            revert(f"{did} is not in dids {did_list}")

        # did_score = self.create_interface_score(self._did_address.get(), DidScore)
        # did_score.auth(did, self.address.body+bytes([tx_id]), auth_proof)

        did_list.remove(did)
        self.Approval(tx_id=tx_id, did=did)
        if len(did_list) == 0:
            self._pending_tx_db_proxy.remove(tx_id)
            self._transfer(account=json_loads(self._accounts[pending_tx["from"]]),
                           token_type=pending_tx["tokenType"],
                           contract_addr=pending_tx["contractAddr"],
                           to=pending_tx["to"],
                           amount=pending_tx["amount"])
        else:
            pending_tx["dids"] = did_list
            self._pending_tx_db_proxy.update(pending_tx)

    def _verify_transferable(self, account: dict, token_type: str, contract_addr: str, amount: int):
        """ Verify value < account balance and value < limit - today_limit
        If verify result is fail this function raise revert

        :param account: account
        :param token_type: send token type
        :param contract_addr: send token contract
        :param amount: send token amount
        :return:
        """
        if account["tokenType"] != token_type or (token_type != "icx" and account["contractAddr"] != contract_addr):
            revert(f"This account can't send {token_type}:{contract_addr}")

        if account["balance"] < amount:
            revert(f"Account:{account['id']} balance is {account['balance']}, can't send {amount}")

        timestamp = int(str(self.block.timestamp)[:9])
        now = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

        if account["lastUsedDate"] != now:
            account['lastUsedDate'] = now
            account['totalUsed'] = 0

        if account["sendLimit"] - account["totalUsed"] < amount:
            revert(f"Account:{account['id']} can send {account['sendLimit'] - account['totalUsed']} "
                   f"today , can't send {amount}")

    def _transfer(self, account: dict, token_type, contract_addr, to, amount):
        """ Transfer token

        :param account:
        :param token_type:
        :param contract_addr:
        :param to:
        :param amount:
        :return:
        """
        # Verify account can send
        self._verify_transferable(account=account,
                                  token_type=token_type,
                                  contract_addr=contract_addr,
                                  amount=amount)

        if to.isdigit():
            self._transfer_to_internal_account(amount, contract_addr, to, token_type)
        else:
            self._transfer_to_outer_account(amount, to, token_type, contract_addr)
        self._transfered_account_update(account, amount)
        self.TransferSuccess(account["id"], token_type, contract_addr, to, amount)

    def _transfered_account_update(self, account, amount):
        account["balance"] = account["balance"] - amount
        account["totalUsed"] = account["totalUsed"] + amount
        self._accounts[account["id"]] = json_dumps(account)

    def _transfer_to_outer_account(self, amount, to, token_type, contract_addr):
        if token_type == "icx":
            self.icx.transfer(to, amount)
        else:
            irc_2 = self.create_interface_score(contract_addr, IRC2Interface)
            irc_2.transfer(to, amount)

    def _transfer_to_internal_account(self, amount, contract_addr, to, token_type):
        to_account_as_str = self._accounts[int(to)]

        if to_account_as_str == "":
            revert(f"To account : {to} is not exist")

        to_account = json_loads(to_account_as_str)

        # check token type is same
        if to_account["tokenType"] != token_type or \
                (token_type != "icx" and to_account["contractAddr"] != contract_addr):
            revert(f"account:{to} can't save {token_type}:{contract_addr}")

        to_account["balance"] = to_account["balance"] + amount
        self._accounts[to_account["id"]] = json_dumps(to_account)

    def _pending(self, account_id, token_type, contract_addr, to, amount, dids):
        pending_tx_as_str = self._pending_tx_db_proxy.add(account_id=account_id,
                                                          token_type=token_type,
                                                          contract_addr=contract_addr,
                                                          to=to,
                                                          amount=amount,
                                                          dids=dids)
        self.Pending(pending_tx_as_str)
