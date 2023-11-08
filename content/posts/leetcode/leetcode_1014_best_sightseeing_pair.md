---
title: 1014. best sightseeing pair
date: '2022-06-28'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1014 best sightseeing pair
---

 

  You are given an integer array values where values[i] represents the value of the i^th sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

  The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

  Return the maximum score of a pair of sightseeing spots.

   

 >   Example 1:

  

 >   Input: values <TeX>=</TeX> [8,1,5,2,6]

 >   Output: 11

 >   Explanation: i <TeX>=</TeX> 0, j <TeX>=</TeX> 2, values[i] + values[j] + i - j <TeX>=</TeX> 8 + 5 + 0 - 2 <TeX>=</TeX> 11

  

 >   Example 2:

  

 >   Input: values <TeX>=</TeX> [1,2]

 >   Output: 2

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> values.length <TeX>\leq</TeX> 5  10^4

 >   	1 <TeX>\leq</TeX> values[i] <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn max_score_sightseeing_pair(values: Vec<i32>) -> i32 {
        // f(i) = values[j] + j + max(values[i] + i)  i < j. 
        // values[i] + values[j] + i - j => values[i] + i and values[j] - j
        let n = values.len();
        let mut dp = values[0] + 0i32;
        let mut max_val = i32::MIN;
        for i in 1..n {
            let val = values[i] - i as i32 + dp;
            max_val = i32::max(max_val, val);
            dp = i32::max(dp, values[i] + i as i32);
        }
        max_val
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1014() {
        assert_eq!(Solution::max_score_sightseeing_pair(vec![8,1,5,2,6]), 11);
        assert_eq!(Solution::max_score_sightseeing_pair(vec![1,2]), 2);
    }
}

```
