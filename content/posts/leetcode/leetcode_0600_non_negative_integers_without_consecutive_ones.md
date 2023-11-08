---
title: 600. Non-negative Integers without Consecutive Ones
date: '2022-04-09'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0600. Non-negative Integers without Consecutive Ones
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={600}/>
 
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

 > Example 1:

 > Input: n = 5
 > Output: 5
 > Explanation:
 > Here are the non-negative integers <TeX>\leq</TeX> 5 with their corresponding binary representations:
 > 0 : 0
 > 1 : 1
 > 2 : 10
 > 3 : 11
 > 4 : 100
 > 5 : 101
 > Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 

 > Example 2:

 > Input: n = 1
 > Output: 2

 > Example 3:

 > Input: n = 2
 > Output: 3

**Constraints:**

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 109


## Solution
The key step is to analyze the result for the range between 2^k  to 2 ^(k + 1) - 1.  If we write the numbers in binary format, they will be 1000000  to 1111111. There will be k - 1 0 or 1 behind the first 1. Then, we use (x, y) to mark the possible options for 0 and 1. In the second position, it can only be 0 and it is not possible to be 1. So the result should be (1, 0). Then, in the third position, we can have 0 or 1.  When we analyze it and we will find that each step follows a a format like (x, y) => (x + y, x) because if the previous position is 0, we can use 1 or 0 to follow. However, if the previous position is 1, we can only use 0.

If n == 2^k, we will just the previous result for 2^k  to 2 ^(k + 1) - 1 to calculate it. 

If n != 2^k, we can use log to figure out the result for [0, 2^k] while k = floor(log2(n)). Then, we will only need to calculate the result between 2^k to n. 

1) If the second bit is 1, the result will be simply to calculate the result between a 2 ^ (k -1) and 0. 

2) Otherwise, the problem is reduced to n - 2^k


### Python
```python
class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [(0, 1), (1, 0)]
        for i in range(40):
            next_val = (dp[-1][0] + dp[-1][1], dp[-1][0])
            dp.append(next_val)
        # between 2^k and 2^(k + 1) -1, there are dp[k - 1][0] + dp[k - 1][1] numbers without consective ones. 
        def helper(n):
            if n == 1:
                return 2        
            k = math.floor(math.log2(n))
            ans = 1
            for i in range(k):
                ans += dp[i][0] + dp[i][1]
            if (n == 2 **k):
                return ans + 1
            if n - 2 ** k >= 2 ** (k - 1): # the second bit is 1.
                res = 1
                for i in range(k - 1):
                    res += dp[i][0] + dp[i][1]
                return ans + res
            return ans + helper(n - 2 ** k)
        return helper(n)  
```
