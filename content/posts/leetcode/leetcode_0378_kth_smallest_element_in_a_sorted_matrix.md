---
title: 378. kth smallest element in a sorted matrix
date: '2022-02-05'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0378 kth smallest element in a sorted matrix
---



Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the k^th smallest element in the matrix.

Note that it is the k^th smallest element in the sorted order, not the k^th distinct element.



>   Example 1:
>   Input: matrix <TeX>=</TeX> [[1,5,9],[10,11,13],[12,13,15]], k <TeX>=</TeX> 8
>   Output: 13
>   Explanation: The elements in the matrix are [1,5,9,10,11,12,13,<u>13</u>,15], and the 8^th smallest number is 13
>   Example 2:
>   Input: matrix <TeX>=</TeX> [[-5]], k <TeX>=</TeX> 1
>   Output: -5
**Constraints:**
>   	n <TeX>=</TeX><TeX>=</TeX> matrix.length
>   	n <TeX>=</TeX><TeX>=</TeX> matrix[i].length
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 300
>   	-10^9 <TeX>\leq</TeX> matrix[i][j] <TeX>\leq</TeX> 10^9
>   	All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> n^2


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::BinaryHeap;
impl Solution {
pub fn kth_smallest(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
let k = k as usize;
let mut heap: BinaryHeap<i32> = BinaryHeap::with_capacity(k);
let n = matrix.len();
for i in 0..n {
for j in 0..n {
if heap.len() < k {
heap.push(matrix[i][j]);
} else {
let val = heap.peek().unwrap();
if val > &matrix[i][j] {
heap.pop();
heap.push(matrix[i][j]);
}
}
}
}
let v = heap.peek().unwrap();
*v
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_378() {
assert_eq!(Solution::kth_smallest(vec![vec![1,5,9],vec![10,11,13],vec![12,13,15]], 8), 13);
assert_eq!(Solution::kth_smallest(vec![vec![1,2],vec![1,3]], 2), 1);
}
}

```
