---
title: 209. minimum size subarray sum
date: '2021-10-26'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0209 minimum size subarray sum
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={209}/>
 

  Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

   

 >   Example 1:

  

 >   Input: target <TeX>=</TeX> 7, nums <TeX>=</TeX> [2,3,1,2,4,3]

 >   Output: 2

 >   Explanation: The subarray [4,3] has the minimal length under the problem constraint.

  

 >   Example 2:

  

 >   Input: target <TeX>=</TeX> 4, nums <TeX>=</TeX> [1,4,4]

 >   Output: 1

  

 >   Example 3:

  

 >   Input: target <TeX>=</TeX> 11, nums <TeX>=</TeX> [1,1,1,1,1,1,1,1]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> target <TeX>\leq</TeX> 10^9

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5

 >   	1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^5

  

   

 >   Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        if nums.len() == 0 {
            return 0;
        }
        for &num in nums.iter() {
            if num > target {
                return 1;
            }
        }
        let total: i32 = nums.iter().sum();
        if total < target {
            return 0;
        }
        let mut i = 0usize;
        let mut j = 0usize;
        let mut min_len = i32::MAX;
        let mut sum = nums[0];
        loop {
            // Move j unitl the total is larger or equal to target. 
            while sum < target {
                j = j + 1;
                if j > nums.len() - 1 {
                    return min_len;
                }
                sum += nums[j];
            }
            // Move i until the total is less than the target. 
            // Now i-1, j is the right which is the smallest possible to be larger or equal to the target. 
            while sum >= target {
                sum -= nums[i];
                i += 1;
            }
            // the size is j - (i - 1) + 1 = j + 2 - i
            min_len = i32::min(min_len, (j + 2 - i) as i32);
        }
    }
}
*/
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut res = i32::MAX;
        for i in 0..n {
            let mut sum = 0;
            for j in i..n {
                sum += nums[j];
                if sum >= target {
                    res = i32::min(res, (j - i + 1) as i32);
                    break;
                }
            }
        }
        if res == i32::MAX {0} else {res}
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_209() {
        assert_eq!(Solution::min_sub_array_len(7, vec![2,3,1,2,4,3]), 2);
        assert_eq!(Solution::min_sub_array_len(4, vec![1, 4, 4]), 1);
        assert_eq!(Solution::min_sub_array_len(11, vec![1,1,1,1,1,1,1,1]), 0);
    }
}

```
