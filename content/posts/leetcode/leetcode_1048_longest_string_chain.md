---
title: 1048. longest string chain
date: '2022-07-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1048 longest string chain
---

 

  You are given an array of words where each word consists of lowercase English letters.

  wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

  

  	For example, "abc" is a predecessor of "ab<u>a</u>c", while "cba" is not a predecessor of "bcad".

  

  A word chain is a sequence of words [word1, word2, ..., wordk] with k ><TeX>=</TeX> 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k <TeX>=</TeX><TeX>=</TeX> 1.

  Return the length of the longest possible word chain with words chosen from the given list of words.

   

 >   Example 1:

  

 >   Input: words <TeX>=</TeX> ["a","b","ba","bca","bda","bdca"]

 >   Output: 4

 >   Explanation: One of the longest word chains is ["a","<u>b</u>a","b<u>d</u>a","bd<u>c</u>a"].

  

 >   Example 2:

  

 >   Input: words <TeX>=</TeX> ["xbc","pcxbcf","xb","cxbc","pcxbc"]

 >   Output: 5

 >   Explanation: All the words can be put in a word chain ["xb", "xb<u>c</u>", "<u>c</u>xbc", "<u>p</u>cxbc", "pcxbc<u>f</u>"].

  

 >   Example 3:

  

 >   Input: words <TeX>=</TeX> ["abcd","dbqca"]

 >   Output: 1

 >   Explanation: The trivial word chain ["abcd"] is one of the longest word chains.

 >   ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> words.length <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> words[i].length <TeX>\leq</TeX> 16

 >   	words[i] only consists of lowercase English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn helper(memo: &mut HashMap<String, i32>, word: &String) -> i32 {
        if memo.contains_key(word) && memo[word] > 0 {
            return memo[word];
        }
        if word.len() == 1 {
            memo.insert(word.clone(), 1);
            return 1i32;
        }
        // let chars: Vec<char> = word.chars().collect();
        //let n = chars.len();
        let mut res = 1;
        for i in 0..word.len() {
            let next_word = format!("{}{}", &word[..i], &word[i + 1..]);
            // let next_word = (0..n).into_iter().filter(|&k| k != i).map(|k| chars[k]).collect::<String>();
            if memo.contains_key(&next_word) {
                let val = Self::helper(memo, &next_word) + 1;
                res = i32::max(val, res);
            }
        }
        memo.insert(word.clone(), res);
        res
    }
    pub fn longest_str_chain(words: Vec<String>) -> i32 {
        let mut memo: HashMap<String, i32> = HashMap::new();
        let n = words.len();
        for i in 0..n {
            memo.insert(words[i].clone(), -1);
        }
        let mut res = i32::MIN;
        for word in words.iter() {
            res = i32::max(res, Self::helper(&mut memo, word));
        }
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1048() {
        assert_eq!(Solution::longest_str_chain(vec_string!["a","b","ba","bca","bda","bdca"]), 4);
        assert_eq!(Solution::longest_str_chain(vec_string!["xbc","pcxbcf","xb","cxbc","pcxbc"]), 5);
    }
}

```
