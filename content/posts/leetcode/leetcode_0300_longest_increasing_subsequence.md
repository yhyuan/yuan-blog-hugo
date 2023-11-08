---
title: 300. longest increasing subsequence
date: '2021-12-26'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0300 longest increasing subsequence
---



Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



>   Example 1:
>   Input: nums <TeX>=</TeX> [10,9,2,5,3,7,101,18]
>   Output: 4
>   Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
>   Example 2:
>   Input: nums <TeX>=</TeX> [0,1,0,3,2,3]
>   Output: 4
>   Example 3:
>   Input: nums <TeX>=</TeX> [7,7,7,7,7,7,7]
>   Output: 1
**Constraints:**
>   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 2500
>   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4
>   Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
/*
pub fn length_of_lis(nums: Vec<i32>) -> i32 {
let n = nums.len();
if n == 0 {
return 0;
}
let mut dp: Vec<i32> = vec![1; n];
for i in 0..n {
//max(dp[0] + 1, dp[1] + 1, dp[2] + 1, ...... dp[i-1] + 1, 1)
for j in 0..i {
if nums[j] < nums[i] {
dp[i] = i32::max(dp[i], dp[j] + 1);
}
}
}
let result = dp.iter().max().unwrap();
*result
}
*/
//dp[i] 表示长度为 i + 1 的所有上升子序列的末尾的最小值。
//nums = [4,5,6,3]
//len = 1   :      [4], [5], [6], [3]   => dp[0] = 3
//长度为 1 的上升子序列有 4 个，末尾最小的值就是 3
//len = 2   :      [4, 5], [5, 6]       => dp[1] = 5
//长度为 2 的上升子序列有 2 个，末尾最小的值就是 5
//len = 3   :      [4, 5, 6]            => dp[2] = 6
//长度为 3 的上升子序列有 1 个，末尾最小的值就是 6
/**
nums = [10,9,2,5,3,7,101,18]
开始没有数字
dp = []
1----------------------------
10  9  2  5  3  7  101  18
^
先考虑 10, 只有 1 个数字, 此时长度为 1 的最长上升子序列末尾的值就是 10
len   1
dp = [10]
2----------------------------
10  9  2  5  3  7  101  18
^
考虑 9, 9 比之前长度为 1 的最长上升子序列末尾的最小值 10 小, 更新长度为 1 的最长上升子序列末尾的值为 9
len   1
dp = [9]
3----------------------------
10  9  2  5  3  7  101  18
^
考虑 2, 2 比之前长度为 1 的最长上升子序列末尾的最小值 9 小, 更新长度为 1 的最长上升子序列末尾的值为 2
len   1
dp = [2]
4----------------------------
10  9  2  5  3  7  101  18
^
考虑 5,
5 比之前长度为 1 的最长上升子序列末尾的最小值 2 大,
此时可以扩展长度, 更新长度为 2 的最长上升子序列末尾的值为 5
len   1  2
dp = [2  5]
5----------------------------
10  9  2  5  3  7  101  18
^
考虑 3,
3 比之前长度为 1 的最长上升子序列末尾的最小值 2 大, 向后考虑
3 比之前长度为 2 的最长上升子序列末尾的最小值 5 小, 更新长度为 2 的最长上升子序列末尾的值为 3
len   1  2
dp = [2  3]
6----------------------------
10  9  2  5  3  7  101  18
^
考虑 7,
7 比之前长度为 1 的最长上升子序列末尾的最小值 2 大, 向后考虑
7 比之前长度为 2 的最长上升子序列末尾的最小值 3 大, 向后考虑
此时可以扩展长度, 更新长度为 3 的最长上升子序列末尾的值为 7
len   1  2  3
dp = [2  3  7]
7----------------------------
10  9  2  5  3  7  101  18
^
考虑 101,
101 比之前长度为 1 的最长上升子序列末尾的最小值 2 大, 向后考虑
101 比之前长度为 2 的最长上升子序列末尾的最小值 3 大, 向后考虑
101 比之前长度为 3 的最长上升子序列末尾的最小值 7 大, 向后考虑
此时可以扩展长度, 更新长度为 4 的最长上升子序列末尾的值为 101
len   1  2  3   4
dp = [2  3  7  101]
8----------------------------
10  9  2  5  3  7  101  18
^
考虑 18,
18 比之前长度为 1 的最长上升子序列末尾的最小值 2 大, 向后考虑
18 比之前长度为 2 的最长上升子序列末尾的最小值 3 大, 向后考虑
18 比之前长度为 3 的最长上升子序列末尾的最小值 7 大, 向后考虑
3 比之前长度为 4 的最长上升子序列末尾的最小值 101 小, 更新长度为 4 的最长上升子序列末尾的值为 18
len   1  2  3   4
dp = [2  3  7   18]
遍历完成，所以数字都考虑了，此时 dp 的长度就是最长上升子序列的长度
*/
/*
In the previous approach, when we have an element num that is not greater than all the elements in sub, we perform a linear scan to find the first element in sub that is greater than or equal to num. Since sub is in sorted order, we can use binary search instead to greatly improve the efficiency of our algorithm.

Algorithm

Initialize an array sub which contains the first element of nums.

Iterate through the input, starting from the second element. For each element num:

If num is greater than any element in sub, then add num to sub.
Otherwise, perform a binary search in sub to find the smallest element that is greater than or equal to num. Replace that element with num.
Return the length of sub.

pub fn length_of_lis(nums: Vec<i32>) -> i32 {
let mut dp: Vec<i32> = vec![];
for &num in nums.iter() {
let n = dp.len();
let k = dp.binary_search(&num);
if let Err(j) = k {
// num is greater than any numbers inside dp
if j == dp.len() {
dp.push(num);
} else {
// Replace the value at position j with a smaller value num.
dp[j] = num;
}
}
}
dp.len() as i32
}
*/
pub fn length_of_lis(nums: Vec<i32>) -> i32 {
// dp[i]: the length of the longest increasing sequence ends with nums[i]
// dp[i] = 1 + max(dp[j]) if nums[j] < nums[i]
// dp[i] = 1
let n = nums.len();
let mut dp: Vec<i32> = vec![0; n];
let mut ans = 0;
for i in 0..n {
let mut res = 0;
for j in 0..i {
if nums[i] > nums[j] {
res = i32::max(res, dp[j]);
}
}
dp[i] = res + 1;
ans = i32::max(ans, dp[i]);
}
ans
//dp[n - 1]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_300() {
assert_eq!(Solution::length_of_lis(vec![4, 10, 4, 3, 8, 9]), 3);
assert_eq!(Solution::length_of_lis(vec![10, 9, 2, 5, 3, 7, 101, 18]), 4);
assert_eq!(Solution::length_of_lis(vec![0, 1, 0, 3, 2, 3]), 4);
assert_eq!(Solution::length_of_lis(vec![7, 7, 7, 7, 7, 7, 7]), 1);
}
}

```
