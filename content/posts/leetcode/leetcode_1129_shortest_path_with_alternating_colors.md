---
title: 1129. shortest path with alternating colors
date: '2022-07-08'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1129 shortest path with alternating colors
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1129}/>
 

  Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

  

  Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

  

  Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

  

   

 >   Example 1:

 >   Input: n <TeX>=</TeX> 3, red_edges <TeX>=</TeX> [[0,1],[1,2]], blue_edges <TeX>=</TeX> []

 >   Output: [0,1,-1]

 >   Example 2:

 >   Input: n <TeX>=</TeX> 3, red_edges <TeX>=</TeX> [[0,1]], blue_edges <TeX>=</TeX> [[2,1]]

 >   Output: [0,1,-1]

 >   Example 3:

 >   Input: n <TeX>=</TeX> 3, red_edges <TeX>=</TeX> [[1,0]], blue_edges <TeX>=</TeX> [[2,1]]

 >   Output: [0,-1,-1]

 >   Example 4:

 >   Input: n <TeX>=</TeX> 3, red_edges <TeX>=</TeX> [[0,1]], blue_edges <TeX>=</TeX> [[1,2]]

 >   Output: [0,1,2]

 >   Example 5:

 >   Input: n <TeX>=</TeX> 3, red_edges <TeX>=</TeX> [[0,1],[0,2]], blue_edges <TeX>=</TeX> [[1,0]]

 >   Output: [0,1,1]

  

   

  **Constraints:**

  

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 100

 >   	red_edges.length <TeX>\leq</TeX> 400

 >   	blue_edges.length <TeX>\leq</TeX> 400

 >   	red_edges[i].length <TeX>=</TeX><TeX>=</TeX> blue_edges[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> red_edges[i][j], blue_edges[i][j] < n


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::VecDeque;

impl Solution {
    pub fn build_graph(n: usize, edges: Vec<Vec<i32>>) -> Vec<Vec<usize>> {
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];
        for i in 0..edges.len() {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            graph[start].push(end);
        }
        graph
    }

    pub fn shortest_alternating_paths(n: i32, red_edges: Vec<Vec<i32>>, blue_edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let red_graph: Vec<Vec<usize>> = Self::build_graph(n, red_edges);
        let blue_graph: Vec<Vec<usize>> = Self::build_graph(n, blue_edges);
        println!("red: {:?}", red_graph);
        println!("blue: {:?}", blue_graph);
        let mut visited: Vec<u8> = vec![0; n];
        let mut q: VecDeque<(usize, usize, bool)> = VecDeque::new();
        q.push_back((0, 0, true)); //next one is red
        q.push_back((0, 0, false)); // next one is blue
        let mut result: Vec<i32> = vec![-1; n];
        while !q.is_empty() {
            let (index, steps, color) = q.pop_front().unwrap();
            println!("index: {}, steps: {}, color: {}", index, steps, color);
            if result[index] == -1 {
                result[index] = steps as i32;
            }
            if color {
                visited[index] = if visited[index] == 0 {1} else {3};
            } else {
                visited[index] = if visited[index] == 0 {2} else {3};
            }
            let neighbors = if color {&red_graph[index]} else {&blue_graph[index]};
            for i in 0..neighbors.len() {
                let neighbor = neighbors[i];
                let status = visited[neighbor];
                if color && (status == 2 || status == 3) {
                    continue;
                }
                if !color && (status == 1 || status == 3) {
                    continue;
                }
                q.push_back((neighbor, steps + 1, !color));
            }
        }
        result
    }
}
*/
const BITFLAG_BLUE: u8 = 1 << 0;
const BITFLAG_RED: u8 = 1 << 1;

impl Solution {
    pub fn shortest_alternating_paths(n: i32, red_edges: Vec<Vec<i32>>, blue_edges: Vec<Vec<i32>>) -> Vec<i32> {
    let n = n as usize;
    let mut red: Vec<Vec<usize>> = vec![vec![]; n];
    for edge in red_edges.into_iter() {
        red[edge[0] as usize].push(edge[1] as usize);
    }

    let mut blue: Vec<Vec<usize>> = vec![vec![]; n];
    for edge in blue_edges.into_iter() {
        blue[edge[0] as usize].push(edge[1] as usize);
    }

    let mut distances = vec![-1; n];
    let mut visted = vec![0; n];

    let mut queue = vec![];
    let mut next = vec![];
    let mut dist = 0;

    queue.push((0, BITFLAG_BLUE));
    queue.push((0, BITFLAG_RED));
    visted[0] = BITFLAG_BLUE | BITFLAG_RED;

    while !queue.is_empty() {
        while let Some((node, color)) = queue.pop() {
            if distances[node] < 0 {
                distances[node] = dist;
            }

            // If the current node is BLUE, the next one must be RED and vice-versa
            let (bitmask, graph) = if color == BITFLAG_BLUE {
                (BITFLAG_RED, &red)
            } else {
                (BITFLAG_BLUE, &blue)
            };

            for &n in graph[node].iter() {
                if visted[n] & bitmask == 0 {
                    visted[n] |= bitmask;
                    next.push((n, bitmask));
                }
            }
        }

        std::mem::swap(&mut queue, &mut next);
        dist += 1;
    }

    distances
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1129() {
        /*
        assert_eq!(Solution::shortest_alternating_paths(3, vec![vec![0,1],vec![1,2]], vec![]), vec![0,1,-1]);
        assert_eq!(Solution::shortest_alternating_paths(3, vec![vec![0,1]], vec![vec![2,1]]), vec![0,1,-1]);
        assert_eq!(Solution::shortest_alternating_paths(3, vec![vec![0,1], vec![0, 2]], vec![vec![1,0]]), vec![0,1,1]);
        assert_eq!(Solution::shortest_alternating_paths(5, 
            vec![vec![0,1],vec![1,2],vec![2,3],vec![3,4]], 
            vec![vec![1,2],vec![2,3],vec![3,1]]), vec![0,1,2,3,7]);
        */
        assert_eq!(Solution::shortest_alternating_paths(9, vec![vec![1,8],vec![5,7],vec![1,2],vec![2,2],vec![7,4],vec![7,2],vec![3,8],vec![7,0],vec![1,5],vec![2,7],vec![2,3],vec![6,3],vec![3,0],vec![4,8],vec![7,5],vec![1,6],vec![3,7]], vec![vec![2,1],vec![1,4],vec![0,3],vec![0,5],vec![1,5],vec![8,2],vec![5,8],vec![2,6],vec![5,3],vec![6,7],vec![4,0],vec![2,2]]), 
        vec![0,5,3,1,8,1,5,2,2]);
    }
}

```
