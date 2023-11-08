---
title: 122. best time to buy and sell stock ii
date: '2021-08-29'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0122 best time to buy and sell stock ii
---



You are given an array prices where prices[i] is the price of a given stock on the i^th day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



>   Example 1:
>   Input: prices <TeX>=</TeX> [7,1,5,3,6,4]
>   Output: 7
>   Explanation: Buy on day 2 (price <TeX>=</TeX> 1) and sell on day 3 (price <TeX>=</TeX> 5), profit <TeX>=</TeX> 5-1 <TeX>=</TeX> 4.
>   Then buy on day 4 (price <TeX>=</TeX> 3) and sell on day 5 (price <TeX>=</TeX> 6), profit <TeX>=</TeX> 6-3 <TeX>=</TeX> 3.
>   Example 2:
>   Input: prices <TeX>=</TeX> [1,2,3,4,5]
>   Output: 4
>   Explanation: Buy on day 1 (price <TeX>=</TeX> 1) and sell on day 5 (price <TeX>=</TeX> 5), profit <TeX>=</TeX> 5-1 <TeX>=</TeX> 4.
>   Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
>   Example 3:
>   Input: prices <TeX>=</TeX> [7,6,4,3,1]
>   Output: 0
>   Explanation: In this case, no transaction is done, i.e., max profit <TeX>=</TeX> 0.
**Constraints:**
>   	1 <TeX>\leq</TeX> prices.length <TeX>\leq</TeX> 3  10^4
>   	0 <TeX>\leq</TeX> prices[i] <TeX>\leq</TeX> 10^4


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn max_profit(prices: Vec<i32>) -> i32 {
let mut result = 0i32;
for i in 1..prices.len() {
if prices[i] > prices[i - 1] {
result += prices[i] - prices[i - 1];
}
}
result
/*
let size = prices.len();
let mut cur = prices[0];
let mut prev = cur;
let mut low = prices[0];
let mut is_rising = false;
let mut total = 0i32;
for i in 1..size {
prev = cur;
cur = prices[i];
if cur > prev {
if !is_rising {
is_rising = true;
low = prev;
}
} else {
if is_rising {
is_rising = false;
let diff = prev - low;
total += diff;
}
}
}
if is_rising {
total += prices[size - 1] - low;
}
total
*/
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_122() {
assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 7);
assert_eq!(Solution::max_profit(vec![1, 2, 3, 4, 5]), 4);
}
}

```
