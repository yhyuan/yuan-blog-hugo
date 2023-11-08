---
title: 541. Reverse String II
date: '2022-03-30'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 0541 Reverse String II
---



Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

> Example 1:
> Input: s <TeX>=</TeX>"abcdefg", k <TeX>=</TeX>2
> Output: "bacdfeg"
> Example 2:
> Input: s <TeX>=</TeX>"abcd", k <TeX>=</TeX>2
> Output: "bacd"
**Constraints:**
> 1 <TeX>\leq</TeX>s.length <TeX>\leq</TeX>104
> s consists of only lowercase English letters.
> 1 <TeX>\leq</TeX>k <TeX>\leq</TeX>104


## Solution
We can use a stack to achieve string reverse.


### Python
```python
class Solution:
def reverseStr(self, s: str, k: int) -> str:
stack = []
enableStack = True
n = len(s)
ans = ""
for i in range(n):
if enableStack:
stack.append(s[i])
else:
ans += s[i]
if i % k == k - 1:
enableStack = not enableStack
while len(stack) > 0:
ch = stack.pop()
ans += ch
while len(stack) > 0:
ch = stack.pop()
ans += ch

return ans
```
