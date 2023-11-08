---
title: 282. expression add operators
date: '2021-12-16'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0282 expression add operators
---



Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '' between the digits of num so that the resultant expression evaluates to the target value.



>   Example 1:
>   Input: num <TeX>=</TeX> "123", target <TeX>=</TeX> 6
>   Output: ["123","1+2+3"]
>   Example 2:
>   Input: num <TeX>=</TeX> "232", target <TeX>=</TeX> 8
>   Output: ["23+2","2+32"]
>   Example 3:
>   Input: num <TeX>=</TeX> "105", target <TeX>=</TeX> 5
>   Output: ["10+5","10-5"]
>   Example 4:
>   Input: num <TeX>=</TeX> "00", target <TeX>=</TeX> 0
>   Output: ["00","0+0","0-0"]
>   Example 5:
>   Input: num <TeX>=</TeX> "3456237490", target <TeX>=</TeX> 9191
>   Output: []
**Constraints:**
>   	1 <TeX>\leq</TeX> num.length <TeX>\leq</TeX> 10
>   	num consists of only digits.
>   	-2^31 <TeX>\leq</TeX> target <TeX>\leq</TeX> 2^31 - 1


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here


#[derive(Debug, PartialEq, Clone, Copy)]
pub enum Token {
Operator(char),
Number(i64),
}

impl Solution {
pub fn parse_number(number_chars: &mut Vec<char>, tokens: &mut Vec<Token>) -> bool {
if number_chars.len() == 0 {
return false;
}
if number_chars.len() == 1 && number_chars[0] == '0' {
tokens.push(Token::Number(0));
number_chars.clear();
return true;
}
if number_chars.len() > 1 && number_chars[0] == '0' {
return false;
}
let val = number_chars.iter().collect::<String>().parse::<i64>().unwrap();
tokens.push(Token::Number(val));
number_chars.clear();
return true;
}
pub fn parse_tokens(chars: &Vec<char>) -> Option<Vec<Token>> {
let mut tokens: Vec<Token> = vec![];
let mut number_chars: Vec<char> = vec![];
for i in 0..chars.len() {
let ch = chars[i];
if ch == '+' || ch == '-' || ch == '*' {
let res = Solution::parse_number(&mut number_chars, &mut tokens);
if !res {
return None;
}
tokens.push(Token::Operator(ch));
} else {
number_chars.push(ch);
}
}
let res = Solution::parse_number(&mut number_chars, &mut tokens);
if !res {
return None;
}
Some(tokens)
}
pub fn calculate(s: &String) -> Option<i64> {
let chars: Vec<char> = s.chars().filter(|ch| *ch != ' ').collect();
let tokens: Option<Vec<Token>> = Solution::parse_tokens(&chars);
if tokens.is_none() {
return None;
}
let tokens: Vec<Token> = tokens.unwrap();
let mut stack: Vec<Token> = vec![];
let mut operator: Option<char> = None;
for token in tokens.iter() {
if token == &Token::Operator('*') {
operator = Some('*');
} else {
if operator.is_none() {
stack.push(token.clone());
} else {
let pre_token = stack.pop().unwrap();
let val = match (pre_token, token) {
(Token::Number(v1), Token::Number(v2)) => {
v1 * v2
},
_ => {
return None;
}
};
stack.push(Token::Number(val));
operator = None;
}
}
}
let tokens = stack;
let mut stack: Vec<Token> = vec![];
let mut operator: Option<char> = None;
for token in tokens.iter() {
if token == &Token::Operator('+') {
operator = Some('+');
} else if token == &Token::Operator('-') {
operator = Some('-');
} else {
if operator.is_none() {
stack.push(token.clone());
} else {
let pre_token = stack.pop().unwrap();
let val = match (pre_token, token) {
(Token::Number(v1), Token::Number(v2)) => {
if operator.unwrap() == '+' {v1 + v2} else {v1 - v2}
},
_ => {
return None;
}
};
stack.push(Token::Number(val));
}
}
}
let token = stack.last().unwrap();
match token {
Token::Number(val) => {
return Some(*val);
},
_ => {
panic!("wrong input");
}
};
}
pub fn add_operators_helper(chars: &Vec<char>, operators: &mut Vec<char>, target: i32) -> Vec<String> {
let n = chars.len();
if operators.len() == n - 1 {
let mut result: Vec<char> = vec![];
for i in 0..n {
result.push(chars[i]);
if i < n - 1 && operators[i] != ' ' {
result.push(operators[i]);
}
}
let s = result.iter().collect::<String>();
let res: Option<i64> = Self::calculate(&s);
if res.is_some() && res.unwrap() == target as i64 {
return vec![s];
} else {
return vec![];
}
}
let ops: Vec<char> = vec!['+', '-', '*', ' '];
let mut results: Vec<String> = vec![];
for &op in ops.iter() {
operators.push(op);
let res = Self::add_operators_helper(chars, operators, target);
for s in res {
results.push(s);
}
operators.pop();
}
results
}
pub fn add_operators(num: String, target: i32) -> Vec<String> {
let chars: Vec<char> = num.chars().collect();
let mut operators: Vec<char> = vec![];
Solution::add_operators_helper(&chars, &mut operators, target)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_282() {
let empty: Vec<String> = vec![];
assert_eq!(Solution::add_operators("3456237490".to_string(), 9191), empty);
assert_eq!(Solution::add_operators("123".to_string(), 6), vec!["1+2+3".to_string(), "1*2*3".to_string()]);
assert_eq!(Solution::add_operators("232".to_string(), 8), vec!["2+3*2".to_string(), "2*3+2".to_string()]);
assert_eq!(Solution::add_operators("105".to_string(), 5), vec!["1*0+5".to_string(),"10-5".to_string()]);
assert_eq!(Solution::add_operators("00".to_string(), 0), vec!["0+0".to_string(),"0-0".to_string(), "0*0".to_string()]);
}
}

```
