---
title: 934. shortest bridge
date: '2022-06-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0934 shortest bridge
---

 

  In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

  Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

  Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

   

 >   Example 1:

  

 >   Input: grid <TeX>=</TeX> [[0,1],[1,0]]

 >   Output: 1

  

 >   Example 2:

  

 >   Input: grid <TeX>=</TeX> [[0,1,0],[0,0,0],[0,0,1]]

 >   Output: 2

  

 >   Example 3:

  

 >   Input: grid <TeX>=</TeX> [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

 >   Output: 1

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> grid.length <TeX>=</TeX><TeX>=</TeX> grid[0].length <TeX>\leq</TeX> 100

 >   	grid[i][j] <TeX>=</TeX><TeX>=</TeX> 0 or grid[i][j] <TeX>=</TeX><TeX>=</TeX> 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;

impl Solution {
    pub fn dfs(grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, row: usize, col: usize) {
        let rows = grid.len();
        let cols = grid[0].len();
        visited[row][col] = true;        
        let diffs = vec![(-1, 0), (1, 0), (0, -1), (0, 1)];
        for i in 0..diffs.len() {
            let (dx, dy) = diffs[i];
            let x = dx + row as i32;
            let y = dy + col as i32;
            if x < 0 || y < 0 || x >= rows as i32 || y >= cols as i32 {
                continue;
            }
            let x = x as usize;
            let y = y as usize;
            if visited[x][y] || grid[x][y] == 0 {
                continue;
            }
            Self::dfs(grid, visited, x, y);
        }
    }
    pub fn calculate_neighbors(visited: &Vec<Vec<bool>>, row: usize, col: usize) -> Vec<(i32, i32)> {
        let rows = visited.len();
        let cols = visited[0].len();
        vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
        .map(|&(dx, dy)| (row as i32 + dx, col as i32 + dy))
        .filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32 && !visited[x as usize][y as usize])
        .collect::<Vec<_>>()
    }

    pub fn shortest_bridge(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; cols]; rows];
        for k in 0..rows * cols {
            let i = k / cols;
            let j = k % cols;
            if grid[i][j] == 1 {
                Self::dfs(&grid, &mut visited, i, j);
                break;
            }
        }
        // println!("{:?}", visited);
        let mut q: VecDeque<(usize, usize, usize)> = VecDeque::new();

        for i in 0..rows {
            for j in 0..cols {
                if visited[i][j] {
                    if Self::calculate_neighbors(&visited, i, j).len() > 0 {
                        q.push_back((i, j, 0));
                    }
                }
            }
        }
        while !q.is_empty() {
            let (row, col, level) = q.pop_front().unwrap();
            if level > 0 && grid[row][col] == 1 {
                return level as i32 - 1;
            }
            let neighbors = Self::calculate_neighbors(&visited, row, col);
            for i in 0..neighbors.len() {
                let (x, y) = neighbors[i];
                visited[x as usize][y as usize] = true;
                q.push_back((x as usize, y as usize, level + 1));
            }
        }
        0
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_934() {
        assert_eq!(Solution::shortest_bridge(vec![vec![0,1],vec![1,0]]), 1);
        assert_eq!(Solution::shortest_bridge(vec![vec![0,1,0],vec![0,0,0],vec![0,0,1]]), 2);
    }
}

```
