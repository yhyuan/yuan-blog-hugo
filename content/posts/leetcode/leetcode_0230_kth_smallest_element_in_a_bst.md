---
title: 230. kth smallest element in a bst
date: '2021-11-16'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0230 kth smallest element in a bst
---



Given the root of a binary search tree, and an integer k, return the k^th (1-indexed) smallest element in the tree.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)
>   Input: root <TeX>=</TeX> [3,1,4,null,2], k <TeX>=</TeX> 1
>   Output: 1
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)
>   Input: root <TeX>=</TeX> [5,3,6,2,4,null,null,1], k <TeX>=</TeX> 3
>   Output: 3
**Constraints:**
>   	The number of nodes in the tree is n.
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4
>   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^4
>   Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


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
pub fn helper(root: Option<&Rc<RefCell<TreeNode>>>, values: &mut Vec<i32>) {
if let Some(node) = root {
//let left = node.borrow().left.as_ref();
Solution::helper(node.borrow().left.as_ref(), values);
values.push(node.borrow().val);
//let right = node.borrow().right.as_ref();
Solution::helper(node.borrow().right.as_ref(), values);
}
}

pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
let mut values: Vec<i32> = vec![];
Solution::helper(root.as_ref(), &mut values);
values[k as usize - 1]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_230() {
assert_eq!(Solution::kth_smallest(tree![3, 1, 4, null, 2], 1), 1);
assert_eq!(Solution::kth_smallest(tree![3, 1, 4, null, 2], 2), 2);
assert_eq!(Solution::kth_smallest(tree![3, 1, 4, null, 2], 3), 3);
assert_eq!(Solution::kth_smallest(tree![5,3,6,2,4,null,null,1], 3), 3);
}
}

```
