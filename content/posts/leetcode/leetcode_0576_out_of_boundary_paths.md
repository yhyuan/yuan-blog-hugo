---
title: 576. out of boundary paths
date: '2022-04-08'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0576 out of boundary paths
---

 

  There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

  Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 10^9 + 7.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png)

 >   Input: m <TeX>=</TeX> 2, n <TeX>=</TeX> 2, maxMove <TeX>=</TeX> 2, startRow <TeX>=</TeX> 0, startColumn <TeX>=</TeX> 0

 >   Output: 6

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png)

 >   Input: m <TeX>=</TeX> 1, n <TeX>=</TeX> 3, maxMove <TeX>=</TeX> 3, startRow <TeX>=</TeX> 0, startColumn <TeX>=</TeX> 1

 >   Output: 12

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 50

 >   	0 <TeX>\leq</TeX> maxMove <TeX>\leq</TeX> 50

 >   	0 <TeX>\leq</TeX> startRow < m

 >   	0 <TeX>\leq</TeX> startColumn < n


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
//https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-576-out-of-boundary-paths/
impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        let k_mod = 1000000007;
        let m = m as usize;
        let n = n as usize;
        let max_move = max_move as usize;
        let start_row = start_row as usize;
        let start_column = start_column as usize;
        let mut dp: Vec<Vec<Vec<i32>>> = vec![vec![vec![0; n]; m]; max_move + 1];
        let dirs = vec![-1, 0, 1, 0, -1];
        for k in 1..=max_move {
            for i in 0..m {
                for j in 0..n {
                    for d in 0..4 {
                        let x = i as i32 + dirs[d];
                        let y = j as i32 + dirs[d + 1];
                        if x < 0 || y < 0 || x >= m as i32 || y >= n as i32 {
                            dp[k][i][j] += 1;
                        } else {
                            dp[k][i][j] = (dp[k][i][j] + dp[k - 1][x as usize][y as usize]) % k_mod;
                        }
                    }
                }
            }
        }
        dp[max_move][start_row][start_column]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_576() {
        assert_eq!(Solution::find_paths(2, 2, 2, 0, 0), 6);
        assert_eq!(Solution::find_paths(1, 3, 3, 0, 1), 12);
        assert_eq!(Solution::find_paths(10, 10, 0, 5, 5), 0);
    }
}

```
