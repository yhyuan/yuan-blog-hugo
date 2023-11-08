---
title: 1510. Stone Game IV
date: '2022-08-11'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1510. Stone Game IV
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1510}/>
 
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 > Example 1:

 > Input: n = 1
 > Output: true
 > Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

 > Example 2:

 > Input: n = 2
 > Output: false
 > Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

 > Example 3:

 > Input: n = 4
 > Output: true
 > Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

**Constraints:**

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 105

## Solution
### Python
Top down approach
```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        def helper(n, isAlice):
            if (n, isAlice) in memo:
                return memo[(n, isAlice)]
            if n == 0:
                ans = False if isAlice else True
                memo[(n, isAlice)] = ans
                return ans
            if n == 1:
                ans = True if isAlice else False
                memo[(n, isAlice)] = ans
                return ans

            for k in range(1, n):
                if k * k > n:
                    break
                res = helper(n - k * k, not isAlice)
                if isAlice:
                    if res: 
                        memo[(n, isAlice)] = True
                        return True
                if not isAlice:
                    if not res:
                        memo[(n, isAlice)] = False
                        return False
            memo[(n, isAlice)] = False if isAlice else True
            return memo[(n, isAlice)] 
        ans = helper(n, True)
        return ans
```
Bottom up approach
```python
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [(True, True) for i in range(n + 1)]
        dp[0] = [False, True] # Alice playing, Alice lose and Bob playing => Alce win.
        dp[1] = [True, False] 
        for i in range(2, n + 1):
            dp[i] = [None, None]
            for p in range(2):
                # p = 0, aplice playing, p = 1 bob playing. 
                for k in range(1, i):
                    if k * k > i:
                        break
                    res = dp[i - k * k][1 if p == 0 else 0]
                    if p == 0: # alice playing
                        if res: 
                            dp[i][p] = True
                            break
                    if p == 1: # bob palying
                        if not res:
                            dp[i][p] = False
                            break
                if dp[i][p] is None:
                    dp[i][p] = False if p == 0 else True
        return dp[n][0]
```
