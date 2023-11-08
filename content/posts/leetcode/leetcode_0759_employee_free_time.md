---
title: 759. employee free time
date: '2022-05-10'
tags: ['leetcode', 'rust', 'hard', 'interval']
draft: false
description: Solution for leetcode 0759 employee free time
---


We are given a list schedule of employees, which represents the working time for each employee.



Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.



Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.



(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start <TeX>=</TeX> 1, schedule[0][0].end <TeX>=</TeX> 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.



 



 > Example 1:



 > Input: schedule <TeX>=</TeX> [[[1,2],[5,6]],[[1,3]],[[4,10]]]

 > Output: [[3,4]]

 > Explanation: There are a total of three employees, and all common

 > free time intervals would be [-inf, 1], [3, 4], [10, inf].

 > We discard any intervals that contain inf as they aren't finite.

 > Example 2:



 > Input: schedule <TeX>=</TeX> [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]

 > Output: [[5,6],[7,9]]

 



**Constraints:**



 > 1 <TeX>\leq</TeX> schedule.length , schedule[i].length <TeX>\leq</TeX> 50

 > 0 <TeX>\leq</TeX> schedule[i].start < schedule[i].end <TeX>\leq</TeX> 10^8


## Solution
### Python
```python
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        points = []
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                start = schedule[i][j].start
                end   = schedule[i][j].end
                points.append((end, 0))
                points.append((start, 1))
        points.sort()
        count = 0
        ans = []
        start = -1
        end = -1
        for i in range(len(points)):
            if points[i][1] == 1: # start
                count += 1
            else: # end
                count -= 1
            if count == 0 and points[i][1] == 0: # we just end
                start = points[i][0]
            if count == 1 and points[i][1] == 1: # we just start
                end = points[i][0]
                if start < end and start != -1:
                    ans.append(Interval(start, end))
        return ans
```
### Rust
```rust
 pub struct Solution {}

 // problem: https://leetcode.com/problems/employee-free-time/
 // discuss: https://leetcode.com/problems/employee-free-time/discuss/?currentPage=1&orderBy=most_votes&query=
 
 // submission codes start here
 
// Definition for an Interval.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct Interval {
    pub start:i32,
    pub end:i32
}

impl Interval {
    #[inline]
    fn new(start:i32, end:i32) -> Self{
        Interval {
            start,
            end
        }
    }
}


impl Solution {
    pub fn employee_free_time(schedule: Vec<Vec<Interval>>) -> Vec<Interval> {
        let mut nodes: Vec<(i32, i32)> = vec![];
        let n = schedule.len();
        for i in 0..n {
            let m = schedule[i].len();
            for j in 0..m {
                nodes.push((schedule[i][j].start, 0));
                nodes.push((schedule[i][j].end, 1));
            }
        }
        nodes.sort();
        let mut intervals_count = 0;
        let mut free_time_start = i32::MAX;
        let mut res: Vec<Interval> = vec![];
        for i in 0..nodes.len() {
            if nodes[i].1 == 0 {
                intervals_count += 1;
            } else {
                intervals_count -= 1;
            }
            if intervals_count == 0 {
                free_time_start = nodes[i].0;
            } else if free_time_start != i32::MAX {
                res.push(Interval::new(free_time_start, nodes[i].0));
                free_time_start = i32::MAX;
            }
        }
        res
    }
}
 // submission codes end
 
 #[cfg(test)]
 mod tests {
     use super::*;
 
     #[test]
     fn test_759() {
         assert_eq!(Solution::employee_free_time(vec![
            vec![Interval::new(1, 2), Interval::new(5, 6)],
            vec![Interval::new(1, 3)],
            vec![Interval::new(4, 10)]
        ]), vec![Interval::new(3, 4)]);
        assert_eq!(Solution::employee_free_time(vec![
            vec![Interval::new(1, 3), Interval::new(6, 7)],
            vec![Interval::new(2, 4)],
            vec![Interval::new(2, 5), Interval::new(9, 12)]
        ]), vec![Interval::new(5, 6), Interval::new(7, 9)]);
        //assert_eq!(Solution::employee_free_time(vec![vec![Interval::new(1, 3), Interval::new(6, 7)]],vec![Interval::new(2, 4)]]), vec![Interval::new(3, 4)]);
    }
 }
 
```
