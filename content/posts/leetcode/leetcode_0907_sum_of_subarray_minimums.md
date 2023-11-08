---
title: 907. Sum of Subarray Minimums
date: '2022-06-07'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 907. Sum of Subarray Minimums
---


Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

>  Example 1:
>  Input: arr <TeX>=</TeX>[3,1,2,4]
>  Output: 17
>  Explanation:
>  Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
>  Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
>  Sum is 17.
>  Example 2:
>  Input: arr <TeX>=</TeX>[11,81,94,43,3]
>  Output: 444
**Constraints:**
>  1 <TeX>\leq</TeX>arr.length <TeX>\leq</TeX>3 * 104
>  1 <TeX>\leq</TeX>arr[i] <TeX>\leq</TeX>3 * 104


## Solution
Monotonic stack will be used to solve this problem.

If we scan from left to right, we will pop the element from the stack if the stack top is larger than the current element. Then, we will push the current element to the stack. The key finding is that when we stop popping, we actually find the leftest element which is smaller than the current element. The elements between the top of the stack and the current element are larger than current elements. Let's define this result array as left.

If we scan from right to left, we can similarly find the most right element. The elements between the top of the stack and the current element are larger than the current elements. Let's define this result array as right.

Therefore, if we choose an index between i and left[i] and choose an index between i and right[i], all the subarrays' minimal value is arr[i]. The total number of array will be (i - left[i]) * (right[i] - i)




### Python
```python
def sumSubarrayMins(arr: List[int]) -> int:
n = len(arr)
stack = []
left = [-1] * n
for i in range(n): # left to right
while len(stack)>0 and arr[stack[-1]]>arr[i]:
stack.pop()
left[i] = -1 if len(stack) == 0 else stack[-1]
stack.append(i)

stack = []
right = [n] * n
for i in reversed(range(n)): # right to left
while len(stack)>0 and arr[stack[-1]]>=arr[i]:
stack.pop()
right[i] = n if len(stack) == 0 else stack[-1]
stack.append(i)

ans = 0
for i in range(n):
ans += (i - left[i]) * (right[i] - i) * arr[i]
ans = ans % 1000000007
return ans
```
