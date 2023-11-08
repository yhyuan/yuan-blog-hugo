---
title: 382. linked list random node
date: '2022-02-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0382 linked list random node
---



Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:



Solution(ListNode head) Initializes the object with the integer array nums.

int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.





>   Example 1:
>   ![](https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg)
>   Input
>   ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
>   [[[1, 2, 3]], [], [], [], [], []]
>   Output
>   [null, 1, 3, 2, 2, 3]
>   Explanation
>   Solution solution <TeX>=</TeX> new Solution([1, 2, 3]);
>   solution.getRandom(); // return 1
>   solution.getRandom(); // return 3
>   solution.getRandom(); // return 2
>   solution.getRandom(); // return 2
>   solution.getRandom(); // return 3
>   // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
**Constraints:**
>   	The number of nodes in the linked list will be in the range [1, 10^4].
>   	-10^4 <TeX>\leq</TeX> Node.val <TeX>\leq</TeX> 10^4
>   	At most 10^4 calls will be made to getRandom.
>   Follow up:
>   	What if the linked list is extremely large and its length is unknown to you?
>   	Could you solve this efficiently without using extra space?


## Solution


### Rust
```rust
//pub struct Solution {}
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
use rand::Rng;
pub struct Solution {
nums: Vec<i32>
}


/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl Solution {

/** @param head The linked list's head.
Note that the head is guaranteed to be not null, so it contains at least one node. */
fn new(head: Option<Box<ListNode>>) -> Self {
let mut p = head.as_ref();
let mut nums: Vec<i32> = vec![];
while p.is_some() {
let val = p.unwrap().val;
nums.push(val);
p = p.unwrap().next.as_ref();
}
Self {nums}
}

/** Returns a random node's value. */
fn get_random(&self) -> i32 {
let i = rand::thread_rng().gen_range(0, self.nums.len());
self.nums[i]
}
}

/**
* Your Solution object will be instantiated and called as such:
* let obj = Solution::new(head);
* let ret_1: i32 = obj.get_random();
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_382() {
}
}

```
