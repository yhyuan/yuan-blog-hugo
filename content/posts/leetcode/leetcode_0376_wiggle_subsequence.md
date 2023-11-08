---
title: 376. wiggle subsequence
date: '2022-02-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0376 wiggle subsequence
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={376}/>
 

  A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

  

  	For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.

  	In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.

  

  A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

  Given an integer array nums, return the length of the longest wiggle subsequence of nums.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,7,4,9,2,5]

 >   Output: 6

 >   Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,17,5,10,13,15,10,5,16,8]

 >   Output: 7

 >   Explanation: There are several subsequences that achieve this length.

 >   One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [1,2,3,4,5,6,7,8,9]

 >   Output: 2

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 1000

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000

  

   

 >   Follow up: Could you solve this in O(n) time?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::cmp::Ordering::*;
impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut up: Vec<usize> = vec![1];
        let mut down: Vec<usize> = vec![1];
        for i in 1..n {
            match nums[i].cmp(&nums[i - 1]) {
                Greater => {
                    down.push(up[i - 1] + 1);
                    up.push(up[i - 1]);
                }
                Less => {
                    down.push(down[i - 1]);
                    up.push(down[i - 1] + 1);
                }
                Equal => {
                    down.push(down[i - 1]);
                    up.push(up[i - 1]);
                }
            }
        }
        up.into_iter().chain(down.into_iter()).max().unwrap() as i32    
    }
}
*/
impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp: Vec<(i32, i32)> = vec![(0, 0); n];
        dp[0] = (1, 1);
        if n == 1 {
            return 1;
        }
        dp[1] = if nums[0] == nums[1] {
            (0, 0)
        } else if nums[0] < nums[1] {
            (2, 1)
        } else {
            (1, 2)
        };
        for i in 2..n {
            let mut pos = i32::MIN;
            let mut neg = i32::MIN;
            for j in 0..i {
                if nums[i] > nums[j] {
                    pos = i32::max(pos, dp[j].1 + 1);
                } else if nums[i] < nums[j] {
                    neg = i32::max(neg, dp[j].0 + 1);
                } else {
                    
                }
            }
            dp[i] = (pos, neg);
        }
        let v0 = dp.iter().map(|&v| v.0).max().unwrap();
        let v1 = dp.iter().map(|&v| v.1).max().unwrap();
        i32::max(v0, v1)
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_376() {
        assert_eq!(Solution::wiggle_max_length(vec![1,17,5,10,13,15,10,5,16,8]), 7);
        assert_eq!(Solution::wiggle_max_length(vec![1,7,4,9,2,5]), 6);
        assert_eq!(Solution::wiggle_max_length(vec![1,2,3,4,5,6,7,8,9]), 2);
        assert_eq!(Solution::wiggle_max_length(vec![0, 0]), 1);
        assert_eq!(Solution::wiggle_max_length(vec![0, 0, 0]), 1);
        assert_eq!(Solution::wiggle_max_length(vec![51,226,208,165,202,286,190,212,219,271,36,245,20,238,238,89,105,66,73,9,254,206,221,237,203,33,249,253,150,102,57,249,203,10,123,178,85,203,35,276,129,116,37,163,99,142,187,249,134,77,217,298,29,127,174,115,122,178,12,80,122,76,16,41,115,84,104,121,127,40,287,129,9,172,112,51,40,135,205,53,259,196,248,5,123,184,209,130,271,42,18,143,24,101,10,273,252,50,173,80,119,129,45,257,299,78,278,78,190,215,284,129,200,232,103,97,167,120,49,298,141,146,154,233,214,196,244,50,110,48,152,82,226,26,254,276,292,286,215,56,128,122,82,241,222,12,272,192,224,136,116,70,39,207,295,49,194,90,210,123,271,18,276,87,177,240,276,33,155,200,51,6,212,36,149,202,48,114,58,91,83,221,175,148,278,300,284,86,191,95,77,215,113,257,153,135,217,76,85,269,126,194,199,195,20,204,194,50,220,228,90,221,256,87,157,246,74,156,9,196,16,259,234,79,31,206,148,12,223,151,96,229,165,9,144,26,255,201,33,89,145,155,1,204,37,107,80,212,88,186,254,9,158,180,24,45,158,100,52,131,71,174,229,236,296,299,184,168,41,45,76,68,122,85,292,238,293,179,143,128,47,87,267,53,187,76,292,0,160,70,172,292,9,64,156,153,26,145,196,222]), 202);
        assert_eq!(Solution::wiggle_max_length(vec![3,3,3,2,5]), 3);
    }
}


//}

```
