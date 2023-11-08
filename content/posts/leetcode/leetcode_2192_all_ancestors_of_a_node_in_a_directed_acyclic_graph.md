---
title: 2192. all ancestors of a node in a directed acyclic graph
date: '2022-09-22'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2192 all ancestors of a node in a directed acyclic graph
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2192}/>

You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).



You are also given a 2D integer array edges, where edges[i] <TeX>=</TeX> [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.



Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.



A node u is an ancestor of another node v if u can reach v via a set of edges.



 



 > Example 1:





 > Input: n <TeX>=</TeX> 8, edgeList <TeX>=</TeX> [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

 > Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]

 > Explanation:

 > The above diagram represents the input graph.

 > - Nodes 0, 1, and 2 do not have any ancestors.

 > - Node 3 has two ancestors 0 and 1.

 > - Node 4 has two ancestors 0 and 2.

 > - Node 5 has three ancestors 0, 1, and 3.

 > - Node 6 has five ancestors 0, 1, 2, 3, and 4.

 > - Node 7 has four ancestors 0, 1, 2, and 3.

 > Example 2:





 > Input: n <TeX>=</TeX> 5, edgeList <TeX>=</TeX> [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

 > Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]

 > Explanation:

 > The above diagram represents the input graph.

 > - Node 0 does not have any ancestor.

 > - Node 1 has one ancestor 0.

 > - Node 2 has two ancestors 0 and 1.

 > - Node 3 has three ancestors 0, 1, and 2.

 > - Node 4 has four ancestors 0, 1, 2, and 3.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000

 > 0 <TeX>\leq</TeX> edges.length <TeX>\leq</TeX> min(2000, n  (n - 1) / 2)

 > edges[i].length <TeX>=</TeX><TeX>=</TeX> 2

 > 0 <TeX>\leq</TeX> fromi, toi <TeX>\leq</TeX> n - 1

 > fromi !<TeX>=</TeX> toi

 > There are no duplicate edges.

 > The graph is directed and acyclic.


## Solution
### Rust
```rust
// use std::collections::HashMap;
pub struct Solution {}

impl Solution {
    pub fn dfs(graph: &Vec<Vec<usize>>, visited: &mut Vec<bool>, index: usize) {
        visited[index] = true;
        // let neighbors = graph[index];
        for i in 0..graph[index].len() {
            let neighbor = graph[index][i];
            if visited[neighbor] {
                continue;
            }
            Self::dfs(graph, visited, neighbor);
        }
    }

    pub fn get_ancestors(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        for i in 0..edges.len() {
            let index = edges[i][1] as usize;
            let value = edges[i][0] as usize;
            graph[index].push(value); 
        }
        // println!("graph: {:?}", graph);
        let mut result: Vec<Vec<i32>> = vec![];
        for i in 0..n {
            let mut visited: Vec<bool> = vec![false; n];
            Self::dfs(&graph, &mut visited, i);
            let mut res: Vec<i32> = vec![];
            for j in 0..n {
                if visited[j] && j != i {
                    res.push(j as i32);
                }
            }
            result.push(res);
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2192() {
        assert_eq!(Solution::get_ancestors(8, vec![
            vec![0,3],vec![0,4],vec![1,3],vec![2,4],vec![2,7],vec![3,5],vec![3,6],vec![3,7],vec![4,6]
        ]), vec![vec![],vec![],vec![],vec![0,1],vec![0,2],vec![0,1,3],vec![0,1,2,3,4],vec![0,1,2,3]]);
    }
}


```
