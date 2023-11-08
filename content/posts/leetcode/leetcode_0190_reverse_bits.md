---
title: 190. reverse bits
date: '2021-10-13'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0190 reverse bits
---



Reverse bits of a given 32 bits unsigned integer.

Note:



Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers using [2"s complement notation](https://en.wikipedia.org/wiki/Two%27s_complement). Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.



Follow up:

If this function is called many times, how would you optimize it?



>   Example 1:
>   Input: n <TeX>=</TeX> 00000010100101000001111010011100
>   Output:    964176192 (00111001011110000010100101000000)
>   Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
>   Example 2:
>   Input: n <TeX>=</TeX> 11111111111111111111111111111101
>   Output:   3221225471 (10111111111111111111111111111111)
>   Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
**Constraints:**
>   	The input must be a binary string of length 32


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
pub fn get_bit(x: u32, pos: u32) -> u32 {
x >> pos & 1u32
}
pub fn set_bit(x: u32, pos: u32, bit: u32) -> u32 {
if bit == 1u32 {
1u32 << pos | x
} else {
!(1u32 << pos) & x
}
}

pub fn reverse_bits(x: u32) -> u32 {
let mut result: u32 = 0u32;
let mut x = x;
let mut items: Vec<u32> = vec![];
for _ in 0..32 {
items.push(x % 2);
x = x / 2;
}
//items.reverse();
for i in 0..32 {
result = result * 2 + items[i];
}
result
}
}
*/
impl Solution {
pub fn reverse_bits(x: u32) -> u32 {
let mut res = 0u32;
for i in 0..32 {
// find ith bit, shift it to the correct pos, add it to res.
let tmp = x & (1u32 << i);
if 31 - i > i {
res += tmp << 31 - i - i;
} else {
res += tmp >> i - (31 - i);
}
}
res
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_190() {
assert_eq!(Solution::reverse_bits(0b00000010100101000001111010011100), 964176192);
}
}

```
