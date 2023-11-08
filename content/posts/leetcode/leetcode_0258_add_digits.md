---
title: 258. add digits
date: '2021-12-02'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0258 add digits
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={258}/>
 

  Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

   

 >   Example 1:

  

 >   Input: num <TeX>=</TeX> 38

 >   Output: 2

 >   Explanation: The process is

 >   38 --> 3 + 8 --> 11

 >   11 --> 1 + 1 --> 2 

 >   Since 2 has only one digit, return it.

  

 >   Example 2:

  

 >   Input: num <TeX>=</TeX> 0

 >   Output: 0

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> num <TeX>\leq</TeX> 2^31 - 1

  

   

 >   Follow up: Could you do it without any loop/recursion in O(1) runtime?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn add_digits(num: i32) -> i32 {
        if num == 0 {
            return num;
        }
        let r = num % 9;
        if r == 0 {9} else {r}
        /*
        if num < 10 {
            return num;
        }
        let mut total = 0;
        let mut num = num;
        while num > 9 {
            total += num % 10;
            num = num / 10;
        }
        total += num;
        if total > 9 {Solution::add_digits(total)} else {total}
        */
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_258() {
        assert_eq!(Solution::add_digits(1234), 1);
    }
}

```
