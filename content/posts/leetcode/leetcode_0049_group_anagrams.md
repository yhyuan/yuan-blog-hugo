---
title: 49. group anagrams
date: '2021-06-19'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0049 group anagrams
---



Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



>   Example 1:
>   Input: strs <TeX>=</TeX> ["eat","tea","tan","ate","nat","bat"]
>   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
>   Example 2:
>   Input: strs <TeX>=</TeX> [""]
>   Output: [[""]]
>   Example 3:
>   Input: strs <TeX>=</TeX> ["a"]
>   Output: [["a"]]
**Constraints:**
>   	1 <TeX>\leq</TeX> strs.length <TeX>\leq</TeX> 10^4
>   	0 <TeX>\leq</TeX> strs[i].length <TeX>\leq</TeX> 100
>   	strs[i] consists of lowercase English letters.


## Solution


### Python
```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
dataDict = {}
def calculateKey(string):
chars = list(map(lambda i: string[i], range(len(string))))
chars.sort()
return "".join(chars)

n = len(strs)
for i in range(n):
key = calculateKey(strs[i])
if key in dataDict:
dataDict[key] = dataDict[key] + [strs[i]]
else:
dataDict[key] = [strs[i]]
ans = []
for key in dataDict:
ans.append(dataDict[key])
return ans
```


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
let mut hashmap: HashMap<String, Vec<String>> = HashMap::new();
for str in strs.iter() {
let mut chars: Vec<char> = str.chars().collect();
chars.sort();
let new_str: String = chars.iter().collect();
if hashmap.contains_key(&new_str) {
let mut strings = hashmap[&new_str].clone();
strings.push(str.to_string());
hashmap.insert(new_str, strings);
} else {
hashmap.insert(new_str, vec![str.to_string()]);
}
}
let mut results: Vec<Vec<String>> = vec![];
for (key, value) in hashmap {
results.push(value);
}
results
//hashmap.values().collect()
//println!("hashmap: {:?}", hashmap);
//vec![]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_49() {
let results = Solution::group_anagrams(vec_string!["eat", "tea", "tan", "ate", "nat", "bat"]);
assert_eq!(results.len(), 3);
/*
let pre_results = vec![
vec_string!["tan", "nat"],
vec_string!["bat"],
vec_string!["eat", "ate", "tea"],
];
*/
//assert_eq!(pre_results.contains(results[&0usize]), true);
//assert_eq!(pre_results.contains(results[&1usize]), true);
//assert_eq!(pre_results.contains(results[&2usize]), true);
}
}

```
