---
title: 108. convert sorted array to binary search tree
date: '2021-08-17'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0108 convert sorted array to binary search tree
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={108}/>
 

  Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

  A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

 >   Input: nums <TeX>=</TeX> [-10,-3,0,5,9]

 >   Output: [0,-3,9,-10,null,5]

 >   Explanation: [0,-10,5,null,-3,null,9] is also accepted:

 >   ![](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

 >   Input: nums <TeX>=</TeX> [1,3]

 >   Output: [3,1]

 >   Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^4

 >   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4

 >   	nums is sorted in a strictly increasing order.


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
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if nums.len() == 0 {
            return None;
        }
        if nums.len() == 1 {
            return Some(Rc::new(RefCell::new(TreeNode::new(nums[0]))));
        }
        let index = nums.len() / 2;
        let left_nums: Vec<i32> = (0..index).into_iter().map(|i|nums[i]).collect();
        let right_nums: Vec<i32> = (index + 1..nums.len()).into_iter().map(|i|nums[i]).collect();
        let left = Solution::sorted_array_to_bst(left_nums);
        let right = Solution::sorted_array_to_bst(right_nums);
        Some(Rc::new(RefCell::new(TreeNode{ val: nums[index], left: left, right: right})))
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_108() {
        assert_eq!(
            Solution::sorted_array_to_bst(vec![-10, -3, 0, 5, 9]),
            tree![0, -3, 9, -10, null, 5]
        );
        assert_eq!(Solution::sorted_array_to_bst(vec![]), tree![]);
    }
}

```
