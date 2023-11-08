---
title: 494. target sum
date: '2022-03-17'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0494 target sum
---

 

  You are given an integer array nums and an integer target.

  You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

  

  	For example, if nums <TeX>=</TeX> [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

  

  Return the number of different expressions that you can build, which evaluates to target.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,1,1,1,1], target <TeX>=</TeX> 3

 >   Output: 5

 >   Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.

 >   -1 + 1 + 1 + 1 + 1 <TeX>=</TeX> 3

 >   +1 - 1 + 1 + 1 + 1 <TeX>=</TeX> 3

 >   +1 + 1 - 1 + 1 + 1 <TeX>=</TeX> 3

 >   +1 + 1 + 1 - 1 + 1 <TeX>=</TeX> 3

 >   +1 + 1 + 1 + 1 - 1 <TeX>=</TeX> 3

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1], target <TeX>=</TeX> 1

 >   Output: 1

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 20

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000

 >   	0 <TeX>\leq</TeX> sum(nums[i]) <TeX>\leq</TeX> 1000

 >   	-1000 <TeX>\leq</TeX> target <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn dfs(nums: &Vec<i32>, memo: &mut HashMap<(i32, usize), i32>, total: i32, index: usize, target: i32) -> i32 {
        if memo.contains_key(&(target, index)) {
            return memo[&(target, index)];
        }
        if target > total || target < -total {
            return 0;
        }
        if index == 0 {
            if (nums[index] == target && nums[index] == -target) {
                return 2i32;
            }
            if (nums[index] == target || nums[index] == -target) {
                return 1i32;
            }
        }
        //let val = nums[index];
        if nums[index] == 0 {
            let res = 2 * Self::dfs(nums, memo, total, index - 1, target);
            memo.insert((target, index), res);
            return res    
        }
        let res = Self::dfs(nums, memo, total - nums[index], index - 1, target + nums[index]) + 
            Self::dfs(nums, memo, total - nums[index], index - 1, target - nums[index]);
        memo.insert((target, index), res);
        res
    }
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let total = nums.iter().sum::<i32>();
        let mut memo: HashMap<(i32, usize), i32> = HashMap::new();
        Self::dfs(&nums, &mut memo, total, n - 1, target)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_494() {
        assert_eq!(Solution::find_target_sum_ways(vec![0,0,0,0,0,0,0,0,1], 1), 256);
        assert_eq!(Solution::find_target_sum_ways(vec![1,1,1,1,1], 3), 5);
        assert_eq!(Solution::find_target_sum_ways(vec![1], 1), 1);
    }
}

```
