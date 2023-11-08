---
title: 59. spiral matrix ii
date: '2021-06-29'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0059 spiral matrix ii
---



Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg)
>   Input: n <TeX>=</TeX> 3
>   Output: [[1,2,3],[8,9,4],[7,6,5]]
>   Example 2:
>   Input: n <TeX>=</TeX> 1
>   Output: [[1]]
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 20


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*


#[derive(Debug)]
enum Direction {
East,
South,
West,
North,
}
impl Solution {
pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
let n = n as usize;
let mut result: Vec<Vec<i32>> = vec![vec![0; n]; n];
let (mut i, mut j) = (0, 0);
let mut direction = Direction::East;
for k in 1..=n*n {
result[i][j] = k as i32;
direction = match direction {
Direction::East => {
if j + 1 <= n - 1 && result[i][j + 1] == 0 { // go east again
j = j + 1;
Direction::East
} else if i + 1 <= n - 1 && result[i + 1][j] == 0 { // go south
i = i + 1;
Direction::South
} else {
return result;
}
},
Direction::South => {
if i + 1 <= n - 1 && result[i + 1][j] == 0 { // go south again
i = i + 1;
Direction::South
} else if j >= 1 && result[i][j - 1] == 0 {
j = j - 1;
Direction::West
} else {
return  result;
}
},
Direction::West => {
if j >= 1 && result[i][j - 1] == 0 { // go west again
j = j - 1;
Direction::West
} else if i >= 1 && result[i - 1][j] == 0 { // go north
i = i - 1;
Direction::North
} else {
return result;
}
},
Direction::North => {
if i >= 1 && result[i - 1][j] == 0 { // go north again
i = i - 1;
Direction::North
} else if j + 1 <= n - 1 && result[i][j + 1] == 0 {
j = j + 1;
Direction::East
} else {
return  result;
}
},
}
}
result
}
}
*/
impl Solution {
pub fn helper(res: &mut Vec<Vec<i32>>, n: usize, k: usize, start: i32) {
if n <= 2 * k {
return;
}
if n == 2 * k + 1 {
res[n / 2][n / 2] = start;
return;
}
let mut val = start;
for j in k..=n - 1 - k {
res[k][j] = val;
val += 1;
}
//println!("k + 1: {}, n - 1 - k - 1: {} ", k + 1, n - 1 - k - 1);
if n - 1 - k - 1 >= k + 1 {
for i in k + 1..=n - 1 - k - 1 {
res[i][n - 1 - k] = val;
val += 1;
}
}
for j in (k..=n - 1 - k).rev() {
res[n - k - 1][j] = val;
val += 1;
}
if n - 1 - k - 1 >= k + 1 {
for i in (k + 1..=n - 1 - k - 1).rev() {
res[i][k] = val;
val += 1;
}
}
//println!("val: {}", val);
Self::helper(res, n, k + 1, val);
}
pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
let n = n as usize;
let mut res: Vec<Vec<i32>> = vec![vec![0; n]; n];
Self::helper(&mut res, n, 0usize, 1i32);
res
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_59() {
assert_eq!(Solution::generate_matrix(1), vec![vec![1]]);
assert_eq!(Solution::generate_matrix(2), vec![vec![1, 2], vec![4, 3]]);
assert_eq!(
Solution::generate_matrix(3),
vec![vec![1, 2, 3], vec![8, 9, 4], vec![7, 6, 5],]
);
}
}

```
