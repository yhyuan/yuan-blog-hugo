---
title: 91. decode ways
date: '2021-07-31'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0091 decode ways
---

 

  A message containing letters from A-Z can be encoded into numbers using the following mapping:

  

  'A' -> "1"

  'B' -> "2"

  ...

  'Z' -> "26"

  

  To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

  

  	"AAJF" with the grouping (1 1 10 6)

  	"KJF" with the grouping (11 10 6)

  

  Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

  Given a string s containing only digits, return the number of ways to decode it.

  The answer is guaranteed to fit in a 32-bit integer.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "12"

 >   Output: 2

 >   Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "226"

 >   Output: 3

 >   Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "0"

 >   Output: 0

 >   Explanation: There is no character that is mapped to a number starting with 0.

 >   The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.

 >   Hence, there are no valid ways to decode this since all digits need to be mapped.

  

 >   Example 4:

  

 >   Input: s <TeX>=</TeX> "06"

 >   Output: 0

 >   Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 100

 >   	s contains only digits and may contain leading zero(s).


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        if chars.len() == 0 {
            return 0;
        }
        let n = chars.len();
        let mut table: Vec<i32> = vec![i32::MIN; n];
        let v = (&s[n-1..]).to_string().parse::<i32>().unwrap();
        table[n - 1] = if v == 0 {0} else {1};
        if n == 1 {
            return table[n - 1];
        }
        let v = (&s[n-2..]).to_string().parse::<i32>().unwrap();
        table[n - 2] = match v {
            0..=9   => {0},
            10 | 20 => {1},
            11..=19 => {2},
            21..=26 => {2},
            30 | 40 | 50 | 60 | 70 | 80 | 90 => {0},
            _ => {1}
        };
        if n == 2 {
            return table[n - 2];
        }
        for i in (0..n-2).rev() {
            let v = (&s[i..i + 2]).to_string().parse::<i32>().unwrap();
            table[i] = match v {
                0..=9   => {0},
                10 | 20 => {table[i + 2]},
                11..=19 => {table[i + 1] + table[i + 2]},
                21..=26 => {table[i + 1] + table[i + 2]},
                30 | 40 | 50 | 60 | 70 | 80 | 90 => {0},
                _ => {table[i + 1]}
            };
        }
        table[0]
    }
}
*/
impl Solution {
    pub fn parseInteger(s: &str) -> i32 {
        s.parse::<i32>().unwrap()
    }
    pub fn num_decodings(s: String) -> i32 {
        let n = s.len();
        let chars = s.chars().collect::<Vec<_>>();
        //let mut dp = vec![0; n];
        if chars[0] == '0' {
            return 0;
        }
        if n == 1 {
            return 1;
        }
        let mut dp = (
            1, if chars[1] == '0' {
                0
            } else {
                1
            } + if Self::parseInteger(&s[0..=1]) <= 26 {
                1
            } else {
                0
            }
        );
        for i in 2..n {
            let v = Self::parseInteger(&s[i-1..=i]);
            dp = (
                dp.1, 
                if chars[i] == '0' {
                    0
                } else {
                    dp.1    
                } + if v <= 26 && v >= 10 {
                    dp.0
                } else {
                    0
                }
            );
        }
        dp.1
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_91() {
        assert_eq!(Solution::num_decodings("12".to_string()), 2);
        assert_eq!(Solution::num_decodings("226".to_string()), 3);
        assert_eq!(Solution::num_decodings("0".to_string()), 0);
        assert_eq!(Solution::num_decodings("2101".to_string()), 1);  
        assert_eq!(Solution::num_decodings("10".to_string()), 1);  
        assert_eq!(Solution::num_decodings("123123".to_string()), 9);  
        assert_eq!(Solution::num_decodings("230".to_string()), 0);
        assert_eq!(Solution::num_decodings("12120".to_string()), 3);  
    }
}

```
