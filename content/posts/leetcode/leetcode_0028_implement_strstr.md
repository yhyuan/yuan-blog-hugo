---
title: 28. implement strstr
date: '2021-05-29'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0028 implement strstr
---



Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).



>   Example 1:
>   Input: haystack <TeX>=</TeX> "hello", needle <TeX>=</TeX> "ll"
>   Output: 2
>   Example 2:
>   Input: haystack <TeX>=</TeX> "aaaaa", needle <TeX>=</TeX> "bba"
>   Output: -1
>   Example 3:
>   Input: haystack <TeX>=</TeX> "", needle <TeX>=</TeX> ""
>   Output: 0
**Constraints:**
>   	0 <TeX>\leq</TeX> haystack.length, needle.length <TeX>\leq</TeX> 5  10^4
>   	haystack and needle consist of only lower-case English characters.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn str_str(haystack: String, needle: String) -> i32 {
if needle.len() == 0 {
return 0;
}
haystack.find(&needle).map_or(-1_i32, |v| v as i32)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_28() {
assert_eq!(Solution::str_str("hello".to_string(), "ll".to_string()), 2);
assert_eq!(Solution::str_str("aaaaa".to_string(), "bba".to_string()), -1);
assert_eq!(Solution::str_str("".to_string(), "".to_string()), 0);
}
}

```
