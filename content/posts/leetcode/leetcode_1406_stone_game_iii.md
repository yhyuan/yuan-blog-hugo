---
title: 1406. Stone Game III
date: '2022-08-06'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1406. Stone Game III
---

 
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

 > Example 1:

 > Input: values = [1,2,3,7]
 > Output: "Bob"
 > Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

 > Example 2:

 > Input: values = [1,2,3,-9]
 > Output: "Alice"
 > Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
 > If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
 > If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
 > Remember that both play optimally so here Alice will choose the scenario that makes her win.

 > Example 3:

 > Input: values = [1,2,3,6]
 > Output: "Tie"
 > Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

**Constraints:**

 > 1 <TeX>\leq</TeX> stoneValue.length <TeX>\leq</TeX> 5 * 104

 > -1000 <TeX>\leq</TeX> stoneValue[i] <TeX>\leq</TeX> 1000


## Solution
Let's define dp[i][j] as when alice (j = 0) or bob (j = 1) has reach the position i and has the privilege to pick, the best results they can achieve. We will add more stones with zero value to to make the code simple because we do not need to judge boundary.  They have three choices. 

pick one

pick two

pick three.

### Python
```python
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[(0, 0) for j in range(2)] for i in range(n + 4)]
        for i in reversed(range(n)):
            s_i = stoneValue[i]
            s_i_1 = 0 if i == n - 1 else stoneValue[i + 1]
            s_i_2 = 0 if i >= n - 2 else stoneValue[i + 2]
            for turn in range(2): # 0: Alice's Turn 1: Bob's Turn
                if turn == 0:
                    res = dp[i + 1][1]
                    ans = (res[0] + s_i, res[1])
                    res = dp[i + 2][1]
                    res = (res[0] + s_i + s_i_1, res[1])                    
                    if res[0] > ans[0]:
                        ans = res
                    res = dp[i + 3][1]
                    res = (res[0] + s_i + s_i_1 + s_i_2, res[1])
                    if res[0] > ans[0]:
                        ans = res
                else:
                    res = dp[i + 1][0]
                    ans = (res[0], res[1] + s_i)
                    res = dp[i + 2][0]
                    res = (res[0], res[1] + s_i + s_i_1)
                    if res[1] > ans[1]:
                        ans = res
                    res = dp[i + 3][0]
                    res = (res[0], res[1] + s_i + s_i_1 + s_i_2)
                    if res[1] > ans[1]:
                        ans = res
                dp[i][turn] = ans
        (aliceScore, bobScore) = dp[0][0]
        if aliceScore == bobScore:
            return "Tie"
        return "Alice" if aliceScore > bobScore else "Bob"

```
