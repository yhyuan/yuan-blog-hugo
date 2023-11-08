---
title: 81. search in rotated sorted array ii
date: '2021-07-21'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0081 search in rotated sorted array ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={81}/>
 

  There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

  Before being passed to your function, nums is rotated at an unknown pivot index k (0 <TeX>\leq</TeX> k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

  Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

  You must decrease the overall operation steps as much as possible.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [2,5,6,0,0,1,2], target <TeX>=</TeX> 0

 >   Output: true

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [2,5,6,0,0,1,2], target <TeX>=</TeX> 3

 >   Output: false

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 5000

 >   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4

 >   	nums is guaranteed to be rotated at some pivot.

 >   	-10^4 <TeX>\leq</TeX> target <TeX>\leq</TeX> 10^4

  

   

 >   Follow up: This problem is similar to [Search in Rotated Sorted Array](/problems/search-in-rotated-sorted-array/description/), but nums may contain duplicates. Would this affect the runtime complexity? How and why?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
/*
    pub fn search_binary_helper(nums: &Vec<i32>, target: i32, start: usize, end: usize) -> bool {
        if start == end {
            return target == nums[start];
        }
        if start + 1 == end {
            return target == nums[start] || target == nums[end];
        }
        let mid = (start + end) / 2;
        if nums[mid] == target {
            return true;
        }
        if nums[mid] > target {
            Solution::search_binary_helper(nums, target, start, mid)
        } else {
            Solution::search_binary_helper(nums, target, mid, end)
        }
    }
    pub fn search_helper(nums: &Vec<i32>, target: i32, start: usize, end: usize) -> bool {
        if start == end {
            return target == nums[start];
        }
        if start + 1 == end {
            return target == nums[start] || target == nums[end];
        }
        if nums[start] < nums[end] {
            return Solution::search_binary_helper(nums, target, start, end);
        }
        let mid = (start + end) / 2;
        if nums[mid] == target || nums[start] == target || nums[end] == target {
            return true;
        }
        if nums[mid] == nums[end] && nums[mid] == nums[start] {
            return Solution::search_helper(nums, target, start, mid) || Solution::search_helper(nums, target, mid, end);
        }
        if nums[mid] == nums[end] {
            return Solution::search_helper(nums, target, start, mid);
        }
        if nums[start] == nums[mid] {
            return Solution::search_helper(nums, target, mid, end);
        }
        println!("start: {}, mid: {}, end: {}, nums[mid]:{}", start, mid, end, nums[mid]);
        println!("first: {:?}, second: {:?}", &nums[start..=mid], &nums[mid..=end]);
        if nums[mid] > nums[start] { // peak on the right. 
            if target > nums[start] && target < nums[mid] {
                return Solution::search_binary_helper(nums, target, start, mid);
            } else {
                return Solution::search_helper(nums, target, mid, end);
            }
        } else {
            if target > nums[end] && target < nums[mid] {
                return Solution::search_binary_helper(nums, target, mid, end);
            } else {
                return Solution::search_helper(nums, target, start, mid);
            }
        }
    }
*/
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        //Solution::search_helper(&nums, target, 0, nums.len() - 1)
        //nums.iter().find(|&&num| num == target).is_some()
        let n = nums.len();
        if n == 0 {
            return false;
        }
        let shift = if nums[0] < nums[n - 1] {
            0usize
        } else {
            let mut low = 0;
            let mut high = n - 1;
            while low + 1 < high {
                while low < high && nums[low] == nums[low + 1] {
                    low += 1;
                }
                while high > low && nums[high] == nums[high - 1] {
                    high -= 1;
                }
                if low + 1 >= high {
                    break;
                } 
                let mid = low + (high - low) / 2;
                if nums[mid] > nums[low] {
                    low = mid;
                } else {
                    high = mid;
                }
            }
            high
        };
        let mut low = shift;
        let mut high = shift + n - 1;
        while low + 1 < high {
            let mid = low + (high - low) / 2;
            if nums[mid % n] == target {
                return true;
            }
            if nums[mid % n] > target {
                high = mid;
            } else {
                low = mid;
            }
        }
        nums[high % n] == target || nums[low % n] == target
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_81() {
        assert_eq!(Solution::search(vec![2,5,6,0,0,1,2], 0), true);
        assert_eq!(Solution::search(vec![2,5,6,0,0,1,2], 3), false);
        assert_eq!(Solution::search(vec![0,0,1,2,2,5,6], 0), true);
        assert_eq!(Solution::search(vec![0,0,1,2,2,5,6,], 3), false);
        assert_eq!(Solution::search(vec![
            1,1,1,1,1,
            1,1,1,1,13,
            1,1,1,1,1,
            1,1,1,1,1,
            1,1
        ], 13), true);
        assert_eq!(Solution::search(vec![3,5,1], 3), true);
    }
}

```
