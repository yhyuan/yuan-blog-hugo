---
title: 29. divide two integers
date: '2021-05-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0029 divide two integers
---



Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) <TeX>=</TeX> 8 and truncate(-2.7335) <TeX>=</TeX> -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [-2^31, 2^31 - 1]. For this problem, assume that your function returns 2^31 - 1 when the division result overflows.



>   Example 1:
>   Input: dividend <TeX>=</TeX> 10, divisor <TeX>=</TeX> 3
>   Output: 3
>   Explanation: 10/3 <TeX>=</TeX> truncate(3.33333..) <TeX>=</TeX> 3.
>   Example 2:
>   Input: dividend <TeX>=</TeX> 7, divisor <TeX>=</TeX> -3
>   Output: -2
>   Explanation: 7/-3 <TeX>=</TeX> truncate(-2.33333..) <TeX>=</TeX> -2.
>   Example 3:
>   Input: dividend <TeX>=</TeX> 0, divisor <TeX>=</TeX> 1
>   Output: 0
>   Example 4:
>   Input: dividend <TeX>=</TeX> 1, divisor <TeX>=</TeX> 1
>   Output: 1
**Constraints:**
>   	-2^31 <TeX>\leq</TeX> dividend, divisor <TeX>\leq</TeX> 2^31 - 1
>   	divisor !<TeX>=</TeX> 0


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn leftest_bit_position(val: i32) -> i32 {
let mut result = 32;
for i in 0..32 {
if (val >> i) == 0 {
result = i;
break;
}
}
result
}
pub fn divide_helper(dividend: i32, divisor: i32) -> i32 {
if dividend < divisor {
return 0;
}
let dividend_leftest_bit = Solution::leftest_bit_position(dividend);
let divisor_leftest_bit = Solution::leftest_bit_position(divisor);
if dividend_leftest_bit == divisor_leftest_bit {
return 1 + Solution::divide_helper(dividend - divisor, divisor);
}
//println!("dividend_leftest_bit: {}", dividend_leftest_bit);
//println!("divisor_leftest_bit: {}", divisor_leftest_bit);
let shift_bits = dividend_leftest_bit - divisor_leftest_bit - 1;
let new_dividend = dividend - (divisor << shift_bits);
let power_2: Vec<i32> = vec![1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824];
power_2[shift_bits as usize] + Solution::divide_helper(new_dividend, divisor)
}
pub fn divide(dividend: i32, divisor: i32) -> i32 {
if divisor == 1 {
return dividend;
}
if divisor == -1 {
if dividend == i32::MIN {
return i32::MAX;
}
return -dividend;
}
if divisor == i32::MIN {
if dividend == i32::MIN {
return 1;
}
return 0;
}
if dividend == i32::MIN {
if divisor > 0 {
return Solution::divide(dividend + divisor, divisor) - 1;
} else {
return Solution::divide(dividend - divisor, divisor) + 1;
}
}
if dividend.abs() < divisor.abs() {
return 0;
}
let sign = (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0);
let dividend = dividend.abs();
let divisor = divisor.abs();
//println!("dividend: {}", dividend);
//println!("dividend >> 31 : {:b}", dividend >> 31);

let result = Solution::divide_helper(dividend, divisor);
if sign {result} else {-result}
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_29() {
assert_eq!(Solution::divide(10, 3), 3);
assert_eq!(Solution::divide(7, -3), -2);
assert_eq!(Solution::divide(0, 1), 0);
assert_eq!(Solution::divide(1, 1), 1);
assert_eq!(Solution::divide(i32::MAX, 2), 1073741823);
assert_eq!(Solution::divide(-2147483648, -1), 2147483647);
assert_eq!(Solution::divide(-2147483648, 2), -1073741824);
assert_eq!(Solution::divide(-2147483648, -3), 715827882);
assert_eq!(Solution::divide(-1010369383, -2147483648), 0);
assert_eq!(Solution::divide(-2147483648, -2147483648), 1);
}
}

```
