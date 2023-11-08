---
title: 125. valid palindrome
date: '2021-09-01'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0125 valid palindrome
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={125}/>
 

  Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "A man, a plan, a canal: Panama"

 >   Output: true

 >   Explanation: "amanaplanacanalpanama" is a palindrome.

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "race a car"

 >   Output: false

 >   Explanation: "raceacar" is not a palindrome.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 2  10^5

 >   	s consists only of printable ASCII characters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut chars: Vec<char> = vec![];
        for ch in s.to_lowercase().chars() {
            match ch {
                '0'..='9' | 'a'..='z' => {
                    chars.push(ch);
                },
                _ => {

                }
            }
        }
        if chars.len() == 0 {
            return true;
        }
        for i in 0..chars.len()/2 {
            if chars[i] != chars[chars.len() - 1 - i] {
                return false;
            }
        }
        true
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_125() {
        assert_eq!(Solution::is_palindrome("A man, a plan, a canal: Panama".to_string()), true);
        assert_eq!(Solution::is_palindrome("race a car".to_string()), false);
    }
}

```
