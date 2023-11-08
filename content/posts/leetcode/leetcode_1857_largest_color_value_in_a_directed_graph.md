---
title: 1857. largest color value in a directed graph
date: '2022-08-27'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 1857 largest color value in a directed graph
---

 

  There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

  

  You are given a string colors where colors[i] is a lowercase English letter representing the color of the i^th node in this graph (0-indexed). You are also given a 2D array edges where edges[j] <TeX>=</TeX> [aj, bj] indicates that there is a directed edge from node aj to node bj.

  

  A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <TeX>\leq</TeX> i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

  

  Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

  

   

 >   Example 1:

  

 >   ![](https://assets.leetcode.com/uploads/2021/04/21/leet1.png)

  

  

 >   Input: colors <TeX>=</TeX> "abaca", edges <TeX>=</TeX> [[0,1],[0,2],[2,3],[3,4]]

 >   Output: 3

 >   Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

  

  

 >   Example 2:

  

 >   ![](https://assets.leetcode.com/uploads/2021/04/21/leet2.png)

  

  

 >   Input: colors <TeX>=</TeX> "a", edges <TeX>=</TeX> [[0,0]]

 >   Output: -1

 >   Explanation: There is a cycle from 0 to 0.

  

  

   

  **Constraints:**

  

  

 >   	n <TeX>=</TeX><TeX>=</TeX> colors.length

 >   	m <TeX>=</TeX><TeX>=</TeX> edges.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> m <TeX>\leq</TeX> 10^5

 >   	colors consists of lowercase English letters.

 >   	0 <TeX>\leq</TeX> aj, bj < n


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
then the output will be 4 as 0 -> 1 -> 2 -> 3 -> 5 has longest path with color 'a'.

To solve this, we will follow these steps −

n:= size of col

graph:= given graph from the edge list

indegree:= map containing nodes and their in-degree values

queue:= a new list

dp:= make an array of size n x 26, and fill with 0

colorvalues:= make a list with order of c in alphabet for all c in col

for u in range 0 to n - 1, do

    if u is not in indegree, then

        insert u at the end of queue

        dp[u, colorvalues[u]]:= 1

visited:= 0

while queue is not empty, do

    u:= front element of queue and delete it after

    visited := visited + 1

    for each v in graph[u], do

        for c in range 0 to 25, do

            dp[v, c] = maximum of dp[v, c] and (dp[u, c] + (1 if c is same as colorvalues[v], otherwise 0)

        indegree[v] := indegree[v] - 1

        if indegree[v] is same as 0, then

            insert v at the end of queue

            del indegree[v]

if visited < n, then

    return -1

return maximum element in dp
*/
// Kahn’s algorithm for Topological Sorting  https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
use std::collections::{VecDeque, HashSet};
impl Solution {
    pub fn largest_path_value(colors: String, edges: Vec<Vec<i32>>) -> i32 {
        let n = colors.len();
        let colors = colors.chars().collect::<Vec<_>>();
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        let mut in_degree = vec![0; n];
        for i in 0..edges.len() {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            graph[start].insert(end);
            in_degree[end] += 1;
        }
        let mut dp = vec![vec![0; 26]; n];
        let mut q: VecDeque<usize> = VecDeque::new();
        for i in 0..n {
            if in_degree[i] == 0 {
                q.push_back(i);
                dp[i][colors[i] as usize - 'a' as usize] = 1;
            }
        }
        // let mut top_order: Vec<usize> = vec![];
        let mut cnt = 0;
        let mut result = 0;
        while !q.is_empty() {
            let u = q.pop_front().unwrap();
            result = i32::max(result, *dp[u].iter().max().unwrap() as i32);
            cnt += 1;
            // top_order.push(u);
            for &v in graph[u].iter() {
                for c in 0..26 {
                    dp[v][c] = i32::max(dp[v][c], dp[u][c] + if c == colors[v] as usize - 'a' as usize {1} else {0});
                }
                in_degree[v] -= 1;
                if in_degree[v] == 0 {
                    q.push_back(v);
                }
            }
        }
        if cnt < n {-1} else {result}
    }
}


// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1857() {
        assert_eq!(Solution::largest_path_value("iivvvvv".to_string(), vec![vec![0,1],vec![1,2],vec![1,3],vec![2,3],vec![3,4],vec![2,4],vec![3,5],vec![1,5],vec![4,5],vec![5,6]]), 5);
        assert_eq!(Solution::largest_path_value("abaca".to_string(), vec![vec![0,1],vec![0,2],vec![2,3],vec![3,4]]), 3);
        assert_eq!(Solution::largest_path_value("a".to_string(), vec![vec![0,0]]), -1);
    }
}




```
