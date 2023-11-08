---
title: 727. Minimum Window Subsequence
date: '2022-05-02'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0727. Minimum Window Subsequence
---


Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

> Example 1:
> Input: s1 = "abcdebdde", s2 = "bde"
> Output: "bcde"
> Explanation:
> "bcde" is the answer because it occurs before "bdde" which has the same length.
> "deb" is not a smaller window because the elements of s2 in the window must occur in order.
> Example 2:
> Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
> Output: ""
**Constraints:**
> 1 <TeX>\leq</TeX> s1.length <TeX>\leq</TeX> 2 * 104
> 1 <TeX>\leq</TeX> s2.length <TeX>\leq</TeX> 100
> s1 and s2 consist of lowercase English letters.


## Solution
let's define dp[i][j] as the starting index in s1 in the answer for s1[0..i] and s2[0..j]. So if we can calculate dp[i][j], we will need to check dp[i][n - 1]. Its value provides the starting point, while i is its ending point. So its length is i - dp[i][n-1] + 1. If it is not possible to find the soultion, the dp vlaue will be -1.

dp[i][0] can be calculated according to the position of s1[0]. If it appears, we will update the dp value with its position. If it does not appears, we will simply use the dp[i - 1][0] as its value.

dp[i][j] calculation.

s1[i] == s2[j] dp[i][j] is as same as dp[i - 1][j - 1]

otherwise, dp[i][j] is as same as dp[i-1][j] since s1[i] can be ignored.



### Python
```python
class Solution:
def minWindow(self, s1: str, s2: str) -> str:


# dp[i][j] = k denote that in substring S(0…i), there exists a subsequence corresponding to T(0…j) starting at index k of S


# if(S[i] == T[j])


#    dp[i][j] = dp[i-1][j-1]


# else


#    dp[i][j] = dp[i-1][j]
m = len(s1)
n = len(s2)
dp = [[-1 for j in range(n)] for i in range(m)]



# dp[i][0]
for i in range(m):
dp[i][0] = i if s1[i] == s2[0] else (dp[i - 1][0] if i >= 1 else -1)
for i in range(1, m):
for j in range(1, n):
dp[i][j] = dp[i - 1][j - 1] if s1[i] == s2[j] else dp[i - 1][j]
minLen = float('inf')
ans = ""
for i in range(m):
beginIndex = dp[i][n - 1]
if beginIndex > -1:
curLen = i - beginIndex + 1
if curLen < minLen:
minLen = curLen
ans = s1[beginIndex: beginIndex + minLen]
return ans
```
