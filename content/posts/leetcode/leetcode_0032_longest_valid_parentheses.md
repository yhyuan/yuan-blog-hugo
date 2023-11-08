---
title: 32. longest valid parentheses
date: '2021-06-02'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0032 longest valid parentheses
---



Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



>   Example 1:
>   Input: s <TeX>=</TeX> "(()"
>   Output: 2
>   Explanation: The longest valid parentheses substring is "()".
>   Example 2:
>   Input: s <TeX>=</TeX> ")()())"
>   Output: 4
>   Explanation: The longest valid parentheses substring is "()()".
>   Example 3:
>   Input: s <TeX>=</TeX> ""
>   Output: 0
**Constraints:**
>   	0 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 3  10^4
>   	s[i] is '(', or ')'.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn longest_valid_parentheses(s: String) -> i32 {
if s.len() == 0 {
return 0;
}
let chars: Vec<char> = s.chars().collect();
let mut dp: Vec<usize> = vec![0; chars.len()];
for i in 1..chars.len() {
if chars[i] == ')' {
if chars[i - 1] == '(' {
if i == 1 {
dp[i] = 2;
} else {
dp[i] = dp[i - 2] + 2;
}
} else {
if i >= dp[i-1] + 1 && chars[i - dp[i - 1] - 1] == '(' {
let v = if i >= dp[i - 1] + 2 {dp[i - dp[i - 1] - 2]} else {0};
dp[i] = dp[i - 1] + v + 2;
} else {
dp[i] = 0;
}
}
}
}
//println!("{:?}", chars);
//println!("{:?}", dp);
let value = dp.iter().max().unwrap();
*value as i32
//dp[s.len() - 1]
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_32() {
//
assert_eq!(Solution::longest_valid_parentheses("(()())".to_string()), 6);

assert_eq!(Solution::longest_valid_parentheses("())".to_string()), 2);
assert_eq!(Solution::longest_valid_parentheses("()()(())".to_string()), 8);
assert_eq!(Solution::longest_valid_parentheses(")()())".to_string()), 4);
assert_eq!(Solution::longest_valid_parentheses(")(".to_string()), 0);
assert_eq!(Solution::longest_valid_parentheses("(()".to_string()), 2);
assert_eq!(
Solution::longest_valid_parentheses("(((((()()".to_string()),
4
);
assert_eq!(
Solution::longest_valid_parentheses("((((((((()))".to_string()),
6
);
assert_eq!(Solution::longest_valid_parentheses("()".to_string()), 2);
assert_eq!(Solution::longest_valid_parentheses("()(()".to_string()), 2);
assert_eq!(
Solution::longest_valid_parentheses(")()(((())))(".to_string()),
10
);
assert_eq!(
Solution::longest_valid_parentheses("(()(((()".to_string()),
2
);
assert_eq!(Solution::longest_valid_parentheses("".to_string()), 0);

}
}

```
