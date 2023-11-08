---
title: 695. max area of island
date: '2022-04-21'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0695 max area of island
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={695}/>
 

  You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

  The area of an island is the number of cells with a value 1 in the island.

  Return the maximum area of an island in grid. If there is no island, return 0.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

 >   Input: grid <TeX>=</TeX> [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

 >   Output: 6

 >   Explanation: The answer is not 11, because the island must be connected 4-directionally.

  

 >   Example 2:

  

 >   Input: grid <TeX>=</TeX> [[0,0,0,0,0,0,0,0]]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> grid.length

 >   	n <TeX>=</TeX><TeX>=</TeX> grid[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 50

 >   	grid[i][j] is either 0 or 1.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn helper(grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, area: &mut i32, row: i32, col: i32) {
        let rows = grid.len() as i32;
        let cols = grid[0].len() as i32;
        let diffs = vec![(-1, 0), (1, 0), (0, -1), (0, 1)];
        if !visited[row as usize][col as usize] {
            println!("x: {}, y:{}", row, col);
            *area += 1;
        }
        visited[row as usize][col as usize] = true;
        let neighbors = diffs.iter()
            .map(|&(dx, dy)| (row + dx, col + dy))
            .filter(|&(x, y)| x >= 0 && x < rows && y >= 0 && y < cols && grid[x as usize][y as usize] == 1 && !visited[x as usize][y as usize])
            .collect::<Vec<_>>();
        for i in 0..neighbors.len() { 
            let (x, y) = neighbors[i];
            Self::helper(grid, visited, area, x, y);
        }
    }
    pub fn max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut visited = vec![vec![false; cols]; rows];
        let mut max_area = 0;
        for i in 0..rows {
            for j in 0..cols {
                if grid[i][j] == 0 {
                    continue;
                }
                if visited[i][j] {
                    continue;
                }
                println!("i: {}, j: {}", i, j);
                let mut area = 0i32;
                Self::helper(&grid, &mut visited, &mut area, i as i32, j as i32);
                println!("area: {}", area);
                max_area = i32::max(max_area, area);
            }
        }
        max_area
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_695() {
        assert_eq!(Solution::max_area_of_island(vec![
            vec![1,1,0,0,0],
            vec![1,1,0,0,0],
            vec![0,0,0,1,1],
            vec![0,0,0,1,1]]), 4);
    }
}

```
