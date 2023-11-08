---
title: 239. sliding window maximum
date: '2021-11-24'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0239 sliding window maximum
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={239}/>




  [239] Sliding Window Maximum

 

  You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

  Return the max sliding window.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,3,-1,-3,5,3,6,7], k <TeX>=</TeX> 3

 >   Output: [3,3,5,5,6,7]

 >   Explanation: 

 >   Window position                Max

 >   ---------------               -----

 >   [1  3  -1] -3  5  3  6  7       3

 >    1 [3  -1  -3] 5  3  6  7       3

 >    1  3 [-1  -3  5] 3  6  7       5

 >    1  3  -1 [-3  5  3] 6  7       5

 >    1  3  -1  -3 [5  3  6] 7       6

 >    1  3  -1  -3  5 [3  6  7]      7

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1], k <TeX>=</TeX> 1

 >   Output: [1]

  

 >   Example 3:

  

 >   Input: nums <TeX>=</TeX> [1,-1], k <TeX>=</TeX> 1

 >   Output: [1,-1]

  

 >   Example 4:

  

 >   Input: nums <TeX>=</TeX> [9,11], k <TeX>=</TeX> 2

 >   Output: [11]

  

 >   Example 5:

  

 >   Input: nums <TeX>=</TeX> [4,-2], k <TeX>=</TeX> 2

 >   Output: [4]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^5

 >   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4

 >   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> nums.length


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        if k > n {
            panic!("k must be smaller than or equal to array size.");
        }
        if n == 0 {
            panic!("Array can not be empty.");
        }
        if k == n {
            let max = nums.iter().max().unwrap();
            return vec![*max];
        }
        if k == 1 {
            return nums;
        }
        //println!("nums: {:?}", nums);
        let mut max_value = i32::MIN; 
        let mut results: Vec<i32> = Vec::with_capacity(n - k + 1);
        for i in 0..=n-k {
            if i == 0 {
                let value = (nums[i..=i+k-1]).iter().max().unwrap();
                max_value = *value;
                results.push(max_value);
            } else {
                //nums[i - 1] left and nums[i + k - 1] enter
                if nums[i - 1] < max_value {
                    if nums[i + k - 1] > max_value {
                        max_value = nums[i + k - 1];
                    }
                    results.push(max_value);
                } else {
                    let value = (nums[i..=i+k-1]).iter().max().unwrap();
                    max_value = *value;
                    results.push(max_value);    
                }
            }
            //println!("{}----{}", nums[i], nums[i + k - 1]);
        }
        //println!("results: {:?}", results);
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_239() {
        assert_eq!(
            Solution::max_sliding_window(vec![9, 10, 9, -7, -4, -8, 2, -6], 5),
            vec![10, 10, 9, 2]
        );
        
        assert_eq!(
            Solution::max_sliding_window(vec![1, 3, 1, 2, 0, 5], 3),
            vec![3, 3, 2, 5]
        );
        assert_eq!(Solution::max_sliding_window(vec![7, 2, 4], 2), vec![7, 4]);
        assert_eq!(Solution::max_sliding_window(vec![1, -1], 1), vec![1, -1]);
        assert_eq!(
            Solution::max_sliding_window(vec![1, 3, -1, -3, 5, 3, 6, 7], 3),
            vec![3, 3, 5, 5, 6, 7]
        );
        
    }
}

```
