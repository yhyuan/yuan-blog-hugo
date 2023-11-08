---
title: 1092. Shortest Common Supersequence
date: '2022-07-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1092. Shortest Common Supersequence
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1092}/>
 
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 > Example 1:

 > Input: str1 = "abac", str2 = "cab"
 > Output: "cabac"
 > Explanation: 
 > str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
 > str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
 > The answer provided is the shortest such string that satisfies these properties.

 > Example 2:

 > Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
 > Output: "aaaaaaaa"

**Constraints:**

 > 1 <TeX>\leq</TeX> str1.length, str2.length <TeX>\leq</TeX> 1000

 > str1 and str2 consist of lowercase English letters.


## Solution
let dp[i][j] represent the result for str1[0 : i + 1] and str2[0:j + 1] .

i = 0 and j = 0. Both of them are just one character. 

i = 0 and j larger than 0. One string is a one character string. 

i larger than 0 and j = 0. One string is one character string. 

if str1[i] == str2[j], the question is simplified to (i - 1, j -1) and add str1[i] in the end. 

Otherwise, we compare the result from (i - 1, j) and (i, j - 1) and use the minimal result add the related character in the ending.


### Python
```python
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        @cache
        def helper(i, j):
            if i == 0 and j == 0:
                return str2[0] if str1[0] == str2[0] else str1[0] + str2[0]
            if i == 0:
                return str2[: j + 1] if str1[0] in str2[: j + 1] else str1[0] + str2[: j + 1]
            if j == 0:
                return str1[: i + 1] if str2[0] in str1[: i + 1] else str2[0] + str1[: i + 1]
            if str1[i] == str2[j]:
                return helper(i - 1, j - 1) + str1[i]
            res1 = helper(i - 1, j)
            res2 = helper(i, j - 1)            
            return  res1 + str1[i] if len(res1) < len(res2) else res2 + str2[j]
        return helper(m - 1, n - 1)
```
Solution with less mememory
```python
        pre_memo = [""] * n
        memo = [""] * n
        def helper(i, j):
            if i == 0 and j == 0:
                memo[j] = str2[0] if str1[0] == str2[0] else str1[0] + str2[0]
                return memo[j]
            if i == 0: # j != 0
                memo[j] = str2[: j + 1] if str1[0] in str2[: j + 1] else str1[0] + str2[: j + 1]
                return memo[j]
            if j == 0:
                memo[j] = str1[: i + 1] if str2[0] in str1[: i + 1] else str2[0] + str1[: i + 1]
                return memo[j] 
            if str1[i] == str2[j]:
                memo[j] = pre_memo[j - 1] + str1[i]
                return memo[j]
            res1 = pre_memo[j]
            res2 = memo[j - 1]         
            memo[j] = res1 + str1[i] if len(res1) < len(res2) else res2 + str2[j]
            return memo[j]
        for i in range(m):
            for j in range(n):
                helper(i, j)
            pre_memo = memo.copy()
            memo = [""] * n
        return pre_memo[-1]
```

