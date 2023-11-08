---
title: 1020. number of enclaves
date: '2022-06-29'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1020 number of enclaves
---

 

  You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

  A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

  Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg)

 >   Input: grid <TeX>=</TeX> [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

 >   Output: 3

 >   Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg)

 >   Input: grid <TeX>=</TeX> [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]

 >   Output: 0

 >   Explanation: All 1s are either on the boundary or can reach the boundary.

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> grid.length

 >   	n <TeX>=</TeX><TeX>=</TeX> grid[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 500

 >   	grid[i][j] is either 0 or 1.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn helper(grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, is_good: &mut bool, area: &mut i32, row: usize, col: usize) {
        let rows = grid.len();
        let cols = grid[0].len();
        if !visited[row][col] {
            *area += 1;
        }
        visited[row][col] = true;
        if row == 0 || col == 0 || row == rows - 1 || col == cols - 1 {
            if *is_good {
                *is_good = false;
            }
        }
        let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
            .map(|&(dx, dy)| (dx + row as i32, dy + col as i32))
            .filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32 && grid[x as usize][y as usize] == 1 && !visited[x as usize][y as usize])
            .collect::<Vec<_>>();
        for i in 0..neighbors.len() {
            let (x, y) = neighbors[i];
            Self::helper(grid, visited, is_good, area, x as usize, y as usize);
        }
    }

    pub fn num_enclaves(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut visited = vec![vec![false; cols]; rows];
        let mut result = 0;
        for i in 0..rows {
            for j in 0..cols {
                if grid[i][j] == 0 {
                    continue;
                }
                if visited[i][j] {
                    continue;
                }
                let mut is_good = true;
                let mut area = 0;
                Self::helper(&grid, &mut visited, &mut is_good, &mut area, i, j);
                if is_good {
                    result += area;
                }
            }
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1020() {
        assert_eq!(Solution::num_enclaves(vec![
            vec![0,0,0,0],
            vec![1,0,1,0],
            vec![0,1,1,0],
            vec![0,0,0,0]]), 3);
    }
}

```
