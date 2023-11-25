---
title: "How to Set Up Rust Stm32 on Ubuntu"
date: 2023-11-24T19:12:20-05:00
draft: false
---

## Original post
This post is translated from a [Japanese Post](https://asukiaaa.blogspot.com/2023/11/run-stm32-rust-on-ubuntu.html)

## VS Code
```
sudo snap install --classic code
```
## VS Code extensions
```
cortex-debug rust-analyzer
```
## Rust
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
## rustup target add
```
rustup target add thumbv7em-none-eabihf
```
## gdb-multiarch
```
sudo apt install -y gdb-multiarch
```
## openocd
```
sudo apt install openocd
```
## Create a project and change settings for stm32f429zi 
```
cargo generate --git https://github.com/rust-embedded/cortex-m-quickstart.git
```
## Changes to .cargo/config.toml
```
[target.thumbv7m-none-eabi]
```
to
```
[target.thumbv7em-none-eabihf]
```
### runner enabled
uncomment this line. 
```
runner = "gdb-multiarch -q -x openocd.gdb"
```
### Disable old build target
```
# target = "thumbv7m-none-eabi"
```
### Enabling build target for thumbv7em-none-eabihf
```
target = "thumbv7em-none-eabihf"
```
## Download the SVD file of the microcontroller to be developed to .vscode
SVD files for stm32 are available on the page below.
https://github.com/cmsis-svd/cmsis-svd/blob/main/data/STMicro

This time it is for stm32f429zi, so I downloaded the file below.
https://github.com/cmsis-svd/cmsis-svd/blob/main/data/STMicro/STM32F429.svd

Once downloaded, place it in the .vscode directory.
 
## Changes to .vscode/launch.json
### Changed for microcontrollers that use device config svdFile
Change before
```
            "device": "STM32F303VCT6",
            "configFiles": [
                "interface/stlink-v2-1.cfg",
                "target/stm32f3x.cfg"
            ],
            "svdFile": "${workspaceRoot}/.vscode/STM32F303.svd",
```
After change
```
            "device": "STM32F429ZI",
            "configFiles": [
                "interface/stlink.cfg",
                "target/stm32f4x.cfg"
            ],
            "svdFile": "${workspaceRoot}/.vscode/STM32F429.svd",
```
### Change according to the microcontroller using the frequency
Change before
```
                "cpuFrequency": 8000000,
```
After change
```
                "cpuFrequency": 16000000,
```
## Cargo.toml changes
### Change related libraries to the latest version
Change before
```toml
[dependencies]
cortex-m = "0.6.0"
cortex-m-rt = "0.6.10"
cortex-m-semihosting = "0.3.3"
```
After change
```toml
[dependencies]
cortex-m = "0.7.7"
cortex-m-rt = "0.7.3"
cortex-m-semihosting = "0.5.0"
```
### Set HAL of target microcontroller
Change before
```toml
# [dependencies.stm32f3]
# features = ["stm32f303", "rt"]
# version = "0.7.1"
```
After change
```toml
[dependencies.stm32f4xx-hal]
features = ["stm32f429", "rt"]
version = "0.17.1"
```

## memory.x changes
Change before
```
  FLASH : ORIGIN = 0x00000000, LENGTH = 256K
  RAM : ORIGIN = 0x20000000, LENGTH = 64K
```
After change
```
  FLASH : ORIGIN = 0x08000000, LENGTH = 2048K
  RAM : ORIGIN = 0x10000000, LENGTH = 64K
```
## Changes to openocd.cfg
Change before
```
source [find target/stm32f3x.cfg]
```
After change
```
source [find target/stm32f4x.cfg]
```
## Changes to src/main.rs
```rust
#![deny(unsafe_code)]
#![no_std]
#![no_main]

use cortex_m_rt as rt;
use hal::prelude::*;
use panic_halt as _;
use stm32f4xx_hal as hal;

#[rt::entry]
fn main() -> ! {
    if let Some(peripherals) = hal::pac::Peripherals::take() {
        let gpiob = peripherals.GPIOB.split();
        let mut led = gpiob.pb7.into_push_pull_output();
        let gpioc = peripherals.GPIOC.split();
        let button = gpioc.pc13;

        loop {
            if button.is_high() {
                led.set_low();
            } else {
                led.set_high();
            }
        }
    }
}
```