---
title: 750. Number Of Corner Rectangles
date: '2022-05-09'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0750. Number Of Corner Rectangles
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={750}/>
 
Given an m x n integer matrix grid where each entry is only 0 or 1, return the number of corner rectangles.

A corner rectangle is four distinct 1's on the grid that forms an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1's used must be distinct.

 > Example 1:

 > Input: grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
 > Output: 1
 > Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].

 > Example 2:

 > Input: grid = [[1,1,1],[1,1,1],[1,1,1]]
 > Output: 9
 > Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.

 > Example 3:

 > Input: grid = [[1,1,1,1]]
 > Output: 0
 > Explanation: Rectangles must have four distinct corners.

**Constraints:**

 > m == grid.length

 > n == grid[i].length

 > 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 200

 > grid[i][j] is either 0 or 1.

 > The number of 1's in the grid is in the range [1, 6000].


## Solution
Turn the grid to a boolean grid. Then, pick two rows in grid and "and" two rows. Then, calculate the number of True values.

### Python
```python
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = True
                else:
                    grid[i][j] = False
        ans = 0
        for i in range(m):
            for j in range(i + 1, m):
                res = 0
                for k in range(n):
                    if grid[i][k] and grid[j][k]: 
                        res += 1
                ans += res * (res - 1) // 2
        return ans

```
