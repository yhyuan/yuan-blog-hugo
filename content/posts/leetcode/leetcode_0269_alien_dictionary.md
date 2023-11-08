---
title: 269. alien dictionary
date: '2021-12-09'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0269 alien dictionary
---



There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.



You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.



Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.



A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.



>   Example 1:
>   Input: words <TeX>=</TeX> ["wrt","wrf","er","ett","rftt"]
>   Output: "wertf"
>   Example 2:
>   Input: words <TeX>=</TeX> ["z","x"]
>   Output: "zx"
>   Example 3:
>   Input: words <TeX>=</TeX> ["z","x","z"]
>   Output: ""
>   Explanation: The order is invalid, so return "".
**Constraints:**
>   1 <TeX>\leq</TeX> words.length <TeX>\leq</TeX> 100
>   1 <TeX>\leq</TeX> words[i].length <TeX>\leq</TeX> 100
>   words[i] consists of only lowercase English letters.


## Solution


### Rust
```rust
pub struct Solution {}
//use std::collections::HashMap;

// submission codes start here
/*
impl Solution {
pub fn create_graph(words: &Vec<String>, hashmap: &mut HashMap<char, Vec<char>>) -> bool {
if words.len() == 0 {
return true;
}
let mut pre_char = ' ';
let mut word_hashmap: HashMap<char, Vec<String>> = HashMap::new();
for word in words.iter() {
if pre_char != ' ' && word.len() == 0 {
return false;
}
if word.len() == 0 {
continue;
}
let first_char = word.chars().nth(0).unwrap();
if pre_char == ' ' {
pre_char = first_char;
} else if pre_char != first_char {
if hashmap.contains_key(&pre_char) {
let mut vect = hashmap.get(&pre_char).unwrap().to_vec();
vect.push(first_char);
hashmap.insert(pre_char, vect);
} else {
hashmap.insert(pre_char, vec![first_char]);
}
pre_char = first_char;
} else {
if !hashmap.contains_key(&pre_char) {
hashmap.insert(pre_char, vec![]);
}
}
// println!("word.len():{}", word.len());
//if word.len() > 1 {
let sub_word = &word[1..];
if word_hashmap.contains_key(&first_char) {
let mut sub_words = word_hashmap.get(&first_char).unwrap().to_vec();
sub_words.push(sub_word.to_string());
word_hashmap.insert(first_char, sub_words);
} else {
word_hashmap.insert(first_char, vec![sub_word.to_string()]);
}
//}
/* else {
if word_hashmap.len() > 0 {
return false;
}
}*/
// println!("{}", word);
}
for ch in word_hashmap.keys() {
let sub_words = word_hashmap.get(&ch).unwrap();
let result = Solution::create_graph(sub_words, hashmap);
if !result {
return false;
}
}
true
}
pub fn dfs(ch: &char, hashmap: &HashMap<char, Vec<char>>, visited: &mut HashMap<char, bool>, on_stack: &mut HashMap<char, bool>, order: &mut Vec<char>, is_cycle_detected: &mut bool) {
visited.insert(*ch, true);
on_stack.insert(*ch, true);
//println!("{}", ch);
if hashmap.get(ch).is_some() {
let neighbors = hashmap.get(ch).unwrap();
//println!("neighbors: {:?}", neighbors);
for neighbor in neighbors.iter() {
let is_visited = visited.get(neighbor).unwrap();
//println!("visited: {:?}", is_visited);
if !*is_visited {
Self::dfs(neighbor, hashmap, visited, on_stack, order, is_cycle_detected);
}
let is_on_stack = on_stack.get(neighbor).unwrap();
if *is_on_stack {
*is_cycle_detected = true;
}
}
}
order.push(*ch);
on_stack.insert(*ch, false);
}
pub fn alien_order(words: Vec<String>) -> String {
let mut hashmap: HashMap<char, Vec<char>> = HashMap::new();
let result = Solution::create_graph(&words, &mut hashmap);
if !result {
return "".to_owned();
}
// println!("{:?}", hashmap);
let mut visited: HashMap<char, bool> = HashMap::new();
let mut on_stack: HashMap<char, bool> = HashMap::new();

for word in words.iter() {
for j in 0..word.len() {
let ch = word.chars().nth(j).unwrap();
visited.insert(ch, false);
on_stack.insert(ch, false);
}
}
let mut order: Vec<char> = vec![];
let mut is_cycle_detected = false;
// println!("hashmap: {:?}", hashmap);
// println!("visited: {:?}", visited);
for ch in hashmap.keys() {
if !visited[ch] {
Solution::dfs(ch, &hashmap, &mut visited, &mut on_stack, &mut order, &mut is_cycle_detected);
if is_cycle_detected {
return "".to_owned();
}
}
}
order.reverse();
for ch in visited.keys() {
// println!("ch: {}", ch);
if !visited[ch] {
order.push(*ch);
}
}
// println!("order: {:?}", order);
// println!("visited: {:?}", visited);
let str = order.iter().collect::<String>();
str
}
}
*/
use std::collections::{HashSet, HashMap};
impl Solution {
pub fn dfs(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, on_stack: &mut Vec<bool>, post_order: &mut Vec<usize>, index: usize) -> bool {
visited[index] = true;
on_stack[index] = true;
for &neighbor in graph[index].iter() {
if on_stack[neighbor] {
return true;
}
if visited[neighbor] {
continue;
}
if Self::dfs(graph, visited, on_stack, post_order, neighbor) {
return true;
}
}
on_stack[index] = false;
post_order.push(index);
false
}
pub fn alien_order(words: Vec<String>) -> String {
let n = words.len();
let words = words.into_iter().map(|s| s.chars().collect::<Vec<_>>()).collect::<Vec<_>>();
let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); 26];
let mut chars_freq = vec![0; 26];
words.iter().for_each(|v| v.iter().for_each(|&ch| {
chars_freq[ch as usize - 'a' as usize] += 1;
}));
for i in 1..n {
let len1 = words[i - 1].len();
let len2 = words[i].len();
let mut index = usize::MAX;
for j in 0..usize::min(len1, len2) {
if words[i - 1][j] != words[i][j] {
index = j;
break;
}
}
if index == usize::MAX {
if len1 <= len2 {
continue;
} else {
return "".to_owned();
}
}
let char1 = words[i - 1][index] as usize - 'a' as usize;
let char2 = words[i][index] as usize - 'a' as usize;
graph[char1].insert(char2);
}
let chars_iter = chars_freq.iter().filter(|&v| v > &0);
if chars_iter.count() == 1 {
let mut index = usize::MAX;
for i in 0..chars_freq.len() {
if chars_freq[i] > 0 {
index = i;
break;
}
}
return format!("{}", ('a' as u8 + index as u8) as char);
}
let mut visited = vec![false; 26];
let mut on_stack = vec![false; 26];
let mut post_order: Vec<usize> = vec![];
for i in 0..26 {
if chars_freq[i] > 0 && !visited[i] {
if Self::dfs(&graph, &mut visited, &mut on_stack, &mut post_order, i) {
return "".to_string();
}
}
}
post_order.reverse();
let mut result_chars: Vec<char> = vec![];
for i in 0..post_order.len() {
chars_freq[post_order[i]] = 0;
result_chars.push((post_order[i] as u8 + 'a' as u8) as char);
}
for i in 0u8..26 {
if chars_freq[i as usize] > 0 {
result_chars.push((i + 'a' as u8) as char);
}
}
result_chars.into_iter().collect::<String>()
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_269() {
assert_eq!(Solution::alien_order(vec!["wrt".to_owned(),"wrf".to_owned(),"er".to_owned(),"ett".to_owned(),"rftt".to_owned()]), "wertf".to_owned());
assert_eq!(Solution::alien_order(vec!["z".to_owned(),"x".to_owned()]), "zx".to_owned());
assert_eq!(Solution::alien_order(vec!["z".to_owned(),"x".to_owned(),"z".to_owned()]), "".to_owned());
assert_eq!(Solution::alien_order(vec!["z".to_owned(),"z".to_owned()]), "z".to_owned());
assert_eq!(Solution::alien_order(vec!["ab".to_owned(),"adc".to_owned()]), "cbda".to_owned());
assert_eq!(Solution::alien_order(vec!["abc".to_owned(),"ab".to_owned()]), "".to_owned());
assert_eq!(Solution::alien_order(vec!["ac".to_owned(),"ab".to_owned(),"b".to_owned()]), "cab".to_owned());
assert_eq!(Solution::alien_order(vec!["wrt".to_owned(),"wrtkj".to_owned()]), "wtrkj".to_owned());
}
}

```
