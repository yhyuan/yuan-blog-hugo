---
title: 2154. keep multiplying found values by two
date: '2022-09-10'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2154 keep multiplying found values by two
---


You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.



You then do the following steps:



If original is found in nums, multiply it by two (i.e., set original <TeX>=</TeX> 2  original).

Otherwise, stop the process.

Repeat this process with the new number as long as you keep finding the number.

Return the final value of original.







> Example 1:
> Input: nums <TeX>=</TeX> [5,3,6,1,12], original <TeX>=</TeX> 3
> Output: 24
> Explanation:
> - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
> - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
> - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
> - 24 is not found in nums. Thus, 24 is returned.
> Example 2:
> Input: nums <TeX>=</TeX> [2,7,9], original <TeX>=</TeX> 4
> Output: 4
> Explanation:
> - 4 is not found in nums. Thus, 4 is returned.
**Constraints:**
> 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 1000
> 1 <TeX>\leq</TeX> nums[i], original <TeX>\leq</TeX> 1000


## Solution


### Rust
```rust

pub struct Solution {}


// submission codes start here

use std::collections::HashSet;
use std::iter::FromIterator;
impl Solution {
pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
let hashset: HashSet<i32> = HashSet::from_iter(nums.iter().cloned());
/*let mut hashset: HashSet<i32> = HashSet::new();
for i in 0..nums.len() {
hashset.insert(nums[i]);
}
*/
let mut result = original;
while hashset.contains(&result) {
result = result * 2;
}
result
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_2154() {
assert_eq!(Solution::find_final_value(vec![5,3,6,1,12], 3), 24);
}
}

```
