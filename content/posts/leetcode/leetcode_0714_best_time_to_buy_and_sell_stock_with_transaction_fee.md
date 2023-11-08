---
title: 714. best time to buy and sell stock with transaction fee
date: '2022-04-29'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0714 best time to buy and sell stock with transaction fee
---

 

  You are given an array prices where prices[i] is the price of a given stock on the i^th day, and an integer fee representing a transaction fee.

  Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

  Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

   

 >   Example 1:

  

 >   Input: prices <TeX>=</TeX> [1,3,2,8,4,9], fee <TeX>=</TeX> 2

 >   Output: 8

 >   Explanation: The maximum profit can be achieved by:

 >   - Buying at prices[0] <TeX>=</TeX> 1

 >   - Selling at prices[3] <TeX>=</TeX> 8

 >   - Buying at prices[4] <TeX>=</TeX> 4

 >   - Selling at prices[5] <TeX>=</TeX> 9

 >   The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) <TeX>=</TeX> 8.

  

 >   Example 2:

  

 >   Input: prices <TeX>=</TeX> [1,3,7,5,10,3], fee <TeX>=</TeX> 3

 >   Output: 6

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> prices.length <TeX>\leq</TeX> 5  10^4

 >   	1 <TeX>\leq</TeX> prices[i] < 5  10^4

 >   	0 <TeX>\leq</TeX> fee < 5  10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        //dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
        //dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        let mut dp = (0, i32::MIN);
        let n = prices.len();
        for i in 0..n {
            dp = (
                i32::max(dp.0, if dp.1 == i32::MIN {i32::MIN} else {dp.1 + prices[i] - fee}),
                i32::max(dp.1, dp.0 - prices[i])
            );
        }
        dp.0
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_714() {
        assert_eq!(Solution::max_profit(vec![1,3,2,8,4,9], 2), 8);
    }
}

```
