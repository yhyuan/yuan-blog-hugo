---
title: 1. two sum
date: '2021-05-02'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0001 two sum
---



Given an array of integers, return indices of the two numbers such that they

add up to a specific target.



You may assume that each input would have exactly one solution, and you may

not use the same element twice.



> Example:
>   Given nums <TeX>=</TeX> [2, 7, 11, 15], target <TeX>=</TeX> 9,
>   Because nums[0] + nums[1] <TeX>=</TeX> 2 + 7 <TeX>=</TeX> 9,
>   return [0, 1].


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::HashMap;
impl Solution {
pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
let mut hashmap: HashMap<i32, usize> = HashMap::with_capacity(nums.len());
for (i, num) in nums.iter().enumerate() {
match hashmap.get(&num) {
None => {
hashmap.insert(target - num, i);
}
Some(&index) => {
return vec![index as i32, i as i32];
}
}
}
vec![]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1() {
assert_eq!(vec![0, 1], Solution::two_sum(vec![2, 7, 11, 15], 9));
assert_eq!(vec![1, 2], Solution::two_sum(vec![3, 2, 4], 6));
}
}

```
