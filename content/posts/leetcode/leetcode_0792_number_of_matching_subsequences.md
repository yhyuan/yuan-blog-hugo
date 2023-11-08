---
title: 792. number of matching subsequences
date: '2022-05-19'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0792 number of matching subsequences
---



Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.



For example, "ace" is a subsequence of "abcde".





>   Example 1:
>   Input: s <TeX>=</TeX> "abcde", words <TeX>=</TeX> ["a","bb","acd","ace"]
>   Output: 3
>   Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
>   Example 2:
>   Input: s <TeX>=</TeX> "dsahjpjauf", words <TeX>=</TeX> ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
>   Output: 2
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 5  10^4
>   	1 <TeX>\leq</TeX> words.length <TeX>\leq</TeX> 5000
>   	1 <TeX>\leq</TeX> words[i].length <TeX>\leq</TeX> 50
>   	s and words[i] consist of only lowercase English letters.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;

impl Solution {
pub fn is_matched(chars: &Vec<char>, word_chars: &Vec<char>) -> bool {
let n = chars.len();
let mut j = 0;
for i in 0..n {
// println!("i: {}, j: {}", i, j);
if j == word_chars.len() {
return true;
}
if chars[i] == word_chars[j] {
j += 1;
}
}
j == word_chars.len()
}
pub fn build_chars_frequency(chars: &Vec<char>) -> HashMap<char, i32> {
let mut freq: HashMap<char, i32> = HashMap::new();
for i in 0..chars.len() {
if freq.contains_key(&chars[i]) {
*freq.get_mut(&chars[i]).unwrap() += 1;
} else {
freq.insert(chars[i], 1);
}
}
freq
}
pub fn compare_frequences(s_freq: &HashMap<char, i32>, word_freq: &HashMap<char, i32>) -> bool {
let mut is_matched = true;
for (&ch, &count) in word_freq.iter() {
if !s_freq.contains_key(&ch) {
is_matched = false;
break;
}
let s_count = s_freq[&ch];
let word_count = word_freq[&ch];
if s_count < word_count {
is_matched = false;
break;
}
}
is_matched
}
pub fn num_matching_subseq(s: String, words: Vec<String>) -> i32 {
let mut ans = 0;
let chars: Vec<char> = s.chars().collect();
let s_freq = Self::build_chars_frequency(&chars);
let mut memo: HashMap<String, bool> = HashMap::new();
for i in 0..words.len() {
if memo.contains_key(&words[i]) {
let val = memo.get(&words[i]).unwrap();
if *val {
ans += 1;
}
continue;
}
let word_chars: Vec<char> = words[i].chars().collect();
let word_freq = Self::build_chars_frequency(&word_chars);
let is_matched = Self::compare_frequences(&s_freq, &word_freq);
if !is_matched {
memo.insert(words[i].clone(), false);
continue;
}
let is_matched = Self::is_matched(&chars, &word_chars);
memo.insert(words[i].clone(), is_matched);
// println!("word: {}, is_matched: {}", words[i], is_matched);
if is_matched {
ans += 1;
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
fn test_792() {
assert_eq!(Solution::num_matching_subseq("abcde".to_string(), vec_string!["a","bb","acd","ace"]), 3);
assert_eq!(Solution::num_matching_subseq("dsahjpjauf".to_string(), vec_string!["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]), 2);
}
}

```
