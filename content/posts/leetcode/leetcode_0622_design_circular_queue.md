---
title: 622. design circular queue
date: '2022-04-10'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0622 design circular queue
---



Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:



MyCircularQueue(k) Initializes the object with the size of the queue to be k.

int Front() Gets the front item from the queue. If the queue is empty, return -1.

int Rear() Gets the last item from the queue. If the queue is empty, return -1.

boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.

boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.

boolean isEmpty() Checks whether the circular queue is empty or not.

boolean isFull() Checks whether the circular queue is full or not.



You must solve the problem without using the built-in queue data structure in your programming language.



>   Example 1:
>   Input
>   ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
>   [[3], [1], [2], [3], [4], [], [], [], [4], []]
>   Output
>   [null, true, true, true, false, 3, true, true, true, 4]
>   Explanation
>   MyCircularQueue myCircularQueue <TeX>=</TeX> new MyCircularQueue(3);
>   myCircularQueue.enQueue(1); // return True
>   myCircularQueue.enQueue(2); // return True
>   myCircularQueue.enQueue(3); // return True
>   myCircularQueue.enQueue(4); // return False
>   myCircularQueue.Rear();     // return 3
>   myCircularQueue.isFull();   // return True
>   myCircularQueue.deQueue();  // return True
>   myCircularQueue.enQueue(4); // return True
>   myCircularQueue.Rear();     // return 4
**Constraints:**
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> 1000
>   	0 <TeX>\leq</TeX> value <TeX>\leq</TeX> 1000
>   	At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

struct MyCircularQueue {
front: usize,
back: usize,
size: usize,
nums: Vec<i32>
}


/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl MyCircularQueue {

fn new(k: i32) -> Self {
Self {nums: vec![0; k as usize], front: 0usize, back: 0usize, size: 0usize}
}

fn en_queue(&mut self, value: i32) -> bool {
if self.is_full() {
return false;
}
self.nums[self.front] = value;
self.front = (self.front + 1) % self.nums.len();
self.size += 1;
true
}

fn de_queue(&mut self) -> bool {
if self.is_empty() {
return false;
}
//let value = self.nums[self.back];
//self.back = if self.back == 0 {self.nums.len() - 1} else {self.back + 1};
self.back = (self.back + 1) % self.nums.len();
self.size -= 1;
true
}

fn front(&self) -> i32 {
if self.is_empty() {
return -1;
}
self.nums[self.back]
}

fn rear(&self) -> i32 {
if self.is_empty() {
return -1;
}
let index = if self.front == 0 {self.nums.len() - 1} else {self.front - 1};
self.nums[index]
}

fn is_empty(&self) -> bool {
self.size == 0
}

fn is_full(&self) -> bool {
self.size == self.nums.len()
}
}

/**
* Your MyCircularQueue object will be instantiated and called as such:
* let obj = MyCircularQueue::new(k);
* let ret_1: bool = obj.en_queue(value);
* let ret_2: bool = obj.de_queue();
* let ret_3: i32 = obj.front();
* let ret_4: i32 = obj.rear();
* let ret_5: bool = obj.is_empty();
* let ret_6: bool = obj.is_full();
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_622() {
/*
let mut obj = MyCircularQueue::new(3);
assert_eq!(obj.en_queue(1), true);
assert_eq!(obj.en_queue(2), true);
assert_eq!(obj.en_queue(3), true);
assert_eq!(obj.en_queue(4), false);
assert_eq!(obj.rear(), 3);
assert_eq!(obj.is_full(), true);
assert_eq!(obj.de_queue(), true);
assert_eq!(obj.en_queue(4), true);
assert_eq!(obj.rear(), 4);
*/
let mut obj = MyCircularQueue::new(7);
assert_eq!(obj.en_queue(0), true);
assert_eq!(obj.front(), 0);
assert_eq!(obj.en_queue(4), true);
assert_eq!(obj.rear(), 4);
assert_eq!(obj.en_queue(6), true);
assert_eq!(obj.en_queue(3), true);
assert_eq!(obj.rear(), 3);
assert_eq!(obj.de_queue(), true);
assert_eq!(obj.front(), 4);
assert_eq!(obj.de_queue(), true);
assert_eq!(obj.front(), 6);

}
}

```
