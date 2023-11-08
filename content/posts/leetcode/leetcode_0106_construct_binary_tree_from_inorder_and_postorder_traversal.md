---
title: 106. construct binary tree from inorder and postorder traversal
date: '2021-08-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0106 construct binary tree from inorder and postorder traversal
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={106}/>
 

  Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

 >   Input: inorder <TeX>=</TeX> [9,3,15,20,7], postorder <TeX>=</TeX> [9,15,7,20,3]

 >   Output: [3,9,20,null,null,15,7]

  

 >   Example 2:

  

 >   Input: inorder <TeX>=</TeX> [-1], postorder <TeX>=</TeX> [-1]

 >   Output: [-1]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> inorder.length <TeX>\leq</TeX> 3000

 >   	postorder.length <TeX>=</TeX><TeX>=</TeX> inorder.length

 >   	-3000 <TeX>\leq</TeX> inorder[i], postorder[i] <TeX>\leq</TeX> 3000

 >   	inorder and postorder consist of unique values.

 >   	Each value of postorder also appears in inorder.

 >   	inorder is guaranteed to be the inorder traversal of the tree.

 >   	postorder is guaranteed to be the postorder traversal of the tree.


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
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if postorder.len() ==0 && inorder.len() == 0 {
            return None;
        }
        if postorder.len() ==1 && inorder.len() == 1 {
            return Some(Rc::new(RefCell::new(TreeNode::new(postorder[0]))));
        }
        let n = postorder.len();
        let root_val = postorder[n - 1];
        let index = inorder.iter().position(|&v| v == root_val);
        if index.is_none() {
            panic!("Wrong input");
        }
        let index = index.unwrap();
        let left_inorder: Vec<i32> = (0..index).into_iter().map(|i|inorder[i]).collect();
        let right_inorder: Vec<i32> = (index + 1..inorder.len()).into_iter().map(|i|inorder[i]).collect();

        let left_postorder: Vec<i32> = (0..index).into_iter().map(|i|postorder[i]).collect();
        let right_postorder: Vec<i32> = (index..postorder.len() - 1).into_iter().map(|i|postorder[i]).collect();        
        let left = Solution::build_tree(left_inorder, left_postorder);
        let right = Solution::build_tree(right_inorder, right_postorder);

        Some(Rc::new(RefCell::new(TreeNode{val: root_val, left: left, right: right})))
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_106() {
        assert_eq!(
            Solution::build_tree(vec![9, 3, 15, 20, 7], vec![9, 15, 7, 20, 3]),
            tree![3, 9, 20, null, null, 15, 7]
        );
        assert_eq!(
            Solution::build_tree(vec![3, 20, 7], vec![7, 20, 3]),
            tree![3, null, 20, null, 7]
        );
        assert_eq!(Solution::build_tree(vec![], vec![]), tree![]);
    }
}

```
