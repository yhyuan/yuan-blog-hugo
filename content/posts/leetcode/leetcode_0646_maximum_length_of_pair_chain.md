---
title: 646. maximum length of pair chain
date: '2022-04-12'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0646 maximum length of pair chain
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={646}/>
 

  You are given an array of n pairs pairs where pairs[i] <TeX>=</TeX> [lefti, righti] and lefti < righti.

  A pair p2 <TeX>=</TeX> [c, d] follows a pair p1 <TeX>=</TeX> [a, b] if b < c. A chain of pairs can be formed in this fashion.

  Return the length longest chain which can be formed.

  You do not need to use up all the given intervals. You can select pairs in any order.

   

 >   Example 1:

  

 >   Input: pairs <TeX>=</TeX> [[1,2],[2,3],[3,4]]

 >   Output: 2

 >   Explanation: The longest chain is [1,2] -> [3,4].

  

 >   Example 2:

  

 >   Input: pairs <TeX>=</TeX> [[1,2],[7,8],[4,5]]

 >   Output: 3

 >   Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

  

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> pairs.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 1000

 >   	-1000 <TeX>\leq</TeX> lefti < righti < 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn helper(pairs: &Vec<Vec<i32>>, memo: &mut HashMap<usize, i32>, index: usize) -> i32 {
        if index >= pairs.len() {
            return 0;
        }
        if memo.contains_key(&index) {
            return memo[&index];
        }
        let n = pairs.len();
        if index == n - 1 {
            memo.insert(index, 1);
            return 1i32;
        }
        let mut res = Self::helper(pairs, memo, index + 1); // index is ignored
        let pair_end = pairs[index][1];
        let next_index = pairs.iter().position(|pair| pair[0] > pair_end);
        res = i32::max(res, if next_index.is_none() {1} else {Self::helper(pairs, memo, next_index.unwrap()) + 1});
        memo.insert(index, res);
        res
    }
    pub fn find_longest_chain(pairs: Vec<Vec<i32>>) -> i32 {
        let mut pairs = pairs;
        pairs.sort_by(|a, b| a[0].partial_cmp(&b[0]).unwrap());
        let mut memo: HashMap<usize, i32> = HashMap::new();
        
        Self::helper(&pairs, &mut memo, 0)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_646() {
        assert_eq!(Solution::find_longest_chain(vec![vec![1,2],vec![2,3],vec![3,4]]), 2);
        assert_eq!(Solution::find_longest_chain(vec![vec![1,2],vec![7,8],vec![4,5]]), 3);
    }
}

```
