---
title: 232. implement queue using stacks
date: '2021-11-18'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0232 implement queue using stacks
---



Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:



void push(int x) Pushes element x to the back of the queue.

int pop() Removes the element from the front of the queue and returns it.

int peek() Returns the element at the front of the queue.

boolean empty() Returns true if the queue is empty, false otherwise.



Notes:



You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.

Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.





>   Example 1:
>   Input
>   ["MyQueue", "push", "push", "peek", "pop", "empty"]
>   [[], [1], [2], [], [], []]
>   Output
>   [null, null, null, 1, 1, false]
>   Explanation
>   MyQueue myQueue <TeX>=</TeX> new MyQueue();
>   myQueue.push(1); // queue is: [1]
>   myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
>   myQueue.peek(); // return 1
>   myQueue.pop(); // return 1, queue is [2]
>   myQueue.empty(); // return false
**Constraints:**
>   	1 <TeX>\leq</TeX> x <TeX>\leq</TeX> 9
>   	At most 100 calls will be made to push, pop, peek, and empty.
>   	All the calls to pop and peek are valid.
>   Follow-up: Can you implement the queue such that each operation is [amortized](https://en.wikipedia.org/wiki/Amortized_analysis) O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

struct MyQueue {
stack: Vec<i32>,
}


/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl MyQueue {

/** Initialize your data structure here. */
fn new() -> Self {
let stack: Vec<i32> = vec![];
MyQueue{stack: stack}
}

/** Push element x to the back of queue. */
fn push(&mut self, x: i32) {
let mut stack_bk: Vec<i32> = vec![];
for i in 0..self.stack.len() {
let val = self.stack.pop().unwrap();
stack_bk.push(val);
}
self.stack.push(x);
for i in (0..stack_bk.len()).rev() {
self.stack.push(stack_bk[i]);
}
}

/** Removes the element from in front of queue and returns that element. */
fn pop(&mut self) -> i32 {
let val = self.stack.pop();
val.unwrap()
}

/** Get the front element. */
fn peek(&self) -> i32 {
self.stack[self.stack.len() - 1]
}

/** Returns whether the queue is empty. */
fn empty(&self) -> bool {
self.stack.len() == 0
}
}

/**
* Your MyQueue object will be instantiated and called as such:
* let obj = MyQueue::new();
* obj.push(x);
* let ret_2: i32 = obj.pop();
* let ret_3: i32 = obj.peek();
* let ret_4: bool = obj.empty();
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_232() {
let mut queue = MyQueue::new();
queue.push(1);
queue.push(2);
assert_eq!(queue.peek(), 1); // returns 1
assert_eq!(queue.pop(), 1); // returns 1
assert_eq!(queue.empty(), false); // returns false
}
}

```
