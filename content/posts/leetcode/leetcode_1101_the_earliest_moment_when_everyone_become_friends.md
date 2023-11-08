---
title: 1101. the earliest moment when everyone become friends
date: '2022-07-07'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1101 the earliest moment when everyone become friends
---


There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] <TeX>=</TeX> [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.



Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.



Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.







> Example 1:
> Input: logs <TeX>=</TeX> [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n <TeX>=</TeX> 6
> Output: 20190301
> Explanation:
> The first event occurs at timestamp <TeX>=</TeX> 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
> The second event occurs at timestamp <TeX>=</TeX> 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
> The third event occurs at timestamp <TeX>=</TeX> 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
> The fourth event occurs at timestamp <TeX>=</TeX> 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
> The fifth event occurs at timestamp <TeX>=</TeX> 20190224 and as 2 and 4 are already friends anything happens.
> The sixth event occurs at timestamp <TeX>=</TeX> 20190301 and after 0 and 3 become friends we have that all become friends.
> Example 2:
> Input: logs <TeX>=</TeX> [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n <TeX>=</TeX> 4
> Output: 3
**Constraints:**
> 2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100
> 1 <TeX>\leq</TeX> logs.length <TeX>\leq</TeX> 104
> logs[i].length <TeX>=</TeX><TeX>=</TeX> 3
> 0 <TeX>\leq</TeX> timestampi <TeX>\leq</TeX> 109
> 0 <TeX>\leq</TeX> xi, yi <TeX>\leq</TeX> n - 1
> xi !<TeX>=</TeX> yi
> All the values timestampi are unique.
> All the pairs (xi, yi) occur at most one time in the input.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
pub parents: Vec<usize>,
pub ranks: Vec<usize>,
pub size: usize,
}

impl DisjointSet {
pub fn new(n: usize) -> Self {
let ranks = vec![1; n];
let parents = (0..n).into_iter().collect::<Vec<_>>();
let size = n;
DisjointSet {
ranks,
parents,
size,
}
}

pub fn find(&self, i: usize) -> usize {
let mut parent = self.parents[i];
while parent != self.parents[parent] {
parent = self.parents[parent];
}
parent
}

pub fn union(&mut self, i: usize, j: usize) -> bool {
let ip = self.find(i);
let jp = self.find(j);
if ip == jp {
return false;
}
if self.ranks[ip] < self.ranks[jp] {
self.parents[ip] = self.parents[jp];
} else if self.parents[ip] > self.parents[jp] {
self.parents[jp] = self.parents[ip];
} else {
self.parents[jp] = self.parents[ip];
self.ranks[ip] += 1;
}
self.size -= 1;
true
}
}
impl Solution {
pub fn earliest_acq(logs: Vec<Vec<i32>>, n: i32) -> i32 {
let mut logs = logs;
logs.sort_by(|x, y| x[0].cmp(&y[0]));
let mut disjoint_set = DisjointSet::new(n as usize);
for i in 0..logs.len() {
let timestamp = logs[i][0];
let start =  logs[i][1] as usize;
let end = logs[i][2] as usize;
disjoint_set.union(start, end);
if disjoint_set.size == 1 {
return timestamp;
}
}
-1
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1101() {
assert_eq!(Solution::earliest_acq(vec![vec![20190101,0,1],vec![20190104,3,4],vec![20190107,2,3],vec![20190211,1,5],vec![20190224,2,4],vec![20190301,0,3],vec![20190312,1,2],vec![20190322,4,5]], 6), 20190301);
assert_eq!(Solution::earliest_acq(vec![vec![9,3,0],vec![0,2,1],vec![8,0,1],vec![1,3,2],vec![2,2,0],vec![3,3,1]], 4), 2);
}
}

```
