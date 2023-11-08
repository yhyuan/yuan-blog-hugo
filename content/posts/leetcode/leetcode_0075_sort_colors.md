---
title: 75. sort colors
date: '2021-07-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0075 sort colors
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={75}/>
 

  Given an array nums with n objects colored red, white, or blue, sort them [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

  We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

  You must solve this problem without using the library's sort function.

   

 >   Example 1:

 >   Input: nums <TeX>=</TeX> [2,0,2,1,1,0]

 >   Output: [0,0,1,1,2,2]

 >   Example 2:

 >   Input: nums <TeX>=</TeX> [2,0,1]

 >   Output: [0,1,2]

 >   Example 3:

 >   Input: nums <TeX>=</TeX> [0]

 >   Output: [0]

 >   Example 4:

 >   Input: nums <TeX>=</TeX> [1]

 >   Output: [1]

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> nums.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 300

 >   	nums[i] is 0, 1, or 2.

  

   

 >   Follow up: Could you come up with a one-pass algorithm using only constant extra space?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut count_0 = 0usize; 
        let mut count_1 = 0usize;
        let mut count_2 = 0usize;
        for &num in nums.iter() {
            if num == 0 {
                count_0 += 1;
            } else if num == 1 {
                count_1 += 1;
            } else if num == 2 {
                count_2 += 1;
            } else {
                panic!("Wrong input!")
            }
        }
        for i in 0..count_0 {
            nums[i] = 0;
        }
        for i in count_0..count_0 + count_1 {
            nums[i] = 1;
        }
        for i in count_0 + count_1..nums.len() {
            nums[i] = 2;
        }
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_75() {
        let mut vec = vec![
            1, 2, 0, 1, 2, 2, 2, 0, 0, 0, 2, 1, 1, 2, 0, 1, 2, 2, 1, 1, 0,
        ];
        Solution::sort_colors(&mut vec);
        assert_eq!(
            vec,
            vec![0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
        );

        let mut vec = vec![];
        Solution::sort_colors(&mut vec);
        let empty: Vec<i32> = vec![];
        assert_eq!(vec, empty);

        let mut vec = vec![2, 2, 2];
        Solution::sort_colors(&mut vec);
        assert_eq!(vec, vec![2, 2, 2]);
    }
}

```
