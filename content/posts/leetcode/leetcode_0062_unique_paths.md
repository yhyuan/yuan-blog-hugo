---
title: 62. unique paths
date: '2021-07-02'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0062 unique paths
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={62}/>
 

  A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

  The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

  How many possible unique paths are there?

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

 >   Input: m <TeX>=</TeX> 3, n <TeX>=</TeX> 7

 >   Output: 28

  

 >   Example 2:

  

 >   Input: m <TeX>=</TeX> 3, n <TeX>=</TeX> 2

 >   Output: 3

 >   Explanation:

 >   From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

 >   1. Right -> Down -> Down

 >   2. Down -> Down -> Right

 >   3. Down -> Right -> Down

  

 >   Example 3:

  

 >   Input: m <TeX>=</TeX> 7, n <TeX>=</TeX> 3

 >   Output: 28

  

 >   Example 4:

  

 >   Input: m <TeX>=</TeX> 3, n <TeX>=</TeX> 3

 >   Output: 6

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 100

 >   	It's guaranteed that the answer will be less than or equal to 2  10^9.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let mut table: Vec<Vec<i32>> = vec![vec![0; n]; m];
        for i in 0..m {
            table[i][0] = 1;
        }
        for i in 0..n {
            table[0][i] = 1;
        }
        for i in 1..m {
            for j in 1..n {
                table[i][j] = table[i - 1][j] + table[i][j - 1];
            }
        }
        table[m - 1][n - 1]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_62() {
        assert_eq!(Solution::unique_paths(7, 3), 28);
        assert_eq!(Solution::unique_paths(3, 7), 28);
        assert_eq!(Solution::unique_paths(1, 1), 1);
        assert_eq!(Solution::unique_paths(2, 2), 2);
        assert_eq!(Solution::unique_paths(36, 7), 4496388);
    }
}

```
