---
title: 977. squares of a sorted array
date: '2022-06-20'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0977 squares of a sorted array
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={977}/>
 

  Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [-4,-1,0,3,10]

 >   Output: [0,1,9,16,100]

 >   Explanation: After squaring, the array becomes [16,1,0,9,100].

 >   After sorting, it becomes [0,1,9,16,100].

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [-7,-3,2,3,11]

 >   Output: [4,9,9,49,121]

  

   

  **Constraints:**

  

 >   	<span>1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> </span>10^4

 >   	-10^4 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^4

 >   	nums is sorted in non-decreasing order.

  

   

 >   Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


## Solution
Find the boundary between negative and positive and merge the squared result arrays.

### Python
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index = -1
        for i in range(1, n):
            if nums[i] >= 0 and nums[i - 1] < 0:
                index = i
                break
        if index == -1: # all positive or all negative
            if nums[0] >= 0:
                return list(map(lambda i: nums[i] * nums[i], range(n)))
            else:
                res = list(map(lambda i: nums[i] * nums[i], range(n)))
                res.reverse()
                return res
        subNums1 = list(map(lambda i: nums[i] * nums[i], range(index, n)))
        subNums2 = list(map(lambda i: nums[i] * nums[i], range(0, index)))
        subNums2.reverse()
        ans = []
        i = 0
        j = 0
        while i < len(subNums1) and j < len(subNums2):
            if subNums1[i] < subNums2[j]:
                ans.append(subNums1[i])
                i += 1
            else:
                ans.append(subNums2[j])
                j += 1
        if i < len(subNums1):
            for k in range(i, len(subNums1)):
                ans.append(subNums1[k])
        if j < len(subNums2):
            for k in range(j, len(subNums2)):
                ans.append(subNums2[k])
        return ans
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let index = nums.iter().position(|&num| num >= 0);
        if index.is_none() {
            let mut nums = nums;
            nums.reverse();
            return nums.iter().map(|&num| num * num).collect::<Vec<_>>();
        }
        let index = index.unwrap();
        if index == 0 {
            return nums.iter().map(|&num| num * num).collect::<Vec<_>>();
        }
        let mut back = index as i32 - 1;
        let mut forward = index as i32;
        let mut result: Vec<i32> = vec![0; n];
        let mut k = 0;
        while k < nums.len() {
            if back >= 0 && forward <= n as i32 - 1 {
                let back_sq = nums[back as usize] * nums[back as usize];
                let forward_sq = nums[forward as usize] * nums[forward as usize];    
                result[k] = if back_sq < forward_sq {
                    back -=1;
                    back_sq
                } else {
                    forward += 1;
                    forward_sq
                };
            } else if back < 0 && forward <= n as i32 - 1 {
                result[k] = nums[forward as usize] * nums[forward as usize]; 
                forward += 1;
            } else if back >= 0 && forward >= n as i32 {
                result[k] = nums[back as usize] * nums[back as usize];
                back -= 1;
            } else {
                break;
            }            
            k += 1;
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_977() {
        assert_eq!(Solution::sorted_squares(vec![-4,-1,0,3,10]), vec![0,1,9,16,100]);
        assert_eq!(Solution::sorted_squares(vec![-4,-1,0,3,10]), vec![0,1,9,16,100]);
    }
}

```
