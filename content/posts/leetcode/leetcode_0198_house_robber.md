---
title: 198. house robber
date: '2021-10-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0198 house robber
---



You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



>   Example 1:
>   Input: nums <TeX>=</TeX> [1,2,3,1]
>   Output: 4
>   Explanation: Rob house 1 (money <TeX>=</TeX> 1) and then rob house 3 (money <TeX>=</TeX> 3).
>   Total amount you can rob <TeX>=</TeX> 1 + 3 <TeX>=</TeX> 4.
>   Example 2:
>   Input: nums <TeX>=</TeX> [2,7,9,3,1]
>   Output: 12
>   Explanation: Rob house 1 (money <TeX>=</TeX> 2), rob house 3 (money <TeX>=</TeX> 9) and rob house 5 (money <TeX>=</TeX> 1).
>   Total amount you can rob <TeX>=</TeX> 2 + 9 + 1 <TeX>=</TeX> 12.
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 100
>   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 400


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
pub fn helper(nums: &Vec<i32>, index: usize, rob_result: &mut Vec<i32>) -> i32 {
if rob_result[index] > 0 {
return rob_result[index];
}
//println!("index: {}", index);
let diff = nums.len() - index;
if diff == 1 {
rob_result[index] = nums[index];
return nums[index];
}
if diff == 2 {
rob_result[index] = i32::max(nums[index], nums[index + 1]);
return rob_result[index];
}
let do_not_rob_this = Solution::helper(nums, index + 1, rob_result);
let do_rob_this = nums[index] + Solution::helper(nums, index + 2, rob_result);
rob_result[index] = i32::max(do_not_rob_this, do_rob_this);
rob_result[index]
}

pub fn remove_zero(nums: Vec<i32>) -> Vec<i32> {
let mut new_nums: Vec<i32> = vec![];
let mut is_zero_status = false;
for &num in nums.iter() {
if num == 0 {
if !is_zero_status {
new_nums.push(num);
is_zero_status = true;
}
} else {
if is_zero_status {
is_zero_status = false;
}
new_nums.push(num);
}
}
new_nums
}

pub fn rob(nums: Vec<i32>) -> i32 {
if nums.len() == 0 {
return 0i32;
}
let nums = Solution::remove_zero(nums);
//println!("{:?}", nums);
let mut rob_result: Vec<i32> = vec![0; nums.len()];
Solution::helper(&nums, 0, &mut rob_result);
rob_result[0]
}
}
*/
/*
impl Solution {
pub fn rob(nums: Vec<i32>) -> i32 {
if nums.len() == 0 {
return 0i32;
}
let mut dp: Vec<i32> = vec![0; nums.len()];
dp[0] = nums[0];
if nums.len() == 1 {
return dp[0];
}
dp[1] = i32::max(nums[0], nums[1]);
for i in 2..nums.len() {
dp[i] = i32::max(dp[i - 1], nums[i] + dp[i - 2]);
}
dp[nums.len() - 1]
}
}
*/
impl Solution {
pub fn rob(nums: Vec<i32>) -> i32 {
let n = nums.len();
if n == 1 {
return nums[0];
}
if n == 2 {
return i32::max(nums[0], nums[1]);
}
let mut dp = (nums[0], i32::max(nums[0], nums[1]));
for i in 3..=n {
dp = (dp.1, i32::max(dp.1, dp.0 + nums[i - 1]));
}
dp.1
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_198() {
assert_eq!(Solution::rob(vec![2, 7, 9, 3, 1]), 12);
assert_eq!(Solution::rob(vec![2, 7, 9, 10, 1]), 17);
assert_eq!(Solution::rob(vec![2, 1, 1, 2]), 4);
assert_eq!(Solution::rob(vec![0]), 0);
}
}

```
