---
title: 139. word break
date: '2021-09-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0139 word break
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={139}/>
 

  Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

  Note that the same word in the dictionary may be reused multiple times in the segmentation.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "leetcode", wordDict <TeX>=</TeX> ["leet","code"]

 >   Output: true

 >   Explanation: Return true because "leetcode" can be segmented as "leet code".

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "applepenapple", wordDict <TeX>=</TeX> ["apple","pen"]

 >   Output: true

 >   Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".

 >   Note that you are allowed to reuse a dictionary word.

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "catsandog", wordDict <TeX>=</TeX> ["cats","dog","sand","and","cat"]

 >   Output: false

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 300

 >   	1 <TeX>\leq</TeX> wordDict.length <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> wordDict[i].length <TeX>\leq</TeX> 20

 >   	s and wordDict[i] consist of only lowercase English letters.

 >   	All the strings of wordDict are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashMap;
impl Solution {
    pub fn word_break_helper(s: &String, start: usize, memo: &mut HashMap<usize, bool>, word_dict: &HashMap<String, bool>, min_word_len: usize, max_word_len: usize) -> bool {
        if s.len() == start {
            return true;
        }
        if memo.contains_key(&start) {
            return memo[&start];
        }
        for i in min_word_len..=max_word_len {
            let next_word = if start + i <= s.len() {(&s[start..start + i]).to_string()} else {(&s[start..s.len()]).to_string()};
            if word_dict.contains_key(&next_word) {
                let res = Solution::word_break_helper(s, start + i, memo, word_dict, min_word_len, max_word_len);
                if res {
                    memo.insert(start, true);
                    return true;
                }
            }
        }
        memo.insert(start, false);
        false
    }
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let mut word_dict_hashmap: HashMap<String, bool> = HashMap::with_capacity(word_dict.len());
        let mut min_word_len = usize::MAX;
        let mut max_word_len = usize::MIN;
        for word in word_dict {
            let len = word.len();
            word_dict_hashmap.insert(word, true);
            max_word_len = usize::max(max_word_len, len);
            min_word_len = usize::min(min_word_len, len);
        }
        let mut memo: HashMap<usize, bool> = HashMap::new();
        Solution::word_break_helper(&s, 0, &mut memo, &word_dict_hashmap, min_word_len, max_word_len)
    }
}
*/
/*
use std::collections::{HashSet, HashMap};
impl Solution {
    pub fn word_break_helper(s: &String, index: usize, word_set: &HashSet<String>, memo: &mut HashMap<usize, bool>, min_len: usize, max_len: usize) -> bool {
        let n = s.len();
        if index == n {
            return true;
        }
        if memo.contains_key(&index) {
            return *memo.get(&index).unwrap();
        }
        for len in min_len..=max_len {
            if index + len <= n {
                if word_set.contains(&s[index..index + len]) {
                    if Self::word_break_helper(s, index + len, word_set, memo, min_len, max_len) {
                        memo.insert(index, true);
                        return true;
                    }
                }
            }
        }
        memo.insert(index, false);
        false
    }
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        
        //let s_chars = s.chars().collect::<HashSet<char>>();
        //let word_chars = word_dict.iter()
        //    .map(|s| s.chars().collect::<HashSet<char>>())
        //    .reduce(|accum, item| {
       //         let mut accum = accum;
        //        accum.extend(&item);
//                accum
//            }).unwrap();
//        let diff = s_chars.difference(&word_chars).collect::<HashSet<_>>();
//        if diff.len() > 0 {
//            return false;
       // }
        
        let max_len = word_dict.iter().map(|s| s.len()).max().unwrap();
        let min_len = word_dict.iter().map(|s| s.len()).min().unwrap();
        let word_set = word_dict.into_iter().collect::<HashSet<_>>();
        let mut memo: HashMap<usize, bool> = HashMap::new();
        Self::word_break_helper(&s, 0, &word_set, &mut memo, min_len, max_len)
    }
}
*/
use std::collections::HashSet;
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let word_set: HashSet<String> = word_dict.into_iter().collect();
        let n = s.len();
        //dp[n] substring ends with n - 1 can be broken to words. 
        //It is true only if dp[j] is ture and s[j..i] is in word_dict.  
        let mut dp: Vec<bool> = vec![false; n + 1];
        dp[0] = true;
        for i in 1..=n {
            for j in 0..i {
                if dp[j] && word_set.contains(&s[j..i]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        dp[n]
    }
}
/* 
use std::collections::HashSet;
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        // dp[i] is s[i..n]
        let n = s.len();
        let max_len = word_dict.iter().map(|s| s.len()).max().unwrap();
        let min_len = word_dict.iter().map(|s| s.len()).min().unwrap();
        let word_set = word_dict.into_iter().collect::<HashSet<_>>();
        let mut dp = vec![false; n];
        for len in min_len..=max_len {
            let mut result = false;
            dp[n - len] = word_set.contains(&s[n - len..]);
        }
        for i in (0..n - max_len).rev() {
            let mut result = false;
            for len in min_len..=max_len {
                if dp[i + len] && word_set.contains(&s[i..i + len])  {
                    result = true;
                    break;
                }
            }
            dp[i] = result;
        }
        dp[0]
    }
}
*/
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_139() {
        assert_eq!(
            Solution::word_break("bb".to_owned(), vec_string!["a", "b", "bbb", "bbbb"]),
            true
        );
        assert_eq!(
            Solution::word_break("applepenapple".to_owned(), vec_string!["apple", "pen"]),
            true
        );
        assert_eq!(
            Solution::word_break("leetcode".to_owned(), vec_string!["leet", "code"]),
            true
        );
        assert_eq!(
            Solution::word_break(
                "catsandog".to_owned(),
                vec_string!["cats", "dog", "sand", "and", "cat"]
            ),
            false
        );
    }
}

```
