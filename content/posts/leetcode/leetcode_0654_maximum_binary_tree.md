---
title: 654. maximum binary tree
date: '2022-04-16'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0654 maximum binary tree
---

 

  You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

  <ol>

  	Create a root node whose value is the maximum value in nums.

  	Recursively build the left subtree on the subarray prefix to the left of the maximum value.

  	Recursively build the right subtree on the subarray suffix to the right of the maximum value.

  </ol>

  Return the maximum binary tree built from nums.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg)

 >   Input: nums <TeX>=</TeX> [3,2,1,6,0,5]

 >   Output: [6,3,5,null,2,0,null,null,1]

 >   Explanation: The recursive calls are as follow:

 >   - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].

 >       - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].

 >           - Empty array, so no child.

 >           - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].

 >               - Empty array, so no child.

 >               - Only one element, so child is a node with value 1.

 >       - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].

 >           - Only one element, so child is a node with value 0.

 >           - Empty array, so no child.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg)

 >   Input: nums <TeX>=</TeX> [3,2,1]

 >   Output: [3,null,2,null,1]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 1000

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000

 >   	All integers in nums are unique.


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
    pub fn construct_maximum_binary_tree_helper(nums: &Vec<i32>, start: usize, end: usize) -> Option<Rc<RefCell<TreeNode>>> {
        if start == end {
            return Some(Rc::new(RefCell::new(TreeNode::new(nums[start]))));
        }
        let mut index_of_max = start;
        for i in start..=end {
            if nums[i] > nums[index_of_max] {
                index_of_max = i;
            }
        }
        if index_of_max >= start + 1 && index_of_max + 1 > end {
            let left = Solution::construct_maximum_binary_tree_helper(nums, start, index_of_max - 1);
            let root = Some(Rc::new(RefCell::new(TreeNode{val: nums[index_of_max], left: left, right: None})));
            return root;
        }
        if index_of_max < start + 1 && index_of_max + 1 <= end {
            let right = Solution::construct_maximum_binary_tree_helper(nums, index_of_max + 1, end);
            let root = Some(Rc::new(RefCell::new(TreeNode{val: nums[index_of_max], left: None, right: right})));
            return root;
        }
        let left = Solution::construct_maximum_binary_tree_helper(nums, start, index_of_max - 1);
        let right = Solution::construct_maximum_binary_tree_helper(nums, index_of_max + 1, end);
        let root = Some(Rc::new(RefCell::new(TreeNode{val: nums[index_of_max], left: left, right: right})));
        root    
    }
    pub fn construct_maximum_binary_tree(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if nums.len() == 0 {
            return None;
        }
        Solution::construct_maximum_binary_tree_helper(&nums, 0, nums.len() - 1)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_654() {
        assert_eq!(Solution::construct_maximum_binary_tree(vec![3,2,1,6,0,5]), tree![6,3,5,null,2,0,null,null,1]);
        assert_eq!(Solution::construct_maximum_binary_tree(vec![3,2,1]), tree![3,null,2,null,1]);
    }
}

```
