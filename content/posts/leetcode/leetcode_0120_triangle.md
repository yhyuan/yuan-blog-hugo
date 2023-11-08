---
title: 120. triangle
date: '2021-08-27'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0120 triangle
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={120}/>
 

  Given a triangle array, return the minimum path sum from top to bottom.

  For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

   

 >   Example 1:

  

 >   Input: triangle <TeX>=</TeX> [[2],[3,4],[6,5,7],[4,1,8,3]]

 >   Output: 11

 >   Explanation: The triangle looks like:

 >      <u>2</u>

 >     <u>3</u> 4

 >    6 <u>5</u> 7

 >   4 <u>1</u> 8 3

 >   The minimum path sum from top to bottom is 2 + 3 + 5 + 1 <TeX>=</TeX> 11 (underlined above).

  

 >   Example 2:

  

 >   Input: triangle <TeX>=</TeX> [[-10]]

 >   Output: -10

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> triangle.length <TeX>\leq</TeX> 200

 >   	triangle[0].length <TeX>=</TeX><TeX>=</TeX> 1

 >   	triangle[i].length <TeX>=</TeX><TeX>=</TeX> triangle[i - 1].length + 1

 >   	-10^4 <TeX>\leq</TeX> triangle[i][j] <TeX>\leq</TeX> 10^4

  

   

 >   Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn minimum_total(triangle: Vec<Vec<i32>>) -> i32 {
        let n = triangle.len();
        let mut min_total: Vec<Vec<i32>> = vec![];
        for i in 0..n {
            min_total.push(vec![0; triangle[i].len()]);
        }
        min_total[0][0] = triangle[0][0];
        for i in 1..n {
            min_total[i][0] = min_total[i - 1][0] + triangle[i][0];
            min_total[i][i] = min_total[i - 1][i - 1] + triangle[i][i];
        }
        if n > 2 {
            for i in 2..n {
                for j in 1..i {
                    min_total[i][j] = triangle[i][j] + i32::min(min_total[i - 1][j - 1], min_total[i - 1][j]);
                }
            }    
        }
        (0..n).into_iter().map(|i| min_total[n - 1][i]).min().unwrap()
    }
}
*/

impl Solution {
    pub fn minimum_total(triangle: Vec<Vec<i32>>) -> i32 {
        let n = triangle.len();
        if n == 1 {
            return triangle[0][0];
        }
        let mut dp = vec![triangle[0][0]];
        for i in 1..n {
            let k = triangle[i].len();
            let mut next_dp = vec![0; k];
            next_dp[0] = dp[0]  + triangle[i][0];
            next_dp[k - 1] = dp[k - 2]  + triangle[i][k - 1];
            for j in 1..k - 1 {
                next_dp[j] = i32::min(dp[j - 1], dp[j]) + triangle[i][j];
            }            
            dp = next_dp;
        }
        *dp.iter().min().unwrap()
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_120() {
        assert_eq!(
            Solution::minimum_total(vec![vec![2], vec![3, 4], vec![6, 5, 7], vec![4, 1, 8, 3]]),
            11
        );
    }
}

```
