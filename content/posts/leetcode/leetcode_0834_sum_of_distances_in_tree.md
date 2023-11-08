---
title: 834. sum of distances in tree
date: '2022-05-24'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0834 sum of distances in tree
---



There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] <TeX>=</TeX> [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the i^th node in the tree and all other nodes.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)
>   Input: n <TeX>=</TeX> 6, edges <TeX>=</TeX> [[0,1],[0,2],[2,3],[2,4],[2,5]]
>   Output: [8,12,6,10,10,10]
>   Explanation: The tree is shown above.
>   We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
>   equals 1 + 1 + 2 + 2 + 2 <TeX>=</TeX> 8.
>   Hence, answer[0] <TeX>=</TeX> 8, and so on.
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg)
>   Input: n <TeX>=</TeX> 1, edges <TeX>=</TeX> []
>   Output: [0]
>   Example 3:
>   ![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg)
>   Input: n <TeX>=</TeX> 2, edges <TeX>=</TeX> [[1,0]]
>   Output: [1,1]
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 3  10^4
>   	edges.length <TeX>=</TeX><TeX>=</TeX> n - 1
>   	edges[i].length <TeX>=</TeX><TeX>=</TeX> 2
>   	0 <TeX>\leq</TeX> ai, bi < n
>   	ai !<TeX>=</TeX> bi
>   	The given input represents a valid tree.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
pub fn dfs(graph: &Vec<HashSet<usize>>, count: &mut Vec<i32>, ans: &mut Vec<i32>, index: usize, parent: usize) {
for &child in graph[index].iter() {
if child != parent {
Self::dfs(graph, count, ans, child, index);
count[index] += count[child];
ans[index] += ans[child] + count[child];
}
}
}
pub fn dfs2(graph: &Vec<HashSet<usize>>, count: &Vec<i32>, ans: &mut Vec<i32>, index: usize, parent: usize) {
let n = graph.len();
for &child in graph[index].iter() {
if child != parent {
ans[child] = ans[index] - count[child] + n as i32 - count[child];
Self::dfs2(graph, count, ans, child, index);
}
}
}
pub fn sum_of_distances_in_tree(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
let n = n as usize;
let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
for i in 0..edges.len() {
let from = edges[i][0] as usize;
let to = edges[i][1] as usize;
graph[from].insert(to);
graph[to].insert(from);
}
let mut count = vec![1i32; n];
let mut ans: Vec<i32> = vec![0i32; n];
Self::dfs(&graph, &mut count, &mut ans, 0, usize::MAX);
Self::dfs2(&graph, &count, &mut ans, 0, usize::MAX);
ans
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_834() {
assert_eq!(Solution::sum_of_distances_in_tree(6, vec![vec![0,1],vec![0,2],vec![2,3],vec![2,4],vec![2,5]]), vec![8,12,6,10,10,10]);
assert_eq!(Solution::sum_of_distances_in_tree(1, vec![]), vec![0]);
assert_eq!(Solution::sum_of_distances_in_tree(2, vec![vec![1, 0]]), vec![1, 1]);
}
}

```
