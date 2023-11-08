---
title: 65. valid number
date: '2021-07-05'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0065 valid number
---



A valid number can be split up into these components (in order):

<ol>

A decimal number or an integer.

(Optional) An 'e' or 'E', followed by an integer.

</ol>

A decimal number can be split up into these components (in order):

<ol>

(Optional) A sign character (either '+' or '-').

One of the following formats:

<ol>

One or more digits, followed by a dot '.'.

One or more digits, followed by a dot '.', followed by one or more digits.

A dot '.', followed by one or more digits.

</ol>



</ol>

An integer can be split up into these components (in order):

<ol>

(Optional) A sign character (either '+' or '-').

One or more digits.

</ol>

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.



>   Example 1:
>   Input: s <TeX>=</TeX> "0"
>   Output: true
>   Example 2:
>   Input: s <TeX>=</TeX> "e"
>   Output: false
>   Example 3:
>   Input: s <TeX>=</TeX> "."
>   Output: false
>   Example 4:
>   Input: s <TeX>=</TeX> ".1"
>   Output: true
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 20
>   	s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here


#[derive(PartialEq, Clone, Copy)]
enum State {
Initial,
Symbol,
Digit,
Decimal,
DecimalDigit,
Exponent,
ExponentSymbol,
ExponentDigit,
Fail,
}
struct StateMachine { state: State }

impl StateMachine {
fn new() -> Self {
StateMachine {
state: State::Initial
}
}
fn parse (&mut self, ch: char) {
self.state = match self.state {
State::Initial => {
match ch {
'+' | '-' => State::Symbol,
'0'..='9' => State::Digit,
'.' => State::Decimal,
_ => State::Fail,
}
},
State::Symbol => {
match ch {
'0'..='9' => State::Digit,
'.' => State::Decimal,
_ => State::Fail,
}
},
State::Digit => {
match ch {
'0'..='9' => State::Digit,
'.' => State::DecimalDigit,
'e' | 'E' => State::Exponent,
_ => State::Fail,
}
},
State::Decimal => {
match ch {
'0'..='9' => State::DecimalDigit,
_ => State::Fail,
}
},
State::DecimalDigit => {
match ch {
'e' | 'E' => State::Exponent,
'0'..='9' => State::DecimalDigit,
_ => State::Fail,
}
},
State::Exponent => {
match ch {
'+' | '-' => State::ExponentSymbol,
'0'..='9' => State::ExponentDigit,
_ => State::Fail,
}
},
State::ExponentSymbol => {
match ch {
'0'..='9' => State::ExponentDigit,
_ => State::Fail,
}
},
State::ExponentDigit => {
match ch {
'0'..='9' => State::ExponentDigit,
_ => State::Fail,
}
},
State::Fail => {
State:: Fail
}
// The rest should fail.
_ => panic!("Invalid state transition!"),
};
}
fn end(&mut self) {
self.state = match self.state {
State::Decimal | State::Exponent | State::ExponentSymbol => {
State::Fail
},
_ => {
self.state
}
};
}
}

impl Solution {
pub fn is_number(s: String) -> bool {
let mut state_machine = StateMachine::new();
for ch in s.trim().chars() {
state_machine.parse(ch);
}
state_machine.end();
state_machine.state != State::Fail
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_65() {
//".1"  "3."  "+.8"
assert_eq!(Solution::is_number("+.8".to_string()), true);
assert_eq!(Solution::is_number(".".to_string()), false);
assert_eq!(Solution::is_number("3.".to_string()), true);
assert_eq!(Solution::is_number(".1".to_string()), true);
assert_eq!(Solution::is_number("+150".to_string()), true);
assert_eq!(Solution::is_number("-150".to_string()), true);
assert_eq!(Solution::is_number("150".to_string()), true);
assert_eq!(Solution::is_number("0".to_string()), true);
assert_eq!(Solution::is_number(" +110.12344 ".to_string()), true);
assert_eq!(Solution::is_number(" -0.1 ".to_string()), true);
assert_eq!(Solution::is_number(" 0.1 ".to_string()), true);
assert_eq!(Solution::is_number("abc".to_string()), false);
assert_eq!(Solution::is_number("1 a".to_string()), false);
assert_eq!(Solution::is_number("2e10".to_string()), true);
assert_eq!(Solution::is_number(" -90e3 ".to_string()), true);
assert_eq!(Solution::is_number(" 1e".to_string()), false);
assert_eq!(Solution::is_number("e3".to_string()), false);
assert_eq!(Solution::is_number(" 6e-1".to_string()), true);
assert_eq!(Solution::is_number(" 99e2.5 ".to_string()), false);
assert_eq!(Solution::is_number(" 53.5e93 ".to_string()), true);
assert_eq!(Solution::is_number(" --6 ".to_string()), false);
assert_eq!(Solution::is_number(" -+3 ".to_string()), false);
assert_eq!(Solution::is_number(" 95a54e53 ".to_string()), false);
}
}

```
