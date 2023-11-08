---
title: 966. Vowel Spellchecker
date: '2022-06-18'
tags: ['leetcode', 'python', 'medium']
draft: false
description: Solution for leetcode 0966. Vowel Spellchecker
---


Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.

Example: wordlist <TeX>=</TeX> ["yellow"], query <TeX>=</TeX> "YellOw": correct <TeX>=</TeX> "yellow"

Example: wordlist <TeX>=</TeX> ["Yellow"], query <TeX>=</TeX> "yellow": correct <TeX>=</TeX> "Yellow"

Example: wordlist <TeX>=</TeX> ["yellow"], query <TeX>=</TeX> "yellow": correct <TeX>=</TeX> "yellow"

Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.

Example: wordlist <TeX>=</TeX> ["YellOw"], query <TeX>=</TeX> "yollow": correct <TeX>=</TeX> "YellOw"

Example: wordlist <TeX>=</TeX> ["YellOw"], query <TeX>=</TeX> "yeellow": correct <TeX>=</TeX> "" (no match)

Example: wordlist <TeX>=</TeX> ["YellOw"], query <TeX>=</TeX> "yllw": correct <TeX>=</TeX> "" (no match)

In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.

When the query matches a word up to capitlization, you should return the first such match in the wordlist.

When the query matches a word up to vowel errors, you should return the first such match in the wordlist.

If the query has no matches in the wordlist, you should return the empty string.

Given some queries, return a list of words answer, where answer[i] is the correct word for query <TeX>=</TeX> queries[i].

Example 1:

Input: wordlist <TeX>=</TeX> ["KiTe","kite","hare","Hare"], queries <TeX>=</TeX> ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

Example 2:

Input: wordlist <TeX>=</TeX> ["yellow"], queries <TeX>=</TeX> ["YellOw"]
Output: ["yellow"]

**Constraints:**

1 <TeX>\leq</TeX> wordlist.length, queries.length <TeX>\leq</TeX> 5000

1 <TeX>\leq</TeX> wordlist[i].length, queries[i].length <TeX>\leq</TeX> 7

wordlist[i] and queries[i] consist only of only English letters.




## Solution


### Python
```python
def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
words = set(wordlist)
wordsCap = {}
wordsVow = {}
def replaceVowel(word):
return "".join(list(map(lambda i: "*" if word[i] in "AEIOU" else word[i], range(len(word)))))
for i in range(len(wordlist)):
wordUpper = wordlist[i].upper()
if wordUpper in wordsCap:
wordsCap[wordUpper] = wordsCap[wordUpper] + [wordlist[i]]
else:
wordsCap[wordUpper] = [wordlist[i]]
wordVowel = replaceVowel(wordUpper)
if wordVowel in wordsVow:
wordsVow[wordVowel] = wordsVow[wordVowel] + [wordlist[i]]
else:
wordsVow[wordVowel] = [wordlist[i]]
def processQuery(query):
if query in words:
return query
queryUpper = query.upper()
if queryUpper in wordsCap:
return wordsCap[queryUpper][0]
queryVowel = replaceVowel(queryUpper)
if queryVowel in wordsVow:
return wordsVow[queryVowel][0]
return ""
return list(map(processQuery, queries))

```
