---
title: 694. number of distinct islands
date: '2022-04-20'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0694 number of distinct islands
---


You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.



An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.



Return the number of distinct islands.







> Example 1:
> Input: grid <TeX>=</TeX> [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
> Output: 1
> Example 2:
> Input: grid <TeX>=</TeX> [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
> Output: 3
**Constraints:**
> m <TeX>=</TeX><TeX>=</TeX> grid.length
> n <TeX>=</TeX><TeX>=</TeX> grid[i].length
> 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 50
> grid[i][j] is either 0 or 1.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
pub fn dfs(grid: &Vec<Vec<i32>>, visited: &mut Vec<Vec<bool>>, coor: (usize, usize), island: &mut Vec<(usize, usize)>) {
let m = grid.len();
let n = grid[0].len();
let (x, y) = coor;
island.push(coor);
visited[x][y] = true;
let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].into_iter()
.map(|(dx, dy)| (x as i32 + dx, y as i32 + dy))
.filter(|&(x, y)| x >= 0 && y >= 0 && x < m as i32 && y < n as i32 && !visited[x as usize][y as usize])
.collect::<Vec<_>>();
for i in 0..neighbors.len() {
let new_coor = (neighbors[i].0 as usize, neighbors[i].1 as usize);
Self::dfs(grid, visited, new_coor, island);
}
}
pub fn is_same_island(island1: &Vec<(usize, usize)>, island2: &Vec<(usize, usize)>) -> bool {
let n1 = island1.len();
let n2 = island2.len();
if n1 != n2 {
return false;
}
for i in 0..n1 {
if island1[i].0 != island2[i].0 || island1[i].1 != island2[i].1 {
return false;
}
}
true
}
pub fn num_distinct_islands(grid: Vec<Vec<i32>>) -> i32 {
let m = grid.len();
let n = grid[0].len();
let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
for i in 0..m {
for j in 0..n {
visited[i][j] = grid[i][j] == 0;
}
}
let mut islands: Vec<Vec<(usize, usize)>> = vec![];
for i in 0..m {
for j in 0..n {
if !visited[i][j] {
let mut island: Vec<(usize, usize)> = vec![];
Self::dfs(&grid, &mut visited, (i, j), &mut island);
let min_x = island.iter().map(|&coor| coor.0).min().unwrap();
let min_y = island.iter().map(|&coor| coor.1).min().unwrap();
island = island.iter().map(|&coor| (coor.0 - min_x, coor.1 - min_y)).collect::<Vec<_>>();
let mut is_found = false;
for k in 0..islands.len() {
if Self::is_same_island(&island, &islands[k]) {
is_found = true;
break;
}
}
if !is_found {
islands.push(island);
}
}
}
}
islands.len() as i32
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_694() {
assert_eq!(Solution::num_distinct_islands(vec![vec![1,1,0,0,0],vec![1,1,0,0,0],vec![0,0,0,1,1],vec![0,0,0,1,1]]), 1);
}
}

```
