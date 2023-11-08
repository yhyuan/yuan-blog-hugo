---
title: 1136. parallel courses
date: '2022-07-11'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1136 parallel courses
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1136}/>

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] <TeX>=</TeX> [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.



In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.



Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.



 



 > Example 1:





 > Input: n <TeX>=</TeX> 3, relations <TeX>=</TeX> [[1,3],[2,3]]

 > Output: 2

 > Explanation: The figure above represents the given graph.

 > In the first semester, you can take courses 1 and 2.

 > In the second semester, you can take course 3.

 > Example 2:





 > Input: n <TeX>=</TeX> 3, relations <TeX>=</TeX> [[1,2],[2,3],[3,1]]

 > Output: -1

 > Explanation: No course can be studied because they are prerequisites of each other.

 



**Constraints:**



 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 5000

 > 1 <TeX>\leq</TeX> relations.length <TeX>\leq</TeX> 5000

 > relations[i].length <TeX>=</TeX><TeX>=</TeX> 2

 > 1 <TeX>\leq</TeX> prevCoursei, nextCoursei <TeX>\leq</TeX> n

 > prevCoursei !<TeX>=</TeX> nextCoursei

 > All the pairs [prevCoursei, nextCoursei] are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
use std::collections::VecDeque;

impl Solution {
    pub fn dfs(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, on_stack: &mut Vec<bool>, post_order: &mut Vec<usize>, index: usize) -> bool {
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
        post_order.push(index);
        false
    }
    pub fn minimum_semesters(n: i32, relations: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        let mut reverse_graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        let mut in_degrees: Vec<usize> = vec![0; n];
        for i in 0..relations.len() {
            let start = relations[i][0] as usize - 1;
            let end   = relations[i][1] as usize - 1;
            in_degrees[end] += 1;
            graph[start].insert(end);
            reverse_graph[end].insert(start);
        }
        /*
        println!("graph: {:?}", graph);
        for i in 0..n {
            let mut neighbors = graph[i].iter().collect::<Vec<_>>();
            neighbors.sort();
            println!("i: {}, neighbors: {:?}", i, neighbors);
        }
        */
        let mut visited = vec![false; n];
        let mut on_stack = vec![false; n];
        let mut post_order: Vec<usize> = vec![];
        for i in 0..n {
            if !visited[i] {
                if Self::dfs(&graph, &mut visited, &mut on_stack, &mut post_order, i) {
                    return -1;
                }
            }
        }

        let mut taken = vec![false; n];
        let mut step = 0;
        loop {
            let mut is_changed = false;
            let indices = (0..n).into_iter().filter(|&i| !taken[i] && in_degrees[i] == 0).collect::<Vec<_>>();
            for &index in indices.iter() {
                for &next in graph[index].iter() {
                    if in_degrees[next] > 0 {
                        in_degrees[next] -= 1;
                        is_changed = true;
                    }
                }
                taken[index] = true;
            }
            step += 1;
            if !is_changed {
                break;
            }
        }
        step
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1136() {
        assert_eq!(Solution::minimum_semesters(25, 
            vec![vec![5,10],vec![11,14],vec![21,22],vec![16,19],vec![21,25],vec![6,18],vec![1,9],vec![4,7],vec![10,23],vec![5,14],vec![9,18],vec![18,21],vec![11,22],vec![1,15],vec![1,2],vec![5,18],vec![7,20],vec![2,23],vec![12,13],vec![9,14],vec![10,16],vec![11,21],vec![5,12],vec![2,24],vec![8,17],vec![15,17],vec![10,13],vec![11,16],vec![20,22],vec![7,11],vec![9,15],vec![16,22],vec![18,20],vec![19,22],vec![10,18],vec![3,20],vec![16,25],vec![10,15],vec![1,23],vec![13,16],vec![23,25],vec![1,8],vec![4,10],vec![19,24],vec![11,20],vec![3,18],vec![6,25],vec![11,13],vec![13,15],vec![22,24],vec![6,24],vec![17,20],vec![2,25],vec![15,24],vec![8,21],vec![14,16],vec![5,16],vec![19,23],vec![1,5],vec![4,22],vec![19,20],vec![12,15],vec![16,18],vec![9,13],vec![13,22],vec![14,22],vec![2,8],vec![3,13],vec![9,23],vec![14,15],vec![14,17],vec![8,20],vec![9,17],vec![3,19],vec![8,25],vec![2,12],vec![7,24],vec![19,25],vec![1,13],vec![6,11],vec![14,21],vec![7,15],vec![3,14],vec![15,23],vec![10,17],vec![4,20],vec![6,14],vec![10,21],vec![2,13],vec![3,21],vec![8,11],vec![5,21],vec![6,23],vec![17,25],vec![16,21],vec![12,22],vec![1,16],vec![6,19],vec![7,25],vec![3,23],vec![11,25],vec![3,10],vec![6,7],vec![2,3],vec![5,25],vec![1,6],vec![4,17],vec![2,16],vec![13,17],vec![17,22],vec![6,13],vec![5,6],vec![4,11],vec![4,23],vec![4,8],vec![12,23],vec![7,21],vec![5,20],vec![3,24],vec![2,10],vec![13,14],vec![11,24],vec![1,3],vec![2,7],vec![7,23],vec![6,17],vec![5,17],vec![16,17],vec![8,15],vec![8,23],vec![7,17],vec![14,18],vec![16,23],vec![23,24],vec![4,12],vec![17,19],vec![5,9],vec![10,11],vec![5,23],vec![2,9],vec![1,19],vec![2,19],vec![12,20],vec![2,14],vec![11,12],vec![1,12],vec![13,23],vec![4,9],vec![7,13],vec![15,20],vec![21,24],vec![8,18],vec![9,11],vec![8,19],vec![6,22],vec![16,20],vec![22,25],vec![20,21],vec![6,16],vec![3,17],vec![1,22],vec![9,22],vec![20,24],vec![2,6],vec![9,16],vec![2,4],vec![2,20],vec![20,25],vec![9,10],vec![3,11],vec![15,18],vec![1,20],vec![3,6],vec![8,14],vec![10,22],vec![12,21],vec![7,8],vec![8,16],vec![9,20],vec![3,8],vec![15,21],vec![17,21],vec![11,18],vec![13,24],vec![17,24],vec![6,20],vec![4,15],vec![6,15],vec![3,22],vec![13,21],vec![2,22],vec![13,25],vec![9,12],vec![4,19],vec![1,24],vec![12,19],vec![5,8],vec![1,7],vec![3,16],vec![3,5],vec![12,24],vec![3,12],vec![2,17],vec![18,22],vec![4,25],vec![8,24],vec![15,19],vec![18,23],vec![1,4],vec![1,21],vec![10,24],vec![20,23],vec![4,14],vec![16,24],vec![10,20],vec![18,24],vec![1,14],vec![12,14],vec![10,12],vec![4,16],vec![5,19],vec![4,5],vec![19,21],vec![15,25],vec![1,18],vec![2,21],vec![4,24],vec![7,14],vec![4,6],vec![15,16],vec![3,7],vec![21,23],vec![1,17],vec![12,16],vec![13,18],vec![5,7],vec![9,19],vec![2,15],vec![22,23],vec![7,19],vec![17,23],vec![8,22],vec![11,17],vec![7,16],vec![8,9],vec![6,21],vec![4,21],vec![4,13],vec![14,24],vec![3,4],vec![7,18],vec![11,15],vec![5,11],vec![12,17],vec![6,9],vec![1,25],vec![12,18],vec![6,12],vec![8,10],vec![6,8],vec![11,23],vec![7,10],vec![14,25],vec![14,23],vec![12,25],vec![5,24],vec![10,19],vec![3,25],vec![7,9],vec![8,12],vec![5,22],vec![24,25],vec![13,19],vec![3,15],vec![5,15],vec![15,22],vec![10,14],vec![3,9],vec![13,20],vec![1,10],vec![9,21],vec![10,25],vec![9,24],vec![14,20],vec![9,25],vec![8,13],vec![7,12],vec![5,13],vec![6,10],vec![2,5],vec![2,18],vec![14,19],vec![1,11],vec![7,22],vec![18,25],vec![11,19],vec![18,19],vec![4,18],vec![17,18],vec![2,11]]
        ), 25);
        assert_eq!(Solution::minimum_semesters(3, vec![vec![1,3],vec![2,3]]), 2);
        assert_eq!(Solution::minimum_semesters(3, vec![vec![1,2], vec![3,1],vec![2,3]]), -1);
    }
}

```
