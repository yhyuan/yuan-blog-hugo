---
title: 260. single number iii
date: '2021-12-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0260 single number iii
---



Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



>   Example 1:
>   Input: nums <TeX>=</TeX> [1,2,1,3,2,5]
>   Output: [3,5]
>   Explanation:  [5, 3] is also a valid answer.
>   Example 2:
>   Input: nums <TeX>=</TeX> [-1,0]
>   Output: [-1,0]
>   Example 3:
>   Input: nums <TeX>=</TeX> [0,1]
>   Output: [1,0]
**Constraints:**
>   	2 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 3  10^4
>   	-2^31 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1
>   	Each integer in nums will appear twice, only two integers will appear once.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn get_bit(num: i32, pos: u8) -> i32 {
num >> pos & 1i32
}
pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
if nums.len() == 2 {
return nums;
}
let mut xor = nums.iter().fold(0i32, |sum, &val| sum ^ val);
let mut i: u8 = 0;

//let bit_value = Solution::get_bit(xor, 31);
//println!("xor: {:b}", xor);
//println!("bit_valu: {}", bit_value);
while xor != 0 {
xor = xor >> 1;
i += 1;
if i > 31 {
break;
}
}
i = i - 1;
//leftest bit.
let mut group_1: i32 = 0;
let mut group_0: i32 = 0;
for &num in nums.iter() {
let bit_value = Solution::get_bit(num, i);
if bit_value == 1 {
group_1 = group_1 ^ num;
} else {
group_0 = group_0 ^ num;
}
}
if group_1 > group_0 {vec![group_0, group_1]} else {vec![group_1, group_0]}
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_260() {
assert_eq!(Solution::single_number(vec![1,1,0,-2147483648]), vec![-2147483648, 0]);
assert_eq!(Solution::single_number(vec![1, 2, 1, 2, 3, 4]), vec![3, 4]);
assert_eq!(Solution::single_number(vec![1, 2, 1, 3, 2, 5]), vec![3, 5]);
}
}

```
