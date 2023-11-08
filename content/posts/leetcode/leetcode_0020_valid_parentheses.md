---
title: 20. valid parentheses
date: '2021-05-21'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0020 valid parentheses
---



Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

<ol>

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

</ol>



>   Example 1:
>   Input: s <TeX>=</TeX> "()"
>   Output: true
>   Example 2:
>   Input: s <TeX>=</TeX> "()[]{}"
>   Output: true
>   Example 3:
>   Input: s <TeX>=</TeX> "(]"
>   Output: false
>   Example 4:
>   Input: s <TeX>=</TeX> "([)]"
>   Output: false
>   Example 5:
>   Input: s <TeX>=</TeX> "{[]}"
>   Output: true
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 10^4
>   	s consists of parentheses only '()[]{}'.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn is_valid(s: String) -> bool {
let chars: Vec<char> = s.chars().collect();
let mut stack: Vec<char> = vec![];
for char in chars {
if char == '(' || char == '[' || char == '{' {
stack.push(char);
} else if char == ')' || char == ']' || char == '}' {
if stack.len() == 0 {
return false;
}
if let Some(_char) = stack.pop() {
if (char == ')' && _char == '(') || (char == ']' && _char == '[') || (char == '}' && _char == '{')  {
continue;
} else {
return false;
}
}
} else {
panic!("Wrong input!")
}
}
stack.len() == 0
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_20() {
assert_eq!(Solution::is_valid("()[]{}".to_string()), true);
assert_eq!(Solution::is_valid("([)]".to_string()), false);
}
}

```
