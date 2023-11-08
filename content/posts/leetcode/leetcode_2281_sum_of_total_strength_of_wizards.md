---
title: 2281. Sum of Total Strength of Wizards
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2281. Sum of Total Strength of Wizards
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2281}/>

As the ruler of a kingdom, you have an army of wizards at your command.

You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

The strength of the weakest wizard in the group.

The total of all the individual strengths of the wizards in the group.

Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 > Example 1:

 > Input: strength <TeX>=</TeX> [1,3,1,2]
 > Output: 44
 > Explanation: The following are all the contiguous groups of wizards:
 > - [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) <TeX>=</TeX> 1 * 1 <TeX>=</TeX> 1
 > - [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) <TeX>=</TeX> 3 * 3 <TeX>=</TeX> 9
 > - [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) <TeX>=</TeX> 1 * 1 <TeX>=</TeX> 1
 > - [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) <TeX>=</TeX> 2 * 2 <TeX>=</TeX> 4
 > - [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) <TeX>=</TeX> 1 * 4 <TeX>=</TeX> 4
 > - [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) <TeX>=</TeX> 1 * 4 <TeX>=</TeX> 4
 > - [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) <TeX>=</TeX> 1 * 3 <TeX>=</TeX> 3
 > - [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) <TeX>=</TeX> 1 * 5 <TeX>=</TeX> 5
 > - [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) <TeX>=</TeX> 1 * 6 <TeX>=</TeX> 6
 > - [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) <TeX>=</TeX> 1 * 7 <TeX>=</TeX> 7
 > The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 <TeX>=</TeX> 44.

 > Example 2:

 > Input: strength <TeX>=</TeX> [5,4,6]
 > Output: 213
 > Explanation: The following are all the contiguous groups of wizards: 
 > - [5] from [5,4,6] has a total strength of min([5]) * sum([5]) <TeX>=</TeX> 5 * 5 <TeX>=</TeX> 25
 > - [4] from [5,4,6] has a total strength of min([4]) * sum([4]) <TeX>=</TeX> 4 * 4 <TeX>=</TeX> 16
 > - [6] from [5,4,6] has a total strength of min([6]) * sum([6]) <TeX>=</TeX> 6 * 6 <TeX>=</TeX> 36
 > - [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) <TeX>=</TeX> 4 * 9 <TeX>=</TeX> 36
 > - [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) <TeX>=</TeX> 4 * 10 <TeX>=</TeX> 40
 > - [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) <TeX>=</TeX> 4 * 15 <TeX>=</TeX> 60
 > The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 <TeX>=</TeX> 213.

**Constraints:**

1 <TeX>\leq</TeX> strength.length <TeX>\leq</TeX> 105

1 <TeX>\leq</TeX> strength[i] <TeX>\leq</TeX> 109


## Solution
We can use monotonic stack to find the list of subarrays whose minimal value is at i. Then, we can calculate the sum of this list of subarray and multiple with the value at i. If we add the results together, it will be the answer. Please notice we use > for the left and >= for right to avoid the situation when there are equal values. 

```python
left = [-1] * n
stack = []
for i in range(n):
  while len(stack) > 0 and strength[stack[-1]] > strength[i]:
    stack.pop()
  left[i] = -1 if len(stack) == 0 else stack[-1]
  stack.append(i)

right = [n] * n
stack = []
for i in reversed(range(n)):
  while len(stack) > 0 and strength[stack[-1]] >= strength[i]:
    stack.pop()
  right[i] = n if len(stack) == 0 else stack[-1]
  stack.append(i)
```
Then, we can go through each element. We notice that ith element is the minimal value between the interval [left[i] + 1, right[i] - 1]. 
```python
ans = 0 
for i in range(n):
  #[left[i] + 1, right[i] - 1]
  minVal = strength[i]
  for j in range(left[i] + 1, i + 1):
    for k in range(i, right[i]):
      sumVal = preSum[k + 1] - preSum[j]
      ans_1 += minVal * sumVal
      ans_1 = ans_1 % 1000000007
```
We use PreSum to speed the calculation of sum between two indices. 
```python
preSum = [0]
for i in range(n):
  nextPreSum = strength[i] + preSum[-1]
  preSum.append(nextPreSum)
```
However, the two for loops cause time out. We can reduce two loops to one loop.
```python
for k in range(left[i] + 1, right[i]):
  if k == i:
    ans += minVal * strength[k] * (i - left[i]) * (right[i] - i)
  elif k < i:
    ans += minVal * strength[k] * (k - left[i]) * (right[i] - i)
  else:
    ans += minVal * strength[k] * (i - left[i]) * (right[i] - k)
  ans = ans % 1000000007
```
It still cause time out.  Finally, Let's analyze the the subarray. The first group of subarray starts at left[i] + 1 and ends at i, i + 1, i + 2, ......right[i] - 1.  Their total will be preSum[i + 1] - preSum[left[i] + 1], 

preSum[i + 2] - preSum[left[i] + 1]

.......

presum[right[i]] - preSum[left[i] + 1]

If we add them together, the total will be preSum[i + 1] + preSum[i + 2] + ... + preSum[right[i]] - (right[i] - i) * preSum[left[i] + 1]. 

The second group will starts at left[i] + 2 and ends at i, i + 1, i + 2, ... right[i] - 1. The total will be preSum[i + 1] + preSum[i + 2] + ... + preSum[right[i]] - (right[i] - i) * preSum[left[i] + 2]. 

.......

The last group will be have a total
```
leftSum = prePreSum[i] - prePreSum[max(0, left[i])]
  rightSum = prePreSum[right[i]] - prePreSum[i]
  leftLen = i - left[i]
  rightLen = right[i] - i
  total = (rightSum * leftLen - leftSum * rightLen)
```

### Python
```python
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        preSum = [0]
        for i in range(n):
            nextPreSum = strength[i] + preSum[-1]
            preSum.append(nextPreSum)
        prePreSum = [preSum[0]]
        for i in range(1, n + 1):
            prePreSum.append(preSum[i] + prePreSum[-1])

        left = [-1] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and strength[stack[-1]] > strength[i]:
                stack.pop()
            left[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(i)
        right = [n] * n
        stack = []
        for i in reversed(range(n)):
            while len(stack) > 0 and strength[stack[-1]] >= strength[i]:
                stack.pop()
            right[i] = n if len(stack) == 0 else stack[-1]
            stack.append(i)
        ans = 0 
        for i in range(n):
            #[left[i] + 1, right[i] - 1]
            minVal = strength[i]
            leftSum = prePreSum[i] - prePreSum[max(0, left[i])]
            rightSum = prePreSum[right[i]] - prePreSum[i]
            leftLen = i - left[i]
            rightLen = right[i] - i
            ans += strength[i] * (rightSum * leftLen - leftSum * rightLen)
            ans = ans % 1000000007
        return ans
  
```
