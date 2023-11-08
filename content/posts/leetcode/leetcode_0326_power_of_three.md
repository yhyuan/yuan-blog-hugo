---
title: 326. power of three
date: '2022-01-10'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0326 power of three
---

 

  Given an integer n, return true if it is a power of three. Otherwise, return false.

  An integer n is a power of three, if there exists an integer x such that n <TeX>=</TeX><TeX>=</TeX> 3^x.

   

 >   Example 1:

 >   Input: n <TeX>=</TeX> 27

 >   Output: true

 >   Example 2:

 >   Input: n <TeX>=</TeX> 0

 >   Output: false

 >   Example 3:

 >   Input: n <TeX>=</TeX> 9

 >   Output: true

 >   Example 4:

 >   Input: n <TeX>=</TeX> 45

 >   Output: false

   

  **Constraints:**

  

 >   	-2^31 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1

  

   

 >   Follow up: Could you solve it without loops/recursion?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        if n <= 0 {
            return false;
        }
        let r = (n as f64).log10() / 3f64.log10();
        3u32.pow(r.ceil() as u32) == n as u32 || 3u32.pow(r.floor() as u32) == n as u32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_326() {
        assert_eq!(Solution::is_power_of_three(27), true);
        assert_eq!(Solution::is_power_of_three(0), false);
        assert_eq!(Solution::is_power_of_three(9), true);
        assert_eq!(Solution::is_power_of_three(45), false);
    }
}

```
