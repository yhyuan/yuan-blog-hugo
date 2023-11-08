---
title: 368. largest divisible subset
date: '2022-01-29'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0368 largest divisible subset
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={368}/>
 

  Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

  

  	answer[i] % answer[j] <TeX>=</TeX><TeX>=</TeX> 0, or

  	answer[j] % answer[i] <TeX>=</TeX><TeX>=</TeX> 0

  

  If there are multiple solutions, return any of them.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,2,3]

 >   Output: [1,2]

 >   Explanation: [1,3] is also accepted.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,2,4,8]

 >   Output: [1,2,4,8]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2  10^9

 >   	All the integers in nums are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn largest_divisible_subset(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let mut dp: Vec<Vec<i32>> = vec![vec![]; n];
        dp[0] = vec![nums[0]];
        let mut max_len = 1;
        let mut res = dp[0].clone();
        for i in 1..n {
            for j in (0..i).rev() {
                if nums[i] % nums[j] == 0 && dp[j].len() > dp[i].len() {
                    dp[i] = dp[j].clone();
                    // break;
                }
            }
            dp[i].push(nums[i]);
            if dp[i].len() > max_len {
                max_len = dp[i].len();
                res = dp[i].clone();
            }
        }
        // println!("dp: {:?}", dp);
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_368() {
        assert_eq!(Solution::largest_divisible_subset(vec![4, 8, 10, 240]), vec![4, 8, 240]);
        assert_eq!(Solution::largest_divisible_subset(vec![1, 2, 3]), vec![1, 2]);
        assert_eq!(Solution::largest_divisible_subset(vec![1, 2, 4, 8]), vec![1, 2, 4, 8]);
    }
}

```
