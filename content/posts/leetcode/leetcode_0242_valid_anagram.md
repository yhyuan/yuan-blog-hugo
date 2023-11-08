---
title: 242. valid anagram
date: '2021-11-27'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0242 valid anagram
---



Given two strings s and t, return true if t is an anagram of s, and false otherwise.



>   Example 1:
>   Input: s <TeX>=</TeX> "anagram", t <TeX>=</TeX> "nagaram"
>   Output: true
>   Example 2:
>   Input: s <TeX>=</TeX> "rat", t <TeX>=</TeX> "car"
>   Output: false
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length, t.length <TeX>\leq</TeX> 5  10^4
>   	s and t consist of lowercase English letters.
>   Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
//use std::collections::HashMap;
impl Solution {
pub fn is_anagram(s: String, t: String) -> bool {
if s.len() != t.len() {
return  false;
}
let mut s_vec: Vec<usize> = vec![0; 26];
let mut t_vec: Vec<usize> = vec![0; 26];

for s_ch in s.chars() {
let index = s_ch as u8 - 'a' as u8;
s_vec[index as usize] += 1;
}
for t_ch in t.chars() {
let index = t_ch as u8 - 'a' as u8;
t_vec[index as usize] += 1;
}

s_vec == t_vec
/*
let s_chars: Vec<char> = s.chars().collect();
let t_chars: Vec<char> = t.chars().collect();
let mut s_hashmap: HashMap<char, usize> = HashMap::with_capacity(s.len());
for ch in s_chars.iter() {
if s_hashmap.contains_key(ch) {
s_hashmap.insert(*ch, s_hashmap[ch] + 1);
} else {
s_hashmap.insert(*ch, 1);
}
}
let mut t_hashmap: HashMap<char, usize> = HashMap::with_capacity(t.len());
for ch in t_chars.iter() {
if t_hashmap.contains_key(ch) {
t_hashmap.insert(*ch, t_hashmap[ch] + 1);
} else {
t_hashmap.insert(*ch, 1);
}
}
println!("t: {:?}", t_hashmap);
println!("s: {:?}", s_hashmap);
for (k, v) in s_hashmap.iter() {
if !t_hashmap.contains_key(k) {
return false;
}
if t_hashmap[k] != *v {
return false;
}
}
for (k, v) in t_hashmap.iter() {
if !s_hashmap.contains_key(k) {
return false;
}
if s_hashmap[k] != *v {
return false;
}
}
true
*/
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_242() {
/*
assert_eq!(
Solution::is_anagram("anagram".to_owned(), "nagaram".to_owned()),
true
);
*/
assert_eq!(
Solution::is_anagram("aa".to_owned(), "a".to_owned()),
false
);

}
}

```
