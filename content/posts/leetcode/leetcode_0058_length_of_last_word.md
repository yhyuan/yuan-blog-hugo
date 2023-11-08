---
title: 58. length of last word
date: '2021-06-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0058 length of last word
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={58}/>
 

  Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

  A word is a maximal substring consisting of non-space characters only.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "Hello World"

 >   Output: 5

 >   Explanation: The last word is "World" with length 5.

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "   fly me   to   the moon  "

 >   Output: 4

 >   Explanation: The last word is "moon" with length 4.

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "luffy is still joyboy"

 >   Output: 6

 >   Explanation: The last word is "joyboy" with length 6.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 10^4

 >   	s consists of only English letters and spaces ' '.

 >   	There will be at least one word in s.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut chars: Vec<char> = s.trim().chars().collect();
        chars.reverse();
        for i in 0..chars.len() {
            if chars[i] == ' ' {
                return i as i32;
            }
        }
        chars.len() as i32
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_58() {
        assert_eq!(Solution::length_of_last_word("Hello World".to_owned()), 5);
        assert_eq!(Solution::length_of_last_word("       ".to_owned()), 0);
        assert_eq!(Solution::length_of_last_word("".to_owned()), 0);
        assert_eq!(Solution::length_of_last_word("     rrrrr  ".to_owned()), 5);
    }
}

```
