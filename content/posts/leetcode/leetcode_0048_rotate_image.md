---
title: 48. rotate image
date: '2021-06-18'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0048 rotate image
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={48}/>
 

  You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

  You have to rotate the image [in-place](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

 >   Input: matrix <TeX>=</TeX> [[1,2,3],[4,5,6],[7,8,9]]

 >   Output: [[7,4,1],[8,5,2],[9,6,3]]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

 >   Input: matrix <TeX>=</TeX> [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

 >   Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

  

 >   Example 3:

  

 >   Input: matrix <TeX>=</TeX> [[1]]

 >   Output: [[1]]

  

 >   Example 4:

  

 >   Input: matrix <TeX>=</TeX> [[1,2],[3,4]]

 >   Output: [[3,1],[4,2]]

  

   

  **Constraints:**

  

 >   	matrix.length <TeX>=</TeX><TeX>=</TeX> n

 >   	matrix[i].length <TeX>=</TeX><TeX>=</TeX> n

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 20

 >   	-1000 <TeX>\leq</TeX> matrix[i][j] <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        // if n is odd, the (i, j) -> (j, n - 1 - i) -> (n - 1 - i, n - 1 - j) -> (n - 1 - j, i)
        if n % 2 == 0 {
            for i in 0..=(n - 1) / 2 {
                for j in 0..=(n - 1) / 2 {
                    let temp = matrix[i][j];
                    //println!("temp: {}", temp);
                    matrix[i][j] = matrix[n - 1 - j][i];
                    matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                    matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                    matrix[j][n - 1 - i] = temp;
                }
            }    
        } else {
            for i in 0..=(n - 1) / 2 {
                for j in 0..(n - 1) / 2 {
                    let temp = matrix[i][j];
                    //println!("temp: {}", temp);
                    matrix[i][j] = matrix[n - 1 - j][i];
                    matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                    matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                    matrix[j][n - 1 - i] = temp;
                }
            }
        }
        
    }
}
*/
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        for i in 0.. n {
            for j in 0..=n - 1 - i {
                let temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][n - 1 - i];
                matrix[n - 1 - j][n - 1 - i] = temp;
                //println!("i: {}, j: {} => i: {}, j: {}", i, j, n - 1 - j, n - 1 - i);
            }
        }
        //println!("matrix: {:?}", matrix);
        for i in 0..n/2 {
            for j in 0..n {
                let temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - i][j];
                matrix[n - 1 - i][j] = temp;
            }
        }
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_48() {
        /*
        let mut matrix = vec![
            vec![5, 1, 9, 11],
            vec![2, 4, 8, 10],
            vec![13, 3, 6, 7],
            vec![15, 14, 12, 16],
        ];
        Solution::rotate(&mut matrix);
        assert_eq!(
            matrix,
            vec![
                vec![15, 13, 2, 5],
                vec![14, 3, 4, 1],
                vec![12, 6, 8, 9],
                vec![16, 7, 10, 11]
            ]
        );
        */
        let mut matrix = vec![
            vec![1, 2, 3],
            vec![4, 5, 6],
            vec![7, 8, 9],
        ];
        Solution::rotate(&mut matrix);
        assert_eq!(
            matrix,
            vec![vec![7,4,1],vec![8,5,2],vec![9,6,3]]
        );

    }
}

```
