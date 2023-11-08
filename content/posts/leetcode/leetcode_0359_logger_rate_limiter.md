---
title: 359. logger rate limiter
date: '2022-01-24'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0359 logger rate limiter
---


Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).



All messages will come in chronological order. Several messages may arrive at the same timestamp.



Implement the Logger class:



Logger() Initializes the logger object.

bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.





> Example 1:
> Input
> ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
> [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
> Output
> [null, true, true, false, false, false, true]
> Explanation
> Logger logger <TeX>=</TeX> new Logger();
> logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 <TeX>=</TeX> 11
> logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 <TeX>=</TeX> 12
> logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
> logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
> logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
> logger.shouldPrintMessage(11, "foo"); // 11 ><TeX>=</TeX> 11, return true, next allowed timestamp for "foo" is 11 + 10 <TeX>=</TeX> 21
**Constraints:**
> 0 <TeX>\leq</TeX> timestamp <TeX>\leq</TeX> 109
> Every timestamp will be passed in non-decreasing order (chronological order).
> 1 <TeX>\leq</TeX> message.length <TeX>\leq</TeX> 30
> At most 104 calls will be made to shouldPrintMessage.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
struct Logger {
messages: HashMap<String, i32>,
}


/**
* `&self` means the method takes an immutable reference.
* If you need a mutable reference, change it to `&mut self` instead.
*/
impl Logger {

fn new() -> Self {
let messages: HashMap<String, i32> = HashMap::new();
Self { messages }
}

fn should_print_message(&mut self, timestamp: i32, message: String) -> bool {
if !self.messages.contains_key(&message) {
self.messages.insert(message, timestamp + 10);
return true;
}
let expired_timestamp = *self.messages.get(&message).unwrap();
if timestamp < expired_timestamp {
return false;
}
self.messages.insert(message, timestamp + 10);
return true;
}
}

/**
* Your Logger object will be instantiated and called as such:
* let obj = Logger::new();
* let ret_1: bool = obj.should_print_message(timestamp, message);
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_359() {
let mut obj = Logger::new();
assert_eq!(obj.should_print_message(1, "foo".to_string()), true);
assert_eq!(obj.should_print_message(2, "bar".to_string()), true);
assert_eq!(obj.should_print_message(3, "foo".to_string()), false);
assert_eq!(obj.should_print_message(8, "bar".to_string()), false);
assert_eq!(obj.should_print_message(10, "foo".to_string()), false);
assert_eq!(obj.should_print_message(11, "foo".to_string()), true);
}
}

```
