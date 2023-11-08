---
title: 1926. nearest exit from entrance in maze
date: '2022-08-30'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1926 nearest exit from entrance in maze
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1926}/>
 

  You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance <TeX>=</TeX> [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

  In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

  Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/06/04/nearest1-grid.jpg)

 >   Input: maze <TeX>=</TeX> [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance <TeX>=</TeX> [1,2]

 >   Output: 1

 >   Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].

 >   Initially, you are at the entrance cell [1,2].

 >   - You can reach [1,0] by moving 2 steps left.

 >   - You can reach [0,2] by moving 1 step up.

 >   It is impossible to reach [2,3] from the entrance.

 >   Thus, the nearest exit is [0,2], which is 1 step away.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg)

 >   Input: maze <TeX>=</TeX> [["+","+","+"],[".",".","."],["+","+","+"]], entrance <TeX>=</TeX> [1,0]

 >   Output: 2

 >   Explanation: There is 1 exit in this maze at [1,2].

 >   [1,0] does not count as an exit since it is the entrance cell.

 >   Initially, you are at the entrance cell [1,0].

 >   - You can reach [1,2] by moving 2 steps right.

 >   Thus, the nearest exit is [1,2], which is 2 steps away.

  

 >   Example 3:

 >   ![](https://assets.leetcode.com/uploads/2021/06/04/nearest3-grid.jpg)

 >   Input: maze <TeX>=</TeX> [[".","+"]], entrance <TeX>=</TeX> [0,0]

 >   Output: -1

 >   Explanation: There are no exits in this maze.

  

   

  **Constraints:**

  

 >   	maze.length <TeX>=</TeX><TeX>=</TeX> m

 >   	maze[i].length <TeX>=</TeX><TeX>=</TeX> n

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 100

 >   	maze[i][j] is either '.' or '+'.

 >   	entrance.length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> entrancerow < m

 >   	0 <TeX>\leq</TeX> entrancecol < n

 >   	entrance will always be an empty cell.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
impl Solution {
    pub fn nearest_exit(maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        let rows = maze.len();
        let cols = maze[0].len();
        let x = entrance[0]  as usize;
        let y = entrance[1] as usize;
        let mut visited: Vec<Vec<bool>> = vec![vec![false; cols]; rows];
        visited[x][y] = true;
        let mut q: VecDeque<(usize, usize, usize)> = VecDeque::new();
        q.push_back((x, y, 0));
        while !q.is_empty() {
            let (row, col, level) = q.pop_front().unwrap();
            let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
                .map(|&(dx, dy)| (dx + row as i32, dy + col as i32))
                .filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32)
                .filter(|&(x, y)| !visited[x as usize][y as usize] && maze[x as usize][y as usize] == '.')
                .collect::<Vec<_>>();
            for i in 0..neighbors.len() {
                let (x, y) = neighbors[i];
                if x == 0 || y == 0 || x == rows as i32 - 1 || y == cols as i32 - 1 {
                    return level as i32 + 1;
                }
                visited[x as usize][y as usize] = true;
                q.push_back((x as usize, y as usize, level + 1));
            } 
        }
        -1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1926() {
        assert_eq!(Solution::nearest_exit(vec![
            vec!['+','+','.','+'],
            vec!['.','.','.','+'],
            vec!['+','+','+','.']], 
        vec![1, 2]), 1);
    }
}

```
