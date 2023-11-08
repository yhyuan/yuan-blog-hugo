---
title: 40. combination sum ii
date: '2021-06-10'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0040 combination sum ii
---

 

  Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

  Each number in candidates may only be used once in the combination.

  Note: The solution set must not contain duplicate combinations.

   

 >   Example 1:

  

 >   Input: candidates <TeX>=</TeX> [10,1,2,7,6,1,5], target <TeX>=</TeX> 8

 >   Output: 

 >   [

 >   [1,1,6],

 >   [1,2,5],

 >   [1,7],

 >   [2,6]

 >   ]

  

 >   Example 2:

  

 >   Input: candidates <TeX>=</TeX> [2,5,2,1,2], target <TeX>=</TeX> 5

 >   Output: 

 >   [

 >   [1,2,2],

 >   [5]

 >   ]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> candidates.length <TeX>\leq</TeX> 100

 >   	1 <TeX>\leq</TeX> candidates[i] <TeX>\leq</TeX> 50

 >   	1 <TeX>\leq</TeX> target <TeX>\leq</TeX> 30


## Solution
dp[(i, target)] is a set of tuples to store the results for [0, i] with target value because we want to eliminated duplicated results.  
### Python
```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        memo = {}
        def helper(i, target):
            if (i, target) in memo:
                return memo[(i, target)]
            if i < 0: return set([])
            if target < candidates[i]:
                ans = set([]) if i == 0 else helper(i - 1, target)
                memo[(i, target)] = ans
                return ans
            if target == candidates[i]:
                ans = helper(i - 1, target).copy()
                ans.add(tuple([candidates[i]]))
                memo[(i, target)] = ans
                return memo[(i, target)]
            if i == 0:
                memo[(i, target)] = set()
                return set([])
            results = helper(i - 1, target - candidates[i])
            ans = set([])
            for result in results:
                r = list(result)
                r.append(candidates[i])
                ans.add(tuple(r))
            for result in helper(i - 1, target):
                ans.add(result)
            memo[(i, target)] = ans
            return ans
        n = len(candidates)
        results = helper(n - 1, target)
        return results
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn combination_sum2_helper(candidates: &Vec<i32>, target: i32, selection: &mut Vec<usize>) -> Vec<Vec<usize>> {
        if target == 0 {
            return vec![selection.clone()];
        }
        let start_index = if selection.len() == 0 {0} else {selection[selection.len() - 1] + 1};
        let option_indices: Vec<usize> = (start_index..candidates.len()).into_iter().filter(|i| candidates[*i] <= target).collect();
        if option_indices.len() == 0 {
            return vec![];
        }
        let mut pre_val = i32::MIN;
        let mut results: Vec<Vec<usize>> = vec![];
        for &option in option_indices.iter() {
            if candidates[option] == pre_val {
                continue;
            }
            selection.push(option);
            let single_results = Solution::combination_sum2_helper(candidates, target - candidates[option], selection);
            for result in single_results {
                results.push(result);
            }
            selection.pop();
            pre_val = candidates[option];
        }
        results
    }
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut candidates = candidates;
        candidates.sort();
        candidates.reverse();
        //println!("candidates: {:?}", candidates);
        let mut selection: Vec<usize> = vec![];
        let indices = Solution::combination_sum2_helper(&candidates, target, &mut selection);
        let mut results: Vec<Vec<i32>> = vec![];
        for indice in indices {
            let values = indice.iter().map(|&i| candidates[i]).collect();
            results.push(values);
        }
        results
        //vec![]
    }
}
*/
impl Solution {
    pub fn helper(candidates: Vec<i32>, values: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        if target == 0 {
            return vec![values];
        }
        let mut candidates: Vec<i32> = candidates.into_iter().filter(|&c| c <= target).collect::<Vec<_>>();
        let n = candidates.len();
        let mut res: Vec<Vec<i32>> = vec![];
        for i in 0..candidates.len() {
            let c = candidates[i];
            let new_candidates = (i + 1..n).into_iter().map(|k| candidates[k]).collect::<Vec<_>>();
            //let values = vec![c];
            let mut new_values = values.clone();
            new_values.push(c);
            let pre_res = Self::helper(new_candidates, new_values, target - c);
            for j in 0..pre_res.len() {
                res.push(pre_res[j].clone());
            }            
        }
        res
    }
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut candidates: Vec<i32> = candidates.into_iter().filter(|&c| c <= target).collect::<Vec<_>>();
        candidates.sort();
        let n = candidates.len();
        let mut res: Vec<Vec<i32>> = vec![];
        let mut pre_c = i32::MAX;
        for i in 0..candidates.len() {
            let c = candidates[i];
            if pre_c == c {
                continue;
            }
            let new_candidates = (i + 1..n).into_iter().map(|k| candidates[k]).collect::<Vec<_>>();
            let values = vec![c];
            let pre_res = Self::helper(new_candidates, values, target - c);
            //println!("c: {}, pre_res: {:?}", c, pre_res);
            for j in 0..pre_res.len() {
                res.push(pre_res[j].clone());
            }
            pre_c = c;
        }
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_40() {
        assert_eq!(
            Solution::combination_sum2(vec![1, 1, 1, 1, 1, 1, 1], 7),
            vec![vec![1, 1, 1, 1, 1, 1, 1]]
        );
        assert_eq!(
            Solution::combination_sum2(vec![10, 1, 2, 7, 6, 1, 5], 8),
            vec![vec![1, 1, 6], vec![1, 2, 5], vec![1, 7], vec![2, 6]]
        );
        assert_eq!(
            Solution::combination_sum2(vec![2, 5, 2, 1, 2], 5),
            vec![vec![5], vec![2, 2, 1],]
        );
    }
}

```
