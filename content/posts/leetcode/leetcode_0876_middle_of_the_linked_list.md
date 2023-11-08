---
title: 876. middle of the linked list
date: '2022-06-02'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0876 middle of the linked list
---



Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)
>   Input: head <TeX>=</TeX> [1,2,3,4,5]
>   Output: [3,4,5]
>   Explanation: The middle node of the list is node 3.
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)
>   Input: head <TeX>=</TeX> [1,2,3,4,5,6]
>   Output: [4,5,6]
>   Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
**Constraints:**
>   	The number of nodes in the list is in the range [1, 100].
>   	1 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100


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
pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
let mut p = head.as_ref();
let mut count = 0;
while p.is_some() {
count += 1;
p = p.unwrap().next.as_ref();
}
let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
let mut p = head.as_ref();
let mut i = 0;
while p.is_some() {
if i >= count / 2 {
//return p;
tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(p.unwrap().val)));
tail = &mut tail.as_mut().unwrap().next;
}
i += 1;
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
fn test_876() {
assert_eq!(Solution::middle_node(linked![1,2,3,4,5]), linked![3,4,5]);
assert_eq!(Solution::middle_node(linked![1,2,3,4,5,6]), linked![4,5,6]);
}
}

```
