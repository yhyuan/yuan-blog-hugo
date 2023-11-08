---
title: 60. permutation sequence
date: '2021-06-30'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0060 permutation sequence
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={60}/>
 

  The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

  By listing and labeling all of the permutations in order, we get the following sequence for n <TeX>=</TeX> 3:

  <ol>

  	"123"

  	"132"

  	"213"

  	"231"

  	"312"

  	"321"

  </ol>

  Given n and k, return the k^th permutation sequence.

   

 >   Example 1:

 >   Input: n <TeX>=</TeX> 3, k <TeX>=</TeX> 3

 >   Output: "213"

 >   Example 2:

 >   Input: n <TeX>=</TeX> 4, k <TeX>=</TeX> 9

 >   Output: "2314"

 >   Example 3:

 >   Input: n <TeX>=</TeX> 3, k <TeX>=</TeX> 1

 >   Output: "123"

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 9

 >   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> n!


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn factorial(n: usize) -> usize {
        let values: Vec<usize> = vec![1, 2, 6, 24, 120, 720, 5040, 40320, 362880];
        values[n - 1]
    }
    
    pub fn get_permutation_sub(chars: Vec<char>, k: i32) -> String {
        if k == 0 && chars.len() == 1 {
            return chars.into_iter().collect();
        }
        let size = Solution::factorial(chars.len() - 1) as i32;
        let index = (k / size) as usize;
        let new_chars: Vec<char> = (0..chars.len()).filter(|i| *i != index).map(|i| chars[i]).collect();
        let new_k = k % size;
        let mut result = Solution::get_permutation_sub(new_chars, new_k);
        result.insert(0, chars[index]);
        result
    }

    pub fn get_permutation(n: i32, k: i32) -> String {
        if n > 9 {
            panic!("n value can not be largerthan 9!")
        }
        if k > Solution::factorial(n as usize) as i32 {
            panic!("k value is too large!")
        }
        let chars: Vec<char> = (1..=n).map(|i| std::char::from_digit(i as u32, 10).unwrap()).collect();
        Solution::get_permutation_sub(chars, k - 1)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_60() {
        assert_eq!(Solution::get_permutation(3, 3), "213".to_string());
        assert_eq!(Solution::get_permutation(4, 9), "2314".to_string());
        assert_eq!(Solution::get_permutation(3, 1), "123".to_string());
    }
}

```
