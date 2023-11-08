---
title: 119. pascals triangle ii
date: '2021-08-26'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0119 pascals triangle ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={119}/>
 

  Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the Pascal's triangle.

  In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

  ![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

   

 >   Example 1:

 >   Input: rowIndex <TeX>=</TeX> 3

 >   Output: [1,3,3,1]

 >   Example 2:

 >   Input: rowIndex <TeX>=</TeX> 0

 >   Output: [1]

 >   Example 3:

 >   Input: rowIndex <TeX>=</TeX> 1

 >   Output: [1,1]

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> rowIndex <TeX>\leq</TeX> 33

  

   

 >   Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        if row_index == 0 {
            return vec![1];
        }
        if row_index == 1 {
            return vec![1, 1];
        }
        let pre_results = Solution::get_row(row_index - 1);
        let row_index = row_index as usize;
        let mut results: Vec<i32> = Vec::with_capacity(row_index + 1); //vec![1];
        results.push(1);
        for i in 1..pre_results.len() {
            results.push(pre_results[i] + pre_results[i - 1]);
        }
        results.push(1);
        results
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_119() {
        assert_eq!(Solution::get_row(0), vec![1]);
        assert_eq!(Solution::get_row(4), vec![1, 4, 6, 4, 1])
    }
}

```
