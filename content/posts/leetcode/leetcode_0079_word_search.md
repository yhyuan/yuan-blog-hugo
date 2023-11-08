---
title: 79. word search
date: '2021-07-19'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0079 word search
---



Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)
>   Input: board <TeX>=</TeX> [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word <TeX>=</TeX> "ABCCED"
>   Output: true
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)
>   Input: board <TeX>=</TeX> [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word <TeX>=</TeX> "SEE"
>   Output: true
>   Example 3:
>   ![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)
>   Input: board <TeX>=</TeX> [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word <TeX>=</TeX> "ABCB"
>   Output: false
**Constraints:**
>   	m <TeX>=</TeX><TeX>=</TeX> board.length
>   	n <TeX>=</TeX> board[i].length
>   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 6
>   	1 <TeX>\leq</TeX> word.length <TeX>\leq</TeX> 15
>   	board and word consists of only lowercase and uppercase English letters.
>   Follow up: Could you use search pruning to make your solution faster with a larger board?


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
pub fn find_start_positions(board: &Vec<Vec<char>>, first_char: char) -> Vec<(usize, usize)> {
let m = board.len();
let n = board[0].len();
let mut coors: Vec<(usize, usize)> = vec![];
for i in 0..m {
for j in 0..n {
if board[i][j] == first_char {
coors.push((i, j));
}
}
}
coors
}
pub fn find_next_positions(board: &Vec<Vec<char>>, explored_positions: &mut Vec<Vec<bool>>, word_chars: &Vec<char>, word_index: usize, pos: (usize, usize)) -> Vec<(usize, usize)> {
let m = board.len();
let n = board[0].len();
let (i, j) = pos;
let i = i as i32;
let j = j as i32;
let positions = vec![(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)];
let positions: Vec<(usize, usize)> = positions.iter()
.filter(|&&pos| pos.0 >= 0 && pos.0 < m as i32 && pos.1 >= 0 && pos.1 < n as i32)
.map(|&pos| (pos.0 as usize, pos.1 as usize))
.filter(|&pos| !explored_positions[pos.0][pos.1])
.filter(|&pos| board[pos.0][pos.1] == word_chars[word_index + 1])
.collect();
positions
}
pub fn find_word_chars_helper(board: &Vec<Vec<char>>, explored_positions: &mut Vec<Vec<bool>>, word_chars: &Vec<char>, word_index: usize, pos: (usize, usize)) -> bool {
//println!("pos: {:?}", pos);
let (i, j) = pos;
if word_index == word_chars.len() - 1 {
return board[i][j] == word_chars[word_index];
}
if board[i][j] != word_chars[word_index] {
return false;
}
explored_positions[i][j] = true;
let next_positions = Solution::find_next_positions(board, explored_positions, word_chars, word_index, pos);
if next_positions.len() == 0 {
explored_positions[i][j] = false;
return false;
}
for &position in next_positions.iter() {
let result = Solution::find_word_chars_helper(board, explored_positions, word_chars, word_index + 1, position);
if result {
explored_positions[i][j] = false;
return true;
}
}
explored_positions[i][j] = false;
false
}
pub fn find_word_chars(board: &Vec<Vec<char>>, word_chars: &Vec<char>, pos: (usize, usize)) -> bool {
let m = board.len();
let n = board[0].len();
let mut explored_positions: Vec<Vec<bool>> = vec![vec![false; n]; m];
Solution::find_word_chars_helper(board, &mut &mut explored_positions, word_chars, 0, pos)
}
pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
let word_chars: Vec<char> = word.chars().collect();
if word_chars.len() == 0 {
return true;
}
let m = board.len();
let n = board[0].len();
let first_char = word_chars[0];
let start_positions = Solution::find_start_positions(&board, first_char);
//println!("start: {:?}", start_positions);
let success = start_positions.iter().find(|&&coor| Solution::find_word_chars(&board, &word_chars, coor));
success.is_some()
}
}
*/
impl Solution {
pub fn helper(board: &Vec<Vec<char>>, chars: &Vec<char>, visited: &mut Vec<Vec<bool>>, i: usize, j: usize, k: usize) -> bool {
if chars.len() == k {
return true;
}
visited[i][j] = true;
let m = board.len();
let n = board[0].len();
let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].into_iter()
.map(|(dx, dy)| (i as i32 + dx, j as i32 + dy))
.filter(|&(x, y)| x >= 0 && y >= 0 && x < m as i32 && y < n as i32 && board[x as usize][y as usize] == chars[k] && !visited[x as usize][y as usize])
.collect::<Vec<_>>();
for i in 0..neighbors.len() {
let (new_i, new_j) = neighbors[i];
if Self::helper(board, chars, visited, new_i as usize, new_j as usize, k + 1) {
return true;
}
}
visited[i][j] = false;
false
}
pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
let chars = word.chars().collect::<Vec<_>>();
let m = board.len();
let n = board[0].len();
for i in 0..m {
for j in 0..n {
if board[i][j] == chars[0] {
let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
if Self::helper(&board, &chars, &mut visited, i, j, 1) {
return true;
}
}
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
fn test_79() {
assert_eq!(Solution::exist(vec![vec!['a']], "a".to_owned()), true);
assert_eq!(
Solution::exist(
vec![
vec!['A', 'B', 'C', 'E'],
vec!['S', 'F', 'C', 'S'],
vec!['A', 'D', 'E', 'E'],
],
"ABCCED".to_owned()
),
true
);
assert_eq!(
Solution::exist(
vec![
vec!['A', 'B', 'C', 'E'],
vec!['S', 'F', 'C', 'S'],
vec!['A', 'D', 'E', 'E'],
],
"SEE".to_owned()
),
true
);

assert_eq!(
Solution::exist(
vec![
vec!['A', 'B', 'C', 'E'],
vec!['S', 'F', 'C', 'S'],
vec!['A', 'D', 'E', 'E'],
],
"ABCB".to_owned()
),
false
);
assert_eq!(
Solution::exist(
vec![
vec!['A', 'B', 'C', 'E'],
vec!['S', 'F', 'E', 'S'],
vec!['A', 'D', 'E', 'E'],
],
"ABCESEEEFS".to_owned()
),
true
);

}
}

```
