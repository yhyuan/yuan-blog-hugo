---
title: 218. the skyline problem
date: '2021-11-04'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0218 the skyline problem
---



A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] <TeX>=</TeX> [lefti, righti, heighti]:



lefti is the x coordinate of the left edge of the i^th building.

righti is the x coordinate of the right edge of the i^th building.

heighti is the height of the i^th building.



You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/12/01/merged.jpg)
>   Input: buildings <TeX>=</TeX> [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
>   Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
>   Explanation:
>   Figure A shows the buildings of the input.
>   Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
>   Example 2:
>   Input: buildings <TeX>=</TeX> [[0,2,3],[2,5,3]]
>   Output: [[0,3],[5,0]]
**Constraints:**
>   	1 <TeX>\leq</TeX> buildings.length <TeX>\leq</TeX> 10^4
>   	0 <TeX>\leq</TeX> lefti < righti <TeX>\leq</TeX> 2^31 - 1
>   	1 <TeX>\leq</TeX> heighti <TeX>\leq</TeX> 2^31 - 1
>   	buildings is sorted by lefti in non-decreasing order.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::cmp::Ordering::*;
use std::collections::VecDeque;

impl Solution {
pub fn get_skyline(buildings: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
if buildings.is_empty() {
return vec![];
}
let mut queue: VecDeque<Vec<Vec<i32>>> = buildings.into_iter()
.map(|x| vec![vec![x[0], x[2]], vec![x[1], 0]])
.collect();
while queue.len() > 1 {
let a = queue.pop_front().unwrap();
let b = queue.pop_front().unwrap();
let c = Self::merge(a, b);
queue.push_back(c);
}
queue.pop_front().unwrap()
}
fn merge(a: Vec<Vec<i32>>, b: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
let mut i = 0;
let mut j = 0;
let mut res = vec![];
let mut prev_h = 0;
let mut l = 0;
let mut r = 0;
let mut x;
while i < a.len() && j < b.len() {
match a[i][0].cmp(&b[j][0]) {
Equal => {
x = a[i][0];
l = a[i][1];
r = b[j][1];
i += 1;
j += 1;
}
Less => {
x = a[i][0];
l = a[i][1];
i += 1;
}
Greater => {
x = b[j][0];
r = b[j][1];
j += 1;
}
}
let h = l.max(r);
if h != prev_h {
res.push(vec![x, h]);
prev_h = h;
}
}
while i < a.len() {
let x = a[i][0];
let h = a[i][1];
i += 1;
if h != prev_h {
res.push(vec![x, h]);
prev_h = h;
}
}
while j < b.len() {
let x = b[j][0];
let h = b[j][1];
j += 1;
if h != prev_h {
res.push(vec![x, h]);
prev_h = h;
}
}
res
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_218() {
assert_eq!(
Solution::get_skyline(vec![
vec![2,9,10],
vec![3,7,15],
vec![5,12,12],
vec![15,20,10],
vec![19,24,8]]),
vec![
vec![2,10],
vec![3,15],
vec![7,12],
vec![12,0],
vec![15,10],
vec![20,8],
vec![24,0]]
);
}
}

```
