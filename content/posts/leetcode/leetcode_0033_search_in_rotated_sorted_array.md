---
title: 33. search in rotated sorted array
date: '2021-06-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0033 search in rotated sorted array
---



There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <TeX>\leq</TeX> k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



>   Example 1:
>   Input: nums <TeX>=</TeX> [4,5,6,7,0,1,2], target <TeX>=</TeX> 0
>   Output: 4
>   Example 2:
>   Input: nums <TeX>=</TeX> [4,5,6,7,0,1,2], target <TeX>=</TeX> 3
>   Output: -1
>   Example 3:
>   Input: nums <TeX>=</TeX> [1], target <TeX>=</TeX> 0
>   Output: -1
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 5000
>   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4
>   	All values of nums are unique.
>   	nums is guaranteed to be rotated at some pivot.
>   	-10^4 <TeX>\leq</TeX> target <TeX>\leq</TeX> 10^4


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
/*
pub fn find_min_value_index(nums: &Vec<i32>, start: usize, end: usize) -> usize {
if start + 1 == end {
if nums[end] < nums[start] {
return end;
}
}
let mid = (start + end) / 2;
if nums[mid] < nums[end] {
Solution::find_min_value_index(nums, start, mid)
} else {
Solution::find_min_value_index(nums, mid, end)
}
}
pub fn get_value(nums: &Vec<i32>, index: usize, shift: usize) -> i32 {
nums[(index + shift) % nums.len()]
}
pub fn binary_search_helper(nums: &Vec<i32>, target: i32, start: usize, end: usize, shift: usize) -> i32 {
if start == end {
if Solution::get_value(nums, start, shift) == target {
return start as i32;
} else {
return -1_i32;
}
}
if start + 1 == end {
let start_val = Solution::get_value(nums, start, shift);
let end_val = Solution::get_value(nums, end, shift);
if start_val == target {
return start as i32;
}
if end_val == target {
return end as i32;
}
return -1;
}
let mid = (start + end) / 2;
let mid_value = Solution::get_value(nums, mid, shift);
if mid_value == target {
return mid as i32;
}
if mid_value > target {
Solution::binary_search_helper(nums, target, start, mid, shift)
} else {
Solution::binary_search_helper(nums, target, mid, end, shift)
}
}
pub fn search(nums: Vec<i32>, target: i32) -> i32 {
if nums.len() == 0 {
return -1;
}
let mut shift = 0usize;
if nums[0] > nums[nums.len() - 1] { //shift value is 0.
shift = Solution::find_min_value_index(&nums, 0, nums.len() - 1);
}
//println!("shift: {}", shift);
let index = Solution::binary_search_helper(&nums, target, 0, nums.len() - 1, shift);
if index == -1 {
return index;
}
((index as usize + shift) % nums.len()) as i32
}
*/
pub fn search(nums: Vec<i32>, target: i32) -> i32 {
let n = nums.len();
if n == 0 {
return -1;
}
let shift =  if nums[0] < nums[n - 1] {
0usize
} else {
let mut low = 0;
let mut high = n - 1;
while low + 1 < high {
let mid = low + (high - low) / 2;
if nums[mid] > nums[low] {
low = mid;
} else {
high = mid;
}
}
high
};
let mut low = shift;
let mut high = shift + n - 1;
while low + 1 < high {
let mid = low + (high - low) / 2;
if nums[mid % n] > target {
high = mid;
} else if nums[mid % n] < target {
low = mid;
} else {
return (mid % n) as i32;
}
}
if nums[low % n] == target {
return (low % n) as i32;
}
if nums[high % n] == target {
return (high % n) as i32;
}
-1
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_33() {
assert_eq!(Solution::search(vec![7, 8, 1, 2, 3, 4, 5, 6], 2), 3);
assert_eq!(Solution::search(vec![4, 5, 6, 7, 0, 1, 2], 3), -1);
assert_eq!(
Solution::search(
vec![
1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 0, 1, 2, 3, 4, 5, 6, 7, 8
],
0
),
9
);
assert_eq!(
Solution::search(
vec![
1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 0, 1, 2, 3, 4, 5, 6, 7, 8
],
1006
),
2
);
assert_eq!(Solution::search(vec![], 3), -1);
}
}

```
