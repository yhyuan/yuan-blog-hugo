---
title: 394. decode string
date: '2022-02-18'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0394 decode string
---



Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



>   Example 1:
>   Input: s <TeX>=</TeX> "3[a]2[bc]"
>   Output: "aaabcbc"
>   Example 2:
>   Input: s <TeX>=</TeX> "3[a2[c]]"
>   Output: "accaccacc"
>   Example 3:
>   Input: s <TeX>=</TeX> "2[abc]3[cd]ef"
>   Output: "abcabccdcdcdef"
>   Example 4:
>   Input: s <TeX>=</TeX> "abc3[cd]xyz"
>   Output: "abccdcdcdxyz"
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 30
>   	s consists of lowercase English letters, digits, and square brackets '[]'.
>   	s is guaranteed to be a valid input.
>   	All the integers in s are in the range [1, 300].


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn decode_string(s: String) -> String {
let n = s.len();
let chars: Vec<char> = s.chars().collect();
let mut result = 0;
let mut num_pos: Option<usize> = None;
let mut left_bracket_pos: Option<usize> = None;
let mut right_bracket_pos: Option<usize> = None;
for (i, &ch) in chars.iter().enumerate() {
if ch >= '0' && ch <= '9' && num_pos.is_none() {
num_pos = Some(i);
} else if ch == '[' {
if left_bracket_pos.is_none() {
left_bracket_pos = Some(i);
}
result += 1;
} else if ch == ']' {
result -= 1;
if result == 0 {
right_bracket_pos = Some(i);
break;
}
}
}
if num_pos.is_none() && left_bracket_pos.is_none() && right_bracket_pos.is_none() {
return s;
}
let num = num_pos.unwrap();
let left = left_bracket_pos.unwrap();
let right = right_bracket_pos.unwrap();
let count = format!("{}", &s[num..left]).parse::<u32>().unwrap();
let sub_s = Self::decode_string(format!("{}", &s[left + 1..right]));
let sub_s = (0..count).into_iter().map(|_| sub_s.clone()).collect::<Vec<String>>().join("");
format!("{}{}{}", format!("{}", &s[0..num]), sub_s, Self::decode_string(format!("{}", &s[right + 1..])))
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_394() {
assert_eq!(Solution::decode_string("3[a]2[bc]".to_owned()), "aaabcbc".to_owned());
assert_eq!(Solution::decode_string("3[a2[c]]".to_owned()), "accaccacc".to_owned());
assert_eq!(Solution::decode_string("2[abc]3[cd]ef".to_owned()), "abcabccdcdcdef".to_owned());
assert_eq!(Solution::decode_string("abc3[cd]xyz".to_owned()), "abccdcdcdxyz".to_owned());
}
}

```
