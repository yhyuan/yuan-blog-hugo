---
title: 1395. Count Number of Teams
date: '2022-08-05'
tags: ['leetcode', 'python', 'easy']
draft: false
description: Solution for leetcode 1395. Count Number of Teams
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1395}/>
 
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).

A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <TeX>\leq</TeX> i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 > Example 1:

 > Input: rating = [2,5,3,4,1]
 > Output: 3
 > Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

 > Example 2:

 > Input: rating = [2,1,3]
 > Output: 0
 > Explanation: We can't form any team given the conditions.

 > Example 3:

 > Input: rating = [1,2,3,4]
 > Output: 4

**Constraints:**

 > n == rating.length

 > 3 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000

 > 1 <TeX>\leq</TeX> rating[i] <TeX>\leq</TeX> 105

 > All the integers in rating are unique.


## Solution
Firstly we notice that (rating[i] > rating[j] > rating[k])  is as same as  (rating[i] < rating[j] < rating[k]) if we reverse the array. So We can create a function to calculate  (rating[i] < rating[j] < rating[k]). Then, we reverse the array and call the same function again. It will cover  (rating[i] > rating[j] > rating[k]) .

We can choose a element at i and calculate the number of elements before i which are smaller than the element at i and the number of elements after i which are larger than the element at i. The time complexity is O(N^2). Then, we multiple them together. The result will be that if we choose the element at i as the middle number. If we add all the results together. It will be final result. 

### Python
```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def helper(rating):
            #print(rating)
            n = len(rating)
            ans = 0
            for i in range(n):
                pre = len(list(filter(lambda j: rating[j] < rating[i], range(0, i))))
                post = len(list(filter(lambda j: rating[j] > rating[i], range(i + 1, n))))
                # print("i: {}, pre: {}, post: {}".format(i, pre, post))
                ans += pre * post
            return ans
        ans = helper(rating)
        rating.reverse()
        res = helper(rating)
        return ans + res

```
