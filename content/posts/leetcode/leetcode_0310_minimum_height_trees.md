---
title: 310. minimum height trees
date: '2022-01-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0310 minimum height trees
---

 

  A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

  Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] <TeX>=</TeX> [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

  Return a list of all MHTs' root labels. You can return the answer in any order.

  The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/09/01/e1.jpg)

 >   Input: n <TeX>=</TeX> 4, edges <TeX>=</TeX> [[1,0],[1,2],[1,3]]

 >   Output: [1]

 >   Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/09/01/e2.jpg)

 >   Input: n <TeX>=</TeX> 6, edges <TeX>=</TeX> [[3,0],[3,1],[3,2],[3,4],[5,4]]

 >   Output: [3,4]

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 1, edges <TeX>=</TeX> []

 >   Output: [0]

  

 >   Example 4:

  

 >   Input: n <TeX>=</TeX> 2, edges <TeX>=</TeX> [[0,1]]

 >   Output: [0,1]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2  10^4

 >   	edges.length <TeX>=</TeX><TeX>=</TeX> n - 1

 >   	0 <TeX>\leq</TeX> ai, bi < n

 >   	ai !<TeX>=</TeX> bi

 >   	All the pairs (ai, bi) are distinct.

 >   	The given input is guaranteed to be a tree and there will be no repeated edges.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::{HashSet, HashMap};

impl Solution {
    /* 
    pub fn find_tree_height(matrix: &Vec<Vec<bool>>, path: &mut Vec<usize>) -> i32 {
        let n = matrix.len();
        let i = path[path.len() - 1];
        let neighbors: Vec<usize> = (0..n).filter(|&j| matrix[i][j] && !path.contains(&j)).collect();
        if neighbors.len() == 0 {
            return path.len() as i32;
        }
        let mut max_len = i32::MIN;
        for neighbor in neighbors {
            path.push(neighbor);
            let height = Solution::find_tree_height(matrix, path);
            max_len = i32::max(max_len, height);
            path.pop();
        }
        max_len
    }
    pub fn calculate_connectivity_matrix(n: usize, edges: &Vec<Vec<i32>>) -> Vec<Vec<bool>>{
        let mut matrix: Vec<Vec<bool>> = Vec::with_capacity(n);
        for _ in 0..n {
            matrix.push(vec![false; n]);
        }
        for i in 0..edges.len() {
            let coor = &edges[i];
            let x = coor[0] as usize;
            let y = coor[1] as usize;
            matrix[x][y] = true;
            matrix[y][x] = true;
        }
        matrix
    }
    pub fn find_min_height_trees(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let matrix = Solution::calculate_connectivity_matrix(n, &edges);
        let mut height_hashmap: HashMap<usize, i32> = HashMap::with_capacity(n);
        let mut min_height = i32::MAX;
        for i in 0..n {
            let mut path: Vec<usize> = vec![];
            path.push(i);
            let height = Solution::find_tree_height(&matrix,&mut path);
            min_height = i32::min(min_height, height);
            height_hashmap.insert(i, height);
        }
        let mut results: Vec<i32> = vec![];
        for (&key, &value) in height_hashmap.iter() {
            if value == min_height {
                results.push(key as i32);
            }
        }
        results.sort();
        results
    }
    */
    /*
    pub fn build_adjacency_list(n: i32, edges: &Vec<Vec<i32>>) -> HashMap<usize, Vec<usize>> {
        let n = n as usize;
        let mut adjacency_list: HashMap<usize, Vec<usize>> = HashMap::with_capacity(n as usize);
        for coor in edges.iter() {
            let x = coor[0] as usize;
            let y = coor[1] as usize;
            if adjacency_list.contains_key(&x) {
                let mut indices = adjacency_list[&x].clone();
                indices.push(y);
                adjacency_list.insert(x, indices);
            } else {
                adjacency_list.insert(x, vec![y]);
            }
            if adjacency_list.contains_key(&y) {
                let mut indices = adjacency_list[&y].clone();
                indices.push(x);
                adjacency_list.insert(y, indices);
            } else {
                adjacency_list.insert(y, vec![x]);
            }           
        }
        adjacency_list
    }
    pub fn find_min_height_trees(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        if n == 1 {
            return vec![0i32];
        }
        let mut adjacency_list = Solution::build_adjacency_list(n, &edges);
        //println!("adjacency_list: {:?}", adjacency_list);
        while adjacency_list.len() > 2 {
            let mut remove_keys: Vec<usize> = vec![];            
            for (&key, value) in adjacency_list.iter() {
                if value.len() == 1 {
                    remove_keys.push(key);
                }
            }
            adjacency_list.retain(|key, value| {
                value.len() > 1
            });
            for (&key, values) in adjacency_list.iter_mut() {
                values.retain(|x| !remove_keys.contains(x));
            }
        }
        let mut results: Vec<i32> = adjacency_list.keys().map(|&i| i as i32).collect();
        results.sort();
        results
    }
    */
    pub fn find_min_height_trees(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        if n == 1 && edges.len() == 0 {
            return vec![0];
        }
        let mut graph: HashMap<usize, HashSet<usize>> = HashMap::new();
        for i in 0..edges.len() {
            let start = edges[i][0] as usize;
            let end = edges[i][1] as usize;
            if graph.contains_key(&start) {
                graph.get_mut(&start).unwrap().insert(end);
            } else {
                let mut hashset: HashSet<usize> = HashSet::new();
                hashset.insert(end);
                graph.insert(start, hashset);
            }

            if graph.contains_key(&end) {
                graph.get_mut(&end).unwrap().insert(start);
            } else {
                let mut hashset: HashSet<usize> = HashSet::new();
                hashset.insert(start);
                graph.insert(end, hashset);
            }
        }
        //println!("graph: {:?}", graph);
        //let mut one_degree_nodes = Self::find_one_degree_nodes(&graph);
        let mut one_degree_nodes: HashSet<usize> = HashSet::new();
        for (&key, value) in graph.iter() {
            if value.len() == 1 {
                one_degree_nodes.insert(key);
            }
        }
        while graph.len() > 2 {
            let mut next_one_degree_nodes: HashSet<usize> = HashSet::new();
            for key in one_degree_nodes.iter() {
                let neighbor = *graph[key].iter().next().unwrap();
                let values = graph.get_mut(&neighbor).unwrap();
                values.remove(key);
                if values.len() == 1 {
                    next_one_degree_nodes.insert(neighbor);
                }
            }
            for key in one_degree_nodes.iter() {
                graph.remove(key);
            }
            one_degree_nodes = next_one_degree_nodes;
        }
        let result = graph.keys().cloned().map(|x| x as i32).collect::<Vec<_>>();
        //println!("graph: {:?}", graph);
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_310() {
        assert_eq!(
            Solution::find_min_height_trees(4, vec![vec![1, 0], vec![1, 2], vec![1, 3]]),
            vec![1]
        );
        assert_eq!(
            Solution::find_min_height_trees(
                6,
                vec![vec![0, 3], vec![1, 3], vec![2, 3], vec![4, 3], vec![5, 4]]
            ),
            vec![3, 4]
        );
        assert_eq!(Solution::find_min_height_trees(1, vec![]), vec![0]);
        
    }
}

```
