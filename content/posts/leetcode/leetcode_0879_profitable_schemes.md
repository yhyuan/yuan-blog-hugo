---
title: 879. Profitable Schemes
date: '2022-06-02'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0879. Profitable Schemes
---


There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

> Example 1:
> Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
> Output: 2
> Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
> In total, there are 2 schemes.
> Example 2:
> Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
> Output: 7
> Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
> There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
**Constraints:**
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100
> 0 <TeX>\leq</TeX> minProfit <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> group.length <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> group[i] <TeX>\leq</TeX> 100
> profit.length == group.length
> 0 <TeX>\leq</TeX> profit[i] <TeX>\leq</TeX> 100


## Solution
Let dp[members, minProfit, i] as the solution for members, minProfit, and the subarray [0, i].

i == 0. We only have one element.

minProfit is 0. We will have two choices: select or not select i if the members is  larger or equal than group[i]. If the members is smaller than group[i], we will only have 1 choice.

minProfit > 0: If minProfit is smaller or equal than profit[i] and members is larger or equal than group[i], we can choose i. So we will have one choice. Otherwise, the result is 0.


i > 0:

members < group[i]. This one can not be choose. The result will be as same as dp[i - 1][j][k].

MinProfit < profit[i]: We can take it. The problem is converted to dp[i][0][k - group[i]]. If we do not take it, the problem is still dp[i-1][j][k]

MinProfit >= profit[i]. We can take it. The problem is converted to dp[i][j - profit[i]][k - group[i]]. If we do not take it, the problem is still dp[i-1][j][k]




### Python
```python
class Solution:
def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
members = n
n = len(group)
dp = [[[0 for k in range(members + 1)] for j in range(minProfit + 1)] for i in range(n)]
for i in range(n):
if i == 0:
for j in range(minProfit + 1):
for k in range(members + 1):
if j == 0:
dp[i][j][k] = 2 if k >= group[i] else 1
else:
dp[i][j][k] = 1 if k >= group[i] and j <= profit[i] else 0
else:
for j in range(minProfit + 1):
for k in range(members + 1):
dp[i][j][k] = dp[i - 1][j][k]
if k < group[i]:
continue
if j < profit[i]:
dp[i][j][k] += dp[i - 1][0][k - group[i]]
else:
dp[i][j][k] += dp[i - 1][j - profit[i]][k - group[i]]
dp[i][j][k] = dp[i][j][k] % 1000000007
return dp[n - 1][minProfit][members]

```

memorized solution: Top - bottom solution.
```python
class Solution:
def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
members = n
@cache
def helper(members, minProfit, index):
res = 0
if members < group[index]:
res = 0
elif index == 0:
res = 1 if minProfit - profit[index] <= 0 else 0
else:
res = helper(members - group[index], minProfit - profit[index], index - 1)
if index == 0:
res += 1 if minProfit <= 0 else 0
else:
res += helper(members, minProfit, index - 1)
return res % (10 ** 9 + 7)

ans = helper(members, minProfit, len(group) - 1)
return ans
```