---
title: 312. burst balloons
date: '2022-01-04'
tags: ['leetcode', 'rust', 'python', 'hard']
draft: false
description: Solution for leetcode 0312 burst balloons
---



You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the i^th balloon, you will get nums[i - 1]  nums[i]  nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



>   Example 1:
>   Input: nums <TeX>=</TeX> [3,1,5,8]
>   Output: 167
>   Explanation:
>   nums <TeX>=</TeX> [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
>   coins <TeX>=</TeX>  315    +   358   +  138  + 181 <TeX>=</TeX> 167
>   Example 2:
>   Input: nums <TeX>=</TeX> [1,5]
>   Output: 10
**Constraints:**
>   	n <TeX>=</TeX><TeX>=</TeX> nums.length
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 500
>   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 100


## Solution
Firstly, let's add 1 in the begining and ending.

Let's define dp[i][j] as the result between [i, j]. So dp[1][n - 2] will be our results.

i = j. The subarray length is only one. So the result will be nums[i-1] * nums[i] * nums[i + 1].

i < j. We pick every element between i and j as the middle element k. It will be the last element to be eliminated. The coins we earn will include three parts.

Before k: It is dp[i][k - 1]

After k: dp[k+1][j]

Eliminate k: nums[k] * nums[i - 1] * nums[j + 1]

So dp[i][j] = max(dp[i][k - 1] + dp[k + 1][j] + nums[k] * nums[i - 1] * nums[j + 1])


### Python
Top down appraoch
```python
class Solution:
def maxCoins(self, nums: List[int]) -> int:
nums = [1] + nums + [1]
n = len(nums)
memo = {}
def helper(i, j):
n = len(nums)
if (i, j) in memo:
return memo[(i, j)]
if i > j:
return 0
if i == j:
memo[(i, j)] = nums[i - 1] * nums[i] * nums[i + 1]
return memo[(i, j)]
ans = 0
for k in range(i, j + 1):
res = helper(i, k - 1) + helper(k + 1, j) + nums[k] * nums[i - 1] * nums[j + 1]
ans = max(ans, res)
memo[(i, j)] = ans
return ans
ans = helper(1, n - 2)
return ans

```

Bottom up approach
```python
class Solution:
def maxCoins(self, nums: List[int]) -> int:
nums = [1] + nums + [1]
n = len(nums)
dp = [[0 for j in range(n)] for i in range(n)]
for i in range(1, n - 1):
dp[i][i] = nums[i - 1] * nums[i] * nums[i + 1]
for size in range(2, n - 1):
for i in range(1, n - 1 - size + 1):
j = i + size - 1
dp[i][j] = 0
for k in range(i, j + 1):
dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])
return dp[1][n - 2]

```


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn helper(nums: &Vec<i32>, start: usize, end: usize, memo: &mut Vec<Vec<i32>>) -> i32 {
if memo[start][end] != 0 {
return memo[start][end];
}
if start == end {
memo[start][end] = nums[start - 1] * nums[start] * nums[start + 1];
return memo[start][end];
}

let mut max = 0;
for i in start..=end {
let left_max = if i > start {Solution::helper(nums, start, i - 1, memo)} else {0};
let right_max = if i < end {Solution::helper(nums, i + 1, end, memo)} else {0};
let result = left_max + nums[start - 1] * nums[i] * nums[end + 1] + right_max; // Last removed
max = i32::max(max, result);
}
memo[start][end] = max;
max
}
pub fn max_coins(nums: Vec<i32>) -> i32 {
let size = nums.len();
if size == 0 {
return 0;
}
if size == 1 {
return nums[0];
}
let mut nums: Vec<i32> = (0..nums.len()).into_iter()
.filter(|&i| nums[i] != 0)
.map(|i| nums[i]).collect();
let len = nums.len();
nums.insert(0, 1);
nums.push(1);
//let len = nums.len() + 2;
let mut memo = vec![vec![0; len + 1]; len + 1];
//println!("{:?}", nums);
Solution::helper(&nums, 1, len, &mut memo)
//0
/*
let mut max_result = i32::MIN;
for i in 0..nums.len() {
let left = if i == 0 {1} else {nums[i - 1]};
let right = if i == (size - 1) {1} else {nums[i + 1]};
let product = left * nums[i]  * right;
let indices: Vec<usize> = (0..nums.len()).into_iter().filter(|&index| index != i).collect();
let new_nums: Vec<i32> = indices.iter().map(|&index| nums[index]).collect();
max_result = i32::max(product + Solution::max_coins(new_nums), max_result);
}
max_result
*/
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_312() {
assert_eq!(Solution::max_coins(vec![3, 1, 5, 8]), 167);
}
}

```
