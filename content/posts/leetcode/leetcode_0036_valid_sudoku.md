---
title: 36. valid sudoku
date: '2021-06-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0036 valid sudoku
---



Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

<ol>

Each row must contain the digits 1-9 without repetition.

Each column must contain the digits 1-9 without repetition.

Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

</ol>

Note:



A Sudoku board (partially filled) could be valid but is not necessarily solvable.

Only the filled cells need to be validated according to the mentioned rules.





>   Example 1:
>   ![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
>   Input: board <TeX>=</TeX>
>   [["5","3",".",".","7",".",".",".","."]
>   ,["6",".",".","1","9","5",".",".","."]
>   ,[".","9","8",".",".",".",".","6","."]
>   ,["8",".",".",".","6",".",".",".","3"]
>   ,["4",".",".","8",".","3",".",".","1"]
>   ,["7",".",".",".","2",".",".",".","6"]
>   ,[".","6",".",".",".",".","2","8","."]
>   ,[".",".",".","4","1","9",".",".","5"]
>   ,[".",".",".",".","8",".",".","7","9"]]
>   Output: true
>   Example 2:
>   Input: board <TeX>=</TeX>
>   [["8","3",".",".","7",".",".",".","."]
>   ,["6",".",".","1","9","5",".",".","."]
>   ,[".","9","8",".",".",".",".","6","."]
>   ,["8",".",".",".","6",".",".",".","3"]
>   ,["4",".",".","8",".","3",".",".","1"]
>   ,["7",".",".",".","2",".",".",".","6"]
>   ,[".","6",".",".",".",".","2","8","."]
>   ,[".",".",".","4","1","9",".",".","5"]
>   ,[".",".",".",".","8",".",".","7","9"]]
>   Output: false
>   Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
**Constraints:**
>   	board.length <TeX>=</TeX><TeX>=</TeX> 9
>   	board[i].length <TeX>=</TeX><TeX>=</TeX> 9
>   	board[i][j] is a digit or '.'.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
//use std::collections::HashMap;
impl Solution {
pub fn is_valid(row: &Vec<char>) -> bool {
let mut states = [false; 9];
for &ch in row.iter() {
if ch == '.' {
continue;
}
let index = ch.to_digit(10).unwrap() as usize - 1;
if states[index] {
return false;
} else {
states[index] = true;
}
}
true
}
pub fn calculate_square_coors(i: usize) -> Vec<(usize, usize)> {
let div = (i / 3) * 3;
let remain = (i % 3) * 3;
let mut coors: Vec<(usize, usize)> = Vec::with_capacity(9);
for i in 0..3usize {
for j in 0..3usize {
coors.push((remain + i, div + j));
}
}
coors
}
pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
let n = board.len();
if n != 9 {
panic!("Wrong input");
}
for i in 0..9 {
//let row = board[i].iter().filter(|&ch| ch != '.').collect();
if !Solution::is_valid(&board[i]) {
return false;
}
}
for j in 0..9 {
let row: Vec<char> = (0..9usize).into_iter().map(|i| board[i][j]).collect();
if !Solution::is_valid(&row) {
return false;
}
}
for i in 0..9 {
let coors: Vec<(usize, usize)> = Solution::calculate_square_coors(i);
let row: Vec<char> = coors.iter().map(|coor| board[coor.0][coor.1]).collect();
if !Solution::is_valid(&row) {
return false;
}
}
true
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_36() {

assert_eq!(
Solution::is_valid_sudoku(vec![
vec!['8', '3', '.', '.', '7', '.', '.', '.', '.'],
vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]),
false
);

assert_eq!(
Solution::is_valid_sudoku(vec![
vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'],
vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
vec!['.', '.', '.', '.', '8', '.', '.', '7', '9']
]),
true
);

}
}

```
