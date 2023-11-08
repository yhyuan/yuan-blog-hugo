---
title: 352. data stream as disjoint intervals
date: '2022-01-22'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0352 data stream as disjoint intervals
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={352}/>
 

  Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

  Implement the SummaryRanges class:

  

  	SummaryRanges() Initializes the object with an empty stream.

  	void addNum(int val) Adds the integer val to the stream.

  	int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi].

  

   

 >   Example 1:

  

 >   Input

 >   ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]

 >   [[], [1], [], [3], [], [7], [], [2], [], [6], []]

 >   Output

 >   [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

 >   Explanation

 >   SummaryRanges summaryRanges <TeX>=</TeX> new SummaryRanges();

 >   summaryRanges.addNum(1);      // arr <TeX>=</TeX> [1]

 >   summaryRanges.getIntervals(); // return [[1, 1]]

 >   summaryRanges.addNum(3);      // arr <TeX>=</TeX> [1, 3]

 >   summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]

 >   summaryRanges.addNum(7);      // arr <TeX>=</TeX> [1, 3, 7]

 >   summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]

 >   summaryRanges.addNum(2);      // arr <TeX>=</TeX> [1, 2, 3, 7]

 >   summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]

 >   summaryRanges.addNum(6);      // arr <TeX>=</TeX> [1, 2, 3, 6, 7]

 >   summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> val <TeX>\leq</TeX> 10^4

 >   	At most 3  10^4 calls will be made to addNum and getIntervals.

  

   

 >   Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

pub struct SummaryRanges {
    intervals: Vec<Vec<i32>>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SummaryRanges {

    /** Initialize your data structure here. */
    pub fn new() -> Self {
        let intervals: Vec<Vec<i32>> = vec![];
        SummaryRanges {
            intervals
        }
    }
    
    pub fn add_num(&mut self, val: i32) {
        if self.intervals.is_empty() {
            self.intervals = vec![vec![val, val]];
            return;
        }
        if val < self.intervals[0][0] - 1 {
            self.intervals.insert(0, vec![val, val]);
            return;
        }
        if val == self.intervals[0][0] - 1 {
            self.intervals[0][0] = val;
            return;
        }
        let n = self.intervals.len();
        if val > self.intervals[n - 1][1] + 1 {
            self.intervals.push(vec![val, val]);
            return;
        }
        if val == self.intervals[n - 1][1] + 1 {
            self.intervals[n - 1][1] = val;
            return;
        }
        let mut low = 0;
        let mut high = n - 1;
        while low + 1 < high {
            let mid = low + (high - low) / 2;
            let mid_interval = &self.intervals[mid];
            if val >= mid_interval[0] && val <= mid_interval[1] {
                return;
            } else if val == mid_interval[0] - 1 {
                if mid > 0 && self.intervals[mid - 1][1] == val - 1{
                    self.intervals[mid - 1][1] = mid_interval[1];
                    self.intervals.remove(mid);
                } else {
                    self.intervals[mid][0] = val;
                }
                return;
            } else if val == mid_interval[1] + 1 {
                if mid < n - 1 && self.intervals[mid + 1][0] == val + 1{
                    self.intervals[mid + 1][0] = mid_interval[0];
                    self.intervals.remove(mid);
                } else {
                    self.intervals[mid][1] = val;
                }
                return;
            } else if val < mid_interval[0] - 1 {
                high = mid;
            } else {
                low = mid;
            }
        }
        if val <= self.intervals[low][1] || val >= self.intervals[low + 1][0] {
            return;
        } else {
            if self.intervals[low + 1][0] == self.intervals[low][1] + 2 {
                //if val == self.intervals[low][1] + 1 {
                    self.intervals[low][1] = self.intervals[low + 1][1];
                    self.intervals.remove(low + 1);
                //} else {

                //}
            } else {
                if self.intervals[low][1] + 1 == val {
                    self.intervals[low][1] = val;
                } else if self.intervals[low + 1][0] - 1 == val {
                    self.intervals[low + 1][0] = val;
                } else {
                    self.intervals.insert(low + 1, vec![val, val]);
                }
            }
        }
    }
    
    pub fn get_intervals(&self) -> Vec<Vec<i32>> {
        self.intervals.clone()
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * let obj = SummaryRanges::new();
 * obj.add_num(val);
 * let ret_2: Vec<Vec<i32>> = obj.get_intervals();
 */

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_352() {
        let mut summary_ranges = SummaryRanges::new();
        summary_ranges.add_num(1);      // arr = [1]
        assert_eq!(summary_ranges.get_intervals(), vec![vec![1, 1]]); // return [[1, 1]]
        summary_ranges.add_num(3);      // arr = [1, 3]
        assert_eq!(summary_ranges.get_intervals(), vec![vec![1, 1], vec![3, 3]]); // return [[1, 1], [3, 3]]
        summary_ranges.add_num(7);      // arr = [1, 3, 7]
        assert_eq!(summary_ranges.get_intervals(), vec![vec![1, 1], vec![3, 3], vec![7, 7]]); // return [[1, 1], [3, 3], [7, 7]]
        summary_ranges.add_num(2);      // arr = [1, 2, 3, 7]
        assert_eq!(summary_ranges.get_intervals(), vec![vec![1, 3], vec![7, 7]]); // return [[1, 3], [7, 7]]
        summary_ranges.add_num(6);      // arr = [1, 2, 3, 6, 7]
        assert_eq!(summary_ranges.get_intervals(), vec![vec![1, 3], vec![6, 7]]); // return [[1, 3], [6, 7]]
    }
}

```
