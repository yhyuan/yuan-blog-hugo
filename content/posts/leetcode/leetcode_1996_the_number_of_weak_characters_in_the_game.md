---
title: 1996. the number of weak characters in the game
date: '2022-09-02'
tags: ['leetcode', 'rust']
draft: false
description: Solution for leetcode 1996 the number of weak characters in the game
---


You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] <TeX>=</TeX> [attacki, defensei] represents the properties of the ith character in the game.



A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.



Return the number of weak characters.







> Example 1:
> Input: properties <TeX>=</TeX> [[5,5],[6,3],[3,6]]
> Output: 0
> Explanation: No character has strictly greater attack and defense than the other.
> Example 2:
> Input: properties <TeX>=</TeX> [[2,2],[3,3]]
> Output: 1
> Explanation: The first character is weak because the second character has a strictly greater attack and defense.
> Example 3:
> Input: properties <TeX>=</TeX> [[1,5],[10,4],[4,3]]
> Output: 1
> Explanation: The third character is weak because the second character has a strictly greater attack and defense.
**Constraints:**
> 2 <TeX>\leq</TeX> properties.length <TeX>\leq</TeX> 105
> properties[i].length <TeX>=</TeX><TeX>=</TeX> 2
> 1 <TeX>\leq</TeX> attacki, defensei <TeX>\leq</TeX> 105


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
// use std::collections::HashMap;
impl Solution {
pub fn number_of_weak_characters(properties: Vec<Vec<i32>>) -> i32 {
let n = properties.len();
let mut points: Vec<(i32, i32)> = vec![];
for i in 0..n {
let attack = properties[i][0];
let defense = properties[i][1];
points.push((attack, -defense));
}
points.sort();
let mut weak_characters = 0i32;
let mut max_defense = 0;
for i in (0..n).rev() {
if -points[i].1 < max_defense {
weak_characters += 1;
}
max_defense = i32::max(max_defense, -points[i].1);
}
weak_characters
}
}
// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1996() {
assert_eq!(Solution::number_of_weak_characters(vec![vec![7,7],vec![1,2],vec![9,7],vec![7,3],vec![3,10],vec![9,8],vec![8,10],vec![4,3],vec![1,5],vec![1,5]]), 6);
/*
assert_eq!(Solution::number_of_weak_characters(vec![vec![1,1],vec![2,1],vec![2,2],vec![1,2]]), 1);
assert_eq!(Solution::number_of_weak_characters(vec![vec![5,5],vec![6,3],vec![3,6]]), 0);
assert_eq!(Solution::number_of_weak_characters(vec![vec![2,2],vec![3,3]]), 1);
assert_eq!(Solution::number_of_weak_characters(vec![vec![1,5],vec![10,4],vec![4,3]]), 1);
*/
}
}

```
