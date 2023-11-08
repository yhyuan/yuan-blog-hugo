---
title: 390. elimination game
date: '2022-02-14'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0390 elimination game
---



You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:



Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.

Keep repeating the steps again, alternating left to right and right to left, until a single number remains.



Given the integer n, return the last number that remains in arr.



>   Example 1:
>   Input: n <TeX>=</TeX> 9
>   Output: 6
>   Explanation:
>   arr <TeX>=</TeX> [<u>1</u>, 2, <u>3</u>, 4, <u>5</u>, 6, <u>7</u>, 8, <u>9</u>]
>   arr <TeX>=</TeX> [2, <u>4</u>, 6, <u>8</u>]
>   arr <TeX>=</TeX> [<u>2</u>, 6]
>   arr <TeX>=</TeX> [6]
>   Example 2:
>   Input: n <TeX>=</TeX> 1
>   Output: 1
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^9


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn last_remaining(n: i32) -> i32 {
if n == 1 {
return 1;
}
if n == 2 || n == 3 || n == 4 || n == 5 {
return 2;
}
if  (n / 2 - 1) % 2 == 0 {
Self::last_remaining((n / 2 - 1) / 2) * 4
} else {
Self::last_remaining(n / 4) * 4 - 2
}
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_390() {
assert_eq!(Solution::last_remaining(9), 6);
assert_eq!(Solution::last_remaining(1), 1);
}
}

```
