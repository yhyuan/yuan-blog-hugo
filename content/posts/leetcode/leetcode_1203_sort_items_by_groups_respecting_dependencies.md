---
title: 1203. sort items by groups respecting dependencies
date: '2022-07-20'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1203 sort items by groups respecting dependencies
---

 

  There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

  Return a sorted list of the items such that:

  

  	The items that belong to the same group are next to each other in the sorted list.

  	There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).

  

  Return any solution if there is more than one solution and return an empty list if there is no solution.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2019/09/11/1359_ex1.png)

  

 >   Input: n <TeX>=</TeX> 8, m <TeX>=</TeX> 2, group <TeX>=</TeX> [-1,-1,1,0,0,1,0,-1], beforeItems <TeX>=</TeX> [[],[6],[5],[6],[3,6],[],[],[]]

 >   Output: [6,3,4,1,5,2,0,7]

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 8, m <TeX>=</TeX> 2, group <TeX>=</TeX> [-1,-1,1,0,0,1,0,-1], beforeItems <TeX>=</TeX> [[],[6],[5],[6],[3],[],[4],[]]

 >   Output: []

 >   Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> m <TeX>\leq</TeX> n <TeX>\leq</TeX> 3  10^4

 >   	group.length <TeX>=</TeX><TeX>=</TeX> beforeItems.length <TeX>=</TeX><TeX>=</TeX> n

 >   	-1 <TeX>\leq</TeX> group[i] <TeX>\leq</TeX> m - 1

 >   	0 <TeX>\leq</TeX> beforeItems[i].length <TeX>\leq</TeX> n - 1

 >   	0 <TeX>\leq</TeX> beforeItems[i][j] <TeX>\leq</TeX> n - 1

 >   	i !<TeX>=</TeX> beforeItems[i][j]

 >   	beforeItems[i] does not contain duplicates elements.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn dfs(graph: &Vec<HashSet<usize>>, visited: &mut Vec<bool>, on_stack: &mut Vec<bool>, postorder: &mut Vec<usize>, index: usize) -> bool {
        visited[index] = true;
        on_stack[index] = true;
        for &neighbor in graph[index].iter() {
            if on_stack[neighbor] {
                return true;
            }
            if visited[neighbor] {
                continue;
            }
            if Self::dfs(graph, visited, on_stack, postorder, neighbor) {
                return true;
            }
        }
        on_stack[index] = false;
        postorder.push(index);
        false
    }
    pub fn topological_sort(graph: &Vec<HashSet<usize>>)->Vec<usize> {
        let m = graph.len();
        let mut visited = vec![false; m];
        let mut on_stack = vec![false; m];
        let mut post_order: Vec<usize> = vec![];
        for i in 0..m {
            if !visited[i] {
                if Self::dfs(&graph, &mut visited, &mut on_stack, &mut post_order, i) {
                    return vec![];
                }
            }
        }
        post_order.reverse();
        post_order
    }
    pub fn sort_items(n: i32, m: i32, group: Vec<i32>, before_items: Vec<Vec<i32>>) -> Vec<i32> {
        let mut group = group;
        let mut m = m as usize;
        for i in 0..group.len() {
            if group[i] == -1 {
                group[i] = m as i32;
                m += 1;
            }
        }
        let n = n as usize;
        // let m = m as usize;
        let mut group_graph: Vec<HashSet<usize>> = vec![HashSet::new(); m];
        let mut item_graph: Vec<HashSet<usize>> = vec![HashSet::new(); n];
        let mut group_in_degree = vec![0; m];
        let mut item_in_degree = vec![0; n];

        for i in 0..n {
            let to_group = group[i] as usize;
            for &j in before_items[i].iter() {
                let from_group = group[j as usize] as usize;
                if from_group != to_group && !group_graph[from_group].contains(&to_group) {
                    group_graph[from_group].insert(to_group);
                    //group_in_degree[to_group] += 1;
                }
                if !item_graph[j as usize].contains(&i) {
                    item_graph[j as usize].insert(i);
                    //item_in_degree[i] += 1;
                }
            }
        }
        //println!("{:?}", group_graph);
        let group_sorted = Self::topological_sort(&group_graph);
        //println!("group_sorted: {:?}", group_sorted);
        let item_sorted = Self::topological_sort(&item_graph);
        //println!("item_sorted: {:?}", item_sorted);
        if group_sorted.len() == 0 || item_sorted.len() == 0 {
            return vec![];
        }
        let mut groups: Vec<Vec<usize>> = vec![vec![]; m];
        for i in item_sorted {
            let group_id = group[i] as usize;
            groups[group_id].push(i);            
        }
        let mut res: Vec<i32> = vec![];
        for group in group_sorted {
            for &j in groups[group].iter() {
                res.push(j as i32);
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
    fn test_1203() {
        assert_eq!(Solution::sort_items(5, 5, vec![2,0,-1,3,0], vec![vec![2,1,3],vec![2,4],vec![],vec![],vec![]]), vec![3,2,4,1,0]);
        assert_eq!(Solution::sort_items(8, 2, vec![-1,-1,1,0,0,1,0,-1], vec![vec![],vec![6],vec![5],vec![6],vec![3,6],vec![],vec![],vec![]]), vec![7, 6, 3, 4, 5, 2, 1, 0]);
        //assert_eq!(Solution::sort_items(8, 2, vec![-1,-1,1,0,0,1,0,-1], vec![vec![],vec![6],vec![5],vec![6],vec![3],vec![],vec![4],vec![]]), vec![]);
    }
}

```
