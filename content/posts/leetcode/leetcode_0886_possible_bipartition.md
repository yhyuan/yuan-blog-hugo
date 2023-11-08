---
title: 886. possible bipartition
date: '2022-06-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0886 possible bipartition
---

 

  We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

  Given the integer n and the array dislikes where dislikes[i] <TeX>=</TeX> [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 4, dislikes <TeX>=</TeX> [[1,2],[1,3],[2,4]]

 >   Output: true

 >   Explanation: group1 [1,4] and group2 [2,3].

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 3, dislikes <TeX>=</TeX> [[1,2],[1,3],[2,3]]

 >   Output: false

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 5, dislikes <TeX>=</TeX> [[1,2],[2,3],[3,4],[4,5],[1,5]]

 >   Output: false

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2000

 >   	0 <TeX>\leq</TeX> dislikes.length <TeX>\leq</TeX> 10^4

 >   	dislikes[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	1 <TeX>\leq</TeX> dislikes[i][j] <TeX>\leq</TeX> n

 >   	ai < bi

 >   	All the pairs of dislikes are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn dfs(graph: &Vec<Vec<usize>>, visited: &mut Vec<i8>, index: usize, color: bool) -> bool {
        visited[index] = if color {0} else {1};
        let neighbors = &graph[index];
        for i in 0..neighbors.len() {
            let neighbor = neighbors[i];
            if visited[neighbor] >= 0 && visited[neighbor] == visited[index] {
                return false;
            }
            if visited[neighbor] >= 0 {
                continue;
            }
            let r = Self::dfs(graph, visited, neighbor, !color);
            if !r {
                return false;
            }
        }
        true
    }
    pub fn possible_bipartition(n: i32, dislikes: Vec<Vec<i32>>) -> bool {
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        for i in 0..dislikes.len() {
            let start = dislikes[i][0] as usize - 1;
            let end = dislikes[i][1] as usize - 1;
            graph[start].push(end);
            graph[end].push(start);
        }
        let mut visited: Vec<i8> = vec![-1;n];
        //let mut result = true;
        for i in 0..n {
            if visited[i] < 0 {
                if !Self::dfs(&graph, &mut visited, i, true) {
                    return false;
                }
            }
        }
        true
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_886() {
        assert_eq!(Solution::possible_bipartition(5, vec![vec![1,2],vec![3,4],vec![4,5],vec![3,5]]), false);
        //assert_eq!(Solution::possible_bipartition(4, vec![vec![1,2],vec![1,3],vec![2,4]]), true);
        //assert_eq!(Solution::possible_bipartition(3, vec![vec![1,2],vec![1,3],vec![2,3]]), false);
        //assert_eq!(Solution::possible_bipartition(5, vec![vec![1,2],vec![2,3],vec![3,4],vec![4,5],vec![1,5]]), false)
    }
}

```
