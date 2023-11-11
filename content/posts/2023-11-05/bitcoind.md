---
title: "Bitcoin"
date: 2023-11-05T14:10:43-05:00
tags: ['Bitcoin']
draft: false
---

## bitcoin.conf
```
 cat /home/yyh/.bitcoin/bitcoin.conf
# testnet=1
datadir=/media/yyh/FDFA-FF1F/bitcoin
listen=1
server=1
daemon=1
rpcuser=yyh
rpcpassword=xxxxxxxxxxxxx
rpcallowip=127.0.0.1
rpcbind=127.0.0.1
rest=1
deprecatedrpc=generate
txindex=1
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
zmqpubhashtx=tcp://127.0.0.1:28334
zmqpubhashblock=tcp://127.0.0.1:28335
[test]
listen=1
server=1
daemon=1
rpcuser=yyh
rpcpassword=xxxxxxxxxxxxx
rpcallowip=127.0.0.1
rpcbind=127.0.0.1
rest=1
deprecatedrpc=generate
txindex=1
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
zmqpubhashtx=tcp://127.0.0.1:28334
zmqpubhashblock=tcp://127.0.0.1:28335
```
## Scipt
### scriptSig
```
[Sig] [PK] OP_DUP op_HASH160 [PKHash] OP_EQUALVERIFY OP_CHECKSIG
```
## bitcoin-cli command examples
### createwallet
```
bitcoin-cli createwallet "Your name"
```
### createwallet
```
bitcoin-cli getnewaddress
bitcoin-cli getnewaddress "p2sh_address" p2sh-segwit
bitcoin-cli getnewaddress "legacy_address" legacy
```
### listunspent
```
bitcoin-cli listunspent
{
    "txid": "fce1294d8b38ea17c1a64e4956d8eff648df839bf3d82f814f80463da28f06f4",
    "vout": 0,
    "address": "2NBP3w5m425n12RePYQoJfsznTXnJr4yGiY",
    "label": "",
    "redeemScript": "0014d46fdaa84262a27cd923ed1b7b4d873c97696084",
    "scriptPubKey": "a914c6ed32ba1058fb436e5cc594710f30bd22a3916987",
    "amount": 50.00000000,
    "confirmations": 126,
    "spendable": true,
    "solvable": true,
    "desc": "sh(wpkh([d697f246/0'/0'/0']029533e360bc3d270c0ace89dd5527190d1d3394a269cae64c89860d20fea701eb))#wj2c7p26",
    "safe": true
},
```
### createrawtransaction
```
RECIPIENT_ADDRESS= 2MsjDqTpNzHKF3CC91swUiGQD44fG8SNfF5
CHANGE_ADDRESS= 2NFG69VfkBYLTzbp8xSaWgNt9Y2gSLjywrQ
MY_UTXO_TXID=fce1294d8b38ea17c1a64e4956d8eff648df839bf3d82f814f80463da28f06f4
MY_UTXO_VOUT=0
bitcoin-cli createrawtransaction 
'[{
"txid" : "'$MY_UTXO_TXID'",
"vout" : '$MY_UTXO_VOUT'
}]'
'{
"'$RECIPIENT_ADDRESS'": 25,
"'$CHANGE_ADDRESS'": 24.99
}'
```
### decoderawtransaction
```
MY_RAW_TX=0200000001f4068fa23d46804f812fd8f39b83df48f6efd856494ea6c117ea388b4d29e1fc0000000000ffffffff0200f902950000000017a914054b851d49d9c9ffca96ef8d781bbfac5b6ee34a87c0b6f3940000000017a914f17ca3410e454656105b854fd7827ecd1ecbbedd8700000000
bitcoin-cli decoderawtransaction $MY_RAW_TX
```
### signrawtranactionwithwallet
```
bitcoin-cli signrawtranactionwithwallet $MY_RAW_TX 
```
### sendrawtransaction 
```
MY_SIGNED_RAW_TX=02000000000101f4068fa23d46804f812fd8f39b83df48f6efd856494ea6c117ea388b4d29e1fc0000000017160014d46fdaa84262a27cd923ed1b7b4d873c97696084ffffffff0200f902950000000017a914054b851d49d9c9ffca96ef8d781bbfac5b6ee34a87c0b6f3940000000017a914f17ca3410e454656105b854fd7827ecd1ecbbedd870247304402204506219bcae5940360d16d6f9764226b5cad65fd41153de7ff955a2a6460a5c902200b3bcd9c83a34635ab46fe2111124d7e991b5e50a20380a21e2911539ae8724e0121029533e360bc3d270c0ace89dd5527190d1d3394a269cae64c89860d20fea701eb00000000
bitcoin-cli sendrawtransaction $MY_SIGNED_RAW_TX
```
### gettransaction 
```
bitcoin-cli gettransaction dda761617c08b443ef652be64485b1741e128fe63b79d689186f0e974ef0b1be
```
