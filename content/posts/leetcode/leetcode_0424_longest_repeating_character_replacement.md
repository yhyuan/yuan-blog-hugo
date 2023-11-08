---
title: 424. Longest Repeating Character Replacement
date: '2022-03-09'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0424. Longest Repeating Character Replacement
---

 
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s <TeX>=</TeX> "ABAB", k <TeX>=</TeX> 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s <TeX>=</TeX> "AABABBA", k <TeX>=</TeX> 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:

1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 105

s consists of only uppercase English letters.

0 <TeX>\leq</TeX> k <TeX>\leq</TeX> s.length

## Solution
Sliding Window

### Python
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # highest freq. non highest freq letters total is k. 
        n = len(s)
        i = 0
        j = 0
        size = 0
        freq = {}
        ans = 0
        def meetCondition(freq, k):
            maxFreq = -1
            maxFreqKey = ""
            for key in freq:
                if freq[key] > maxFreq:
                    maxFreq = freq[key]
                    maxFreqKey = key
            total = 0
            for key in freq:
                if key != maxFreqKey:
                    total += freq[key]
            return total <= k
            
        while i < n:
            while i < n and meetCondition(freq, k):
                freq[s[i]] = freq.get(s[i], 0) + 1
                size += 1
                i += 1
            if not meetCondition(freq, k):
                ans = max(ans, size - 1)
            else:
                ans = max(ans, size)
            while j < i and not meetCondition(freq, k):
                if freq[s[j]] == 1:
                    del freq[s[j]]
                else:
                    freq[s[j]] -= 1
                size -= 1
                j += 1
        return ans
```
