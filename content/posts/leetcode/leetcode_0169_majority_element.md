---
title: 169. majority element
date: '2021-10-04'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0169 majority element
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={169}/>
 

  Given an array nums of size n, return the majority element.

  The majority element is the element that appears more than &lfloor;n / 2&rfloor; times. You may assume that the majority element always exists in the array.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [3,2,3]

 >   Output: 3

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [2,2,1,1,1,2,2]

 >   Output: 2

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> nums.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 5  10^4

 >   	-2^31 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1

  

   

 >   Follow-up: Could you solve the problem in linear time and in O(1) space?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/* 
use std::collections::HashMap;
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut hashmap: HashMap<i32, usize> = HashMap::new();
        for num in nums.iter() {
            if hashmap.contains_key(num) {
                hashmap.insert(*num, hashmap[num] + 1);
            } else {
                hashmap.insert(*num, 1);
            }
        }
        for (&k, &v) in hashmap.iter() {
            if v > n / 2 {
                return k;
            }
        }
        0
    }
}
*/
impl Solution {
    pub fn count_bit(nums: &Vec<i32>, bit_pos: usize) -> bool {
        let count_1 = nums.iter().map(|&num| (num >> bit_pos) & 1i32).filter(|&v| v == 1).count();
        let count_0 = nums.len() - count_1;
        if count_1 > count_0 {true} else {false}
    }
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut result = 0i32;
        for i in 0..32 {
            let res = Solution::count_bit(&nums, i);
            if res {
                result = (1i32 << i) | result; 
            } else {
                result = !(1i32 << i) & result; 
            }
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_169() {
        assert_eq!(Solution::majority_element(vec![3,2,3]), 3);
        assert_eq!(Solution::majority_element(vec![2,2,1,1,1,2,2]), 2);
    }
}

```
