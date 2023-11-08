---
title: 464. Can I Win
date: '2022-03-13'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0464. Can I Win
---


In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

> Example 1:
> Input: maxChoosableInteger = 10, desiredTotal = 11
> Output: false
> Explanation:
> No matter which integer the first player choose, the first player will lose.
> The first player can choose an integer from 1 up to 10.
> If the first player choose 1, the second player can only choose integers from 2 up to 10.
> The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
> Same with other integers chosen by the first player, the second player will always win.
> Example 2:
> Input: maxChoosableInteger = 10, desiredTotal = 0
> Output: true
> Example 3:
> Input: maxChoosableInteger = 10, desiredTotal = 1
> Output: true
**Constraints:**
> 1 <TeX>\leq</TeX> maxChoosableInteger <TeX>\leq</TeX> 20
> 0 <TeX>\leq</TeX> desiredTotal <TeX>\leq</TeX> 300


## Solution
let's define dp[(state, desiredTotal, isPlayer1)] as the result. The state is a tuple with boolean values to store whether ith stone is selected or not. isPlayer1 is a boolean for the state whether player 1 is playing or not.

For each state, we need to find out the stones that have not been selected and try to select them.



### Python
```python
class Solution:
def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
if desiredTotal > (maxChoosableInteger + 1) * maxChoosableInteger:
return False
memo = {}
def helper(state, desiredTotal, isPalyer1):
if (state, desiredTotal, isPalyer1) in memo:
return memo[(state, desiredTotal, isPalyer1)]
if isPalyer1:
for i in range(maxChoosableInteger):
if not state[i] and (i + 1) >= desiredTotal:
memo[(state, desiredTotal, isPalyer1)] = True
return True
for i in range(maxChoosableInteger):
if not state[i]:
newState = list(state)
newState[i] = True
newState = tuple(newState)
res = helper(newState, desiredTotal - (i + 1), not isPalyer1)
if res:
memo[(state, desiredTotal, isPalyer1)] = True
return True
memo[(state, desiredTotal, isPalyer1)] = False
return False


# is Player 2 playing
for i in range(maxChoosableInteger):
if not state[i] and (i + 1) >= desiredTotal:
memo[(state, desiredTotal, isPalyer1)] = False
return False
for i in range(maxChoosableInteger):
if not state[i]:
newState = list(state)
newState[i] = True
newState = tuple(newState)
res = helper(newState, desiredTotal - (i + 1), not isPalyer1)
if not res:
memo[(state, desiredTotal, isPalyer1)] = False
return False
memo[(state, desiredTotal, isPalyer1)] = True
return True
state = tuple(list(map(lambda i: False, range(maxChoosableInteger))))
ans = helper(state, desiredTotal, True)
return ans
```
