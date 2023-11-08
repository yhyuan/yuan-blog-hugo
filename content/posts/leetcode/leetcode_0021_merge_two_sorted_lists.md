---
title: 21. merge two sorted lists
date: '2021-05-22'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0021 merge two sorted lists
---



Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)
>   Input: l1 <TeX>=</TeX> [1,2,4], l2 <TeX>=</TeX> [1,3,4]
>   Output: [1,1,2,3,4,4]
>   Example 2:
>   Input: l1 <TeX>=</TeX> [], l2 <TeX>=</TeX> []
>   Output: []
>   Example 3:
>   Input: l1 <TeX>=</TeX> [], l2 <TeX>=</TeX> [0]
>   Output: [0]
**Constraints:**
>   	The number of nodes in both lists is in the range [0, 50].
>   	-100 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100
>   	Both l1 and l2 are sorted in non-decreasing order.


## Solution


### Rust
```rust
pub struct Solution {}
use crate::util::linked_list::{ListNode, to_list};


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
impl Solution {
pub fn merge_two_lists(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
let mut p1 = l1.as_ref();
let mut p2 = l2.as_ref();

while p1.is_some() || p2.is_some() {
let v1 = if p1.is_none() {i32::MAX} else {p1.unwrap().val};
let v2 = if p2.is_none() {i32::MAX} else {p2.unwrap().val};
if v1 <= v2 {
p1 = p1.unwrap().next.as_ref();
} else {
p2 = p2.unwrap().next.as_ref();
}
tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(i32::min(v1, v2))));
tail = &mut tail.as_mut().unwrap().next;
}
dummy_head.unwrap().next
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_21() {
assert_eq!(
Solution::merge_two_lists(to_list(vec![1, 2, 4]), to_list(vec![1, 3, 4])),
to_list(vec![1, 1, 2, 3, 4, 4])
);
}
}

```
