---
title: 105. construct binary tree from preorder and inorder traversal
date: '2021-08-14'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0105 construct binary tree from preorder and inorder traversal
---

 

  Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

 >   Input: preorder <TeX>=</TeX> [3,9,20,15,7], inorder <TeX>=</TeX> [9,3,15,20,7]

 >   Output: [3,9,20,null,null,15,7]

  

 >   Example 2:

  

 >   Input: preorder <TeX>=</TeX> [-1], inorder <TeX>=</TeX> [-1]

 >   Output: [-1]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> preorder.length <TeX>\leq</TeX> 3000

 >   	inorder.length <TeX>=</TeX><TeX>=</TeX> preorder.length

 >   	-3000 <TeX>\leq</TeX> preorder[i], inorder[i] <TeX>\leq</TeX> 3000

 >   	preorder and inorder consist of unique values.

 >   	Each value of inorder also appears in preorder.

 >   	preorder is guaranteed to be the preorder traversal of the tree.

 >   	inorder is guaranteed to be the inorder traversal of the tree.


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
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if preorder.len() ==0 && inorder.len() == 0 {
            return None;
        }
        if preorder.len() ==1 && inorder.len() == 1 {
            return Some(Rc::new(RefCell::new(TreeNode::new(preorder[0]))));
        }
        let root_val = preorder[0];
        let index = inorder.iter().position(|&v| v == root_val);
        if index.is_none() {
            panic!("Wrong input");
        }
        let index = index.unwrap();
        let left_inorder: Vec<i32> = (0..index).into_iter().map(|i|inorder[i]).collect();
        let right_inorder: Vec<i32> = (index + 1..preorder.len()).into_iter().map(|i|inorder[i]).collect();
        let left_preorder: Vec<i32> = (1..index + 1).into_iter().map(|i|preorder[i]).collect();
        let right_preorder: Vec<i32> = (index + 1..preorder.len()).into_iter().map(|i|preorder[i]).collect();        
        let left = Solution::build_tree(left_preorder, left_inorder);
        let right = Solution::build_tree(right_preorder, right_inorder);

        Some(Rc::new(RefCell::new(TreeNode{val: root_val, left: left, right: right})))
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_105() {
        assert_eq!(
            Solution::build_tree(vec![3, 9, 20, 15, 7], vec![9, 3, 15, 20, 7]),
            tree![3, 9, 20, null, null, 15, 7]
        );
        assert_eq!(
            Solution::build_tree(vec![3, 20, 7], vec![3, 20, 7]),
            tree![3, null, 20, null, 7]
        );
        assert_eq!(Solution::build_tree(vec![], vec![]), tree![]);
    }
}

```
