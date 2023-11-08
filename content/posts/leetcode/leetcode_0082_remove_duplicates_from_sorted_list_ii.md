---
title: 82. remove duplicates from sorted list ii
date: '2021-07-22'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0082 remove duplicates from sorted list ii
---



Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)
>   Input: head <TeX>=</TeX> [1,2,3,3,4,4,5]
>   Output: [1,2,5]
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)
>   Input: head <TeX>=</TeX> [1,1,1,2,3]
>   Output: [2,3]
**Constraints:**
>   	The number of nodes in the list is in the range [0, 300].
>   	-100 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100
>   	The list is guaranteed to be sorted in ascending order.


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
/**
pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
let mut head = head;
let mut pre_val = i32::MIN;
while let Some(node) = head {
if node.val != pre_val {
let next_value= match &node.next {
None => {
i32::MIN
},
Some(node) => {
node.val
}
};
if node.val != next_value {
tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(node.val)));
tail = &mut tail.as_mut().unwrap().next;
}
}
pre_val = node.val;
head = node.next;
}
dummy_head.unwrap().next
}
*/
pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
let mut p = head.as_ref();
let mut pre_val = i32::MIN;
while  p.is_some() {
let val = p.unwrap().val;
if val != pre_val {
let next_p = p.unwrap().next.as_ref();
let next_value = if next_p.is_none() {i32::MIN} else {next_p.unwrap().val};
if val != next_value {
tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
tail = &mut tail.as_mut().unwrap().next;
}
}
pre_val = val;
p = p.unwrap().next.as_ref();
}
dummy_head.unwrap().next
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_82() {
assert_eq!(Solution::delete_duplicates(to_list(vec![1, 2, 3, 3, 4, 4, 5])), to_list(vec![1, 2, 5]));
assert_eq!(Solution::delete_duplicates(to_list(vec![1, 1, 1, 2, 3])), to_list(vec![2, 3]));
}
}

```
