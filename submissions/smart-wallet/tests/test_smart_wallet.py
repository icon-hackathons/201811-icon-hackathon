""" Testcases for Smart Wallet

"""
import json
from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock

from iconservice import Address, IconScoreBase
from iconservice.base.address import AddressPrefix
from iconservice.base.message import Message
from iconservice.database.db import ContextDatabase, IconScoreDatabase

from tests.mocks import MockKeyValueDatabase
from smart_wallet.smart_wallet import SmartWallet
from smart_wallet.utils import only_owner


class TestSmartWallet(TestCase):
    sender = Address(AddressPrefix(0), b"1"*20)

    def setUp(self):
        self.key_value_mock = MockKeyValueDatabase({})
        self.db = IconScoreDatabase(self.sender, ContextDatabase(self.key_value_mock))
        IconScoreBase.get_owner = lambda score_object, score_address: self.sender

        self.smart_wallet = SmartWallet(self.db)
        type(self.smart_wallet).msg = PropertyMock(return_value=Message(sender=self.sender, value=10000))

        # print test name
        print(f"===== {self._testMethodName} ==========================")

    def tearDown(self):
        print("=================================================")

    def test_add_account(self):
        """
        GIVEN account to put
        WHEN on_install and call from the method `add_account`
        THEN _accounts have all of accounts (3)
        """
        # GIVEN
        SmartWallet.Account = lambda _self, acccount: None
        # WHEN
        sample_account = {
            "id": 0,
            "tokenType": "test_token_type",
            "contractAddr": "test_contract_addr",
            "balance": "test_balance",
            "sendLimit": "test_send_limit",
            "totalUsed": "test_total_used",
            "lastUsedDate": "test_last_used_date",
            "dids": "test_dids"
        }
        str_sample_account = json.dumps(sample_account)
        self.smart_wallet.on_install(str_sample_account)
        self.smart_wallet.add_account(str_sample_account)
        self.smart_wallet.add_account(str_sample_account)
        # THEN
        assert len(self.smart_wallet._accounts) == 3

    def test_change_setting_value(self):
        """
        GIVEN the previous account
        WHEN the previous account is updated
        THEN the account change to the new one
        """
        # GIVEN
        SmartWallet.Account = lambda _self, account: None
        sample_account = {
            "id": 0,
            "tokenType": "test_token_type",
            "contractAddr": "test_contract_addr",
            "balance": "test_balance",
            "sendLimit": "test_send_limit",
            "totalUsed": "test_total_used",
            "lastUsedDate": "test_last_used_date",
            "dids": "test_dids"
        }
        str_sample_account = json.dumps(sample_account)
        self.smart_wallet.on_install(str_sample_account)
        self.smart_wallet.add_account(str_sample_account)
        # WHEN
        sample_account["id"] = 1
        sample_account["tokenType"] = "new"
        str_sample_account = json.dumps(sample_account)
        self.smart_wallet._change_setting_value(account=str_sample_account)
        json_sample_account = json.loads(self.smart_wallet._accounts[1])
        # THEN
        self.assertEqual(json_sample_account["tokenType"], "new")

    @only_owner
    def _test_only_owner(self):
        pass

    def test_only_owner(self):
        self.msg = MagicMock(return_value=self.smart_wallet.owner)
        self.msg.sender = self.msg()
        self.owner = self.msg()
        self._test_only_owner()

        self.msg.sender = 123
        self.assertRaises(AttributeError, self._test_only_owner)





