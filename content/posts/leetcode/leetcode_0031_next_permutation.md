---
title: 31. next permutation
date: '2021-06-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0031 next permutation
---



Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be [in place](http://en.wikipedia.org/wiki/In-place_algorithm) and use only constant extra memory.



>   Example 1:
>   Input: nums <TeX>=</TeX> [1,2,3]
>   Output: [1,3,2]
>   Example 2:
>   Input: nums <TeX>=</TeX> [3,2,1]
>   Output: [1,2,3]
>   Example 3:
>   Input: nums <TeX>=</TeX> [1,1,5]
>   Output: [1,5,1]
>   Example 4:
>   Input: nums <TeX>=</TeX> [1]
>   Output: [1]
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 100
>   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 100


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn swap(nums: &mut Vec<i32>, i: usize, j: usize) {
let temp = nums[i];
nums[i] = nums[j];
nums[j] = temp;
}
pub fn next_permutation(nums: &mut Vec<i32>) {
let n = nums.len();
let mut index = usize::MAX;
for i in (1..nums.len()).rev() {
if nums[i] > nums[i - 1] {
index = i;
break;
}
}
// For sorted Array, index is len - 1. for reversed sorted array, index = MAX.
if index == usize::MAX { // reverse array
for i in 0..nums.len()/2 {
Solution::swap(nums, i,  n - 1 - i);
}
return;
}
let value = nums[index - 1];
if index == n - 1 {
Solution::swap(nums, n - 1, n - 2);
return;
}
//nums[index - 1] = value + 1;
//println!("index: {}", index);
let swap_size = n - index;
for i in 0..swap_size / 2 {
Solution::swap(nums, index + i,  n - 1 - i);
}
//println!("nums: {:?}", nums);
let mut find_index = usize::MAX;
for i in index..n {
if nums[i] > nums[index - 1] {
find_index = i;
break;
}
}
Solution::swap(nums, index - 1, find_index);
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_31() {
/*
let mut vec1 = vec![1, 2, 3, 4, 5];
Solution::next_permutation(&mut vec1);
assert_eq!(vec1, vec![1, 2, 3, 5, 4]);

let mut vec2 = vec![5, 4, 3, 2, 1];
Solution::next_permutation(&mut vec2);
assert_eq!(vec2, vec![1, 2, 3, 4, 5]);

let mut vec3 = vec![1, 1, 5];
Solution::next_permutation(&mut vec3);
assert_eq!(vec3, vec![1, 5, 1]);
*/
let mut vec4 = vec![2, 3, 1];
Solution::next_permutation(&mut vec4);
assert_eq!(vec4, vec![3, 1, 2]);
}
}

```
