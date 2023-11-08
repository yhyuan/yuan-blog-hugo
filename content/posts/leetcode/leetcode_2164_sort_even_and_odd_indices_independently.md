---
title: 2164. sort even and odd indices independently
date: '2022-09-16'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2164 sort even and odd indices independently
---


You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:



Sort the values at odd indices of nums in non-increasing order.

For example, if nums <TeX>=</TeX> [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.

Sort the values at even indices of nums in non-decreasing order.

For example, if nums <TeX>=</TeX> [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.

Return the array formed after rearranging the values of nums.







> Example 1:
> Input: nums <TeX>=</TeX> [4,1,2,3]
> Output: [2,3,4,1]
> Explanation:
> First, we sort the values present at odd indices (1 and 3) in non-increasing order.
> So, nums changes from [4,1,2,3] to [4,3,2,1].
> Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
> So, nums changes from [4,1,2,3] to [2,3,4,1].
> Thus, the array formed after rearranging the values is [2,3,4,1].
> Example 2:
> Input: nums <TeX>=</TeX> [2,1]
> Output: [2,1]
> Explanation:
> Since there is exactly one odd index and one even index, no rearrangement of values takes place.
> The resultant array formed is [2,1], which is the same as the initial array.
**Constraints:**
> 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 100


## Solution


### Rust
```rust
pub struct Solution {}

impl Solution {
pub fn sort_even_odd(nums: Vec<i32>) -> Vec<i32> {
let n = nums.len();
let mut odd_index_vec: Vec<usize> = (0usize..n).into_iter().filter(|i| i % 2 == 1).collect();
odd_index_vec.sort_by(|a, b| nums[*b].partial_cmp(&nums[*a]).unwrap());;
let mut even_index_vec: Vec<usize> = (0usize..n).into_iter().filter(|i| i % 2 == 0).collect();
even_index_vec.sort_by(|a, b| nums[*a].partial_cmp(&nums[*b]).unwrap());;
let result: Vec<i32> = (0..n).into_iter()
.map(|i| if i % 2 == 0 {nums[even_index_vec[i/2]]} else {nums[odd_index_vec[ (i -1) /2]]})
.collect();
//println!("{:?}", odd_index_vec);
//println!("{:?}", even_index_vec);

result
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_2164() {
assert_eq!(Solution::sort_even_odd(vec![4,1,2,3]), vec![2,3,4,1]);
}
}


```
