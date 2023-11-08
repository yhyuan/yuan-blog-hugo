---
title: 39. combination sum
date: '2021-06-09'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0039 combination sum
---

 

  Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

  The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

  It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

   

 >   Example 1:

  

 >   Input: candidates <TeX>=</TeX> [2,3,6,7], target <TeX>=</TeX> 7

 >   Output: [[2,2,3],[7]]

 >   Explanation:

 >   2 and 3 are candidates, and 2 + 2 + 3 <TeX>=</TeX> 7. Note that 2 can be used multiple times.

 >   7 is a candidate, and 7 <TeX>=</TeX> 7.

 >   These are the only two combinations.

  

 >   Example 2:

  

 >   Input: candidates <TeX>=</TeX> [2,3,5], target <TeX>=</TeX> 8

 >   Output: [[2,2,2,2],[2,3,3],[3,5]]

  

 >   Example 3:

  

 >   Input: candidates <TeX>=</TeX> [2], target <TeX>=</TeX> 1

 >   Output: []

  

 >   Example 4:

  

 >   Input: candidates <TeX>=</TeX> [1], target <TeX>=</TeX> 1

 >   Output: [[1]]

  

 >   Example 5:

  

 >   Input: candidates <TeX>=</TeX> [1], target <TeX>=</TeX> 2

 >   Output: [[1,1]]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> candidates.length <TeX>\leq</TeX> 30

 >   	1 <TeX>\leq</TeX> candidates[i] <TeX>\leq</TeX> 200

 >   	All elements of candidates are distinct.

 >   	1 <TeX>\leq</TeX> target <TeX>\leq</TeX> 500


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn combination_sum_helper(candidates: &Vec<i32>, target: i32, values: &mut Vec<i32>, values_sum: i32) -> Vec<Vec<i32>> {
        //println!("values: {:?}", values);
        if target == values_sum {
            return vec![values.clone()];
        }
        let diff = target - values_sum;
        let mut final_results: Vec<Vec<i32>> = vec![];
        let max_value = if values.len() == 0 {i32::MIN} else {values[values.len() - 1]};
        for &candidate in candidates.iter() {
            if candidate <= diff && candidate >= max_value {
                values.push(candidate);
                let results = Solution::combination_sum_helper(candidates, target, values, values_sum + candidate);
                for result in results.into_iter() {
                    final_results.push(result);
                }
                values.pop();
            }
        }
        //let candidates = candidates.into_iter().filter(|&&canidate| candidate > target).collect::<Vec<i32>>();
        final_results
    }
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut candidates = candidates;
        candidates.sort();
        let mut values:Vec<i32> = vec![];
        Solution::combination_sum_helper(&candidates, target, &mut values, 0i32)
    }
}
*/
impl Solution {
    pub fn helper(candidates: &Vec<i32>, target: i32, values: &mut Vec<i32>) -> Vec<Vec<i32>> {
        let total_value = values.iter().sum::<i32>();
        if target == total_value {
            return vec![values.clone()];
        }
        let max_value = if values.len() == 0 {i32::MIN} else {*values.last().unwrap()};
        let n = candidates.len();
        let good_candidates = (0..n).into_iter().filter(|&i| candidates[i] >= max_value && total_value + candidates[i] <= target).collect::<Vec<_>>();
        let mut res: Vec<Vec<i32>> = vec![];
        for i in good_candidates {
            values.push(candidates[i]);
            let mut pre_res = Self::helper(candidates, target, values);
            for j in 0..pre_res.len() {
                res.push(pre_res[j].clone());
            }
            values.pop();            
        }
        res
    }
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut candidates = candidates;
        candidates.sort();
        let mut values: Vec<i32> = vec![];
        Self::helper(&candidates, target, &mut values)
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_39() {
        assert_eq!(
            Solution::combination_sum(vec![1], 7),
            vec![vec![1, 1, 1, 1, 1, 1, 1]]
        );
        assert_eq!(
            Solution::combination_sum(vec![2, 3, 6, 7], 7),
            vec![vec![2, 2, 3],vec![7],]
        );
        assert_eq!(
            Solution::combination_sum(vec![2, 3, 5], 8),
            vec![vec![2, 2, 2, 2], vec![2, 3, 3], vec![3, 5], ]
        );
    }
}

```
