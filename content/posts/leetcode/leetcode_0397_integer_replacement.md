---
title: 397. integer replacement
date: '2022-02-21'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0397 integer replacement
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={397}/>
 

  Given a positive integer n, you can apply one of the following operations:

  <ol>

  	If n is even, replace n with n / 2.

  	If n is odd, replace n with either n + 1 or n - 1.

  </ol>

  Return the minimum number of operations needed for n to become 1.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 8

 >   Output: 3

 >   Explanation: 8 -> 4 -> 2 -> 1

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 7

 >   Output: 4

 >   Explanation: 7 -> 8 -> 4 -> 2 -> 1

 >   or 7 -> 6 -> 3 -> 2 -> 1

  

 >   Example 3:

  

 >   Input: n <TeX>=</TeX> 4

 >   Output: 2

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::VecDeque;
impl Solution {
    pub fn integer_replacement(n: i32) -> i32 {
        let mut queue: VecDeque<(i64, usize)> = VecDeque::new();
        queue.push_back((n as i64, 0));
        while !queue.is_empty() {
            let (val, layer) = queue.pop_front().unwrap();
            if val == 1 {
                return layer as i32;
            }
            if val % 2 == 0 {
                queue.push_back((val / 2, layer + 1));
            } else {
                queue.push_back((val + 1, layer + 1));
                if val > 1 {
                    queue.push_back((val - 1, layer + 1));
                }
            }
        }
        i32::MAX
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_397() {
        //assert_eq!(Solution::integer_replacement(8), 3);
        //assert_eq!(Solution::integer_replacement(7), 4);
        assert_eq!(Solution::integer_replacement(i32::MAX), 32);

        //2147483647
    }
}

```
