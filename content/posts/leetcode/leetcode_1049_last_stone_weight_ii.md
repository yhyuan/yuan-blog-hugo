---
title: 1049. Last Stone Weight II
date: '2022-07-03'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 1049. Last Stone Weight II
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1049}/>
 
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <TeX>\leq</TeX> y. The result of this smash is:

If x <TeX>==</TeX> y, both stones are destroyed, and

If x <TeX>\neq</TeX> y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:

Input: stones <TeX>=</TeX> [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:

Input: stones <TeX>=</TeX> [31,26,33,21,40]
Output: 5

**Constraints:**

1 <TeX>\leq</TeX> stones.length <TeX>\leq</TeX> 30

1 <TeX>\leq</TeX> stones[i] <TeX>\leq</TeX> 100


## Solution
Let's assume we pick a1, a2 and get a1 - a2. Then, we pick a3 and a4, we get a3 - a4. Then, we get (a1 - a2) - (a3 - a4) = a1 - a2 - a3 + a4. We can repeat the process. We realize that we basically just add + and - sign for different elements and add them together. We can group the elements with + sign together and - sign together. We basically just divide the elements into two groups and try to minimize the differences. We can use dynamic programming to figure out the possible values. Let's assume we can get dp[i] at i index. In i + 1, we will get each element in dp[i] plus stones[i + 1] and we add it to the dp[i]. We will get dp[i + 1]. 

After we get dp[n - 1], we can explore the the total / 2 and try to find the val which make the difference as small as possible.

### Python
```python
def lastStoneWeightII(self, stones: List[int]) -> int:
  n = len(stones)
  if n == 0:
    return 0
  if n == 1:
    return stones[0]
  total = sum(stones)
  possible = set()
  for i in range(len(stones)):
    newSet = set([stones[i]])
    for val in possible:
      if not (val + stones[i]) in possible:
        newSet.add(val + stones[i])
    for val in newSet:
      possible.add(val)
  initial = total // 2
  while not (initial in possible) or not ((total - initial) in possible):
    initial -= 1
        
  return (total - initial) - initial
```
