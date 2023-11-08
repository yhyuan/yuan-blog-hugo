---
title: 99. recover binary search tree
date: '2021-08-08'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0099 recover binary search tree
---

 

  You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

  Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg)

 >   Input: root <TeX>=</TeX> [1,3,null,null,2]

 >   Output: [3,1,null,null,2]

 >   Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg)

 >   Input: root <TeX>=</TeX> [3,1,4,null,null,2]

 >   Output: [2,1,4,null,null,3]

 >   Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [2, 1000].

 >   	-2^31 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 2^31 - 1


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
use std::mem::swap;

type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Inorder {
    fn inorder(&self, prev: &mut TreeLink, first: &mut TreeLink, second: &mut TreeLink);
}
impl Inorder for TreeLink {
    fn inorder(&self, prev: &mut TreeLink, first: &mut TreeLink, second: &mut TreeLink) {
        if let Some(node) = self {
            let node = node.borrow();
            node.left.inorder(prev, first, second);
            if let Some(prev_val) = prev.clone() {
                if prev_val.borrow().val >= node.val {
                    if first.is_none() {
                        *first = prev.clone();
                    }
                    *second = self.clone();
                }
            }
            *prev = self.clone();
            node.right.inorder(prev, first, second);
        }    
    }
}

impl Solution {
    pub fn recover_tree(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        let mut prev = None;
        let mut first = None;
        let mut second = None;
        root.inorder(&mut prev, &mut first, &mut second);
        swap(
            &mut first.unwrap().borrow_mut().val,
            &mut second.unwrap().borrow_mut().val,
        )
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_99() {
        let mut tree = tree![3, 1, 4, null, null, 2];
        Solution::recover_tree(&mut tree);
        assert_eq!(tree, tree![2, 1, 4, null, null, 3]);

        let mut tree = tree![2, 6, 5, null, null, 3, 1, null, 4];
        Solution::recover_tree(&mut tree);
        assert_eq!(tree, tree![2, 1, 5, null, null, 3, 6, null, 4]);

    }
}

```
