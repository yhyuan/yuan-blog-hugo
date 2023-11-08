---
title: 634. Find the Derangement of An Array
date: '2022-04-10'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0634. Find the Derangement of An Array
---


n combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

You are given an integer n. There is originally an array consisting of n integers from 1 to n in ascending order, return the number of derangements it can generate. Since the answer may be huge, return it modulo 109 + 7.

> Example 1:
> Input: n = 3
> Output: 2
> Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
> Example 2:
> Input: n = 2
> Output: 1
**Constraints:**
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 106


## Solution
dp[n] is the result for n. We can reach dp[n] by using two approaches:

we have dp[n - 1]. Then, we pick one number in current result and switch with n in the last position. Obviously, none of them is in their original position. We have (n - 1) option and we will dp[n - 1] * (n - 1) possible results.

From 1 to n - 1, there is only one number in their position and n - 2 are not in their position, we can switch this number with n. There are n - 1 possible results and the total number of n - 2 are not in their position.  The result is dp[n - 2] * (n - 1).

So we can get dp[n] = dp[n - 1] * (n - 1) + dp[n - 2] * (n - 1).




### Python
```python
memo = {}
'''
def helper(n):
if n == 1: return 0
if n == 2: return 1
if n in memo: return memo[n]
ans = (n - 1) * (helper(n - 1) + helper(n - 2))
memo[n] = ans % 1000000007
return memo[n]
return helper(n)
'''
memo = {1: 0, 2: 1}
for i in range(3, n + 1):
memo[i] = (i - 1) * (memo[i - 1] + memo[i - 2]) % 1000000007
del memo[i - 2]
return memo[n]
```
