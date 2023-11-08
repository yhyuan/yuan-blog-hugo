---
title: 9998. rank imbalance
date: '2022-09-29'
tags: ['leetcode', 'rust']
draft: true
description: Solution for leetcode 9998 rank imbalance
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={9998}/>
This one is pretty hard (for me at least). So you are given an array called rank and it has size of n and all its elements are 

from 1 to n and there's no duplicates. now there are several rules:



get an subarray of any possible size k (1 <TeX>\leq</TeX> k <TeX>\leq</TeX> n)

sort this subarray

find the imbalance of this subarray.

Imbalance is defined as, for each element a[i] at index i, a[i] - a[i - 1] > 1. Then a[i] contributes 1 imbalance. e.g. for subarry [1,5,4], after sorting it's [1,4,5]. 

So 1 and 4 this pair will contribute 1 imbalance. but 4 and 5 won't contribute imbalance. But for subarray [1, 4, ,6], there will be 2 imbalance.

Find the total imbalance of all possible subarray

For example, given [4,1,3,2] rank array. There could be [4], [1], [3], [2], [4,1], [1,3], [3,2], [4,1,3],[1,3,2] and [4,1,3,2] subarrays. [4,1], [1,3], [4,1,3] each 

of these 3 subarrays has 1 imbalance. So return 3.


## Solution
### Rust
```rust

pub struct Solution {}

// submission codes start here

impl Solution {
    pub fn rank_imbalance(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut index_arr = vec![0; n + 1];
        for i in 0..n {
            index_arr[nums[i] as usize] = i;
        }
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut max_stack = vec![0i32; n];
        let mut index = -1i32;
        for i in 0..n {
            // Find index 
            while index >= 0 && nums[max_stack[index as usize] as usize] < nums[i] {
                index -= 1
            }
            left[i] = if index < 0  {-1i32} else {max_stack[index as usize]};
            index += 1;
            max_stack[index as usize] = i as i32;
        }
        println!("left: {:?}", left);
        index = -1i32;
        for i in (0..n).rev() {
            while index >= 0 && nums[max_stack[index as usize] as usize] < nums[i] {
                index -= 1
            }
            right[i] = if index < 0 {n as i32 } else {max_stack[index as usize]};
            index += 1;
            max_stack[index as usize] = i as i32;
        }
        let mut count = 0i32;
        for i in 0..n {
            if nums[i] < n as i32 - 1 {
                let add_one_index = index_arr[nums[i] as usize + 1];
                if add_one_index > i {
                    count += (i as i32 + 1) * (add_one_index as i32 - right[i]);
                    if left[i] >= 0 {
                        count += (left[i] + 1) * (right[i] - i as i32);
                    }
                } else {
                    count += (left[i] - add_one_index as i32) * (n as i32 - i as i32);
                    if right[i] < n as i32 {
                        count += (i as i32 - left[i]) * (n as i32 - right[i]);
                    }
                }
            }
        }
        return count;
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_9998() {
        assert_eq!(Solution::rank_imbalance(vec![4, 1, 3, 2]), 3);
    }
}

```
