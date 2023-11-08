---
title: 9999. knuth morris pratt kmp substring search
date: '2022-09-30'
tags: ['leetcode', 'rust']
draft: true
description: Solution for leetcode 9999 knuth morris pratt kmp substring search
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={9999}/>

## Solution
### Rust
```rust
pub struct Solution {}

// submission codes start here

impl Solution {
    pub fn calculate_partial_match_table(sub_chars: &Vec<char>) -> Vec<usize> {
        vec![0, 0, 0, 0, 1, 2, 0]
    }
    pub fn knuth_morris_pratt_kmp_substring_search(s: String, sub_s: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        let sub_chars: Vec<char> = sub_s.chars().collect();
        let table = Solution::calculate_partial_match_table(&sub_chars);
        let mut i = 0usize;
        let mut j = 0usize;
        while i < chars.len() {
            if chars[i] != sub_chars[j] {
                if j > 0 {
                    j -= j - table[j];
                    
                } else {
                    i += 1;
                }
            } else {
                i += 1;
                j += 1;
            }
        }
        false
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_9999() {
        assert_eq!(Solution::knuth_morris_pratt_kmp_substring_search("BBC ABCDAB ABCDABCDABDE".to_string(), "ABCDABD".to_string()), true);
    }
}

```
