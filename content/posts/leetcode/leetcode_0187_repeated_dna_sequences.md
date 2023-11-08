---
title: 187. repeated dna sequences
date: '2021-10-10'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0187 repeated dna sequences
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={187}/>
 

  The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

  

  	For example, "ACGAATTCCG" is a DNA sequence.

  

  When studying DNA, it is useful to identify repeated sequences within the DNA.

  Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

   

 >   Example 1:

 >   Input: s <TeX>=</TeX> "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

 >   Output: ["AAAAACCCCC","CCCCCAAAAA"]

 >   Example 2:

 >   Input: s <TeX>=</TeX> "AAAAAAAAAAAAA"

 >   Output: ["AAAAAAAAAA"]

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 10^5

 >   	s[i] is either 'A', 'C', 'G', or 'T'.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashMap;
impl Solution {
    pub fn create_lookup_dict(s: String) -> HashMap<u32, u32> {
        let mut lookup_dict:HashMap<u32, u32> = HashMap::new();
        let mut seq_code = 0u32;
        for (i, ch) in s.chars().enumerate() {
            seq_code <<= 2;
            match ch {
                'A' => seq_code |= 0_u32,
                'C' => seq_code |= 1_u32,
                'G' => seq_code |= 2_u32,
                'T' => seq_code |= 3_u32,
                _ => unreachable!()
            }
            if i < 9 {
                continue;
            }
            seq_code &= 0b0000_0000_0000_1111_1111_1111_1111_1111;
            if lookup_dict.contains_key(&seq_code) {
                lookup_dict.insert(seq_code, 2);
            } else {
                lookup_dict.insert(seq_code, 1);
            }
        }
        lookup_dict
    }

    pub fn convert_code_to_string(seq_code: &u32) -> String {
        let mut code = *seq_code;
        let mut substr = String::new();
        for _ in 0..10 {
            let ch = match code & 0b0000_0000_0000_1100_0000_0000_0000_0000 {
                0b0000_0000_0000_0000_0000_0000_0000_0000 => 'A',
                0b0000_0000_0000_0100_0000_0000_0000_0000 => 'C',
                0b0000_0000_0000_1000_0000_0000_0000_0000 => 'G',
                0b0000_0000_0000_1100_0000_0000_0000_0000 => 'T',
                _ => unreachable!()
            };
            substr.push(ch);
            code <<= 2;
        }
        substr
    }

    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        let lookup_dict = Solution::create_lookup_dict(s);
        let result: Vec<String> = lookup_dict.keys()
            .filter(|code| lookup_dict.get(code).unwrap() > &1u32)
            .map(Solution::convert_code_to_string)
            .collect();
        result
    }
}
*/
use std::collections::HashSet;
impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        let mut hashmap: HashSet<String> = HashSet::new();
        let n = s.len();
        if n < 10 {
            return vec![];
        }
        let mut res: HashSet<String> = HashSet::new();
        //println!("n: {}", n);
        for i in 0..=n - 10 {
            //println!("i: {}", i);
            let str = format!("{}", &s[i..i + 10]);
            if hashmap.contains(&str) {
                res.insert(str);
            } else {
                hashmap.insert(str);
            }
        }
        res.into_iter().collect::<Vec<String>>()
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_187() {
        assert_eq!(vec!["AAAAAAAAAA".to_string()], Solution::find_repeated_dna_sequences("AAAAAAAAAAA".to_string()));
        assert_eq!(vec!["AAAAACCCCC".to_string(),"CCCCCAAAAA".to_string()], Solution::find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT".to_string()));
        assert_eq!(vec!["AAAAAAAAAA".to_string()], Solution::find_repeated_dna_sequences("AAAAAAAAAAAAA".to_string()));
    }
}

```
