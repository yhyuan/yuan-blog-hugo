---
title: 788. rotated digits
date: '2022-05-18'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0788 rotated digits
---

 

  An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

  A number is valid if each digit remains a digit after rotation. For example:

  

  	0, 1, and 8 rotate to themselves,

  	2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),

  	6 and 9 rotate to each other, and

  	the rest of the numbers do not rotate to any other number and become invalid.

  

  Given an integer n, return the number of good integers in the range [1, n].

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 10

 >   Output: 4

 >   Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.

 >   Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 1

 >   Output: 0

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 2

 >   Output: 1

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_good(n: i32) -> bool {
        let mut rotation: Vec<usize> = vec![0, 1, 5, usize::MAX, usize::MAX, 2, 9, usize::MAX, 8, 6];
        let mut digits: Vec<usize> = vec![];
        let mut res = n;
        while res > 0 {
            let d = rotation[(res % 10) as usize];
            if d == usize::MAX {
                return false;
            }
            digits.push(d);
            res = res / 10;
        }
        digits.reverse();
        let mut ans = 0;
        let len = digits.len();
        for i in 0..len {
            ans = 10 * ans + digits[i];
        }
        (ans as i32) != n
    }
    pub fn rotated_digits(n: i32) -> i32 {
        let mut ans = 0;
        for i in 1..=n {
            let res = Self::is_good(i);
            if res {
                ans += 1;
            }
        }
        ans
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_788() {
    }
}

```
