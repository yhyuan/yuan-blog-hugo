---
title: 231. power of two
date: '2021-11-17'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0231 power of two
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={231}/>
 

  Given an integer n, return true if it is a power of two. Otherwise, return false.

  An integer n is a power of two, if there exists an integer x such that n <TeX>=</TeX><TeX>=</TeX> 2^x.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 1

 >   Output: true

 >   Explanation: 2^0 <TeX>=</TeX> 1

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 16

 >   Output: true

 >   Explanation: 2^4 <TeX>=</TeX> 16

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 3

 >   Output: false

  

 >   Example 4:

  

 >   Input: n <TeX>=</TeX> 4

 >   Output: true

  

 >   Example 5:

  

 >   Input: n <TeX>=</TeX> 5

 >   Output: false

  

   

  **Constraints:**

  

 >   	-2^31 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1

  

   

 >   Follow up: Could you solve it without loops/recursion?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/* 
impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let mut count_one = 0;
        for i in 0..32 {
            let r = (n >> i) & 1i32;
            if r == 1 {
                count_one += 1;
            }
        }
        count_one == 1
    }
}
*/
impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let mut count_one = 0;
        let mut n = n;
        for i in 0..32 {
            if n & 1i32 != 0 {
                count_one += 1;                
            }
            n = n >> 1;
        }
        count_one == 1
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_231() {
        assert_eq!(Solution::is_power_of_two(1), true);
        assert_eq!(Solution::is_power_of_two(16), true);
        assert_eq!(Solution::is_power_of_two(3), false);
        assert_eq!(Solution::is_power_of_two(4), true);
        assert_eq!(Solution::is_power_of_two(i32::MIN), false);
        assert_eq!(Solution::is_power_of_two(i32::MIN + 1), false);
    }
}

```
