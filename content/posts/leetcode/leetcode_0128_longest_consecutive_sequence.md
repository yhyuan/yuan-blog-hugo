---
title: 128. longest consecutive sequence
date: '2021-09-04'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0128 longest consecutive sequence
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={128}/>
 

  Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

  You must write an algorithm that runs in O(n) time.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [100,4,200,1,3,2]

 >   Output: 4

 >   Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [0,3,7,2,5,8,4,6,0,1]

 >   Output: 9

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5

 >   	-10^9 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut max = 0;
        let nums = nums.into_iter().collect::<Vec<_>>();
        for &num in nums.iter() {
            if !nums.contains(&(num - 1)) {
                let mut curr = num;
                let mut curr_max = 1;
                while nums.contains(&(curr + 1)) {
                    curr += 1;
                    curr_max += 1;
                }
                max = i32::max(curr_max, max);
            }
        }
        max
    }
}
*/
use std::collections::HashMap;
impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut hashmap: HashMap<i32, usize> = HashMap::new();
        let mut max = i32::MIN;
        for &num in nums.iter() {
            if hashmap.contains_key(&num) {
                continue;
            }
            let left_num = num - 1;
            let right_num = num + 1;
            let left = if hashmap.contains_key(&left_num) {hashmap[&left_num]} else {0};
            let right = if hashmap.contains_key(&right_num) {hashmap[&right_num]} else {0};
            let new_length = left + right + 1;
            max = i32::max(max, new_length as i32);
            hashmap.insert(num, usize::MAX);
            hashmap.insert(num - left as i32, new_length); 
            hashmap.insert(num + right as i32, new_length); 
        }
        max
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_128() {
        assert_eq!(Solution::longest_consecutive(vec![100, 4, 200, 1, 3, 2]), 4)
    }
}

```
