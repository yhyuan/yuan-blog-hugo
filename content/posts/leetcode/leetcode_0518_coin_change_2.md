---
title: 518. coin change 2
date: '2022-03-25'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0518 coin change 2
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={518}/>
 

  You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

  Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

  You may assume that you have an infinite number of each kind of coin.

  The answer is guaranteed to fit into a signed 32-bit integer.

   

 >   Example 1:

  

 >   Input: amount <TeX>=</TeX> 5, coins <TeX>=</TeX> [1,2,5]

 >   Output: 4

 >   Explanation: there are four ways to make up the amount:

 >   5<TeX>=</TeX>5

 >   5<TeX>=</TeX>2+2+1

 >   5<TeX>=</TeX>2+1+1+1

 >   5<TeX>=</TeX>1+1+1+1+1

  

 >   Example 2:

  

 >   Input: amount <TeX>=</TeX> 3, coins <TeX>=</TeX> [2]

 >   Output: 0

 >   Explanation: the amount of 3 cannot be made up just with coins of 2.

  

 >   Example 3:

  

 >   Input: amount <TeX>=</TeX> 10, coins <TeX>=</TeX> [10]

 >   Output: 1

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> coins.length <TeX>\leq</TeX> 300

 >   	1 <TeX>\leq</TeX> coins[i] <TeX>\leq</TeX> 5000

 >   	All the values of coins are unique.

 >   	0 <TeX>\leq</TeX> amount <TeX>\leq</TeX> 5000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let amount = amount as usize;
        //dp[k][i] is the answer for with the first k coins and amount i
        //dp[k][i] = dp[k - 1][i] + dp[k][i - coin] 
        //There are two possible to do it. The first is with this coin but less amount. 
        //The second one is the same amount, but fewer kinds of coins. 
        let mut dp: Vec<i32> = vec![0; amount + 1];
        dp[0] = 1;
        for coin in coins {
            for i in coin as usize..=amount {
                dp[i] =  dp[i - coin as usize] + dp[i]           
            }
        }
        dp[amount]
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_518() {
    }
}

```
