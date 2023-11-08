---
title: 217. contains duplicate
date: '2021-11-03'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0217 contains duplicate
---

 

  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [1,2,3,1]

 >   Output: true

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [1,2,3,4]

 >   Output: false

 >   Example 3:

 >   Input: nums <TeX>=</TeX> [1,1,1,3,3,4,3,2,4,2]

 >   Output: true

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5

 >   	-10^9 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut hashset: HashSet<i32> = HashSet::new();
        for num in nums.iter() {
            if hashset.contains(num) {
                return true;
            } else {
                hashset.insert(*num);
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
    fn test_217() {
        assert_eq!(Solution::contains_duplicate(vec![1,2,3,1]), true);
        assert_eq!(Solution::contains_duplicate(vec![1,2,3,4]), false);
    }
}

```
