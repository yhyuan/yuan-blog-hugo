---
title: Pattern 1 Sliding Window
date: '2022-10-03'
tags: ['leetcode', 'pattern']
draft: false
description: Pattern 1 Sliding Window
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

## Problem solving boilerplate code
### 1) Fixed sliding window
````python
def fixedSlidingWindow(arr, k):
  n = len(arr)
  for i in range(0, n - k + 1):
    if i == 0: 
      calculateWindow(0, k - 1) # [0, k - 1]
    else: 
      updateWindowRemove(i - 1)
      updateWindowAdd(i + k - 1)
  return ans
````
### 2) Minimum sliding window
````python
def minSlidingWindow(nums):
  i = j = size = 0
  ans = float('inf')
  n = len(nums)
  while i < n:
    while i < n and not meetCondition():
      updateConditionAdd(i)
      i += 1
      size += 1
    if not meetCondition():
      break
    while j < n and meetCondition():
      updateConditionRemove(j)
      j += 1
      size -= 1
    # [j - 1, i - 1]    
    ans = min(ans, size + 1)   
  return ans
````
### 3) Maximum sliding window
````python
def maxSlidingWindow(nums):
  i = j = size = 0
  ans = 0
  n = len(nums)
  while i < n:
    while i < n and meetCondition():
      updateConditionAdd(i)
      i += 1
      size += 1
    if meetCondition():
      ans = max(ans, size)
      break
    else:
      # size - 1 is current window size that meet condition
      ans = max(ans, size - 1)
    while j < n and not meetCondition():
      updateConditionRemove(j)
      j += 1
      size -= 1
  return ans
````

## Problems
### 1. Fixed Sliding Window

<LeetCode.ProblemCard id={643}/>
> Given an array, find the average of all contiguous subarrays of size K in it.

````python
def findMaxAverage(arr, k):
  n = len(arr)
  total = 0
  ans = -float('inf')
  for i in range(0, n - k + 1):
    if i == 0: 
      # total = calculateWindow(0, k - 1) # [0, k - 1]
      for j in range(k):
        total += arr[j]
    else: 
      # updateWindowRemove(i - 1)
      total -= arr[i - 1]
      #updateWindowAdd(i + k - 1)
      total += arr[i + k - 1]

    ans = max(ans, total / k)
  return ans
````
<LeetCode.ProblemCard id={1708}/>
> Given an array of positive numbers and a positive number K, find the maximum sum of any contiguous subarray of size K.
````python
def maxSubarrayOfSizeK(arr, k):
  n = len(arr)
  total = 0
  ans = -float('inf')
  for i in range(0, n - k + 1):
    if i == 0: 
      # total = calculateWindow(0, k - 1) # [0, k - 1]
      for j in range(k):
        total += arr[j]
    else: 
      # updateWindowRemove(i - 1)
      total -= arr[i - 1]
      #updateWindowAdd(i + k - 1)
      total += arr[i + k - 1]
    ans = max(ans, total)
  return ans
````

- The time complexity of the above algorithm will be O(N)
- The space complexity of the above algorithm will be O(1)
<LeetCode.ProblemCard id={567}/>
> Given a string and a pattern, find out if the <b>string contains any permutation of the pattern</b>.

<b>Permutation</b> is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
- abc
- acb
- bac
- bca
- cab
- cba

If a string has n distinct characters, it will have n! permutations.
````python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def calculateFreq(s):
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] +=  1
            return freq
        def compareFreq(freq1, freq2):
            for i in range(26):
                if freq1[i] != freq2[i]:
                    return False
            return True
        n = len(s2)
        k = len(s1)
        if n < k:
            return False
        freq1 = calculateFreq(s1)
        for i in range(n - k + 1):
            if i == 0:
                freq2 = calculateFreq(s2[:k])
            else:
                # updateWindowRemove(i - 1)
                freq2[ord(s2[i - 1]) - ord('a')] -= 1
                #updateWindowAdd(i + k - 1)
                freq2[ord(s2[i + k - 1]) - ord('a')] += 1
            if compareFreq(freq1, freq2):
                return True
        return False
````
- The above algorithms time complexity will be O(N + M), where N and M are the number of characters in the input string and the pattern, respectively.
- The algorithms space complexity is O(M) since, in the worst case, the whole pattern can have distinct characters that will go into the <b>HashMap</b>.

<LeetCode.ProblemCard id={438}/>
> Given a string and a pattern, <b>find all anagrams of the pattern in the given string</b>.

Every <b>anagram</b> is a <b>permutation</b> of a string. 

As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N! permutations (or anagrams) of a string having N characters. For example, here are the six anagrams of the string “abc”:
- abc
- acb
- bac
- bca
- cab
- cba

> Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

````python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def calculateFreq(s):
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] +=  1
            return freq
        def compareFreq(freq1, freq2):
            for i in range(26):
                if freq1[i] != freq2[i]:
                    return False
            return True
        n = len(s)
        k = len(p)
        if n < k:
            return False
        freq1 = calculateFreq(p)
        ans = []
        for i in range(n - k + 1):
            if i == 0:
                freq2 = calculateFreq(s[:k])
            else:
                # updateWindowRemove(i - 1)
                freq2[ord(s[i - 1]) - ord('a')] -= 1
                #updateWindowAdd(i + k - 1)
                freq2[ord(s[i + k - 1]) - ord('a')] += 1
            if compareFreq(freq1, freq2):
                ans.append(i)
        return ans
````

- The time complexity of the above algorithm will be O(N + M) where N and M are the number of characters in the input string and the pattern respectively.
- The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the <b>HashMap</b>. In the worst case, we also need O(N) space for the result list, this will happen when the pattern has only one character and the string contains only that character.
<LeetCode.ProblemCard id={30}/>
Given a string and a list of words, find all the starting indices of substrings in the given string that are a <b>concatenation of all the given words</b> exactly once without any <b>overlapping of words</b>. It is given that all words are of the same length.

````python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def calculateFreq(s):
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            return freq
        def compareFreq(freq1, freq2):
            for i in range(26):
                if freq1[i] != freq2[i]:
                    return False
            return True
        def helper(s, words):
            wordLen = len(s) // len(words)
            newWords = []
            for i in range(len(words)):
                # [i * wordLen : i * wordLen + wordLen]
                newWords.append(s[i * wordLen : i * wordLen + wordLen])
            newWords.sort()
            for i in range(len(words)):
                if words[i] != newWords[i]:
                    return False
            return True

        wordsString = "".join(words)
        targetFreq = calculateFreq(wordsString)
        n = len(s)
        if n < len(wordsString):
            return []
        k = len(wordsString)
        freq = [0] * 26
        ans = []
        #wordsSet = set(words)
        words.sort()
        for i in range(n - k + 1):
            if i == 0:
                freq = calculateFreq(s[:k])
            else:
                # i - 1 out and i + k - 1 in
                freq[ord(s[i - 1]) - ord('a')] -= 1
                freq[ord(s[i + k - 1]) - ord('a')] += 1
            if compareFreq(freq, targetFreq) and helper(s[i: i + k], words):
                ans.append(i)
        return ans
````

- The time complexity of the above algorithm will be O(N * M * Len) where N is the number of characters in the given string, M is the total number of words, and Len is the length of a word.
- The space complexity of the algorithm is O(M) since at most, we will be storing all the words in the two <b>HashMaps</b>. In the worst case, we also need O(N) space for the resulting list. So, the overall space complexity of the algorithm will be O(M+N).

### 2. Minimum sliding window
<LeetCode.ProblemCard id={209}/>
> Given an array of positive numbers and a positive number S, find the length of the <b>smallest contiguous subarray whose sum is greater than or equal to S</b>. 
> 
> Return 0 if no such subarray exists.

````python
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    i = j = size = 0
    n = len(nums)
    ans = float('inf')
    total = 0
    def meetCondition(total, target):
        return total >= target
    while i < n:
        while i < n and not meetCondition(total, target):
            # updateConditionAdd(s, i)
            total += nums[i]
            i += 1
            size += 1
        if not meetCondition(total, target):
            break
        while j < n and meetCondition(total, target):
            # updateConditionRemove(s, j)
            total -= nums[j]
            j += 1
            size -= 1
        # [j - 1, i - 1]
        ans = min(ans, size + 1)    
    return 0 if ans == float('inf') else ans        
````

- The time complexity of the above algorithm will be O(N). 
- The algorithm runs in constant space O(1).
<LeetCode.ProblemCard id={76}/>
> Given a string and a pattern, find the <b>smallest substring</b> in the given string which has <b>all the characters of the given pattern</b>.

