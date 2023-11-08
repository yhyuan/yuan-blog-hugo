---
title: 739. daily temperatures
date: '2022-05-05'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0739 daily temperatures
---



Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the i^th day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] <TeX>=</TeX><TeX>=</TeX> 0 instead.



>   Example 1:
>   Input: temperatures <TeX>=</TeX> [73,74,75,71,69,72,76,73]
>   Output: [1,1,4,2,1,1,0,0]
>   Example 2:
>   Input: temperatures <TeX>=</TeX> [30,40,50,60]
>   Output: [1,1,1,0]
>   Example 3:
>   Input: temperatures <TeX>=</TeX> [30,60,90]
>   Output: [1,1,0]
**Constraints:**
>   	1 <TeX>\leq</TeX> temperatures.length <TeX>\leq</TeX> 10^5
>   	30 <TeX>\leq</TeX> temperatures[i] <TeX>\leq</TeX> 100


## Solution
If we use monotonic decreasing stack from right, we will find the following fact: For each index: i, we will find the values between [i + 1, right[i] - 1] are always smaller than temperatures[i] and the temperature[right[i]] is larger than i. So If we minus right[i] with i, we will get the result. Meanwhile, if right[i] is invalid (the length of array), we will assign 0 to the result.

Is left to right or right to left. The direction will determinate index range and initial value.

Is monotonic increasing stack or monotonic decreasing stack? If we pop out the values which are smaller than current value, we are creating monotonic decreasing stack and we are trying to find the range that the current value is maximum.




### Python
```python
class Solution:
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
def calculateBoundary(isLeftToRight):
n = len(temperatures)
IndexRange = range(n) if isLeftToRight else reversed(range(n))
initVal = -1 if isLeftToRight else n
result = [initVal] * n
stack = []
for i in IndexRange:


# Decreasing stack.
while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
stack.pop()
result[i] = initVal if len(stack) == 0 else stack[-1]
stack.append(i)
return result


# from i to right[i] - 1, temperatures[i]


#is the largest and tempearture[right[i]]


# is larger than temperature[i]
right = calculateBoundary(False)


# print(right)
n = len(temperatures)
ans = [0] * n
for i in range(n):
ans[i] = 0 if right[i] == n else right[i] - i
return ans
```


### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
let n = temperatures.len();
let mut result: Vec<i32> = vec![0; n];
let mut stack: Vec<(usize, i32)> = vec![];
for i in 0..n - 1 {
if temperatures[i + 1] > temperatures[i] {
result[i] = 1;
if stack.len() > 0 {
let (mut index, mut value) = stack[stack.len() - 1];
while stack.len() > 0 && temperatures[i] > value {
result[index] = (i - index) as i32;
stack.pop();
if stack.len() > 0 {
let top = stack[stack.len() - 1];
index = top.0;
value = top.1;
}
}
while stack.len() > 0 && temperatures[i + 1] > value {
result[index] = (i + 1 - index) as i32;
stack.pop();
if stack.len() > 0 {
let top = stack[stack.len() - 1];
index = top.0;
value = top.1;
}
}
}
} else {
stack.push((i, temperatures[i]));
}
}
result
}
}

/*
impl Solution {
pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
let n = temperatures.len();
let mut result: Vec<i32> = vec![0; n];
for i in 0..n {
for j in i + 1..n {
if temperatures[j] > temperatures[i] {
result[i] = (j - i) as i32;
break;
}
}
}
result
}
}

*/
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_739() {
assert_eq!(Solution::daily_temperatures(vec![73,74,75,71,69,72,76,73]), vec![1,1,4,2,1,1,0,0]);
assert_eq!(Solution::daily_temperatures(vec![30,40,50,60]), vec![1,1,1,0]);
assert_eq!(Solution::daily_temperatures(vec![30,60,90]), vec![1,1,0]);
}
}

```
