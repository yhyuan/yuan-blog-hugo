---
title: 1248. count number of nice subarrays
date: '2022-07-22'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1248 count number of nice subarrays
---



Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.



Return the number of nice sub-arrays.





>   Example 1:
>   Input: nums <TeX>=</TeX> [1,1,2,1,1], k <TeX>=</TeX> 3
>   Output: 2
>   Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
>   Example 2:
>   Input: nums <TeX>=</TeX> [2,4,6], k <TeX>=</TeX> 1
>   Output: 0
>   Explanation: There is no odd numbers in the array.
>   Example 3:
>   Input: nums <TeX>=</TeX> [2,2,2,1,2,2,1,2,2,2], k <TeX>=</TeX> 2
>   Output: 16
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 50000
>   	1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^5
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> nums.length


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn number_of_subarrays_at_most(nums: &Vec<i32>, k: usize) -> i32 {
let n = nums.len();
let mut i = 0usize;
let mut j = 0usize;
let mut ans = 0;
let mut count = if nums[i] % 2 == 0 { 0 } else {1};
while j < n {
if count <= k { // at most k
ans += (j - i + 1) as i32; // number of subarrays which start i end j.
j += 1;
if j < n {
count += if nums[j] % 2 == 0 { 0 } else {1};
}
} else {
count -= if nums[i] % 2 == 0 { 0 } else {1};
i += 1;
}
}
ans
}
pub fn number_of_subarrays(nums: Vec<i32>, k: i32) -> i32 {
Self::number_of_subarrays_at_most(&nums, k as usize) - Self::number_of_subarrays_at_most(&nums, k as usize - 1)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1248() {
assert_eq!(Solution::number_of_subarrays(vec![1,1,2,1,1], 3), 2);
assert_eq!(Solution::number_of_subarrays(vec![2,4,6], 1), 0);
assert_eq!(Solution::number_of_subarrays(vec![2,2,2,1,2,2,1,2,2,2], 2), 16);
}
}

```
