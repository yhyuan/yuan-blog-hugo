---
title: 377. combination sum iv
date: '2022-02-04'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0377 combination sum iv
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={377}/>
 

  Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

  The answer is guaranteed to fit in a 32-bit integer.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,2,3], target <TeX>=</TeX> 4

 >   Output: 7

 >   Explanation:

 >   The possible combination ways are:

 >   (1, 1, 1, 1)

 >   (1, 1, 2)

 >   (1, 2, 1)

 >   (1, 3)

 >   (2, 1, 1)

 >   (2, 2)

 >   (3, 1)

 >   Note that different sequences are counted as different combinations.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [9], target <TeX>=</TeX> 3

 >   Output: 0

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 200

 >   	1 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000

 >   	All the elements of nums are unique.

 >   	1 <TeX>\leq</TeX> target <TeX>\leq</TeX> 1000

  

   

 >   Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashMap;
impl Solution {
    pub fn combination_sum4_helper(nums: &Vec<i32>, target: i32, hashmap: &mut HashMap<i32, i32>) -> i32 {
        if hashmap.contains_key(&target) {
            return hashmap[&target];
        }
        if target == 0 {
            return 1;
        }
        if nums[0] > target {
            return 0;
        }
        let mut k = nums.len();
        if target <= nums[k - 1] {
            for i in 0..nums.len() {
                if nums[i] > target {
                    k = i;
                    break;
                }
            }    
        } 
        let mut result = 0;
        for i in 0..k {
            let res = Self::combination_sum4_helper(nums, target - nums[i], hashmap);
            result += res;
        }
        hashmap.insert(target, result);
        result
    }
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let mut nums = nums;
        nums.sort();
        let mut hashmap: HashMap<i32, i32> = HashMap::new();
        Self::combination_sum4_helper(&nums, target, &mut hashmap)
    }
}
*/
impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let mut nums = nums;
        nums.sort();
        let target = target as usize;
        let mut dp: Vec<i32> = vec![0; target + 1];
        dp[0] = 1;
        for i in 1..=target {
            dp[i] =  (0..nums.len()).into_iter()
                .filter(|&k| nums[k] <= i as i32)
                .map(|k| dp[i - nums[k] as usize])
                .sum::<i32>();
        }
        dp[target]
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_377() {
        assert_eq!(Solution::combination_sum4(vec![2,1,3], 35), 1132436852);
        assert_eq!(Solution::combination_sum4(vec![1,2,3], 4), 7);
        assert_eq!(Solution::combination_sum4(vec![9], 3), 0);
    }
}

```
