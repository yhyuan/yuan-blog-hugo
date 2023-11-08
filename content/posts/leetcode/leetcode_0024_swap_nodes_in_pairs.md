---
title: 24. swap nodes in pairs
date: '2021-05-25'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0024 swap nodes in pairs
---

 

  Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

 >   Input: head <TeX>=</TeX> [1,2,3,4]

 >   Output: [2,1,4,3]

  

 >   Example 2:

  

 >   Input: head <TeX>=</TeX> []

 >   Output: []

  

 >   Example 3:

  

 >   Input: head <TeX>=</TeX> [1]

 >   Output: [1]

  

   

  **Constraints:**

  

 >   	The number of nodes in the list is in the range [0, 100].

 >   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100


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
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy_head = Some(Box::new(ListNode { val: 0, next: head }));
        let mut head = dummy_head.as_mut();
        loop {
            let mut left = head.as_mut().unwrap().next.take();
            if left.is_none() {
                break;
            }
            let mut right = left.as_mut().unwrap().next.take();
            // handle the un-paired one, e.g. [1, 2, 3] -> [2, 1, 3], 3 is un-paired
            if right.is_none() {
                head.as_mut().unwrap().next = left;
                break;
            }
            let mut next = right.as_mut().unwrap().next.take();
            // BEFORE: head -> left -> right -> next
            // AFTER: head -> right -> left -> next
            left.as_mut().unwrap().next = next;
            right.as_mut().unwrap().next = left;
            head.as_mut().unwrap().next = right;
            head = head.unwrap().next.as_mut().unwrap().next.as_mut();
        }
        dummy_head.unwrap().next
    }
}
*/
impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy_head = Some(Box::new(ListNode::new(0)));
        let mut tail = &mut dummy_head;
        let mut stack: Vec<i32> = vec![];
        let mut p = head.as_ref();
        while p.is_some() {
            let v = p.unwrap().val;
            if stack.len() == 0 {
                stack.push(v);
            } else {
                tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(v)));
                tail = &mut tail.as_mut().unwrap().next;
                let v = stack.pop().unwrap();
                tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(v)));
                tail = &mut tail.as_mut().unwrap().next;                                
            }
            p = p.unwrap().next.as_ref();
        }
        if stack.len() > 0 {
            let v = stack.pop().unwrap();
            tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(v)));
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
    fn test_24() {
        /*
        assert_eq!(
            Solution::swap_pairs(to_list(vec![1, 2, 3, 4])),
            to_list(vec![2, 1, 4, 3]) 
        );
        assert_eq!(
            Solution::swap_pairs(to_list(vec![1, 2, 3])),
            to_list(vec![2, 1, 3])
        );
        */
        //assert_eq!(Solution::swap_pairs(to_list(vec![])), to_list(vec![]));
        assert_eq!(Solution::swap_pairs(to_list(vec![1])), to_list(vec![1]));
    }
}

```
