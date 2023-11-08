---
title: 547. number of provinces
date: '2022-03-31'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0547 number of provinces
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={547}/>
 

  There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

  A province is a group of directly or indirectly connected cities and no other cities outside of the group.

  You are given an n x n matrix isConnected where isConnected[i][j] <TeX>=</TeX> 1 if the i^th city and the j^th city are directly connected, and isConnected[i][j] <TeX>=</TeX> 0 otherwise.

  Return the total number of provinces.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

 >   Input: isConnected <TeX>=</TeX> [[1,1,0],[1,1,0],[0,0,1]]

 >   Output: 2

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

 >   Input: isConnected <TeX>=</TeX> [[1,0,0],[0,1,0],[0,0,1]]

 >   Output: 3

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 200

 >   	n <TeX>=</TeX><TeX>=</TeX> isConnected.length

 >   	n <TeX>=</TeX><TeX>=</TeX> isConnected[i].length

 >   	isConnected[i][j] is 1 or 0.

 >   	isConnected[i][i] <TeX>=</TeX><TeX>=</TeX> 1

 >   	isConnected[i][j] <TeX>=</TeX><TeX>=</TeX> isConnected[j][i]


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn dfs(is_connected: &Vec<Vec<i32>>, visited: &mut Vec<bool>, index: usize) {
        visited[index] = true;
        let n = is_connected.len();
        let neighbors = (0..n).into_iter().filter(|&i| is_connected[index][i] == 1 && !visited[i]).collect::<Vec<_>>();
        for i in 0..neighbors.len() {
            let neighbor = neighbors[i];
            Self::dfs(is_connected, visited, neighbor);
        }
    }
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut visited: Vec<bool> = vec![false; n];
        let mut count = 0;
        for i in 0..n {
            if visited[i] {
                continue;
            }
            Self::dfs(&is_connected, &mut visited, i);
            count += 1;

        }
        count
    }
}
*/
use std::collections::HashSet;
impl Solution {
    pub fn dfs(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, index: usize) {
        visited[index] = true;
        for &neighbor in graph[index].iter() {
            if visited[neighbor] {
                continue;
            }
            Self::dfs(graph, visited, neighbor);
        }
    }
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        for i in 0..n {
            for j in i + 1..n {
                if is_connected[i][j] == 1 {
                    graph[i].insert(j);
                    graph[j].insert(i);
                }
            }
        }
        let mut visited: Vec<bool> = vec![false; n];
        let mut res = 0;
        for i in 0..n{
            if !visited[i] {
                Self::dfs(&graph, &mut visited, i);
                res += 1;
            }
        }
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_547() {
        assert_eq!(Solution::find_circle_num(vec![vec![1,1,0],vec![1,1,0],vec![0,0,1]]), 2);
    }
}

```
