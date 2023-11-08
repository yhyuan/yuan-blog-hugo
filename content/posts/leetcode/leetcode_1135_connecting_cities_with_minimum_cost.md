---
title: 1135. connecting cities with minimum cost
date: '2022-07-10'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1135 connecting cities with minimum cost
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1135}/>

There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] <TeX>=</TeX> [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.



Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,



The cost is the sum of the connections' costs used.



 



 > Example 1:





 > Input: n <TeX>=</TeX> 3, connections <TeX>=</TeX> [[1,2,5],[1,3,6],[2,3,1]]

 > Output: 6

 > Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.

 > Example 2:





 > Input: n <TeX>=</TeX> 4, connections <TeX>=</TeX> [[1,2,3],[3,4,4]]

 > Output: -1

 > Explanation: There is no way to connect all cities even if all edges are used.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 104

 > 1 <TeX>\leq</TeX> connections.length <TeX>\leq</TeX> 104

 > connections[i].length <TeX>=</TeX><TeX>=</TeX> 3

 > 1 <TeX>\leq</TeX> xi, yi <TeX>\leq</TeX> n

 > xi !<TeX>=</TeX> yi

 > 0 <TeX>\leq</TeX> costi <TeX>\leq</TeX> 105


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
impl Solution {
    pub fn minimum_cost(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let mut connections = connections;
        connections.sort_by(|a, b| a[2].partial_cmp(&b[2]).unwrap());
        let n = n as usize;
        let mut uf = UF::new(n);
        let mut res = 0;
        for i in 0..connections.len() {
            let start = connections[i][0] as usize - 1;
            let end   = connections[i][1] as usize - 1;
            let cost  = connections[i][2];
            let start_parent = uf.find(start);
            let end_parent = uf.find(end);
            if start_parent != end_parent {
                res += cost;
                uf.union(start, end);
            }
        }
        if uf.count == 1 {res} else {-1}
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1135() {
        assert_eq!(Solution::minimum_cost(3, vec![vec![1,2,5],vec![1,3,6],vec![2,3,1]]), 6);
        assert_eq!(Solution::minimum_cost(4, vec![vec![1,2,3],vec![3,4,4]]), -1);
    }
}

```
