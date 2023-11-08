---
title: 123. best time to buy and sell stock iii
date: '2021-08-30'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0123 best time to buy and sell stock iii
---



You are given an array prices where prices[i] is the price of a given stock on the i^th day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



>   Example 1:
>   Input: prices <TeX>=</TeX> [3,3,5,0,0,3,1,4]
>   Output: 6
>   Explanation: Buy on day 4 (price <TeX>=</TeX> 0) and sell on day 6 (price <TeX>=</TeX> 3), profit <TeX>=</TeX> 3-0 <TeX>=</TeX> 3.
>   Then buy on day 7 (price <TeX>=</TeX> 1) and sell on day 8 (price <TeX>=</TeX> 4), profit <TeX>=</TeX> 4-1 <TeX>=</TeX> 3.
>   Example 2:
>   Input: prices <TeX>=</TeX> [1,2,3,4,5]
>   Output: 4
>   Explanation: Buy on day 1 (price <TeX>=</TeX> 1) and sell on day 5 (price <TeX>=</TeX> 5), profit <TeX>=</TeX> 5-1 <TeX>=</TeX> 4.
>   Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
>   Example 3:
>   Input: prices <TeX>=</TeX> [7,6,4,3,1]
>   Output: 0
>   Explanation: In this case, no transaction is done, i.e. max profit <TeX>=</TeX> 0.
>   Example 4:
>   Input: prices <TeX>=</TeX> [1]
>   Output: 0
**Constraints:**
>   	1 <TeX>\leq</TeX> prices.length <TeX>\leq</TeX> 10^5
>   	0 <TeX>\leq</TeX> prices[i] <TeX>\leq</TeX> 10^5


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
pub fn find_rightest_peak_index(prices: &Vec<i32>) -> usize {
let mut index = prices.len() - 1;
while index >= 1 && prices[index] <= prices[index - 1] {
index -= 1;
}
index
}
pub fn max_profit(prices: Vec<i32>) -> i32 {
let n = prices.len();
if n <= 1 {
return 0;
}
let rightest_peak_index = Solution::find_rightest_peak_index(&prices);
let prices = &prices[0..=rightest_peak_index];
let n = rightest_peak_index + 1;
if n <= 1 {
return 0;
}
let mut dp: Vec<Vec<i32>> = vec![vec![0; n]; n];
for i in 0..n {
let mut min_price = prices[i];
for j in i + 1..n {
dp[i][j] = i32::max(dp[i][j - 1], i32::max(prices[j] - min_price, 0));
min_price = i32::min(min_price, prices[j]);
}
}
let mut result: i32 = i32::MIN;
for k in 0..n {
result = i32::max(result, dp[0][k] + dp[k][n - 1]);
}
result
}
}
*/
impl Solution {
pub fn max_profit(prices: Vec<i32>) -> i32 {
let mut t1_cost = std::i32::MAX;
let mut t2_cost = std::i32::MAX;
let mut t1_profit = 0;
let mut t2_profit = 0;
for x in prices {
t1_cost = t1_cost.min(x);
t1_profit = t1_profit.max(x - t1_cost);
t2_cost = t2_cost.min(x - t1_profit);
t2_profit = t2_profit.max(x - t2_cost);
}
t2_profit
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_123() {
assert_eq!(Solution::max_profit(vec![3,3,5,0,0,3,1,4]), 6);
assert_eq!(Solution::max_profit(vec![1,2,3,4,5]), 4);
assert_eq!(Solution::max_profit(vec![7,6,4,3,1]), 0);
assert_eq!(Solution::max_profit(vec![1]), 0);
}
}

```
