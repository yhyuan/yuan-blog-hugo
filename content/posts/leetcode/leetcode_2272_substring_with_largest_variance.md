---
title: 2272. Substring With Largest Variance
date: '2022-09-28'
tags: ['leetcode', 'python']
draft: false
description: Solution for leetcode 2272. Substring With Largest Variance
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2272}/>

The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

 > Example 1:

 > Input: s <TeX>=</TeX> "aababbb"
 > Output: 3
 > Explanation:
 > All possible variances along with their respective substrings are listed below:
 > - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
 > - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
 > - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
 > - Variance 3 for substring "babbb".
 > Since the largest possible variance is 3, we return it.

 > Example 2:

 > Input: s <TeX>=</TeX> "abcde"
 > Output: 0
 > Explanation:
 > No letter occurs more than once in s, so the variance of every substring is 0.

**Constraints:**

 > 1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 104

 > s consists of lowercase English letters.

## Solution
The brute force method will need O(N^3) to solve it. We can use dynamic programming to reduce it to O(N^2) by recording the frequency between i and j. However, we can convert this question to a O(N) by converting to it a max subarray sum problem and solve it with Kadane's Algorithm. 

Calculate the letters in the string. 

Use two for loops to iterate all combinations. Because the maximum of the combinations is only 26x25. So it is still O(1).

Let's assign 1 to the first letter, assign -1 to another letter, assign 0 to other letters. The problem turn into find the result of maximum sum of a subarray. This problem can be solved by Kadane's Algorithm.


However, this Kadane's Algorithm needs the subarray at least contains one -1. Let's define that dp[i] is the max subarray with at least one -1 and the subarray ends at i. Let's figure the calculation of dp[i + 1]. If we can find the max element in dp, this is our result. We firstly need to add two more variables: start and valid. The start is used to mark current subarray's starting position and the valid is used to mark whether current subarray contains a -1 or not.

If nums[i + 1] <TeX>==</TeX> 1, obviously dp[i + 1] <TeX>=</TeX> dp[i] + 1

If nums[i + 1] <TeX>==</TeX> -1 and valid is false. It means the subarray ends with i is not valid. We will add this -1 behind and make it valid. Meanwhile, the dp[i + 1] <TeX>=</TeX> dp[i] - 1

If nums[i + 1] <TeX>==</TeX> -1 and valid is true and dp[i] is less than 0. It means we have included more -1 than 1 in the subarray. Since the minimal value of the result is at least 0, we will need to move the start to i and set the dp value to -1

If nums[i + 1] <TeX>==</TeX> -1 and valid is true and dp[i] <TeX>\geq</TeX> 0 and nums[start] <TeX>==</TeX> -1.  It means current subarray starts with a -1. Since we are going to add a new -1, we can simple move the start forward one step and get ride of this -1 and add another -1 behind. The dp value will not change. 

If nums[i + 1] <TeX>==</TeX> -1 and valid is true and dp[i] <TeX>\geq</TeX>0 and nums[start] <TeX>==</TeX> 1. It means the current subarray starts with a 1. If the dp[i] is 0, it means we will need to restart from i + 1. The start is set to current index and dp is set to be -1. If the dp[i] is larger than 0, the max value for i + 1 is simply dp[i] - 1.

### Python
```python
def largestVariance(self, s: str) -> int:
  def kadane(nums):
    n = len(nums)
    dp = nums[0]
    start = 0
    valid = nums[0] == -1
    max_dp = 0
    for i in range(1, n):
      next_dp = 0
      if nums[i] == 1:
        next_dp = dp + 1
      else:
        if not valid:
          next_dp = dp - 1
          valid = True
        else:
          if dp >= 0:
            if nums[start] == -1:
              next_dp = dp
              start += 1
            else:
              if dp == 0:
                next_dp = -1
                start = i
              else:
                next_dp = dp - 1
          else:
            start = i
            next_dp = -1
      dp = next_dp
      if valid:
        max_dp = max(dp, max_dp)
    return max_dp
  n = len(s)
  letters = set(s)
  if len(letters) == 1:
    return 0
  ans = -float('inf')
  for a in letters:
    for b in letters:
      if a == b:
        continue
      nums = list(map(lambda ch: 1 if ch == a else -1, filter(lambda ch: ch == a or ch == b, s)))
      res = kadane(nums)
      ans = max(ans, res)
  return ans
  
```
