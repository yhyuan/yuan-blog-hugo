---
title: 213. house robber ii
date: '2021-10-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0213 house robber ii
---

 

  You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

  Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [2,3,2]

 >   Output: 3

 >   Explanation: You cannot rob house 1 (money <TeX>=</TeX> 2) and then rob house 3 (money <TeX>=</TeX> 2), because they are adjacent houses.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,2,3,1]

 >   Output: 4

 >   Explanation: Rob house 1 (money <TeX>=</TeX> 1) and then rob house 3 (money <TeX>=</TeX> 3).

 >   Total amount you can rob <TeX>=</TeX> 1 + 3 <TeX>=</TeX> 4.

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [1,2,3]

 >   Output: 3

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 100

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn rob_helper(nums: &Vec<i32>, start: usize, end: usize) -> i32 {
        let mut results: Vec<i32> = vec![0; end  + 1 - start];
        results[0] = nums[start];
        if results.len() == 1 {
            return results[0];
        }
        results[1] = i32::max(nums[start], nums[start + 1]);

        for i in 2..results.len() {
            results[i] = i32::max(results[i-1], results[i-2] + nums[start + i]);
        }
        results[results.len() - 1]
    }

    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() == 0 {
            return 0i32;
        }
        if nums.len() == 1 {
            return nums[0];
        }
        let v1 = Solution::rob_helper(&nums, 1 as usize, nums.len() - 1);
        let v2 = Solution::rob_helper(&nums, 0 as usize, nums.len() - 2);
        i32::max(v1, v2)
    }
}
*/
impl Solution {
    pub fn rob_helper(nums: &Vec<i32>, start: usize, end: usize) -> i32 {
        if start == end {
            return nums[start];
        }
        let mut dp = (nums[start], i32::max(nums[start], nums[start + 1]));
         for i in 2..end - start + 1 {
             dp = (dp.1, i32::max(dp.1, dp.0 + nums[start + i]));
         }
         dp.1
     }
     pub fn rob(nums: Vec<i32>) -> i32 {
         if nums.len() == 0 {
             return 0i32;
         }
         if nums.len() == 1 {
             return nums[0];
         }
         let v1 = Solution::rob_helper(&nums, 1 as usize, nums.len() - 1);
         let v2 = Solution::rob_helper(&nums, 0 as usize, nums.len() - 2);
         i32::max(v1, v2)
     }
 }

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_213() {
        assert_eq!(Solution::rob(vec![2, 3, 2]), 3);
        assert_eq!(Solution::rob(vec![1, 2, 3, 1]), 4);
    }
}

```
