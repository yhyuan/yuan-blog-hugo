---
title: 1567. maximum length of subarray with positive product
date: '2022-08-14'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1567 maximum length of subarray with positive product
---



Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.



>   Example 1:
>   Input: nums <TeX>=</TeX> [1,-2,-3,4]
>   Output: 4
>   Explanation: The array nums already has a positive product of 24.
>   Example 2:
>   Input: nums <TeX>=</TeX> [0,1,-2,-3,-4]
>   Output: 3
>   Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
>   Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
>   Example 3:
>   Input: nums <TeX>=</TeX> [-1,-2,-3,0,1]
>   Output: 2
>   Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
>   Example 4:
>   Input: nums <TeX>=</TeX> [-1,2]
>   Output: 1
>   Example 5:
>   Input: nums <TeX>=</TeX> [1,2,3,5,-6,4,0,10]
>   Output: 4
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5
>   	-10^9 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9


## Solution
We will use dynamic programming to solve this problem. Let's use dp[i] =(pos, neg) to represent the max subarray length with positive and negative results for the subarray ends at i. If we move to i + 1, there are three cases.

nums[i + 1] is 0. the dp[i + 1] will become (0, 0)

nums[i + 1] > 0. the next pos value is simple, we can simple add 1. The next neg will be different. If the previous neg is 0, it means it is not possible to find a subarray ends at i with negative result. If we add more positive number, it will not be changed. It is still 0. If the previous neg is not 0, we can simply add 1.

nums[i + 1] < 0. The next neg value is simple. We can simply add 1 to the previous pos. The next pos value is similar to case 2. We need to determinate whether the previous neg value is 0 or not. If it is 0, the next pos value is still 0. Otherwise, it is the previous neg plus 1.



### Python
```python
def getMaxLen(self, nums: List[int]) -> int:
dp = (0, 0)
ans = 0
for i in range(len(nums)):
if nums[i] == 0:
dp = (0, 0)
elif nums[i] > 0:
dp=(dp[0]+1, 0 if dp[1]==0 else dp[1] + 1)
else:
dp =(0 if dp[1]==0 else dp[1] + 1, dp[0]+1)
ans = max(ans, dp[0])
return ans
```



### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn get_max_len(nums: Vec<i32>) -> i32 {
// dp_pos[n] = if nums[i] > 0 {dp_pos[n - 1] + 1}
let n = nums.len();
let mut dp_pos: Vec<i32> = vec![0; n];
let mut dp_neg: Vec<i32> = vec![0; n];
dp_pos[0] = if nums[0] > 0 {1} else if nums[0] < 0 {0} else {0};
dp_neg[0] = if nums[0] > 0 {0} else if nums[0] < 0 {1} else {0};
for i in 1..n {
if nums[i] > 0 {
dp_pos[i] = if dp_pos[i - 1] == 0 {1} else {dp_pos[i - 1] + 1};
dp_neg[i] = if dp_neg[i - 1] == 0 {0} else {dp_neg[i - 1] + 1};
} else if nums[i] < 0 {
dp_pos[i] = if dp_neg[i - 1] == 0 {0} else {dp_neg[i - 1] + 1};
dp_neg[i] = if dp_pos[i - 1] == 0 {1} else {dp_pos[i - 1] + 1};
} else {
dp_pos[i] = 0;
dp_neg[i] = 0;
}
}
*dp_pos.iter().max().unwrap()
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1567() {
assert_eq!(Solution::get_max_len(vec![1,-2,-3,4]), 4);
assert_eq!(Solution::get_max_len(vec![0,1,-2,-3,-4]), 3);
assert_eq!(Solution::get_max_len(vec![-1,-2,-3,0,1]), 2);
}
}

```
