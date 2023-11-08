---
title: 73. set matrix zeroes
date: '2021-07-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0073 set matrix zeroes
---



Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)
>   Input: matrix <TeX>=</TeX> [[1,1,1],[1,0,1],[1,1,1]]
>   Output: [[1,0,1],[0,0,0],[1,0,1]]
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
>   Input: matrix <TeX>=</TeX> [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
>   Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
**Constraints:**
>   	m <TeX>=</TeX><TeX>=</TeX> matrix.length
>   	n <TeX>=</TeX><TeX>=</TeX> matrix[0].length
>   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 200
>   	-2^31 <TeX>\leq</TeX> matrix[i][j] <TeX>\leq</TeX> 2^31 - 1
>   Follow up:
>   	A straightforward solution using O(mn) space is probably a bad idea.
>   	A simple improvement uses O(m + n) space, but still not the best solution.
>   	Could you devise a constant space solution?


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
let m = matrix.len();
let n = matrix[0].len();
let zero_rows: Vec<usize> = (0..m).into_iter()
.filter(|&i| matrix[i].contains(&0))
.collect();
let zero_cols: Vec<usize> = (0..n).into_iter()
.filter(|&j| (0..m).into_iter().map(|i| matrix[i][j]).collect::<Vec<i32>>().contains(&0))
.collect();
for &i in zero_rows.iter() {
matrix[i] = vec![0; n];
}
for &j in zero_cols.iter() {
for i in 0..m {
matrix[i][j] = 0;
}
}
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_73() {
let mut matrix = vec![vec![1,1,1],vec![1,0,1],vec![1,1,1]];
Solution::set_zeroes(&mut matrix);
assert_eq!(matrix, vec![vec![1,0,1],vec![0,0,0],vec![1,0,1]]);

let mut matrix = vec![vec![0,1,2,0],vec![3,4,5,2],vec![1,3,1,5]];
Solution::set_zeroes(&mut matrix);
assert_eq!(matrix, vec![vec![0,0,0,0],vec![0,4,5,0],vec![0,3,1,0]]);

}
}

```
