""" Testcases for wallet manager

"""
import json
from datetime import datetime
from unittest import TestCase
from unittest.mock import PropertyMock

from iconservice import Address, IconScoreBase, DictDB, VarDB
from iconservice.base.address import AddressPrefix
from iconservice.base.exception import RevertException
from iconservice.base.message import Message
from iconservice.database.db import ContextDatabase, IconScoreDatabase
from iconservice.iconscore.icon_score_base2 import Block
from iconservice.iconscore.icx import Icx
from traitlets import Dict

from smart_wallet.pending_tx_db_proxy import PENDING_TX_ID_LIST, LAST_TX_ID
from tests.mocks import MockKeyValueDatabase
from smart_wallet.smart_wallet import SmartWallet, PENDING_TX


class TestWalletManager(TestCase):
    sender = Address(AddressPrefix(0), b"1"*20)

    def setUp(self):
        self.key_value_mock = MockKeyValueDatabase({})
        self.db = IconScoreDatabase(self.sender, ContextDatabase(self.key_value_mock))
        IconScoreBase.get_owner = lambda score_object, score_address: self.sender

        self.smart_wallet = SmartWallet(self.db)
        type(self.smart_wallet).msg = PropertyMock(return_value=Message(sender=self.sender, value=10000))
        SmartWallet.Account = lambda _self, account: None
        self.smart_wallet.on_install(json.dumps({
            "id": 0,
            "tokenType": "icx",
            "balance": 3000,
            "sendLimit": 1000,
            "totalUsed": 500,
            "lastUsedDate": "2018-11-21",
            "dids": []
        })
        )
        # print test name
        print("=====================================================")
        print(f"{self._testMethodName}")

    def tearDown(self):
        print(f"end test")
        print("=====================================================")

    def test_transfer_direct_send(self):
        """GIVEN an account that has token icx and required did is nothing
        WHEN send icx lower than today used_limits
        THEN account update balance and limit and register event send_transaction
        """
        # GIVEN
        self.__setup_no_did_transfer_env()

        def TransferSuccessMock(contract, account_id: int, token_type: str, token_address: str, to: str, amount: int):
            self.assertEqual(0, account_id)
            self.assertEqual("icx", token_type)
            self.assertEqual("", token_address)
            self.assertEqual("hx111111111111111111111111111111111111111111", to)
            self.assertEqual(500, amount)

        SmartWallet.TransferSuccess = TransferSuccessMock

        # WHEN
        self.smart_wallet.transfer(account_id=0,
                                   token_type="icx",
                                   contract_addr="",
                                   to="hx111111111111111111111111111111111111111111",
                                   amount=500)

        # THEN
        updated_account = json.loads(self.smart_wallet._accounts[0])
        self.assertEqual(updated_account["totalUsed"], 1000)
        self.assertEqual(updated_account["balance"], 2500)

    def __setup_no_did_transfer_env(self):
        Icx.transfer = lambda contract, addr_to, amount: None
        self.smart_wallet._accounts = [json.dumps({
            "id": 0,
            "tokenType": "icx",
            "balance": 3000,
            "sendLimit": 1000,
            "totalUsed": 500,
            "lastUsedDate": "2018-11-21",
            "dids": []
        })]
        type(self.smart_wallet).block = PropertyMock(return_value=Block(0, 1542773377))

    def test_transfer_amount_is_higher_than_balance_must_raise_revert(self):
        # GIVEN
        self.__setup_no_did_transfer_env()
        # WHEN THEN

        self.assertRaises(RevertException, self.smart_wallet.transfer,
                          account_id=0,
                          token_type="icx",
                          contract_addr="",
                          to="hx111111111111111111111111111111111111111111",
                          amount=3500)

    def test_transfer_amount_is_higher_than_left_today_limit_must_raise_revert(self):
        # GIVEN
        self.__setup_no_did_transfer_env()
        # WHEN THEN

        self.assertRaises(RevertException, self.smart_wallet.transfer,
                          account_id=0,
                          token_type="icx",
                          contract_addr="",
                          to="hx111111111111111111111111111111111111111111",
                          amount=600)

    def test_transfer_amount_is_higher_than_left_today_limit_but_can_if_day_change(self):
        # GIVEN
        self.__setup_no_did_transfer_env()
        # setup last date is 11_21
        ts_11_23 = 1542993377
        type(self.smart_wallet).block = PropertyMock(return_value=Block(0, ts_11_23))

        # THEN
        def TransferSuccessMock(contract, account_id: int, token_type: str, token_address: str, to: str, amount: int):
            self.assertEqual(0, account_id)
            self.assertEqual("icx", token_type)
            self.assertEqual("", token_address)
            self.assertEqual("hx111111111111111111111111111111111111111111", to)
            self.assertEqual(600, amount)

        SmartWallet.TransferSuccess = TransferSuccessMock
        # WHEN
        self.smart_wallet.transfer(account_id=0,
                                   token_type="icx",
                                   contract_addr="",
                                   to="hx111111111111111111111111111111111111111111",
                                   amount=600)
        # THEN
        account = json.loads(self.smart_wallet._accounts[0])
        self.assertEqual(2400, account["balance"])
        self.assertEqual(600, account["totalUsed"])
        self.assertEqual("2018-11-23", account["lastUsedDate"])

    def test_pending_transaction(self):
        """ GIVEN account with did_list not empty
        WHEN call transfer with transferable info
        THEN a transaction will be pending
        """
        # GIVEN
        self.__setup_processing_pending_tx()

        # THEN
        def PendingMock(_self, pending_tx: str):
            print(pending_tx)
            pending_tx_as_dict = json.loads(pending_tx)
            self.assertEqual(1, pending_tx_as_dict["id"])
            self.assertEqual(0, pending_tx_as_dict["from"])
            self.assertEqual("hx"+"1"*40, pending_tx_as_dict["to"])
            self.assertEqual("icx", pending_tx_as_dict["tokenType"])
            self.assertEqual("", pending_tx_as_dict["contractAddr"])
            self.assertEqual(500, pending_tx_as_dict["amount"])
            self.assertEqual(["kakao", "chainId"], pending_tx_as_dict["dids"])

        SmartWallet.Pending = PendingMock

        # WHEN
        self.smart_wallet.transfer(account_id=0,
                                   token_type="icx",
                                   contract_addr="",
                                   to="hx"+"1"*40,
                                   amount=500)

        # THEN
        pending_tx_db = DictDB(PENDING_TX, self.smart_wallet.db, str, 1)
        pending_tx_as_dict = json.loads(pending_tx_db[1])
        self.assertEqual(1, pending_tx_as_dict["id"])
        self.assertEqual(0, pending_tx_as_dict["from"])
        self.assertEqual("hx" + "1" * 40, pending_tx_as_dict["to"])
        self.assertEqual("icx", pending_tx_as_dict["tokenType"])
        self.assertEqual("", pending_tx_as_dict["contractAddr"])
        self.assertEqual(500, pending_tx_as_dict["amount"])
        self.assertEqual(["kakao", "chainId"], pending_tx_as_dict["dids"])

        pending_tx_list = json.loads(VarDB(PENDING_TX_ID_LIST, self.smart_wallet.db, str).get())
        self.assertEqual(1, len(pending_tx_list))
        self.assertEqual(1, pending_tx_list[0])

        last_tx_id = VarDB(LAST_TX_ID, self.smart_wallet.db, int).get()
        self.assertEqual(1, last_tx_id)

    def __setup_processing_pending_tx(self):
        Icx.transfer = lambda contract, addr_to, amount: None
        self.smart_wallet._accounts = [json.dumps({
            "id": 0,
            "tokenType": "icx",
            "balance": 3000,
            "sendLimit": 1000,
            "totalUsed": 500,
            "lastUsedDate": "2018-11-21",
            "dids": ["kakao", "chainId"]
        })]
        type(self.smart_wallet).block = PropertyMock(return_value=Block(0, 1542773377))

    def test_approval(self):
        """ GIVEN account with two dids, and pending one tx from that account,
        WHEN call approval twice
        THEN first approval remove dids in pending tx, second remove pending tx
        with TransferSuccess event
        """
        # GIVEN
        self.__setup_processing_pending_tx()
        SmartWallet.Pending = lambda _self, pending_tx: None

        self.smart_wallet.transfer(account_id=0,
                                   token_type="icx",
                                   contract_addr="",
                                   to="hx"+"1"*40,
                                   amount=500)

        # first WHEN
        def FirstApprovalMock(_self, tx_id, did):
            self.assertEqual(1, tx_id)
            self.assertEqual("kakao", did)
        SmartWallet.Approval = FirstApprovalMock
        self.smart_wallet.approval(1, "kakao", "true")

        # first THEN
        pending_tx_db = DictDB(PENDING_TX, self.smart_wallet.db, str, 1)
        pending_tx_as_dict = json.loads(pending_tx_db[1])
        self.assertEqual(["chainId"], pending_tx_as_dict["dids"])

        # second WHEN
        def SecondApprovalMock(_self, tx_id, did):
            self.assertEqual(1, tx_id)
            self.assertEqual("chainId", did)

        SmartWallet.Approval = SecondApprovalMock
        SmartWallet.TransferSuccess = lambda _self, account_id, token_type, contract_addr, to, amount: None

        self.smart_wallet.approval(1, "chainId", "true")

        # second THEN
        self.assertEqual("", pending_tx_db[1])
        self.assertEqual(json.dumps([]), VarDB(PENDING_TX_ID_LIST, self.smart_wallet.db, str).get())

    def test_transfer_account_to_account(self):
        """ GIVEN two accounts
        WHEN to address is 1
        THEN transfer success to account
        """
        # GIVEN
        self.__setup_no_did_transfer_env()
        self.smart_wallet._accounts\
            .append(json.dumps({
                    "id": 1,
                    "tokenType": "icx",
                    "balance": 3000,
                    "sendLimit": 1000,
                    "totalUsed": 500,
                    "lastUsedDate": "2018-11-21",
                    "dids": ["kakao", "chainId"]
            })
        )

        def TransferSuccessMock(contract, account_id: int, token_type: str, token_address: str, to: str, amount: int):
            self.assertEqual(0, account_id)
            self.assertEqual("icx", token_type)
            self.assertEqual("", token_address)
            self.assertEqual("1", to)
            self.assertEqual(500, amount)

        SmartWallet.TransferSuccess = TransferSuccessMock

        self.smart_wallet.transfer(0, "icx", "", "1", 500)

        # THEN
        account0 = json.loads(self.smart_wallet._accounts[0])
        assert account0['balance'] == 2500
        assert account0['totalUsed'] == 1000

        account1 = json.loads(self.smart_wallet._accounts[1])
        assert  account1['balance'] == 3500
