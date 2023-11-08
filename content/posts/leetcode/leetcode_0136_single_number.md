---
title: 136. single number
date: '2021-09-11'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0136 single number
---



Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



>   Example 1:
>   Input: nums <TeX>=</TeX> [2,2,1]
>   Output: 1
>   Example 2:
>   Input: nums <TeX>=</TeX> [4,1,2,1,2]
>   Output: 4
>   Example 3:
>   Input: nums <TeX>=</TeX> [1]
>   Output: 1
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 3  10^4
>   	-3  10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 3  10^4
>   	Each element in the array appears twice except for one element which appears only once.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn single_number(nums: Vec<i32>) -> i32 {
nums.iter().fold(0i32, |sum, &val| sum ^ val)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_136() {
assert_eq!(Solution::single_number(vec![2, 2, 1]), 1);
assert_eq!(Solution::single_number(vec![4, 1, 2, 1, 2]), 4);
}
}

```
