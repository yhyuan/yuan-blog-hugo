---
title: 371. sum of two integers
date: '2022-01-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0371 sum of two integers
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={371}/>
 

  Given two integers a and b, return the sum of the two integers without using the operators + and -.

   

 >   Example 1:

 >   Input: a <TeX>=</TeX> 1, b <TeX>=</TeX> 2

 >   Output: 3

 >   Example 2:

 >   Input: a <TeX>=</TeX> 2, b <TeX>=</TeX> 3

 >   Output: 5

   

  **Constraints:**

  

 >   	-1000 <TeX>\leq</TeX> a, b <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        if b == 0 {
            return a;
        }
        //println!("a: {:b}, b: {:b}", a, b);
        let x = a ^ b; //adding without carry.
        let y = (a & b) << 1; //adding with carry
        Self::get_sum(x, y)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_371() {
        assert_eq!(Solution::get_sum(1, 2), 3);
        assert_eq!(Solution::get_sum(-2, 3), 1);
    }
}

```
