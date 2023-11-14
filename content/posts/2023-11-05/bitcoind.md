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
bitcoin-cli listunspent 6 9999999 "[\"bc1q09vm5lfy0j5reeulh4x5752q25uqqvz34hufdl\",\"bc1q02ad21edsxd23d32dfgqqsz4vv4nmtfzuklhy3\"]"
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

Example: 
list the Bitcoin under `tb1qwfe95s7n84m7jhg73jhjhjhw5zxn6dcuslscvq` and `mrvYcFxF7Gv4PFj6ubizkDUq5LpKaCGp8F` and send most of Bitcoin in the first address to the second one. 
```shell
❯ bitcoin-cli listunspent 6 9999999 "[\"tb1qwfe95s7n84m7jhg73jhjhjhw5zxn6dcuslscvq\",\"mrvYcFxF7Gv4PFj6ubizkDUq5LpKaCGp8F\"]"
[
  {
    "txid": "8599a988804b7488af1be084b18c9aefb3aac74cbc984830dd55b85b7e1ea490",
    "vout": 1,
    "address": "mrvYcFxF7Gv4PFj6ubizkDUq5LpKaCGp8F",
    "label": "legacy_address_test",
    "scriptPubKey": "76a9147d1f983284eab6a1e70d7ff6336d029b7df44ae188ac",
    "amount": 0.00009438,
    "confirmations": 122,
    "spendable": true,
    "solvable": true,
    "desc": "pkh([fad7c683/44h/1h/0h/0/0]0244bb42905a1b0572de0647de39153673cdbc7e8dc5ef8884426fab3cc22822df)#pvgva5zt",
    "parent_descs": [
      "pkh(tpubD6NzVbkrYhZ4YVfCH3s4XS8iyrqQ9yiv8K4WJhtqZc6jWKFwtnFxxrxnY8Rjhc2wEgaajcU17YnThxuy5jr9nNCV3nC3bgXdA9MLM5XDMkw/44h/1h/0h/0/*)#zxepd3y0"
    ],
    "safe": true
  },
  {
    "txid": "ef94f7eb2ca75b5211ed3568a638a2e42af2e036ab9d42f87831e0cb771b2b5d",
    "vout": 0,
    "address": "tb1qwfe95s7n84m7jhg73jhjhjhw5zxn6dcuslscvq",
    "label": "",
    "scriptPubKey": "001472725a43d33d77e95d1e8caf2bcaeea08d3d371c",
    "amount": 0.00001000,
    "confirmations": 122,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([fad7c683/84h/1h/0h/0/0]02a71e3f2089d647ee4b4c216694a669d5018c64dd0f1de275c94286657b4b354c)#tdzra023",
    "parent_descs": [
      "wpkh(tpubD6NzVbkrYhZ4YVfCH3s4XS8iyrqQ9yiv8K4WJhtqZc6jWKFwtnFxxrxnY8Rjhc2wEgaajcU17YnThxuy5jr9nNCV3nC3bgXdA9MLM5XDMkw/84h/1h/0h/0/*)#g9zsqe7n"
    ],
    "safe": true
  }
]

❯ bitcoin-cli createrawtransaction "[{\"txid\":\"ef94f7eb2ca75b5211ed3568a638a2e42af2e036ab9d42f87831e0cb771b2b5d\",\"vout\":0}]" "[{\"mrvYcFxF7Gv4PFj6ubizkDUq5LpKaCGp8F\":0.0000085}]"

02000000015d2b1b77cbe03178f8429dab36e0f22ae4a238a66835ed11525ba72cebf794ef0000000000fdffffff0152030000000000001976a9147d1f983284eab6a1e70d7ff6336d029b7df44ae188ac00000000
❯ MY_RAW_TX=02000000015d2b1b77cbe03178f8429dab36e0f22ae4a238a66835ed11525ba72cebf794ef0000000000fdffffff0152030000000000001976a9147d1f983284eab6a1e70d7ff6336d029b7df44ae188ac00000000
❯ bitcoin-cli signrawtransactionwithwallet $MY_RAW_TX
{
  "hex": "020000000001015d2b1b77cbe03178f8429dab36e0f22ae4a238a66835ed11525ba72cebf794ef0000000000fdffffff0152030000000000001976a9147d1f983284eab6a1e70d7ff6336d029b7df44ae188ac0247304402201b827571701a4394f5d14b99fe09faef564b15f1af8daba10648f4a62adb33a702205dc21af56171b1245ba8dc06898da90965204ed2f16a36a95740a2a0a36dfa39012102a71e3f2089d647ee4b4c216694a669d5018c64dd0f1de275c94286657b4b354c00000000",
  "complete": true
}
❯ MY_SIGNED_RAW_TX=020000000001015d2b1b77cbe03178f8429dab36e0f22ae4a238a66835ed11525ba72cebf794ef0000000000fdffffff0152030000000000001976a9147d1f983284eab6a1e70d7ff6336d029b7df44ae188ac0247304402201b827571701a4394f5d14b99fe09faef564b15f1af8daba10648f4a62adb33a702205dc21af56171b1245ba8dc06898da90965204ed2f16a36a95740a2a0a36dfa39012102a71e3f2089d647ee4b4c216694a669d5018c64dd0f1de275c94286657b4b354c00000000
❯ bitcoin-cli sendrawtransaction $MY_SIGNED_RAW_TX
8679b1b0ac9d842ad618438da422f25e7f5336e2f48ab334a256782b9a6f38d6

```