---
title: 2165. smallest value of the rearranged number
date: '2022-09-17'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 2165 smallest value of the rearranged number
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={2165}/>

You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.



Return the rearranged number with minimal value.



Note that the sign of the number does not change after rearranging the digits.



 



 > Example 1:



 > Input: num <TeX>=</TeX> 310

 > Output: 103

 > Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 

 > The arrangement with the smallest value that does not contain any leading zeros is 103.

 > Example 2:



 > Input: num <TeX>=</TeX> -7605

 > Output: -7650

 > Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.

 > The arrangement with the smallest value that does not contain any leading zeros is -7650.

 



**Constraints:**



 > -1015 <TeX>\leq</TeX> num <TeX>\leq</TeX> 1015


## Solution
### Rust
```rust
pub struct Solution {}

use std::iter::FromIterator;

impl Solution {

pub fn find_smallest_num(chars: &Vec<char>, can_be_zero: bool) -> u64 {
    let n = chars.len();
    if chars.len() == 1 {
        return chars[0].to_digit(10u32).unwrap() as u64;
    }
    // let pow = 10i32.pow(chars.len() as u32 - 1) as u64;
    if can_be_zero {
        let mut v = chars[0].to_digit(10u32).unwrap() as u64;
        for i in 0..n-1 {
            v = v * 10;
        }
        let part = Vec::from_iter(chars[1..].iter().cloned());
        return v + Self::find_smallest_num(&part, true);
    }
    let mut cur_ch = chars[0];
    let mut i = 0;
    while i < chars.len() && chars[i] == '0' {
        i = i + 1;
    }
    //println!("chars: {:?}", chars);
    //println!("i: {:?}", i);

    let mut v = chars[i].to_digit(10u32).unwrap() as u64;
    //println!("v: {:?}", v);

    let iter1 = chars[0..i].iter();
    let iter2 = chars[i+1..].iter();
    let iter3 = iter1.chain(iter2);
    let part = Vec::from_iter(iter3.cloned());
    //println!("part: {:?}", part);
        for i in 0..n-1 {
            v = v * 10;
        }
    return v + Self::find_smallest_num(&part, true);    
}
pub fn find_largest_num(chars: &Vec<char>) -> u64 {
    if chars.len() == 1 {
        return chars[0].to_digit(10u32).unwrap() as u64;
    }
    //let pow = 10i32.pow(chars.len() as u32 - 1) as u64;
    let n = chars.len();
    let mut v = chars[n - 1].to_digit(10u32).unwrap() as u64;
    let part = Vec::from_iter(chars[..n - 1].iter().cloned());
    for i in 0..n-1 {
        v = v * 10;
    }
    //println!("v: {}, pow: {}", v, pow);
    return v + Self::find_largest_num(&part);
}

pub fn smallest_number(num: i64) -> i64 {
        if num >=0 {
            let mut chars: Vec<char> = format!("{}", num).chars().collect();
            chars.sort();
            Self::find_smallest_num(&chars, false) as i64
        } else {
            let mut chars: Vec<char> = format!("{}", -num).chars().collect();
            chars.sort();
            -(Self::find_largest_num(&chars) as i64)
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2165() {
        assert_eq!(Solution::smallest_number(310), 103);        
        assert_eq!(Solution::smallest_number(-7605), -7650);        
    }
}


```
