---
title: 685. redundant connection ii
date: '2022-04-19'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0685 redundant connection ii
---



In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg)
>   Input: edges <TeX>=</TeX> [[1,2],[1,3],[2,3]]
>   Output: [2,3]
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg)
>   Input: edges <TeX>=</TeX> [[1,2],[2,3],[3,4],[4,1],[1,5]]
>   Output: [4,1]
**Constraints:**
>   	n <TeX>=</TeX><TeX>=</TeX> edges.length
>   	3 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000
>   	edges[i].length <TeX>=</TeX><TeX>=</TeX> 2
>   	1 <TeX>\leq</TeX> ui, vi <TeX>\leq</TeX> n
>   	ui !<TeX>=</TeX> vi


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
pub parents: Vec<usize>,
pub ranks: Vec<usize>,
}
impl DisjointSet {
pub fn new(n: usize) -> DisjointSet {
let parents = (0..n).into_iter().collect::<Vec<_>>();
let ranks = vec![1; n];
DisjointSet {
parents,
ranks
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
self.parents[j] = i;
true
}
}
/*
impl Solution {
//Fail
pub fn find_redundant_directed_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
let n = edges.iter().map(|edge| i32::max(edge[0], edge[1])).max().unwrap() as usize;
let mut in_degrees: Vec<i32> = vec![0; n];
for i in 0..edges.len() {
let start = edges[i][0] as usize - 1;
let end = edges[i][1] as usize - 1;
in_degrees[end] += 1;
}
println!("in_dgrees: {:?}", in_degrees);
let mut disjoint_set = DisjointSet::new(n);
for i in 0..edges.len() {
let start = edges[i][0] as usize - 1;
let end = edges[i][1] as usize - 1;
let r = disjoint_set.union(start, end);
println!("start: {}, end: {}", start, end);
println!("{:?}", disjoint_set.parents);
if !r {
return edges[i].clone();
}
}
vec![]
}
}
*/
/*
Step 1. Build In and Out Degree map, detect if any any vertex with Multiple parents.
Step 2. If we don’t find vertex ‘A’ with multiple parents
2.1) Start at ‘root’ and detect any cycle with DFS, find all edges that form the cycle. Scan the edges from the back and find the first
edge that is inside the edges of the cycle.
Step 3. If we find vertex ‘A’ with multiple parents
3.1) If out degree at vertex ‘A’ is > 0, i.e there is a edge going out of the ‘A’ vertex
3.1.1) Start at ‘A’ and detect any cycle with DFS, return the edge causing the cycle. If no edge is found that form the cycle, follow the
same method in 3.2.1.
3.2) If there is NO outgoing edge from vertex ‘A’
3.2.1) Return the LAST edge that is ending at ‘A’ (i.e ‘A’ last parent)
*/
use std::collections::HashSet;
impl Solution {
pub fn dfs(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, parents: &mut Vec<usize>, count: &mut i32, index: usize, back_edge: &mut (usize, usize)) {
visited[index] = true;
*count += 1;
for &i in graph[index].iter() {
if visited[i] {
*back_edge = (index, i);
continue;
}
parents[i] = index;
Self::dfs(graph, visited, parents, count, i, back_edge);
}
}
pub fn find_last_edge(edges: &Vec<Vec<i32>>, v: usize) -> Vec<i32> {
let mut edge = vec![0i32, 0i32];
for i in (0..edges.len()).rev() {
let end = edges[i][1] as usize - 1;
if v == end  {
edge = edges[i].clone();
break;
}
}
return edge;
}
pub fn find_redundant_directed_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
let n = edges.iter().map(|edge| i32::max(edge[0], edge[1])).max().unwrap() as usize;
let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
let mut reverse_graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
for i in 0..edges.len() {
let start = edges[i][0] as usize - 1;
let end = edges[i][1] as usize - 1;
graph[start].insert(end);
reverse_graph[end].insert(start);
}
let in_degree_larger_than_two = reverse_graph.iter().position(|v| v.len() >= 2);
if in_degree_larger_than_two.is_none() { // No in degrees is larger than two
for i in 0..graph.len() {
let mut visited = vec![false; n];
let mut parents = vec![usize::MAX; n];
let mut back_edge = (usize::MAX, usize::MAX);
let mut count = 0;
Self::dfs(&graph, &mut visited, &mut parents, &mut count, i, &mut back_edge);
if count == graph.len() as i32 {
let mut hashset: HashSet<(usize, usize)> = HashSet::new();
hashset.insert((back_edge.0, back_edge.1));
let mut start = back_edge.0;
let mut end = back_edge.1;
let mut edge = back_edge;
while edge.0 != back_edge.1 {
edge = (parents[edge.0], edge.0);
hashset.insert(edge);
}
let mut edge = vec![0i32, 0i32];
for i in (0..edges.len()).rev() {
let start = edges[i][0] as usize - 1;
let end = edges[i][1] as usize - 1;
if hashset.contains(&(start, end)) {
edge = edges[i].clone();
break;
}
}
return edge;
}
}
} else {
let v = in_degree_larger_than_two.unwrap();
let out_degree = graph[v].len();
if out_degree > 0 {
let mut visited = vec![false; n];
let mut parents = vec![usize::MAX; n];
let mut back_edge = (usize::MAX, usize::MAX);
let mut count = 0;
Self::dfs(&graph, &mut visited, &mut parents, &mut count, v, &mut back_edge);
if back_edge.0 == usize::MAX && back_edge.1 == usize::MAX {
return Self::find_last_edge(&edges, v);
} else {
return vec![back_edge.0 as i32 + 1, back_edge.1 as i32 + 1];
}
} else {
return Self::find_last_edge(&edges, v);
}
}
vec![]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_685() {
assert_eq!(Solution::find_redundant_directed_connection(vec![vec![1,2],vec![3,1],vec![2,3]]), vec![2,3]);
assert_eq!(Solution::find_redundant_directed_connection(vec![vec![1,4],vec![5,2],vec![1,3],vec![4,5],vec![1,5]]), vec![1,5]);
assert_eq!(Solution::find_redundant_directed_connection(vec![vec![5,2],vec![5,1],vec![3,1],vec![3,4],vec![3,5]]), vec![3,1]);
assert_eq!(Solution::find_redundant_directed_connection(vec![vec![2,1],vec![3,1],vec![4,2],vec![1,4]]), vec![2,1]);
assert_eq!(Solution::find_redundant_directed_connection(vec![vec![1,2],vec![1,3],vec![2,3]]), vec![2,3]);
assert_eq!(Solution::find_redundant_directed_connection(vec![vec![1,2],vec![2,3],vec![3,4],vec![4,1],vec![1,5]]), vec![4,1]);
}
}



```
