---
title: 264. ugly number ii
date: '2021-12-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0264 ugly number ii
---



An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the n^th ugly number.



>   Example 1:
>   Input: n <TeX>=</TeX> 10
>   Output: 12
>   Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
>   Example 2:
>   Input: n <TeX>=</TeX> 1
>   Output: 1
>   Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1690


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn nth_ugly_number(n: i32) -> i32 {
let n = n as usize;
let mut two = 0;
let mut three = 0;
let mut five = 0;
let mut dp: Vec<i32> = vec![1; n as usize];
for i in 1..n {
let two_multiple = 2 * dp[two];
let three_multiple = 3 * dp[three];
let five_multiple = 5 * dp[five];

dp[i] = i32::min(two_multiple , i32::min(three_multiple , five_multiple));
if(dp[i] == two_multiple){
two += 1;
}
if(dp[i] == three_multiple){
three += 1;
}
if(dp[i] == five_multiple){
five += 1;
}
}
dp[n - 1]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_264() {
assert_eq!(Solution::nth_ugly_number(10), 12);
assert_eq!(Solution::nth_ugly_number(1), 1);
assert_eq!(Solution::nth_ugly_number(1352), 0);
}
}

```
