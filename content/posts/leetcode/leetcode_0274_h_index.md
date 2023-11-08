---
title: 274. h index
date: '2021-12-11'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0274 h index
---

 

  Given an array of integers citations where citations[i] is the number of citations a researcher received for their i^th paper, return compute the researcher's h-index.

  According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): A scientist has an index h if h of their n papers have at least h citations each, and the other n - h papers have no more than h citations each.

  If there are several possible values for h, the maximum one is taken as the h-index.

   

 >   Example 1:

  

 >   Input: citations <TeX>=</TeX> [3,0,6,1,5]

 >   Output: 3

 >   Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.

 >   Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

  

 >   Example 2:

  

 >   Input: citations <TeX>=</TeX> [1,3,1]

 >   Output: 1

  

   

  **Constraints:**

  

 >   	n <TeX>=</TeX><TeX>=</TeX> citations.length

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 5000

 >   	0 <TeX>\leq</TeX> citations[i] <TeX>\leq</TeX> 1000


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let n = citations.len();
        let mut result = 0i32;
        for h in 0..=n {
            let count = citations.iter().filter(|&&x| x >= h as i32).count();
            if count >= h {
                result = i32::max(h as i32, result);
            } 
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_274() {
        assert_eq!(Solution::h_index(vec![3, 0, 6, 1, 5]), 3);
        assert_eq!(Solution::h_index(vec![1,3,1]), 1);
        assert_eq!(Solution::h_index(vec![1]), 1);
    }
}

```
