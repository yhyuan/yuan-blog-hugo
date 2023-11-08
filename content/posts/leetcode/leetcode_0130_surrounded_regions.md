---
title: 130. surrounded regions
date: '2021-09-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0130 surrounded regions
---

 

  Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

  A region is captured by flipping all 'O's into 'X's in that surrounded region.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

 >   Input: board <TeX>=</TeX> [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

 >   Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

 >   Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

  

 >   Example 2:

  

 >   Input: board <TeX>=</TeX> [["X"]]

 >   Output: [["X"]]

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> board.length

 >   	n <TeX>=</TeX><TeX>=</TeX> board[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 200

 >   	board[i][j] is 'X' or 'O'.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn dfs(i: usize, j: usize, board: &mut Vec<Vec<char>>, states: &mut Vec<Vec<bool>>) {
        let rows = board.len();
        let cols = board[0].len();
        states[i][j] = true;
        //let options: Vec<(usize, usize)> = vec![];
        //let mut candidates: Vec<(usize, usize)> = vec![];
        let i = i as i32;
        let j = j as i32;
        let rows = rows as i32;
        let cols = cols as i32;
        let coors = vec![(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)];
        let mut coordinates:Vec<&(i32, i32)> = coors.iter()
            .filter(|&coor| coor.0 >= 0 && coor.0 < rows && coor.1 >= 0 && coor.1 < cols)
            .filter(|&coor| board[coor.0 as usize][coor.1 as usize] == 'O')
            .filter(|&coor| !states[coor.0 as usize][coor.1  as usize])
            .collect();
        for &&coor in coordinates.iter() {
            let (i, j) = coor;
            Solution::dfs(i as usize, j as usize, board, states);
        }
    }

    pub fn solve(board: &mut Vec<Vec<char>>) {
        let rows = board.len();
        if rows == 0 {
            panic!("Wrong input.");
        }
        let cols = board[0].len();
        if cols == 0 {
            panic!("Wrong input.");
        }
        if rows == 1 {
            return;
        }
        if cols == 1 {
            return;
        }
        let mut states: Vec<Vec<bool>> = vec![vec![false; cols]; rows];

        let coordinates: Vec<(usize, usize)> = (0usize..rows).into_iter()
            .filter(|&i| board[i][0] == 'O').map(|i| (i, 0))
            .chain((0usize..rows).into_iter().filter(|&i| board[i][cols-1] == 'O').map(|i| (i, cols-1)))
            .chain((1usize..cols-1).into_iter().filter(|&j| board[0][j] == 'O').map(|j| (0, j)))
            .chain((1usize..cols-1).into_iter().filter(|&j| board[rows-1][j] == 'O').map(|j| (rows - 1, j)))
            .collect();
        for &coor in coordinates.iter() {
            let (i, j) = coor;
            if !states[i][j] {
                Solution::dfs(i, j, board, &mut states);
            }
        }
        for i in 0..rows {
            for j in 0..cols {
                if states[i][j] {
                    board[i][j] = 'O';
                } else {
                    board[i][j] = 'X';
                }
            }
        }
        //println!("coorindates: {:?}", coordinates);
    }
}
*/
use std::collections::HashSet;
impl Solution {
    pub fn dfs(board: &Vec<Vec<char>>, visited: &mut Vec<Vec<bool>>, i: usize, j: usize) {
        let m = board.len();
        let n = board[0].len();
        visited[i][j] = true;
        let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].into_iter()
            .map(|(dx, dy)| (i as i32 + dx, j as i32 + dy))
            .filter(|&(x, y)| x >= 0 && y >= 0 && x < m as i32 && y < n as i32 && !visited[x as usize][y as usize])
            .map(|(x, y)| (x as usize, y as usize))
            .collect::<Vec<_>>();
        for k in 0..neighbors.len() {
            let (new_i, new_j) = neighbors[k];
            Self::dfs(&board, visited, new_i, new_j);
        }
    }
    pub fn solve(board: &mut Vec<Vec<char>>) {
        let m = board.len();
        let n = board[0].len();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
        for i in 0..m {
            for j in 0..n {
                visited[i][j] = board[i][j] == 'X';
            }
        }
        let boundary_cells = (0..n).into_iter().filter(|&j| board[0][j] == 'O').map(|j| (0, j))
            .chain((0..n).into_iter().filter(|&j| board[m - 1][j] == 'O').map(|j| (m - 1, j)))
            .chain((0..m).into_iter().filter(|&i| board[i][0] == 'O').map(|i| (i, 0)))
            .chain((0..m).into_iter().filter(|&i| board[i][n - 1] == 'O').map(|i| (i, n - 1)))
            .collect::<HashSet<_>>();
        for &(x, y) in boundary_cells.iter() {
            if !visited[x][y] {
                Self::dfs(&board, &mut visited, x, y);
            }
        }
        for i in 0..m {
            for j in 0..n {
                if !visited[i][j] {
                    board[i][j] = 'X';
                }
            }
        }
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_130() {
        let mut matrix = vec![
            vec!['X', 'X', 'X', 'X'],
            vec!['X', 'O', 'O', 'X'],
            vec!['X', 'X', 'O', 'X'],
            vec!['X', 'O', 'X', 'X'],
        ];
        Solution::solve(&mut matrix);
        assert_eq!(
            matrix,
            vec![
                vec!['X', 'X', 'X', 'X'],
                vec!['X', 'X', 'X', 'X'],
                vec!['X', 'X', 'X', 'X'],
                vec!['X', 'O', 'X', 'X'],
            ]
        );
        
        let mut matrix = vec![
            vec!['X', 'X', 'X', 'X'],
            vec!['X', 'O', 'O', 'X'],
            vec!['X', 'O', 'O', 'X'],
            vec!['X', 'X', 'X', 'X'],
        ];
        Solution::solve(&mut matrix);
        assert_eq!(
            matrix,
            vec![
                vec!['X', 'X', 'X', 'X'],
                vec!['X', 'X', 'X', 'X'],
                vec!['X', 'X', 'X', 'X'],
                vec!['X', 'X', 'X', 'X'],
            ]
        );

        let mut matrix = vec![
            vec!['X', 'X', 'X', 'X'],
            vec!['O', 'X', 'O', 'X'],
            vec!['O', 'X', 'O', 'X'],
            vec!['X', 'O', 'X', 'X'],
        ];
        Solution::solve(&mut matrix);
        assert_eq!(
            matrix,
            vec![
                vec!['X', 'X', 'X', 'X'],
                vec!['O', 'X', 'X', 'X'],
                vec!['O', 'X', 'X', 'X'],
                vec!['X', 'O', 'X', 'X'],
            ]
        );

        let mut matrix = vec![
            vec!['X', 'X', 'X', 'X', 'O', 'X'],
            vec!['O', 'X', 'X', 'O', 'O', 'X'],
            vec!['X', 'O', 'X', 'O', 'O', 'O'],
            vec!['X', 'O', 'O', 'O', 'X', 'O'],
            vec!['O', 'O', 'X', 'X', 'O', 'X'],
            vec!['X', 'O', 'X', 'O', 'X', 'X'],
        ];
        Solution::solve(&mut matrix);
        assert_eq!(
            matrix,
            vec![
                vec!['X', 'X', 'X', 'X', 'O', 'X'],
                vec!['O', 'X', 'X', 'O', 'O', 'X'],
                vec!['X', 'O', 'X', 'O', 'O', 'O'],
                vec!['X', 'O', 'O', 'O', 'X', 'O'],
                vec!['O', 'O', 'X', 'X', 'X', 'X'],
                vec!['X', 'O', 'X', 'O', 'X', 'X'],
            ]
        );

        let mut matrix = vec![
            vec![
                'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                'X', 'X', 'X', 'X',
            ],
            vec![
                'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X',
                'X', 'X', 'X', 'X',
            ],
            vec![
                'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'X',
                'X', 'X', 'X', 'X',
            ],
            vec![
                'X', 'X', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X',
                'X', 'X', 'X', 'X',
            ],
            vec![
                'X', 'X', 'X', 'X', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X',
                'X', 'X', 'X', 'X',
            ],
            vec![
                'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                'X', 'X', 'X', 'X',
            ],
        ];
        Solution::solve(&mut matrix);
        assert_eq!(
            matrix,
            vec![
                vec![
                    'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X'
                ],
                vec![
                    'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X'
                ],
                vec![
                    'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X'
                ],
                vec![
                    'X', 'X', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X',
                    'X', 'X', 'X', 'X'
                ],
                vec![
                    'X', 'X', 'X', 'X', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X'
                ],
                vec![
                    'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                    'X', 'X', 'X', 'X'
                ]
            ]
        );
        
    }
}

```
