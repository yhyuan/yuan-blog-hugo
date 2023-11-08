---
title: 45. jump game ii
date: '2021-06-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0045 jump game ii
---



Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



>   Example 1:
>   Input: nums <TeX>=</TeX> [2,3,1,1,4]
>   Output: 2
>   Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
>   Example 2:
>   Input: nums <TeX>=</TeX> [2,3,0,1,4]
>   Output: 2
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^4
>   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
pub fn jump(nums: Vec<i32>) -> i32 {
let n = nums.len();
let mut min_jumps: Vec<i32> = vec![i32::MAX; n];
min_jumps[0] = 0;
for (i, &num) in nums.iter().enumerate() {
let num = num as usize;
for j in 1..=num {
if i + j < nums.len() {
min_jumps[i + j] = i32::min(min_jumps[i + j], min_jumps[i] + 1);
}
}
}
min_jumps[n - 1]
}
}
*/

impl Solution {
pub fn jump(nums: Vec<i32>) -> i32 {
let n = nums.len();
let mut dp = vec![i32::MAX; n];
dp[0] = 0;
for i in 0..n {
let val = nums[i] as usize; // dp[i]
for j in 0..val {
if i + j + 1 > n - 1 {
break;
}
dp[i + j + 1] = if dp[i] == i32::MAX {i32::MAX} else {i32::min(dp[i + j + 1], dp[i] + 1)};
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
fn test_45() {
assert_eq!(Solution::jump(vec![1,2,1,1,1]), 3);
assert_eq!(Solution::jump(vec![2,3,1,1,4]), 2);
assert_eq!(Solution::jump(vec![2,3,0,1,4]), 2);
//
}
}

```
