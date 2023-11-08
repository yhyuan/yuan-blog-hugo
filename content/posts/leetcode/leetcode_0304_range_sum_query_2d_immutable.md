---
title: 304. range sum query 2d immutable
date: '2021-12-29'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0304 range sum query 2d immutable
---



Given a 2D matrix matrix, handle multiple queries of the following type:



Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).



Implement the NumMatrix class:



NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.

int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).





>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg)
>   Input
>   ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
>   [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
>   Output
>   [null, 8, 11, 12]
>   Explanation
>   NumMatrix numMatrix <TeX>=</TeX> new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
>   numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
>   numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
>   numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
**Constraints:**
>   	m <TeX>=</TeX><TeX>=</TeX> matrix.length
>   	n <TeX>=</TeX><TeX>=</TeX> matrix[i].length
>   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 200
>   	-10^5 <TeX>\leq</TeX> matrix[i][j] <TeX>\leq</TeX> 10^5
>   	0 <TeX>\leq</TeX> row1 <TeX>\leq</TeX> row2 < m
>   	0 <TeX>\leq</TeX> col1 <TeX>\leq</TeX> col2 < n
>   	At most 10^4 calls will be made to sumRegion.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

struct NumMatrix {
sum_matrix: Vec<Vec<i32>>
}


/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl NumMatrix {

fn new(matrix: Vec<Vec<i32>>) -> Self {
if matrix.len() == 0 {
return NumMatrix {sum_matrix: matrix};
}
let mut sum_matrix: Vec<Vec<i32>> = Vec::with_capacity(matrix.len());
for i in 0..matrix.len() {
sum_matrix.push(vec![0; matrix[i].len()]);
}
//first row
for j in 0..matrix[0].len() {
sum_matrix[0][j] = if j == 0 {matrix[0][0]} else {matrix[0][j] + sum_matrix[0][j - 1]};
}
//first column
for i in 1..matrix.len() {
sum_matrix[i][0] = matrix[i][0] + sum_matrix[i - 1][0];
}

for i in 1..matrix.len() {
for j in 1..matrix[i].len() {
sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1] + matrix[i][j];
}
}
NumMatrix {sum_matrix: sum_matrix}
}

fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
//println!("{:?}", self.sum_matrix);
let row1 = row1 as usize;
let row2 = row2 as usize;
let col1 = col1 as usize;
let col2 = col2 as usize;
let v0 = self.sum_matrix[row2][col2];
let v1 = if row1 == 0 {0} else {self.sum_matrix[row1 - 1][col2]};
let v2 = if col1 == 0 {0} else {self.sum_matrix[row2][col1 - 1]};
let v3 = if row1 == 0 || col1 == 0 {0} else {self.sum_matrix[row1 - 1][col1 - 1]};
//println!("v0: {}, v1: {}, v2: {}, v3: {}", v0, v1, v2, v3);
v0 - v1 - v2 + v3
}
}

/**
* Your NumMatrix object will be instantiated and called as such:
* let obj = NumMatrix::new(matrix);
* let ret_1: i32 = obj.sum_region(row1, col1, row2, col2);
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_304() {
let matrix = NumMatrix::new(vec![
vec![3, 0, 1, 4, 2],
vec![5, 6, 3, 2, 1],
vec![1, 2, 0, 1, 5],
vec![4, 1, 0, 1, 7],
vec![1, 0, 3, 0, 5],
]);
assert_eq!(matrix.sum_region(1, 1, 2, 2), 11);
assert_eq!(matrix.sum_region(2, 1, 4, 3), 8);
assert_eq!(matrix.sum_region(1, 2, 2, 4), 12);
}
}

```
