---
title: 983. Minimum Cost For Tickets
date: '2022-06-21'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0983. Minimum Cost For Tickets
---

 
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,

a 7-day pass is sold for costs[1] dollars, and

a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

 > Example 1:

 > Input: days = [1,4,6,7,8,20], costs = [2,7,15]
 > Output: 11
 > Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
 > On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
 > On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
 > On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
 > In total, you spent $11 and covered all the days of your travel.

 > Example 2:

 > Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
 > Output: 17
 > Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
 > On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
 > On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
 > In total, you spent $17 and covered all the days of your travel.

**Constraints:**

 > 1 <TeX>\leq</TeX> days.length <TeX>\leq</TeX> 365

 > 1 <TeX>\leq</TeX> days[i] <TeX>\leq</TeX> 365

 > days is in strictly increasing order.

 > costs.length == 3

 > 1 <TeX>\leq</TeX> costs[i] <TeX>\leq</TeX> 1000


## Solution
Let's define dp[i] as the result for the days starting at i to the end. So the final result will be dp[0]. At day i, we have three choices:

We choose 1 day plan. Then, we check the days to find the next index if 1 day is passed. 

 We choose 7 day plan. Then, we check the days to find the next index if 7 day is passed. 

We choose 30 day plan. Then, we check the days to find the next index if 30 day is passed.

If we have reached the end of days, the cost will be the plan's cost. Otherwise, it is plan cost plus the cost from next index to the end. We just choose the minimal value of three choices as the solution at i. 

### Python
```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def helper(i):
            n = len(days)
            if i in memo:
                return memo[i]
            def findIndex(i, addDay):
                day = days[i] + addDay
                for j in range(i, len(days)):
                    if days[j] >= day:
                        return j
                return len(days)
            nextIndex = findIndex(i, 1)
            res1 = costs[0] if nextIndex == n else costs[0] + helper(nextIndex) # 1 day plan
            nextIndex = findIndex(i, 7)
            res2 = costs[1] if nextIndex == n else costs[1] + helper(nextIndex) # 7 day plan
            nextIndex = findIndex(i, 30)
            res3 = costs[2] if nextIndex == n else costs[2] + helper(nextIndex) # 30 day plan
            ans = min([res1, res2, res3])
            memo[i] = ans
            return ans
        helper(0)
        return memo[0]

```
