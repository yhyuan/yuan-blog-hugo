---
title: 1306. jump game iii
date: '2022-07-29'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 1306 jump game iii
---

 

  Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

  Notice that you can not jump outside of the array at any time.

   

 >   Example 1:

  

 >   Input: arr <TeX>=</TeX> [4,2,3,0,3,1,2], start <TeX>=</TeX> 5

 >   Output: true

 >   Explanation: 

 >   All possible ways to reach at index 3 with value 0 are: 

 >   index 5 -> index 4 -> index 1 -> index 3 

 >   index 5 -> index 6 -> index 4 -> index 1 -> index 3 

  

 >   Example 2:

  

 >   Input: arr <TeX>=</TeX> [4,2,3,0,3,1,2], start <TeX>=</TeX> 0

 >   Output: true 

 >   Explanation: 

 >   One possible way to reach at index 3 with value 0 is: 

 >   index 0 -> index 4 -> index 1 -> index 3

  

 >   Example 3:

  

 >   Input: arr <TeX>=</TeX> [3,0,2,1,2], start <TeX>=</TeX> 2

 >   Output: false

 >   Explanation: There is no way to reach at index 1 with value 0.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> arr.length <TeX>\leq</TeX> 5  10^4

 >   	0 <TeX>\leq</TeX> arr[i] < arr.length

 >   	0 <TeX>\leq</TeX> start < arr.length


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn helper(arr: &Vec<i32>, visited: &mut Vec<bool>, index: usize) -> bool {
        let n = arr.len();
        visited[index] = true;
        if arr[index] == 0 {
            return true;
        }
        let val = arr[index] as usize;
        if index + val < n && !visited[index + val] {
            if Self::helper(arr, visited, index + val) {
                return true;
            }
        }
        if index >= val && !visited[index - val] {
            if Self::helper(arr, visited, index - val) {
                return true;
            }
        }
        false
    }

    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        let start = start as usize;
        let n = arr.len();
        let mut visited: Vec<bool> = vec![false; n];
        Self::helper(&arr, &mut visited, start)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1306() {
        assert_eq!(Solution::can_reach(vec![4,2,3,0,3,1,2], 5), true);
        assert_eq!(Solution::can_reach(vec![4,2,3,0,3,1,2], 0), true);
        assert_eq!(Solution::can_reach(vec![3,0,2,1,2], 2), false);
    }
}

```
