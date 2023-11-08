---
title: 828. Count Unique Characters of All Substrings of a Given String
date: '2022-05-22'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 828. Count Unique Characters of All Substrings of a Given String
---

 
Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s <TeX>=</TeX> "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) <TeX>=</TeX> 5.

Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example 1:

Input: s <TeX>=</TeX> "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 <TeX>=</TeX> 10

Example 2:

Input: s <TeX>=</TeX> "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") <TeX>=</TeX> 1.

Example 3:

Input: s <TeX>=</TeX> "LEETCODE"
Output: 92

Constraints:

1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 105

s consists of uppercase English letters only.

## Solution
Let's use count to record the result for the substrings end at i. If we add the count at different i, we will get the result. 

In order to calculate count, let's analyze the following pattern. Let's assume that we have X at position i and we have processed a very long string and have met X many times. 

....X....X.......X     

Before X is met, we have the following string:

....X....X....... 

Its substrings  which also ends at i - 1 are 

...X....X.......

..X....X.......

.X....X.......

X....X.......

....X.......

....X.......

...X.......

..X.......

.X.......

X.......

.......

......

.....

....

...

..

.

If we added X at i, we notice that if there are two X in the substring, the unique count will not change if we add one more X in the end.

If there is one X in the substring, the unique count will decrease one for each substring after one more X is added to the end. 

Finally, if there is no X in the substring, the unique count will increase one for each substring after one X is added to the end. 

Therefore, in order to calculate count after one X is added, we will need to know the distance between this new X and the previous X and we also need to know the distance between the previous X and the previous previous X. The former will bring the increase of the count and the later will bring the decrease of the count. 

 So we need to record three variables for each location.

count: The result for the substring ends at i.

preLocation: record the location of each character before current location i. This will help us calculate the distance between current location and previousLocation. 

prevCount: record the distance between the previous character and previous previous character. 

count <TeX>=</TeX> count + (i - previousLocation[ch]) + previousCount[ch]

previousCount <TeX>=</TeX> i - previousLocation[ch]

previousLocation[ch] <TeX>=</TeX> i

### Python
```python
def uniqueLetterString(self, s: str) -> int:
  n = len(s)
  dp = (0, [-1] * 26, [0] * 26)
  ans = 0
  for i in range(n):
    (count, preLocation, preCount) = dp
    index = ord(s[i]) - ord('A')
    count += (i - preLocation[index])
    count -= preCount[index]
    preCount[index] = i - preLocation[index]
    preLocation[index] = i
    dp = (count, preLocation, preCount)
    ans += count
  return ans
```
