---
title: 13. roman to integer
date: '2021-05-14'
tags: ['leetcode', 'rust', 'python', 'easy']
draft: false
description: Solution for leetcode 0013 roman to integer
---

 

  Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

  

  Symbol       Value

  I             1

  V             5

  X             10

  L             50

  C             100

  D             500

  M             1000

  For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

  Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

  

  	I can be placed before V (5) and X (10) to make 4 and 9. 

  	X can be placed before L (50) and C (100) to make 40 and 90. 

  	C can be placed before D (500) and M (1000) to make 400 and 900.

  

  Given a roman numeral, convert it to an integer.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "III"

 >   Output: 3

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "IV"

 >   Output: 4

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "IX"

 >   Output: 9

  

 >   Example 4:

  

 >   Input: s <TeX>=</TeX> "LVIII"

 >   Output: 58

 >   Explanation: L <TeX>=</TeX> 50, V<TeX>=</TeX> 5, III <TeX>=</TeX> 3.

  

 >   Example 5:

  

 >   Input: s <TeX>=</TeX> "MCMXCIV"

 >   Output: 1994

 >   Explanation: M <TeX>=</TeX> 1000, CM <TeX>=</TeX> 900, XC <TeX>=</TeX> 90 and IV <TeX>=</TeX> 4.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 15

 >   	s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').

 >   	It is guaranteed that s is a valid roman numeral in the range [1, 3999].


## Solution
The key is to generate a lookup dictionary which stores the letter or two letters combination and their associated values. Then, we can parse the string step by step to see whether we can find two letters combination. If we can find it, we will use the values of two letters. Otherwise, we will use one letter's value. 
### python
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        lookupDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        n = len(s)
        i = 0
        total = 0
        while i < n:
            if s[i] == "I":
                if i < n - 1 and s[i + 1] == "V":
                    total += 4
                    i = i + 2
                elif i < n - 1 and s[i + 1] == "X":
                    total += 9
                    i = i + 2
                else:
                    total += 1
                    i = i + 1
            elif s[i] == "X":
                if i < n - 1 and s[i + 1] == "L":
                    total += 40
                    i = i + 2
                elif i < n - 1 and s[i + 1] == "C":
                    total += 90
                    i = i + 2
                else:
                    total += 10
                    i = i + 1
            elif s[i] == "C":
                if i < n - 1 and s[i + 1] == "D":
                    total += 400
                    i = i + 2
                elif i < n - 1 and s[i + 1] == "M":
                    total += 900
                    i = i + 2
                else:
                    total += 100
                    i = i + 1
            else:
                total += lookupDict[s[i]]
                i += 1
        return total
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut chars: Vec<char> = s.chars().collect();
        let mut result = 0i32;
        for i in 0..chars.len() {
            let val = match chars[i] {
                'M' => 1000,
                'D' => 500,
                'C' => 100,
                'L' => 50,
                'X' => 10,
                'V' => 5,
                'I' => 1,
                 _ => {
                     panic!("Wrong");
                 }
            };
            result += val;
        }
        //CD, CM. XC, XL, IX, IV
        if s.contains("CD") || s.contains("CM"){
            result -= 200;
        } 
        if s.contains("XC") || s.contains("XL"){
            result -= 20;
        } 
        if s.contains("IX") || s.contains("IV"){
            result -= 2;
        } 
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_13() {
        assert_eq!(Solution::roman_to_int("III".to_string()), 3);
        assert_eq!(Solution::roman_to_int("IV".to_string()), 4);
        assert_eq!(Solution::roman_to_int("IX".to_string()), 9);
        assert_eq!(Solution::roman_to_int("MCMXCIV".to_string()), 1994);
        assert_eq!(Solution::roman_to_int("DCXXI".to_string()), 621);
    }
}

```
