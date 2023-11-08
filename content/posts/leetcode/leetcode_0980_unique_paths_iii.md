---
title: 980. Unique Paths III
date: '2022-06-21'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0980. Unique Paths III
---

 
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.

2 representing the ending square. There is exactly one ending square.

0 representing empty squares we can walk over.

-1 representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:

Input: grid <TeX>=</TeX> [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: grid <TeX>=</TeX> [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: grid <TeX>=</TeX> [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Constraints:

m <TeX>==</TeX> grid.length

n <TeX>==</TeX> grid[i].length

1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 20

1 <TeX>\leq</TeX> m * n <TeX>\leq</TeX> 20

-1 <TeX>\leq</TeX> grid[i][j] <TeX>\leq</TeX> 2

There is exactly one starting cell and one ending cell.

## Solution
Use dfs to solve this problem. A bug is found in visited.remove((i, j)) when the target is found. 
### Python
```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def calculateTotalNodes(grid):
            m = len(grid)
            n = len(grid[0])
            ans = 0
            start = (-1, -1)
            end = (-1, -1)
            for i in range(m):
                for j in range(n):
                    if grid[i][j] >= 0:
                        ans += 1
                    if grid[i][j] == 1:
                        start = (i, j)
                    if grid[i][j] == 2:
                        end = (i, j)
            return (ans, start, end)
        (totalNodes, start, end) = calculateTotalNodes(grid)
        def getNeighbors(i, j, visited):
            m = len(grid)
            n = len(grid[0])
            diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            ans = []
            for diff in diffs:
                n_i = diff[0] + i
                n_j = diff[1] + j
                if n_i >= 0 and n_j >= 0 and n_i < m and n_j < n:
                    if (n_i, n_j) == end and len(visited) < totalNodes - 1:
                        continue
                    if grid[n_i][n_j] != -1 and not (n_i, n_j) in visited:
                        ans.append((n_i, n_j))
            return ans
        
        def dfs(i, j, visited):
            visited.add((i, j))
            if len(visited) == totalNodes and i == end[0] and j == end[1]:
                visited.remove((i, j))
                return 1
            neighbors = getNeighbors(i, j, visited)
            ans = 0
            for neighbor in neighbors:
                res = dfs(neighbor[0], neighbor[1], visited)
                ans += res
            visited.remove((i, j))
            return ans
        visited = set([])
        return dfs(start[0], start[1], visited)
```
