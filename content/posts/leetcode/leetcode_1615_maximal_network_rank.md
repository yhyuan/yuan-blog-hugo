---
title: 1615. maximal network rank
date: '2022-08-19'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1615 maximal network rank
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1615}/>
 

  There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] <TeX>=</TeX> [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

  The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

  The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

  Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/09/21/ex1.png)

  

 >   Input: n <TeX>=</TeX> 4, roads <TeX>=</TeX> [[0,1],[0,3],[1,2],[1,3]]

 >   Output: 4

 >   Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/09/21/ex2.png)

  

 >   Input: n <TeX>=</TeX> 5, roads <TeX>=</TeX> [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]

 >   Output: 5

 >   Explanation: There are 5 roads that are connected to cities 1 or 2.

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 8, roads <TeX>=</TeX> [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]

 >   Output: 5

 >   Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100

 >   	0 <TeX>\leq</TeX> roads.length <TeX>\leq</TeX> n  (n - 1) / 2

 >   	roads[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> ai, bi <TeX>\leq</TeX> n-1

 >   	ai !<TeX>=</TeX> bi

 >   	Each pair of cities has at most one road connecting them.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        for i in 0..roads.len() {
            let start = roads[i][0] as usize;
            let end = roads[i][1] as usize;
            graph[start].insert(end);
            graph[end].insert(start);
        }
        let mut result = -1;
        for i in 0..n {
            for j in i + 1..n {
                let a = &graph[i].iter().map(|&k|if i < k {(i, k)} else {(k, i)}).collect::<HashSet<_>>();
                let b = &graph[j].iter().map(|&k|if j < k {(j, k)} else {(k, j)}).collect::<HashSet<_>>();
                // println!("a: {:?}, b: {:?}", a, b);
                let a = a.clone();
                let union_set = a.union(b).collect::<Vec<&(usize, usize)>>();
                result = i32::max(result, union_set.len() as i32);
            }
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1615() {
        assert_eq!(Solution::maximal_network_rank(2, vec![vec![1,0]]), 1);
        //assert_eq!(Solution::maximal_network_rank(4, vec![vec![0,1],vec![0,3],vec![1,2],vec![1,3]]), 4);
        //assert_eq!(Solution::maximal_network_rank(5, vec![vec![0,1],vec![0,3],vec![1,2],vec![1,3],vec![2,3],vec![2,4]]), 5);
        //assert_eq!(Solution::maximal_network_rank(8, vec![vec![0,1],vec![1,2],vec![2,3],vec![2,4],vec![5,6],vec![5,7]]), 5);
    }
}

```
