---
title: 1478. Allocate Mailboxes
date: '2022-08-09'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 1478. Allocate Mailboxes
---


Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The test cases are generated so that the answer fits in a 32-bit integer.

> Example 1:
> Input: houses <TeX>=</TeX> [1,4,8,10,20], k <TeX>=</TeX> 3
> Output: 5
> Explanation: Allocate mailboxes in position 3, 9 and 20.
> Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| <TeX>=</TeX> 5
> Example 2:
> Input: houses <TeX>=</TeX> [2,3,5,12,18], k <TeX>=</TeX> 2
> Output: 9
> Explanation: Allocate mailboxes in position 3 and 14.
> Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| <TeX>=</TeX> 9.
**Constraints:**
> 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> houses.length <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> houses[i] <TeX>\leq</TeX> 104
> All the integers of houses are unique.


## Solution
Let's start from simple case. If k = 1.

if n <TeX>=</TeX> 1, we simply will set the mail box at the only house. And the result will be 0.

if n <TeX>=</TeX> 2, we notice that if we set the mail box at the possible between two houses, we will gain the same result because one house's gain will be another house's loss. So we can simply set the mailbox at the begging house.

if n <TeX>=</TeX> 3, we will set the mailbox at the middle house.

if n <TeX>=</TeX> 4 we will set the mail box the left of the middle two houses.

So if k <TeX>=</TeX> 1, we will set the mailbox in the location of houses[n // 2].

Let's assume we are working between index start and index end and we have k mail box to set. We can set the leftest mailbox firstly. We can pick start, start + 1, start + 2, .... end. Then, we divide the whole question to two steps.

Set one mailbox between start and i.

set k - 1 mailbox between i + 1 and end.

And we want to find the i which make the result minimal. Meanwhile, we also add memo to cache the calculation result.


### Python
```python
class Solution:
def minDistance(self, houses: List[int], k: int) -> int:
n = len(houses)
houses.sort()
memo = {}
def helper(start, end, k):
if (start, end, k) in memo:
return memo[(start, end, k)]
if k == 1:
mid = (end + start) // 2
total = 0
for i in range(start, end + 1):
total += abs(houses[i] - houses[mid])
memo[(start, end, k)] = total
return total
result = float('inf')
for i in range(start, end + 1):
if end - i < k - 1:
break
result = min(result, helper(start, i, 1) + helper(i + 1, end, k - 1))
memo[(start, end, k)] = result
return result
return helper(0, n - 1, k)
```
