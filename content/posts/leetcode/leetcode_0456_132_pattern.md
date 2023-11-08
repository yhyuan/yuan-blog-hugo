---
title: 456. 132 Pattern
date: '2022-03-13'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0456. 132 Pattern
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={456}/>
 
 Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 > Example 1:

 > Input: nums = [1,2,3,4]
 > Output: false
 > Explanation: There is no 132 pattern in the sequence.

 > Example 2:

 > Input: nums = [3,1,4,2]
 > Output: true
 > Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

 > Example 3:

 > Input: nums = [-1,3,2,0]
 > Output: true
 > Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

**Constraints:**

 > n == nums.length

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2 * 105

 > -109 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 109

## Solution
Calculate minVals. For each index i, minVals will return the minimal value between [0, i]. So For all position from [1..n - 1], minVals[i - 1] will be the leftest number. 

If we calculate monotonic stack from right to left, firstly we make sure all the values are larger than minVal. The values in the stack are larger than minVal. The indices in the stack is always larger than the current index. If the stack top is smaller than the current value, that will be result we are looking for.

### Python
```python
def find132pattern(nums: List[int]) -> bool:
  n = len(nums)
  minVals = [0] * n
  minVals[0] = nums[0]
  for i in range(1, n):
    minVals[i] = min(minVals[i - 1], nums[i])
  stack = []
  for i in reversed(range(1, n)):
    minVal = minVals[i - 1]
    curr = nums[i]
    while len(stack) > 0 and stack[-1] <= minVal:
      stack.pop()
    if len(stack) > 0 and stack[-1] < curr:
      return True
    stack.append(nums[i]);
  return False
```
