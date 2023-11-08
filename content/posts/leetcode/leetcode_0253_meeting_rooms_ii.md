---
title: 253. meeting rooms ii
date: '2021-11-28'
tags: ['leetcode', 'rust', 'medium', 'interval']
draft: false
description: Solution for leetcode 0253 meeting rooms ii
---

Given an array of meeting time intervals intervals where intervals[i] <TeX>=</TeX> [starti, endi], return the minimum number of conference rooms required.
 > Example 1:



 > Input: intervals <TeX>=</TeX> [[0,30],[5,10],[15,20]]

 > Output: 2

 > Example 2:



 > Input: intervals <TeX>=</TeX> [[7,10],[2,4]]

 > Output: 1

 



**Constraints:**



 > 1 <TeX>\leq</TeX> intervals.length <TeX>\leq</TeX> 104

 > 0 <TeX>\leq</TeX> starti < endi <TeX>\leq</TeX> 106


## Solution
We can add the starting and ending position with its types to an array. We can assign the ending's type is 0 and the starting's type is 1 to make sure when they are the same position. The ending point will be sorted in front of the starting. We sort these positions and iterate these positions. If we have starting position, we just add one more room. If we have an ending position, we just remove one room. Then, we check the max room during this process.
### Python
```python
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
  n = len(intervals)
  points = []
  for i in range(n):
    start = intervals[i][0]
    end   = intervals[i][1]
    # 1 for starting point
    points.append((start, 1))
    # 0 for ending points. 
    points.append((end, 0)) 
  points.sort()
  rooms = 0
  ans = 0
  for i in range(len(points)):
    if points[i][1] == 1:
      rooms += 1
    else:
      rooms -= 1
    ans = max(rooms, ans)
  return ans
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
//use std::collections::HashMap;
impl Solution {
    pub fn min_meeting_rooms(intervals: Vec<Vec<i32>>) -> i32 {
        let mut nodes: Vec<(i32, i32)> = vec![];
        let n = intervals.len();
        for i in 0..n {
            nodes.push((intervals[i][0], 1)); // start
            nodes.push((intervals[i][1], 0)); // end
        }
        nodes.sort();
        let mut current_rooms = 0;
        let mut max_rooms = 0;
        for i in 0..nodes.len() {
            let (x, start_end) = nodes[i];
            if start_end == 1 {
                current_rooms += 1;
            } else {
                current_rooms -= 1;
            }
            max_rooms = i32::max(max_rooms, current_rooms);
        }
        max_rooms
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_253() {
        assert_eq!(Solution::min_meeting_rooms(vec![vec![0,30], vec![5,10], vec![15,20]]), 2);
        assert_eq!(Solution::min_meeting_rooms(vec![vec![7,10], vec![2,4]]), 1);
    }
}

```
