---
title: 263. ugly number
date: '2021-12-05'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0263 ugly number
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={263}/>
 

  An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

  Given an integer n, return true if n is an ugly number.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 6

 >   Output: true

 >   Explanation: 6 <TeX>=</TeX> 2 &times; 3

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 8

 >   Output: true

 >   Explanation: 8 <TeX>=</TeX> 2 &times; 2 &times; 2

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 14

 >   Output: false

 >   Explanation: 14 is not ugly since it includes the prime factor 7.

  

 >   Example 4:

  

 >   Input: n <TeX>=</TeX> 1

 >   Output: true

 >   Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

  

   

  **Constraints:**

  

 >   	-2^31 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_ugly(n: i32) -> bool {
        if n == 0 {
            return false;
        }
        let mut n = n;
        while n % 5 == 0 {
            n = n / 5;
        }
        while n % 3 == 0 {
            n = n / 3;
        }
        while n % 2 == 0 {
            n = n / 2;
        }

        n == 1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_263() {
        assert_eq!(Solution::is_ugly(6), true);
        assert_eq!(Solution::is_ugly(8), true);
        assert_eq!(Solution::is_ugly(14), false);
        assert_eq!(Solution::is_ugly(1), true);
    }
}

```
