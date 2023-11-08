---
title: 715. range module
date: '2022-04-30'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0715 range module
---



A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <TeX>\leq</TeX> x < right.

Implement the RangeModule class:



RangeModule() Initializes the object of the data structure.

void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.

boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.

void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).





>   Example 1:
>   Input
>   ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
>   [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
>   Output
>   [null, null, null, true, false, true]
>   Explanation
>   RangeModule rangeModule <TeX>=</TeX> new RangeModule();
>   rangeModule.addRange(10, 20);
>   rangeModule.removeRange(14, 16);
>   rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
>   rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
>   rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
**Constraints:**
>   	1 <TeX>\leq</TeX> left < right <TeX>\leq</TeX> 10^9
>   	At most 10^4 calls will be made to addRange, queryRange, and removeRange.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::BTreeMap;
/**
*
* Digested explanation after reading some posts... [Python]
1
user9051K's avatar
user9051K

6
Last Edit: July 13, 2022 8:51 PM

48 VIEWS

I had a hard time understanding the solution. So I digested the explanation in a number of posts as concise comments.

We use one array to track all intervals. Some invariants we keep about this array:

1) Even index is start of interval. Odd index is end of interval
2) Intervals are in order. No overlap (we merge them).
3) len(array) is always even
With that in mind, you can understand the code with comments

from bisect import bisect_left as bl, bisect_right as br
class RangeModule:

def __init__(self):
self._X = []

def addRange(self, left: int, right: int) -> None:


# Main Logic


#   If idx(left) or idx(right) is odd, it's in a interval. So don't add it.


#   If idx(left) or idx(right) is even, it's not in any interval. So add it as new interval


#   Slice array[idx(left) : idx(right)]


#       1) both odd: Nothing is added. Merge all middle intervals.


#       2) both even: Add new intervals. Merge all middle intervals


#       3) idx(left) is even: update start point of next interval with left


#       4) idx(right) is even: update end point of previous interval with right


# Bisect_left vs. Bisect_right


#   left need to proceed all interval closing at left, so use Bisect_left


#   right need to go after all interval openning at right, so use Bisect_right
i, j = bl(self._X, left), br(self._X, right)
self._X[i : j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)


def queryRange(self, left: int, right: int) -> bool:


# Main logic


#   If idx of left/right is odd, it's in a interval. Else it's not.


#   If idx of left&right is the same, they're in the same interval


# Bisect_left vs. Bisect_right


#   [start, end). Start is included. End is not.


#   so use bisect_right for left


#   so use bisect_left for right
i, j = br(self._X, left), bl(self._X, right)
return i == j and i % 2 == 1


def removeRange(self, left: int, right: int) -> None:


# Main Logic


#   If idx(left) is odd, the interval that contains left need to change end point to left


#   If idx(right) is odd, the interval that contains right need to change start point to right


#   Else, everything from idx(left) to idx(right) is removed. Nothing is changed.


# Bisect_left vs. Bisect_right


#   Same as addRange
i, j = bl(self._X, left), br(self._X, right)
self._X[i : j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)
*/
//use std::collections::{BTreeMap, LinkedList};




#[derive(Debug)]
struct RangeModule {
intervals: BTreeMap<i32, i32>,
}

impl RangeModule {
fn new() -> Self {
RangeModule {
intervals: BTreeMap::new(),
}
}

fn add_range(&mut self, mut left: i32, mut right: i32) {
if let Some((bgn, end)) = self.intervals.range(..=left).next_back() {
println!("bgn: {}, end: {}", bgn, end);
if *end >= left {
left = i32::min(left, *bgn)
}
}

if let Some((_, end)) = self.intervals.range(..=right).next_back() {
if left < *end {
right = i32::max(right, *end)
}
}

let mut new_intervals: BTreeMap<i32, i32> = self
.intervals
.clone()
.into_iter()
.filter(|(bgn, _)| *bgn < left || *bgn > right)
.collect();
new_intervals.insert(left, right);

self.intervals = new_intervals;
}

fn query_range(&self, left: i32, right: i32) -> bool {
match self.intervals.range(..=left).next_back() {
Some((_, end)) => *end >= right,
None => false,
}
}

fn remove_range(&mut self, left: i32, right: i32) {
if let Some((_, end)) = self.intervals.range(..=right).next_back() {
if *end > right {
self.intervals.insert(right, *end);
}
}

if let Some((_, end)) = self.intervals.range_mut(..=left).next_back() {
if *end > left {
*end = left;
}
}

let new_intervals: BTreeMap<i32, i32> = self
.intervals
.clone()
.into_iter()
.filter(|(bgn, _)| *bgn < left || *bgn >= right)
.collect();

self.intervals = new_intervals;
}
}

/**
* Your RangeModule object will be instantiated and called as such:
* let obj = RangeModule::new();
* obj.add_range(left, right);
* let ret_2: bool = obj.query_range(left, right);
* obj.remove_range(left, right);
*/

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_715() {
let mut obj = RangeModule::new();
obj.add_range(10, 20);
obj.remove_range(14, 16);
assert_eq!(obj.query_range(10, 14), true);
assert_eq!(obj.query_range(13, 15), false);
assert_eq!(obj.query_range(16, 17), true);
}
}

```
