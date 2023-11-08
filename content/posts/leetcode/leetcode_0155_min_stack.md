---
title: 155. min stack
date: '2021-09-27'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0155 min stack
---

 

  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

  Implement the MinStack class:

  

  	MinStack() initializes the stack object.

  	void push(val) pushes the element val onto the stack.

  	void pop() removes the element on the top of the stack.

  	int top() gets the top element of the stack.

  	int getMin() retrieves the minimum element in the stack.

  

   

 >   Example 1:

  

 >   Input

 >   ["MinStack","push","push","push","getMin","pop","top","getMin"]

 >   [[],[-2],[0],[-3],[],[],[],[]]

 >   Output

 >   [null,null,null,null,-3,null,0,-2]

 >   Explanation

 >   MinStack minStack <TeX>=</TeX> new MinStack();

 >   minStack.push(-2);

 >   minStack.push(0);

 >   minStack.push(-3);

 >   minStack.getMin(); // return -3

 >   minStack.pop();

 >   minStack.top();    // return 0

 >   minStack.getMin(); // return -2

  

   

  **Constraints:**

  

 >   	-2^31 <TeX>\leq</TeX> val <TeX>\leq</TeX> 2^31 - 1

 >   	Methods pop, top and getMin operations will always be called on non-empty stacks.

 >   	At most 3  10^4 calls will be made to push, pop, top, and getMin.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/* 
struct MinStack {
    nums: Vec<i32>,
    min_val: i32
}

impl MinStack {

    fn new() -> Self {
        let nums: Vec<i32> = vec![];
        let min_val: i32 = i32::MAX;
        Self {nums, min_val}
    }
    
    fn push(&mut self, val: i32) {
        self.nums.push(val);
        self.min_val = i32::min(val, self.min_val);        
    }
    
    fn pop(&mut self) {
        let val = self.nums.pop().unwrap();
        if self.nums.len() == 0 {
            self.min_val = i32::MAX;
        } else {
            if val == self.min_val {
                let val = self.nums.iter().min().unwrap();
                self.min_val = *val;
            }    
        }
    }
    
    fn top(&self) -> i32 {
        self.nums[self.nums.len() - 1]
    }
    
    fn get_min(&self) -> i32 {
        self.min_val
    }
}
*/

struct MinStack {
    nums: Vec<(i32, i32)>
}


impl MinStack {
    fn new() -> Self {
        let nums: Vec<(i32, i32)> = vec![];
        Self {nums}
    }
    
    fn push(&mut self, val: i32) {
        if self.nums.len() == 0 {
            self.nums.push((val, val));
        } else {
            let min_val = i32::min(val, self.nums.last().unwrap().1);
            self.nums.push((val, min_val));
        }
    }
    
    fn pop(&mut self) {
        self.nums.pop();
    }
    
    fn top(&self) -> i32 {
        self.nums.last().unwrap().0
    }
    
    fn get_min(&self) -> i32 {
        self.nums.last().unwrap().1
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_155() {
        let mut min_stack = MinStack::new();
        min_stack.push(-2);
        min_stack.push(0);
        min_stack.push(-3);
        assert_eq!(min_stack.get_min(), -3); // --> Returns -3.
        min_stack.pop();
        assert_eq!(min_stack.top(), 0); // --> Returns 0.
        assert_eq!(min_stack.get_min(), -2); // --> Returns -2.[]
    }
}

```
