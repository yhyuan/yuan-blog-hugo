---
title: 421. maximum xor of two numbers in an array
date: '2022-03-09'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0421 maximum xor of two numbers in an array
---

 

  Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <TeX>\leq</TeX> i <TeX>\leq</TeX> j < n.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [3,10,5,25,2,8]

 >   Output: 28

 >   Explanation: The maximum result is 5 XOR 25 <TeX>=</TeX> 28.

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [0]

 >   Output: 0

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [2,4]

 >   Output: 6

  

 >   Example 4:

  

 >   Input: nums <TeX>=</TeX> [8,10,2]

 >   Output: 10

  

 >   Example 5:

  

 >   Input: nums <TeX>=</TeX> [14,70,53,83,49,91,36,80,92,51,66,70]

 >   Output: 127

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 2  10^5

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
    pub fn find_maximum_xor(nums: Vec<i32>) -> i32 {
        let mut max = 0;
        let mut mask = 0;
        for i in (0..31).rev() {
            // set the i'th bit in mask
            // like 100000, 110000, 111000..
            mask |= 1 << i;
            //println!("mask: {:b}", mask);
            let mut hs: HashSet<i32> = HashSet::new();
            for &x in nums.iter() {
                // Just keep the prefix till
                // i'th bit neglecting all
                // the bit's after i'th bit
                hs.insert(x & mask);
            }
            //println!("hs: {:?}", hs);
            let new_max  = max | (1 << i);
            //println!("new_max: {:b}", new_max);
            // find two pair in set
            // such that a^b = newMaxx, => a ^ b ^ b = newMaxx ^ b => a =  newMaxx ^ b
            // which is the highest
            // possible bit can be obtained
            for &x in hs.iter() {
                if hs.contains(&(new_max ^ x)) {
                    max = new_max;
                    break;
                }
            }
        }
        max
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_421() {
        assert_eq!(Solution::find_maximum_xor(vec![3,10,5,25,2,8]), 28);
        assert_eq!(Solution::find_maximum_xor(vec![0]), 0);
        assert_eq!(Solution::find_maximum_xor(vec![2,4]), 6);
        assert_eq!(Solution::find_maximum_xor(vec![8,10,2]), 10);
        assert_eq!(Solution::find_maximum_xor(vec![14,70,53,83,49,91,36,80,92,51,66,70]), 127);
    }
}

```
