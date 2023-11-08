---
title: 973. K Closest Points to Origin
date: '2022-06-19'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 973. K Closest Points to Origin
---


Given an array of points where points[i] <TeX>=</TeX> [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

> Example 1:
> Input: points <TeX>=</TeX> [[1,3],[-2,2]], k <TeX>=</TeX> 1
> Output: [[-2,2]]
> Explanation:
> The distance between (1, 3) and the origin is sqrt(10).
> The distance between (-2, 2) and the origin is sqrt(8).
> Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
> We only want the closest k <TeX>=</TeX> 1 points from the origin, so the answer is just [[-2,2]].
> Example 2:
> Input: points <TeX>=</TeX> [[3,3],[5,-1],[-2,4]], k <TeX>=</TeX> 2
> Output: [[3,3],[-2,4]]
> Explanation: The answer [[-2,4],[3,3]] would also be accepted.
**Constraints:**
> 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> points.length <TeX>\leq</TeX> 104
> -104 <TeX>\leq</TeX> xi, yi <TeX>\leq</TeX> 104


## Solution
We can use a Max heap to keep the first k minimal elements. If a value is smaller than the max heap's first element, it will be insert to the heap and heap will pop out the largest value. If a value is larger than the max heap's first element, we will skip it.

Python's heap is a minimum heap. We will add a negative sign to make a maximum heap.


### Python
```python
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
n = len(points)
heap = []
for i in range(n):
x = points[i][0]
y = points[i][1]
dist = x * x + y * y
if len(heap) < k:
heappush(heap, (-dist, x, y))
else:
if -dist > heap[0][0]:
heappop(heap)
heappush(heap, (-dist, x, y))
ans = []
while len(heap) > 0:
(dist, x, y) = heappop(heap)
ans.append([x, y])
return ans
```
