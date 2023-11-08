---
title: 227. basic calculator ii
date: '2021-11-13'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0227 basic calculator ii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={227}/>
 

  Given a string s which represents an expression, evaluate this expression and return its value. 

  The integer division should truncate toward zero.

  You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].

  Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

   

 >   Example 1:

 >   Input: s <TeX>=</TeX> "3+22"

 >   Output: 7

 >   Example 2:

 >   Input: s <TeX>=</TeX> " 3/2 "

 >   Output: 1

 >   Example 3:

 >   Input: s <TeX>=</TeX> " 3+5 / 2 "

 >   Output: 5

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 3  10^5

 >   	s consists of integers and operators ('+', '-', '', '/') separated by some number of spaces.

 >   	s represents a valid expression.

 >   	All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].

 >   	The answer is guaranteed to fit in a 32-bit integer.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
#[derive(Debug, PartialEq, Clone, Copy)]
pub enum Token {
    Operator(char),
    Number(i32),
}

impl Solution {
    pub fn parse_number(number_chars: &mut Vec<char>, tokens: &mut Vec<Token>) {
        if number_chars.len() > 0 {
            let val = number_chars.iter().collect::<String>().parse::<i32>().unwrap();
            tokens.push(Token::Number(val));
            number_chars.clear();
        }
    }
    pub fn parse_tokens(chars: &Vec<char>) -> Vec<Token> {
        let mut tokens: Vec<Token> = vec![];
        let mut number_chars: Vec<char> = vec![];
        for i in 0..chars.len() {
            let ch = chars[i];
            if ch == '+' || ch == '-' || ch == '*' || ch == '/' {
                Solution::parse_number(&mut number_chars, &mut tokens);
                tokens.push(Token::Operator(ch));
            } else {
                number_chars.push(ch);
            }
        }
        Solution::parse_number(&mut number_chars, &mut tokens);
        tokens
    }
    pub fn calculate(s: String) -> i32 {
        let chars: Vec<char> = s.chars().filter(|ch| *ch != ' ').collect();
        let tokens: Vec<Token> = Solution::parse_tokens(&chars);
        let mut stack: Vec<Token> = vec![];
        let mut operator: Option<char> = None;
        for token in tokens.iter() {
            if token == &Token::Operator('*') {
                operator = Some('*');
            } else if token == &Token::Operator('/') {
                operator = Some('/');
            } else {
                if operator.is_none() {
                    stack.push(token.clone());
                } else {
                    let pre_token = stack.pop().unwrap();
                    let val = match (pre_token, token) {
                        (Token::Number(v1), Token::Number(v2)) => {
                            if operator.unwrap() == '*' {v1 * v2} else {v1 / v2}
                        },
                        _ => {
                            panic!("wrong input.")
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
                            panic!("wrong input.")
                        }
                    };
                    stack.push(Token::Number(val));
                }
            }
        }
        let token = stack.last().unwrap();
        match token {
            Token::Number(val) => {
                return *val;
            },
            _ => {
                panic!("wrong input");
            }
        };
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_227() {
        assert_eq!(Solution::calculate("3+2*2".to_string()), 7);
        assert_eq!(Solution::calculate(" 3/2 ".to_string()), 1);
        assert_eq!(Solution::calculate(" 3+5 / 2 ".to_string()), 5);
    }
}

```
