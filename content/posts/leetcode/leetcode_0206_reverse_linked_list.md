---
title: 206. reverse linked list
date: '2021-10-23'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0206 reverse linked list
---



Given the head of a singly linked list, reverse the list, and return the reversed list.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)
>   Input: head <TeX>=</TeX> [1,2,3,4,5]
>   Output: [5,4,3,2,1]
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)
>   Input: head <TeX>=</TeX> [1,2]
>   Output: [2,1]
>   Example 3:
>   Input: head <TeX>=</TeX> []
>   Output: []
**Constraints:**
>   	The number of nodes in the list is the range [0, 5000].
>   	-5000 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 5000
>   Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


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
pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
let mut p = head.as_ref();
let mut values: Vec<i32> = vec![];
while p.is_some() {
let value = p.unwrap().val;
values.push(value);
p = p.unwrap().next.as_ref();
}
values.reverse();
let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
for value in values {
tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(value)));
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
fn test_206() {
assert_eq!(Solution::reverse_list(linked![1,2,3,4,5]), linked![5,4,3,2,1]);
}
}

```
