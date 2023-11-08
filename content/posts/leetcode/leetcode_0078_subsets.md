---
title: 78. subsets
date: '2021-07-18'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0078 subsets
---

 

  Given an integer array nums of unique elements, return all possible subsets (the power set).

  The solution set must not contain duplicate subsets. Return the solution in any order.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,2,3]

 >   Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [0]

 >   Output: [[],[0]]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10

 >   	-10 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10

 >   	All the numbers of nums are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    /*
    pub fn subsets_helper(nums: &Vec<i32>, i: usize) -> Vec<Vec<i32>> {
        if i == nums.len() {
            return vec![vec![]];
        }
        if i == nums.len() - 1 {
            return vec![vec![],vec![nums[nums.len() - 1]]];
        }
        let mut results: Vec<Vec<i32>> = Solution::subsets_helper(nums, i + 1);
        let results_with_i: Vec<Vec<i32>> = results.clone().into_iter().map(|v| {
            let mut v = v;
            v.insert(0, nums[i]);
            v
        }).collect();
        for result in results_with_i {
            results.push(result);
        }
        results
    }
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        Solution::subsets_helper(&nums, 0)
    }
    */

    pub fn helper(nums: &Vec<i32>, index: usize) -> Vec<Vec<i32>> {
        if index == nums.len() {
            return vec![vec![]];
        }
        let mut pre_results = Self::helper(nums, index + 1);
        let mut pre_results_clone = pre_results.clone();
        for i in 0..pre_results_clone.len() {
            pre_results_clone[i].insert(0, nums[index]);
        }
        pre_results.append(&mut pre_results_clone);
        pre_results
    }
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        Self::helper(&nums, 0)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_78() {
        let empty: Vec<i32> = vec![];
        assert_eq!(Solution::subsets(vec![]), vec![empty]);
        assert_eq!(Solution::subsets(vec![1]), vec![vec![], vec![1]]);
        assert_eq!(
            Solution::subsets(vec![1, 2]),
            vec![vec![], vec![2], vec![1], vec![1, 2]]
        );
    }
}

```
