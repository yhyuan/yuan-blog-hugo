---
title: 1884. egg drop with 2 eggs and n floors
date: '2022-08-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1884 egg drop with 2 eggs and n floors
---



You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <TeX>\leq</TeX> f <TeX>\leq</TeX> n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

In each move, you may take an unbroken egg and drop it from any floor x (where 1 <TeX>\leq</TeX> x <TeX>\leq</TeX> n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.



>   Example 1:
>   Input: n <TeX>=</TeX> 2
>   Output: 2
>   Explanation: We can drop the first egg from floor 1 and the second egg from floor 2.
>   If the first egg breaks, we know that f <TeX>=</TeX> 0.
>   If the second egg breaks but the first egg didn't, we know that f <TeX>=</TeX> 1.
>   Otherwise, if both eggs survive, we know that f <TeX>=</TeX> 2.
>   Example 2:
>   Input: n <TeX>=</TeX> 100
>   Output: 14
>   Explanation: One optimal strategy is:
>   - Drop the 1st egg at floor 9. If it breaks, we know f is between 0 and 8. Drop the 2nd egg starting
>     from floor 1 and going up one at a time to find f within 7 more drops. Total drops is 1 + 7 <TeX>=</TeX> 8.
>   - If the 1st egg does not break, drop the 1st egg again at floor 22. If it breaks, we know f is between 9
>     and 21. Drop the 2nd egg starting from floor 10 and going up one at a time to find f within 12 more
>     drops. Total drops is 2 + 12 <TeX>=</TeX> 14.
>   - If the 1st egg does not break again, follow a similar process dropping the 1st egg from floors 34, 45,
>     55, 64, 72, 79, 85, 90, 94, 97, 99, and 100.
>   Regardless of the outcome, it takes at most 14 drops to determine f.
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000


## Solution
Solution:

Let's assume we have k eggs and n floors.

Base case n <TeX>=</TeX> 0: the result will be 0.

Base case k <TeX>=</TeX> 1: we have try every floor and under the worst scenario, we have to try n times.

From 1st to nth floor, we try each floor i:

It may break at i th floor. We lost one egg and have i - 1 floors to try. The case becomes (k - 1, i - 1)

It does not break at i th floor. We still have k eggs and we have n - i floors to try. The floors starts and i + 1 and ends with n. The total number of floors is n - (i + 1) + 1 <TeX>=</TeX> n - i

under the worst scenario, the result will be max(dp[(k - 1, i - 1)], dp[(k, n - i)]) + 1 because we just had one drop.

The minimal value for the step 3 will be the final result.

Step 3 currently is using linear search. However, we can improve it by using binary search because broken is an increasing function and unbroken is a decreasing function with the change of i.



### Python
```
class Solution:
def twoEggDrop(self, n: int) -> int:
def helper(k, n, memo):
if n == 0: return 0
if k == 1: return n
if (k, n) in memo:
return memo[(k, n)]
ans = float('inf')
'''
for i in range(1, n + 1):
broken= helper(k - 1, i - 1, memo)
unbroken = helper(k, n - i, memo)
res = 1 + max(broken, unbroken)
ans = min(ans, res)
'''
lo, hi = 1, n
while lo <= hi:
mid = (lo + hi) // 2
broken=helper(k-1, mid - 1, memo)
unbroken = helper(k, n-mid, memo)
if broken > unbroken:
hi = mid - 1
ans = min(ans, broken + 1)
else:
lo = mid + 1
ans = min(ans, unbroken + 1)
memo[(k, n)] = ans
return ans
memo = {}
return helper(2, n, memo)
```


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn two_egg_drop(n: i32) -> i32 {
//Calculate the root of k^2 + k - 2 * n = 0
let a = 1;
let b = 1;
let c = -2 * n;
let mut temp = (b * b - 4 * a * c) as f64;
temp = temp.sqrt();
let k =(temp - b as f64) / (2f64 * a as f64);
k.ceil() as i32
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1884() {
assert_eq!(Solution::two_egg_drop(2), 2);
assert_eq!(Solution::two_egg_drop(100), 14);
}
}

```
