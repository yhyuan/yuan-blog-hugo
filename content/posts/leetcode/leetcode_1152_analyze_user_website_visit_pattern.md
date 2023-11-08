---
title: 1152. Analyze User Website Visit Pattern
date: '2022-07-14'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 1152. Analyze User Website Visit Pattern
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1152}/>
 
You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.

The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.

Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.

Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.

Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

Example 1:

Input: username <TeX>=</TeX> ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp <TeX>=</TeX> [1,2,3,4,5,6,7,8,9,10], website <TeX>=</TeX> ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).

Example 2:

Input: username <TeX>=</TeX> ["ua","ua","ua","ub","ub","ub"], timestamp <TeX>=</TeX> [1,2,3,4,5,6], website <TeX>=</TeX> ["a","b","a","a","b","c"]
Output: ["a","b","a"]

Constraints:

3 <TeX>\leq</TeX> username.length <TeX>\leq</TeX> 50

1 <TeX>\leq</TeX> username[i].length <TeX>\leq</TeX> 10

timestamp.length <TeX>=</TeX><TeX>=</TeX> username.length

1 <TeX>\leq</TeX> timestamp[i] <TeX>\leq</TeX> 109

website.length <TeX>=</TeX><TeX>=</TeX> username.length

1 <TeX>\leq</TeX> website[i].length <TeX>\leq</TeX> 10

username[i] and website[i] consist of lowercase English letters.

It is guaranteed that there is at least one user who visited at least three websites.

All the tuples [username[i], timestamp[i], website[i]] are unique.


## Solution
First create a tuple list with username[i], timestamp[i], and website[i] and sort this tuple list to make it is ordered by username, timestamp, and website. 

Then, create a dictionary whose key is username and whose values are the list of visited website sorted by time stamp. 

Then, we need to go through every username and find the list of visited websites. Then, we use three for loops to get all possible patterns. But, we will have to remove the duplicated ones. Then, we add these patterns to a dictionary which is used to record the count. 

Finally, we find the max count and its pattern.

### Python
```python
def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
  n = len(username)
  records = list(map(lambda i: (username[i], timestamp[i], website[i]), range(n)))
  records.sort()
  n = len(records)
  userDict = {}
  for i in range(n):
    user = records[i][0]
    userDict[user] = userDict.get(user, [])
  pattersDict = {}
  for username in userDict:
    if len(userDict[username]) < 3:
      continue
    websites = userDict[username]
    patterns = []
    n = len(websites)
    for i in range(n - 2):
      for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
          p = (websites[i], websites[j], websites[k])
          patterns.append(p)
    patterns = set(patterns)
    for p in patterns:
      pattersDict[p] = pattersDict.get(p, 0) + 1
        
  # [a, b, c, d]
  maxCount = 0
  maxPatterns = []
  for p in pattersDict:
    if pattersDict[p] > maxCount:
      maxPatterns = [p]
      maxCount = pattersDict[p]
    elif pattersDict[p] == maxCount:
      maxPatterns = maxPatterns + [p]
  maxPatterns.sort()
  #print(maxPatterns)
  return list(maxPatterns[0])
```
