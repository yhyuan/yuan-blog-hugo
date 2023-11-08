---
title: 172. factorial trailing zeroes
date: '2021-10-06'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0172 factorial trailing zeroes
---

 

  Given an integer n, return the number of trailing zeroes in n!.

  Follow up: Could you write a solution that works in logarithmic time complexity?

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 3

 >   Output: 0

 >   Explanation: 3! <TeX>=</TeX> 6, no trailing zero.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 5

 >   Output: 1

 >   Explanation: 5! <TeX>=</TeX> 120, one trailing zero.

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 0

 >   Output: 0

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn trailing_zeroes(n: i32) -> i32 {
        let mut n = n;
        let mut result = 0;
        while n >= 5 {
            result += n / 5;
            n = n / 5;
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_172() {
        assert_eq!(Solution::trailing_zeroes(3), 0);
        assert_eq!(Solution::trailing_zeroes(5), 1);
        assert_eq!(Solution::trailing_zeroes(20), 4);
        assert_eq!(Solution::trailing_zeroes(1808548329), 452137076);
    }
}

```
