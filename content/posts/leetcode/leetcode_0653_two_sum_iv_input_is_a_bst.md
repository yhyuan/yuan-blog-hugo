---
title: 653. two sum iv input is a bst
date: '2022-04-15'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0653 two sum iv input is a bst
---



Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)
>   Input: root <TeX>=</TeX> [5,3,6,2,4,null,7], k <TeX>=</TeX> 9
>   Output: true
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)
>   Input: root <TeX>=</TeX> [5,3,6,2,4,null,7], k <TeX>=</TeX> 28
>   Output: false
>   Example 3:
>   Input: root <TeX>=</TeX> [2,1,3], k <TeX>=</TeX> 4
>   Output: true
>   Example 4:
>   Input: root <TeX>=</TeX> [2,1,3], k <TeX>=</TeX> 1
>   Output: false
>   Example 5:
>   Input: root <TeX>=</TeX> [2,1,3], k <TeX>=</TeX> 3
>   Output: true
**Constraints:**
>   	The number of nodes in the tree is in the range [1, 10^4].
>   	-10^4 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^4
>   	root is guaranteed to be a valid binary search tree.
>   	-10^5 <TeX>\leq</TeX> k <TeX>\leq</TeX> 10^5


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
use std::collections::HashSet;
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Find {
fn find(&self, hashset: &mut HashSet<i32>, k: i32) -> bool;
}
impl Find for TreeLink {
fn find(&self, hashset: &mut HashSet<i32>, k: i32) -> bool {
if let Some(node) = self {
let _node = node.borrow();
if hashset.contains(&_node.val) {
true
} else {
hashset.insert(k - _node.val);
_node.left.find(hashset, k) || _node.right.find(hashset, k)
}
} else {
false
}
}
}
impl Solution {
pub fn find_target(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> bool {
let mut hashset: HashSet<i32> = HashSet::new();
root.find(&mut hashset, k)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_653() {
}
}

```
