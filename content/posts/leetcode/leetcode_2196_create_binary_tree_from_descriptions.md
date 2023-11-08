---
title: 2196. create binary tree from descriptions
date: '2022-09-26'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2196 create binary tree from descriptions
---


You are given a 2D integer array descriptions where descriptions[i] <TeX>=</TeX> [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,



If isLefti <TeX>=</TeX><TeX>=</TeX> 1, then childi is the left child of parenti.

If isLefti <TeX>=</TeX><TeX>=</TeX> 0, then childi is the right child of parenti.

Construct the binary tree described by descriptions and return its root.



The test cases will be generated such that the binary tree is valid.







> Example 1:
> Input: descriptions <TeX>=</TeX> [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
> Output: [50,20,80,15,17,19]
> Explanation: The root node is the node with value 50 since it has no parent.
> The resulting binary tree is shown in the diagram.
> Example 2:
> Input: descriptions <TeX>=</TeX> [[1,2,1],[2,3,0],[3,4,1]]
> Output: [1,2,null,null,3,4]
> Explanation: The root node is the node with value 1 since it has no parent.
> The resulting binary tree is shown in the diagram.
**Constraints:**
> 1 <TeX>\leq</TeX> descriptions.length <TeX>\leq</TeX> 104
> descriptions[i].length <TeX>=</TeX><TeX>=</TeX> 3
> 1 <TeX>\leq</TeX> parenti, childi <TeX>\leq</TeX> 105
> 0 <TeX>\leq</TeX> isLefti <TeX>\leq</TeX> 1
> The binary tree described by descriptions is valid.


## Solution


### Rust
```rust
// use std::collections::HashMap;
pub struct Solution {}
use crate::util::tree::{TreeNode, to_tree};

use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;
impl Solution {
pub fn build_tree(parent_children_hashmap: &HashMap<i32, (i32, i32)>, value: i32) -> Option<Rc<RefCell<TreeNode>>> {
if value == -1 {
return None;
}
// println!("value: {}", value);
if !parent_children_hashmap.contains_key(&value) {
return Some(Rc::new(RefCell::new(TreeNode::new(value))));
}
let children = *parent_children_hashmap.get(&value).unwrap();
let left_child = Self::build_tree(parent_children_hashmap, children.0);
let right_child = Self::build_tree(parent_children_hashmap, children.1);

let root = Some(Rc::new(RefCell::new(TreeNode {
val: value,
left: left_child,
right: right_child
})));
root
}

pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
let mut parent_children_hashmap: HashMap<i32, (i32, i32)> = HashMap::new();
let mut children_parent_hashmap: HashMap<i32, i32> = HashMap::new();
let n = descriptions.len();
for i in 0..n{
let parent =  descriptions[i][0];
let child =  descriptions[i][1];
let is_left =  descriptions[i][2];
children_parent_hashmap.insert(child, parent);
if parent_children_hashmap.contains_key(&parent) {
let mut children =  *parent_children_hashmap.get(&parent).unwrap();
let children = if is_left == 1 { (child, children.1) } else {(children.0, child)};
parent_children_hashmap.insert(parent, children);
} else {
let children = if is_left == 1 { (child, -1) } else {(-1, child)};
parent_children_hashmap.insert(parent, children);
}
}
let mut root_value = -1i32;
for (&parent, &children) in parent_children_hashmap.iter() {
if !children_parent_hashmap.contains_key(&parent) {
root_value = parent;
}
}
let root = Self::build_tree(&parent_children_hashmap, root_value);
root
}
}



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_2196() {
assert_eq!(Solution::create_binary_tree(vec![vec![20,15,1],vec![20,17,0],vec![50,20,1],vec![50,80,0],vec![80,19,1]]), tree![50,20,80,15,17,19]);
}
}


```
