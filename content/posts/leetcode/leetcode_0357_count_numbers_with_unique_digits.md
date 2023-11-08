---
title: 357. count numbers with unique digits
date: '2022-01-23'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0357 count numbers with unique digits
---

 

  Given an integer n, return the count of all numbers with unique digits, x, where 0 <TeX>\leq</TeX> x < 10^n.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 2

 >   Output: 91

 >   Explanation: The answer should be the total numbers in the range of 0 &le; x < 100, excluding 11,22,33,44,55,66,77,88,99

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 0

 >   Output: 1

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> n <TeX>\leq</TeX> 8


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn count_numbers_with_unique_digits(n: i32) -> i32 {
        if n == 0 {
            return 1;
        }
        if n == 1 {
            return 10;
        }
        let mut result = 9;
        for i in 0..n - 1 {
            result = result * (9 - i);
        }
        result + Self::count_numbers_with_unique_digits(n - 1)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_357() {
        assert_eq!(Solution::count_numbers_with_unique_digits(2), 91);
        assert_eq!(Solution::count_numbers_with_unique_digits(1), 10);
        assert_eq!(Solution::count_numbers_with_unique_digits(0), 1);
    }
}

```
