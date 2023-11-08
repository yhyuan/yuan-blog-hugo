---
title: 2096. step by step directions from a binary tree node to another
date: '2022-09-06'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2096 step by step directions from a binary tree node to another
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2096}/>

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.



Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:



'L' means to go from a node to its left child node.

'R' means to go from a node to its right child node.

'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node s to node t.



 



 > Example 1:





 > Input: root <TeX>=</TeX> [5,1,2,3,null,6,4], startValue <TeX>=</TeX> 3, destValue <TeX>=</TeX> 6

 > Output: "UURL"

 > Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

 > Example 2:





 > Input: root <TeX>=</TeX> [2,1], startValue <TeX>=</TeX> 2, destValue <TeX>=</TeX> 1

 > Output: "L"

 > Explanation: The shortest path is: 2 → 1.

 



**Constraints:**



 > The number of nodes in the tree is n.

 > 2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 105

 > 1 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> n

 > All the values in the tree are unique.

 > 1 <TeX>\leq</TeX> startValue, destValue <TeX>\leq</TeX> n

 > startValue !<TeX>=</TeX> destValue


## Solution
### Rust
```rust
 pub struct Solution {}
 use crate::util::tree::{TreeNode, to_tree};

 // problem: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
 // discuss: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/?currentPage=1&orderBy=most_votes&query=
 
 // submission codes start here
 // Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::{RefCell, Ref};
use std::collections::HashMap;
use std::collections::HashSet;
use std::collections::VecDeque;
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Postorder {
    fn postorder(&self, visited: &mut dyn FnMut(i32, i32, char)) -> i32;
}
impl Postorder for TreeLink {
    fn postorder(&self, visited: &mut dyn FnMut(i32, i32, char)) -> i32 {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            let left_node_val = node.left.postorder(visited);
            let right_node_val = node.right.postorder(visited);
            if left_node_val != -1 {
                visited(node.val, left_node_val, 'L');
            }
            if right_node_val != -1 {
                visited(node.val, right_node_val, 'R');
            }
            return node.val;
        }
        return -1;
    }
}
//use std::rc::Rc;
//use std::cell::RefCell;
impl Solution {
    pub fn get_directions(root: Option<Rc<RefCell<TreeNode>>>, start_value: i32, dest_value: i32) -> String {
        let mut graph: HashMap<i32, Vec<(i32, char)>> = HashMap::new();
        root.postorder(&mut |node_val, child_node_val, direction| {
            if !graph.contains_key(&node_val) {
                graph.insert(node_val, vec![]);
            }
            graph.get_mut(&node_val).unwrap().push((child_node_val, direction));
            if !graph.contains_key(&child_node_val) {
                graph.insert(child_node_val, vec![]);
            }
            graph.get_mut(&child_node_val).unwrap().push((node_val, 'U'));
        });
        let mut q: VecDeque<(i32, String)> = VecDeque::new();
        let mut visited: HashSet<i32> = HashSet::new();
        q.push_back((start_value, "".to_string()));
        visited.insert(start_value);
        while !q.is_empty() {
            let (u, path) = q.pop_front().unwrap();
            /*
            if u == dest_value {
                return path;
            }
            */
            for (neighbor, next_step) in graph[&u].iter() {
                if visited.contains(neighbor) {
                    continue;
                }
                if (*neighbor == dest_value) {
                    return format!("{}{}", path, next_step)
                }
                visited.insert(*neighbor);
                q.push_back((*neighbor, format!("{}{}", path, next_step)));
            }
        }
        unreachable!()
    }
}
 
 
 // submission codes end
 
 #[cfg(test)]
 mod tests {
     use super::*;
 
     #[test]
     fn test_2096() {
         assert_eq!(Solution::get_directions(tree![5,1,2,3,null,6,4], 3, 6), "UURL".to_string());
         assert_eq!(Solution::get_directions(tree![2, 1], 2, 1), "L".to_string());
     }
 }
 
```
