---
title: 746. min cost climbing stairs
date: '2022-05-08'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0746 min cost climbing stairs
---



You are given an integer array cost where cost[i] is the cost of i^th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



>   Example 1:
>   Input: cost <TeX>=</TeX> [10,15,20]
>   Output: 15
>   Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
>   Example 2:
>   Input: cost <TeX>=</TeX> [1,100,1,1,1,100,1,1,100,1]
>   Output: 6
>   Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
**Constraints:**
>   	2 <TeX>\leq</TeX> cost.length <TeX>\leq</TeX> 1000
>   	0 <TeX>\leq</TeX> cost[i] <TeX>\leq</TeX> 999


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
// f(n) = min(f(n - 1) + cost[n - 1], f(n - 2) + cost[n - 2])
pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
let n = cost.len();
let mut val = (0, 0);
for i in 2..=n {
val = (val.1, i32::min(val.0 + cost[i - 2], val.1 + cost[i - 1]));
}
val.1
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_746() {
assert_eq!(Solution::min_cost_climbing_stairs(vec![10, 15, 20]), 15);
assert_eq!(Solution::min_cost_climbing_stairs(vec![1,100,1,1,1,100,1,1,100,1]), 6);
}
}

```
