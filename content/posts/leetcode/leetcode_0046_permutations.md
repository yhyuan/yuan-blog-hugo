---
title: 46. permutations
date: '2021-06-16'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0046 permutations
---

 

  Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [1,2,3]

 >   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [0,1]

 >   Output: [[0,1],[1,0]]

 >   Example 3:

 >   Input: nums <TeX>=</TeX> [1]

 >   Output: [[1]]

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 6

 >   	-10 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10

 >   	All the integers of nums are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn permute_helper(nums: &Vec<i32>) -> Vec<Vec<i32>> {
        if nums.len() == 1 {
            return vec![nums.clone()];
        }
        let mut results: Vec<Vec<i32>> =vec![];
        for i in 0..nums.len() {
            let num = nums[i];
            let new_nums: Vec<i32> = (0..nums.len()).into_iter()
                .filter(|&k| k != i)
                .map(|k| nums[k])
                .collect();
            let mut single_results = Solution::permute_helper(&new_nums);
            for result in single_results.iter_mut() {
                result.insert(0, num);
                results.push(result.clone());
            }
        }
        results
    }

    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        Solution::permute_helper(&nums)
    }
}
*/
/*
impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        if nums.len() == 1 {
            return vec![nums];
        }
        nums.iter()
            .flat_map(|&num| {
                let new_nums = nums.clone().into_iter().filter(|&x| x != num).collect();
                Solution::permute(new_nums).into_iter().map(|vec| {
                    let mut vec = vec;
                    vec.insert(0, num);
                    vec
                }).collect::<Vec<Vec<i32>>>()
            }).collect()
    }

    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();
        if n == 0 {
            return vec![vec![]];
        }
        let mut final_results: Vec<Vec<i32>> = vec![];
        for i in 0..n {
            let mut removed_nums = nums.clone();
            removed_nums.remove(i);
            let mut results = Self::permute(removed_nums);
            results.iter_mut().for_each(|r| {
                r.insert(0, nums[i]);
            });
            //final_results.extend(&mut results);
            for j in 0..results.len() {
                final_results.push(results[j].clone());
            }
        }
        final_results
    }
}
*/
impl Solution {
    pub fn helper(nums: &Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();
        if n == 1 {
            return vec![nums.clone()];
        }
        let mut results: Vec<Vec<i32>> = vec![];
        for i in 0..n {
            let num = nums[i];
            let filtered_nums = (0..n).into_iter()
                .filter(|&k| k != i)
                .map(|k| nums[k])
                .collect::<Vec<_>>();
            let recursive_results = Self::helper(&filtered_nums);
            for j in 0..recursive_results.len() {
                let mut result = recursive_results[j].clone();   
                result.insert(0, num);
                results.push(result);
            }
        }
        results
    }
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        Self::helper(&nums)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_46() {
        assert_eq!(
            Solution::permute(vec![1, 2, 3]),
            vec![vec![1,2,3],vec![1,3,2],vec![2,1,3],vec![2,3,1],vec![3,1,2],vec![3,2,1]]
        );
    }
}

```
