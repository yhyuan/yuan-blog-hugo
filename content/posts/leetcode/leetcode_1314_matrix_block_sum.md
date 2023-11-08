---
title: 1314. matrix block sum
date: '2022-07-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1314 matrix block sum
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1314}/>
 

  Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

  

  	i - k <TeX>\leq</TeX> r <TeX>\leq</TeX> i + k,

  	j - k <TeX>\leq</TeX> c <TeX>\leq</TeX> j + k, and

  	(r, c) is a valid position in the matrix.

  

   

 >   Example 1:

  

 >   Input: mat <TeX>=</TeX> [[1,2,3],[4,5,6],[7,8,9]], k <TeX>=</TeX> 1

 >   Output: [[12,21,16],[27,45,33],[24,39,28]]

  

 >   Example 2:

  

 >   Input: mat <TeX>=</TeX> [[1,2,3],[4,5,6],[7,8,9]], k <TeX>=</TeX> 2

 >   Output: [[45,45,45],[45,45,45],[45,45,45]]

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> mat.length

 >   	n <TeX>=</TeX><TeX>=</TeX> mat[i].length

 >   	1 <TeX>\leq</TeX> m, n, k <TeX>\leq</TeX> 100

 >   	1 <TeX>\leq</TeX> mat[i][j] <TeX>\leq</TeX> 100


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn get(mat: &Vec<Vec<i32>>, k: usize, i: usize, j: usize) -> i32 {
        let rows = mat.len();
        let cols = mat[0].len();

        if i >= k && j >= k && i < rows + k && j < cols + k {
            return mat[i - k][j - k];
        }
        0i32
    }
    pub fn matrix_block_sum(mat: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let rows = mat.len();
        let cols = mat[0].len();
        let k = k as usize;
        let mut res: Vec<Vec<i32>> = vec![];
        for i in k..rows + k {
            let mut row: Vec<i32> = vec![];
            for j in k..cols + k {
                if j == k {
                    let mut val = 0;
                    for m in i - k..=i + k {
                        for n in j - k..=j + k {
                            val += Self::get(&mat, k, m, n);
                        }
                    }
                    row.push(val);
                } else {
                    // remove col [j - k - 1], add col[j + k]
                    let mut removed = 0i32;
                    let mut added = 0i32;
                    for m in i - k..=i + k {
                        removed += Self::get(&mat, k,m, j - k - 1);
                        added += Self::get(&mat, k,m, j + k);
                    }
                    let last_val = row[row.len() - 1] - removed + added;
                    row.push(last_val);
                }
            }
            res.push(row);
        }
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1314() {
    }
}

```
