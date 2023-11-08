---
title: 472. Concatenated Words
date: '2022-03-14'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 472. Concatenated Words
---


Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

> Example 1:
> Input: words <TeX>=</TeX> ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
> Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
> Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
> "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
> "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
> Example 2:
> Input: words <TeX>=</TeX> ["cat","dog","catdog"]
> Output: ["catdog"]
**Constraints:**
> 1 <TeX>\leq</TeX> words.length <TeX>\leq</TeX> 104
> 1 <TeX>\leq</TeX> words[i].length <TeX>\leq</TeX> 30
> words[i] consists of only lowercase English letters.
> All the strings of words are unique.
> 1 <TeX>\leq</TeX> sum(words[i].length) <TeX>\leq</TeX> 105


## Solution
The key to solve this problem is to have a function which can judge whether a word is a concatenated word or not. Then, we can go through word by word. If the time complexity of this function is O(m) (m is the length of the word), the time complexity will be O(mN).  If it is a concatenated word, we can have more than two cutting positions.
```python
def calculatePositions(word, words):
def helper(word, index):


# If succeed, we will return the ending index
if index >= len(word):
return [index]
for i in range(index + 1, len(word) + 1):
subWord = word[index:i]


# try to cut in the positions from index + 1
if subWord in words:
res = helper(word, i)
if len(res) > 0:
return [index] + res


#If we failed, we returned an empty array
return []
return helper(word, 0)
```


### Python
```python
class Solution:
def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
words = set(words)
def calculatePositions(word, words):
def helper(word, index):
if index >= len(word):
return [index]
for i in range(index + 1, len(word) + 1):
subWord = word[index:i]
if subWord in words:
res = helper(word, i)
if len(res) > 0:
return [index] + res
return []
return helper(word, 0)
ans = []

for word in words:
res = calculatePositions(word, words)
if len(res) > 2:
ans.append(word)
return ans
```
