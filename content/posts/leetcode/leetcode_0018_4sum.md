---
title: 18. 4sum
date: '2021-05-19'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0018 4sum
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={18}/>
 

  Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

  

  	0 <TeX>\leq</TeX> a, b, c, d < n

  	a, b, c, and d are distinct.

  	nums[a] + nums[b] + nums[c] + nums[d] <TeX>=</TeX><TeX>=</TeX> target

  

  You may return the answer in any order.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,0,-1,0,-2,2], target <TeX>=</TeX> 0

 >   Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [2,2,2,2,2], target <TeX>=</TeX> 8

 >   Output: [[2,2,2,2]]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 200

 >   	-10^9 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9

 >   	-10^9 <TeX>\leq</TeX> target <TeX>\leq</TeX> 10^9


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn four_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let zeros = nums.iter().filter(|&&i| i == 0).count();
        let mut nums = nums;
        if zeros >= 5 {
            nums = nums.iter().filter(|&&i| i != 0).map(|&i| i).collect();
            nums.push(0);
            nums.push(0);
            nums.push(0);
            nums.push(0);
        }
        nums.sort();
        //println!("nums: {:?}", nums);
        let mut results: Vec<Vec<i32>> = vec![];
        let mut is_existed: HashMap<(i32, i32, i32, i32), i32> = HashMap::new();
        for i in 0..nums.len() {
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }
            for j in i + 1..nums.len() {
                if j > i + 1 && nums[j] == nums[j - 1] {
                    continue;
                }    
                let mut hashmap: HashMap<i32, i32> = HashMap::new();
                for k in j + 1..nums.len() {
                    /*
                    if k > j + 1 && nums[k] == nums[k - 1] {
                        continue;
                    }
                    */
                    let diff = target - nums[i] - nums[j] - nums[k];
                    if hashmap.contains_key(&nums[k]) {
                        let v = if diff < nums[k] {(nums[i], nums[j], diff, nums[k])} else {(nums[i], nums[j], nums[k], diff)};
                        if !is_existed.contains_key(&v) {
                            results.push(vec![v.0, v.1, v.2, v.3]);
                            is_existed.insert(v, 0);
                        }
                    } else {
                        hashmap.insert(diff, 0);
                    }
                    // println!("k: {}, results: {:?}", k, results);
                }
                // println!("j: {}, results: {:?}", j, results);
            }
            // println!("i: {}, results: {:?}", i, results);
        }
        results.reverse();
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_18() {
        assert_eq!(
            Solution::four_sum(vec![1, 0, -1, 0, -2, 2], 0),
            vec![vec![-1, 0, 0, 1], vec![-2, 0, 0, 2], vec![-2, -1, 1, 2]]
        );
        assert_eq!(
            Solution::four_sum(vec![2,2,2,2,2], 8),
            vec![vec![2,2,2,2]]
        );
    }
}

```
