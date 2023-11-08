---
title: 1182. shortest distance to target color
date: '2022-07-17'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1182 shortest distance to target color
---


You are given an array colors, in which there are three colors: 1, 2 and 3.



You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.



 



 > Example 1:



 > Input: colors <TeX>=</TeX> [1,1,2,1,3,2,2,3,3], queries <TeX>=</TeX> [[1,3],[2,2],[6,1]]

 > Output: [3,0,3]

 > Explanation: 

 > The nearest 3 from index 1 is at index 4 (3 steps away).

 > The nearest 2 from index 2 is at index 2 itself (0 steps away).

 > The nearest 1 from index 6 is at index 3 (3 steps away).

 > Example 2:



 > Input: colors <TeX>=</TeX> [1,2], queries <TeX>=</TeX> [[0,3]]

 > Output: [-1]

 > Explanation: There is no 3 in the array.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> colors.length <TeX>\leq</TeX> 510^4

 > 1 <TeX>\leq</TeX> colors[i] <TeX>\leq</TeX> 3

 > 1 <TeX>\leq</TeX> queries.length <TeX>\leq</TeX> 510^4

 > queries[i].length <TeX>=</TeX><TeX>=</TeX> 2

 > 0 <TeX>\leq</TeX> queries[i][0] < colors.length

 > 1 <TeX>\leq</TeX> queries[i][1] <TeX>\leq</TeX> 3


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
    pub fn calculate_left_right_dp(colors: &Vec<i32>) -> Vec<Vec<i32>> {
        let n = colors.len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; 3]; n];
        dp[0] = if colors[0] == 1 {
            vec![0, -1, -1]
        } else if colors[0] == 2 {
            vec![-1, 0, -1]
        } else {
            vec![-1, -1, 0]
        };
        for i in 1..n {
            dp[i] = dp[i - 1].clone();
            if colors[i] == 1 {
                dp[i][0] = i as i32;
            } else if colors[i] == 2 {
                dp[i][1] = i as i32;
            } else {
                dp[i][2] = i as i32;
            }
        }
        dp
    }
    pub fn calculate_right_left_dp(colors: &Vec<i32>) -> Vec<Vec<i32>> {
        let n = colors.len();
        let mut dp: Vec<Vec<i32>> = vec![vec![0; 3]; n];
        dp[n - 1] = if colors[n - 1] == 1 {
            vec![n as i32 - 1, -1, -1]
        } else if colors[n - 1] == 2 {
            vec![-1, n as i32 - 1, -1]
        } else {
            vec![-1, -1, n as i32 - 1]
        };
        for i in (0..n - 1).rev() {
            dp[i] = dp[i + 1].clone();
            if colors[i] == 1 {
                dp[i][0] = i as i32;
            } else if colors[i] == 2 {
                dp[i][1] = i as i32;
            } else {
                dp[i][2] = i as i32;
            }
        }
        dp
    }
    pub fn shortest_distance_color(colors: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        // from left to right
        let left_right_dp = Self::calculate_left_right_dp(&colors);
        let right_left_dp = Self::calculate_right_left_dp(&colors);
        let mut res: Vec<i32> = vec![];
        for i in 0..queries.len() {
            let index = queries[i][0] as usize;
            let color_index = queries[i][1] as usize - 1;
            let left_right = left_right_dp[index][color_index];
            let right_left = right_left_dp[index][color_index];
            if left_right == -1 && right_left == -1 {
                res.push(-1);
            } else if left_right == - 1 {
                res.push(right_left as i32 - index as i32);
            } else if right_left == -1 {
                res.push(index as i32 - left_right as i32);
            } else {
                let result = i32::min(index as i32 - left_right as i32, right_left as i32 - index as i32);
                res.push(result);
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
    fn test_1168() {
        assert_eq!(Solution::shortest_distance_color(vec![1,1,2,1,3,2,2,3,3], vec![vec![1,3],vec![2,2],vec![6,1]]), vec![3,0,3]);
        assert_eq!(Solution::shortest_distance_color(vec![1,2], vec![vec![0,3]]), vec![-1]);
    }
}

```
