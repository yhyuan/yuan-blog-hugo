---
title: 707. design linked list
date: '2022-04-26'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0707 design linked list
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={707}/>
 

  Design your implementation of the linked list. You can choose to use a singly or doubly linked list.<br />

  A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.<br />

  If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

  Implement the MyLinkedList class:

  

  	MyLinkedList() Initializes the MyLinkedList object.

  	int get(int index) Get the value of the index^th node in the linked list. If the index is invalid, return -1.

  	void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.

  	void addAtTail(int val) Append a node of value val as the last element of the linked list.

  	void addAtIndex(int index, int val) Add a node of value val before the index^th node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.

  	void deleteAtIndex(int index) Delete the index^th node in the linked list, if the index is valid.

  

   

 >   Example 1:

  

 >   Input

 >   ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]

 >   [[], [1], [3], [1, 2], [1], [1], [1]]

 >   Output

 >   [null, null, null, null, 2, null, 3]

 >   Explanation

 >   MyLinkedList myLinkedList <TeX>=</TeX> new MyLinkedList();

 >   myLinkedList.addAtHead(1);

 >   myLinkedList.addAtTail(3);

 >   myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3

 >   myLinkedList.get(1);              // return 2

 >   myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3

 >   myLinkedList.get(1);              // return 3

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> index, val <TeX>\leq</TeX> 1000

 >   	Please do not use the built-in LinkedList library.

 >   	At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
   pub val: i32,
   pub next: Option<Box<ListNode>>
}
 
impl ListNode {
   #[inline]
   fn new(val: i32) -> Self {
     ListNode {
       next: None,
       val
     }
   }
}

struct MyLinkedList {
    pub head: Option<Box<ListNode>>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyLinkedList {

    /** Initialize your data structure here. */
    fn new() -> Self {
        Self {
            head: None
        }
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    fn get(&self, index: i32) -> i32 {
        if index < 0 {
            return -1;
        }
        let mut p = self.head.as_ref();
        let mut index = index;
        while p.is_some() {
            if index == 0 {
                return p.unwrap().val;
            }
            index -= 1;
            p = p.unwrap().next.as_ref();
        }
        -1
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    fn add_at_head(&mut self, val: i32) {
        self.head = Some(Box::new(ListNode {
            val: val,
            next: self.head.take()
        }));
    }
    
    /** Append a node of value val to the last element of the linked list. */
    fn add_at_tail(&mut self, val: i32) {
        let mut p = &mut self.head;
        while let Some(node) = p {
            p = &mut node.next;
        }
        *p = Some(Box::new(ListNode::new(val)));
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    fn add_at_index(&mut self, index: i32, val: i32) {
        if index <= 0 {
            self.add_at_head(val);
        } else {
            let mut i = 0;
            let mut link: &mut Option<Box<ListNode>> = &mut self.head;
            while let Some(node) = link {
                if index == i + 1 {
                    node.next = Some(Box::new(ListNode{
                        val: val,
                        next: node.next.take()
                    }));
                    return;
                } else {
                    link = &mut node.next;
                    i += 1;
                }
            }
        }
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    fn delete_at_index(&mut self, index: i32) {
        if index < 0 {
            return;
        }
        let mut i = 0;
        let mut link: &mut Option<Box<ListNode>> = &mut self.head;
        loop {
            match link {
                None => {
                    return;
                }
                Some(node) if index == i => {
                    *link = node.next.take();
                    return;
                }
                Some(node) => {
                    link = &mut node.next;
                    i += 1;
                }
            }
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let obj = MyLinkedList::new();
 * let ret_1: i32 = obj.get(index);
 * obj.add_at_head(val);
 * obj.add_at_tail(val);
 * obj.add_at_index(index, val);
 * obj.delete_at_index(index);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_707() {
        /* 
        let obj = MyLinkedList::new();
        let ret_1: i32 = obj.get(index);
        obj.add_at_head(val);
        obj.add_at_tail(val);
        obj.add_at_index(index, val);
        obj.delete_at_index(index);  
        */     
    }
}

```
