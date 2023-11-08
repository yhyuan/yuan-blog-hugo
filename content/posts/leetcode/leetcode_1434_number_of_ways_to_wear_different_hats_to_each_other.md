---
title: 1434. Number of Ways to Wear Different Hats to Each Other
date: '2022-08-06'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1434. Number of Ways to Wear Different Hats to Each Other
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1434}/>
 There are n people and 40 types of hats labeled from 1 to 40.

Given a 2D integer array hats, where hats[i] is a list of all hats preferred by the ith person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 109 + 7.

 > Example 1:

 > Input: hats = [[3,4],[4,5],[5]]
 > Output: 1
 > Explanation: There is only one way to choose hats given the conditions. 
 > First person choose hat 3, Second person choose hat 4 and last one hat 5.

 > Example 2:

 > Input: hats = [[3,5,1],[3,5]]
 > Output: 4
 > Explanation: There are 4 ways to choose hats:
 > (3,5), (5,3), (1,3) and (1,5)

 > Example 3:

 > Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
 > Output: 24
 > Explanation: Each person can choose hats labeled from 1 to 4.
 > Number of Permutations of (1,2,3,4) = 24.

**Constraints:**

 > n == hats.length

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10

 > 1 <TeX>\leq</TeX> hats[i].length <TeX>\leq</TeX> 40

 > 1 <TeX>\leq</TeX> hats[i][j] <TeX>\leq</TeX> 40

 > hats[i] contains a list of unique integers.

## Solution
### Python
```python
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        hat_dict = {}
        for index, hat_list in enumerate(hats):
            for hat in hat_list:
                if hat not in hat_dict:
                    hat_dict[hat] = []
                hat_dict[hat].append(index)
        #print(hat_dict)
        n = len(hats)
        max_state = 1 << n
        # print(max_state)
        l = len(hat_dict)

        g = [0] * max_state
        g[0] = 1

        mod = 10 ** 9 + 7

        for hat in hat_dict.keys():
            f = g[:]
            for state in range(1, max_state):
                for p in hat_dict[hat]:
                    if state & (1 << p):
                        f[state] += g[state ^ (1 << p)]
                        f[state] %= mod
        
            g = f[:]
        
        return f[-1]

```
