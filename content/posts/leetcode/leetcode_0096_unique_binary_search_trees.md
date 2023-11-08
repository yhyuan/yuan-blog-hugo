---
title: 96. unique binary search trees
date: '2021-08-05'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0096 unique binary search trees
---

 

  Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)

 >   Input: n <TeX>=</TeX> 3

 >   Output: 5

  

 >   Example 2:

  

 >   Input: n <TeX>=</TeX> 1

 >   Output: 1

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 19


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn num_trees_helper(n: usize, cache: &mut Vec<i32>) -> i32 {
        //let n = n as usize;
        if cache[n] != i32::MIN {
            return cache[n];
        }
        // root = 1, nums_trees(n - 1)
        // root = 2, nums_trees(1) * nums_trees(n - 2)

        // root = n - 1, nums_trees(n - 2) * nums_trees(1)
        // root = n, nums_trees(n - 1)
        let mut total = 0;
        for i in 1..=n {
            total += Solution::num_trees_helper(i - 1, cache) * Solution::num_trees_helper(n - i, cache);
        }
        cache[n] = total;
        total
    }
    pub fn num_trees(n: i32) -> i32 {
        let n = n as usize;
        let mut cache = vec![i32::MIN; n + 1];
        cache[0] = 1;
        cache[1] = 1;
        Solution::num_trees_helper(n, &mut cache)
    }
}
*/

impl Solution {
    pub fn num_trees(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![0i32; n + 1];
        dp[0] = 1;
        dp[1] = 1;
        if n == 1 {
            return 1;
        }
        for i in 2..=n {
            for k in 0..=i-1 {
                dp[i] += dp[k] * dp[i - 1 - k];
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
    fn test_96() {
        assert_eq!(Solution::num_trees(3), 5);
        assert_eq!(Solution::num_trees(4), 14);
    }
}

```
