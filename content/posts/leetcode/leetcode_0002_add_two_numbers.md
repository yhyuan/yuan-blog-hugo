---
title: 2. add two numbers
date: '2021-05-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0002 add two numbers
---

 

  You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

  You may assume the two numbers do not contain any leading zero, except the number 0 itself.

   

>   Example 1:

>   ![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

>   Input: l1 <TeX>=</TeX> [2,4,3], l2 <TeX>=</TeX> [5,6,4]

>   Output: [7,0,8]

>   Explanation: 342 + 465 <TeX>=</TeX> 807.

  

>   Example 2:

  

>   Input: l1 <TeX>=</TeX> [0], l2 <TeX>=</TeX> [0]

>   Output: [0]

  

>   Example 3:

  

>   Input: l1 <TeX>=</TeX> [9,9,9,9,9,9,9], l2 <TeX>=</TeX> [9,9,9,9]

>   Output: [8,9,9,9,0,0,0,1]

  

   

  **Constraints:**

  

 >  	The number of nodes in each linked list is in the range [1, 100].

 >  	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 9

 >  	It is guaranteed that the list represents a number that does not have leading zeros.


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
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;
        let (mut l1_end, mut l2_end, mut overflow) = (false, false, false);
        let (mut l1, mut l2) = (l1, l2);
        loop {
            let rhs = match l1 {
                Some(node) => {
                    l1 = node.next;
                    node.val
                }, 
                None => {
                    l1_end = true;
                    0
                }
            };
            let lhs = match l2 {
                Some(node) => {
                    l2 = node.next;
                    node.val
                }, 
                None => {
                    l2_end = true;
                    0
                }
            };
            if l1_end && l2_end && !overflow {
                return dummy_head.unwrap().next;
            }
            let mut sum = rhs + lhs + if overflow {1} else {0};
            if sum >= 10 {
                overflow = true;
                sum -= 10;
            } else {
                overflow = false;
            }
            tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(sum)));
            tail = &mut tail.as_mut().unwrap().next;
        }
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2() {
        assert_eq!(
            Solution::add_two_numbers(to_list(vec![2, 4, 3]), to_list(vec![5, 6, 4])),
            to_list(vec![7, 0, 8])
        );

        assert_eq!(
            Solution::add_two_numbers(to_list(vec![9, 9, 9, 9]), to_list(vec![9, 9, 9, 9, 9, 9])),
            to_list(vec![8, 9, 9, 9, 0, 0, 1])
        );

        assert_eq!(
            Solution::add_two_numbers(to_list(vec![0]), to_list(vec![0])),
            to_list(vec![0])
        )
    }
}

```
