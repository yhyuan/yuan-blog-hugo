---
title: 63. unique paths ii
date: '2021-07-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0063 unique paths ii
---



A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)
>   Input: obstacleGrid <TeX>=</TeX> [[0,0,0],[0,1,0],[0,0,0]]
>   Output: 2
>   Explanation: There is one obstacle in the middle of the 3x3 grid above.
>   There are two ways to reach the bottom-right corner:
>   1. Right -> Right -> Down -> Down
>   2. Down -> Down -> Right -> Right
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)
>   Input: obstacleGrid <TeX>=</TeX> [[0,1],[0,0]]
>   Output: 1
**Constraints:**
>   	m <TeX>=</TeX><TeX>=</TeX> obstacleGrid.length
>   	n <TeX>=</TeX><TeX>=</TeX> obstacleGrid[i].length
>   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 100
>   	obstacleGrid[i][j] is 0 or 1.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
let m = obstacle_grid.len();
let n = obstacle_grid[0].len();
let mut table: Vec<Vec<i32>> = vec![vec![0; n]; m];
let mut found = false;
for i in 0..m {
if obstacle_grid[i][0] == 1 {
found = true;
}
table[i][0] = if found {0} else {1};
}
found = false;
for i in 0..n {
if obstacle_grid[0][i] == 1 {
found = true;
}
table[0][i] = if found {0} else {1};
}
for i in 1..m {
for j in 1..n {
let v1 = if obstacle_grid[i - 1][j] == 1 {0} else {table[i - 1][j]};
let v2 = if obstacle_grid[i][j - 1] == 1 {0} else {table[i][j - 1]};
table[i][j] = v1 + v2;
}
}
if obstacle_grid[m - 1][n - 1] == 1 {0} else {table[m - 1][n - 1]}
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_63() {
assert_eq!(Solution::unique_paths_with_obstacles(vec![vec![0]]), 1);
assert_eq!(
Solution::unique_paths_with_obstacles(vec![vec![0, 0], vec![0, 0],]),
2
);
assert_eq!(
Solution::unique_paths_with_obstacles(vec![vec![0, 1], vec![1, 0],]),
0
);
assert_eq!(
Solution::unique_paths_with_obstacles(vec![
vec![0, 0, 0],
vec![0, 1, 0],
vec![0, 0, 0],
]),
2
);
assert_eq!(
Solution::unique_paths_with_obstacles(vec![
vec![0, 0, 0, 0],
vec![0, 0, 0, 0],
vec![0, 0, 0, 0],
]),
10
);
assert_eq!(
Solution::unique_paths_with_obstacles(vec![
vec![0, 0, 0, 0],
vec![0, 0, 0, 1],
vec![0, 0, 1, 0],
]),
0
);
}
}

```
