---
title: 1751. Maximum Number of Events That Can Be Attended II
date: '2022-08-24'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1751. Maximum Number of Events That Can Be Attended II
---


You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

> Example 1:
> Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
> Output: 7
> Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
> Example 2:
> Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
> Output: 10
> Explanation: Choose event 2 for a total value of 10.
> Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
> Example 3:
> Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
> Output: 9
> Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
**Constraints:**
> 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> events.length
> 1 <TeX>\leq</TeX> k * events.length <TeX>\leq</TeX> 106
> 1 <TeX>\leq</TeX> startDayi <TeX>\leq</TeX> endDayi <TeX>\leq</TeX> 109
> 1 <TeX>\leq</TeX> valuei <TeX>\leq</TeX> 106


## Solution
Firstly let's sort the events according to its starting date. Let's assume we want to find the values we can get from i to the end. Obviously, the final result should be 0 to the end.
if k == 1, the answer is very simple. we just want to find the event with max value.

if i == n - 1, since we only have one event, we will pick its value.

At event i, we have two choices. We will pick the choice with max value.

We do not attend event i. Then, the value we will get is as same as the value we can get from i + 1 to the end.

We attend event i. Then, we need to find the next available event index. The value we will get will be the value we can get from index to the end plus the value at event i.

We will use memo to memorize the calculation result.




### Python
```python
class Solution:
def maxValue(self, events: List[List[int]], k: int) -> int:
events = list(map(lambda event: (event[0], event[1], event[2]), events))
events.sort()
memo = {}
def helper(i, k):
n = len(events)
if (i, k) in memo:
return memo[(i, k)]
if i == n - 1:
memo[(i, k)] = events[n - 1][2]
return events[n - 1][2]
if k == 1:
ans = 0
for j in range(i, n):
ans = max(ans, events[j][2])
memo[(i, k)] = ans
return ans
ans = helper(i + 1, k) # not take i
index = -1
for j in range(i, n):
if events[j][0] > events[i][1]:
index = j
break
if index >= 0:
ans = max(ans, helper(index, k - 1) + events[i][2])
else:
ans = max(ans, events[i][2])


# There is no event we can take.
memo[(i, k)] = ans
return ans
res = helper(0, k)
return res

```
