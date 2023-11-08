---
title: 150. evaluate reverse polish notation
date: '2021-09-22'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0150 evaluate reverse polish notation
---

 

  Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

  Valid operators are +, -, , and /. Each operand may be an integer or another expression.

  Note that division between two integers should truncate toward zero.

  It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

   

 >   Example 1:

  

 >   Input: tokens <TeX>=</TeX> ["2","1","+","3",""]

 >   Output: 9

 >   Explanation: ((2 + 1)  3) <TeX>=</TeX> 9

  

 >   Example 2:

  

 >   Input: tokens <TeX>=</TeX> ["4","13","5","/","+"]

 >   Output: 6

 >   Explanation: (4 + (13 / 5)) <TeX>=</TeX> 6

  

 >   Example 3:

  

 >   Input: tokens <TeX>=</TeX> ["10","6","9","3","+","-11","","/","","17","+","5","+"]

 >   Output: 22

 >   Explanation: ((10  (6 / ((9 + 3)  -11))) + 17) + 5

 >   <TeX>=</TeX> ((10  (6 / (12  -11))) + 17) + 5

 >   <TeX>=</TeX> ((10  (6 / -132)) + 17) + 5

 >   <TeX>=</TeX> ((10  0) + 17) + 5

 >   <TeX>=</TeX> (0 + 17) + 5

 >   <TeX>=</TeX> 17 + 5

 >   <TeX>=</TeX> 22

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> tokens.length <TeX>\leq</TeX> 10^4

 >   	tokens[i] is either an operator: "+", "-", "", or "/", or an integer in the range [-200, 200].


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = vec![];
        for token in tokens {
            if token.len() == 1 {
                let chars: Vec<char> = token.chars().collect();
                if chars[0] == '+' || chars[0] == '-' || chars[0] == '*' || chars[0] == '/' {
                    let v1 = stack.pop().unwrap();
                    let v2 = stack.pop().unwrap();
                    let v = match chars[0] {
                        '+' => {
                            v1 + v2
                        },
                        '-' => {
                            v2 - v1
                        },
                        '*' => {
                            v1 * v2
                        },
                        '/' => {
                            v2 / v1
                        }
                        _ => {
                            panic!("wrong input")
                        }
                    };
                    stack.push(v);
                } else {
                    stack.push(token.parse::<i32>().unwrap());
                }
            } else {
                stack.push(token.parse::<i32>().unwrap());
            }
        }
        stack.pop().unwrap()
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_150() {
        assert_eq!(Solution::eval_rpn(vec!["10".to_string(),"6".to_string(),"9".to_string(),"3".to_string(),"+".to_string(),"-11".to_string(),"*".to_string(),"/".to_string(),"*".to_string(),"17".to_string(),"+".to_string(),"5".to_string(),"+".to_string()]), 22);
    }
}

```
