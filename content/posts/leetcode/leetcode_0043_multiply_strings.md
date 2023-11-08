---
title: 43. multiply strings
date: '2021-06-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0043 multiply strings
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={43}/>
 

  Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

  Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

   

 >   Example 1:

 >   Input: num1 <TeX>=</TeX> "2", num2 <TeX>=</TeX> "3"

 >   Output: "6"

 >   Example 2:

 >   Input: num1 <TeX>=</TeX> "123", num2 <TeX>=</TeX> "456"

 >   Output: "56088"

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> num1.length, num2.length <TeX>\leq</TeX> 200

 >   	num1 and num2 consist of digits only.

 >   	Both num1 and num2 do not contain any leading zero, except the number 0 itself.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        const RADIX: u32 = 10;
        let chars1: Vec<u32> = num1.chars().map(|c| c.to_digit(RADIX).unwrap()).collect();
        let chars2: Vec<u32> = num2.chars().map(|c| c.to_digit(RADIX).unwrap()).collect();
        let mut results: Vec<u32> = vec![0; chars1.len() + chars2.len()];
        let m = results.len();
        for i in (0..chars2.len()).rev().into_iter() {
            let d = chars2[i];
            let mut chars3: Vec<u32> = vec![0; chars2.len() - 1 - i];
            let mut carry = 0u32;
            for j in (0..chars1.len()).rev().into_iter() {
                let v = d * chars1[j] + carry;
                chars3.insert(0, v % 10);
                carry = v / 10;
            }
            if carry > 0 {
                chars3.insert(0, carry);
            }
            //println!("chars3: {:?}", chars3);
            let mut carry = 0u32;
            let n = chars3.len();
            for k in (0..chars3.len()).rev().into_iter() { // n - 1, n -2, ..... 0
                let v = chars3[k] + results[m - 1 + k - (n - 1)] + carry;
                results[m - 1 + k - (n - 1)] = v % 10;
                carry = v / 10;
            }
            let mut index = 0;
            while carry > 0 {
                let v = results[m - 1 - n - index] + carry;
                results[m - 1 - n - index] = v % 10;
                carry = v / 10;
                index += 1;
            }
            //println!("{}: results: {:?}", i, results);
        }
        let mut index = 0;
        while index < results.len() && results[index] == 0 {
            index += 1;
        }
        if index == results.len() {
            return "0".to_string();
        }
        for _ in 0..index {
            results.remove(0);
        }
        let digites: [char; 10] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
        let chars: Vec<char> = results.iter().map(|&d| digites[d as usize]).collect();
        //println!("results: {:?}", results);
        //println!("index: {:?}", index);

        //String::new(chars)
        chars.iter().collect()
    }
}
*/
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        let n1 = num1.len();
        let n2 = num2.len();
        let mut chars1 = num1.chars().map(|ch| ch as u8 - '0' as u8).collect::<Vec<_>>();
        let mut chars2 = num2.chars().map(|ch| ch as u8 - '0' as u8).collect::<Vec<_>>();
        chars1.reverse();
        chars2.reverse();
        let mut res: Vec<u8> = vec![0; n1 + n2 + 1];
        for i in 0..chars1.len() {
            // chars1[i]
            let mut temp: Vec<u8> = vec![];
            for k in 0..i {
                temp.push(0u8);
            }
            let mut carry = 0u8;
            for j in 0..chars2.len() {
                let val = chars1[i] * chars2[j] + carry;
                temp.push(val % 10);
                carry = val / 10;
            }
            if carry > 0 {
                temp.push(carry);
            }
            carry = 0;
            for k in 0..res.len() {
                let val = res[k] + if k < temp.len() {temp[k]} else {0} + carry;
                res[k] = val % 10;
                carry = val / 10;
            }
        }
        res.reverse();
        //println!("res: {:?}", res);
        let index = res.iter().position(|&v| v > 0);
        if index.is_none() {
            return "0".to_string();
        }
        let index = index.unwrap();
        (index..res.len()).into_iter().map(|i| (res[i] + '0' as u8) as char ).collect::<String>()
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_43() {
        assert_eq!(Solution::multiply("0".to_string(), "".to_string()), "0".to_string());
        assert_eq!(Solution::multiply("2".to_string(), "3".to_string()), "6".to_string());
        assert_eq!(Solution::multiply("123".to_string(), "456".to_string()), "56088".to_string());
    }
}

```
