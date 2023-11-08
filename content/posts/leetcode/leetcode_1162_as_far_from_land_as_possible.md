---
title: 1162. as far from land as possible
date: '2022-07-15'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1162 as far from land as possible
---



Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2019/05/03/1336_ex1.JPG)
>   Input: grid <TeX>=</TeX> [[1,0,1],[0,0,0],[1,0,1]]
>   Output: 2
>   Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2019/05/03/1336_ex2.JPG)
>   Input: grid <TeX>=</TeX> [[1,0,0],[0,0,0],[0,0,0]]
>   Output: 4
>   Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
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
pub fn max_distance(grid: Vec<Vec<i32>>) -> i32 {
let rows = grid.len();
let cols = grid[0].len();
let mut q: VecDeque<(usize, usize, usize)> = VecDeque::new();
for i in 0..rows {
for j in 0..cols {
if grid[i][j] == 1 {
q.push_back((i, j, 0));
}
}
}
if q.len() == 0 || q.len() == rows * cols {
return -1;
}
if q.len() == 1 {
let (i, j, level) = q.pop_front().unwrap();
let res = vec![(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)].iter()
.map(|&(x, y)| (x as i32 - i as i32).abs() + (y as i32 - j as i32).abs()).max().unwrap();
return res;
}
let mut dists: Vec<Vec<i32>> = vec![vec![i32::MAX; cols]; rows];
while !q.is_empty() {
let (i, j, level) = q.pop_front().unwrap();
dists[i][j] = i32::min(dists[i][j], level as i32);
let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
.map(|&(dx, dy)| (dx + i as i32, dy + j as i32))
.filter(|&(x, y)| x >= 0 && y >= 0 && x < rows as i32 && y < cols as i32)
.filter(|&(x, y)| dists[x as usize][y as usize] > level as i32 + 1)
.collect::<Vec<_>>();
for k in 0..neighbors.len() {
let (x, y) = neighbors[k];
q.push_back((x as usize, y as usize, level + 1));
}
}
let mut result = i32::MIN;
for i in 0..rows {
for j in 0..cols {
result = i32::max(result, dists[i][j]);
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
fn test_1162() {
assert_eq!(Solution::max_distance(vec![vec![1,0,1],vec![0,0,0],vec![1,0,1]]), 2);
assert_eq!(Solution::max_distance(vec![vec![1,0,0],vec![0,0,0],vec![0,0,0]]), 4);
}
}

```
