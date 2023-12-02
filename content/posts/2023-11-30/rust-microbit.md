---
title: "Rust Microbit"
date: 2023-11-30T22:29:56-05:00
draft: false
---

## Introduction
This post is based on the [Discovery book](https://docs.rust-embedded.org/discovery/microbit/01-background/index.html)

## Tools
* `gdb-multiarch`
* `cargo-binutils`
```
$ cargo install cargo-binutils
$ rustup component add llvm-tools-preview
$ cargo nm --release
$ cargo nm --release -- --print-size --size-sort
$ cargo objcopy --release -- -O binary app.bin
$ cargo objdump --release -- --disassemble --no-show-raw-insn
$ cargo size --release -- -A -x
$ stat --printf="%s\n" target/release/hello
```
* [`cargo-embed`](https://probe.rs/docs/tools/cargo-embed/)
```
sudo apt install -y pkg-config libusb-1.0-0-dev libftdi1-dev libudev-dev libssl-dev
```
cargo-embed is the big brother of cargo-flash.
It can also flash a target just like cargo-flash, but it can also open an RTT terminal as well as a GDB server.
* `minicom`
```
$ sudo apt-get install gdb-multiarch minicom
```
Create this file in /etc/udev/rules.d with the content shown below.
```
$ cat /etc/udev/rules.d/99-microbit.rules
# CMSIS-DAP for microbit
SUBSYSTEM=="usb", ATTR{idVendor}=="0d28", ATTR{idProduct}=="0204", MODE:="666"
```
Then reload the udev rules with:
```
$ sudo udevadm control --reload-rules
```
