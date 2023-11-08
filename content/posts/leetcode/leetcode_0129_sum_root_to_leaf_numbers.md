---
title: 129. sum root to leaf numbers
date: '2021-09-05'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0129 sum root to leaf numbers
---

 

  You are given the root of a binary tree containing digits from 0 to 9 only.

  Each root-to-leaf path in the tree represents a number.

  

  	For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

  

  Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

  A leaf node is a node with no children.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)

 >   Input: root <TeX>=</TeX> [1,2,3]

 >   Output: 25

 >   Explanation:

 >   The root-to-leaf path 1->2 represents the number 12.

 >   The root-to-leaf path 1->3 represents the number 13.

 >   Therefore, sum <TeX>=</TeX> 12 + 13 <TeX>=</TeX> 25.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)

 >   Input: root <TeX>=</TeX> [4,9,0,5,1]

 >   Output: 1026

 >   Explanation:

 >   The root-to-leaf path 4->9->5 represents the number 495.

 >   The root-to-leaf path 4->9->1 represents the number 491.

 >   The root-to-leaf path 4->0 represents the number 40.

 >   Therefore, sum <TeX>=</TeX> 495 + 491 + 40 <TeX>=</TeX> 1026.

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [1, 1000].

 >   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 9

 >   	The depth of the tree will not exceed 10.


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
                visit(node.val, path_sum * 10 + node.val);
                return;
            }
            let left_depth = node.left.preorder(visit, path_sum * 10 + node.val);
            let right_depth = node.right.preorder(visit, path_sum * 10 + node.val);
        }
    }
}
impl Solution {
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = 0i32;
        root.preorder(&mut |x, path_sum| {
            res += path_sum;
        }, 0);
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_129() {
        assert_eq!(Solution::sum_numbers(tree![1, 2, 3]), 25);
        assert_eq!(Solution::sum_numbers(tree![4, 9, 0, 5, 1]), 1026);
    }
}

```
