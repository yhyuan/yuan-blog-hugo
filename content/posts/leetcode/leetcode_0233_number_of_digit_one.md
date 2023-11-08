---
title: 233. number of digit one
date: '2021-11-19'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0233 number of digit one
---



Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.



>   Example 1:
>   Input: n <TeX>=</TeX> 13
>   Output: 6
>   Example 2:
>   Input: n <TeX>=</TeX> 0
>   Output: 0
**Constraints:**
>   	0 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^9


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
/*
pub fn count_digit_one(n: i32) -> i32 {
let mut result = 0i32;
for i in 1..=n {
let size = format!("{}", i).chars().filter(|&ch| ch == '1').count();
result += size as i32;
}
result
}
*/
pub fn count_digit_one(n: i32) -> i32 {
if n < 10 {
return if n >= 1 {1} else {0};
}
let mut counts: Vec<i32> = vec![0; 11];
counts[1] = 1; // < 10, <100, <1000,
for i in 2..10 {
counts[i] = 10 * counts[i - 1] + (10u32.pow(i as u32 - 1)) as i32;
}
//println!("counts: {:?}", counts);
let chars: Vec<char> = format!("{}", n).chars().collect();
let size = chars.len();
let digit = (chars[0] as u8 - '0' as u8) as usize;
let next_n = n as u32 % 10u32.pow(size as u32 - 1);
//println!("next_n: {}", next_n);
if digit == 1 {
counts[size - 1] + next_n as i32 + 1i32 + Self::count_digit_one(next_n as i32)
} else {//digit== 2, 3, 4, 5, 6, 7, 8, 9
// d00000
let val = (digit as i32) * counts[size - 1] + 10u32.pow(size as u32 - 1) as i32;
return val + Self::count_digit_one(next_n as i32)
}
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_233() {
assert_eq!(Solution::count_digit_one(13), 6);
assert_eq!(Solution::count_digit_one(0), 0);
assert_eq!(Solution::count_digit_one(100), 21);
assert_eq!(Solution::count_digit_one(20), 12);
assert_eq!(Solution::count_digit_one(999), 300);
assert_eq!(Solution::count_digit_one(99), 20);
assert_eq!(Solution::count_digit_one(199), 140);
}
}

```
