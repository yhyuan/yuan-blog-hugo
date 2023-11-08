---
title: 25. reverse nodes in k group
date: '2021-05-26'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0025 reverse nodes in k group
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={25}/>
 

  Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

  k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

  You may not alter the values in the list's nodes, only nodes themselves may be changed.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

 >   Input: head <TeX>=</TeX> [1,2,3,4,5], k <TeX>=</TeX> 2

 >   Output: [2,1,4,3,5]

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

 >   Input: head <TeX>=</TeX> [1,2,3,4,5], k <TeX>=</TeX> 3

 >   Output: [3,2,1,4,5]

  

 >   Example 3:

  

 >   Input: head <TeX>=</TeX> [1,2,3,4,5], k <TeX>=</TeX> 1

 >   Output: [1,2,3,4,5]

  

 >   Example 4:

  

 >   Input: head <TeX>=</TeX> [1], k <TeX>=</TeX> 1

 >   Output: [1]

  

   

  **Constraints:**

  

 >   	The number of nodes in the list is in the range sz.

 >   	1 <TeX>\leq</TeX> sz <TeX>\leq</TeX> 5000

 >   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 1000

 >   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> sz

  

   

 >   Follow-up: Can you solve the problem in O(1) extra memory space?


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
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut dummy_head = Some(Box::new(ListNode { val: 0, next: head }));
        let mut head = dummy_head.as_mut();
        'outer: loop {
            let mut start = head.as_mut().unwrap().next.take();
            if start.is_none() {
                break 'outer;
            }
            let mut end = start.as_mut();
            for _ in 0..(k - 1) {
                end = end.unwrap().next.as_mut();
                if end.is_none() {
                    head.as_mut().unwrap().next = start;
                    break 'outer;
                }
            }
            let tail = end.as_mut().unwrap().next.take();
            // BEFORE: head -> start -> 123456... -> end   -> tail
            // AFTER:  head -> end   -> ...654321 -> start -> tail
            let end = Solution::reverse(start, tail);
            head.as_mut().unwrap().next = end;
            for _ in 0..k {
                head = head.unwrap().next.as_mut()
            }
        }
        dummy_head.unwrap().next
    }

    #[inline(always)]
    fn reverse(
        head: Option<Box<ListNode>>,
        tail: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut prev = tail;
        let mut current = head;
        while let Some(mut current_node_inner) = current {
            let next = current_node_inner.next.take();
            current_node_inner.next = prev.take();
            prev = Some(current_node_inner);
            current = next;
        }
        prev
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_25() {
        assert_eq!(
            Solution::reverse_k_group(to_list(vec![1, 2, 3, 4, 5]), 2),
            to_list(vec![2, 1, 4, 3, 5])
        );
        assert_eq!(
            Solution::reverse_k_group(to_list(vec![1, 2, 3, 4, 5]), 3),
            to_list(vec![3, 2, 1, 4, 5])
        );
        assert_eq!(
            Solution::reverse_k_group(to_list(vec![1, 2, 3, 4, 5]), 5),
            to_list(vec![5, 4, 3, 2, 1])
        );
        assert_eq!(
            Solution::reverse_k_group(to_list(vec![1]), 1),
            to_list(vec![1])
        );
    }
}

```
