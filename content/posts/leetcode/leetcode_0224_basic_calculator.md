---
title: 224. basic calculator
date: '2021-11-10'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0224 basic calculator
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={224}/>
 

  Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

  Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "1 + 1"

 >   Output: 2

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> " 2-1 + 2 "

 >   Output: 3

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "(1+(4+5+2)-3)+(6+8)"

 >   Output: 23

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 3  10^5

 >   	s consists of digits, '+', '-', '(', ')', and ' '.

 >   	s represents a valid expression.

 >   	'+' is not used as a unary operation.

 >   	'-' could be used as a unary operation but it has to be inside parentheses.

 >   	There will be no two consecutive operators in the input.

 >   	Every number and running calculation will fit in a signed 32-bit integer.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
#[derive(Debug, PartialEq, Clone, Copy)]
pub enum Token {
    LeftBracket,
    RightBracket,
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
            if ch == ' ' {
                continue;
            }
            if ch == '(' {
                tokens.push(Token::LeftBracket);
            } else if ch == ')' {
                Solution::parse_number(&mut number_chars, &mut tokens);
                tokens.push(Token::RightBracket);
            } else if ch == '+' || ch == '-' {
                Solution::parse_number(&mut number_chars, &mut tokens);
                tokens.push(Token::Operator(ch));
            } else {
                number_chars.push(ch);
            }
        }
        Solution::parse_number(&mut number_chars, &mut tokens);
        tokens
    }
    pub fn calculate_helper(tokens: &Vec<Token>) -> i32 {
        let mut result = i32::MIN;
        let mut operator: char = ' ';
        for i in 0..tokens.len() {
            match &tokens[i] {
                Token::Number(num) => {
                    if result == i32::MIN {
                        if operator == '-' {
                            result = -*num;
                        } else {
                            result = *num;
                        }
                    } else {
                        if operator == '+' {
                            result = result + num;
                        } else if operator == '-' {
                            result = result - num; 
                        } else {
                            panic!("Wrong operator");
                        }
                    }
                },
                Token::Operator(op) => {
                    operator = *op;
                }
                _ => {
                    panic!("Wrong input");
                }
            }
        }
        result
    }
    pub fn calculate(s: String) -> i32 {
        let chars: Vec<char> = s.chars().filter(|ch| *ch != ' ').collect();
        let tokens = Solution::parse_tokens(&chars);
        let mut stack: Vec<Token> = vec![];
        for i in 0..tokens.len() {
            if tokens[i] == Token::RightBracket {
                let mut items: Vec<Token> = vec![];
                while stack.last().unwrap() != &Token::LeftBracket {
                    let token = stack.pop().unwrap();
                    items.insert(0, token);
                }
                stack.pop();
                let val = Solution::calculate_helper(&items);
                stack.push(Token::Number(val));
            } else {
                stack.push(tokens[i]);
            }
        }
        Solution::calculate_helper(&stack)
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_224() {
        assert_eq!(Solution::calculate("-2+ 1".to_string()), -1);
        assert_eq!(Solution::calculate("1 + 1".to_string()), 2);
        assert_eq!(Solution::calculate(" 2-1 + 2 ".to_string()), 3);
        assert_eq!(Solution::calculate("(1+(4+5+2)-3)+(6+8)".to_string()), 23);
    }
}

```
