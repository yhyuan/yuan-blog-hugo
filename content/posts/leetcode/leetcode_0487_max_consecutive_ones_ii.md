---
title: 487. max consecutive ones ii
date: '2022-03-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0487 max consecutive ones ii
---


Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.



 



 > Example 1:



 > Input: nums <TeX>=</TeX> [1,0,1,1,0]

 > Output: 4

 > Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

 > Example 2:



 > Input: nums <TeX>=</TeX> [1,0,1,1,0,1]

 > Output: 4

 



**Constraints:**



 > 1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 105

 > nums[i] is either 0 or 1.

 



 > Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut count = 0;
        let mut vals: Vec<i32> = vec![];
        for i in 0..n {
            if nums[i] == 0 {
                vals.push(count);
                count = 0;
            } else {
                count += 1;
            }
        }
        vals.push(count);
        println!("vals: {:?}", vals);
        let mut res = *vals.iter().max().unwrap();
        for i in 1..vals.len() {
            res = i32::max(res, vals[i - 1] + vals[i] + 1);
        }
        res
    }
}
*/
impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pre_count = i32::MIN;
        let mut count = 0;
        let mut res = i32::MIN;
        for i in 0..n {
            if nums[i] == 0 {
                res = if pre_count == i32::MIN {
                    i32::max(res,  count)
                } else {
                    i32::max(res, pre_count + count + 1)
                };
                pre_count = count;
                count = 0;
            } else {
                count += 1;
            }
        }
        res = if pre_count == i32::MIN {
            i32::max(res,  count)
        } else {
            i32::max(res, pre_count + count + 1)
        };
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_487() {
        //assert_eq!(Solution::find_max_consecutive_ones(vec![1,0,1,1,0]), 4);
        assert_eq!(Solution::find_max_consecutive_ones(vec![1,1,0,1]), 4);
    }
}

```
