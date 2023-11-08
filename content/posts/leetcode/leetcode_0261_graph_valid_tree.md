---
title: 261. graph valid tree
date: '2021-12-04'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0261 graph valid tree
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={261}/>

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] <TeX>=</TeX> [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.



Return true if the edges of the given graph make up a valid tree, and false otherwise.



 



 > Example 1:





 > Input: n <TeX>=</TeX> 5, edges <TeX>=</TeX> [[0,1],[0,2],[0,3],[1,4]]

 > Output: true

 > Example 2:





 > Input: n <TeX>=</TeX> 5, edges <TeX>=</TeX> [[0,1],[1,2],[2,3],[1,3],[1,4]]

 > Output: false

 



**Constraints:**



 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2000

 > 0 <TeX>\leq</TeX> edges.length <TeX>\leq</TeX> 5000

 > edges[i].length <TeX>=</TeX><TeX>=</TeX> 2

 > 0 <TeX>\leq</TeX> ai, bi < n

 > ai !<TeX>=</TeX> bi

 > There are no self-loops or repeated edges.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
    parents: Vec<usize>, 
    ranks: Vec<usize>
}

impl DisjointSet {
    pub fn new(n: usize) -> DisjointSet {
        let parents = (0..n).into_iter().collect::<Vec<usize>>();
        let ranks = vec![1; n];
        DisjointSet {
            parents: parents,
            ranks: ranks
        }
    }

    pub fn find(&self, i: usize) -> usize {
        let mut parent = i;
        while parent != self.parents[parent] {
            parent = self.parents[parent];
        }
        parent
    }

    pub fn union(&mut self, i: usize, j: usize) -> bool {
        let (i_p, j_p) = (self.find(i), self.find(j));
        if i_p == j_p {
            return false;
        }
        if self.ranks[i_p] < self.ranks[j_p] {
            self.parents[i_p] = j_p;
        } else if self.ranks[i_p] > self.ranks[j_p] {
            self.parents[j_p] = i_p;
        } else {
            self.parents[j_p] = i_p;
            self.ranks[i_p] += 1;
        }
        true
    }
}
impl Solution {
    /*
    pub fn dfs(graph: &Vec<Vec<usize>>, visited: &mut Vec<bool>, on_stack: &mut Vec<bool>, index: usize) -> bool {
        visited[index] = true;
        on_stack[index] = true;
        let neighbors = &graph[index];
        for i in 0..neighbors.len() {
            let neighbor = neighbors[i];
            if visited[neighbor] {
                if on_stack[neighbor] {
                    return true;
                }
                continue;
            }
            if Self::dfs(graph, visited, on_stack, neighbor) {
                return true;
            }
        }
        on_stack[index] = false;
        false 
    }

    pub fn valid_tree(n: i32, edges: Vec<Vec<i32>>) -> bool {
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        for i in 0..edges.len() {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            graph[start].push(end);
            graph[end].push(start);
        }
        let mut visited: Vec<bool> = vec![false; n];
        let mut on_stack: Vec<bool> = vec![false; n];
        for i in 0..n {
            if !visited[i] {
                let is_cycle = Self::dfs(&graph, &mut visited, &mut on_stack, i);
                if is_cycle {
                    return false;
                }
            }
        }
        true
    }
    */
    pub fn valid_tree(n: i32, edges: Vec<Vec<i32>>) -> bool {
        let mut disjoint_set = DisjointSet::new(n as usize);
        for i in 0..edges.len() {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            let r = disjoint_set.union(start, end);
            if !r {
                return false;
            }
        }
        let n = n as usize;
        let p = disjoint_set.find(0);
        for i in 1..n {
            if p != disjoint_set.find(i) {
                return false;
            }
        }
        //println!("parents: {:?}", disjoint_set.parents);
        true
    }

}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_261() {
        assert_eq!(Solution::valid_tree(5, vec![vec![0,1],vec![0,2],vec![0,3],vec![1,4]]), true);
        assert_eq!(Solution::valid_tree(5, vec![vec![0,1],vec![1,2],vec![2,3],vec![1,3],vec![1,4]]), false);
        assert_eq!(Solution::valid_tree(4, vec![vec![0,1],vec![2,3]]), false);
    }
}

```
