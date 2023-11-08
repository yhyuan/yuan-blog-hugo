---
title: 1235. Maximum Profit in Job Scheduling
date: '2022-07-21'
tags: ['leetcode', 'python', 'hard']
draft: false
description: Solution for leetcode 1235. Maximum Profit in Job Scheduling
---


We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

> Example 1:
> Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
> Output: 120
> Explanation: The subset chosen is the first and fourth job.
> Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
> Example 2:
> Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
> Output: 150
> Explanation: The subset chosen is the first, fourth and fifth job.
> Profit obtained 150 = 20 + 70 + 60.
> Example 3:
> Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
> Output: 6
**Constraints:**
> 1 <TeX>\leq</TeX> startTime.length == endTime.length == profit.length <TeX>\leq</TeX> 5 * 104
> 1 <TeX>\leq</TeX> startTime[i] < endTime[i] <TeX>\leq</TeX> 109
> 1 <TeX>\leq</TeX> profit[i] <TeX>\leq</TeX> 104


## Solution
Sort the jobs according to the starting time. Then define the dp[i] as the profit we can get from job i to the end. We have two choices. We ignore the job i. The profit we will get will be dp[i+1]. Or we take the job i. Then, we can use job i's ending time to find the next available job. If the find index is index, the profit we will get is dp[index] + job[i].proft. So the formula is dp[i] = max(dp[i + 1], dp[index] + job[i].profit)



### Python
```python
class Solution:
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
n = len(startTime)
jobs = list(map(lambda i: (startTime[i], endTime[i], profit[i]), range(n)))
jobs.sort()
memo = {}
def helper(i):
if i in memo: return memo[i]
n = len(jobs)
if i == n - 1:
memo[i] = jobs[i][2]
return memo[i]
ans = helper(i + 1) # not take i
def findNextIndex(i):
n = len(jobs)
index = -1
for j in range(i, n):
if jobs[j][0] >= jobs[i][1]:
index = j
break
return index
index = findNextIndex(i)
if index == -1:
ans = max(ans, jobs[i][2])
else:
ans = max(ans, helper(index) + jobs[i][2]) # no other jobs we can take.
memo[i] = ans
return ans
ans = helper(0)
return ans
```


### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
/*
Create a 2D array dp with length + 1 rows and target + 1 columns. The element at dp[i][j] stands for the probability
that after the first i coins are tossed, there are j coins facing heads.

Obviously, if no coin is tossed, then definitely no coin faces heads, which has a probability 1, so dp[0][0] = 1.
Each time a coin is tossed, the number of coins facing heads either remains the same or increase by 1, depending on
the current coin’s probability of facing heads. So the probability can be calculated. For the case j equals 0, dp[i][0]
only depends on prob[i - 1] and dp[i - 1][0]. For other cases, dp[i][j] depends on prob[i - 1], dp[i - 1][j - 1] and dp[i - 1][j].

Finally, return dp[length][target] for the result.
*/
//dp[i][j] := prob of j coins face up after tossing first i coins.
//dp[i][j] = dp[i-1][j] * (1 – p[i]) + dp[i-1][j-1] * p[i]
pub fn probability_of_heads(prob: Vec<f64>, target: i32) -> f64 {
let n = prob.len();
let target = target as usize;
// target p, n - target  (1-p)
let mut dp: Vec<Vec<f64>> = vec![vec![0f64; target + 1]; n + 1];
dp[0][0] = 1.0;
for i in 1..=n {
let cur_prob = prob[i - 1];
dp[i][0] = dp[i - 1][0] * (1.0f64 - cur_prob);
for j in 1..=target {
dp[i][j] = dp[i - 1][j] * (1.0f64 - cur_prob) + dp[i - 1][j - 1] * cur_prob;
}
}
// println!("{:?}", dp);
dp[n][target]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1230() {
assert_eq!(Solution::probability_of_heads(vec![1f64,1f64,1f64,1f64,1f64,1f64,1f64,1f64,1f64,1f64], 9), 0.0);
assert_eq!(Solution::probability_of_heads(vec![0.4], 1), 0.4);
assert_eq!(Solution::probability_of_heads(vec![0.5,0.5,0.5,0.5,0.5], 0), 0.03125);
}
}

```
