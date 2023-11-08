---
title: 1246. Palindrome Removal
date: '2022-07-22'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1246. Palindrome Removal
---

 
Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i <TeX>\leq</TeX> j, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.

 > Example 1:

 > Input: arr = [1,2]
 > Output: 2

 > Example 2:

 > Input: arr = [1,3,4,1,5]
 > Output: 3
 > Explanation: Remove [4] then remove [1,3,1] then remove [5].

**Constraints:**

 > 1 <TeX>\leq</TeX> arr.length <TeX>\leq</TeX> 100

 > 1 <TeX>\leq</TeX> arr[i] <TeX>\leq</TeX> 20

## Solution
Let's define dp[i][j] as the result for subarray [i, j] and the result will be dp[0][n - 1]. 

i = j. The length of subarray is 1. The result is 1. 

i + 1 = j. The length of subarray is 2. The result is 1 if arr[i] == arr[j]. Otherwise, it is 2. 

For subarray [i, j]. If arr[i] == arr[j], the problem is reduced to [i + 1, j - 1]. 

For subarray [i, j], we will divide it two smaller subarrays: [i, k], [k + 1, j]. The result for [i, j] will be minimal value of these divisions. 

### Python
Top down approach
```python
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        memo = {}
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j:
                return 0
            if i == j:
                memo[(i, i)] = 1
                return 1
            if i + 1 == j:
                memo[(i, j)] = 1 if arr[i] == arr[j] else 2
                return memo[(i, j)]
            if arr[i] == arr[j]:
                ans = helper(i + 1, j - 1)
                memo[(i, j)] = ans
                return ans
            ans = float('inf')
            for k in range(i, j):
                res = helper(i, k) + helper(k + 1, j)
                ans = min(ans, res)
            memo[(i, j)] = ans
            return ans
        return helper(0, n - 1) 
```
Bottom up approach
```python
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] =1
        for i in range(n - 1):
            dp[i][i + 1] = 1 if arr[i] == arr[i + 1] else 2
        for size in range(3, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]
```