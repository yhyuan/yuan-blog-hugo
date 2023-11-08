---
title: 539. minimum time difference
date: '2022-03-29'
tags: ['leetcode', 'rust', 'medium']
draft: false
description: Solution for leetcode 0539 minimum time difference
---



Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.



>   Example 1:
>   Input: timePoints <TeX>=</TeX> ["23:59","00:00"]
>   Output: 1
>   Example 2:
>   Input: timePoints <TeX>=</TeX> ["00:00","23:59","00:00"]
>   Output: 0
**Constraints:**
>   	2 <TeX>\leq</TeX> timePoints <TeX>\leq</TeX> 2  10^4
>   	timePoints[i] is in the format "HH:MM".


## Solution


### Rust
```rust
pub struct Solution {}


// submission codes start here

impl Solution {
pub fn calculate_difference(time1: &String, time2: &String) -> i32 {
let items1 = time1.split(":").collect::<Vec<_>>();
let hour1 = items1[0].parse::<i32>().unwrap();
let minute1 = items1[1].parse::<i32>().unwrap();
let start_time = hour1 * 60 + minute1;
let items2 = time2.split(":").collect::<Vec<_>>();
let hour2 = items2[0].parse::<i32>().unwrap();
let minute2 = items2[1].parse::<i32>().unwrap();
let end_time = hour2 * 60 + minute2;

return i32::min(end_time - start_time, start_time + 24 * 60 - end_time);
}
pub fn find_min_difference(time_points: Vec<String>) -> i32 {
let n = time_points.len();
let mut min_diff = i32::MAX;
for i in 0..n {
for j in i + 1..n {
if &time_points[j] == &time_points[i] {
return 0;
}
let diff = if &time_points[i] < &time_points[j] {
Self::calculate_difference(&time_points[i], &time_points[j])
} else {
Self::calculate_difference(&time_points[j], &time_points[i])
};
min_diff = i32::min(min_diff, diff);
}
}
min_diff
}
}

// submission codes end



#[cfg(test)]
mod tests {
use super::*;



#[test]
fn test_539() {
assert_eq!(Solution::find_min_difference(vec_string!["23:59","00:00"]), 1);
assert_eq!(Solution::find_min_difference(vec_string!["00:00","23:59","00:00"]), 0);
}
}

```
