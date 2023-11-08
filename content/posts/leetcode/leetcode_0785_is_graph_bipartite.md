---
title: 785. is graph bipartite
date: '2022-05-16'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0785 is graph bipartite
---



There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:



There are no self-edges (graph[u] does not contain u).

There are no parallel edges (graph[u] does not contain duplicate values).

If v is in graph[u], then u is in graph[v] (the graph is undirected).

The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.



A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg)
>   Input: graph <TeX>=</TeX> [[1,2,3],[0,2],[0,1,3],[0,2]]
>   Output: false
>   Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg)
>   Input: graph <TeX>=</TeX> [[1,3],[0,2],[1,3],[0,2]]
>   Output: true
>   Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
**Constraints:**
>   	graph.length <TeX>=</TeX><TeX>=</TeX> n
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100
>   	0 <TeX>\leq</TeX> graph[u].length < n
>   	0 <TeX>\leq</TeX> graph[u][i] <TeX>\leq</TeX> n - 1
>   	graph[u] does not contain u.
>   	All the values of graph[u] are unique.
>   	If graph[u] contains v, then graph[v] contains u.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashSet;
struct Graph {
edges: Vec<HashSet<usize>>,
n: usize,
}

impl Graph {
fn new(n: usize) -> Self {
let edges: Vec<HashSet<usize>> = vec![HashSet::new(); n];
Graph {edges, n}
}
fn insert_edge(&mut self, u: usize, v: usize) {
self.edges[u].insert(v);
}
fn neighbors(&self, u: usize) -> HashSet<usize> {
self.edges[u].clone()
}
}

struct TwoColor {
graph: Graph,
marked: Vec<bool>,
color: Vec<bool>,
is_colorable: bool
}
impl TwoColor {
fn new(graph: Graph) -> Self {
let n = graph.n;
let marked: Vec<bool> = vec![false; n];
let color: Vec<bool> = vec![false; n];
let is_colorable = true;
TwoColor {graph, marked, color, is_colorable}
}

fn color(&mut self) {
for i in 0..self.graph.n {
if !self.marked[i] {
self.dfs(i);
}
}
}

fn dfs(&mut self, i: usize) {
self.marked[i] = true;
for j in self.graph.neighbors(i) {
if !self.marked[j] {
self.color[j] = !self.color[i];
self.dfs(j);
} else if self.color[i] == self.color[j] {
self.is_colorable = false;
}
}
}
}
impl Solution {
pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
let n = graph.len();
let mut g = Graph::new(n);
for u in 0..n {
for &v in graph[u].iter() {
g.insert_edge(u, v as usize);
}
}
let mut two_color = TwoColor::new(g);
two_color.color();
two_color.is_colorable
}
}
*/
impl Solution {
pub fn dfs(graph: &Vec<Vec<i32>>, visited: &mut Vec<i8>, index: usize, color: bool) -> bool {
visited[index] = if color {0} else {1};
let neighbors = &graph[index];
for i in 0..neighbors.len() {
let neighbor = neighbors[i] as usize;
if visited[neighbor] >= 0 {
if visited[neighbor] == visited[index] {
return false;
} else {
continue;
}
}
let r = Self::dfs(graph, visited, neighbor, !color);
if !r {
return false;
}
}
true
}
pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
let n = graph.len();
let mut visited: Vec<i8> = vec![-1; n];

for i in 0..n {
if visited[i] < 0 {
if !Self::dfs(&graph, &mut visited, i, true) {
return false;
}
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
fn test_785() {
assert_eq!(Solution::is_bipartite(vec![vec![1,2,3],vec![0,2],vec![0,1,3],vec![0,2]]), false);
assert_eq!(Solution::is_bipartite(vec![vec![1,3],vec![0,2],vec![1,3],vec![0,2]]), true);
let graph = vec![
vec![],
vec![2, 4, 6],
vec![1, 4, 8, 9],
vec![7, 8],
vec![1, 2, 8, 9],
vec![6, 9],
vec![1, 5, 7, 8, 9],
vec![3, 6, 9],
vec![2, 3, 4, 6, 9],
vec![2, 4, 5, 6, 7, 8],
];
let res = false;
assert_eq!(Solution::is_bipartite(graph), res);
}
}

```
