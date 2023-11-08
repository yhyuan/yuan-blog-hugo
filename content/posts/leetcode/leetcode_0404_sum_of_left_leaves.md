---
title: 404. sum of left leaves
date: '2022-02-26'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0404 sum of left leaves
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={404}/>
 

  Given the root of a binary tree, return the sum of all left leaves.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg)

 >   Input: root <TeX>=</TeX> [3,9,20,null,null,15,7]

 >   Output: 24

 >   Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

  

 >   Example 2:

  

 >   Input: root <TeX>=</TeX> [1]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [1, 1000].

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
    fn inorder(&self, visit: &mut dyn FnMut(i32), is_left: bool);
}
impl Inorder for TreeLink {
    fn inorder(&self, visit: &mut dyn FnMut(i32), is_left: bool) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            node.left.inorder(visit, true);
            if is_left && node.left.is_none() && node.right.is_none() {
                visit(node.val);
            }
            node.right.inorder(visit, false);
        }    
    }
}
impl Solution {
    pub fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 0;
        root.inorder(&mut |x| {
            res += x;
        }, false);
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_404() {
        assert_eq!(Solution::sum_of_left_leaves(tree![3,9,20,null,null,15,7]), 24);
    }
}

```
