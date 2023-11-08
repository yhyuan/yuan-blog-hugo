---
title: 220. contains duplicate iii
date: '2021-11-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0220 contains duplicate iii
---

 

  Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <TeX>\leq</TeX> t and abs(i - j) <TeX>\leq</TeX> k.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [1,2,3,1], k <TeX>=</TeX> 3, t <TeX>=</TeX> 0

 >   Output: true

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [1,0,1,1], k <TeX>=</TeX> 1, t <TeX>=</TeX> 2

 >   Output: true

 >   Example 3:

 >   Input: nums <TeX>=</TeX> [1,5,9,1,5,9], k <TeX>=</TeX> 2, t <TeX>=</TeX> 3

 >   Output: false

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 2  10^4

 >   	-2^31 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1

 >   	0 <TeX>\leq</TeX> k <TeX>\leq</TeX> 10^4

 >   	0 <TeX>\leq</TeX> t <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn contains_nearby_almost_duplicate(nums: Vec<i32>, k: i32, t: i32) -> bool {
        let n = nums.len();
        for i in 0..n {
            for j in i + 1..n {
                if (nums[i] as i64 - nums[j] as i64).abs() <= t as i64 && (j - i) as i32 <= k {
                    return true;
                }
            }
        }
        false
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_220() {
        //assert_eq!(Solution::contains_nearby_almost_duplicate(vec![1,2,3,1], 3, 0), true);
        //assert_eq!(Solution::contains_nearby_almost_duplicate(vec![1,0,1,1], 1, 2), true);
        //assert_eq!(Solution::contains_nearby_almost_duplicate(vec![1,5,9,1,5,9], 2, 3), false);
        assert_eq!(Solution::contains_nearby_almost_duplicate(vec![-2147483648,2147483647], 1, 1), false);
    }
}

```
