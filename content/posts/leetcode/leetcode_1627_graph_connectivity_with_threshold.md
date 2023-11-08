---
title: 1627. graph connectivity with threshold
date: '2022-08-20'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1627 graph connectivity with threshold
---



We have n cities labeled from 1 to n. Two different cities with labels x and y are directly connected by a bidirectional road if and only if x and y share a common divisor strictly greater than some threshold. More formally, cities with labels x and y have a road between them if there exists an integer z such that all of the following are true:



x % z <TeX>=</TeX><TeX>=</TeX> 0,

y % z <TeX>=</TeX><TeX>=</TeX> 0, and

z > threshold.



Given the two integers, n and threshold, and an array of queries, you must determine for each queries[i] <TeX>=</TeX> [ai, bi] if cities ai and bi are connected directly or indirectly. (i.e. there is some path between them).

Return an array answer, where answer.length <TeX>=</TeX><TeX>=</TeX> queries.length and answer[i] is true if for the i^th query, there is a path between ai and bi, or answer[i] is false if there is no path.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/10/09/ex1.jpg)
>   Input: n <TeX>=</TeX> 6, threshold <TeX>=</TeX> 2, queries <TeX>=</TeX> [[1,4],[2,5],[3,6]]
>   Output: [false,false,true]
>   Explanation: The divisors for each number:
>   1:   1
>   2:   1, 2
>   3:   1, <u>3</u>
>   4:   1, 2, <u>4</u>
>   5:   1, <u>5</u>
>   6:   1, 2, <u>3</u>, <u>6</u>
>   Using the underlined divisors above the threshold, only cities 3 and 6 share a common divisor, so they are the
>   only ones directly connected. The result of each query:
>   [1,4]   1 is not connected to 4
>   [2,5]   2 is not connected to 5
>   [3,6]   3 is connected to 6 through path 3--6
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/10/10/tmp.jpg)
>   Input: n <TeX>=</TeX> 6, threshold <TeX>=</TeX> 0, queries <TeX>=</TeX> [[4,5],[3,4],[3,2],[2,6],[1,3]]
>   Output: [true,true,true,true,true]
>   Explanation: The divisors for each number are the same as the previous example. However, since the threshold is 0,
>   all divisors can be used. Since all numbers share 1 as a divisor, all cities are connected.
>   Example 3:
>   ![](https://assets.leetcode.com/uploads/2020/10/17/ex3.jpg)
>   Input: n <TeX>=</TeX> 5, threshold <TeX>=</TeX> 1, queries <TeX>=</TeX> [[4,5],[4,5],[3,2],[2,3],[3,4]]
>   Output: [false,false,false,false,false]
>   Explanation: Only cities 2 and 4 share a common divisor 2 which is strictly greater than the threshold 1, so they are the only ones directly connected.
>   Please notice that there can be multiple queries for the same pair of nodes [x, y], and that the query [x, y] is equivalent to the query [y, x].
**Constraints:**
>   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4
>   	0 <TeX>\leq</TeX> threshold <TeX>\leq</TeX> n
>   	1 <TeX>\leq</TeX> queries.length <TeX>\leq</TeX> 10^5
>   	queries[i].length <TeX>=</TeX><TeX>=</TeX> 2
>   	1 <TeX>\leq</TeX> ai, bi <TeX>\leq</TeX> cities
>   	ai !<TeX>=</TeX> bi


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
pub parents: Vec<usize>,
pub ranks: Vec<usize>,
pub count: usize,
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

pub fn find(&mut self, i: usize) -> usize {
let mut root = self.parents[i];
while root != self.parents[root] {
root = self.parents[root];
}
let mut p = self.parents[i];
while p != self.parents[p] {
let tmp = self.parents[p];
self.parents[p] = root;
p = tmp;
}
root
}

pub fn union(&mut self, i: usize, j: usize) -> bool {
let ip = self.find(i);
let jp = self.find(j);
if ip == jp {
return false;
}
if self.ranks[ip] > self.ranks[jp] {
self.parents[jp] = ip;
} else {
self.parents[ip] = jp;
if self.ranks[ip] == self.ranks[jp] {
self.ranks[jp] += 1;
}
}
self.count -= 1;
true
}
}
impl Solution {
pub fn gcd(small: usize, large: usize) -> usize {
let temp = large % small;
if temp == 0 {
return small;
}
Self::gcd(temp, small)
}
pub fn are_connected(n: i32, threshold: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
let n = n as usize;
let threshold = threshold as usize;
if threshold == 0 {
return vec![true; queries.len()];
}
let mut disjoint_set = DisjointSet::new(n + 1);
for i in threshold + 1..=n {
let mut j = 2 * i;
while j <= n {
disjoint_set.union(i, j);
j += i;
}
}
queries.into_iter()
.map(|query| disjoint_set.find(query[0] as usize) == disjoint_set.find(query[1] as usize))
.collect::<Vec<bool>>()
/*
let mut disjoint_set = DisjointSet::new(n);
for i in 0..n {
if i < threshold {
continue;
}
for j in i + 1..n {
//println!("i: {}, j: {}, gcd: {}", i + 1, j + 1, Self::gcd(i + 1, j + 1));
if j - i < threshold {
continue;
}
if Self::gcd(i + 1, j + 1) > threshold {
disjoint_set.union(i, j);
}
}
}
queries.into_iter()
.map(|query| disjoint_set.find(query[0] as usize - 1) == disjoint_set.find(query[1] as usize - 1))
.collect::<Vec<bool>>()
*/
//println!("done");
/*
let mut result: Vec<bool> = Vec::new();
for i in 0..queries.len() {
let start = queries[i][0] as usize;
let end = queries[i][1] as usize;
result.push(disjoint_set.find(start - 1) == disjoint_set.find(end - 1));
}
result
*/
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1627() {
assert_eq!(Solution::are_connected(10000, 255, vec![vec![1,4],vec![2,5],vec![3,6]]), vec![false,false,false]);
assert_eq!(Solution::are_connected(6, 2, vec![vec![1,4],vec![2,5],vec![3,6]]), vec![false,false,true]);
assert_eq!(Solution::are_connected(6, 0, vec![vec![4,5],vec![3,4],vec![3,2],vec![2,6],vec![1,3]]), vec![true,true,true,true,true]);
assert_eq!(Solution::are_connected(5, 1, vec![vec![4,5],vec![4,5],vec![3,2],vec![2,3],vec![3,4]]), vec![false,false,false,false,false]);
}
}

```
