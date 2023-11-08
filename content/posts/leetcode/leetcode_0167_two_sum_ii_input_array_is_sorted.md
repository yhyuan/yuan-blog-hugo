---
title: 167. two sum ii input array is sorted
date: '2021-10-02'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0167 two sum ii input array is sorted
---



Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <TeX>\leq</TeX> answer[0] < answer[1] <TeX>\leq</TeX> numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.



>   Example 1:
>   Input: numbers <TeX>=</TeX> [2,7,11,15], target <TeX>=</TeX> 9
>   Output: [1,2]
>   Explanation: The sum of 2 and 7 is 9. Therefore index1 <TeX>=</TeX> 1, index2 <TeX>=</TeX> 2.
>   Example 2:
>   Input: numbers <TeX>=</TeX> [2,3,4], target <TeX>=</TeX> 6
>   Output: [1,3]
>   Example 3:
>   Input: numbers <TeX>=</TeX> [-1,0], target <TeX>=</TeX> -1
>   Output: [1,2]
**Constraints:**
>   	2 <TeX>\leq</TeX> numbers.length <TeX>\leq</TeX> 3  10^4
>   	-1000 <TeX>\leq</TeX> numbers[i] <TeX>\leq</TeX> 1000
>   	numbers is sorted in non-decreasing order.
>   	-1000 <TeX>\leq</TeX> target <TeX>\leq</TeX> 1000
>   	The tests are generated such that there is exactly one solution.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
let mut begin = 0usize;
let mut end = numbers.len() - 1;
while end >= begin {
let max_val = target - numbers[begin];
while numbers[end] > max_val {
end -= 1;
}
if numbers[begin] + numbers[end] == target {
return vec![begin as i32 + 1, end as i32 + 1];
}
begin += 1;
}
vec![0, 0]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_167() {
assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![1, 2]);
assert_eq!(Solution::two_sum(vec![2, 3, 4], 6), vec![1, 3]);
assert_eq!(Solution::two_sum(vec![-1, 0], -1), vec![1, 2]);
assert_eq!(Solution::two_sum(vec![-1, 0, 1, 2, 7, 11, 15], 9), vec![4, 5]);
}
}

```
