---
title: 2128. remove all ones with row and column flips
date: '2022-09-08'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2128 remove all ones with row and column flips
---


You are given an m x n binary matrix grid.



In one operation, you can choose any row or column and flip each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).



Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.







> Example 1:
> Input: grid <TeX>=</TeX> [[0,1,0],[1,0,1],[0,1,0]]
> Output: true
> Explanation: One possible way to remove all 1's from grid is to:
> - Flip the middle row
> - Flip the middle column
> Example 2:
> Input: grid <TeX>=</TeX> [[1,1,0],[0,0,0],[0,0,0]]
> Output: false
> Explanation: It is impossible to remove all 1's from grid.
> Example 3:
> Input: grid <TeX>=</TeX> [[0]]
> Output: true
> Explanation: There are no 1's in grid.
**Constraints:**
> m <TeX>=</TeX><TeX>=</TeX> grid.length
> n <TeX>=</TeX><TeX>=</TeX> grid[i].length
> 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 300
> grid[i][j] is either 0 or 1.


## Solution


### Rust
```rust
pub struct Solution {}

use std::collections::HashMap;
/**
*
* 翻一个只有0和1的矩阵, 只能翻一个行或者一个列. 返回能不能翻成全1或者全0矩阵.

这题只需要判断第一行, 见到0不动, 见到1翻过来,这样第一行就是全0. 然后通过判断其他行是不是全1或者全0, 即可知道答案.

证: 如果第一行已经全0, 其他某行, 非全1或者全0, 那么这行通过行翻转, 肯定不能得到全1或者全0, 但是通过列翻转, 又破坏第一行的全0,故此.
*/
impl Solution {
pub fn flip_column(grid: &mut Vec<Vec<i32>>, j: usize) {
for i in 0..grid.len() {
grid[i][j] = if grid[i][j] == 0 {1} else {0};
}
}
pub fn are_same_values(row: &Vec<i32>) -> bool {
let n = row.len();
let val = row[0];
for i in 1..n {
if row[i] != val {
return false;
}
}
true
}
pub fn remove_ones(grid: Vec<Vec<i32>>) -> bool {
let mut grid = grid;
let m = grid.len();
let n = grid[0].len();
for j in 0..n {
if grid[0][j] == 1 {
Self::flip_column(&mut grid, j);
}
}
for i in 0..m {
if !Self::are_same_values(&grid[i]) {
return false
}
}
true
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_2128() {
assert_eq!(Solution::remove_ones(vec![vec![0,1,0],vec![1,0,1],vec![0,1,0]]), true);
}
}

```
