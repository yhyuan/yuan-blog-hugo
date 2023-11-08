---
title: 1004. Max Consecutive Ones III
date: '2022-06-28'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 1004. Max Consecutive Ones III
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1004}/>
 
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 > Example 1:

 > Input: nums <TeX>=</TeX> [1,1,1,0,0,0,1,1,1,1,0], k <TeX>=</TeX> 2
 > Output: 6
 > Explanation: [1,1,1,0,0,1,1,1,1,1,1]
 > Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

 > Example 2:

 > Input: nums <TeX>=</TeX> [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k <TeX>=</TeX> 3
 > Output: 10
 > Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
 > Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

**Constraints:**

 > 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 105

 > nums[i] is either 0 or 1.

 > 0 <TeX>\leq</TeX> k <TeX>\leq</TeX> nums.length

## Solution
### Python
```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding windown. Count of 0 <= k
        def meetCondition(countZero, k):
            return countZero <= k
        i = 0
        j = 0
        size = 0
        countZero = 0
        ans = 0
        n = len(nums)
        while i < n:
            while i < n and meetCondition(countZero, k):
                if nums[i] == 0:
                    countZero += 1

                size += 1
                i += 1
            if not meetCondition(countZero, k):
                ans = max(ans, size - 1)
            else:
                ans = max(ans, size)
            while j < i and not meetCondition(countZero, k):
                if nums[j] == 0:
                    countZero -= 1

                size -= 1
                j += 1
        return ans

```
