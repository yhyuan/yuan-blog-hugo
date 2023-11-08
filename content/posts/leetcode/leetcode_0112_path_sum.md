---
title: 112. path sum
date: '2021-08-21'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0112 path sum
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={112}/>
 

  Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

  A leaf is a node with no children.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

 >   Input: root <TeX>=</TeX> [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum <TeX>=</TeX> 22

 >   Output: true

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

 >   Input: root <TeX>=</TeX> [1,2,3], targetSum <TeX>=</TeX> 5

 >   Output: false

  

 >   Example 3:

  

 >   Input: root <TeX>=</TeX> [1,2], targetSum <TeX>=</TeX> 0

 >   Output: false

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [0, 5000].

 >   	-1000 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 1000

 >   	-1000 <TeX>\leq</TeX> targetSum <TeX>\leq</TeX> 1000


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
trait Preorder {
    fn preorder(&self, visit: &mut dyn FnMut(i32, i32), path_sum: i32);
}
impl Preorder for TreeLink {
    fn preorder(&self, visit: &mut dyn FnMut(i32, i32), path_sum: i32) {
        if let Some(node) = self {
            let node: Ref<TreeNode> = node.borrow();
            if node.left.is_none() && node.right.is_none() {
                visit(node.val, path_sum);
                return;
            }
            let left_depth = node.left.preorder(visit, path_sum + node.val);
            let right_depth = node.right.preorder(visit, path_sum + node.val);
        }
    }
}
impl Solution {
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool {
        let mut res = false;
        root.preorder(&mut |x, path_sum| {
            if x + path_sum == target_sum {
                res = true;
            }
        }, 0);
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_112() {
        assert_eq!(
            Solution::has_path_sum(
                tree![5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1],
                22
            ),
            true);
        assert_eq!(Solution::has_path_sum(tree![1,2,3], 5), false);
        assert_eq!(Solution::has_path_sum(tree![1,2], 0), false);
    }
}

```
