---
title: 16. 3sum closest
date: '2021-05-17'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0016 3sum closest
---

 

  Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

  Return the sum of the three integers.

  You may assume that each input would have exactly one solution.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [-1,2,1,-4], target <TeX>=</TeX> 1

 >   Output: 2

 >   Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 <TeX>=</TeX> 2).

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [0,0,0], target <TeX>=</TeX> 1

 >   Output: 0

  

   

  **Constraints:**

  

 >   	3 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 1000

 >   	-1000 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 1000

 >   	-10^4 <TeX>\leq</TeX> target <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn count_zero(nums: &Vec<i32>) -> usize {
        let mut zero_count = 0;
        for &num in nums.iter() {
            if num == 0 {
                zero_count += 1;
            }
        }
        zero_count
    }
    pub fn binary_search(nums: &Vec<i32>, start: usize, end: usize, val: i32) -> i32 {
        if start == end {
            return nums[start];
        }
        if start + 1 == end {
            let start_diff = (nums[start] - val).abs();
            let end_diff = (nums[end] - val).abs();
            if start_diff < end_diff {
                return nums[start];
            } else {
                return nums[end];
            }
        }
        let middle = (start + end) / 2;
        if nums[middle] == val {
            nums[middle]
        } else if nums[middle] > val {
            Solution::binary_search(nums, start, middle, val)
        } else {
            Solution::binary_search(nums, middle, end, val)
        }
    }

    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        if nums.len() < 3 {
            panic!("Wrong input!");
        }
        let zero_count = Solution::count_zero(&nums);
        let mut nums = nums;
        if zero_count >= 3 {
            nums = nums.into_iter().filter(|&x| x != 0).collect();
            nums.push(0i32);
            nums.push(0i32);
            nums.push(0i32);
        }
        let n = nums.len();
        //let mut start = Instant::now();
        nums.sort();
        let mut hashmap: HashMap<(i32, i32), i32> = HashMap::with_capacity(n);
        let mut result = i32::MAX;
        for (i, &num_1) in nums.iter().enumerate() {
            for j in i+1..nums.len()-1 {
                let num_2 = nums[j];
                if !hashmap.contains_key(&(num_1, num_2)) {
                    let total_1 = nums[i] + nums[j] + nums[j + 1];
                    let total_2 = nums[i] + nums[j] + nums[n - 1];
                    let mut total = i32::MAX;
                    if total_1 >= target {
                        hashmap.insert((num_1, num_2), total_1);
                        total = total_1;
                    } else if total_2 <= target {
                        hashmap.insert((num_1, num_2), total_2);
                        total = total_2;
                    } else {
                        let val = target - num_1 - num_2;
                        let val = Solution::binary_search(&nums, j + 1, n - 1, val);
                        total = val + num_1 + num_2;
                        hashmap.insert((num_1, num_2), total);
                    }
                    if result == i32::MAX {
                        result = total;
                    } else if (total - target).abs() < (result - target).abs() {
                        result = total;
                    }
                }
            }
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_16() {
        
        assert_eq!(Solution::three_sum_closest(vec![1,1,-1,-1,3], -1), -1);
        /*
        assert_eq!(Solution::three_sum_closest(vec![-1, 2, 1, -4], 1), 2);
        assert_eq!(Solution::three_sum_closest(vec![1, 2, 3], 1), 6);
        assert_eq!(
            Solution::three_sum_closest(vec![1, 2, 4, 8, 16, 32, 64, 128], 82),
            82
        );
        */
    }
}

```
