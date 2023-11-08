---
title: 140. word break ii
date: '2021-09-14'
tags: ['leetcode', 'rust', 'python', 'hard']
draft: false
description: Solution for leetcode 0140 word break ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={140}/>
 

  Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

  Note that the same word in the dictionary may be reused multiple times in the segmentation.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "catsanddog", wordDict <TeX>=</TeX> ["cat","cats","and","sand","dog"]

 >   Output: ["cats and dog","cat sand dog"]

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "pineapplepenapple", wordDict <TeX>=</TeX> ["apple","pen","applepen","pine","pineapple"]

 >   Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

 >   Explanation: Note that you are allowed to reuse a dictionary word.

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "catsandog", wordDict <TeX>=</TeX> ["cats","dog","sand","and","cat"]

 >   Output: []

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 20

 >   	1 <TeX>\leq</TeX> wordDict.length <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> wordDict[i].length <TeX>\leq</TeX> 10

 >   	s and wordDict[i] consist of only lowercase English letters.

 >   	All the strings of wordDict are unique.


## Solution
### Python
```python
def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
  maxLen = max(list(map(lambda word: len(word), wordDict)))
  words = set(wordDict)
  n = len(s)
  def helper(index):
    if index >= n: 
      return [""]
    totalResults = []
    for size in range(1, maxLen + 1):
      if index + size > n:
        continue
      subString = s[index: index + size]
      if subString in words:
        results = helper(index + size)
        totalResults = totalResults + list(map(lambda result: subString + " " + result if len(result) > 0 else subString, results))
    return totalResults
        
  return helper(0)
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;

impl Solution {
    pub fn word_break_helper(s: &String, start: usize, words: &mut Vec<String>, word_dict: &HashMap<String, bool>, min_word_len: usize, max_word_len: usize) -> Vec<String> {
        if s.len() == start {
            let res = words.join(" ");
            return vec![res];
        }
        let end_index_lower_limit = start + min_word_len;
        let end_index_upper_limit = usize::min(start + max_word_len, s.len());
        let next_words: Vec<String> = (end_index_lower_limit..=end_index_upper_limit).into_iter()
        .map(|end_index|(&s[start..end_index]).to_string())
        .collect();
        let valid_next_words: Vec<String> = next_words.into_iter().filter(|word| word_dict.contains_key(word)).collect();
        let mut result: Vec<String> = vec![];
        for next_word in valid_next_words {
            let size = next_word.len();
            words.push(next_word);
            let res = Solution::word_break_helper(s, start + size, words, word_dict, min_word_len, max_word_len);
            for s in res {
                result.push(s);
            }
            words.pop();
        }
        result
    }
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        let mut word_dict_hashmap: HashMap<String, bool> = HashMap::with_capacity(word_dict.len());
        let mut min_word_len = usize::MAX;
        let mut max_word_len = usize::MIN;
        for word in word_dict {
            let len = word.len();
            word_dict_hashmap.insert(word, true);
            max_word_len = usize::max(max_word_len, len);
            min_word_len = usize::min(min_word_len, len);
        }
        let mut words: Vec<String> = vec![];
        Solution::word_break_helper(&s, 0, &mut words, &word_dict_hashmap, min_word_len, max_word_len)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_140() {
        assert_eq!(Solution::word_break("catsanddog".to_string(), 
            vec!["cat".to_string(),"cats".to_string(),"and".to_string(),"sand".to_string(),"dog".to_string()]), 
            vec!["cat sand dog".to_string(), "cats and dog".to_string()]);

        assert_eq!(Solution::word_break("pineapplepenapple".to_string(), 
            vec!["apple".to_string(),"pen".to_string(),"applepen".to_string(),"pine".to_string(),"pineapple".to_string()])
        , vec!["pine apple pen apple".to_string(),"pine applepen apple".to_string(),"pineapple pen apple".to_string()]);

        let empty: Vec<String> = vec![];
        assert_eq!(Solution::word_break(
            "catsandog".to_string(), 
            vec!["cats".to_string(),"dog".to_string(),"sand".to_string(),"and".to_string(),"cat".to_string()])
        , empty);
    }
}

```
