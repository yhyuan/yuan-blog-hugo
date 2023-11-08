---
title: 268. missing number
date: '2021-12-08'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0268 missing number
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={268}/>
 

  Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

  Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [3,0,1]

 >   Output: 2

 >   Explanation: n <TeX>=</TeX> 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [0,1]

 >   Output: 2

 >   Explanation: n <TeX>=</TeX> 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [9,6,4,2,3,5,7,0,1]

 >   Output: 8

 >   Explanation: n <TeX>=</TeX> 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

  

 >   Example 4:

  

 >   Input: nums <TeX>=</TeX> [0]

 >   Output: 1

 >   Explanation: n <TeX>=</TeX> 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

  

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> nums.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> n

 >   	All the numbers of nums are unique.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut status: Vec<bool> = vec![false; nums.len() + 1];
        for num in nums {
            status[num as usize] = true;
        }
        status.iter().position(|&x| !x).unwrap() as i32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_268() {
        assert_eq!(Solution::missing_number(vec![9,6,4,2,3,5,7,0,1]), 8);
    }
}

```
