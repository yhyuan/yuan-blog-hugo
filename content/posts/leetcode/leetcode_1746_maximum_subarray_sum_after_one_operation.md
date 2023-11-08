---
title: 1746. maximum subarray sum after one operation
date: '2022-08-24'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1746 maximum subarray sum after one operation
---


You are given an integer array nums. You must perform exactly one operation where you can replace one element nums[i] with nums[i]  nums[i]. 



Return the maximum possible subarray sum after exactly one operation. The subarray must be non-empty.


 > Example 1:



 > Input: nums <TeX>=</TeX> [2,-1,-4,-3]

 > Output: 17

 > Explanation: You can perform the operation on index 2 (0-indexed) to make nums <TeX>=</TeX> [2,-1,16,-3]. Now, the maximum subarray sum is 2 + -1 + 16 <TeX>=</TeX> 17.

 > Example 2:



 > Input: nums <TeX>=</TeX> [1,-1,1,1,-1,-1,1]

 > Output: 4

 > Explanation: You can perform the operation on index 1 (0-indexed) to make nums <TeX>=</TeX> [1,1,1,1,-1,-1,1]. Now, the maximum subarray sum is 1 + 1 + 1 + 1 <TeX>=</TeX> 4.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 105

 > -104 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 104


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn max_sum_after_operation(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut res = i32::MIN;
        for i in 0..n {
            let mut max_val_index = i;
            let mut total = 0i32;
            for j in i..n {
                if nums[j].abs() > nums[max_val_index].abs() {
                    max_val_index = j;
                } else if nums[j].abs() == nums[max_val_index].abs() && nums[j] < 0 {
                    max_val_index = j;
                }
                total += nums[j];
                res = i32::max(res, total - nums[max_val_index] + nums[max_val_index] * nums[max_val_index]);
                //println!("i: {}, j: {}, total: {}, res: {}", i, j, total, res);
            }
        }
        res
    }
}
*/
impl Solution {
    /*
    https://leetcode.ca/2021-03-29-1746-Maximum-Subarray-Sum-After-One-Operation/
    Use dynamic programming. Let n be the length of nums. Create a 2D array dp of n rows and 3 columns, where

dp[i][0] represents the maximum subarray sum that ends at index i when no operation is performed,
dp[i][1] represents the maximum subarray sum that ends at index i when the one operation is performed at index i, and
dp[i][2] represents the maximum subarray sum that ends at index i when the one operation is performed before index i.
Initially, dp[0][0] = nums[0], dp[0][1] = nums[0] * nums[0] and dp[0][2] = Integer.MIN_VALUE, which means dp[0][2] is an impossible value.

Loop over i from 1 to n - 1. For each i, there is dp[i][0] = Math.max(dp[i - 1][0], 0) + nums[i], dp[i][1] = Math.max(dp[i - 1][0], 0) + nums[i] * nums[i] and dp[i][2] = Math.max(Math.max(dp[i - 1][1], dp[i - 1][2]), 0) + nums[i].

Finally, return the maximum value in the last two columns of dp.
    */
    pub fn max_sum_after_operation(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp: Vec<(i32, i32, i32)> = vec![(0, 0, 0); n];
        dp[0] = (nums[0], nums[0] * nums[0], i32::MIN);
        for i in 1..n {
            dp[i] = (
                i32::max(dp[i - 1].0, 0) + nums[i],
                i32::max(dp[i - 1].0, 0) + nums[i] * nums[i],
                i32::max(i32::max(dp[i - 1].1, dp[i - 1].2), 0) + nums[i]
            );
        }
        let v1 = dp.iter().map(|&v| v.1).max().unwrap();
        let v2 = dp.iter().map(|&v| v.2).max().unwrap();
        i32::max(v1, v2)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1746() {
        assert_eq!(Solution::max_sum_after_operation(vec![2,-1,-4,-3]), 17);
        assert_eq!(Solution::max_sum_after_operation(vec![1,-1,1,1,-1,-1,1]), 4);
    }
}

```
