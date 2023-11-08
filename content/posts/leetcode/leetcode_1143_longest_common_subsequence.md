---
title: 1143. longest common subsequence
date: '2022-07-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1143 longest common subsequence
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1143}/>
 

  Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

  A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

  

  	For example, "ace" is a subsequence of "abcde".

  

  A common subsequence of two strings is a subsequence that is common to both strings.

   

 >   Example 1:

  

 >   Input: text1 <TeX>=</TeX> "abcde", text2 <TeX>=</TeX> "ace" 

 >   Output: 3  

 >   Explanation: The longest common subsequence is "ace" and its length is 3.

  

 >   Example 2:

  

 >   Input: text1 <TeX>=</TeX> "abc", text2 <TeX>=</TeX> "abc"

 >   Output: 3

 >   Explanation: The longest common subsequence is "abc" and its length is 3.

  

 >   Example 3:

  

 >   Input: text1 <TeX>=</TeX> "abc", text2 <TeX>=</TeX> "def"

 >   Output: 0

 >   Explanation: There is no such common subsequence, so the result is 0.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> text1.length, text2.length <TeX>\leq</TeX> 1000

 >   	text1 and text2 consist of only lowercase English characters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/* 
impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let chars1: Vec<char> = text1.chars().collect();
        let chars2: Vec<char> = text2.chars().collect();
        let m = chars1.len();
        let n = chars2.len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0i32; n + 1]; m + 1];
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                if chars1[i] == chars2[j] {
                    dp[i][j] = dp[i + 1][j + 1] + 1;
                } else {
                    dp[i][j] = i32::max(dp[i][j + 1], dp[i + 1][j]);
                }
            }
        }
        dp[0][0]
    }
}
*/
impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let m = text1.len();
        let n = text2.len();
        let chars1 = text1.chars().collect::<Vec<_>>();
        let chars2 = text2.chars().collect::<Vec<_>>();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        /* 
        dp[0][0] = if chars1[0] == chars2[0] {1} else {0};
        for j in 1..n {
            dp[0][j] = dp[0][0];
        }
        for i in 1..m {
            dp[i][0] = dp[0][0];
        }
        */
        let mut res = 0;
        for i in 0..m {
            for j in 0..n {
                if i == 0 || j == 0 {
                    dp[i][j] = if chars1[i] == chars2[j] {1} else {0};
                } else {
                    dp[i][j] = if chars1[i] == chars2[j] {
                        dp[i - 1][j - 1] + 1
                    } else {
                        i32::max(dp[i - 1][j], dp[i][j - 1])
                    };    
                }
                res = i32::max(res, dp[i][j]);
            }
        }
        println!("dp: {:?}", dp);
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1143() {
        assert_eq!(Solution::longest_common_subsequence("bl".to_string(), "yby".to_string()), 1);
        
        assert_eq!(Solution::longest_common_subsequence("abcde".to_string(), "ace".to_string()), 3);
        /*assert_eq!(Solution::longest_common_subsequence("abc".to_string(), "abc".to_string()), 3);
        assert_eq!(Solution::longest_common_subsequence("abc".to_string(), "def".to_string()), 0);
        */
    }
}

```
