---
title: 85. maximal rectangle
date: '2021-07-25'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0085 maximal rectangle
---



Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)
>   Input: matrix <TeX>=</TeX> [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
>   Output: 6
>   Explanation: The maximal rectangle is shown in the above picture.
>   Example 2:
>   Input: matrix <TeX>=</TeX> []
>   Output: 0
>   Example 3:
>   Input: matrix <TeX>=</TeX> [["0"]]
>   Output: 0
>   Example 4:
>   Input: matrix <TeX>=</TeX> [["1"]]
>   Output: 1
>   Example 5:
>   Input: matrix <TeX>=</TeX> [["0","0"]]
>   Output: 0
**Constraints:**
>   	rows <TeX>=</TeX><TeX>=</TeX> matrix.length
>   	cols <TeX>=</TeX><TeX>=</TeX> matrix[i].length
>   	0 <TeX>\leq</TeX> row, cols <TeX>\leq</TeX> 200
>   	matrix[i][j] is '0' or '1'.


## Solution
We can convert this problem to the max rectangle in histogram. We check each row from the top to the bottom and calculate the heights of number 1. After we get the heights, we calculate the max histogram area. The max of the max histogram will be the answer.



### Python
```python
def maximalRectangle(self, matrix: List[List[str]]) -> int:
def largestRectangleArea(heights):
def calculateBoundary(isLeftToRight, isIncreasingStack):
n = len(heights)
initVal = -1 if isLeftToRight else n
result = [initVal] * n
stack = []
IndexRange = range(n) if isLeftToRight else reversed(range(n))
if isIncreasingStack:
cmp = lambda top, val: top > val if isLeftToRight else top >= val
else:
cmp = lambda top, val: top < val if isLeftToRight else top <= val
for i in IndexRange:
while len(stack) > 0 and cmp(heights[stack[-1]], heights[i]):
stack.pop()
result[i] = initVal if len(stack) == 0 else stack[-1]
stack.append(i)
return result

left = calculateBoundary(True, True)
right = calculateBoundary(False, True)
n = len(heights)
ans = 0
for i in range(n):
height = heights[i]
width = right[i] - left[i] - 1
ans = max(ans, height * width)
return ans

m = len(matrix)
n = len(matrix[0])
heights = [0] * n
ans = 0
for i in range(m):
for j in range(n):
if matrix[i][j] == "1":
heights[j] += 1
else:
heights[j] = 0
ans = max(ans, largestRectangleArea(heights))
return ans
```


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn largest_rectangle_area(heights: &Vec<i32>, leftest_less_indices: &Vec<i32>, rightest_less_indices: &Vec<i32>) -> i32 {
let n = heights.len();
let mut largest_area = i32::MIN;
for i in 0..n {
let area = heights[i] * (rightest_less_indices[i] - leftest_less_indices[i] - 1);
largest_area = i32::max(largest_area, area);
}
largest_area
}

pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
if matrix.len() == 0 {
return 0;
}
let m = matrix.len();
let n = matrix[0].len();
let mut heights: Vec<i32> = vec![];
let mut leftest_less_indices: Vec<i32> = vec![-1; n];
let mut rightest_less_indices: Vec<i32> = vec![-1; n];
let mut result = i32::MIN;
for i in 0..m {
if i == 0 {
heights = matrix[0].iter().map(|&ch| if ch == '1' {1} else {0}).collect::<Vec<i32>>();
leftest_less_indices[0] = -1;
for i in 1..n {
if heights[i] <= heights[i - 1] {
let mut index = leftest_less_indices[i - 1];
while index >= 0 && heights[index as usize] >= heights[i] {
index = leftest_less_indices[index as usize];
}
leftest_less_indices[i] = index as i32;
} else {
leftest_less_indices[i] = i as i32 - 1;
}
}
rightest_less_indices[n - 1] = n as i32;
for i in (0..n-1).rev() {
if heights[i] <= heights[i + 1] {
let mut index = rightest_less_indices[i + 1];
while index < n as i32 && heights[index as usize] >= heights[i] {
index = rightest_less_indices[index as usize];
}
rightest_less_indices[i] = index as i32;
} else {
rightest_less_indices[i] = i as i32 + 1;
}
}
} else {
let mut zero_index = usize::MAX;
for j in 0..n {
if matrix[i][j] == '1' {
if zero_index == usize::MAX {
leftest_less_indices[j] = leftest_less_indices[j];
} else {
leftest_less_indices[j] = i32::max(zero_index as i32, leftest_less_indices[j]);
}
} else {
leftest_less_indices[j] = -1;
zero_index = j;
}
}
let mut zero_index = usize::MAX;
for j in (0..n).rev() {
if matrix[i][j] == '1' {
if zero_index == usize::MAX {
rightest_less_indices[j] = rightest_less_indices[j];
} else {
rightest_less_indices[j] = i32::min(zero_index as i32, rightest_less_indices[j]);
}
} else {
rightest_less_indices[j] = n as i32;
zero_index = j;
}
}
for j in 0..n {
if matrix[i][j] == '1' {
heights[j] = heights[j] + 1;
} else {
heights[j] = 0;
}
}
}
println!("heights: {:?}", heights);
println!("leftest_less_indices: {:?}", leftest_less_indices);
println!("rightest_less_indices: {:?}", rightest_less_indices);

let max_area = Solution::largest_rectangle_area(&heights, &leftest_less_indices, &rightest_less_indices);
println!("max_area: {}", max_area);
result = i32::max(max_area, result);
}
result
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_85() {
/*
assert_eq!(Solution::maximal_rectangle(vec![
vec!['1','0','1','0','0'],
vec!['1','0','1','1','1'],
vec!['1','1','1','1','1'],
vec!['1','0','0','1','0']]), 6);
let empty: Vec<Vec<char>> = vec![];
assert_eq!(Solution::maximal_rectangle(empty), 0);
assert_eq!(Solution::maximal_rectangle(vec![vec!['0']]), 0);
assert_eq!(Solution::maximal_rectangle(vec![vec!['1']]), 1);
assert_eq!(Solution::maximal_rectangle(vec![vec!['0', '0']]), 0);
*/
assert_eq!(Solution::maximal_rectangle(vec![vec!['0', '1'], vec!['1', '0']]), 1);
}
}

```
