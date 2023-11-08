---
title: 396. rotate function
date: '2022-02-20'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0396 rotate function
---

 

  You are given an integer array nums of length n.

  Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

  

  	F(k) <TeX>=</TeX> 0  arrk[0] + 1  arrk[1] + ... + (n - 1)  arrk[n - 1].

  

  Return the maximum value of F(0), F(1), ..., F(n-1).

  The test cases are generated so that the answer fits in a 32-bit integer.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [4,3,2,6]

 >   Output: 26

 >   Explanation:

 >   F(0) <TeX>=</TeX> (0  4) + (1  3) + (2  2) + (3  6) <TeX>=</TeX> 0 + 3 + 4 + 18 <TeX>=</TeX> 25

 >   F(1) <TeX>=</TeX> (0  6) + (1  4) + (2  3) + (3  2) <TeX>=</TeX> 0 + 4 + 6 + 6 <TeX>=</TeX> 16

 >   F(2) <TeX>=</TeX> (0  2) + (1  6) + (2  4) + (3  3) <TeX>=</TeX> 0 + 6 + 8 + 9 <TeX>=</TeX> 23

 >   F(3) <TeX>=</TeX> (0  3) + (1  2) + (2  6) + (3  4) <TeX>=</TeX> 0 + 2 + 12 + 12 <TeX>=</TeX> 26

 >   So the maximum value of F(0), F(1), F(2), F(3) is F(3) <TeX>=</TeX> 26.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [100]

 >   Output: 0

  

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> nums.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^5

 >   	-100 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 100


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let sum: i32 = nums.iter().sum();
        let mut total = 0;
        for (i, &num) in nums.iter().enumerate() {
            total += i as i32 * num;
        }
        let mut result = total;
        let n = nums.len() as i32;
        for i in 0..nums.len() - 1 {
            total = total - sum + n * nums[i];
            result = i32::max(result, total);
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_396() {
        assert_eq!(Solution::max_rotate_function(vec![4,3,2,6]), 26);
    }
}

```
