---
title: 651. 4 Keys Keyboard
date: '2022-04-14'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0651. 4 Keys Keyboard
---


Imagine you have a special keyboard with the following keys:

A: Print one 'A' on the screen.

Ctrl-A: Select the whole screen.

Ctrl-C: Copy selection to buffer.

Ctrl-V: Print buffer on screen appending it after what has already been printed.

Given an integer n, return the maximum number of 'A' you can print on the screen with at most n presses on the keys.

> Example 1:
> Input: n = 3
> Output: 3
> Explanation: We can at most get 3 A's on screen by pressing the following key sequence:
> A, A, A
> Example 2:
> Input: n = 7
> Output: 9
> Explanation: We can at most get 9 A's on screen by pressing following key sequence:
> A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
**Constraints:**
> 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 50


## Solution
dp[i] can be two cases:

Always press A. The result will be i.

Paste from dp[j], we will need Ctrl + A, Ctrl + C, Ctrl + V, Ctrl + V, ... Ctrl + V to reach dp[i].

i < 4, we can not use Ctrl + A, Ctrl + C, Ctrl + V because it needs at least 4 keys input.

i >= 4.  The dp[i] will be the max value of the following choices. For example, we can Ctrl +V  dp[1] i - 4 + 1 times and get the values of i - 4 + 1 + 1. We can also Ctrl + v dp[i -3]  one time to reach the value of 2 * dp[i -3 ].

dp[1] * (i - 4 + 1 + 1)

dp[2] * ( i - 5 + 1 + 1)

dp[3] * (i - 6 + 1 + 1)

dp[i - 3] * 2




### Python
```python
class Solution:
def maxA(self, n: int) -> int:
dp = [0] * (n + 1)
for i in range(1, n + 1):
dp[i] = i # Press A
if (i >=4):
for j in range(1, i - 2):
dp[i] = max(dp[i], dp[j] * (i - 2 - j + 1))
return dp[n]
```
