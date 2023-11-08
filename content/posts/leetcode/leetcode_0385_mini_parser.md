---
title: 385. mini parser
date: '2022-02-09'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0385 mini parser
---

 

  Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.

  Each element is either an integer or a list whose elements may also be integers or other lists.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "324"

 >   Output: 324

 >   Explanation: You should return a NestedInteger object which contains a single integer 324.

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "[123,[456,[789]]]"

 >   Output: [123,[456,[789]]]

 >   Explanation: Return a NestedInteger object containing a nested list with 2 elements:

 >   1. An integer containing value 123.

 >   2. A nested list containing two elements:

 >       i.  An integer containing value 456.

 >       ii. A nested list with one element:

 >            a. An integer containing value 789

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 5  10^4

 >   	s consists of digits, square brackets "[]", negative sign '-', and commas ','.

 >   	s is the serialization of valid NestedInteger.


## Solution
### Rust
```rust
pub struct Solution {}
#[derive(Debug, PartialEq, Eq)]
pub enum NestedInteger {
   Int(i32),
   List(Vec<NestedInteger>)
}

// submission codes start here

// #[derive(Debug, PartialEq, Eq)]
// pub enum NestedInteger {
//   Int(i32),
//   List(Vec<NestedInteger>)
// }
impl Solution {
    pub fn deserialize(s: String) -> NestedInteger {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        //println!("s: {}", s);
        if chars[0] != '[' {
            let val = s.parse::<i32>().unwrap();
            NestedInteger::Int(val)
        } else {
            if n == 2 {
                return NestedInteger::List(vec![]);
            }
            let mut results: Vec<NestedInteger> = vec![];
            let mut count = 0;
            let mut start_index = 1;
            for i in 1..n - 1 {
                let ch = chars[i];
                if ch == ',' {
                    if count == 0 {
                        //println!("val: {}", &s[start_index..i]);
                        let item = Self::deserialize(format!("{}", &s[start_index..i]));
                        results.push(item);
                        start_index = i + 1;
                    }
                } else if ch == '[' {
                    count += 1;
                } else if ch == ']' {
                    count -= 1;
                }
            }
            //println!("val: {}", &s[start_index..n-1]);
            let item = Self::deserialize(format!("{}", &s[start_index..n - 1]));
            results.push(item);
            NestedInteger::List(results)
        }
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_385() {
        assert_eq!(Solution::deserialize("324".to_string()), NestedInteger::Int(324));
        assert_eq!(Solution::deserialize("[123,[456,[789]]]".to_string()), NestedInteger::List(vec![
            NestedInteger::Int(123),
            NestedInteger::List(vec![
                NestedInteger::Int(456),
                NestedInteger::List(vec![
                    NestedInteger::Int(789)
                ])
            ])
        ]));
        assert_eq!(Solution::deserialize("[123,456,[788,799,833],[[]],10,[]]".to_string()), NestedInteger::List(vec![
            NestedInteger::Int(123),
            NestedInteger::Int(456),
            NestedInteger::List(vec![
                NestedInteger::Int(788),
                NestedInteger::Int(799),
                NestedInteger::Int(833),
            ]),
            NestedInteger::List(vec![
                NestedInteger::List(vec![]),
            ]),
            NestedInteger::Int(10),
            NestedInteger::List(vec![
            ]),
        ]));

    }
}

// 
```
