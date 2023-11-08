---
title: 1539. Kth Missing Positive Number
date: '2022-08-12'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 1539. Kth Missing Positive Number
---


Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

> Example 1:
> Input: arr = [2,3,4,7,11], k = 5
> Output: 9
> Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
> Example 2:
> Input: arr = [1,2,3,4], k = 2
> Output: 6
> Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
**Constraints:**
> 1 <TeX>\leq</TeX> arr.length <TeX>\leq</TeX> 1000
> 1 <TeX>\leq</TeX> arr[i] <TeX>\leq</TeX> 1000
> 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> 1000
> arr[i] < arr[j] for 1 <TeX>\leq</TeX> i < j <TeX>\leq</TeX> arr.length
Follow up:
Could you solve this problem in less than O(n) complexity?


## Solution
Firstly, we divide the range to three small ranges: < arr[0], between arr[0] and arr[-1], larger than arr[-1]. We can count the missing number before arr[0] is arr[0] - 1, the missing number between arr[0] and arr[-1] is (arr[-1] - arr[0] + 1) - (n - 1 - 0 + 1). So we can just the k's range. If k is small and less than arr[0], it can be easily solved. If k is very larger and behind the arr[-1], it can also be easily solved. If k is in the middle, we can use binary search to limited the range of k.



### Python
```python
class Solution:
def findKthPositive(self, arr: List[int], k: int) -> int:
before = arr[0] - 1
n = len(arr)
mid = arr[-1] - arr[0] + 1 - (n - 1 - 0 + 1)
if k <= before:
return k
if k > before + mid:
return arr[-1] + (k - (before + mid))



# between index start and end, find k missing number
def helper(start, end, k):
if start + 1 == end:
return arr[start] + k
mid = (start + end) // 2
leftMissing = (arr[mid] - arr[start] + 1) - (mid - start + 1)
rightMissing = (arr[end] - arr[mid] + 1) - (end - mid + 1)
if k <= leftMissing:
return helper(start, mid, k)
else:
return helper(mid, end, k - leftMissing)

k -= before
return helper(0, n - 1, k)
```
