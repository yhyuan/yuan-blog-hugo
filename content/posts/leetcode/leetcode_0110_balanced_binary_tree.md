---
title: 110. balanced binary tree
date: '2021-08-19'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0110 balanced binary tree
---

 

  Given a binary tree, determine if it is height-balanced.

  For this problem, a height-balanced binary tree is defined as:

  <blockquote>

  a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

  </blockquote>

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

 >   Input: root <TeX>=</TeX> [3,9,20,null,null,15,7]

 >   Output: true

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

 >   Input: root <TeX>=</TeX> [1,2,2,3,3,null,null,4,4]

 >   Output: false

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> []

 >   Output: true

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [0, 5000].

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
use std::cell::{RefCell, Ref};
type TreeLink = Option<Rc<RefCell<TreeNode>>>;
trait Postorder {
    fn postorder(&self, visit: &mut dyn FnMut(i32, usize, usize, usize), layer: usize) -> usize;
}
impl Postorder for TreeLink {
    fn postorder(&self, visit: &mut dyn FnMut(i32, usize, usize, usize), layer: usize) -> usize {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            let left_depth = node.left.postorder(visit, layer + 1);
            let right_depth = node.right.postorder(visit, layer + 1);
            visit(node.val, layer, left_depth, right_depth);
            return usize::max(left_depth, right_depth);
        }
        layer
    }
}
impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut res = true;
        root.postorder(&mut |x, layer, left_depth, right_depth| {
            let diff = if right_depth > left_depth {right_depth - left_depth} else {left_depth - right_depth};
            res = res && diff <= 1;
        }, 0);
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_110() {
        assert_eq!(Solution::is_balanced(tree![]), true);
        assert_eq!(
            Solution::is_balanced(tree![3, 9, 20, null, null, 15, 7]),
            true
        );
        assert_eq!(
            Solution::is_balanced(tree![1, 2, 2, 3, 3, null, null, 4, 4]),
            false
        );
    }
}

```
