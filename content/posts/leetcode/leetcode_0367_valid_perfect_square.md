---
title: 367. valid perfect square
date: '2022-01-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0367 valid perfect square
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={367}/>
 

  Given a positive integer num, write a function which returns True if num is a perfect square else False.

  Follow up: Do not use any built-in library function such as sqrt.

   

 >   Example 1:

 >   Input: num <TeX>=</TeX> 16

 >   Output: true

 >   Example 2:

 >   Input: num <TeX>=</TeX> 14

 >   Output: false

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> num <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        if num == 1 {
            return true;
        }
        let mut start = 0; 
        let mut end = num - 1;
        while start + 1 < end {
            println!("start: {}, end: {}", start, end);
            let mid = (end + start) / 2;
            let square = mid * mid;
            if square == num {
                return true;
            }
            if square > num {
                end = mid;
            } else {
                start = mid;
            }
        }
        start * start == num || end * end == num
    }
}
//1, 4, 9, 16, 25, 36, 49, 64, 81 10x + y 100x^2 + 20x*y + y^2
//1, 4, 9, 6, 5
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_367() {
        assert_eq!(Solution::is_perfect_square(16), true);
        assert_eq!(Solution::is_perfect_square(14), false);
    }
}

```
