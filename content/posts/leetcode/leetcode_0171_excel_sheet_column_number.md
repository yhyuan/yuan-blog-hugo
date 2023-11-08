---
title: 171. excel sheet column number
date: '2021-10-05'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0171 excel sheet column number
---



Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:



A -> 1

B -> 2

C -> 3

...

Z -> 26

AA -> 27

AB -> 28

...





>   Example 1:
>   Input: columnTitle <TeX>=</TeX> "A"
>   Output: 1
>   Example 2:
>   Input: columnTitle <TeX>=</TeX> "AB"
>   Output: 28
>   Example 3:
>   Input: columnTitle <TeX>=</TeX> "ZY"
>   Output: 701
>   Example 4:
>   Input: columnTitle <TeX>=</TeX> "FXSHRXW"
>   Output: 2147483647
**Constraints:**
>   	1 <TeX>\leq</TeX> columnTitle.length <TeX>\leq</TeX> 7
>   	columnTitle consists only of uppercase English letters.
>   	columnTitle is in the range ["A", "FXSHRXW"].


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn title_to_number(column_title: String) -> i32 {
let chars: Vec<char> = column_title.chars().collect();
let mut mul = 1i128;
let mut result = 0i128;
let a_value = 'A' as i128;
for &ch in chars.iter().rev() {
result += mul * (ch as i128 - a_value + 1);
mul *= 26;
}
result as i32
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_171() {
assert_eq!(Solution::title_to_number("A".to_string()), 1);
assert_eq!(Solution::title_to_number("AB".to_string()), 28);
assert_eq!(Solution::title_to_number("ZY".to_string()), 701);
assert_eq!(Solution::title_to_number("FXSHRXW".to_string()), 2147483647);
}
}

```
