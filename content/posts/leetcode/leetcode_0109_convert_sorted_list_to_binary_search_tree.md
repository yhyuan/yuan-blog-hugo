---
title: 109. convert sorted list to binary search tree
date: '2021-08-18'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0109 convert sorted list to binary search tree
---



Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)
>   Input: head <TeX>=</TeX> [-10,-3,0,5,9]
>   Output: [0,-3,9,-10,null,5]
>   Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
>   Example 2:
>   Input: head <TeX>=</TeX> []
>   Output: []
>   Example 3:
>   Input: head <TeX>=</TeX> [0]
>   Output: [0]
>   Example 4:
>   Input: head <TeX>=</TeX> [1,3]
>   Output: [3,1]
**Constraints:**
>   	The number of nodes in head is in the range [0, 2  10^4].
>   	-10^5 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^5


## Solution


### Rust
```rust
pub struct Solution {}
use crate::util::linked_list::{ListNode, to_list};
use crate::util::tree::{TreeNode, to_tree};


// submission codes start here

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
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
pub fn convert_vector(head: Option<&Box<ListNode>>) -> Vec<i32> {
let mut p = head;
let mut nums: Vec<i32> = vec![];
while p.is_some() {
nums.push(p.unwrap().val);
p = p.unwrap().next.as_ref();
}
nums
}
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
pub fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Option<Rc<RefCell<TreeNode>>> {
let nums = Solution::convert_vector(head.as_ref());
Solution::sorted_array_to_bst(nums)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_109() {
assert_eq!(
Solution::sorted_list_to_bst(linked![-10, -3, 0, 5, 9]),
tree![0, -3, 9, -10, null, 5]
);
}
}

```
