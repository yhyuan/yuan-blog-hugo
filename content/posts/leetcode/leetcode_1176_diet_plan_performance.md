---
title: 1176. Diet Plan Performance
date: '2022-07-16'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 1176. Diet Plan Performance
---


A dieter consumes calories[i] calories on the i-th day. 

Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <TeX>\leq</TeX> i <TeX>\leq</TeX> n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):

If T <TeX>\leq</TeX> lower, they performed poorly on their diet and lose 1 point; 
If T <TeX>></TeX> upper, they performed well on their diet and gain 1 point;
Otherwise, they performed normally and there is no change in points.
Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.

Note that the total points can be negative.

 

 > Example 1:

 > Input: calories <TeX>=</TeX> [1,2,3,4,5], k <TeX>=</TeX> 1, lower <TeX>=</TeX> 3, upper <TeX>=</TeX> 3
 > Output: 0
 > Explanation: Since k <TeX>=</TeX> 1, we consider each element of the array separately and compare it to lower and upper.
 > calories[0] and calories[1] are less than lower so 2 points are lost.
 > calories[3] and calories[4] are greater than upper so 2 points are gained.
 > Example 2:

 > Input: calories <TeX>=</TeX> [3,2], k <TeX>=</TeX> 2, lower <TeX>=</TeX> 0, upper <TeX>=</TeX> 1
 > Output: 1
 > Explanation: Since k <TeX>=</TeX> 2, we consider subarrays of length 2.
 > calories[0] + calories[1] > upper so 1 point is gained.
 > Example 3:

 > Input: calories <TeX>=</TeX> [6,5,0,0], k <TeX>=</TeX> 2, lower <TeX>=</TeX> 1, upper <TeX>=</TeX> 5
 > Output: 0
 > Explanation:
 > calories[0] + calories[1] > upper so 1 point is gained.
 > lower <TeX>\leq</TeX> calories[1] + calories[2] <TeX>\leq</TeX> upper so no change in points.
 > calories[2] + calories[3] < lower so 1 point is lost.
 

Constraints:

 > 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> calories.length <TeX>\leq</TeX> 10^5
 > 0 <TeX>\leq</TeX> calories[i] <TeX>\leq</TeX> 20000
 > 0 <TeX>\leq</TeX> lower <TeX>\leq</TeX> upper

## Solution
use Pre_sum to calculate the total from 0 to k. Then, make the calculation of i to i + k - 1 easy. 
### Python
```python
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        pre_sum = []
        n = len(calories)
        total = 0
        for i in range(n):
            total += calories[i]
            pre_sum.append(total)
        points = 0
        for i in range(n - k + 1):
            total = pre_sum[k - 1] if i == 0 else pre_sum[i + k - 1] - pre_sum[i - 1]
            if total > upper:
                points += 1
            elif total < lower:
                points -= 1
        return points
```
