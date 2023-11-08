---
title: 741. Cherry Pickup
date: '2022-05-07'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0741. Cherry Pickup
---

 
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,

1 means the cell contains a cherry that you can pick up and pass through, or

-1 means the cell contains a thorn that blocks your way.

Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).

After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.

When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.

If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.

 > Example 1:

 > Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
 > Output: 5
 > Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
 > 4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
 > Then, the player went left, up, up, left to return home, picking up one more cherry.
 > The total number of cherries picked up is 5, and this is the maximum possible.

 > Example 2:

 > Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
 > Output: 0

**Constraints:**

 > n == grid.length

 > n == grid[i].length

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 50

 > grid[i][j] is -1, 0, or 1.

 > grid[0][0] != -1

 > grid[n - 1][n - 1] != -1


## Solution
Solution: We can use two people from (0, 0) to (n - 1, n - 1) to mimic this process.
If both of them in the same grid with cherry, only one cherry will be taken.

If person 1 is at (x1, y1) and person 2 is at (x2, y2), therefore we have x1 + y1 = x2 + y2 because we can only walk down or right. Therefore, we can use (x1, y1, x2) to represent the current state.

let assume dp[(x1, y1, x2)] is the max cherry we can pick from (0, 0) to (x1, y1) and (x2, y2). Then dp[(n - 1, n - 1, n - 1)] will be the result we want.

When two person are at (x1, y1) and (x2, y2). They may come from: 

(x1 - 1, y1) and (x2 - 1, y2)

(x1 - 1, y1) and (x2, y2 - 1)

(x1, y1 - 1) and (x2 - 1, y2)

(x1, y1 - 1) and (x2, y2 - 1).

The max value will be the dp at (x1, y1, x2)

### Python
```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = {}
        def helper(x1, y1, x2):
            y2 = (x1 + y1) - x2
            if (x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0 or grid[x1][y1] == -1 or grid[x2][y2] == -1):
                return -float('inf')
            if x1 == 0 and y1 == 0:
                return grid[0][0]
            if (x1, y1, x2) in memo: return memo[(x1, y1, x2)]
            ans = 0
            if x1 == x2 and y1 == y2:
                ans = grid[x1][y1]
            else:
                ans = grid[x1][y1] + grid[x2][y2]
            ans += max(helper(x1 - 1, y1, x2 - 1), helper(x1, y1 - 1, x2), helper(x1 - 1, y1, x2), helper(x1, y1 - 1, x2 - 1))
            memo[(x1, y1, x2)] = ans
            return ans
        res = helper(n - 1, n - 1, n - 1)
        if res <= 0: return 0
        return res
```
