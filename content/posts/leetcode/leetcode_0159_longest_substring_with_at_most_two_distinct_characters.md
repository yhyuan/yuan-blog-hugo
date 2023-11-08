---
title: 159. Longest Substring with At Most Two Distinct Characters
date: '2021-09-27'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0159. Longest Substring with At Most Two Distinct Characters
---

 
Given a string s, return the length of the longest substring that contains at most two distinct characters.

 > Example 1:

 > Input: s <TeX>=</TeX> "eceba"
 > Output: 3
 > Explanation: The substring is "ece" which its length is 3.

 > Example 2:

 > Input: s <TeX>=</TeX> "ccaabbb"
 > Output: 5
 > Explanation: The substring is "aabbb" which its length is 5.

**Constraints:**

 > 1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 105

 > s consists of English letters.


## Solution
Sliding Window

### Python
```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        size = 0
        freq = {}
        ans = 0
        while i < n:
            while i < n and len(freq) < 3:
                freq[s[i]] = freq.get(s[i], 0) + 1
                i += 1
                size += 1
            if len(freq) == 3:
                ans = max(ans, size - 1)
            else:
                ans = max(ans, size)
            while j < i and len(freq) > 2:
                if freq[s[j]] == 1:
                    del freq[s[j]]
                else:
                    freq[s[j]] -= 1
                j += 1
                size -= 1
        return ans
```
