---
title: 9. palindrome number
date: '2021-05-10'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0009 palindrome number
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={9}/>
 

  Given an integer x, return true if x is palindrome integer.

  An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

   

 >   Example 1:

  

 >   Input: x <TeX>=</TeX> 121

 >   Output: true

  

 >   Example 2:

  

 >   Input: x <TeX>=</TeX> -121

 >   Output: false

 >   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

  

 >   Example 3:

  

 >   Input: x <TeX>=</TeX> 10

 >   Output: false

 >   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

  

 >   Example 4:

  

 >   Input: x <TeX>=</TeX> -101

 >   Output: false

  

   

  **Constraints:**

  

 >   	-2^31 <TeX>\leq</TeX> x <TeX>\leq</TeX> 2^31 - 1

  

   

 >   Follow up: Could you solve it without converting the integer to a string?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return  false;
        }
        let mut v = x;
        let mut digits: Vec<i32> = vec![];
        while v > 0 {
            digits.push(v % 10);
            v = v / 10;
        }
        let mut v = 0;
        for i in 0..digits.len() {
            v = v * 10 + digits[i];
        }
        v == x
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_9() {
        assert_eq!(Solution::is_palindrome(-32), false);
        assert_eq!(Solution::is_palindrome(10), false);
        assert_eq!(Solution::is_palindrome(0), true);
        assert_eq!(Solution::is_palindrome(9), true);
        assert_eq!(Solution::is_palindrome(121), true);
        assert_eq!(Solution::is_palindrome(2222), true);
        assert_eq!(Solution::is_palindrome(11222211), true);
    }
}

```
