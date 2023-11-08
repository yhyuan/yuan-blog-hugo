---
title: 1021. remove outermost parentheses
date: '2022-06-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1021 remove outermost parentheses
---



A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.



For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.



A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s <TeX>=</TeX> A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s <TeX>=</TeX> P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.



>   Example 1:
>   Input: s <TeX>=</TeX> "(()())(())"
>   Output: "()()()"
>   Explanation:
>   The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
>   After removing outer parentheses of each part, this is "()()" + "()" <TeX>=</TeX> "()()()".
>   Example 2:
>   Input: s <TeX>=</TeX> "(()())(())(()(()))"
>   Output: "()()()()(())"
>   Explanation:
>   The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
>   After removing outer parentheses of each part, this is "()()" + "()" + "()(())" <TeX>=</TeX> "()()()()(())".
>   Example 3:
>   Input: s <TeX>=</TeX> "()()"
>   Output: ""
>   Explanation:
>   The input string is "()()", with primitive decomposition "()" + "()".
>   After removing outer parentheses of each part, this is "" + "" <TeX>=</TeX> "".
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 10^5
>   	s[i] is either '(' or ')'.
>   	s is a valid parentheses string.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn remove_outer_parentheses(s: String) -> String {
let mut chars: Vec<char> = s.chars().collect();
let mut stack: Vec<char> = vec![];
//let mut indices: Vec<usize> = vec![0];
let mut start = 0usize;
let n = chars.len();
let mut ans: Vec<char> = vec![];
for i in 0..n {
if chars[i] == '(' {
stack.push(chars[i]);
} else {
stack.pop();
if stack.len() == 0 {
for j in start + 1..i {
ans.push(chars[j]);
}
start = i + 1;
}
}
}
if stack.len() == 0 {
for j in start + 1..n - 1 {
ans.push(chars[j]);
}
}
let res = ans.iter().collect::<String>();
res
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1021() {
}
}

```
