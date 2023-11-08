---
title: 1216. Valid Palindrome III
date: '2022-07-21'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1216. Valid Palindrome III
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1216}/>

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 > Example 1:

 > Input: s = "abcdeca", k = 2
 > Output: true
 > Explanation: Remove 'b' and 'e' characters.

 > Example 2:

 > Input: s = "abbababa", k = 1
 > Output: true

**Constraints:**

 > 1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 1000

 > s consists of only lowercase English letters.

 > 1 <TeX>\leq</TeX> k <TeX>\leq</TeX> s.length


## Solution
dp[i, j, k] represent substring s[i, j] is k palindrome or not.

k = 0. it is easy to handle. 

the substring length is 1 or 2 and k > 0. it always return True. 

if s[i] == s[j], the problem is converted to dp[i + 1, j - 1, k]. 

otherwise, the problem is converted to two cases: we can remove i th character or we remove the j th character and turn the problem to dp[i + 1, j, k - 1] or dp[i, j -1, k - 1]. If one of them return True, we will get True.

### Python
```python
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def helper(i, j, k):
            if k == 0:
                isPalindrome = True
                while i < j:
                    if s[i] != s[j]:
                        isPalindrome = False
                        break
                    i += 1
                    j -= 1
                return isPalindrome
            if i == j or i + 1 == j:
                return True
                
            if s[i] == s[j]:
                return helper(i + 1, j - 1, k)
            return helper(i + 1, j, k - 1) or helper(i, j - 1, k - 1)
                    
        n = len(s)
        return helper(0, n - 1, k)

```
