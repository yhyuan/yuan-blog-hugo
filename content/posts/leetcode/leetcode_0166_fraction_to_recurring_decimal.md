---
title: 166. fraction to recurring decimal
date: '2021-10-01'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0166 fraction to recurring decimal
---

 

  Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

  If the fractional part is repeating, enclose the repeating part in parentheses.

  If multiple answers are possible, return any of them.

  It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.

   

 >   Example 1:

 >   Input: numerator <TeX>=</TeX> 1, denominator <TeX>=</TeX> 2

 >   Output: "0.5"

 >   Example 2:

 >   Input: numerator <TeX>=</TeX> 2, denominator <TeX>=</TeX> 1

 >   Output: "2"

 >   Example 3:

 >   Input: numerator <TeX>=</TeX> 2, denominator <TeX>=</TeX> 3

 >   Output: "0.(6)"

 >   Example 4:

 >   Input: numerator <TeX>=</TeX> 4, denominator <TeX>=</TeX> 333

 >   Output: "0.(012)"

 >   Example 5:

 >   Input: numerator <TeX>=</TeX> 1, denominator <TeX>=</TeX> 5

 >   Output: "0.2"

   

  **Constraints:**

  

 >   	-2^31 <TeX>\leq</TeX> numerator, denominator <TeX>\leq</TeX> 2^31 - 1

 >   	denominator !<TeX>=</TeX> 0


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    // Calculate numberator * 10^n / denominator
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
        let digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
        if denominator == 0 {
            panic!("Wrong input!");
        }
        let is_positive = (numerator >= 0 && denominator > 0) || (numerator <= 0 && denominator < 0);
        let numerator = numerator as i128;
        let denominator = denominator as i128;
        if numerator % denominator == 0 {
            return format!("{}", numerator / denominator);
        }
        let numerator = numerator.abs();
        let denominator = denominator.abs();
        let integer = numerator / denominator;
        let numerator = numerator % denominator;
        let mut remainer = numerator;
        let mut hashmap: HashMap<i128, i128> = HashMap::new();
        let mut divides: Vec<i128> = vec![];
        let mut i: usize = 0;
        //println!("numerator: {:?}, denominator: {}", numerator, denominator);
        loop {
            i = i + 1;
            let val = remainer * 10;
            remainer = val % denominator;
            divides.push(val / denominator);
            //println!("divides: {:?}", divides);
            if remainer == 0 {
                let decimal = divides.iter().map(|&x| digits[x as usize]).collect::<Vec<char>>().into_iter().collect::<String>();
                return format!("{}{}.{}", if is_positive {""} else {"-"},  integer, decimal);    
            } else {
                if hashmap.contains_key(&val) {
                    let count = hashmap[&val];
                    if count == 1 {
                        hashmap.insert(val, 2);
                    } else {
                        divides.pop(); // undo the previous push. 
                        let size = hashmap.values().filter(|&&v| v == 2).count(); // Calculate repeated patter size. 
                        //Remove one pattern. 
                        for _ in 0..size {
                            divides.pop();
                        }
                        let mut divides = divides.iter().map(|&x| digits[x as usize]).collect::<Vec<char>>();
                        //Insert ( infront of pattern
                        divides.insert(divides.len() - size, '(');
                        //Insert ) after pattern
                        divides.push(')');
                        let decimal = divides.into_iter().collect::<String>();
                        return format!("{}{}.{}", if is_positive {""} else {"-"}, integer, decimal);    
                    }
                } else {
                    hashmap.insert(val, 1);
                }    
            }
        }
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_166() {
        
        assert_eq!(Solution::fraction_to_decimal(1, 16), "0.0625".to_string());
        assert_eq!(Solution::fraction_to_decimal(1, 7), "0.(142857)".to_string());
        assert_eq!(Solution::fraction_to_decimal(1, 2), "0.5".to_string());
        assert_eq!(Solution::fraction_to_decimal(2, 1), "2".to_string());
        assert_eq!(Solution::fraction_to_decimal(4, 2), "2".to_string());
        assert_eq!(Solution::fraction_to_decimal(1, 4), "0.25".to_string());
        assert_eq!(Solution::fraction_to_decimal(5, 4), "1.25".to_string());
        assert_eq!(Solution::fraction_to_decimal(6, 4), "1.5".to_string());
        assert_eq!(Solution::fraction_to_decimal(1, 5), "0.2".to_string());
        assert_eq!(Solution::fraction_to_decimal(2, 3), "0.(6)".to_string());
        assert_eq!(Solution::fraction_to_decimal(4, 333), "0.(012)".to_string());
        assert_eq!(Solution::fraction_to_decimal(1, 6), "0.1(6)".to_string());        
        assert_eq!(Solution::fraction_to_decimal(-50, 8), "-6.25".to_string()); 
               
        assert_eq!(Solution::fraction_to_decimal(-1, -2147483648), "0.0000000004656612873077392578125".to_string());
    }
}


```
