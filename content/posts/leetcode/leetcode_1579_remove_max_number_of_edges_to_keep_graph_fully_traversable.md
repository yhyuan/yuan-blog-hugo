---
title: 1579. remove max number of edges to keep graph fully traversable
date: '2022-08-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1579 remove max number of edges to keep graph fully traversable
---

 

  Alice and Bob have an undirected graph of n nodes and 3 types of edges:

  

  	Type 1: Can be traversed by Alice only.

  	Type 2: Can be traversed by Bob only.

  	Type 3: Can by traversed by both Alice and Bob.

  

  Given an array edges where edges[i] <TeX>=</TeX> [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

  Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/08/19/ex1.png)

  

 >   Input: n <TeX>=</TeX> 4, edges <TeX>=</TeX> [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]

 >   Output: 2

 >   Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/08/19/ex2.png)

  

 >   Input: n <TeX>=</TeX> 4, edges <TeX>=</TeX> [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]

 >   Output: 0

 >   Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

  

 >   Example 3:

 >   ![](https://assets.leetcode.com/uploads/2020/08/19/ex3.png)

  

 >   Input: n <TeX>=</TeX> 4, edges <TeX>=</TeX> [[3,2,3],[1,1,2],[2,3,4]]

 >   Output: -1

 >   Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

   

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5

 >   	1 <TeX>\leq</TeX> edges.length <TeX>\leq</TeX> min(10^5, 3  n  (n-1) / 2)

 >   	edges[i].length <TeX>=</TeX><TeX>=</TeX> 3

 >   	1 <TeX>\leq</TeX> edges[i][0] <TeX>\leq</TeX> 3

 >   	1 <TeX>\leq</TeX> edges[i][1] < edges[i][2] <TeX>\leq</TeX> n

 >   	All tuples (typei, ui, vi) are distinct.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
pub struct DisjointSet {
    parents: Vec<usize>,
    ranks: Vec<usize>,
    count: usize,
}

impl DisjointSet {
    pub fn new(n: usize) -> Self {
        let parents = (0..n).into_iter().collect::<Vec<_>>();
        let ranks = vec![1; n];
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
        let mut p = i;
        while p != self.parents[p] {
            let tmp = self.parents[p];
            self.parents[p] = root;
            p = tmp;
        }
        root
    }

    pub fn union(&mut self, i: usize, j: usize) -> bool {
        let i_root = self.find(i);
        let j_root = self.find(j);
        if i_root == j_root {
            return false;
        }
        if self.ranks[i_root] < self.ranks[j_root] {
            self.parents[i_root] = j_root;
        } else {
            self.parents[j_root] = i_root;
            if self.ranks[i_root] == self.ranks[j_root] {
                self.ranks[i_root] += 1;
            }
        }
        self.count -= 1;
        true
    }
}
impl Solution {
    pub fn max_num_edges_to_remove(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut alice_edges: Vec<(usize, usize)> = vec![];
        let mut bob_edges: Vec<(usize, usize)> = vec![];
        let mut both_edges: Vec<(usize, usize)> = vec![];
        for i in 0..edges.len() {
            let start = edges[i][1] as usize - 1;
            let end = edges[i][2] as usize - 1;
            if edges[i][0] == 1 {
                alice_edges.push((start, end));
            }
            if edges[i][0] == 2 {
                bob_edges.push((start, end));
            }
            if edges[i][0] == 3 {
                both_edges.push((start, end));
            }
        }
        let n = n as usize;
        let mut alice_disjoint_set = DisjointSet::new(n);
        let mut bob_disjoint_set = DisjointSet::new(n);
        let mut count = 0;
        for i in 0..both_edges.len() {
            let alice_union = alice_disjoint_set.union(both_edges[i].0, both_edges[i].1);
            let bob_union = bob_disjoint_set.union(both_edges[i].0, both_edges[i].1);
            if !alice_union {
                //return edges.len() as i32 - i as i32;
                count += 1;
            }
        }
        for i in 0..alice_edges.len() {
            let alice_union = alice_disjoint_set.union(alice_edges[i].0, alice_edges[i].1);
            if !alice_union {
                count += 1;
            }
        }
        for i in 0..bob_edges.len() {
            let bob_union = bob_disjoint_set.union(bob_edges[i].0, bob_edges[i].1);
            if !bob_union {
                count += 1;
            }
        }
        if alice_disjoint_set.count == 1 && bob_disjoint_set.count == 1 {
            return count;
        }
        -1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1579() {
        assert_eq!(Solution::max_num_edges_to_remove(4, vec![vec![3,1,2],vec![3,2,3],vec![1,1,3],vec![1,2,4],vec![1,1,2],vec![2,3,4]]), 2);
        assert_eq!(Solution::max_num_edges_to_remove(4, vec![vec![3,1,2],vec![3,2,3],vec![1,1,4],vec![2,1,4]]), 0);
        assert_eq!(Solution::max_num_edges_to_remove(4, vec![vec![3,2,3],vec![1,1,2],vec![2,3,4]]), -1);
    }
}

```
