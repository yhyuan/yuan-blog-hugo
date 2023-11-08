---
title: 164. maximum gap
date: '2021-09-29'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0164 maximum gap
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={164}/>
 

  Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

  You must write an algorithm that runs in linear time and uses linear extra space.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [3,6,9,1]

 >   Output: 3

 >   Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [10]

 >   Output: 0

 >   Explanation: The array contains less than 2 elements, therefore return 0.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn maximum_gap(nums: Vec<i32>) -> i32 {
        if nums.len() < 2 {
            return 0i32;
        }
        let mut nums = nums;
        nums.sort();
        let mut gap = i32::MIN;
        for i in 1..nums.len() {
            let diff = nums[i] - nums[i - 1];
            if gap <  diff {
                gap = diff;
            }
        }
        gap
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_164() {
        assert_eq!(3, Solution::maximum_gap(vec![3, 6, 9, 1]));
    }
}

```
