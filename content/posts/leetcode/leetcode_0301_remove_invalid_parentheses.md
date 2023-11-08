---
title: 301. remove invalid parentheses
date: '2021-12-27'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0301 remove invalid parentheses
---

 

  Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

  Return all the possible results. You may return the answer in any order.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "()())()"

 >   Output: ["(())()","()()()"]

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "(a)())()"

 >   Output: ["(a())()","(a)()()"]

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> ")("

 >   Output: [""]

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 25

 >   	s consists of lowercase English letters and parentheses '(' and ')'.

 >   	There will be at most 20 parentheses in s.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
use std::collections::VecDeque;
impl Solution {
    #[inline]
    pub fn is_valid_parentheses(s: &String) -> bool {
        //let chars: Vec<char> = s.chars().collect();
        let mut res = 0;
        for ch in s.chars() {
            if ch == '(' {
                res += 1;
            } else if ch == ')' {
                if res == 0 {
                    return false;
                }
                res -= 1;
            }
        }
        res == 0
    }

    pub fn remove_invalid_parentheses_helper(s: String) -> Vec<String> {
        let n = s.len();
        if n <= 0 {
            return vec!["".to_string()];
        }
        //let mut hashmap: HashMap<String, bool> = HashMap::new();
        if Self::is_valid_parentheses(&s) {
            return vec![s.clone()];
        }
        let mut results: HashSet<String> = HashSet::new();
        let mut queue: VecDeque<(String, usize, usize, usize)> = VecDeque::new();
        let chars: Vec<char> = s.chars().collect();
        let left_brackets = chars.iter().filter(|&&ch| ch == '(').count();
        let right_brackets = chars.iter().filter(|&&ch| ch == ')').count();
        queue.push_back((s, 0usize, left_brackets, right_brackets));
        let mut found_layer = usize::MAX;
        while !queue.is_empty() {
            let (s, layer, left_brackets, right_brackets) = queue.pop_front().unwrap();
            let brackets_diff = if left_brackets > right_brackets {left_brackets - right_brackets} else {right_brackets - left_brackets};
            //println!("chars: {:?}", chars);
            let n = s.len();
            if layer > found_layer {
                break;
            }
            for (i, ch) in s.chars().enumerate() {
                if ch != '(' && ch != ')' {
                    continue;
                }
                let new_left_brackets = if ch == '(' {left_brackets - 1} else {left_brackets};
                let new_right_brackets = if ch == ')' {right_brackets - 1} else {right_brackets};
                let new_brackets_diff = if new_left_brackets > new_right_brackets {new_left_brackets - new_right_brackets} else {new_right_brackets - new_left_brackets};
                if brackets_diff!= 0 && new_brackets_diff > brackets_diff {
                    continue;
                }
                //let new_chars: Vec<char> = (0..n).into_iter().filter(|&j| j != i).map(|j| chars[j]).collect();
                //let new_s: String = new_chars.iter().collect();
                let new_s = format!("{}{}", &s[0..i], &s[i + 1..n]);
                if new_left_brackets == new_right_brackets && Self::is_valid_parentheses(&new_s) {
                    found_layer = layer;
                    if !results.contains(&new_s) {
                        results.insert(new_s.clone());
                    }
                }
                queue.push_back((new_s, layer + 1, new_left_brackets, new_right_brackets));
            }    
        }
        let mut v: Vec<String> = results.into_iter().collect();
        //v.sort();
        return v;
    }
    pub fn choose_positions(positions: &Vec<usize>, index: usize, count: usize, nums: &mut Vec<usize>) -> Vec<Vec<usize>> {
        if nums.len() == count {
            return vec![nums.clone()];
        }
        let n = positions.len();
        if index == n {
            return vec![];
        }
        let mut result: Vec<Vec<usize>> = vec![];
        for i in index..n {
            nums.push(positions[i]);
            let res = Self::choose_positions(positions, i + 1, count, nums);
            for v in res {
                result.push(v);
            }
            nums.pop();
        }
        result
    }
    pub fn build_string(group_1: &Vec<usize>, group_2: &Vec<usize>, group_3: &Vec<usize>, chars: &Vec<char>) -> String {
        let mut result: Vec<usize> = vec![];
        for &p in group_1.iter() {
            result.push(p);
        }
        for &p in group_2.iter() {
            result.push(p);
        }
        for &p in group_3.iter() {
            result.push(p);
        }
        result.sort();
        let mut chars: Vec<char> = result.iter().map(|&j| chars[j]).collect();
        Self::remove_invalid_start_end(&mut chars);
        let s = chars.iter().collect::<String>();
        //let s = result.iter().map(|&j| chars[j]).collect::<String>();
        s
    }
    pub fn remove_invalid_start_end(chars: &mut Vec<char>) {
        while chars.len() > 0 && chars[0] == ')' {
            chars.remove(0);
        }
        while chars.len() > 0 && chars[chars.len() - 1] == '(' {
            chars.pop();
        }
    }
    /*
    pub fn find_valid_start_end(chars: &Vec<char>) -> (usize, usize) {
        let mut result = 0;
        let mut start = 0usize;
        for (i, &ch) in chars.iter().enumerate() {
            if ch == '(' {
                result += 1;
            } else if ch == ')' {
                if result == 0 {
                    start = i;
                    break;
                }
                result -= 1;
            }
        }
        result = 0;
        let mut end = chars.len() - 1;
        for (i, &ch) in chars.iter().rev().enumerate() {
            if ch == ')' {
                result += 1;
            } else if ch == '(' {
                if result == 0 {
                    end = i;
                    break;
                }
                result -= 1;
            }
        }
        (start, end)
    }
    */
    pub fn remove_invalid_parentheses(s: String) -> Vec<String> {
        let mut chars: Vec<char> = s.chars().collect();
        Self::remove_invalid_start_end(&mut chars);
        let n = chars.len();
        //let (start, end) = Self::find_valid_start_end(&chars);
        //println!("start: {}, end: {}, s: {:?}", start, chars.len() - end - 1, &chars[start..=n - end - 1]);
        //return vec![];
        let right_bracket_positions: Vec<usize> = (0..n).into_iter().filter(|&i| chars[i] == ')').collect();
        let left_bracket_positions: Vec<usize> = (0..n).into_iter().filter(|&i| chars[i] == '(').collect();
        let none_bracket_positions: Vec<usize> = (0..n).into_iter().filter(|&i| chars[i] != '(' && chars[i] != ')').collect();

        if left_bracket_positions.len() > right_bracket_positions.len() {
            let mut nums: Vec<usize> = vec![];
            let pos_v = Self::choose_positions(&left_bracket_positions, 0, right_bracket_positions.len(), &mut nums);
            let mut max_len = 0usize;
            let mut results: HashSet<String> = HashSet::new();
            for i in 0..pos_v.len() {
                let s = Self::build_string(&right_bracket_positions, &pos_v[i], &none_bracket_positions, &chars);
                let res = Self::remove_invalid_parentheses_helper(s);
                if res.len() > 0 {
                    if res[0].len() > max_len {
                        max_len = res[0].len();
                        results.clear();
                        for s in res {
                            results.insert(s);
                        }
                    } else if res[0].len() == max_len {
                        for s in res {
                            results.insert(s);
                        }
                    }
                }
            }
            let mut results = results.into_iter().collect::<Vec<String>>();
            results.sort();
            return results;
        } else if left_bracket_positions.len() < right_bracket_positions.len() {
            let mut nums: Vec<usize> = vec![];
            let pos_v = Self::choose_positions(&right_bracket_positions, 0, left_bracket_positions.len(), &mut nums);
            let mut max_len = 0usize;
            let mut results: HashSet<String> = HashSet::new();
            for i in 0..pos_v.len() {
                let s = Self::build_string(&left_bracket_positions, &pos_v[i], &none_bracket_positions, &chars);
                let res = Self::remove_invalid_parentheses_helper(s);
                if res.len() > 0 {
                    if res[0].len() > max_len {
                        max_len = res[0].len();
                        results.clear();
                        for s in res {
                            results.insert(s);
                        }
                    } else if res[0].len() == max_len {
                        for s in res {
                            results.insert(s);
                        }
                    }
                }
            }
            let mut results = results.into_iter().collect::<Vec<String>>();
            results.sort();
            return results;
        } 
        let res = Self::remove_invalid_parentheses_helper(s);
        res
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_301() {

        assert_eq!(
            Solution::remove_invalid_parentheses("()())()".to_owned()),
            vec_string!["(())()", "()()()"]
        );
        assert_eq!(
            Solution::remove_invalid_parentheses("(a)())()".to_owned()),
            vec_string!["(a())()", "(a)()()"]
        );
        let empty: Vec<String> = vec!["".to_string()];
        assert_eq!(
            Solution::remove_invalid_parentheses(")(".to_owned()),
            empty
        );
        assert_eq!(
            Solution::remove_invalid_parentheses("n".to_owned()),
            vec_string!["n"]
        );
        assert_eq!(
            Solution::remove_invalid_parentheses("()".to_owned()),
            vec_string!["()"]
        );
        assert_eq!(
            Solution::remove_invalid_parentheses("(j))(".to_owned()),
            vec_string!["(j)"]
        );
        assert_eq!(
            Solution::remove_invalid_parentheses("((()((s((((()".to_owned()),
            vec_string!["(()s)", "()(s)", "()s()"]
        );
        assert_eq!(
            Solution::remove_invalid_parentheses("())((((((((((b))(".to_owned()),
            vec_string!["()((b))"]
        );
        assert_eq!(
            Solution::remove_invalid_parentheses("))y((())()())((((".to_owned()),
            vec_string!["y((())()())"]
        );
        
        /*
        assert_eq!(
            Solution::remove_invalid_parentheses("(())))))()(()()x()(".to_owned()),
            vec_string!["(())()(()()x)", "(())()(())x()", "(())()()()x()"]
        );
        */
        //
    }
}

```
