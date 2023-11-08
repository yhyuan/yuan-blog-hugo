---
title: 767. reorganize string
date: '2022-05-12'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0767 reorganize string
---



Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



>   Example 1:
>   Input: s <TeX>=</TeX> "aab"
>   Output: "aba"
>   Example 2:
>   Input: s <TeX>=</TeX> "aaab"
>   Output: ""
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 500
>   	s consists of lowercase English letters.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::HashMap;
impl Solution {
pub fn helper(hashmap: &mut HashMap<char, usize>) -> String {
let mut chars: Vec<char> = hashmap.iter()
.map(|(&key, _)| key)
.collect();
chars.sort_by_key(|ch| *hashmap.get(&ch).unwrap());
chars.reverse();
//println!("chars: {:?}", chars);
let s: String = format!("{}{}", chars[0], chars[1]);
for i in 0..2 {
let val = *hashmap.get(&chars[i]).unwrap();
if val == 1usize {
hashmap.remove(&chars[i]);
} else {
hashmap.insert(chars[i], val - 1);
}
}
if hashmap.keys().len() == 0 {
return s;
}
if hashmap.keys().len() == 1 {
let mut chars: Vec<char> = hashmap.iter()
.map(|(&key, _)| key)
.collect();
let key = chars[0];
let count = *hashmap.get(&key).unwrap();
return if count > 1 {
"".to_string()
} else {
format!("{}{}", s, key)
}
}
let sub_res = Self::helper(hashmap);
if sub_res.len() == 0 {
return "".to_string();
}
format!("{}{}", s, sub_res)

}
pub fn reorganize_string(s: String) -> String {
let chars: Vec<char> = s.chars().collect();
let mut hashmap: HashMap<char, usize> = HashMap::new();
let n = chars.len();
for i in 0..n {
*hashmap.entry(chars[i]).or_insert(0) += 1;
}
let key = chars[0];
if hashmap.keys().len() == 1 {
let count = *hashmap.get(&key).unwrap();
return if count > 1 {
"".to_string()
} else {
format!("{}", key)
}
}
Self::helper(&mut hashmap)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_767() {
assert_eq!(Solution::reorganize_string("aab".to_string()), "aba".to_string());
assert_eq!(Solution::reorganize_string("aaab".to_string()), "".to_string());
}
}

```
