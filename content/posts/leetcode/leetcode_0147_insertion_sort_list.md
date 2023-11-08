---
title: 147. insertion sort list
date: '2021-09-19'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0147 insertion sort list
---



Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

<ol>

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.

At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.

It repeats until no input elements remain.

</ol>

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

![](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)



>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg)
>   Input: head <TeX>=</TeX> [4,2,1,3]
>   Output: [1,2,3,4]
>   Example 2:
>   ![](https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg)
>   Input: head <TeX>=</TeX> [-1,5,3,4,0]
>   Output: [-1,0,3,4,5]
**Constraints:**
>   	The number of nodes in the list is in the range [1, 5000].
>   	-5000 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 5000


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
trait Insertion {
fn insert(self, link: Option<Box<ListNode>>) -> Option<Box<ListNode>>;
}

impl Insertion for Option<Box<ListNode>> {
fn insert(self, mut link: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
let val = link.as_ref().unwrap().val;
if let Some(mut node) = self {
if node.val > val {
link.as_mut().unwrap().next = Some(node);
link
} else {
node.next = node.next.take().insert(link);
Some(node)
}
} else {
link
}
}
}

impl Solution {
pub fn insertion_sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
let mut head = head;
let mut prev = None;
while let Some(mut node) = head {
head = node.next.take();
prev = prev.insert(Some(node));
}
prev
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_147() {
assert_eq!(Solution::insertion_sort_list(linked![4,2,1,3]), linked![1,2,3,4]);
assert_eq!(Solution::insertion_sort_list(linked![-1,5,3,4,0]), linked![-1,0,3,4,5]);
}
}

```
