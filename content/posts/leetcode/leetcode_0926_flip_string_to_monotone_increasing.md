---
title: 926. Flip String to Monotone Increasing
date: '2022-06-11'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0926. Flip String to Monotone Increasing
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={926}/>
 
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Example 1:

Input: s <TeX>=</TeX> "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:

Input: s <TeX>=</TeX> "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:

Input: s <TeX>=</TeX> "00011000"
Output: 2
Explanation: We flip to get 00000000.

Constraints:

1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 105

s[i] is either '0' or '1'.

## Solution
If the string s is monotonic increasing, every element before i will be 0 and every element after i will be 1. We will need to try each position. We will need to know the the number of 0 before i and the number of 1 after i. The total will be the number of flipping. We can calculate the total number of 0 and 1 firstly. Then, we scan from left to right and calculate the total number of 0 and 1 on left and right and calculate the flipping. 
### Python
```python
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        def calculateZeroAndOne(s):
            ans = (0, 0)
            n = len(s)
            for i in range(n):
                if s[i] == '0':
                    ans = (ans[0] + 1, ans[1])
                else:
                    ans = (ans[0], ans[1] + 1)
            return ans
        (zeros, ones) = calculateZeroAndOne(s)
        n = len(s)
        dp = ((0, 0), (zeros, ones))
        ans = zeros
        for i in range(n):
            ((leftZeros, leftOnes), (rightZeros, rightOnes)) = dp
            if s[i] == '0':
                dp = ((leftZeros + 1, leftOnes), (rightZeros - 1, rightOnes))
            else:
                dp = ((leftZeros, leftOnes + 1), (rightZeros, rightOnes - 1))
            ans = min(ans, dp[0][1] + dp[1][0])
        return ans
```
