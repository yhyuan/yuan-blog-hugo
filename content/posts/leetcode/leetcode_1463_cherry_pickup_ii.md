---
title: 1463. Cherry Pickup II
date: '2022-08-07'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1463. Cherry Pickup II
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1463}/>
 
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and

Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).

When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.

When both robots stay in the same cell, only one takes the cherries.

Both robots cannot move outside of the grid at any moment.

Both robots should reach the bottom row in grid.

 > Example 1:

 > Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
 > Output: 24
 > Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
 > Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
 > Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
 > Total of cherries: 12 + 12 = 24.

 > Example 2:

 > Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
 > Output: 28
 > Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
 > Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
 > Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
 > Total of cherries: 17 + 11 = 28.

**Constraints:**

 > rows == grid.length

 > cols == grid[i].length

 > 2 <TeX>\leq</TeX> rows, cols <TeX>\leq</TeX> 70

 > 0 <TeX>\leq</TeX> grid[i][j] <TeX>\leq</TeX> 100

## Solution
The robots state can be represent as (x, y1, y2). 

The initial state is (0, 0, cols - 1). 

There are nine possible previous states, which can end at (x, y1, y2). We need to filter out these invalid states and find the one with max. Then, we need to judge whether two robots are in the same location or not. Then, we can calculate the result at (x, y1, y2). 

Finally, the max value of dp[rows - 1, y1, y2] will be our result.


### Python
Top down approach
```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # robots position is (x, y1), (x, y2)
        memo = {}
        def helper(x, y1, y2):
            rows = len(grid)
            cols = len(grid[0])
            if x == 0:
                if y1 == 0 and y2 == cols - 1: return grid[x][y1] + grid[x][y2] if cols > 1 else grid[x][y1]
                return -float('inf')
            if (x, y1, y2) in memo: return memo[(x, y1, y2)]
            preStates = [(x - 1, y1 - 1, y2 - 1), (x - 1, y1, y2 - 1), (x - 1, y1 + 1, y2 - 1),  (x - 1, y1 - 1, y2), (x - 1, y1, y2), (x - 1, y1 + 1, y2), (x - 1, y1 - 1, y2 + 1), (x - 1, y1, y2 + 1), (x - 1, y1 + 1, y2 + 1)]
            preStates = list(filter(lambda state: state[1] >= 0 and state[1] < cols and state[2] >= 0 and state[2] < cols , preStates))
            ans = max(list(map(lambda state: helper(state[0], state[1], state[2]), preStates)))
            if y1 == y2: 
                ans += grid[x][y1]
            else:
                ans += grid[x][y1] + grid[x][y2]
            memo[(x, y1, y2)] = ans
            return ans
        cols = len(grid[0])
        rows = len(grid)
        ans = 0
        for i in range(cols):
            for j in range(cols):
                res = helper(rows - 1, i, j)
                ans = max(ans, res)
        return ans
```
Bottom up approach
```python
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # robots position is (x, y1), (x, y2)
        cols = len(grid[0])
        rows = len(grid)
        dp = [[[-float('inf') for k in range(cols)] for j in range(cols)] for i in range(rows)]
        if cols == 1:
            dp[0][0][0] = grid[0][0]
        else:
            dp[0][0][cols - 1] = grid[0][0] + grid[0][cols - 1]
        for x in range(1, rows):
            for y1 in range(cols):
                for y2 in range(cols):
                    preStates = [(x - 1, y1 - 1, y2 - 1), (x - 1, y1, y2 - 1), (x - 1, y1 + 1, y2 - 1),  (x - 1, y1 - 1, y2), (x - 1, y1, y2), (x - 1, y1 + 1, y2), (x - 1, y1 - 1, y2 + 1), (x - 1, y1, y2 + 1), (x - 1, y1 + 1, y2 + 1)]
                    preStates = list(filter(lambda state: state[1] >= 0 and state[1] < cols and state[2] >= 0 and state[2] < cols , preStates))
                    ans = max(list(map(lambda state: dp[state[0]][state[1]][state[2]], preStates)))
                    if y1 == y2: 
                        ans += grid[x][y1]
                    else:
                        ans += grid[x][y1] + grid[x][y2]
                    dp[x][y1][y2] = ans
        ans = 0
        for y1 in range(cols):
            for y2 in range(cols):
                ans = max(ans, dp[rows - 1][y1][y2])
        return ans
```