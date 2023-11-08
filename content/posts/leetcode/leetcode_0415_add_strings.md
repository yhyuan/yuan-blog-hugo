---
title: 415. add strings
date: '2022-03-04'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0415 add strings
---

 

  Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

  You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

   

 >   Example 1:

  

 >   Input: num1 <TeX>=</TeX> "11", num2 <TeX>=</TeX> "123"

 >   Output: "134"

  

 >   Example 2:

  

 >   Input: num1 <TeX>=</TeX> "456", num2 <TeX>=</TeX> "77"

 >   Output: "533"

  

 >   Example 3:

  

 >   Input: num1 <TeX>=</TeX> "0", num2 <TeX>=</TeX> "0"

 >   Output: "0"

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> num1.length, num2.length <TeX>\leq</TeX> 10^4

 >   	num1 and num2 consist of only digits.

 >   	num1 and num2 don't have any leading zeros except for the zero itself.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn add_strings(num1: String, num2: String) -> String {
        let chars1: Vec<char> = num1.chars().collect();
        let chars2: Vec<char> = num2.chars().collect();
        let mut result: Vec<char> = vec![];
        let n1 = num1.len();
        let n2 = num2.len();
        let max_n = usize::max(n1, n2);
        let mut carry = 0u8;
        for i in 0..max_n {
            let d1 = if n1 >= i + 1 {chars1[n1 - 1 - i] as u8 - '0' as u8} else {0};
            let d2 = if n2 >= i + 1 {chars2[n2 - 1 - i] as u8 - '0' as u8} else {0};
            let mut v = d1 + d2 + carry;
            if v >= 10 {
                carry = 1;
                v = v % 10;
            } else {
                carry = 0;
            }
            println!("v: {}", v);
            result.insert(0, (v + '0' as u8) as char);
        }
        if carry > 0 {
            result.insert(0, '1');
        }
        println!("result: {:?}", result);
        let s = result.iter().collect::<String>();
        s
    }
}
*/
impl Solution {
    pub fn add_strings(num1: String, num2: String) -> String {
        let mut chars_1 = num1.chars().collect::<Vec<_>>();
        chars_1.reverse();
        let mut chars_2 = num2.chars().collect::<Vec<_>>();
        chars_2.reverse();
        let max_len = usize::max(num1.len(), num2.len());
        let mut chars: Vec<char> = vec![];
        let mut carry = false;
        for i in 0..max_len {
            let mut total = if i < num1.len() && i < num2.len() {
                (chars_1[i] as u8 - '0' as u8) + (chars_2[i] as u8  - '0' as u8)
            } else if i < num1.len() && i >= num2.len() {
                (chars_1[i] as u8  - '0' as u8)
            } else /*if i < num2.len() && i >= num1.len()*/ {
                (chars_2[i]  as u8 - '0' as u8)
            };
            total += if carry {1} else {0};
            if total >= 10 {
                total -= 10;
                carry = true;
            } else {
                carry = false;
            }
            chars.push((total + '0' as u8) as char);            
        }
        if carry {
            chars.push('1');
        }
        chars.reverse();
        let s = chars.iter().collect::<String>();
        s
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_415() {
        //assert_eq!(Solution::add_strings("456".to_owned(), "77".to_owned()), "533".to_owned());
        assert_eq!(Solution::add_strings("1".to_owned(), "9".to_owned()), "10".to_owned());
    }
}

```
