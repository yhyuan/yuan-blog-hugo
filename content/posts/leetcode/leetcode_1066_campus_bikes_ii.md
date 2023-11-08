---
title: 1066. Campus Bikes II
date: '2022-07-05'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1066. Campus Bikes II
---



On a campus represented as a 2D grid, there are n workers and m bikes, with n <TeX>\leq</TeX> m. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

> Example 1:
> Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
> Output: 6
> Explanation:
> We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.
> Example 2:
> Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
> Output: 4
> Explanation:
> We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.
> Example 3:
> Input: workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]
> Output: 4995
**Constraints:**
> n == workers.length
> m == bikes.length
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> m <TeX>\leq</TeX> 10
> workers[i].length == 2
> bikes[i].length == 2
> 0 <TeX>\leq</TeX> workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
> All the workers and the bikes locations are unique.


## Solution
define dp[i, bikeStates] as the result for works[i: n] and the bikeSates is a boolean tuple to store the used state of bikes.

i == n -1, we only have one worker. We will find the best bike from the remained bikes.

We try each bikes and reduce the problem to [i + 1, newBikeStates]. The min result will be the final result.


### Python
```python
class Solution:
def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
n = len(workers)
m = len(bikes)
memo = {}
def helper(index, bikesState):
if (index, bikesState) in memo:
return memo[(index, bikesState)]
n = len(workers)
if index == n - 1:
worker = workers[index]
minDist = float('inf')
for i in range(m):
if not bikesState[i]:
dist = abs(worker[0] - bikes[i][0]) + abs(worker[1] - bikes[i][1])
minDist = min(minDist, dist)
memo[(index, bikesState)] = minDist
return minDist
ans = float('inf')
for i in range(m):
if not bikesState[i]:
newBikesState = list(bikesState)
newBikesState[i] = True
newBikesState = tuple(newBikesState)
dist = abs(workers[index][0] - bikes[i][0]) + abs(workers[index][1] - bikes[i][1])
res = helper(index + 1, newBikesState) + dist
if res < ans:
ans = res
memo[(index, bikesState)] = ans
return ans

bikesState = tuple(list(map(lambda i: False, range(m))))
ans = helper(0, bikesState)
return ans
```
