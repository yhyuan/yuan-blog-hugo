---
title: 499. the maze iii
date: '2022-03-19'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0499 the maze iii
---


There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.



Given the m x n maze, the ball's position ball and the hole's position hole, where ball <TeX>=</TeX> [ballrow, ballcol] and hole <TeX>=</TeX> [holerow, holecol], return a string instructions of all the instructions that the ball should follow to drop in the hole with the shortest distance possible. If there are multiple valid instructions, return the lexicographically minimum one. If the ball can't drop in the hole, return "impossible".



If there is a way for the ball to drop in the hole, the answer instructions should contain the characters 'u' (i.e., up), 'd' (i.e., down), 'l' (i.e., left), and 'r' (i.e., right).



The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).



You may assume that the borders of the maze are all walls (see examples).







> Example 1:
> Input: maze <TeX>=</TeX> [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball <TeX>=</TeX> [4,3], hole <TeX>=</TeX> [0,1]
> Output: "lul"
> Explanation: There are two shortest ways for the ball to drop into the hole.
> The first way is left -> up -> left, represented by "lul".
> The second way is up -> left, represented by 'ul'.
> Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".
> Example 2:
> Input: maze <TeX>=</TeX> [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball <TeX>=</TeX> [4,3], hole <TeX>=</TeX> [3,0]
> Output: "impossible"
> Explanation: The ball cannot reach the hole.
> Example 3:
> Input: maze <TeX>=</TeX> [[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]], ball <TeX>=</TeX> [0,4], hole <TeX>=</TeX> [3,5]
> Output: "dldr"
**Constraints:**
> m <TeX>=</TeX><TeX>=</TeX> maze.length
> n <TeX>=</TeX><TeX>=</TeX> maze[i].length
> 1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 100
> maze[i][j] is 0 or 1.
> ball.length <TeX>=</TeX><TeX>=</TeX> 2
> hole.length <TeX>=</TeX><TeX>=</TeX> 2
> 0 <TeX>\leq</TeX> ballrow, holerow <TeX>\leq</TeX> m
> 0 <TeX>\leq</TeX> ballcol, holecol <TeX>\leq</TeX> n
> Both the ball and the hole exist in an empty space, and they will not be in the same position initially.
> The maze contains at least 2 empty spaces.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
fn find_shortest_way(maze: Vec<Vec<i32>>, ball: Vec<i32>, hole: Vec<i32>) -> String {
let start_r = ball[0] as usize;
let start_c = ball[1] as usize;
let end_r = hole[0] as usize;
let end_c = hole[1] as usize;
let n = maze.len();
let m = maze[0].len();
let mut states = vec![vec![(std::usize::MAX, "".to_string()); m]; n];
let mut queue: BinaryHeap<(Reverse<usize>, Reverse<String>, usize, usize)> =
BinaryHeap::new();
queue.push((Reverse(0), Reverse("".to_string()), start_r, start_c));
while let Some((Reverse(dist), Reverse(path), r, c)) = queue.pop() {
if r == end_r && c == end_c {
return path;
}
let mut i = r;
let j = c;
let mut d = 0;
let mut p = path.to_string();
p.push('u');
while i > 0 && maze[i - 1][j] == 0 {
i -= 1;
d += 1;
if i == end_r && j == end_c {
break;
}
}
if d > 0 && (d, p.to_string()) < states[i][j] {
states[i][j] = (d, p.to_string());
queue.push((Reverse(dist + d), Reverse(p), i, j));
}

let i = r;
let mut j = c;
let mut d = 0;
let mut p = path.to_string();
p.push('l');
while j > 0 && maze[i][j - 1] == 0 {
j -= 1;
d += 1;
if i == end_r && j == end_c {
break;
}
}
if d > 0 && (d, p.to_string()) < states[i][j] {
states[i][j] = (d, p.to_string());
queue.push((Reverse(dist + d), Reverse(p), i, j));
}

let mut i = r;
let j = c;
let mut d = 0;
let mut p = path.to_string();
p.push('d');
while i + 1 < n && maze[i + 1][j] == 0 {
i += 1;
d += 1;
if i == end_r && j == end_c {
break;
}
}
if d > 0 && (d, p.to_string()) < states[i][j] {
states[i][j] = (d, p.to_string());
queue.push((Reverse(dist + d), Reverse(p), i, j));
}

let i = r;
let mut j = c;
let mut d = 0;
let mut p = path.to_string();
p.push('r');
while j + 1 < m && maze[i][j + 1] == 0 {
j += 1;
d += 1;
if i == end_r && j == end_c {
break;
}
}
if d > 0 && (d, p.to_string()) < states[i][j] {
states[i][j] = (d, p.to_string());
queue.push((Reverse(dist + d), Reverse(p), i, j));
}
}
"impossible".to_string()
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_499() {
/*
assert_eq!(Solution::find_shortest_way(vec![
vec![0,0,0,0,0],
vec![1,1,0,0,1],
vec![0,0,0,0,0],
vec![0,1,0,0,1],
vec![0,1,0,0,0]], vec![4,3], vec![0, 1]), "lul".to_string());
assert_eq!(Solution::find_shortest_way(vec![
vec![0,0,0,0,0],
vec![1,1,0,0,1],
vec![0,0,0,0,0],
vec![0,1,0,0,1],
vec![0,1,0,0,0]], vec![4,3], vec![3,0]), "impossible".to_string());
assert_eq!(Solution::find_shortest_way(vec![
vec![0,0,0,0,0,0,0],
vec![0,0,1,0,0,1,0],
vec![0,0,0,0,1,0,0],
vec![0,0,0,0,0,0,1]], vec![0,4], vec![3,5]), "dldr".to_string());
*/
assert_eq!(Solution::find_shortest_way(vec![vec![0,1,0,0,1,0,0,1,0,0],vec![0,0,1,0,0,1,0,0,1,0],vec![0,0,0,0,0,0,1,0,0,1],vec![0,0,0,0,0,0,1,0,0,1],vec![0,1,0,0,1,0,0,1,0,0],vec![0,0,1,0,0,1,0,0,0,0],vec![0,0,0,0,0,0,1,0,0,0],vec![1,0,0,1,0,0,0,0,0,1],vec![0,1,0,0,1,0,0,1,0,0],vec![0,0,0,0,0,1,0,0,1,0]],
vec![2,4], vec![7,6]), "drdrdrdldl".to_string());
}
}

```
