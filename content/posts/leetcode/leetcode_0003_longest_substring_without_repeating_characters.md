---
title: 3. longest substring without repeating characters
date: '2021-05-04'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0003 longest substring without repeating characters
---



Given a string s, find the length of the longest substring without repeating characters.



>   Example 1:
>   Input: s <TeX>=</TeX> "abcabcbb"
>   Output: 3
>   Explanation: The answer is "abc", with the length of 3.
>   Example 2:
>   Input: s <TeX>=</TeX> "bbbbb"
>   Output: 1
>   Explanation: The answer is "b", with the length of 1.
>   Example 3:
>   Input: s <TeX>=</TeX> "pwwkew"
>   Output: 3
>   Explanation: The answer is "wke", with the length of 3.
>   Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
>   Example 4:
>   Input: s <TeX>=</TeX> ""
>   Output: 0
**Constraints:**
>   	0 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 5  10^4
>   	s consists of English letters, digits, symbols and spaces.


## Solution
Sliding window


### Python
```python
class Solution:
def lengthOfLongestSubstring(self, s: str) -> int:
n = len(s)
i = 0
j = 0
size = 0
freq = {}
ans = 0
def haveReapting(freq):
for ch in freq:
if freq[ch] > 1:
return True
return False

while i < n:
while i < n and not haveReapting(freq):
freq[s[i]] = freq.get(s[i], 0) + 1
size += 1
i += 1
if haveReapting(freq):
ans = max(ans, size - 1)
else:
ans = max(ans, size)
while j < i and haveReapting(freq):
if freq[s[j]] == 1:
del freq[s[j]]
else:
freq[s[j]] -= 1
size -= 1
j += 1
return ans
```


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashMap;
impl Solution {
pub fn length_of_longest_substring(s: String) -> i32 {
//let s = s.trim();
let chars: Vec<char> = s.chars().collect();
let mut max_len = 0i32;
let mut hashmap: HashMap<char, usize> = HashMap::new();
let mut start = 0usize;
for (i, &ch) in chars.iter().enumerate() {
if hashmap.contains_key(&ch) {
let hashmap_size = hashmap.keys().len() as i32;
max_len = i32::max(hashmap_size, max_len);
let index = hashmap[&ch];
for j in start..index {
let ch = chars[j];
hashmap.remove_entry(&ch);
}
hashmap.insert(ch, i);
start = index + 1;
} else {
hashmap.insert(ch, i);
}
}
//println!("chars: {:?}", chars);
i32::max(max_len, hashmap.keys().len() as i32)
}
}
*/
use std::collections::HashSet;
impl Solution {
pub fn length_of_longest_substring(s: String) -> i32 {
let chars: Vec<char> = s.chars().collect();
let n = chars.len();
let mut hashset: HashSet<char> = HashSet::new();
let mut start = 0usize;
let mut result = 0i32;
for i in 0..n {
let ch = chars[i];
if hashset.contains(&ch) {
while hashset.contains(&ch) {
hashset.remove(&chars[start]);
start += 1;
}
}
hashset.insert(ch);
result = i32::max(result, i as i32 - start as i32 + 1);
}
result = i32::max(result, hashset.len() as i32);
result
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_3() {
assert_eq!(Solution::length_of_longest_substring(" ".to_string()), 1);
assert_eq!(Solution::length_of_longest_substring("abcabcbb".to_string()),3);
assert_eq!(Solution::length_of_longest_substring("bbbb".to_string()), 1);
assert_eq!(Solution::length_of_longest_substring("pwwkew".to_string()), 3);
assert_eq!(Solution::length_of_longest_substring("dvdf".to_string()), 3);
}
}

```
