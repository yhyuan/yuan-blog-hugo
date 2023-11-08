---
title: 844. backspace string compare
date: '2022-05-28'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0844 backspace string compare
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={844}/>
 

  Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

  Note that after backspacing an empty text, the text will continue empty.

   

 >   Example 1:

  

 >   Input: s <TeX>=</TeX> "ab#c", t <TeX>=</TeX> "ad#c"

 >   Output: true

 >   Explanation: Both s and t become "ac".

  

 >   Example 2:

  

 >   Input: s <TeX>=</TeX> "ab##", t <TeX>=</TeX> "c#d#"

 >   Output: true

 >   Explanation: Both s and t become "".

  

 >   Example 3:

  

 >   Input: s <TeX>=</TeX> "a##c", t <TeX>=</TeX> "#a#c"

 >   Output: true

 >   Explanation: Both s and t become "c".

  

 >   Example 4:

  

 >   Input: s <TeX>=</TeX> "a#c", t <TeX>=</TeX> "b"

 >   Output: false

 >   Explanation: s becomes "c" while t becomes "b".

  

   

  **Constraints:**

  

 >   	<span>1 <TeX>\leq</TeX> s.length, t.length <TeX>\leq</TeX> 200</span>

 >   	<span>s and t only contain lowercase letters and '#' characters.</span>

  

   

 >   Follow up: Can you solve it in O(n) time and O(1) space?


## Solution
### Python
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(s):
            n = len(s)
            stack = []
            for i in range(n):
                if s[i] == '#':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(s[i])
            return "".join(stack)
        return processString(s) == processString(t)
```
Another solution
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(s):
            n = len(s)
            ignore = 0
            ans = []
            for i in reversed(range(n)):
                if s[i] == '#':
                    ignore += 1
                else:
                    if ignore > 0:
                        ignore -= 1
                    else:
                        ans.append(s[i])
            return "".join(ans)
        return processString(s) == processString(t)
```
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn helper(s: &String) -> String {
        let chars = s.chars().collect::<Vec<_>>();
        let mut stack: Vec<char> = vec![];
        for i in 0..chars.len() {
            if chars[i] == '#' {
                if stack.len() > 0 {
                    stack.pop();
                }
            } else {
                stack.push(chars[i]);
            }
        }
        let s: String = stack.iter().collect::<String>();
        s
    }
    pub fn backspace_compare(s: String, t: String) -> bool {
        let s = Self::helper(&s);
        let t = Self::helper(&t);
        s == t
    }
}
// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_844() {
    }
}

```
