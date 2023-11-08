---
title: 688. Knight Probability in Chessboard
date: '2022-04-19'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0688. Knight Probability in Chessboard
---

 
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

 > Example 1:

 > Input: n = 3, k = 2, row = 0, column = 0
 > Output: 0.06250
 > Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
 > From each of those positions, there are also two moves that will keep the knight on the board.
 > The total probability the knight stays on the board is 0.0625.

 > Example 2:

 > Input: n = 1, k = 0, row = 0, column = 0
 > Output: 1.00000

**Constraints:**

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 25

 > 0 <TeX>\leq</TeX> k <TeX>\leq</TeX> 100

 > 0 <TeX>\leq</TeX> row, column <TeX>\leq</TeX> n


## Solution
dp[k, row, col] = 0.125 * dp[k - 1, nx, ny] if (nx, ny) is valid. if k = 0, the probability is 1.


### Python
```python
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}
        def helper(n, k, row, col):
            if k == 0:
                return 1.0
            if (k, row, col) in memo:
                return memo[(k, row, col)]
            diffs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
            ans = 0
            for diff in diffs:
                nx = row + diff[0]
                ny = col + diff[1]
                if nx >= 0 and ny >= 0 and nx < n and ny < n:
                    p = helper(n, k - 1, nx, ny)
                    ans += p * 0.125
            memo[(k, row, col)] = ans
            return ans
        return helper(n, k, row, column)
```
