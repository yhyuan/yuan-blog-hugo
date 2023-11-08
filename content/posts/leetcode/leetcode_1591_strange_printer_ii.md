---
title: 1591. strange printer ii
date: '2022-08-17'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 1591 strange printer ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1591}/>
 

  There is a strange printer with the following two special requirements:

  

  	On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.

  	Once the printer has used a color for the above operation, the same color cannot be used again.

  

  You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.

  Return true if it is possible to print the matrix targetGrid, otherwise, return false.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/08/15/sample_1_1929.png)

  

 >   Input: targetGrid <TeX>=</TeX> [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]

 >   Output: true

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/08/15/sample_2_1929.png)

  

 >   Input: targetGrid <TeX>=</TeX> [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]

 >   Output: true

  

 >   Example 3:

  

 >   Input: targetGrid <TeX>=</TeX> [[1,2,1],[2,1,2],[1,2,1]]

 >   Output: false

 >   Explanation: It is impossible to form targetGrid because it is not allowed to print the same color in different turns.

 >   Example 4:

  

 >   Input: targetGrid <TeX>=</TeX> [[1,1,1],[3,1,3]]

 >   Output: false

  

   

  **Constraints:**

  

 >   	m <TeX>=</TeX><TeX>=</TeX> targetGrid.length

 >   	n <TeX>=</TeX><TeX>=</TeX> targetGrid[i].length

 >   	1 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 60

 >   	1 <TeX>\leq</TeX> targetGrid[row][col] <TeX>\leq</TeX> 60


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn is_printable(target_grid: Vec<Vec<i32>>) -> bool {
        let m = target_grid.len();
        let n = target_grid[0].len();
        let mut hashmap: HashMap<i32, (usize, usize, usize, usize)> = HashMap::new();
        let mut max_val = 0;
        for i in 0..m {
            for j in 0..n {
                //target_grid[i][j] = target_grid[]
                let val = target_grid[i][j];
                max_val = i32::max(max_val, val);
                if hashmap.contains_key(&val) {
                    let min_max_values = hashmap.get_mut(&target_grid[i][j]).unwrap();
                    *min_max_values = (
                        usize::min(min_max_values.0, i), usize::min(min_max_values.1, j), 
                        usize::max(min_max_values.2, i), usize::max(min_max_values.3, j), 
                    );
                } else {
                    hashmap.insert(val, (i, j, i, j));
                }
            }
        }
        let mut graph: Vec<HashSet<usize>> = vec![HashSet::new(); max_val as usize + 1];
        let nodes = hashmap.keys().collect::<Vec<_>>();
        //println!("hashmap: {:?}", hashmap);
        //println!("nodes: {:?}", nodes);
        for i in 0..nodes.len() {
            let (min_x_i, min_y_i, max_x_i, max_y_i) = hashmap.get(nodes[i]).unwrap();
            //println!("nodes[i]: {}, range: {:?}", nodes[i], (min_x_i, min_y_i, max_x_i, max_y_i));
            for j in i + 1..nodes.len() {
                let (min_x_j, min_y_j, max_x_j, max_y_j) = hashmap.get(nodes[j]).unwrap();
                let min_x = usize::max(*min_x_i, *min_x_j);
                let min_y = usize::max(*min_y_i, *min_y_j);
                let max_x = usize::min(*max_x_i, *max_x_j);
                let max_y = usize::min(*max_y_i, *max_y_j);
                for i1 in min_x..=max_x {
                    for j1 in min_y..=max_y {
                        if &target_grid[i1][j1] == nodes[i] {
                            graph[*nodes[j] as usize].insert(*nodes[i] as usize);
                        }
                        if &target_grid[i1][j1] == nodes[j] {
                            graph[*nodes[i] as usize].insert(*nodes[j] as usize);
                        }
                    }
                }                
                //println!("    nodes[j]: {}, range: {:?}", nodes[j], (min_x_j, min_y_j, max_x_j, max_y_j));
            }
        }
        //println!("graph: {:?}", graph);
        let n = graph.len();
        let mut visited = vec![false; n];
        let mut on_stack: Vec<bool> = vec![false; n];
        for i in 0..n {
            if !visited[i] {
                if Self::dfs(&graph, &mut visited, &mut on_stack, i) {
                    return false;
                }
            }
        }
        true
    }
    pub fn dfs(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, on_stack: &mut Vec<bool>, index: usize) -> bool {
        visited[index] = true;
        on_stack[index] = true;
        for &neighbor in graph[index].iter() {
            if on_stack[neighbor] {
                return true;
            }
            if visited[neighbor] {
                continue;
            }
            if Self::dfs(graph, visited, on_stack, neighbor) {
                return true;
            }
        }
        on_stack[index] = false;
        false
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1591() {
        assert_eq!(Solution::is_printable(vec![vec![1,1,1,1],vec![1,2,2,1],vec![1,2,2,1],vec![1,1,1,1]]), true);
        assert_eq!(Solution::is_printable(vec![vec![1,1,1,1],vec![1,1,3,3],vec![1,1,3,4],vec![5,5,1,4]]), true);
        assert_eq!(Solution::is_printable(vec![vec![1,2,1],vec![2,1,2],vec![1,2,1]]), false);
    }
}

```
