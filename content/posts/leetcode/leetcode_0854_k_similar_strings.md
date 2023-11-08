---
title: 854. K-Similar Strings
date: '2022-05-31'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 0854. K-Similar Strings
---


Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

> Example 1:
> Input: s1 <TeX>=</TeX> "ab", s2 <TeX>=</TeX> "ba"
> Output: 1
> Example 2:
> Input: s1 <TeX>=</TeX> "abc", s2 <TeX>=</TeX> "bca"
> Output: 2
**Constraints:**
> 1 <TeX>\leq</TeX> s1.length <TeX>\leq</TeX> 20
> s2.length <TeX>=</TeX><TeX>=</TeX> s1.length
> s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
> s2 is an anagram of s1.


## Solution
We can use BFS to solve this problem. Since we have the target string, we can use it to speed up the search process. First we try to make the first letter match. Then, we move it to the second one. until we reach the end of the string.


### Python
```python
def kSimilarity(self, s1: str, s2: str) -> int:
if s1 == s2:
return 0
visited = set()
def findNeighbors(s, target):
n = len(s)
chars = list(s)
targetChars = list(target)
nextIndex = -1
for i in range(n):
if chars[i] != targetChars[i]:
nextIndex = i
break
targetChar = targetChars[nextIndex]
indices = list(filter(lambda i: chars[i] == targetChar, range(nextIndex, n)))
ans = []
for ind in indices:
(chars[ind], chars[nextIndex]) = (chars[nextIndex], chars[ind])
ans.append("".join(chars))
(chars[ind], chars[nextIndex]) = (chars[nextIndex], chars[ind])
return ans

q = deque([s1])
q.append(s1)
visited = set([s1])
steps = 0
while len(q) > 0:
n = len(q)
for i in range(n):
n_s = q.popleft()
neighbors = findNeighbors(n_s, s2)
for neighbor in neighbors:
if not neighbor in visited:
if neighbor == s2:
return steps + 1
visited.add(neighbor)
q.append(neighbor)
steps += 1
return -1
```
