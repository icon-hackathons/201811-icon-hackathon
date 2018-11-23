## environments setup
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```



## Tutorial

 1. Deploy smart-wallet

 2. Send icx for store icx in SmartWallet

 3. Account structure
```json
{
    "id": len(self._accounts),
    "tokenType": token_type,
    "contractAddr": contract_addr,
    "balance": balance,
    "sendLimit": send_limit,
    "totalUsed": total_used,
    "lastUsedDate": last_used_date,
    "dids": dids
}

``` 

 4. Add account 

```python
    def add_account(self, account: str):
``` 

 5. Transfer
```python
    def transfer(self, account_id: int, token_type: str, contract_addr: str, to: str, amount: int):

```

 6. Approval pending tx 
```python
    def approval(self, tx_id: int, did: str, auth_proof: str):
```