---
title: 2135. count words obtained after adding a letter
date: '2022-09-09'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2135 count words obtained after adding a letter
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2135}/>

You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.



For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.



The conversion operation is described in the following two steps:



Append any lowercase letter that is not present in the string to its end.

For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".

Rearrange the letters of the new string in any arbitrary order.

For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.

Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.



Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.



 



 > Example 1:



 > Input: startWords <TeX>=</TeX> ["ant","act","tack"], targetWords <TeX>=</TeX> ["tack","act","acti"]

 > Output: 2

 > Explanation:

 > - In order to form targetWords[0] <TeX>=</TeX> "tack", we use startWords[1] <TeX>=</TeX> "act", append 'k' to it, and rearrange "actk" to "tack".

 > - There is no string in startWords that can be used to obtain targetWords[1] <TeX>=</TeX> "act".

 >   Note that "act" does exist in startWords, but we must append one letter to the string before rearranging it.

 > - In order to form targetWords[2] <TeX>=</TeX> "acti", we use startWords[1] <TeX>=</TeX> "act", append 'i' to it, and rearrange "acti" to "acti" itself.

 > Example 2:



 > Input: startWords <TeX>=</TeX> ["ab","a"], targetWords <TeX>=</TeX> ["abc","abcd"]

 > Output: 1

 > Explanation:

 > - In order to form targetWords[0] <TeX>=</TeX> "abc", we use startWords[0] <TeX>=</TeX> "ab", add 'c' to it, and rearrange it to "abc".

 > - There is no string in startWords that can be used to obtain targetWords[1] <TeX>=</TeX> "abcd".

 



**Constraints:**



 > 1 <TeX>\leq</TeX> startWords.length, targetWords.length <TeX>\leq</TeX> 5  104

 > 1 <TeX>\leq</TeX> startWords[i].length, targetWords[j].length <TeX>\leq</TeX> 26

 > Each string of startWords and targetWords consists of lowercase English letters only.

 > No letter occurs more than once in any string of startWords or targetWords.


## Solution
### Rust
```rust
 pub struct Solution {}
 use std::collections::{HashMap, HashSet};
 impl Solution {
    /*
    pub fn count_freq(word: &String) -> [i32; 26] {
        let chars: Vec<char> = word.chars().collect();
        let mut res: [i32; 26] = [0; 26];
        for i in 0..chars.len() {
            res[chars[i] as usize - 'a' as usize] += 1;
        }
        res
    }
    pub fn compare_count(target_count: &[i32; 26], start_count: &[i32; 26]) -> bool {
        let mut diff = 0;
        for i in 0usize..26usize {
            if start_count[i] > target_count[i] {
                return false;
            }
            diff += target_count[i] - start_count[i];
            if diff >= 2 {
                return false;
            }
        }
        diff == 1
    }
    pub fn word_count(start_words: Vec<String>, target_words: Vec<String>) -> i32 {
        let start_count: Vec<[i32; 26]> = start_words.iter().map(|word| Self::count_freq(&word)).collect();
        let target_count: Vec<[i32; 26]> = target_words.iter().map(|word| Self::count_freq(&word)).collect();
        let mut res = 0;
        for i in 0..target_count.len() {
            let mut is_possible = false;
            for j in 0..start_count.len() {
                if Self::compare_count(&target_count[i], &start_count[j]) {
                    is_possible = true;
                    break;
                }
            }
            if is_possible {
                res += 1;
            }
        }
        res
    }
    */
    pub fn word_count(start_words: Vec<String>, target_words: Vec<String>) -> i32 {
        let mut start_words = start_words;
        let mut start_set: HashSet<String> = HashSet::new();
        for i in 0..start_words.len() {
            let mut chars: Vec<char> = start_words[i].chars().collect();
            chars.sort();
            let word = chars.iter().collect::<String>();
            start_set.insert(word);
        }
        let mut target_hashmap: HashMap<String, i32> = HashMap::new();
        for i in 0..target_words.len() {
            let mut chars: Vec<char> = target_words[i].chars().collect();
            chars.sort();
            let word = chars.iter().collect::<String>();
            if target_hashmap.contains_key(&word) {
                *target_hashmap.get_mut(&word).unwrap() += 1;
            } else {
                target_hashmap.insert(word, 1);
            }
        }
        let mut ans = 0;
        for (word, count) in target_hashmap.iter() {
            let mut chars: Vec<char> = word.chars().collect();
            for i in 0..chars.len() {
                let ch = chars[i];
                chars.remove(i);
                let res: String = chars.iter().collect::<String>();
                if start_set.contains(&res) {
                    ans += *count;
                    break;
                }
                chars.insert(i, ch)
            }
        }
        ans
    }
}
// submission codes end
 
 #[cfg(test)]
 mod tests {
     use super::*;
 
     #[test]
     fn test_2135() {
        assert_eq!(Solution::word_count(vec_string!["ant","act","tack"], vec_string!["tack","act","acti"]), 2);
        assert_eq!(Solution::word_count(vec_string!["ab","a"], vec_string!["abc","abcd"]), 1);
            
    }
 }
 
```
