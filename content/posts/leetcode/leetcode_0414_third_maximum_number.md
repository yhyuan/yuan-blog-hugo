---
title: 414. third maximum number
date: '2022-03-03'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0414 third maximum number
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={414}/>
 

  Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [3,2,1]

 >   Output: 1

 >   Explanation: The third maximum is 1.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,2]

 >   Output: 2

 >   Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [2,2,3,1]

 >   Output: 1

 >   Explanation: Note that the third maximum here means the third maximum distinct number.

 >   Both numbers with value 2 are both considered as second maximum.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^4

 >   	-2^31 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 2^31 - 1

  

   

 >   Follow up: Can you find an O(n) solution?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn third_max(nums: Vec<i32>) -> i32 {
        let mut maxs: Vec<i64> = vec![i64::MIN, i64::MIN, i64::MIN];
        for &num in nums.iter() {
            let num = num as i64;
            if num == maxs[0] || num == maxs[1] || num == maxs[2] {
                continue;
            }
            if num > maxs[0] {
                maxs[2] = maxs[1];
                maxs[1] = maxs[0];
                maxs[0] = num;
            } else if num > maxs[1] {
                maxs[2] = maxs[1];
                maxs[1] = num;
            } else if num > maxs[2] {
                maxs[2] = num;
            }
        }
        if maxs[2] == i64::MIN {maxs[0] as i32} else {maxs[2] as i32}
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_414() {
        assert_eq!(Solution::third_max(vec![3,2,1]), 1);
        assert_eq!(Solution::third_max(vec![1,2]), 2);
        assert_eq!(Solution::third_max(vec![2,2,3,1]), 1);
        assert_eq!(Solution::third_max(vec![1,2,i32::MIN]), i32::MIN);
    }
}

```
