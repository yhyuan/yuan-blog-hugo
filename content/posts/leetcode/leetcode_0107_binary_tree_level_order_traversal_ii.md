---
title: 107. binary tree level order traversal ii
date: '2021-08-16'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0107 binary tree level order traversal ii
---



Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
>   Input: root <TeX>=</TeX> [3,9,20,null,null,15,7]
>   Output: [[15,7],[9,20],[3]]
>   Example 2:
>   Input: root <TeX>=</TeX> [1]
>   Output: [[1]]
>   Example 3:
>   Input: root <TeX>=</TeX> []
>   Output: []
**Constraints:**
>   	The number of nodes in the tree is in the range [0, 2000].
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
trait Inorder {
fn inorder(&self, visit: &mut dyn FnMut(i32, usize), layer: usize);
}
impl Inorder for TreeLink {
fn inorder(&self, visit: &mut dyn FnMut(i32, usize), layer: usize) {
if let Some(node) = self {
let node: Ref<TreeNode> = node.borrow();
node.left.inorder(visit, layer + 1);
visit(node.val, layer);
node.right.inorder(visit, layer + 1);
}
}
}
impl Solution {
pub fn level_order_bottom(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
let mut res:Vec<Vec<i32>> = vec![];
root.inorder(&mut |x, layer| {
if res.len() < layer + 1 {
for i in res.len()..layer + 1 {
res.push(vec![]);
}
}
res[layer].push(x);
}, 0);
res.reverse();
res
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_107() {
assert_eq!(
Solution::level_order_bottom(tree![3, 9, 20, null, null, 15, 7]),
vec![vec![15, 7], vec![9, 20], vec![3],]
);
}
}

```
