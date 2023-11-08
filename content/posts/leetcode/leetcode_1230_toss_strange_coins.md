---
title: 1230. toss strange coins
date: '2022-07-21'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1230 toss strange coins
---


You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.



Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.







> Example 1:
> Input: prob <TeX>=</TeX> [0.4], target <TeX>=</TeX> 1
> Output: 0.40000
> Example 2:
> Input: prob <TeX>=</TeX> [0.5,0.5,0.5,0.5,0.5], target <TeX>=</TeX> 0
> Output: 0.03125
**Constraints:**
> 1 <TeX>\leq</TeX> prob.length <TeX>\leq</TeX> 1000
> 0 <TeX>\leq</TeX> prob[i] <TeX>\leq</TeX> 1
> 0 <TeX>\leq</TeX> target <TeX>\leq</TeX> prob.length
> Answers will be accepted as correct if they are within 10^-5 of the correct answer.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
/*
Create a 2D array dp with length + 1 rows and target + 1 columns. The element at dp[i][j] stands for the probability
that after the first i coins are tossed, there are j coins facing heads.

Obviously, if no coin is tossed, then definitely no coin faces heads, which has a probability 1, so dp[0][0] = 1.
Each time a coin is tossed, the number of coins facing heads either remains the same or increase by 1, depending on
the current coin’s probability of facing heads. So the probability can be calculated. For the case j equals 0, dp[i][0]
only depends on prob[i - 1] and dp[i - 1][0]. For other cases, dp[i][j] depends on prob[i - 1], dp[i - 1][j - 1] and dp[i - 1][j].

Finally, return dp[length][target] for the result.
*/
//dp[i][j] := prob of j coins face up after tossing first i coins.
//dp[i][j] = dp[i-1][j] * (1 – p[i]) + dp[i-1][j-1] * p[i]
pub fn probability_of_heads(prob: Vec<f64>, target: i32) -> f64 {
let n = prob.len();
let target = target as usize;
// target p, n - target  (1-p)
let mut dp: Vec<Vec<f64>> = vec![vec![0f64; target + 1]; n + 1];
dp[0][0] = 1.0;
for i in 1..=n {
let cur_prob = prob[i - 1];
dp[i][0] = dp[i - 1][0] * (1.0f64 - cur_prob);
for j in 1..=target {
dp[i][j] = dp[i - 1][j] * (1.0f64 - cur_prob) + dp[i - 1][j - 1] * cur_prob;
}
}
// println!("{:?}", dp);
dp[n][target]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1230() {
assert_eq!(Solution::probability_of_heads(vec![1f64,1f64,1f64,1f64,1f64,1f64,1f64,1f64,1f64,1f64], 9), 0.0);
assert_eq!(Solution::probability_of_heads(vec![0.4], 1), 0.4);
assert_eq!(Solution::probability_of_heads(vec![0.5,0.5,0.5,0.5,0.5], 0), 0.03125);
}
}

```
