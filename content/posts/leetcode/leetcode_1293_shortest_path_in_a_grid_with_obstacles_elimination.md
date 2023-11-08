---
title: 1293. shortest path in a grid with obstacles elimination
date: '2022-07-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1293 shortest path in a grid with obstacles elimination
---



You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



>   Example 1:
>   Input:
>   grid <TeX>=</TeX>
>   [[0,0,0],
>    [1,1,0],
>    [0,0,0],
>    [0,1,1],
>    [0,0,0]],
>   k <TeX>=</TeX> 1
>   Output: 6
>   Explanation:
>   The shortest path without eliminating any obstacle is 10.
>   The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
>   Example 2:
>   Input:
>   grid <TeX>=</TeX>
>   [[0,1,1],
>    [1,1,1],
>    [1,0,0]],
>   k <TeX>=</TeX> 1
>   Output: -1
>   Explanation:
>   We need to eliminate at least two obstacles to find such a walk.
**Constraints:**
>   	m <TeX>=</TeX><TeX>=</TeX> grid.length
>   	n <TeX>=</TeX><TeX>=</TeX> grid[i].length
>   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 40
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> m  n
>   	grid[i][j] <TeX>=</TeX><TeX>=</TeX> 0 or 1
>   	grid[0][0] <TeX>=</TeX><TeX>=</TeX> grid[m - 1][n - 1] <TeX>=</TeX><TeX>=</TeX> 0


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
use std::collections::HashSet;
/*
impl Solution {
pub fn bfs(grid: &mut Vec<Vec<i32>>) -> i32 {
let m = grid.len();
let n = grid[0].len();
let mut q: VecDeque<(usize, usize)> = VecDeque::new();
let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];
q.push_back((0, 0));
visited[0][0] = true;
let mut step = 0;
let mut found = false;
while !q.is_empty() {
let q_size = q.len();
for _ in 0..q_size {
let (i, j) = q.pop_front().unwrap();
if i == m - 1 && j == n - 1 {
found = true;
break;
}
let mut diffs = vec![(-1, 0), (0, -1), (1, 0), (0, 1)];
for k in 0..diffs.len() {
let (dx, dy) = diffs[k];
let next_i = i as i32 + dx;
let next_j = j as i32 + dy;
if next_i < 0 || next_i >= m as i32 || next_j < 0 || next_j >= n as i32 {
continue;
}
let next_i = next_i as usize;
let next_j = next_j as usize;
if visited[next_i][next_j] || grid[next_i][next_j] == 1 {
continue;
}
visited[next_i][next_j] = true;
q.push_back((next_i, next_j));
}
}
if found {
break;
}
step += 1;
}
if found {
return step;
}
return i32::MAX;
}
pub fn shortest_path_helper(grid: &mut Vec<Vec<i32>>, obstacles_positions: &mut Vec<(usize, usize)>, k: i32) -> i32 {
if k == 0 || obstacles_positions.len() == 0 {
return Self::bfs(grid);
}
//let mut grid = grid;
let mut min_result = i32::MAX;
for position_index in 0..obstacles_positions.len() {
let obstacle_postion = obstacles_positions[position_index];
grid[obstacle_postion.0][obstacle_postion.1] = 0;
obstacles_positions.remove(position_index);
let result = Self::shortest_path_helper(grid, obstacles_positions, k - 1);
min_result = i32::min(min_result, result);
grid[obstacle_postion.0][obstacle_postion.1] = 1;
obstacles_positions.insert(position_index, obstacle_postion); //v.insert(pos, new_elem),
}
min_result
}

pub fn shortest_path(grid: Vec<Vec<i32>>, k: i32) -> i32 {
let mut grid = grid;
let mut obstacles_positions: Vec<(usize, usize)> = vec![];
let m = grid.len();
let n = grid[0].len();
for i in 0..m {
for j in 0..n {
if grid[i][j] == 1 {
obstacles_positions.push((i, j));
}
}
}
// println!("obstacles: {:?}", obstacles_positions);
if obstacles_positions.len() as i32 <= k {
return (m + n - 2) as i32;
}
let result = Self::shortest_path_helper(&mut grid, &mut obstacles_positions, k);
if result == i32::MAX {
return -1;
}
result
}
}
*/
impl Solution {
pub fn shortest_path(grid: Vec<Vec<i32>>, k: i32) -> i32 {
let rows = grid.len();
let cols = grid[0].len();
let mahaton_length = (rows + cols - 2) as i32;
if k >= mahaton_length {
return mahaton_length;
}
let mut q: VecDeque<(usize, (usize, usize, i32))> = VecDeque::new();
let mut visited: HashSet<(usize, usize, i32)> = HashSet::new();
q.push_back((0, (0, 0, k)));
visited.insert((0, 0, k));
while !q.is_empty() {
let (steps, (row, col, current_k)) = q.pop_front().unwrap();
// println!("steps: {}, state: ({}, {}, {})", steps, row, col, current_k);
if row == rows - 1 && col == cols - 1 {
return steps as i32;
}
let deltas = vec![(-1, 0), (0, -1), (1, 0), (0, 1)];
let next_states = deltas.iter()
.map(|&(dx, dy)| (row as i32 + dx, col as i32 + dy))
.filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32)
.map(|(x, y)| (x as usize, y as usize))
.map(|(x, y)|(x, y, if grid[x][y] == 1 {current_k - 1} else {current_k}))
.filter(|&(_, _, k_value)| k_value >= 0)
.filter(|&state| !visited.contains(&state))
.collect::<Vec<_>>();
for i in 0..next_states.len() {
let next_state = next_states[i];
visited.insert(next_state);
q.push_back((steps + 1, next_state));
}
}
return -1;
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1293() {
assert_eq!(Solution::shortest_path(vec![vec![0,0,0],vec![1,1,0],vec![0,0,0],vec![0,1,1],vec![0,0,0]], 1), 6);
assert_eq!(Solution::shortest_path(vec![vec![0,1,1],vec![1,1,1],vec![1,0,0]], 1), -1);
assert_eq!(Solution::shortest_path(vec![vec![0]], 1), 0);
assert_eq!(Solution::shortest_path(vec![vec![0,0,0,1,0],vec![0,1,0,1,0],vec![0,1,0,1,1],vec![0,1,1,0,1],vec![1,1,0,0,0]], 14), 8);
}
}


```
