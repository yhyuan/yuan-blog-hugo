---
title: 241. different ways to add parentheses
date: '2021-11-26'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0241 different ways to add parentheses
---



Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.



>   Example 1:
>   Input: expression <TeX>=</TeX> "2-1-1"
>   Output: [0,2]
>   Explanation:
>   ((2-1)-1) <TeX>=</TeX> 0
>   (2-(1-1)) <TeX>=</TeX> 2
>   Example 2:
>   Input: expression <TeX>=</TeX> "23-45"
>   Output: [-34,-14,-10,-10,10]
>   Explanation:
>   (2(3-(45))) <TeX>=</TeX> -34
>   ((23)-(45)) <TeX>=</TeX> -14
>   ((2(3-4))5) <TeX>=</TeX> -10
>   (2((3-4)5)) <TeX>=</TeX> -10
>   (((23)-4)5) <TeX>=</TeX> 10
**Constraints:**
>   	1 <TeX>\leq</TeX> expression.length <TeX>\leq</TeX> 20
>   	expression consists of digits and the operator '+', '-', and ''.


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
let n = expression.len();
let chars: Vec<char> = expression.chars().collect();
let opterator_positions: Vec<usize> = (0..n).into_iter().filter(|&i| chars[i] == '+' || chars[i] == '-' || chars[i] == '*').collect();
//println!("opterator_positions: {:?}", opterator_positions);
if opterator_positions.len() == 0 {
return vec![expression.parse::<i32>().unwrap()];
}
let mut results: Vec<i32> = vec![];
for &pos in opterator_positions.iter() {
let expression1: String = (&expression[0..pos]).to_string();
let expression2: String = (&expression[pos + 1..n]).to_string();
let nums1 = Solution::diff_ways_to_compute(expression1);
let nums2 = Solution::diff_ways_to_compute(expression2);
let operator = chars[pos];
for &num1 in nums1.iter() {
for &num2 in nums2.iter() {
let val = match operator {
'+' => {num1 + num2},
'-' => {num1 - num2},
'*' => {num1 * num2},
_ => {panic!("Wrong operator")}
};
results.push(val);
}
}
}
results
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_241() {
assert_eq!(
Solution::diff_ways_to_compute("2*3-4*5".to_owned()),
vec![-34, -10, -14, -10, 10]
);
}
}

```
