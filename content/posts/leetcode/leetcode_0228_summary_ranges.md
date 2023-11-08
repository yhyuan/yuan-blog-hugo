---
title: 228. summary ranges
date: '2021-11-14'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0228 summary ranges
---



You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:



"a->b" if a !<TeX>=</TeX> b

"a" if a <TeX>=</TeX><TeX>=</TeX> b





>   Example 1:
>   Input: nums <TeX>=</TeX> [0,1,2,4,5,7]
>   Output: ["0->2","4->5","7"]
>   Explanation: The ranges are:
>   [0,2] --> "0->2"
>   [4,5] --> "4->5"
>   [7,7] --> "7"
>   Example 2:
>   Input: nums <TeX>=</TeX> [0,2,3,4,6,8,9]
>   Output: ["0","2->4","6","8->9"]
>   Explanation: The ranges are:
>   [0,0] --> "0"
>   [2,4] --> "2->4"
>   [6,6] --> "6"
>   [8,9] --> "8->9"
>   Example 3:
>   Input: nums <TeX>=</TeX> []
>   Output: []
>   Example 4:
>   Input: nums <TeX>=</TeX> [-1]
>   Output: ["-1"]
>   Example 5:
>   Input: nums <TeX>=</TeX> [0]
>   Output: ["0"]
**Constraints:**
>   	0 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 20
>   	-2^31 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1
>   	All the values of nums are unique.
>   	nums is sorted in ascending order.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
if nums.len() == 0 {
return vec![];
}
let mut ranges: Vec<Vec<i32>> = vec![];
let mut range = vec![nums[0], nums[0]];
for i in 1..nums.len() {
if nums[i] == (range[1] + 1) {
range[1] = nums[i];
} else {
ranges.push(vec![range[0], range[1]]);
range = vec![nums[i], nums[i]];
}
}
ranges.push(vec![range[0], range[1]]);
ranges.iter().map(|range| if range[0] == range[1] {format!("{}", range[0])} else {format!("{}->{}", range[0], range[1])}).collect()
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_228() {
assert_eq!(
Solution::summary_ranges(vec![0, 1, 2, 3, 4, 5, 6]),
vec_string!["0->6"]
);
}
}

```
