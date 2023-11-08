---
title: 617. merge two binary trees
date: '2022-04-09'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0617 merge two binary trees
---

 

  You are given two binary trees root1 and root2.

  Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

  Return the merged tree.

  Note: The merging process must start from the root nodes of both trees.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/05/merge.jpg)

 >   Input: root1 <TeX>=</TeX> [1,3,2,5], root2 <TeX>=</TeX> [2,1,3,null,4,null,7]

 >   Output: [3,4,5,5,4,null,7]

  

 >   Example 2:

  

 >   Input: root1 <TeX>=</TeX> [1], root2 <TeX>=</TeX> [1,2]

 >   Output: [2,2]

  

   

  **Constraints:**

  

 >   	The number of nodes in both trees is in the range [0, 2000].

 >   	-10^4 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^4


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
    pub fn merge_helper(target: &mut Option<Rc<RefCell<TreeNode>>>, tree: Option<Rc<RefCell<TreeNode>>>) {
        if let Some(tree) = tree {
            if let Some(target) = target {
                let mut target = target.borrow_mut();
                let mut tree = tree.borrow_mut();
                target.val += tree.val;
                Self::merge_helper(&mut target.left, tree.left.take());
                Self::merge_helper(&mut target.right, tree.right.take());
            } else {
                *target = Some(tree);
            }
        }
    }
    pub fn merge_trees(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut root1 = root1;
        Self::merge_helper(&mut root1, root2);
        root1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_617() {
    }
}

```
