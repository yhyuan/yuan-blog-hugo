---
title: 41. first missing positive
date: '2021-06-11'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0041 first missing positive
---

 

  Given an unsorted integer array nums, return the smallest missing positive integer.

  You must implement an algorithm that runs in O(n) time and uses constant extra space.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [1,2,0]

 >   Output: 3

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [3,4,-1,1]

 >   Output: 2

 >   Example 3:

 >   Input: nums <TeX>=</TeX> [7,8,9,11,12]

 >   Output: 1

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 5  10^5

 >   	-2^31 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut nums = nums;
        for i in 0..n {
            while nums[i] > 0 && nums[i] < n as i32 && nums[i] != nums[nums[i] as usize - 1] {
                let k = nums[i] as usize - 1;
                nums.swap(i, k);
            }
        }
        for i in 0..n {
            if nums[i] != i as i32 + 1 {
                return  i as i32 + 1;
            }
        }
        n as i32 + 1
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_41() {
        assert_eq!(Solution::first_missing_positive(vec![2, 2]), 1);
        assert_eq!(
            Solution::first_missing_positive(vec![12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]),
            1
        );
        assert_eq!(
            Solution::first_missing_positive(vec![2, 2, 2, 2, 2, 2, 2]),
            1
        );
        assert_eq!(Solution::first_missing_positive(vec![3, 4, -1, 1]), 2);
        assert_eq!(Solution::first_missing_positive(vec![2, 1, 0]), 3);
        assert_eq!(Solution::first_missing_positive(vec![7, 8, 9, 11, 12]), 1);
        assert_eq!(
            Solution::first_missing_positive(vec![7, 8, 1, 2, 3, 3, 3, 3, 3, 3, 3, -5, -7, 1234]),
            4
        );
    }
}

```
