---
title: 2018. check if word can be placed in crossword
date: '2022-09-04'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2018 check if word can be placed in crossword
---


You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.



A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:



It does not occupy a cell containing the character '#'.

The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.

There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.

There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.

Given a string word, return true if word can be placed in board, or false otherwise.







> Example 1:
> Input: board <TeX>=</TeX> [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word <TeX>=</TeX> "abc"
> Output: true
> Explanation: The word "abc" can be placed as shown above (top to bottom).
> Example 2:
> Input: board <TeX>=</TeX> [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word <TeX>=</TeX> "ac"
> Output: false
> Explanation: It is impossible to place the word because there will always be a space/letter above or below it.
> Example 3:
> Input: board <TeX>=</TeX> [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word <TeX>=</TeX> "ca"
> Output: true
> Explanation: The word "ca" can be placed as shown above (right to left).
**Constraints:**
> m <TeX>=</TeX><TeX>=</TeX> board.length
> n <TeX>=</TeX><TeX>=</TeX> board[i].length
> 1 <TeX>\leq</TeX> m  n <TeX>\leq</TeX> 2  105
> board[i][j] will be ' ', '#', or a lowercase English letter.
> 1 <TeX>\leq</TeX> word.length <TeX>\leq</TeX> max(m, n)
> word will contain only lowercase English letters.


## Solution


### Rust
```rust
pub struct Solution {}

// problem: https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
// discuss: https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/discuss/?currentPage=1&orderBy=most_votes&query=
use std::collections::HashMap;
impl Solution {
pub fn calculate_space_hashmap(board: &Vec<Vec<char>>) -> HashMap<usize, Vec<((usize, usize), (usize, usize))>> {
let mut hashmap: HashMap<usize, Vec<((usize, usize), (usize, usize))>> = HashMap::new(); // space length is key
// space starting and ending coordinates are the values.
let m = board.len();
let n = board[0].len();
//search horizontal spaces
for i in 0..m {
//let mut in_space = false;
let mut space_start_index = usize::MAX;
for j in 0..n {
if board[i][j] != '#' {
if space_start_index == usize::MAX {
space_start_index = j;
}
} else {
if space_start_index != usize::MAX {
//(i, space_start_index) => (i, j - 1)
let length = j - space_start_index;
if hashmap.contains_key(&length) {
hashmap.get_mut(&length).unwrap().push(((i, space_start_index), (i, j - 1)));
} else {
hashmap.insert(length, vec![((i, space_start_index), (i, j - 1))]);
}
space_start_index = usize::MAX;
}
}
}
if space_start_index != usize::MAX {
//(i, space_start_index) => (i, n - 1)
let length = n - space_start_index;
if hashmap.contains_key(&length) {
hashmap.get_mut(&length).unwrap().push(((i, space_start_index), (i, n - 1)));
} else {
hashmap.insert(length, vec![((i, space_start_index), (i, n - 1))]);
}
}
}

//search vertical spaces
for i in 0..n {
let mut space_start_index = usize::MAX;
for j in 0..m {
if board[j][i] != '#' {
if space_start_index == usize::MAX {
space_start_index = j;
}
} else {
if space_start_index != usize::MAX {
//(space_start_index, i) => (j - 1, i)
let length = j - space_start_index;
if hashmap.contains_key(&length) {
hashmap.get_mut(&length).unwrap().push(((space_start_index, i), (j - 1, i)));
} else {
hashmap.insert(length, vec![((space_start_index, i), (j - 1, i))]);
}
space_start_index = usize::MAX;
}
}
}
if space_start_index != usize::MAX {
//(space_start_index, i) => (m - 1, i)
let length = m - space_start_index;
if hashmap.contains_key(&length) {
hashmap.get_mut(&length).unwrap().push(((space_start_index, i), (m - 1, i)));
} else {
hashmap.insert(length, vec![((space_start_index, i), (m - 1, i))]);
}
}
}

hashmap
}

pub fn place_word_in_crossword(board: Vec<Vec<char>>, word: String) -> bool {
let hashmap: HashMap<usize, Vec<((usize, usize), (usize, usize))>> = Self::calculate_space_hashmap(&board);
//println!("hashmap: {:?}", hashmap);
let n = word.len();
if !hashmap.contains_key(&n) {
return false;
}
let spaces = &hashmap[&n];
let chars: Vec<char> = word.chars().collect();
for i in 0..spaces.len() {
let ((x1, y1), (x2, y2)) = spaces[i];
let mut success = true;
if x1 == x2 { // horizontal
for i in 0..chars.len() {
if board[x1][y1 + i] != ' ' && board[x1][y1 + i] != chars[i] {
success = false;
break;
}
}
if !success {
success = true;
for i in 0..chars.len() {
if board[x1][y2 - i] != ' ' && board[x1][y2 - i] != chars[i] {
success = false;
break;
}
}
}
} else { // vertical
for i in 0..chars.len() {
if board[x1 + i][y1] != ' ' && board[x1 + i][y1] != chars[i] {
success = false;
break;
}
}
if !success {
success = true;
for i in 0..chars.len() {
if board[x2 - i][y1] != ' ' && board[x2 - i][y1] != chars[i] {
success = false;
break;
}
}
}
}
if success {
return true;
}
}
false
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_2018() {
assert_eq!(Solution::place_word_in_crossword(vec![vec!['#', ' ', '#'], vec!['#', ' ', '#'], vec!['#', ' ', 'c']], "ca".to_string()), true);
//assert_eq!(Solution::place_word_in_crossword(vec![vec!['#', ' ', '#'], vec![' ', ' ', '#'], vec!['#', ' ', 'c']], "abc".to_string()), true);
//assert_eq!(Solution::place_word_in_crossword(vec![vec![' ', '#', 'a'], vec![' ', '#', 'c'], vec![' ', '#', 'a']], "ac".to_string()), false);
//assert_eq!(Solution::place_word_in_crossword(vec![vec!['#', ' ', '#'], vec![' ', ' ', '#'], vec!['#', ' ', 'c']], "ca".to_string()), true);
}
}

```
