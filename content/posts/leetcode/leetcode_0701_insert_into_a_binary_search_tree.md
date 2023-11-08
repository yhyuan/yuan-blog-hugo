---
title: 701. insert into a binary search tree
date: '2022-04-23'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0701 insert into a binary search tree
---

 

  You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

  Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)

 >   Input: root <TeX>=</TeX> [4,2,7,1,3], val <TeX>=</TeX> 5

 >   Output: [4,2,7,1,3,5]

 >   Explanation: Another accepted tree is:

 >   ![](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)

  

 >   Example 2:

  

 >   Input: root <TeX>=</TeX> [40,20,60,10,30,50,70], val <TeX>=</TeX> 25

 >   Output: [40,20,60,10,30,50,70,null,null,25]

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> [4,2,7,1,3,null,null,null,null,null,null], val <TeX>=</TeX> 5

 >   Output: [4,2,7,1,3,5]

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree will be in the range [0, 10^4].

 >   	-10^8 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^8

 >   	All the values Node.val are unique.

 >   	-10^8 <TeX>\leq</TeX> val <TeX>\leq</TeX> 10^8

 >   	It's guaranteed that val does not exist in the original BST.


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

type TreeLink = Option<Rc<RefCell<TreeNode>>>;

trait Insert {
    fn insert(self, val: i32) -> TreeLink;
}
impl Insert for TreeLink {
    fn insert(self, val: i32) -> TreeLink {
        if let Some(node) = self {
            let node_val = node.borrow().val;
            let left = node.borrow_mut().left.take();
            let right = node.borrow_mut().right.take();            
            if val < node_val {
                Some(Rc::new(RefCell::new(TreeNode {
                    val: node_val,
                    left: left.insert(val),
                    right,
                })))
            } else {
                Some(Rc::new(RefCell::new(TreeNode {
                    val: node_val,
                    left,
                    right: right.insert(val),
                })))
            }
        } else {
            Some(Rc::new(RefCell::new(TreeNode::new(val))))
        }
    }
}
impl Solution {
    pub fn insert_into_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        let mut root = root;
        root.insert(val)
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_701() {
    }
}

```
