---
title: 86. partition list
date: '2021-07-26'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0086 partition list
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={86}/>
 

  Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

  You should preserve the original relative order of the nodes in each of the two partitions.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)

 >   Input: head <TeX>=</TeX> [1,4,3,2,5,2], x <TeX>=</TeX> 3

 >   Output: [1,2,2,4,3,5]

  

 >   Example 2:

  

 >   Input: head <TeX>=</TeX> [2,1], x <TeX>=</TeX> 2

 >   Output: [1,2]

  

   

  **Constraints:**

  

 >   	The number of nodes in the list is in the range [0, 200].

 >   	-100 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 100

 >   	-200 <TeX>\leq</TeX> x <TeX>\leq</TeX> 200


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
    /*
    pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let mut lower: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut higher: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut lower_tail: Option<&mut Box<ListNode>> = lower.as_mut();
        let mut higher_tail: Option<&mut Box<ListNode>> = higher.as_mut();
        let mut head = head;
        while let Some(mut inner) = head {
            let next = inner.next.take();
            if inner.val < x {
                lower_tail.as_mut().unwrap().next = Some(inner);
                lower_tail = lower_tail.unwrap().next.as_mut();
            } else {
                higher_tail.as_mut().unwrap().next = Some(inner);
                higher_tail = higher_tail.unwrap().next.as_mut();
            }
            //println!("val: {}", inner.val);
            head = next;
        }
        lower_tail.as_mut().unwrap().next = higher.unwrap().next.take();
        lower.unwrap().next.take()
    }
    */
    pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let mut lower: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut higher: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut lower_tail: &mut Option<Box<ListNode>> = &mut lower;//lower.as_mut();
        let mut higher_tail: &mut Option<Box<ListNode>> = &mut higher; //higher.as_mut();
        let mut p = head.as_ref();
        while p.is_some() {
            let val = p.unwrap().val;
            if val < x {
                lower_tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
                lower_tail = &mut lower_tail.as_mut().unwrap().next;
            } else {
                higher_tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(val)));
                higher_tail = &mut higher_tail.as_mut().unwrap().next;
            }
            p = p.unwrap().next.as_ref();
        }
        lower_tail.as_mut().unwrap().next = higher.unwrap().next.take();
        lower.unwrap().next.take()
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_86() {
        assert_eq!(
            Solution::partition(linked![1, 4, 3, 2, 5, 2], 3),
            linked![1, 2, 2, 4, 3, 5]
        );
        assert_eq!(
            Solution::partition(linked![1, 4, 3, 2, 5, 2], 8),
            linked![1, 4, 3, 2, 5, 2]
        );
        assert_eq!(Solution::partition(linked![], 0), linked![]);
    }
}

```
