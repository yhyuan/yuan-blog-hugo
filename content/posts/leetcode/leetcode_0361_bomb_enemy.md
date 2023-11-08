---
title: 361. bomb enemy
date: '2022-01-25'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0361 bomb enemy
---


Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.



The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.



 



 > Example 1:





 > Input: grid <TeX>=</TeX> [['0','E','0','0'],['E','0','W','E'],['0','E','0','0']]

 > Output: 3

 > Example 2:





 > Input: grid <TeX>=</TeX> [['W','W','W'],['0','0','0'],['E','E','E']]

 > Output: 1

 



**Constraints:**



 > m <TeX>=</TeX><TeX>=</TeX> grid.length

 > n <TeX>=</TeX><TeX>=</TeX> grid[i].length

 > 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 500

 > grid[i][j] is either 'W', 'E', or '0'.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
    pub fn calculate_up_dp(grid: &Vec<Vec<char>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        dp[0] = grid[0].iter().map(|&ch| if ch == 'E' {1} else {0}).collect::<Vec<_>>();
        for i in 1..m {
            for j in 0..n {
                dp[i][j] = if grid[i][j] == 'W' {
                    0
                } else if grid[i][j] == 'E'{
                    dp[i - 1][j] + 1
                } else {
                    dp[i - 1][j]
                };
            }
        }
        dp
    }
    pub fn calculate_down_dp(grid: &Vec<Vec<char>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        dp[m - 1] = grid[m - 1].iter().map(|&ch| if ch == 'E' {1} else {0}).collect::<Vec<_>>();
        for i in (0..m - 1).rev() {
            for j in 0..n {
                dp[i][j] = if grid[i][j] == 'W' {
                    0
                } else if grid[i][j] == 'E'{
                    dp[i + 1][j] + 1
                } else {
                    dp[i + 1][j]
                };
            }
        }
        dp
    }

    pub fn calculate_left_dp(grid: &Vec<Vec<char>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                if j == 0 {
                    dp[i][j] = if grid[i][j] == 'E'{
                        1
                    } else {
                        0
                    };
                } else {
                    dp[i][j] = if grid[i][j] == 'W' {
                        0
                    } else if grid[i][j] == 'E'{
                        dp[i][j - 1] + 1
                    } else {
                        dp[i][j - 1]
                    };    
                }
            }
        }
        dp
    }

    pub fn calculate_right_dp(grid: &Vec<Vec<char>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; m];
        for i in 0..m {
            dp[i][n - 1] == if grid[i][n - 1] == 'E' {1} else {0};
        }
        for i in 0..m {
            for j in (0..n).rev() {
                if j == n - 1 {
                    dp[i][j] = if grid[i][j] == 'E'{
                        1
                    } else {
                        0
                    };
                } else {
                    dp[i][j] = if grid[i][j] == 'W' {
                        0
                    } else if grid[i][j] == 'E'{
                        dp[i][j + 1] + 1
                    } else {
                        dp[i][j + 1]
                    };
                }
            }
        }
        dp
    }

    pub fn max_killed_enemies(grid: Vec<Vec<char>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let up_dp = Self::calculate_up_dp(&grid);
        let left_dp = Self::calculate_left_dp(&grid);
        let down_dp = Self::calculate_down_dp(&grid);
        let right_dp = Self::calculate_right_dp(&grid);
        let mut res = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == '0' {
                    res = i32::max(res, 
                        up_dp[i][j] + left_dp[i][j] + down_dp[i][j] + right_dp[i][j]);
                }
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
    fn test_361() {
        assert_eq!(Solution::max_killed_enemies(vec![vec!['0','E','0','0'],vec!['E','0','W','E'],vec!['0','E','0','0']]), 3);
        assert_eq!(Solution::max_killed_enemies(vec![vec!['W','W','W'],vec!['0','0','0'],vec!['E','E','E']]), 1);
    }
}

```
