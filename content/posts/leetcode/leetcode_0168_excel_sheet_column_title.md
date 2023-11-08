---
title: 168. excel sheet column title
date: '2021-10-03'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0168 excel sheet column title
---

 

  Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

  For example:

  

  A -> 1

  B -> 2

  C -> 3

  ...

  Z -> 26

  AA -> 27

  AB -> 28 

  ...

  

   

 >   Example 1:

  

 >   Input: columnNumber <TeX>=</TeX> 1

 >   Output: "A"

  

 >   Example 2:

  

 >   Input: columnNumber <TeX>=</TeX> 28

 >   Output: "AB"

  

 >   Example 3:

  

 >   Input: columnNumber <TeX>=</TeX> 701

 >   Output: "ZY"

  

 >   Example 4:

  

 >   Input: columnNumber <TeX>=</TeX> 2147483647

 >   Output: "FXSHRXW"

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> columnNumber <TeX>\leq</TeX> 2^31 - 1


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn convert_to_title(column_number: i32) -> String {
        let letters: Vec<char> = ('A'..='Z').into_iter().collect();
        //println!("{:?}", letters);
        let mut results: Vec<char> = vec![];
        let mut column_number = column_number as usize;
        while column_number > 0 {
            if column_number % 26 == 0 {
                results.push('Z');
                column_number = (column_number - 26) / 26;
            } else {
                let letter = letters[column_number % 26 - 1];
                results.push(letter);
                column_number = column_number / 26;    
            }
        }
        results.reverse();
        results.into_iter().collect()
        //String::new()
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_168() {
        assert_eq!(Solution::convert_to_title(28), "AB".to_string());
        assert_eq!(Solution::convert_to_title(2147483647), "FXSHRXW".to_string());
        assert_eq!(Solution::convert_to_title(701), "ZY".to_string());
    }
}

```
