---
title: 1557. minimum number of vertices to reach all nodes
date: '2022-08-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1557 minimum number of vertices to reach all nodes
---

 

  Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] <TeX>=</TeX> [fromi, toi] represents a directed edge from node fromi to node toi.

  

  Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

  

  Notice that you can return the vertices in any order.

  

   

 >   Example 1:

  

 >   ![](https://assets.leetcode.com/uploads/2020/07/07/untitled22.png)

  

  

 >   Input: n <TeX>=</TeX> 6, edges <TeX>=</TeX> [[0,1],[0,2],[2,5],[3,4],[4,2]]

 >   Output: [0,3]

 >   Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

  

 >   Example 2:

  

 >   ![](https://assets.leetcode.com/uploads/2020/07/07/untitled.png)

  

  

 >   Input: n <TeX>=</TeX> 5, edges <TeX>=</TeX> [[0,1],[2,1],[3,1],[1,4],[2,4]]

 >   Output: [0,2,3]

 >   Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.

  

  

   

  **Constraints:**

  

  

 >   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5

 >   	1 <TeX>\leq</TeX> edges.length <TeX>\leq</TeX> min(10^5, n  (n - 1) / 2)

 >   	edges[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> fromi, toi < n

 >   	All pairs (fromi, toi) are distinct.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
    pub fn find_smallest_set_of_vertices(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        //let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        let mut ends: HashSet<usize> = HashSet::new();
        for i in 0..edges.len() {
            //let start = edges[i][0] as usize;
            let end   = edges[i][1] as usize;
            ends.insert(end);
            //graph[start].push(end);
        }
        let mut result: Vec<i32> = vec![];
        for i in 0..n {
            if ends.contains(&i) {
                continue;
            }
            result.push(i as i32);
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1557() {
        assert_eq!(Solution::find_smallest_set_of_vertices(6, vec![vec![0,1],vec![0,2],vec![2,5],vec![3,4],vec![4,2]]), vec![0,3]);
        assert_eq!(Solution::find_smallest_set_of_vertices(5, vec![vec![0,1],vec![2,1],vec![3,1],vec![1,4],vec![2,4]]), vec![0,2,3]);
    }
}

```
