---
title: 700. search in a binary search tree
date: '2022-04-22'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0700 search in a binary search tree
---

 

  You are given the root of a binary search tree (BST) and an integer val.

  Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)

 >   Input: root <TeX>=</TeX> [4,2,7,1,3], val <TeX>=</TeX> 2

 >   Output: [2,1,3]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg)

 >   Input: root <TeX>=</TeX> [4,2,7,1,3], val <TeX>=</TeX> 5

 >   Output: []

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [1, 5000].

 >   	1 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^7

 >   	root is a binary search tree.

 >   	1 <TeX>\leq</TeX> val <TeX>\leq</TeX> 10^7


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
use std::cell::{Ref, RefCell};
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Search {
    fn find(&self, val: i32) -> TreeLink;
}

impl Search for TreeLink {
    fn find(&self, val: i32) -> TreeLink {
        if let Some(node) = self {
            let temp: Rc<RefCell<TreeNode>> = node.clone();
            let _node: Ref<TreeNode> = node.borrow();
            if _node.val == val {
                Some(temp)
            } else {
                if val < _node.val {
                    _node.left.find(val)  // Self::find(&_node.left, val)
                } else {
                    _node.right.find(val)  // Self::find(&_node.right, val)
                }
            }
        } else {
            None
        }
    }
}
impl Solution {
    pub fn search_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        root.find(val)
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_700() {
    }
}

```
