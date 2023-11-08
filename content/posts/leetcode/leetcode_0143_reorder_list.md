---
title: 143. reorder list
date: '2021-09-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0143 reorder list
---



You are given the head of a singly linked-list. The list can be represented as:



L0 &rarr; L1 &rarr; &hellip; &rarr; Ln - 1 &rarr; Ln



Reorder the list to be on the following form:



L0 &rarr; Ln &rarr; L1 &rarr; Ln - 1 &rarr; L2 &rarr; Ln - 2 &rarr; &hellip;



You may not modify the values in the list's nodes. Only nodes themselves may be changed.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)
>   Input: head <TeX>=</TeX> [1,2,3,4]
>   Output: [1,4,2,3]
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)
>   Input: head <TeX>=</TeX> [1,2,3,4,5]
>   Output: [1,5,2,4,3]
**Constraints:**
>   	The number of nodes in the list is in the range [1, 5  10^4].
>   	1 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 1000


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
use std::collections::VecDeque;
impl Solution {
pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
let mut p = head.take();
let mut deque: VecDeque<Option<Box<ListNode>>> = VecDeque::new();
while let Some(mut node) = p {
p = node.next.take();
deque.push_back(Some(node));
}
let mut stack: Vec<Option<Box<ListNode>>> = vec![];
let mut direction = true;
while !deque.is_empty() {
if direction {
stack.push(deque.pop_front().unwrap());
} else {
stack.push(deque.pop_back().unwrap());
}
direction = !direction;
}
let mut prev: Option<Box<ListNode>> = None;
while let Some(last) = stack.pop() {
let mut node = last.unwrap();
node.next = prev;
prev = Some(node);
}
*head = prev;
}
}

// submission codes end



#[cfg(test)]

mod tests {
use super::*;



#[test]
fn test_143() {
let mut head = linked![1,2,3,4];
Solution::reorder_list(&mut head);
assert_eq!(head, linked![1,4,2,3]);
let mut head = linked![1,2,3,4,5];
Solution::reorder_list(&mut head);
assert_eq!(head, linked![1,5,2,4,3]);

}
}

```
