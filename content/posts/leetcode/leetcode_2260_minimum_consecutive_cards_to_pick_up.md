---
title: 2260. Minimum Consecutive Cards to Pick Up
date: '2022-11-12'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2260. Minimum Consecutive Cards to Pick Up
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2260}/>
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

 > Example 1:

 > Input: cards = [3,4,2,3,4,7]
 > Output: 4
 > Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

 > Example 2:

 > Input: cards = [1,0,5,3]
 > Output: -1
 > Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.

**Constraints:**

 > 1 <TeX>\leq</TeX> cards.length <TeX>\leq</TeX> 10^5

 > 0 <TeX>\leq</TeX> cards[i] <TeX>\leq</TeX> 10^5


## Solution
Solution: Let's use sliding window to solve it. 

We will not use frequency dictionary sinced it will need to iterate through the elements. We will use a set and a duplicated list to store the elements inside the window and the duplicated element. We will use the list to store to the duplicated element rather than use a number to store it because we want it to be passed as reference. 


### Python
```python
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
```
