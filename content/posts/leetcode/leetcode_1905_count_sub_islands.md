---
title: 1905. count sub islands
date: '2022-08-29'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 1905 count sub islands
---

 

  You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

  An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

  Return the number of islands in grid2 that are considered sub-islands.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/06/10/test1.png)

 >   Input: grid1 <TeX>=</TeX> [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 <TeX>=</TeX> [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

 >   Output: 3

 >   Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.

 >   The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/06/03/testcasex2.png)

 >   Input: grid1 <TeX>=</TeX> [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 <TeX>=</TeX> [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]

 >   Output: 2 

 >   Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.

 >   The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> grid1.length <TeX>=</TeX><TeX>=</TeX> grid2.length

 >   	n <TeX>=</TeX><TeX>=</TeX> grid1[i].length <TeX>=</TeX><TeX>=</TeX> grid2[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 500

 >   	grid1[i][j] and grid2[i][j] are either 0 or 1.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn dfs(grid: &Vec<Vec<i32>>, islands: &mut Vec<Vec<i32>>, count: i32, row: usize, col: usize) {
        let rows = grid.len();
        let cols = grid[0].len();
        islands[row][col] = count;
        let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
            .map(|&(dx, dy)| (dx + row as i32, dy + col as i32))
            .filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32 && islands[x as usize][y as usize] < 0 && grid[x as usize][y as usize] == 1)
            .collect::<Vec<_>>();
        for i in 0..neighbors.len() {
            let (x, y) = neighbors[i];
            Self::dfs(grid, islands, count, x as usize, y as usize);
        }
    }
    pub fn dfs2(grid: &Vec<Vec<i32>>, islands: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, is_good: &mut bool, id: &mut i32, row: usize, col: usize) {
        let rows = grid.len();
        let cols = grid[0].len();
        visited[row][col] = true;
        if islands[row][col] >= 0 {
            if *id < 0 {
                *id = islands[row][col];
            } else {
                if *id != islands[row][col] {
                    *is_good = false;
                }
            }
        } else {
            if *is_good {
                *is_good = false;
            }
        }
        let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
            .map(|&(dx, dy)| (dx + row as i32, dy + col as i32))
            .filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32 && !visited[x as usize][y as usize] && grid[x as usize][y as usize] == 1)
            .collect::<Vec<_>>();
        for i in 0..neighbors.len() {
            let (x, y) = neighbors[i];
            Self::dfs2(grid, islands, visited, is_good, id, x as usize, y as usize);
        }
    }
    pub fn count_sub_islands(grid1: Vec<Vec<i32>>, grid2: Vec<Vec<i32>>) -> i32 {
        let rows = grid1.len();
        let cols = grid1[0].len();
        let mut islands = vec![vec![-1; cols]; rows];
        let mut count = 0;
        for i in 0..rows {
            for j in 0..cols {
                if grid1[i][j] == 0 {
                    continue;
                }
                if islands[i][j] >= 0 {
                    continue;
                }
                Self::dfs(&grid1, &mut islands, count, i, j);
                count += 1;
            }
        }
        // println!("islands: {:?}", islands);
        let mut visited = vec![vec![false; cols]; rows];
        // let mut count = 0;
        let mut result = 0;
        for i in 0..rows {
            for j in 0..cols {
                if grid2[i][j] == 0 {
                    continue;
                }
                if visited[i][j] {
                    continue;
                }
                let mut is_good = islands[i][j] >= 0;
                // println!("is_good: {}", is_good);
                let mut id = -1;
                Self::dfs2(&grid2, &islands, &mut visited, &mut is_good, &mut id, i, j);
                // println!("i: {}, j: {}, is_good: {}", i, j, is_good);
                count += 1;
                // println!("is_good: {}", is_good);
                if is_good {
                    result += 1;
                }
            }
        }
        // println!("islands: {:?}", islands);
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1905() {
/*
        assert_eq!(Solution::count_sub_islands(
        vec![
            vec![1,1,1,0,0],
            vec![0,1,1,1,1],
            vec![0,0,0,0,0],
            vec![1,0,0,0,0],
            vec![1,1,0,1,1]], 
        vec![
            vec![1,1,1,0,0],
            vec![0,0,1,1,1],
            vec![0,1,0,0,0],
            vec![1,0,1,1,0],
            vec![0,1,0,1,0]]), 3);
*/
        assert_eq!(Solution::count_sub_islands(
            vec![
                vec![1,1,0,1,0,1,1,1],
                vec![0,1,1,1,1,0,1,1],
                vec![1,1,1,1,0,1,0,1],
                vec![1,1,1,0,1,1,1,1],
                vec![1,1,1,1,0,1,1,0],
                vec![1,1,1,1,0,1,0,0],
                vec![1,0,1,1,1,1,0,0],
                vec![1,0,0,1,1,1,1,1]], 
            vec![
                vec![1,1,1,1,0,0,0,0],
                vec![0,1,1,1,0,0,1,1],
                vec![1,1,1,1,0,1,1,1],
                vec![1,1,0,1,1,1,1,0],
                vec![1,0,0,1,0,1,1,1],
                vec![1,1,0,1,1,1,1,0],
                vec![1,0,1,0,1,1,1,1],
                vec![1,1,1,1,1,0,1,1]]), 0);
    }
}

```
