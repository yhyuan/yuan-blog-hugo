---
title: 1000. Minimum Cost to Merge Stones
date: '2022-06-28'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 1000. Minimum Cost to Merge Stones
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1000}/>
 
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

 > Example 1:

 > Input: stones = [3,2,4,1], k = 2
 > Output: 20
 > Explanation: We start with [3, 2, 4, 1].
 > We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
 > We merge [4, 1] for a cost of 5, and we are left with [5, 5].
 > We merge [5, 5] for a cost of 10, and we are left with [10].
 > The total cost was 20, and this is the minimum possible.

 > Example 2:

 > Input: stones = [3,2,4,1], k = 3
 > Output: -1
 > Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.

 > Example 3:

 > Input: stones = [3,5,1,2,6], k = 3
 > Output: 25
 > Explanation: We start with [3, 5, 1, 2, 6].
 > We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
 > We merge [3, 8, 6] for a cost of 17, and we are left with [17].
 > The total cost was 25, and this is the minimum possible.

Constraints:

 > n == stones.length

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 30

 > 1 <TeX>\leq</TeX> stones[i] <TeX>\leq</TeX> 100

 > 2 <TeX>\leq</TeX> k <TeX>\leq</TeX> 30

## Solution
Each merge will cost k piles and add 1 piles back. So the total number of piles is (k - 1). So if n = m *(k - 1) + 1. So if (n - 1) % (k - 1) != 0, we will not able to find an answer. 

let define dp[i][j] as the result that is the minimal cost to merge the piles from i to j. So dp[0][n - 1] will be the result for the question. Since the minimal number of elements is k. We will start from the length: k to length: n. For each possible length, we will start to explore i from 0 to the n - size. The end will be i + size - 1
### Python
```python
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + stones[i]
        dp = [[0 for j in range(n)] for i in range(n)]
        for size in range(k, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                dp[i][j] = float('inf')
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
                if ((j - i) % (k - 1) == 0):
                    dp[i][j] += preSum[j + 1] - preSum[i]
        return dp[0][n - 1]

```
