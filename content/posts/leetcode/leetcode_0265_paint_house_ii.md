---
title: 265. paint house ii
date: '2021-12-07'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0265 paint house ii
---


There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.



The cost of painting each house with a certain color is represented by an n x k cost matrix costs.



For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...

Return the minimum cost to paint all houses.







> Example 1:
> Input: costs <TeX>=</TeX> [[1,5,3],[2,9,4]]
> Output: 5
> Explanation:
> Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 <TeX>=</TeX> 5;
> Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 <TeX>=</TeX> 5.
> Example 2:
> Input: costs <TeX>=</TeX> [[1,3],[2,4]]
> Output: 5
**Constraints:**
> costs.length <TeX>=</TeX><TeX>=</TeX> n
> costs[i].length <TeX>=</TeX><TeX>=</TeX> k
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100
> 2 <TeX>\leq</TeX> k <TeX>\leq</TeX> 20
> 1 <TeX>\leq</TeX> costs[i][j] <TeX>\leq</TeX> 20
> Follow up: Could you solve it in O(nk) runtime?


## Solution


### Rust
```rust
pub struct Solution {}

impl Solution {
pub fn min_cost_ii(costs: Vec<Vec<i32>>) -> i32 {
let n = costs.len();
let k = costs[0].len();
let mut dp: Vec<Vec<i32>> = vec![vec![0; k]; n];
dp[0] = costs[0].clone();
for i in 1..n {
for j in 0..k {
dp[i][j] = (0..k).into_iter()
.filter(|&m| m != j)
.map(|m| dp[i - 1][m])
.min().unwrap() + costs[i][j];
}
}
*dp[n - 1].iter().min().unwrap()
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_265() {
assert_eq!(Solution::min_cost_ii(vec![vec![1,5,3],vec![2,9,4]]), 5);
}
}

```
