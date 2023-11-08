---
title: 1091. shortest path in binary matrix
date: '2022-07-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1091 shortest path in binary matrix
---

 

  Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

  A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

  

  	All the visited cells of the path are 0.

  	All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

  

  The length of a clear path is the number of visited cells of this path.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)

 >   Input: grid <TeX>=</TeX> [[0,1],[1,0]]

 >   Output: 2

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)

 >   Input: grid <TeX>=</TeX> [[0,0,0],[1,1,0],[1,1,0]]

 >   Output: 4

  

 >   Example 3:

  

 >   Input: grid <TeX>=</TeX> [[1,0,0],[1,1,0],[1,1,0]]

 >   Output: -1

  

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> grid.length

 >   	n <TeX>=</TeX><TeX>=</TeX> grid[i].length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100

 >   	grid[i][j] is 0 or 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
impl Solution {
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        if grid[0][0] != 0 {
            return -1;
        }
        let mut visited: Vec<Vec<bool>> = vec![vec![false;cols]; rows];
        let mut q: VecDeque<(usize, usize, usize)> = VecDeque::new();
        q.push_back((0, 0, 1));
        while !q.is_empty() {
            let (row, col, level) = q.pop_front().unwrap();
            if row == rows - 1 && col == cols - 1 {
                return level as i32;
            }
            let diffs = vec![(-1, -1), (-1, 0), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)];
            for i in 0..diffs.len() {
                let (dx, dy) = diffs[i];
                let (x, y) = (dx + row as i32, dy + col as i32);
                if x < 0 || y < 0 || x >= rows as i32 || y >= cols as i32 || grid[x as usize][y as usize] == 1 || visited[x as usize][y as usize] {
                    continue;
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
    fn test_1091() {
        assert_eq!(Solution::shortest_path_binary_matrix(vec![vec![0,1],vec![1,0]]), 2);
        assert_eq!(Solution::shortest_path_binary_matrix(vec![vec![0,0,0],vec![1,1,0],vec![1,1,0]]), 4);
        assert_eq!(Solution::shortest_path_binary_matrix(vec![vec![1,0,0],vec![1,1,0],vec![1,1,0]]), -1);
        assert_eq!(Solution::shortest_path_binary_matrix(vec![vec![0,1],vec![0,0]]), 2);
    }
}

```
