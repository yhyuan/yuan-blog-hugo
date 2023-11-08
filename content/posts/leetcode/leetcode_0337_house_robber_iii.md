---
title: 337. house robber iii
date: '2022-01-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0337 house robber iii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={337}/>
 

  The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

  Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

  Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg)

 >   Input: root <TeX>=</TeX> [3,2,3,null,3,null,1]

 >   Output: 7

 >   Explanation: Maximum amount of money the thief can rob <TeX>=</TeX> 3 + 3 + 1 <TeX>=</TeX> 7.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg)

 >   Input: root <TeX>=</TeX> [3,4,5,1,3,null,1]

 >   Output: 9

 >   Explanation: Maximum amount of money the thief can rob <TeX>=</TeX> 4 + 5 <TeX>=</TeX> 9.

  

   

  **Constraints:**

  

 >   	The number of nodes in the tree is in the range [1, 10^4].

 >   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^4


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
use std::cell::{RefCell};

impl Solution {
    pub fn rob(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        0
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_337() {
        assert_eq!(Solution::rob(tree![3,2,3,null,3,null,1]), 7);
        assert_eq!(Solution::rob(tree![3,4,5,1,3,null,1]), 9);
    }
}

```
