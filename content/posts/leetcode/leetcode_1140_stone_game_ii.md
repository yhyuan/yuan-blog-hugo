---
title: 1140. Stone Game II
date: '2022-07-13'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 1140. Stone Game II
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1140}/>
 
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <TeX>\leq</TeX> X <TeX>\leq</TeX> 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 > Example 1:

 > Input: piles = [2,7,9,4,4]
 > Output: 10
 > Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

 > Example 2:

 > Input: piles = [1,2,3,4,5,100]
 > Output: 104

**Constraints:**

 > 1 <TeX>\leq</TeX> piles.length <TeX>\leq</TeX> 100

 > 1 <TeX>\leq</TeX> piles[i] <TeX>\leq</TeX> 104


## Solution
Solution: let's define dp[(i, m, isAlice)] as the scores that Alice and Bob can get for the piles starting at i , M value is m, and whether Alice is playing or not.

If it is Alice playing, she will go through her options and pick the best one. 

If it is Bob playing, he will go through his options and pick the best one.

### Python
```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def helper(i, m, isAlice):
            n = len(piles)
            if (i, m, isAlice) in memo:
                return memo[(i, m, isAlice)]
            if i == n:
                return (0, 0)
            if isAlice:
                ans = (0, 0)
                for j in range(1, 2 * m + 1):
                    if i + j > n:
                        break
                    res = sum(list(map(lambda k: piles[k] if k < n else 0, range(i, i + j))))
                    pre_res = helper(i + j, max(m, j), not isAlice)
                    if res + pre_res[0] > ans[0]:
                        ans = (res + pre_res[0], pre_res[1])
                memo[(i, m, isAlice)] = ans
                return ans

            ans = (0, 0)
            for j in range(1, 2 * m + 1):
                if i + j > n:
                    break
                res = sum(list(map(lambda k: piles[k] if k < n else 0, range(i, i + j))))
                pre_res = helper(i + j, max(m, j), not isAlice)
                if res + pre_res[1] > ans[1]:
                    ans = (pre_res[0], res + pre_res[1])
            memo[(i, m, isAlice)] = ans
            return ans

        ans = helper(0, 1, True)
        return ans[0]

```
