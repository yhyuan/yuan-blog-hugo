---
title: 1319. number of operations to make network connected
date: '2022-07-31'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1319 number of operations to make network connected
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1319}/>
 

  There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] <TeX>=</TeX> [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

  Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png)

  

 >   Input: n <TeX>=</TeX> 4, connections <TeX>=</TeX> [[0,1],[0,2],[1,2]]

 >   Output: 1

 >   Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/01/02/sample_2_1677.png)

  

 >   Input: n <TeX>=</TeX> 6, connections <TeX>=</TeX> [[0,1],[0,2],[0,3],[1,2],[1,3]]

 >   Output: 2

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 6, connections <TeX>=</TeX> [[0,1],[0,2],[0,3],[1,2]]

 >   Output: -1

 >   Explanation: There are not enough cables.

  

 >   Example 4:

  

 >   Input: n <TeX>=</TeX> 5, connections <TeX>=</TeX> [[0,1],[0,2],[3,4],[2,3]]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5

 >   	1 <TeX>\leq</TeX> connections.length <TeX>\leq</TeX> min(n(n-1)/2, 10^5)

 >   	connections[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> connections[i][0], connections[i][1] < n

 >   	connections[i][0] !<TeX>=</TeX> connections[i][1]

 >   	There are no repeated connections.

 >   	No two computers are connected by more than one cable.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn dfs(graph: &Vec<Vec<usize>>, visited: &mut Vec<bool>, index: usize, connection_count: &mut i32) {
        visited[index] = true;
        for &i in (graph[index]).iter(){
            if visited[i] {
                //*back_edge_count += 1;
                // valid_connections[i.1] = false;
                continue;
            }
            *connection_count += 1;
            Self::dfs(graph, visited, i, connection_count);
        }
    }
    pub fn make_connected(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        for i in 0..connections.len() {
            let start = connections[i][0] as usize;
            let end = connections[i][1] as usize;
            graph[start].push(end);
            graph[end].push(start);
        }
        let mut visited = vec![false; n];
        let mut count = 0;
        let mut connection_count = 0;
        for i in 0..n {
            if visited[i] {
                continue;
            }
            count += 1;
            Self::dfs(&graph, &mut visited, i, &mut connection_count);
        }
        let extra = connections.len() as i32 - connection_count; // 
        if extra + 1 >= count {
            return count - 1;
        }
        // println!("count: {}, connection_count: {}", count, connection_count);
        -1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1319() {
        assert_eq!(Solution::make_connected(4, vec![vec![0,1],vec![0,2],vec![1,2]]), 1);
        assert_eq!(Solution::make_connected(6, vec![vec![0,1],vec![0,2],vec![0,3],vec![1,2],vec![1,3]]), 2);
        assert_eq!(Solution::make_connected(6, vec![vec![0,1],vec![0,2],vec![1,2]]), -1);
    }
}

```
