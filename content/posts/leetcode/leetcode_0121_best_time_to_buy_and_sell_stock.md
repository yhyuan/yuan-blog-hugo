---
title: 121. best time to buy and sell stock
date: '2021-08-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0121 best time to buy and sell stock
---

 

  You are given an array prices where prices[i] is the price of a given stock on the i^th day.

  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

   

 >   Example 1:

  

 >   Input: prices <TeX>=</TeX> [7,1,5,3,6,4]

 >   Output: 5

 >   Explanation: Buy on day 2 (price <TeX>=</TeX> 1) and sell on day 5 (price <TeX>=</TeX> 6), profit <TeX>=</TeX> 6-1 <TeX>=</TeX> 5.

 >   Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

  

 >   Example 2:

  

 >   Input: prices <TeX>=</TeX> [7,6,4,3,1]

 >   Output: 0

 >   Explanation: In this case, no transactions are done and the max profit <TeX>=</TeX> 0.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> prices.length <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> prices[i] <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
//Solution 1
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len() <= 1 {
            return 0;
        }
        let mut buy = 0usize; 
        let mut sell = 0usize;
        let mut max_profit = 0i32;
        while sell < prices.len() {
            if prices[sell] < prices[buy] {
                buy = sell;
            } else {
                let profit = prices[sell] - prices[buy];
                max_profit = i32::max(profit, max_profit);
            }
            sell += 1;
        }
        max_profit
    }
}
*/
// Solution 2
/*
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        if n <= 1 {
            return 0;
        }
        let mut table: Vec<i32> = vec![0; n];
        table[0] = 0;
        table[1] = i32::max(table[0], i32::max(prices[1] - prices[0], 0));
        let mut min_price =  i32::min(prices[0], prices[1]);
        for i in 2..n {
            table[i] = i32::max(table[i - 1], prices[i] - min_price);
            min_price = i32::min(min_price, prices[i]);
        }
        table[n - 1]
    }
}
*/
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // max_profit[n] = max(max_profit[n - 1], if prices[n] > min_price[n - 1] {prices[n] - min_price[n - 1]} else {0})
        let n = prices.len();
        if n == 1 {
            return 0;
        }
        let mut min_price = i32::min(prices[0], prices[1]);
        let mut max_profit = 0i32;
        for i in 1..n {
            // If we sold on day i, the max_profit will be prices[i] - min_price or 0.
            max_profit = i32::max(max_profit, if prices[i] > min_price {prices[i] - min_price} else {0});
            min_price = i32::min(min_price, prices[i]);
        }
        max_profit
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_121() {
        assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
        assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
        assert_eq!(Solution::max_profit(vec![2, 4, 1]), 2);
    }
}

```
