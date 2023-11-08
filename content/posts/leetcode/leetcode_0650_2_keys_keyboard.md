---
title: 650. 2 keys keyboard
date: '2022-04-14'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0650 2 keys keyboard
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={650}/>
 

  There is only one character 'A' on the screen of a notepad. You can perform two operations on this notepad for each step:

  

  	Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).

  	Paste: You can paste the characters which are copied last time.

  

  Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 3

 >   Output: 3

 >   Explanation: Intitally, we have one character 'A'.

 >   In step 1, we use Copy All operation.

 >   In step 2, we use Paste operation to get 'AA'.

 >   In step 3, we use Paste operation to get 'AAA'.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 1

 >   Output: 0

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn min_steps(n: i32) -> i32 {
        let n = n as usize;
        if n == 1 {
            return 0;
        }
        let mut dp: Vec<i32> = vec![0; n + 1];
        dp[1] = 0;
        for i in 2..=n {
            for j in 2..=i {
                if i % j == 0 {
                    dp[i] = dp[i / j] + j as i32;
                    break;
                }
            }
        }
        dp[n]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_650() {
        assert_eq!(Solution::min_steps(11), 11);
        assert_eq!(Solution::min_steps(3), 3);
        assert_eq!(Solution::min_steps(1), 0);
    }
}

```
