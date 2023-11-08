---
title: 1168. optimize water distribution in a village
date: '2022-07-16'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1168 optimize water distribution in a village
---


There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.



For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each pipes[j] <TeX>=</TeX> [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.



Return the minimum total cost to supply water to all houses.







> Example 1:
> Input: n <TeX>=</TeX> 3, wells <TeX>=</TeX> [1,2,2], pipes <TeX>=</TeX> [[1,2,1],[2,3,1]]
> Output: 3
> Explanation: The image shows the costs of connecting houses using pipes.
> The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
> Example 2:
> Input: n <TeX>=</TeX> 2, wells <TeX>=</TeX> [1,1], pipes <TeX>=</TeX> [[1,2,1],[1,2,2]]
> Output: 2
> Explanation: We can supply water with cost two using one of the three options:
> Option 1:
>   - Build a well inside house 1 with cost 1.
>   - Build a well inside house 2 with cost 1.
> The total cost will be 2.
> Option 2:
>   - Build a well inside house 1 with cost 1.
>   - Connect house 2 with house 1 with cost 1.
> The total cost will be 2.
> Option 3:
>   - Build a well inside house 2 with cost 1.
>   - Connect house 1 with house 2 with cost 1.
> The total cost will be 2.
> Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option.
**Constraints:**
> 2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 104
> wells.length <TeX>=</TeX><TeX>=</TeX> n
> 0 <TeX>\leq</TeX> wells[i] <TeX>\leq</TeX> 105
> 1 <TeX>\leq</TeX> pipes.length <TeX>\leq</TeX> 104
> pipes[j].length <TeX>=</TeX><TeX>=</TeX> 3
> 1 <TeX>\leq</TeX> house1j, house2j <TeX>\leq</TeX> n
> 0 <TeX>\leq</TeX> costj <TeX>\leq</TeX> 105
> house1j !<TeX>=</TeX> house2j


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct UF {
parents: Vec<usize>,
ranks: Vec<usize>,
count: usize,
}

impl UF {
pub fn new(n: usize) -> UF {
let parents = (0..n).into_iter().collect::<Vec<_>>();
let ranks = vec![1; n];
let count = n;
UF {
parents,
ranks,
count,
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
if self.ranks[ip] < self.ranks[jp] {
self.parents[ip] = jp;
} else {
self.parents[jp] = ip;
if self.ranks[ip] == self.ranks[jp] {
self.ranks[ip] += 1;
}
}
self.count -= 1;
true
}
}
use std::collections::{HashSet, HashMap};
impl Solution {
pub fn min_cost_to_supply_water(n: i32, wells: Vec<i32>, pipes: Vec<Vec<i32>>) -> i32 {
let n = n as usize;
//let mut wells_res = wells.iter().sum::<i32>();
let mut uf = UF::new(n + 1);
let mut pipes = pipes;
for i in 0..wells.len() {
pipes.push(vec![0, i as i32 + 1, wells[i]]); // Virtual link for wells.
}
pipes.sort_by(|a, b| a[2].partial_cmp(&b[2]).unwrap());
// let mut selected_pipes: Vec<usize> = vec![];
let mut res = 0;
for i in 0..pipes.len() {
let start = pipes[i][0] as usize;
let end = pipes[i][1] as usize;
let cost = pipes[i][2];
if uf.find(start) != uf.find(end) {
uf.union(start, end);
res += cost;
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
fn test_1168() {
assert_eq!(Solution::min_cost_to_supply_water(3, vec![1, 2, 2], vec![vec![1,2,1],vec![2,3,1]]), 3);
assert_eq!(Solution::min_cost_to_supply_water(2, vec![1, 1], vec![vec![1,2,1],vec![1,2,2]]), 2);
}
}

```
