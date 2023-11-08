---
title: 777. swap adjacent in lr string
date: '2022-05-13'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0777 swap adjacent in lr string
---



In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.



>   Example 1:
>   Input: start <TeX>=</TeX> "RXXLRXRXL", end <TeX>=</TeX> "XRLXXRRLX"
>   Output: true
>   Explanation: We can transform start to end following these steps:
>   RXXLRXRXL ->
>   XRXLRXRXL ->
>   XRLXRXRXL ->
>   XRLXXRRXL ->
>   XRLXXRRLX
>   Example 2:
>   Input: start <TeX>=</TeX> "X", end <TeX>=</TeX> "L"
>   Output: false
>   Example 3:
>   Input: start <TeX>=</TeX> "LLR", end <TeX>=</TeX> "RRL"
>   Output: false
>   Example 4:
>   Input: start <TeX>=</TeX> "XL", end <TeX>=</TeX> "LX"
>   Output: true
>   Example 5:
>   Input: start <TeX>=</TeX> "XLLR", end <TeX>=</TeX> "LXLX"
>   Output: false
**Constraints:**
>   	1 <TeX>\leq</TeX> start.length <TeX>\leq</TeX> 10^4
>   	start.length <TeX>=</TeX><TeX>=</TeX> end.length
>   	Both start and end will only consist of characters in 'L', 'R', and 'X'.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
/*
pub fn can_transform_helper(chars: &mut Vec<char>, memo: &mut HashMap<String, bool>) -> bool {
let start = chars.iter().collect::<String>();
// println!("start: {}", start);
if memo.contains_key(&start) {
return memo[&start];
}
let mut indices: Vec<usize> = vec![];
for i in 1..chars.len() {
if (chars[i - 1] == 'X' && chars[i] == 'L') || (chars[i - 1] == 'R' && chars[i] == 'X') {
indices.push(i - 1);
}
}
// println!("indices: {:?}", indices);
let mut res = false;
for k in 0..indices.len() {
let i = indices[k];
if chars[i] == 'X' && chars[i + 1] == 'L' {
chars[i] = 'L';
chars[i + 1] = 'X';
if Self::can_transform_helper(chars, memo) {
res = true;
break;
}
chars[i] = 'X';
chars[i + 1] = 'L';
} else {
chars[i] = 'X';
chars[i + 1] = 'R';
if Self::can_transform_helper(chars, memo) {
res = true;
break;
}
chars[i] = 'R';
chars[i + 1] = 'X';
}
}
memo.insert(start, res);
res
}

pub fn can_transform(start: String, end: String) -> bool {
let mut memo: HashMap<String, bool> = HashMap::new();
memo.insert(end.clone(), true);
let mut chars: Vec<char> = start.chars().collect();
Self::can_transform_helper(&mut chars, &mut memo)
}
*/
/*
Explanation
Key observations:

There are three kinds of characters, ‘L’, ‘R’, ‘X’.

Replacing XL with LX = move L to the left by one

Replacing RX with XR = move R to the right by one

If we remove all the X in both strings, the resulting strings should be the same.

Additional observations:

Since a move always involves X, an L or R cannot move through another L or R.

Since anL can only move to the right, for each occurrence of L in the start string, its position should be to the same or to the left of its corresponding L in the end string.


And vice versa for the R characters.

Implementation

We first compare two strings with X removed. This checks relative position between Ls and Rs are correct.

Then we find the indices for each occurence of L and check the condition in the above figure. Then we do the same for R.
*/
pub fn remove_x(s: &String) -> String {
let mut chars: Vec<char> = vec![];
for ch in s.chars() {
if ch != 'X' {
chars.push(ch);
}
}
let result: String = chars.iter().collect();
result
}
pub fn can_transform(start: String, end: String) -> bool {
if start.len() != end.len() {
return false;
}
let start_without_x = Self::remove_x(&start);
let end_without_x = Self::remove_x(&end);
if start_without_x != end_without_x {
return false
}
let n = start.len();
let start_chars: Vec<char> = start.chars().collect();
let end_chars: Vec<char> = end.chars().collect();

let start_l_indices: Vec<usize> = (0..n).into_iter().filter(|&i| start_chars[i] == 'L').collect();
let end_l_indices: Vec<usize> = (0..n).into_iter().filter(|&i| end_chars[i] == 'L').collect();
if start_l_indices.len() != end_l_indices.len() {
return false;
}
for i in 0..start_l_indices.len() {
if start_l_indices[i] < end_l_indices[i] {
return false;
}
}
let start_r_indices: Vec<usize> = (0..n).into_iter().filter(|&i| start_chars[i] == 'R').collect();
let end_r_indices: Vec<usize> = (0..n).into_iter().filter(|&i| end_chars[i] == 'R').collect();
if start_r_indices.len() != end_r_indices.len() {
return false;
}
for i in 0..start_r_indices.len() {
if start_r_indices[i] > end_r_indices[i] {
return false;
}
}
true
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_777() {
assert_eq!(Solution::can_transform("RXXLRXRXL".to_string(), "XRLXXRRLX".to_string()), true);
}
}

```
