---
title: 256. paint house
date: '2021-11-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0256 paint house
---


There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.



The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.



For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.







> Example 1:
> Input: costs <TeX>=</TeX> [[17,2,17],[16,16,5],[14,3,19]]
> Output: 10
> Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
> Minimum cost: 2 + 5 + 3 <TeX>=</TeX> 10.
> Example 2:
> Input: costs <TeX>=</TeX> [[7,6,2]]
> Output: 2
**Constraints:**
> costs.length <TeX>=</TeX><TeX>=</TeX> n
> costs[i].length <TeX>=</TeX><TeX>=</TeX> 3
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> costs[i][j] <TeX>\leq</TeX> 20


## Solution


### Rust
```rust
pub struct Solution {}

impl Solution {
pub fn min_cost(costs: Vec<Vec<i32>>) -> i32 {
let n = costs.len();
let mut dp: Vec<Vec<i32>> = vec![vec![0; 3]; n];
dp[0] = costs[0].clone();
for i in 1..n {
dp[i][0] = i32::min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0];
dp[i][1] = i32::min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1];
dp[i][2] = i32::min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2];
}
*dp[n - 1].iter().min().unwrap()
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_256() {
assert_eq!(Solution::min_cost(vec![vec![17,2,17],vec![16,16,5],vec![14,3,19]]), 10);
}
}

```
