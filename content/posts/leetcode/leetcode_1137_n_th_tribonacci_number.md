---
title: 1137. n th tribonacci number
date: '2022-07-12'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1137 n th tribonacci number
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={1137}/>
 

  The Tribonacci sequence Tn is defined as follows: 

  

  T0 <TeX>=</TeX> 0, T1 <TeX>=</TeX> 1, T2 <TeX>=</TeX> 1, and Tn+3 <TeX>=</TeX> Tn + Tn+1 + Tn+2 for n ><TeX>=</TeX> 0.

  

  Given n, return the value of Tn.

  

   

 >   Example 1:

  

  

 >   Input: n <TeX>=</TeX> 4

 >   Output: 4

 >   Explanation:

 >   T_3 <TeX>=</TeX> 0 + 1 + 1 <TeX>=</TeX> 2

 >   T_4 <TeX>=</TeX> 1 + 1 + 2 <TeX>=</TeX> 4

  

  

 >   Example 2:

  

  

 >   Input: n <TeX>=</TeX> 25

 >   Output: 1389537

  

  

   

  **Constraints:**

  

  

 >   	0 <TeX>\leq</TeX> n <TeX>\leq</TeX> 37

 >   	The answer is guaranteed to fit within a 32-bit integer, ie. answer <TeX>\leq</TeX> 2^31 - 1.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        if n == 1 {
            return 1;
        }
        if n == 2 {
            return 1;
        }
        let mut t = (0, 1, 1);
        for i in 0..n-2 {
            t = (t.1, t.2, t.0 + t.1 + t.2)
        }
        t.2
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1137() {
        assert_eq!(Solution::tribonacci(4), 4);
        assert_eq!(Solution::tribonacci(25), 1389537);
    }
}

```
