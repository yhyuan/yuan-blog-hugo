---
title: 344. reverse string
date: '2022-01-17'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0344 reverse string
---

 

  Write a function that reverses a string. The input string is given as an array of characters s.

   

 >   Example 1:

 >   Input: s <TeX>=</TeX> ['h','e','l','l','o']

 >   Output: ['o','l','l','e','h']

 >   Example 2:

 >   Input: s <TeX>=</TeX> ['H','a','n','n','a','h']

 >   Output: ['h','a','n','n','a','H']

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 10^5

 >   	s[i] is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

  

   

 >   Follow up: Do not allocate extra space for another array. You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with O(1) extra memory.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        // s.reverse();
        let mut start = 0;
        let mut end = s.len() - 1;
        while start < end {
            s.swap(start, end);
            start += 1;
            end -= 1;
        }    
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_344() {
        let mut chars: Vec<char> = vec!['h','e','l','l','o'];
        Solution::reverse_string(&mut chars);
        assert_eq!(chars, vec!['o','l','l','e','h']);

        let mut chars: Vec<char> = vec!['h','e','l','l','o', 'x'];
        Solution::reverse_string(&mut chars);
        assert_eq!(chars, vec!['x', 'o','l','l','e','h']);

    }
}

```
