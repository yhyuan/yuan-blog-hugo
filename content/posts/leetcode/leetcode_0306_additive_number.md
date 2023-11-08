---
title: 306. additive number
date: '2021-12-31'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0306 additive number
---

 

  Additive number is a string whose digits can form additive sequence.

  A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

  Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

  Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

   

 >   Example 1:

  

 >   Input: "112358"

 >   Output: true

 >   Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 

 >                1 + 1 <TeX>=</TeX> 2, 1 + 2 <TeX>=</TeX> 3, 2 + 3 <TeX>=</TeX> 5, 3 + 5 <TeX>=</TeX> 8

  

 >   Example 2:

  

 >   Input: "199100199"

 >   Output: true

 >   Explanation: The additive sequence is: 1, 99, 100, 199. 

 >                1 + 99 <TeX>=</TeX> 100, 99 + 100 <TeX>=</TeX> 199

  

   

  **Constraints:**

  

 >   	num consists only of digits '0'-'9'.

 >   	1 <TeX>\leq</TeX> num.length <TeX>\leq</TeX> 35

  

 >   Follow up:<br />

 >   How would you handle overflow for very large input integers?


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {

    pub fn helper(num: String, hashmap: &mut HashMap<String, Vec<Vec<u128>>>) -> Vec<Vec<u128>> {
        if hashmap.contains_key(&num) {
            return hashmap[&num].clone();
        }
        let n = num.len();
        if n <= 2 {
            hashmap.insert(num, vec![]);
            return vec![];
        }
        if n == 3 {
            let v1 = format!("{}", &num[0..1]).parse::<u128>().unwrap();
            let v2 = format!("{}", &num[1..2]).parse::<u128>().unwrap();
            let v3 = format!("{}", &num[2..3]).parse::<u128>().unwrap();
            if v1 + v2 == v3 {
                hashmap.insert(num, vec![vec![v1, v2, v3]]);
                return vec![vec![v1, v2, v3]];
            } else {
                hashmap.insert(num, vec![]);
                return vec![];
            }
        }
        let mut chars: Vec<char> = num.chars().collect();
        let mut results: Vec<Vec<u128>> = vec![];
        for i in 1..n {
            if i > 1 && chars[0] == '0' {
                continue;
            }
            for j in i + 1..n {
                if j > i + 1 && chars[i] == '0' {
                    continue;
                }
                if n > j + 1 && chars[j] == '0' {
                    continue;
                }
                let v1 = format!("{}", &num[0..i]).parse::<u128>().unwrap();
                let v2 = format!("{}", &num[i..j]).parse::<u128>().unwrap();
                let v3 = format!("{}", &num[j..n]).parse::<u128>().unwrap();
                if v1 + v2 == v3 {
                    results.push(vec![v1, v2, v3]);
                }       
            }
        }
        for i in 1..n - 1 {
            if i > 1 && chars[n - i] == '0' {
                continue;
            }
            let val = format!("{}", &num[n - i..n]).parse::<u128>().unwrap();
            let mut sub_results = Self::helper(format!("{}", &num[0..n - i]), hashmap);
            for sub_result in sub_results.iter_mut() {
                let m = sub_result.len();
                if sub_result[m - 1] + sub_result[m - 2] == val {
                    sub_result.push(val);
                    results.push(sub_result.clone());
                }
            }    
        }
        hashmap.insert(num, results.clone());
        results
    }
    pub fn is_additive_number(num: String) -> bool {
        let mut hashmap: HashMap<String, Vec<Vec<u128>>> = HashMap::new();
        Self::helper(num, &mut hashmap).len() > 0
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_306() {
        /*
        assert_eq!(Solution::is_additive_number("112358".to_string()), true);
        assert_eq!(Solution::is_additive_number("199100199".to_string()), true);
        assert_eq!(Solution::is_additive_number("1023".to_string()), false);
        assert_eq!(Solution::is_additive_number("0235813".to_string()), false);
        assert_eq!(Solution::is_additive_number("000".to_string()), true);
        */
        assert_eq!(Solution::is_additive_number("11111111111011111111111".to_string()), true);
    }
}

```
