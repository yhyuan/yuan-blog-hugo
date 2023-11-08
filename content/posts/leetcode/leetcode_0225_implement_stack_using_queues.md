---
title: 225. implement stack using queues
date: '2021-11-11'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0225 implement stack using queues
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={225}/>
 

  Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

  Implement the MyStack class:

  

  	void push(int x) Pushes element x to the top of the stack.

  	int pop() Removes the element on the top of the stack and returns it.

  	int top() Returns the element on the top of the stack.

  	boolean empty() Returns true if the stack is empty, false otherwise.

  

  Notes:

  

  	You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.

  	Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

  

   

 >   Example 1:

  

 >   Input

 >   ["MyStack", "push", "push", "top", "pop", "empty"]

 >   [[], [1], [2], [], [], []]

 >   Output

 >   [null, null, null, 2, 2, false]

 >   Explanation

 >   MyStack myStack <TeX>=</TeX> new MyStack();

 >   myStack.push(1);

 >   myStack.push(2);

 >   myStack.top(); // return 2

 >   myStack.pop(); // return 2

 >   myStack.empty(); // return False

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> x <TeX>\leq</TeX> 9

 >   	At most 100 calls will be made to push, pop, top, and empty.

 >   	All the calls to pop and top are valid.

  

   

 >   Follow-up: Can you implement the stack using only one queue?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
struct MyStack {
    q: VecDeque<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyStack {

    /** Initialize your data structure here. */
    fn new() -> Self {
        let q: VecDeque<i32> = VecDeque::new();
        MyStack{q: q}
    }
    
    /** Push element x onto stack. */
    fn push(&mut self, x: i32) {
        let mut backup_q: VecDeque<i32> = VecDeque::new();
        for _ in 0..self.q.len() {
            backup_q.push_back(self.q.pop_front().unwrap());
        }
        self.q.push_back(x);
        for _ in 0..backup_q.len() {
            self.q.push_back(backup_q.pop_front().unwrap());
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    fn pop(&mut self) -> i32 {
        self.q.pop_front().unwrap()
    }
    
    /** Get the top element. */
    fn top(&mut self) -> i32 {
        let v = self.q.front().unwrap();
        *v
    }
    
    /** Returns whether the stack is empty. */
    fn empty(&self) -> bool {
        self.q.len() == 0
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj = MyStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: bool = obj.empty();
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_225() {
        let mut stack = MyStack::new();

        stack.push(1);
        stack.push(2);
        assert_eq!(stack.top(), 2); // returns 2
        assert_eq!(stack.pop(), 2); // returns 2
        assert_eq!(stack.empty(), false); // returns false
        assert_eq!(stack.pop(), 1);
        assert_eq!(stack.empty(), true);
    }
}

```
