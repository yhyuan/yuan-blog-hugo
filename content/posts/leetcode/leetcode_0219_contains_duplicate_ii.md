---
title: 219. contains duplicate ii
date: '2021-11-05'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0219 contains duplicate ii
---

 

  Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] <TeX>=</TeX><TeX>=</TeX> nums[j] and abs(i - j) <TeX>\leq</TeX> k.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,2,3,1], k <TeX>=</TeX> 3

 >   Output: true

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,0,1,1], k <TeX>=</TeX> 1

 >   Output: true

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [1,2,3,1,2,3], k <TeX>=</TeX> 2

 >   Output: false

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5

 >   	-10^9 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9

 >   	0 <TeX>\leq</TeX> k <TeX>\leq</TeX> 10^5


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut hashmap: HashMap<i32, usize> = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            if hashmap.contains_key(num) && (i as i32 - hashmap[num] as i32).abs() <= k {
                return true;
            } else {
                hashmap.insert(*num, i);
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
    fn test_219() {
        assert_eq!(Solution::contains_nearby_duplicate(vec![1,2,3,1], 3), true);
        assert_eq!(Solution::contains_nearby_duplicate(vec![1,0,1,1], 1), true);
        assert_eq!(Solution::contains_nearby_duplicate(vec![1,2,3,1,2,3], 2), false);
    }
}

```
