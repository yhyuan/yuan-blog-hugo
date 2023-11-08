---
title: 1094. Car Pooling
date: '2022-07-06'
tags: ['leetcode', 'python', 'easy', 'interval']
draft: false
description: Solution for leetcode 1094. Car Pooling
---


 There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] <TeX>=</TeX> [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 > Example 1:

 > Input: trips <TeX>=</TeX> [[2,1,5],[3,3,7]], capacity <TeX>=</TeX> 4
 > Output: false

 > Example 2:

 > Input: trips <TeX>=</TeX> [[2,1,5],[3,3,7]], capacity <TeX>=</TeX> 5
 > Output: true

**Constraints:**

 > 1 <TeX>\leq</TeX> trips.length <TeX>\leq</TeX> 1000

 > trips[i].length <TeX>=</TeX><TeX>=</TeX> 3

 > 1 <TeX>\leq</TeX> numPassengersi <TeX>\leq</TeX> 100

 > 0 <TeX>\leq</TeX> fromi < toi <TeX>\leq</TeX> 1000

 > 1 <TeX>\leq</TeX> capacity <TeX>\leq</TeX> 105

## Solution
### Python
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        points = []
        for i in range(n):
            load = trips[i][0]
            start = trips[i][1]
            end   = trips[i][2]
            points.append((start, 1, load))
            points.append((end, 0, load))
        points.sort()
        currentLoad = 0
        for i in range(len(points)):
            if points[i][1] == 1: # start
                currentLoad += points[i][2]
            else:
                currentLoad -= points[i][2]
            if currentLoad > capacity:
                return False
        return True
```