````python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        def calculateFreq(s):
            freq = [0] * 52
            for ch in s:
                if ch >= 'A' and ch <= 'Z':
                    freq[ord(ch) - ord('A') + 26] += 1
                else:
                    freq[ord(ch) - ord('a')] += 1
            return freq
        def meetCondition(freq1, freq2):
            for i in range(52):
                if freq1[i] > freq2[i]:
                    return False
            return True
        t_freq = calculateFreq(t)     
        i = 0
        j = 0
        size = 0
        ans = 0
        freq = [0] * 52
        n = len(s)
        ans = [0, n] # start and end
        while i < n:
            # add ch until the condition is meeting. 
            while i < n and not meetCondition(t_freq, freq):
                if s[i] >= 'A' and s[i] <= 'Z':
                    freq[ord(s[i]) - ord('A') + 26] += 1
                else:
                    freq[ord(s[i]) - ord('a')] += 1
                i += 1
                size += 1
            # print("i: {}".format(i))
            if not meetCondition(t_freq, freq):
                break
            while j < i and meetCondition(t_freq, freq):
                if s[j] >= 'A' and s[j] <= 'Z':
                    freq[ord(s[j]) - ord('A') + 26] -= 1
                else:
                    freq[ord(s[j]) - ord('a')] -= 1
                size -= 1
                j += 1
            # [i - 1, j - 1]
            if ans[1] - ans[0] + 1 > size:
                ans = [j - 1, i - 1]
        if ans[0] == 0 and ans[1] == n:
            return ""
        return s[ans[0]: ans[1] + 1]      
````
- The time complexity of the above algorithm will be O(N + M) where N and M are the number of characters in the input string and the pattern respectively.
- The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the <b>HashMap</b>. In the worst case, we also need O(N) space for the resulting substring, which will happen when the input string is a permutation of the pattern.

<LeetCode.ProblemCard id={2260}/>
> Given a array of integers, find the minimum length of the sub array that contain duplicated elements. 
> The only tricky part is that we will use a set and a duplicated list to store the elements and duplicated element inside the sliding window.
````python
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        nums = cards
        i = j = size = 0
        ans = float('inf')
        n = len(nums)
        cardSet = set([])
        duplicated = [None]
        def meetCondition():
            return duplicated[0] is not None
        def updateConditionAdd(i):
            if nums[i] in cardSet:
                duplicated[0] = nums[i]
            else:
                cardSet.add(nums[i])
            return
        def updateConditionRemove(j):
            if nums[j] in cardSet:
                if duplicated[0] == nums[j]:
                    duplicated[0] = None
                else:
                    cardSet.remove(nums[j])
            return
        while i < n:
            while i < n and not meetCondition():
                updateConditionAdd(i)
                i += 1
                size += 1
            if not meetCondition():
                break
            while j < n and meetCondition():
                updateConditionRemove(j)
                j += 1
                size -= 1
            # [j - 1, i - 1]        
            ans = min(ans, size + 1)     
        return -1 if ans == float('inf') else ans
````

### 3. Maximum sliding window
<LeetCode.ProblemCard id={340}/>
>Given a string, find the length of the <b>longest substring</b> in it with <b>no more than K distinct characters</b>.
>
>You can assume that K is less than or equal to the length of the given string.
````python
def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
  i = j = size = 0
  ans = 0
  n = len(s)
  freq = {}
  def meetCondition(freq, k):
    return len(freq.keys()) <= k
  while i < n:
    while i < n and meetCondition(freq, k):
      # updateConditionAdd(s, i)
      freq[s[i]] = freq.get(s[i], 0) + 1
      i += 1
      size += 1
    if meetCondition(freq, k):
      ans = max(ans, size)
      break
    else:
      # size - 1 is current window size that meet condition
      ans = max(ans, size - 1)
    while j < n and not meetCondition(freq, k):
      #updateConditionRemove(s, j)
      if freq[s[j]] == 1:
        del freq[s[j]]
      else:
        freq[s[j]] -= 1
      j += 1
      size -= 1
  return ans
````

- The above algorithms time complexity will be O(N)
- The algorithms space complexity is O(K), as we will be storing a maximum of K+1 characters in the <b>HashMap</b>.
<LeetCode.ProblemCard id={904}/>
> Given an array of characters where each character represents a fruit tree, you are given <b>two baskets</b>, and your goal is to put the <b>maximum number of fruits in each basket</b>. The only restriction is that <b>each basket can have only one type of fruit</b>.
>
> You can start with any tree, but you cant skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
>
> Write a function to return the maximum number of fruits in both baskets.

````python
def totalFruit(self, fruits: List[int]) -> int:
  i = j = size = 0
  ans = 0
  n = len(fruits)
  freq = {}
  def meetCondition(freq):
    return len(freq.keys()) <= 2
  while i < n:
    while i < n and meetCondition(freq):
      # updateConditionAdd(s, i)
      freq[fruits[i]] = freq.get(fruits[i], 0) + 1
      i += 1
      size += 1
    if meetCondition(freq):
      ans = max(ans, size)
      break
    else:
      # size - 1 is current window size that meet condition
      ans = max(ans, size - 1)
    while j < n and not meetCondition(freq):
      #updateConditionRemove(s, j)
      if freq[fruits[j]] == 1:
        del freq[fruits[j]]
      else:
        freq[fruits[j]] -= 1
      j += 1
      size -= 1
  return ans
