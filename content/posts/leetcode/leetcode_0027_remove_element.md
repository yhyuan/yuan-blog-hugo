---
title: 27. remove element
date: '2021-05-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0027 remove element
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={27}/>
 

  Given an integer array nums and an integer val, remove all occurrences of val in nums [in-place](https://en.wikipedia.org/wiki/In-place_algorithm). The relative order of the elements may be changed.

  Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

  Return k after placing the final result in the first k slots of nums.

  Do not allocate extra space for another array. You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with O(1) extra memory.

  Custom Judge:

  The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array

  int val = ...; // Value to remove

  int[] expectedNums = [...]; // The expected answer with correct length.

                              // It is sorted with no values equaling val.

  int k = removeElement(nums, val); // Calls your implementation

  assert k == expectedNums.length;

  sort(nums, 0, k); // Sort the first k elements of nums

  for (int i = 0; i < actualLength; i++) {

      assert nums[i] == expectedNums[i];

  }
```
If all assertions pass, then your solution will be accepted.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [3,2,2,3], val <TeX>=</TeX> 3

 >   Output: 2, nums <TeX>=</TeX> [2,2,_,_]

 >   Explanation: Your function should return k <TeX>=</TeX> 2, with the first two elements of nums being 2.

 >   It does not matter what you leave beyond the returned k (hence they are underscores).

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [0,1,2,2,3,0,4,2], val <TeX>=</TeX> 2

 >   Output: 5, nums <TeX>=</TeX> [0,1,4,0,3,_,_,_]

 >   Explanation: Your function should return k <TeX>=</TeX> 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.

 >   Note that the five elements can be returned in any order.

 >   It does not matter what you leave beyond the returned k (hence they are underscores).

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 100

 >   	0 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 50

 >   	0 <TeX>\leq</TeX> val <TeX>\leq</TeX> 100


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let n = nums.len() as i32;
        let mut i = 0i32;
        let mut j = n - 1;
        loop {
            while j >= 0 && nums[j as usize] == val {
                j -= 1;
            }
            if j == -1 {
                return 0;
            }
            // j is the value from right, which is not val. 
            while i <= n - 1 && nums[i as usize] != val {
                i += 1;
            }
            if i == n {
                return nums.len() as i32;
            }
            // i is the value from left, which is val. 
            if j > i {
                let temp = nums[i as usize];
                nums[i as usize] = nums[j as usize];
                nums[j as usize] = temp;
            } else {
                break;
            }
        }
        i as i32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_27() {
        let mut vec1 = vec![0, 1, 2, 2, 3, 0, 4, 2];
        assert_eq!(Solution::remove_element(&mut vec1, 2), 5);
        assert_eq!(vec1[0..5], [0, 1, 4, 0, 3]);
        assert_eq!(Solution::remove_element(&mut vec![], 2), 0);
        assert_eq!(
            Solution::remove_element(&mut vec![1, 2, 2, 2, 2, 2, 2], 2),
            1
        );
        assert_eq!(
            Solution::remove_element(&mut vec![2, 2, 2, 2, 2, 2, 2], 2),
            0
        );
        assert_eq!(Solution::remove_element(&mut vec![1], 1), 0);
    }
}

```
