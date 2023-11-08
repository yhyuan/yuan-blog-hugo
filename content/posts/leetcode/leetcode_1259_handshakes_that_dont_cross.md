---
title: 1259. Handshakes That Don't Cross
date: '2022-07-25'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 1259. Handshakes That Don't Cross
---


You are given an even number of people numPeople that stand around a circle and each person shakes hands with someone else so that there are numPeople / 2 handshakes total.

Return the number of ways these handshakes could occur such that none of the handshakes cross.

Since the answer could be very large, return it modulo 109 + 7.

> Example 1:
> Input: numPeople = 4
> Output: 2
> Explanation: There are two ways to do it, the first way is [(1,2),(3,4)] and the second one is [(2,3),(4,1)].
> Example 2:
> Input: numPeople = 6
> Output: 5
**Constraints:**
> 2 <TeX>\leq</TeX> numPeople <TeX>\leq</TeX> 1000
> numPeople is even.


## Solution
Solution: If the 1st person shake hands with person i (i >= 2 and i <TeX>\leq</TeX> n), the whole group is divided into two group. If the number of persons is odd, the result will be 0 and can be ignored.

One group has i - 2 persons and another group has n - i persons. If the number of persons is 0, we will simple calculate another group's result. If both of groups have more than 0 persons, we will calculate both group's results and multiple them together.



### Python
```python
class Solution:
def numberOfWays(self, numPeople: int) -> int:
memo = {}
def helper(n):
if n == 0:
return 0
if n == 2:
return 1
if n in memo:
return memo[n]
ans = 0
for i in range(2, n + 1):
if (i - 2) % 2 == 0:
res1 = helper(i - 2)
res2 = helper(n - i)
if res1 == 0:
ans += res2
elif res2 == 0:
ans += res1
else:
ans += res1 * res2
memo[n] = ans % 1000000007
return memo[n]
return helper(numPeople)
```
