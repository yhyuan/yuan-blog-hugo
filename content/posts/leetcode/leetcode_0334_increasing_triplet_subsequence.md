---
title: 334. increasing triplet subsequence
date: '2022-01-12'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0334 increasing triplet subsequence
---

 

  Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,2,3,4,5]

 >   Output: true

 >   Explanation: Any triplet where i < j < k is valid.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [5,4,3,2,1]

 >   Output: false

 >   Explanation: No triplet exists.

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [2,1,5,0,4,6]

 >   Output: true

 >   Explanation: The triplet (3, 4, 5) is valid because nums[3] <TeX>=</TeX><TeX>=</TeX> 0 < nums[4] <TeX>=</TeX><TeX>=</TeX> 4 < nums[5] <TeX>=</TeX><TeX>=</TeX> 6.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 5  10^5

 >   	-2^31 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1

  

   

 >   Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut first_num = i32::MAX;
        let mut second_num = i32::MAX;
        for i in 0..n {
            if nums[i] <= first_num {
                first_num = nums[i];
            } else if nums[i] <= second_num {
                second_num = nums[i];
            } else {
                return true;
            }
        }
        false
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_334() {
        assert_eq!(Solution::increasing_triplet(vec![20,100,10,12,5,13]), true);
        assert_eq!(Solution::increasing_triplet(vec![1,2,3,4,5]), true);
        assert_eq!(Solution::increasing_triplet(vec![5,4,3,2,1]), false);
        assert_eq!(Solution::increasing_triplet(vec![2,1,5,0,4,6]), true);
    }
}

```
