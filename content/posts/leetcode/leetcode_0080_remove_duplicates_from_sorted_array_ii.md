---
title: 80. remove duplicates from sorted array ii
date: '2021-07-20'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0080 remove duplicates from sorted array ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={80}/>
 

  Given an integer array nums sorted in non-decreasing order, remove some duplicates [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears at most twice. The relative order of the elements should be kept the same.

  Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

  Return k after placing the final result in the first k slots of nums.

  Do not allocate extra space for another array. You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with O(1) extra memory.

  Custom Judge:

  The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array

  int[] expectedNums = [...]; // The expected answer with correct length

  int k = removeDuplicates(nums); // Calls your implementation

  assert k == expectedNums.length;

  for (int i = 0; i < k; i++) {

      assert nums[i] == expectedNums[i];

  }
```
If all assertions pass, then your solution will be accepted.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,1,1,2,2,3]

 >   Output: 5, nums <TeX>=</TeX> [1,1,2,2,3,_]

 >   Explanation: Your function should return k <TeX>=</TeX> 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

 >   It does not matter what you leave beyond the returned k (hence they are underscores).

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [0,0,1,1,1,1,2,3,3]

 >   Output: 7, nums <TeX>=</TeX> [0,0,1,1,2,3,3,_,_]

 >   Explanation: Your function should return k <TeX>=</TeX> 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.

 >   It does not matter what you leave beyond the returned k (hence they are underscores).

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 3  10^4

 >   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4

 >   	nums is sorted in non-decreasing order.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    /*
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() <= 2 {
            return nums.len() as i32;
        }
        let n = nums.len();
        let mut index = 0usize;
        for i in 0..n - 2 {
            if nums[i] == nums[i+1] && nums[i+1] == nums[i+2] {
                continue;
            }
            nums[index] = nums[i];
            index += 1;
        }
        if index == 0 {
            for _ in 0..n - 2 {
                nums.pop();
            }    
            return 2i32;
        }
        if nums[index - 1] == nums[n - 2] && nums[index - 1] == nums[n - 1] {
            nums[index] = nums[n - 2];
            index += 1;
        } else {
            nums[index] = nums[n - 2];
            nums[index + 1] = nums[n - 1];
            index += 2;
        }
        for _ in 0..n - index {
            nums.pop();
        }
        //println!("n - k: {}", n - index);
        index as i32
    }
    */
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pre_val = i32::MAX;
        let mut i = 0;
        let mut count = 0;
        let mut j = 0;
        while i < n {
            let val = nums[i];
            if pre_val != val {
                nums[j] = nums[i];
                j += 1;
                pre_val = val;
                count = 1;
            } else {
                count += 1;
                if count <= 2 {
                    nums[j] = nums[i];
                    j += 1;
                }
            }
            i += 1;
        }
        for _ in j..n {
            nums.pop();
        }
        j as i32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_80() {
        /*
        let mut nums = vec![1,1,1,2,2,3];
        assert_eq!(Solution::remove_duplicates(&mut nums), 5);
        assert_eq!(nums, vec![1,1,2,2,3]);

        let mut nums = vec![0,0,1,1,1,1,2,3,3];
        assert_eq!(Solution::remove_duplicates(&mut nums), 7);
        assert_eq!(nums, vec![0,0,1,1,2,3,3]);
        */
        //[1,1,1]
        let mut nums = vec![1,1,1];
        assert_eq!(Solution::remove_duplicates(&mut nums), 2);
        assert_eq!(nums, vec![1,1]);

    }
}

```
