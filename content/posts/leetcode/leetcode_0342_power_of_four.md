---
title: 342. power of four
date: '2022-01-15'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0342 power of four
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={342}/>
 

  Given an integer n, return true if it is a power of four. Otherwise, return false.

  An integer n is a power of four, if there exists an integer x such that n <TeX>=</TeX><TeX>=</TeX> 4^x.

   

 >   Example 1:

 >   Input: n <TeX>=</TeX> 16

 >   Output: true

 >   Example 2:

 >   Input: n <TeX>=</TeX> 5

 >   Output: false

 >   Example 3:

 >   Input: n <TeX>=</TeX> 1

 >   Output: true

   

  **Constraints:**

  

 >   	-2^31 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1

  

   

 >   Follow up: Could you solve it without loops/recursion?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let r = (n as f64).log10() / 4f64.log10();
        4u32.pow(r.ceil() as u32) == n as u32 || 4u32.pow(r.floor() as u32) == n as u32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_342() {
        assert_eq!(Solution::is_power_of_four(16), true);
        //assert_eq!(Solution::is_power_of_four(5), false);
        //assert_eq!(Solution::is_power_of_four(1), true);
    }
}

```
