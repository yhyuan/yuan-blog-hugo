---
title: 566. reshape the matrix
date: '2022-04-05'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0566 reshape the matrix
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={566}/>
 

  In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

  You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

  The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

  If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg)

 >   Input: mat <TeX>=</TeX> [[1,2],[3,4]], r <TeX>=</TeX> 1, c <TeX>=</TeX> 4

 >   Output: [[1,2,3,4]]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg)

 >   Input: mat <TeX>=</TeX> [[1,2],[3,4]], r <TeX>=</TeX> 2, c <TeX>=</TeX> 4

 >   Output: [[1,2],[3,4]]

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> mat.length

 >   	n <TeX>=</TeX><TeX>=</TeX> mat[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 100

 >   	-1000 <TeX>\leq</TeX> mat[i][j] <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> r, c <TeX>\leq</TeX> 300


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn matrix_reshape(mat: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        let r = r as usize;
        let c = c as usize;
        let rows = mat.len();
        let cols = mat[0].len();
        if r*c != rows*cols {
            return mat;
        }
        let mut result: Vec<Vec<i32>> = vec![vec![0; c]; r];
        let mut k = 0usize;
        for i in 0..rows {
            for j in 0..cols {
                let k = i * cols + j;
                result[k / c][ k % c] = mat[i][j];
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
    fn test_566() {
    }
}

```
