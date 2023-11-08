---
title: 849. maximize distance to closest person
date: '2022-05-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0849 maximize distance to closest person
---



You are given an array representing a row of seats where seats[i] <TeX>=</TeX> 1 represents a person sitting in the i^th seat, and seats[i] <TeX>=</TeX> 0 represents that the i^th seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/09/10/distance.jpg)
>   Input: seats <TeX>=</TeX> [1,0,0,0,1,0,1]
>   Output: 2
>   Explanation:
>   If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
>   If Alex sits in any other open seat, the closest person has distance 1.
>   Thus, the maximum distance to the closest person is 2.
>   Example 2:
>   Input: seats <TeX>=</TeX> [1,0,0,0]
>   Output: 3
>   Explanation:
>   If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
>   This is the maximum distance possible, so the answer is 3.
>   Example 3:
>   Input: seats <TeX>=</TeX> [0,1]
>   Output: 1
**Constraints:**
>   	2 <TeX>\leq</TeX> seats.length <TeX>\leq</TeX> 2  10^4
>   	seats[i] is 0 or 1.
>   	At least one seat is empty.
>   	At least one seat is occupied.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn max_dist_to_closest(seats: Vec<i32>) -> i32 {
let n = seats.len();
let mut index = 0;
for i in 0..n {
if seats[i] == 1 {
index = i;
break;
}
}
let mut ans = if index == 0 {i32::MIN} else {index as i32}; // if seat on the index 0.

let mut index = n - 1;
for i in (0..n).rev() {
if seats[i] == 1 {
index = i;
break;
}
}
let res = if index == n - 1 {i32::MIN} else {n as i32 - 1 - index as i32}; // if seat on the index 0.
ans = i32::max(res, ans);

let mut index = 0;
for i in 0..n {
if seats[i] == 0 {
index = i;
break;
}
}
let mut max_len = i32::MIN;
let mut i = index;
let mut j = index;
while j < n {
while j < n && seats[j] != 1 {
j += 1;
}
max_len = i32::max(max_len, (j - i) as i32);
while j < n && seats[j] != 0 {
j += 1;
}
i = j;
}
ans = i32::max(ans, (max_len + 1) / 2);
ans
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_849() {
}
}

```
