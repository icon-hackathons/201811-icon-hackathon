# -*- coding: utf-8 -*-

# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""IconScoreEngine testcase
"""

import unittest
from typing import TYPE_CHECKING, Any

from iconservice.base.address import ZERO_SCORE_ADDRESS, GOVERNANCE_SCORE_ADDRESS
from tests import create_tx_hash
from tests.integrate_test.test_integrate_base import TestIntegrateBase

if TYPE_CHECKING:
    from iconservice.base.address import Address


class TestIntegrateApp(TestIntegrateBase):

    def _update_governance(self):
        tx = self._make_deploy_tx("test_builtin",
                                  "latest_version/governance",
                                  self._admin,
                                  GOVERNANCE_SCORE_ADDRESS)
        prev_block, tx_results = self._make_and_req_block([tx])
        self._write_precommit_state(prev_block)

    def _deploy_score(self, score_path: str,
                      from_addr: 'Address',
                      update_score_addr: 'Address' = None) -> Any:
        address = ZERO_SCORE_ADDRESS
        if update_score_addr:
            address = update_score_addr

        tx = self._make_deploy_tx("test_scores",
                                  score_path,
                                  from_addr,
                                  address)

        prev_block, tx_results = self._make_and_req_block([tx])
        self._write_precommit_state(prev_block)
        return tx_results[0]

    def test_app_success(self):
        self._update_governance()

        # 1. deploy
        tx_result = self._deploy_score("dapp", self._admin)
        self.assertEqual(tx_result.status, int(True))
        score_addr = tx_result.score_address

        init_icx = 10
        icx_decimals = 10 ** 18

        addr1_icx = init_icx * icx_decimals
        addr2_icx = init_icx * icx_decimals

        tx1 = self._make_icx_send_tx(self._genesis, self._addr_array[0], addr1_icx)
        tx2 = self._make_icx_send_tx(self._genesis, self._addr_array[1], addr2_icx)

        prev_block, tx_results = self._make_and_req_block([tx1, tx2])
        self._write_precommit_state(prev_block)
        self.assertEqual(tx_results[0].status, int(True))
        self.assertEqual(tx_results[1].status, int(True))

        response = self._query({"address": self._addr_array[0]}, 'icx_getBalance')
        self.assertEqual(response, addr1_icx)
        response = self._query({"address": self._addr_array[1]}, 'icx_getBalance')
        self.assertEqual(response, addr2_icx)

        # pay advance
        game_pay_icx = 1 * icx_decimals
        tx1 = self._make_score_call_tx(self._addr_array[0],
                                       score_addr,
                                       "pay_advance", {}, game_pay_icx)
        tx2 = self._make_score_call_tx(self._addr_array[1],
                                       score_addr,
                                       "pay_advance", {}, game_pay_icx)
        prev_block, tx_results = self._make_and_req_block([tx1, tx2])
        self._write_precommit_state(prev_block)
        self.assertEqual(tx_results[0].status, int(True))
        self.assertEqual(tx_results[1].status, int(True))

        addr1_icx -= game_pay_icx
        response = self._query({"address": self._addr_array[0]}, 'icx_getBalance')
        self.assertEqual(response, addr1_icx)
        addr2_icx -= game_pay_icx
        response = self._query({"address": self._addr_array[1]}, 'icx_getBalance')
        self.assertEqual(response, addr1_icx)

        # start game
        game_id = create_tx_hash()
        addr1_seed = b"addr1"
        addr1_sha = create_tx_hash(addr1_seed)
        addr2_seed = b"addr2"
        addr2_sha = create_tx_hash(addr2_seed)

        tx1 = self._make_score_call_tx(self._addr_array[0],
                                       score_addr,
                                       "start_game",
                                       {"game_id": f"0x{bytes.hex(game_id)}", "sha_key": f"0x{bytes.hex(addr1_sha)}"})
        tx2 = self._make_score_call_tx(self._addr_array[1],
                                       score_addr,
                                       "start_game",
                                       {"game_id": f"0x{bytes.hex(game_id)}", "sha_key": f"0x{bytes.hex(addr2_sha)}"})
        prev_block, tx_results = self._make_and_req_block([tx1, tx2])
        self._write_precommit_state(prev_block)
        self.assertEqual(tx_results[0].status, int(True))
        self.assertEqual(tx_results[1].status, int(True))

        # reveal_game
        tx1 = self._make_score_call_tx(self._addr_array[0],
                                       score_addr,
                                       "reveal_game",
                                       {"game_id": f"0x{bytes.hex(game_id)}", "seed_key": f"0x{bytes.hex(addr1_seed)}"})
        tx2 = self._make_score_call_tx(self._addr_array[1],
                                       score_addr,
                                       "reveal_game",
                                       {"game_id": f"0x{bytes.hex(game_id)}", "seed_key": f"0x{bytes.hex(addr2_seed)}"})
        prev_block, tx_results = self._make_and_req_block([tx1, tx2])
        self._write_precommit_state(prev_block)
        self.assertEqual(tx_results[0].status, int(True))
        self.assertEqual(tx_results[1].status, int(True))

        # result_game
        tx = self._make_score_call_tx(self._addr_array[2],
                                      score_addr,
                                      "end_game",
                                      {"game_id": f"0x{bytes.hex(game_id)}",
                                       "addr1": str(self._addr_array[0]),
                                       "addr2": str(self._addr_array[1])
                                       })
        prev_block, tx_results = self._make_and_req_block([tx])
        self._write_precommit_state(prev_block)
        self.assertEqual(tx_results[0].status, int(True))

        event_log = tx_results[0].event_logs[0]
        self.assertEqual(event_log.indexed[0], "GameResult(Address,Address,int,int)")
        self.assertEqual(event_log.data[0], self._addr_array[0])
        self.assertEqual(event_log.data[1], self._addr_array[1])

        if event_log.data[2] > event_log.data[3]:
            # win addr1
            query_request = {
                "from": self._admin,
                "to": score_addr,
                "dataType": "call",
                "data": {
                    "method": "get_deposit",
                    "params": {
                        "addr": str(self._addr_array[0])
                    }
                }
            }
            response = self._query(query_request)
            self.assertEqual(response, game_pay_icx * 2)

            query_request = {
                "from": self._admin,
                "to": score_addr,
                "dataType": "call",
                "data": {
                    "method": "get_deposit",
                    "params": {
                        "addr": str(self._addr_array[1])
                    }
                }
            }
            response = self._query(query_request)
            self.assertEqual(response, 0)
        else:
            # win addr2
            query_request = {
                "from": self._admin,
                "to": score_addr,
                "dataType": "call",
                "data": {
                    "method": "get_deposit",
                    "params": {
                        "addr": str(self._addr_array[0])
                    }
                }
            }
            response = self._query(query_request)
            self.assertEqual(response, 0)

            query_request = {
                "from": self._admin,
                "to": score_addr,
                "dataType": "call",
                "data": {
                    "method": "get_deposit",
                    "params": {
                        "addr": str(self._addr_array[1])
                    }
                }
            }
            response = self._query(query_request)
            self.assertEqual(response, game_pay_icx * 2)


if __name__ == '__main__':
    unittest.main()
