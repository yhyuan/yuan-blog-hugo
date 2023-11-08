---
title: 316. remove duplicate letters
date: '2022-01-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0316 remove duplicate letters
---

 

  Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "bcabc"

 >   Output: "abc"

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "cbacdcbc"

 >   Output: "acdb"

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 10^4

 >   	s consists of lowercase English letters.

  

   

 >   Note: This question is the same as 1081: [https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)


## Solution
 we need to build a variant of monotonic increasing stack. If a character will appear later, we will try to create a monotonic increasing stack. Otherwise, we will to add it the stack. 
https://jimmy-shen.medium.com/stack-leetcode-316-remove-duplicate-letters-1459b1946c6d

### Python
```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {ch:i for i, ch in enumerate(s)}
        stack = []
        visited = set()
        for i, ch in enumerate(s):
            if ch in visited:continue
            # Increasing monotonic stack if the 
            # character appears later. If it is 
            # the last appearance, we will add it 
            # to stack.
            while len(stack) > 0 and ch < stack[-1] and last_occur[stack[-1]] > i:
                c = stack.pop()
                visited.remove(c)
            stack.append(ch)
            visited.add(ch)
        return "".join(stack)
```
