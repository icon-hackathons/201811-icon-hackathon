from typing import List

from iconservice import IconScoreDatabase, VarDB, DictDB, json_dumps, json_loads, IconScoreBase

LAST_TX_ID = 'LastTxId'
PENDING_TX = 'PendingTx'
PENDING_TX_ID_LIST = 'PendingTxIdList'


class PendingTxDbProxy:
    def __init__(self, db: IconScoreDatabase):
        self._last_pending_tx_id_db = VarDB(LAST_TX_ID, db, int)
        self._pending_tx_list = DictDB(PENDING_TX, db, str, 1)
        self._pending_tx_id_list_db = VarDB(PENDING_TX_ID_LIST, db, str)

    def add(self, account_id, token_type, contract_addr, to, amount, dids) -> str:
        """

        :param account_id:
        :param token_type:
        :param contract_addr:
        :param to:
        :param amount:
        :param dids:
        :return:
        """
        # get need data
        last_tx_id = self._last_pending_tx_id_db.get() + 1

        pending_tx_id_list_as_str = self._pending_tx_id_list_db.get()
        if pending_tx_id_list_as_str == "":
            pending_tx_id_list_as_str = json_dumps([])

        pending_tx_id_list = json_loads(pending_tx_id_list_as_str)

        # create pending tx
        pending_tx = {
            "id": last_tx_id,
            "tokenType": token_type,
            "contractAddr": contract_addr,
            "from": account_id,
            "to": to,
            "amount": amount,
            "dids": dids
        }

        # update db
        pending_tx_as_str = json_dumps(pending_tx)
        self._pending_tx_list[last_tx_id] = pending_tx_as_str
        self._last_pending_tx_id_db.set(last_tx_id)
        pending_tx_id_list.append(last_tx_id)
        self._pending_tx_id_list_db.set(json_dumps(pending_tx_id_list))
        return pending_tx_as_str

    def get(self, tx_id: int) -> dict:
        if self._pending_tx_list[tx_id] != "":
            return json_loads(self._pending_tx_list[tx_id])
        return {}

    def remove(self, tx_id: int):
        del self._pending_tx_list[tx_id]
        pending_tx_id_list = json_loads(self._pending_tx_id_list_db.get())  # type: List
        pending_tx_id_list.remove(tx_id)
        self._pending_tx_id_list_db.set(json_dumps(pending_tx_id_list))

    def update(self, pending_tx: dict):
        self._pending_tx_list[pending_tx["id"]] = json_dumps(pending_tx)
