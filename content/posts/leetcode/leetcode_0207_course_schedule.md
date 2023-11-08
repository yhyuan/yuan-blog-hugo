---
title: 207. course schedule
date: '2021-10-24'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0207 course schedule
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={207}/>
 

  There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] <TeX>=</TeX> [ai, bi] indicates that you must take course bi first if you want to take course ai.

  

  	For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

  

  Return true if you can finish all courses. Otherwise, return false.

   

 >   Example 1:

  

 >   Input: numCourses <TeX>=</TeX> 2, prerequisites <TeX>=</TeX> [[1,0]]

 >   Output: true

 >   Explanation: There are a total of 2 courses to take. 

 >   To take course 1 you should have finished course 0. So it is possible.

  

 >   Example 2:

  

 >   Input: numCourses <TeX>=</TeX> 2, prerequisites <TeX>=</TeX> [[1,0],[0,1]]

 >   Output: false

 >   Explanation: There are a total of 2 courses to take. 

 >   To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> numCourses <TeX>\leq</TeX> 10^5

 >   	0 <TeX>\leq</TeX> prerequisites.length <TeX>\leq</TeX> 5000

 >   	prerequisites[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> ai, bi < numCourses

 >   	All the pairs prerequisites[i] are unique.


## Solution
Firstly, built a graph from this input. 

Secondly, run a DFS for the graph to detect cycle and get topological sorting.

### Python
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        graph = [[]] * numCourses
        for i in range(n):
            start = prerequisites[i][0] 
            end = prerequisites[i][1]
            graph[start] = graph[start] + [end]
        visited = [False] * (numCourses)
        on_stack = [False] * (numCourses)
        
        def hasCircle(index):
            visited[index] = True
            on_stack[index] = True
            for neighbor in graph[index]:
                if on_stack[neighbor]:
                    return True
                if visited[neighbor]:
                    continue
                if hasCircle(neighbor):
                    return True
            on_stack[index] = False
            return False
            
        for i in range(numCourses):
            if not visited[i]:
                if hasCircle(i):
                    return False
        return True
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashSet;
//use std::collections::VecDeque;
pub struct Graph {
    edges: Vec<HashSet<usize>>,
    has_cycle: bool,
    n: usize,
}

impl Graph {
    fn new(n: usize) -> Self {
        let edges: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        let has_cycle = false;
        Graph {edges, n, has_cycle}
    }

    fn insert_edge(&mut self, u: usize, v: usize) {
        self.edges[u].insert(v);
    }

    fn neighbors(&self, u: usize) -> HashSet<usize> {
        self.edges[u].clone()
    }
    pub fn dfs(&mut self, u: usize, marked: &mut Vec<bool>, 
        on_stack: &mut Vec<bool>//, pre: &mut VecDeque<usize>, 
        //post: &mut VecDeque<usize>, reverse_post: &mut Vec<usize>
        ) {
        //pre.push_back(u);
        marked[u] = true;
        on_stack[u] = true;
        for v in self.edges[u].clone() {
            if !marked[v] {
                self.dfs(v, marked, on_stack);
            } else if on_stack[v] {
                self.has_cycle = true;
            } 
        }
        on_stack[u] = false;
        //post.push_back(u);
        //reverse_post.push(u);
    }
    pub fn has_a_cycle(&mut self) -> bool {
        //let mut pre: VecDeque<usize> = VecDeque::new(); 
        //let mut post: VecDeque<usize> = VecDeque::new();
        //let mut reverse_post: Vec<usize> = vec![];
        let mut marked: Vec<bool> = vec![false; self.n];
        let mut on_stack: Vec<bool> = vec![false; self.n];
        for u in 0..self.n {
            if !marked[u] {
                self.dfs(u, &mut marked, &mut on_stack);
            }
        }
        //println!("reverse_post: {:?}", reverse_post);
        self.has_cycle
    }
}
impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let n = num_courses as usize;
        let mut graph = Graph::new(n);
        for prerequisite in prerequisites.iter() {
            let u = prerequisite[0] as usize;
            let v = prerequisite[1] as usize;
            graph.insert_edge(u, v);
        }
        !graph.has_a_cycle()
    }
}
*/
use std::collections::HashSet;
impl Solution {
    pub fn has_a_cycle(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, index: usize, on_stack: &mut Vec<bool>) -> bool {
        visited[index] = true;
        on_stack[index] = true;
        for &neighbor in graph[index].iter() {
            if on_stack[neighbor] {
                return true;
            }
            if visited[neighbor] {
                continue;
            }
            if Self::has_a_cycle(graph, visited, neighbor, on_stack) {
                return true;
            }
        }
        on_stack[index] = false;
        return false;
    }
    
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let n = num_courses as usize;
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        for i in 0..prerequisites.len() {
            let start = prerequisites[i][0] as usize;
            let end = prerequisites[i][1] as usize;
            graph[start].insert(end);
        }
        let mut visited: Vec<bool> = vec![false; n];
        let mut on_stack: Vec<bool> = vec![false; n];
        //let mut post_order: Vec<usize> = vec![];
        for i in 0..n {
            if !visited[i] {
                if Self::has_a_cycle(&graph, &mut visited, i, &mut on_stack) {
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
    fn test_207() {
        assert_eq!(Solution::can_finish(2, vec![vec![1, 0]]), true);
        assert_eq!(Solution::can_finish(2, vec![vec![1, 0], vec![0, 1]]), false);
        assert_eq!(
            Solution::can_finish(
                8,
                vec![
                    vec![1, 0],
                    vec![2, 6],
                    vec![1, 7],
                    vec![6, 4],
                    vec![7, 0],
                    vec![0, 5]
                ]
            ),
            true
        );
    }
}

```
