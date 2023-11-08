---
title: 279. perfect squares
date: '2021-12-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0279 perfect squares
---

 

  Given an integer n, return the least number of perfect square numbers that sum to n.

  A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 12

 >   Output: 3

 >   Explanation: 12 <TeX>=</TeX> 4 + 4 + 4.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 13

 >   Output: 2

 >   Explanation: 13 <TeX>=</TeX> 4 + 9.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn num_squares_helper(n: usize, cache: &mut Vec<i32>) -> i32 {
        if cache[n] != i32::MIN {
            return  cache[n];
        }
        let mut sq_root = (n as f64).sqrt() as usize + 1;
        while sq_root * sq_root > n {
            sq_root -= 1;
        }
        if sq_root * sq_root == n {
            cache[n] = 1i32;
            return 1i32;
        }
        let mut result = i32::MAX;
        for i in (1..=sq_root).rev() {
            result = i32::min(result, Solution::num_squares_helper(n - i * i, cache));
        }
        result = result + 1;
        cache[n] = result;
        result
    }
    pub fn num_squares(n: i32) -> i32 {
        let n = n as usize;
        let mut cache: Vec<i32> = vec![i32::MIN; n + 1];
        cache[0] = 0;
        cache[1] = 1;
        //cache[2] = 2;
        //cache[3] = 3;
        Solution::num_squares_helper(n, &mut cache)
    }
}
*/
use std::collections::HashSet;
impl Solution {
    pub fn num_squares(n: i32) -> i32 {
        let mut squares: Vec<i32> = vec![];
        for i in 1..n {
            let sq = i * i;
            if sq <= n {
                squares.push(sq);
            } else {
                break;
            }
        }
        let squares_set: HashSet<i32> = squares.iter().map(|&k| k).collect::<HashSet<_>>();
        let n = n as usize;
        let mut dp: Vec<i32> = vec![0; n + 1];
        for i in 1..=n {
            if squares_set.contains(&(i as i32)) {
                dp[i] = 1;
            } else {
                let sqrt = (i as f64).sqrt().floor() as usize;
                dp[i] = (1..=sqrt).into_iter().map(|k| dp[i - k * k]).min().unwrap() + 1;
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
    fn test_279() {
        assert_eq!(Solution::num_squares(9), 1);
        assert_eq!(Solution::num_squares(12), 3);
        assert_eq!(Solution::num_squares(13), 2);
    }
}

```
