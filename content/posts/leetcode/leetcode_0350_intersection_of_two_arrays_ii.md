---
title: 350. intersection of two arrays ii
date: '2022-01-21'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0350 intersection of two arrays ii
---



Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



>   Example 1:
>   Input: nums1 <TeX>=</TeX> [1,2,2,1], nums2 <TeX>=</TeX> [2,2]
>   Output: [2,2]
>   Example 2:
>   Input: nums1 <TeX>=</TeX> [4,9,5], nums2 <TeX>=</TeX> [9,4,9,8,4]
>   Output: [4,9]
>   Explanation: [9,4] is also accepted.
**Constraints:**
>   	1 <TeX>\leq</TeX> nums1.length, nums2.length <TeX>\leq</TeX> 1000
>   	0 <TeX>\leq</TeX> nums1[i], nums2[i] <TeX>\leq</TeX> 1000
>   Follow up:
>   	What if the given array is already sorted? How would you optimize your algorithm?
>   	What if nums1's size is small compared to nums2's size? Which algorithm is better?
>   	What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
pub fn convert_vec_to_hashmap(nums: Vec<i32>) -> HashMap<i32, usize> {
let mut hashmap1: HashMap<i32, usize> = HashMap::new();
for num in nums {
if hashmap1.contains_key(&num) {
hashmap1.insert(num, hashmap1[&num] + 1);
} else {
hashmap1.insert(num,  1);
}
}
hashmap1
}
pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
let hashmap1 = Solution::convert_vec_to_hashmap(nums1);
let hashmap2 = Solution::convert_vec_to_hashmap(nums2);
let mut result: Vec<i32> = vec![];
for (k1, &v1) in hashmap1.iter() {
if hashmap2.contains_key(k1) {
let val = usize::min(v1, hashmap2[k1]);
for i in 0..val {
result.push(*k1);
}
}
}
result
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_350() {
assert_eq!(Solution::intersect(vec![1,2,2,1], vec![2,2]), vec![2, 2]);
assert_eq!(Solution::intersect(vec![4,9,5], vec![9,4,9,8,4]), vec![4,9]);
}
}

```
