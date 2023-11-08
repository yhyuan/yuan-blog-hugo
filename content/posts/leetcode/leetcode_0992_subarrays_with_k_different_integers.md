---
title: 992. subarrays with k different integers
date: '2022-06-24'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0992 subarrays with k different integers
---

 

  Given an integer array nums and an integer k, return the number of good subarrays of nums.

  A good array is an array where the number of different integers in that array is exactly k.

  

  	For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

  

  A subarray is a contiguous part of an array.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,2,1,2,3], k <TeX>=</TeX> 2

 >   Output: 7

 >   Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,2,1,3,4], k <TeX>=</TeX> 3

 >   Output: 3

 >   Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 2  10^4

 >   	1 <TeX>\leq</TeX> nums[i], k <TeX>\leq</TeX> nums.length


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    //Sliding Window
    //The idea is to calculate the number of subarrays with at most K distinct characters and with at most K - 1 distinct characters and then do subtraction.
    pub fn subarrays_with_at_most_k_distinct(nums: &Vec<i32>, k: usize) -> i32 {
        let n = nums.len();
        let mut i = 0usize;
        let mut j = 0usize;
        let mut ans = 0i32;
        let mut memo: HashMap<i32, usize> = HashMap::new();
        *memo.entry(nums[0]).or_insert(0) += 1;
        while j < n {
            if memo.keys().len() <= k { 
                ans += (j - i + 1) as i32; // subarrays ends at j
                j += 1;
                if j < n {
                    *memo.entry(nums[j]).or_insert(0) += 1;                    
                }
            } else {
                *memo.entry(nums[i]).or_insert(0) -= 1;
                let val = *memo.get(&nums[i]).unwrap();
                if val == 0 {
                    memo.remove(&nums[i]);
                }
                i += 1;
            }
        }
        ans
    }
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        Self::subarrays_with_at_most_k_distinct(&nums, k as usize) - Self::subarrays_with_at_most_k_distinct(&nums, k as usize - 1)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_992() {
        assert_eq!(Solution::subarrays_with_k_distinct(vec![1,2,1,2,3], 2), 7);
        assert_eq!(Solution::subarrays_with_k_distinct(vec![1,2,1,3,4], 3), 3);
    }
}

```
