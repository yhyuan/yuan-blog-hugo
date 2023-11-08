---
title: 305. number of islands ii
date: '2021-12-30'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0305 number of islands ii
---


You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).



We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] <TeX>=</TeX> [ri, ci] is the position (ri, ci) at which we should operate the ith operation.



Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.



An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.







> Example 1:
> Input: m <TeX>=</TeX> 3, n <TeX>=</TeX> 3, positions <TeX>=</TeX> [[0,0],[0,1],[1,2],[2,1]]
> Output: [1,1,2,3]
> Explanation:
> Initially, the 2d grid is filled with water.
> - Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
> - Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
> - Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
> - Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
> Example 2:
> Input: m <TeX>=</TeX> 1, n <TeX>=</TeX> 1, positions <TeX>=</TeX> [[0,0]]
> Output: [1]
**Constraints:**
> 1 <TeX>\leq</TeX> m, n, positions.length <TeX>\leq</TeX> 104
> 1 <TeX>\leq</TeX> m  n <TeX>\leq</TeX> 104
> positions[i].length <TeX>=</TeX><TeX>=</TeX> 2
> 0 <TeX>\leq</TeX> ri < m
> 0 <TeX>\leq</TeX> ci < n


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
parents: Vec<usize>,
ranks: Vec<usize>,
count: usize,
}

impl DisjointSet {
pub fn new(n: usize) -> Self {
let parents = (0..n).into_iter().collect::<Vec<_>>();
let ranks = vec![1usize; n];
let count = n;
DisjointSet {
parents,
ranks,
count
}
}

pub fn find(&self, i: usize) -> usize {
let mut p = self.parents[i];
while p != self.parents[p] {
p = self.parents[p];
}
p
}

pub fn union(&mut self, i: usize, j: usize) -> bool {
let ip = self.find(i);
let jp = self.find(j);
if ip == jp {
return false;
}
if self.ranks[ip] < self.ranks[jp] {
self.parents[ip] = self.parents[jp];
} else {
self.parents[jp] = self.parents[ip];
if self.ranks[ip] == self.ranks[jp] {
self.ranks[ip] += 1;
}
}
self.count -= 1;
true
}
}
impl Solution {
pub fn num_islands2(m: i32, n: i32, positions: Vec<Vec<i32>>) -> Vec<i32> {
let m = m as usize;
let n = n as usize;
let mut disjoint_set = DisjointSet::new(m * n);
let mut matrix: Vec<Vec<bool>> = vec![vec![false; n]; m];
let mut result: Vec<i32> = vec![];
let mut duplicated = 0usize;
for k in 0..positions.len() {
let i = positions[k][0] as usize;
let j = positions[k][1] as usize;
//println!("i: {}, j: {}", i, j);
if matrix[i][j] {
let last_value = *result.last().unwrap();
result.push(last_value);
duplicated += 1;
//result.push(disjoint_set.count as i32 - (m * n - (k + 1)) as i32);
continue;
}
matrix[i][j] = true;
let neighbors = vec![(-1, 0), (1, 0), (0, -1), (0, 1)].iter()
.map(|&(dx, dy)| (i as i32 + dx, j as i32 + dy))
.filter(|&(x, y)| x >= 0 && y >= 0 && x < m as i32 && y < n as i32 && matrix[x as usize][y as usize])
.collect::<Vec<_>>();
for w in 0..neighbors.len() {
let x = neighbors[w].0 as usize;
let y = neighbors[w].1 as usize;
//println!("x: {}, y: {}, i * n + j: {}, x * n + y: {}", x, y, i * n + j, x * n + y);
disjoint_set.union(i * n + j, x * n + y);
}
// m * n - (k + 1) is zero.
// k + 1 is one.
result.push(disjoint_set.count as i32 - (m * n - (k - duplicated + 1)) as i32);
}
result
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_305() {
assert_eq!(Solution::num_islands2(3, 3, vec![vec![0,0],vec![0,1],vec![1,2],vec![1,2]]), vec![1,1,2,2]);
assert_eq!(Solution::num_islands2(3, 3, vec![vec![0,0],vec![0,1],vec![1,2],vec![2,1]]), vec![1,1,2,3]);
assert_eq!(Solution::num_islands2(3, 3, vec![vec![0,1],vec![1,2],vec![2,1],vec![1,0],vec![0,2],vec![0,0],vec![1,1]]), vec![1, 2, 3, 4, 3, 2, 1]);
}
}

```
