---
title: 763. partition labels
date: '2022-05-11'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0763 partition labels
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={763}/>
 

  You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

  Return a list of integers representing the size of these parts.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "ababcbacadefegdehijhklij"

 >   Output: [9,7,8]

 >   Explanation:

 >   The partition is "ababcbaca", "defegde", "hijhklij".

 >   This is a partition so that each letter appears in at most one part.

 >   A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "eccbbbbdec"

 >   Output: [10]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 500

 >   	s consists of lowercase English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn merge(intervals: &Vec<(usize, usize)>, index: usize, res: &mut Vec<i32>) {
        let n = intervals.len();
        if index == n {
            return;
        }
        let mut interval = intervals[index];
        let mut next_index = usize::MAX;
        for k in index..n {
            interval = (interval.0, usize::max(interval.1, intervals[k].1));
            if k == n - 1 {
                next_index = k + 1;
                break;
            } 
            if interval.1 < intervals[k + 1].0 {
                next_index = k + 1;
                break;
            }                
        }
        res.push(interval.1 as i32 - interval.0 as i32 + 1);
        Self::merge(intervals, next_index, res);
    }

    pub fn partition_labels(s: String) -> Vec<i32> {
        let n = s.len();
        let chars = s.chars().collect::<Vec<_>>();
        //let mut starts_ends: [(usize, usize); 26] = [(usize::MAX, usize::MAX); 26];
        let mut starts_ends = vec![(usize::MAX, usize::MAX); 26];
        for i in 0..chars.len() {
            let index = chars[i] as usize - 'a' as usize;
            if starts_ends[index].0 == usize::MAX {
                starts_ends[index] = (i, i);
            } else {
                starts_ends[index] = (starts_ends[index].0, i);
            }
        }
        let mut intervals: Vec<(usize, usize)> = starts_ends.into_iter()
            .filter(|&v| v.0 != usize::MAX)
            .collect::<Vec<_>>();
        intervals.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
        let mut res: Vec<i32> = vec![];
        //println!("{:?}", intervals);
        Self::merge(&intervals, 0usize, &mut res); 
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_763() {
        assert_eq!(Solution::partition_labels("caedbdedda".to_string()), vec![1, 9]);
        assert_eq!(Solution::partition_labels("ababcbacadefegdehijhklij".to_string()), vec![9,7,8]);
    }
}

```
