---
title: 1520. Maximum Number of Non-Overlapping Substrings
date: '2022-08-12'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 1520. Maximum Number of Non-Overlapping Substrings
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1520}/>

Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.

A substring that contains a certain character c must also contain all occurrences of c.

Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 > Example 1:

 > Input: s <TeX>=</TeX> "adefaddaccc"
 > Output: ["e","f","ccc"]
 > Explanation: The following are all the possible substrings that meet the conditions:
 > [
 >   "adefaddaccc"
 >   "adefadda",
 >   "ef",
 >   "e",
 >   "f",
 >   "ccc",
 > ]
 > If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

 > Example 2:

 > Input: s <TeX>=</TeX> "abbaccd"
 > Output: ["d","bb","cc"]
 > Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

**Constraints:**

 > 1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 105

 > s contains only lowercase English letters.

## Solution
Firstly we find each character's starting index, ending index, and count. We basically found multiple intervals with counts. If these intervals do not overlap with other, we can simply add them to the results. If they overlap each other, we want to merge them together. If the merged length is equal to the total count, we have found the qualified interval. We also need to add it to the result.

### Python
```python
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        starts = [-1] * 26
        ends   = [-1] * 26
        counts = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if starts[index] == -1:
                starts[index] = i
            ends[index] = i
            counts[index] += 1

        endIndices = []
        for index in range(26):
            if ends[index] >= 0:
                endIndices.append((ends[index], starts[index], counts[index] , chr(index + ord('a'))))
        endIndices.sort() 
# Interval scheduling algorithm (Greedy) https://en.wikipedia.org/wiki/Interval_scheduling
        ans = []
        total = 0
        left = None
        for i in range(len(endIndices)):
            (end, start, count, ch) = endIndices[i]
            if end - start + 1 == count:
 # no other characters between start and end.
                ans.append(s[start: end + 1])
                left = None
                total = 0
            else:
                if left is None:
                    left = start
                else:
                    left = min(left, start)
                right = end
                total += count
                if right - left + 1 == total:
                    ans.append(s[left: right + 1])
                    left = None
                    total = 0
        return ans
```
