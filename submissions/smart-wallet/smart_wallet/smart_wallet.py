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
        """ 새로운 Account를 생성합니다. Owner만 새로운 Account를 생성할 수 있습니다.
        account의 id는 마지막으로 생성된 Account의 id + 1로 설정 됩니다.
        추가된 Account의 정보는 Account(str) 이벤트를 통해 확인 할 수 있습니다.

        :param account: (str) String으로 Serialize된 JSON 형태의 Account 정보
        """
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
        """ Account 정보를 변경합니다.
        변경된 Account의 정보는 Account(str) 이벤트를 통해 확인 할 수 있습니다.

        :param account: (str) String으로 Serialize된 JSON 형태의 Account Setting 정보
        Account Setting 정보에는 하루 송금 제한과 인증에 활용할 did가 명시되어 있어야 합니다.
        Example)
        {
            "sendLimit": {하루 송금 제한 액(int)},
            "dids": [{송금시 인증에 사용하는 Did 이름(str)}, ex)"kakao",...]
        }
        """
        self._change_setting_value(account)

    def _change_setting_value(self, account: str):
        """Changes setting values of account on accounts

        :param account: one of accounts
        """
        account = json_loads(account)
        self._accounts[account["id"]] = json_dumps(account)
        self.Account(account)

    def on_install(self, account: str) -> None:
        """ account의 정보를 통해 초기 계좌를 생성하고 Sender를 Contract의 Owner로 설정합니다.
        첫 계좌의 id는 0입니다.
        생성된 Account의 정보는 Account(str) 이벤트를 통해 확인 할 수 있습니다.
        Account 이벤트는 다음과 같은 메시지를 생성합니다.
        {
            "id": {AccountID (int)},
            "tokenType": {"ICX" or "IRC2" (str)},
            "contractAddr": {TokenType이 IRC2이면 IRC2 Contract의 주소(ICONAddr)},
            "balance": {잔액 (int)},
            "sendLimit": {하루 송금 제한 액(int)},
            "totalUsed": {하루 동안 사용한 Token 액수(int)},
            "lastUsedDate": {마지막 사용 날짜(int)},
            "dids": [{송금시 인증에 사용하는 Did 이름(str)}, ex)"kakao",...]
        }

        :param account: (str) String으로 Serialize된 JSON 형태의 Account 정보
        Account 정보에는 에는 Token Type과 Token Contract Addr, 하루 송금 제한, 인증에 활용할 did가 명시되어 있어야 합니다.
        Example)
        {
            "tokenType": {"ICX" or "IRC2" (str)},
            "contractAddr": {TokenType이 IRC2이면 IRC2 Contract의 주소(ICONAddr)},
            "sendLimit": {하루 송금 제한 액(int)},
            "dids": [{송금시 인증에 사용하는 Did 이름(str)}, ex)"kakao",...]
        }
        """
        super().on_install()
        self._add_account(account)
        self.msg.sender.to_bytes()
        self.wallet_owner.set(self.msg.sender)

    # smart wallet 생성
    def on_update(self) -> None:
        super().on_update()

    @payable
    def fallback(self):
        """ 받은 icx를 기본 계좌(account id = 0)에 추가합니다.
        """
        account = json_loads(self._accounts[0])
        account["balance"] = account["balance"] + self.msg.value
        account_as_str = json_dumps(account)
        self._accounts[0] = account_as_str

        self.Account(account_as_str)
        self.Recieve(self.msg.value)
        self.Balance(self.icx.get_balance(self.address))

    @external
    def change_new_wallet(self, did_infos: str):
        """ SmartWallet Owner를 Message Sender로 변경합니다.
        Owner를 변경하기 위해서는 모든 did 인증 데이터를 보내야 합니다.

        :param did_infos: (str) serialize된 did 인증 정보들
        """
        # TODO change to specific required dids depending on Did_SCORE
        required_dids = ["A", "B", "C"]
        #did_score = self.create_interface_score(self._did_address.get(), DidScore)
        did_infos_as_dict = json_loads(did_infos)
        # for did in required_dids:
        #     if not did_score.auth(did, self.address.body+self.tx.origin, did_infos[did]):
        #         self.revert(f"Authentication failed ")
        # owner update / test 필요

    @payable
    def tokenFallback(self, _from: Address, _value: int, _data: bytes=b''):
        pass

    @only_owner
    @external
    def transfer(self, account_id: int, token_type: str, contract_addr: str, to: str, amount: int):
        """ SmartWallet의 Account에 송금을 요청합니다.
        송금을 시도하는 Account에 did 인증 요구사항이 있을 경우 송금 요청은 Pending 됩니다.
        송금이 Pending 될 경우 Pending 이벤트를 발생합니다.
        Pending Event를 통해 Pending된 송금 요청의 id와 did인증 정보를 알 수 있습니다.
        송금을 시도하는 Account에 did 인증 요구사항이 없을 경우 송금 요청을 바로 실행합니다.
        송금이 성공할 경우 TransferSuccess 이벤트를 발생합니다.

        :param account_id: (int) 송금하는 계좌의 id
        :param token_type: (str) 송금하는 Token Type ("ICX" or "IRC2")
        :param contract_addr: (str) 송금을 처리하는 Contract의 주소 (ICX의 경우 "")
        :param to: (str) 송금을 전송받는 계좌의 ICON Address
        :param amount: (int) 송금 수량
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
        """ Pending된 송금 요청을 did 인증을 통해 승인합니다.
        모든 승인을 완료하면 송금 요청을 실행합니다.
        추가 승인이 필요하면 Pending 이벤트를 발생해 새로운 Pending 이벤트를 발생합니다.

        :param tx_id: (int) 승인하는 Transaction ID
        :param did: (str) 승인하는 did 이름
        :param auth_proof: (str) did 인증 정보
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
