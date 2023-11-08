---
title: 2242. maximum score of a node sequence
date: '2022-09-28'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2242 maximum score of a node sequence
---


There is an undirected graph with n nodes, numbered from 0 to n - 1.



You are given a 0-indexed integer array scores of length n where scores[i] denotes the score of node i. You are also given a 2D integer array edges where edges[i] <TeX>=</TeX> [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.



A node sequence is valid if it meets the following conditions:



There is an edge connecting every pair of adjacent nodes in the sequence.

No node appears more than once in the sequence.

The score of a node sequence is defined as the sum of the scores of the nodes in the sequence.



Return the maximum score of a valid node sequence with a length of 4. If no such sequence exists, return -1.



 



 > Example 1:





 > Input: scores <TeX>=</TeX> [5,2,9,8,4], edges <TeX>=</TeX> [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]

 > Output: 24

 > Explanation: The figure above shows the graph and the chosen node sequence [0,1,2,3].

 > The score of the node sequence is 5 + 2 + 9 + 8 <TeX>=</TeX> 24.

 > It can be shown that no other node sequence has a score of more than 24.

 > Note that the sequences [3,1,2,0] and [1,0,2,3] are also valid and have a score of 24.

 > The sequence [0,3,2,4] is not valid since no edge connects nodes 0 and 3.

 > Example 2:





 > Input: scores <TeX>=</TeX> [9,20,6,4,11,12], edges <TeX>=</TeX> [[0,3],[5,3],[2,4],[1,3]]

 > Output: -1

 > Explanation: The figure above shows the graph.

 > There are no valid node sequences of length 4, so we return -1.

 



**Constraints:**



 > n <TeX>=</TeX><TeX>=</TeX> scores.length

 > 4 <TeX>\leq</TeX> n <TeX>\leq</TeX> 5  104

 > 1 <TeX>\leq</TeX> scores[i] <TeX>\leq</TeX> 108

 > 0 <TeX>\leq</TeX> edges.length <TeX>\leq</TeX> 5  104

 > edges[i].length <TeX>=</TeX><TeX>=</TeX> 2

 > 0 <TeX>\leq</TeX> ai, bi <TeX>\leq</TeX> n - 1

 > ai !<TeX>=</TeX> bi

 > There are no duplicate edges.


## Solution
### Rust
```rust
pub struct Solution {}
use std::collections::HashSet;
/*
    We do not need to computer all neighbors. We just need to computer the top K neighbors. 
    K must >= 3 but, why? Consider an edge (a, b)
    Assume b's largest neighbor is d, and d != a.
    K = 1. The largest neighbor of a may be b, => we get [b, a, b, d]. We will need to consider the seoncd largest neighbor.
    K = 2  The largest neighbors of a may be [b, d] => we will get [b/d, a, b, d]. We ill need to consier the third largest neighbor.
    K = 3  The largest neighbors of a may be [b, c, d] => We ill get [b/c/d, a, b, d]. It is guarranteed to find a valid one. 
*/
impl Solution {
    pub fn maximum_score(scores: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = scores.len();
        let mut graph: Vec<Vec<(i32, usize)>> = vec![];
        for i in 0..n {
            graph.push(vec![]);
        }
        let m = edges.len();
        for i in 0..m {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            graph[start].push((-scores[end], end));
            graph[end].push((-scores[start], start));
        }
        for i in 0..n {
            graph[i].sort();
        }
        let mut ans = i32::MIN;
        for i in 0..m {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            let max_count_start = usize::min(3, graph[start].len());
            let max_count_end = usize::min(3, graph[end].len());
            for j in 0..max_count_start {
                let node_1 = graph[start][j].1;
                for k in 0..max_count_end {
                    let node_2 = graph[end][k].1;
                    let mut set: HashSet<usize> = HashSet::new();
                    set.insert(start);
                    set.insert(end);
                    set.insert(node_1);
                    set.insert(node_2);
                    if set.len() == 4 {
                        let score = (scores[start] + scores[end] + scores[node_1] + scores[node_2]);
                        ans = i32::max(ans, score);
                    }
                }
            }
        }
        if ans == i32::MIN {
            return -1;
        }
        ans
        /*
        let mut dp: HashSet<(usize, usize)> = HashSet::new();
        for i in 0..n {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            dp.insert((start, end));
            // dp.insert((end, start));
        }

        let mut next_dp: HashSet<(usize, usize, usize)> = HashSet::new();
        for &(start, end) in dp.iter() {
            for &neighbor in graph[start].iter() {
                if neighbor != end {
                    next_dp.insert((neighbor, start, end));
                }
            }
            for &neighbor in graph[end].iter() {
                if neighbor != start {
                    next_dp.insert((start, end, neighbor));
                }
            }
        }
        let dp = next_dp;
        let mut next_dp: HashSet<(usize, usize, usize, usize)> = HashSet::new();
        for &(start, middle, end) in dp.iter() {
            for &neighbor in graph[start].iter() {
                if neighbor != end && neighbor != middle {
                    next_dp.insert((neighbor, start, middle, end));
                }
            }
            for &neighbor in graph[end].iter() {
                if neighbor != start && neighbor != middle {
                    next_dp.insert((start, middle, end, neighbor));
                }
            }
        }
        if next_dp.len() == 0 {
            return -1;
        }
        //println!("next_dp: {:?}", next_dp);
        let mut ans = i32::MIN;
        for &(s1, s2, s3, s4) in next_dp.iter() {
            let score = scores[s1] + scores[s2] + scores[s3] + scores[s4];
            ans = i32::max(ans, score);
        }
        ans
        */
        // 2 nodes
        /*
        let mut dp: Vec<(HashSet<usize>, i32, (usize, usize))> = vec![];
        // let mut ans = 0;
        for i in 0..n {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            let score = scores[start] + scores[end];
            // ans = i32::max(ans, score);
            let mut hashset: HashSet<usize> = HashSet::new();
            hashset.insert(start);
            hashset.insert(end);
            dp.push((hashset, score, (start, end)));
        }
        // println!("dp:{:?}", dp);
        // 3 and 4 nodes.
        for _ in 3..=4 {
            // println!("dp:{:?}", dp);
            let mut next_dp: Vec<(HashSet<usize>, i32, (usize, usize))> = vec![];
            for i in 0..dp.len() {
                let (_, score, (start, end)) = dp[i];
                for &neighbor in graph[start].iter() {
                    if dp[i].0.contains(&neighbor) {
                        continue;
                    }
                    let mut hashset = dp[i].0.clone();
                    hashset.insert(neighbor);
                    // ans = i32::max(ans, score + scores[neighbor]);
                    next_dp.push((hashset, score + scores[neighbor], (neighbor, end)));
                }
                for &neighbor in graph[end].iter() {
                    if dp[i].0.contains(&neighbor) {
                        continue;
                    }
                    let mut hashset = dp[i].0.clone();
                    hashset.insert(neighbor);
                    // ans = i32::max(ans, score + scores[neighbor]);
                    next_dp.push((hashset, score + scores[neighbor], (start, neighbor)));
                }
            }
            dp = next_dp;
        }
        if dp.len() == 0 {
            return -1;
        }
        let ans = dp.iter().map(|item| item.1).max().unwrap();
        ans
        */
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2242() {
        assert_eq!(Solution::maximum_score(vec![5,2,9,8,4], vec![vec![0,1],vec![1,2],vec![2,3],vec![0,2],vec![1,3],vec![2,4]]), 24);
        assert_eq!(Solution::maximum_score(vec![9,20,6,4,11,12], vec![vec![0,3],vec![5,3],vec![2,4],vec![1,3]]), -1);
    }
}



```
