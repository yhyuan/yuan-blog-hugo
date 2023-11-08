---
title: 34. find first and last position of element in sorted array
date: '2021-06-04'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0034 find first and last position of element in sorted array
---



Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



>   Example 1:
>   Input: nums <TeX>=</TeX> [5,7,7,8,8,10], target <TeX>=</TeX> 8
>   Output: [3,4]
>   Example 2:
>   Input: nums <TeX>=</TeX> [5,7,7,8,8,10], target <TeX>=</TeX> 6
>   Output: [-1,-1]
>   Example 3:
>   Input: nums <TeX>=</TeX> [], target <TeX>=</TeX> 0
>   Output: [-1,-1]
**Constraints:**
>   	0 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5
>   	-10^9 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9
>   	nums is a non-decreasing array.
>   	-10^9 <TeX>\leq</TeX> target <TeX>\leq</TeX> 10^9


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
/*
pub fn search_range_left_bound(nums: &Vec<i32>, target: i32, start: usize, end: usize) -> i32 {
if start == end {
return start as i32;
}
if start + 1 == end {
if nums[start] == target {
return start as i32;
} else {
return end as i32;
}
}
let middle = (start + end) / 2;
if nums[middle] == target {
Solution::search_range_left_bound(nums, target, start, middle)
} else {
Solution::search_range_left_bound(nums, target, middle, end)
}
}
pub fn search_range_right_bound(nums: &Vec<i32>, target: i32, start: usize, end: usize) -> i32 {
if start == end {
return start as i32;
}
if start + 1 == end {
if nums[end] == target {
return end as i32;
} else {
return start as i32;
}
}
let middle = (start + end) / 2;
if nums[middle] == target {
Solution::search_range_right_bound(nums, target, middle, end)
} else {
Solution::search_range_right_bound(nums, target, start, middle)
}
}
pub fn search_range_helper(nums: &Vec<i32>, target: i32, start: usize, end: usize) -> Vec<i32> {
if start == end {
if nums[start] == target {
return vec![start as i32, end as i32];
} else {
return vec![-1, -1];
}
}
if start + 1 == end {
if nums[start] == nums[end] {
if nums[start] == target {
return vec![start as i32, end as i32];
} else {
return vec![-1, -1];
}
} else if nums[start] == target {
return vec![start as i32, start as i32];
} else if nums[end] == target {
return vec![end as i32, end as i32];
} else {
return vec![-1, -1];
}
}
let middle = (start + end) / 2;
if nums[middle] == target {
let left = Solution::search_range_left_bound(nums, target, start, middle);
let right = Solution::search_range_right_bound(nums, target, middle, end);
return vec![left, right];
} else if nums[middle] > target {
Solution::search_range_helper(nums, target, start, middle - 1)
} else {
Solution::search_range_helper(nums, target, middle + 1, end)
}
//vec![]
}
pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
if nums.len() == 0 {
return vec![-1, -1];
}
if nums.len() == 1 {
if target == nums[0] {
return vec![0, 0];
} else {
return vec![-1, -1];
}
}
Solution::search_range_helper(&nums, target, 0, nums.len() - 1)
}
*/
pub fn search_right_end(nums: &Vec<i32>, target: i32) -> i32 {
let mut low = 0;
let mut high = nums.len() - 1;
while low + 1 < high {
let mid = low + (high - low) / 2;
if nums[mid] > target {
high = mid;
} else if nums[mid] <= target {
low = mid;
}
}
if nums[high] == target {
return high as i32;
}
if nums[low] == target {
return low as i32;
}
return -1;
}
pub fn search_left_end(nums: &Vec<i32>, target: i32) -> i32 {
let mut low = 0;
let mut high = nums.len() - 1;
while low + 1 < high {
let mid = low + (high - low) / 2;
if nums[mid] >= target {
high = mid;
} else if nums[mid] < target {
low = mid;
}
}
if nums[low] == target {
return low as i32;
}
if nums[high] == target {
return high as i32;
}
return -1;
}

pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
let n = nums.len();
if n == 0 {
return vec![-1, -1];
}
vec![Self::search_left_end(&nums, target), Self::search_right_end(&nums, target)]
}

}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_34() {
assert_eq!(Solution::search_range(vec![5, 7, 7, 8, 8, 10], 8), vec![3, 4]);
assert_eq!(Solution::search_range(vec![5, 7, 7, 8, 8, 10], 6), vec![-1, -1]);
assert_eq!(Solution::search_range(vec![2, 2], 1), vec![-1, -1]);
assert_eq!(Solution::search_range(vec![1, 1, 2], 1), vec![0, 1]);
}
}

```
