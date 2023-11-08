---
title: 509. fibonacci number
date: '2022-03-23'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0509 fibonacci number
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={509}/>
 

  The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

  

  F(0) <TeX>=</TeX> 0, F(1) <TeX>=</TeX> 1

  F(n) <TeX>=</TeX> F(n - 1) + F(n - 2), for n > 1.

  

  Given n, calculate F(n).

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 2

 >   Output: 1

 >   Explanation: F(2) <TeX>=</TeX> F(1) + F(0) <TeX>=</TeX> 1 + 0 <TeX>=</TeX> 1.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 3

 >   Output: 2

 >   Explanation: F(3) <TeX>=</TeX> F(2) + F(1) <TeX>=</TeX> 1 + 1 <TeX>=</TeX> 2.

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 4

 >   Output: 3

 >   Explanation: F(4) <TeX>=</TeX> F(3) + F(2) <TeX>=</TeX> 2 + 1 <TeX>=</TeX> 3.

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> n <TeX>\leq</TeX> 30


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        if n == 1 {
            return 1;
        }
        let mut values = (0, 1);
        for _ in 2..=n {
            let n_2 = values.0;
            let n_1 = values.1;
            values = (n_1, n_1 + n_2);
        }
        values.1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_509() {
        assert_eq!(Solution::fib(2), 1);
        assert_eq!(Solution::fib(3), 2);
        assert_eq!(Solution::fib(4), 3);
    }
}

```
