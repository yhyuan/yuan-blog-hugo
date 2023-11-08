---
title: 784. letter case permutation
date: '2022-05-15'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0784 letter case permutation
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={784}/>
 

  Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

  Return a list of all possible strings we could create. You can return the output in any order.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "a1b2"

 >   Output: ["a1b2","a1B2","A1b2","A1B2"]

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "3z4"

 >   Output: ["3z4","3Z4"]

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "12345"

 >   Output: ["12345"]

  

 >   Example 4:

  

 >   Input: s <TeX>=</TeX> "0"

 >   Output: ["0"]

  

   

  **Constraints:**

  

 >   	s will be a string with length between 1 and 12.

 >   	s will consist only of letters or digits.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn helper(chars: &Vec<char>, index: usize) -> Vec<String> {
        if index == chars.len() {
            return vec!["".to_owned()];
        }
        let mut find_index = usize::MAX;
        for j in index..chars.len() {
            if chars[j] >= 'a' && chars[j] <= 'z' {
                find_index = j;
                break;
            }
        }
        if find_index == usize::MAX {
            let str = (index..chars.len()).into_iter().map(|k| chars[k]).collect::<String>();
            return vec![str];
        }
        let pre_results = Self::helper(chars, find_index + 1);
        //println!("pre_results: {:?}", pre_results);
        let mut results: Vec<String> = Vec::new();
        for k in 0..pre_results.len() {
            let pre_s = (index..find_index).into_iter().map(|k| chars[k]).collect::<String>();
            let s1 = format!("{}{}{}", pre_s, chars[find_index], pre_results[k]);
            results.push(s1);
            let s2 = format!("{}{}{}", pre_s, chars[find_index].to_uppercase(), pre_results[k]);
            results.push(s2);
        }
        results
    }
    pub fn letter_case_permutation(s: String) -> Vec<String> {
        let s = s.to_lowercase();
        let chars = s.chars().collect::<Vec<_>>();
        Self::helper(&chars, 0)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_784() {
        assert_eq!(Solution::letter_case_permutation("a1b2".to_string()), vec_string!["a1b2","a1B2","A1b2","A1B2"]);
        assert_eq!(Solution::letter_case_permutation("3z4".to_string()), vec_string!["3z4","3Z4"]);
    }
}

```
