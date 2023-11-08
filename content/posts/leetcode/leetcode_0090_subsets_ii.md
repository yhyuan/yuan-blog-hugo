---
title: 90. subsets ii
date: '2021-07-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0090 subsets ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={90}/>
 

  Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

  The solution set must not contain duplicate subsets. Return the solution in any order.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [1,2,2]

 >   Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [0]

 >   Output: [[],[0]]

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10

 >   	-10 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    /*
    pub fn subsets_with_dup_helper(nums: &Vec<i32>, index: usize) -> Vec<Vec<i32>> {
        if nums.len() == index {
            return vec![vec![]];
        }
        let num = nums[index];
        let mut pre_results: Vec<Vec<i32>> = Solution::subsets_with_dup_helper(nums, index + 1);
        let n = pre_results.len();
        let mut same_num_count = 0usize;
        while same_num_count + index < nums.len() && nums[same_num_count + index] == num {
            same_num_count += 1;
        }
        same_num_count = same_num_count - 1;
        if same_num_count == 0 {
            let results: Vec<Vec<i32>> = pre_results.iter().map(|v| {
                let mut v = v.clone();
                v.insert(0, num);
                v
            }).collect();
            for result in results {
                pre_results.push(result);
            }
            return pre_results;
        }
        let results: Vec<Vec<i32>> = pre_results.iter()
            .filter(|&result| {
            if result.len() == 0 {
                return false;
            }
            if result[0] != num {
                return false;
            }
            let mut i = 0usize;
            while i < result.len() && result[i] == num {
                i += 1;
            }
            //i = i - 1;
            i == same_num_count
        })
        .map(|res| {
            let mut res = res.clone();
            res.insert(0, num);
            res
        }).collect();
        for result in results {
            pre_results.push(result);
        }
        pre_results
    }
    pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
        if nums.len() == 0 {
            return vec![vec![]];
        }
        let mut nums = nums;
        nums.sort();
        Solution::subsets_with_dup_helper(&nums, 0)
    }
    */
    pub fn helper(nums: &Vec<i32>, index: usize) -> (Vec<Vec<i32>>, usize) {
        if index == nums.len() {
            return (vec![vec![]], 0);
        }
        let (mut pre_results, size) = Self::helper(nums, index + 1);
        let mut pre_results_size = pre_results.len();
        let val = nums[index];
        let pre_val = if size == 0 {i32::MAX} else {pre_results[pre_results.len() - 1][0]};
        if pre_val == val {
            let mut pre_results_clone: Vec<Vec<i32>> = vec![];
            for i in 0..size {
                let mut r = pre_results[pre_results_size - 1 - i].clone();
                r.insert(0, val);
                pre_results_clone.push(r);
            }
            pre_results.append(&mut pre_results_clone);
            pre_results_size = size;
        } else {
            let mut pre_results_clone = pre_results.clone();
            for i in 0..pre_results_clone.len() {
                pre_results_clone[i].insert(0, val);
            }
            pre_results.append(&mut pre_results_clone);
        }
        (pre_results, pre_results_size)
    }
    pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
        if nums.len() == 0 {
            return vec![vec![]];
        }
        let mut nums = nums;
        nums.sort();
        let (results, _) = Self::helper(&nums, 0);
        results
        //Solution::subsets_with_dup_helper(&nums, 0)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_90() {
        //
        assert_eq!(
            Solution::subsets_with_dup(vec![5,5,5,5,5]),
            vec![vec![],vec![5],vec![5,5],vec![5,5,5],vec![5,5,5,5],vec![5,5,5,5,5]]
        );
        
        assert_eq!(
            Solution::subsets_with_dup(vec![1, 1, 2, 2]),
            vec![vec![], vec![2], vec![2, 2], vec![1], vec![1, 2], vec![1, 2, 2], vec![1, 1], vec![1, 1, 2], vec![1, 1, 2, 2]]
        );
        
        assert_eq!(
            Solution::subsets_with_dup(vec![1, 2, 2]),
            vec![
                vec![],
                vec![2],
                vec![2, 2],
                vec![1],
                vec![1, 2],
                vec![1, 2, 2],
            ]
        );
        assert_eq!(
            Solution::subsets_with_dup(vec![1, 2, 3]),
            vec![vec![], vec![3], vec![2], vec![2, 3], vec![1], vec![1, 3], vec![1, 2], vec![1, 2, 3]]
        );
        assert_eq!(Solution::subsets_with_dup(vec![1]), vec![vec![], vec![1],]);
        let empty: Vec<i32> = vec![];
        assert_eq!(Solution::subsets_with_dup(vec![]), vec![empty,]);

    }
}

```
