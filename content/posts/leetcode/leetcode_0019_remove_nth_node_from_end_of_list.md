---
title: 19. remove nth node from end of list
date: '2021-05-20'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0019 remove nth node from end of list
---

 

  Given the head of a linked list, remove the n^th node from the end of the list and return its head.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

 >   Input: head <TeX>=</TeX> [1,2,3,4,5], n <TeX>=</TeX> 2

 >   Output: [1,2,3,5]

  

 >   Example 2:

  

 >   Input: head <TeX>=</TeX> [1], n <TeX>=</TeX> 1

 >   Output: []

  

 >   Example 3:

  

 >   Input: head <TeX>=</TeX> [1,2], n <TeX>=</TeX> 1

 >   Output: [1]

  

   

  **Constraints:**

  

 >   	The number of nodes in the list is sz.

 >   	1 <TeX>\leq</TeX> sz <TeX>\leq</TeX> 30

 >   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> sz

  

   

 >   Follow up: Could you do this in one pass?


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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode{val: 0, next: head}));
        let mut len = 0;
        {
            let mut p: Option<&Box<ListNode>> = dummy_head.as_ref();
            while p.unwrap().next.is_some() { // p->next
                len += 1;
                p = p.unwrap().next.as_ref(); // p = p->next
            }    
        }
        {
            let mut p: Option<&mut Box<ListNode>> = dummy_head.as_mut();
            for _ in 0..len - n {
                p = p.unwrap().next.as_mut();
            }
            let next = p.as_mut().unwrap().next.as_mut().unwrap().next.take();
            p.as_mut().unwrap().next = next;
        }
        dummy_head.unwrap().next
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_19() {
        assert_eq!(
            Solution::remove_nth_from_end(to_list(vec![1, 2, 3, 4, 5]), 2),
            to_list(vec![1, 2, 3, 5])
        );
        assert_eq!(Solution::remove_nth_from_end(to_list(vec![1]), 1), None);
    }
}

```