````


- The above algorithms time complexity will be O(N)
- The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency map.
<LeetCode.ProblemCard id={159}/>
> Given a string, find the length of the longest substring in it with at most two distinct characters.

````python
def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
  i = j = size = 0
  ans = 0
  n = len(s)
  freq = {}
  def meetCondition(freq):
    return len(freq.keys()) <= 2
  while i < n:
    while i < n and meetCondition(freq):
      # updateConditionAdd(s, i)
      freq[s[i]] = freq.get(s[i], 0) + 1
      i += 1
      size += 1
    if meetCondition(freq):
      ans = max(ans, size)
      break
    else:
      # size - 1 is current window size that meet condition
      ans = max(ans, size - 1)
    while j < n and not meetCondition(freq):
      #updateConditionRemove(s, j)
      if freq[s[j]] == 1:
        del freq[s[j]]
      else:
        freq[s[j]] -= 1
      j += 1
      size -= 1
  return ans
````
<LeetCode.ProblemCard id={3}/>
> Given a string, find the <b>length of the longest substring</b>, which has <b>no repeating characters</b>.

````python
def lengthOfLongestSubstring(self, s: str) -> int:
  i = j = size = 0
  ans = 0
  n = len(s)
  freq = {}
  def meetCondition(freq):
    for ch in freq:
        if freq[ch] > 1:
            return False
    return True  
  while i < n:
    while i < n and meetCondition(freq):
      # updateConditionAdd(s, i)
      freq[s[i]] = freq.get(s[i], 0) + 1
      i += 1
      size += 1
    if meetCondition(freq):
      ans = max(ans, size)
      break
    else:
      # size - 1 is current window size that meet condition
      ans = max(ans, size - 1)
    while j < n and not meetCondition(freq):
      #updateConditionRemove(s, j)
      if freq[s[j]] == 1:
        del freq[s[j]]
      else:
        freq[s[j]] -= 1
      j += 1
      size -= 1
  return ans
````
- The above algorithms time complexity will be O(N), where N is the number of characters in the input string.
- The algorithms space complexity will be O(K), where K is the number of distinct characters in the input string. 
<LeetCode.ProblemCard id={424}/>
> Given a string with lowercase letters only, if you are allowed to <b>replace no more than K letters</b> with any letter, find the <b>length of the longest substring having the same letters</b> after replacement.
````python
    def characterReplacement(self, s: str, k: int) -> int:
        # highest freq. non highest freq letters total is k. 
        n = len(s)
        i = 0
        j = 0
        size = 0
        freq = {}
        ans = 0
        def meetCondition(freq, k):
            maxFreq = -1
            maxFreqKey = ""
            for key in freq:
                if freq[key] > maxFreq:
                    maxFreq = freq[key]
                    maxFreqKey = key
            total = 0
            for key in freq:
                if key != maxFreqKey:
                    total += freq[key]
            return total <= k
            
        while i < n:
            while i < n and meetCondition(freq, k):
                freq[s[i]] = freq.get(s[i], 0) + 1
                size += 1
                i += 1
            #print(meetCondition(freq, k))
            if meetCondition(freq, k):
                ans = max(ans, size)
                break
            else:
                ans = max(ans, size - 1)
            while j < i and not meetCondition(freq, k):
                if freq[s[j]] == 1:
                    del freq[s[j]]
                else:
                    freq[s[j]] -= 1
                size -= 1
                j += 1
        return ans
````

- The above algorithms time complexity will be O(N), where N is the number of letters in the input string.
- As we expect only the lower case letters in the input string, we can conclude that the space complexity will be O(26) to store each letters frequency in the <b>HashMap</b>, which is asymptotically equal to O(1).

<LeetCode.ProblemCard id={1004}/>
> Given an array containing 0's and 1's, if you are allowed to <b>replace no more than K 0's with 1's</b>, 
> find the length of the <b>longest contiguous subarray having all 1's</b>.
````python
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding windown. Count of 0 <= k
        def meetCondition(countZero, k):
            return countZero <= k
        i = 0
        j = 0
        size = 0
        countZero = 0
        ans = 0
        n = len(nums)
        while i < n:
            while i < n and meetCondition(countZero, k):
                if nums[i] == 0:
                    countZero += 1
                size += 1
                i += 1
            if meetCondition(countZero, k):
                ans = max(ans, size)
                break
            else:
                ans = max(ans, size - 1)
            while j < i and not meetCondition(countZero, k):
                if nums[j] == 0:
                    countZero -= 1
                size -= 1
                j += 1
        return ans
````
- The above algorithms time complexity will be O(N), where N is the count of numbers in the input array.
- The algorithm runs in constant space O(1).
