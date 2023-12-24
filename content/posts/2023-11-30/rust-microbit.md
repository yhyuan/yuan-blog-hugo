---
title: "Rust Microbit on Ubuntu"
date: 2023-11-30T22:29:56-05:00
tags: ['Rust', 'Microbit', 'Ubuntu']
draft: false
---

## Introduction
This post is based on the [Discovery book](https://docs.rust-embedded.org/discovery/microbit/01-background/index.html)

## Tools
* `gdb-multiarch`
* `cargo-binutils`
```shell
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
```shell
sudo apt install -y pkg-config libusb-1.0-0-dev libftdi1-dev libudev-dev libssl-dev
```
cargo-embed is the big brother of cargo-flash.
It can also flash a target just like cargo-flash, but it can also open an RTT terminal as well as a GDB server.
* `minicom`
```shell
$ sudo apt-get install gdb-multiarch minicom
```
Create this file in /etc/udev/rules.d with the content shown below.
```shell
$ cat /etc/udev/rules.d/99-microbit.rules
# CMSIS-DAP for microbit
SUBSYSTEM=="usb", ATTR{idVendor}=="0d28", ATTR{idProduct}=="0204", MODE:="666"
```
Then reload the udev rules with:
```shell
$ sudo udevadm control --reload-rules
```
```shell
$ lsusb | grep -i "NXP ARM mbed"
Bus 001 Device 065: ID 0d28:0204 NXP ARM mbed
$ # ^^^        ^^^
```
modify `Embed.toml`
```toml
[default.general]
# chip = "nrf52833_xxAA" # uncomment this line for micro:bit V2
# chip = "nrf51822_xxAA" # uncomment this line for micro:bit V1
```
Next run one of these commands:
```shell
$ # make sure you are in src/03-setup of the books source code
$ # If you are working with micro:bit v2
$ rustup target add thumbv7em-none-eabihf
$ cargo embed --target thumbv7em-none-eabihf

$ # If you are working with micro:bit v1
$ rustup target add thumbv6m-none-eabi
$ cargo embed --target thumbv6m-none-eabi
```

### main.rs
```rust
#![deny(unsafe_code)]
#![no_main]
#![no_std]

use cortex_m_rt::entry;
use panic_halt as _;
use microbit as _;

#[entry]
fn main() -> ! {
    let _y;
    let x = 42;
    _y = x;

    // infinite loop; just so we don't leave this stack frame
    loop {}
}
```
`Embed.toml`
```toml
[default.general]
# chip = "nrf52833_xxAA" # uncomment this line for micro:bit V2
# chip = "nrf51822_xxAA" # uncomment this line for micro:bit V1

[default.reset]
halt_afterwards = true

[default.rtt]
enabled = false

[default.gdb]
enabled = true
```
This file tells cargo-embed that:

* we are working with either a nrf52833 or nrf51822, you will again have to remove the comments from the chip you are using, just like you did in chapter 3.
* we want to halt the chip after we flashed it so our program does not instantly jump to the loop
* we want to disable RTT, RTT being a protocol that allows the chip to send text to a debugger. You have in fact already seen RTT in action, it was the protocol that sent "Hello World" in chapter 3.
* we want to enable GDB, this will be required for the debugging procedure

```shell
cargo build --features v2 --target thumbv7em-none-eabihf
cargo readobj --features v2 --target thumbv7em-none-eabihf --bin led-roulette -- --file-headers
cargo embed --features v2 --target thumbv7em-none-eabihf
gdb-multiarch target/thumbv7em-none-eabihf/debug/led-roulette
(gdb) target remote :1337
(gdb) break main
(gdb) layout src
(gdb) break 13
(gdb) tui disable
(gdb) print x
(gdb) print &x
(gdb) next
(gdb) info locals
```

### rtt_target
```rust
#![deny(unsafe_code)]
#![no_main]
#![no_std]

use cortex_m_rt::entry;
use rtt_target::{rtt_init_print, rprintln};
use panic_rtt_target as _;
use microbit::board::Board;
use microbit::hal::timer::Timer;
use microbit::hal::prelude::*;

#[entry]
fn main() -> ! {
    rtt_init_print!();
    let mut board = Board::take().unwrap();

    let mut timer = Timer::new(board.TIMER0);

    loop {
        timer.delay_ms(1000u16);
        rprintln!("1000 ms passed");
    }
}
```

In order to actually see the prints we have to change Embed.toml like this:

```toml
[default.general]
# chip = "nrf52833_xxAA" # uncomment this line for micro:bit V2
# chip = "nrf51822_xxAA" # uncomment this line for micro:bit V1

[default.reset]
halt_afterwards = false

[default.rtt]
enabled = true

[default.gdb]
enabled = false
```
```shell
cargo embed
```
main.rs
```rust
#![deny(unsafe_code)]
#![no_main]
#![no_std]

use cortex_m_rt::entry;
use rtt_target::{rtt_init_print, rprintln};
use panic_rtt_target as _;
use microbit::board::Board;
use microbit::hal::timer::Timer;
use microbit::hal::prelude::*;

#[entry]
fn main() -> ! {
    rtt_init_print!();
    let mut board = Board::take().unwrap();

    let mut timer = Timer::new(board.TIMER0);

    board.display_pins.col1.set_low().unwrap();
    let mut row1 = board.display_pins.row1;

    loop {
        row1.set_low().unwrap();
        rprintln!("Dark!");
        timer.delay_ms(1_000_u16);
        row1.set_high().unwrap();
        rprintln!("Light!");
        timer.delay_ms(1_000_u16);
    }
}
```
### UART
```rust
#![no_main]
#![no_std]

use cortex_m_rt::entry;
use rtt_target::rtt_init_print;
use panic_rtt_target as _;

#[cfg(feature = "v1")]
use microbit::{
    hal::prelude::*,
    hal::uart,
    hal::uart::{Baudrate, Parity},
};

#[cfg(feature = "v2")]
use microbit::{
    hal::prelude::*,
    hal::uarte,
    hal::uarte::{Baudrate, Parity},
};

#[cfg(feature = "v2")]
mod serial_setup;
#[cfg(feature = "v2")]
use serial_setup::UartePort;

#[entry]
fn main() -> ! {
    rtt_init_print!();
    let board = microbit::Board::take().unwrap();

    #[cfg(feature = "v1")]
    let mut serial = {
        uart::Uart::new(
            board.UART0,
            board.uart.into(),
            Parity::EXCLUDED,
            Baudrate::BAUD115200,
        )
    };

    #[cfg(feature = "v2")]
    let mut serial = {
        let serial = uarte::Uarte::new(
            board.UARTE0,
            board.uart.into(),
            Parity::EXCLUDED,
            Baudrate::BAUD115200,
        );
        UartePort::new(serial)
    };

    nb::block!(serial.write(b'X')).unwrap();
    nb::block!(serial.flush()).unwrap();

    loop {}
}
```
### write! and core::fmt::Write
```rust
#![no_main]
#![no_std]

use cortex_m_rt::entry;
use rtt_target::rtt_init_print;
use panic_rtt_target as _;
use core::fmt::Write;

#[cfg(feature = "v1")]
use microbit::{
    hal::prelude::*,
    hal::uart,
    hal::uart::{Baudrate, Parity},
};

#[cfg(feature = "v2")]
use microbit::{
    hal::prelude::*,
    hal::uarte,
    hal::uarte::{Baudrate, Parity},
};

#[cfg(feature = "v2")]
mod serial_setup;
#[cfg(feature = "v2")]
use serial_setup::UartePort;

#[entry]
fn main() -> ! {
    rtt_init_print!();
    let board = microbit::Board::take().unwrap();

    #[cfg(feature = "v1")]
    let mut serial = {
        uart::Uart::new(
            board.UART0,
            board.uart.into(),
            Parity::EXCLUDED,
            Baudrate::BAUD115200,
        )
    };

    #[cfg(feature = "v2")]
    let mut serial = {
        let serial = uarte::Uarte::new(
            board.UARTE0,
            board.uart.into(),
            Parity::EXCLUDED,
            Baudrate::BAUD115200,
        );
        UartePort::new(serial)
    };

    write!(serial, "The quick brown fox jumps over the lazy dog.\r\n").unwrap();
    nb::block!(serial.flush()).unwrap();

    loop {}
}
```

Reference: [Discovery github](https://github.com/rust-embedded/discovery)