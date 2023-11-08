---
title: 560. subarray sum equals k
date: '2022-04-03'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0560 subarray sum equals k
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={560}/>
 

  Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [1,1,1], k <TeX>=</TeX> 2

 >   Output: 2

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [1,2,3], k <TeX>=</TeX> 3

 >   Output: 2

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 2  10^4

 >   	-1000 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000

 >   	-10^7 <TeX>\leq</TeX> k <TeX>\leq</TeX> 10^7


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut totals: Vec<i32> = Vec::with_capacity(n);
        let mut total = 0 ;
        for &num in nums.iter() {
            total += num;
            totals.push(total);
        }
        let mut res = 0i32;
        for i in 0..n {
            if totals[i] == k {
                res += 1;
            }
            for j in i + 1..n {
                let sum = totals[j] - totals[i];
                if sum == k {
                    res += 1;
                }
            }
        }
        res
    }
}
*/
impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut res = 0i32;
        for i in 0..n {
            let mut total = 0i32;
            for j in i..n {
                total += nums[j];
                if total == k {
                    res += 1;
                }
            }
        }
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_560() {
        assert_eq!(Solution::subarray_sum(vec![1,1,1], 2), 2);
        assert_eq!(Solution::subarray_sum(vec![1,2,3], 3), 2);
    }
}

```
