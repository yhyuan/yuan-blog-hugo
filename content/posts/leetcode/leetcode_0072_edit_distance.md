---
title: 72. edit distance
date: '2021-07-12'
tags: ['leetcode', 'rust', 'hard']
draft: false
description: Solution for leetcode 0072 edit distance
---



Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:



Insert a character

Delete a character

Replace a character





>   Example 1:
>   Input: word1 <TeX>=</TeX> "horse", word2 <TeX>=</TeX> "ros"
>   Output: 3
>   Explanation:
>   horse -> rorse (replace 'h' with 'r')
>   rorse -> rose (remove 'r')
>   rose -> ros (remove 'e')
>   Example 2:
>   Input: word1 <TeX>=</TeX> "intention", word2 <TeX>=</TeX> "execution"
>   Output: 5
>   Explanation:
>   intention -> inention (remove 't')
>   inention -> enention (replace 'i' with 'e')
>   enention -> exention (replace 'n' with 'x')
>   exention -> exection (replace 'n' with 'c')
>   exection -> execution (insert 'u')
**Constraints:**
>   	0 <TeX>\leq</TeX> word1.length, word2.length <TeX>\leq</TeX> 500
>   	word1 and word2 consist of lowercase English letters.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
/*
use std::collections::HashMap;
impl Solution {
pub fn min_distance_helper(chars1: &Vec<char>, index1: usize, chars2: &Vec<char>, index2: usize, hashmap: &mut HashMap<(usize, usize), i32>) -> i32 {
if hashmap.contains_key(&(index1, index2)) {
return hashmap[&(index1, index2)];
}
if chars1.len() == index1 {
let result = (chars2.len() - index2) as i32;
hashmap.insert((index1, index2), result);
return result;
}
if chars2.len() == index2 {
let result = (chars1.len() - index1) as i32;
hashmap.insert((index1, index2), result);
return result;
}
if chars1[index1] == chars2[index2] {
let result = Solution::min_distance_helper(chars1, index1 + 1, chars2, index2 + 1, hashmap);
hashmap.insert((index1, index2), result);
return result;
}
let result_delete = Solution::min_distance_helper(chars1, index1 + 1, chars2, index2, hashmap);
let result_replace = Solution::min_distance_helper(chars1, index1 + 1, chars2, index2 + 1, hashmap);
let result_insert  = Solution::min_distance_helper(chars1, index1, chars2, index2 + 1, hashmap);
let result = i32::min(result_delete, i32::min(result_replace, result_insert)) + 1;
hashmap.insert((index1, index2), result);
return result;
}
pub fn min_distance(word1: String, word2: String) -> i32 {
let chars1: Vec<char> = word1.chars().collect();
let chars2: Vec<char> = word2.chars().collect();
let mut hashmap: HashMap<(usize, usize), i32> = HashMap::new();

Solution::min_distance_helper(&chars1, 0, &chars2, 0, &mut hashmap)
}
}
*/
impl Solution {
pub fn min_distance(word1: String, word2: String) -> i32 {
let chars1 = word1.chars().collect::<Vec<_>>();
let chars2 = word2.chars().collect::<Vec<_>>();
let m = chars1.len();
let n = chars2.len();
let mut dp: Vec<Vec<i32>> = vec![vec![0; n + 1]; m + 1];
for i in 0..=m {
dp[i][0] = i as i32;
}
for j in 0..=n {
dp[0][j] = j as i32;
}
//println!("dp: {:?}", dp);
for i in 1..=m {
for j in 1..=n {
dp[i][j] = if chars1[i - 1] == chars2[j - 1] {
dp[i - 1][j - 1]
} else {
i32::min(dp[i - 1][j], i32::min(dp[i][j - 1], dp[i - 1][j - 1])) + 1
};
}
}
//println!("dp: {:?}", dp);
dp[m][n]
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_72() {
assert_eq!(Solution::min_distance("".to_string(), "a".to_string()), 1);
assert_eq!(Solution::min_distance("horse".to_string(), "ros".to_string()), 3);
assert_eq!(Solution::min_distance("intention".to_string(), "execution".to_string()), 5);
}
}

```
