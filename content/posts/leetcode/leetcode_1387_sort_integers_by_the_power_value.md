---
title: 1387. sort integers by the power value
date: '2022-08-05'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 1387 sort integers by the power value
---



The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:





if x is even then x <TeX>=</TeX> x / 2

if x is odd then x <TeX>=</TeX> 3  x + 1





For example, the power of x <TeX>=</TeX> 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).



Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.



Return the k-th integer in the range [lo, hi] sorted by the power value.



Notice that for any integer x (lo <TeX>\leq</TeX> x <TeX>\leq</TeX> hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in 32 bit signed integer.





>   Example 1:
>   Input: lo <TeX>=</TeX> 12, hi <TeX>=</TeX> 15, k <TeX>=</TeX> 2
>   Output: 13
>   Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
>   The power of 13 is 9
>   The power of 14 is 17
>   The power of 15 is 17
>   The interval sorted by the power value [12,13,14,15]. For k <TeX>=</TeX> 2 answer is the second element which is 13.
>   Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.
>   Example 2:
>   Input: lo <TeX>=</TeX> 1, hi <TeX>=</TeX> 1, k <TeX>=</TeX> 1
>   Output: 1
>   Example 3:
>   Input: lo <TeX>=</TeX> 7, hi <TeX>=</TeX> 11, k <TeX>=</TeX> 4
>   Output: 7
>   Explanation: The power array corresponding to the interval [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
>   The interval sorted by power is [8, 10, 11, 7, 9].
>   The fourth number in the sorted array is 7.
>   Example 4:
>   Input: lo <TeX>=</TeX> 10, hi <TeX>=</TeX> 20, k <TeX>=</TeX> 5
>   Output: 13
>   Example 5:
>   Input: lo <TeX>=</TeX> 1, hi <TeX>=</TeX> 1000, k <TeX>=</TeX> 777
>   Output: 570
**Constraints:**
>   	1 <TeX>\leq</TeX> lo <TeX>\leq</TeX> hi <TeX>\leq</TeX> 1000
>   	1 <TeX>\leq</TeX> k <TeX>\leq</TeX> hi - lo + 1


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here
use std::collections::HashMap;
impl Solution {
pub fn calculate_power(i: i32, memo: &mut HashMap<i32, i32>) -> i32 {
if memo.contains_key(&i) {
return memo[&i];
}
let res = if i % 2 == 0 {
1 + Self::calculate_power(i / 2, memo)
} else {
1 + Self::calculate_power(3 * i + 1, memo)
};
memo.insert(i, res);
res
}
pub fn get_kth(lo: i32, hi: i32, k: i32) -> i32 {
let mut memo: HashMap<i32, i32> = HashMap::new();
memo.insert(1, 0);
let mut power_values: Vec<(i32, i32)> = vec![];
for i in lo..=hi {
let power_value = Self::calculate_power(i, &mut memo);
power_values.push((power_value, i));
}
power_values.sort();
power_values[k as usize - 1].1
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_1387() {
assert_eq!(Solution::get_kth(12, 15, 2), 13);
}
}

```
