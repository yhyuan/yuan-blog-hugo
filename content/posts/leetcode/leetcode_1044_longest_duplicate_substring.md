---
title: 1044. Longest Duplicate Substring
date: '2022-07-03'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1044. Longest Duplicate Substring
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1044}/>
 
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

> Example 1:

> Input: s <TeX>=</TeX> "banana"
> Output: "ana"

> Example 2:

> Input: s <TeX>=</TeX> "abcd"
> Output: ""

**Constraints:**

> 2 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 3 * 104

> s consists of lowercase English letters.

## Solution
We will use the fact that if a size of k is longest duplicated substring, we can find duplicated substring k - 1 and we can not find duplicated substring k + 1. We can use binary search to test the size from 1 to n - 1. We can use sliding windows to search through the string. We can put the substring in the set and test whether substring can be found in the set or not.

### Python
```python
def longestDupSubstring(self, s: str) -> str:
  n = len(s)
  def search(s, k):
    stringSet = set()
    for i in range(n - k + 1):
      substring = s[i: i + k]
      if substring in stringSet:
        return substring
      else:
        stringSet.add(substring)
    return None

  ans = search(s, 1)
  if ans is None:
    return ""
  ans = search(s, n - 1)
  if ans is not None:
    return ans
  low = 1 # return not None
  high = n - 1 # return None
  while low + 1 < high:
    mid = (low + high) // 2
    res = search(s, mid)
    if res is None:
      high = mid
    else:
      low = mid
  ans = search(s, low + 1)
  if ans is not None:
    return ans
  return search(s, low)

```
