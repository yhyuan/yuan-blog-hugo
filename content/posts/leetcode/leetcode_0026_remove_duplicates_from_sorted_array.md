---
title: 26. remove duplicates from sorted array
date: '2021-05-27'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0026 remove duplicates from sorted array
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={26}/>
 

  Given an integer array nums sorted in non-decreasing order, remove the duplicates [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only once. The relative order of the elements should be kept the same.

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

  

 >   Input: nums <TeX>=</TeX> [1,1,2]

 >   Output: 2, nums <TeX>=</TeX> [1,2,_]

 >   Explanation: Your function should return k <TeX>=</TeX> 2, with the first two elements of nums being 1 and 2 respectively.

 >   It does not matter what you leave beyond the returned k (hence they are underscores).

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [0,0,1,1,1,2,2,3,3,4]

 >   Output: 5, nums <TeX>=</TeX> [0,1,2,3,4,_,_,_,_,_]

 >   Explanation: Your function should return k <TeX>=</TeX> 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.

 >   It does not matter what you leave beyond the returned k (hence they are underscores).

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 3  10^4

 >   	-100 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 100

 >   	nums is sorted in non-decreasing order.


## Solution
### Python
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = nums[0]
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != cur:
                cur = nums[i]
                nums[index] = cur
                index += 1
        return index
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    /*
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() == 0 {
            return 0;
        }
        if nums.len() == 1 {
            return 1;
        }
        let mut i = 0usize;
        let mut j = 0usize;
        loop {
            while j < nums.len() && nums[i] == nums[j] {
                j += 1;
            }
            if j == nums.len() {
                break;
            }
            i += 1;
            nums[i] = nums[j];
        }
        for _ in 0..nums.len() - i - 1 {
            nums.pop();
        }
        i as i32 + 1
    }
    */
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        nums.dedup();
        nums.len() as i32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_26() {
        assert_eq!(Solution::remove_duplicates(&mut vec![]), 0);
        let mut vec1 = vec![1, 1, 1, 1, 3];
        assert_eq!(Solution::remove_duplicates(&mut vec1), 2);
        assert_eq!(vec1, vec![1, 3]);
        let mut vec2 = vec![1, 1, 2];
        assert_eq!(Solution::remove_duplicates(&mut vec2), 2);
        assert_eq!(vec2, vec![1, 2]);
    }
}

```
