---
title: 67. add binary
date: '2021-07-07'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0067 add binary
---

 

  Given two binary strings a and b, return their sum as a binary string.

   

 >   Example 1:

 >   Input: a <TeX>=</TeX> "11", b <TeX>=</TeX> "1"

 >   Output: "100"

 >   Example 2:

 >   Input: a <TeX>=</TeX> "1010", b <TeX>=</TeX> "1011"

 >   Output: "10101"

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> a.length, b.length <TeX>\leq</TeX> 10^4

 >   	a and b consist only of '0' or '1' characters.

 >   	Each string does not contain leading zeros except for the zero itself.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn add_one_char(carry: bool, a_char: char) -> (bool, char) {
        if carry {
            if a_char == '0' {
                (false, '1')
            } else {
                (true, '0')
            }
         } else {
            (false, a_char) 
         }
    }
    pub fn add_tow_chars(carry: bool, a_char: char, b_char: char) -> (bool, char) {
        if carry {
            match (a_char, b_char) {
                ('0', '0') => {
                    (false, '1')
                },
                ('0', '1') => {
                    (true, '0')
                },
                ('1', '0') => {
                    (true, '0')
                },
                ('1', '1') => {
                    (true, '1')
                },
                _ => {
                    panic!("Wrong input");
                }
            }
        } else {
            match (a_char, b_char) {
                ('0', '0') => {
                    (false, '0')
                },
                ('0', '1') => {
                    (false, '1')
                },
                ('1', '0') => {
                    (false, '1')
                },
                ('1', '1') => {
                    (true, '0')
                }
                _ => {
                    panic!("Wrong input");
                }
            }
        }
    }
    pub fn add_binary(a: String, b: String) -> String {
        let mut a_chars: Vec<char> = a.chars().collect();
        a_chars.reverse();
        let mut b_chars: Vec<char> = b.chars().collect();
        b_chars.reverse();
        let n = usize::max(a_chars.len(), b_chars.len());
        let mut result: Vec<char> = Vec::with_capacity(n);
        let mut carry = false;
        for i in 0..n {
            let a_char = if i < a_chars.len() {Some(a_chars[i])} else {None};
            let b_char = if i < b_chars.len() {Some(b_chars[i])} else {None};
            let (new_carry, char) = match (a_char, b_char) {
                (Some(a_char), Some(b_char)) => {
                    Solution::add_tow_chars(carry, a_char, b_char)
                },
                (Some(a_char), None) => {
                    Solution::add_one_char(carry, a_char)
                },
                (None, Some(b_char)) => {
                    Solution::add_one_char(carry, b_char)
                },
                (None, None) => {
                    panic!("Wrong input");
                },
            };
            result.push(char);
            carry = new_carry;
        }
        if carry {
            result.push('1');
        }
        result.reverse();

        result.iter().collect()
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_67() {
        assert_eq!(
            Solution::add_binary("0".to_owned(), "0".to_owned()),
            "0".to_owned()
        );
        assert_eq!(
            Solution::add_binary("1010".to_owned(), "1011".to_owned()),
            "10101".to_owned()
        );
        assert_eq!(
            Solution::add_binary("11".to_owned(), "1".to_owned()),
            "100".to_owned()
        );
        assert_eq!(
            Solution::add_binary("1111".to_owned(), "1111".to_owned()),
            "11110".to_owned()
        );
    }
}

```
