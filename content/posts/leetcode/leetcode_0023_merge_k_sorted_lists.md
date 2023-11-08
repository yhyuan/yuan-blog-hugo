---
title: 23. merge k sorted lists
date: '2021-05-24'
tags: ['leetcode', 'rust', 'python', 'hard']
draft: false
description: Solution for leetcode 0023 merge k sorted lists
---

 

  You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

  Merge all the linked-lists into one sorted linked-list and return it.

   

 >   Example 1:

  

 >   Input: lists <TeX>=</TeX> [[1,4,5],[1,3,4],[2,6]]

 >   Output: [1,1,2,3,4,4,5,6]

 >   Explanation: The linked-lists are:

 >   [

 >     1->4->5,

 >     1->3->4,

 >     2->6

 >   ]

 >   merging them into one sorted list:

 >   1->1->2->3->4->4->5->6

  

 >   Example 2:

  

 >   Input: lists <TeX>=</TeX> []

 >   Output: []

  

 >   Example 3:

  

 >   Input: lists <TeX>=</TeX> [[]]

 >   Output: []

  

   

  **Constraints:**

  

 >   	k <TeX>=</TeX><TeX>=</TeX> lists.length

 >   	0 <TeX>\leq</TeX> k <TeX>\leq</TeX> 10^4

 >   	0 <TeX>\leq</TeX> lists[i].length <TeX>\leq</TeX> 500

 >   	-10^4 <TeX>\leq</TeX> lists[i][j] <TeX>\leq</TeX> 10^4

 >   	lists[i] is sorted in ascending order.

 >   	The sum of lists[i].length won't exceed 10^4.


## Solution
We use heap to store the heads of the lists and implement their comparison method. The heap will will pop out the one with min val and we can insert it to a dummy list one by one. The time complexity is O(N * LOG(K))
### Python
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def __lt__(self, other):
    return self.val < other.val

setattr(ListNode, '__lt__', __lt__)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heappush(heap, lists[i])
        dummy = ListNode(0)
        p = dummy
        while len(heap) > 0:
            node = heappop(heap)
            p.next = node
            next_node = node.next
            node.next = None
            p = p.next
            if next_node is not None:
                heappush(heap, next_node)
        return dummy.next
```
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
use std::collections::BinaryHeap;
use std::cmp::Ordering;
#[derive(Debug)]
pub struct Node (i32, usize);
impl Eq for Node {}
impl Ord for Node {
    fn cmp(&self, other: &Self) -> Ordering {
        self.0.cmp(&other.0).reverse()
    }
}
impl PartialEq for Node {
    fn eq(&self, other: &Self) -> bool {
        self.0.eq(&other.0)
    }
}
impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.0.cmp(&other.0).reverse())
    }
}
impl Solution {
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        let mut dummy_head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(0)));
        let mut tail: &mut Option<Box<ListNode>> = &mut dummy_head;

        let mut points: Vec<Option<&Box<ListNode>>> = lists.iter()
            .filter(|list| list.is_some())    
            .map(|list| list.as_ref())
            .collect();
        let values: Vec<Node> = (0..points.len()).into_iter()
            .map(|i| Node(points[i].unwrap().val, i))
            .collect();
        points = points.iter().map(|&p| p.unwrap().next.as_ref()).collect();
        let mut min_heap: BinaryHeap<Node> = BinaryHeap::from(values);
        loop {
            let item = min_heap.pop();
            if item.is_none() {
                break;
            }
            let node = item.unwrap();
            let value = node.0;
            let index = node.1;
            tail.as_mut().unwrap().next = Some(Box::new(ListNode::new(value)));
            tail = &mut tail.as_mut().unwrap().next;    
            let mut p = points[index];
            if p.is_some() {
                min_heap.push(Node(p.unwrap().val, index));
                points[index] = p.unwrap().next.as_ref();
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
    fn test_23() {
        assert_eq!(
            Solution::merge_k_lists(vec![
                to_list(vec![1, 4, 5]),
                to_list(vec![1, 3, 4]),
                to_list(vec![2, 6]),
            ]),
            to_list(vec![1, 1, 2, 3, 4, 4, 5, 6])
        );
        assert_eq!(Solution::merge_k_lists(vec![]), None);
    }
}

```
