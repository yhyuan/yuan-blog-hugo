---
title: 95. unique binary search trees ii
date: '2021-08-04'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0095 unique binary search trees ii
---



Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)
>   Input: n <TeX>=</TeX> 3
>   Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
>   Example 2:
>   Input: n <TeX>=</TeX> 1
>   Output: [[1]]
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 8


## Solution


### Rust
```rust
pub struct Solution {}
use crate::util::tree::{TreeNode, to_tree};


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
use std::cell::RefCell;
impl Solution {
pub fn generate_trees_helper(nums: &Vec<i32>) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
if nums.len() == 0 {
let res: Vec<Option<Rc<RefCell<TreeNode>>>> = vec![None];
return res;
}
if nums.len() == 1 {
let res: Vec<Option<Rc<RefCell<TreeNode>>>> = vec![Some(Rc::new(RefCell::new(TreeNode::new(nums[0]))))];
return res;
}
let mut res: Vec<Option<Rc<RefCell<TreeNode>>>> = vec![];
for i in 0..nums.len() {
// i is the root
let left_nums = (0..i).into_iter().map(|k| nums[k]).collect();
let left_trees = Solution::generate_trees_helper(&left_nums);
let right_nums = (i + 1..nums.len()).into_iter().map(|k| nums[k]).collect();
let right_trees = Solution::generate_trees_helper(&right_nums);
for left_tree in left_trees.iter() {
for right_tree in right_trees.iter() {
let tree = Some(Rc::new(RefCell::new(TreeNode {val: nums[i], left: left_tree.clone(), right: right_tree.clone()})));
res.push(tree);
}
}
}
res
}
pub fn generate_trees(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
if n < 1 {
return vec![];
}
let nums: Vec<i32> = (1..=n).into_iter().collect();
//println!("nums: {:?}", nums);
Solution::generate_trees_helper(&nums)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_95() {
assert_eq!(Solution::generate_trees(3), vec![
tree![1,null,2,null,3],
tree![1,null,3,2],
tree![2,1,3],
tree![3,1,null,null,2],
tree![3,2,null,1]]);
}
}

```
