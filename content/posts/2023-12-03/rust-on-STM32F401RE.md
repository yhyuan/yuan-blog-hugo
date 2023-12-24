---
title: "Rust on STM32F401RE"
date: 2023-12-03T06:16:13-05:00
tags: ['Rust', 'Stm32', 'Ubuntu']
draft: false
---

This post is a reading notes for [a series of Japanese posts](https://moons.link/category/rust/)

## Set up
```shell
cargo generate --git https://github.com/rust-embedded/cortex-m-quickstart.git
 Unable to load config file: C:\Users\xxxxx\.cargo\cargo-general.toml
 Project Name : stm32f401a
```
### Editing `config.toml` to enable or disable `runner` and `target`. 
```toml
runner = “arm-none-eabi-gdb -q -x openocd.gdb” 
# target = “thumbv7m-none-eabi” # Cortex-M3
target = “thumbv7me-none-eabihf” # Cortex-M4F and Cortex-M7F (with FPU) 
```
### Editing launch.json (under .vscode)
in configurations section, edit OpenOCD section. 
* (1) In this environment, line 35 says “#device”: “STM32F303VCT6”, so change it to “STM32F401RET6”. 
* (2) In this environment, line 38 says “target/stm32f3x.cfg”. Change it to “target/stm32f4x.cfg”.
* (3) In this environment, line 40 says “svdFile”: “${workspaceRoot}/.vscode/STM32F303.svd”, so change the 303 part to 401 To do.

### Edit Cargo.toml
```toml
[dependencies.stm32f4xx-hal]
features = ["stm32f401", "rt"]
version = "0.8"
```

### Editing memory.x
```
  FLASH : ORIGIN = 0x08000000, LENGTH = 512K
  RAM : ORIGIN = 0x20000000, LENGTH = 96K
```

### svd file
required for debuging. You can download the svd file　[here](https://github.com/posborne/cmsis-svd).
Unzip and save STM32F401.svd in data\STMicro to C:\Users\xxxxx\stm32f401a\.vscode.

### Editing openocd.cfg
Change stm32f3x.cfg on the 5th line to stm32f4x.cfg.

### Edit main.rs
```rust
#![no_std]
#![no_main]

extern crate panic_halt;
use cortex_m_rt::entry;
use stm32f4xx_hal::{delay::Delay, prelude::*, stm32};

#[entry]
fn main() -> ! {
    if let (Some(dp), Some(cp)) = (stm32::Peripherals::take(), stm32::CorePeripherals::take()) {

        let rcc = dp.RCC.constrain();
        let clocks = rcc.cfgr.sysclk(48.mhz()).freeze();
        let gpioa = dp.GPIOA.split();
        let mut led = gpioa.pa5.into_push_pull_output();
        let mut delay = Delay::new(cp.SYST, clocks);

        loop {
            led.set_high().unwrap();
            delay.delay_ms(100_u32);
            led.set_low().unwrap();
            delay.delay_ms(100_u32);
        }
    }
    loop {}
}
```

### Run it
Launch it by selecting Run – Start Debugging (F5) in VSCode.

As shown in the attached image, select Debug(OpenOCD) from the Debug menu.

## GPIO
### main.rs
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4::stm32f401; // (1)

#[entry]
fn main() -> ! {
    let dp = stm32f401::Peripherals::take().unwrap();       // (2)
    dp.RCC.ahb1enr.modify(|_, w| w.gpioaen().enabled());    // (3)
    let gpioa = &dp.GPIOA;                                  // (4)
    gpioa.moder.modify(|_, w| w.moder5().output());         // (5)    
    gpioa.odr.modify(|_, w| w.odr5().high());               // (6)
    gpioa.odr.modify(|_, w| w.odr5().low());                // (7)
    gpioa.odr.modify(|_, w| w.odr5().high());    
    gpioa.odr.modify(|_, w| w.odr5().low());    
    loop {
        // your code goes here
    }
}
```

## Interrupt
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4::stm32f401;
use stm32f4::stm32f401::interrupt;  // (1)割り込みを使う

#[entry]
fn main() -> ! {
    unsafe {
        stm32f401::NVIC::unmask(stm32f401::interrupt::TIM2);    // (2)TIM2 NVIC割り込み許可
    }
    let dp = stm32f401::Peripherals::take().unwrap();   // (3)Peripheralsの取得

    // PLLSRC = HSI (default)
    dp.RCC.pllcfgr.modify(|_, w| w.pllp().div4());  // (4)P=4
    dp.RCC.pllcfgr.modify(|_, w| unsafe { w.plln().bits(336) });    // (5)N=336
    // PLLM = 16 (default)

    dp.RCC.cfgr.modify(|_, w| w.ppre1().div2());    // (6) APB1 PSC = 1/2

    dp.RCC.cr.modify(|_, w| w.pllon().on());    // (7)PLL On
    while dp.RCC.cr.read().pllrdy().is_not_ready() {    // (8)安定するまで待つ
        // PLLがロックするまで待つ (PLLRDY)
    }

    // データシートのテーブル15より
    dp.FLASH.acr.modify(|_,w| w.latency().bits(2));    // (9)レイテンシの設定: 2ウェイト (3.3V, 84MHz)

    dp.RCC.cfgr.modify(|_,w| w.sw().pll()); // (10)sysclk = PLL
    while !dp.RCC.cfgr.read().sws().is_pll() {  // (11)SWS システムクロックソースがPLLになるまで待つ
    }

    dp.RCC.apb1enr.modify(|_,w| w.tim2en().enabled());  // (12)TIM2のクロックを有効にする

    let tim2 = &dp.TIM2;    // (13)TIM2の取得
    tim2.psc.modify(|_, w| unsafe { w.bits(84 - 1) });   // (14)プリスケーラの設定
    tim2.arr.modify(|_, w| unsafe { w.bits(1000000 - 1) }); // (15)ロードするカウント値
    tim2.dier.modify(|_, w| w.uie().enabled()); // (16)更新割り込み有効
    tim2.cr1.modify(|_, w| w.cen().enabled());  // (17)カウンタ有効

    dp.RCC.ahb1enr.modify(|_, w| w.gpioaen().enabled());    // (18)GPIOAのクロックを有効にする
    let gpioa = &dp.GPIOA;                                  // (19)GPIOAの取得
    gpioa.moder.modify(|_, w| w.moder5().output());         // (20)GPIOA5を出力に設定    
    loop {
        // your code goes here
    }
}

#[interrupt]    // (21)割り込みの指定
fn TIM2() {     // (22)TIM2割り込みハンドラ
    unsafe {
        let dp = stm32f401::Peripherals::steal();   // (23)Peripheralsの取得
        dp.TIM2.sr.modify(|_, w| w.uif().clear());  // (24)更新フラグのクリア
        dp.GPIOA.odr.modify(|r, w| w.odr5().bit(r.odr5().is_low()));    // (25)GPIOA5の出力を反転する
    }
}
```

## Delay
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use cortex_m::delay;    // (1)Delayを使う
use stm32f4::stm32f401;

#[entry]
fn main() -> ! {

    let dp = stm32f401::Peripherals::take().unwrap();
    let cp = cortex_m::peripheral::Peripherals::take().unwrap();

    clock_init(&dp);    // (2)クロック関連の初期化
    gpioa5_init(&dp);   // (3)GPIOA5の初期化
    let mut delay = delay::Delay::new(cp.SYST, 84000000_u32);   // (4)Delayの初期化

    loop {
        dp.GPIOA.odr.modify(|r, w| w.odr5().bit(r.odr5().is_low()));    // (5)GPIOAの出力を反転する
        delay.delay_ms(1000_u32);   // (6)1000msec遅延
    }
}

fn clock_init(dp: &stm32f401::Peripherals) {

    // PLLSRC = HSI: 16MHz (default)
    dp.RCC.pllcfgr.modify(|_, w| w.pllp().div4());      // P=4
    dp.RCC.pllcfgr.modify(|_, w| unsafe { w.plln().bits(336) });    // N=336
    // PLLM = 16 (default)

    dp.RCC.cfgr.modify(|_, w| w.ppre1().div2());        // APB1 PSC = 1/2
    dp.RCC.cr.modify(|_, w| w.pllon().on());            // PLL On
    while dp.RCC.cr.read().pllrdy().is_not_ready() {    // 安定するまで待つ
        // PLLがロックするまで待つ (PLLRDY)
    }

    // データシートのテーブル15より
    dp.FLASH.acr.modify(|_,w| w.latency().bits(2));    // レイテンシの設定: 2ウェイト

    dp.RCC.cfgr.modify(|_,w| w.sw().pll());     // sysclk = PLL
    while !dp.RCC.cfgr.read().sws().is_pll() {  // SWS システムクロックソースがPLLになるまで待つ
    }
}

fn gpioa5_init(dp: &stm32f401::Peripherals) {
    dp.RCC.ahb1enr.modify(|_, w| w.gpioaen().enabled());    // GPIOAのクロックを有効にする
    dp.GPIOA.moder.modify(|_, w| w.moder5().output());   // GPIOA5を汎用出力に設定    
}
```

## PWM
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics

use cortex_m_rt::entry;
use cortex_m::delay;    // (1)Delayを使う
use stm32f4::stm32f401;

#[entry]
fn main() -> ! {

    let dp = stm32f401::Peripherals::take().unwrap();   // (2)デバイス用Peripheralsの取得
    let cp = cortex_m::peripheral::Peripherals::take().unwrap();    // (3)cortex-m Peripheralsの取得
    let mut delay = delay::Delay::new(cp.SYST, 84000000_u32);   // (4)Delayの生成
    clock_init(&dp);    // (5)クロック関連の初期化
    tim2_init(&dp);     // (6)TIM2の初期化
    gpioa5_init(&dp);   // (7)GPIOAの初期化
    tim2_start(&dp);    // (8)PWM スタート
    loop {
        tim2_change_duty(&dp, 500_u32);     // (9)Duty を 50% に変更する
        delay.delay_ms(2000_u32);           // (10)delay 2000msec
        tim2_change_duty(&dp, 100_u32);     // (11)High(LED On)の期間を 10% に変更して暗くする
        delay.delay_ms(1000_u32);           // (12)delay 1000msec
    }
}

fn clock_init(dp: &stm32f401::Peripherals) {

    // PLLSRC = HSI: 16MHz (default)
    dp.RCC.pllcfgr.modify(|_, w| w.pllp().div4());      // (13)P=4
    dp.RCC.pllcfgr.modify(|_, w| unsafe { w.plln().bits(336) });    // (14)N=336
    // PLLM = 16 (default)

    dp.RCC.cfgr.modify(|_, w| w.ppre1().div2());        // (15) APB1 PSC = 1/2
    dp.RCC.cr.modify(|_, w| w.pllon().on());            // (16)PLL On
    while dp.RCC.cr.read().pllrdy().is_not_ready() {    // (17)安定するまで待つ
        // PLLがロックするまで待つ (PLLRDY)
    }

    // データシートのテーブル15より
    dp.FLASH.acr.modify(|_,w| w.latency().bits(2));    // (18)レイテンシの設定: 2ウェイト

    dp.RCC.cfgr.modify(|_,w| w.sw().pll());     // (19)sysclk = PLL
    while !dp.RCC.cfgr.read().sws().is_pll() {  // (20)SWS システムクロックソースがPLLになるまで待つ
    }
}

fn gpioa5_init(dp: &stm32f401::Peripherals) {
    dp.RCC.ahb1enr.modify(|_, w| w.gpioaen().enabled());    // (21)GPIOAのクロックを有効にする
    dp.GPIOA.moder.modify(|_, w| w.moder5().alternate());   // (22)GPIOA5をオルタネートに設定    
    dp.GPIOA.afrl.modify(|_, w| w.afrl5().af1());           // (23)GPIOA5をAF1に設定    
}

fn tim2_init(dp: &stm32f401::Peripherals) {
    dp.RCC.apb1enr.modify(|_,w| w.tim2en().enabled());          // (24)TIM2のクロックを有効にする
    dp.TIM2.psc.modify(|_, w| unsafe { w.bits(84 - 1) });       // (25)プリスケーラの設定

    // 周波数はここで決める
    dp.TIM2.arr.modify(|_, w| unsafe { w.bits(1000 - 1) });     // (26)ロードするカウント値
    dp.TIM2.ccmr1_output().modify(|_, w| w.oc1m().pwm_mode1()); // (27)出力比較1 PWMモード1

    // Duty比はここで決まる
    dp.TIM2.ccr1.modify(|_, w| unsafe { w.bits(500 - 1) });     // (28)キャプチャ比較モードレジスタ1
}

fn tim2_start(dp: &stm32f401::Peripherals) {
    dp.TIM2.cr1.modify(|_, w| w.cen().enabled());   // (29)カウンタ有効
    dp.TIM2.ccer.modify(|_, w| w.cc1e().set_bit()); // (30)キャプチャ比較1出力イネーブル
}

// duty : 1 ～ 1000
// 値が 0 ～ 999 の範囲で設定されるように制限しておく

fn tim2_change_duty(dp: &stm32f401::Peripherals, duty: u32) {
    let config;
    if duty == 0 {
        config = 1;
    }
    else if duty > 1000 {
        config = 1000;
    }
    else {
        config = duty;
    }
    dp.TIM2.ccr1.modify(|_, w| unsafe { w.bits(config - 1) });     // (31)キャプチャ比較モードレジスタ1
}
```

## DWT
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics

use cortex_m_rt::entry;
use cortex_m::delay;
use stm32f4::stm32f401;

#[entry]
fn main() -> ! {
    let dp = stm32f401::Peripherals::take().unwrap();
    let mut cp = cortex_m::peripheral::Peripherals::take().unwrap();

    // PLLSRC = HSI (default)
    dp.RCC.pllcfgr.modify(|_, w| w.pllp().div4());  // P=4
    dp.RCC.pllcfgr.modify(|_, w| unsafe { w.plln().bits(336) });    // N=336
    // PLLM = 16 (default)

    dp.RCC.cfgr.modify(|_, w| w.ppre1().div2());    // APB1 PSC = 1/2

    dp.RCC.cr.modify(|_, w| w.pllon().on());    // PLL On
    while dp.RCC.cr.read().pllrdy().is_not_ready() {    // 安定するまで待つ
        // PLLがロックするまで待つ (PLLRDY)
    }

    // データシートのテーブル15より
    dp.FLASH.acr.modify(|_,w| w.latency().bits(2));    // レイテンシの設定: 2ウェイト (3.3V, 84MHz)

    dp.RCC.cfgr.modify(|_,w| w.sw().pll()); // sysclk = PLL
    while !dp.RCC.cfgr.read().sws().is_pll() {  // SWS システムクロックソースがPLLになるまで待つ
    }
    // SYSCLK = 16M * 1/M * N * 1/P = 84MHz (= AHB Clock)

    let mut delay = delay::Delay::new(cp.SYST, 84000000_u32);

    cp.DWT.enable_cycle_counter();  // (1)
    let mut msecond: u32 = 1000;

    loop {
        cp.DWT.set_cycle_count(0_u32);  // (2)
        delay.delay_ms(msecond);  // (3)
        usecond = get_usec();  // (4)
        msecond = get_msec();  // (5)
    }
}

fn get_msec() -> u32 {
    stm32f401::DWT::cycle_count() / 84000_u32
}

fn get_usec() -> u32 {
    stm32f401::DWT::cycle_count() / 84_u32
}
```

## GPIO with button
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4::stm32f401; // (1)

#[entry]
fn main() -> ! {
    let dp = stm32f401::Peripherals::take().unwrap();   // (2)
    dp.RCC.ahb1enr.modify(|_, w| w.gpioaen().enabled());    // (3)
    let gpioa = &dp.GPIOA;                                  // (4)
    gpioa.moder.modify(|_, w| w.moder5().output());         // (5)
    
    loop {
        if gpioa.idr.read().idr6().is_low() {    // (6)GPIOA6を読む
            gpioa.odr.modify(|_, w| w.odr5().high());       // (7)
        }
        else {
            gpioa.odr.modify(|_, w| w.odr5().low());        // (8)
        }
    }
}
```
## GPIO with hal
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4xx_hal::{prelude::*, stm32, gpio::*};    // (1)
use stm32f4xx_hal::gpio::gpioa::PA5;    // (2)
use stm32f4xx_hal::gpio::gpioa::PA6;    // (3)

#[entry]
fn main() -> ! {
    let dp = stm32::Peripherals::take().unwrap();   // (4)
    let gpioa = dp.GPIOA.split();   // (5)
    let mut led = Led::new(gpioa.pa5);  // (6)
    let sw = Sw::new(gpioa.pa6);    // (7)

    loop {
        if sw.is_pressed() {    // (8)
            led.turn_on();  // (9)
        } else {
            led.turn_off(); // (10)
        }
    }
}

struct Sw { // (11)
    pin: PA6<Input<Floating>>   // (12)
}

impl Sw {   // (13)
    fn new(pin: PA6<Input<Floating>>) -> Sw {   // (14)
        Sw { pin: pin.into_floating_input() }   // (15) Sw { pin: pin }
    }
    fn is_pressed(&self) -> bool {  // (16)
        self.pin.is_low().unwrap()  // (17)
    }
    fn is_released(&self) -> bool { // (18)
        self.pin.is_high().unwrap() // (19)
    }
}

struct Led {    // (20)
    pin: PA5<Output<PushPull>>  // (21)
}

impl Led {  // (22)
    fn new(pin: PA5<Input<Floating>>) -> Led {  // (23)
        Led { pin: pin.into_push_pull_output() }    // (24)
    }
    fn turn_on(&mut self) { // (25)
        self.pin.set_high().unwrap();   // (26)
    }
    fn turn_off(&mut self) {    // (27)
        self.pin.set_low().unwrap();    // (28)
    }
}
```

## GPIO library
```
C:\Users\xxxxx\stm32f401-gpio4>cargo new --lib stm32lib
    Created libral `stm32lib` package
```
lib.rs
```rust
#![no_std]
pub mod gpio;
```
Carto.toml
```toml
[dependencies]
stm32lib = { path = "stm32lib" } 
```
```toml
[dependencies.stm32f4xx-hal]
features = ["stm32f401", "rt"]
version = "0.9"
```
gipo.rs
```rust
use stm32f4xx_hal::{prelude::*, gpio::*};
use stm32f4xx_hal::gpio::gpioa::PA5;
use stm32f4xx_hal::gpio::gpioa::PA6;

pub struct Sw {
    pin: PA6<Input<Floating>>
}

impl Sw {
    pub fn new(pin: PA6<Input<Floating>>) -> Sw {
        Sw { pin: pin.into_floating_input() }
    }
    pub fn is_pressed(&self) -> bool {
        self.pin.is_low().unwrap()
    }
    pub fn is_released(&self) -> bool {
        self.pin.is_high().unwrap()
    }
}

pub struct Led {
    pin: PA5<Output<PushPull>>
}

impl Led {
    pub fn new(pin: PA5<Input<Floating>>) -> Led {
        Led { pin: pin.into_push_pull_output() }
    }
    pub fn turn_on(&mut self) {
        self.pin.set_high().unwrap();
    }
    pub fn turn_off(&mut self) {
        self.pin.set_low().unwrap();
    }
}
```
main.rs
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4xx_hal::{prelude::*, stm32};

use stm32lib::gpio::Sw; // (1)
use stm32lib::gpio::Led; // (2)

#[entry]
fn main() -> ! {
    let dp = stm32::Peripherals::take().unwrap();
    let gpioa = dp.GPIOA.split();
    let mut led = Led::new(gpioa.pa5);
    let sw = Sw::new(gpioa.pa6);

    loop {
        if sw.is_pressed() {
            led.turn_on();
        } else {
            led.turn_off();
        }
    }
}
```

## UART
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4::stm32f401;

#[entry]
fn main() -> ! {
    let dp = stm32f401::Peripherals::take().unwrap();   // (1)デバイス用Peripheralsの取得
    clock_init(&dp);    // (2)クロック関連の初期化
    gpioa2a3_init(&dp); // (3)GPIOAの初期化
    usart2_init(&dp);   // (4)usart2の初期化
    loop {
        while dp.USART2.sr.read().rxne().bit() {	// (5)
            if dp.USART2.sr.read().pe().bit() {	// (6)parity error
                let err = b"\r\nDetected parity error.\r\n";    // (7)エラー検出時に送信する文字列
                let _ = dp.USART2.dr.read().bits(); // (8)読み捨てる
                for c in err.iter() {   // (9)文字列の送信処理
                    let data: u32 = *c as u32;
                    dp.USART2.dr.write( |w| unsafe { w.bits(data) });
                    while !dp.USART2.sr.read().txe().bit() {}   // (10)送り終わるまで待つ
                }
            }
            else if dp.USART2.sr.read().fe().bit() {	// (11)framing error
                let err = b"\r\nDetected framing error.\r\n";
                let _ = dp.USART2.dr.read().bits();
                for c in err.iter() {
                    let data: u32 = *c as u32;
                    dp.USART2.dr.write( |w| unsafe { w.bits(data) });
                    while !dp.USART2.sr.read().txe().bit() {}
                }
            }
            else if dp.USART2.sr.read().ore().bit() {	// (12)overrun error
                let err = b"\r\nDetected overrun error.\r\n";
                let _ = dp.USART2.dr.read().bits();
                for c in err.iter() {
                    let data: u32 = *c as u32;
                    dp.USART2.dr.write( |w| unsafe { w.bits(data) });
                    while !dp.USART2.sr.read().txe().bit() {}
                }
            }
            else {	// (13)no error
                dp.USART2.dr.write( |w| unsafe { w.bits(dp.USART2.dr.read().bits()) });	// echo back
                while !dp.USART2.sr.read().txe().bit() {}
            }
        }
    }
}

fn clock_init(dp: &stm32f401::Peripherals) {

    // PLLSRC = HSI: 16MHz (default)
    dp.RCC.pllcfgr.modify(|_, w| w.pllp().div4());      // (14)P=4
    dp.RCC.pllcfgr.modify(|_, w| unsafe { w.plln().bits(336) });    // (15)N=336
    // PLLM = 16 (default)

    dp.RCC.cfgr.modify(|_, w| w.ppre1().div2());        // (16) APB1 PSC = 1/2
    dp.RCC.cr.modify(|_, w| w.pllon().on());            // (17)PLL On
    while dp.RCC.cr.read().pllrdy().is_not_ready() {    // (18)安定するまで待つ
        // PLLがロックするまで待つ (PLLRDY)
    }

    // データシートのテーブル15より
    dp.FLASH.acr.modify(|_,w| w.latency().bits(2));    // (19)レイテンシの設定: 2ウェイト

    dp.RCC.cfgr.modify(|_,w| w.sw().pll());     // (20)sysclk = PLL
    while !dp.RCC.cfgr.read().sws().is_pll() {  // (21)SWS システムクロックソースがPLLになるまで待つ
    }

//  SYSCLK = 16MHz * 1/M * N * 1/P
//  SYSCLK = 16MHz * 1/16 * 336 * 1/4 = 84MHz
//  APB1 = 42MHz (USTAR2 pclk1)

}

fn gpioa2a3_init(dp: &stm32f401::Peripherals) {
    dp.RCC.ahb1enr.modify(|_, w| w.gpioaen().enabled());    // (22)GPIOAのクロックを有効にする
    dp.GPIOA.moder.modify(|_, w| w.moder2().alternate());   // (23)GPIOA2をオルタネートに設定    
    dp.GPIOA.moder.modify(|_, w| w.moder3().alternate());   // (24)GPIOA3をオルタネートに設定    
    dp.GPIOA.afrl.modify(|_, w| w.afrl2().af7());           // (25)GPIOA2をAF7に設定    
    dp.GPIOA.afrl.modify(|_, w| w.afrl3().af7());           // (26)GPIOA3をAF7に設定
    
    // GPIOA2 = USART2 Tx
    // GPIOA3 = USART2 Rx
}

fn usart2_init(dp: &stm32f401::Peripherals) {

    // 通信速度: 115,200
    // データ長: 7ビット
    // パリティ: 偶数(EVEN)
    // ストップビット: 1ビット

    dp.RCC.apb1enr.modify(|_,w| w.usart2en().enabled());    // (27)USART2のクロックを有効にする
    dp.USART2.cr1.modify(|_, w| w.te().enabled());  // (28)送信有効
    dp.USART2.cr1.modify(|_, w| w.re().enabled());  // (29)受信有効
    dp.USART2.cr1.modify(|_, w| w.pce().enabled()); // (30)パリティチェック有効
    dp.USART2.cr1.modify(|_, w| w.ue().enabled());  // (31)USART有効

// 以下のようにまとめて書くこともできる
// dp.USART2.cr1.modify(|_, w| w.te().enabled().re().enabled().pce().enabled().ue().enabled());

    dp.USART2.brr.modify(|_, w| w.div_mantissa().bits(22)); // (32)ボーレート（整数部）
    dp.USART2.brr.modify(|_, w| w.div_fraction().bits(12)); // (33)ボーレート（小数部）

//  bps = pclk1 / 16 * USARTDIV
//  USARTDIV = 22 + 12/16 = 22.75
//  bps = 42M / 16 * 22.75 = 42M / 364 =115384
//  誤差 115384/115200 = 1.001597222
}
```
## UART with library
```
C:\Users\xxxxx\stm32f401-uart2>cargo new --lib stm32lib
    Created libral `stm32lib` package
```
lib.rs
```rust
#![no_std]
pub mod uart;
```
Cargo.toml
```toml
[dependencies]
stm32lib = { path = "stm32lib" } 

[dependencies.stm32f4xx-hal]
features = ["stm32f401", "rt"]
version = "0.9"
```
uart.rs
```rust
use stm32f4xx_hal::serial::Serial;
use stm32f4xx_hal::serial::Instance;
use stm32f4xx_hal::serial::Pins;

pub trait ErrorDetect {
    fn is_pe(&self) -> bool;    // パリティエラー
    fn is_fe(&self) -> bool;    // フレーミングエラー
    fn is_ore(&self) -> bool;   // オーバーランエラー
}

impl<USART, PINS> ErrorDetect for Serial<USART, PINS>
where
    PINS: Pins<USART>,
    USART: Instance,
{
    fn is_pe(&self) -> bool {
        unsafe { (*USART::ptr()).sr.read().pe().bit_is_set() }
    }
    fn is_fe(&self) -> bool {
        unsafe { (*USART::ptr()).sr.read().fe().bit_is_set() }
    }
    fn is_ore(&self) -> bool {
        unsafe { (*USART::ptr()).sr.read().ore().bit_is_set() }
    }
}
```
main.rs
```rust
#![no_std]
#![no_main]

use embedded_hal::prelude::_embedded_hal_serial_Write;
use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4xx_hal::serial::{Serial, config};
use stm32f4xx_hal::gpio::{GpioExt};
use stm32f4xx_hal::rcc::RccExt;
use stm32f4xx_hal::time::Bps;

use embedded_hal::serial::Read;
use core::fmt::Write;   // (1)write!()マクロを使えるようにする
use stm32lib::uart::ErrorDetect;    // (2)追加するトレイトを使えるようにする

#[entry]
fn main() -> ! {

    let dp = stm32f4xx_hal::pac::Peripherals::take().unwrap();
    let gpioa = dp.GPIOA.split();   // GPIOAのclockも有効にしてくれる （AHBENRレジスタ）
    let pa2 = gpioa.pa2.into_alternate_af7();   // afrl, modeレジスタを設定してくれる
    let pa3 = gpioa.pa3.into_alternate_af7();   // afrl, modeレジスタを設定してくれる

    let bps = Bps(115_200_u32); // (3)通信速度

    let seri_config = config::Config {  // (4)通信パラメーターの設定
        baudrate: bps,
        wordlength: config::WordLength::DataBits8,  // 実際には7ビット
        parity: config::Parity::ParityEven,
        stopbits: config::StopBits::STOP1,
        dma: config::DmaConfig::None,
    };

    let rcc = dp.RCC.constrain();   // (5)RCCの取得
    let clks = rcc.cfgr.freeze();   // (6)各clockの設定

    let mut serial = Serial::usart2(
        dp.USART2,
        (pa2, pa3),
        seri_config,
        clks,
    ).unwrap(); // (5)Serial構造体の生成

    loop {
        while !serial.is_rxne() {}
        if serial.is_pe() {
            let _ = serial.read();  // 読み捨てる
            write!(serial, "\r\nParity error {}", "detected.\r\n").unwrap();
        }
        else if serial.is_fe() {
            let _ = serial.read();  // 読み捨てる
            write!(serial, "\r\nFraming error {}", "detected.\r\n").unwrap();
        }
        else if serial.is_ore() {
            let _ = serial.read();  // 読み捨てる
            write!(serial, "\r\nOver run error {}", "detected.\r\n").unwrap();
        }
        else if let Ok(c) = serial.read() {
            while !serial.is_txe() {}
            serial.write(c).unwrap();
        }
    }
}
```

## SPI
```rust
#![no_std]
#![no_main]

const WHO_AM_I: u8 = 0x0f;  // デバイス確認用のコマンド
const CTRL_REG1: u8 = 0x20; // コントロールレジスタ1
const WAKE_UP: u8 = 0x90;   // デバイスを起こすためのコマンド
const P_ADRS: u8 = 0x28;    // 気圧読み込み用のアドレス
const LPS25HB_DEVICE_CODE: u8 = 0xbd;

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use cortex_m::delay;    // Delayを使う
use stm32f4::stm32f401;

#[entry]
fn main() -> ! {

    let mut dp = stm32f401::Peripherals::take().unwrap();   // デバイス用Peripheralsの取得
    let cp = cortex_m::peripheral::Peripherals::take().unwrap();    // cortex-m Peripheralsの取得
    let mut delay = delay::Delay::new(cp.SYST, 84000000_u32);   // Delayの生成
    clock_init(&dp);    // クロック関連の初期化
    gpioa5_init(&dp);   // GPIOAの初期化
    spi1_init(&dp);     // SPI1の初期化
    lps25hb_init(&mut dp);  // LPS25HBの初期化
    loop {
        delay.delay_ms(5_u32);           // delay 2000msec
        lps25hb_select(&dp);
        lps25hb_send(&mut dp, (P_ADRS | 0xc0) as u16);
        let l = lps25hb_send(&mut dp, 0);
        let m = lps25hb_send(&mut dp, 0);
        let h = lps25hb_send(&mut dp, 0);
        lps25hb_deselect(&dp);
        let mut press = h << 16 | m << 8 | l;
        press >>= 12;   // 1/4096
    }
}

fn clock_init(dp: &stm32f401::Peripherals) {

    // PLLSRC = HSI: 16MHz (default)
    dp.RCC.pllcfgr.modify(|_, w| w.pllp().div4());      // (13)P=4
    dp.RCC.pllcfgr.modify(|_, w| unsafe { w.plln().bits(336) });    // (14)N=336
    // PLLM = 16 (default)

    dp.RCC.cfgr.modify(|_, w| w.ppre1().div2());        // (15) APB1 PSC = 1/2
    dp.RCC.cr.modify(|_, w| w.pllon().on());            // (16)PLL On
    while dp.RCC.cr.read().pllrdy().is_not_ready() {    // (17)安定するまで待つ
        // PLLがロックするまで待つ (PLLRDY)
    }

    // データシートのテーブル15より
    dp.FLASH.acr.modify(|_,w| w.latency().bits(2));    // (18)レイテンシの設定: 2ウェイト

    dp.RCC.cfgr.modify(|_,w| w.sw().pll());     // (19)sysclk = PLL
    while !dp.RCC.cfgr.read().sws().is_pll() {  // (20)SWS システムクロックソースがPLLになるまで待つ
    }
//  SYSCLK = 16MHz * 1/M * N * 1/P
//  SYSCLK = 16MHz * 1/16 * 336 * 1/4 = 84MHz
//  APB2 = 84MHz (SPI1 pclk1)
}

fn gpioa5_init(dp: &stm32f401::Peripherals) {

    dp.RCC.ahb1enr.modify(|_, w| w.gpioaen().enabled());    // (21)GPIOAのクロックを有効にする
    dp.GPIOA.moder.modify(|_, w| w.moder4().output());      // (22)GPIOA4を汎用出力に設定    

    dp.GPIOA.moder.modify(|_, w| w.moder5().alternate());   // (22)GPIOA5をオルタネートに設定    
    dp.GPIOA.afrl.modify(|_, w| w.afrl5().af5());           // (23)GPIOA5をAF5に設定    
    dp.GPIOA.moder.modify(|_, w| w.moder6().alternate());   // (22)GPIOA6をオルタネートに設定    
    dp.GPIOA.afrl.modify(|_, w| w.afrl6().af5());           // (23)GPIOA6をAF5に設定    
    dp.GPIOA.moder.modify(|_, w| w.moder7().alternate());   // (22)GPIOA7をオルタネートに設定    
    dp.GPIOA.afrl.modify(|_, w| w.afrl7().af5());           // (23)GPIOA7をAF5に設定    

    lps25hb_deselect(dp);   // CS=High
}

fn spi1_init(dp: &stm32f401::Peripherals) {

    // SPI1のクロックイネーブル機能は APB2 にある
    dp.RCC.apb2enr.modify(|_,w| w.spi1en().enabled());          // (24)SPI1のクロックを有効にする
    dp.SPI1.cr1.modify(|_, w| w.ssm().set_bit());
    dp.SPI1.cr1.modify(|_, w| w.ssi().set_bit());
    dp.SPI1.cr1.modify(|_, w| w.br().div16());          // 84MHz/16=5.25MHz
    dp.SPI1.cr1.modify(|_, w| w.cpha().second_edge());
    dp.SPI1.cr1.modify(|_, w| w.cpol().idle_high());
    dp.SPI1.cr1.modify(|_, w| w.mstr().master());
    dp.SPI1.cr1.modify(|_, w| w.spe().enabled());
}

fn lps25hb_init(dp: &mut stm32f401::Peripherals) -> bool {

    lps25hb_select(dp);
    lps25hb_send(dp, (WHO_AM_I | 0x80).into());  // WHO_AM_I コマンドを送る
    let res = lps25hb_send(dp, 0u16);  // 読む
    lps25hb_deselect(dp);

    lps25hb_select(dp);
    lps25hb_send(dp, (CTRL_REG1).into());   // CTRLREG1
    lps25hb_send(dp, (WAKE_UP).into());     // 起床を指示
    lps25hb_deselect(dp);
    if res == LPS25HB_DEVICE_CODE.into() {
        return true;    // デバイスコードが返ってくれば true
    }
    false
}

fn lps25hb_select(dp: &stm32f401::Peripherals) {    // CS=Low
    dp.GPIOA.odr.modify(|_, w| w.odr4().low());
}

fn lps25hb_deselect(dp: &stm32f401::Peripherals) {  // CS=High
    dp.GPIOA.odr.modify(|_, w| w.odr4().high());
}

fn lps25hb_send(dp: &mut stm32f401::Peripherals, data: u16) -> u32 {
    while dp.SPI1.sr.read().txe().is_not_empty() {}
    dp.SPI1.dr.write(|w| w.dr().bits(data));    // 書いて
    while dp.SPI1.sr.read().rxne().is_empty() {}
    dp.SPI1.dr.read().bits()    // 読む
}
```

## SPI with hal
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4xx_hal::gpio::{GpioExt};
use stm32f4xx_hal::{prelude::*, gpio::*};
use stm32f4xx_hal::gpio::gpioa::PA4;
use stm32f4xx_hal::gpio::gpioa::PA5;
use stm32f4xx_hal::gpio::gpioa::PA6;
use stm32f4xx_hal::gpio::gpioa::PA7;
use stm32f4xx_hal::rcc::RccExt;
use stm32f4xx_hal::time;
use stm32f4xx_hal::stm32::SPI1;
use stm32f4xx_hal::spi::*;

const WHO_AM_I: u8 = 0x0f;  // デバイス確認用のコマンド
const CTRL_REG1: u8 = 0x20; // コントロールレジスタ1
const WAKE_UP: u8 = 0x90;   // デバイスを起こすためのコマンド
const P_ADRS: u8 = 0x28;    // 気圧読み込み用のアドレス
const LPS25HB_DEVICE_CODE: u8 = 0xbd;

#[entry]
fn main() -> ! {

    let dp = stm32f4xx_hal::pac::Peripherals::take().unwrap();
    let gpioa = dp.GPIOA.split();   // GPIOAのclockも有効にしてくれる （AHBENRレジスタ）
    let mut cs = DigitalOut::new(gpioa.pa4);
    let sck = gpioa.pa5.into_alternate_af5();   // afrl, modeレジスタを設定してくれる
    let miso = gpioa.pa6.into_alternate_af5();   // afrl, modeレジスタを設定してくれる
    let mosi = gpioa.pa7.into_alternate_af5();   // afrl, modeレジスタを設定してくれる

    let rcc = dp.RCC.constrain();   // RCCの取得
    let clks = rcc.cfgr.freeze();   // 各clockの設定

    let mode = Mode { polarity: Polarity::IdleHigh, phase: Phase::CaptureOnSecondTransition };  // SPIのモード
    let hz = time::Hertz(1000_000u32);  // SPIのクロック

    lps25hb_deselect(&mut cs);  // CS=Highにしておく

    let mut spi = Spi::spi1(
        dp.SPI1,
        (sck, miso, mosi),
        mode,
        hz,
        clks,
    );  // SPIの生成
    lps25hb_init(&mut spi, &mut cs);    // LPS25HBの初期化
    loop {
        let mut data: [u8; 4] = [P_ADRS | 0xc0, 0, 0, 0];
        lps25hb_select(&mut cs);
        lps25hb_send_buf(&mut spi, &mut data);
        lps25hb_deselect(&mut cs);
        let mut press = (data[3] as u32) << 16_u32 | (data[2] as u32) << 8_u32 | data[1] as u32;
        press >>= 12_i32;   // 1/4096
    }
}

fn lps25hb_init(spi: &mut Spi<SPI1, (PA5<Alternate<AF5>>, PA6<Alternate<AF5>>, PA7<Alternate<AF5>>)>, cs: &mut DigitalOut) -> bool {

    lps25hb_select(cs);
    lps25hb_send(spi, WHO_AM_I | 0x80);     // WHO_AM_I コマンドを送る
    let res = lps25hb_send(spi, 0u8);   // 返事を読む
    lps25hb_deselect(cs);

    lps25hb_select(cs);
    lps25hb_send(spi, CTRL_REG1);           // CTRLREG1
    lps25hb_send(spi, WAKE_UP);             // 起床を指示
    lps25hb_deselect(cs);
    if res == LPS25HB_DEVICE_CODE { // デバイスコードが返ること
        return true;
    }
    false
}

fn lps25hb_select(cs: &mut DigitalOut) {    // CS=Low
    cs.select();
}

fn lps25hb_deselect(cs: &mut DigitalOut) {  // CS=High
    cs.deselect();
}

fn lps25hb_send(spi: &mut Spi<SPI1, (PA5<Alternate<AF5>>, PA6<Alternate<AF5>>, PA7<Alternate<AF5>>)>, data: u8) -> u8 {
    while !spi.is_txe() {}
    spi.send(data).unwrap();    // 送って
    while !spi.is_rxne() {}
    spi.read().unwrap() // 読む
}

fn lps25hb_send_buf(spi: &mut Spi<SPI1, (PA5<Alternate<AF5>>, PA6<Alternate<AF5>>, PA7<Alternate<AF5>>)>, data: &mut [u8]) {
    spi.transfer(data).unwrap();    // 送って読む
}

struct DigitalOut { // GPIO出力用の構造体
    pin: PA4<Output<PushPull>>
}

impl DigitalOut {
    fn new(pin: PA4<Input<Floating>>) -> DigitalOut {
        DigitalOut { pin: pin.into_push_pull_output() }
    }
    fn deselect(&mut self) {
        self.pin.set_high().unwrap();
    }
    fn select(&mut self) {
        self.pin.set_low().unwrap();
    }    
}
```
## I2C
```rust
#![no_std]
#![no_main]

const DEVICE_ADRS_FOR_WRITE: u8 = 0xa0;
const DEVICE_ADRS_FOR_READ: u8 = 0xa1;
const UPPER_ADRS: u8 = 0x00;
const LOWER_ADRS: u8 = 0x01;

use core::convert::TryInto;
use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use cortex_m::delay;    // Delayを使う
use stm32f4::stm32f401;

#[entry]
fn main() -> ! {

    let dp = stm32f401::Peripherals::take().unwrap();   // デバイス用Peripheralsの取得
    let cp = cortex_m::peripheral::Peripherals::take().unwrap();    // cortex-m Peripheralsの取得
    let mut delay = delay::Delay::new(cp.SYST, 84000000_u32);   // Delayの生成
    clock_init(&dp);    // クロック関連の初期化
    gpiob89_init(&dp);  // GPIOBの初期化
    i2c1_init(&dp);     // I2C1の初期化

    i2c_set_ack(&dp, true); // ACKを返す指示
    i2c_start(&dp);
    i2c_control_byte_write(&dp, DEVICE_ADRS_FOR_WRITE);

    i2c_write(&dp, UPPER_ADRS);
    i2c_write(&dp, LOWER_ADRS);

    i2c_write(&dp, 18);   // 0x12
    i2c_write(&dp, 52);   // 0x34
    i2c_write(&dp, 86);   // 0x56

    i2c_stop_after_writing(&dp);

    // 書き込んだアドレス(01番地)から値を読む

    delay.delay_ms(5_u32);  // 休憩する

    i2c_start(&dp);
    i2c_control_byte_write(&dp, DEVICE_ADRS_FOR_WRITE);

    i2c_write(&dp, UPPER_ADRS);
    i2c_write(&dp, LOWER_ADRS);

    i2c_start(&dp);
    i2c_control_byte_write(&dp, DEVICE_ADRS_FOR_READ);

    let _ul = i2c_read(&dp);
    let _um = i2c_read(&dp);
    i2c_set_ack(&dp, false); // ACKを返さない(NAK)指示
    let _uh = i2c_read(&dp);

    i2c_stop_after_reading(&dp);
    loop {
    }
}

fn clock_init(dp: &stm32f401::Peripherals) {

    // PLLSRC = HSI: 16MHz (default)
    dp.RCC.pllcfgr.modify(|_, w| w.pllp().div4());      // P=4
    dp.RCC.pllcfgr.modify(|_, w| unsafe { w.plln().bits(336) });    // N=336
    // PLLM = 16 (default)

    dp.RCC.cfgr.modify(|_, w| w.ppre1().div2());        // APB1 PSC = 1/2
    dp.RCC.cr.modify(|_, w| w.pllon().on());            // PLL On
    while dp.RCC.cr.read().pllrdy().is_not_ready() {    // 安定するまで待つ
        // PLLがロックするまで待つ (PLLRDY)
    }

    // データシートのテーブル15より
    dp.FLASH.acr.modify(|_,w| w.latency().bits(2));    // レイテンシの設定: 2ウェイト

    dp.RCC.cfgr.modify(|_,w| w.sw().pll());     // sysclk = PLL
    while !dp.RCC.cfgr.read().sws().is_pll() {  // SWS システムクロックソースがPLLになるまで待つ
    }
//  SYSCLK = 16MHz * 1/M * N * 1/P
//  SYSCLK = 16MHz * 1/16 * 336 * 1/4 = 84MHz
//  APB2 = 84MHz
//  APB1 = 42MHz (I2C1 pclk)
}

fn gpiob89_init(dp: &stm32f401::Peripherals) {

    dp.RCC.ahb1enr.modify(|_, w| w.gpioben().enabled());            // GPIOBのクロックを有効にする

    dp.GPIOB.otyper.modify(|_, w| w.ot8().open_drain());            // GPIOB8をオープンドレイン出力にする
    dp.GPIOB.otyper.modify(|_, w| w.ot9().open_drain());            // GPIOB9をオープンドレイン出力にする
    dp.GPIOB.ospeedr.modify(|_, w| w.ospeedr8().very_high_speed()); // GPIOB8を高速動作にする
    dp.GPIOB.ospeedr.modify(|_, w| w.ospeedr9().very_high_speed()); // GPIOB9を高速動作にする

    dp.GPIOB.moder.modify(|_, w| w.moder8().alternate());           // GPIOB8をオルタネートに設定    
    dp.GPIOB.afrh.modify(|_, w| w.afrh8().af4());                   // GPIOB8をAF4に設定    
    dp.GPIOB.moder.modify(|_, w| w.moder9().alternate());           // GPIOB9をオルタネートに設定    
    dp.GPIOB.afrh.modify(|_, w| w.afrh9().af4());                   // GPIOB9をAF4に設定    

}

fn i2c1_init(dp: &stm32f401::Peripherals) {

    // I2C1のクロックイネーブル機能は APB1 にある
    dp.RCC.apb1enr.modify(|_,w| w.i2c1en().enabled());      // I2C1のクロックを有効にする

    dp.I2C1.cr2.modify(|_, w| unsafe { w.freq().bits(42) });// クロック=42MHz (APB1)
    dp.I2C1.ccr.modify(|_, w| unsafe { w.bits(210) });
    dp.I2C1.trise.modify(|_, w| unsafe { w.bits(43) }); 
    dp.I2C1.cr1.modify(|_, w| w.pe().enabled());            // ペリフェラルイネーブル

    // f = 100kHz として計算
    // CCR:210の計算
    // Thigh = 1/200kHz, CCR = 42M / 200k = 210
    // TRISE:43の計算
    // 42M * 1000n = 42, 42 + 1 = 43

}

fn i2c_set_ack(dp: &stm32f401::Peripherals, ack: bool) {
    if ack {
        dp.I2C1.cr1.modify(|_, w| w.ack().ack());   // ACKを返すように指示
    } else {
        dp.I2C1.cr1.modify(|_, w| w.ack().nak()); // ACKを返さないように指示
    }
}

fn i2c_start(dp: &stm32f401::Peripherals) {
    dp.I2C1.cr1.modify(|_, w| w.start().set_bit()); // スタートコンディション
    while dp.I2C1.sr1.read().sb().is_no_start() {    // 生成されるまで待つ
    }
}

fn i2c_stop_after_writing(dp: &stm32f401::Peripherals) {
    while dp.I2C1.sr1.read().tx_e().is_not_empty() {    // エンプティでない間待つ
    }
    dp.I2C1.cr1.modify(|_, w| w.stop().set_bit());  // ストップコンディション
}

fn i2c_stop_after_reading(dp: &stm32f401::Peripherals) {
    dp.I2C1.cr1.modify(|_, w| w.stop().set_bit());  // ストップコンディション
}

fn i2c_write(dp: &stm32f401::Peripherals, data: u8) {
    while dp.I2C1.sr1.read().tx_e().is_not_empty() {   // エンプティでない間待つ
    }
    dp.I2C1.dr.write(|w| w.dr().bits(data));    // データをライト
    while dp.I2C1.sr1.read().btf().is_not_finished() {    // byte transfer finished
    }
}

fn i2c_read(dp: &stm32f401::Peripherals) -> u8 {
    while dp.I2C1.sr1.read().rx_ne().is_empty() {   // エンプティの間待つ
    }
    dp.I2C1.dr.read().bits().try_into().unwrap()    // データをリード
}

fn i2c_control_byte_write(dp: &stm32f401::Peripherals, data: u8) {
    dp.I2C1.dr.write(|w| w.dr().bits(data));    // コントロールバイトをライト
    while dp.I2C1.sr1.read().addr().is_not_match() {    // 一致するまで待つ
    }
    let _ = dp.I2C1.sr2.read().busy();  // ダミーリードする
}
```

## I2C with hal
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4xx_hal::gpio::{GpioExt};
use stm32f4xx_hal::prelude::*;
use stm32f4xx_hal::rcc::RccExt;
use stm32f4xx_hal::time;
use stm32f4xx_hal::i2c::*;

const DEVICE_ADRS_FOR_WRITE: u8 = 0xa0;

#[entry]
fn main() -> ! {

    let dp = stm32f4xx_hal::pac::Peripherals::take().unwrap();
    let gpiob = dp.GPIOB.split();   // GPIOBのclockも有効にしてくれる （AHBENRレジスタ）
    let scl = gpiob.pb8.into_alternate_af4_open_drain();   // afrh, modeレジスタを設定してくれる (I2Cはオープンドレイン指定する)
    let sda = gpiob.pb9.into_alternate_af4_open_drain();   // afrh, modeレジスタを設定してくれる (I2Cはオープンドレイン指定する)

    let rcc = dp.RCC.constrain();       // RCCの取得
    let clks = rcc.cfgr.freeze();   // 各clockの設定
    let kilohz = time::KiloHertz(100u32);  // I2Cのクロック 100kHz

    let mut i2c = I2c::new(
        dp.I2C1,
        (scl, sda),
        kilohz,
        clks,
    );  // I2Cの生成

    let wbuf = [0, 1, 18, 52, 86];
    // 0, 1 : 書き込むメモリーの先頭アドレス (0x0001 番地)
    // 18, 52, 86 はメモリーに書く値（数値に意味はない）

    let adrs = DEVICE_ADRS_FOR_WRITE >> 1;  // 中で左シフトされるので右シフトしておく
    let _ = i2c.write(adrs, &wbuf);

    let mut rbuf = [0; 3];

    let _ = i2c.write_read(adrs, &wbuf[..2], &mut rbuf);    // 第2引数はスライスを使って最初の２バイトのみ書くように指示する

    loop {
    }
}
```

## I2C with hal (hal version to 0.13)
```rust
#![no_std]
#![no_main]

use panic_halt as _; // you can put a breakpoint on `rust_begin_unwind` to catch panics
use cortex_m_rt::entry;
use stm32f4xx_hal::prelude::*; // Hz()
use stm32f4xx_hal::i2c::*;

const DEVICE_ADRS_FOR_WRITE: u8 = 0xa0;

#[entry]
fn main() -> ! {

    let dp = stm32f4xx_hal::pac::Peripherals::take().unwrap();
    let gpiob = dp.GPIOB.split();   // GPIOBのclockも有効にしてくれる （AHBENRレジスタ）

    let rcc = dp.RCC.constrain();       // RCCの取得
    let clks = rcc.cfgr.freeze();   // 各clockの設定
    let mode = Mode::Standard { frequency: 100_000_u32.Hz() };

    let mut i2c = I2c::new(
        dp.I2C1,
        (gpiob.pb8, gpiob.pb9),
        mode,
        &clks,
    );  // I2Cの生成

    let wbuf = [0, 1, 18, 52, 86];
    // 0, 1 : 書き込むメモリーの先頭アドレス (0x0001 番地)
    // 18, 52, 86 はメモリーに書く値（数値に意味はない）

    let adrs = DEVICE_ADRS_FOR_WRITE >> 1;  // 中で左シフトされるので右シフトしておく
    let _ = i2c.write(adrs, &wbuf);

    let mut rbuf = [0; 3];

    let _ = i2c.write_read(adrs, &wbuf[..2], &mut rbuf);    // 第2引数はスライスを使って最初の２バイトのみ書くように指示する

    loop {
    }
}
```
