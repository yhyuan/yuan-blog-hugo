---
title: 433. minimum genetic mutation
date: '2022-03-10'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0433 minimum genetic mutation
---



A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.



For example, "AACCGGTT" --> "AACCGGTA" is one mutation.



There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



>   Example 1:
>   Input: start <TeX>=</TeX> "AACCGGTT", end <TeX>=</TeX> "AACCGGTA", bank <TeX>=</TeX> ["AACCGGTA"]
>   Output: 1
>   Example 2:
>   Input: start <TeX>=</TeX> "AACCGGTT", end <TeX>=</TeX> "AAACGGTA", bank <TeX>=</TeX> ["AACCGGTA","AACCGCTA","AAACGGTA"]
>   Output: 2
>   Example 3:
>   Input: start <TeX>=</TeX> "AAAAACCC", end <TeX>=</TeX> "AACCCCCC", bank <TeX>=</TeX> ["AAAACCCC","AAACCCCC","AACCCCCC"]
>   Output: 3
**Constraints:**
>   	start.length <TeX>=</TeX><TeX>=</TeX> 8
>   	end.length <TeX>=</TeX><TeX>=</TeX> 8
>   	0 <TeX>\leq</TeX> bank.length <TeX>\leq</TeX> 10
>   	bank[i].length <TeX>=</TeX><TeX>=</TeX> 8
>   	start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
use std::collections::VecDeque;
impl Solution {
pub fn find_neighbors(word: &String, visited: &HashSet<String>, bank: &HashSet<String>) -> Vec<String> {
let chars = word.chars().collect::<Vec<_>>();
let mut results: Vec<String> = vec![];
for i in 0..chars.len() {
let ch = chars[i];
for new_ch in ['A', 'C', 'G', 'T'] {
if ch == new_ch {
continue;
}
let mut new_chars = chars.clone();
new_chars[i] = new_ch;
let s = new_chars.iter().collect::<String>();
if !bank.contains(&s) || visited.contains(&s) {
continue;
}
results.push(s);
}
}
results
}

pub fn min_mutation(start: String, end: String, bank: Vec<String>) -> i32 {
let bank = bank.into_iter().collect::<HashSet<_>>();
let mut q: VecDeque<String> = VecDeque::new();
q.push_back(start);
let mut step = 0;
let mut visited: HashSet<String> = HashSet::new();
while !q.is_empty() {
let mut next_q: VecDeque<String> = VecDeque::new();
while !q.is_empty() {
let seq = q.pop_front().unwrap();
if &seq == &end {
return step;
}
let neighbors = Self::find_neighbors(&seq, &visited, &bank);
for neighbor in neighbors {
visited.insert(neighbor.clone());
next_q.push_back(neighbor.clone());
}
}
q = next_q;
step += 1;
}
-1
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_433() {
assert_eq!(Solution::min_mutation("AACCGGTT".to_string(), "AACCGGTA".to_string(), vec_string!["AACCGGTA"]), 1);
assert_eq!(Solution::min_mutation("AACCGGTT".to_string(), "AAACGGTA".to_string(), vec_string!["AACCGGTA","AACCGCTA","AAACGGTA"]), 2);
assert_eq!(Solution::min_mutation("AAAAACCC".to_string(), "AACCCCCC".to_string(), vec_string!["AAAACCCC","AAACCCCC","AACCCCCC"]), 3);
}
}

```
