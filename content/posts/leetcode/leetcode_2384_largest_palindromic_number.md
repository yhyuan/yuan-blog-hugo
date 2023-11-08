---
title: 2384. Largest Palindromic Number
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: 2384. Largest Palindromic Number
---


You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.

The digits can be reordered.

> Example 1:
> Input: num = "444947137"
> Output: "7449447"
> Explanation:
> Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
> It can be shown that "7449447" is the largest palindromic integer that can be formed.
> Example 2:
> Input: num = "00009"
> Output: "9"
> Explanation:
> It can be shown that "9" is the largest palindromic integer that can be formed.
> Note that the integer returned should not contain leading zeroes.
**Constraints:**
> 1 <TeX>\leq</TeX> num.length <TeX>\leq</TeX> 105
> num consists of digits.


## Solution


### Python
```python
class Solution:
def largestPalindromic(self, num: str) -> str:
digitsDict = {}
for dig in num:
digitsDict[dig] = digitsDict.get(dig, 0) + 1
def helper(digitsDict):


# Find the largest digit with more or equal to 2 times and the digits can not be zero.


# If none can be found, find the largest digit.
def findLargestDigit(digitsDict, freq):
for dig in '9876543210':
if dig in digitsDict and digitsDict[dig] >= freq:
return dig
return None
largestDigit = findLargestDigit(digitsDict, 2)
if largestDigit is not None:
digitsDict[largestDigit] -= 2
return largestDigit + helper(digitsDict) + largestDigit

largestDigit = findLargestDigit(digitsDict, 1)
return "" if largestDigit is None else largestDigit
res = helper(digitsDict)
def removeZeros(res):
n = len(res)
index = -1
for i in range(n):
if res[i] != '0':
index = i
break
if index == -1:
return "0"
return res[index: n - index]
return removeZeros(res)
```
