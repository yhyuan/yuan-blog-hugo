---
title: 529. minesweeper
date: '2022-03-27'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0529 minesweeper
---

 

  Let's play the minesweeper game ([Wikipedia](https://en.wikipedia.org/wiki/Minesweeper_(video_game)), [online game](http://minesweeperonline.com))!

  You are given an m x n char matrix board representing the game board where:

  

  	'M' represents an unrevealed mine,

  	'E' represents an unrevealed empty square,

  	'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),

  	digit ('1' to '8') represents how many mines are adjacent to this revealed square, and

  	'X' represents a revealed mine.

  

  You are also given an integer array click where click <TeX>=</TeX> [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

  Return the board after revealing this position according to the following rules:

  <ol>

  	If a mine 'M' is revealed, then the game is over. You should change it to 'X'.

  	If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.

  	If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.

  	Return the board when no more squares will be revealed.

  </ol>

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_1.png)

 >   Input: board <TeX>=</TeX> [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click <TeX>=</TeX> [3,0]

 >   Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_2.png)

 >   Input: board <TeX>=</TeX> [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click <TeX>=</TeX> [1,2]

 >   Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> board.length

 >   	n <TeX>=</TeX><TeX>=</TeX> board[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 50

 >   	board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.

 >   	click.length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> clickr < m

 >   	0 <TeX>\leq</TeX> clickc < n

 >   	board[clickr][clickc] is either 'M' or 'E'.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn calculate_neighbors_mine(board: &Vec<Vec<char>>, row: usize, col: usize) -> Vec<(usize, usize)> {
        let rows = board.len();
        let cols = board[0].len();
        let neighbors = Solution::calculate_neighbors(rows, cols, row, col);
        let neighbors_mine = neighbors
            .into_iter()
            .filter(|n| board[n.0][n.1] == 'M')
            .collect::<Vec<_>>();                
        return neighbors_mine;
    }

    pub fn calculate_neighbors(rows: usize, cols: usize, row: usize, col: usize) -> Vec<(usize, usize)> {
        // let mut count = 0;
        let row = row as i32;
        let col = col as i32;
        let mut neighbors: Vec<(usize, usize)> = vec![];
        for i in -1..=1 {
            if row + i >= 0 && row + i < rows as i32 {
                for j in -1..=1 {
                    if col + j >= 0 && col + j < cols as i32 {
                        if i == 0 && j == 0 {
                            continue;
                        }
                        neighbors.push(((row + i) as usize, (col + j) as usize));
                        /*
                        if board[(row + i) as usize][(col + j) as usize] == 'M' {
                            count += 1;
                        }
                        */
                    }                    
                }
            }
        }
        neighbors
    }

    pub fn update_board(board: Vec<Vec<char>>, click: Vec<i32>) -> Vec<Vec<char>> {
        let mut board = board;
        let row = click[0] as usize;
        let col = click[1] as usize;
        if board[row][col] == 'M' {
            board[row][col] = 'X';
            return board;
        }
        if board[row][col] == 'E' {
            let neighbors_mine = Solution::calculate_neighbors_mine(&board, row, col);
            // println!("neighbors_mine.len(): {}", neighbors_mine.len());
            if neighbors_mine.len() > 0 {
                board[row][col] = std::char::from_digit(neighbors_mine.len() as u32, 10).unwrap();
                return board;
            }
            let rows = board.len();
            let cols = board[0].len();    
            let mut visited = vec![vec![false; cols]; rows];
            let mut stack: Vec<(usize, usize)> = vec![];
            stack.push((row, col));
            while stack.len() > 0 {
                let coor = stack.pop().unwrap();
                // println!("coor: {}, {}", coor.0, coor.1);
                let row = coor.0;
                let col = coor.1;
                board[row][col] = 'B';
                visited[row][col] = true;
                let neighbors = Solution::calculate_neighbors(rows, cols, row, col);
                // println!("neighbors.len(): {}", neighbors.len());
                for neighbor in neighbors {
                    let neighbors_mine = Solution::calculate_neighbors_mine(&board, neighbor.0, neighbor.1);
                    if neighbors_mine.len() > 0 {
                        board[neighbor.0][neighbor.1] = std::char::from_digit(neighbors_mine.len() as u32, 10).unwrap();
                    } else {
                        if !visited[neighbor.0][neighbor.1] {
                            stack.push(neighbor);
                        }
                    }
                }
            }
        }
        board
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_529() {
        assert_eq!(Solution::update_board(
            vec![
                vec!['E','E','E','E','E'],
                vec!['E','E','M','E','E'],
                vec!['E','E','E','E','E'],
                vec!['E','E','E','E','E']], 
            vec![3, 0]), 
            vec![
                vec!['B','1','E','1','B'],
                vec!['B','1','M','1','B'],
                vec!['B','1','1','1','B'],
                vec!['B','B','B','B','B']]
        );
        assert_eq!(Solution::update_board(
            vec![
                vec!['B','1','E','1','B'],
                vec!['B','1','M','1','B'],
                vec!['B','1','1','1','B'],
                vec!['B','B','B','B','B']], 
            vec![1, 2]), 
            vec![
                vec!['B','1','E','1','B'],
                vec!['B','1','X','1','B'],
                vec!['B','1','1','1','B'],
                vec!['B','B','B','B','B']]
        );
    }
}

```
