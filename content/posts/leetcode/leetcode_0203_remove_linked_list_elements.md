---
title: 203. remove linked list elements
date: '2021-10-20'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0203 remove linked list elements
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={203}/>
 

  Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val <TeX>=</TeX><TeX>=</TeX> val, and return the new head.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

 >   Input: head <TeX>=</TeX> [1,2,6,3,4,5,6], val <TeX>=</TeX> 6

 >   Output: [1,2,3,4,5]

  

 >   Example 2:

  

 >   Input: head <TeX>=</TeX> [], val <TeX>=</TeX> 1

 >   Output: []

  

 >   Example 3:

  

 >   Input: head <TeX>=</TeX> [7,7,7,7], val <TeX>=</TeX> 7

 >   Output: []

  

   

  **Constraints:**

  

 >   	The number of nodes in the list is in the range [0, 10^4].

 >   	1 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 50

 >   	0 <TeX>\leq</TeX> val <TeX>\leq</TeX> 50


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
/*
impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
        let mut p = head.as_ref();

        while p.is_some() {
            let value = p.unwrap().val;
            p = p.unwrap().next.as_ref();
            if value != val {
                tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(value)));
                tail = &mut tail.as_mut().unwrap().next;    
            }
        }
        dummy_head.unwrap().next
    }
}
*/
impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
        let mut head = head;
        let mut p = head.take();
        while let Some(mut node) = p {
            //println!("val: {}", node.val);
            p = node.next.take();
            if node.val != val {
                tail.as_mut().unwrap().next = Some(node);
                tail = &mut tail.as_mut().unwrap().next;    
            }
        }
        dummy_head.unwrap().next
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_203() {
        assert_eq!(Solution::remove_elements(linked![1,2,6,3,4,5,6], 6), linked![1,2,3,4,5]);
        assert_eq!(Solution::remove_elements(linked![], 6), linked![]);
        assert_eq!(Solution::remove_elements(linked![7,7,7,7], 7), linked![]);
    }
}

```
