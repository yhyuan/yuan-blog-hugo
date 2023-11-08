---
title: 673. number of longest increasing subsequence
date: '2022-04-17'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0673 number of longest increasing subsequence
---



Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.



>   Example 1:
>   Input: nums <TeX>=</TeX> [1,3,5,4,7]
>   Output: 2
>   Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
>   Example 2:
>   Input: nums <TeX>=</TeX> [2,2,2,2,2]
>   Output: 5
>   Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 2000
>   	-10^6 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^6


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
let n = nums.len();
let mut dp: Vec<i32> = vec![0; n];
let mut dp_counts: Vec<i32> = vec![0; n];
dp[0] = 1;
dp_counts[0] = 1;
for i in 1..n {
dp[i] = 1;
dp_counts[i] = 1;
for j in 0..i {
if nums[j] < nums[i] {
if dp[j] + 1 > dp[i] {
dp[i] = dp[j] + 1;
dp_counts[i] = dp_counts[j];
} else if dp[j] + 1 == dp[i] {
dp_counts[i] += dp_counts[j];
}
}
}
}
//println!("dp: {:?}", dp);
//println!("dp_counts: {:?}", dp_counts);
let max_val = *dp.iter().max().unwrap();
let mut res = 0;
for i in 0..n {
if dp[i] == max_val {
res += dp_counts[i];
}
}
res
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_673() {
assert_eq!(Solution::find_number_of_lis(vec![1,3,5,4,7]), 2);
assert_eq!(Solution::find_number_of_lis(vec![2,2,2,2,2]), 5);
}
}

```
