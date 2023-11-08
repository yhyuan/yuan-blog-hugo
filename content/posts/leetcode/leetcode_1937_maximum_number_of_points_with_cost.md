---
title: 1937. maximum number of points with cost
date: '2022-09-01'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 1937 maximum number of points with cost
---



You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <TeX>\leq</TeX> r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:



x for x ><TeX>=</TeX> 0.

-x for x < 0.





>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png)
>   Input: points <TeX>=</TeX> [[1,2,3],[1,5,1],[3,1,1]]
>   Output: 9
>   Explanation:
>   The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
>   You add 3 + 5 + 3 <TeX>=</TeX> 11 to your score.
>   However, you must subtract abs(2 - 1) + abs(1 - 0) <TeX>=</TeX> 2 from your score.
>   Your final score is 11 - 2 <TeX>=</TeX> 9.
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png)
>   Input: points <TeX>=</TeX> [[1,5],[2,3],[4,2]]
>   Output: 11
>   Explanation:
>   The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
>   You add 5 + 3 + 4 <TeX>=</TeX> 12 to your score.
>   However, you must subtract abs(1 - 1) + abs(1 - 0) <TeX>=</TeX> 1 from your score.
>   Your final score is 12 - 1 <TeX>=</TeX> 11.
**Constraints:**
>   	m <TeX>=</TeX><TeX>=</TeX> points.length
>   	n <TeX>=</TeX><TeX>=</TeX> points[r].length
>   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 10^5
>   	1 <TeX>\leq</TeX> m  n <TeX>\leq</TeX> 10^5
>   	0 <TeX>\leq</TeX> points[r][c] <TeX>\leq</TeX> 10^5


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
/*
pub fn max_points_helper(points: &Vec<Vec<i32>>, row: usize, col: usize, memo: &mut HashMap<(usize, usize), i64>) -> i64 {
let rows = points.len();
if row == rows - 1 {
return 0i64;
}
if memo.contains_key(&(row, col)) {
return *memo.get(&(row, col)).unwrap();
}
let cols = points[0].len();
let mut max_res = i64::MIN;
for j in 0..cols {
let diff = if col > j {col as i32 - j as i32} else {j as i32 - col as i32};
let res = Self::max_points_helper(&points, row + 1, j, memo) + points[row + 1][j] as i64 - diff as i64;
max_res = i64::max(max_res, res);
}
memo.insert((row, col), max_res);
max_res
}
*/
pub fn max_points(points: Vec<Vec<i32>>) -> i64 {
let cols = points[0].len();
let rows = points.len();
let mut dp: Vec<i64> = vec![0i64; cols];
for j in 0..cols {
dp[j] = points[rows - 1][j] as i64;
}
for i in 1..rows {
//println!("dp: {:?}", dp);
let row_id = rows - 1 - i;
let mut left_right_dp: Vec<i64> = vec![0i64; cols];
/*
for j in 0..cols {
next_dp[j] = points[row_id][j] as i64;
}
*/
// from left to right, next_dp[j] = points[row_id][j] as i64 + i64::max(dp[j], dp[j - 1] - 1, dp[j - 2] - 2, dp[j - 3] - 3... dp[0] - j)
// => i64::max(dp[j], dp[j - 1] - 1, dp[j - 2] - 2, dp[j - 3] - 3... dp[0] - j) = next_dp[j] - points[row_id][j] as i64
// next_dp[j + 1] = points[row_id][j + 1] as i64 + i64::max(dp[j + 1],  dp[j] - 1, dp[j - 1] - 2, dp[j - 2] - 3, dp[j - 3] - 4... dp[0] - j - 1)
//     = points[row_id][j + 1] as i64 + i64::max(dp[j + 1], (next_dp[j] - points[row_id][j] as i64) - 1)
// from right to left, we will have similar relationship.
for j in 0..cols {
if j == 0 {
left_right_dp[j] = points[row_id][j] as i64 + dp[j];
} else {
left_right_dp[j] = points[row_id][j] as i64 + i64::max(dp[j], left_right_dp[j - 1] - points[row_id][j - 1] as i64 - 1);
}
/*
let mut max_res = i64::MIN;
for k in 0..cols {
let res =  dp[k] - if j > k {j as i64 - k as i64} else {k as i64 - j as i64};
max_res = i64::max(max_res, res);
}
next_dp[j] += max_res;
*/
}
//println!("left_right_dp: {:?}", left_right_dp);
let mut right_left_dp: Vec<i64> = vec![0i64; cols];
for j in (0..cols).rev() {
if j == cols - 1 {
right_left_dp[j] = points[row_id][j] as i64 + dp[j];
} else {
right_left_dp[j] = points[row_id][j] as i64 + i64::max(dp[j], right_left_dp[j + 1] - points[row_id][j + 1] as i64 - 1);
}
}
//println!("right_left_dp: {:?}", right_left_dp);
let mut next_dp: Vec<i64> = vec![0i64; cols];
for j in 0..cols {
next_dp[j] = i64::max(left_right_dp[j], right_left_dp[j]);
}
dp = next_dp;
}
*dp.iter().max().unwrap()
/*
let cols = points[0].len();
let mut max_res = i64::MIN;
let mut memo: HashMap<(usize, usize), i64> = HashMap::new();
for j in 0..cols {
let res = Self::max_points_helper(&points, 0, j, &mut memo) + points[0][j] as i64;
max_res = i64::max(max_res, res);
}
max_res
*/
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1937() {
assert_eq!(Solution::max_points(vec![vec![1,2,3],vec![1,5,1],vec![3,1,1]]), 9);
assert_eq!(Solution::max_points(vec![vec![1,5],vec![3,2],vec![4,2]]), 11);
}
}

```
