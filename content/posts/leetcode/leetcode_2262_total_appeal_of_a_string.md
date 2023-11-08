---
title: 2262. Total Appeal of A String
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2262. Total Appeal of A String
---

The appeal of a string is the number of distinct characters found in the string.

For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.

Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.

> Example 1:
> Input: s <TeX>=</TeX> "abbca"
> Output: 28
> Explanation: The following are the substrings of "abbca":
> - Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
> - Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
> - Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
> - Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
> - Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
> The total sum is 5 + 7 + 7 + 6 + 3 <TeX>=</TeX> 28.
> Example 2:
> Input: s <TeX>=</TeX> "code"
> Output: 20
> Explanation: The following are the substrings of "code":
> - Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4.
> - Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6.
> - Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6. >
> - Substrings of length 4: "code" has an appeal of 4. The sum is 4.
> The total sum is 4 + 6 + 6 + 4 <TeX>=</TeX> 20.
**Constraints:**
> 1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 105
> s consists of lowercase English letters.


## Solution
Solution: Let's use dynamic programming to solve this question.

The dp[i] at index i store two variable: the first one the total appear for the all the substring ends at i and the locations of the most recent index for 'a', 'b', 'c', 'd'...'z'. If the letter has never appear, the value will be -1.

When we come to i + 1, if the character at i + 1 has never appeared (it means its most recent index before i + 1 is -1), we obviously add a new character to all the substring at i + 1. The total number of the substring ends at i + 1 is i + 1. So the total appear we gain in i + 1 is dp[i] + (i + 1).

If the character at i + 1 has appeared. Then, we can get its most recent index. From i to the most recent index, this character has never appeared. Now we added it at i + 1. It means that the total appear we gain in i + 1 is dp[i] + (i - preIndex[ch]).



### Python
```python
def appealSum(self, s: str) -> int:


# dp[i]: total appeal of all of the substrings


# end at i and preIndex store the most recent


# index of a, b, c, d...z
preIndex = [-1] * 26
totalAppeal = 0
ans = 0
for i in range(len(s)):
ch = s[i]
ch_i = ord(s[i]) - ord('a')
if preIndex[ch_i] == -1:# never appear
totalAppeal += i + 1
else: # appeared
totalAppeal += (i - preIndex[ch_i])
ans += totalAppeal
preIndex[ch_i] = i
return ans
```
