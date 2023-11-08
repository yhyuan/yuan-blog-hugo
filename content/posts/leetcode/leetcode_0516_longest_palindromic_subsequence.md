---
title: 516. longest palindromic subsequence
date: '2022-03-24'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0516 longest palindromic subsequence
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={516}/>
 

  Given a string s, find the longest palindromic subsequence's length in s.

  A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "bbbab"

 >   Output: 4

 >   Explanation: One possible longest palindromic subsequence is "bbbb".

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "cbbd"

 >   Output: 2

 >   Explanation: One possible longest palindromic subsequence is "bb".

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 1000

 >   	s consists only of lowercase English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let n = s.len();
        let chars = s.chars().collect::<Vec<_>>();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; n];
        for i in 0..n {
            dp[i][i] = 1;
        }
        for i in 0..n - 1 {
            dp[i][i + 1] = if chars[i] == chars[i + 1] {2} else {1};
        }
        for k in 3..=n {
            for i in 0..n - k + 1 {
                dp[i][i + k - 1] = if chars[i] == chars[i + k - 1] {
                    dp[i + 1][i + k - 1 - 1] + 2
                } else {
                    i32::max(dp[i + 1][i + k - 1], dp[i][i + k - 1 - 1])
                };    
            }
        }
        //println!("dp: {:?}", dp);
        dp[0][n - 1]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_516() {
        assert_eq!(Solution::longest_palindrome_subseq("bbbab".to_string()), 4);
        assert_eq!(Solution::longest_palindrome_subseq("cbbd".to_string()), 2);
    }
}

```
