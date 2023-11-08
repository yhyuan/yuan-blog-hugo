---
title: 240. search a 2d matrix ii
date: '2021-11-25'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0240 search a 2d matrix ii
---



Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:



Integers in each row are sorted in ascending from left to right.

Integers in each column are sorted in ascending from top to bottom.





>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)
>   Input: matrix <TeX>=</TeX> [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target <TeX>=</TeX> 5
>   Output: true
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg)
>   Input: matrix <TeX>=</TeX> [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target <TeX>=</TeX> 20
>   Output: false
**Constraints:**
>   	m <TeX>=</TeX><TeX>=</TeX> matrix.length
>   	n <TeX>=</TeX><TeX>=</TeX> matrix[i].length
>   	1 <TeX>\leq</TeX> n, m <TeX>\leq</TeX> 300
>   	-10^9 <TeX>\leq</TeX> matix[i][j] <TeX>\leq</TeX> 10^9
>   	All the integers in each row are sorted in ascending order.
>   	All the integers in each column are sorted in ascending order.
>   	-10^9 <TeX>\leq</TeX> target <TeX>\leq</TeX> 10^9


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
pub fn search_single_row(matrix: &Vec<Vec<i32>>, x:usize, start_y: usize, end_y: usize, target: i32) -> bool {
if start_y == end_y {
return matrix[x][start_y] == target;
}
let mid_y = start_y + (end_y - start_y) / 2;
if matrix[x][mid_y] == target {
return true;
}
return if matrix[x][mid_y] > target {
Solution::search_single_row(matrix, x, start_y, mid_y, target)
} else {
Solution::search_single_row(matrix, x, mid_y, end_y, target)
};
}
pub fn search_matrix_helper(matrix: &Vec<Vec<i32>>, start_x:usize, end_x: usize, start_y: usize, end_y: usize, target: i32) -> bool {
if start_x == end_x || start_y == end_y {
return if start_x == end_x {
(start_y..=end_y).into_iter().map(|i|matrix[start_x][i]).position(|x| x == target).is_some()
//Solution::search_single_row(matrix, start_x, start_y, end_y, target)
} else {
(start_x..=end_x).into_iter().map(|i|matrix[i][start_y]).position(|x| x == target).is_some()
};
}
let mid_x = start_x + (end_x - start_x) / 2;
let mid_y = start_y + (end_y - start_y) / 2;
//println!("mid_x: {}, mid_y: {}, matrix[mid]: {}", mid_x, mid_y, matrix[mid_x][mid_y]);
if matrix[mid_x][mid_y] == target {
return true;
}
if matrix[mid_x][mid_y] > target {
let r1 = Self::search_matrix_helper(matrix, start_x, mid_x, start_y, end_y, target);
let r2 = Self::search_matrix_helper(matrix, mid_x, end_x, start_y, mid_y, target);
return r1 || r2;
} else {
let r1 = Self::search_matrix_helper(matrix, mid_x + 1, end_x, start_y, end_y, target);
let r2 = Self::search_matrix_helper(matrix, start_x,mid_x, mid_y + 1, end_y, target);
return r1 || r2;
}
}
pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
let m = matrix.len();
let n = matrix[0].len();
let mut start_x = 0usize;
let mut start_y = 0usize;
let mut end_x = m - 1;
let mut end_y = n - 1;
Solution::search_matrix_helper(&matrix, start_x, end_x, start_y, end_y, target)
}
}
*/
impl Solution {
pub fn helper(matrix: &Vec<Vec<i32>>, target: i32, low_rows: usize, high_rows: usize, low_cols: usize, high_cols: usize) -> bool {
if low_rows == high_rows && low_cols == high_cols {
return matrix[low_rows][low_cols] == target;
}
if low_rows == high_rows {
let mid = (low_cols + high_cols) / 2;
if matrix[low_rows][mid] == target {
return true;
}
if low_cols + 1 == high_cols {
return matrix[low_rows][low_cols] == target || matrix[low_rows][high_cols] == target;
}
return if matrix[low_rows][mid] > target {
Self::helper(matrix, target, low_rows, high_rows, low_cols, mid - 1)
} else {
Self::helper(matrix, target, low_rows, high_rows, mid + 1, high_cols)
};
}
if low_rows + 1 == high_rows {
return Self::helper(matrix, target, low_rows, low_rows, low_cols, high_cols)
|| Self::helper(matrix, target, high_rows, high_rows, low_cols, high_cols);
}
if low_cols == high_cols {
let mid = (low_rows + high_rows) / 2;
if matrix[mid][low_cols] == target {
return true;
}
if low_rows + 1 == high_rows {
return matrix[low_rows][low_cols] == target || matrix[high_rows][low_cols] == target;
}
return if matrix[mid][low_cols] > target {
Self::helper(matrix, target, low_rows, mid - 1, low_cols, high_cols)
} else {
Self::helper(matrix, target, mid + 1, high_rows, low_cols, high_cols)
};
}
if low_cols + 1 == high_cols {
return Self::helper(matrix, target, low_rows, high_rows, low_cols, low_cols)
|| Self::helper(matrix, target, low_rows, high_rows, high_cols, high_cols);
}
let mid_rows = (low_rows + high_rows) / 2;
let mid_cols = (low_cols + high_cols) / 2;
let mid_val = matrix[mid_rows][mid_cols];
return if target == mid_val {
true
} else if mid_val > target {
Self::helper(matrix, target, low_rows, mid_rows - 1, low_cols, high_cols)
|| Self::helper(matrix, target, mid_rows, high_rows, low_cols, mid_cols - 1)
} else {
Self::helper(matrix, target, mid_rows + 1, high_rows, low_cols, high_cols)
|| Self::helper(matrix, target, low_rows, mid_rows, mid_cols + 1, high_cols)
};
}
pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
let m = matrix.len();
let n = matrix[0].len();
Self::helper(&matrix, target, 0, m - 1, 0, n - 1)
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_240() {
assert_eq!(Solution::search_matrix(vec![vec![1,4,7,11,15],vec![2,5,8,12,19],vec![3,6,9,16,22],vec![10,13,14,17,24],vec![18,21,23,26,30]], 5), true);
assert_eq!(Solution::search_matrix(vec![vec![1,4,7,11,15],vec![2,5,8,12,19],vec![3,6,9,16,22],vec![10,13,14,17,24],vec![18,21,23,26,30]], 20), false);
assert_eq!(Solution::search_matrix(vec![vec![-5]], -2), false);
assert_eq!(Solution::search_matrix(vec![vec![-5]], -10), false);
assert_eq!(Solution::search_matrix(vec![vec![1, 1]], 0), false);
assert_eq!(Solution::search_matrix(vec![vec![-5]], -5), true);
}
}

```
