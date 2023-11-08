---
title: 12. integer to roman
date: '2021-05-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0012 integer to roman
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={12}/>
 

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

  

  Given an integer, convert it to a roman numeral.

   

 >   Example 1:

  

 >   Input: num <TeX>=</TeX> 3

 >   Output: "III"

  

 >   Example 2:

  

 >   Input: num <TeX>=</TeX> 4

 >   Output: "IV"

  

 >   Example 3:

  

 >   Input: num <TeX>=</TeX> 9

 >   Output: "IX"

  

 >   Example 4:

  

 >   Input: num <TeX>=</TeX> 58

 >   Output: "LVIII"

 >   Explanation: L <TeX>=</TeX> 50, V <TeX>=</TeX> 5, III <TeX>=</TeX> 3.

  

 >   Example 5:

  

 >   Input: num <TeX>=</TeX> 1994

 >   Output: "MCMXCIV"

 >   Explanation: M <TeX>=</TeX> 1000, CM <TeX>=</TeX> 900, XC <TeX>=</TeX> 90 and IV <TeX>=</TeX> 4.

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> num <TeX>\leq</TeX> 3999


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let thousand = num / 1000;
        let thousand_vector: Vec<String> = vec!["".to_string(), "M".to_string(), "MM".to_string(), "MMM".to_string()];
        let m_1: &String = &thousand_vector[thousand as usize];
        let num = num - thousand * 1000;

        let hundred = num / 100;
        let hundred_vector: Vec<String> = vec!["".to_string(), "C".to_string(), "CC".to_string(), "CCC".to_string(), "CD".to_string(), "D".to_string(), "DC".to_string(), "DCC".to_string(), "DCCC".to_string(), "CM".to_string()];
        let m_2: &String = &hundred_vector[hundred as usize];
        let num = num - hundred * 100;

        let ten = num / 10;
        let ten_vector: Vec<String> = vec!["".to_string(), "X".to_string(), "XX".to_string(), "XXX".to_string(), "XL".to_string(), "L".to_string(), "LX".to_string(), "LXX".to_string(), "LXXX".to_string(), "XC".to_string()];
        let m_3: &String = &ten_vector[ten as usize];
        let num = num - ten * 10;

        let one_vector: Vec<String> = vec!["".to_string(), "I".to_string(), "II".to_string(), "III".to_string(), "IV".to_string(), "V".to_string(), "VI".to_string(), "VII".to_string(), "VIII".to_string(), "IX".to_string()];
        let m_4: &String = &one_vector[num as usize];
        format!("{}{}{}{}", m_1, m_2, m_3, m_4)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_12() {
        assert_eq!(Solution::int_to_roman(3), "III");
        assert_eq!(Solution::int_to_roman(4), "IV");
        assert_eq!(Solution::int_to_roman(9), "IX");
        assert_eq!(Solution::int_to_roman(1994), "MCMXCIV");
    }
}

```
