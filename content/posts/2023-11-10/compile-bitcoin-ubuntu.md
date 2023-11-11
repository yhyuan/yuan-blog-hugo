---
title: "Compile Bitcoin Ubuntu"
date: 2023-11-10T21:09:16-05:00
draft: false
---

### Install required packages
```
sudo apt-get install automake autotools-dev bsdmainutils build-essential ccache clang gcc git libboost-dev libboost-filesystem-dev libboost-system-dev libboost-test-dev libevent-dev libminiupnpc-dev libnatpmp-dev libqt5gui5 libqt5core5a libqt5dbus5 libsqlite3-dev libtool libzmq3-dev pkg-config python3 qttools5-dev qttools5-dev-tools qtwayland5 systemtap-sdt-dev
```

### Download source code
```
git clone https://github.com/bitcoin/bitcoin.git
```

### Compile
```
/autogen.sh
./configure --with-incompatible-bdb
make -j "$(($(nproc) + 1))"
sudo make install
```
Reference: [How to compile Bitcoin Core and run the unit and functional tests](https://jonatack.github.io/articles/how-to-compile-bitcoin-core-and-run-the-tests)