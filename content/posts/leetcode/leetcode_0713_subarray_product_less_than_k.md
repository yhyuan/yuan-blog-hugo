---
title: 713. subarray product less than k
date: '2022-04-28'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0713 subarray product less than k
---

 

  Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [10,5,2,6], k <TeX>=</TeX> 100

 >   Output: 8

 >   Explanation: The 8 subarrays that have product less than 100 are:

 >   [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

 >   Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,2,3], k <TeX>=</TeX> 0

 >   Output: 0

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 3  10^4

 >   	1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000

 >   	0 <TeX>\leq</TeX> k <TeX>\leq</TeX> 10^6


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut count = 0;
        for i in 0..n {
            let mut prod = 1i32;
            for j in i..n {
                prod = prod * nums[j];
                if prod >= k {
                    break;
                } else {
                    count += 1;
                }
            }
        }
        count
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_713() {
    }
}

```
