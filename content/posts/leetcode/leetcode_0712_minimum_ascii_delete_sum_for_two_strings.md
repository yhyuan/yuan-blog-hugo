---
title: 712. minimum ascii delete sum for two strings
date: '2022-04-27'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0712 minimum ascii delete sum for two strings
---

 

  Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

   

 >   Example 1:

  

 >   Input: s1 <TeX>=</TeX> "sea", s2 <TeX>=</TeX> "eat"

 >   Output: 231

 >   Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.

 >   Deleting "t" from "eat" adds 116 to the sum.

 >   At the end, both strings are equal, and 115 + 116 <TeX>=</TeX> 231 is the minimum sum possible to achieve this.

  

 >   Example 2:

  

 >   Input: s1 <TeX>=</TeX> "delete", s2 <TeX>=</TeX> "leet"

 >   Output: 403

 >   Explanation: Deleting "dee" from "delete" to turn the string into "let",

 >   adds 100[d] + 101[e] + 101[e] to the sum.

 >   Deleting "e" from "leet" adds 101[e] to the sum.

 >   At the end, both strings are equal to "let", and the answer is 100+101+101+101 <TeX>=</TeX> 403.

 >   If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s1.length, s2.length <TeX>\leq</TeX> 1000

 >   	s1 and s2 consist of lowercase English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let m = s1.len();
        let n = s2.len();
        let chars1 = s1.chars().collect::<Vec<_>>();
        let chars2 = s2.chars().collect::<Vec<_>>();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n + 1]; m + 1];
        for i in (0..m).rev() {
            dp[i][n] = dp[i + 1][n] + chars1[i] as i32;
        }
        for j in (0..n).rev() {
            dp[m][j] = dp[m][j + 1] + chars2[j] as i32;
        }
        for i in (0..m).rev() {
            for j in (0..n).rev() {
                dp[i][j] = if chars1[i] == chars2[j] {
                    dp[i + 1][j + 1]
                } else {
                    i32::min(dp[i + 1][j] + chars1[i] as i32, dp[i][j + 1] + chars2[j] as i32)
                };
            }
        }
        //println!("dp: {:?}", dp);
        dp[0][0]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_712() {
        assert_eq!(Solution::minimum_delete_sum("sea".to_string(), "eat".to_string()), 231);
        assert_eq!(Solution::minimum_delete_sum("delete".to_string(), "leet".to_string()), 403);
    }
}

```
