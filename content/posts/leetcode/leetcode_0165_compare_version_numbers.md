---
title: 165. compare version numbers
date: '2021-09-30'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0165 compare version numbers
---



Given two version numbers, version1 and version2, compare them.





Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:



If version1 < version2, return -1.

If version1 > version2, return 1.

Otherwise, return 0.





>   Example 1:
>   Input: version1 <TeX>=</TeX> "1.01", version2 <TeX>=</TeX> "1.001"
>   Output: 0
>   Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
>   Example 2:
>   Input: version1 <TeX>=</TeX> "1.0", version2 <TeX>=</TeX> "1.0.0"
>   Output: 0
>   Explanation: version1 does not specify revision 2, which means it is treated as "0".
>   Example 3:
>   Input: version1 <TeX>=</TeX> "0.1", version2 <TeX>=</TeX> "1.1"
>   Output: -1
>   Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
>   Example 4:
>   Input: version1 <TeX>=</TeX> "1.0.1", version2 <TeX>=</TeX> "1"
>   Output: 1
>   Example 5:
>   Input: version1 <TeX>=</TeX> "7.5.2.4", version2 <TeX>=</TeX> "7.5.3"
>   Output: -1
**Constraints:**
>   	1 <TeX>\leq</TeX> version1.length, version2.length <TeX>\leq</TeX> 500
>   	version1 and version2 only contain digits and '.'.
>   	version1 and version2 are valid version numbers.
>   	All the given revisions in version1 and version2 can be stored in a 32-bit integer.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn compare_version(version1: String, version2: String) -> i32 {
let mut items1 = version1
.split(".")
.map(|x| x.parse::<i32>().unwrap())
.collect::<Vec<i32>>();
let mut items2 = version2
.split(".")
.map(|x| x.parse::<i32>().unwrap())
.collect::<Vec<i32>>();
let max_len = usize::max(items1.len(), items2.len());
while items1.len() < max_len {
items1.push(0i32);
}
while items2.len() < max_len {
items2.push(0i32);
}
for i in 0..max_len {
if items1[i] < items2[i] {
return -1;
}
if items2[i] < items1[i] {
return 1;
}
}
0
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_165() {
assert_eq!(
Solution::compare_version("0.1".to_owned(), "1.1".to_owned()),
-1
);
assert_eq!(
Solution::compare_version("1.0.1".to_owned(), "1".to_owned()),
1
);
assert_eq!(
Solution::compare_version("7.5.2.4".to_owned(), "7.5.3".to_owned()),
-1
);
assert_eq!(
Solution::compare_version("1.01".to_owned(), "1.0001".to_owned()),
0
);
}
}

```
