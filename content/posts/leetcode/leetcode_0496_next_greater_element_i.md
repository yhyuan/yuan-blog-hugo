---
title: 496. Next Greater Element I
date: '2022-03-17'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 0496. Next Greater Element I
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={496}/>
 
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <TeX>\leq</TeX> i < nums1.length, find the index j such that nums1[i] <TeX>=</TeX><TeX>=</TeX> nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 > Example 1:

 > Input: nums1 <TeX>=</TeX> [4,1,2], nums2 <TeX>=</TeX> [1,3,4,2]
 > Output: [-1,3,-1]
 > Explanation: The next greater element for each value of nums1 is as follows:
 > - 4 is underlined in nums2 <TeX>=</TeX> [1,3,4,2]. There is no next greater element, so the answer is -1.
 > - 1 is underlined in nums2 <TeX>=</TeX> [1,3,4,2]. The next greater element is 3.
 > - 2 is underlined in nums2 <TeX>=</TeX> [1,3,4,2]. There is no next greater element, so the answer is -1.

 > Example 2:

 > Input: nums1 <TeX>=</TeX> [2,4], nums2 <TeX>=</TeX> [1,2,3,4]
 > Output: [3,-1]
 > Explanation: The next greater element for each value of nums1 is as follows:
 > - 2 is underlined in nums2 <TeX>=</TeX> [1,2,3,4]. The next greater element is 3.
 > - 4 is underlined in nums2 <TeX>=</TeX> [1,2,3,4]. There is no next greater element, so the answer is -1.

**Constraints:**

 > 1 <TeX>\leq</TeX> nums1.length <TeX>\leq</TeX> nums2.length <TeX>\leq</TeX> 1000

 > 0 <TeX>\leq</TeX> nums1[i], nums2[i] <TeX>\leq</TeX> 104

 > All integers in nums1 and nums2 are unique.

 > All the integers of nums1 also appear in nums2.

## Solution
Using monotonic increasing stack from right to left to find the the nearest index on the right which has the larger values than index i. 
### Python
```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        right = [n] * n
        lookup = {}
        for i in reversed(range(n)):
            while len(stack) > 0 and nums2[stack[-1]] <= nums2[i]:
                stack.pop()
            right[i] = n if len(stack) == 0 else stack[-1]
            stack.append(i)
            lookup[nums2[i]] = i
        ans = []
        for num in nums1:
            index = lookup[num]
            res = -1 if right[index] == n else nums2[right[index]]
            ans.append(res)
        return ans
```
