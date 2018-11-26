# ICON SDK C#

## Requirements
* JsonDotNet
* BoundcyCastle
* System.Collections.Immutable

## How to use

#### Balance

```C#
var getBalance = new GetBalance(url);
await getBalance.Invoke(address);
```


#### SendTransaction
```C#
var txBuilder = new TransactionBuilder();
txBuilder.To = new ExtrenalAddress("3f376559204079671b6a8df481c976e7d51b3c7c");
txBuilder.PrivateKey = new PrivateKey("1746aa10d068a543c66422e62890aadd649cc23aa5838f98beb93bd7d421fa42");
txBuilder.Value = 100;
txBuilder.StepLimit = 100000000;
txBuilder.NID = 3;

var tx = txBuilder.Build();
var sendTx = new SendTransaction(url):
await sendTx.Invoke(tx);
```