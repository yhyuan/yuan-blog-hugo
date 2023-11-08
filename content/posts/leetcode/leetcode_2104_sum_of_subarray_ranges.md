---
title: 2104. Sum of Subarray Ranges
date: '2022-09-07'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2104. Sum of Subarray Ranges
---


You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

array.

> Example 1:
> Input: nums <TeX>=</TeX> [1,2,3]
> Output: 4
> Explanation: The 6 subarrays of nums are the following:
> [1], range <TeX>=</TeX> largest - smallest <TeX>=</TeX> 1 - 1 <TeX>=</TeX> 0
> [2], range <TeX>=</TeX> 2 - 2 <TeX>=</TeX> 0
> [3], range <TeX>=</TeX> 3 - 3 <TeX>=</TeX> 0
> [1,2], range <TeX>=</TeX> 2 - 1 <TeX>=</TeX> 1
> [2,3], range <TeX>=</TeX> 3 - 2 <TeX>=</TeX> 1
> [1,2,3], range <TeX>=</TeX> 3 - 1 <TeX>=</TeX> 2
> So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 <TeX>=</TeX> 4.
> Example 2:
> Input: nums <TeX>=</TeX> [1,3,3]
> Output: 4
> Explanation: The 6 subarrays of nums are the following:
> [1], range <TeX>=</TeX> largest - smallest <TeX>=</TeX> 1 - 1 <TeX>=</TeX> 0
> [3], range <TeX>=</TeX> 3 - 3 <TeX>=</TeX> 0
> [3], range <TeX>=</TeX> 3 - 3 <TeX>=</TeX> 0
> [1,3], range <TeX>=</TeX> 3 - 1 <TeX>=</TeX> 2
> [3,3], range <TeX>=</TeX> 3 - 3 <TeX>=</TeX> 0
> [1,3,3], range <TeX>=</TeX> 3 - 1 <TeX>=</TeX> 2
> So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 <TeX>=</TeX> 4.
> Example 3:
> Input: nums <TeX>=</TeX> [4,-2,-3,4,1]
> Output: 59
> Explanation: The sum of all subarray ranges of nums is 59.
**Constraints:**
> 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 1000
> -109 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 109


## Solution
The sum of ranges is equal to the sum of maximum minus the sum of minimum. The problem is converted to calculate the sum of the maximum and the sum of the minimum.

The second question has been solved in leet code 907. The basic idea is to use monotonic stack and scan the array from left to right to find the leftest boundary of a subarray whose minimal value is at location i. If we choose the same method, we will find the rightest boundary. Then, for each location i, we know that if we choose an index between leftest to i and an index between i to rightest, we will find a subarray whose minimal value is at i. The total number of this kind of sub array is (i - left[i]) * (right[i] - i) and the sum will be  (i - left[i]) * (right[i] - i) * arr[i]. If we add them together, we will get the sum of minimal values of subarrays.

The first question can be solved with same approach. But, we need to change the stack from monotonic increasing stack to monotonic decreasing stack.



### Python
```python
def subArrayRanges(self, nums: List[int]) -> int:
def findBoundary(nums, compare, reverse):
n = len(nums)
indexRange = reversed(range(n)) if reverse else range(n)
result = [n] * n if reverse else [-1] * n
stack = []
for i in indexRange:
while len(stack)>0 and compare(nums[stack[-1]], nums[i]):
stack.pop()
v = n if reverse else -1
result[i] = v if len(stack)==0 else stack[-1]
stack.append(i)
return result

def calExtremeSum(nums, left, right):
n = len(nums)
ans = 0
for i in range(n):
ans += (i - left[i])*(right[i] - i) * nums[i]
return ans
minLeft = findBoundary(nums, lambda top, val: top > val, False)
minRight = findBoundary(nums, lambda top, val: top >= val, True)
maxLeft = findBoundary(nums, lambda top, val: top < val, False)
maxRight = findBoundary(nums, lambda top, val: top <= val, True)
max_sum = calExtremeSum(nums, maxLeft, maxRight)
min_sum = calExtremeSum(nums, minLeft, minRight)
return max_sum - min_sum
```
