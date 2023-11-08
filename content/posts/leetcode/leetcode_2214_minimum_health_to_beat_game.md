---
title: 2214. Minimum Health to Beat Game
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2214. Minimum Health to Beat Game
---


You are playing a game that has n levels numbered from 0 to n - 1. You are given a 0-indexed integer array damage where damage[i] is the amount of health you will lose to complete the ith level.

You are also given an integer armor. You may use your armor ability at most once during the game on any level which will protect you from at most armor damage.

You must complete the levels in order and your health must be greater than 0 at all times to beat the game.

Return the minimum health you need to start with to beat the game.

Example 1:

Input: damage <TeX>=</TeX> [2,7,4,3], armor <TeX>=</TeX> 4
Output: 13
Explanation: One optimal way to beat the game starting at 13 health is:
On round 1, take 2 damage. You have 13 - 2 <TeX>=</TeX> 11 health.
On round 2, take 7 damage. You have 11 - 7 <TeX>=</TeX> 4 health.
On round 3, use your armor to protect you from 4 damage. You have 4 - 0 <TeX>=</TeX> 4 health.
On round 4, take 3 damage. You have 4 - 3 <TeX>=</TeX> 1 health.
Note that 13 is the minimum health you need to start with to beat the game.

Example 2:

Input: damage <TeX>=</TeX> [2,5,3,4], armor <TeX>=</TeX> 7
Output: 10
Explanation: One optimal way to beat the game starting at 10 health is:
On round 1, take 2 damage. You have 10 - 2 <TeX>=</TeX> 8 health.
On round 2, use your armor to protect you from 5 damage. You have 8 - 0 <TeX>=</TeX> 8 health.
On round 3, take 3 damage. You have 8 - 3 <TeX>=</TeX> 5 health.
On round 4, take 4 damage. You have 5 - 4 <TeX>=</TeX> 1 health.
Note that 10 is the minimum health you need to start with to beat the game.

Example 3:

Input: damage <TeX>=</TeX> [3,3,3], armor <TeX>=</TeX> 0
Output: 10
Explanation: One optimal way to beat the game starting at 10 health is:
On round 1, take 3 damage. You have 10 - 3 <TeX>=</TeX> 7 health.
On round 2, take 3 damage. You have 7 - 3 <TeX>=</TeX> 4 health.
On round 3, take 3 damage. You have 4 - 3 <TeX>=</TeX> 1 health.
Note that you did not use your armor ability.

Constraints:

n <TeX><TeX>=</TeX><TeX>=</TeX></TeX> damage.length

1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 105

0 <TeX>\leq</TeX> damage[i] <TeX>\leq</TeX> 105

0 <TeX>\leq</TeX> armor <TeX>\leq</TeX> 105



## Solution
The question can be summarized that if we remove an element at index i  or reduce the armor at index i and calculate the sum. What is the minimal sum plus 1. We can calculate preSum firstly. preSum will help us calculate the sum between [i, j) quickly by using preSum[j] - preSum[i]. Then, we can go through each element, calculate the sum before i and the sum behind i, and the damage at i. Then, we find the min value of the sum.



### Python
```python
class Solution:
def minimumHealth(self, damage: List[int], armor: int) -> int:
preSum = [0]
n = len(damage)
for i in range(n):
preSum.append(preSum[-1] + damage[i])


# sum([i, j)) = preSum[j] - preSum[i]
ans = float('inf')
for i in range(n):


# use armor at i
healthBefore = preSum[i] - preSum[0]
healthAfter = preSum[n] - preSum[i + 1]
if damage[i] > armor:
ans = min(ans, healthBefore + (damage[i] - armor) + healthAfter)
else:
ans = min(ans, healthBefore + healthAfter)
return ans + 1
```
