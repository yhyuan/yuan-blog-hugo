---
title: 55. jump game
date: '2021-06-25'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0055 jump game
---

 

  You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

  Return true if you can reach the last index, or false otherwise.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [2,3,1,1,4]

 >   Output: true

 >   Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [3,2,1,0,4]

 >   Output: false

 >   Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^4

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^5


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn can_jump_helper(nums: &Vec<i32>, i: usize, can_jump_status: &mut Vec<i32>) -> bool {
        if i >= nums.len() - 1 {
            return  true;
        }
        if can_jump_status[i] >= 0 {
            return can_jump_status[i] == 1i32;
        }
        let num = nums[i] as usize;
        if num > 0 {
            for k in 1..=num {
                let result = Solution::can_jump_helper(nums, i + k, can_jump_status);
                if result {
                    can_jump_status[i] = 1;
                    return true;
                }
            }
        }
        can_jump_status[i] = 0;
        return false;
    }
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut can_jump_status: Vec<i32> = vec![-1; nums.len()]; 
        Solution::can_jump_helper(&nums, 0, &mut can_jump_status)
    }
}
*/
impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut dp = vec![i32::MAX; n];
        dp[0] = 0;
        for i in 0..n {
            let val = nums[i] as usize; // dp[i]
            for j in 0..val {
                if i + j + 1 > n - 1 {
                    break;
                }
                dp[i + j + 1] = if dp[i] == i32::MAX {i32::MAX} else {i32::min(dp[i + j + 1], dp[i] + 1)};
            }
        }
        dp[n - 1] < i32::MAX
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_55() {
        assert_eq!(Solution::can_jump(vec![0,2,3]), false);
        assert_eq!(Solution::can_jump(vec![2, 3, 1, 1, 4]), true);
        assert_eq!(Solution::can_jump(vec![3, 2, 1, 0, 4]), false);
        assert_eq!(Solution::can_jump(vec![2, 3, 1, 1, 0, 0, 0, 4]), false);
        assert_eq!(Solution::can_jump(vec![8, 3, 1, 1, 0, 0, 0, 4]), true);
        assert_eq!(Solution::can_jump(vec![0]), true);
        assert_eq!(Solution::can_jump(vec![1, 1, 2, 2, 0, 1, 1]), true);
        assert_eq!(
            Solution::can_jump(vec![1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]),
            true
        );
    }
}

```
