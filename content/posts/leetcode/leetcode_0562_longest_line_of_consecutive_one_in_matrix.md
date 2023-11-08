---
title: 562. longest line of consecutive one in matrix
date: '2022-04-04'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0562 longest line of consecutive one in matrix
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={562}/>

Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.



The line could be horizontal, vertical, diagonal, or anti-diagonal.



 



 > Example 1:





 > Input: mat <TeX>=</TeX> [[0,1,1,0],[0,1,1,0],[0,0,0,1]]

 > Output: 3

 > Example 2:





 > Input: mat <TeX>=</TeX> [[1,1,1,1],[0,1,1,0],[0,0,0,1]]

 > Output: 4

 



**Constraints:**



 > m <TeX>=</TeX><TeX>=</TeX> mat.length

 > n <TeX>=</TeX><TeX>=</TeX> mat[i].length

 > 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 104

 > 1 <TeX>\leq</TeX> m  n <TeX>\leq</TeX> 104

 > mat[i][j] is either 0 or 1.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
    pub fn longest_line(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut res = i32::MIN;
        // Horizontal
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                if j == 0 {
                    dp[i][j] = if mat[i][j] == 1 {1} else {0};
                } else {
                    dp[i][j] = if mat[i][j] == 1 {dp[i][j - 1] + 1} else {0};
                }
                res = i32::max(res, dp[i][j]);
            }
        }
        // Vertical
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                if i == 0 {
                    dp[i][j] = if mat[i][j] == 1 {1} else {0};
                } else {
                    dp[i][j] = if mat[i][j] == 1 {dp[i - 1][j] + 1} else {0};
                }
                res = i32::max(res, dp[i][j]);
            }
        }

        // Diagonal
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                if i == 0 || j == 0 {
                    dp[i][j] = if mat[i][j] == 1 {1} else {0};
                } else {
                    dp[i][j] = if mat[i][j] == 1 {dp[i - 1][j - 1] + 1} else {0};
                }
                res = i32::max(res, dp[i][j]);
            }
        }

        // Anti-Diagonal
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        for i in 0..m {
            for j in (0..n).rev() {
                if i == 0 || j == n - 1 {
                    dp[i][j] = if mat[i][j] == 1 {1} else {0};
                } else {
                    dp[i][j] = if mat[i][j] == 1 {dp[i - 1][j + 1] + 1} else {0};
                }
                res = i32::max(res, dp[i][j]);
            }
        }
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_562() {
        assert_eq!(Solution::longest_line(vec![vec![0,1,1,0],vec![0,1,1,0],vec![0,0,0,1]]), 3);
        assert_eq!(Solution::longest_line(vec![vec![1,1,1,1],vec![0,1,1,0],vec![0,0,0,1]]), 4);
    }
}

```
