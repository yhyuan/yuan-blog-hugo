---
title: 435. non overlapping intervals
date: '2022-03-11'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0435 non overlapping intervals
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={435}/>
 

  Given an array of intervals intervals where intervals[i] <TeX>=</TeX> [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

   

 >   Example 1:

  

 >   Input: intervals <TeX>=</TeX> [[1,2],[2,3],[3,4],[1,3]]

 >   Output: 1

 >   Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

  

 >   Example 2:

  

 >   Input: intervals <TeX>=</TeX> [[1,2],[1,2],[1,2]]

 >   Output: 2

 >   Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

  

 >   Example 3:

  

 >   Input: intervals <TeX>=</TeX> [[1,2],[2,3]]

 >   Output: 0

 >   Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> intervals.length <TeX>\leq</TeX> 10^5

 >   	intervals[i].length <TeX>=</TeX><TeX>=</TeX> 2

 >   	-5  10^4 <TeX>\leq</TeX> starti < endi <TeX>\leq</TeX> 5  10^4


## Solution
Let's sort the intervals according to its starting point.  Then we define the dp[i] as at index i, we maximally can have dp[i] intervals if we keep interval i. 
### Python
```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #  dp[i] stores the maximum number of valid intervals that can be included in the final list if the intervals upto the
        #  i thinterval only are considered,
        # dp[i + 1]: we will have examine from 0 to i. Test whether i + 1 interval intersect with j or not. We calculate the max result. 
        # dp[i + 1] = max(dp[j]) + 1 interval j does not intersect with i + 1
        intervals = list(map(lambda interval: (interval[0], interval[1]), intervals))
        intervals.sort()
        def intersect(i, j):
            # j is smaller than i
            return intervals[i][0] < intervals[j][1]

        n = len(intervals)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            # dp[i]
            for j in range(i):
                if not intersect(i, j):
                    dp[i] = max(dp[j], dp[i])
            dp[i] += 1
        return n - dp[-1]
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
    pub fn overlapping(pre_interval: &Vec<i32>, post_interval: &Vec<i32>) -> bool {
        pre_interval[1] > post_interval[0]
    }
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let n = intervals.len();
        if n == 0 {
            return 0i32;
        }
        let mut intervals = intervals;
        intervals.sort_by(|a, b| a[0].partial_cmp(&b[0]).unwrap());
        let mut dp: Vec<i32> = vec![0; n];
        // println!("intervals{:?}", intervals);
        //stores the maximum number of valid intervals that can be included in the final list if the intervals upto the i^{th}i 
// th  interval only are considered, including itself. 
        dp[0] = 1;
        //let mut res = 1;
        for i in 1..n {
            let mut max = 0;
            for j in (0..=i - 1).rev() {
                if dp[j] <= max {
                    break;
                }
                if !Self::overlapping(&intervals[j], &intervals[i]) {
                    max = dp[j];
                }
            }
            dp[i] = max + 1;
        }
        //println!("dp: {:?}", dp);
        //n as i32 - dp.into_iter().max().unwrap()
        n as i32 - dp[n - 1]
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_435() {
        assert_eq!(Solution::erase_overlap_intervals(vec![vec![1,2],vec![2,3],vec![3,4],vec![1,3]]), 1);
    }
}

```
