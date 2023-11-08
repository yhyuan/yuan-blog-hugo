---
title: 1258. synonymous sentences
date: '2022-07-25'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1258 synonymous sentences
---


You are given a list of equivalent string pairs synonyms where synonyms[i] <TeX>=</TeX> [si, ti] indicates that si and ti are equivalent strings. You are also given a sentence text.



Return all possible synonymous sentences sorted lexicographically.







> Example 1:
> Input: synonyms <TeX>=</TeX> [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text <TeX>=</TeX> "I am happy today but was sad yesterday"
> Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]
> Example 2:
> Input: synonyms <TeX>=</TeX> [["happy","joy"],["cheerful","glad"]], text <TeX>=</TeX> "I am happy today but was sad yesterday"
> Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
**Constraints:**
> 0 <TeX>\leq</TeX> synonyms.length <TeX>\leq</TeX> 10
> synonyms[i].length <TeX>=</TeX><TeX>=</TeX> 2
> 1 <TeX>\leq</TeX> si.length, ti.length <TeX>\leq</TeX> 10
> si !<TeX>=</TeX> ti
> text consists of at most 10 words.
> The words of text are separated by single spaces.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::{HashSet, HashMap};
pub struct DisjointSet {
parents: Vec<usize>,
ranks: Vec<usize>,
}

impl DisjointSet {
pub fn new(n: usize) -> Self {
let parents = (0..n).into_iter().collect::<Vec<_>>();
let ranks: Vec<usize> = vec![1; n];
DisjointSet {
parents,
ranks
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
impl Solution {
pub fn generate(text_words: &Vec<&str>, index: usize, words_map: &HashMap<String, Vec<String>>) -> Vec<String> {
if index >= text_words.len() {
return vec!["".to_owned()];
}
let mut first_index = usize::MAX;
for i in index..text_words.len() {
if words_map.contains_key(text_words[i]) {
first_index = i;
break;
}
}
if first_index == usize::MAX {
let s = text_words[index..].join(" ");
return vec![s];
}
let pre = text_words[index..first_index].join(" ");
//println!("s:{}:", s);
let results = Self::generate(text_words, first_index + 1, words_map);
let words = words_map.get(text_words[first_index]).unwrap();
//println!("words: {:?}", words);
let mut new_results: Vec<String> = vec![];
for i in 0..words.len() {
for j in 0..results.len() {
if pre.len() == 0 {
if results[j].len() == 0 {
new_results.push(words[i].clone());
} else {
new_results.push(format!("{} {}", words[i], results[j]));
}
} else {
if results[j].len() == 0 {
new_results.push(format!("{} {}", pre, words[i]));
} else {
new_results.push(format!("{} {} {}", pre, words[i], results[j]));
}
}
}
}
new_results
}

pub fn generate_sentences(synonyms: Vec<Vec<String>>, text: String) -> Vec<String> {
let set: HashSet<String> = synonyms.iter().map(|v|v[0].clone())
.chain(synonyms.iter().map(|v|v[1].clone())).collect();
let words = set.iter().collect::<Vec<_>>();
let n = words.len();
let mut hashmap: HashMap<String, usize> = HashMap::new();
for i in 0..n {
hashmap.insert(words[i].clone(), i);
}
let mut disjoint_set = DisjointSet::new(n);
for i in 0..synonyms.len() {
let k0 = hashmap.get(&synonyms[i][0]).unwrap();
let k1 = hashmap.get(&synonyms[i][1]).unwrap();
//println!("k0: {}, k1: {}", k0, k1);
disjoint_set.union(*k0, *k1);
//println!("parents: {:?}", disjoint_set.parents);
}
let mut parent_words_map: HashMap<usize, Vec<String>> = HashMap::new();
for i in 0..n {
let p = disjoint_set.find(i);
let child = words[i];
if parent_words_map.contains_key(&p) {
let children = parent_words_map.get_mut(&p).unwrap();
children.push(child.clone());
children.sort();
} else {
parent_words_map.insert(p, vec![child.clone()]);
}
}
let mut words_map: HashMap<String, Vec<String>> = HashMap::new();
for i in 0..n {
let word = words[i];
let p = disjoint_set.find(i);
let children = parent_words_map.get(&p).unwrap();
words_map.insert(word.clone(), children.clone());
}
let text_words = text.split_whitespace().collect::<Vec<_>>();
let mut results = Self::generate(&text_words, 0, &words_map);
//println!("parents: {:?}", disjoint_set.parents);
//println!("words_map: {:?}", words_map);

results
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1254() {
assert_eq!(Solution::generate_sentences(vec![vec_string!["a","b"],vec_string!["b","c"],vec_string!["d","e"],vec_string!["c","d"]], "a b".to_string()),
vec_string!["a a","a b","a c","a d","a e","b a","b b","b c","b d","b e","c a","c b","c c","c d","c e","d a","d b","d c","d d","d e","e a","e b","e c","e d","e e"]);

assert_eq!(Solution::generate_sentences(vec![vec_string!["a","QrbCl"]], "d QrbCl ya ya NjZQ".to_string()),
vec_string!["d QrbCl ya ya NjZQ","d a ya ya NjZQ"]);

assert_eq!(Solution::generate_sentences(vec![
vec_string!["a","b"],
vec_string!["c","d"],
vec_string!["e","f"]], "a c e".to_string()),
vec_string!["a c e","a c f","a d e","a d f","b c e","b c f","b d e","b d f"]);

assert_eq!(Solution::generate_sentences(vec![
vec_string!["happy","joy"],
vec_string!["sad","sorrow"],
vec_string!["joy","cheerful"]], "I am happy today but was sad yesterday".to_string()),
vec_string!["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]);
assert_eq!(Solution::generate_sentences(vec![
vec_string!["happy","joy"],
vec_string!["glad","cheerful"]], "I am happy today but was sad yesterday".to_string()),
vec_string!["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]);

}
}




```
