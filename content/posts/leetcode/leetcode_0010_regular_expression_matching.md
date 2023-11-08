---
title: 10. regular expression matching
date: '2021-05-11'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0010 regular expression matching
---

 

  Given an input string s and a pattern p, implement regular expression matching with support for '.' and '' where:

  

  	'.' Matches any single character.​​​​

  	'' Matches zero or more of the preceding element.

  

  The matching should cover the entire input string (not partial).

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "aa", p <TeX>=</TeX> "a"

 >   Output: false

 >   Explanation: "a" does not match the entire string "aa".

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "aa", p <TeX>=</TeX> "a"

 >   Output: true

 >   Explanation: '' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "ab", p <TeX>=</TeX> "."

 >   Output: true

 >   Explanation: "." means "zero or more () of any character (.)".

  

 >   Example 4:

  

 >   Input: s <TeX>=</TeX> "aab", p <TeX>=</TeX> "cab"

 >   Output: true

 >   Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

  

 >   Example 5:

  

 >   Input: s <TeX>=</TeX> "mississippi", p <TeX>=</TeX> "misisp."

 >   Output: false

  

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 20

 >   	1 <TeX>\leq</TeX> p.length <TeX>\leq</TeX> 30

 >   	s contains only lowercase English letters.

 >   	p contains only lowercase English letters, '.', and ''.

 >   	It is guaranteed for each appearance of the character '', there will be a previous valid character to match.


## Solution
dp[i][j] represent whether s[0:i + 1] can be match with p[0: j + 1].  

if p[j] is a *, we may consume it or ignore it. If we ignore it, the problem turn into s[0:i + 1] and p[0: j - 2 + 1]. If we can consume it, the problem turn into s[0: i] and p[0: j + 1].

if p[j] is a ., we can turn the problem to s[0: i] and p[0: j].

if p[j] is a letter, we can turn the problem to s[0: i] and p[0: j] if we can match the letter.

