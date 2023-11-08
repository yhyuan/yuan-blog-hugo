---
title: 5. longest palindromic substring
date: '2021-05-06'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0005 longest palindromic substring
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={5}/>
 

  Given a string s, return the longest palindromic substring in s.

 

 >   Example 1:

 

 >   Input: s <TeX>=</TeX> "babad"

 >   Output: "bab"

 >   Note: "aba" is also a valid answer.

 

 >   Example 2:

 

 >   Input: s <TeX>=</TeX> "cbbd"

 >   Output: "bb"

 

 >   Example 3:

 

 >   Input: s <TeX>=</TeX> "a"

 >   Output: "a"

 

 >   Example 4:

 

 >   Input: s <TeX>=</TeX> "ac"

 >   Output: "a"

 

 

  **Constraints:**

 

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 1000

 >   	s consist of only digits and English letters.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        if s.len() == 0 {
            return "".to_string();
        }
        let chars: Vec<char> = s.chars().collect();
        //let max_len = i32::MIN;
        let mut min_index = usize::MAX;
        let mut max_index = usize::MAX;
        let mut max_len = 0usize;
        // If the length of palindromic is odd, so we start from the center of each possible letter.
        for i in 0..chars.len() {
            let mut k = 0usize;
            while chars[i + k] == chars[i - k] {
                k = k + 1;
                if i < k || i + k >= chars.len() {
                    break;
                }
            }
            k = if k > 0 { k - 1 } else { 0 };
            //k = k - 1;
            let len = 2 * k + 1;
            if len > max_len {
                max_len = len;
                min_index = i - k;
                max_index = i + k;
            }
        }
        //println!("max_len: {}", max_len);
        // If the length of palindromic is even, so we start from the of each possible gap between two letters.
        for i in 0..(chars.len() - 1) {
            if chars[i] == chars[i + 1] {
                let mut k = 0usize;
                while chars[i - k] == chars[i + 1 + k] {
                    k = k + 1;
                    if i < k || i + k + 1 >= chars.len() {
                        break;
                    }
                }
                // k = 0, 2; k = 1; 4
                k = k - 1;
                let len = 2 * (k + 1);
                if len > max_len {
                    max_len = len;
                    min_index = i - k;
                    max_index = i + k + 1;
                }
            }
        }
        chars[min_index..=max_index].iter().collect()
    }
}
*/
impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let n = s.len(); 
        if n == 0 {
            return "".to_string();
        }
        let chars: Vec<char> = s.chars().collect();
        let mut dp:Vec<Vec<bool>> = vec![vec![false; n]; n];
        for i in 0..n {
            dp[i][i] = true;
            if i < n - 1 {
                dp[i][i + 1] = chars[i] == chars[i + 1];
            }
        }
        //println!("dp: {:?}", dp);
        for len in 3..=n {
            for i in 0..=n - len {
                dp[i][i + len - 1] = dp[i + 1][i + len - 1 - 1] && chars[i] == chars[i + len - 1];  
            }
        }
        //println!("dp: {:?}", dp);
        /*
        for i in 0..n {
            for j in i+2..n {
                dp[i][j] = dp[i + 1][j - 1] && chars[i] == chars[j];  
            }
        }
        */
        let mut len = 0usize;
        let mut pos = (0usize, 0usize);
        for i in 0..n {
            for j in i..n {
                if dp[i][j] {
                    if j - i + 1 > len {
                        len = j - i + 1;
                        pos = (i, j);
                    }
                }
            }
        }
        (pos.0..=pos.1).into_iter().map(|k| chars[k]).collect::<String>()
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_5() {
        assert_eq!(Solution::longest_palindrome("aaaaa".to_owned()), "aaaaa");
        assert_eq!(Solution::longest_palindrome("babab".to_owned()), "babab");
        assert_eq!(Solution::longest_palindrome("babcd".to_owned()), "bab");
        assert_eq!(Solution::longest_palindrome("cbbd".to_owned()), "bb");
        assert_eq!(Solution::longest_palindrome("bb".to_owned()), "bb");
        assert_eq!(Solution::longest_palindrome("".to_owned()), "");
    }
}

```
