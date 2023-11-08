---
title: 729. my calendar i
date: '2022-05-02'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0729 my calendar i
---

 

  You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

  A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

  The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <TeX>\leq</TeX> x < end.

  Implement the MyCalendar class:

  

  	MyCalendar() Initializes the calendar object.

  	boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

  

   

 >   Example 1:

  

 >   Input

 >   ["MyCalendar", "book", "book", "book"]

 >   [[], [10, 20], [15, 25], [20, 30]]

 >   Output

 >   [null, true, false, true]

 >   Explanation

 >   MyCalendar myCalendar <TeX>=</TeX> new MyCalendar();

 >   myCalendar.book(10, 20); // return True

 >   myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.

 >   myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> start < end <TeX>\leq</TeX> 10^9

 >   	At most 1000 calls will be made to book.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

struct MyCalendar {
    events: Vec<(i32, i32)>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendar {

    fn new() -> Self {
        let events: Vec<(i32, i32)> = vec![];
        Self { events: events }
    }
    
    fn book(&mut self, start: i32, end: i32) -> bool {
        if self.events.len() == 0 {
            self.events.push((start, end));
            return true;
        }
        if end <= self.events[0].0 {
            self.events.insert(0, (start, end));
            return true;
        }
        if start >= self.events[self.events.len() - 1].1 {
            self.events.push((start, end));
            return true;
        }
        if start >= self.events[self.events.len() - 1].0 {
            return false;
        }
        // start < self.events[high].start
        // start >
        let mut low = 0;
        let mut high = self.events.len() - 1;
        while low + 1 < high {
            let mid = low + (high - low) / 2;
            if self.events[mid].0 > start {
                high = mid;
            } else {
                low = mid;
            }
        }
        if self.events[low].1 <= start && self.events[low + 1].0 >= end {
            self.events.insert(low + 1, (start, end));
            return true;
        }
        false
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar::new();
 * let ret_1: bool = obj.book(start, end);
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_729() {
        let mut obj = MyCalendar::new();
        assert_eq!(obj.book(10, 20), true);
        assert_eq!(obj.book(15, 25), false);
        assert_eq!(obj.book(20, 30), true);
       
    }
}

```
