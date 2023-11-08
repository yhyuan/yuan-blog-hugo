---
title: 54. spiral matrix
date: '2021-06-24'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0054 spiral matrix
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={54}/>
 

  Given an m x n matrix, return all elements of the matrix in spiral order.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

 >   Input: matrix <TeX>=</TeX> [[1,2,3],[4,5,6],[7,8,9]]

 >   Output: [1,2,3,6,9,8,7,4,5]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

 >   Input: matrix <TeX>=</TeX> [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

 >   Output: [1,2,3,4,8,12,11,10,9,5,6,7]

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> matrix.length

 >   	n <TeX>=</TeX><TeX>=</TeX> matrix[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 10

 >   	-100 <TeX>\leq</TeX> matrix[i][j] <TeX>\leq</TeX> 100


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn spiral_order_help(matrix: &Vec<Vec<i32>>, k: usize) -> Vec<i32> {
        let rows = matrix.len();
        let cols = matrix[0].len();
        //println!("rows: {}, cols: {}", rows, cols);
        //println!("k: {}, cols - 1 - k: {}", k, cols - 1 - k);

        let mut v1: Vec<i32> = if cols >= 2 * k + 1 {(k..=cols - 1 - k).into_iter().map(|j| matrix[k][j]).collect::<Vec<i32>>()} else {vec![]};
        let mut v2: Vec<i32> = if rows > 2 * k + 2 {(k + 1..rows - 1 - k).into_iter().map(|i| matrix[i][cols - 1 - k]).collect::<Vec<i32>>()} else {vec![]};
        let mut v3: Vec<i32> = if cols >= 2 * k + 1 {(k..=cols - 1 - k).into_iter().rev().map(|j| matrix[rows - 1 - k][j]).collect::<Vec<i32>>()} else {vec![]};
        let mut v4: Vec<i32> = if rows > 2 * k + 2 {(k + 1..rows - 1 - k).into_iter().rev().map(|i| matrix[i][k]).collect::<Vec<i32>>()} else {vec![]};
        v1.append(&mut v2);
        if rows != 2 * k + 1 {
            v1.append(&mut v3);
        }
        if cols != 2 * k + 1 {
            v1.append(&mut v4);
        }
        v1
    }

    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let rows = matrix.len();
        let cols = matrix[0].len();
        //let mut k = 0;
        let max_rows_cols = usize::max(rows, cols);
        let mut max_k = if max_rows_cols % 2 == 0 {max_rows_cols / 2} else {max_rows_cols / 2}; 
        let mut results: Vec<i32> = vec![];
        for k in 0..=max_k {
            let result = Solution::spiral_order_help(&matrix, k);
            for val in result {
                results.push(val);
            }
            if results.len() == rows * cols {
                break;
            }
        }
        //println!("results: {:?}", results);
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_54() {
        /*
        assert_eq!(
            Solution::spiral_order(vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]]),
            vec![1, 2, 3, 6, 9, 8, 7, 4, 5]
        );
        assert_eq!(Solution::spiral_order(vec![vec![1, 2, 3]]), vec![1, 2, 3]);
        
        assert_eq!(
            Solution::spiral_order(vec![vec![1], vec![2], vec![3],]),
            vec![1, 2, 3]
        );
        
        
        assert_eq!(Solution::spiral_order(vec![vec![1],]), vec![1]);
        assert_eq!(
            Solution::spiral_order(vec![vec![1, 2], vec![4, 5],]),
            vec![1, 2, 5, 4]
        );
        */
        assert_eq!(Solution::spiral_order(vec![vec![2,5,8],vec![4,0,-1]]), vec![2,5,8,-1,0,4]);
    }
}

```
