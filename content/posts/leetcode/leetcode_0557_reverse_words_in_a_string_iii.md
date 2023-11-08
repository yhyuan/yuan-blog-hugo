---
title: 557. reverse words in a string iii
date: '2022-04-02'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0557 reverse words in a string iii
---
import LeetCode from "@/components/LeetCode";
import TeX from '@matejmazur/react-katex';

<LeetCode.ProblemCard id={557}/>
 

  Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

   

 >   Example 1:

 >   Input: s <TeX>=</TeX> "Let's take LeetCode contest"

 >   Output: "s'teL ekat edoCteeL tsetnoc"

 >   Example 2:

 >   Input: s <TeX>=</TeX> "God Ding"

 >   Output: "doG gniD"

   

  **Constraints:**

  

 >   	1 <TeX>\leq</TeX> s.length <TeX>\leq</TeX> 5  10^4

 >   	s contains printable ASCII characters.

 >   	s does not contain any leading or trailing spaces.

 >   	There is at least one word in s.

 >   	All the words in s are separated by a single space.


## Solution
### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
    pub fn reverse_words(s: String) -> String {
        let items: Vec<String> = s.split(' ').map(|s| s.chars().rev().collect::<String>()).collect::<Vec<_>>();
        //println!("{:?}", items.join(" "));
        items.join(" ")
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_557() {
    }
}

```
