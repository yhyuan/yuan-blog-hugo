---
title: 115. distinct subsequences
date: '2021-08-24'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0115 distinct subsequences
---



Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.



>   Example 1:
>   Input: s <TeX>=</TeX> "rabbbit", t <TeX>=</TeX> "rabbit"
>   Output: 3
>   Explanation:
>   As shown below, there are 3 ways you can generate "rabbit" from S.
>   <u>rabb</u>b<u>it</u>
>   <u>ra</u>b<u>bbit</u>
>   <u>rab</u>b<u>bit</u>
>   Example 2:
>   Input: s <TeX>=</TeX> "babgbag", t <TeX>=</TeX> "bag"
>   Output: 5
>   Explanation:
>   As shown below, there are 5 ways you can generate "bag" from S.
>   <u>ba</u>b<u>g</u>bag
>   <u>ba</u>bgba<u>g</u>
>   <u>b</u>abgb<u>ag</u>
>   ba<u>b</u>gb<u>ag</u>
>   babg<u>bag</u>
**Constraints:**
>   	1 <TeX>\leq</TeX> s.length, t.length <TeX>\leq</TeX> 1000
>   	s and t consist of English letters.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
pub fn num_distinct_helper(s_chars: &Vec<char>, s_index: usize, t_chars: &Vec<char>, t_index: usize, hashmap: &mut HashMap<(usize, usize), i32>) -> i32 {
if t_chars.len() == t_index {
hashmap.insert((s_index, t_index), 1);
return 1;
}
if s_chars.len() == s_index {
hashmap.insert((s_index, t_index), 0);
return 0;
}
if hashmap.contains_key(&(s_index, t_index)) {
return hashmap[&(s_index, t_index)];
}
let result = if s_chars[s_index] == t_chars[t_index] {
Solution::num_distinct_helper(s_chars, s_index + 1, t_chars, t_index + 1, hashmap)
+ Solution::num_distinct_helper(s_chars, s_index + 1, t_chars, t_index, hashmap)
} else {
Solution::num_distinct_helper(s_chars, s_index + 1, t_chars, t_index, hashmap)
};
hashmap.insert((s_index, t_index), result);
result
}
pub fn num_distinct(s: String, t: String) -> i32 {
let s_chars: Vec<char> = s.chars().collect();
let t_chars: Vec<char> = t.chars().collect();
let mut hashmap: HashMap<(usize, usize), i32> = HashMap::new();
Solution::num_distinct_helper(&s_chars, 0, &t_chars, 0, &mut hashmap)
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_115() {
assert_eq!(
Solution::num_distinct("babgbag".to_owned(), "bag".to_owned()),
5
);
assert_eq!(
Solution::num_distinct("aaaaaaaaaaaaaaaaaaaa".to_owned(), "aaaaaaaaaa".to_owned()),
184756
);
}
}

```
