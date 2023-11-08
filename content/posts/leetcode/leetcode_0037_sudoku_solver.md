---
title: 37. sudoku solver
date: '2021-06-07'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0037 sudoku solver
---

 

  Write a program to solve a Sudoku puzzle by filling the empty cells.

  A sudoku solution must satisfy all of the following rules:

  <ol>

  	Each of the digits 1-9 must occur exactly once in each row.

  	Each of the digits 1-9 must occur exactly once in each column.

  	Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

  </ol>

  The '.' character indicates empty cells.

   

 >   Example 1:

 >   ![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

 >   Input: board <TeX>=</TeX> [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

 >   Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

 >   Explanation: The input board is shown above and the only valid solution is shown below:

 >   ![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

  

   

  **Constraints:**

  

 >   	board.length <TeX>=</TeX><TeX>=</TeX> 9

 >   	board[i].length <TeX>=</TeX><TeX>=</TeX> 9

 >   	board[i][j] is a digit or '.'.

 >   	It is guaranteed that the input board has only one solution.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_valid_row(row: &Vec<char>) -> bool {
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
    pub fn is_valid_sudoku(board: &mut Vec<Vec<char>>) -> bool {
        //println!("board: {:?}", board);
        let n = board.len();
        if n != 9 {
            panic!("Wrong input");
        }
        for i in 0..9 {
            if !Solution::is_valid_row(&board[i]) {
                return false;
            }
        }
        for j in 0..9 {
            let row: Vec<char> = (0..9usize).into_iter().map(|i| board[i][j]).collect();
            if !Solution::is_valid_row(&row) {
                return false;
            }
        }
        for i in 0..9 {
            let coors: Vec<(usize, usize)> = Solution::calculate_square_coors(i);
            let row: Vec<char> = coors.iter().map(|coor| board[coor.0][coor.1]).collect();
            if !Solution::is_valid_row(&row) {
                return false;
            }
        }
        true
    }
    pub fn find_index(board: &mut Vec<Vec<char>>) -> usize {
        let mut dot_index = usize::MAX;
        for i in 0..81usize {
            if board[i / 9][i % 9] == '.' {
                dot_index = i;
                break;
            }
        }
        dot_index        
    }
    pub fn solve_sudoku_helper(board: &mut Vec<Vec<char>>) -> bool {
        let nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
        let dot_index = (0..81usize).into_iter().find(|i|board[i / 9][i % 9] == '.');
        if dot_index.is_none() {
            return true;
        }
        let dot_index = dot_index.unwrap();
        let mut is_solved = false;
        for i in 1..10usize {
            board[dot_index / 9][dot_index % 9] = nums[i];
            if Solution::is_valid_sudoku(board) {
                if Solution::solve_sudoku_helper(board) {
                    is_solved = true;
                    break;
                }
            }
        }
        if !is_solved {
            board[dot_index / 9][dot_index % 9] = '.';
        }
        is_solved
    }
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        Solution::solve_sudoku_helper(board);
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_37() {
        let mut board = vec![
            vec!['5','3','.','.','7','.','.','.','.'],
            vec!['6','.','.','1','9','5','.','.','.'],
            vec!['.','9','8','.','.','.','.','6','.'],
            vec!['8','.','.','.','6','.','.','.','3'],
            vec!['4','.','.','8','.','3','.','.','1'],
            vec!['7','.','.','.','2','.','.','.','6'],
            vec!['.','6','.','.','.','.','2','8','.'],
            vec!['.','.','.','4','1','9','.','.','5'],
            vec!['.','.','.','.','8','.','.','7','9']
        ];
        Solution::solve_sudoku(&mut board);
        assert_eq!(board, 
            vec![
                vec!['5','3','4','6','7','8','9','1','2'],
                vec!['6','7','2','1','9','5','3','4','8'],
                vec!['1','9','8','3','4','2','5','6','7'],
                vec!['8','5','9','7','6','1','4','2','3'],
                vec!['4','2','6','8','5','3','7','9','1'],
                vec!['7','1','3','9','2','4','8','5','6'],
                vec!['9','6','1','5','3','7','2','8','4'],
                vec!['2','8','7','4','1','9','6','3','5'],
                vec!['3','4','5','2','8','6','1','7','9']
        ]);
    }
}

```
