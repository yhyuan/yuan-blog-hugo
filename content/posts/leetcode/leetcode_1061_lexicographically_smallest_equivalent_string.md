---
title: 1061. lexicographically smallest equivalent string
date: '2022-07-05'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 1061 lexicographically smallest equivalent string
---


You are given two strings of the same length s1 and s2 and a string baseStr.



We say s1[i] and s2[i] are equivalent characters.



For example, if s1 <TeX>=</TeX> "abc" and s2 <TeX>=</TeX> "cde", then we have 'a' <TeX>=</TeX><TeX>=</TeX> 'c', 'b' <TeX>=</TeX><TeX>=</TeX> 'd', and 'c' <TeX>=</TeX><TeX>=</TeX> 'e'.

Equivalent characters follow the usual rules of any equivalence relation:



Reflexivity: 'a' <TeX>=</TeX><TeX>=</TeX> 'a'.

Symmetry: 'a' <TeX>=</TeX><TeX>=</TeX> 'b' implies 'b' <TeX>=</TeX><TeX>=</TeX> 'a'.

Transitivity: 'a' <TeX>=</TeX><TeX>=</TeX> 'b' and 'b' <TeX>=</TeX><TeX>=</TeX> 'c' implies 'a' <TeX>=</TeX><TeX>=</TeX> 'c'.

For example, given the equivalency information from s1 <TeX>=</TeX> "abc" and s2 <TeX>=</TeX> "cde", "acd" and "aab" are equivalent strings of baseStr <TeX>=</TeX> "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.



Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.







> Example 1:
> Input: s1 <TeX>=</TeX> "parker", s2 <TeX>=</TeX> "morris", baseStr <TeX>=</TeX> "parser"
> Output: "makkek"
> Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
> The characters in each group are equivalent and sorted in lexicographical order.
> So the answer is "makkek".
> Example 2:
> Input: s1 <TeX>=</TeX> "hello", s2 <TeX>=</TeX> "world", baseStr <TeX>=</TeX> "hold"
> Output: "hdld"
> Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
> So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
> Example 3:
> Input: s1 <TeX>=</TeX> "leetcode", s2 <TeX>=</TeX> "programs", baseStr <TeX>=</TeX> "sourcecode"
> Output: "aauaaaaada"
> Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
**Constraints:**
> 1 <TeX>\leq</TeX> s1.length, s2.length, baseStr <TeX>\leq</TeX> 1000
> s1.length <TeX>=</TeX><TeX>=</TeX> s2.length
> s1, s2, and baseStr consist of lowercase English letters.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
pub parents: Vec<usize>,
pub ranks: Vec<usize>,
}

impl DisjointSet {
pub fn new(n: usize) -> Self {
let parents = (0..n).into_iter().collect::<Vec<_>>();
let ranks = vec![1; n];
DisjointSet {
parents,
ranks,
}
}

pub fn find(&self, i: usize) -> usize {
let mut parent = self.parents[i];
while parent != self.parents[parent] {
parent = self.parents[parent];
}
parent
}

pub fn union(&mut self, i: usize, j: usize) -> bool {
let ip = self.find(i);
let jp = self.find(j);
if ip == jp {
return false;
}
if self.ranks[ip] < self.ranks[jp] {
self.parents[ip] = self.parents[jp];
} else if self.ranks[ip] > self.ranks[jp] {
self.parents[jp] = self.parents[ip];
} else {
self.parents[jp] = self.parents[ip];
self.ranks[ip] += 1;
}
true
}
}
use std::collections::{HashSet, HashMap};
impl Solution {
pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
let chars = s1.chars().chain(s2.chars()).collect::<HashSet<_>>();
let chars = chars.into_iter().collect::<Vec<char>>();
let mut hashmap: HashMap<char, usize> = HashMap::new();
for i in 0..chars.len() {
hashmap.insert(chars[i], i);
}
let n = s1.len();
let mut disjoint_set = DisjointSet::new(hashmap.len());
for i in 0..n {
let char1 = s1.chars().nth(i).unwrap();
let char2 = s2.chars().nth(i).unwrap();
let k1 = hashmap.get(&char1).unwrap();
let k2 = hashmap.get(&char2).unwrap();
disjoint_set.union(*k1, *k2);
}
//println!("chars: {:?}", chars);
let mut parents_hashmap: HashMap<usize, Vec<char>> = HashMap::new();
for i in 0..disjoint_set.parents.len() {
let ip = disjoint_set.find(i);
if parents_hashmap.contains_key(&ip) {
let mut chars_vector = parents_hashmap.get_mut(&ip).unwrap();
chars_vector.push(chars[i]);
} else {
parents_hashmap.insert(ip, vec![chars[i]]);
}
}
let mut smallest_hashmap: HashMap<usize, char> = HashMap::new();
for (key, value) in parents_hashmap.iter() {
let min_val = value.iter().min().unwrap();
smallest_hashmap.insert(*key, * min_val);
}
let mut parents = (0..hashmap.len()).into_iter().map(|i| disjoint_set.find(i)).collect::<Vec<_>>();
let base_chars = base_str.chars().collect::<Vec<char>>();
let mut result: Vec<char> = Vec::new();
//println!("base_str: {}",base_str);
//println!("hashmap: {:?}",hashmap);
for i in 0..base_chars.len() {
let ch = base_chars[i];
//println!("ch: {}", ch);
let c = if hashmap.contains_key(&ch) {
let k = *hashmap.get(&ch).unwrap();
let parent = disjoint_set.find(k);
smallest_hashmap.get(&parent).unwrap()
} else {
&ch
};
result.push(*c);
}
let s = result.into_iter().collect::<String>();
s
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1101() {
assert_eq!(Solution::smallest_equivalent_string("parker".to_string(), "morris".to_string(), "parser".to_string()), "makkek".to_string());
assert_eq!(Solution::smallest_equivalent_string("hello".to_string(), "world".to_string(), "hold".to_string()), "hdld".to_string());
assert_eq!(Solution::smallest_equivalent_string("leetcode".to_string(), "programs".to_string(), "sourcecode".to_string()), "aauaaaaada".to_string());
}
}

```
