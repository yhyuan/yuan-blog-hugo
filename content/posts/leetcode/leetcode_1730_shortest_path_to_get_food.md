---
title: 1730. Shortest Path to Get Food
date: '2022-08-24'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1730. Shortest Path to Get Food
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1730}/>

You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.

'#' is a food cell. There may be multiple food cells.

'O' is free space, and you can travel through these cells.

'X' is an obstacle, and you cannot travel through these cells.

You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

> Example 1:

> Input: grid <TeX>=</TeX> [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
> Output: 3
> Explanation: It takes 3 steps to reach the food.

> Example 2:

> Input: grid <TeX>=</TeX> [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
> Output: -1
> Explanation: It is not possible to reach the food.

> Example 3:

> Input: grid <TeX>=</TeX> [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
> Output: 6
> Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

**Constraints:**

> m <TeX>=</TeX><TeX>=</TeX> grid.length

> n <TeX>=</TeX><TeX>=</TeX> grid[i].length

> 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 200

> grid[row][col] is '*', 'X', 'O', or '#'.

> The grid contains exactly one '*'.


## Solution
Solution:  We use BFS to solve this question. Python use deque to define a queue, append to add the tail and popleft get it from the head. 

We also add all obstacles to the visited. 

### Python
```python
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        init = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "X":
                    visited.add((i, j))
                elif grid[i][j] == "*":
                    init = (i, j)
        # Initializing a queue
        q = deque()
        q.append((0, init))
        visited.add(init)
        while len(q) > 0:
            (steps, (i, j)) = q.popleft()
            diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for diff in diffs:
                n_i = i + diff[0]
                n_j = j + diff[1]
                if n_i >= 0 and n_j >= 0 and n_i < m and n_j < n and not (n_i, n_j) in visited:
                    if grid[n_i][n_j] == "#":
                        return steps + 1
                    q.append((steps + 1, (n_i, n_j)))
                    visited.add((n_i, n_j))
        return -1
```
