---
title: 704. binary search
date: '2022-04-24'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0704 binary search
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={704}/>
 

  Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

  You must write an algorithm with O(log n) runtime complexity.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [-1,0,3,5,9,12], target <TeX>=</TeX> 9

 >   Output: 4

 >   Explanation: 9 exists in nums and its index is 4

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [-1,0,3,5,9,12], target <TeX>=</TeX> 2

 >   Output: -1

 >   Explanation: 2 does not exist in nums so return -1

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^4

 >   	-10^4 < nums[i], target < 10^4

 >   	All the integers in nums are unique.

 >   	nums is sorted in ascending order.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        if nums.len() == 1 {
            if nums[0] == target {
                return 0;
            }
            return -1;
        }
        let mut low = 0;
        let mut high = nums.len() - 1;
        while low + 1 < high {
            let mid = low + (high - low) / 2;
            if nums[mid] == target {
                return mid as i32;
            } else if nums[mid] > target {
                high = mid;
            } else {
                low = mid;
            }
        }
        if nums[low] == target {
            return low as i32;
        }
        if nums[low + 1] == target {
            return low as i32 + 1;
        }
        -1
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_704() {
    }
}

```
