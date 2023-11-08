---
title: 221. maximal square
date: '2021-11-07'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0221 maximal square
---

 

  Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)

 >   Input: matrix <TeX>=</TeX> [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

 >   Output: 4

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)

 >   Input: matrix <TeX>=</TeX> [["0","1"],["1","0"]]

 >   Output: 1

  

 >   Example 3:

  

 >   Input: matrix <TeX>=</TeX> [["0"]]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> matrix.length

 >   	n <TeX>=</TeX><TeX>=</TeX> matrix[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 300

 >   	matrix[i][j] is '0' or '1'.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
        let mut coordinates: Vec<(usize, usize)> = vec![];
        for i in 0..matrix.len() {
            let row = &matrix[i];
            for j in 0..row.len() {
                let ch = row[j];
                if ch == '1' {
                    coordinates.push((i, j));
                }
            }
        }
        if coordinates.len() == 0 {
            return 0;
        }
        let row_size = matrix.len();
        let column_size = matrix[0].len();
        let mut square_size = 1;
        loop {
            let mut new_coordinates: Vec<(usize, usize)> = vec![];
            for k in 0..coordinates.len() {
                let (i, j) = coordinates[k];
                if (i + square_size >= row_size) || (j + square_size >= column_size) {
                    continue;
                }
                let is_zero_inside = (i..=i + square_size).into_iter()
                    .map(|ii| matrix[ii][j + square_size])
                    .chain((j..=j + square_size).into_iter()
                    .map(|jj| matrix[i + square_size][jj])).find(|&x| x == '0');
                if is_zero_inside.is_none() {
                    new_coordinates.push((i, j));
                }
            }
            if new_coordinates.len() == 0 {
                return (square_size * square_size) as i32;
            }
            coordinates = new_coordinates;
            square_size += 1;
        }
    }
}
*/
impl Solution {
    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut dp_rows: Vec<Vec<i32>> = vec![vec![0; cols]; rows];
        for j in 0..cols {
            dp_rows[0][j] = if matrix[0][j] == '1' {1} else {0};
        }
        for i in 1..rows {
            for j in 0..cols {
                dp_rows[i][j] = if matrix[i][j] == '0' {
                    0
                } else {
                    1 + dp_rows[i - 1][j]
                };
            }
        }

        let mut dp_cols: Vec<Vec<i32>> = vec![vec![0; cols]; rows];
        for i in 0..rows {
            dp_cols[i][0] = if matrix[i][0] == '1' {1} else {0};
        }
        for j in 1..cols {
            for i in 0..rows {
                dp_cols[i][j] = if matrix[i][j] == '0' {
                    0
                } else {
                    1 + dp_cols[i][j - 1]
                };
            }
        }

        let mut dp: Vec<Vec<i32>> = vec![vec![0; cols]; rows];
        for j in 0..cols {
            dp[0][j] = if matrix[0][j] == '1' {1} else {0};
        }
        for i in 0..rows {
            dp[i][0] = if matrix[i][0] == '1' {1} else {0};
        }
        for i in 1..rows {
            for j in 1..cols {
                dp[i][j] = if matrix[i][j] == '0' {
                    0
                } else {
                    if matrix[i - 1][j - 1] == '0' {
                        1
                    } else {
                        i32::min(i32::min(dp_cols[i][j], dp_rows[i][j]), dp[i - 1][j - 1] + 1)
                    }
                };
            }
        }
        //println!("dp: {:?}", dp);
        let mut res = i32::MIN;
        for i in 0..rows {
            for j in 0..cols {
                res = i32::max(res, dp[i][j]);
            }
        }
        res * res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_221() {
        assert_eq!(
            Solution::maximal_square(vec![
                vec!['1', '0', '1', '0', '0'],
                vec!['1', '0', '1', '1', '1'],
                vec!['1', '1', '1', '1', '1'],
                vec!['1', '0', '0', '1', '0'],
            ]),
            4
        )
    }
}

```
