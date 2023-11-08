---
title: 210. course schedule ii
date: '2021-10-27'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0210 course schedule ii
---

 

  There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] <TeX>=</TeX> [ai, bi] indicates that you must take course bi first if you want to take course ai.

  

  	For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

  

  Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

   

 >   Example 1:

  

 >   Input: numCourses <TeX>=</TeX> 2, prerequisites <TeX>=</TeX> [[1,0]]

 >   Output: [0,1]

 >   Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

  

 >   Example 2:

  

 >   Input: numCourses <TeX>=</TeX> 4, prerequisites <TeX>=</TeX> [[1,0],[2,0],[3,1],[3,2]]

 >   Output: [0,2,1,3]

 >   Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.

 >   So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

  

 >   Example 3:

  

 >   Input: numCourses <TeX>=</TeX> 1, prerequisites <TeX>=</TeX> []

 >   Output: [0]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> numCourses <TeX>\leq</TeX> 2000

 >   	0 <TeX>\leq</TeX> prerequisites.length <TeX>\leq</TeX> numCourses  (numCourses - 1)

 >   	prerequisites[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> ai, bi < numCourses

 >   	ai !<TeX>=</TeX> bi

 >   	All the pairs [ai, bi] are distinct.


## Solution
DFS to search topological sorting. 
### Python
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[]] * numCourses
        n = len(prerequisites)
        for i in range(n):
            start = prerequisites[i][0]
            end = prerequisites[i][1]
            graph[end] = graph[end] + [start]
        #print(graph)
        visited = [False] * numCourses
        on_stack = [False] * numCourses
        post_order = []
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
            post_order.append(index)
            return False
        #print(post_order)
        for i in range(numCourses):
            if visited[i]:
                continue
            if hasCircle(i):
                return []
        #print(post_order)
        post_order.reverse()
        return post_order
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
        on_stack: &mut Vec<bool>, /*pre: &mut VecDeque<usize>, 
        post: &mut VecDeque<usize>, */ reverse_post: &mut Vec<usize>) {
        //pre.push_back(u);
        marked[u] = true;
        on_stack[u] = true;
        for v in self.edges[u].clone() {
            if !marked[v] {
                self.dfs(v, marked, on_stack, reverse_post);
            } else if on_stack[v] {
                self.has_cycle = true;
            } 
        }
        on_stack[u] = false;
        //post.push_back(u);
        reverse_post.push(u);
    }
    pub fn topological_sort(&mut self) -> Vec<usize> {
        //let mut pre: VecDeque<usize> = VecDeque::new(); 
        //let mut post: VecDeque<usize> = VecDeque::new();
        let mut reverse_post: Vec<usize> = vec![];
        let mut marked: Vec<bool> = vec![false; self.n];
        let mut on_stack: Vec<bool> = vec![false; self.n];
        for u in 0..self.n {
            if !marked[u] {
                self.dfs(u, &mut marked, &mut on_stack, &mut reverse_post);
            }
        }
        //println!("reverse_post: {:?}", reverse_post);
        if self.has_cycle {
            return vec![];
        }
        reverse_post
    }
}
impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let n = num_courses as usize;
        let mut graph = Graph::new(n);
        for prerequisite in prerequisites.iter() {
            let u = prerequisite[0] as usize;
            let v = prerequisite[1] as usize;
            graph.insert_edge(u, v);
        }
        graph.topological_sort().iter().map(|&v| v as i32).collect::<Vec<i32>>()
    }
}
*/
use std::collections::HashSet;
impl Solution {
    pub fn dfs(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, on_stack: &mut Vec<bool>, post_order: &mut Vec<i32>, index: usize) -> bool {
        visited[index] = true;
        on_stack[index] = true;
        for &neighbor in graph[index].iter() {
            if on_stack[neighbor] {
                return true;
            }
            if visited[neighbor] {
                continue;
            }
            if Self::dfs(graph, visited, on_stack, post_order, neighbor) {
                return true;
            }
        }
        on_stack[index] = false;
        post_order.push(index as i32);
        false
    }
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let n = num_courses as usize;
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        for i in 0..prerequisites.len() {
            let start = prerequisites[i][0] as usize;
            let end   = prerequisites[i][1] as usize;
            graph[start].insert(end);
        }
        let mut visited = vec![false; n];
        let mut on_stack = vec![false; n];
        let mut post_order: Vec<i32> = vec![];
        for i in 0..n {
            if !visited[i] {
                if Self::dfs(&graph, &mut visited, &mut on_stack, &mut post_order, i) {
                    return vec![];
                }
            }
        }
        post_order
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_210() {
        assert_eq!(Solution::find_order(2, vec![vec![1,0]]), vec![0,1]);
        assert_eq!(Solution::find_order(4, vec![vec![1,0],vec![2,0],vec![3,1],vec![3,2]]), vec![0,1,2,3]);
    }
}

```
