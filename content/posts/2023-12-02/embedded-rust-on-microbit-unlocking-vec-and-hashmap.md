---
title: "Embedded Rust on Micro:bit Unlocking Vec and Hashmap"
date: 2023-12-02T00:26:59-05:00
tags: ['Rust', 'Microbit']
draft: false
---

Reading notes for [this post](https://www.linkedin.com/pulse/embedded-rust-bbc-micro-bit-unlocking-vec-hashmap-cyril-marpaud/)


## Create Project
```shell
cargo init microbit
cd microbit
cargo add cortex-m-rt microbit-v2 panic_halt
```
create `Embed.toml`
```toml
[default.general]
chip = "nrf52833_xxAA"
```
Create the following `.cargo/config`
```
[target.'cfg(all(target_arch = "arm", target_os = "none"))']
rustflags = ["-C", "link-arg=-Tlink.x",]

[build]
target = "thumbv7em-none-eabihf"
```
Create `src/main.rs`
```rust
#![no_main]
#![no_std]

use cortex_m_rt::entry;
use microbit::{
	board::Board,
	hal::{prelude::*, timer::Timer},
};
use panic_halt as _;

#[entry]
fn main() -> ! {
	let mut board = Board::take().expect("Failed to take board");
	let mut timer = Timer::new(board.TIMER0);
	let mut row = board.display_pins.row1;
	let delay = 150u16;

	board.display_pins.col1.set_low().expect("Failed to set col1 low");

	loop {
		row.set_high().expect("Failed to set row1 high");
		timer.delay_ms(delay);

		row.set_low().expect("Failed to set row1 low");
		timer.delay_ms(delay);
	}
}
```
Upload
```shell
cargo embed
```

## Unlocking Vec
Vec requires an allocator. The `embedded-alloc` crate provides one. The `cortex-m` crate to handle critical sections. 
```shell
cargo add embedded-alloc
cargo add cortex-m --features critical-section-single-core
```
Add the following code to import Vec. 
```rust
extern crate alloc;
use alloc::vec::Vec;

use embedded_alloc::Heap;

#[global_allocator]
static HEAP: Heap = Heap::empty();
```
At the beginning of the main function, initialize the allocator and a size for our heap (the Micro Bit has 128KiB of RAM):
```rust
{
	use core::mem::MaybeUninit;
	const HEAP_SIZE: usize = 8192; // 8KiB
	static mut HEAP_MEM: [MaybeUninit<u8>; HEAP_SIZE] = [MaybeUninit::uninit(); HEAP_SIZE];
	unsafe { HEAP.init(HEAP_MEM.as_ptr() as usize, HEAP_SIZE) }
}
```
Replace the loop with 
```rust
let mut vec = Vec::new();
vec.push(true);
vec.push(false);
vec.push(true);
vec.push(false);
vec.push(false);
vec.push(false);

vec.iter().cycle().for_each(|v| {
	match v {
		true => row.set_high().expect("Failed to set row high"),
		false => row.set_low().expect("Failed to set row low"),
	}
	timer.delay_ms(delay);
});

loop {}
```
Upload
```
cargo embed
```

## Unlocking HashMap
create `rust-toolchain.toml`
```toml
[toolchain]
channel = "nightly"
``` 
Add `rust-src`. 
```shell
rustup component add rust-src
```
In .cargo/config, add the following lines (panic_abort is needed here because of a currently unresolved issue):
```toml
[unstable]
build-std = ["std", "panic_abort"]
```
The std crate provides an allocator, we can therefore remove those lines from src/main.rs:
```rust
#![no_std]
extern crate alloc
use alloc::vec::Vec;;
```
std also provides a panic handler, the import and panic-halt dependency can therefore be removed:
```rust
use panic_halt as _;
```
```shell
cargo remove panic-halt
```
Now that we are rid of those useless parts, there are a few things we need to add. As we're building std for an unsupported (thus flagged unstable) platform, we need the restricted_std feature. Add it to src/main.rs:
```rust
#![feature(restricted_std)]
```
Import HashMap:
```rust
use std::{
	collections::{hash_map::DefaultHasher, HashMap},
	hash::BuildHasherDefault,
};
```
And use it instead of Vec:
```rust
let mut hm = HashMap::with_hasher(BuildHasherDefault::<DefaultHasher>::default());
hm.insert(0, false);
hm.insert(1, true);
hm.insert(2, false);
hm.insert(3, true);
hm.insert(4, true);
hm.insert(5, true);

hm.values().cycle().for_each(|v| {
	match v {
		true => row.set_high().expect("Failed to set row high"),
		false => row.set_low().expect("Failed to set row low"),
	}
	timer.delay_ms(delay);
});

loop {}
```
The reason we are providing our own hasher is that the default one relies on the sys crate which is platform dependent. Our platform being unsupported, the associated implementation either does nothing or fails.
Therefore, keep in mind that using anything from said sys crate will either fail or hang (in particular: threads). HashMap is fine though, and the above snippet should make the LED blink in an inverted heartbeat pattern:
```
cargo embed
```
### Actually using HashMap
The alphabet folder of my Gitlab repository demonstrates how to display caracters on the LED matrix using a HashMap. You can flash it by running the following commands:
```shell
cd	# We need to move out of the "microbit" folder we created earlier
sudo apt install --yes git
git clone https://gitlab.com/cyril-marpaud/microbit_vec_hashmap.git
cd microbit_vec_hashmap/alphabet
cargo embed
```