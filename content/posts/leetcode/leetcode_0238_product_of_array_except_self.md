---
title: 238. product of array except self
date: '2021-11-23'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0238 product of array except self
---



Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



>   Example 1:
>   Input: nums <TeX>=</TeX> [1,2,3,4]
>   Output: [24,12,8,6]
>   Example 2:
>   Input: nums <TeX>=</TeX> [-1,1,0,-3,3]
>   Output: [0,0,9,0,0]
**Constraints:**
>   	2 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5
>   	-30 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 30
>   	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
>   Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
let zero_indices: Vec<usize> = (0..nums.len()).into_iter().filter(|&i| nums[i] == 0).collect();
if zero_indices.len() > 1 {
return nums.iter().map(|_| 0i32).collect();
}
if zero_indices.len() == 1 {
let index = zero_indices[0];
let multiple_result = (0..nums.len())
.into_iter()
.filter(|&i| i != index)
.map(|i| nums[i])
.fold(1, |mut sum, x| {sum *= x; sum});
return (0..nums.len()).into_iter().map(|i| if i == index {multiple_result} else {0}).collect()
}
let mut results: Vec<i32> = vec![1; nums.len()];
for i in 1..nums.len() {
results[i] = results[i - 1] * nums[i - 1];
}
let mut result = 1;
for i in (0..nums.len()-1).rev() {
result *= nums[i + 1];
results[i] *= result;
}

//println!("results: {:?}", results);
results
}
}
*/
impl Solution {
pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
let n = nums.len();
let mut left_right: Vec<i32> = vec![0; n];
let mut right_left: Vec<i32> = vec![0; n];

let mut res = 1i32;
for i in 0..n {
res *= nums[i];
left_right[i] = res;
}
res = 1i32;
for i in (0..n).rev() {
res *= nums[i];
right_left[i] = res;
}
let mut results: Vec<i32> = vec![0; n];
for i in 0..n {
if i == 0 {
results[0] = right_left[1];
} else if i == n - 1 {
results[n - 1] = left_right[n - 2];
} else {
results[i] = left_right[i - 1] * right_left[i + 1];
}
}
results
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_238() {
assert_eq!(
Solution::product_except_self(vec![1, 2, 3, 4]),
vec![24, 12, 8, 6]
);
}
}

```
