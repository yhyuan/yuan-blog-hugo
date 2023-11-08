---
title: 309. best time to buy and sell stock with cooldown
date: '2022-01-02'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0309 best time to buy and sell stock with cooldown
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={309}/>
 

  You are given an array prices where prices[i] is the price of a given stock on the i^th day.

  Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

  

  	After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

  

  Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

   

 >   Example 1:

  

 >   Input: prices <TeX>=</TeX> [1,2,3,0,2]

 >   Output: 3

 >   Explanation: transactions <TeX>=</TeX> [buy, sell, cooldown, buy, sell]

  

 >   Example 2:

  

 >   Input: prices <TeX>=</TeX> [1]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> prices.length <TeX>\leq</TeX> 5000

 >   	0 <TeX>\leq</TeX> prices[i] <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        //dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
        //dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        //dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
        //dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 2][k - 1][0] - prices[i])

        //dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        //dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        let n = prices.len();
        if n <= 1 {
            return 0;
        }
        let mut dp: Vec<(i32, i32)> = vec![(0, 0); n];
        dp[0] = (0, -prices[0]);
        dp[1] = (i32::max(dp[0].0, dp[0].1 + prices[1]), i32::max(dp[0].1, -prices[1]));
        for i in 2..n {
                dp[i] = (
                    i32::max(dp[i-1].0, dp[i-1].1 + prices[i]),i32::max(dp[i-1].1, dp[i-2].0 - prices[i])
                );
        }
        dp[n - 1].0
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_309() {
        assert_eq!(Solution::max_profit(vec![1,2,3,0,2]), 3);
    }
}

```
