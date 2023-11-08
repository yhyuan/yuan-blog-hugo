---
title: 222. count complete tree nodes
date: '2021-11-08'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0222 count complete tree nodes
---

 

  Given the root of a complete binary tree, return the number of the nodes in the tree.

  According to [Wikipedia](http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees), every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2^h nodes inclusive at the last level h.

  Design an algorithm that runs in less than O(n) time complexity.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)

 >   Input: root <TeX>=</TeX> [1,2,3,4,5,6]

 >   Output: 6

  

 >   Example 2:

  

 >   Input: root <TeX>=</TeX> []

 >   Output: 0

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> [1]

 >   Output: 1

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [0, 5  10^4].

 >   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 5  10^4

 >   	The tree is guaranteed to be complete.


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
    fn inorder(&self, visit: &mut dyn FnMut(i32));
}
impl Inorder for TreeLink {
    fn inorder(&self, visit: &mut dyn FnMut(i32)) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            //Self::inorder(&node.left, visit);
            node.left.inorder(visit);
            visit(node.val);
            //Self::inorder(&node.right, visit);
            node.right.inorder(visit);
        }    
    }
}
impl Solution {
    pub fn count_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 0i32;
        root.inorder(&mut |x| {
            res += 1;
        });
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_222() {
        assert_eq!(Solution::count_nodes(tree![1,2,3,4,5,6]), 6);
    }
}

```
