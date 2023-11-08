---
title: 503. next greater element ii
date: '2022-03-21'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0503 next greater element ii
---

 

  Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

  The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

   

 >   Example 1:

  

 >   Input: nums <TeX>=</TeX> [1,2,1]

 >   Output: [2,-1,2]

 >   Explanation: The first 1's next greater number is 2; 

 >   The number 2 can't find next greater number. 

 >   The second 1's next greater number needs to search circularly, which is also 2.

  

 >   Example 2:

  

 >   Input: nums <TeX>=</TeX> [1,2,3,4,3]

 >   Output: [2,3,4,-1,4]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> nums.length <TeX>\leq</TeX> 10^4

 >   	-10^9 <TeX>\leq</TeX> nums[i] <TeX>\leq</TeX> 10^9


## Solution

### Python
```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [2 * n] * (2 * n)
        stack = []
        for i in reversed(range(2 * n)):
            while len(stack) > 0 and stack[-1] <= nums[i % n]:
                stack.pop()
            right[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums[i % n])
        return right[ : n]
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn next_greater_elements(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut results: Vec<i32> = Vec::with_capacity(n);
        for (i, &num) in nums.iter().enumerate() {
            let mut index = (i + 1) % n;
            while index != i {
                if nums[index] > num {
                    break;
                }
                index = (index + 1) % n;
            }
            if index == i {
                results.push(-1);
            } else {
                results.push(nums[index]);
            }
        }
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_503() {
        assert_eq!(Solution::next_greater_elements(vec![1,2,3,4,3]), vec![2,3,4,-1,4]);
    }
}

```
