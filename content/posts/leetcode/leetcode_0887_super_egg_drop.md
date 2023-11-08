---
title: 887. super egg drop
date: '2022-06-04'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0887 super egg drop
---



You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <TeX>\leq</TeX> f <TeX>\leq</TeX> n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <TeX>\leq</TeX> x <TeX>\leq</TeX> n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.



>   Example 1:
>   Input: k <TeX>=</TeX> 1, n <TeX>=</TeX> 2
>   Output: 2
>   Explanation:
>   Drop the egg from floor 1. If it breaks, we know that f <TeX>=</TeX> 0.
>   Otherwise, drop the egg from floor 2. If it breaks, we know that f <TeX>=</TeX> 1.
>   If it does not break, then we know f <TeX>=</TeX> 2.
>   Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
>   Example 2:
>   Input: k <TeX>=</TeX> 2, n <TeX>=</TeX> 6
>   Output: 3
>   Example 3:
>   Input: k <TeX>=</TeX> 3, n <TeX>=</TeX> 14
>   Output: 4
**Constraints:**
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> 100
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
pub fn super_egg_drop_helper(k: i32, n: i32, memo: &mut HashMap<(i32, i32), i32>) -> i32 {
if k == 1i32 {
return n;
}
if n == 0i32 {
return 0i32;
}
if memo.contains_key(&(k, n)) {
return *memo.get(&(k, n)).unwrap();
}
let mut res = i32::MAX;
let (mut lo, mut hi) = (1, n);
while lo <= hi {
let mid = (lo + hi) / 2;
let broken = Self::super_egg_drop_helper(k - 1, mid - 1, memo);
let not_broken = Self::super_egg_drop_helper(k, n - mid, memo);
if broken > not_broken {
hi = mid - 1;
res = i32::min(res, broken + 1);
} else {
lo = mid + 1;
res = i32::min(res, not_broken + 1);
}
}

/*
println!("k: {}", k);
for i in 1..n + 1 {
let not_broken = Self::super_egg_drop_helper(k, n - i, memo);
let broken = Self::super_egg_drop_helper(k - 1, i - 1, memo);
println!("i: {}, k: {}, broken: {}, not broken: {}", i, k, broken, not_broken);
let val = i32::max(not_broken, broken);
res = i32::min(res, val + 1);
}
*/
memo.insert((k, n), res);
res
}

pub fn super_egg_drop(k: i32, n: i32) -> i32 {
// let k = k as usize;
// let n = n as usize;

let mut memo: HashMap<(i32, i32), i32> = HashMap::new();
Self::super_egg_drop_helper(k, n, &mut memo)
}
/*
pub fn super_egg_drop(k: i32, n: i32) -> i32 {
let k = k as usize;
let n = n as usize;
let mut dp = vec![vec![0i32; k + 1]; n + 1];
// Only one egg.
for i in 0..=n {
dp[i][1] = i as i32;
}
for j in 0..=k {
dp[0][j] = 0;
dp[1][j] = 1;
}
for i in 2..=n {
for j in 2..=k {
//Try i in different values
let result = (1..=i)
.into_iter()
.map(|k| i32::max(dp[k - 1][j - 1], dp[i - k][j]))
.min();
dp[i][j] = result.unwrap() + 1;
}
}
dp[n][k]
}
*/
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_887() {
assert_eq!(Solution::super_egg_drop(4, 5000), 19);
assert_eq!(Solution::super_egg_drop(1, 2), 2);
assert_eq!(Solution::super_egg_drop(2, 6), 3);
assert_eq!(Solution::super_egg_drop(3, 14), 4);
}
}

```
