---
title: 201. bitwise and of numbers range
date: '2021-10-18'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0201 bitwise and of numbers range
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={201}/>
 

  Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

   

 >   Example 1:

  

 >   Input: left <TeX>=</TeX> 5, right <TeX>=</TeX> 7

 >   Output: 4

  

 >   Example 2:

  

 >   Input: left <TeX>=</TeX> 0, right <TeX>=</TeX> 0

 >   Output: 0

  

 >   Example 3:

  

 >   Input: left <TeX>=</TeX> 1, right <TeX>=</TeX> 2147483647

 >   Output: 0

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> left <TeX>\leq</TeX> right <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn get_bit(x: i32, pos: u8) -> i32 {
        x >> pos & 1i32
    }
    pub fn set_bit(x: i32, pos: u8, bit: i32) -> i32 {
        if bit == 1i32 {
            1i32 << pos | x
        } else {
            !(1i32 << pos) & x
        }
    }
    pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
        let mut result = 0i32;
        let mut diff_start = false;
        for i in (0..32u8).rev() { //31, 30, 29, ....... 0
            let left_bit = Solution::get_bit(left, i);
            let right_bit = Solution::get_bit(right, i);
            if left_bit != right_bit {
                result = Solution::set_bit(result, i, 0i32);
                diff_start = true;
            } else {
                if diff_start {
                    result = Solution::set_bit(result, i, 0i32);
                } else {
                    result = Solution::set_bit(result, i, left_bit);
                }
            }
        }
        result
        /*
        let mut res = left;
        for num in left..=right {
            res = res & num;
        }
        res
        */
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_201() {
        assert_eq!(Solution::range_bitwise_and(5, 7), 4);
    }
}

```
