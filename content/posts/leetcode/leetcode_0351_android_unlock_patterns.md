---
title: 351. Android Unlock Patterns
date: '2022-01-21'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0351. Android Unlock Patterns
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={351}/>
 
Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

All the dots in the sequence are distinct.

If the line segment connecting two consecutive dots in the sequence passes through the center of any other dot, the other dot must have previously appeared in the sequence. No jumps through the center non-selected dots are allowed.

For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand is valid because the line from dot 2 to dot 9 does not pass through the center of either dot 5 or 6.

However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid because the line from dot 1 to dot 3 passes through the center of dot 2.

Here are some example valid and invalid unlock patterns:

The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but dot 2 did not previously appear in the sequence.

The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but dot 5 did not previously appear in the sequence.

The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 meets the condition because dot 2 previously appeared in the sequence.

The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 9 meets the condition because dot 5 previously appeared in the sequence.

Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.

Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.

 > Example 1:

 > Input: m = 1, n = 1
 > Output: 9

 > Example 2:

 > Input: m = 1, n = 2
 > Output: 65

**Constraints:**

 > 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 9

## Solution
Define dp[k] as the valid pattern list for k keys. Then, the result will be len(dp[m]) + len(dp[m + 1]) + ... + len(dp[n]).

dp[0] is simple. It is [1, 2, 3, 4, 5, 6, 7, 8, 9].

If we know dp[i - 1], we will have a lit of valid pattern. Then, we try to add [1, 2, 3, 4, 5, 6, 7, 8, 9] to the end. Firstly, we need to make sure the digits are distinct. Then, we will check cross relationship. If there is no crossing, we are good. Otherwise, we check whether the crossed digit appear previously or not. If yes, the pattern is still valid. Otherwise, the pattern is not valid.

### Python
```python
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        crossCenter = {}
        crossCenter[(1, 3)] = 2
        crossCenter[(3, 1)] = 2
        crossCenter[(4, 6)] = 5
        crossCenter[(6, 4)] = 5
        crossCenter[(7, 9)] = 8
        crossCenter[(9, 7)] = 8
        crossCenter[(1, 7)] = 4
        crossCenter[(7, 1)] = 4
        crossCenter[(2, 8)] = 5
        crossCenter[(8, 2)] = 5
        crossCenter[(3, 9)] = 6
        crossCenter[(9, 3)] = 6
        crossCenter[(1, 9)] = 5
        crossCenter[(9, 1)] = 5
        crossCenter[(3, 7)] = 5
        crossCenter[(7, 3)] = 5
        
        memo = {}
        def isValidPattern(pattern):
            last = pattern[-1]
            prev = pattern[-2]
            if (last, prev) not in crossCenter:
                return True
            mid = crossCenter[(last, prev)]
            return mid in pattern
        def helper(k):
            if k in memo:
                return memo[k]
            if k == 1:
                memo[k] = list(map(lambda i: [i], range(1, 10)))
                return memo[k]
            pre_results = helper(k - 1)
            ans = []
            for result in pre_results:
                for i in range(1, 10):
                    if i in result: continue # All dots must be distinct. 
                    res = result.copy()
                    res.append(i)
                    if isValidPattern(res):
                        ans.append(res)
            return ans
        ans = 0
        for k in range(m, n + 1):
            ans += len(helper(k))
        return ans

```
