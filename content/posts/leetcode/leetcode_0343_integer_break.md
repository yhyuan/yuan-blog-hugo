---
title: 343. integer break
date: '2022-01-16'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0343 integer break
---

 

  Given an integer n, break it into the sum of k positive integers, where k ><TeX>=</TeX> 2, and maximize the product of those integers.

  Return the maximum product you can get.

   

 >   Example 1:

  

 >   Input: n <TeX>=</TeX> 2

 >   Output: 1

 >   Explanation: 2 <TeX>=</TeX> 1 + 1, 1 &times; 1 <TeX>=</TeX> 1.

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 10

 >   Output: 36

 >   Explanation: 10 <TeX>=</TeX> 3 + 3 + 4, 3 &times; 3 &times; 4 <TeX>=</TeX> 36.

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> n <TeX>\leq</TeX> 58


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashMap;
impl Solution {
    pub fn integer_break_helper(n: i32, hashmap: &mut HashMap<i32, i32>) -> i32 {
        if hashmap.contains_key(&n) {
            return hashmap[&n];
        }
        let mut result = 0;
        for i in 1..n {
            result = i32::max(result, i * Self::integer_break_helper(n - i, hashmap));
            result = i32::max(result, i * (n - i));
        }
        hashmap.insert(n, result);
        result
    }
    pub fn integer_break(n: i32) -> i32 {
        let mut hashmap: HashMap<i32, i32> = HashMap::new();
        hashmap.insert(1, 1);
        hashmap.insert(2, 1);
        Self::integer_break_helper(n, &mut hashmap)
    }
}
*/
impl Solution {
    pub fn integer_break(n: i32) -> i32 {
        // f(n) = max(f(i) * f(n - i))
        let n = n as usize;
        let mut dp: Vec<i32> = vec![0; n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for i in 2..=n {
            dp[i] = (1..i).into_iter().map(|j| i32::max(j as i32 * dp[i - j], (j * (i - j)) as i32 )).max().unwrap();            
        }
        //println!("dp: {:?}", dp);
        dp[n]
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_343() {
        assert_eq!(Solution::integer_break(8), 18);
        assert_eq!(Solution::integer_break(2), 1);
        assert_eq!(Solution::integer_break(3), 2);
        assert_eq!(Solution::integer_break(4), 4);
        assert_eq!(Solution::integer_break(10), 36);
        assert_eq!(Solution::integer_break(30), 59049);
    }
}

```
