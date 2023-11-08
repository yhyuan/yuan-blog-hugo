---
title: 1489. find critical and pseudo critical edges in minimum spanning tree
date: '2022-08-09'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 1489 find critical and pseudo critical edges in minimum spanning tree
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1489}/>
 

  Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] <TeX>=</TeX> [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

  Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

  Note that you can return the indices of the edges in any order.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/06/04/ex1.png)

  

 >   Input: n <TeX>=</TeX> 5, edges <TeX>=</TeX> [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]

 >   Output: [[0,1],[2,3,4,5]]

 >   Explanation: The figure above describes the graph.

 >   The following figure shows all the possible MSTs:

 >   ![](https://assets.leetcode.com/uploads/2020/06/04/msts.png)

 >   Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.

 >   The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/06/04/ex2.png)

  

 >   Input: n <TeX>=</TeX> 4, edges <TeX>=</TeX> [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]

 >   Output: [[],[0,1,2,3]]

 >   Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100

 >   	1 <TeX>\leq</TeX> edges.length <TeX>\leq</TeX> min(200, n  (n - 1) / 2)

 >   	edges[i].length <TeX>=</TeX><TeX>=</TeX> 3

 >   	0 <TeX>\leq</TeX> ai < bi < n

 >   	1 <TeX>\leq</TeX> weighti <TeX>\leq</TeX> 1000

 >   	All pairs (ai, bi) are distinct.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
pub struct UF {
    parents: Vec<usize>,
    ranks: Vec<usize>,
    count: usize,
}

impl UF {
    pub fn new(n: usize) -> Self {
        let parents = (0..n).into_iter().collect::<Vec<_>>();
        let ranks = vec![1; n];
        let count = n;
        UF {
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
    pub fn build_mst(n: usize, edges: &Vec<Vec<i32>>, included: usize, excluded: usize) -> i32 {
        let mut uf = UF::new(n);
        let mut res = 0i32;
        if included != usize::MAX {
            let start = edges[included][0] as usize;
            let end = edges[included][1] as usize;
            let cost = edges[included][2];
            uf.union(start, end);
            res += cost;
        }
        for i in 0..edges.len() {
            if excluded != usize::MAX && i == excluded {
                continue;
            }
            if included != usize::MAX && i == included {
                continue;
            }
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            let cost = edges[i][2];
            if uf.find(start) != uf.find(end) {
                uf.union(start, end);
                res += cost;
            }
        }
        //println!("count: {}", uf.count);
        if uf.count > 1 {
            return i32::MAX;
        }
        res
    }
    pub fn find_critical_and_pseudo_critical_edges(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut edges = edges;
        for i in 0..edges.len() {
            edges[i].push(i as i32);
        }
        edges.sort_by(|a, b| a[2].partial_cmp(&b[2]).unwrap()); // sort by cost
        let all_res = Self::build_mst(n, &edges, usize::MAX, usize::MAX);
        let mut critical: Vec<i32> = vec![];
        let mut non_critical: Vec<i32> = vec![];
        for i in 0..edges.len() {
            let exclude_res = Self::build_mst(n, &edges, usize::MAX, i);
            let include_res = Self::build_mst(n, &edges, i, usize::MAX);
            if exclude_res > all_res {
                critical.push(edges[i][3]);
            } else if include_res == all_res {
                non_critical.push(edges[i][3])
            }
        }
        vec![critical, non_critical]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1489() {
        assert_eq!(Solution::find_critical_and_pseudo_critical_edges(4, vec![vec![0,1,1],vec![0,3,1],vec![0,2,1],vec![1,2,1],vec![1,3,1],vec![2,3,1]]), vec![vec![],vec![0,1, 2,3,4,5]]);
        assert_eq!(Solution::find_critical_and_pseudo_critical_edges(5, vec![vec![0,1,1],vec![1,2,1],vec![2,3,2],vec![0,3,2],vec![0,4,3],vec![3,4,3],vec![1,4,6]]), vec![vec![0,1],vec![2,3,4,5]]);
        assert_eq!(Solution::find_critical_and_pseudo_critical_edges(4, vec![vec![0,1,1],vec![1,2,1],vec![2,3,1],vec![0,3,1]]), vec![vec![],vec![0,1,2,3]]);
    }
}

```
