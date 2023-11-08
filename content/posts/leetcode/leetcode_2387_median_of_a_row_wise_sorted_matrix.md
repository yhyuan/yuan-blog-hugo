---
title: 2387. Median of a Row Wise Sorted Matrix
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2387. Median of a Row Wise Sorted Matrix
---


Given an m x n matrix grid containing an odd number of integers where each row is sorted in non-decreasing order, return the median of the matrix.

You must solve the problem in O(m * log(n)) time complexity.

> Example 1:
> Input: grid <TeX>=</TeX> [[1,1,2],[2,3,3],[1,3,4]]
> Output: 2
> Explanation: The elements of the matrix in sorted order are 1,1,1,2,2,3,3,3,4. The median is 2.
> Example 2:
> Input: grid <TeX>=</TeX> [[1,1,3,3,4]]
> Output: 3
> Explanation: The elements of the matrix in sorted order are 1,1,3,3,4. The median is 3.
**Constraints:**
> m <TeX>==</TeX> grid.length
> n <TeX>==</TeX> grid[i].length
> 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 500
> m and n are both odd.
> 1 <TeX>\leq</TeX> grid[i][j] <TeX>\leq</TeX> 106
> grid[i] is sorted in non-decreasing order.


## Solution
m rows looks m queues. The numbers on the head are pushed to a heap. When the min value is pop out of the heap, the related queue's next element is pushed to heap again . Until the (m * n) // 2 is popped out, we get the median.


### Python
```python
class Solution:
def matrixMedian(self, grid: List[List[int]]) -> int:
m = len(grid)
n = len(grid[0])
indexs = [0] * m
heap = []
for i in range(m):
heappush(heap, (grid[i][0], i))
k = 0
midIndex = (m * n) // 2
while True:
(val, row) = heappop(heap)
k += 1
if k == midIndex + 1:
return val
if indexs[row] < n - 1:
indexs[row] += 1
heappush(heap, (grid[row][indexs[row]], row))
return -1
```
