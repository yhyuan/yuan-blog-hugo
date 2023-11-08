---
title: 995. minimum number of k consecutive bit flips
date: '2022-06-26'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0995 minimum number of k consecutive bit flips
---

 

  You are given a binary array nums and an integer k.

  A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

  Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

  A subarray is a contiguous part of an array.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [0,1,0], k <TeX>=</TeX> 1

 >   Output: 2

 >   Explanation: Flip nums[0], then flip nums[2].

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,1,0], k <TeX>=</TeX> 2

 >   Output: -1

 >   Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [0,0,0,1,0,1,1,0], k <TeX>=</TeX> 3

 >   Output: 3

 >   Explanation: 

 >   Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]

 >   Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]

 >   Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 3  10^4

 >   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> nums.length


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn min_k_bit_flips(nums: Vec<i32>, k: i32) -> i32 {
        0
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_995() {
    }
}

```
