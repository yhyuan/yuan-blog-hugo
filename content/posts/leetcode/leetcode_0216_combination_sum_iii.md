---
title: 216. combination sum iii
date: '2021-11-02'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0216 combination sum iii
---

 

  Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

  

  	Only numbers 1 through 9 are used.

  	Each number is used at most once.

  

  Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

   

 >   Example 1:

  

 >   Input: k <TeX>=</TeX> 3, n <TeX>=</TeX> 7

 >   Output: [[1,2,4]]

 >   Explanation:

 >   1 + 2 + 4 <TeX>=</TeX> 7

 >   There are no other valid combinations.

 >   Example 2:

  

 >   Input: k <TeX>=</TeX> 3, n <TeX>=</TeX> 9

 >   Output: [[1,2,6],[1,3,5],[2,3,4]]

 >   Explanation:

 >   1 + 2 + 6 <TeX>=</TeX> 9

 >   1 + 3 + 5 <TeX>=</TeX> 9

 >   2 + 3 + 4 <TeX>=</TeX> 9

 >   There are no other valid combinations.

  

 >   Example 3:

  

 >   Input: k <TeX>=</TeX> 4, n <TeX>=</TeX> 1

 >   Output: []

 >   Explanation: There are no valid combinations.

 >   Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 <TeX>=</TeX> 10 and since 10 > 1, there are no valid combination.

  

 >   Example 4:

  

 >   Input: k <TeX>=</TeX> 3, n <TeX>=</TeX> 2

 >   Output: []

 >   Explanation: There are no valid combinations.

  

 >   Example 5:

  

 >   Input: k <TeX>=</TeX> 9, n <TeX>=</TeX> 45

 >   Output: [[1,2,3,4,5,6,7,8,9]]

 >   Explanation:

 >   1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 <TeX>=</TeX> 45

 >   There are no other valid combinations.

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> k <TeX>\leq</TeX> 9

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 60


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn combination_sum3_helper(k: i32, target: i32, values: &mut Vec<i32>) -> Vec<Vec<i32>> {
        //println!("values: {:?}", values);
        let values_sum = values.iter().sum(); // target - value_sum is the new target. 
        if target < values_sum {
            return vec![];
        } else if target == values_sum {
            if k == 0 {
                return  vec![values.clone()];
            } else {
                return vec![];
            }
        } else { // target > values_sum
            if k > 0 {
                let mut final_results: Vec<Vec<i32>> = vec![];
                let start_value = if values.len() == 0 {1} else {values[values.len() - 1] + 1};
                for i in start_value..=9 {
                    if i <= target - values_sum && !values.contains(&i) {
                        values.push(i);
                        let single_results = Solution::combination_sum3_helper(k - 1, target, values);
                        for result in single_results {
                            final_results.push(result);
                        }
                        values.pop();
                    }
                }
                return  final_results;
            } else {
                return vec![];
            }
        }
    }
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        //1, 2, 3, 4, 5, 6, 7, 8, 9
        let mut values: Vec<i32> = vec![];
        Solution::combination_sum3_helper(k, n, &mut values)
        //vec![]
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_216() {
        assert_eq!(Solution::combination_sum3(3, 7), vec![vec![1,2,4]]);
        assert_eq!(Solution::combination_sum3(3, 9), vec![vec![1,2,6],vec![1,3,5],vec![2,3,4]]);
        //assert_eq!(Solution::combination_sum3(4, 1), Vec::<Vec<i32>>new());
        //assert_eq!(Solution::combination_sum3(3, 2), Vec::<Vec<i32>>new());
        assert_eq!(Solution::combination_sum3(9, 45), vec![vec![1,2,3,4,5,6,7,8,9]]);
    }
}

```
