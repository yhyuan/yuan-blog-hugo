---
title: 131. palindrome partitioning
date: '2021-09-07'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0131 palindrome partitioning
---

 

  Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

  A palindrome string is a string that reads the same backward as forward.

   

 >   Example 1:

 >   Input: s <TeX>=</TeX> "aab"

 >   Output: [["a","a","b"],["aa","b"]]

 >   Example 2:

 >   Input: s <TeX>=</TeX> "a"

 >   Output: [["a"]]

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 16

 >   	s contains only lowercase English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_palindrome(chars: &Vec<char>, start: usize, end: usize) -> bool {
        for i in 0..(end - start + 1) / 2 {
            if chars[start + i] != chars[end - i] {
                return false;
            }
        }
        return true;
    }

    pub fn partition(s: String) -> Vec<Vec<String>> {
        if s.len() == 0 {
            return vec![];
        }
        if s.len() == 1 {
            return vec![vec![s]];
        }
        let chars: Vec<char> = s.chars().collect();
        let mut results: Vec<Vec<String>> = vec![];
        for i in 0..s.len() {
            if Solution::is_palindrome(&chars, 0, i) {
                //let string = s[..=i].to_string();
                //println!("test: {}", s[..=i].to_string());
                if i == s.len() - 1 {
                    results.push(vec![s[..].to_string()]);
                } else {
                    let mut pre_results = Solution::partition(s[i+1..].to_string());
                    //pre_results.iter().map(|vec| ).collect();
                    for result in pre_results.iter_mut() {
                        result.insert(0, s[..=i].to_string());
                    }
                    for result in pre_results {
                        results.push(result);
                    }    
                }
            }
        }
        results
        //vec![]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_131() {
        assert_eq!(
            Solution::partition("aab".to_owned()),
            vec![vec_string!["a", "a", "b"],vec_string!["aa", "b"], ]
        );
        assert_eq!(
            Solution::partition("aaa".to_owned()),
            vec![
                vec_string!["a", "a", "a"],
                vec_string!["a", "aa"],
                vec_string!["aa", "a"],
                vec_string!["aaa"],
            ]
        );
    }
}

```
