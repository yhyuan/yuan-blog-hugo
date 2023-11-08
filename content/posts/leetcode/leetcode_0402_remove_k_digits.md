---
title: 402. remove k digits
date: '2022-02-25'
tags: ['leetcode', 'rust', 'python', 'medium']
draft: false
description: Solution for leetcode 0402 remove k digits
---



Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.



>   Example 1:
>   Input: num <TeX>=</TeX> "1432219", k <TeX>=</TeX> 3
>   Output: "1219"
>   Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
>   Example 2:
>   Input: num <TeX>=</TeX> "10200", k <TeX>=</TeX> 1
>   Output: "200"
>   Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
>   Example 3:
>   Input: num <TeX>=</TeX> "10", k <TeX>=</TeX> 2
>   Output: "0"
>   Explanation: Remove all the digits from the number and it is left with nothing which is 0.
**Constraints:**
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> num.length <TeX>\leq</TeX> 10^5
>   	num consists of only digits.
>   	num does not have any leading zeros except for the zero itself.


## Solution


### Python
```rust
class Solution:
def removeKdigits(self, num: str, k: int) -> str:


# build a monotonic increasing stack from


# beginning. will end when we pop out k


#digits.
if len(num) == k:
return "0"
stack = []


# count = 0
def processResult(res):
return str(int(res))

for i in range(len(num)):
while len(stack) > 0 and stack[-1] > num[i]:
stack.pop()
k -= 1
if k == 0:
res = "".join(stack)+num[i: ]
return str(int(res))
stack.append(num[i])
if k > 0:
for i in range(k):
stack.pop()
return str(int(res))
```


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn remove_kdigits(num: String, k: i32) -> String {
if k == 0 {
return num;
}
if num.len() == 1 {
return "0".to_string();
}
let chars: Vec<char> = num.chars().collect();
let n = chars.len();
let mut i = 0;
while i < n - 1 && chars[i] <= chars[i + 1] {
i += 1;
}
//println!("i: {}", i);
if i == 0 {
let mut j = 1;
while chars[j] == '0' {
j += 1;
if j >= n {
break;
}
}
if j == n {
return "0".to_string();
}
let new_num = format!("{}", &num[j..n]);
return Self::remove_kdigits(new_num, k - 1);
}
if i == n - 1 {
let new_num = format!("{}", &num[0..n - 1]);
return Self::remove_kdigits(new_num, k - 1);
}
let new_num = format!("{}{}", &num[0..i], &num[i + 1..n]);
return Self::remove_kdigits(new_num, k - 1);
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_402() {
//assert_eq!(Solution::remove_kdigits("1432219".to_string(), 3), "1219".to_string());
//assert_eq!(Solution::remove_kdigits("10200".to_string(), 1), "200".to_string());
//assert_eq!(Solution::remove_kdigits("10".to_string(), 2), "0".to_string());
assert_eq!(Solution::remove_kdigits("112".to_string(), 1), "11".to_string());
}
}

```
