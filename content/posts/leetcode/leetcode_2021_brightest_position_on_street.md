---
title: 2021. Brightest Position on Street
date: '2022-10-06'
tags: ['leetcode', 'python', 'interval']
draft: false
description: Solution for leetcode 2021. Brightest Position on Street
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2021}/>

A perfectly straight street is represented by a number line. The street has street lamp(s) on it and is represented by a 2D integer array lights. Each lights[i] = [positioni, rangei] indicates that there is a street lamp at position positioni that lights up the area from [positioni - rangei, positioni + rangei] (inclusive).

The brightness of a position p is defined as the number of street lamp that light up the position p.

Given lights, return the brightest position on the street. If there are multiple brightest positions, return the smallest one.

 

 > Example 1:


 > Input: lights = [[-3,2],[1,2],[3,3]]
 > Output: -1
 > Explanation:
 > The first street lamp lights up the area from [(-3) - 2, (-3) + 2] = [-5, -1].
 > The second street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].
 > The third street lamp lights up the area from [3 - 3, 3 + 3] = [0, 6].

 > Position -1 has a brightness of 2, illuminated by the first and second street light.
 > Positions 0, 1, 2, and 3 have a brightness of 2, illuminated by the second and third street light.
 > Out of all these positions, -1 is the smallest, so return it.
 > Example 2:

 > Input: lights = [[1,0],[0,1]]
 > Output: 1
 > Explanation:
 > The first street lamp lights up the area from [1 - 0, 1 + 0] = [1, 1].
 > The second street lamp lights up the area from [0 - 1, 0 + 1] = [-1, 1].

 > Position 1 has a brightness of 2, illuminated by the first and second street light.
 > Return 1 because it is the brightest position on the street.
 > Example 3:

 > Input: lights = [[1,2]]
 > Output: -1
 > Explanation:
 > The first street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].

 > Positions -1, 0, 1, 2, and 3 have a brightness of 1, illuminated by the first street light.
 > Out of all these positions, -1 is the smallest, so return it.
 

**Constraints:**

 > 1 <TeX>\leq</TeX> lights.length <TeX>\leq</TeX> 105
 > lights[i].length == 2
 > -108 <TeX>\leq</TeX> positioni <TeX>\leq</TeX> 108
 > 0 <TeX>\leq</TeX> rangei <TeX>\leq</TeX> 108

## Solution
Obviously, this is an interval related question. Since the light range is inclusive, we will assign the starting point of the interval as type 0 and the ending point as type 1. We create a points list with coordinates and types. Then, we sort this list and go through the points. If we meet point type 0, it means we enter an interval. Otherwise, it means we leave an interval. We will keep the record of the number of intervals. When we enter the interval, we compare the current result with max result. If it is larger than the maximum result, we will update its coordinate and the max result. The final coordinate will be our answer. 
### Python
```python
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        points = []
        for i in range(len(lights)):
            position = lights[i][0]
            light_range = lights[i][1]
            points.append((position - light_range, 0))
            points.append((position + light_range, 1))
        points.sort()
        curr_lights = 0
        max_lights = 0
        max_light_pos = None
        for i in range(len(points)):
            if points[i][1] == 0:
                curr_lights += 1
                if curr_lights > max_lights:
                    max_lights = curr_lights
                    max_light_pos = points[i][0]
            else:
                curr_lights -= 1
        return max_light_pos
```
