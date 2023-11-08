---
title: 438. find all anagrams in a string
date: '2022-03-12'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0438 find all anagrams in a string
---



Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



>   Example 1:
>   Input: s <TeX>=</TeX> "cbaebabacd", p <TeX>=</TeX> "abc"
>   Output: [0,6]
>   Explanation:
>   The substring with start index <TeX>=</TeX> 0 is "cba", which is an anagram of "abc".
>   The substring with start index <TeX>=</TeX> 6 is "bac", which is an anagram of "abc".
>   Example 2:
>   Input: s <TeX>=</TeX> "abab", p <TeX>=</TeX> "ab"
>   Output: [0,1,2]
>   Explanation:
>   The substring with start index <TeX>=</TeX> 0 is "ab", which is an anagram of "ab".
>   The substring with start index <TeX>=</TeX> 1 is "ba", which is an anagram of "ab".
>   The substring with start index <TeX>=</TeX> 2 is "ab", which is an anagram of "ab".
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length, p.length <TeX>\leq</TeX> 3  10^4
>   	s and p consist of lowercase English letters.


## Solution


### Python
```python
class Solution:
def findAnagrams(self, s: str, p: str) -> List[int]:
def calculateFreq(s):
freq = [0] * 26
for ch in s:
freq[ord(ch) - ord('a')] += 1
return freq
def compareFreq(freq1, freq2):
for i in range(26):
if freq1[i] != freq2[i]:
return False
return True
n = len(s)
k = len(p)
p_freq = calculateFreq(p)
ans = []
for i in range(n - k + 1): # [i, i + k -1]
if i == 0:
freq = calculateFreq(s[i: i + k])
else:


# i - 1 out and i + k - 1 in.
freq[ord(s[i - 1]) - ord('a')] -= 1
freq[ord(s[i + k - 1]) - ord('a')] += 1
if compareFreq(freq, p_freq):
ans.append(i)
return ans
```


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn is_all_same(counts: &[i32; 26], cur_counts: &[i32; 26]) -> bool {
for i in 0..26 {
if counts[i] != cur_counts[i] {
return false;
}
}
true
}
pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
if p.len() > s.len() {
return vec![];
}
let mut counts = [0; 26];
for ch in p.chars() {
let index = (ch as usize - 'a' as usize);
counts[index] += 1;
}
let chars: Vec<char> = s.chars().collect();
let mut cur_counts = [0; 26];
for i in 0..p.len() {
let index = chars[i] as usize - 'a' as usize;
cur_counts[index] += 1;
}
let mut results: Vec<i32> = vec![];
if Self::is_all_same(&counts, &cur_counts) {
results.push(0);
}
for i in p.len()..s.len() {
let enter_index = chars[i] as usize - 'a' as usize;
let remove_index = chars[i - p.len()] as usize - 'a' as usize;
cur_counts[enter_index] += 1;
cur_counts[remove_index] -= 1;
// println!("i: {}, cur_counts: {:?}", i, cur_counts);
if Self::is_all_same(&counts, &cur_counts) {
results.push((i - p.len() + 1) as i32);
}
}
results
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_438() {
assert_eq!(Solution::find_anagrams("cbaebabacd".to_string(), "abc".to_string()), vec![0, 6]);
}
}

```
