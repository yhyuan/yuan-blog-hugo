---
title: 843. guess the word
date: '2022-05-27'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0843 guess the word
---



This is an interactive problem.

You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.



>   Example 1:
>   Input: secret <TeX>=</TeX> "acckzz", wordlist <TeX>=</TeX> ["acckzz","ccbazz","eiowzz","abcczz"], numguesses <TeX>=</TeX> 10
>   Output: You guessed the secret word correctly.
>   Explanation:
>   master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
>   master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
>   master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
>   master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
>   master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
>   We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
>   Example 2:
>   Input: secret <TeX>=</TeX> "hamada", wordlist <TeX>=</TeX> ["hamada","khaled"], numguesses <TeX>=</TeX> 10
>   Output: You guessed the secret word correctly.
**Constraints:**
>   	1 <TeX>\leq</TeX> wordlist.length <TeX>\leq</TeX> 100
>   	wordlist[i].length <TeX>=</TeX><TeX>=</TeX> 6
>   	wordlist[i] consist of lowercase English letters.
>   	All the strings of wordlist are unique.
>   	secret exists in wordlist.
>   	numguesses <TeX>=</TeX><TeX>=</TeX> 10


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

/**
* // This is the Master's API interface.
* // You should not implement it, or speculate about its implementation
* struct Master;
* impl Master {
*     fn guess(word:String)->int;
* };
*/

/**
* // This is the Master's API interface.
* // You should not implement it, or speculate about its implementation
* struct Master;
* impl Master {
*     fn guess(word:String)->int;
* };
*/
pub struct Master {
secret: String,
}
impl Master {
pub fn new(secret: String) -> Self {
Self {secret}
}
pub fn guess(&self, word:String)-> i32 {
let chars1: Vec<char> = word.chars().collect();
let chars2: Vec<char> = self.secret.chars().collect();
let mut ans = 0;
for i in 0..6 {
if chars1[i] == chars2[i] {
ans += 1;
}
}
ans
}
}

use rand::Rng;
impl Solution {
pub fn calculate_match(word1: &String, word2: &String) -> i32 {
let chars1: Vec<char> = word1.chars().collect();
let chars2: Vec<char> = word2.chars().collect();
let mut ans = 0;
for i in 0..6 {
if chars1[i] == chars2[i] {
ans += 1;
}
}
ans
}
pub fn find_secret_word(words: Vec<String>, master: &Master) {
let mut rng = rand::thread_rng();
//println!("Integer: {}", rng.gen_range(0..10));
let n = words.len();
let mut candidates = (0..n).into_iter().collect::<Vec<usize>>();
for i in 0..10 {
let index = rng.gen_range(0, candidates.len());
let res = master.guess(words[candidates[index]].clone());
if res == 6 {
break;
}
candidates = candidates.iter()
.filter(|&i| Self::calculate_match(&words[*i], &words[candidates[index]]) == res)
.map(|i| *i)
.collect::<Vec<_>>();
if candidates.len() == 0 {
break;
}
}
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_843() {
}
}

```
