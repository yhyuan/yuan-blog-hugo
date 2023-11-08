---
title: 70. climbing stairs
date: '2021-07-10'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0070 climbing stairs
---

 

  You are climbing a staircase. It takes n steps to reach the top.

  Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 2

 >   Output: 2

 >   Explanation: There are two ways to climb to the top.

 >   1. 1 step + 1 step

 >   2. 2 steps

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 3

 >   Output: 3

 >   Explanation: There are three ways to climb to the top.

 >   1. 1 step + 1 step + 1 step

 >   2. 1 step + 2 steps

 >   3. 2 steps + 1 step

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 45


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n == 1 {
            return 1i32;
        }
        if n == 2 {
            return 2i32;
        }
        let mut f_n_1 = 2i32;
        let mut f_n_2 = 1i32;
        for i in 3..=n {
            let temp = f_n_2 + f_n_1;
            f_n_2 = f_n_1;
            f_n_1 = temp;
        }
        f_n_1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_70() {
        assert_eq!(Solution::climb_stairs(3), 3);
        assert_eq!(Solution::climb_stairs(4), 5);
        assert_eq!(Solution::climb_stairs(5), 8);
    }
}

```
