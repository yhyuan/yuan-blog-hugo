---
title: 229. majority element ii
date: '2021-11-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0229 majority element ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={229}/>
 

  Given an integer array of size n, find all elements that appear more than &lfloor; n/3 &rfloor; times.

  Follow-up: Could you solve the problem in linear time and in O(1) space?

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [3,2,3]

 >   Output: [3]

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1]

 >   Output: [1]

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [1,2]

 >   Output: [1,2]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 5  10^4

 >   	-10^9 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
//use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        /*
        let n = nums.len();
        if n == 0 {
            return vec![];
        }
        if n == 1 {
            return nums;
        }
        if n == 2 {
            if nums[0] == nums[1] {
                return vec![nums[0]];
            }
            return nums;
        }
        let (mut vet1, mut vet2, mut num1, mut num2) = (0, 0, i32::MIN, i32::MIN);
        for &num in nums.iter() {
            if num == num1 {
                vet1 += 1;
            } else if num == num2 {
                vet2 += 1;
            } else if vet1 == 0 {
                num1 = num;
            } else if vet2 == 0 {
                num2 = num;
            } else {
                vet1 -= 1;
                vet2 -= 1;
            }
        }
        //println!("num1: {}, num2: {}", num1, num2);
        let num1_count = nums.iter().filter(|&&num| num == num1).count();
        let num2_count = nums.iter().filter(|&&num| num == num2).count();
        let mut results: Vec<i32> = vec![];
        if num1_count > nums.len() / 3 {
            results.push(num1);
        }
        if num2_count > nums.len() / 3 {
            results.push(num2);
        }
        results
        */
        //vec![1]
        /*
        let n = nums.len();
        let mut hashmap:HashMap<i32, usize> = HashMap::new();
        for &num in nums.iter() {
            if hashmap.contains_key(&num) {
                //let values = hashmap[&num];
                hashmap.insert(num, hashmap[&num] + 1);
            } else {
                hashmap.insert(num, 1);
            }
        }
        let mut results: Vec<i32> = vec![];
        for (&k, &v) in hashmap.iter() {
            if v > n / 3 {
                results.push(k);
            }
        }
        results
        //vec![]
        */
        vec![]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_229() {
        let empty: Vec<i32> = vec![];
        assert_eq!(
            Solution::majority_element(vec![1, 1, 1, 2, 2, 2, 3, 3, 3]),
            empty
        );
        assert_eq!(
            Solution::majority_element(vec![1, 1, 1, 2, 2, 3, 3, 3]),
            vec![1, 3]
        );
        assert_eq!(Solution::majority_element(vec![1]), vec![1]);
        assert_eq!(Solution::majority_element(vec![5, 6, 6]), vec![6]);
        let empty: Vec<i32> = vec![];
        assert_eq!(Solution::majority_element(vec![1, 2, 3, 4]), empty);
        //[3,0,3,4]
    }
}

```
