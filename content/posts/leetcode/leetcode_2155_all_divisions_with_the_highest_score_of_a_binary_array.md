---
title: 2155. all divisions with the highest score of a binary array
date: '2022-09-11'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2155 all divisions with the highest score of a binary array
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2155}/>

You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <TeX>\leq</TeX> i <TeX>\leq</TeX> n) into two arrays (possibly empty) numsleft and numsright:



numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).

If i <TeX>=</TeX><TeX>=</TeX> 0, numsleft is empty, while numsright has all the elements of nums.

If i <TeX>=</TeX><TeX>=</TeX> n, numsleft has all the elements of nums, while numsright is empty.

The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.



Return all distinct indices that have the highest possible division score. You may return the answer in any order.



 



 > Example 1:



 > Input: nums <TeX>=</TeX> [0,0,1,0]

 > Output: [2,4]

 > Explanation: Division at index

 > - 0: numsleft is []. numsright is [0,0,1,0]. The score is 0 + 1 <TeX>=</TeX> 1.

 > - 1: numsleft is [0]. numsright is [0,1,0]. The score is 1 + 1 <TeX>=</TeX> 2.

 > - 2: numsleft is [0,0]. numsright is [1,0]. The score is 2 + 1 <TeX>=</TeX> 3.

 > - 3: numsleft is [0,0,1]. numsright is [0]. The score is 2 + 0 <TeX>=</TeX> 2.

 > - 4: numsleft is [0,0,1,0]. numsright is []. The score is 3 + 0 <TeX>=</TeX> 3.

 > Indices 2 and 4 both have the highest possible division score 3.

 > Note the answer [4,2] would also be accepted.

 > Example 2:



 > Input: nums <TeX>=</TeX> [0,0,0]

 > Output: [3]

 > Explanation: Division at index

 > - 0: numsleft is []. numsright is [0,0,0]. The score is 0 + 0 <TeX>=</TeX> 0.

 > - 1: numsleft is [0]. numsright is [0,0]. The score is 1 + 0 <TeX>=</TeX> 1.

 > - 2: numsleft is [0,0]. numsright is [0]. The score is 2 + 0 <TeX>=</TeX> 2.

 > - 3: numsleft is [0,0,0]. numsright is []. The score is 3 + 0 <TeX>=</TeX> 3.

 > Only index 3 has the highest possible division score 3.

 > Example 3:



 > Input: nums <TeX>=</TeX> [1,1]

 > Output: [0]

 > Explanation: Division at index

 > - 0: numsleft is []. numsright is [1,1]. The score is 0 + 2 <TeX>=</TeX> 2.

 > - 1: numsleft is [1]. numsright is [1]. The score is 0 + 1 <TeX>=</TeX> 1.

 > - 2: numsleft is [1,1]. numsright is []. The score is 0 + 0 <TeX>=</TeX> 0.

 > Only index 0 has the highest possible division score 2.

 



**Constraints:**



 > n <TeX>=</TeX><TeX>=</TeX> nums.length

 > 1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 105

 > nums[i] is either 0 or 1.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

use std::collections::HashSet;
use std::iter::FromIterator;
impl Solution {
    pub fn max_score_indices(nums: Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let mut v = (0, 0);
    let mut counts: Vec<(i32, i32)> = vec![];
    for i in 0..n {
        v = if nums[i] == 0 {
            (v.0 + 1, v.1)
        } else {
            (v.0, v.1 + 1)
        };
        counts.push(v);
    }
    // println!("{:?}", counts);
    let mut highest_score = counts[n - 1].1;
    let mut result: Vec<i32> = vec![0];
    for i in 0..n {
        let left = counts[i].0;
        let right = counts[n - 1].1 - counts[i].1;
        let score = left + right;
        // println!("i: {}, score: {}", i + 1, score);
        if highest_score == score {
            result.push(i as i32 + 1);
        } else if highest_score < score {
            highest_score = score;
            result = vec![i as i32 + 1];
        }
    }
    // println!("{}", highest_score);
    result        
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2155() {
        assert_eq!(Solution::max_score_indices(vec![0, 0, 1, 0]),vec![2, 4]);        
        assert_eq!(Solution::max_score_indices(vec![0, 0, 0]),vec![3]);        
        assert_eq!(Solution::max_score_indices(vec![1, 1]),vec![0]);        
    }
}
```
