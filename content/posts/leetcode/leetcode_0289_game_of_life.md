---
title: 289. game of life
date: '2021-12-19'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0289 game of life
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={289}/>
 

  According to [Wikipedia"s article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

  The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

  <ol>

  	Any live cell with fewer than two live neighbors dies as if caused by under-population.

  	Any live cell with two or three live neighbors lives on to the next generation.

  	Any live cell with more than three live neighbors dies, as if by over-population.

  	Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

  </ol>

  <span>The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.</span>

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg)

 >   Input: board <TeX>=</TeX> [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

 >   Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg)

 >   Input: board <TeX>=</TeX> [[1,1],[1,0]]

 >   Output: [[1,1],[1,1]]

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> board.length

 >   	n <TeX>=</TeX><TeX>=</TeX> board[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 25

 >   	board[i][j] is 0 or 1.

  

   

 >   Follow up:

  

 >   	Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.

 >   	In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn calculate_neighbors(board: &Vec<Vec<i32>>, i: usize, j: usize) -> usize {
        let m = board.len() as i32;
        let n = board[0].len() as i32;
        let neighbors: Vec<(i32, i32)> = vec![(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)];
        let neighbors_count = neighbors.iter()
            .map(|&delta|(i as i32 + delta.0, j as i32 + delta.1))
            .filter(|&coor| (coor.0 >= 0) && (coor.0 <= m - 1) &&(coor.1 >= 0) && (coor.1 <= n - 1))
            .map(|coor| (coor.0 as usize, coor.1 as usize))
            .filter(|coor| board[coor.0][coor.1] == 1).count();
        neighbors_count
    }
    pub fn calculate_next_state(curr_state: i32, neighbors_count: usize) -> i32 {
        if neighbors_count < 2 {
            return 0;
        }
        if neighbors_count == 2 {
            return curr_state;
        }
        if neighbors_count == 3 {
            return 1;
        }
        return 0;
    }
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        let clone = board.clone();
        let m = board.len();
        let n = board[0].len();
        for i in 0..m {
            for j in 0..n {
                let neighbors_count = Solution::calculate_neighbors(&clone, i, j);
                board[i][j] = Solution::calculate_next_state(board[i][j], neighbors_count);
                /*
                if board[i][j] == 0 && neighbors_count == 3 {
                    board[i][j] = 1;
                } else if board[i][j] == 1 {
                    if neighbors_count < 2 {
                        board[i][j] = 0;
                    } else if neighbors_count == 2 || neighbors_count == 3 {
                        board[i][j] = 1;
                    } else {
                        board[i][j] = 0;
                    }
                }
                */
            }
        }
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_289() {
        let mut test = vec![vec![0, 1, 0], vec![0, 0, 1], vec![1, 1, 1], vec![0, 0, 0]];
        Solution::game_of_life(&mut test);
        assert_eq!(
            test,
            vec![vec![0, 0, 0], vec![1, 0, 1], vec![0, 1, 1], vec![0, 1, 0],]
        );
    }
}

```
