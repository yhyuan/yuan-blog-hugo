---
title: 252. meeting rooms
date: '2021-11-28'
tags: ['leetcode', 'python', 'easy', 'interval']
draft: false
description: Solution for leetcode 0252. meeting rooms
---

Given an array of meeting time intervals where intervals[i] <TeX>=</TeX> [starti, endi], determine if a person could attend all meetings.

> Example 1:
> Input: intervals <TeX>=</TeX> [[0,30],[5,10],[15,20]]
> Output: 2
> Example 2:
> Input: intervals <TeX>=</TeX> [[7,10],[2,4]]
> Output: 1
**Constraints:**
> 1 <TeX>\leq</TeX> intervals.length <TeX>\leq</TeX> 104
> 0 <TeX>\leq</TeX> starti < endi <TeX>\leq</TeX> 106


## Solution


### Python
```python
class Solution:
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
points = []
n = len(intervals)
for i in range(n):
start = intervals[i][0]
end   = intervals[i][1]
points.append((start, 1))
points.append((end, 0))
points.sort()
count = 0
for i in range(len(points)):
if points[i][1] == 1:
count += 1
else:
count -= 1
if count >= 2:
return False
return True
```

