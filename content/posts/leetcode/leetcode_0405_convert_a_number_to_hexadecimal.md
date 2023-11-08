---
title: 405. convert a number to hexadecimal
date: '2022-02-27'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0405 convert a number to hexadecimal
---

 

  Given an integer num, return a string representing its hexadecimal representation. For negative integers, [two&rsquo;s complement](https://en.wikipedia.org/wiki/Two%27s_complement) method is used.

  All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

  Note: You are not allowed to use any built-in library method to directly solve this problem.

   

 >   Example 1:

 >   Input: num <TeX>=</TeX> 26

 >   Output: "1a"

 >   Example 2:

 >   Input: num <TeX>=</TeX> -1

 >   Output: "ffffffff"

   

  **Constraints:**

  

 >   	-2^31 <TeX>\leq</TeX> num <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn to_hex(num: i32) -> String {
        if num == 0 {
            return "0".to_string();
        }
        let chars: Vec<char> = vec!['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'];
        let mut result: Vec<char> = vec![];
        if num > 0 {
            let mut num = num as usize;
            while num > 0 {
                let index = num % chars.len();
                result.insert(0, chars[index]);
                num = num / chars.len();
            }
            return result.iter().collect::<String>();
        }
        //println!("aa: {:x}", i32::MIN);
        if num == i32::MIN {
            return "80000000".to_string();
        }
        let s = Self::to_hex(-num);
        let mut s_chars: Vec<char> = s.chars().collect();
        while s_chars.len() < 8 {
            s_chars.insert(0, '0');
        }
        //println!("{:?}", s_chars);
        let mut carry = 1usize;
        for i in (0..s_chars.len()).rev() {
            let index = chars.iter().position(|&ch| ch == s_chars[i]).unwrap();
            let mut new_index = chars.len() - 1 - index;
            new_index = new_index + carry;
            if new_index >= chars.len() {
                new_index = new_index % chars.len();
                carry = 1;
            } else {
                carry = 0;
            }
            s_chars[i] = chars[new_index];
        }
        return s_chars.iter().collect::<String>();
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_405() {
        assert_eq!(Solution::to_hex(26), "1a".to_owned());
        assert_eq!(Solution::to_hex(-1), "ffffffff".to_owned());
    }
}

```
