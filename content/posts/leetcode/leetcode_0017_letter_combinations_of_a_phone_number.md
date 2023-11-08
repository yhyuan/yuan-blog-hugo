---
title: 17. letter combinations of a phone number
date: '2021-05-18'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0017 letter combinations of a phone number
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={17}/>
 

  Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

  A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

   

 >   Example 1:

  

 >   Input: digits <TeX>=</TeX> "23"

 >   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

  

 >   Example 2:

  

 >   Input: digits <TeX>=</TeX> ""

 >   Output: []

  

 >   Example 3:

  

 >   Input: digits <TeX>=</TeX> "2"

 >   Output: ["a","b","c"]

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> digits.length <TeX>\leq</TeX> 4

 >   	digits[i] is a digit in the range ['2', '9'].


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/* 
use std::collections::HashMap;
impl Solution {
    fn helper(digits: String, dict: &HashMap<char, Vec<char>>) -> Vec<String> {
        if digits.len() == 0 {
            return vec![];
        }
        let char = digits.chars().next().unwrap();
        let new_digits = digits.chars().skip(1).collect();
        let letters = dict.get(&char).unwrap();
        let strings = Solution::helper(new_digits, dict);
        if strings.len() == 0 {
            return letters.iter().map(|&ch| ch.to_string()).collect();
        }
        let size = letters.len() * strings.len();
        let vectors: Vec<Vec<String>> = letters.iter().map(|&ch| strings.iter().map(|str| ch.to_string() + str).collect()).collect();
        vectors.into_iter().fold(Vec::with_capacity(size), |mut acc, v| {
            acc.extend(v); acc
        })
    }

    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.len() == 0 {
            return vec![];
        }
        let mut dict: HashMap<char, Vec<char>> = HashMap::new();
        dict.insert('2', vec!['a', 'b', 'c']);
        dict.insert('2', vec!['a', 'b', 'c']);
        dict.insert('3', vec!['d', 'e', 'f']);
        dict.insert('4', vec!['g', 'h', 'i']);
        dict.insert('5', vec!['j', 'k', 'l']);
        dict.insert('6', vec!['m', 'n', 'o']);
        dict.insert('7', vec!['p', 'q', 'r', 's']);
        dict.insert('8', vec!['t', 'u', 'v']);
        dict.insert('9', vec!['w', 'x', 'y', 'z']);
        Solution::helper(digits, &dict)
    }
}
*/
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        let n = digits.len();
        if n == 0 {
            return vec![];
        }
        let digit = digits.chars().nth(0).unwrap() as usize - '0' as usize;
        let lookup = vec![vec![], vec![], vec!['a', 'b', 'c'], vec!['d', 'e', 'f'], vec!['g', 'h', 'i'], vec!['j', 'k', 'l'], 
        vec!['m', 'n', 'o'], vec!['p', 'q', 'r', 's'], vec!['t', 'u', 'v'], vec!['w', 'x', 'y', 'z']];
        if n == 1 {
            let res = lookup[digit].iter().map(|ch| format!("{}", ch)).collect::<Vec<_>>();
            return res;
        }
        let chars = &lookup[digit];
        let pre_results = Self::letter_combinations(format!("{}", &digits[1..]));
        let mut res: Vec<String> = vec![];
        for ch in lookup[digit].iter() {
            for str in pre_results.iter() {
                res.push(format!("{}{}", ch, str));
            }
        }
        res
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_17() {
        assert_eq!(
            Solution::letter_combinations("23".to_string()),
            vec!["ad".to_string(), "ae".to_string(), "af".to_string(), "bd".to_string(), "be".to_string(), "bf".to_string(), "cd".to_string(), "ce".to_string(), "cf".to_string()]
        );
    }
}

```
