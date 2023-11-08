---
title: 1692. Count Ways to Distribute Candies
date: '2022-08-22'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 1692. Count Ways to Distribute Candies
---

 
There are n unique candies (labeled 1 through n) and k bags. You are asked to distribute all the candies into the bags such that every bag has at least one candy.

There can be multiple ways to distribute the candies. Two ways are considered different if the candies in one bag in the first way are not all in the same bag in the second way. The order of the bags and the order of the candies within each bag do not matter.

For example, (1), (2,3) and (2), (1,3) are considered different because candies 2 and 3 in the bag (2,3) in the first way are not in the same bag in the second way (they are split between the bags (2) and (1,3)). However, (1), (2,3) and (3,2), (1) are considered the same because the candies in each bag are all in the same bags in both ways.

Given two integers, n and k, return the number of different ways to distribute the candies. As the answer may be too large, return it modulo 109 + 7.

> Example 1:

> Input: n = 3, k = 2
> Output: 3
> Explanation: You can distribute 3 candies into 2 bags in 3 ways:
> (1), (2,3)
> (1,2), (3)
> (1,3), (2)

> Example 2:

> Input: n = 4, k = 2
> Output: 7
> Explanation: You can distribute 4 candies into 2 bags in 7 ways:
> (1), (2,3,4)
> (1,2), (3,4)
> (1,3), (2,4)
> (1,4), (2,3)
> (1,2,3), (4)
> (1,2,4), (3)
> (1,3,4), (2)

> Example 3:

> Input: n = 20, k = 5
> Output: 206085257
> Explanation: You can distribute 20 candies into 5 bags in 1881780996 ways. 1881780996 modulo 109 + 7 = 206085257.

**Constraints:**

> 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000


## Solution
Let's use dp[n][k] as the solution for n candies and k bag. The last candy n will have two possibilities. The result will be the sum of these two results.

It is located inside a bag with one candy. Then the remaining candies will be n - 1 and we will have k - 1 bags. The questions become dp[n - 1][k - 1].

It is located with other candies. Then, firstly solve the problem for dp[n - 1][k]. Then, we have pick one out of k bag and put the last candy in. So the result will be k * dp[n - 1][k].

Corn cases: 

n == k. We will put one candy in each bag. The result will be 1. 

k = 1. We will put all candies into one bag. The result will be 1. 

### Python
Top down approach
```python
class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        @cache
        def helper(n, k):
            if k == 1:
                return 1
            if n == k:
                return 1
            ans = helper(n - 1, k - 1) 
            ans += k * helper(n - 1, k)
            ans = ans % 1000000007
            return ans
        return helper(n, k)
```
Bottom up approach
```python
class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        dp = [1]
        for i in range(2, n + 1):
            next_dp = [1] * i # j = 0 and j == i - 1 are always 1. Other values are updated with the following loop. 
            for j in range(1, i - 1):
                next_dp[j] = (dp[j - 1] + (j + 1) * dp[j]) % 1000000007
            dp = next_dp
        return dp[k - 1]
```