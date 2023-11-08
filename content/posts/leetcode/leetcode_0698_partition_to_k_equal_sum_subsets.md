---
title: 698. Partition to K Equal Sum Subsets
date: '2022-04-21'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0698. Partition to K Equal Sum Subsets
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={698}/>
 
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 > Example 1:

 > Input: nums = [4,3,2,3,5,2,1], k = 4
 > Output: true
 > Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

 > Example 2:

 > Input: nums = [1,2,3,4], k = 3
 > Output: false

**Constraints:**

 > 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 16

 > 1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 104

 > The frequency of each element is in the range [1, 4].

## Solution
if n < k or total % k != 0, the result will be False. 

define dp[k, currSum, used, start] as the result for k: the number of buckets, the total in current bucket, and used: a tuple which specify whether a number is used or not, start: the current index of nums. 

if k == 1, the result is True. 

if currSum == target value, the problem is reduced to dp[k - 1, 0, used, 0]

We try every value from start. If the value is not used and the value + currSum < target, we add it the currSum and update used, the problem is reduced to dp[k, currSum + val, used, i + 1]. If we find True result, we will return the result as True. If we fail to find a result with True vale, we will return False. 

We will memo to store the results to make sure we do the calculation only once.


### Python
```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < k:
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k 
        memo = {}
        def helper(k, currSum, used, start):
            if k == 1: 
                return True
            if (k, currSum, used, start) in memo:
                return memo[(k, currSum, used, start)]
            if currSum == target:
                memo[(k, currSum, used, start)] = helper(k - 1, 0, used, 0)
                return memo[(k, currSum, used, start)]
            for i in range(start, n):
                if not used[i] and nums[i] + currSum <= target:
                    newUsed = list(used)
                    newUsed[i] = True
                    newUsed = tuple(newUsed)
                    res = helper(k, nums[i] + currSum, newUsed, i + 1)
                    if res:
                        memo[(k, currSum, used, start)] = True
                        return True
            memo[(k, currSum, used, start)] = False
            return False
        used = tuple([False] * n)
        ans = helper(k, 0, used, 0)            
        return ans
```
