---
title: 111. minimum depth of binary tree
date: '2021-08-20'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0111 minimum depth of binary tree
---



Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)
>   Input: root <TeX>=</TeX> [3,9,20,null,null,15,7]
>   Output: 2
>   Example 2:
>   Input: root <TeX>=</TeX> [2,null,3,null,4,null,5,null,6]
>   Output: 5
**Constraints:**
>   	The number of nodes in the tree is in the range [0, 10^5].
>   	-1000 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 1000


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
use std::cell::{RefCell, Ref};
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Preorder {
fn preorder(&self, visit: &mut dyn FnMut(i32, usize), layer: usize);
}
impl Preorder for TreeLink {
fn preorder(&self, visit: &mut dyn FnMut(i32, usize), layer: usize) {
if let Some(node) = self {
let node: Ref<TreeNode> = node.borrow();
if node.left.is_none() && node.right.is_none() {
visit(node.val, layer);
return;
}
let left_depth = node.left.preorder(visit, layer + 1);
let right_depth = node.right.preorder(visit, layer + 1);
}
}
}
impl Solution {
pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
let mut res: Option<usize> = None;
root.preorder(&mut |x, layer| {
if let Some(min_depth) = res {
res = Some(usize::min(min_depth, layer));
} else {
res = Some(layer);
}
}, 1);
if res.is_none() {0} else {res.unwrap() as i32}
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_111() {
assert_eq!(Solution::min_depth(tree![3, 9, 20, null, null, 15, 7]), 2);
assert_eq!(Solution::min_depth(tree![2,null,3,null,4,null,5,null,6]), 5);
assert_eq!(Solution::min_depth(tree![]), 0);
}
}

```
