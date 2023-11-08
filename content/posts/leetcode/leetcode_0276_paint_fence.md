---
title: 276. paint fence
date: '2021-12-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0276 paint fence
---


You are painting a fence of n posts with k different colors. You must paint the posts following these rules:



Every post must be painted exactly one color.

There cannot be three or more consecutive posts with the same color.

Given the two integers n and k, return the number of ways you can paint the fence.







> Example 1:
> Input: n <TeX>=</TeX> 3, k <TeX>=</TeX> 2
> Output: 6
> Explanation: All the possibilities are shown.
> Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
> Example 2:
> Input: n <TeX>=</TeX> 1, k <TeX>=</TeX> 1
> Output: 1
> Example 3:
> Input: n <TeX>=</TeX> 7, k <TeX>=</TeX> 2
> Output: 42
**Constraints:**
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 50
> 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> 105
> The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k.


## Solution


### Rust
```rust
pub struct Solution {
}

impl Solution {
pub fn num_ways(n: i32, k: i32) -> i32 {
//dp[n].diff = dp[n - 1].same * (k - 1) + dp[n - 1].diff * (k - 1) = (dp[n - 1].same + dp[n - 1].diff) * (k - 1)
//dp[n].same = dp[n - 1].diff
if n == 0 || k == 0 {
return 0i32;
}
if n == 1 {
return k;
}
let mut dp = (k, k * (k - 1)); // same and differnt colors at n = 2
for _ in 3..=n {
dp = (dp.1, (dp.0 + dp.1)* (k - 1));
}
dp.0 + dp.1
}
}
// submission codes end



#[cfg(test)]
mod tests {
use crate::solution;

use super::*;



#[test]
fn test_276() {
assert_eq!( Solution::num_ways(3, 2), 6);
assert_eq!( Solution::num_ways(1, 1), 1);
assert_eq!( Solution::num_ways(7, 2), 42);
}
}

```
