---
title: 202. happy number
date: '2021-10-19'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0202 happy number
---



Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:



Starting with any positive integer, replace the number by the sum of the squares of its digits.

Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.



Return true if n is a happy number, and false if not.



>   Example 1:
>   Input: n <TeX>=</TeX> 19
>   Output: true
>   Explanation:
>   1^2 + 9^2 <TeX>=</TeX> 82
>   8^2 + 2^2 <TeX>=</TeX> 68
>   6^2 + 8^2 <TeX>=</TeX> 100
>   1^2 + 0^2 + 0^2 <TeX>=</TeX> 1
>   Example 2:
>   Input: n <TeX>=</TeX> 2
>   Output: false
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 2^31 - 1


## Solution


### Python
```python
class Solution:
def isHappy(self, n: int) -> bool:
visited = set([n])
while True:
next_n = 0
while n > 0:
r = n % 10
next_n += r * r
n = n // 10
if next_n == 1:
return True
if next_n in visited:
return False
visited.add(next_n)
n = next_n
```


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashSet;
impl Solution {
pub fn is_happy_helper(n: i32) -> i32 {
let mut n = n;
let mut res = 0;
while n > 9 {
let x = n % 10;
res += x * x;
n = n / 10;
}
res + n * n
}
pub fn is_happy(n: i32) -> bool {
let mut n = n;
let mut hashset: HashSet<i32> = HashSet::new();
hashset.insert(n);
while n != 1 {
let new_n = Solution::is_happy_helper(n);
if hashset.contains(&new_n) {
return false;
}
hashset.insert(new_n);
n = new_n;
}
true
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_202() {
assert_eq!(Solution::is_happy(19), true);
assert_eq!(Solution::is_happy(2), true);
}
}

```
