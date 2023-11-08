---
title: 44. wildcard matching
date: '2021-06-14'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0044 wildcard matching
---

 

  Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '' where:

  

  	'?' Matches any single character.

  	'' Matches any sequence of characters (including the empty sequence).

  

  The matching should cover the entire input string (not partial).

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "aa", p <TeX>=</TeX> "a"

 >   Output: false

 >   Explanation: "a" does not match the entire string "aa".

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "aa", p <TeX>=</TeX> ""

 >   Output: true

 >   Explanation: '' matches any sequence.

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "cb", p <TeX>=</TeX> "?a"

 >   Output: false

 >   Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

  

 >   Example 4:

  

 >   Input: s <TeX>=</TeX> "adceb", p <TeX>=</TeX> "ab"

 >   Output: true

 >   Explanation: The first '' matches the empty sequence, while the second '' matches the substring "dce".

  

 >   Example 5:

  

 >   Input: s <TeX>=</TeX> "acdcb", p <TeX>=</TeX> "ac?b"

 >   Output: false

  

   

  **Constraints:**

  

 >   	0 <TeX>\leq</TeX> s.length, p.length <TeX>\leq</TeX> 2000

 >   	s contains only lowercase English letters.

 >   	p contains only lowercase English letters, '?' or ''.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
    pub fn is_match_helper(s_chars: &Vec<char>, s_index: usize, p_chars: &Vec<char>, p_index: usize, hashmap: &mut HashMap<(usize, usize), bool>) -> bool {
        if hashmap.contains_key(&(s_index, p_index)) {
            return hashmap[&(s_index, p_index)];
        }
        if s_chars.len() == s_index && p_chars.len() == p_index {
            hashmap.insert((s_index, p_index), true);
            return true;
        }
        if s_chars.len() == s_index && p_chars.len() != p_index {
            let mut is_all_star = true;
            for i in p_index..p_chars.len() {
                if p_chars[i] != '*' {
                    is_all_star = false;
                    hashmap.insert((s_index, i), false);
                    break;
                } else {
                    hashmap.insert((s_index, i), true);
                }
            }
            if is_all_star {
                hashmap.insert((s_index, p_index), true);
                return true;    
            } else {
                hashmap.insert((s_index, p_index), false);
                return false;    
            }
        }
        if s_chars.len() != s_index && p_chars.len() == p_index {
            hashmap.insert((s_index, p_index), false);
            return false;
        }
        //println!("s_chars: {:?}", &s_chars[s_index..]);
        //println!("p_chars: {:?}", &p_chars[p_index..]);

        if p_chars[p_index] == '*' {
            //println!("s_chars: {:?}", &s_chars[s_index..]);
            for index in s_index..=s_chars.len() {
                let result = Solution::is_match_helper(s_chars, index, p_chars, p_index + 1, hashmap);
                hashmap.insert((index, p_index + 1), result);
                if result {
                    hashmap.insert((s_index, p_index), true);
                    return true;
                }
            }
            hashmap.insert((s_index, p_index), false);
            return false;
        } else if p_chars[p_index] == '?' {
            let result = Solution::is_match_helper(s_chars, s_index + 1, p_chars, p_index + 1, hashmap);
            hashmap.insert((s_index + 1, p_index + 1), result);
            return result;
        } else if p_chars[p_index] == s_chars[s_index] {
            let result = Solution::is_match_helper(s_chars, s_index + 1, p_chars, p_index + 1, hashmap);
            hashmap.insert((s_index + 1, p_index + 1), result);
            return result;
        } else {
            hashmap.insert((s_index, p_index), false);
            return false;
        }
    }
    pub fn is_match(s: String, p: String) -> bool {
        let mut hashmap: HashMap<(usize, usize), bool> = HashMap::new();
        let s_chars: Vec<char> = s.chars().collect();
        let p_chars: Vec<char> = p.chars().collect();
        Solution::is_match_helper(&s_chars, 0, &p_chars, 0, &mut hashmap)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_44() {
        assert_eq!(Solution::is_match("".to_string(), "******".to_string()), true);
        assert_eq!(Solution::is_match("ab".to_string(), "?*".to_string()), true);
        assert_eq!(Solution::is_match("aa".to_string(), "a".to_string()), false);
        assert_eq!(Solution::is_match("aa".to_string(), "*".to_string()), true);
        assert_eq!(Solution::is_match("cb".to_string(), "?a".to_string()), false);
        assert_eq!(Solution::is_match("adceb".to_string(), "*a*b".to_string()), true);
        assert_eq!(Solution::is_match("acdcb".to_string(), "a*c?b".to_string()), false);
    }
}

```
