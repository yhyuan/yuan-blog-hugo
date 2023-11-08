---
title: 51. n queens
date: '2021-06-21'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0051 n queens
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={51}/>
 

  The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

  Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

  Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

 >   Input: n <TeX>=</TeX> 4

 >   Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

 >   Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 1

 >   Output: [["Q"]]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 9


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;

impl Solution {
    /*
    pub fn calculate_status_board(positions: &mut Vec<(usize, usize)>, n: usize) ->  Vec<Vec<bool>> {
        let mut board: Vec<Vec<bool>> = vec![vec![false; n];n];
        for &coor in positions.iter() {
            let (x, y) = coor;
            board[x][y] = true;
            for i in 0..n {
                board[x][i] = true; // x row
                board[i][y] = true; // y col
            }
            let (i, j) = (x, y);
            let mut k = 0;
            while i + k < n && j + k < n {
                board[i + k][j + k] = true;
                k += 1;
            }
            let (i, j) = (x, y);
            k = 0;
            while i >= k && j >= k {
                board[i - k][j - k] = true;
                k += 1;
            }
            let (i, j) = (x, y);
            k = 0;
            while i + k < n && j >= k {
                board[i + k][j - k] = true;
                k += 1;
            }
            let (i, j) = (x, y);
            k = 0;
            while i >= k && j + k < n {
                board[i - k][j + k] = true;
                k += 1;
            }
        }
        board
    }
    pub fn solve_n_queens_helper(positions: &mut Vec<(usize, usize)>, n: i32) -> Vec<Vec<String>> {
        let n = n as usize;
        if n == positions.len() {
            let mut board = vec![vec!['.'; n];n];
            for i in 0..n {
                let (x, y) = positions[i];
                board[x][y] = 'Q';
            }
            return vec![board.iter().map(|chars| chars.into_iter().collect()).collect()];
        }
        let status_board = Solution::calculate_status_board(positions, n);
        //println!("status: {:?}", status_board);
        let n = n as usize;
        let mut results: Vec<Vec<String>> = vec![];
        for i in 0..n {
            for j in 0..n {
                if !status_board[i][j] {
                    positions.push((i, j));
                    for r in Solution::solve_n_queens_helper(positions, n as i32) {
                        let mut is_inside = false;
                        for res in results.iter() {
                            let mut is_same = true;
                            for i in 0..r.len() {
                                if r[i] != res[i] {
                                    is_same = false;
                                    break;
                                }
                            }
                            if is_same {
                                is_inside = true;
                                break;
                            }
                        }
                        if !is_inside {
                            results.push(r);
                        }
                    }
                    positions.pop();
                }
            }
        }
        results
    }

    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let mut positions: Vec<(usize, usize)> = vec![];
        Solution::solve_n_queens_helper(&mut positions, n)
    }
    */
    pub fn solve_n_queens_helper(positions: &mut Vec<usize>) -> Vec<Vec<usize>> {
        let n = positions.len();
        let new_x = positions.iter().position(|&y| y == usize::MAX);
        if new_x.is_none() {
            return vec![positions.clone()];
        }
        let new_x = new_x.unwrap();
        let mut unsafe_coors: HashMap<usize, usize> = HashMap::with_capacity(n);
        for (x, &y) in positions.iter().enumerate() {
            if y != usize::MAX {
                unsafe_coors.insert(y, x);
                if y + new_x >= x {
                    unsafe_coors.insert(y + new_x - x, x);
                }
                if y + x >= new_x {
                    unsafe_coors.insert(y + x - new_x, x);
                }
            }
        }
        let new_ys: Vec<usize> = (0usize..n).into_iter().filter(|y| !unsafe_coors.contains_key(y)).collect();
        let mut results: Vec<Vec<usize>> = vec![];
        for &new_y in new_ys.iter() {
            positions[new_x] = new_y;
            let new_results = Solution::solve_n_queens_helper(positions);
            for result in new_results {
                results.push(result);
            }
        }
        positions[new_x] = usize::MAX;
        results
    }
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let n = n as usize;
        //let mut board: Vec<Vec<Status>> = vec![vec![Status::Safe; n]; n];
        //let mut positions: Vec<(usize, usize)> = vec![];
        let mut positions: Vec<usize> = vec![usize::MAX; n]; // (index, positions[index]) is a queen position. 
        //let mut board: Vec<Vec<bool>> = vec![vec![false; n]; n];
        let positions_list = Solution::solve_n_queens_helper(&mut positions);
        let mut results: Vec<Vec<String>> = vec![];
        for positions in positions_list.iter() {
            let mut board = vec![vec!['.'; n];n];
            for x in 0..n {
                let y = positions[x];
                board[x][y] = 'Q';
            }
            results.push(board.iter().map(|chars| chars.into_iter().collect()).collect());
        }
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_51() {
        assert_eq!(
            Solution::solve_n_queens(4),
            vec![
                vec![".Q..", "...Q", "Q...", "..Q."],
                vec!["..Q.", "Q...", "...Q", ".Q.."]
            ]
        );
        //assert_eq!(Solution::solve_n_queens(8).len(), 92);
    }
}

```
