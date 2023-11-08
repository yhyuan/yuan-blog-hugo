---
title: 188. best time to buy and sell stock iv
date: '2021-10-11'
tags: ['leetcode', 'rust', 'python', 'hard']
draft: false
description: Solution for leetcode 0188 best time to buy and sell stock iv
---



You are given an integer array prices where prices[i] is the price of a given stock on the i^th day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



>   Example 1:
>   Input: k <TeX>=</TeX> 2, prices <TeX>=</TeX> [2,4,1]
>   Output: 2
>   Explanation: Buy on day 1 (price <TeX>=</TeX> 2) and sell on day 2 (price <TeX>=</TeX> 4), profit <TeX>=</TeX> 4-2 <TeX>=</TeX> 2.
>   Example 2:
>   Input: k <TeX>=</TeX> 2, prices <TeX>=</TeX> [3,2,6,5,0,3]
>   Output: 7
>   Explanation: Buy on day 2 (price <TeX>=</TeX> 2) and sell on day 3 (price <TeX>=</TeX> 6), profit <TeX>=</TeX> 6-2 <TeX>=</TeX> 4. Then buy on day 5 (price <TeX>=</TeX> 0) and sell on day 6 (price <TeX>=</TeX> 3), profit <TeX>=</TeX> 3-0 <TeX>=</TeX> 3.
**Constraints:**
>   	0 <TeX>\leq</TeX> k <TeX>\leq</TeX> 100
>   	0 <TeX>\leq</TeX> prices.length <TeX>\leq</TeX> 1000
>   	0 <TeX>\leq</TeX> prices[i] <TeX>\leq</TeX> 1000


## Solution
At each day, we will calculate the profit of holding a stock and not holding stock (sold) if we have j opportunities to buy/sell the stock. We will define two array to store the state.

hold with size k + 1. hold[j] means that if we hold the stock at day i with j opportunities to buy or sell a stock.

sell with size k + 1. sell[j] means that if we do not hold the stock at day i with j opportunities to buy or sell a stock.

Analysis:

For sell[j] at day i,  it means that we are not holding the stock at day i. There two ways  to reach this state at day i. We can do nothing at day i. It means the value is sell[j]. We can also sell the stock at day i. It means the value is hold[j] + prices[i].  Since we count the transaction according to the time we buy the stock. It will be hold[j] rather than hold[j - 1]. It means that sell[j] = max(sell[j], hold[j]  + prices[i]). Please notice that sell[j] and hold[j] are the result for the previous day.

For hold[j] at day i, it means that we are holding the stock at day i. There two ways  to reach this state at day i. We can do nothing at day i. It means the value is hold[j]. We can also buy the stock at day i. It means the value is sell[j - 1] - prices[i].  Since we count the transaction according to the time we buy the stock. It will be sell[j - 1] rather than sell[j]. It means that hold[j] = max(hold[j], sell[j - 1]  - prices[i]). Please notice that sell[j - 1] and hold[j] are the result for the previous day.



### Python
```python
class Solution:
def maxProfit(self, k: int, prices: List[int]) -> int:
n = len(prices)
if n < 2: return 0
hold = [-float('inf')] * (k + 1)
sell = [0] * (k + 1)
for i in range(n):
for j in range(1, k + 1):
hold[j] = max(hold[j], sell[j - 1] - prices[i])
sell[j] = max(sell[j], hold[j] + prices[i])
return sell[k]
```


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
0
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_188() {
}
}

```
