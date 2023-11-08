---
title: 89. gray code
date: '2021-07-29'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0089 gray code
---



An n-bit gray code sequence is a sequence of 2^n integers where:



Every integer is in the inclusive range [0, 2^n - 1],

The first integer is 0,

An integer appears no more than once in the sequence,

The binary representation of every pair of adjacent integers differs by exactly one bit, and

The binary representation of the first and last integers differs by exactly one bit.



Given an integer n, return any valid n-bit gray code sequence.



>   Example 1:
>   Input: n <TeX>=</TeX> 2
>   Output: [0,1,3,2]
>   Explanation:
>   The binary representation of [0,1,3,2] is [00,01,11,10].
>   - 0<u>0</u> and 0<u>1</u> differ by one bit
>   - <u>0</u>1 and <u>1</u>1 differ by one bit
>   - 1<u>1</u> and 1<u>0</u> differ by one bit
>   - <u>1</u>0 and <u>0</u>0 differ by one bit
>   [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
>   - <u>0</u>0 and <u>1</u>0 differ by one bit
>   - 1<u>0</u> and 1<u>1</u> differ by one bit
>   - <u>1</u>1 and <u>0</u>1 differ by one bit
>   - 0<u>1</u> and 0<u>0</u> differ by one bit
>   Example 2:
>   Input: n <TeX>=</TeX> 1
>   Output: [0,1]
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 16


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn gray_code(n: i32) -> Vec<i32> {
if n == 0 {
return vec![0];
}
if n == 1 {
return vec![0, 1];
}
let mut pre_result: Vec<i32> = vec![0, 1];
for i in 2..=n {
let mut cur_result: Vec<i32> = Vec::with_capacity(pre_result.len() * 2); //vec![0];
cur_result.push(0);
for j in 0..pre_result.len() {
cur_result.push(2_i32.pow(i as u32 - 1) + pre_result[j]);
}
for j in 1..pre_result.len() {
cur_result.push(pre_result[j]);
}
pre_result = cur_result;
}
pre_result
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_89() {
assert_eq!(Solution::gray_code(2), vec![0, 2, 3, 1]);
assert_eq!(Solution::gray_code(1), vec![0, 1]);
assert_eq!(Solution::gray_code(0), vec![0]);
assert_eq!(Solution::gray_code(3), vec![0, 4, 6, 7, 5, 2, 3, 1]);
}
}

```
