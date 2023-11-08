---
title: 416. partition equal subset sum
date: '2022-03-05'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0416 partition equal subset sum
---



Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



>   Example 1:
>   Input: nums <TeX>=</TeX> [1,5,11,5]
>   Output: true
>   Explanation: The array can be partitioned as [1, 5, 5] and [11].
>   Example 2:
>   Input: nums <TeX>=</TeX> [1,2,3,5]
>   Output: false
>   Explanation: The array cannot be partitioned into equal sum subsets.
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 200
>   	1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 100


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
pub fn helper(nums: &Vec<i32>, memo: &mut HashMap<(usize, i32), bool>, index: usize, target: i32) -> bool {
if memo.contains_key(&(index, target)) {
return memo[&(index, target)];
}
if nums[index] > target {
if index == 0 {
memo.insert((index, target), false);
return false;
} else {
let res = Self::helper(nums, memo, index - 1, target);
memo.insert((index, target), res);
}
}
if nums[index] == target {
memo.insert((index, target), true);
return true;
}
if index == 0 {
memo.insert((index, target), false);
return false;
}
let mut res = Self::helper(nums, memo, index - 1, target - nums[index]);
res = res || Self::helper(nums, memo, index - 1, target);
memo.insert((index, target), res);
res
}
pub fn can_partition(nums: Vec<i32>) -> bool {
let total = nums.iter().sum::<i32>();
if total % 2 != 0 {
return false;
}
let half = total / 2;
//let mut nums = nums;
//nums.sort();
let n = nums.len();
let mut memo: HashMap<(usize, i32), bool> = HashMap::new();
Self::helper(&nums, &mut memo, n - 1, half)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_416() {
assert_eq!(Solution::can_partition(vec![14,9,8,4,3,2]), true);
assert_eq!(Solution::can_partition(vec![1,5,11,5]), true);
assert_eq!(Solution::can_partition(vec![1,2,3,5]), false);
}
}

```
