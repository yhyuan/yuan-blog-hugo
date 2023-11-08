---
title: 87. scramble string
date: '2021-07-27'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0087 scramble string
---

 

  We can scramble a string s to get a string t using the following algorithm:

  <ol>

  	If the length of the string is 1, stop.

  	If the length of the string is > 1, do the following:

  	

  		Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s <TeX>=</TeX> x + y.

  		Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s <TeX>=</TeX> x + y or s <TeX>=</TeX> y + x.

  		Apply step 1 recursively on each of the two substrings x and y.

  	

  	

  </ol>

  Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

   

 >   Example 1:

  

 >   Input: s1 <TeX>=</TeX> "great", s2 <TeX>=</TeX> "rgeat"

 >   Output: true

 >   Explanation: One possible scenario applied on s1 is:

 >   "great" --> "gr/eat" // divide at random index.

 >   "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.

 >   "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at ranom index each of them.

 >   "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.

 >   "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".

 >   "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.

 >   The algorithm stops now and the result string is "rgeat" which is s2.

 >   As there is one possible scenario that led s1 to be scrambled to s2, we return true.

  

 >   Example 2:

  

 >   Input: s1 <TeX>=</TeX> "abcde", s2 <TeX>=</TeX> "caebd"

 >   Output: false

  

 >   Example 3:

  

 >   Input: s1 <TeX>=</TeX> "a", s2 <TeX>=</TeX> "a"

 >   Output: true

  

   

  **Constraints:**

  

 >   	s1.length <TeX>=</TeX><TeX>=</TeX> s2.length

 >   	1 <TeX>\leq</TeX> s1.length <TeX>\leq</TeX> 30

 >   	s1 and s2 consist of lower-case English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
//use std::collections::HashSet;
impl Solution {
    pub fn is_scramble_helper(s1: &String, start: usize, end: usize, memo: &mut HashMap<(usize, usize), HashMap<String, bool>>) -> HashMap<String, bool> {
        if memo.contains_key(&(start, end)) {
            return memo[&(start, end)].clone();
        }
        let mut hashmap: HashMap<String, bool> = HashMap::new();
        if start == end {
            let str = (&s1[start..=end]).to_string();
            hashmap.insert(str, true);
            memo.insert((start, end), hashmap);
            return memo[&(start, end)].clone();
        }
        for i in start..end {
            let hashmap_1 = Solution::is_scramble_helper(&s1, start, i, memo);
            let hashmap_2 = Solution::is_scramble_helper(&s1, i + 1, end, memo);
            for (k1, _) in hashmap_1.iter() {
                for (k2, _) in hashmap_2.iter() {
                    let str1 = format!("{}{}", k1, k2);
                    if !hashmap.contains_key(&str1) {
                        hashmap.insert(str1, true);
                    }
                    let str2 = format!("{}{}", k2, k1);
                    if !hashmap.contains_key(&str2) {
                        hashmap.insert(str2, true);
                    }
                }
            }
        }
        memo.insert((start, end), hashmap);
        return memo[&(start, end)].clone();
    }
    pub fn is_scramble(s1: String, s2: String) -> bool {
        let n = s1.len();
        let mut memo: HashMap<(usize, usize), HashMap<String, bool>> = HashMap::new();
        let results: HashMap<String, bool> = Solution::is_scramble_helper(&s1, 0, n - 1, &mut memo);
        //println!("results: {:?}", results);
        results.contains_key(&s2)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_87() {
        assert_eq!(Solution::is_scramble("great".to_string(), "rgeat".to_string()), true);
        assert_eq!(Solution::is_scramble("abcde".to_string(), "caebd".to_string()), false);
        assert_eq!(Solution::is_scramble("a".to_string(), "a".to_string()), true);
        assert_eq!(Solution::is_scramble("a".to_string(), "b".to_string()), false);
        //assert_eq!(Solution::is_scramble("abcdefghijklmn".to_string(), "efghijklmncadb".to_string()), false);
    }
}


```
