---
title: 412. fizz buzz
date: '2022-03-01'
tags: ['leetcode', 'rust', 'easy']
draft: false
description: Solution for leetcode 0412 fizz buzz
---



Given an integer n, return a string array answer (1-indexed) where:



answer[i] <TeX>=</TeX><TeX>=</TeX> "FizzBuzz" if i is divisible by 3 and 5.

answer[i] <TeX>=</TeX><TeX>=</TeX> "Fizz" if i is divisible by 3.

answer[i] <TeX>=</TeX><TeX>=</TeX> "Buzz" if i is divisible by 5.

answer[i] <TeX>=</TeX><TeX>=</TeX> i if non of the above conditions are true.





>   Example 1:
>   Input: n <TeX>=</TeX> 3
>   Output: ["1","2","Fizz"]
>   Example 2:
>   Input: n <TeX>=</TeX> 5
>   Output: ["1","2","Fizz","4","Buzz"]
>   Example 3:
>   Input: n <TeX>=</TeX> 15
>   Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
**Constraints:**
>   	1 <TeX>\leq</TeX> n <TeX>\leq</TeX> 10^4


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn fizz_buzz(n: i32) -> Vec<String> {
(0..n).into_iter().map(|x|
if (x + 1) % 3 == 0 && (x + 1) % 5 == 0 {
"FizzBuzz".to_string()
} else if (x + 1) % 3 == 0 {
"Fizz".to_string()
} else if (x + 1) % 5 == 0 {
"Buzz".to_string()
} else {
format!("{}", x + 1)
}
).collect::<Vec<String>>()
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_412() {
assert_eq!(Solution::fizz_buzz(5), vec_string!["1","2","Fizz","4","Buzz"]);
}
}

```
