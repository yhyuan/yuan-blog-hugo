---
title: 234. palindrome linked list
date: '2021-11-20'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0234 palindrome linked list
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={234}/>
 

  Given the head of a singly linked list, return true if it is a palindrome.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

 >   Input: head <TeX>=</TeX> [1,2,2,1]

 >   Output: true

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

 >   Input: head <TeX>=</TeX> [1,2]

 >   Output: false

  

   

  **Constraints:**

  

 >   	The number of nodes in the list is in the range [1, 10^5].

 >   	0 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 9

  

   

 >   Follow up: Could you do it in O(n) time and O(1) space?


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
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut p = head.as_ref();
        let mut nums: Vec<i32> = vec![];
        while p.is_some() {
            nums.push(p.unwrap().val);
            p = p.unwrap().next.as_ref();
        }
        for i in 0..nums.len() / 2 {
            if nums[i] != nums[nums.len() - 1 - i] {
                return false;
            }
        }
        true
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_234() {
        assert_eq!(Solution::is_palindrome(linked![1,2,2,1]), true);
        assert_eq!(Solution::is_palindrome(linked![1,2]), false);
    }
}

```
