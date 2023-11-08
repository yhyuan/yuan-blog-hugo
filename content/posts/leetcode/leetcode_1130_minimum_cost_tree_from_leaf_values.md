---
title: 1130. minimum cost tree from leaf values
date: '2022-07-09'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1130 minimum cost tree from leaf values
---

 

  Given an array arr of positive integers, consider all binary trees such that:

  

  	Each node has either 0 or 2 children;

  	The values of arr correspond to the values of each leaf in an in-order traversal of the tree.

  	The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.

  

  Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

  A node is a leaf if and only if it has zero children.

   

 >   Example 1:

 >   ![](https://assets.leetcode.com/uploads/2021/08/10/tree1.jpg)

 >   Input: arr <TeX>=</TeX> [6,2,4]

 >   Output: 32

 >   Explanation: There are two possible trees shown.

 >   The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

  

 >   Example 2:

 >   ![](https://assets.leetcode.com/uploads/2021/08/10/tree2.jpg)

 >   Input: arr <TeX>=</TeX> [4,11]

 >   Output: 44

  

   

  **Constraints:**

  

 >   	2 <TeX>\leq</TeX> arr.length <TeX>\leq</TeX> 40

 >   	1 <TeX>\leq</TeX> arr[i] <TeX>\leq</TeX> 15

 >   	It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 2^31).


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn helper(arr: &Vec<i32>, max_values: &Vec<Vec<i32>>, hashmap: &mut HashMap<(usize, usize), i32>, start: usize, end: usize) -> i32 {
        let n = arr.len();
        if hashmap.contains_key(&(start, end)) {
            return hashmap[&(start, end)];
        }
        if start == end {
            hashmap.insert((start, end), 0i32);
            return 0i32;
        }
        if start + 1 == end {
            hashmap.insert((start, end), arr[start] * arr[end]);
            return arr[start] * arr[end];
        }
        let mut res = i32::MAX;
        for i in start..end {
            // [start..=i], i + 1..=end
            let left_max = max_values[start][i];
            let right_max = max_values[i + 1][end];
            let max_val = left_max * right_max;
            let left_res = Self::helper(arr, max_values, hashmap, start, i);
            let right_res = Self::helper(arr, max_values, hashmap, i + 1, end);
            let result = max_val + left_res + right_res;
            if res > result {
                res = result;
            }
        }
        hashmap.insert((start, end), res);
        res
    }
    pub fn mct_from_leaf_values(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut max_values = vec![vec![0; n]; n];
        for i in 0..n {
            let mut max_val = arr[i];
            for j in i..n {
                if i == j {
                    max_values[i][j] = max_val;
                } else {
                    max_values[i][j] = i32::max(max_values[i][j - 1], arr[j]);
                }
            }
        }
        let mut hashmap: HashMap<(usize, usize), i32> = HashMap::new();
        // println!("max_values: {:?}", max_values);
        Self::helper(&arr, &max_values, &mut hashmap, 0, arr.len() - 1)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1130() {
        assert_eq!(Solution::mct_from_leaf_values(vec![15,13,5,3,15]), 500);
        assert_eq!(Solution::mct_from_leaf_values(vec![6, 2, 4]), 32);
        assert_eq!(Solution::mct_from_leaf_values(vec![4, 11]), 44);
    }
}


```
