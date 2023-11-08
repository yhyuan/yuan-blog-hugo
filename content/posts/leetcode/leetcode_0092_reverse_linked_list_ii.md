---
title: 92. reverse linked list ii
date: '2021-08-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0092 reverse linked list ii
---



Given the head of a singly linked list and two integers left and right where left <TeX>\leq</TeX> right, reverse the nodes of the list from position left to position right, and return the reversed list.



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)
>   Input: head <TeX>=</TeX> [1,2,3,4,5], left <TeX>=</TeX> 2, right <TeX>=</TeX> 4
>   Output: [1,4,3,2,5]
>   Example 2:
>   Input: head <TeX>=</TeX> [5], left <TeX>=</TeX> 1, right <TeX>=</TeX> 1
>   Output: [5]
**Constraints:**
>   	The number of nodes in the list is n.
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 500
>   	-500 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 500
>   	1 <TeX>\leq</TeX> left <TeX>\leq</TeX> right <TeX>\leq</TeX> n
>   Follow up: Could you do it in one pass?


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
pub fn reverse_between(head: Option<Box<ListNode>>, left: i32, right: i32) -> Option<Box<ListNode>> {
if head.is_none() {
return head;
}
if left == right {
return head;
}
let left = left as usize;
let right = right as usize;
let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
let mut p = head.as_ref();
let mut i = 0;
let mut nums: Vec<i32> = Vec::with_capacity(right - left + 1);
while  p.is_some() {
i += 1;
if i < left || i > right {
let val = p.unwrap().val;
tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
tail = &mut tail.as_mut().unwrap().next;
} else {
nums.push(p.unwrap().val);
if i == right {
for i in (0..nums.len()).rev() {
let val = nums[i];
tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
tail = &mut tail.as_mut().unwrap().next;
}
}
}
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
fn test_92() {
assert_eq!(Solution::reverse_between(to_list(vec![1,2,3,4,5]), 2, 4), to_list(vec![1,4,3,2,5]));
assert_eq!(Solution::reverse_between(to_list(vec![5]), 1, 1), to_list(vec![5]));

}
}

```
