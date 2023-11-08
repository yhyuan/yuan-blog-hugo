---
title: 61. rotate list
date: '2021-07-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0061 rotate list
---

 

  Given the head of a linked list, rotate the list to the right by k places.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

 >   Input: head <TeX>=</TeX> [1,2,3,4,5], k <TeX>=</TeX> 2

 >   Output: [4,5,1,2,3]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

 >   Input: head <TeX>=</TeX> [0,1,2], k <TeX>=</TeX> 4

 >   Output: [2,0,1]

  

   

  **Constraints:**

  

 >   	The number of nodes in the list is in the range [0, 500].

 >   	-100 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100

 >   	0 <TeX>\leq</TeX> k <TeX>\leq</TeX> 2  10^9


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
    pub fn rotate_right(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if head.is_none() {
            return head;
        }
        let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
        let mut p = head.as_ref();
        let mut len = 0;
        while  p.is_some() {
            len += 1;
            p = p.unwrap().next.as_ref();
        }
        let k = k % len;
        if k == 0 {
            return head;
        }
        let mut p = head.as_ref();
        let mut i = 1;
        while  p.is_some() {
            if i > len - k {
                let val = p.unwrap().val;
                //println!("1 val: {}", val);
                tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
                tail = &mut tail.as_mut().unwrap().next;
            }
            i += 1;
            p = p.unwrap().next.as_ref();
        }
        let mut p = head.as_ref();
        let mut i = 0;
        while  p.is_some() {
            if i < len - k {
                let val = p.unwrap().val;
                //println!("2 val: {}", val);
                tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
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
    fn test_61() {
        assert_eq!(Solution::rotate_right(linked![1,2,3,4,5], 2), linked![4, 5, 1, 2, 3]);
        assert_eq!(Solution::rotate_right(linked![0,1,2], 4), linked![2,0,1]);
        assert_eq!(Solution::rotate_right(linked![1,2], 1), linked![2,1]);
    }
}

```
