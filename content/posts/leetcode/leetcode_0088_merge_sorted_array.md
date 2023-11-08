---
title: 88. merge sorted array
date: '2021-07-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0088 merge sorted array
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={88}/>
 

  You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

  Merge nums1 and nums2 into a single array sorted in non-decreasing order.

  The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

   

 >   Example 1:

  

 >   Input: nums1 <TeX>=</TeX> [1,2,3,0,0,0], m <TeX>=</TeX> 3, nums2 <TeX>=</TeX> [2,5,6], n <TeX>=</TeX> 3

 >   Output: [1,2,2,3,5,6]

 >   Explanation: The arrays we are merging are [1,2,3] and [2,5,6].

 >   The result of the merge is [<u>1</u>,<u>2</u>,2,<u>3</u>,5,6] with the underlined elements coming from nums1.

  

 >   Example 2:

  

 >   Input: nums1 <TeX>=</TeX> [1], m <TeX>=</TeX> 1, nums2 <TeX>=</TeX> [], n <TeX>=</TeX> 0

 >   Output: [1]

 >   Explanation: The arrays we are merging are [1] and [].

 >   The result of the merge is [1].

  

 >   Example 3:

  

 >   Input: nums1 <TeX>=</TeX> [0], m <TeX>=</TeX> 0, nums2 <TeX>=</TeX> [1], n <TeX>=</TeX> 1

 >   Output: [1]

 >   Explanation: The arrays we are merging are [] and [1].

 >   The result of the merge is [1].

 >   Note that because m <TeX>=</TeX> 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

  

   

  **Constraints:**

  

 >   	nums1.length <TeX>=</TeX><TeX>=</TeX> m + n

 >   	nums2.length <TeX>=</TeX><TeX>=</TeX> n

 >   	0 <TeX>\leq</TeX> m, n <TeX>\leq</TeX> 200

 >   	1 <TeX>\leq</TeX> m + n <TeX>\leq</TeX> 200

 >   	-10^9 <TeX>\leq</TeX> nums1[i], nums2[j] <TeX>\leq</TeX> 10^9

  

   

 >   Follow up: Can you come up with an algorithm that runs in O(m + n) time?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut i = m - 1;
        let mut j = n - 1;
        let mut k = m + n - 1;
        while k >= 0 {
            let val1 = if i >= 0 {nums1[i as usize]} else {i32::MIN};
            let val2 = if j >= 0 {nums2[j as usize]} else {i32::MIN};
            if val1 >= val2 {
                nums1[k as usize] = val1;
                i -= 1;
            } else {
                nums1[k as usize] = val2;
                j -= 1;
            }
            k -= 1;
        }
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_88() {
        let mut vec1 = vec![1, 2, 3, 0, 0, 0];
        let mut vec2 = vec![2, 5, 6];
        Solution::merge(&mut vec1, 3, &mut vec2, 3);
        assert_eq!(vec1, vec![1, 2, 2, 3, 5, 6]);

        let mut vec1 = vec![1, 2, 3];
        let mut vec2 = vec![];
        Solution::merge(&mut vec1, 3, &mut vec2, 0);
        assert_eq!(vec1, vec![1, 2, 3]);

        let mut vec1 = vec![0, 0, 0];
        let mut vec2 = vec![1, 2, 3];
        Solution::merge(&mut vec1, 0, &mut vec2, 3);
        assert_eq!(vec1, vec![1, 2, 3]);
    }
}

```
