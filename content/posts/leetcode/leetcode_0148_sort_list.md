---
title: 148. sort list
date: '2021-09-20'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0148 sort list
---

 

  Given the head of a linked list, return the list after sorting it in ascending order.

  Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)

 >   Input: head <TeX>=</TeX> [4,2,1,3]

 >   Output: [1,2,3,4]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)

 >   Input: head <TeX>=</TeX> [-1,5,3,4,0]

 >   Output: [-1,0,3,4,5]

  

 >   Example 3:

  

 >   Input: head <TeX>=</TeX> []

 >   Output: []

  

   

  **Constraints:**

  

 >   	The number of nodes in the list is in the range [0, 5  10^4].

 >   	-10^5 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^5


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
    pub fn sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut p = head.as_ref();
        let mut values: Vec<i32> = vec![];
        while p.is_some() {
            let val = p.unwrap().val;
            values.push(val);
            p = p.unwrap().next.as_ref();
        }
        values.sort();
        let mut dummy_head = Some(Box::new(ListNode::new(0)));
        let mut tail = &mut dummy_head;
        for &val in values.iter() {
            //let node = Some(Box::new(ListNode::new(val)));
            tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
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
    fn test_148() {
        assert_eq!(Solution::sort_list(linked![4,2,1,3]), linked![1,2,3,4]);
        assert_eq!(Solution::sort_list(linked![-1,5,3,4,0]), linked![-1,0,3,4,5]);
    }
}

```
