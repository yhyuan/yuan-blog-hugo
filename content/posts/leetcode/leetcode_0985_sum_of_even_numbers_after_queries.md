---
title: 985. sum of even numbers after queries
date: '2022-06-21'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0985 sum of even numbers after queries
---

 

  You are given an integer array nums and an array queries where queries[i] <TeX>=</TeX> [vali, indexi].

  For each query i, first, apply nums[indexi] <TeX>=</TeX> nums[indexi] + vali, then print the sum of the even values of nums.

  Return an integer array answer where answer[i] is the answer to the i^th query.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,2,3,4], queries <TeX>=</TeX> [[1,0],[-3,1],[-4,0],[2,3]]

 >   Output: [8,6,2,4]

 >   Explanation: At the beginning, the array is [1,2,3,4].

 >   After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 <TeX>=</TeX> 8.

 >   After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 <TeX>=</TeX> 6.

 >   After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 <TeX>=</TeX> 2.

 >   After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 <TeX>=</TeX> 4.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1], queries <TeX>=</TeX> [[4,0]]

 >   Output: [0]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^4

 >   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4

 >   	1 <TeX>\leq</TeX> queries.length <TeX>\leq</TeX> 10^4

 >   	-10^4 <TeX>\leq</TeX> vali <TeX>\leq</TeX> 10^4

 >   	0 <TeX>\leq</TeX> indexi < nums.length


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn sum_even_after_queries(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut nums = nums;
        let mut total: i32 = nums.iter().filter(|&&v| v % 2 == 0).sum();
        let mut results: Vec<i32> = Vec::with_capacity(nums.len());
        for query in queries.iter() {
            let val = query[0];
            let index = query[1] as usize;
            let num = nums[index];
            nums[index] = num + val;
            let is_new_even = nums[index] % 2 == 0;
            let is_old_even = num % 2 == 0;
            if is_new_even & is_old_even {
                total += val;
            } else if is_new_even & !is_old_even {
                total += nums[index];
            } else if !is_new_even & is_old_even {
                total -= num;
            }
            results.push(total);
        }
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_985() {
        assert_eq!(Solution::sum_even_after_queries(vec![1,2,3,4], vec![vec![1,0],vec![-3,1],vec![-4,0],vec![2,3]]), vec![8,6,2,4]);
    }
}

```
