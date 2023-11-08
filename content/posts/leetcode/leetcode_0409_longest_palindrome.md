---
title: 409. longest palindrome
date: '2022-02-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0409 longest palindrome
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={409}/>
 

  Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

  Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "abccccdd"

 >   Output: 7

 >   Explanation:

 >   One longest palindrome that can be built is "dccaccd", whose length is 7.

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "a"

 >   Output: 1

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "bb"

 >   Output: 2

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 2000

 >   	s consists of lowercase and/or uppercase English letters only.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashMap;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut hashmap: HashMap<char, usize> = HashMap::new();
        for ch in s.chars() {
            if hashmap.contains_key(&ch) {
                hashmap.insert(ch, hashmap[&ch] + 1);
            } else {
                hashmap.insert(ch, 1);
            }
        }
        let mut result = 0i32;
        let mut odd = 0i32;
        for (&k, &v) in hashmap.iter() {
            let v = v as i32;
            if v % 2 == 0 {
                result += v;
            } else {
                result += v - 1;
                odd += 1;
            }
        }
        if odd > 0 {
            result += 1;
        }
        result
    }
}
*/
use std::collections::HashMap;
impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut hashmap: HashMap<char, usize> = HashMap::new();
        let chars: Vec<char> = s.chars().collect::<Vec<_>>();
        for i in 0..chars.len() {
            if hashmap.contains_key(&chars[i]) {
                *hashmap.get_mut(&chars[i]).unwrap() += 1;
            } else {
                hashmap.insert(chars[i], 1);
            }
        }
        //println!("hashmap: {:?}", hashmap);
        let mut res = 0;
        let mut find_odd = false;
        for (&key, &val) in hashmap.iter() {
            if val % 2 == 0 {
                res += val;
            } else {
                res += val - 1;
                find_odd = true;
            }
        }
        if find_odd {res as i32 + 1} else {res as i32}
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_409() {
        assert_eq!(Solution::longest_palindrome("abccccdd".to_string()), 7);
    }
}

```
