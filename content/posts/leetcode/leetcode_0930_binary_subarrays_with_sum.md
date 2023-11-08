---
title: 930. binary subarrays with sum
date: '2022-06-12'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0930 binary subarrays with sum
---



Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.



A subarray is a contiguous part of the array.





>   Example 1:
>   Input: nums <TeX>=</TeX> [1,0,1,0,1], goal <TeX>=</TeX> 2
>   Output: 4
>   Explanation: The 4 subarrays are bolded and underlined below:
>   [<u>1,0,1</u>,0,1]
>   [<u>1,0,1,0</u>,1]
>   [1,<u>0,1,0,1</u>]
>   [1,0,<u>1,0,1</u>]
>   Example 2:
>   Input: nums <TeX>=</TeX> [0,0,0,0,0], goal <TeX>=</TeX> 0
>   Output: 15
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 3  10^4
>   	nums[i] is either 0 or 1.
>   	0 <TeX>\leq</TeX> goal <TeX>\leq</TeX> nums.length


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
let mut memo: HashMap<i32, i32> = HashMap::new();
let n = nums.len();
let mut ans = 0i32;
let mut pre_sum = 0;
for i in 0..n {
pre_sum = pre_sum + nums[i];
if pre_sum == goal {
ans += 1;
}
if memo.contains_key(&pre_sum) {
let val = *memo.get(&pre_sum).unwrap();
ans += val;
}
let next_val = pre_sum + goal;
if memo.contains_key(&next_val) {
*memo.get_mut(&next_val).unwrap() += 1;
} else {
memo.insert(next_val, 1);
}
}
ans
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_930() {
assert_eq!(Solution::num_subarrays_with_sum(vec![1,0,1,0,1], 2), 4);
assert_eq!(Solution::num_subarrays_with_sum(vec![0,0,0,0,0], 0), 15);
}
}

```
