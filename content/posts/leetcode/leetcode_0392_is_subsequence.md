---
title: 392. is subsequence
date: '2022-02-16'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0392 is subsequence
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={392}/>
 

  Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

  A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "<u>a</u>b<u>c</u>d<u>e</u>" while "aec" is not).

   

 >   Example 1:

 >   Input: s <TeX>=</TeX> "abc", t <TeX>=</TeX> "ahbgdc"

 >   Output: true

 >   Example 2:

 >   Input: s <TeX>=</TeX> "axc", t <TeX>=</TeX> "ahbgdc"

 >   Output: false

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 100

 >   	0 <TeX>\leq</TeX> t.length <TeX>\leq</TeX> 10^4

 >   	s and t consist only of lowercase English letters.

  

   

 >   Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k ><TeX>=</TeX> 10^9, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        if s.len() == 0 {
            return true;
        }
        let s_chars: Vec<char> = s.chars().collect();
        let t_chars: Vec<char> = t.chars().collect();
        let mut i = 0;
        for ch in t_chars {
            if ch == s_chars[i] {
                i = i + 1;
                if i == s_chars.len() {
                    break;
                }
            }
        }
        i == s_chars.len()
    }
}
*/
impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let s_chars: Vec<char> = s.chars().collect::<Vec<_>>();
        let t_chars: Vec<char> = t.chars().collect::<Vec<_>>();
        let mut i = 0;
        let mut j = 0;
        while i < s_chars.len() {
            println!("i: {}, j: {}", i, j);
            let ch = s_chars[i];
            let index = (j..t_chars.len()).into_iter().find(|&k| t_chars[k] == ch);
            if index.is_none() {
                break;
            }
            let index = index.unwrap();
            println!("i: {}, j: {}, index: {}", i, j, index);
            j = index + 1;
            i += 1;
        }
        println!("i: {}", i);
        if i < s.len() {
            return false;
        }
        true
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_392() {
        assert_eq!(Solution::is_subsequence("aaaaaa".to_string(), "bbaaaa".to_string()), false);
        assert_eq!(Solution::is_subsequence("abc".to_string(), "ahbgdc".to_string()), true);
        assert_eq!(Solution::is_subsequence("axc".to_string(), "ahbgdc".to_string()), false);
    }
}
```
