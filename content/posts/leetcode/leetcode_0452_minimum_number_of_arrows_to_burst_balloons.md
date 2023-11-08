---
title: 452. Minimum Number of Arrows to Burst Balloons
date: '2022-03-13'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0452. Minimum Number of Arrows to Burst Balloons
---


There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <TeX>\leq</TeX> x <TeX>\leq</TeX> xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

> Example 1:
> Input: points = [[10,16],[2,8],[1,6],[7,12]]
> Output: 2
> Explanation: The balloons can be burst by 2 arrows:
> - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
> - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
> Example 2:
> Input: points = [[1,2],[3,4],[5,6],[7,8]]
> Output: 4
> Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
> Example 3:
> Input: points = [[1,2],[2,3],[3,4],[4,5]]
> Output: 2
> Explanation: The balloons can be burst by 2 arrows:
> - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
> - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
**Constraints:**
> 1 <TeX>\leq</TeX> points.length <TeX>\leq</TeX> 105
> points[i].length == 2
> -231 <TeX>\leq</TeX> xstart < xend <TeX>\leq</TeX> 231 - 1


## Solution
Sort the intervals with its end. Firstly, shot the first interval. For the rest of intervals, if its starting point is smaller than the previous shot interval, it means it has been shot (we shot at the end of that interval). If the starting point is larger than the shot interval, it also mean its ending point will come in the future. When it comes, we simply add one more arrow and update the previous shot interval's ending point.




### Python
```python
class Solution:
def findMinArrowShots(self, points: List[List[int]]) -> int:


# sort with its ends
points.sort(key=lambda x: x[1])
ans = 1
arrowEnd = points[0][1]
for i in range(len(points)):
start = points[i][0]
end = points[i][1]
if start > arrowEnd:
ans += 1
arrowEnd = points[i][1]
return ans
```
