---
title: 57. insert interval
date: '2021-06-27'
tags: ['leetcode', 'rust', 'python', 'medium', 'interval']
draft: false
description: Solution for leetcode 0057 insert interval
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={57}/>
 

  You are given an array of non-overlapping intervals intervals where intervals[i] <TeX>=</TeX> [starti, endi] represent the start and the end of the i^th interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval <TeX>=</TeX> [start, end] that represents the start and end of another interval.

  Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

  Return intervals after the insertion.

   

 >   Example 1:

  

 >   Input: intervals <TeX>=</TeX> [[1,3],[6,9]], newInterval <TeX>=</TeX> [2,5]

 >   Output: [[1,5],[6,9]]

  

 >   Example 2:

  

 >   Input: intervals <TeX>=</TeX> [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval <TeX>=</TeX> [4,8]

 >   Output: [[1,2],[3,10],[12,16]]

 >   Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

 >   Example 3:

  

 >   Input: intervals <TeX>=</TeX> [], newInterval <TeX>=</TeX> [5,7]

 >   Output: [[5,7]]

  

 >   Example 4:

  

 >   Input: intervals <TeX>=</TeX> [[1,5]], newInterval <TeX>=</TeX> [2,3]

 >   Output: [[1,5]]

  

 >   Example 5:

  

 >   Input: intervals <TeX>=</TeX> [[1,5]], newInterval <TeX>=</TeX> [2,7]

 >   Output: [[1,7]]

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> intervals.length <TeX>\leq</TeX> 10^4

 >   	intervals[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> starti <TeX>\leq</TeX> endi <TeX>\leq</TeX> 10^5

 >   	intervals is sorted by starti in ascending order.

 >   	newInterval.length <TeX>=</TeX><TeX>=</TeX> 2

 >   	0 <TeX>\leq</TeX> start <TeX>\leq</TeX> end <TeX>\leq</TeX> 10^5


## Solution
Convert the problem to points insertion problem. 
### Python
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        points = []
        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]
            points.append((start, 0))
            points.append((end, 1))     
        def findInsertionIndex(points, item):
            if item <= points[0]:
                return 0
            if item >= points[-1]:
                return len(points)
            for i in range(1, len(points)):
                if points[i - 1] < item and item <= points[i]:
                    return i
            return -1
        #print(points)
        index = findInsertionIndex(points, (newInterval[0], 0))
        points.insert(index, (newInterval[0], 0))
        index = findInsertionIndex(points, (newInterval[1], 1))
        points.insert(index, (newInterval[1], 1))
        #print(points)
        ans = []
        count = 0
        for i in range(len(points)):
            if points[i][1] == 0:
                count += 1
            else:
                count -= 1
            if count == 1 and points[i][1] == 0: # Just start
                start = points[i][0]
            if count == 0 and points[i][1] == 1: # Just end
                end = points[i][0]
                ans.append([start, end])
        return ans
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        if intervals.len() == 0 {
            return vec![new_interval];
        }
        if intervals[0][0] > new_interval[1] { // if the end of new interval is smaller than all interval's start. 
            return [&(vec![new_interval])[..], &intervals[..]].concat();
        }
        if intervals[intervals.len() - 1][1] < new_interval[0] { // if the start of new interval is larger than all interval's end. 
            return [&intervals[..], &(vec![new_interval])[..]].concat();
        }
        let start = match (0..intervals.len()).into_iter().filter(|&i| intervals[i][1] < new_interval[0]).max() {
            Some(v) => {v + 1}
            None => {0}
        };
        let end = match (0..intervals.len()).into_iter().filter(|&i| intervals[i][0] > new_interval[1]).min() {
            Some(v) => {v - 1}
            None => {intervals.len() - 1}
        };
        let start_val = i32::min(intervals[start][0], new_interval[0]);
        let end_val = i32::max(intervals[end][1], new_interval[1]);
        let middle = vec![vec![start_val, end_val]];

        if start == 0 {
            [&middle, &intervals[end + 1..]].concat()
        } else if end == intervals.len() - 1 {
            [&intervals[..start], &middle].concat()
        } else {
            [&intervals[..start], &middle, &intervals[end + 1..]].concat()
        }
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_57() {
        
        assert_eq!(
            Solution::insert(
                vec![vec![1, 3], vec![6, 9]],
                vec![2, 5]
            ),
            vec![vec![1, 5], vec![6, 9]]
        );
        
        
        assert_eq!(
            Solution::insert(
                vec![
                    vec![1, 2],
                    vec![3, 5],
                    vec![6, 7],
                    vec![8, 10],
                    vec![12, 16]
                ],
                vec![4, 8]
            ),
            vec![
                vec![1, 2],
                vec![3, 10],
                vec![12, 16]
            ]
        );
        
        
        assert_eq!(
            Solution::insert(vec![vec![3, 4]], vec![1, 2]),
            vec![vec![1, 2], vec![3, 4]]
        );

        assert_eq!(
            Solution::insert(vec![vec![1, 2]], vec![3, 4]),
            vec![vec![1, 2], vec![3, 4]]
        );
        assert_eq!(
            Solution::insert(vec![vec![1, 2]], vec![2, 3]),
            vec![vec![1, 3]]
        );
        assert_eq!(
            Solution::insert(
                vec![vec![1, 2], vec![3, 4]],
                vec![0, 6]
            ),
            vec![vec![0, 6]]
        );

    }
}

```