### Python
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        memo = {}
        def helper(i, j):
            if i == -1 and j == -1:
                return True
            if i < 0 and j >= 0:
                if p[j] == "*":
                    return helper(i, j - 2)
                return False
            if i >=0 and j < 0:
                return False
            if (i, j) in memo:
                return memo[(i, j)]
            n = len(s)
            m = len(p)
            
            if p[j] == "*":
                memo[(i, j)] = helper(i, j - 2) or (s[i] == p[j - 1] and helper(i - 1, j)) or (p[j - 1] == "." and helper(i - 1, j))
                return memo[(i, j)]
            if p[j] == '.' or p[j] == s[i]:
                memo[(i, j)] = helper(i - 1, j - 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return False
        
        res = helper(n - 1, m - 1)
        return res
```
### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
#[derive(PartialEq, Clone, Copy)]
enum State {
    Success,
    Failure,
}
struct StateMachine { 
    pattern: Vec<char>,
    p_index: usize,
    state: State,
}

impl StateMachine {
    fn new(pattern: Vec<char>) -> Self {
        let star_indices: Vec<usize> = (0..pattern.len()).into_iter().filter(|&i| pattern[i] == '*').collect();
        let pre_star_indices: Vec<usize> = star_indices.iter().map(|&i| i - 1).collect();
        //let mut intervals: Vec<(usize, usize)> = vec![];
        let mut remove_indices: Vec<usize> = vec![];
        for k in 0..star_indices.len() {
            let pre_star_char = pattern[pre_star_indices[k]];
            let pre_star_index = pre_star_indices[k];
            if pre_star_index > 0 {
                let mut index = (pre_star_index - 1) as i32;
                while index >= 0 && pattern[index as usize] == pre_star_char {
                    remove_indices.push(index as usize);
                    index -= 1;
                }
                index -= 1;
            }
            if star_indices[k] < pattern.len() - 1 {
                let mut index = (star_indices[k] + 1) as i32;
                while index < pattern.len() as i32 && pattern[index as usize] == pre_star_char {
                    remove_indices.push(index as usize);
                    index += 1;
                }
            }
        }
        let pattern: Vec<char> = (0..pattern.len()).into_iter()
            .filter(|&i| !remove_indices.contains(&i))
            .map(|i| pattern[i])
            .collect();
        //println!("new pattern: {:?}", pattern);
        StateMachine {
            pattern: pattern,
            p_index: 0usize,
            state: State::Success
        }
    }
    fn parse (&mut self, cur_char: char) -> State {
        if self.state == State::Failure {
            return State::Failure;
        }
        if self.p_index == self.pattern.len() {
            self.state = State::Failure;
            return State::Failure;
        }
        let cur_pattern_char = self.pattern[self.p_index];
        let next_pattern_char: Option<char> = if self.p_index + 1 < self.pattern.len() {
            Some(self.pattern[self.p_index + 1])
        } else {
            None
        };
        //println!("cur_char: {}, p_index: {}, cur_pattern_char: {}, next_pattern_char: {:?}", cur_char, self.p_index, cur_pattern_char, next_pattern_char);
        self.state = match (cur_pattern_char, next_pattern_char) {
            ('.', Some('*')) => {
                State::Success
            },
            ('a'..='z', Some('*')) => {
                if cur_char == cur_pattern_char {
                    State::Success
                } else {
                    self.p_index += 2;
                    self.parse(cur_char)
                }
            },
            ('.', _) => {
                self.p_index += 1;
                State::Success
            },
            ('a'..='z', _) => {
                if cur_pattern_char == cur_char {
                    self.p_index += 1;
                    State::Success
                } else {
                    self.p_index += 1;
                    State::Failure
                }
            },
            _ => {
                panic!("Wrong input!");
            }
        };
        self.state
    }
    fn end(&mut self) {
        //println!("end p_index: {}", self.p_index);
        if self.p_index + 1 < self.pattern.len() && self.pattern[self.p_index + 1] == '*' {
            self.p_index += 2;
        }
        if self.p_index == self.pattern.len() && self.state == State::Success {
            self.state = State::Success;
        } else {
            self.state = State::Failure;
        }
    }
}


impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let pattern: Vec<char> = p.chars().collect();
        let mut state_machine = StateMachine::new(pattern);
        for ch in s.chars() {
            let state = state_machine.parse(ch);
            if state == State::Failure {
                return false;
            }
        }
        state_machine.end();
        state_machine.state != State::Failure
    }
}
*/
/*
impl Solution {
    pub fn is_pre_star(pattern_chars: &Vec<char>, i: usize) -> bool {
        if i == pattern_chars.len() - 1 {
            false
        } else {
            pattern_chars[i + 1] == '*'
        }
    }
    pub fn is_match_helper(chars: &Vec<char>, i: usize, pattern_chars: &Vec<char>, j: usize) -> bool {
        if i == chars.len() {
            if j == pattern_chars.len() {
                return true;
            }
            if j == pattern_chars.len() - 2 && pattern_chars[pattern_chars.len() - 1] == '*' {
                return true;
            }
            return false;
        }
        if i < chars.len() && j == pattern_chars.len() {
            return false;
        }
        let cur_char = chars[i];
        let cur_pattern_char = pattern_chars[j];
        let is_pre_star = Solution::is_pre_star(pattern_chars, j);
        if is_pre_star {
            if cur_pattern_char == '.' {  // .*
                let result_1 = Solution::is_match_helper(chars, i, pattern_chars, j + 2);
                let result_2 = Solution::is_match_helper(chars, i + 1, pattern_chars, j);
                //println!("i: {}, j: {}, result_1: {}, result_2: {}", i, j, result_1, result_2);
                result_1 || result_2
            } else if cur_pattern_char == cur_char { //a*
                let result_1 = Solution::is_match_helper(chars, i + 1, pattern_chars, j); // no pattern is consumed. 
                let result_2 = Solution::is_match_helper(chars, i + 1, pattern_chars, j + 2); // pattern is consumed. 
                let result_3 = Solution::is_match_helper(chars, i, pattern_chars, j + 2); // pattern is consumed. 

                //println!("xx i: {}, j: {}, result_1: {}, result_2: {}", i, j, result_1, result_2);
                result_1 || result_2 || result_3
            } else {
                Solution::is_match_helper(chars, i, pattern_chars, j + 2)
            }
        } else {
            if cur_pattern_char == '.' {
                Solution::is_match_helper(chars, i + 1, pattern_chars, j + 1)
            } else if cur_pattern_char == cur_char {
                Solution::is_match_helper(chars, i + 1, pattern_chars, j + 1)
            } else {
                false
            }
        }
        //true
    }
    pub fn is_match(s: String, p: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        let pattern_chars: Vec<char> = p.chars().collect();
        let mut pattern: Vec<char> = vec![];
        let mut i = 0;
        let mut in_star_mode = false;
        while i < pattern_chars.len() - 1 {
            if pattern_chars[i + 1] == '*' {
                if in_star_mode {
                    if pattern_chars[i] != pattern[pattern.len() - 2] {
                        pattern.push(pattern_chars[i]);
                        pattern.push(pattern_chars[i + 1]);
                    }
                } else {
                    in_star_mode = true;
                    pattern.push(pattern_chars[i]);
                    pattern.push(pattern_chars[i + 1]);
                }
                i = i + 2;
            } else {
                in_star_mode = false;
                pattern.push(pattern_chars[i]);
                i = i + 1;
            }
        }
        if pattern_chars[pattern_chars.len() - 1] != '*' {
            pattern.push(pattern_chars[pattern_chars.len() - 1]);
        }
        Solution::is_match_helper(&chars, 0, &pattern, 0)
    }
}
*/
use std::collections::HashMap;
impl Solution {
    pub fn convert_pattern(p: String) -> Vec<char> {
        let pattern_chars: Vec<char> = p.chars().collect();
        let mut p_chars: Vec<char> = vec![];
        for i in 0..pattern_chars.len() - 1 {
            let ch = pattern_chars[i];
            if ch == '*' {
                continue;
            }
            if pattern_chars[i + 1] == '*' {
                if ch == '.' {
                    p_chars.push('?');
                } else {
                    let mut c = ch.to_uppercase();
                    p_chars.push(c.next().unwrap());
                }
            } else {
                p_chars.push(ch);
            }
        }
        if pattern_chars[pattern_chars.len() - 1] != '*' {
            p_chars.push(pattern_chars[pattern_chars.len() - 1]);
        }
        let mut result: Vec<char> = vec![];
        for i in 0..p_chars.len() {
            let pre_ch = if i == 0 {' '} else {p_chars[i - 1]};
            let ch = p_chars[i];
            if (ch.is_uppercase() || ch == '?') && pre_ch == ch {
                continue;
            }
            result.push(ch);
        }
        result
    }

    pub fn is_match_helper(s_chars: &Vec<char>, s_index: usize, p_chars: &Vec<char>, p_index: usize, hashmap: &mut HashMap<(usize, usize), bool>) -> bool {
        if hashmap.contains_key(&(s_index, p_index)) {
            return hashmap[&(s_index, p_index)];
        }
        if s_chars.len() == s_index && p_chars.len() == p_index {
            hashmap.insert((s_index, p_index), true);
            return true;
        }
        if s_chars.len() == s_index {
            let indices: Vec<usize> = (p_index..p_chars.len()).into_iter().filter(|&i| p_chars[i].is_uppercase() || p_chars[i] == '?').collect();
            let result = indices.len() == p_chars.len() - p_index;
            hashmap.insert((s_index, p_index), result);
            return result;
        }
        if p_chars.len() == p_index {
            hashmap.insert((s_index, p_index), false);
            return false;
        }
        let result: bool = match p_chars[p_index] {
            '?' => {
                let result1 = Solution::is_match_helper(s_chars, s_index, p_chars, p_index + 1, hashmap);
                let result2 = Solution::is_match_helper(s_chars, s_index + 1, p_chars, p_index + 1, hashmap);
                let result3 = Solution::is_match_helper(s_chars, s_index + 1, p_chars, p_index, hashmap);
                result1 || result2 || result3
            },
            'A'..='Z' => {
                let mut c = p_chars[p_index].to_lowercase();
                if s_chars[s_index] == c.next().unwrap() {
                    let result1 = Solution::is_match_helper(s_chars, s_index, p_chars, p_index + 1, hashmap);
                    let result2 = Solution::is_match_helper(s_chars, s_index + 1, p_chars, p_index + 1, hashmap);
                    let result3 = Solution::is_match_helper(s_chars, s_index + 1, p_chars, p_index, hashmap);
                    result1 || result2 || result3
                } else {
                    Solution::is_match_helper(s_chars, s_index, p_chars, p_index + 1, hashmap)
                }
            },
            '.' => {
                Solution::is_match_helper(s_chars, s_index + 1, p_chars, p_index + 1, hashmap)
            },
            'a'..='z' => {
                if s_chars[s_index] == p_chars[p_index] {
                    Solution::is_match_helper(s_chars, s_index + 1, p_chars, p_index + 1, hashmap)
                } else {
                    false
                }
            },
            _ => {
                panic!("wrong input");
            }
        };
        hashmap.insert((s_index, p_index), result);
        result
    }
    pub fn is_match(s: String, p: String) -> bool {
        let s_chars: Vec<char> = s.chars().collect();
        let p_chars = Solution::convert_pattern(p);
        let mut hashmap: HashMap<(usize, usize), bool> = HashMap::new();
        //println!("p_chars: {:?}", p_chars);
        Solution::is_match_helper(&s_chars, 0, &p_chars, 0, &mut hashmap)
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_10() {
        assert_eq!(Solution::is_match("aaa".to_string(), "aaaa".to_string()), false);
        assert_eq!(Solution::is_match("aa".to_string(), "a".to_string()), false);
        assert_eq!(Solution::is_match("aa".to_string(), "a*".to_string()), true);
        assert_eq!(Solution::is_match("ab".to_string(), ".*".to_string()), true);
        assert_eq!(Solution::is_match("aab".to_string(), "c*a*b".to_string()), true);
        //assert_eq!(Solution::is_match("ab".to_string(), ".*".to_string()), false);
        //assert_eq!(Solution::is_match("mississippi".to_string(), "mis*is*p*.".to_string()), false);
        //assert_eq!(Solution::is_match("aaaaaaaaaaaaab".to_string(), "a*a*a*a*a*a*a*a*a*a*a*a*b".to_string()), true);
        assert_eq!(Solution::is_match("mississippi".to_string(), "mis*is*ip*.".to_string()), true);
        assert_eq!(Solution::is_match("aaa".to_string(), "a*a".to_string()), true);
        assert_eq!(Solution::is_match("bbbba".to_string(), ".*a*a".to_string()), true);
        assert_eq!(Solution::is_match("aaaaaaaaaaaaab".to_string(), "a*a*a*a*a*a*a*a*a*a*a*a*b".to_string()), true);
    }
}

```
