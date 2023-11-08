---
title: 215. kth largest element in an array
date: '2021-11-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0215 kth largest element in an array
---

 

  Given an integer array nums and an integer k, return the k^th largest element in the array.

  Note that it is the k^th largest element in the sorted order, not the k^th distinct element.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [3,2,1,5,6,4], k <TeX>=</TeX> 2

 >   Output: 5

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [3,2,3,1,2,4,5,5,6], k <TeX>=</TeX> 4

 >   Output: 4

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^4

 >   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::BinaryHeap;
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let n = nums.len();
        //max_heap
        let mut heap: BinaryHeap<i32> = BinaryHeap::with_capacity(k as usize);
        for i in 0..k {
            heap.push(-nums[i]);
        }
        for i in k..n {
            let val = heap.peek().unwrap();
            if *val > -nums[i] {
                heap.pop();
                heap.push(-nums[i]);    
            }
        }
        -heap.pop().unwrap()
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_215() {
        assert_eq!(Solution::find_kth_largest(vec![3,2,1,5,6,4], 2), 5);
        assert_eq!(Solution::find_kth_largest(vec![3,2,3,1,2,4,5,5,6], 4), 4);
    }
}

```
