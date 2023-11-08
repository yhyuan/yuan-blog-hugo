---
title: 2364. Count Number of Bad Pairs
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2364. Count Number of Bad Pairs
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2364}/>
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 > Example 1:

 > Input: nums = [4,1,3,3]
 > Output: 5
 > Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
 > The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
 > The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
 > The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
 > The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
 > There are a total of 5 bad pairs, so we return 5.

 > Example 2:

 > Input: nums = [1,2,3,4,5]
 > Output: 0
 > Explanation: There are no bad pairs.

**Constraints:**

 > 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 105

 > 1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 109

## Solution
Let calculate the count of pairs that meet j - i == nums[j] - nums[i]. It can be converted to nums[i] - i == nums[j] - j. So we convert the array to nums[i] - i. Then, we calculate its frequency. If the frequency is larger than 1, we can calculate the pairs as k * (k - 1). The total number of pairs is n * (n - 1). We have to divide the final result with 2 because the i and j is ordered. 
### Python
```python
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(map(lambda i: nums[i] - i, range(n)))
        numsDict = {}
        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
        ans = 0
        for num in numsDict:
            if numsDict[num] > 1:
                ans += numsDict[num] * (numsDict[num] - 1)
        return (n * (n - 1) - ans) // 2
  
```
